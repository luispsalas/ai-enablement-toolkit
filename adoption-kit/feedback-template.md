# Feedback page: one issue, one page

One page per issue, written for the team that can fix it. It should be possible to act on without a meeting, and still make sense to someone who reads it three months later. Copy this file to `feedback-NN.md` and fill in every section. If a section cannot be filled honestly, say why in that section rather than deleting it.

---

**Feedback NN — <short title of the issue>**

| | |
|---|---|
| Tool | <name and version or date, if known> |
| Raised by / date | <initials> · YYYY-MM-DD |
| For (fix owner) | dev team · process owner · enablement · manager |
| Class | tool · workflow · training · habit (from the diagnosis sheet, row `S..`) |
| Reproduced by the person raising it | yes · no · not possible · not applicable |
| Status | open · fix planned · shipped · checked |

## 1. What happens

What people do, where they stop, and what they do instead. Two to four plain sentences, with no interpretation yet.

## 2. Who hits it, and how we know

- **n:** <number> of <number> people interviewed (codes: `P01 P03`), on <team>.
- **How they were found:** <for example: interviews with everyone given access in the first month; or volunteers who replied to an invitation>. Say if the sample is small or self-selected.

## 3. Evidence

- **Steps to reproduce** (for a tool issue: every step, the input used, what was expected, what happened):
  1. …
- **What people said:** paraphrased. A word-for-word quotation goes in quotation marks only with the person's consent, and must match the interview notes exactly.
- **What was ruled out:** <for example: "not training: P01 was shown the feature and still hit the error">.

## 4. Impact

What it costs today: time, rework, a task done the old way, a risk (for example output used without checking). Use numbers only if they were observed or reported, and say which.

## 5. Requested change

One change, specific enough to estimate. If there are several, write one page each, or list them in priority order here.

- **Change:** …
- **Owner:** …
- **How we will know it worked:** the observable sign, for example "P01 and P03 complete the task in the tool without switching to the spreadsheet", or "the team's status in the tracker moves from `stalled` to `regular` within four weeks".

**Priority** (so the fix owner can rank this page against the others):

| Input | Value | Where it comes from |
|---|---|---|
| Reach | <n> of <N> people interviewed; <teams> | Section 2 |
| Impact | high · medium · low | Section 4, with its source (observed, reported or estimated) |
| Effort | small · medium · large · not estimated yet | The fix owner's estimate, never the interviewer's |
| **Priority** | high · medium · low · not set | The rule below |

Rank by impact first, then reach; between equals, the smaller effort goes first. A risk (wrong output used without checking, data going where it should not) is high whatever its reach. **Never give a priority without its three inputs**, and leave it `not set` while the class is `undetermined`: the owner, and so the effort, are not known yet.

## 6. Follow-up (filled after the fix ships)

| | |
|---|---|
| Fix shipped on | YYYY-MM-DD (release or change reference) |
| Checked on | YYYY-MM-DD, by <initials> |
| What was checked | <re-ran the steps in section 3; asked P01 and P03 to do the task; read the tracker> |
| Result | fixed · partly fixed · not fixed · could not check (say why) |
| Usage after | the tracker row before and after, with dates and n |
| Next | close · reopen with a new page · watch until <date> |

A page is **closed only when section 6 is filled**. "Shipped" is not the same as "fixed": the follow-up checks that the change reached the people who were stuck.
