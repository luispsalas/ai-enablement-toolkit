"""Check the toolkit's CSV files against their fixed lists and rules.

    python3 tools/check_lists.py adoption-kit/diagnosis-sheet.csv adoption-kit/usage-tracker.csv
    python3 tools/check_lists.py examples/trial-n1/diagnosis-sheet.csv examples/trial-n1/usage-tracker.csv
    python3 tools/check_lists.py examples/synthetic-rollout/ai-inventory.csv

Three kinds of file: the diagnosis sheet and usage tracker (adoption kit) and
the AI and agent inventory (governance/ai-inventory.md).

Each file is recognized by its header. Exit code 0 = every rule passed,
1 = at least one row broke a rule (each problem is printed with its rule ID),
2 = a file could not be read or has the wrong columns.

`--disable RULE` switches one rule off. It exists only so the test script can
prove each rule is needed (tools/test_check_lists.py); never use it otherwise.
"""
import csv, re, sys

CLASSES = {"tool", "workflow", "training", "habit", "undetermined"}
NOT_A_STALL = "not a stall"  # a diagnosis outcome only: it never appears in the tracker
STATUSES = {"not started", "trying", "regular", "stalled", "dropped"}
OWNERS = {"dev team", "process owner", "enablement", "manager"}
REPRODUCED = {"yes", "no", "not possible", "not applicable"}
SOURCES = {"interview", "self-report", "usage log", "estimate"}
YESNO = {"yes", "no"}
KINDS = {"chat tool", "built-in assistant", "agent", "automation"}
INV_STATUSES = {"found", "pilot", "approved", "retired"}
DATA_CLASSES = {"public", "internal", "confidential", "personal", "restricted"}
LEVELS = {"full review", "selective review", "human on the loop", "human-initiated"}

DIAG_COLS = ["stall_id", "date", "tool", "team", "observation", "evidence", "ruled_out",
             "class_primary", "class_secondary", "reproduced", "users_affected", "sources",
             "fix_owner", "next_check", "feedback_ref", "synthetic"]
TRACK_COLS = ["team", "tool", "access_given", "users_with_access", "first_real_use", "last_use",
              "users_regular", "status", "stall_class", "stall_ref", "next_action", "action_owner",
              "review_date", "source", "synthetic"]

INV_COLS = ["system_id", "system", "purpose", "kind", "provider", "owner", "team", "status",
            "data_classes", "oversight_level", "connections", "spec_ref", "obligations_ref",
            "approved_on", "review_date", "retirement_criteria", "synthetic"]

DATE = re.compile(r"^\d{4}-\d{2}-\d{2}$")
SYSTEM_ID = re.compile(r"^A\d{2,}$")
CODE = re.compile(r"^P\d{2,}$")


def is_int(s):
    return s.isdigit()


# Each rule: (id, description, function(row) -> True when the row is OK)
DIAG_RULES = [
    ("D1", "class_primary is one of the classes, or not a stall", lambda r: r["class_primary"] in CLASSES | {NOT_A_STALL}),
    ("D2", "class_secondary is empty or one of the classes", lambda r: r["class_secondary"] in CLASSES | {""}),
    ("D3", "reproduced is one of the allowed values", lambda r: r["reproduced"] in REPRODUCED),
    ("D4", "a tool problem must be reproduced (broken vs confusing, test T1)",
     lambda r: r["class_primary"] != "tool" or r["reproduced"] == "yes"),
    ("D5", "an undetermined row must say what would decide it (next_check)",
     lambda r: r["class_primary"] != "undetermined" or r["next_check"].strip() != ""),
    ("D6", "fix_owner is one of the owners (empty only for not a stall)",
     lambda r: r["fix_owner"] in OWNERS or (r["class_primary"] == NOT_A_STALL and r["fix_owner"] == "")),
    ("D7", "synthetic is yes or no", lambda r: r["synthetic"] in YESNO),
    ("D8", "users_affected equals the number of distinct interview codes in sources (test T3)",
     lambda r: is_int(r["users_affected"]) and all(CODE.match(c) for c in r["sources"].split())
     and int(r["users_affected"]) == len(set(r["sources"].split()))),
    ("D9", "date is YYYY-MM-DD", lambda r: bool(DATE.match(r["date"]))),
    ("D10", "a not a stall row has no fix_owner and no class_secondary (there is nothing to fix)",
     lambda r: r["class_primary"] != NOT_A_STALL or (r["fix_owner"] == "" and r["class_secondary"] == "")),
]


def dates_ok(r):
    for c in ("access_given", "first_real_use", "last_use", "review_date"):
        if r[c] and not DATE.match(r[c]):
            return False
    if not r["access_given"]:
        return False
    if r["first_real_use"] and r["first_real_use"] < r["access_given"]:
        return False
    if r["last_use"] and (not r["first_real_use"] or r["last_use"] < r["first_real_use"]):
        return False
    return True


