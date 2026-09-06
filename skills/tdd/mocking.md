# Test doubles and real boundaries

Prefer real collaborators when they are practical and deterministic. Use a fake, stub,
spy, or mock to control a boundary relevant to the test, such as network responses,
time, randomness, or a costly dependency. Avoid mocks that merely reproduce internal
implementation structure and break whenever that structure changes.

Introduce injection where it makes the required behavior controllable; do not require a
new abstraction around every call. Assert interactions when the interaction itself is part
of the contract. Separately check relevant real integration: a passing mock-based test
establishes behavior under its assumptions, not that the external system satisfies them.
