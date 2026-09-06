# Refactoring

Refactor to resolve a concrete design problem within the agreed scope while preserving
observable behavior. Candidates include duplication that should change together, leaked
implementation choices, or responsibilities that repeatedly require cross-slice coordination.

Names, length, or method counts can prompt inspection; they do not by themselves justify
extraction, merging, or a new abstraction. Keep replacement boundaries and the contract
intact. Check behavior before and after; broaden verification only for a remaining risk or
required project gate. Revisit the arrangement when a structural assumption fails.
