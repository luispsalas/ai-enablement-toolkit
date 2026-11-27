"""Build the status report and a draft leadership brief from the kit's files.

    python3 tools/build_reports.py examples/trial-n1/diagnosis-sheet.csv \\
        examples/trial-n1/usage-tracker.csv examples/trial-n1 --date 2026-10-10

Reads the diagnosis sheet, the usage tracker and every `feedback-NN.md` page in
the folder given. Writes three files next to the usage tracker (or into --out):
`status-report-<date>.md`, `brief-<date>-draft.md` and `report-snapshot-<date>.json`.
The snapshot is what the next run compares against: the status report's "What
changed" section lists the differences from the latest snapshot dated before
this report in the same folder.

The rules it follows are in adoption-kit/REPORTING.md:
- It first runs check_lists.py on both CSV files and writes nothing if any rule
  fails: a report built on rows that fail the checks is not sent.
- Feedback pages are read strictly against feedback-template.md. A page that
  does not match is named and nothing is written.
- Real and example (synthetic) data never share a file, so inputs that mix
  them are refused.
- A snapshot of real data is never compared with one of example data.
- The brief is a DRAFT: section 3 (decisions) and the evidence-base limit are
  left for a person to write, and the evidence lines should be edited.

Exit code 0 = all three files written, 1 = the CSV checks failed, 2 = an input
could not be read, did not match its template, the tracker has no rows, or an
output already exists.
"""
import argparse, csv, datetime, json, os, re, sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from check_lists import check, OWNERS, NOT_A_STALL  # noqa: E402

PAGE_NAME = re.compile(r"^feedback-(\d+)\.md$")
TITLE = re.compile(r"^\*\*Feedback (\d+) [—-] (.+)\*\*\s*$")
PAGE_STATUS = ["open", "fix planned", "shipped", "checked"]
PRIORITY = ["high", "medium", "low", "not set"]
RESULTS = ["fixed", "partly fixed", "not fixed", "could not check"]
REQUIRED = ["For (fix owner)", "Status", "Priority", "Fix shipped on", "Checked on", "Result"]
CLASS_ORDER = ["tool", "workflow", "training", "habit", "undetermined"]
INTERVIEW_CODE = re.compile(r"\bP\d{2,}\b")
SNAPSHOT_NAME = re.compile(r"^report-snapshot-(\d{4}-\d{2}-\d{2})\.json$")


class InputError(Exception):
    pass


def read_csv(path):
    with open(path, newline="", encoding="utf-8") as f:
        return [{k: (v or "").strip() for k, v in r.items()} for r in csv.DictReader(f)]


def head(value):
    """The value before any explanation: 'dev team (provisional)' -> 'dev team'."""
    return re.split(r"\s*[(:]", value, maxsplit=1)[0].strip()


def read_page(path):
    """Read one feedback page; raise InputError naming what does not match the template."""
    name = os.path.basename(path)
    text = open(path, encoding="utf-8").read()
    title = next((TITLE.match(l) for l in text.splitlines() if TITLE.match(l)), None)
    if not title:
        raise InputError(f"{name}: no title line like '**Feedback 01 — <title>**'")
    fields = {}
    for line in text.splitlines():
        if line.startswith("|"):
            cells = [c.strip() for c in line.strip().strip("|").split("|")]
            if len(cells) >= 2:
                fields.setdefault(cells[0].strip("*").strip(), cells[1])
    missing = [k for k in REQUIRED if k not in fields]
    if missing:
        raise InputError(f"{name}: missing table rows {missing}")
    page = {
        "id": f"feedback-{PAGE_NAME.match(name).group(1)}",
        "title": title.group(2).strip(),
        "owner": head(fields["For (fix owner)"]),
        "status": head(fields["Status"]),
        "priority": head(fields["Priority"]),
        "shipped": head(fields["Fix shipped on"]) or "not yet",
        "checked": head(fields["Checked on"]) or "not yet",
        "result": head(fields["Result"]) or "not checked yet",
    }
    for key, allowed in (("owner", OWNERS), ("status", PAGE_STATUS), ("priority", PRIORITY)):
        if page[key] not in allowed:
            raise InputError(f"{name}: {key} '{page[key]}' is not one of {sorted(allowed)}")
    if page["result"] != "not checked yet" and page["result"] not in RESULTS:
        raise InputError(f"{name}: result '{page['result']}' is not one of {RESULTS}")
    return page


