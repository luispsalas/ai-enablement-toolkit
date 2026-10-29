# AI agent specification: template

*Part of the [AI Enablement Toolkit](../README.md).*

One page that a business owner and a delivery team fill in together before anyone builds an AI agent. It records what the agent is for, what it may touch, what it may decide on its own, and how everyone will know it is working. Copy the template below, fill every section, and keep the page next to the agent's code and change log.

> *"Agentic AI requires a different governance posture. When AI systems take actions rather than producing outputs for human review, the intervention point moves. Governance must shift from output review to action authorization, defining what the system is permitted to do before it does it, not after."* ([AI Governance](https://luispsalas.github.io/applied-ai-concepts/concepts/ai-governance.html), Applied AI Concepts wiki)

> [!IMPORTANT]
> **Not yet tried with a real team.** The template is filled in once below, for a lab built on synthetic data. Until a delivery team has built from it, treat it as a starting draft to adapt.

**How it connects to the rest of the toolkit:** the [operating model](operating-model.md) says who approves the agent and who reviews it. The planned *acceptable-use one-pager* will hold the data rules that section 2 points to. The [use-case intake canvas](../assessment/intake-canvas.md) decides whether the agent is worth building at all; this page starts after that decision. The [AI oversight levels](oversight-levels.md) page sets how much human review each decision gets.

## The template

**Agent:** name · **Business owner:** role · **Built by:** team · **Version and date** · **Status:** draft, pilot or live

### 1. Goal
- **The job:** one sentence on the task, for whom, and how often it comes up.
- **Done well means:** the outcome a user would notice, with a number where one exists.
- **Not for:** the nearby tasks it must not take on.

### 2. Inputs and data
- **What it receives,** and from where.
- **Data it must never see,** following the team's acceptable-use rules, and **where that data is removed** (before the model, never after).
- **What it keeps:** logs, history, retention, and who can read them.

### 3. Tools and permissions
| Tool or system | Read or write | Limits (amount, rate, scope) | Who granted it |
|---|---|---|---|

Grant the least that the job needs, and list anything the platform does by default that was switched off.

### 4. Decisions and handoffs
| Decision | Who makes it | Oversight |
|---|---|---|

**Oversight:** one of the four [AI oversight levels](oversight-levels.md): *full review* of every output before it takes effect · *selective review* of a sample and the cases that trip a rule · *human on the loop*, where a person watches the logs and alerts · *human-initiated*, where the system acts until someone stops it. Any decision involving money, access or a person's record starts at *full review*.

### 5. Failure paths
| Failure | How it is detected | Where it goes | Who sees it |
|---|---|---|---|
| Wrong or malformed output | | | |
| Model slow or unavailable | | | |
| Input that tries to steer the agent | | | |
| A step that fails without an error | | | |

Every path ends somewhere a person will see. A failure that is only logged, where nobody looks, has no path.

### 6. Success metrics
| Metric | Target | How it is measured | Sample and source |
|---|---|---|---|

Name metrics from the [AI Observability Toolkit's metric list](https://github.com/luispsalas/ai-observability-toolkit/blob/main/data/metrics.csv) where one fits, so that definitions and healthy ranges are shared rather than invented again. State the sample size beside every result.

### 7. Before go-live
- Each failure path in section 5 was triggered on purpose and reached its destination.
- Each limit in section 3 was tested by trying to exceed it.
- The business owner has read sections 1, 4 and 6 and agrees with them.
- **Sign-off:** business owner, data owner, and the approver named in the operating model, each with a date.

## Example: a vendor-request triage agent

*A lab on synthetic data, run on one computer and described in its [public write-up](https://luispsalas.github.io/portfolio/workflow-automation/). It is a workflow with one AI step, so it is a modest agent; it shows the template filled in, not a production system.*

**Agent:** vendor-request triage · **Business owner:** a finance operations lead (illustrative) · **Built by:** one builder, AI-assisted · **Status:** lab

1. **Goal.** Sort free-text purchase and reimbursement requests into a category, an urgency and a one-line summary, in about a second each. **Not for:** approving anything.
2. **Inputs and data.** Requests arrive through a form. Emails, phone numbers and ID-like numbers are removed by fixed rules that run locally, before any text reaches the model. If the text seems to mention a person, the request goes to a human and the model receives nothing. The model never sees the amount. Every run writes one log line with redacted text only.
3. **Tools and permissions.** A hosted model that only classifies text, reached only after the privacy gate. The workflow writes one log line per request to a file.
4. **Decisions and handoffs.**

| Decision | Who makes it | Oversight |
|---|---|---|
| Category, urgency, summary | the model | human on the loop: a person reads the log |
| Whether personal data is present | fixed rules, no AI | a suspected name goes to a person |
| Approval of $5,000 or more | a named approver | full review |
| Approval below $5,000 | the same fixed rule, no AI | no approver; logged (the write-up states only the $5,000 threshold) |

5. **Failure paths.** A missing vendor or a non-numeric amount is rejected before any model call. A bad model reply, or the model being unavailable, is logged with a status and a reason, never lost. A request telling the model to mark it approved was flagged, and routing still used the real amount, which the model never sees. *Gap found in the lab:* no alert when something unexpected crashes.
6. **Success metrics** (measured in the lab, small samples):

| Metric | Result | Sample |
|---|---|---|
| M09 Answer Correctness (category) | 9/10 clear-cut, 2/5 ambiguous | 15 requests, labels confirmed by the owner |
| M09 Answer Correctness (urgency) | 14/15 | same 15 requests |
| M27 PII Detection Recall (gate) | 0 of 6 planted cases reached the model with the gate on | 6 synthetic requests |
| M18 Latency (P50/P95/P99) | ~1.2 s per request, about 95% of it the model call | lab runs |
| M13 Prompt Injection Detection Rate | the one injection attempt was flagged | 1 test |
| M36 Error Rate, M37 Human Override Rate, M42 Audit Trail Coverage | not measured yet; every path does write a log line | none |

7. **Before go-live.** Every failure path above was triggered on purpose and logged as intended. Still open before any real use: an independent check for names the rules miss, an alert for unexpected crashes, and approval by named people rather than a shared password.
