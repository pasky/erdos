---
name: research/erdos_774/evidence/prime_circuit
title: Exact checks of the eight- and twenty-point prime-tensor circuits
desc: Exact minors and kernel checks certify the displayed seed circuit in S_3 x S_3 x S_3 and its twenty-point dissociated lift in S_3 x S_5 x S_7.
tags: [E0774, computational, proved, tensor]
sources: []
created: 2026-09-24T23:30:00Z
updated: 2026-09-24T23:30:00Z
---

# Exact checks of the eight- and twenty-point prime-tensor circuits

[[research/erdos_774/evidence/_index|..]]

***

## Purpose

The [twenty-point circuit page](../../lemmas/prime_tensor_circuit.md)
exhibits a dissociated rational circuit in $S_3\otimes S_5\otimes S_7$ of
rank nineteen with a saturated column lattice and a primitive relation
having one coefficient of magnitude two. Its algebraic argument is the
durable justification; this probe checks the displayed matrices exactly.

## What is checked

Run, from the repository root,

```sh
uv run --no-sync python wiki/research/erdos_774/evidence/prime_circuit/main.py
```

The [checker](main.py) constructs only two prescribed matrices and three
prescribed minors, using exact Bareiss elimination, the standard library
and the shared root `tools` checker; it performs no search and finishes in
under a second. Its named checks are:

- the eight-point seed in $S_3\otimes S_3\otimes S_3$ gives an $8\times8$
  matrix, its coefficient vector $(-1,1,-1,1,-1,1,-1,-2)$ is a zero
  relation, and its prescribed $7\times7$ minor equals $-1$;
- the twenty-point lift has twenty distinct labels, gives a $48\times20$
  matrix, its displayed coefficient vector is a zero relation, and its two
  prescribed $19\times19$ minors equal $2$ and $-1$;
- both relations have full support, a unit coefficient, and a coefficient
  $-2$.

A nonzero $(n-1)$-minor with a full-support relation proves a rational
circuit; a unit coefficient makes the displayed integer relation primitive,
and its coefficient two excludes every nonzero ternary relation. A failed
clause exits nonzero. The lemma page states the exact scope: the seed check
inspected at most 64 rank-seven minors, and neither computation is a search
for unbounded coloring.

## Retained exploratory probes

Two bounded enumerations preceded the graph-cut circuits of the
[prime staircase](../../lemmas/prime_staircase_obstruction.md), which made
them unnecessary. They are recorded observations, not inputs to any
theorem; the checker above does not run them, and their arithmetic is
short enough to repeat with a few lines of code.

**Powers of $1+\sqrt2$ through ten columns.** The question was whether
algebraic integrality and being a unit, without the root-of-unity
conjugate constraints, could exclude mandatory coordinates. For each
$n=3,\ldots,10$, encode $\beta^j$, $0\le j<n$, for $\beta=1+\sqrt2$ by
the integer pair $(a_j,b_j)$ with

$$
(a_0,b_0)=(1,0),\qquad
(a_{j+1},b_{j+1})=(a_j+2b_j,a_j+b_j),
$$

enumerate all $\epsilon\in\{-1,0,1\}^n$, group them by the exact integer
pair $\sum_j\epsilon_j(a_j,b_j)$, and intersect the support bitmasks
within each group. For every $n$ from $3$ to $10$, only the zero
coefficient vector maps to zero, and every nonzero value group has
nonempty support intersection; the enumeration covered
$\sum_{n=3}^{10}3^n=88{,}560$ vectors. A separate pass at $n=6$ over its
$729$ vectors found $336$ distinct nonzero value classes. No infinite
conclusion is drawn: these powers are not roots of unity, and the
staircase's mandatory-coordinate proof does not use them.

**Twenty-seven seed layer choices.** The question was whether duplicating
one old layer in each seed coordinate could keep the circuit size linear
in three growing side lengths. For the eight-point seed
$\{000,012,021,102,110,211,222,001\}$ of the
[twenty-point circuit page](../../lemmas/prime_tensor_circuit.md),
enumerate all $a\in\{0,1,2\}^3$ and test whether each seed point agrees
with $a$ in at most one coordinate. None of the $27$ choices passes, after
at most $27\cdot8=216$ point-choice comparisons. This rules out only that
particular no-cross-duplication condition, not linear-size circuits, which
the staircase's graph-cut construction then supplied directly, with no
further search.