def stall_refs(row):
    """The diagnosis IDs a tracker row names in stall_ref: several are allowed, e.g. "S01 S04"."""
    return row["stall_ref"].split()


def follow_up_date(page, diag, track):
    """A page's follow-up date is the review_date of the tracker rows linked to it."""
    stalls = {r["stall_id"] for r in diag if r["feedback_ref"] == page["id"] + ".md"}
    dates = sorted(r["review_date"] for r in track if stalls & set(stall_refs(r)) and r["review_date"])
    return dates[0] if dates else ""


def evidence(diag, track):
    codes = set()
    for r in diag:
        codes |= set(INTERVIEW_CODE.findall(r["sources"]))
    teams = {r["team"] for r in track}
    sources = sorted({r["source"] for r in track})
    return len(codes), len(teams), sources


def status_report(date, diag, track, pages, example, changed):
    n, teams, sources = evidence(diag, track)
    out = [f"# Status report, {date}", ""]
    if example:
        out += ["*Example data (synthetic), not a real rollout.*", ""]
    out += [f"**Read:** {len(track)} usage tracker row(s), {len(diag)} diagnosis row(s), "
            f"{len(pages)} feedback page(s). Both CSV files passed `check_lists.py`.", "",
            f"**Evidence base:** {n} interviewed, {teams} team(s), sources: {', '.join(sources) or 'none'}.",
            "", "## Adoption by team and tool", "",
            "| Team | Tool | Status | Regular users | Source | Review date |", "|---|---|---|---|---|---|"]
    for r in track:
        out.append(f"| {r['team']} | {r['tool']} | {r['status']} | {r['users_regular']} of "
                   f"{r['users_with_access']} | {r['source']} | {r['review_date'] or 'not set'} |")
    out += ["", "## Stalls by class", ""]
    for c in CLASS_ORDER:
        rows = [r for r in diag if r["class_primary"] == c]
        listed = "; ".join(f"`{r['stall_id']}` {r['team']} · {r['tool']}" for r in rows) or "none"
        out.append(f"- **{c}** ({len(rows)}): {listed}")
    not_stalls = [r["stall_id"] for r in diag if r["class_primary"] == NOT_A_STALL]
    if not_stalls:
        out.append(f"- *Not a stall* ({len(not_stalls)}): {', '.join(f'`{s}`' for s in not_stalls)}")
    out += ["", "## Open feedback pages by priority", ""]
    open_pages = sorted((p for p in pages if p["status"] != "checked"),
                        key=lambda p: (PRIORITY.index(p["priority"]), p["id"]))
    if open_pages:
        out += ["| Page | Issue | Priority | Owner | Status | Follow-up date |", "|---|---|---|---|---|---|"]
        for p in open_pages:
            out.append(f"| `{p['id']}` | {p['title']} | {p['priority']} | {p['owner']} | "
                       f"{p['status']} | {p['follow_up'] or 'not set'} |")
    else:
        out.append("None.")
    out += ["", "## Overdue follow-ups", "", *overdue_lines(date, track, open_pages),
            "", "## What changed since the last report", "", *changed, ""]
    return "\n".join(out)


def keyed(rows, key):
    """Rows by a readable key; a repeated key gets ' #2', ' #3' so no row is lost."""
    out = {}
    for r in rows:
        k, n = key(r), 2
        while k in out:
            k, n = f"{key(r)} #{n}", n + 1
        out[k] = r
    return out


def snapshot(date, diag, track, pages, example):
    """The figures the next report compares against."""
    return {
        "date": date,
        "synthetic": example,
        "tracker": {k: {"status": r["status"], "users_regular": r["users_regular"],
                        "users_with_access": r["users_with_access"]}
                    for k, r in keyed(track, lambda r: f"{r['team']} · {r['tool']}").items()},
        "stalls": {k: {"class": r["class_primary"], "class_secondary": r["class_secondary"]}
                   for k, r in keyed(diag, lambda r: r["stall_id"]).items()},
        "pages": {p["id"]: {"status": p["status"], "priority": p["priority"], "result": p["result"]}
                  for p in pages},
    }


def previous_snapshot(folder, date):
    """The latest snapshot in the folder dated before this report, or None."""
    try:
        names = os.listdir(folder)
    except OSError:
        return None, None
    dated = sorted((m.group(1), n) for n in names if (m := SNAPSHOT_NAME.match(n)) and m.group(1) < date)
    if not dated:
        return None, None
    name = dated[-1][1]
    with open(os.path.join(folder, name), encoding="utf-8") as f:
        return json.load(f), name


