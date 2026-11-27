# AI operating model: one page

*Part of the [AI Enablement Toolkit](../README.md).*

Who decides what about AI tools in a team, how an idea becomes a tool people use every day, and what gets checked along the way. It fits on one page so that a team can agree on it in one meeting and pin it where everyone can see it.

> [!IMPORTANT]
> **Not yet tried with a real team.** This page sets out how the toolkit's pieces fit together. Until a team has run it through a full cycle, treat it as a starting draft to adapt.

## 1. Roles and decision rights

Each decision has one owner. Others are consulted, but the owner decides and the decision is written down. Each owner also answers to someone, who can ask for the evidence behind a decision and overturn it.

| Decision | Owner | Consulted | Answers to |
|---|---|---|---|
| Fund and prioritize AI work | **sponsor** (a leader who can say yes and no) | process owners | the leadership team |
| Accept an idea for a pilot | **process owner** of the work it changes | enablement, data owner | sponsor |
| What data may go into which tool | **data owner** | dev team, sponsor | sponsor |
| Approve a new tool for wider use | **sponsor** | data owner, dev team, process owner | the leadership team |
| Stop, extend or roll out a pilot | **process owner** | the people in the pilot, enablement | sponsor |
| Change or remove a role because AI takes over its work | **sponsor** | HR, process owner | the leadership team |
| Fix what the diagnosis finds | the **fix owner** for its class (below) | whoever raised it | process owner |

Fix owners follow the [diagnosis sheet](../adoption-kit/diagnosis-sheet.md): a **tool** problem goes to the dev team, a **workflow** problem to the process owner, a **training** problem to enablement, and a **habit** problem to the manager. In a small team one person may hold several roles. Name the role anyway, so each decision is still sorted by kind.

## 2. The cycle

| Stage | Starts when | What happens | Ends when |
|---|---|---|---|
| **Idea** | Anyone proposes a use for AI | The process owner writes down the problem, the people affected and what success would look like | The idea is accepted for a pilot or declined, with the reason |
| **Pilot** | A small group, a start date, a **baseline** and **stop rules** are agreed | The group uses the tool on real work; the [usage tracker](../adoption-kit/usage-tracker.md) records each team and tool | The pilot's end date, or a stop rule fires |
| **Rollout** | The process owner decides to extend it, and the sponsor approves the tool | Access, a short [walkthrough](../rollout/walkthrough.md), and a named person to ask | Most people with access use it when the task comes up |
| **Review** | On the team's review date | Interviews with the [interview guide](../adoption-kit/interview-guide.md) where usage stalls; one [feedback page](../adoption-kit/feedback-template.md) per issue | Each finding has an owner and a follow-up date |

**Stop rules and the baseline are fixed before a pilot starts**, while nobody has a stake in continuing. The baseline is how the work performs today, recorded in the [value check](../assessment/value-check.md) and not changed afterwards. Stop rules are, for example: output needs checking so often that the old way is faster; the tool needs data the data owner has not cleared; nobody in the pilot uses it after the first two weeks.

**Emergency stop and escalation.** Any tool or agent that acts on its own has a stop that named people can trigger, tried before it goes live (see its [specification](agent-spec-template.md)). When stopping is not your call, escalate instead of carrying the risk alone: write down what you saw and what you recommend, send it to the process owner, or to the sponsor if the process owner cannot be reached, and log their decision with its date.

## 3. What each review checks

Pick a cadence and keep it ([`REPORTING.md`](../adoption-kit/REPORTING.md) suggests every two weeks during a rollout, then monthly). Each review checks:

- Adoption for each team and tool, as *n of N* from the usage tracker, with its source;
- Stalls by class, each pointing at its diagnosis rows;
- Open feedback pages by priority, and any follow-up past its date;
- Pilots against their stop rules;
- The [AI and agent inventory](ai-inventory.md): systems found, added or retired since the last review, and rows past their review date. Enablement keeps the file; each row's owner keeps their row current;
- Decisions needed, which go into the [leadership brief](../adoption-kit/leadership-brief-template.md) for the sponsor.

Every decision taken goes into a short log with its date and owner, so a settled question is not reopened at the next review.

## 4. Example: a five-person operations team

*Illustrative only. The team, tool and figures are made up to show the page in use.*

| Role | Held by |
|---|---|
| Sponsor | head of operations |
| Process owner | team lead |
| Data owner | head of operations (customer data) |
| Enablement | one team member, two hours a week |
| Dev team | the tool vendor's support, through the team lead |
| Manager | team lead |

- **Idea:** draft replies to routine customer emails with an AI assistant.
- **Pilot:** two people for four weeks. Stop rules: more than half the drafts need rewriting, or a draft includes customer data from another case.
- **Review at week four:** 2 of 2 use it for most routine emails (self-report). One stall, classed **training**: neither knew the assistant could use the team's reply templates. Feedback page to enablement, follow-up in two weeks.
- **Decision logged:** roll out to all five, with a 15-minute walkthrough on templates first. Owner: team lead.
- **Later, an agent:** the team asks to let an agent close routine cases on its own. That is a new idea, so it goes through the intake canvas again. Accepted for a pilot, it gets a named owner, the team lead, who answers to the head of operations, plus an agent specification and a stop that was tried before the first case closed.

## Where this sits among the other one-pagers

This page says **who decides and when**. The [acceptable-use one-pager](acceptable-use.md) holds the data rules the data owner sets. The [use-case intake canvas](../assessment/intake-canvas.md) holds the scoring for each idea, and the [AI oversight levels](oversight-levels.md) page sets how much human review each AI task gets. The [adoption review kit](../adoption-kit/) is how the review stage finds out why usage stalls. For a deeper check of accountability than this page, use the wiki's [accountability checklist](https://luispsalas.github.io/applied-ai-concepts/notes/governance-and-observability.html#accountability-checklist).
