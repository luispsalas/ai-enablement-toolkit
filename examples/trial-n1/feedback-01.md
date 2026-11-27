**Feedback 01 — Usage by model is hard to find, and cannot be compared around a launch**

| | |
|---|---|
| Tool | Claude Code (version not recorded) |
| Raised by / date | Interviewer (AI agent, trial of the kit) · 2026-10-09 |
| For (fix owner) | enablement (the missing part is the vendor's: see section 5) |
| Class | training, with tool second (diagnosis sheet, row `S01`; first recorded as undetermined, settled 2026-11-27) |
| Reproduced by the person raising it | no: the view by model works when the reviewer opens it (2026-11-27, section 3) |
| Status | open |

## 1. What happens

The user reports that token usage for one model sometimes changes sharply around the time new models are launched, even when they are not using the new models. They have no consistent history of their usage to look back at, so they cannot explain the change or know what to expect next.

## 2. Who hits it, and how we know

- **n:** 1 of 1 person interviewed (code `P01`), a solo consultant who uses the tool daily.
- **How they were found:** a single trial interview of the kit, with the person who set up and maintains their own tool configuration. The sample is one person, chosen for convenience. It shows that the problem exists for one daily user, not how common it is.

## 3. Evidence

- **Where the history is** (checked 2026-11-27 on the user's setup, an individual Pro plan signed in to Claude Code with a claude.ai account):
  1. In Claude Code, run `/stats` and open the Models tab. It shows each model's share of tokens, with input, output and cache counts, for the last 7 days, the last 30 days or all time.
  2. The Overview tab of the same screen shows activity by day since first use, but not by model.
  3. On claude.ai, Settings > Usage shows the current session and the current week as a share of the plan limit. It keeps no history and has no breakdown by model.
  4. Anthropic's documentation names `/stats` only as "activity stats" and says Claude Code usage analytics are not available to individual plans.

  **Result:** a usage history by model exists, so the problem does not reproduce as a missing report. The interviewer still has no access to the figures from before the interview, so the sharp change the user reported remains unobserved.
- **What the user said** (paraphrased; the user chose paraphrase only): usage for one model changes radically around new model launches without a clear reason; usage history has been hard to track; it is hard to know what to expect.
- **What was ruled out:** **tool** as the main cause. The question that decided the class was whether a usage report already exists that the user was not shown. One does, so this is a **training** issue first. Two gaps keep **tool** as the second class. The view has fixed windows (7 days, 30 days, all time), so the weeks before and after a launch cannot be compared later unless the figures were recorded at the time. It also counts tokens, while Settings > Usage shows the share of the plan limit, and the limits themselves change around launches. That may explain part of what the user saw.

## 4. Impact

Reported, not measured: the user cannot plan their usage or explain changes in it. No figures were observed in this trial, so none are given.

## 5. Requested change

- **Change:** show the user the Models tab of `/stats`, and record its 30-day figures at each review, so the weeks after a launch can be compared with the weeks before it (usage-log guide, [Keep a history](../../adoption-kit/usage-log-guide.md#keep-a-history)).
- **Still missing (the tool gap):** a history by model for any chosen period, and a link between tokens and the share of the plan limit. Only the vendor can build that. It is recorded here and has not been raised.
- **Owner:** enablement, for showing the view and keeping the record. The missing history is the vendor's, through the dev team if it is raised.
- **How we will know it worked:** after the next model launch, the user can compare the figures recorded before and after, see whether usage by model changed, and say which models account for the change.

**Priority** (added 2026-10-10, when the kit gained this block):

| Input | Value | Where it comes from |
|---|---|---|
| Reach | 1 of 1 person interviewed; one solo consultant | Section 2 |
| Impact | low (the interviewer's rating) | Section 4: reported, not measured. The user cannot plan or explain usage; no lost work was reported |
| Effort | small | Enablement's part: one walkthrough and a note at each review. The vendor's part is not ours to estimate |
| **Priority** | low | Reach 1, impact low, effort small; set when the class was settled (2026-11-27) |

## 6. Follow-up (filled after the fix ships)

| | |
|---|---|
| Fix shipped on | not yet |
| Checked on | not yet: the check comes after the next model launch, once figures from before it are recorded |
| What was checked | 2026-11-27: the user's `/stats` and Settings > Usage, and Anthropic's documentation for individual plans (section 3). A model launch has passed since the interview, but no figures from before it were recorded, so it cannot be compared |
| Result | |
| Usage after | |
| Next | Record the Models tab's 30-day figures at each review, starting now. After the next model launch, compare before and after (diagnosis row `S01`, next check) |

*The page stays open until section 6 is filled.*
