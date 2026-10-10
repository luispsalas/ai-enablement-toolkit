# AI Enablement Toolkit

Practical, reusable material for helping teams adopt AI tools. **Release v0.1 holds the first piece: the AI Adoption Review Kit.**

A team gets a new AI tool, and a month later few people use it. The kit finds out why, in four steps: an interview, a diagnosis, a page for whoever can fix it, and a tracker that checks the fix worked. Literacy and assessment material follow in later releases (see [Roadmap](#roadmap)).

> [!IMPORTANT]
> **What this does not do (read first)**
> - **It is a method, tried once.** One trial, n = 1, and the person interviewed set up the tool being studied. It shows the method runs end to end, not how common any finding is.
> - **It does not measure usage automatically.** The tracker records what people report or what a usage log shows, and every row says which.
> - **It shows where people get stuck, not how many.** A handful of interviews cannot give a rate for a whole organization; every figure is reported as *n of N*.
> - **No research grounding yet.** It cites no adoption studies; if it does later, each source will be checked against the primary first.

## Why it matters

Teams are given AI tools faster than they are shown how to use them. When usage stays low, the usual reactions are to blame the tool or to run another training session. Both can be wrong. Low usage has at least four different causes, and each needs a different person to fix it:

| Cause | What it looks like | Who fixes it |
|---|---|---|
| **tool** | errors, wrong output, too slow | the development team |
| **workflow** | the tool works but adds a step or a hand-off | the process owner |
| **training** | people don't know how, or when, to use it | enablement |
| **habit** | the old way is easier and nothing in the day prompts the new one | the manager |

Sending a training problem to developers wastes their time. Sending a broken tool to a training session wastes everyone's. The kit decides which is which, and then checks that the fix reached the people who were stuck.

## How it works

```
 Interview ──> Diagnosis ──> Feedback page ──> Tracker
     ^                                            |
     └──────────────── follow-up ─────────────────┘
```

1. **Interview one person about one tool, for 20–30 minutes** ([`interview-guide.md`](adoption-kit/interview-guide.md)). Start with an inventory of what the person has access to. Ask about the *last time* they did the task, not what they usually do, and turn every general answer into a concrete case with follow-up prompts. A variant covers one-person teams.
2. **Classify each stall** as tool, workflow, training or habit ([`diagnosis-sheet.md`](adoption-kit/diagnosis-sheet.md)). Each class lists the evidence that points to it and the evidence that rules it out. When the evidence is not enough, the row says `undetermined` and names what would settle it. Something that only looked like a stall is recorded as `not a stall`, so it is kept and not raised again.
3. **Write one page per issue** for the team that can fix it ([`feedback-template.md`](adoption-kit/feedback-template.md)): what happens, *n of N* affected, the evidence, the impact, one requested change, and a priority built from stated inputs.
4. **Track each team and tool** ([`usage-tracker.md`](adoption-kit/usage-tracker.md)) from access, to first real use, to regular use, stalled or dropped. Then follow up after the fix ships.

## Broken or confusing?

The rule that matters most is the simplest: **before filing anything as a tool defect, reproduce it yourself.** If it fails for you too, it is a tool problem, with steps a developer can follow. If it works for you, the person did something different, or the tool misled them. That is still a real finding, but it is a training or design question, not a bug. The check script refuses a `tool` diagnosis that was not reproduced, so the rule cannot be skipped.

## How findings are reported

Findings travel at three levels ([`REPORTING.md`](adoption-kit/REPORTING.md)):

1. **The finding:** one feedback page per issue, for its fix owner, open until its follow-up is filled.
2. **The status report:** a dated page across all teams: adoption as *n of N*, stalls by class, open pages by priority, overdue follow-ups, what changed.
3. **The leadership brief** ([template](adoption-kit/leadership-brief-template.md)): one page for a reader with two minutes: what works, what stalled and why, decisions needed, fixes and whether they landed.

A fixed cadence closes the loop: the report flags anything past its review date, the brief carries decisions back to owners, and the follow-up interview checks the fix with the people who were stuck.

## Governance

The governance questions here are about **people**, not data:

- **Consent first.** Every conversation opens with a one-paragraph consent script. Quoting someone word for word needs a second, separate yes.
- **Anonymity by design.** Interviewees are codes (P01, P02), teams are role-level labels, and notes never hold names, employers or contact details. Notes stay private and never enter this repository.
- **Not blaming the tool unfairly, or the person.** The reproduce-first test keeps a confusing tool from being filed as a broken one. People using unapproved AI tools are recorded as a pattern, never as a person.
- **Fixed lists, checked.** Classes, statuses, owners and sources are fixed lists, checked by a small script ([`tools/check_lists.py`](tools/check_lists.py)). Each of its 20 rules is tested twice: it must catch a planted error, and must miss it when switched off, which shows no other rule is doing its job.

## The first trial

The kit was used once, on a real tool: an AI coding assistant and the custom skills built on it, used daily by one person for their own projects. That person is also the author of this kit, and the interview was run in a chat by an AI agent following the guide word for word. The results are in [`examples/trial-n1/`](examples/trial-n1/): 2 diagnosis rows, 2 tracker rows, 1 feedback page and a leadership brief filled from them.

What it surfaced:

- **Most of what looked like friction was not a stall.** The user often changes the plan midway. Asked for concrete cases, each came from their own review of real output against the people who would use it. That is iteration. The kit now has a `not a stall` outcome for exactly this.
- **A gap in inventory, not in features.** Generic add-ons installed early were replaced by custom ones that fit the user's work, and the user is not sure which old ones remain. Classed as **workflow**, with **habit** second. The guide now starts with an inventory step.
- **An open question kept open.** The user could not explain sharp changes in usage around new model releases, because they had no usage history to look at. Nobody could reproduce or inspect it, so the row says **undetermined** and names the check that would settle it.

The trial changed the kit in five places: follow-up prompts, the `not a stall` outcome, the one-person variant, the inventory step, and a closing question that asks what the person would want to see after a fix and when to check back.

## Quick start

Copy the `adoption-kit/` folder, then:

```bash
python3 tools/test_check_lists.py
```

This proves the checker works; it should end with `ALL PASSED`. Then check your own files before sending anything on:

```bash
python3 tools/check_lists.py adoption-kit/diagnosis-sheet.csv adoption-kit/usage-tracker.csv
```

Python 3, standard library only. The documents are plain Markdown and CSV, so they work in any editor or spreadsheet.

## Repository map

```
adoption-kit/   interview guide, diagnosis sheet, feedback template, usage tracker,
                REPORTING.md, leadership brief template, and the two CSV templates
tools/          check_lists.py (20 rules) and its tests
examples/       trial-n1/: the first trial (n = 1, real, anonymized)
```

## Roadmap

| Release | Adds |
|---|---|
| **v0.1** (this) | The adoption review kit, minimum structured reporting, the first trial |
| v0.2 | A script that builds the status report and brief from the CSV files, with the same tested checks; a walkthrough script and quick-reference template; a guide to reading a tool's usage log |
| v0.3 | AI literacy material, starting with an English–Spanish glossary of governance and literacy terms; facilitation practices for groups |
| v0.4 | A business AI needs assessment and a use-case intake and prioritization canvas |
| v0.5 | A Spanish version of the kit, and a second trial with other people, which lifts *n* above 1 |

## How it was built

Written in plain Markdown and CSV, with a short Python check script. The build was **AI-assisted**: an AI coding agent drafted the guide, sheet, templates and script from a brief I wrote, and I reviewed and edited them. The trial interview was also run by an AI agent, in a chat, following the guide as written; I answered as the interviewee.

## Related concepts

From the [Applied AI Concepts](https://luispsalas.github.io/applied-ai-concepts/) wiki: [AI Literacy](https://luispsalas.github.io/applied-ai-concepts/concepts/ai-literacy.html) · [Shadow AI](https://luispsalas.github.io/applied-ai-concepts/concepts/shadow-ai.html) · [Automation Bias](https://luispsalas.github.io/applied-ai-concepts/concepts/automation-bias.html) · [Human-in-the-Loop](https://luispsalas.github.io/applied-ai-concepts/concepts/human-in-the-loop.html) · [Continuous Feedback & Improvement](https://luispsalas.github.io/applied-ai-concepts/concepts/continuous-feedback-improvement.html)

## License

Code (`tools/`): [MIT](LICENSE). Documents, templates and examples: [CC BY 4.0](LICENSE-docs). © 2026 Luis P. Salas.
