"""Prove check_lists.py works, and that each of its rules is needed.

    python3 tools/test_check_lists.py

Covers the diagnosis sheet, the usage tracker and the AI inventory.
For every rule: (1) a clean example file passes; (2) one seeded fault makes
that rule fail, naming its ID; (3) with that rule switched off, the same fault
is NOT caught, so no other rule does its job. All example rows are synthetic.
"""
import csv, os, subprocess, sys, tempfile

HERE = os.path.dirname(os.path.abspath(__file__))
CHECK = os.path.join(HERE, "check_lists.py")
sys.path.insert(0, HERE)
from check_lists import DIAG_COLS, TRACK_COLS, INV_COLS  # noqa: E402

DIAG = [  # synthetic example rows, one per situation the rules cover
    dict(stall_id="S01", date="2026-10-09", tool="Example tool", team="example team",
         observation="Export fails", evidence="Error shown", ruled_out="not training",
         class_primary="tool", class_secondary="", reproduced="yes", users_affected="2",
         sources="P01 P02", fix_owner="dev team", next_check="re-run export", feedback_ref="", synthetic="yes"),
    dict(stall_id="S02", date="2026-10-09", tool="Example tool", team="example team",
         observation="Summary never used", evidence="Did not know it existed", ruled_out="not tool",
         class_primary="training", class_secondary="habit", reproduced="not applicable", users_affected="1",
         sources="P03", fix_owner="enablement", next_check="", feedback_ref="", synthetic="yes"),
    dict(stall_id="S03", date="2026-10-09", tool="Example tool", team="example team",
         observation="Stopped after first week", evidence="Unclear", ruled_out="",
         class_primary="undetermined", class_secondary="", reproduced="not possible", users_affected="1",
         sources="P04", fix_owner="enablement", next_check="watch P04 do the task", feedback_ref="", synthetic="yes"),
    dict(stall_id="S04", date="2026-10-10", tool="Example tool", team="example team",
         observation="Plan changes after each review", evidence="Two cases, both after reviewing output",
         ruled_out="not workflow: no extra step", class_primary="not a stall", class_secondary="",
         reproduced="not applicable", users_affected="1", sources="P05", fix_owner="", next_check="",
         feedback_ref="", synthetic="yes"),
]
TRACK = [
    dict(team="team a", tool="Example tool", access_given="2026-09-01", users_with_access="5",
         first_real_use="2026-09-03", last_use="2026-10-08", users_regular="4", status="regular",
         stall_class="", stall_ref="", next_action="", action_owner="", review_date="2026-11-01",
         source="interview", synthetic="yes"),
    dict(team="team b", tool="Example tool", access_given="2026-09-01", users_with_access="6",
         first_real_use="2026-09-10", last_use="2026-09-20", users_regular="1", status="stalled",
         stall_class="training", stall_ref="S02", next_action="walkthrough", action_owner="enablement",
         review_date="2026-10-20", source="self-report", synthetic="yes"),
    dict(team="team c", tool="Example tool", access_given="2026-09-15", users_with_access="3",
         first_real_use="", last_use="", users_regular="0", status="not started",
         stall_class="", stall_ref="", next_action="check access", action_owner="manager",
         review_date="2026-10-15", source="estimate", synthetic="yes"),
]
INV = [
    dict(system_id="A01", system="Example assistant", purpose="Drafts replies", kind="chat tool",
         provider="Example provider", owner="owner a", team="team a", status="approved",
         data_classes="internal personal", oversight_level="", connections="", spec_ref="",
         obligations_ref="", approved_on="2026-09-01", review_date="2026-12-01",
         retirement_criteria="Unused for three months, or replaced", synthetic="yes"),
    dict(system_id="A02", system="Example agent", purpose="Updates records", kind="agent",
         provider="Example provider", owner="owner b", team="team b", status="pilot",
         data_classes="internal", oversight_level="full review", connections="CRM (write)",
         spec_ref="agent-spec-a02.md", obligations_ref="", approved_on="", review_date="2026-11-15",
         retirement_criteria="Pilot stop rules fire", synthetic="yes"),
    dict(system_id="A03", system="Found tool", purpose="Rewording replies", kind="chat tool",
         provider="Unknown", owner="", team="team a", status="found", data_classes="personal",
         oversight_level="", connections="", spec_ref="", obligations_ref="", approved_on="",
         review_date="2026-11-10", retirement_criteria="", synthetic="yes"),
    dict(system_id="A04", system="Old automation", purpose="Tagged emails", kind="automation",
         provider="Example provider", owner="owner c", team="team a", status="retired",
         data_classes="internal", oversight_level="selective review", connections="", spec_ref="",
         obligations_ref="", approved_on="2025-01-10", review_date="", retirement_criteria="Replaced by triage",
         synthetic="yes"),
]

