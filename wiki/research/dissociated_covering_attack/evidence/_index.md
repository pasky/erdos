---
name: research/dissociated_covering_attack/evidence
title: Exact small cases for twisted layers
desc: Exact arithmetic checks the relations and proper 2-colorings of the 15th roots of unity, a nine-layer two-color certificate, the root spans of arc classes below the rank threshold, signed-pair and signed-triple survival under coordinate twists, the failure of two arcs at 165 and 195, the diverging first moment, and exhaustive survival sets at 105 for arc and layered classes.
tags: [E0774, computational, tensor]
sources: []
created: 2026-10-15T17:59:57Z
updated: 2026-10-15T17:59:57Z
---

# Exact small cases for twisted layers

[[research/dissociated_covering_attack/_index|..]]

***

## Purpose

The [twisted-layer note](../layer_race.md) uses a handful of finite facts:
the structure of the proper 2-colorings of $\mu_{15}$, a family of nine
layer colorings with trivial signed-span intersections, the root-span
fraction of arc classes below the rank threshold, the survival of signed
pairs and triples of roots under coordinate twists, the least flat-multiple
degrees $D(165)$ and $D(195)$, the numbers behind Lemma 7, the lower
bound on the first moment of common values, and survival sets of signed
sums under all coordinate twists at 105. This probe checks them exactly. It proves no
statement about larger conductors; the race model that these numbers
inform is a heuristic.

## What is checked

Run, from the repository root,

```sh
uv run --no-sync python wiki/research/dissociated_covering_attack/evidence/main.py
```

The [checker](main.py) uses exact integer arithmetic (NumPy int64 arrays
with bounds checked before arithmetic), exact rational logarithm enclosures,
the standard library and the shared root
`tools` checker. The full run takes about twenty minutes, most of it at
the conductor $255255$; `--quick` omits that conductor and the seeded parts
of items 8 and 9 and takes under a minute. Before each coordinate recurrence,
the bound $\|v\|_\infty+|v_{d-1}|\max_{j<d}|\Phi_M[j]|$ is evaluated
with Python integers and required to be at most $2^{60}$. It bounds every
product and sum in the update. The stored coordinate tables also satisfy
$2M\max|v_{i,j}|\le2^{60}$, bounding every later signed sum and difference
in the fixed input domain. Its named checks are:

1. **$\mu_{15}$.** Enumerating all $3^{15}$ signed vectors gives 446 nonzero
   signed relations with 127 supports, 98 of them minimal, of sizes 3, 5,
   6, 7, 8 and 9; the largest dissociated subsets have 8 elements; there
   are 1440 proper 2-colorings, all with classes of sizes 7 and 8; the
   minimal supports are invariant under the 720 coordinate permutations of
   $\mathbb Z/3\times\mathbb Z/5$, and the colorings form four orbits of 360.
   In every coloring the 8-element class signed-spans all 15 roots, and the
   7-element class spans 9 roots in 360 colorings and 11 roots in the other
   1080.
2. **Nine layers.** The nine labeled colorings in
   `assets/nine_layers.json` are proper, and the successive signed-span
   intersections of their classes shrink to $\{0\}$ for both colors, with
   sizes 2187, 447, 117, 87, 29, 21, 7, 1, 1 for color 0 and 6561, 447,
   227, 67, 49, 13, 9, 7, 1 for color 1. By the layer criterion this gives
   $\tau_2(S_3\otimes S_5)\le9$.
3. **Arc classes.** For $M\in\{105,165,195,1155,15015,255255\}$ and
   $q\in\{3,4\}$, the arc of $\lceil M/q\rceil$ consecutive roots lies below
   the rank $\varphi(M)$ and no root outside it has power-basis coordinates
   in $\{-1,0,1\}$ supported on the arc, so the arc spans exactly its own
   roots.
4. **Signed pairs.** For the $q=3$ arc class at $M=105$ and $M=1155$, every
   ordered pair of distinct roots and each relative sign is tested; per
   agreement pattern of grid coordinates, the fraction inside the arc's
   signed span is $1/3$ for pairs on one coset of $\mu_3$ with sign $+1$,
   and at most $2/15$ for every other pattern and sign, the maximum being
   attained.
5. **Two arcs at 165 and 195.** $\Phi_{165}$ and $\Phi_{195}$ have height two
   and $(1-x)\Phi_{165}$, $(1-x)\Phi_{195}$ are flat, so $D(165)=81$ and
   $D(195)=97$ and two arcs are not proper there.
