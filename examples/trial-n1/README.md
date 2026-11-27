# Example: the first trial (n = 1)

The kit's first real use, on 2026-10-09: one person, interviewed in a chat by an AI agent following the guide word for word, about an AI coding assistant (Claude Code) and the custom skills built on it.

**Read it with its limits:** n = 1, and the person interviewed set up the tool being studied. It shows the method runs end to end and produces usable output. It says nothing about how common any finding is.

| File | What it is |
|---|---|
| `diagnosis-sheet.csv` | 2 rows: `S01` training with tool second (a usage view by model exists but had not been shown, and it covers fixed windows only; classed 2026-11-27, first recorded as undetermined), `S02` workflow with habit second (add-ons replaced, inventory unclear) |
| `usage-tracker.csv` | 2 rows, self-reported, dates accurate to the month |
| `feedback-01.md` | The one feedback page, still open: the view is found, and the follow-up compares figures recorded before and after the next model launch |
| `leadership-brief.md` | The brief template filled by hand from the three files above |
| `status-report-2026-10-10.md` | The status report as `tools/build_reports.py` generated it from the same three files, unedited. It predates report snapshots, so its *What changed* section still says to write it by hand |

**Not here, on purpose:** the interview notes. The guide keeps notes private, and the interviewee chose paraphrase only, so no file in this repository quotes them.

Check the two CSV files from the repository root:

```bash
python3 tools/check_lists.py examples/trial-n1/diagnosis-sheet.csv examples/trial-n1/usage-tracker.csv
```

The generator's draft brief for this folder carries the same figures and row IDs as the hand-written one; `tools/test_build_reports.py` checks that.
