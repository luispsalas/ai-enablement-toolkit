# Usage tracker: which teams use what

One row per **team and tool**, in `usage-tracker.csv`. It answers three questions at a glance: where usage never started, where it stalled, and what is being done about each. Update a row after every interview, after every fix, and at each `review_date`.

Keep it at team level. It tracks adoption, not individual people, and it never holds names.

## Columns

| Column | What goes in it |
|---|---|
| `team` | Role-level label, the same one used in the diagnosis sheet ("support team", not a manager's name) |
| `tool` | The tool's name |
| `access_given` | Date the team got access, `YYYY-MM-DD` |
| `users_with_access` | How many people on the team have access |
| `first_real_use` | Date of the first use for real work (not a demo or a trial run). Empty if none yet |
| `last_use` | Date of the most recent real use known. Empty if none |
| `users_regular` | How many use it for real work at least as often as the task comes up |
| `status` | One of the five values below |
| `stall_class` | `tool`, `workflow`, `training`, `habit` or `undetermined`, from the diagnosis sheet. **Required** when `status` is `stalled` or `dropped`; empty or a class otherwise |
| `stall_ref` | The diagnosis row(s) behind it, for example `S01 S04` |
| `next_action` | The next concrete step, for example "send feedback-02 to the dev team" or "15-minute walkthrough of the summary feature" |
| `action_owner` | `dev team`, `process owner`, `enablement` or `manager` |
| `review_date` | When to look at this row again, `YYYY-MM-DD`. Leave it empty when the review waits on an event rather than a date, and name the event in `next_action` |
| `source` | How the dates and counts were learned: `interview`, `self-report`, `usage log` or `estimate`. An `estimate` must say so wherever its numbers are repeated |
| `synthetic` | `no` for real teams. `yes` only for example rows, which must never be mixed into real results |

**Dates known only to the month** (common in self-reports) are entered as the first day of that month, and the row's `source` must not be `usage log`. Say "accurate to the month" wherever such a date is repeated.

## Status values (a fixed list)

| Status | Meaning |
|---|---|
| `not started` | Has access, no real use yet |
| `trying` | Some real use, not yet part of how the task is done |
| `regular` | Used for the task most times it comes up |
| `stalled` | Was used, now used much less, but nobody has decided to stop |
| `dropped` | People have stopped and gone back to another way, or the team decided not to use it |

The check script (`../tools/check_lists.py`) rejects any other value, so a new situation forces a decision about the list instead of a one-off label. If a real case does not fit, change the list here and in the script together.

## Reading it

- **Count `not started` rows first.** A tool nobody opened is a rollout problem (access, announcement, training), and it is the cheapest to fix.
- **`users_regular` out of `users_with_access`** is the adoption figure. Always quote it with both numbers and the `source`, never as a bare percentage.
- **A row is not "done" when the fix ships.** It is done when the next review shows the status moved, which is the same follow-up the feedback page asks for.
