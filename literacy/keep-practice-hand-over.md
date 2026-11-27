# Keep, practice or hand over: a skills map for AI

*Part of the [AI Enablement Toolkit](../README.md).*

A team exercise for deciding, skill by skill, what people keep doing themselves, what they keep practicing while AI does most of it, and what they hand over to AI. Without it, skills fade by default. The Applied AI Concepts wiki puts the alternative plainly: *"Decide explicitly which skills may atrophy"* ([Cognitive Offloading & Deskilling](https://luispsalas.github.io/applied-ai-concepts/concepts/cognitive-offloading-deskilling.html)). The map is revisited at each model release, and it ends with the questions to answer before AI takes over a whole role.

> [!IMPORTANT]
> **Not yet tried with a real team.** The columns, the questions and the example are a starting draft. Adapt them before relying on them.

## What it does not do

- **It does not rest on long-term evidence.** That relying on AI can erode the skill needed to check it is well argued, but the wiki notes there is no long-term study of AI-specific deskilling yet. Treat the map as a precaution you can revise, not as a measured result.
- **It does not assess people.** It maps the skills the work depends on, not how good anyone is at them. It is not a performance review or a hiring tool.
- **It does not set how much review a task gets.** The [oversight levels](../governance/oversight-levels.md) page does that. This map decides whether people can still do the review.
- **It does not decide staffing.** That decision belongs to the sponsor, with HR consulted ([operating model](../governance/operating-model.md)). The section *Before you cut* lists what to establish first.

## The three columns

| Column | What it means | What belongs here | To move a skill here |
|---|---|---|---|
| **Keep** | People do it themselves. AI may help, but does not do it. | Any skill needed to check the AI's output. Decisions someone must answer for. Work where the relationship is the point. | Nothing: this is where every skill starts. |
| **Practice** | AI does most of it. People still do some of it on purpose, so they can check it and take over when needed. | Skills the team must be able to fall back on, or that keep a reviewer's judgment sharp. | Say how and how often: the [judgment drill](reviewing-ai-output.md#the-judgment-drill), a sample done by hand each month, a rotation. |
| **Hand over** | AI does it. People check it at the task's oversight level, with no deliberate practice. | Work where errors are cheap, quick to notice and easy to undo, and the skill is not needed to check anything else. | A measured record on real work, and a reviewer who can tell right from wrong (see below). |

**The trap to look for:** the skill needed to check an AI output is often the skill being handed over. If drafting goes to AI, the ability to tell a good draft from a bad one has to stay in Keep or Practice, or the review becomes a signature.

## Running the exercise

Plan about an hour with the people who do the work. They know which skills the work really depends on.

1. **List the skills** the work depends on, in the team's own words. Start from tasks ("route a ticket", "explain a refund") and name the skill behind each.
2. **Ask four questions of each skill:**

   | Question | If the answer is no |
   |---|---|
   | Can someone on the team tell a right AI output from a wrong one for this skill? | It cannot be handed over. Keep it, or narrow the task until someone can. |
   | Is there a measured record of the AI doing it on real work? | Not Hand over yet. Practice at most. |
   | If the tool were gone for a week, could the team still do the work? | Practice at least, so someone can. |
   | Can the AI's output be checked without this skill? | Keep or Practice it, because the review depends on it. |

3. **Place each skill** in a column, with the reason, the evidence and the date. The process owner records the map and the decisions in the operating model's decision log.
4. **For each Practice skill**, name the practice, how often it happens, and who keeps track of it.

## Moving between columns

- **Toward Hand over, only on evidence:** a measured record at the task's current oversight level, on real work, with the sample size stated, and reviewers who pass the judgment drill.
- **Back toward Keep** when the model behind the tool changes (a [release briefing](../rollout/office-hours-and-release-briefings.md) is the signal), when error rates rise, or when the people who could check the work leave.
- **Revisit the whole map** at each model release and whenever the team changes. A map nobody has looked at since the last release describes a different tool.

## Before you cut

Sometimes handing skills to AI means a role changes or goes. That is a staffing decision, and the [operating model](../governance/operating-model.md#1-roles-and-decision-rights) gives it to the **sponsor**, with HR and the process owner consulted. Before it is taken, six questions need an answer. Three are answered elsewhere in the toolkit:

| Question | Where it is answered |
|---|---|
| Who will catch the AI's errors, and can they tell right from wrong? | [Oversight levels](../governance/oversight-levels.md#choosing-a-level) and *Is the review real?* on the same page |
| What does the change really cost, including checking, fixing and work moved to others? | [Value check](../assessment/value-check.md#where-the-effort-went) |
| Which expertise stays, and how is it kept sharp? | This map's Keep and Practice columns, and [Protect judgment](../PRINCIPLES.md#protect-judgment) |

The other three are specific to cutting a role:

- **What can the organization no longer do itself?** List the capabilities that leave with the role, not only the hours. A team that no longer has anyone who knows how a process works cannot judge a vendor's fix for it.
- **What happens when the tool is down, wrong for a week, or withdrawn by its provider?** Name who does the work then, and how fast they can start.
- **How would you rebuild?** If the decision proves wrong, how long would it take to hire or train someone to do the work again, and at what cost? The harder a decision is to undo, the stronger the evidence it needs.

If any answer is "nobody" or "we do not know", the decision is not ready.

## Example: a customer service and sales team

*Illustrative only. The same made-up company as the [intake canvas](../assessment/intake-canvas.md), [oversight levels](../governance/oversight-levels.md) and [acceptable-use](../governance/acceptable-use.md) examples; the skills and decisions are invented to show the map in use.*

The support team mapped its skills after ticket triage moved to selective review and the reply assistant reached regular use:

| Skill | Column | Why |
|---|---|---|
| Routing each ticket to a queue | Hand over | Triage corrected 38 of 1,012 routings in the pilot, below the agreed threshold, and is now checked at selective review. |
| Knowing the categories and what belongs in each | Keep | Selective review depends on it: an agent who cannot tell a misroute cannot catch one. |
| Drafting routine replies | Practice | The assistant drafts most of them. Each agent writes a few by hand every month, so the team can still reply when the tool is down. |
| Knowing the current refund and return policy | Keep | Agents caught drafts quoting an outdated refund window because they knew the policy. |
| Replying to complaints | Keep | The relationship is the point, and the team chose to keep these personal. |

**A proposal to cut.** With routing handed over, a manager proposed reducing the support team by two. The sponsor asked the six questions. The first three had answers: the agents who check triage stay, the [value check](../assessment/value-check.md#example-ticket-triage) showed about 20 minutes a day per agent had moved to checking the sorting, and the map named what stays sharp. The last three did not: nobody had planned how the team would route tickets in an outage at the current volume, or how long it would take to bring the skill back. The sponsor logged the decision as *not ready* and asked for both answers by the next review.

*Related wiki concepts:* [Cognitive Offloading & Deskilling](https://luispsalas.github.io/applied-ai-concepts/concepts/cognitive-offloading-deskilling.html) · [Tacit Knowledge](https://luispsalas.github.io/applied-ai-concepts/concepts/tacit-knowledge.html) · [Automation Bias](https://luispsalas.github.io/applied-ai-concepts/concepts/automation-bias.html) · [Human Responsibility in AI Use](https://luispsalas.github.io/applied-ai-concepts/concepts/human-responsibility-in-ai-use.html)
