# Diagnosis sheet: why did usage stall?

Low usage of a new AI tool has four common causes. They need different fixes from different people, so naming the right one matters more than describing the symptom. This sheet turns interview notes into one classified row per stall, in `diagnosis-sheet.csv`.

**One row = one stall** (one place where one or more people stopped, never started, or went back to the old way), or one apparent stall that turned out not to be one (see *Not a stall* below). A conversation can produce several rows, and a stall seen in several conversations is still one row, with `users_affected` counting them.

---

## The four classes

| Class | What it means | Evidence that points to it | Evidence that rules it out | Usual fix owner |
|---|---|---|---|---|
| **tool** | The tool itself fails: an error, a crash, wrong or unusable output, too slow for the task, missing access or permissions | You can **reproduce** it yourself, following the same steps (test T1). Several people hit it at the same step. An error message or a wrong output can be shown | It works when you do it. It works for some people and not others with the same steps, which usually points to training or access instead | **dev team** (or the vendor, through the dev team) |
| **workflow** | The tool works, but does not fit the work: wrong point in the process, an extra hand-off, output in the wrong format or place, a step it cannot do | The person can use it, and did, but has to copy, re-format or re-check the output to fit the next step. The old way has fewer steps. The task itself rarely matches what the tool does | The tool fits the steps when someone shows them how (then **training**). It fails outright (then **tool**) | **process owner** |
| **training** | People do not know how, or when, to use it: never shown, shown once, or shown on a different task | "I didn't know it could…" (interview question 9). People who were shown use it, and people who were not, don't. Errors come from using it the wrong way, and stop once they are shown | They know how, and say so, but still don't use it (then **habit** or **workflow**). It fails for people who do know how (then **tool**) | **enablement** |
| **habit** | They know how, and it works, but the old way is easier or more familiar, and nothing in the day prompts the new one | "I just do it the old way." No trigger in the process (interview question 15). Use rose after training and then faded. Works fine when they do use it | Using it is genuinely harder or slower than the old way (then **workflow**). They don't know how (then **training**) | **manager** (who can change what is expected), with the **process owner** |

**When the evidence is not enough to choose,** use `undetermined` and write in `next_check` what would decide it, for example "watch P02 do the task" or "ask P04 whether they were shown the summary feature". An `undetermined` row is a question still open, not a fifth cause, and the check script refuses an `undetermined` row with an empty `next_check`.

**Not a stall.** Some things look like friction and are not: a person who keeps changing the plan after reviewing real output is iterating, and a person who dropped a generic add-on for one that fits their work made a choice. Record these as `not a stall`, with the cases that show it in `evidence` and what you checked in `ruled_out`. Leave `class_secondary` and `fix_owner` empty: there is nothing to fix. The row exists so the finding is kept, and so it is not counted as a stall or raised again. The check script refuses a `not a stall` row that names a fix owner or a second class.

**A stall can have two causes.** Put the one you would fix first in `class_primary` and the other in `class_secondary`. A common pair is **training + habit**: people were shown it once, nothing prompts it, and it faded.

## The tests

**T1. Broken or confusing? Reproduce it before you file it.** Before a row can say `tool`:

1. Follow the person's steps yourself, in the same tool, with a similar input.
2. If it **fails for you too**, it is a tool problem. Write down the steps and the result, and mark `reproduced = yes`.
3. If it **works for you**, it is not (yet) a tool problem. The person did something different, didn't know a step, or the tool is confusing. Class it as **training** or **workflow** and note what differed. If the screen or wording misled them, say so in `observation`: a *confusing* tool is a real finding for the dev team, but it goes in as a design change, not as a defect.
4. If you **cannot** try it (no access, no similar data), mark `reproduced = not possible` and use `undetermined` until someone can.

The check script refuses a `tool` row whose `reproduced` is not `yes`. That is the rule that stops a confusing tool from being filed as a broken one.

**T2. Ask about the last time, not "usually".** Classify from what people *did* (interview section 2), not from opinions. "It's useless" is not evidence of anything. "It returned last quarter's numbers, so I stopped" is.

**T3. Count people, not mentions.** `users_affected` is the number of distinct interview codes that hit the stall, listed in `sources`. Always read it as *n out of how many interviewed*.

**T4. Look at who does use it.** If some people on the same team use it regularly, ask what they do differently. That difference is usually the fix.

## Columns of `diagnosis-sheet.csv`

| Column | What goes in it |
|---|---|
| `stall_id` | `S01`, `S02`… in order |
| `date` | Date the row was written, `YYYY-MM-DD` |
| `tool` | The tool's name |
| `team` | Role-level team label, the same one used in the usage tracker |
| `observation` | What happened, in one or two plain sentences: the step where people stopped and what they did next |
| `evidence` | What was said or seen that supports the class (paraphrase; verbatim only with consent, and then exactly as in the notes) |
| `ruled_out` | Which other class you considered and why the evidence rules it out |
| `class_primary` | `tool`, `workflow`, `training`, `habit`, `undetermined` or `not a stall` |
| `class_secondary` | `tool`, `workflow`, `training`, `habit` or `undetermined`, or empty. Always empty for `not a stall` |
| `reproduced` | `yes`, `no`, `not possible` or `not applicable` (test T1). It must be `yes` when `class_primary` is `tool` |
| `users_affected` | Number of distinct people who hit it |
| `sources` | Their interview codes, separated by spaces: `P01 P03` |
| `fix_owner` | `dev team`, `process owner`, `enablement` or `manager`. Empty only for `not a stall` |
| `next_check` | What would settle an `undetermined` row, or how you will know the fix worked |
| `feedback_ref` | The feedback page it went into, if any (for example `feedback-01.md`) |
| `synthetic` | `no` for real interviews. `yes` only for made-up example rows, which must never be mixed into real results |

The check script (`../tools/check_lists.py`) validates every fixed list in this sheet. Run it before sending anything on.

## Related concepts (Applied AI Concepts wiki)

- [AI Literacy](https://luispsalas.github.io/applied-ai-concepts/concepts/ai-literacy.html): what people need to know before a tool helps them (the **training** class).
- [Shadow AI](https://luispsalas.github.io/applied-ai-concepts/concepts/shadow-ai.html): what people use when the approved tool loses.
- [Automation Bias](https://luispsalas.github.io/applied-ai-concepts/concepts/automation-bias.html): the risk on the other side of adoption, accepting output without checking.
- [Human-in-the-Loop (HITL)](https://luispsalas.github.io/applied-ai-concepts/concepts/human-in-the-loop.html) and [Human–AI Collaboration Model](https://luispsalas.github.io/applied-ai-concepts/concepts/human-ai-collaboration-model.html): where the person sits in the workflow, which is often the real **workflow** question.
- [Human–LLM Communication Skills](https://luispsalas.github.io/applied-ai-concepts/concepts/human-llm-communication-skills.html): the prompting skill a **training** fix usually has to cover.
- [Human Responsibility in AI Use](https://luispsalas.github.io/applied-ai-concepts/concepts/human-responsibility-in-ai-use.html): who answers for the output once the tool is used.
- [Continuous Feedback & Improvement](https://luispsalas.github.io/applied-ai-concepts/concepts/continuous-feedback-improvement.html): the loop the feedback page and the follow-up step close.