# rule -> (which file, row index, field, seeded bad value)
SEEDS = {
    "D1": ("diag", 1, "class_primary", "habbit"),
    "D2": ("diag", 1, "class_secondary", "culture"),
    "D3": ("diag", 1, "reproduced", "maybe"),
    "D4": ("diag", 0, "reproduced", "no"),
    "D5": ("diag", 2, "next_check", ""),
    "D6": ("diag", 0, "fix_owner", "vendor"),
    "D7": ("diag", 0, "synthetic", "maybe"),
    "D8": ("diag", 0, "users_affected", "3"),
    "D9": ("diag", 0, "date", "09/10/2026"),
    "D10": ("diag", 3, "fix_owner", "process owner"),
    "T1": ("track", 0, "status", "paused"),
    "T2": ("track", 1, "stall_class", "culture"),
    "T3": ("track", 1, "stall_class", ""),
    "T4": ("track", 1, "action_owner", "vendor"),
    "T5": ("track", 0, "source", "guess"),
    "T6": ("track", 0, "synthetic", "maybe"),
    "T7": ("track", 0, "first_real_use", "2026-08-01"),
    "T8": ("track", 0, "users_regular", "9"),
    "T9": ("track", 2, "first_real_use", "2026-09-20"),
    "M1": ("track", 2, "synthetic", "no"),
    "I1": ("inv", 0, "system_id", "1"),
    "I2": ("inv", 0, "kind", "bot"),
    "I3": ("inv", 0, "status", "live"),
    "I4": ("inv", 0, "data_classes", "internal secret"),
    "I5": ("inv", 1, "oversight_level", ""),
    "I6": ("inv", 0, "owner", ""),
    "I7": ("inv", 0, "approved_on", ""),
    "I8": ("inv", 0, "review_date", ""),
    "I9": ("inv", 1, "spec_ref", ""),
    "I10": ("inv", 1, "retirement_criteria", ""),
    "I11": ("inv", 0, "synthetic", "maybe"),
    "I12": ("inv", 1, "system_id", "A01"),
}
# Rules that check two things get a second seed, one per part.
EXTRA_SEEDS = [
    ("I4", ("inv", 0, "data_classes", "")),
    ("I5", ("inv", 0, "oversight_level", "spot checks")),
    ("I7", ("inv", 3, "approved_on", "10/01/2025")),
    ("I8", ("inv", 1, "review_date", "mid-November")),
]
FILES = {"diag": (DIAG_COLS, DIAG), "track": (TRACK_COLS, TRACK), "inv": (INV_COLS, INV)}


def write(path, cols, rows):
    with open(path, "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=cols)
        w.writeheader()
        w.writerows(rows)


def run(paths, disable=None):
    cmd = [sys.executable, "-I", CHECK, *paths] + (["--disable", disable] if disable else [])
    p = subprocess.run(cmd, capture_output=True, text=True)
    return p.returncode, p.stdout


def main():
    failures = 0
    with tempfile.TemporaryDirectory() as d:
        paths = {k: os.path.join(d, f"{k}.csv") for k in FILES}
        dp = paths["diag"]

        for k, (cols, rows) in FILES.items():
            write(paths[k], cols, rows)
        code, out = run(list(paths.values()))
        ok = code == 0 and all(f"{len(rows)} row(s) checked" in out for _, rows in FILES.values()) \
            and "AI inventory, 4 row(s)" in out
        print(f"clean example passes: {'ok' if ok else 'FAIL'}")
        failures += not ok

        for rule, (which, i, field, bad) in [*SEEDS.items(), *EXTRA_SEEDS]:
            for k, (cols, base) in FILES.items():
                rows = [dict(r) for r in base]
                if k == which:
                    rows[i][field] = bad
                write(paths[k], cols, rows)
            code_on, out_on = run(list(paths.values()))
            fires = code_on == 1 and f"[{rule}]" in out_on
            code_off, _ = run(list(paths.values()), disable=rule)
            needed = code_off == 0
            print(f"{rule} ({field}={bad!r}): fires on seeded fault {'ok' if fires else 'FAIL'} · "
                  f"undetected when disabled {'ok' if needed else 'FAIL (another rule also catches it)'}")
            failures += (not fires) + (not needed)

        # A file with the wrong columns is refused, not passed.
        with open(dp, "w") as f:
            f.write("a,b\n1,2\n")
        code, _ = run([dp])
        ok = code == 2
        print(f"wrong columns refused: {'ok' if ok else 'FAIL'}")
        failures += not ok

    print("ALL PASSED" if failures == 0 else f"{failures} FAILURE(S)")
    return 1 if failures else 0


if __name__ == "__main__":
    sys.exit(main())
