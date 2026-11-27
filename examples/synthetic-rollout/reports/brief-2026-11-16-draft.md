# AI adoption brief, period ending 2026-11-16 (draft)

*Draft built by `tools/build_reports.py`. Write section 3 and the limit sentence, edit the evidence lines, then save as `brief-<date>.md`.*

*Example data (synthetic), not a real rollout.*

**Evidence base:** 11 interview(s), 3 team(s), sources: interview, usage log. **n = 11.** *TO WRITE: one sentence on any limit the reader must know first.*

## 1. What is working

- reply assistant, on support team: 10 of 12 use it regularly (usage log).

## 2. What stalled, and why

| Team · tool | Status | Class | Evidence (one line) | Diagnosis row |
|---|---|---|---|---|
| support team · reply assistant | regular | tool | Drafts for refund emails state a 30-day refund window; the policy changed to 14 days, so agents rewrite the paragraph or stop using the assistant for refunds. | `S01` |
| account management · reply assistant | trying | training, with habit second | After the walkthrough, P07 uses the assistant for renewals; P08 still writes them by hand, because nothing in the renewal checklist prompts it. | `S02` |
| sales team · call summary assistant | trying | workflow, with habit second | Call summaries are saved as a separate document, so reps copy each one into the CRM record by hand, and most stop using the assistant after a few calls. | `S03` |
| account management · call summary assistant | not started | not diagnosed | TO WRITE | none yet |

## 3. Decisions needed

*TO WRITE by hand: at most three, each a question the reader can answer (decision · options · recommended, because · by date).*

## 4. Fixes shipped, and whether they landed

| Fix | Shipped | Checked | Result |
|---|---|---|---|
| `feedback-01` | 2026-11-10 | not yet | not checked yet |
| `feedback-02` | not yet | not yet | not checked yet |
| `feedback-03` | not yet | not yet | not checked yet |

## 5. Next review

2026-11-30. Overdue items: Tracker: sales team · call summary assistant, review date 2026-11-12; `feedback-02`, follow-up date 2026-11-12.
