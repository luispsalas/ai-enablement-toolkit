# Reporting: from one interview to a decision

Interviews only help if what people say reaches someone who can act on it, and if someone checks afterwards that the fix worked. This page describes how findings travel, at three levels, and the loop that keeps them moving.

```
 Interview ──> Diagnosis row ──> Feedback page ──> Status report ──> Leadership brief
     ^          (one per stall)   (one per issue)   (all teams)       (decisions)
     |                                                                     |
     └────────────── follow-up after the fix ships <───── owners act <────┘
```

## Level 1: the finding (for the person who can fix it)

**One feedback page per issue** (`feedback-template.md`), written for its fix owner: dev team, process owner, enablement or manager. It says what happens, who hits it as **n of N**, the evidence, the impact, one requested change, and a **priority** built from three stated inputs (reach, impact, effort). It stays open until its follow-up section is filled.

## Level 2: the status report (for whoever runs the rollout)

A dated one-page summary of every team and tool, built from `usage-tracker.csv`, `diagnosis-sheet.csv` and the open feedback pages. In this release it is written by hand; a script that builds it from the files is planned (see the README's roadmap). It covers:

- **adoption by team and tool**, always as `users_regular` of `users_with_access`, with the source;
- **stalls by class** (tool, workflow, training, habit, undetermined), each pointing at its diagnosis rows;
- **open feedback pages by priority**, with owner and follow-up date;
- **overdue follow-ups**: any tracker row or feedback page past its review date;
- **what changed since the last report**.

Run the check script on both CSV files before writing it. A report built on rows that fail the checks is not sent.

## Level 3: the leadership brief (for a reader with two minutes)

One page (`leadership-brief-template.md`): what is working, what stalled and why, the decisions needed, the fixes shipped and whether they landed, and the next review date. Every figure in it must be traceable to the tracker or the diagnosis sheet. If the evidence is thin, the brief says so at the top, with *n*.

## The loop

1. **Cadence.** Pick one and keep it, for example every two weeks while a tool is being rolled out, then monthly.
2. **A feedback page stays open** until its follow-up section is filled. "Shipped" is not "fixed".
3. **The status report flags anything past its review date.** A flag means someone looks again, not that someone is blamed.
4. **The brief carries decisions back to owners**, and the owners' next actions go into the tracker's `next_action` and `review_date`.
5. **The follow-up interview** (question 18 of the guide) checks the fix with the people who were stuck, and the tracker row moves, or does not.

## Rules that apply at every level

- **Adoption is always n of N**, never a bare percentage.
- **Every number says where it came from**: interview, self-report, usage log or estimate.
- **Real and example data never share a file.** Example files say so in their title.
- **Small samples are stated at the top**, not in a footnote. A report on three interviews is a report on three interviews.
- **No names.** Interviewees are codes, teams are role-level labels.
