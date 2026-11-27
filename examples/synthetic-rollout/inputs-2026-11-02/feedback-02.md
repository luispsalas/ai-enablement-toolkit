*Example data (synthetic), not a real rollout.*

**Feedback 02 — Call summaries do not reach the CRM record**

| | |
|---|---|
| Tool | call summary assistant (version of 2026-10-12) |
| Raised by / date | EN (enablement) · 2026-10-30 |
| For (fix owner) | process owner |
| Class | workflow, with habit second (diagnosis sheet, row `S03`) |
| Reproduced by the person raising it | not applicable |
| Status | open |

## 1. What happens

After a sales call, the assistant saves its summary as a separate document. Reps have to copy it into the customer record in the CRM by hand, and four of six have stopped using the assistant.

## 2. Who hits it, and how we know

- **n:** 3 of 9 people interviewed (codes: `P10 P11 P12`), on the sales team.
- **How they were found:** interviews with three of the six reps, chosen by the sales lead; the usage log covers all six.

## 3. Evidence

- **Steps to reproduce:** not a tool fault: the save works as designed. The extra step is copying the summary into the CRM record.
- **What people said:** the reps described the copy step as the reason they stopped (paraphrased).
- **What was ruled out:** not tool: summaries are accurate and saved. Not training: all three know how to use it.

## 4. Impact

Reported: a copy step on every call. Usage log: 2 of 6 reps use the assistant after the second week.

## 5. Requested change

- **Change:** save each summary to the customer record in the CRM directly.
- **Owner:** process owner, with the CRM administrator
- **How we will know it worked:** summaries appear in the CRM record without a copy step, and the sales row moves to regular within four weeks.

**Priority** (so the fix owner can rank this page against the others):

| Input | Value | Where it comes from |
|---|---|---|
| Reach | 3 of 9 interviewed; sales team | Section 2 |
| Impact | medium (reported, with the usage log) | Section 4 |
| Effort | medium | The fix owner's estimate |
| **Priority** | medium | The rule in the template |

## 6. Follow-up (filled after the fix ships)

| | |
|---|---|
| Fix shipped on | not yet |
| Checked on | not yet |
| What was checked | not yet |
| Result | not checked yet |
| Usage after | not yet |
| Next | not yet |
