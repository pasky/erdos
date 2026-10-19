---
name: theory/integer_sequences/L124_flat_cyclotomic_degree_ratio
title: No signed vanishing sum of odd squarefree roots of unity fits in a short arc
desc: |
  Open: the least degree of a {-1,0,1} multiple of the M-th cyclotomic
  polynomial is at least a fixed positive fraction of M for all odd
  squarefree M; a proof would bound the dissociated coloring number of
  every distinct-prime tensor grid of Problem 774.
tags: []
sources:
- problems/integer_sequences/E0774
id: L124
statement: |
  For an integer M > 1 let D(M) be the least degree of a nonzero polynomial
  with coefficients in {-1, 0, 1} that is divisible by the M-th cyclotomic
  polynomial. There is a real number c > 0 such that D(M) >= c*M for every
  odd squarefree integer M > 1. Equivalently, there is e > 0 such that no
  sum of the form s_1*w_1 + ... + s_n*w_n with n >= 1, signs s_i in {-1, 1}
  and distinct roots of unity w_i of odd squarefree order whose arguments
  all lie in one closed interval of length 2*pi*e is zero.
status: open
depends_on: []
created: 2026-10-15T11:14:17Z
updated: 2026-10-15T11:14:17Z
---

# No signed vanishing sum of odd squarefree roots of unity fits in a short arc

[[theory/integer_sequences/_index|..]]

***

This open claim is recorded by Plasma AI. It asks for a uniform obstruction to the
distinct-prime tensor route to
[[problems/integer_sequences/E0774/_index|Problem 774]]. By
[[theory/integer_sequences/L123_odd_root_arc_colorings/_index|L123, part (3), a positive constant c bounds the dissociated coloring of all roots of unity of odd squarefree order by the ceiling of 1/c]],
so it bounds the coloring number of every grid
$S_3\otimes S_5\otimes\cdots\otimes S_{p_k}$, and that family could not
supply the counterexample sought there. Conversely, unbounded coloring of
those grids, the missing theorem of the
[[research/erdos_774/proof_sketch|main argument]], would refute this claim.
The claim is a statement about cyclotomic polynomials alone; it uses no
coloring hypothesis.

## Equivalence of the two forms

Choose $P=\sum_{j\le D}s_jx^j$ of minimum degree $D=D(M)$ among the nonzero
multiples of $\Phi_M$ with coefficients in $\{-1,0,1\}$. Since
$1+x+\cdots+x^{M-1}$ is such a multiple, $D<M$. The roots
$e^{2\pi\mathrm ij/M}$
with $s_j\ne0$ are distinct, of odd squarefree order dividing $M$, lie in the
closed arc of arguments $[0,2\pi D/M]$, and carry the vanishing signed sum
$P(e^{2\pi i/M})=0$. Conversely, a vanishing signed sum of distinct roots of
odd squarefree orders lies in $\mu_M$ for the least common multiple $M>1$
of those orders; rotating it so that the first root of the arc is $1$ gives
such a polynomial of degree at most $eM$ when the arc has length $2\pi e$.
So the first form with constant $c$ implies the second with any $e<c$, and
the second with $e$ implies the first with $c=e$.

## Standing

Open. Neither a proof nor a counterexample is known here. A literature
search on 2026-10-15 for least-degree multiples of cyclotomic polynomials
with restricted coefficients, and for vanishing sums of roots of unity in
arcs, found no result that settles it. It found the nonnegative-coefficient
problem of
[[../library/number_theory/steinberger_2012_lowest_degree_polynomial_nonnegative_coefficients_divisible_by_n_th_cyclotomic_polynomial/_index|Steinberger]],
where for the orders its Theorem 1 covers the least degree is
$(p-1)n/p$ with $p$ the least prime factor of $n$, and A. S. Reddy's
arXiv preprint 1106.1271, which treats $0,1$-polynomials only for even
orders with at most three prime factors; neither concerns signed
multiples. An incomplete search does not establish novelty. The
[[research/erdos_774/routes/angular_colorings|research account]] records the
evidence: the exact values $D(15)/15=8/15$ and $D(105)/105=7/15$, an
explicit flat multiple showing $D(1155)\le502$, the structure that any
counterexample family must have, and heuristics in both directions. The
largest constant compatible with those values is at most $502/1155$.

## Remaining obligations

- [ ] Prove or refute the statement. A refutation needs, for every $e>0$,
  a vanishing signed sum of distinct roots of odd squarefree order inside
  an arc of length $2\pi e$; by the research account's layer lemma, each
  strict improvement over a subconductor must have a nonzero common layer
  value in that prime direction, and every minimal vanishing subsum of such
  a sum has a reduced exponent of totient ratio at most $e$.
- [ ] A proof with $c\ge1/3$ would show that the dissociated coloring
  number of every distinct-prime grid from $S_3\otimes S_5\otimes S_7$ on
  is exactly three; the bracket $3\le\chi\le4$ at the prime 23 is the first
  case it would decide.
