# Use-case intake and prioritization canvas

*Part of the [AI Enablement Toolkit](../README.md).*

One card per idea for using AI, filled in before anyone builds. It answers two questions in order: **can it be done**, and **should it be**. Ideas that fail a stop criterion are set aside early, before anyone has a stake in them. The ones that pass are ranked so the team starts with the most valuable thing it can actually deliver.

> [!IMPORTANT]
> **Not yet tried with a real team.** The example below is made up to show the canvas in use. Until a team has run real ideas through it, treat it as a starting draft to adapt.

**Where it sits:** ideas come from anyone, or from the [business AI needs assessment](needs-assessment.md), which also records today's cost for each. The process owner of the work decides whether an idea goes to a pilot, as the [operating model](../governance/operating-model.md) sets out. An accepted idea is then written up with the [agent specification template](../governance/agent-spec-template.md). How much human review the result needs is set by the planned *AI oversight levels* page; this canvas only records the facts that page will use.

## The canvas

### 1. The idea
- **Problem:** what goes wrong or takes too long today, in one or two sentences.
- **Who and how often:** the team, how many people, how many times a day or week.
- **Today's cost:** time, errors or delays, and whether that figure was measured, reported or estimated.
- **Data and systems:** what the AI would read, what it would write, and in which systems.
- **Proposed by · process owner · date**

### 2. Stop check (answer before scoring)
Any *yes* sets the idea aside, with the reason written down. A set-aside idea can come back once the reason is fixed.

| Question | Yes means |
|---|---|
| Is there no process owner willing to own the result? | Nobody will act on it |
| Does it need data that may not go into an AI tool? | It conflicts with the team's acceptable-use rules |
| Can nobody say what a correct output looks like? | It cannot be tested, and people and the AI will disagree while both seem right |
| Could a wrong output reach a customer or move money before anyone sees it, with no way to undo it? | Redesign it so a person approves first, or stop |
| Is the real problem training, habit or a workflow step? | Fix that instead; the [adoption review kit](../adoption-kit/) helps tell which |
| Does the task come up too rarely to repay the setup? | Do it by hand |

### 3. Score
Score each line 1 (low), 2 or 3 (high), and write the evidence beside it. A score without evidence counts as 1.

| | Question | Evidence |
|---|---|---|
| **Value** | How much time or error does it remove, across everyone who does the task? | |
| | Does it improve something a customer or a decision depends on? | |
| **Feasibility** | Is the data there, complete and consistent enough? | |
| | Can the AI reach the systems it needs (an API, read or write access)? | |
| | Is there a written definition of a correct output, and a few labeled examples? | |
| **Risk facts** | Can a wrong output be undone? How many people or records would one reach? Would anyone notice? What data is involved? | recorded for the oversight levels page, not scored |

**Ranking:** value first, then feasibility; between equals, the smaller build goes first. Risk does not lower an idea's rank. It raises how much review it needs and how carefully it is built. **Never give a rank without its scores and their evidence**, so anyone can check how it was reached.

### 4. Decision
**Pilot · park · stop**, with the reason, the process owner who decided, the date, and the next review date. The decision goes in the team's decision log.

## Example: three ideas from a customer service and sales team

*Illustrative only. A made-up mid-size company that runs sales and service in a CRM; the people, volumes and scores are invented to show the canvas in use.*

| | Service-ticket triage | Lead qualification | Automatic retention discounts |
|---|---|---|---|
| **Problem** | Agents read and route every incoming support email by hand | Sales reps work leads in arrival order, not by fit | Customers who look likely to cancel are offered nothing until they call |
| **Who and how often** | 12 agents, about 300 emails a day (estimated) | 6 reps, about 40 leads a day (reported) | Account managers, a few cases a week |
| **Data and systems** | Email text and the customer record; writes a category, urgency and queue in the CRM | Lead form fields and past won and lost deals | Usage history; would write and send an offer |
| **Stop check** | Passes | **Fails:** sales and marketing define a qualified lead differently, so nobody can say what a correct score is | **Fails:** a wrong offer reaches the customer and moves money, with no way to take it back |
| **Value** | 3: about 300 reads a day moved off agents | 3: reps start with the best leads | n/a |
| **Feasibility** | 3, 3, 2: text and CRM API are available; categories exist but need written definitions | n/a | n/a |
| **Risk facts** | A misroute is undone by moving the ticket; affects one ticket; agents see it at once | n/a | n/a |
| **Decision** | **Pilot** with two agents for four weeks; write the category definitions first | **Park** until sales and marketing agree a written definition; review next quarter | **Stop as designed.** Redesign as a drafted offer that an account manager approves, then score again |

**What the example shows:** of three reasonable ideas, one goes ahead, one waits for a business decision that no model can make, and one comes back in a safer form. The triage pilot would next be written up with the [agent specification template](../governance/agent-spec-template.md), whose own example is a triage workflow of the same shape.
