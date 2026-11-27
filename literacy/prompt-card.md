# Prompt quick-reference card

*Part of the [AI Enablement Toolkit](../README.md).*

One page to keep beside any AI chat tool: how to ask, and what to do before you rely on the answer. It condenses the prompts section of the [AI literacy deck](deck/) (slides 14 and 15), where the examples are worked through. For one tool and one task, the [walkthrough](../rollout/walkthrough.md) comes with its own card.

## Before you type

- **The model knows only what you tell it.** Unless the tool has memory or saved instructions turned on, every conversation starts from nothing.
- **Put in only the data this tool is allowed.** The [acceptable-use one-pager](../governance/acceptable-use.md) says which data may go into which kind of tool. If the task works without real names or figures, leave them out.

## How to ask

Copy it and fill in only the fields that prevent a misunderstanding. The more sensitive the task, the more explicit the context should be.

```
Context: I work in [area / company / sector]. The goal is [purpose].
Task: [one clear, specific instruction]
Constraints: [length, tone, format, what to leave out]
Expected result: [table, list, paragraphs, draft]
Role (optional): Write as [profile], for [audience].
```

**Why the role comes last.** Telling a model to act as an expert sounds like it should make it more accurate. In a controlled test on six models, it did not: expert personas brought no consistent gain on difficult multiple-choice questions in science, engineering and law, though the authors add that *"personas may serve other purposes (such as altering the tone of outputs)"* ([Basil et al., 2025](https://arxiv.org/abs/2512.05858)). Use the role for tone and audience. Put what accuracy depends on into the task and the constraints.

**Before and after** (from the deck):

| Weak | With context |
|---|---|
| Summarize this meeting. | Summarize this transcript for the leadership team. Include: decisions, owners and next steps with dates. Three sections with headings. Half a page at most. |

## Three habits

1. **Give the context up front.** Do not assume the model knows your organization.
2. **Treat the first answer as a draft.** Ask for changes: shorter, another tone, a different format.
3. **Leave out data the task does not need.** Generic or anonymized examples often work just as well.

## Before you rely on the answer

- **Mark the few facts, figures or sources** that your next step depends on.
- **Check each against its source.** Asking the same AI whether it was right is not a check.
- **Say what you checked** and what you are taking on trust when you pass the work on.

The full routine, and what to do when you cannot check something yourself, is in [Reviewing AI output](reviewing-ai-output.md).

## Going further

- **Building prompts into a system** that runs without a person reading each answer is a different job: the prompt has to be tested on fixed cases and measured. The [Prompt Portfolio](https://github.com/luispsalas/prompt-portfolio) shows how.
- **Terms** such as context, grounding and hallucination are in the [glossary](glossary.md).

*Related wiki concept:* [Prompt Engineering](https://luispsalas.github.io/applied-ai-concepts/concepts/prompt-engineering.html)
