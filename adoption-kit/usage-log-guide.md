# Reading a tool's usage report

*Part of the [AI Adoption Review Kit](README.md).*

How to fill the [usage tracker](usage-tracker.md) from a tool's own usage report instead of from memory. Every tracker row says where its figures came from: `interview`, `self-report`, `usage log` or `estimate`. A usage log is the strongest of the four for counts and dates, because it does not depend on anyone remembering. It is also the easiest to misread, because each tool defines its own terms. This guide covers finding the report, reading its definitions, turning it into tracker figures, and the traps along the way.

> [!IMPORTANT]
> **Not yet tried on a real rollout.** The kit's first trial used self-reported figures. Treat this guide as a starting draft until a team has filled a tracker from a real usage report with it.

## What it does not do

- **It does not explain why.** A usage report shows who used a tool and when. Why people stopped, or never started, comes from the [interview guide](interview-guide.md). Whether the use did any good comes from the [value check](../assessment/value-check.md).
- **It is not for watching individuals.** Reports usually list people. The tracker holds team-level counts only, never names, and the people whose use is counted should know that the team's figures are read and why.
- **It does not describe any particular product.** Reports differ from tool to tool and change over time. Read your tool's own documentation, and write down the date you read it.

## Before you read: find the report and its definitions

Answer these first, and keep the answers with the tracker. They decide what the numbers mean.

| Question | Why it matters |
|---|---|
| **Where is the report**, and who can open it? | It may sit in an admin console, the account settings, a command inside the tool, or an export. Often only an administrator can see it, so ask the dev team or the vendor for access early. |
| **What counts as "active"?** | One tool may count opening it; another, completing a task with it. Copy the tool's own definition word for word, with the date. Two reports that use different definitions cannot be compared. |
| **What does it count: people, licenses or accounts?** | A shared account or a test account looks like a person. Licenses bought are not people with access. |
| **How far back does it go?** | Many reports keep a limited history. Anything older than that window is gone unless someone exported it. |
| **Can it break down by team, feature or period?** | A company-wide total hides the team that stopped. |
| **What time zone and what period** does it use? | A weekly figure that starts on a different day from yours shifts every count slightly. |

**If there is no usage report at all,** that is a finding in itself: nobody can tell whether the tool is used without asking people. Record it as a feedback page for the dev team, and fill the tracker from interviews in the meantime, labeled as such.

## From the report to the tracker

| Tracker column | What to take from the report | Watch for |
|---|---|---|
| `users_with_access` | People on the team who have been given access | Licenses bought but not assigned, test and administrator accounts, people who have left |
| `first_real_use` | The first day someone on the team used it for real work | Setup and demo days look like use. Check the date with the team lead |
| `last_use` | The most recent day of real use by anyone on the team | A single test click after weeks of silence |
| `users_regular` | People who used it at least as often as the task comes up | Decide the threshold before you read, from how often the task comes up: for a daily task, perhaps three or more days a week over the last four weeks. Write the threshold down and keep it the same at every review |
| `status` | The trend across reviews, together with `users_regular` | The report shows activity. `stalled` and `dropped` are still judgments, and the tracker's definitions decide them |
| `source` | `usage log`, when the counts and dates come from the report | If some figures in the row come from the report and others from people, record the weaker source. A row is only as strong as its weakest figure |

**Always keep both numbers.** `users_regular` of `users_with_access` is the adoption figure, quoted as *n of N* with its source, never as a bare percentage.

## Traps

- **Active is not regular.** A person counted as active once in the month is not using the tool for the task. Use your threshold, not the report's headline figure.
- **Access is not adoption.** A team where every license is assigned can still have nobody using the tool.
- **Totals hide teams.** Break the report down by team before reading it. A rising total can hide one team that dropped the tool.
- **Spikes have causes.** Use often jumps after an announcement, a walkthrough or a release, and falls back. Compare the same length of time before and after, and check the [release briefings](../rollout/office-hours-and-release-briefings.md) for what changed. A change of the model behind the tool can move usage with nothing else different ([Model Version & Update](https://luispsalas.github.io/applied-ai-concepts/concepts/model-version-update.html)).
- **Automations and shared accounts inflate counts.** A script or a shared login can look like a busy user.
- **Spending is not use.** A report of cost or volume (requests, tokens, credits) measures how much was consumed, not how many people rely on the tool. Use it to explain a change, never as the adoption figure.
- **What the log cannot see.** Use of an unapproved tool never appears in the approved tool's report. If usage is low and the work still gets done, ask what people use instead, and record anything found in the [AI and agent inventory](../governance/ai-inventory.md).

## Keep a history

A report that only goes back a few weeks cannot show a trend across months, and a question about what changed around a release cannot be answered after the window has passed. So at each review:

1. **Export the report**, or the part you used, and keep it with that review's status report.
2. **Write down the threshold and the tool's definition of "active"** you used, so the next review reads the figures the same way.
3. **Keep the exports where only the people running the rollout can open them**, because they usually name people, and delete them on the organization's retention rules. The tracker keeps the team-level counts.

## Example: a customer service and sales team

*Illustrative only. The same made-up company as the [synthetic report sample](../examples/synthetic-rollout/), whose tracker rows marked `usage log` come from readings like these.*

**The reply assistant, support team.** The CRM's admin report lists 12 people with access and 11 "active in the last 30 days". Its documentation says *active* means opening the assistant once. The team set its threshold before reading: drafted at least one reply on three or more days a week, in each of the last four weeks. Filtering the export by that gives 10. The tracker row reads `users_regular` 10 of 12, source `usage log`, and the threshold is written into the review notes.

**The call summary assistant, sales team.** The report shows all 6 reps with access and summaries created by 5 of them in the past month. Only 2 created summaries after most of their calls in the last four weeks, so the row reads 2 of 6. The interviews explained the gap: summaries had to be copied into the CRM by hand.

**The call summary assistant, account management.** Access was given to 4 people on 9 November. The report shows no summaries yet, so the row is `not started`, 0 of 4, with `first_real_use` empty.

*Related wiki concepts:* [Observability](https://luispsalas.github.io/applied-ai-concepts/concepts/observability.html) · [Value Realization](https://luispsalas.github.io/applied-ai-concepts/concepts/value-realization-ai.html) · [Shadow AI](https://luispsalas.github.io/applied-ai-concepts/concepts/shadow-ai.html)