TRACK_RULES = [
    ("T1", "status is one of the five statuses", lambda r: r["status"] in STATUSES),
    ("T2", "stall_class is empty or one of the classes", lambda r: r["stall_class"] in CLASSES | {""}),
    ("T3", "stalled or dropped needs a stall_class",
     lambda r: r["status"] not in {"stalled", "dropped"} or r["stall_class"] != ""),
    ("T4", "action_owner is empty or one of the owners", lambda r: r["action_owner"] in OWNERS | {""}),
    ("T5", "source is one of the allowed sources", lambda r: r["source"] in SOURCES),
    ("T6", "synthetic is yes or no", lambda r: r["synthetic"] in YESNO),
    ("T7", "dates are YYYY-MM-DD and in order (access <= first use <= last use)", dates_ok),
    ("T8", "users_regular is a number no larger than users_with_access",
     lambda r: is_int(r["users_regular"]) and is_int(r["users_with_access"])
     and int(r["users_regular"]) <= int(r["users_with_access"])),
    ("T9", "not started has no first use; regular has one",
     lambda r: not (r["status"] == "not started" and r["first_real_use"])
     and not (r["status"] == "regular" and not r["first_real_use"])),
]

# The inventory's rules check that each record is complete and consistent. None of
# them rejects a row because it describes a problem: a found tool holding personal
# data is exactly what the inventory must be able to show.
ACTIVE = {"pilot", "approved"}
INV_RULES = [
    ("I1", "system_id is A followed by digits (A01, A02...)", lambda r: bool(SYSTEM_ID.match(r["system_id"]))),
    ("I2", "kind is one of the four kinds", lambda r: r["kind"] in KINDS),
    ("I3", "status is one of the four statuses", lambda r: r["status"] in INV_STATUSES),
    ("I4", "data_classes lists one or more of the five data classes, separated by spaces",
     lambda r: r["data_classes"] != "" and set(r["data_classes"].split()) <= DATA_CLASSES),
    ("I5", "oversight_level is empty or one of the four levels, and set for an agent or automation in pilot or approved",
     lambda r: r["oversight_level"] in LEVELS | {""}
     and not (r["kind"] in {"agent", "automation"} and r["status"] in ACTIVE and r["oversight_level"] == "")),
    ("I6", "owner is set unless the status is found", lambda r: r["status"] == "found" or r["owner"] != ""),
    ("I7", "approved_on is YYYY-MM-DD, and set when the status is approved",
     lambda r: (r["approved_on"] == "" or bool(DATE.match(r["approved_on"])))
     and not (r["status"] == "approved" and r["approved_on"] == "")),
    ("I8", "review_date is YYYY-MM-DD, and set unless the status is retired",
     lambda r: (r["review_date"] == "" or bool(DATE.match(r["review_date"])))
     and not (r["status"] != "retired" and r["review_date"] == "")),
    ("I9", "an agent in pilot or approved points to its agent specification (spec_ref)",
     lambda r: not (r["kind"] == "agent" and r["status"] in ACTIVE and r["spec_ref"] == "")),
    ("I10", "a system in pilot or approved has retirement_criteria",
     lambda r: not (r["status"] in ACTIVE and r["retirement_criteria"] == "")),
    ("I11", "synthetic is yes or no", lambda r: r["synthetic"] in YESNO),
]
UNIQUE_RULE = ("I12", "each system_id appears once in the file")

# File-level rule: real and example rows must never be mixed in one file.
MIX_RULE = ("M1", "a file holds either real rows or synthetic rows, never both")


def check(path, disabled):
    try:
        with open(path, newline="", encoding="utf-8") as f:
            reader = csv.DictReader(f)
            header = reader.fieldnames or []
            rows = list(reader)
    except OSError as e:
        print(f"{path}: cannot read ({e})")
        return None
    if header == DIAG_COLS:
        kind, rules, key = "diagnosis sheet", DIAG_RULES, "stall_id"
    elif header == TRACK_COLS:
        kind, rules, key = "usage tracker", TRACK_RULES, "team"
    elif header == INV_COLS:
        kind, rules, key = "AI inventory", INV_RULES, "system_id"
    else:
        print(f"{path}: columns do not match the diagnosis sheet, the usage tracker or the AI inventory")
        return None
    problems = []
    for n, row in enumerate(rows, start=2):  # line 1 is the header
        row = {k: (v or "").strip() for k, v in row.items()}
        for rid, desc, ok in rules:
            if rid in disabled:
                continue
            if not ok(row):
                problems.append(f"{path}:{n} [{rid}] {row.get(key, '?')}: {desc}")
    ids = [(r.get("system_id") or "").strip() for r in rows]
    if kind == "AI inventory" and UNIQUE_RULE[0] not in disabled:
        for d in sorted({i for i in ids if ids.count(i) > 1}):
            problems.append(f"{path} [{UNIQUE_RULE[0]}] {d}: {UNIQUE_RULE[1]}")
    if MIX_RULE[0] not in disabled and len({(r.get("synthetic") or "").strip() for r in rows} & YESNO) > 1:
        problems.append(f"{path} [{MIX_RULE[0]}] {MIX_RULE[1]}")
    # The positive control: say how many rows were looked at, so an empty
    # or misread file is visible instead of passing silently.
    print(f"{path}: {kind}, {len(rows)} row(s) checked, {len(problems)} problem(s)")
    for p in problems:
        print("  " + p)
    return len(problems)


def main(argv):
    disabled, paths = set(), []
    it = iter(argv)
    for a in it:
        if a == "--disable":
            disabled.add(next(it))
        else:
            paths.append(a)
    if not paths:
        print(__doc__)
        return 2
    results = [check(p, disabled) for p in paths]
    if any(r is None for r in results):
        return 2
    return 1 if sum(results) else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
