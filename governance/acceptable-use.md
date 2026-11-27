# Acceptable use of AI tools: one page

*Part of the [AI Enablement Toolkit](../README.md).*

What data may go into which kind of AI tool, what the output may be relied on for, and when to ask before going ahead. It is written about kinds of data and kinds of use, never about named products, so it still holds when someone finds a new tool next week. It builds on the [Acceptable Use Policy](https://luispsalas.github.io/applied-ai-concepts/concepts/acceptable-use-policy.html) entry of the Applied AI Concepts wiki, which explains why each choice below is made.

> [!IMPORTANT]
> **Not yet tried with a real team.** The data classes, the tables and the example are a starting draft. Adapt them to your organization's own data classes and rules before anyone relies on them.

## What it does not do

- **It is not legal advice.** Privacy law, sector rules and client contracts come first. Where one of them is stricter than this page, it wins.
- **It does not enforce anything.** A written rule only works with a place where it is applied, such as permissions, a single gateway to the approved tools, or a blocked upload ([A policy needs a place to act](../PRINCIPLES.md#a-policy-needs-a-place-to-act)). The [controls in layers](agent-safety-practices.md#controls-in-layers) show where those places are.
- **It does not approve tools.** The [operating model](operating-model.md) gives that decision to the sponsor and gives the data rules on this page to the data owner.
- **It does not cover AI that acts on its own.** An agent that sends, changes or pays needs its own [specification](agent-spec-template.md) and the [agent safety practices](agent-safety-practices.md). This page covers people using AI tools in their own work.

## Two policies always apply

Your organization writes one. The provider of each AI tool writes the other, as a condition of using it, and **changes it when it chooses**, without any change on your side. A use that was allowed when you signed up may not be allowed at renewal, and nothing in your systems will say so.

- **Name one person to track each provider's usage policy**, usually whoever owns the relationship with that provider. They re-read it at renewal and whenever the provider announces a change.
- **Never allow internally what a provider prohibits.** When the two disagree, the stricter rule applies.

## Two kinds of tool

| Kind | What makes it this kind |
|---|---|
| **Approved tool** | The organization has an agreement with the provider that covers how data is handled: whether it is kept, for how long, who can see it, and whether it is used to train models. People sign in with their work account. |
| **Personal or public tool** | Anything without that agreement: a personal account, a free version, a browser extension, a tool a colleague recommended. The organization cannot see or control what happens to the data. |

The approved tools are the rows marked `approved` in the [AI and agent inventory](ai-inventory.md), each with its review date. That list is the only place products are named, so this page never needs updating when a tool is added.

## What data may go in

Every "no" comes with a permitted way to do the work. A rule without one pushes people toward tools nobody can see, which is how [shadow AI](https://luispsalas.github.io/applied-ai-concepts/concepts/shadow-ai.html) starts.

| Data | Approved tool | Personal or public tool | Instead |
|---|---|---|---|
| **Public:** published material, public websites | Yes | Yes | |
| **Internal:** everyday work documents with nothing about clients or identifiable people | Yes | No | Use an approved tool |
| **Confidential:** client material, contracts, finances, unreleased plans, source code | Only once the data owner has cleared this use | No | Ask the data owner; meanwhile, describe the task without the material |
| **Personal data:** anything about identifiable customers, staff or applicants | Only once the data owner has cleared this use, and only the [minimum the task needs](https://luispsalas.github.io/applied-ai-concepts/concepts/data-minimization.html) | No | Remove names and identifiers first, where the task still works without them |
| **Restricted:** passwords, keys, payment cards, ID numbers, health records, legally privileged material | No | No | The data owner names the system that may hold it, if any |

If your organization already classifies its data, use its classes and keep the columns.

## What the output may be relied on for

| Use | Rule |
|---|---|
| Drafts, ideas, summaries for your own work | Yes. You answer for what you do with it. |
| Facts, figures, quotations and sources | Check each one against its source before relying on it ([reviewing AI output](../literacy/reviewing-ai-output.md)). |
| Anything sent outside the organization | A person reads and approves it first. |
| Decisions about a person: hiring, pay, performance, eligibility | Ask first. A person makes the decision, at [full review](oversight-levels.md#the-four-levels), and some laws set further duties. |
| Legal, medical or financial advice to anyone | Ask first. |

## When to ask first

Ask before going ahead when the data or the use is not in the tables above, when a table says to ask, or when a new tool comes along. **Not listed does not mean allowed, and it does not mean forbidden.** It means ask.

- **Whom to ask:** the data owner for questions about data, and the process owner for questions about a use. Name both here, with how quickly they answer.
- **Keep the answers.** Record each one in the [decision log](operating-model.md#3-what-each-review-checks), so the next person with the same question finds it there and the tables grow from real cases.
- **If something went in that should not have**, say so straight away to the data owner, without blame. Early reports are what make a fix possible, and blame teaches people to stay quiet.

## Keeping it current

Review this page when something it describes changes: a tool is approved or dropped, a provider changes its terms, a contract renews, or the decision log shows the same question coming up again. Tell people what changed, in plain words, before it applies to them ([Communicate early and clearly](../PRINCIPLES.md#communicate-early-and-clearly)).

## Example: a customer service and sales team

*Illustrative only. The same made-up company as the [intake canvas](../assessment/intake-canvas.md) and [oversight levels](oversight-levels.md) examples; the people and cases are invented to show the page in use.*

- **A support agent wants a customer complaint rewritten in a calmer tone.** The email names the customer, so it is personal data. A personal chatbot is out. The team's approved assistant is allowed once the data owner has cleared customer emails for drafting, which happened when the ticket-triage pilot began.
- **A sales rep wants a summary of a competitor's public pricing page.** Public data, so any tool will do. The figures go into a proposal, so the rep checks each one against the page first.
- **An account manager wants an AI tool to pick which customers get a discount.** That decides something about customers and moves money, so it goes to the process owner first. The team already has an answer: the intake canvas stopped this idea, and offers are now drafted by AI and approved by a named person at full review.
- **The provider of the approved assistant updates its usage policy.** The person who owns that relationship reads the change, finds nothing that affects the team's uses, and logs the check with its date.

*Related wiki concepts:* [Acceptable Use Policy](https://luispsalas.github.io/applied-ai-concepts/concepts/acceptable-use-policy.html) · [Shadow AI](https://luispsalas.github.io/applied-ai-concepts/concepts/shadow-ai.html) · [Data Minimization](https://luispsalas.github.io/applied-ai-concepts/concepts/data-minimization.html) · [AI Gateway](https://luispsalas.github.io/applied-ai-concepts/concepts/ai-gateway.html) · [Supply Chain Risk](https://luispsalas.github.io/applied-ai-concepts/concepts/supply-chain-risk-ai.html) · [Permission Model](https://luispsalas.github.io/applied-ai-concepts/concepts/permission-model-ai.html)
