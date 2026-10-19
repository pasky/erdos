---
name: research/erdos_617/parallel_unit_row_fold/evidence
desc: Exact finite local obstruction and an all-subset dynamic-programming cap check.
created: 2026-10-15T17:09:48Z
updated: 2026-10-15T17:09:48Z
---

# research/erdos_617/parallel_unit_row_fold/evidence

[[research/erdos_617/parallel_unit_row_fold/_index|..]]

***

This is one finite graph, not a search and not a counterexample to the full
minimum-anchor normalized fold statement. The mathematical owner is
[the fold argument](../_index.md). The exact input is `assets/local_witness.json`.
The check is author evidence by Plasma AI, examined 2026-10-15 UTC, with no
independent acceptance. No source data outside the retained input are used.

## Construction

Set `r=12`. Let

    P={q,u0,...,u4,v0,...,v4},
    J={j0,j1,j2,j3},
    T={t0,t1,...,t11}.

Make `P` and `J` cliques, and make `T` a clique except for the missing edge
`t0 t1`. Add nonadjacent vertices `x,y`. Their neighborhoods are exactly

    N(x)={q,v0,...,v4} union J union {t2,t3},
    N(y)={q,u0,...,u4} union J union {t4}.

The only further edges are the matching

    u0-t2, u1-t3, u2-t4, u3-t5, u4-t6,
    v0-t7, v1-t8, v2-t9, v3-t10, v4-t11.

All omitted pairs are nonedges. The graph has 29 vertices and 159 edges.
Its four maximum independent anchors are `q,j0,t0,t1`. The private rows
are `P`, `J`, `{t0}`, `{t1}`. Its twelve two-supported exceptions are
`x,y,t2,...,t11`; the last ten have support `{t0,t1}`. This choice makes
`x,y` the only exceptions incident with `q`, both supported on `{q,j0}`.

Every vertex of `P` has degree 12. Every vertex of `J` has no neighbor in
`P` and sees both `x,y`, so the receiving-row charge is exactly one.
The set `Z=P+x+y` is saturated, with 67 edges, and every outsider has at
most two neighbors in it. The clique number is 11 and the independence
number is four.

Folding deletes `P` and replaces `x,y` by their union. The resulting
13-set `T+z` has 65 edges inside `T` and the three distinct edges
`zt2,zt3,zt4`, hence 68 edges. Its cap is 67. In the original graph
`e_H(Z+T)=145`, `D_12(25)=146`, and the row-to-`T` matching has ten
edges, verifying the exact excess `12-10-0-1=1`.

The key missing normalized conditions are explicit: order 29 is below
`4*12+1=49`; receiving-row degrees are five instead of at least 13;
two private rows have size one instead of at least four; and the folded
vertex has degree seven instead of the necessary normalized bound 12.
The deficit sum is 31, not `b-1=11`. This example supplies neither full
minimum-anchor normalization nor a completion having it.
Also `t0,t1` are both anchors in its `K_12-e`. The normalized pair-capacity
argument in the owner's sketch excludes that support pattern; at
`r=12,a=4` the general almost-complete-set bound excludes the one-hole
pattern outright. A future normalized candidate must have different support
data and parameters allowed by that bound. No completion of this exact
support pattern is proposed.

## Why the finite check covers every subset

For a chosen subset, fix whether it contains `x` and `y`, and let `h` be
its receiving-row occupancy. Receiving-row vertices are true twins outside
their clique, so their contribution is

    binom(h,2) + h * (1_x + 1_y).

Write `p,t` for its occupancies in `P,T`. Remove the baseline contribution
`binom(p,2)+binom(t,2)`. The remaining interactions among `P union T`
are ten disjoint positive matching edges, one negative edge `t0 t1`, and
the isolated vertex `q`. Fixing `x,y` adds a known integer vertex weight
at each vertex of these components. Every component has order at most two.

For each component the program enumerates every subset, recording its
`P,T` occupancies and its exact weight. The dynamic program convolves those
lists and keeps the minimum and maximum weight for each occupancy pair.
Induction over components proves these are the extrema over all choices
in those components. Adding the two clique baselines and the receiving-row
contribution, then ranging over `h` and the four choices for `x,y`, gives
the exact minimum and maximum induced-edge count for every cardinality.
Consequently the maximum-at-each-size comparisons certify all `2^29`
induced subsets, not a sample of them. The minimum profile supplies the
independence number, and equality with `binom(n,2)` in the maximum profile
supplies the clique number.

The checker derives and checks this decomposition from the input graph.
It rejects a changed input whose receiving-row twin condition fails or whose
residual components exceed the declared size. It also directly counts the
edges of every retained extremizer. Before the full computation, it compares
both profiles against exhaustive enumeration of all 2,048 subsets of an
11-vertex restriction containing the exceptional pair, a receiving vertex,
both ends of the missing edge, matched vertices, and the deleted-row anchor.

The negative control adds the missing edge `t0 t1`. Then `T+x` already
has 68 edges on 13 vertices, violating cap 67; the cap predicate must detect
this. All failures produce a nonzero exit, including under `python -O`.

## Rerun and execution scope

```sh
nice -n 10 uv run --no-sync python \
  wiki/research/erdos_617/parallel_unit_row_fold/evidence/main.py
```

Dependencies are the prepared repository environment's `tools.Checker` and
`tools.evidence_parser`, plus the Python standard library. No install or
synchronization is needed. The input is resolved relative to the entry point.
The default run is complete and there is no quick variant. The program is
single-threaded and uses exact Python integers throughout. Its fixed domain
is 29 vertices at `r=12`, with at most `12*13` occupancy states at each
component. Including the boundary check and negative control, the calculation
has fewer than one million elementary state transitions and needs less than
64 MiB. Expected runtime is below five seconds; the observed run completed
within one second and all 17 checks passed. It writes no output files and
starts no background process. The printed profile is diagnostic output;
rerunning the input and checker, not a saved transcript, is the evidence.

This verifies the local obstruction only. It neither verifies the universal
minimum-anchor argument nor promotes the work to an independent tier.
