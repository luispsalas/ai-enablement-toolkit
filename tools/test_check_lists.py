"""Prove check_lists.py works, and that each of its rules is needed.

    python3 tools/test_check_lists.py

For every rule: (1) a clean example file passes; (2) one seeded fault makes
that rule fail, naming its ID; (3) with that rule switched off, the same fault
is NOT caught, so no other rule does its job. All example rows are synthetic.
"""
import csv, os, subprocess, sys, tempfile

HERE = os.path.dirname(os.path.abspath(__file__))
CHECK = os.path.join(HERE, "check_lists.py")
sys.path.insert(0, HERE)
from check_lists import DIAG_COLS, TRACK_COLS  # noqa: E402

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
}


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
        dp, tp = os.path.join(d, "diag.csv"), os.path.join(d, "track.csv")

        write(dp, DIAG_COLS, DIAG)
        write(tp, TRACK_COLS, TRACK)
        code, out = run([dp, tp])
        ok = code == 0 and f"{len(DIAG)} row(s) checked" in out and f"{len(TRACK)} row(s) checked" in out
        print(f"clean example passes: {'ok' if ok else 'FAIL'}")
        failures += not ok

        for rule, (which, i, field, bad) in SEEDS.items():
            rows = [dict(r) for r in (DIAG if which == "diag" else TRACK)]
            rows[i][field] = bad
            write(dp, DIAG_COLS, rows if which == "diag" else DIAG)
            write(tp, TRACK_COLS, rows if which == "track" else TRACK)
            code_on, out_on = run([dp, tp])
            fires = code_on == 1 and f"[{rule}]" in out_on
            code_off, _ = run([dp, tp], disable=rule)
            needed = code_off == 0
            print(f"{rule}: fires on seeded fault {'ok' if fires else 'FAIL'} · "
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
