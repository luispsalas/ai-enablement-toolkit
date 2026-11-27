"""Prove build_reports.py works: its gates stop bad input, and its output follows the files.

    python3 tools/test_build_reports.py

1. Gates: a CSV that fails check_lists.py, a feedback page that does not match
   the template, an empty tracker, inputs mixing real and synthetic rows, and
   an output that already exists each stop the run with nothing written.
2. Sections: for each derived section, one planted change in the inputs must
   appear in the output, and the baseline must NOT already show it (so a test
   cannot pass on text that was there anyway).
3. The trial: on examples/trial-n1 the generated brief carries the same figures
   and row IDs as the hand-written leadership-brief.md (wording is not compared).
All test rows and pages are synthetic.
"""
import csv, os, re, subprocess, sys, tempfile

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
BUILD = os.path.join(HERE, "build_reports.py")
sys.path.insert(0, HERE)
from check_lists import DIAG_COLS, TRACK_COLS  # noqa: E402
from test_check_lists import DIAG as BASE_DIAG, TRACK as BASE_TRACK  # noqa: E402

DATE = "2026-10-18"
DIAG = [dict(r) for r in BASE_DIAG]
DIAG[1]["feedback_ref"] = "feedback-01.md"  # S02 is linked to page 01, and S02 to team b's tracker row
TRACK = [dict(r) for r in BASE_TRACK]
PAGES = {
    "01": dict(title="Summary feature not found", owner="enablement", status="open", priority="low",
               shipped="not yet", checked="not yet", result=""),
    "02": dict(title="Export fails on large files", owner="dev team", status="fix planned", priority="medium",
               shipped="not yet", checked="not yet", result=""),
}


def page_text(num, p, drop=None):
    rows = [("For (fix owner)", p["owner"]), ("Status", p["status"])]
    head = "\n".join(f"| {k} | {v} |" for k, v in rows if k != drop)
    prio = "" if drop == "Priority" else f"| **Priority** | {p['priority']} | The rule below |\n"
    return (f"**Feedback {num} — {p['title']}**\n\n| | |\n|---|---|\n| Tool | Example tool |\n{head}\n\n"
            f"| Input | Value | Where it comes from |\n|---|---|---|\n{prio}\n"
            f"## 6. Follow-up\n\n| | |\n|---|---|\n| Fix shipped on | {p['shipped']} |\n"
            f"| Checked on | {p['checked']} |\n| Result | {p['result']} |\n")


def setup(d, diag=None, track=None, pages=None, drop=None):
    for name, cols, rows in (("diag.csv", DIAG_COLS, diag or DIAG), ("track.csv", TRACK_COLS, track or TRACK)):
        with open(os.path.join(d, name), "w", newline="", encoding="utf-8") as f:
            w = csv.DictWriter(f, fieldnames=cols)
            w.writeheader()
            w.writerows(rows)
    for num, p in (pages or PAGES).items():
        with open(os.path.join(d, f"feedback-{num}.md"), "w", encoding="utf-8") as f:
            f.write(page_text(num, p, drop if num == "01" else None))
    with open(os.path.join(d, "feedback-template.md"), "w", encoding="utf-8") as f:
        f.write("not a page: must be ignored\n")


def build(d, date=DATE, extra=()):
    cmd = [sys.executable, "-I", BUILD, os.path.join(d, "diag.csv"), os.path.join(d, "track.csv"), d,
           "--date", date, *extra]
    p = subprocess.run(cmd, capture_output=True, text=True)
    outs = {}
    for kind in ("status-report", "brief"):
        path = os.path.join(d, f"{kind}-{date}.md" if kind == "status-report" else f"brief-{date}-draft.md")
        outs[kind] = open(path, encoding="utf-8").read() if os.path.exists(path) else None
    return p.returncode, p.stdout, outs


def section(text, title):
    m = re.search(rf"^## {re.escape(title)}\n(.*?)(?=^## |\Z)", text, re.M | re.S)
    return m.group(1) if m else ""


def run_case(**inputs):
    with tempfile.TemporaryDirectory() as d:
        setup(d, **inputs)
        return build(d)


