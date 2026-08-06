---
name: model-strategy
description: Assign the right model tier and reasoning effort to every subagent before spawning them, instead of letting them all inherit one model. Use whenever you are about to launch subagents — the Agent/Task tools, a Workflow, or any multi-agent fan-out (parallel finders, pipelines, judge panels, verifiers, worktree migrations). Trigger on "spawn agents", "use subagents", "run a workflow", "fan out", "orchestrate", "delegate this", or any plan that dispatches more than one agent.
---

# Model Strategy for Subagents

Before dispatching **any** subagent, decide its model **and** reasoning effort on purpose. The default is to inherit the parent model — that is almost always wrong for a fleet, because most roles in a workflow are cheaper or harder than the orchestrator. A strategized fleet is faster and cheaper for the same quality.

**Rule: never spawn a batch of subagents on one uniform model without first running the decision below.** One sentence of reasoning per role is enough — don't over-deliberate.

## The one-pass decision

For each distinct role in the workflow, answer two questions:

1. **How hard is the reasoning?** → picks the **model tier**.
2. **How much does a wrong answer cost the whole run?** → picks the **effort** (and whether to verify).

Then write it down as a fleet plan (see template below) before you spawn anything.

## Tier heuristics

| Role in the fleet | Tier | Why |
|---|---|---|
| Mechanical / high-volume: grep-and-collect, file listing, format conversion, boilerplate edits, extract-to-schema, simple lint | **haiku** | Cheap, fast, runs wide in parallel. Reserve smarter tiers for judgment. |
| Standard build/read/research: implement a scoped change, summarize a subsystem, single-angle search, draft docs, routine review | **sonnet** | The workhorse. Most pipeline stages live here. |
| Hard reasoning / high stakes: architecture & design tradeoffs, adversarial verification, judge/synthesis stages, security-sensitive or ambiguous code, the final "is this actually correct?" gate | **opus** | Use where a wrong answer is expensive or the problem is genuinely open. |
| The very hardest problems: the most complex or open-ended reasoning, gnarly multi-system debugging, design synthesis where opus-level judgment isn't enough; also creative/prose work where voice matters | **fable** | The smartest tier — sits **above opus**. Reserve it for tasks that are genuinely at the ceiling. |

The ladder is **haiku < sonnet < opus < fable**. Default when unsure: **sonnet**. Escalate a role only when you can name why it's hard; drop it to haiku only when it's genuinely mechanical.

**Mismatches are forbidden in both directions:**
- Never assign a **lower** tier to a harder-tier task — no sonnet subagent on an opus/fable-hard problem. It will produce a plausible wrong answer, and verification cost eats the savings.
- Never assign a **higher** tier to routine work — no fable subagent on a sonnet-grade task. You pay ceiling prices for workhorse output.

## Effort heuristics (Workflow `effort`, or how hard the agent should think)

Effort upgrades have steeply diminishing returns: benchmark cost curves (DeepSWE) show **high → max buys a few points of quality for a multiple of the cost**, and even **medium → high is sometimes not worth it**. Prefer the right *model tier* at moderate effort over a lower tier cranked to max.

- **low** — mechanical stages, large fan-out, anything on haiku. Keep it cheap.
- **medium** — default for workhorse stages. Question every upgrade past this.
- **high** — the hardest judgment stages only: final verifiers, design synthesis, the gate that decides whether findings are real. Pair with opus/fable.
- **xhigh / max** — almost never. Justified only when a single run-deciding stage demonstrably failed at high and re-running smarter beats re-designing the stage.

## Shape-of-workflow rules

- **Fan-out finders** (many parallel searchers): haiku or sonnet, low/medium effort. Breadth beats depth here.
- **Pipeline middle stages**: sonnet. Only the final synthesis stage climbs to opus.
- **Adversarial verify / judge panels**: opus at high effort. This is where uniform-cheap fleets silently pass bad findings — spend here.
- **Worktree migrations** (`isolation: 'worktree'`): match tier to per-site difficulty; a repetitive codemod is haiku, a semantic refactor is sonnet+.
- **Single delegated subagent** (not a fleet): match the parent's tier unless the task is clearly easier or harder — a one-off grep drops to haiku, a design question climbs to opus.

## Cost/quality sanity check

Before spawning, glance at the fleet plan and ask:
- Am I paying opus prices for grep? → downgrade.
- Is a cheap model gating correctness on the final step? → upgrade that one stage.
- Do 20 parallel agents all need to be smart, or just the 2 that decide? → make the 18 cheap.

## Fleet plan template

Emit this (briefly) before dispatching, so the choice is explicit and reviewable:

```
Fleet plan:
- <role> ×N — <tier>/<effort> — <one-line why>
- <role> ×N — <tier>/<effort> — <one-line why>
Spend concentrated on: <the stage that decides correctness>
```

Example — a review workflow:

```
Fleet plan:
- dimension finders ×5 — sonnet/medium — scoped reviews, breadth
- adversarial verifiers ×1-per-finding — opus/high — the correctness gate
- synthesis ×1 — opus/high — merges & ranks, expensive to get wrong
Spend concentrated on: verify + synthesis; finders stay cheap
```

## How to apply it in each harness

- **Agent tool** — pass `model` (`opus` | `sonnet` | `haiku` | `fable`) per `Agent` call. Different roles → different calls → different models, in the same batch.
- **Workflow** — pass `model` and `effort` per `agent(...)` call. Omit to inherit the session model **only** for roles that genuinely match the parent tier; set them explicitly for everything else. Scale fleet size and tier to the task, not to habit.
- **Codex / other agents** — same discipline: name each subagent's role, assign the cheapest tier that clears the bar, concentrate the expensive tier on the stages that decide correctness.

Keep it lightweight: a fleet plan is 3–5 lines, not an essay. The point is that no subagent gets a model by accident.
