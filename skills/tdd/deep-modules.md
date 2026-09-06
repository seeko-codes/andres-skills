# Deep modules

Ousterhout’s deep-module principle favors an interface that is simple to understand while
hiding substantial useful implementation complexity. It is about the abstraction the caller
must understand, not maximizing lines of code behind the fewest possible methods.

For a vertical slice, keep decisions that change together behind its contract. Other slices
should not need those internal choices. Preserve a boundary that makes the implementation
easy to replace; combine components only when their coupling justifies it. A thin adapter
can still be useful when it isolates an external dependency.

See the author’s source in [REFERENCES.md](REFERENCES.md) if the design principle is unclear.
