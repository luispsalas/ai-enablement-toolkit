# Governing AI agents: safety practices from design to use

*Part of the [AI Enablement Toolkit](../README.md).*

Practices to keep at hand when an organization designs, builds, enables or uses an AI agent or an automation that acts on its own: one that reads, decides and then does something, such as sending, changing, buying or deleting, often without a person watching each step. They apply to any vendor's agent, to automation platforms with an AI step, and to agents a team builds itself.

The practices are grouped by the challenge they answer. Each is tagged with the stage where it is put in place: **Design**, **Build**, **Enable** (set up and grant access) or **Use** (run, review and change).

> [!IMPORTANT]
> **Current as of November 2026, and not yet tried with a real team.** Agent tools and the guidance on them change quickly. Treat this page as a starting checklist to adapt, and review it whenever your models, tools or rules change.

## What it does not do

- **It is not legal or compliance advice.** It does not map any regulation or standard. Where one applies to your system, its requirements come first.
- **It does not describe one product.** Where a practice needs a feature, such as a sandbox or a permission rule, use your platform's equivalent.
- **It does not record decisions for a specific agent.** The [agent specification template](agent-spec-template.md) does that, and the [AI oversight levels](oversight-levels.md) page sets how much human review each task gets. This page is the checklist those decisions are made against.

**Where it sits:** an idea passes the [intake canvas](../assessment/intake-canvas.md), the agent is written up with the specification template, its review level comes from the oversight levels page, and the [operating model](operating-model.md) says who approves it. This page covers how to make that agent safe in practice, at every stage.

## Two ideas that run through every practice

**The deciding question is whether a mistake can be undone.** If the agent gets something wrong once, can someone reverse it, and at what cost? Mistakes that can be reversed, such as a draft or a change on a test branch, can be left to the agent's judgment with checks after the fact. Mistakes that cannot be reversed, such as a payment, a deletion, a message to a customer or leaked data, need a rule the agent cannot get around, or a person's approval before they happen.

**Guidance is followed most of the time. Rules are enforced every time.** Instructions and prompts are read and interpreted by the model, which usually follows them. Permissions, blocked actions, isolated environments and required checks are applied by the system around the model, whatever the model decides. Sort every requirement into one of the two.

| Concern | Guidance (the model judges) | Rules (the system enforces) |
|---|---|---|
| What to do | Instructions, task description, examples | Fixed workflow steps, actions only a person can start |
| What it can touch | Asking the agent to stay within scope | Permissions, blocked actions, isolated environments, network limits |
| When it is done | A stated goal, a request for evidence | Automated checks that must pass before the task can close |
| How much it spends | A suggested effort or length | Hard limits on steps, time and money |
| Final say | The agent's own summary | A person's approval, required by the system, for anything irreversible |

## Defined outcomes

An agent working alone cannot ask what was meant. If done is not defined, it will decide for itself, and it may decide differently from the person who asked.

| Practice | Stage |
|---|---|
| Start with the simplest thing that works. Use a fixed workflow when the steps are known, and an agent only when they cannot be known in advance. Add complexity only when it measurably improves results | Design |
| Write down the goal, what counts as done, and what is out of scope, before the agent starts | Design |
| Turn the definition of done into checks a machine can run: a test, a validation rule, an expected output for known cases | Build |
| Add checkpoints along the way, so a wrong approach fails early instead of at the end | Build |
| Have the agent show the evidence of its checks, such as the actual results, instead of only reporting that it passed | Build |
| Record the business result the agent is meant to change, with a baseline, and measure it after rollout (see the [value check](../assessment/value-check.md)) | Design, Use |

## Risk acknowledgment and management

Agents fail in ways that look reasonable to them: they take an action that fits the instructions and is still not what was meant. Saying so plainly, and planning for it, is part of using them well.

| Practice | Stage |
|---|---|
| List what the agent could do wrong, how far each mistake would reach, and whether it could be undone. Do this before granting any access | Design |
| Set the human review level per task by its risk, not per tool, using the [oversight levels](oversight-levels.md) | Design |
| Turn everything that must never happen into an enforced rule, never only an instruction | Build |
| Start with a small scope and few permissions, and widen them only on measured results | Enable |
| Keep a short register of each agent's known risks and limits, with an owner and a review date | Use |
| Tell the people affected what the agent does, what it cannot be trusted with, and how to raise a problem | Use |

## Security

The main new threat is instructions hidden in content the agent reads: an email, a web page, a document or a tool's response can tell the agent to do something else. The danger grows when one agent can read untrusted content, reach private data and send information out, all at once.

