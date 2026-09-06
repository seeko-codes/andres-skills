# Human-owned priorities, not a new reward function

Read when configuring or resolving tradeoffs. Reuse preferences in the project's existing
instructions. An optional repo-root `TURN-TO-LIFE.md` may hold them when no authoritative
location exists; do not create a second configuration source. Explicit current human
direction and higher-priority instructions govern conflicts. Record unresolved consequential
conflicts and ask; do not silently pick the agent's preferred interpretation.

## Two controls for effort allocation

| Setting | Default | Meaning |
|---|---|---|
| `optimization_priority` | `[elegance, cost, latency]` | Ordered preference among feasible candidates with comparable required quality; not numerical weights |
| `optional_refinement_experiments` | `2` | Maximum additional experiments per task devoted to optional polish or improving methods, not a target to exhaust |

**Elegance** is minimal sufficient responsibilities, dependencies, and procedure at the
agreed quality bar across current needs and credible future changes, not short code or
elaborate abstractions. **Cost** is aggregate model, tool acquisition/building, context,
integration, human-interruption, verification, operation, rework, maintenance, and retirement
cost where assessable. Use the project's stated horizon and concrete change expectations;
label forecast uncertainty and clarify consequential gaps rather than assuming infinite reuse.
[Tool sufficiency](TOOLS.md) applies these priorities without another size or plugin setting.
**Latency** is elapsed time to the user's verified result, not one agent's lifetime.

Use the ordering only for material tradeoffs supported by evidence. Prefer an option that
is no worse on the relevant criteria and better on at least one. For conflicting options,
consider the highest-priority meaningful difference within scope and budgets; investigate
or ask when consequences exceed existing direction. Do not invent precise measurements
or pursue a negligible elegance gain indefinitely because it appears first in a list.

Optional refinement includes speculative tool generalization or method improvement; required
tooling still follows the same task scope and acceptance gates as other implementation.
The refinement limit counts optional experiments across the task, including workers; carry
the remaining allowance in the existing brief/handoff, not a new ledger. Zero disables
optional experiments, not necessary investigation, required verification, or ordinary
implementation. A justified task-critical experiment still follows scope/resource gates.
If necessary work cannot fit those gates, preserve progress and report the gap. No incentive
to reclassify optional work as mandatory or split tasks to reset an exhausted allowance.

Both defaults are adjustable policy choices, not empirically established constants. The
agent may propose changes from evidence but cannot change human preferences autonomously.
Use each priority label once; the refinement count must be a nonnegative integer. Clarify
invalid or ambiguous supplied settings rather than treating them as authorization.

## Example project preferences

Put only overrides in the established project record, for example:

```yaml
optimization_priority: [latency, elegance, cost]
optional_refinement_experiments: 1
```

This asks for faster verified delivery when acceptable solutions have material tradeoffs.
It does not permit skipped checks, weaker behavior, more agents without authorization,
or ignoring a resource limit. A human may instead prioritize aggregate cost or elegance.

Existing settings retain their owners: [CONTEXT.md](CONTEXT.md) defines context ceilings
and warnings, [model-strategy](../model-strategy/SKILL.md) defines effort approval, and
Wayfinder remains explicitly opt-in. Carry resolved preferences through orchestration.
These are instructions interpreted by the agent, not an executable optimizer or enforced
runtime budget. Do not claim telemetry, scheduling, or learning machinery that is absent.
