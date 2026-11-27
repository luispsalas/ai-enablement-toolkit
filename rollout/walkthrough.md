# Walkthrough script and quick reference

*Part of the [AI Enablement Toolkit](../README.md).*

A short guided session, about 20 minutes, in which people do one real task with one AI tool while someone who knows it watches. It ends with a one-page card for that tool and task, which people keep. A walkthrough is the usual way into a new tool at rollout, and the usual fix when the [diagnosis sheet](../adoption-kit/diagnosis-sheet.md) classes a stall as **training**: people were never shown, were shown once, or were shown a different task.

> [!IMPORTANT]
> **Not yet tried with a real team.** The script, the timings and the example are a starting draft. Adapt them before relying on them.

## What it does not do

- **It does not teach AI in general.** The [AI literacy deck](../literacy/deck/) does that, and the [prompt quick-reference card](../literacy/prompt-card.md) covers asking any chat tool. A walkthrough covers one task in one tool.
- **It does not announce a tool.** Telling people a tool is coming and what changes for them is the job of the planned change-communication pack.
- **It does not answer whatever people bring.** That is [office hours](office-hours-and-release-briefings.md), which start after the walkthrough.
- **It does not show that anything changed.** Whether people now use the tool is read from the [usage tracker](../adoption-kit/usage-tracker.md) at the next review.

## Before the session

- **Pick one task** that people do often, in their own words. If the walkthrough fixes a stall, take the task from its diagnosis row.
- **Prepare an example** that looks like real work and is safe to use: no data the [acceptable-use one-pager](../governance/acceptable-use.md) keeps out of this tool. Made-up or anonymized material is usually enough.
- **Do the task yourself first**, in the same tool, with the same access people will have. If it fails for you, fix it or postpone, because a walkthrough of a broken step teaches people that the tool does not work.
- **Keep the group small.** One to five people is easiest. With more, plan about twice the time, or split the group, because everyone needs a turn at the keyboard.
- **Send two or three terms ahead** if the task brings new vocabulary, with links to the [glossary](../literacy/glossary.md), so the session is spent on the task and not on definitions.
- **Write the card** before the session, from the template below, so you can hand it out at the end.

## The script

| Step | Time | What happens |
|---|---|---|
| **1. Why this task** | 2 min | What changes for them, what the tool will and will not do, and whom to ask afterwards. |
| **2. Show it once** | 5 min | Do the whole task on the example. Explain the decisions, such as what to give the tool and what to look at in its answer, more than the clicks. |
| **3. They do it** | 8 min | Each person does the task on their own copy of the example. Watch, and do not take the keyboard. Write questions about anything else on a side list, each with a name and a date for the answer. |
| **4. Check the result** | 3 min | Show the one or two checks that matter for this task before using the output, and one wrong output, so people see what a mistake looks like here ([Reviewing AI output](../literacy/reviewing-ai-output.md)). |
| **5. Close** | 2 min | Ask what surprised them, and what they will do first. Agree on a few next steps, each small enough to do within three days. Hand out the card, and say when office hours run. |

**If someone gets stuck in step 3,** note where. The same step stopping two people is a finding: it goes on the side list and, if it is the tool's fault, on a [feedback page](../adoption-kit/feedback-template.md).

## The quick-reference card

One card per tool and task, on one page or one screen. Date it, and update it when the tool changes: a [release briefing](office-hours-and-release-briefings.md#release-briefings) that touches this task means the card changes too.

```
<Tool> · <task>                                  Updated <date>

When to use it:   <the situation, in the team's words>
Steps:            1. ...
                  2. ...
                  3. ...
What to give it:  <the input, and what data may go in>
Check before use: <the one or two checks that matter>
If it goes wrong: <what to do instead, and whom to ask>
Don't:            <the one mistake that causes most trouble>
```

## After the session

- **Update the tracker row:** the walkthrough in `next_action` is done, and `review_date` is when you will look again.
- **At the next review, read the row.** If the stall was training, the status should move toward `regular`. If people were shown and still do not use the tool, the cause was not only training: interview again, and expect habit or workflow ([diagnosis sheet](../adoption-kit/diagnosis-sheet.md#the-four-classes)).
- **Answer the side list** by the dates you gave, and send the card again if it changed.

## Example: a customer service and sales team

*Illustrative only. The same made-up company as the [synthetic report sample](../examples/synthetic-rollout/), where this walkthrough appears in the second report.*

Two account managers had tried the reply assistant once and gone back to writing renewal emails by hand. Neither had been shown that it could start from the team's reply templates, so the diagnosis row classed the stall as **training**. Enablement ran a 20-minute walkthrough on 5 November with all four account managers, on a made-up customer whose contract renews next month.

The card they kept:

```
Reply assistant · renewal emails                 Updated 2026-11-05

When to use it:   A customer's contract renews within 60 days
Steps:            1. Open the customer's record in the CRM
                  2. Choose "Reply with assistant", then the "Renewal" template
                  3. Add the renewal date and any change in terms
                  4. Read the draft and edit it
What to give it:  The customer's own record only. Never paste another customer's details
Check before use: The renewal date, price and terms, against the contract
If it goes wrong: Write it by hand and post the case in the team channel;
                  office hours are on Thursdays
Don't:            Send a draft you have not read to the end
```

**Two weeks later,** the tracker showed one of the four using the assistant for renewals. The follow-up interviews found a second cause for the account manager who still wrote by hand: nothing in the renewal checklist prompts the assistant, so it is forgotten. That is **habit**, and its fix belongs to the manager, who adds the assistant to the checklist. A walkthrough alone would not have fixed it.

*Related wiki concepts:* [AI Literacy](https://luispsalas.github.io/applied-ai-concepts/concepts/ai-literacy.html) · [Verification](https://luispsalas.github.io/applied-ai-concepts/concepts/verification.html) · [Automation Bias](https://luispsalas.github.io/applied-ai-concepts/concepts/automation-bias.html)