| Practice | Stage |
|---|---|
| Give the agent the fewest permissions and tools the task needs, and no standing access it uses only occasionally | Design |
| Treat everything the agent reads from outside as untrusted, and decide what it may do after reading it | Design |
| Avoid combining untrusted input, access to private data and the ability to send data out in one agent. Where that cannot be avoided, require a person's approval for the outbound step | Design |
| Give each agent its own identity and credentials, scoped to its task and set to expire, never a person's account | Enable |
| Keep secrets out of what the model can read. Inject them at the point of use | Enable |
| Run the agent in an isolated environment with network access limited to an approved list, so a compromised step cannot reach further | Enable |
| Check every tool, plugin and connector before adding it, as you would any software supplier | Enable |
| Test the agent against attempts to misuse it before launch and after each significant change | Build, Use |

## Explainability and traceability

When an agent acts on its own, nobody watched it decide. The only way to understand what happened later is what was recorded at the time.

| Practice | Stage |
|---|---|
| Record each consequential action: what triggered it, what the agent was asked, which rule or permission applied, what it did and what resulted | Build |
| Keep records append-only and tamper-evident, and leave out secrets and unnecessary personal data | Build |
| Make the agent's plan and progress visible while it runs, such as a task list or a step log, so a person can follow and step in | Build |
| Have the agent state the reasons and sources behind recommendations a person will act on | Build |
| Be able to answer, for any action, which agent did it, with which version, under which instructions, and who approved it | Use |

## Timeliness

Timeliness has three parts here: stopping an agent in time, acting on information that is still current, and keeping these practices up to date.

