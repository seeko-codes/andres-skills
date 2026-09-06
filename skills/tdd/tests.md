# Tests of replaceable implementations

Derive expected behavior from the contract, not the implementation's own explanation.
Exercise the interface that exposes that behavior and assert the outcome callers depend on.
Tests should survive replacing a slice with another implementation of the same contract.

An internal method rename should not break a behavior test. Conversely, persistence,
ordering, call counts, or exact messages may warrant direct assertions when the requirement
actually includes them. A database check is legitimate for a persistence requirement;
a round trip through the public API tests a different observable contract. Choose deliberately.

Keep each test focused on one behavior; use enough assertions to establish it. Do not
add redundant tests or forbid useful checks solely because they use a particular technique.
