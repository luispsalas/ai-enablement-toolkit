# Interview guide: one user, one AI tool

A 20–30 minute conversation with **one person** about **one AI tool** their team was given. The aim is to learn what they actually did with it, not what they think of it. Answers feed the diagnosis sheet (`diagnosis-sheet.md`) and the usage tracker (`usage-tracker.md`).

Use it as written the first few times. Skip a section only when it clearly does not apply, and write down that you skipped it.

---

## Before the conversation

- **Pick one tool.** If the person uses several, run one conversation per tool, or pick the one their team was asked to adopt.
- **Know the tool yourself.** Open it and try the main task before the interview. You cannot tell "broken" from "confusing" later without this (diagnosis sheet, test T1).
- **Make an inventory of what this person has.** List the features, add-ons, plugins, integrations and saved prompts available to them, from an admin, the tool's settings or the person, before the conversation. Question 9 asks about things they never opened, and you cannot ask about what you do not know is there. If nobody can produce the list, that is already a finding: write it down.
- **Give the person a code, not a name.** Use `P01`, `P02`… in order. Write the team as a role-level label (for example "finance operations", "support team") and never the company, the manager or a project name.
- **Do not record audio or video.** Take notes by hand or typed, in the note format below.
- **Ask for 30 minutes and stop at 30.** If there is more to cover, ask for a second slot.

## Opening and consent (read it out, about one minute)

> Thanks for your time. I'm trying to understand how people actually use [tool] day to day, where it helps and where it gets in the way. This is about the tool and how it was rolled out, not about you: there are no right answers, and nothing you say will be used to judge your work. I'm taking notes but not recording. Your name won't be written down. In anything I write up you'll be a code like "P03", and I'll leave out anything that could identify you or your team. If I'd like to quote something you said word for word, I'll ask you first, and you can say no. You can skip any question or stop at any time. Is that OK?

Write down the answer in the notes as **consent: yes / no**. If it is no, thank them and stop. Nothing from the conversation is kept.

Ask a second, separate question only if you may want to publish a quotation:

> If something you say would make a good example, may I quote it word for word in a public write-up, without your name? Or would you prefer I only paraphrase?

Record it as **quote consent: public / internal only / paraphrase only**.

## Follow-up prompts (use them throughout)

General answers ("I often go back and change things", "it's sometimes slow") are opinions about a pattern. Turn each one into a case before you move on:

- **"When did that last happen?"** Then: what were you doing, what happened, what did you do next?
- **"Can you give me a second example?"** One case can be an exception; two that look alike are a pattern worth a row.
- **"What happened just before?"** The trigger usually tells the classes apart: a review that brought a new idea is not the same as an error.
- **"What did you do instead?"** It shows whether they kept going, worked around it, or stopped.

Write each case in the notes as its own item. Classify only from cases, never from the general statement (diagnosis sheet, test T2).

## 1. The job, not the tool (about 5 min)

Start from their work. The tool comes later.

1. What part of your work was [tool] supposed to help with?
2. Walk me through the last time you did that task. Start at the beginning: what triggered it, and what was the first thing you did?
3. How often does that task come up? (Daily, weekly, a few times a month.)

*Listen for:* the real steps and hand-offs. Write them as a numbered list in the notes. They are what you compare the tool against in the diagnosis.

## 2. The last real use (about 8 min)

Ask about **one specific recent occasion**, not "usually". People describe what they believe they do when you ask about habits. They describe what they did when you ask about last Tuesday.

4. When did you last use [tool] for real work, not to try it out? What were you doing?
5. Show me, or tell me step by step, what you did in the tool.
6. Did you get what you needed? What did you do with the result? (Used it as is, edited it, checked it, threw it away.)
7. Was there a point where you stopped, got stuck, or switched to something else? What happened just before that?
8. If they have never used it for real work: what happened the last time you had that task? Why not the tool, that time?

*Listen for:* the exact place where they stopped, and whether they tried again. Write down error messages, wrong outputs and screen names exactly as described.

## 3. What they never opened (about 4 min)

9. [Tool] can also do [feature A, feature B]. Have you tried those? If not, why not? ("Didn't know", "didn't need it" and "tried once, didn't work" are three different answers. Write down which one.)
10. Is there anything you expected it to do that it doesn't?