| Practice | Stage |
|---|---|
| Set hard limits on steps, run time and spending, so a stuck or looping agent stops on its own | Build |
| Have a tested way to stop the agent quickly, with named people allowed to use it, and agree what happens to work in progress (see [know how to stop, and who decides](../PRINCIPLES.md#know-how-to-stop-and-who-decides)) | Enable |
| Make sure the people asked to approve actions can respond in time. An approval step that is always rushed becomes a formality | Enable |
| Check that the data and documents the agent relies on are current, and show their date where it matters | Build, Use |
| Re-test the agent whenever its model, instructions, tools or data change, since a provider update can change behavior with no visible error | Use |
| Review these practices, the agent's permissions and its risk register on a set schedule, and after any incident | Use |

## Human control and accountability

Removing a person from each step does not remove the need for a person in charge. It moves their job to setting limits, approving what cannot be undone, and answering for results.

| Practice | Stage |
|---|---|
| Name one person who owns each agent and answers for what it does | Design |
| Require a person's approval for irreversible actions, enforced by the system rather than requested in the instructions | Build |
| Make sure approvers can see enough to judge, and can say no without penalty | Enable |
| Watch for approval rates near 100%, a sign that review has become a formality | Use |
| Log every change to an agent's permissions or review level, with its owner, date and reason | Use |

## Privacy and data

Agents can carry information from one task, team or customer into another, and they read far more than a person would.

| Practice | Stage |
|---|---|
| Decide which data the agent may read, which it may write and which it must never see | Design |
| Keep data separate between tasks, teams and customers, with access checked on every request | Enable |
| Minimize what goes into the agent's context and records to what the task needs | Build |
| Follow the organization's acceptable-use rules for what data may go into which tool | Use |

## Cost and resources

An agent that runs unattended spends money unattended. Limits make cost a governed decision instead of a surprise.

| Practice | Stage |
|---|---|
| Set a budget per task and per period, enforced by the platform | Enable |
| Give the agent only the information the task needs, which also keeps it more accurate | Build |
| Track cost per completed task beside the value it produces | Use |

## Change, monitoring and incidents

Agents change when their models, tools or data change, often without any visible error. Problems are found by measuring and watching, rarely by someone noticing.

| Practice | Stage |
|---|---|
| Run the same quality checks on a fixed set of examples before launch and after every change | Build, Use |
| Monitor for actions outside the agent's assigned scope, unusual volumes and repeated failures, and alert a named person | Use |
| When something goes wrong, contain it first, then work out whether the agent acted on its own or was manipulated, since the fix differs | Use |
| Confirm the containment works before restarting the agent | Use |
| Record near misses as well as incidents, and feed what was learned back into rules and checks | Use |

## People and skills

The controls above only work if the people around the agent understand it. Reviewers who trust fluent output catch little.

| Practice | Stage |
|---|---|
| Train the people who approve or review agent work in what its errors look like (see [reviewing AI output](../literacy/reviewing-ai-output.md)) | Enable |
| Make sure the people who once did the task can still judge the agent's work, and can take over if it stops | Use |
| Expand use in steps: one larger task first, then more, watching where the agent stalls or errs | Use |

## Before any agent runs unattended

- **Does it know what done looks like?** A goal, a definition of done, checks it must pass.
- **Can it check its own work?** Automated checks, evidence it must show.
- **What may it touch?** Permissions, an isolated environment, an approved network list.
- **What stops it?** Limits on steps, time and money, and a tested way to halt it.
- **Who signs off?** A named owner, and a person approving anything that cannot be undone.
- **What is recorded?** Its actions, the rules that applied, and who approved what.

## Controls in layers

Each layer covers something the ones before it cannot. The further down the list, the less the safety depends on the model's judgment. Use the lower layers for anything costly to get wrong.

1. **An automated reviewer** checks risky actions before they run. It catches most problems and misses some.
2. **Blocked actions and permissions** apply before any judgment, every time.
3. **A sandbox** limits what a running action can reach, including anything it starts.
4. **An isolated environment** holds no secrets the agent does not need, and limits where data can go.
5. **Independent checks and a person's approval** at the point where work leaves the agent's environment, because that is where actions become permanent.

## Sources

The practices above are drawn from, and written in this toolkit's own words from, these documents. Titles and dates were read on each publisher's page in November 2026.

**Governments and standards bodies**

1. National Institute of Standards and Technology (NIST), [*Artificial Intelligence Risk Management Framework (AI RMF 1.0)*](https://doi.org/10.6028/NIST.AI.100-1), NIST AI 100-1, January 2023.
2. NIST, [*Artificial Intelligence Risk Management Framework: Generative Artificial Intelligence Profile*](https://doi.org/10.6028/NIST.AI.600-1), NIST AI 600-1, July 2024.
3. CISA, Australian Signals Directorate's Australian Cyber Security Centre and partners, [*Careful Adoption of Agentic AI Services*](https://www.cisa.gov/resources-tools/resources/careful-adoption-agentic-ai-services), May 1, 2026 (the CISA page now titles it *Careful Adoption of Agentic SI Services*).
4. NIST, NSA and CISA, [*Key Practices for Incident Readiness and Response in Super Intelligence Training and Evaluation*](https://www.nist.gov/document/keypracticesforincidentreadinessandresponseinsuperintelligence-trainingandevaluation), October 2026.
5. UK National Cyber Security Centre, CISA and partners, [*Guidelines for secure AI system development*](https://www.ncsc.gov.uk/collection/guidelines-secure-ai-system-development), November 27, 2023.
6. European Union, [Regulation (EU) 2024/1689 (Artificial Intelligence Act)](https://eur-lex.europa.eu/eli/reg/2024/1689/oj/eng), Article 12 (record-keeping) and Article 14 (human oversight).
7. ISO/IEC, [*ISO/IEC 42001:2023, AI management systems*](https://www.iso.org/standard/81230.html), 2023.

**Independent security projects and research**

8. OWASP GenAI Security Project, [*Top 10 for LLM Applications, 2025*](https://genai.owasp.org/llm-top-10/), in particular [Prompt Injection](https://genai.owasp.org/llmrisk/llm01-prompt-injection/) and [Excessive Agency](https://genai.owasp.org/llmrisk/llm062025-excessive-agency/).
9. OWASP GenAI Security Project, [*Agentic AI: Threats and Mitigations*](https://genai.owasp.org/resource/agentic-ai-threats-and-mitigations/), February 17, 2025.
10. Shavit, Agarwal, Brundage and others (OpenAI), [*Practices for Governing Agentic AI Systems*](https://cdn.openai.com/papers/practices-for-governing-agentic-ai-systems.pdf), December 2023.
11. Díaz, Kern and Olive (Google), [*Google's Approach for Secure AI Agents*](https://research.google/pubs/an-introduction-to-googles-approach-for-secure-ai-agents/), 2025.

**Agent developer guidance**

12. Anthropic, [*Our framework for developing safe and trustworthy agents*](https://www.anthropic.com/news/our-framework-for-developing-safe-and-trustworthy-agents), August 4, 2025.
13. Anthropic, [*Building effective AI agents*](https://www.anthropic.com/engineering/building-effective-agents), December 19, 2024.
14. Anthropic, [*Writing effective tools for AI agents*](https://www.anthropic.com/engineering/writing-tools-for-agents), September 11, 2025, and [*Effective context engineering for AI agents*](https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents), September 29, 2025.
15. Anthropic, [*How we built Claude Code auto mode*](https://www.anthropic.com/engineering/claude-code-auto-mode), March 25, 2026.
16. Anthropic, Claude Code documentation: [Best practices](https://code.claude.com/docs/en/best-practices), [Permissions](https://code.claude.com/docs/en/permissions), [Sandboxing](https://code.claude.com/docs/en/sandboxing) and [Hooks](https://code.claude.com/docs/en/hooks), read November 18, 2026.