6. **Signed triples at 105.** For the $q=3$ arc class at $M=105$, every
   ordered triple of distinct roots and each sign pattern is tested, and
   the orbits under coordinate twists are read off from the equality types
   of the three residues at each prime. Leaving out the orbits whose values
   visibly have lower complexity (two equally signed points on one coset of
   $\mu_3$, a whole coset of $\mu_3$, or three equally signed points on one
   coset of $\mu_5$), every orbit survives with probability at most $4/45$,
   and every orbit with positive survival needs no more layers than the
   roots, that is $\lambda\le|O|^{-\log3/\log105}$, with $|O|$ counted as
   ordered triples (an overcount, which only strengthens the check).
   The logarithmic comparison uses rational intervals: after reducing an
   argument to $y\in[1,2)$ by powers of two, set $z=(y-1)/(y+1)$ and
   bound $\log y$ by the first 32 terms of
   $2\sum_{j\ge0}z^{2j+1}/(2j+1)$. The omitted tail is at most
   $2z^{65}/(65(1-z^2))$; the same series at $z=1/3$ bounds $\log2$.
   Upper bounds on $\log|O|\log(1/\kappa)$ are compared with lower
   bounds on $\log M\log(1/\lambda)$. An inconclusive interval fails
   the check; floating-point output is used only for display.
7. **The first moment of Lemma 7.** With $p$ the next prime and $|G_M|$ the
   product of the factorials of the primes of $M$, the lower bound
   $(2^{|C|}-1)/|G_M|^{p-1}$ exceeds $2^{12}$ for a class of
   $\lceil M/2\rceil$ roots at $M=1155$ and exceeds $2^{2479}$ for classes
   of $\lceil M/q\rceil$ roots at $M=15015$ and $q\in\{2,3,4\}$, by exact
   integer comparison; for $q=3$ at $M=1155$ it is below one, so the lemma
   says nothing there.
8. **Survival sets at 105.** For the arc class of 35 roots at $M=105$, and
   for a signed sum $F$ of some of its roots, the checker computes, over all
   $3!\,5!\,7!=3628800$ coordinate twists $g$, whether $\hat gF$ lies in the
   class's signed span; below the rank this means that its power-basis
   coordinates are in $\{-1,0,1\}$ and vanish outside the arc. The sums of
   the whole class, with all signs $+1$ and with alternating signs, survive
   exactly the identity and the reflection $e\mapsto34-e$, as Lemma 10 of
   the note predicts, with no other survivor. The full run adds seeded sums:
   twelve on 20, 22 and 24 points meet fewer than 11 of the 720 left cosets
   of the affine group (at most eight), each of four on 10 points meets at
   least 11 (29 to 415), and among ten on 17 points one meets at least 11
   cosets and one survives twists that move its support off the arc; the
   relation between each such twisted image and its representation inside
   the arc lies on at most three grid lines (cosets of some $\mu_p$). The
   threshold 11 is the next prime, the number of layers that Lemma 9 can use
   for the step to 1155.
9. **Survival sets of layered classes at 105.** Seven twists of
   $\mu_{15}$ drawn from a fixed seed layer the three arcs of $\mu_{15}$
   into a 3-coloring of $\mu_{105}$; the checker confirms by the layer
   criterion, with exact signed spans at 15, that it is proper and stays
   proper after deleting any one layer. Each class has 35 roots, linearly
   independent (rank 35 modulo the prime $2^{31}-1$). A separately checked
   right inverse modulo 65521 recovers the only possible ternary coefficient
   vector, and multiplication by the original integer matrix confirms it.
   This certifies rejection as well as acceptance without floating-point
   arithmetic. The sum of each whole class survives only
   the identity among all twists; in the full run, six seeded signed sums on
   20 class points survive at most two twists each (fewer than 11), and six
   on 10 class points survive 52 to 165 twists each.

## Inputs

`assets/nine_layers.json` lists the color-0 classes of the nine layers as
exponents $e$ of $\zeta_{15}^e$; color 1 is the complement. The family was
found by a greedy search over all proper 2-colorings of $\mu_{15}$; the
checker validates the retained family and does not repeat the search.

## Observations that are not certificates

For signed triples at $M=1155$ the note quotes a Monte Carlo estimate, 1500
random triples for each orbit of ordered triples and each sign pattern,
with a fixed seed; it is an estimate, not a check. Two further findings
come from an exact-coefficient integer program (HiGHS through SciPy, one
thread) and are solver verdicts only. The
layering of the nine colorings, padded by repetition to 11 and 13 layers,
gives 2-colorings of $\mu_{165}$ and $\mu_{195}$ in which the program found
no signed relation in either class, while it found one in an arc of
$\lceil N/2\rceil$ roots and in the layering with all layers equal; the
layer criterion and item 2 already prove these colorings proper. In the
coloring of $\mu_{165}$ the program found and checked representations of
71 of the 83 roots outside the 82-element class and of 70 of the 82 roots
outside the 83-element class, and declared the remaining 12 roots of each
unrepresentable.
