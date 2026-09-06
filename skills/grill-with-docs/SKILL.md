---
name: grill-with-docs
description: Clarify human-owned project intent, scope, domain meaning, and consequential tradeoffs through one-question-at-a-time discussion. Use for unresolved project direction or an explicit plan review; record settled decisions in project docs.
---

## Human-owned direction

This skill resolves missing human decisions, not missing implementation facts. Receive
the current intent, evidence, and consequential ambiguity; return a recorded decision
that architecture and orchestration can reuse instead of repeatedly asking the same question.

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

## Domain awareness

During codebase exploration, also look for existing documentation:

### File structure

Most repos have a single context:

```
/
├── CONTEXT.md
├── docs/
│   └── adr/
│       ├── 0001-event-sourced-orders.md
│       └── 0002-postgres-for-write-model.md
└── src/
```

If a `CONTEXT-MAP.md` exists at the root, the repo has multiple contexts. The map points to where each one lives:

```
/
├── CONTEXT-MAP.md
├── docs/
│   └── adr/                          ← system-wide decisions
├── src/
│   ├── ordering/
│   │   ├── CONTEXT.md
│   │   └── docs/adr/                 ← context-specific decisions
│   └── billing/
│       ├── CONTEXT.md
│       └── docs/adr/
```

Create files lazily — only when you have something to write. If no `CONTEXT.md` exists, create one when the first term is resolved. If no `docs/adr/` exists, create it when the first ADR is needed.

## During the session

### Challenge against the glossary

When the user uses a term that conflicts with the existing language in `CONTEXT.md`, call it out immediately. "Your glossary defines 'cancellation' as X, but you seem to mean Y — which is it?"

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

### Update CONTEXT.md inline

When a term is resolved, update `CONTEXT.md` right there. Don't batch these up — capture them as they happen. Use the format in [CONTEXT-FORMAT.md](./CONTEXT-FORMAT.md).

Don't couple `CONTEXT.md` to implementation details. Only include terms that are meaningful to domain experts.

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
