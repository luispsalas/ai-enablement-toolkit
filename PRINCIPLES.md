# Principles

*Part of the [AI Enablement Toolkit](README.md).*

The working principles behind this toolkit: how it approaches helping an organization adopt AI tools, govern them and get value from them. Each principle says what it means in practice and which part of the toolkit puts it to work. Where the [Applied AI Concepts](https://luispsalas.github.io/applied-ai-concepts/) wiki already argues a principle in depth, this page links it rather than repeating it.

> [!NOTE]
> **These are working principles, written while building the toolkit.** They will change as the toolkit is used with real teams, and the changes will be recorded here.

## Find the cause before choosing the fix

When people stop using an AI tool, the cause can be the tool itself, a workflow it does not fit, missing training, or old habits. Each needs a different person to fix it, so naming the cause matters more than describing the symptom. More training will not fix a broken tool, and a better tool will not change a habit.

*In the toolkit:* the [adoption review kit](adoption-kit/) diagnoses each stall as tool, workflow, training or habit, and sends it to the owner who can act.

## Tell broken from confusing

A tool people stop using may be badly built, badly implemented or badly explained, and each needs a different fix. Before calling something a defect, reproduce it. If it fails for you too, it is a design or build problem with steps a developer can follow. If it works for you, the person did something different or the tool misled them: the gap is in how it was implemented or communicated, which makes it a training, workflow or design question. Finding where the gap sits keeps effort on the fix that will actually change what people do.

*In the toolkit:* the kit's diagnosis refuses a tool finding that was not reproduced, and the [tool evaluation scorecard](README.md#governance-one-pagers) will apply the same test before buying.

## Say what you know, and how you know it

Report adoption as *n of N*, never as a bare percentage, and say where every number came from: an interview, a self-report, a usage log or an estimate. Put the limits at the top, where they change how the rest is read. A small, honest result is more useful than a large claim nobody can check.

*In the toolkit:* the README and each template open with their limits, and the kit's first trial states its sample of one before anything else.

## Authorize actions, not only outputs

When an AI system only drafts, a person reviews the draft. When it acts (sends, pays, publishes, deletes), the review comes too late. As the wiki puts it, governance *"must shift from output review to action authorization"* ([AI Governance](https://luispsalas.github.io/applied-ai-concepts/concepts/ai-governance.html)). Decide what the system may do on its own, what needs approval, and what is never allowed, before it runs.

*In the toolkit:* the [agent specification template](governance/agent-spec-template.md) records those decisions for each agent, and the planned oversight levels page will set how much review each kind of task needs.

## Keep responsibility with named people

*"Automation does not transfer responsibility. It concentrates it."* ([Human Responsibility in AI Use](https://luispsalas.github.io/applied-ai-concepts/concepts/human-responsibility-in-ai-use.html)). Every decision an AI system influences needs one named owner who can explain it, not a team or a committee, and that owner needs access to the evidence to do so.

*In the toolkit:* the [operating model](governance/operating-model.md) gives each decision one owner and logs every decision taken with its owner and date.

## Protect judgment

AI mistakes rarely look like mistakes: the output is fluent and confident whether or not it is right. The ability to judge AI output is therefore the skill an organization most needs to keep, and it improves with deliberate practice, not with exposure. Check the claims a decision depends on against the source, and choose them by their consequence, never by how suspicious they look.

*In the toolkit:* [reviewing AI output](literacy/reviewing-ai-output.md) lists where errors hide and includes a drill to build the skill.

## Literacy is about behavior

*"AI literacy changes what people do, not just what they know."* ([AI Literacy](https://luispsalas.github.io/applied-ai-concepts/concepts/ai-literacy.html)). Different roles need different depths, and the test of a training program is whether people work differently afterwards, not whether they completed it.

*In the toolkit:* the [literacy deck](literacy/deck/) and the planned training pre/post check, which measures what changed in practice.

## Measure value, do not assume it

Adoption is not value. People can use a tool every day without the work getting any better, so value has to be measured on its own, and the measurement has to start before anything changes. Without a baseline there is nothing to compare against, and every later claim of improvement is a guess.

Measurement belongs at every stage of the work:

- **When an idea is proposed:** record how the task performs today (time, errors, rework, delay) and say whether that was measured, reported or estimated.
- **When a pilot starts:** fix the baseline and the one or two measures that will decide the result, before anyone sees the new numbers.
- **During the pilot:** track adoption separately from value, so heavy use is not mistaken for benefit.
- **After rollout:** measure the same things the same way, on real work, and compare with the baseline.
- **At each review:** report what landed, what did not and why, and tie each result to the goal the organization set for it.

Measure a small number of things well rather than many things loosely, and keep the people doing the work involved in choosing them: they know where the time and errors really are.

*In the toolkit:* the [needs assessment](assessment/needs-assessment.md) records how the work performs today and where each figure came from, the [intake canvas](assessment/intake-canvas.md) records today's cost and expected value, the [usage tracker](adoption-kit/usage-tracker.md) tracks adoption on its own, so it is never read as value, the [leadership brief](adoption-kit/leadership-brief-template.md) reports whether fixes landed, and the planned value check carries a baseline through to the result.

## A policy needs a place to act

Writing down what is allowed does not make it happen. *"A policy is not a control"* ([Acceptable Use Policy](https://luispsalas.github.io/applied-ai-concepts/concepts/acceptable-use-policy.html)): it needs a point where it is enforced, and a permitted way to do the work, or people will find an unofficial one.

*In the toolkit:* the planned acceptable-use one-pager pairs each rule with a sanctioned route.

## Know how to stop, and who decides

Stopping is rarely in one person's hands, so plan for it in three ways.

- **Planned stops.** Where you can, agree before a pilot starts what would end it, while nobody has a stake in continuing.
- **Emergency stops.** Every AI system that acts needs a way to halt it quickly when something goes off the rails: who can trigger it, how fast it takes effect, what happens to work already in progress, and whether anyone has ever tried it. As the wiki warns, look for *"a stop path that exists on paper and has never been exercised"* ([Agency](https://luispsalas.github.io/applied-ai-concepts/concepts/agency-ai-systems.html)).
- **When the decision is not yours.** Make the risk visible instead of carrying it alone: write down what you saw and what you recommend, send it to the person who owns the decision, and record what they decided and when.

*In the toolkit:* the intake canvas's stop check, the stop rules in the [operating model](governance/operating-model.md)'s pilot stage, and the failure paths in the [agent specification template](governance/agent-spec-template.md).

## Keep one current record

Documentation is how an organization knows what is true about its AI systems: what each one does, what it was allowed to do, what changed and who decided. When it is current, people can rely on it, AI tools can work from it, and an auditor can check it. When it is stale, it misleads all three at once, and a procedure nobody updated is worse than none, because someone will follow it. *"Accountability without transparency is a formality"* ([Accountability](https://luispsalas.github.io/applied-ai-concepts/concepts/accountability-ai-systems.html)).

Keep one place for each fact, with an owner, and update it when the thing it describes changes, not on a schedule. Record decisions with their date and reason, so they can be explained later. The same applies to the context an AI tool reads: instructions and documents nobody maintains become wrong answers delivered with confidence.

*In the toolkit:* the operating model's decision log, the agent specification (kept next to the agent's code and change log), the dated feedback pages, and the planned shared context kit. The wiki's [Audit Trail](https://luispsalas.github.io/applied-ai-concepts/concepts/audit-trail-ai.html) entry covers the system side, and its [Governance & Observability Notes](https://luispsalas.github.io/applied-ai-concepts/notes/governance-and-observability.html) the risks of context nobody maintains.

## Communicate early and clearly

Most adoption problems are cheaper to fix the earlier someone hears about them, so make it easy to speak up and quick to get an answer. Tell people what will change for them before it changes, what the AI tool will and will not do, how to check its work, and whom to ask. Then keep talking: share what was learned, what was fixed and what still needs work, so people see their feedback lead somewhere.

Clear communication is also what makes people and AI work well together. Teams that understand what a tool is for, where it is weak and where their own judgment is needed use it with more confidence and fewer surprises, and they are the first to notice when something is going wrong.

*In the toolkit:* the kit's follow-up step closes the loop with the people who raised an issue, the [leadership brief](adoption-kit/leadership-brief-template.md) reports up, and the planned walkthrough, office-hours and change-communication templates cover rollout.