## 4. What they do instead (about 5 min)

11. When you don't use [tool] for this task, what do you use? (The old way, a spreadsheet, a colleague, another AI tool.)
12. What makes that easier, or safer, than [tool]?
13. Is anyone on your team using a different AI tool for this? You don't need to name anyone.

*Handle with care:* question 13 can surface **shadow AI**, people using unapproved tools instead. Record it as a pattern ("team uses an unapproved chat assistant for drafting"), never against a person. The point is that the approved tool lost to something easier. It is not a compliance finding about the interviewee.

## 5. Help, prompts and trust (about 4 min)

14. How did you learn to use it? (Training, a guide, a colleague, trial and error.) What was missing?
15. Is there anything in your day that reminds you to use it, or a step where it is expected? (A form, a checklist, a manager asking.)
16. How do you check what it gives you? Has it ever been wrong in a way that mattered?

*Listen for:* both over-trust and distrust. Accepting output without checking points to **automation bias**. Never trusting it, so redoing the work by hand, means the tool adds a step instead of removing one.

## Close (1 min)

17. If you could change one thing about [tool] or how it was introduced, what would it be?
18. If that changed, what would you want to see, and when would be a good time for me to check back with you? (Record what they would see and when, and **follow-up: yes / no**. The contact detail goes in your own address book, never in these notes.)

Thank them. Tell them when they can expect to hear what changed.

---

## Variant: one person, or a very small team

When the person is the whole team (a freelancer, a founder, a two-person office), they chose the tool, set it up and decide how it is used. Run the guide as written, with these changes:

- **Team label:** use a role-level label such as "solo consultant". There is no team behind it, so the tracker's `users_with_access` is usually 1.
- **Question 13 (others using a different tool):** ask instead which other AI tools *they* use, and for what. With nobody to bypass, this is not shadow AI: record it as part of how they work.
- **Question 15 (reminders):** nobody else sets expectations, so ask what they do to remember a feature exists (a list, a pinned note, a habit).
- **Fix owners:** keep the fixed list (dev team, process owner, enablement, manager). The person may hold several of these roles; name the role, not the person, so the fix is still sorted by kind.
- **Dates:** self-reported dates are often known only to the month. The usage tracker says how to enter them.
- **If you built or set up their tool,** say so in the notes and in every write-up. You know what to look for, and you may also miss what you take for granted.

## Note format

One file per conversation, named `notes-P01-<tool>-<YYYY-MM-DD>.md`, kept **private** (never in a public folder).

```
Code: P01            Tool: <tool>            Date: YYYY-MM-DD
Team (role-level):   <e.g. support team>     Interviewer: <initials>
Consent: yes         Quote consent: paraphrase only        Follow-up: yes

Task and its steps (section 1):
1. ...

Last real use (section 2), in order, with where it stopped:
- ...

Never opened (section 3), with the reason given:
- feature: reason (didn't know / didn't need / tried, failed)

Instead (section 4):
- ...

Learning, prompts, checking (section 5):
- ...

One change they'd make:
- ...

Verbatim (ONLY with quote consent, word for word, in quotation marks):
- "..."
```

**Rules for the notes:**

- **No names, employers, managers, project names, email addresses or anything else that identifies the person**, even in passing. If they name a colleague, write "a colleague".
- **Separate what they said from what you think.** Write your own interpretation on lines starting `My read:`. The diagnosis uses both, but only what they said counts as evidence.
- **Quotation marks mean word for word.** Anything paraphrased goes without them. A quotation used later in a report must match these notes exactly.
- **Write the notes up within the day.** Memory fills gaps with what you expected to hear.

## After the conversation

1. Fill one row of the diagnosis sheet **per stall** you found (`diagnosis-sheet.csv`). One conversation can produce zero, one or several rows. Something that looked like a stall but turned out to be normal work (iteration, a deliberate choice) gets a `not a stall` row, so the next person does not raise it again.
2. Update the team's row in the usage tracker (`usage-tracker.csv`).
3. Before calling anything a tool defect, reproduce it yourself (diagnosis sheet, test T1).
