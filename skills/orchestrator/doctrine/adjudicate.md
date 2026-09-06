# Independent review

Review the assigned target against requirements and risk. Establish relevant expected
properties from the contract before relying on the implementation's explanation. Attempt
to find counterexamples, dropped requirements, dependency mismatches, and integration defects.

For batch review, inspect the composed result: individually valid slices may still disagree.
For implementation boundaries, check public-contract compatibility, private-detail leaks,
explicit wiring, owned state, and replacement evidence. Distinguish a test double
demonstration from compatibility of a real replacement; see [components.md](components.md).
Use an independent context with sufficient capability; a reviewer label alone adds no expertise.
Report a verdict, evidence, severity of findings, uncertainty, and checks that could resolve it.
Agreement with a prediction is not proof. Do not rewrite outside an explicitly assigned write-set.
