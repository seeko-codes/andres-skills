# Vertical slices as replaceable components

The Lego principle: consumers depend on the public contract, so a compatible implementation
can replace the component without rewriting those consumers. A vertical slice is a work
assignment; its implementation deliverable should have a coherent replaceable boundary.
Research, contract-setting, and integration assignments need not create artificial plugins.

## Define the connection points

For each implementation component, record only what is relevant:

- Responsibility and public inputs/outputs, including behavior and error semantics.
- Explicit provided/required interfaces and the location where implementations are selected.
- Owned state and resources, lifecycle, and any externally visible side effects.
- Compatibility constraints and any required state migration when replacing it.

Keep internals private. Other slices must not import private details or mutate its owned
state behind the contract. Inject dependencies or connect through explicit interfaces;
central wiring/registration has an assigned owner so concurrent slices do not collide there.
Use existing functions, modules, interfaces, or adapters when sufficient. Do not impose
separate packages, services, dynamic loading, version machinery, or a generic plugin framework
without a concrete need. Replaceability does not imply live hot-swapping or migration-free replacement.

## Explore the seam; harden the contract

During exploration, try the simplest boundary and wiring that tests the arrangement.
Interfaces can change with manager coordination; do not freeze a speculative abstraction
merely to claim modularity. The coherence gate assesses whether the boundary is useful.

During hardening, check behavior through the public contract, avoiding tests coupled to
private structure. Demonstrate substitution with an available alternative or a meaningful
test double at the wiring point: consumers should remain unchanged. A test double checks
dependency separation; it does not prove a future implementation's compatibility. Run the
same contract checks on actual replacements and verify composition, side effects, and state.
Do not build an unnecessary second production implementation merely to demonstrate swapping.

If replacement requires consumer rewrites, identify a leaked dependency or an intentional
contract change. The manager owns changes affecting other slices and plans affected tests,
consumers, and migrations. Report the limitation rather than promising universal interchangeability.
