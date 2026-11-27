# Office hours and release briefings

*Part of the [AI Enablement Toolkit](../README.md).*

Two templates for the time after an AI tool is in use. **Office hours** are a standing session where anyone can bring a question about the tool. A **release briefing** is a short note sent each time something about the tool changes. Together they keep the conversation going once the rollout is over, and they send what people say to whoever can act on it.

> [!IMPORTANT]
> **Not yet tried with a real team.** The templates and the example are a starting draft. Adapt the cadence, the channels and the wording to your team before relying on them.

## What it does not do

- **It does not cover the first rollout.** Announcing a new tool and explaining what changes for people is the job of the planned change-communication pack. These templates start once people are using the tool.
- **It does not teach a task.** Showing someone how to do one task with one tool is the [walkthrough](walkthrough.md). Office hours answer whatever people bring.
- **It does not diagnose why usage stalled.** A question asked in office hours is a signal. Finding the cause takes the [adoption review kit](../adoption-kit/), with its interview guide and diagnosis sheet.
- **It is not an outage channel.** When the tool is down, people need the dev team's or the vendor's support route, not a session next week.

## Office hours

### Set up

| | |
|---|---|
| **Who runs it** | Someone from enablement, as the [operating model](../governance/operating-model.md) assigns it. They bring in the process owner or the data owner when a question needs them. |
| **When** | The same slot every time, so nobody has to look it up. Weekly or every two weeks during a rollout, then monthly, in step with the [reporting cadence](../adoption-kit/REPORTING.md). |
| **Who comes** | Anyone with access to the tool. No preparation, no slides. A question asked badly is still welcome. |
| **Between sessions** | One named place to post questions, answered there or carried to the next session. |
| **Side list** | A visible list for questions that need someone else or more time. Each one gets a name and a date. |

### Running a session

1. **Start with what changed** since the last session: the latest release briefing, and answers to anything left on the side list.
2. **Take questions, and try each one live.** If it works when you do it, show the person the steps. If it fails for you too, the tool has a fault: write down the steps and the result. This is the kit's [broken or confusing](../adoption-kit/README.md#broken-or-confusing) test, applied in the room.
3. **Move to the side list** any question that needs the data owner (what data may go in, under the [acceptable-use one-pager](../governance/acceptable-use.md)), the process owner (how the tool fits the work), or more time than the session has.
4. **Close with one question:** what will you try first? It ends the session on a next step instead of a summary.

### The log

Keep one line per question. Record the team, never the person's name, so people can ask freely.

| Date | Team | Question, in a few words | Kind | Answered? | Where it went |
|---|---|---|---|---|---|
| | | | how-to · fault · fit with the work · data or policy · other | yes · side list | answered here · FAQ · feedback page · data owner · next briefing |

The kinds line up with the [diagnosis sheet](../adoption-kit/diagnosis-sheet.md)'s classes. A how-to question suggests **training**, a fault you reproduced suggests **tool**, and a question about fit suggests **workflow**. Suggests, and no more: the log records what people asked, not why usage stalled. **When the same question comes from several people**, count the people, not the mentions, and take it to an interview before filing a diagnosis.

### Signs it is not working

- **Nobody comes.** That does not prove everything is fine. Check the [usage tracker](../adoption-kit/usage-tracker.md) for teams marked `stalled` or `dropped`, and ask them directly.
- **The same questions every time.** The answer is not reaching people. Fix the source, such as the walkthrough's [quick-reference card](walkthrough.md#the-quick-reference-card), the FAQ or the training, instead of answering it again.
- **Only the same few people come.** The session may be at the wrong time, or people may not know it is for them.

## Release briefings

### When to send one

Send a briefing for any change people would notice in their work:

- a feature added, removed or moved;
- a new model behind the tool, even when the tool looks the same;
- changed limits, such as how much text it takes or how many requests a day;
- a change to the acceptable-use rules, or to the provider's own usage policy that affects a use;
- a fix for something people reported.

Skip changes nobody will notice. Too many briefings and people stop reading them.

**A new model deserves a briefing of its own.** Output on the same task can change when the model behind a tool changes, with nothing else different ([Model Version & Update](https://luispsalas.github.io/applied-ai-concepts/concepts/model-version-update.html)). Tell people it happened, and ask them to check outputs they rely on more closely for a while. When someone says in office hours that the tool "behaves differently", check whether the model changed before looking for anything else.

### Template

```
Subject: <tool>: <what changes>, from <date>

What changes: <one or two sentences, in terms of the work, not the technology>
What you need to do: <nothing>, or <one action, by when>
What stays the same: <the part people might worry about>
Correction (only if needed): Earlier we said <X>. It is <Y>. For you, this means <Z>.
Questions: office hours on <date>, or <where to post them>
Owner: <name> · Logged on <date>
```

### Rules

- **Send it before the change takes effect**, so nobody meets it in the middle of a task.
- **Keep it under 150 words.** If it needs more, it is a walkthrough or a change-communication pack.
- **Write corrections out in full.** Say what was said before, what is true now and what it means for the reader, so the correction is not lost in a longer note.
- **When the change fixes something people reported, tell the people who hit it.** The [feedback page](../adoption-kit/feedback-template.md)'s follow-up section then checks that the fix reached them.
- **Log each briefing** in the operating model's decision log, with its date and owner, so the status report can say what changed.

## Example: a customer service and sales team

*Illustrative only. The same made-up company as the [intake canvas](../assessment/intake-canvas.md), [oversight levels](../governance/oversight-levels.md) and [acceptable-use](../governance/acceptable-use.md) examples; the people, questions and dates are invented to show the templates in use.*

**Office hours, three weeks into the ticket-triage rollout.** Five support agents came. Three questions went into the log:

| Team | Question | Kind | Where it went |
|---|---|---|---|
| Support | Why did a refund request go to billing? | how-to | Answered: the session showed how to move a ticket, and that every correction is recorded |
| Support | Can it send tickets to the new returns queue? | fit with the work | Side list, then a feedback page to the process owner: the queue is not among the categories yet |
| Support | Can I paste a customer's email into my own chatbot to reword a reply? | data or policy | Answered from the acceptable-use one-pager: no, use the approved assistant |

**The briefing two weeks later:**

```
Subject: Ticket triage: new returns queue, from Monday

What changes: Triage can now send tickets to the returns queue.
What you need to do: Nothing. If a return lands somewhere else, move it as usual.
What stays the same: Urgent tickets are still checked, and so is one in ten of the rest.
Questions: office hours on Thursday, or the support channel
Owner: team lead · Logged on Friday
```

The two agents who raised the returns question get a direct note too, and the feedback page stays open until its follow-up shows the fix reached them.

*Related wiki concepts:* [Model Version & Update](https://luispsalas.github.io/applied-ai-concepts/concepts/model-version-update.html) · [Continuous Feedback & Improvement](https://luispsalas.github.io/applied-ai-concepts/concepts/continuous-feedback-improvement.html) · [AI Literacy](https://luispsalas.github.io/applied-ai-concepts/concepts/ai-literacy.html) · [Shadow AI](https://luispsalas.github.io/applied-ai-concepts/concepts/shadow-ai.html)
