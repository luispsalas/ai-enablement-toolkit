# Status report, 2026-11-16

*Example data (synthetic), not a real rollout.*

**Read:** 4 usage tracker row(s), 5 diagnosis row(s), 3 feedback page(s). Both CSV files passed `check_lists.py`.

**Evidence base:** 11 interviewed, 3 team(s), sources: interview, usage log.

## Adoption by team and tool

| Team | Tool | Status | Regular users | Source | Review date |
|---|---|---|---|---|---|
| support team | reply assistant | regular | 10 of 12 | usage log | 2026-11-30 |
| account management | reply assistant | trying | 1 of 4 | interview | 2026-11-30 |
| sales team | call summary assistant | trying | 2 of 6 | usage log | 2026-11-12 |
| account management | call summary assistant | not started | 0 of 4 | usage log | 2026-11-30 |

## Stalls by class

- **tool** (1): `S01` support team · reply assistant
- **workflow** (1): `S03` sales team · call summary assistant
- **training** (1): `S02` account management · reply assistant
- **habit** (0): none
- **undetermined** (1): `S05` support team · reply assistant
- *Not a stall* (1): `S04`

## Open feedback pages by priority

| Page | Issue | Priority | Owner | Status | Follow-up date |
|---|---|---|---|---|---|
| `feedback-01` | Refund drafts quote an outdated refund window | high | dev team | shipped | 2026-11-30 |
| `feedback-02` | Call summaries do not reach the CRM record | medium | process owner | fix planned | 2026-11-12 |
| `feedback-03` | Spanish-language replies are drafted in English | not set | enablement | open | not set |

## Overdue follow-ups

- Tracker: sales team · call summary assistant, review date 2026-11-12
- `feedback-02`, follow-up date 2026-11-12

## What changed since the last report

*Compared with `report-snapshot-2026-11-02.json`, the snapshot of the report of 2026-11-02.*

- Tracker: support team · reply assistant, status trying → regular.
- Tracker: support team · reply assistant, regular users 7 of 12 → 10 of 12.
- Tracker: account management · reply assistant, status stalled → trying.
- Tracker: account management · reply assistant, regular users 0 of 4 → 1 of 4.
- Tracker: new row account management · call summary assistant (status not started, regular users 0 of 4).
- Diagnosis: `S02`, class training → training, with habit second.
- Diagnosis: new row `S05` (undetermined).
- Feedback: `feedback-01`, status fix planned → shipped.
- Feedback: `feedback-02`, status open → fix planned.
- Feedback: new page `feedback-03` (priority not set, status open).
