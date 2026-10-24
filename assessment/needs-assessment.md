# Business AI needs assessment

*Part of the [AI Enablement Toolkit](../README.md).*

A first look at where AI could help across an organization, before anyone has picked a tool or an idea. It ends in a short list of ideas, each with the facts the [intake canvas](intake-canvas.md) needs, and a record of how the work performs today, so value can later be measured against something real.

Organizations arrive in two states. Some can name what they want AI to change. Others only know that they should be doing something with AI. The assessment has a path for each: a **questionnaire** when the goals are clear, and a **wireframe** when they are not, which sketches a hypothetical use case to find out what the goals should be.

> [!IMPORTANT]
> **Not yet tried with a real organization.** The example below is made up to show the assessment in use. Until it has been run with real teams, treat it as a starting draft to adapt.

## What it does not do

- **It does not choose or rank ideas.** It finds them. Each idea it produces still goes through the [intake canvas](intake-canvas.md), which decides whether it can and should be done.
- **It does not measure value.** It records how the work performs today, and says whether each figure was measured, reported or estimated. The comparison happens after a pilot, against that record.
- **It does not test skills.** The section on people is a quick snapshot of where they stand. Whether training changed what people do is the planned training pre/post check's job.
- **It does not set the rules.** It asks what the rules are today. Who decides what is set out in the [operating model](../governance/operating-model.md).

## Before you start

**Ask how defined the initiative is, on a scale of 1 to 5.** At 1, someone has said the organization should use AI, and nothing more. At 5, there is a named goal, an owner and a rough idea of the work involved. **From 1 to 2, start with the wireframe.** From 3 to 5, go straight to the questionnaire. A wireframe that produces a clear goal then continues into the questionnaire.

**Ask how many people will take part.** With one or two people, a single conversation is usually enough. From four people up, plan two to three times as long and split it into several shorter sessions, or the later sections get rushed.

**Keep discovery apart from the deliverables.** The sessions are for asking and listening. The written outputs come afterwards, chosen by the organization from the menu at the end. Producing documents in the room, or every document by default, crowds out the ones that matter.

## Path A: the questionnaire

For organizations that can name their goals. Each section has a few questions and a note on what the answers are for. Write down who answered and where each figure came from.

### 1. Goals
- What should be different in a year? Name one or two outcomes, such as faster responses, fewer errors or more capacity without hiring.
- Who owns each outcome, by name?
- How would you know it had happened?

*For:* every idea found later has to serve one of these goals, or it does not go on the list.

### 2. Work and where time goes
- Which tasks take the most time, cause the most rework or create the longest waits?
- For each: who does it, how many people, how often, and how long it takes.
- Is that figure measured (from a system), reported (from the people doing it) or estimated?

*For:* this is the baseline. Each idea's *today's cost* on the intake canvas comes from here, and so does the starting point the planned value check compares against. A reported figure is fine if it is labeled as one.

### 3. Data and systems
- Where does the information for those tasks live, and is it complete and consistent?
- Which systems would an AI tool need to read from or write to, and do they allow it?
- Is there any data that must never go into an AI tool?

*For:* the canvas's feasibility scores and its stop check on data.

### 4. People and skills
- Who already uses AI tools at work, for what, and with which tools (including ones the organization has not approved)?
- How confident are people at checking AI output before they rely on it?
- Who would people go to with a question about an AI tool today?

*For:* a snapshot that shows where literacy work should start. The [AI literacy deck](../literacy/deck/) and [reviewing AI output](../literacy/reviewing-ai-output.md) cover the basics; the planned training pre/post check measures whether they changed anything.

### 5. Risk and rules
- Are there written rules on using AI tools, and does anyone follow them?
- Which decisions or customer-facing outputs must always have a person check them?
- If an AI tool got something wrong, who would notice, and how fast?

*For:* the canvas's stop check, and the gaps the [operating model](../governance/operating-model.md) and the planned acceptable-use one-pager should close. Record the answers; do not settle them here.

### 6. Quick wins and longer bets
- Which problem could be helped within a month with tools you already have?
- Which would take longer, but would matter much more if it worked?

*For:* a balanced idea list. Quick wins build confidence and early evidence; longer bets may matter more in the end.

