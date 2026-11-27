# AI and agent inventory

*Part of the [AI Enablement Toolkit](../README.md).*

One row per AI system or agent the organization uses, is piloting, has retired, or has found in use without approval. Each row names the owner, the data the system touches, how much human review it gets and where its other records are. It is the index that ties those records together, and the one place the list of approved tools lives. The NIST AI Risk Management Framework (AI RMF 1.0, GOVERN 1.6) asks for exactly this: *"Mechanisms are in place to inventory AI systems and are resourced according to organizational risk priorities"* ([NIST AI 100-1](https://doi.org/10.6028/NIST.AI.100-1)).

The rows go in [`ai-inventory.csv`](ai-inventory.csv). Copy it, fill it in, and check it with [`tools/check_lists.py`](../tools/check_lists.py), which refuses a row that breaks the rules below.

> [!IMPORTANT]
> **Not yet tried with a real team.** The columns, the fixed lists and the example are a starting draft. Adapt them before relying on them, and change the check script with the lists.

## What it does not do

- **It does not find systems by itself.** Rows come from people: approvals, pilots, procurement, admin consoles, and the interviews in the [adoption review kit](../adoption-kit/), which ask what people actually use.
- **It does not replace the detailed records.** An agent keeps its [specification](agent-spec-template.md), and the legal and regulatory duties that apply to each system belong in an obligation register kept by legal or compliance. The inventory points to them.
- **It does not judge compliance.** The rules check that each record is complete and consistent. None of them rejects a row because it describes a problem: a found tool that holds personal data is exactly what the inventory must be able to show.

## Who keeps it

Enablement keeps the file, and each row's owner keeps their row current. Each review in the [operating model](operating-model.md#3-what-each-review-checks) looks at what was found, added or retired since the last one, and at rows past their review date.

Add or change a row when:

- a tool or agent is approved, starts a pilot, or is retired;
- someone finds a tool in use that nobody approved (record it as `found`, without blame: see the interview guide's question 13);
- a system gains a connection to another system, its provider changes its terms, or the model behind it changes.

## Columns

| Column | What goes in it |
|---|---|
| `system_id` | `A01`, `A02`… in order, never reused |
| `system` | The name people use for it |
| `purpose` | What it does, in one plain sentence |
| `kind` | `chat tool`, `built-in assistant` (inside another product), `agent` (acts on its own) or `automation` (runs a fixed task without a person starting it) |
| `provider` | Who supplies it, or `unknown` for a found tool |
| `owner` | The named person accountable for it, never a team. Empty only for a `found` tool |
| `team` | The teams that use it, at role level |
| `status` | One of the four values below |
| `data_classes` | The classes it touches, from the [acceptable-use one-pager](acceptable-use.md#what-data-may-go-in): `public`, `internal`, `confidential`, `personal`, `restricted`, separated by spaces |
| `oversight_level` | `full review`, `selective review`, `human on the loop` or `human-initiated`, from [oversight levels](oversight-levels.md). Required for an agent or automation in pilot or approved. Empty for a tool a person uses directly, who then checks its output |
| `connections` | Other systems it can read from or write to, with which (`CRM (writes draft offers)`) |
| `spec_ref` | Its agent specification. Required for an agent in pilot or approved |
| `obligations_ref` | Its entry in the obligation register, if there is one |
| `approved_on` | Date it was approved, `YYYY-MM-DD`. Required when the status is `approved` |
| `review_date` | When to look at the row again, `YYYY-MM-DD`. Required unless the system is retired |
| `retirement_criteria` | What would make you stop using it. Required for pilot and approved, written while nobody has a stake in keeping it |
| `synthetic` | `no` for real systems. `yes` only for example rows, which must never be mixed into a real file |

## Status values (a fixed list)

| Status | Meaning |
|---|---|
| `found` | In use, but nobody approved it. The row records what is known; the next step is to approve it, offer an approved alternative, or stop it |
| `pilot` | In a time-boxed trial with stop rules, as in the operating model's cycle |
| `approved` | Approved for use. **The rows with this status are the approved-tool list** the acceptable-use one-pager refers to |
| `retired` | No longer in use. Keep the row, with the reason in `retirement_criteria`, so the history stays readable |

## The rules

The check script applies these to every row, and each one is tested: it must catch a planted error, and must miss it when switched off.

| Rule | What it checks |
|---|---|
| I1 | `system_id` is `A` followed by digits |
| I2 | `kind` is one of the four kinds |
| I3 | `status` is one of the four statuses |
| I4 | `data_classes` lists one or more of the five classes |
| I5 | `oversight_level` is one of the four levels or empty, and is set for an agent or automation in pilot or approved |
| I6 | `owner` is set unless the status is `found` |
| I7 | `approved_on` is a date, and is set when the status is `approved` |
| I8 | `review_date` is a date, and is set unless the status is `retired` |
| I9 | An agent in pilot or approved has a `spec_ref` |
| I10 | A system in pilot or approved has `retirement_criteria` |
| I11 | `synthetic` is `yes` or `no` |
| I12 | Each `system_id` appears once in the file |
| M1 | A file holds either real rows or synthetic rows, never both |

## Retiring a system

Write the retirement criteria before a system goes into use, when the decision is easy to make honestly. When one is met, the owner proposes retirement and the decision goes in the operating model's decision log. Retiring means more than switching it off: tell the people who use it, decide what happens to the data it holds and the records it wrote, and remove its access to other systems. Then mark the row `retired` and keep it.

## Example: a customer service and sales team

*Illustrative only. The same made-up company as the other pages' examples; the rows are in [`examples/synthetic-rollout/ai-inventory.csv`](../examples/synthetic-rollout/ai-inventory.csv), marked synthetic, and pass the checks.*

| ID | System | Kind | Owner | Status | Data | Oversight |
|---|---|---|---|---|---|---|
| A01 | reply assistant | built-in assistant | service manager | approved | internal, personal | a person uses it directly |
| A02 | call summary assistant | built-in assistant | sales lead | approved | internal, confidential, personal | a person uses it directly |
| A03 | ticket triage | automation | service manager | approved | internal, personal | selective review |
| A04 | retention offer drafts | agent | account management lead | pilot | internal, personal | full review |
| A05 | free chat assistant | chat tool | none yet | found | personal | none |

**What the example shows:** the approved-tool list is rows A01 to A03, so the acceptable-use one-pager needs no list of its own. A05 came from interviews: some agents reword replies with a free chat assistant on personal accounts. Recording it as `found` makes the problem visible without naming anyone, and its review date puts a decision on the next review's agenda. A04 is an agent in pilot, so it points to its specification and has retirement criteria taken from its stop rules. In a real file, each owner is a named person; the example uses roles.

*Related wiki concepts:* [Shadow AI](https://luispsalas.github.io/applied-ai-concepts/concepts/shadow-ai.html) · [Accountability](https://luispsalas.github.io/applied-ai-concepts/concepts/accountability-ai-systems.html) · [Ownership](https://luispsalas.github.io/applied-ai-concepts/concepts/ownership-ai-systems.html) · [Governance & Observability Notes](https://luispsalas.github.io/applied-ai-concepts/notes/governance-and-observability.html)
