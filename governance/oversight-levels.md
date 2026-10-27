# AI oversight levels

*Part of the [AI Enablement Toolkit](../README.md).*

How much human review an AI task needs, how to choose that level for each task, and how to check that the review is real. The four levels come from the [Human-in-the-Loop](https://luispsalas.github.io/applied-ai-concepts/concepts/human-in-the-loop.html) entry of the Applied AI Concepts wiki. This page adds the part a team needs to use them: which level fits a task, what evidence moves a task between levels, and the signs that a review step has stopped working.

> [!IMPORTANT]
> **Not yet tried with a real team.** The example below is made up to show the page in use. Until teams have set levels with it, treat it as a starting draft to adapt.

## What it does not do

- **It is not legal advice.** If a regulation sets oversight requirements for your system, those come first, and this page does not map them.
- **It does not decide whether to build something.** The [intake canvas](../assessment/intake-canvas.md) does that. This page starts once a task is going ahead.
- **It does not teach how to review an output.** [Reviewing AI output](../literacy/reviewing-ai-output.md) covers how to check. This page covers how much checking each task gets.

**Where it sits:** the intake canvas records each idea's risk facts. This page turns them into a level. The [agent specification template](agent-spec-template.md) records the level for each decision an agent makes, and the [operating model](operating-model.md)'s decision log records every change of level, with its owner and date.

## The four levels

| Level | What the person does | When it fits | What it costs |
|---|---|---|---|
| **Full review** | Checks every output before it takes effect. | A wrong output cannot be undone, or reaches customers, money or a person's record. Also the starting point for any pilot. | Person time on every case, so volume is limited by the reviewers. |
| **Selective review** | Checks a sample, plus every case that trips a rule set in advance (a category, a threshold, low confidence). | Errors can be undone, the system has a measured record on this task, and the volume is too high to check everything. | The sample and the rules must be maintained, and cases outside them go unchecked. |
| **Human on the loop** | Watches the pattern (logs, counts, alerts) and steps in when something looks wrong, without checking individual outputs. | Errors are cheap, quick to notice and easy to undo, and the system has been reliable on this task for some time. | A wrong output takes effect before anyone sees it, so the alerts must work. |
| **Human-initiated** | Nothing routinely. The system acts until a person stops it. | Rarely the right choice: only where an error costs almost nothing. | Everything depends on someone noticing and on a stop that has been tested. |

*The agent specification template used three provisional levels until this page. They map as follows: person approves → full review; person reviews a sample or the exceptions → selective review; agent acts and a person reads the log → human on the loop.*

## Choosing a level

Answer these questions for each task, and write the answers down. The first four are the risk questions the intake canvas already asks, so its answers carry over.

| Question | Points toward stricter review when… |
|---|---|
| **Can a wrong output be undone?** By whom, and at what cost? | It cannot, or only with effort, money or an apology. Sending, paying, publishing and deleting are the usual cases. |
| **How far would one wrong output reach?** How many people or records? | Many, or anyone outside the organization. |
| **Would anyone notice?** How soon? | Nobody would, or only much later. |
| **What data is involved?** | Personal, financial or confidential data. |
| **Can the reviewer tell a right output from a wrong one?** | They cannot do so confidently. No level fixes this: change the reviewer, narrow the task, or do not automate it. |
| **How has the system done on this task, measured?** | There is no measured record yet, on real work. |

Two rules sit on top of the table.

- **Start strict, and earn lighter levels with evidence.** A new task starts at full review in its pilot, unless every answer above points the other way.
- **Some decisions start at full review regardless:** anything involving money, access to systems or data, or a person's record.

The level belongs to the task, never to the tool. One assistant can draft emails under selective review and send offers under full review.

## Is the review real?

A review step can exist on paper and check nothing. As the wiki puts it, *"An oversight step nobody must use is not oversight"* ([Agency](https://luispsalas.github.io/applied-ai-concepts/concepts/agency-ai-systems.html)). Watch for these signs, each with a simple check:

| Sign | Check |
|---|---|
| **Almost everything is approved.** The wiki calls approval rates approaching 100% the clearest available signal that review has become ratification ([Automation Bias](https://luispsalas.github.io/applied-ai-concepts/concepts/automation-bias.html)). | Slip in a few known errors, as in the drill in [reviewing AI output](../literacy/reviewing-ai-output.md), and count how many are caught. |
| **Reviewers have no time for it.** | Measure the time spent per review, and give the step a time budget in people's work, not on top of it. |
| **Corrections are never recorded.** | Record each override. The human override rate is a defined metric in the [AI Observability Toolkit](https://github.com/luispsalas/ai-observability-toolkit/blob/main/data/metrics.csv). |
| **Reviewers only check what is there.** | Ask what is missing as well as what is wrong. |
| **The review can be skipped, and is.** | Make the step required, or record the level the task actually runs at. |

## Moving between levels

**To a lighter level,** a task needs:

- measured results at its current level, on real work, with the sample size stated (*38 of 1,012*, never a bare percentage);
- an agreed threshold for errors or overrides, set before the results were seen;
- a decision by the process owner, logged with the date and the reason.

**Back to a stricter level,** without waiting for the next review, when:

- something goes wrong that the current level should have caught;
- the model, the vendor or the system's instructions change;
- the scope changes: new data, new users or new actions;
- the error or override rate drifts above the agreed threshold.

**Every level below full review needs a tested way to stop the system,** with named people allowed to use it. [Know how to stop, and who decides](../PRINCIPLES.md#know-how-to-stop-and-who-decides) in the principles covers what that involves.

## Example: a customer service and sales team

*Illustrative only. The same made-up company as the [intake canvas](../assessment/intake-canvas.md) and [needs assessment](../assessment/needs-assessment.md) examples; the people, volumes and results are invented to show the levels in use.*

**Ticket triage.** The canvas sent this idea to a four-week pilot with two agents. A misrouted ticket can be moved back, it affects one ticket, and agents see it at once, so on those answers it could run lighter. The rule above still makes it **start at full review**: the two agents check every routing before it takes effect. The team lead's two-week count of misroutes, from the needs assessment, is the baseline.

At the end of the pilot, the agents had corrected 38 of 1,012 routings, below the threshold of 5% agreed at the start. The process owner moves triage to **selective review** and logs the decision: every ticket marked urgent is checked, plus one in ten of the rest, and every correction is recorded. If corrections rise above the threshold, or the categories change, triage goes back to full review.

**Retention offers.** The canvas stopped the original design and brought it back as an offer that the AI drafts and an account manager approves. Offers move money and reach customers, so this one **stays at full review**: no offer goes out until a named person approves it.

**What the example shows:** the level was set per task and changed only on evidence, recorded with its reason. One team ran two levels at once, because the tasks carried different risks.

*Related wiki concepts:* [Human-in-the-Loop](https://luispsalas.github.io/applied-ai-concepts/concepts/human-in-the-loop.html) · [Automation Bias](https://luispsalas.github.io/applied-ai-concepts/concepts/automation-bias.html) · [Scalable Oversight](https://luispsalas.github.io/applied-ai-concepts/concepts/scalable-oversight.html) · [Permission Model](https://luispsalas.github.io/applied-ai-concepts/concepts/permission-model-ai.html) · [Agency](https://luispsalas.github.io/applied-ai-concepts/concepts/agency-ai-systems.html)
