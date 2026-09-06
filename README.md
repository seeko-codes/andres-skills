<p align="center"><img src="brand/hero.webp" alt="Turn to Life — a purposeful path grows from a seed into a leaf." width="100%"></p>

# Turn to Life

**From a problem worth solving to an elegant, verified solution.**

A portable workflow for building software with AI agents. You own the purpose and the
tradeoffs. The agent clarifies, builds, tests, and preserves the understanding that makes
the next change easier. **Not less thinking. Less wasted thinking.**

[Get started](#start) · [The core logic](LOGIC.md) · [Evaluation](skills/context-architecture/EVALUATION.md) · [MIT license](LICENSE)

## Start

Download this repository using **Code → Download ZIP**, then extract it and open a terminal
in the extracted folder. Install into the **existing project you want to work on**:

```sh
python3 install.py /path/to/your-project
```

Python 3 is needed for this copy step; the workflow itself is Markdown. The default
destination is `/path/to/your-project/.agents/skills/`. The installer uses no network,
refuses existing skill names, and leaves project instructions and global tools alone.

Then ask your agent:

> Use the local .agents/skills/turn-to-life/SKILL.md. The problem I want to solve is
> [problem], for [people].
> Success would look like [outcome]. My constraints are [constraints]. Help me turn
> this into an elegant, verified solution.

You can start with an incomplete idea. The agent should ask about consequential gaps,
not make you complete a questionnaire. If you choose another local directory, adjust the
prompt's path. If the skill is not discovered, use your runner's reload/new-session procedure
or point it directly to the installed `turn-to-life/SKILL.md`.

<details>
<summary><strong>Other runners, manual installation, and discovery</strong></summary>

For a runner that uses another project-local directory, choose it explicitly, for example:

```sh
python3 install.py /path/to/your-project --skills-dir .claude/skills
```

Use your runner's supported local directory, or point it directly to the installed skill.
The installer does not register discovery. It rejects paths or shared symlinks that escape
the project.
Inspect planned paths with `--dry-run`. For manual installation, copy the initial seven
folders inside `skills/` together into the project's local skills directory, preserving names.
Keep skill code and non-sensitive project preferences under the project's version control.

</details>

## What changes in the work

1. **Find the real problem.** Questions reveal purposes and governing principles—not just feature votes.

2. **Build the explanation before accumulating detail.** Responsibilities and contracts make code understandable; early structure stays revisable.

3. **Spend effort where it changes the result.** Inspect, ask, experiment, or implement. Small work stays local; helpers are conditional.

4. **Test what you claim.** Check the solution logic, actual behavior, and total cost separately. A beautiful explanation does not excuse broken code.

5. **Keep what the work taught you.** Correct existing project knowledge so the next task starts better informed, not with a larger transcript.

Build from **problem → solution logic → responsibilities → implementation**.
The model stays revisable: **purpose → model → useful action → evidence → correction**.

Elegance means minimal sufficient structure at the agreed quality bar, not the fewest lines
or the shortest agent session. Necessary effort stays; extraneous load is what we remove.

## A project that improves its own methods

The agent can find, reuse, build, adapt, test, combine, or retire any task-justified tool:
skills, scripts, checkers, generators, or other capabilities. Authored tools stay repo-local
in appropriate locations; the starting skill bundle is not a closed catalog.

**Sufficient across time, not smallest today.** Meet current acceptance while accommodating
credible future changes at justified lifecycle cost. A larger tool or replaceable component
can earn its place by reducing future work; imagined reuse does not justify a framework.
Plugin-like boundaries are optional means, not an architectural requirement. See the
conditional [tool lifecycle](skills/turn-to-life/TOOLS.md). No toolkit growth target or
silent change to global agent behavior is implied.

You can prioritize elegance, aggregate cost, or elapsed time among acceptable solutions.
Put overrides in existing project instructions or an optional project-root `TURN-TO-LIFE.md`:

```yaml
optimization_priority: [elegance, cost, latency]
optional_refinement_experiments: 2
```

These are the adjustable defaults, not calibrated constants. The experiment limit applies
to optional refinement, not required checks. [Settings](skills/turn-to-life/SETTINGS.md)
define the tradeoffs; quality, authority, and resource gates still bind. The agent improves
methods against evidence—it does not rewrite your preferences to improve its score.

## One entrypoint, focused supporting methods

You do not need to learn this table before starting. Install the bundle; the entrypoint
loads a method when its decision is relevant, not all supporting documents at startup.

<details>
<summary><strong>Explore the seven starting skills and their responsibilities</strong></summary>

| Component | Owns |
|---|---|
| [turn-to-life](skills/turn-to-life/SKILL.md) | The problem-to-solution loop; scoped execution and orchestration |
| [grill-with-docs](skills/grill-with-docs/SKILL.md) | Principle-driven human clarification and domain understanding |
| [context-architecture](skills/context-architecture/SKILL.md) | Reusable relationships, code boundaries, and precise navigation |
| [model-strategy](skills/model-strategy/SKILL.md) | Capability recommendations and human-approved helper effort |
| [lean-quality](skills/lean-quality/SKILL.md) | Proportionate verification of retained implementation |
| [tdd](skills/tdd/SKILL.md) | The explicitly requested test-first method |
| [wait-what](skills/wait-what/SKILL.md) | A clearer explanation when you request one |


</details>

There is one orchestrator: `turn-to-life`. Its [delegation procedure](skills/turn-to-life/ORCHESTRATION.md)
is a conditional mode, not another layer of management. Supporting skills remain separable;
installing the starting bundle is the simplest way to keep their local links available.
Project methods can evolve after installation; there is no requirement to retain all seven forever.

## What stays in your control

Project instructions, scope, data protections, and required checks remain in force.
Helpers require your approval of reasoning effort, or an existing approval covering the work.
Manager policy prefers maximum available capability/effort; unsupported settings are reported,
not silently changed. These are [operating policies](skills/model-strategy/SKILL.md), not efficacy claims.

Context defaults to 100000 tokens per agent, with a warning at 80% or a lower runtime limit.
You can override them. [Budget rules](skills/turn-to-life/CONTEXT.md) distinguish measured,
estimated, and unavailable telemetry. Installing instructions does not install monitoring.
Wayfinder is off by default; optional runtime modes and visual-review tools stay optional.

## Does it work?

The workflow is designed to improve output quality and effort allocation. That is a
**testable aim, not a demonstrated universal improvement**. Compare representative tasks
against your existing process at the same quality bar, including failures, rework, and
maintenance. See the [evaluation guide](skills/context-architecture/EVALUATION.md).

The [logic](LOGIC.md) separates premises, chosen policies, and hypotheses. Predictive
processing and active inference inform the design; free energy is not a token/time metric.
No paid learning corpus, private project context, model subscription, or extra agent service
is bundled or required. You provide your agent runtime and its normal model/tool access.

## Updating or migrating

<details>
<summary><strong>Existing installations and legacy skill names</strong></summary>

The installer intentionally refuses collisions in the selected project-local directory. Back up and review existing skills before
replacing them; keep one active copy of each procedural owner. It will flag an old
`orchestrator` installation rather than leave two competing entrypoints. Update any project
instructions that explicitly invoke that old skill name to `turn-to-life` after migration.
Global skills and global discovery rules are never modified. If older global instructions
conflict, resolve those explicitly; local installation does not erase them. Do not delete
the canonical source behind a shared skill symlink. Obsolete `diagnose` copies
from earlier collections are not removed automatically; review and archive them separately.

</details>

## Contribute

Keep purpose in [LOGIC.md](LOGIC.md), procedure in the responsible skill, and conditional
detail behind a relevant link. Do not add a rule without a decision it improves or a failure
it prevents. Run `python3 -m unittest discover -s tests` before proposing installer changes.

## License and attribution

[MIT](LICENSE). `wait-what` is Matt Pocock's skill, preserved verbatim with its
[notice](skills/wait-what/NOTICE.md) and [license](skills/wait-what/LICENSE).
The collection's explanatory and integration material is maintained here.

---

<p align="center"><sub>Effort with purpose.</sub></p>
