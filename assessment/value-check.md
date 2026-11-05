# Value baseline and check

*Part of the [AI Enablement Toolkit](../README.md).*

One record per use case that carries its value from the first idea to a decision. It fixes what will count as success before anyone sees results, keeps the starting figures with their sources, and makes each review compare like with like. At the end, the team can say whether the work got better, by how much, and who confirmed it.

> [!IMPORTANT]
> **Not yet tried with a real team.** The example below is made up to show the record in use. Until teams have carried real use cases through it, treat it as a starting draft to adapt.

## What it does not do

- **It is not a return-on-investment model.** It records whether the work improved. Turning that into money, with costs and payback, is a separate step this page does not cover.
- **It is not a statistics method.** It asks for a fair comparison and an honest count. Where the stakes justify it, a proper experiment design is worth getting help with.
- **It does not track adoption.** The [usage tracker](../adoption-kit/usage-tracker.md) does that, separately, so that heavy use is never read as value.
- **It does not monitor the AI system.** Technical and operational measures for a running system belong in a scorecard such as the one in the [AI Observability Toolkit](https://github.com/luispsalas/ai-observability-toolkit/tree/main/business-goals). This record holds the business measures that decide whether the use case is worth keeping.

**Where it sits:** the [needs assessment](needs-assessment.md) records how the work performs today, and the [intake canvas](intake-canvas.md) records each idea's expected value. This record starts when an idea is accepted for a pilot and stays open until the use case is kept, changed or stopped. Decisions are made by the process owner, as the [operating model](../governance/operating-model.md) sets out, and each one goes in the decision log.

## The value record

Fill in one per use case. Every field above *During and after the pilot* is settled before the pilot starts and does not change afterwards without a logged decision.

| Field | What to write |
|---|---|
| **Use case and owner** | The task, and the process owner who will decide on it |
| **Goal it serves** | The one organizational goal this should move, in a sentence |
| **Measures** | One or two, chosen with the people who do the work. Prefer a measure of the work itself (time, errors, rework, delay) over an opinion of the tool |
| **How each is measured** | The source (a system, a count, a short survey), the period, and who collects it |
| **Baseline** | Each measure's starting value, labeled *measured*, *reported* or *estimated*, with its dates |
| **Comparison** | What the result will be compared with: the baseline, a group still working the old way, or both |
| **Threshold** | The result that would justify continuing, and the one that would trigger a stop |
| **Review dates** | When results are read, set now |
| *During and after the pilot* | |
| **Results** | Each measure at each review, collected the same way as the baseline |
| **Where the effort went** | See the next section |
| **Confirmed by** | The named person who checked that the gain actually arrived |
| **Decision** | Continue, adjust or stop, with the reason and date |

## Where the effort went

A tool rarely removes work outright. Some of the time it saves is spent checking its output, fixing what it got wrong, or doing work that used to sit somewhere else. A gain that ignores this overstates the value, and the people now carrying the extra work notice long before the report does.

For each claimed gain, write down:

- **Work removed:** what nobody has to do any more.
- **Work moved:** what someone now does instead, such as checking, correcting or handling exceptions, and **who** does it. Include work that moved to another team, to customers, or to nobody, meaning it is simply no longer done.
- **Time absorbed:** time freed up that was quietly filled by other tasks or new expectations. It is not a loss, but it is not a gain toward the goal either.
- **Where the gain lands:** the specific place it should show up (shorter waits, fewer errors, more cases handled), and the person who can confirm it there.

**No landing place and no one to confirm it, no counted gain.** A saving that cannot be pointed to, a few months later, by someone who would know, is a hope.

## Through the stages

| Stage | What goes into the record |
|---|---|
| **Idea accepted** | The goal and a first choice of measures. Copy any starting figures from the needs assessment with their labels |
| **Before the pilot** | Fix the measures, the baseline, the comparison, the thresholds and the review dates. Replace estimates with measured figures where a short count is possible |
| **During the pilot** | Collect results the same way as the baseline. Keep adoption in the usage tracker. Record work moved as it appears, not only at the end |
| **At each review** | Results against the baseline and the comparison, work moved, who confirmed the gain, and the decision |
| **After rollout** | Measure again, the same way, on the wider group, a few months on. Pilot groups are often keener than everyone else, so expect some of the gain to shrink |

Budget time for the groundwork, such as writing definitions, organizing information or training people, and agree when results should start to show. An early dip then reads as part of the plan rather than as failure. [Why governance helps](../literacy/why-governance-helps.md#it-is-how-the-value-shows-up) explains why value often arrives late.

## Reading the result honestly

- **Compare like with like.** Same measure, same method, similar period. A pilot in a quiet month against a baseline from a busy one says nothing.
- **Say how many.** Report counts out of totals (*38 of 1,012*), and name the group: two volunteers are not the whole team.
- **Look at who gained.** The same tool can help some people and slow others. Report differences between groups instead of hiding them in an average.
- **Keep the labels.** A result compared against an *estimated* baseline is an estimate too.
- **Separate value from use.** A tool everyone uses can still leave the work no better. That is a finding, not a failure of the record.

For a formal definition of the change in a business measure and of adoption, see *Business Outcome Lift* and *Adoption Rate* in the AI Observability Toolkit's [metric data](https://github.com/luispsalas/ai-observability-toolkit/blob/main/data/metrics.csv).

## Example: ticket triage

*Illustrative only. The same made-up company as the [needs assessment](needs-assessment.md#example-a-customer-service-and-sales-team), [intake canvas](intake-canvas.md#example-three-ideas-from-a-customer-service-and-sales-team) and [oversight levels](../governance/oversight-levels.md#example-a-customer-service-and-sales-team) examples. Figures those pages already give are reused; the rest are invented to show the record in use.*

| Field | Ticket triage |
|---|---|
| **Use case and owner** | AI sorts incoming support email into category, urgency and queue; owner: the service manager |
| **Goal it serves** | Faster first responses without adding staff |
| **Measures** | 1. Median time to first response. 2. Share of tickets misrouted |
| **How each is measured** | 1. From the CRM's timestamps, weekly. 2. Team lead's count of tickets moved to another queue |
| **Baseline** | 1. 5.2 hours, *measured*, two weeks before the pilot. 2. 171 of 2,960 tickets (5.8%), *measured*, same two weeks |
| **Comparison** | The baseline, and the ten agents not in the pilot over the same four weeks |
| **Threshold** | Continue if the pilot agents' first responses are at least 20% faster than the comparison group's, with misroutes below 5%. Stop if misroutes go above the baseline |
| **Review dates** | End of week 4; then three months after any rollout |
| *During and after the pilot* | |
| **Results (week 4)** | 1. Pilot agents 3.9 hours; comparison group 5.0 hours, about 22% faster. 2. Agents corrected 38 of 1,012 routings (3.8%) |
| **Where the effort went** | Removed: most of the first hour of reading and sorting. Moved: about 20 minutes a day per agent spent checking the sorting (*reported*); the service manager spent two days writing category definitions before the pilot. Absorbed: none noticed yet. Lands in: first-response time |
| **Confirmed by** | The service manager, from the CRM report, not from the agents' impression |
| **Decision** | Continue and roll out to all 12 agents under selective review. Re-measure both figures three months after rollout, the same way. Logged with date and reason |

**What the example shows:** the gain was measured against both the old figures and colleagues working the old way, so a quiet month could not explain it. The record states what the pilot cannot show: two agents are a small group, and they were the first to volunteer. Checking time was counted against the saving instead of being left out, and the category definitions were recorded as groundwork, not as part of the gain.

*Related wiki concepts:* [Value Realization](https://luispsalas.github.io/applied-ai-concepts/concepts/value-realization-ai.html) · [AI Use Case](https://luispsalas.github.io/applied-ai-concepts/concepts/ai-use-case.html)