def main():
    failures = 0

    def report(name, ok):
        nonlocal failures
        print(f"{name}: {'ok' if ok else 'FAIL'}")
        failures += not ok

    code, out, base = run_case()
    report("clean inputs build both files, 2 pages read (template ignored)",
           code == 0 and base["status-report"] and base["brief"] and "2 feedback page(s) read" in out)
    report("example data is labeled as synthetic", "Example data (synthetic)" in base["brief"])
    report("a secondary class is shown with the primary (S02: training, then habit)",
           "| training, with habit second |" in section(base["brief"], "2. What stalled, and why"))

    # 1. Gates
    bad = [dict(r) for r in DIAG]
    bad[1]["class_primary"] = "habbit"
    code, out, outs = run_case(diag=bad)
    report("gate: a failing CSV stops the run, nothing written",
           code == 1 and "[D1]" in out and not any(outs.values()))
    code, out, outs = run_case(drop="Status")
    report("gate: a page missing its Status row is named, nothing written",
           code == 2 and "feedback-01.md" in out and not any(outs.values()))
    unfilled = {**PAGES, "01": {**PAGES["01"], "priority": "high · medium · low · not set"}}
    code, out, outs = run_case(pages=unfilled)
    report("gate: a page with an unfilled priority is refused, nothing written",
           code == 2 and "priority" in out and not any(outs.values()))
    with tempfile.TemporaryDirectory() as d:
        setup(d)
        with open(os.path.join(d, "track.csv"), "w", encoding="utf-8") as f:
            f.write(",".join(TRACK_COLS) + "\n")
        code, out, outs = build(d)
        report("gate: an empty tracker is refused, nothing written",
               code == 2 and "no rows" in out and not any(outs.values()))
    real = [dict(r, synthetic="no") for r in TRACK]
    code, out, outs = run_case(track=real)
    report("gate: real and synthetic inputs are not mixed, nothing written",
           code == 2 and "mix" in out and not any(outs.values()))
    with tempfile.TemporaryDirectory() as d:
        setup(d)
        build(d)
        path = os.path.join(d, f"status-report-{DATE}.md")
        with open(path, "w") as f:
            f.write("keep me")
        code, out, _ = build(d)
        report("gate: an existing output is not overwritten", code == 2 and open(path).read() == "keep me")

    # 2. Sections: each planted change shows up, and was not in the baseline.
    def seeded(name, where, needle, **inputs):
        code, _, outs = run_case(**inputs)
        kind, title = where
        before, after = section(base[kind], title), section(outs[kind] or "", title)
        report(f"section '{title}' ({kind}): planted change shows up, absent before",
               code == 0 and needle in after and needle not in before)

    t = [dict(r) for r in TRACK]
    t[0]["users_regular"] = "2"
    seeded("adoption", ("status-report", "Adoption by team and tool"), "2 of 5", track=t)
    seeded("working", ("brief", "1. What is working"), "2 of 5 use it regularly", track=t)
    dg = [dict(r) for r in DIAG]
    dg[1]["class_primary"] = "habit"
    seeded("class", ("status-report", "Stalls by class"), "**habit** (1): `S02`", diag=dg)
    dg = [dict(r) for r in DIAG]
    dg[1]["observation"] = "Planted observation"
    seeded("stalled", ("brief", "2. What stalled, and why"), "Planted observation", diag=dg)
    t = [dict(r) for r in TRACK]
    t[0]["review_date"] = "2026-10-01"
    seeded("overdue tracker", ("status-report", "Overdue follow-ups"), "team a", track=t)
    t = [dict(r) for r in TRACK]
    t[1]["review_date"] = "2026-10-17"
    seeded("overdue page", ("status-report", "Overdue follow-ups"), "`feedback-01`, follow-up date 2026-10-17", track=t)
    done = {**PAGES, "02": {**PAGES["02"], "status": "checked", "shipped": "2026-10-12",
                            "checked": "2026-10-16", "result": "fixed"}}
    seeded("fixes", ("brief", "4. Fixes shipped, and whether they landed"),
           "| `feedback-02` | 2026-10-12 | 2026-10-16 | fixed |", pages=done)
    code, _, outs = run_case(pages=done)
    report("a checked page leaves the open list",
           "`feedback-02`" in section(base["status-report"], "Open feedback pages by priority")
           and "`feedback-02`" not in section(outs["status-report"], "Open feedback pages by priority"))
    first = lambda text: re.search(r"`(feedback-\d+)`", section(text, "Open feedback pages by priority")).group(1)
    high = {**PAGES, "01": {**PAGES["01"], "priority": "high"}}
    code, _, outs = run_case(pages=high)
    report("open pages sort by priority (02 medium first, then 01 high first)",
           first(base["status-report"]) == "feedback-02" and first(outs["status-report"]) == "feedback-01")

    # 3. The trial, against the hand-written brief: figures and row IDs, not wording.
    trial = os.path.join(ROOT, "examples", "trial-n1")
    with tempfile.TemporaryDirectory() as d:
        cmd = [sys.executable, "-I", BUILD, os.path.join(trial, "diagnosis-sheet.csv"),
               os.path.join(trial, "usage-tracker.csv"), trial, "--date", "2026-10-10", "--out", d]
        code = subprocess.run(cmd, capture_output=True, text=True).returncode
        gen = open(os.path.join(d, "brief-2026-10-10-draft.md"), encoding="utf-8").read() if code == 0 else ""
    hand = open(os.path.join(trial, "leadership-brief.md"), encoding="utf-8").read()

    def facts(text):
        return {
            "interviews": re.search(r"(\d+) interview", text).group(1),
            "sources": re.search(r"sources?: ([\w -]+?)[.,]", text).group(1).strip(),
            "working": set(re.findall(r"(\d+ of \d+)", section(text, "1. What is working"))),
            "stalls": set(re.findall(r"`(S\d+)`", section(text, "2. What stalled, and why"))),
            "fixes": set(re.findall(r"`(feedback-\d+)`", section(text, "4. Fixes shipped, and whether they landed"))),
            "overdue": re.search(r"Overdue items: (\w+)", text).group(1),
        }
    if gen:
        g, h = facts(gen), facts(hand)
        for key in h:
            report(f"trial brief matches the hand-written one: {key} ({h[key]})", g[key] == h[key])
    else:
        report("trial brief generated", False)

    print("ALL PASSED" if failures == 0 else f"{failures} FAILURE(S)")
    return 1 if failures else 0


if __name__ == "__main__":
    sys.exit(main())