def what_changed(prev, name, cur):
    """Lines for the status report's 'What changed' section."""
    if prev is None:
        return ["*No earlier snapshot in this folder, so there is nothing to compare with. "
                "Write this section by hand, or leave it for the next report.*"]
    if prev.get("synthetic") != cur["synthetic"]:
        return [f"*Not compared: `{name}` holds {'example' if prev.get('synthetic') else 'real'} data "
                f"and this report holds {'example' if cur['synthetic'] else 'real'} data.*"]
    lines = []
    users = lambda r: f"{r['users_regular']} of {r['users_with_access']}"
    old, new = prev.get("tracker", {}), cur["tracker"]
    for k in new:
        if k not in old:
            lines.append(f"- Tracker: new row {k} (status {new[k]['status']}, regular users {users(new[k])}).")
            continue
        if old[k]["status"] != new[k]["status"]:
            lines.append(f"- Tracker: {k}, status {old[k]['status']} → {new[k]['status']}.")
        if users(old[k]) != users(new[k]):
            lines.append(f"- Tracker: {k}, regular users {users(old[k])} → {users(new[k])}.")
    lines += [f"- Tracker: row removed, {k}." for k in old if k not in new]
    old, new = prev.get("stalls", {}), cur["stalls"]
    cls = lambda r: r["class"] + (f", with {r['class_secondary']} second" if r["class_secondary"] else "")
    for k in new:
        if k not in old:
            lines.append(f"- Diagnosis: new row `{k}` ({cls(new[k])}).")
        elif cls(old[k]) != cls(new[k]):
            lines.append(f"- Diagnosis: `{k}`, class {cls(old[k])} → {cls(new[k])}.")
    lines += [f"- Diagnosis: row removed, `{k}`." for k in old if k not in new]
    old, new = prev.get("pages", {}), cur["pages"]
    for k in new:
        if k not in old:
            lines.append(f"- Feedback: new page `{k}` (priority {new[k]['priority']}, status {new[k]['status']}).")
            continue
        for field in ("status", "priority", "result"):
            if old[k][field] != new[k][field]:
                lines.append(f"- Feedback: `{k}`, {field} {old[k][field]} → {new[k][field]}.")
    lines += [f"- Feedback: page removed, `{k}`." for k in old if k not in new]
    intro = f"*Compared with `{name}`, the snapshot of the report of {prev.get('date', 'unknown date')}.*"
    return [intro, ""] + (lines or ["No changes in the tracker, the diagnosis sheet or the feedback pages."])


def overdue_lines(date, track, open_pages):
    lines = [f"- Tracker: {r['team']} · {r['tool']}, review date {r['review_date']}"
             for r in track if r["review_date"] and r["review_date"] < date]
    lines += [f"- `{p['id']}`, follow-up date {p['follow_up']}"
              for p in open_pages if p["follow_up"] and p["follow_up"] < date]
    return lines or ["None."]


def brief(date, diag, track, pages, example):
    n, teams, sources = evidence(diag, track)
    by_stall = {r["stall_id"]: r for r in diag}
    out = [f"# AI adoption brief, period ending {date} (draft)", "",
           "*Draft built by `tools/build_reports.py`. Write section 3 and the limit sentence, edit the "
           "evidence lines, then save as `brief-<date>.md`.*", ""]
    if example:
        out += ["*Example data (synthetic), not a real rollout.*", ""]
    out += [f"**Evidence base:** {n} interview(s), {teams} team(s), sources: {', '.join(sources) or 'none'}. "
            f"**n = {n}.** *TO WRITE: one sentence on any limit the reader must know first.*",
            "", "## 1. What is working", ""]
    working = [r for r in track if r["status"] == "regular"]
    out += [f"- {r['tool']}, on {r['team']}: {r['users_regular']} of {r['users_with_access']} "
            f"use it regularly ({r['source']})." for r in working] or ["Nothing this period."]
    out += ["", "## 2. What stalled, and why", "",
            "| Team · tool | Status | Class | Evidence (one line) | Diagnosis row |", "|---|---|---|---|---|"]
    stalled = [r for r in track if r["status"] in {"stalled", "dropped", "not started"} or r["stall_ref"]]
    for r in stalled:
        # One line per linked diagnosis row, in the order stall_ref lists them.
        for sid in stall_refs(r) or [None]:
            d = by_stall.get(sid, {})
            cls = d.get("class_primary", r["stall_class"] or "not diagnosed")
            if d.get("class_secondary"):
                cls += f", with {d['class_secondary']} second"
            ref = f"`{sid}`" if sid else "none yet"
            out.append(f"| {r['team']} · {r['tool']} | {r['status']} | {cls} | "
                       f"{d.get('observation', 'TO WRITE')} | {ref} |")
    if not stalled:
        out.append("| nothing this period | | | | |")
    out += ["", "## 3. Decisions needed", "",
            "*TO WRITE by hand: at most three, each a question the reader can answer "
            "(decision · options · recommended, because · by date).*",
            "", "## 4. Fixes shipped, and whether they landed", ""]
    if pages:
        out += ["| Fix | Shipped | Checked | Result |", "|---|---|---|---|"]
        out += [f"| `{p['id']}` | {p['shipped']} | {p['checked']} | {p['result']} |" for p in pages]
    else:
        out.append("Nothing this period.")
    future = sorted(r["review_date"] for r in track if r["review_date"] and r["review_date"] >= date)
    overdue = [l.lstrip("- ") for l in overdue_lines(date, track,
               [p for p in pages if p["status"] != "checked"]) if l != "None."]
    out += ["", "## 5. Next review", "",
            (future[0] + "." if future else "*TO WRITE: no future review date in the tracker; give a date or the event it waits on.*")
            + f" Overdue items: {'; '.join(overdue) if overdue else 'none'}.", ""]
    return "\n".join(out)


