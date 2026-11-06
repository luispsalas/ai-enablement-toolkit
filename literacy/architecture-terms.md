# AI and data architecture terms for business

*Part of the [AI Enablement Toolkit](../README.md).*

Short explanations of the architecture, data, development and organization terms that come up when a business works with technical teams or vendors on AI. Each entry says what the thing is, what it is for, and, where it helps, what it is often confused with. The aim is to help readers follow the conversation and ask better questions.

## What it does not do

- **It is not a technical reference.** Each entry is one paragraph. Where the [Applied AI Concepts](https://luispsalas.github.io/applied-ai-concepts/) wiki has a full entry, the term links to it.
- **It does not repeat the toolkit's own vocabulary.** Terms the toolkit's pages use, such as RAG, grounding, orchestration, guardrails and observability, are in the [English–Spanish glossary](glossary.md). Each term lives in one of the two pages only.
- **It does not recommend products.** Entries describe ideas and name no brands, except where a vendor's name for an idea is now in general use; then the entry says so in a clause.
- **It is in English only for now.**

## How terms are chosen

A term is added when all of these hold:

1. **A business reader meets it** in vendor pitches, architecture reviews, proposals or project plans, and understanding it changes what they decide or ask.
2. **It names a concept, not a product.** Vendor-named ideas in general use are included, with their origin noted.
3. **Its meaning has settled.** Terms still being argued over wait.
4. **It fits in one paragraph** without relying on other undefined terms. Model internals and mathematics are left out.
5. **It is not already in the toolkit glossary.**

## Data foundations

**Structured and unstructured data.** Structured data sits in fixed fields, like a spreadsheet or a database table: names, amounts, dates. Unstructured data is everything else, such as emails, documents, call recordings and images. Most of an organization's knowledge is unstructured, which is why language models matter: they can work with text that traditional reporting tools could not use.

**Metadata.** Data that describes other data: who created a file, when, what a column means, how sensitive a record is, who owns it. AI systems rely on metadata to find and filter information, and they trust it without checking. Wrong or missing metadata is a common, quiet reason an AI tool gives poor answers. [Wiki](https://luispsalas.github.io/applied-ai-concepts/concepts/metadata.html)

**Data pipeline (ETL and ELT).** The automated steps that move data from where it is created to where it is used. ETL extracts, transforms (cleans and reshapes) and then loads the data into its destination; ELT loads it first and transforms it there. For a business reader, the point is that data reaching a report or an AI tool has usually passed through several steps, and any of them can change it.

**Data warehouse.** A central store of cleaned, structured data organized for reporting and analysis. Data is shaped to a fixed design before it goes in, which makes it reliable and fast to query but slower to change. *Often confused with* a data lake, which accepts data in any form.

**Star schema.** A common way of designing tables in a data warehouse for reporting. A central *fact* table holds the events being measured, such as each sale with its amount, and links to surrounding *dimension* tables that describe them: customer, product, store, date. Drawn out, it looks like a star. It makes reports simple and fast, and it is often what an AI tool that writes its own queries is reading, so clear dimension names and definitions matter.

**Data lake.** A large, low-cost store that holds data in its original form, structured or not, until someone needs it. It is flexible, but without ownership and descriptions it becomes hard to find anything in or to trust, which practitioners call a data swamp.

**Lakehouse.** An approach that keeps data in low-cost lake storage while adding warehouse features on top: tables, consistent updates, access controls. The aim is one place for both analytics and AI work instead of copying data between a lake and a warehouse. Databricks uses the term for its own platform.

**Medallion architecture.** A way of organizing data in layers by how refined it is. *Bronze* holds raw data as it arrived, *silver* holds cleaned and matched data, and *gold* holds business-ready tables for reports and AI tools. It makes clear which data can be trusted for which use. Databricks documents the pattern as part of its lakehouse approach.

**Data catalog.** A searchable inventory of an organization's data: what exists, where it is, what it means, who owns it and how it may be used. It answers the question every AI project starts with, which is whether the data it needs exists and can be used.

**Data lineage.** The record of where data came from and every step that changed it on the way. When a figure in a report or an AI answer looks wrong, lineage is how a team traces it back to its source. [Wiki](https://luispsalas.github.io/applied-ai-concepts/concepts/data-provenance-lineage.html)

## Knowledge and meaning

**Taxonomy.** A classification of things into categories and subcategories, such as product lines or ticket types. It is the simplest way to give information a shared structure. *Often confused with* an ontology, which also describes how things relate, not only how they are grouped.

**Ontology.** A formal description of the kinds of things an organization deals with and how they may relate: a customer *holds* a policy, a policy *covers* an asset. It sets what a system can represent at all, so anything left out of it cannot be recorded later. [Wiki](https://luispsalas.github.io/applied-ai-concepts/concepts/ontology.html)

**Knowledge graph.** A network of real facts connected by their relationships, usually following an ontology: this customer holds these three policies, which cover these assets. Because each connection is explicit, people can inspect why a system reached an answer. *Often confused with* the ontology itself, which is the design; the graph is the data that follows it. [Wiki](https://luispsalas.github.io/applied-ai-concepts/concepts/knowledge-graphs.html)

**Semantic layer.** A shared set of business definitions placed between the data and the tools that use it, so that *revenue* or *active customer* is calculated the same way in every report and AI tool. Without one, each dashboard can define the same measure differently, and AI tools that write their own queries make the problem worse.

**Knowledge base.** The collection of documents and records an AI tool can look things up in when answering. The quality of its answers depends on how complete, current and well organized that collection is. [Wiki](https://luispsalas.github.io/applied-ai-concepts/concepts/knowledge-base.html)

**Embeddings.** A way of turning text, or images, into lists of numbers so that items with similar meanings end up close together. They are what lets a computer find a document about *cancelling a contract* when someone searches for *ending my subscription*. [Wiki](https://luispsalas.github.io/applied-ai-concepts/concepts/embeddings.html)

**Vector database.** A database built to store embeddings and quickly find the ones closest to a query. It is the usual storage behind semantic search and RAG systems. *Often confused with* a knowledge graph, which stores explicit facts and the links between them.

**Semantic search engine.** Search that matches by meaning rather than by exact words, using embeddings. It finds relevant material phrased differently from the question, but it can also return passages that sound related and say the opposite, so many systems combine it with ordinary keyword search. *Often confused with* keyword search, which only finds the words typed.

## AI models and patterns

**Large language model (LLM).** A model trained on very large amounts of text to predict and produce language. It powers chat assistants, drafting tools and most AI agents. It produces fluent text whether or not the content is correct, which is why its output needs checking. [Wiki](https://luispsalas.github.io/applied-ai-concepts/concepts/large-language-models.html)

**Small language model.** A language model small enough to run cheaply, or on an organization's own hardware or devices. It suits narrow, well-defined tasks and data that must not leave the organization, with less general ability than the largest models. [Wiki](https://luispsalas.github.io/applied-ai-concepts/concepts/small-language-models.html)

**Prompt engineering.** Writing the instructions given to a model so that it produces the result needed: the task, the context, the format and examples. It is the cheapest way to change what a model does and usually the first one to try. [Wiki](https://luispsalas.github.io/applied-ai-concepts/concepts/prompt-engineering.html)

**Fine-tuning.** Further training of an existing model on an organization's own examples, to change its style, format or behavior on a specific task. *Often confused with* RAG: fine-tuning changes how the model behaves, while RAG gives it facts at the moment it answers. For keeping facts current, RAG is usually the better fit. [Wiki](https://luispsalas.github.io/applied-ai-concepts/concepts/fine-tuning.html)

**Tool use.** A model's ability to call other software, such as a search, a database query or an action in a business system, instead of only producing text. It is what turns a chat assistant into something that can act, which is also why the permissions given to those tools matter. Also called function calling. [Wiki](https://luispsalas.github.io/applied-ai-concepts/concepts/tool-use.html)

**Model Context Protocol (MCP).** An open standard for connecting AI tools to data sources and business systems, so that one connector can work with many AI applications. Anthropic introduced it as an open-source standard in 2024. For a business, each connection is also a new access path that needs an owner and limits.

**Multi-agent system.** Several AI agents, each with its own role, working on one task and passing work between them, for example one that researches, one that drafts and one that checks. It can handle larger tasks, and it adds more places for errors to start and spread. [Wiki](https://luispsalas.github.io/applied-ai-concepts/concepts/multi-agent-systems.html)

**AI gateway.** A single control point between an organization's applications and the AI models they use. It routes requests, applies access rules, records usage and enforces spending limits. It gives one place to see and govern AI use instead of one per application. [Wiki](https://luispsalas.github.io/applied-ai-concepts/concepts/ai-gateway.html)

## Development and operations

**API (application programming interface).** The defined way one piece of software asks another for data or actions. AI tools reach business systems through APIs, so whether a system has one, and what it allows, often decides what an AI project can do.

**Proof of concept.** A small, short test that shows something can work technically, usually on sample data and without real users. *Often confused with* a [pilot](glossary.md#adoption-and-value), which tests whether it works for real people on real work. A successful proof of concept says little about value.

**Inference.** Running a trained model to get an answer. Each request costs computing time, and providers usually charge by the amount of text processed, so inference is where the running cost of an AI tool comes from. [Wiki](https://luispsalas.github.io/applied-ai-concepts/concepts/inference.html)

**Evaluation (evals).** Testing an AI system's output on a fixed set of examples with known good answers, before launch and after every change. It is how a team knows whether a new model, prompt or data source made things better or worse, without relying on impressions. [Wiki](https://luispsalas.github.io/applied-ai-concepts/concepts/evaluation.html)

**Model drift.** A gradual change in how well an AI system performs, because the data it sees has changed or the model itself has been updated by its provider. Nothing breaks visibly, so drift is found only by measuring regularly. [Wiki](https://luispsalas.github.io/applied-ai-concepts/concepts/model-data-drift.html)

**MLOps and LLMOps.** The practices and tools for running AI models reliably once they are in use: versioning, testing, deployment, monitoring and rollback. LLMOps is the same discipline adapted to language models, adding prompts and evaluation sets to what is managed. It is the difference between a working demo and a service people can depend on.

## Organization

**Center of excellence.** A small central team that sets standards, shares methods and tools, and supports other teams using AI. *Often confused with* a team that does all the AI work itself, which tends to become a bottleneck.

**Data owner and data steward.** The data owner is the person accountable for a set of data and decides who may use it and for what. The data steward looks after it day to day: its definitions, quality and documentation. AI projects need both to be named before they use the data.

**Data mesh.** An approach in which each business area owns and publishes its data as a product for others to use, following shared standards and a common platform, instead of one central team managing all data. It spreads responsibility to those who know the data best, and it depends on those standards being followed.

**RACI matrix.** A table that sets out, for each task or decision, who is Responsible for doing it, who is Accountable for the result, who is Consulted and who is Informed. It is a quick way to make AI ownership and approvals explicit. [Wiki](https://luispsalas.github.io/applied-ai-concepts/concepts/raci.html)
