# Reviewing AI output

*Part of the [AI Enablement Toolkit](../README.md).*

A person's mistakes usually look like mistakes: a typo, a gap, a sentence that trails off. An AI system's mistakes usually look like finished work. The output is fluent, well formatted and confident whether or not it is right, so the usual signals a reviewer relies on are missing. This page lists where AI errors tend to hide, gives a short routine for checking the parts that matter, and sets out a drill that builds the skill over time.

> [!IMPORTANT]
> **Not yet tried with a team.** Most patterns come from the author's own daily work with AI tools, where each was caught in real output; the rest come from the wiki entries linked below and from recent research on AI results that needed outside checks. The drill has not been run with a group yet. Treat both as a starting draft to adapt.

Background on why this happens is in the wiki: [Hallucination](https://luispsalas.github.io/applied-ai-concepts/concepts/hallucination.html) (plausible content that is wrong), [Sycophancy](https://luispsalas.github.io/applied-ai-concepts/concepts/sycophancy-llms.html) (agreeing with the user over being accurate), [Automation Bias](https://luispsalas.github.io/applied-ai-concepts/concepts/automation-bias.html) (people stop checking) and [Verification](https://luispsalas.github.io/applied-ai-concepts/concepts/verification.html) (checking against ground truth).

## Where AI errors hide

| Pattern | What it looks like | How to check |
|---|---|---|
| **Right form, wrong target** | A link, citation or ID that opens fine but points to a different document, person or version | Open it and confirm the title, author and date match what the text claims. A page that loads proves nothing |
| **Invented specifics** | A name, figure, date or quotation that fits the sentence perfectly | Find it in the source. If it cannot be found, treat it as invented until shown otherwise |
| **Consensus with nothing behind it** | *Widely used*, *industry standard*, *experts agree* | Ask for the sources. If none come back, the claim is the finding |
| **Hardened hedges** | The source says *may*, *suggests* or *early results*; the output says *shows* or *proves* | Compare the strength of each key claim with the wording of the source |
| **A paraphrase in quotation marks** | Words in quotation marks that are close to, but not exactly, what the source says | Search the cited page for the exact words. Check the page that is cited, not any page that happens to contain them |
| **Numbers that do not hold up** | A total that does not add up, a percentage without its base, mixed units | Recompute one figure by hand and ask what each number counts |
| **Labels or order swapped** | Option A and B reversed, before and after inverted, actions credited to the wrong party | Check every labeled list or sequence against the original |
| **A dropped condition** | A summary that keeps the claim and loses the *only if*, *except* or *in this sample* | Read the source's limits and conditions, then look for them in the summary |
| **Agreement with you** | The output repeats your framing, or changes its answer when you push back | Ask the question without revealing your view, or ask it the opposite way |
| **A clean result that saw nothing** | *No issues found*, *0 errors*, *all checks passed* | Before trusting it, give the same check one case you know is wrong. If it misses that case, the clean result means nothing |
| **Agreement across runs** | The same answer every time the task is rerun, taken as proof it is right | Repetition shows consistency, not correctness: the same error can repeat in every run. Check one result against an independent source or a different method |
| **A claim of novelty** | *New insight*, *first of its kind*, *nobody has done this* | Search for what already exists before treating it as new. A check can confirm a result is valid; it cannot tell you nobody found it first |
| **Correct once, out of date now** | A rule, product feature or regulation described accurately for an earlier version | Check the date or version of what is described, and whether something has replaced it |

## A short routine

Checking everything is slow, and people who try usually end up skimming. Check what the decision depends on.

1. **Find the load-bearing claims.** Mark the few facts, figures or sources that the decision or the next step depends on. Those get checked; the rest gets read.
2. **Check against the source, never against the output.** Asking the same AI whether it was right is not a check. Open the source, run the code, recompute the number.
3. **Use the table above as a checklist** for the load-bearing claims, especially the patterns that look most like correct work.
4. **Say what you verified and what you did not.** When you pass the work on, mark which claims you checked and which you are taking on trust.
5. **Record what you found.** A repeated error is useful evidence: it may be a tool problem for the developers, or a training need for the people using it. The [adoption review kit](../adoption-kit/) has a way to tell the two apart.

How much of each output needs this routine depends on what is at stake. The planned *AI oversight levels* page will set that scale; until then, anything involving money, access or a person's record gets the full routine every time.

## When you cannot check it yourself

Some results sit beyond what one reviewer can verify: a statistical analysis, a legal or technical claim, a forecast built on data you have not seen. You do not have to check those yourself, but before the organization acts on them, someone should confirm that the right outside check happened. Four questions cover most cases.

1. **Is it really new?** An AI-generated insight, product idea or first-of-its-kind finding may already be well known, published or in use by a competitor. Before anyone invests in it as a discovery, search for what already exists.
2. **What exactly was checked?** When a tool or a vendor says an output was *validated* or *tested*, ask against what. An automated check usually confirms that the output follows a rule or a format. It does not confirm that the output answers the business question, and parts of the work may have been left outside the check.
3. **Has it been reproduced independently?** Getting the same answer from the same system every time is not confirmation, because the same mistake can repeat in every run. For any figure a decision depends on, have a different person or a different method reach it again.
4. **Who has signed off?** A result the organization will act on needs a named person with the expertise to judge it, who is accountable for it. The [operating model](../governance/operating-model.md) says who that is.

These questions come from recent cases in which AI results looked finished and needed an outside check. In one evaluation of an AI agent analysing clinical data, its errors *"propagated identically across independent repetitions"*, and only 8 of 17 of its narrative summaries were fully satisfactory ([J Med Internet Res 2026;28:e99597](https://www.jmir.org/2026/1/e99597)).

## The judgment drill

Reviewing is a skill, and like any skill it improves with deliberate practice rather than with exposure. The drill comes in two forms.

**Judge form (use for most skills).** A facilitator prepares five short AI outputs on a task the team does every week. Three contain planted errors taken from the table above, and two are clean. Each person reviews them alone, marks every error they find and how they would check it, then the group compares answers with the key. Planting is simple: change one figure, swap two labels, strengthen one hedge, or replace a correct link with a near miss. About 30 minutes.

**Side-by-side form (use for a few critical skills only).** A person does a task by hand, and a rough draft is enough. The AI does the same task. Both outputs are compared to list the weaknesses on each side. The human's weaknesses feed training; the AI's weaknesses feed the prompt, the agent's specification or the decision to keep that task with people. This form is slow on purpose, so reserve it for the skills the team has decided to keep.

**Keep score over time.** Record how many planted errors each round catches, by pattern. The patterns people keep missing are where to focus next. Run the drill again after any major model change, because the errors a new model makes can differ from the old one's.

### Example drill item

*Made up for illustration.* The task: summarize a short internal policy for a team update.

> **AI summary:** The new expense policy, effective March 1, shows that approval is required for all purchases over $500. Finance confirmed the change, and the full policy is on the intranet (with a link).

The source policy actually says approval *may* be required above $500 *for software purchases*, and takes effect on April 1. The key for this item:

| Planted error | Pattern | How a reviewer catches it |
|---|---|---|
| "shows that approval is required" | Hardened hedge | The policy says *may* |
| "all purchases" | Dropped condition | The policy limits it to software |
| "effective March 1" | Invented specific | The policy says April 1 |

The link is a fourth thing to check: open it and confirm it goes to this policy, not an older version.

## Where it fits

This page is about **how** to review. How **much** review each task needs belongs to the planned AI oversight levels page. Whether training changed what people actually do belongs to the planned training pre/post check, which can use drill scores as one of its measures. Errors found here feed the adoption review kit's feedback pages, and the failure paths section of the [agent specification template](../governance/agent-spec-template.md).
