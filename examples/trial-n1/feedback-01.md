**Feedback 01 — Token usage cannot be tracked over time, so sharp changes go unexplained**

| | |
|---|---|
| Tool | Claude Code (version not recorded) |
| Raised by / date | Interviewer (AI agent, trial of the kit) · 2026-10-09 |
| For (fix owner) | dev team (provisional: see Class) |
| Class | undetermined (diagnosis sheet, row `S01`) |
| Reproduced by the person raising it | not possible |
| Status | open |

## 1. What happens

The user reports that token usage for one model sometimes changes sharply around the time new models are launched, even when they are not using the new models. They have no consistent history of their usage to look back at, so they cannot explain the change or know what to expect next.

## 2. Who hits it, and how we know

- **n:** 1 of 1 person interviewed (code `P01`), a solo consultant who uses the tool daily.
- **How they were found:** a single trial interview of the kit, with the person who set up and maintains their own tool configuration. The sample is one person, chosen for convenience. It shows that the problem exists for one daily user, not how common it is.

## 3. Evidence

- **Steps to reproduce:** none yet. The interviewer had no access to the user's usage records, so the reported change could not be observed. This is why the class is `undetermined` and not `tool`.
- **What the user said** (paraphrased; the user chose paraphrase only): usage for one model changes radically around new model launches without a clear reason; usage history has been hard to track; it is hard to know what to expect.
- **What was ruled out:** nothing yet. The question that decides the class is whether a usage report already exists that the user was not shown. If one does, this is a **training** issue for enablement; if none does, it is a **tool** gap for the dev team.

## 4. Impact

Reported, not measured: the user cannot plan their usage or explain changes in it. No figures were observed in this trial, so none are given.

## 5. Requested change

- **Change:** a consistent usage report the user can look back on, broken down by task and by model (the breakdown the user asked for).
- **Owner:** dev team, provisionally. If a report like this already exists, the owner becomes enablement and the change becomes "show users where it is and how to read it".
- **How we will know it worked:** after the next model launch, the user can open the report for the weeks before and after, see whether usage changed, and say which tasks or models account for the change.

**Priority** (added 2026-10-10, when the kit gained this block):

| Input | Value | Where it comes from |
|---|---|---|
| Reach | 1 of 1 person interviewed; one solo consultant | Section 2 |
| Impact | low (the interviewer's rating) | Section 4: reported, not measured. The user cannot plan or explain usage; no lost work was reported |
| Effort | not estimated yet | No owner is settled while the class is `undetermined` |
| **Priority** | not set | The class must be settled first (diagnosis row `S01`) |

## 6. Follow-up (filled after the fix ships)

| | |
|---|---|
| Fix shipped on | not yet |
| Checked on | not yet: agreed with P01 to check after the next model launch |
| What was checked | |
| Result | |
| Usage after | |
| Next | First settle the class: compare usage records before and after a model launch (diagnosis row `S01`, next check) |

*The page stays open until section 6 is filled.*
