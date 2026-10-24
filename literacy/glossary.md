# English–Spanish glossary

*Part of the [AI Enablement Toolkit](../README.md).*

One list of terms for the whole toolkit: the English pages, the Spanish [AI literacy deck](deck/) and the planned English version of the deck all use these names. Each term has its English and Spanish form, a definition short enough to fit on a slide, and a link for reading further, usually to the [Applied AI Concepts](https://luispsalas.github.io/applied-ai-concepts/) wiki.

Terms are grouped by theme, so related ideas sit together. Where English and Spanish usage differ, the **Usage** column says how and which form the toolkit chose.

> [!NOTE]
> **Acronyms keep their English form.** RAG, HITL and XAI are used as they are in both languages, followed by the full English term and a Spanish reference translation.

## How AI works

| English | Español | Definition | Usage | More |
|---|---|---|---|---|
| AI agent | Agente de IA | An AI system that pursues a goal by planning steps, using tools and acting on the results. | | [Wiki](https://luispsalas.github.io/applied-ai-concepts/concepts/ai-agent.html) |
| Context | Contexto | Everything the model reads before it answers: instructions, conversation history, documents and tool results. | | [Wiki](https://luispsalas.github.io/applied-ai-concepts/concepts/context-ai-systems.html) |
| Context framing | Enmarcado de contexto | How information is presented to the model (its order, tone and assumptions), which shapes how the request is read. | One part of what the wiki calls context engineering. | [Wiki](https://luispsalas.github.io/applied-ai-concepts/concepts/context-engineering.html) |
| Context window | Ventana de contexto | The most a model can take in at once, counted in tokens and shared by everything in the context. | | [Wiki](https://luispsalas.github.io/applied-ai-concepts/concepts/context-window.html) |
| Domain | Dominio | The field an AI system works in, which sets its terms, its standards and the cost of an error. | In Spanish, *dominio* can also mean a web domain. | [Wiki](https://luispsalas.github.io/applied-ai-concepts/concepts/domain.html) |
| Grounding | Fundamentación | Tying a model's answers to sources that can be checked, instead of to what it learned in training. | | [Wiki](https://luispsalas.github.io/applied-ai-concepts/concepts/grounding.html) |
| Orchestration | Orquestación | Coordinating models, tools and steps so each runs in the right order and a failed step is handled. | | [Wiki](https://luispsalas.github.io/applied-ai-concepts/concepts/orchestration-ai-systems.html) |
| RAG · Retrieval-augmented generation | RAG · *generación aumentada por recuperación* | Finding the relevant documents first, then having the model answer from them. | The acronym is used in both languages. | [Wiki](https://luispsalas.github.io/applied-ai-concepts/concepts/rag.html) |
| Tokenization | Tokenización | Splitting text into small units, called tokens, before the model processes it. Limits and costs are counted in tokens. | | [Wiki](https://luispsalas.github.io/applied-ai-concepts/concepts/tokenization.html) |

## Where it goes wrong

| English | Español | Definition | Usage | More |
|---|---|---|---|---|
| Automation bias | Sesgo de automatización | Trusting an automated output instead of checking it, especially when it reads fluently and confidently. | | [Wiki](https://luispsalas.github.io/applied-ai-concepts/concepts/automation-bias.html) |
| Bias | Sesgo | Systematic error that unfairly favors or disadvantages some groups, often inherited from the training data. | | [Wiki](https://luispsalas.github.io/applied-ai-concepts/concepts/bias-ai-systems.html) |
| Black box | Caja negra | A system whose inner workings the people using or overseeing it cannot see or interpret. | | [Wiki](https://luispsalas.github.io/applied-ai-concepts/concepts/black-box.html) |
| Data quality | Calidad de datos | How fit data is for its intended use: accurate, complete, consistent and current enough. | | [Wiki](https://luispsalas.github.io/applied-ai-concepts/concepts/data-quality.html) |
| Failure modes | Modos de fallo | The specific, recognizable ways an AI system goes wrong, each with its own cause and fix. | | [Wiki](https://luispsalas.github.io/applied-ai-concepts/concepts/failure-modes-ai-systems.html) |
| Hallucination | Alucinación | Output that is false or invented, presented as fluently and confidently as accurate output. | | [Wiki](https://luispsalas.github.io/applied-ai-concepts/concepts/hallucination.html) |
| Sycophancy | Complacencia | A model telling people what they seem to want to hear instead of what the evidence supports. | *Adulación* also works; the toolkit uses *complacencia*. | [Wiki](https://luispsalas.github.io/applied-ai-concepts/concepts/sycophancy-llms.html) |
| Verification | Verificación | Checking an output against something outside the system that produced it, such as the source, the data or a test. | | [Wiki](https://luispsalas.github.io/applied-ai-concepts/concepts/verification.html) · [Reviewing AI output](reviewing-ai-output.md) |

## Governance

| English | Español | Definition | Usage | More |
|---|---|---|---|---|
| Acceptable use | Uso aceptable | The rules on which AI tools may be used, for what work, and with which data. | | [Wiki](https://luispsalas.github.io/applied-ai-concepts/concepts/acceptable-use-policy.html) |
| Accountability | Responsabilidad proactiva | The ongoing duty of a named person to answer for an AI system's results and show how they were reached. | Everyday Spanish uses *responsabilidad* for both accountability and ownership. *Responsabilidad proactiva* is the term the Spanish text of the GDPR uses for accountability ([Art. 5.2](https://eur-lex.europa.eu/legal-content/ES/TXT/HTML/?uri=CELEX:32016R0679)). *Rendición de cuentas* suggests a one-off audit, so it is not used here. | [Wiki](https://luispsalas.github.io/applied-ai-concepts/concepts/accountability-ai-systems.html) |
| AI alignment | Alineación de la IA | Getting an AI system to do what its developers and users intend, not only what was literally specified. | In organizations, *alineación* also means fit with strategy. Here it has the technical meaning. | [Wiki](https://luispsalas.github.io/applied-ai-concepts/concepts/alignment-ai-systems.html) |
| Compliance | Cumplimiento normativo | Showing that AI use meets the laws, regulations, standards and internal policies that apply to it. | | [Wiki](https://luispsalas.github.io/applied-ai-concepts/concepts/compliance-ai-systems.html) |
| Explainability · XAI | Explicabilidad | Making an AI system's output or logic understandable to the people who rely on it. | XAI (explainable AI) names the research field; the property itself is explainability. | [Wiki](https://luispsalas.github.io/applied-ai-concepts/concepts/explainability-xai.html) |
| Ownership | Responsable asignado | One AI system assigned, in writing, to one named person, never to a team or a committee. | The Spanish names the person who holds ownership. *Propiedad* means property, and *responsabilidad* is kept for accountability. | [Wiki](https://luispsalas.github.io/applied-ai-concepts/concepts/ownership-ai-systems.html) |
| Shadow AI | IA en la sombra | AI use the organization has not approved or assessed, such as work pasted into a personal chatbot. | *IA no autorizada* also works. | [Wiki](https://luispsalas.github.io/applied-ai-concepts/concepts/shadow-ai.html) |

## Oversight and control

| English | Español | Definition | Usage | More |
|---|---|---|---|---|
| Audit trail | Rastro de auditoría | A lasting, ordered record of an AI system's inputs, actions and outputs, so its behavior can be reconstructed. | | [Wiki](https://luispsalas.github.io/applied-ai-concepts/concepts/audit-trail-ai.html) |
| Emergency stop | Parada de emergencia | A tested way to halt an AI system quickly, with named people allowed to trigger it. | | [Principles](../PRINCIPLES.md#know-how-to-stop-and-who-decides) · [Wiki](https://luispsalas.github.io/applied-ai-concepts/concepts/agency-ai-systems.html) |
| Guardrails | Barreras de protección | Controls around a model, such as filters and permission limits, that keep its behavior within set bounds. | | [Wiki](https://luispsalas.github.io/applied-ai-concepts/concepts/guardrails-ai-systems.html) |
| HITL · Human in the loop | HITL · *humano en el bucle* | A person reviews, corrects or approves the AI's work at defined points, at one of the oversight levels. | The acronym is used in both languages. | [Wiki](https://luispsalas.github.io/applied-ai-concepts/concepts/human-in-the-loop.html) |
| Observability | Observabilidad | Being able to see what an AI system is doing in production, from its logs, traces and measurements. | | [Wiki](https://luispsalas.github.io/applied-ai-concepts/concepts/observability.html) |
| Oversight levels | Niveles de supervisión | How much human review a task gets: full review, selective review, human on the loop, or human-initiated. | The four levels are the wiki's. The toolkit's own page on choosing a level is planned. | [Wiki](https://luispsalas.github.io/applied-ai-concepts/concepts/human-in-the-loop.html) |

## Adoption and value

| English | Español | Definition | Usage | More |
|---|---|---|---|---|
| Adoption | Adopción | Whether people actually use an AI tool in their work. It is measured separately from the value it brings. | | [Adoption review kit](../adoption-kit/) |
| Baseline | Línea base | How a task performs before anything changes, recorded so later results have something to be compared with. | | [Needs assessment](../assessment/needs-assessment.md) · [Wiki](https://luispsalas.github.io/applied-ai-concepts/concepts/value-realization-ai.html) |
| Continuous feedback | Retroalimentación continua | A loop that turns evidence from use into decisions and fixes, with an owner for each step. | | [Wiki](https://luispsalas.github.io/applied-ai-concepts/concepts/continuous-feedback-improvement.html) |
| Decision log | Registro de decisiones | A dated list of each decision about an AI system, with who made it and why. | | [Operating model](../governance/operating-model.md) |
| n of N | n de N | Reporting a result as a count out of a total, such as 3 of 12 people, not a bare percentage. | | [Principles](../PRINCIPLES.md#say-what-you-know-and-how-you-know-it) |
| Pilot | Piloto | A limited, time-boxed trial with a few users, a baseline, and agreed criteria for continuing or stopping. | | [Operating model](../governance/operating-model.md) |
| Process owner | Responsable del proceso | The person responsible for the work an AI tool changes, who decides whether a pilot goes ahead. | *Dueño del proceso* also works. The process owner answers for the work; the *responsable asignado* answers for an AI system. | [Operating model](../governance/operating-model.md) |
| Use case | Caso de uso | A specific task an AI system would do for specific people, with a result that can be measured. | | [Intake canvas](../assessment/intake-canvas.md) · [Wiki](https://luispsalas.github.io/applied-ai-concepts/concepts/ai-use-case.html) |

## Changes from the deck's first glossary

The deck's glossary slide listed 24 of these terms. When the deck is next updated, it takes these changes from this page:

- **Ownership** is *responsable asignado* (was *propiedad / responsabilidad*), and **accountability** is *responsabilidad proactiva* (was *responsabilidad*), so the two no longer share a name.
- **Alignment** is *alineación de la IA* and has its technical meaning. The deck used the organizational one.
- **Explainability** is the English term, with XAI as its acronym. The deck labeled it XAI only.
- **RAG** and **HITL** carry their full English terms and a Spanish reference translation.
- **Hallucination** is *alucinación* (was *alucinación de IA*).
- **Human in the loop** now points to the four oversight levels instead of describing approval before every action.
- **Fourteen terms are new**, all used by the toolkit's pages. They include *adoption*, *baseline*, *oversight levels* and *n of N*.
