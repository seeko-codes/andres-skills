# Interface design for testability

Choose interfaces from the behavior and replacement boundary. Make relevant external
inputs controllable through parameters or dependency injection when needed for a reliable
check. Pure calculations can return values; stateful behavior and external effects remain
valid when required by the contract.

Keep the interface understandable and implementation choices private. Fewer methods or
parameters are not goals by themselves: do not hide required behavior or introduce a new
abstraction merely to reduce a count. Testability should support the design, not replace
its requirements.
