# Example: a made-up rollout, two reports apart

*Example data (synthetic), not a real rollout.* Every team, person, figure and date here is invented to show the [report generator](../../tools/build_reports.py) at a realistic size. For real use of the kit, see the [first trial](../trial-n1/) (n = 1).

The company is the same made-up one as in the [intake canvas](../../assessment/intake-canvas.md), [oversight levels](../../governance/oversight-levels.md) and [acceptable-use](../../governance/acceptable-use.md) examples: a mid-size business that runs sales and service in a CRM. Three teams use two AI tools, a reply assistant and a call summary assistant, and the rollout is reviewed every two weeks.

## What is in it

| Folder or file | What it holds |
|---|---|
| `inputs-2026-11-02/` | The kit's files at the first review: usage tracker (3 rows), diagnosis sheet (4 rows) and 2 feedback pages |
| `inputs-2026-11-16/` | The same files two weeks later: 4 tracker rows, 5 diagnosis rows, 3 feedback pages |
| `ai-inventory.csv` | The company's [AI and agent inventory](../../governance/ai-inventory.md): five systems, including one found in use without approval. Check it with `python3 tools/check_lists.py examples/synthetic-rollout/ai-inventory.csv` |
| `reports/` | What the generator wrote for each date, unedited: the status report, the draft leadership brief and the snapshot the next run compares against |

## What the second report shows

Between the two dates, the fix for the outdated refund window ships, the support team moves to regular use, a walkthrough gets account managers started, a new tool reaches a team that has not used it yet, and a new problem appears that nobody can classify yet. The second status report's *What changed since the last report* section lists each of these, worked out from the snapshot of the first report. Its *Overdue follow-ups* section flags the sales team's review date, which has passed.

The briefs are drafts, as the generator leaves them. Section 3 (decisions needed) and the limit sentence are for a person to write, so here they still say *TO WRITE*.

## Rebuild it

From the repository root, into a new folder so nothing here is overwritten:

```bash
mkdir -p /tmp/sample-reports
```

```bash
for d in 2026-11-02 2026-11-16; do python3 tools/build_reports.py examples/synthetic-rollout/inputs-$d/diagnosis-sheet.csv examples/synthetic-rollout/inputs-$d/usage-tracker.csv examples/synthetic-rollout/inputs-$d --date $d --out /tmp/sample-reports; done
```

Run the first date before the second: the second report compares against the snapshot the first one writes. `tools/test_build_reports.py` rebuilds this sample on every run and fails if the result differs from the files in `reports/`.
