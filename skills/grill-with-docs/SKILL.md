---
name: grill-with-docs
description: Clarify human-owned intent, domain meaning, and consequential tradeoffs through principle-driven, one-question-at-a-time discussion. Use for unresolved project direction, consequential domain-knowledge gaps, or an explicit plan review; record decisions and evidence in existing project docs.
---

## Human-owned direction

This skill elicits human direction and domain understanding when these can resolve a
consequential gap; it does not outsource implementation facts the agent can inspect.
Receive intent, evidence, and ambiguity; return reusable principles, confirmed decisions,
and factual claims with their source and uncertainty. Do not ask the same settled question again.

Use this interview when the project's purpose, scope, priorities, domain meaning, or
consequential tradeoffs need clarification. The human owns those decisions. The agent
can model the intent, investigate feasibility, challenge assumptions, and recommend options;
it must not substitute its preferred goal for an unresolved human choice.

Start breadth first: desired outcome, constraints, exclusions, and evidence of success.
Then narrow to the decision that blocks useful progress, resolving prerequisites first.
Ask one question at a time with context, options, tradeoffs, and a recommendation when
supported. Wait for the human's answer to that question. Do not interview every imaginable
branch or reopen decisions already settled unless new evidence puts them in doubt.

Inspect the code or relevant sources for questions they can answer. Existing implementation
is evidence of current behavior, not authority over the human's intended future behavior.
Leave routine execution choices with the assigned agent. Once the current goal and
acceptance are clear enough, return them and any unresolved dependencies to the orchestrator.
Only work depending on an unanswered decision needs to wait.

<supporting-info>

## Ask for the governing relationship

Choose the gap whose resolution could change the most consequential downstream work.
Supply the concrete situation, known evidence, and competing consequences. Ask about the
purpose, invariant, or tradeoff behind the choice rather than requesting an implementation
vote. A direct factual question is still appropriate when that is the actual gap.

For example, replace "Should we support offline mode?" with "When connectivity fails, what
must the user still accomplish, and what consequence makes that essential?" Do not lead the
answer or require abstract language. Help the human reason; do not make them redo the research.
Probe a boundary case as a follow-up when it could change the principle's application.

Separate what the answer establishes: a preference sets direction; a factual assertion is
sourced evidence to assess; an architectural implication is an inference to test. Confirm
consequential interpretations, not every paraphrase. A persuasive answer is not proof of
behavior. Workers return shared questions through their manager, not a competing interview.

## Domain awareness

Locate authoritative domain language, context maps, and decision records using project
routing instructions. Choose by purpose and contents, not filename alone. Reuse existing
locations and formats; do not create a parallel glossary or mix routing with domain meaning.

Only when no authoritative equivalent exists, create a minimal record lazily for the first
resolved term or warranted decision. `CONTEXT.md`, `CONTEXT-MAP.md`, and `docs/adr/` are fallback
conventions, not required topology. If a name already serves another purpose, choose a
non-conflicting location consistent with the project. [CONTEXT-FORMAT.md](CONTEXT-FORMAT.md)
supplies a default glossary and examples, not permission to relocate existing documentation.

## During the session

### Challenge against the glossary

When the user uses a term that conflicts with the authoritative domain glossary, call it out immediately. "Your glossary defines 'cancellation' as X, but you seem to mean Y — which is it?"

### Sharpen fuzzy language

When the user uses vague or overloaded terms, propose a precise canonical term. "You're saying 'account' — do you mean the Customer or the User? Those are different things."

### Discuss concrete scenarios

When domain relationships are being discussed, stress-test them with specific scenarios. Invent scenarios that probe edge cases and force the user to be precise about the boundaries between concepts.

### Cross-reference with code

When the user states how something works, check whether the code agrees. If you find a contradiction, surface it: "Your code cancels entire Orders, but you just said partial cancellation is possible — which is right?"

### Record human decisions

Record agreed purpose, scope, exclusions, and acceptance in the existing project plan or
brief. Keep unresolved choices marked open; a proposed answer is not an accepted decision.
Use ADRs for decisions that warrant their rationale being preserved, not as a prerequisite
for recording the user’s goal. Respect existing documentation locations.

### Update the authoritative glossary

Capture a resolved term in the established glossary while the decision is current, within
write ownership. Follow its existing format; use [CONTEXT-FORMAT.md](CONTEXT-FORMAT.md) as a
default only when needed. Keep domain meaning separate from implementation-routing detail.
Workers report changes outside their ownership rather than writing shared records directly.

### Offer ADRs sparingly

Only offer to create an ADR when all three are true:

1. **Hard to reverse** — the cost of changing your mind later is meaningful
2. **Surprising without context** — a future reader will wonder "why did they do it this way?"
3. **The result of a real trade-off** — there were genuine alternatives and you picked one for specific reasons

If any of the three is missing, skip the ADR. Use the format in [ADR-FORMAT.md](./ADR-FORMAT.md).

### Optional: put the surviving plan on a page

Only if `lavish-axi` is installed. When the interview is over, the plan that survived it can be rendered as an HTML artifact (`lavish-axi playbook plan`), opened with `lavish-axi <file>`, and annotated by the user; `lavish-axi poll <file>` returns their marks. Use it at the end, as a final read-through of what was decided — never to replace the interview.

The one-question-at-a-time rule still binds. Do not batch questions into an artifact. The single exception is one question with many discrete options — a term to canonicalise, a scope to pick — where `lavish-axi playbook input` renders that one question as choices; ask it, wait for the answer, then continue.

</supporting-info>

## Terminology, explanation, and ambiguity

Use canonical technical terminology in agent instructions, contracts, and technical
records. In human-facing updates, explain the action, purpose, evidence, and decision in
familiar language; introduce a technical term only when useful and explain it briefly.
For an unresolved method or tool question, consult [REFERENCES.md](REFERENCES.md) on demand.
Do not load the shelf or its sources automatically, and do not use external research to
guess the human's intent.