def main(argv):
    ap = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    ap.add_argument("diagnosis")
    ap.add_argument("tracker")
    ap.add_argument("feedback_dir")
    ap.add_argument("--date", default=datetime.date.today().isoformat(), help="report date, YYYY-MM-DD")
    ap.add_argument("--out", help="output folder, created if missing (default: the usage tracker's folder)")
    a = ap.parse_args(argv)
    if not re.match(r"^\d{4}-\d{2}-\d{2}$", a.date):
        print(f"--date must be YYYY-MM-DD, got {a.date}")
        return 2

    results = [check(a.diagnosis, set()), check(a.tracker, set())]
    if any(r is None for r in results):
        return 2
    if sum(results):
        print("CSV checks failed: nothing written. Fix the rows above first.")
        return 1
    diag, track = read_csv(a.diagnosis), read_csv(a.tracker)
    if (diag and "stall_id" not in diag[0]) or (track and "stall_ref" not in track[0]):
        print("give the diagnosis sheet first and the usage tracker second")
        return 2
    if not track:
        print(f"{a.tracker} has no rows: there is nothing to report. Nothing written.")
        return 2

    try:
        names = sorted(f for f in os.listdir(a.feedback_dir) if PAGE_NAME.match(f))
        pages = [read_page(os.path.join(a.feedback_dir, f)) for f in names]
    except (OSError, InputError) as e:
        print(f"feedback pages: {e}. Nothing written.")
        return 2
    for p in pages:
        p["follow_up"] = follow_up_date(p, diag, track)
    print(f"{a.feedback_dir}: {len(pages)} feedback page(s) read")

    flags = {r["synthetic"] for r in diag + track}
    if flags == {"yes", "no"}:
        print("inputs mix real and synthetic rows; a report never mixes them. Nothing written.")
        return 2
    example = flags == {"yes"}

    out_dir = a.out or os.path.dirname(os.path.abspath(a.tracker))
    snap = snapshot(a.date, diag, track, pages, example)
    try:
        prev, prev_name = previous_snapshot(out_dir, a.date)
    except (OSError, ValueError) as e:
        print(f"earlier snapshot could not be read: {e}. Nothing written.")
        return 2
    changed = what_changed(prev, prev_name, snap)
    targets = {os.path.join(out_dir, f"status-report-{a.date}.md"): status_report(a.date, diag, track, pages, example, changed),
               os.path.join(out_dir, f"brief-{a.date}-draft.md"): brief(a.date, diag, track, pages, example),
               os.path.join(out_dir, f"report-snapshot-{a.date}.json"): json.dumps(snap, ensure_ascii=False, indent=2) + "\n"}
    existing = [t for t in targets if os.path.exists(t)]
    if existing:
        print(f"already exists, not overwritten: {existing}. Nothing written.")
        return 2
    if not os.path.isdir(out_dir):
        os.makedirs(out_dir)
        print(f"created folder {out_dir}")
    for path, text in targets.items():
        with open(path, "w", encoding="utf-8") as f:
            f.write(text)
        print(f"wrote {path}")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