## Path B: the wireframe

For organizations that cannot yet name their goals. Instead of asking what they want, sketch one hypothetical use case with them and let the gaps in the sketch show what needs deciding. Start from a frustration someone mentions, such as a morning lost to email, and never from a tool.

Fill in one card per sketch. Leave a cell blank rather than guess, and write what is missing in the last row.

| | Question | Sketch |
|---|---|---|
| **Who** | Which people would use it, and how many? | |
| **Task** | What exactly would they do with it, step by step? | |
| **Today** | How is that task done now, and what does it cost (time, errors, delay)? Measured, reported or estimated? | |
| **Change** | What would be different for them if it worked? | |
| **Success** | What would someone see that proves it worked? | |
| **Value hypothesis** | If it worked, what would the organization gain, and roughly how much? | |
| **Unknowns** | What did nobody in the room know? | |

**How to read the result.** The *Unknowns* row matters most. Each unknown becomes a question with an owner and a date. A sketch ends one of two ways:

- **A draft goal**, with its value hypothesis and the baseline to collect. Continue with the questionnaire, starting from section 2.
- **A list of what to learn first**, when too much is unknown to state a goal. That list is a useful result in its own right: it shows the organization what to find out before spending money on AI.

A wireframe is a hypothesis to test. Sketch two or more if the first one stalls, and drop any sketch that cannot name who would use it.

## Outputs: a menu

The organization picks which of these it wants. Produce only those.

| Output | What it holds | Goes to |
|---|---|---|
| **Idea list** | One line per idea: the problem, who and how often, today's cost and its source, and the goal it serves | Each idea becomes a card in the [intake canvas](intake-canvas.md) |
| **Baseline record** | The figures from section 2 (or from the wireframe's *Today* row), each labeled measured, reported or estimated, with the date | The planned value check, after a pilot |
| **Readiness gaps** | What is missing in data, skills or rules, each with a suggested owner | The [operating model](../governance/operating-model.md)'s decision log, and the literacy work |
| **What to learn first** | The open questions from a wireframe, each with an owner and a date | The next conversation |

## Example: a customer service and sales team

*Illustrative only. The same made-up mid-size company as the [intake canvas](intake-canvas.md) example, which runs sales and service in a CRM; the people, volumes and answers are invented to show the assessment in use.*

**Before starting.** The head of operations scores the initiative at 2: leadership has asked for AI in customer service, with no goal attached. Five people will take part, so the work is split into two sessions.

**Wireframe.** An agent mentions that the first hour of every day goes on reading and routing email. The sketch:

| | Sketch |
|---|---|
| **Who** | The 12 service agents |
| **Task** | Read each incoming email, decide its category and urgency, move it to the right queue |
| **Today** | About 300 emails a day, read one by one (estimated by the team lead) |
| **Change** | Agents start the day with emails already sorted, and check the sorting instead of doing it |
| **Success** | Fewer misrouted tickets, and agents answering sooner |
| **Value hypothesis** | Most of that first hour back for each agent |
| **Unknowns** | How many tickets are misrouted today; whether the categories are written down anywhere |

The sketch produces a draft goal (faster first responses without adding staff) and two questions: the team lead will count misroutes for two weeks, and the service manager will write down the categories.

**Questionnaire.** With a goal named, the second session runs sections 2 to 6. Section 2 adds the sales team's lead handling (6 reps, about 40 leads a day, reported). Section 5 brings out a rule that any discount needs an account manager's approval, which any retention idea will have to respect.

**Outputs chosen.** The organization asks for the idea list and the baseline record. The idea list holds ticket triage, lead qualification and automatic retention discounts, which are the three ideas the [intake canvas example](intake-canvas.md#example-three-ideas-from-a-customer-service-and-sales-team) then assesses. The baseline record holds the email and lead volumes, labeled *estimated* and *reported*, and the misroute count, labeled *measured* once the two weeks are done.

**What the example shows:** a request with no goal behind it became a named goal, a baseline with its sources and a short idea list in two sessions. The wireframe did not decide that triage was worth doing. It found the question that had to be answered first, which is how often tickets are misrouted today.
