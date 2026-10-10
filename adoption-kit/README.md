# AI Adoption Review Kit

*Part of the [AI Enablement Toolkit](../README.md). Release v0.1.*

A team gets a new AI tool, and a month later few people use it. This kit finds out why, in four steps: an interview, a diagnosis, a page for whoever can fix it, and a tracker that checks the fix worked.

> [!IMPORTANT]
> **Tried once.** One trial, n = 1, and the person interviewed set up the tool being studied. It shows the method runs end to end, not how common any finding is. Every figure is reported as *n of N*, and the tracker records what people report or what a usage log shows, never an automatic measurement.

| File | What it is |
|---|---|
| [`interview-guide.md`](interview-guide.md) | A 20–30 minute conversation with one person about one tool, with consent script, follow-up prompts and a one-person variant |
| [`diagnosis-sheet.md`](diagnosis-sheet.md) + `.csv` | One classified row per stall: tool, workflow, training, habit, undetermined, or not a stall |
| [`feedback-template.md`](feedback-template.md) | One page per issue for its fix owner, with a priority block and a follow-up section |
| [`usage-tracker.md`](usage-tracker.md) + `.csv` | One row per team and tool, from access to regular use, stalled or dropped |
| [`REPORTING.md`](REPORTING.md) | How findings travel: feedback page, status report, leadership brief, and the loop |
| [`leadership-brief-template.md`](leadership-brief-template.md) | A one-page brief for a reader with two minutes |

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

1. **Interview one person about one tool, for 20–30 minutes** ([`interview-guide.md`](interview-guide.md)). Start with an inventory of what the person has access to. Ask about the *last time* they did the task, not what they usually do, and turn every general answer into a concrete case with follow-up prompts. A variant covers one-person teams.
2. **Classify each stall** as tool, workflow, training or habit ([`diagnosis-sheet.md`](diagnosis-sheet.md)). Each class lists the evidence that points to it and the evidence that rules it out. When the evidence is not enough, the row says `undetermined` and names what would settle it. Something that only looked like a stall is recorded as `not a stall`, so it is kept and not raised again.
3. **Write one page per issue** for the team that can fix it ([`feedback-template.md`](feedback-template.md)): what happens, *n of N* affected, the evidence, the impact, one requested change, and a priority built from stated inputs.
4. **Track each team and tool** ([`usage-tracker.md`](usage-tracker.md)) from access, to first real use, to regular use, stalled or dropped. Then follow up after the fix ships.

## Broken or confusing?

The rule that matters most is the simplest: **before filing anything as a tool defect, reproduce it yourself.** If it fails for you too, it is a tool problem, with steps a developer can follow. If it works for you, the person did something different, or the tool misled them. That is still a real finding, but it is a training or design question, not a bug. The check script refuses a `tool` diagnosis that was not reproduced, so the rule cannot be skipped.

## How findings are reported

Findings travel at three levels ([`REPORTING.md`](REPORTING.md)):

1. **The finding:** one feedback page per issue, for its fix owner, open until its follow-up is filled.
2. **The status report:** a dated page across all teams: adoption as *n of N*, stalls by class, open pages by priority, overdue follow-ups, what changed.
3. **The leadership brief** ([template](leadership-brief-template.md)): one page for a reader with two minutes: what works, what stalled and why, decisions needed, fixes and whether they landed.

A fixed cadence closes the loop: the report flags anything past its review date, the brief carries decisions back to owners, and the follow-up interview checks the fix with the people who were stuck.

## Governance

The governance questions here are about **people**, not data:

- **Consent first.** Every conversation opens with a one-paragraph consent script. Quoting someone word for word needs a second, separate yes.
- **Anonymity by design.** Interviewees are codes (P01, P02), teams are role-level labels, and notes never hold names, employers or contact details. Notes stay private and never enter this repository.
- **Not blaming the tool unfairly, or the person.** The reproduce-first test keeps a confusing tool from being filed as a broken one. People using unapproved AI tools are recorded as a pattern, never as a person.
- **Fixed lists, checked.** Classes, statuses, owners and sources are fixed lists, checked by a small script ([`tools/check_lists.py`](../tools/check_lists.py)). Each of its 20 rules is tested twice: it must catch a planted error, and must miss it when switched off, which shows no other rule is doing its job.

## The first trial

The kit was used once, on a real tool: an AI coding assistant and the custom skills built on it, used daily by one person for their own projects. That person is also the author of this kit, and the interview was run in a chat by an AI agent following the guide word for word. The results are in [`examples/trial-n1/`](../examples/trial-n1/): 2 diagnosis rows, 2 tracker rows, 1 feedback page and a leadership brief filled from them.

What it surfaced:

- **Most of what looked like friction was not a stall.** The user often changes the plan midway. Asked for concrete cases, each came from their own review of real output against the people who would use it. That is iteration. The kit now has a `not a stall` outcome for exactly this.
- **A gap in inventory, not in features.** Generic add-ons installed early were replaced by custom ones that fit the user's work, and the user is not sure which old ones remain. Classed as **workflow**, with **habit** second. The guide now starts with an inventory step.
- **An open question kept open.** The user could not explain sharp changes in usage around new model releases, because they had no usage history to look at. Nobody could reproduce or inspect it, so the row says **undetermined** and names the check that would settle it.

The trial changed the kit in five places: follow-up prompts, the `not a stall` outcome, the one-person variant, the inventory step, and a closing question that asks what the person would want to see after a fix and when to check back.

## Quick start

From the repository root:

```bash
python3 tools/test_check_lists.py
```

This proves the checker works; it should end with `ALL PASSED`. Then check your own files before sending anything on:

```bash
python3 tools/check_lists.py adoption-kit/diagnosis-sheet.csv adoption-kit/usage-tracker.csv
```

Python 3, standard library only. The documents are plain Markdown and CSV, so they work in any editor or spreadsheet.
