*Example data (synthetic), not a real rollout.*

**Feedback 01 — Refund drafts quote an outdated refund window**

| | |
|---|---|
| Tool | reply assistant (version of 2026-10-05) |
| Raised by / date | EN (enablement) · 2026-10-28 |
| For (fix owner) | dev team |
| Class | tool (diagnosis sheet, row `S01`) |
| Reproduced by the person raising it | yes |
| Status | shipped |

## 1. What happens

When an agent asks the reply assistant to draft an answer to a refund request, the draft says customers have 30 days to request a refund. The policy changed to 14 days. Agents either rewrite that paragraph or stop using the assistant for refund emails.

## 2. Who hits it, and how we know

- **n:** 3 of 11 people interviewed (codes: `P01 P02 P05`), on the support team.
- **How they were found:** interviews with support agents in the fourth week of the rollout. The sample is small and was chosen by the team lead.

## 3. Evidence

- **Steps to reproduce:** open a refund request in the CRM; ask the assistant for a draft reply with default settings; read the refund paragraph. Expected: 14 days. Got: 30 days, in 10 of 10 sample emails tried by enablement.
- **What people said:** all three agents described catching the wrong window themselves and rewriting it (paraphrased).
- **What was ruled out:** not training: the agents spotted the error and know how to edit a draft. Not workflow: the assistant is used at the right step.

## 4. Impact

Risk: a draft that is sent unchanged gives a customer the wrong refund terms. Reported: agents spend extra time on every refund reply, and some have stopped using the assistant for refunds.

## 5. Requested change

- **Change:** update the policy source the assistant drafts from, so refund drafts state the current window.
- **Owner:** dev team
- **How we will know it worked:** refund drafts state 14 days in a new sample of 10 refund emails, and the support row stays at regular.

**Priority** (so the fix owner can rank this page against the others):

| Input | Value | Where it comes from |
|---|---|---|
| Reach | 3 of 11 interviewed; support team | Section 2 |
| Impact | high (risk, reported and reproduced) | Section 4 |
| Effort | small | The fix owner's estimate |
| **Priority** | high | The rule in the template |

## 6. Follow-up (filled after the fix ships)

| | |
|---|---|
| Fix shipped on | 2026-11-10 (policy source updated) |
| Checked on | not yet |
| What was checked | not yet |
| Result | not checked yet |
| Usage after | not yet |
| Next | not yet |
