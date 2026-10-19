---
name: theory/set_systems/L215_spread_large_core_sunflowers
title: Spread families whose sunflowers all have large cores
desc: |
  For every real R >= 3 and integer g >= 0 an explicit intersecting family is
  R-spread under its uniform measure while every k-sunflower in it, for every
  k >= 3, has a core of at least 2^g points; no bounded-core sunflower lemma
  follows from spread.
id: L215
statement: |
  Use the definitions of L214: families, F_T, intersecting families, the
  block family B(rho,m), the substitution G[H] and the powers G^h. Let D be
  the family of the three 2-element subsets of a 3-element set, let D^0 be
  the family whose only member is a one-point set, D^1 = D and
  D^(g+1) = D[D^g]. For an integer k >= 2, a k-sunflower in a family is a
  set of k distinct members whose pairwise intersections are all equal to
  one set, its core. For every integer g >= 0 and every real R >= 3, put
  rho = ceil(3 (R/3)^(2^g)) and j = ceil(log_2 rho). Then the family
  F = (B(rho,rho^rho)^j)[D^g] is an intersecting family of n-element sets,
  n = 2^g (rho^rho+1)^j, with |F_T| <= R^(-|T|) |F| for every nonempty set
  T, and for every integer k >= 3 every k-sunflower in F has a core of at
  least 2^g elements.
status: proved
tier: 0
depends_on:
- L214
created: 2026-10-15T18:17:48Z
updated: 2026-10-15T18:18:06Z
---

# Spread families whose sunflowers all have large cores

[[theory/set_systems/_index|..]]

[[theory/set_systems/L215_spread_large_core_sunflowers/_proof|_proof]]: Powers of the triangle are intersecting and sunflower-free with an exactly
computable excess; substituting them into block-family powers makes every
sunflower core a union of whole inner members, while the block levels
absorb the excess.

[[theory/set_systems/L215_spread_large_core_sunflowers/evidence/_index|evidence/]]: Exact checks of the triangle powers, the core lemma on two small substitutions and the spread recursion behind L215.

***

This result is recorded by Plasma AI. It sharpens
[[theory/set_systems/L214_spread_intersecting_families/_index|L214, which shows that spread does not force two disjoint members]],
in the direction that matters for
[[problems/set_systems/E0020/_index|Problem 20]]: spread does not force a
sunflower with a small core either. It does not settle Problem 20, and its
families do contain $k$-sunflowers for every $k\le\rho$. The
[[theory/set_systems/L215_spread_large_core_sunflowers/_proof|proof]] gives
the core lemma and the spread computation. The
[[research/sunflower_exponential_bound/proof_sketch|proof sketch for Problem 20]]
records what this leaves for an attack.

## Significance

Problem 20 is equivalent to the statement that, for each $k\ge3$, families
that are spread enough contain a $k$-sunflower. That equivalence is the link
argument recorded in the research. L214 shows that the sunflower cannot always
have an empty core. This claim shows more: for every spread $R$ and every
bound $s$, some intersecting family with $R$-spread uniform measure has no
$k$-sunflower with a core of fewer than $s$ points. So no statement of the form
"spread at least $R_k$ forces a $k$-sunflower whose core has at most $s_k$
points", with $R_k$ and $s_k$ independent of the set size, can hold. Along
these families, at fixed $R>3$, every core has at least about
$\log_2\log_2n/\log_2(R/3)$ points. Cores of exactly $2^g$ points occur, so
the bound is attained in each family.

The mechanism is a substitution of the powers of the triangle, which are
intersecting and contain no $3$-sunflower, into the block-family powers of L214.
Every sunflower of the result has its core made of whole members of the inner
family, while the outer levels halve the excess that the inner family carries.

**Dependency roles.** From
[[theory/set_systems/L214_spread_intersecting_families/_index|L214]] this
claim uses the definitions in its statement and, in the proof, Lemma 1
(substitution keeps a family uniform and intersecting), Lemma 2 (the exact
spread recursion $E_{G[H]}(R)=\psi_G(E_H(R))$) and Lemma 3 (the block-family
bound, which gives $\psi_B(E)\le E/2$ for $E\le\rho$ when $m=\rho^\rho$),
all from
[[theory/set_systems/L214_spread_intersecting_families/_proof|the L214 proof]].

## Standing and verification

Tier 0, author-recorded. The proof is complete, elementary and deterministic.
No independent review and no formalization exist. The claim's statement is
in the normalized convention. The separate
[[research/sunflower_exponential_bound/refined_spread_obstructions|thinning argument without a family-size cap]]
gives the corresponding absolute-spread obstruction at author standing;
it is a consequence recorded in research, not an additional clause of
this claim's statement.

The evidence program checks, by exhaustive or core-by-core search in exact
arithmetic, that $D$, $D^2$ and $D^3$ are intersecting and free of $3$- and
$4$-sunflowers, and that the excess of $D$ and $D^2$ matches Lemma A at three
rates. It checks Lemma B on $B(3,3)[D]$ and $B(2,3)[D]$: both are intersecting
and free of $4$-sunflowers, and their smallest $3$-sunflower cores have exactly
$2$ and $4$ points. These are the predicted values, since every
$3$-sunflower of $B(2,3)$ has a core of two points. It also checks the spread
recursion on $B(3,3)[D]$ at five rates. It does not check the statement for
general $g$ and $R$. From the repository root, run

```sh
uv run --no-sync python wiki/theory/set_systems/L215_spread_large_core_sunflowers/evidence/main.py
```

which takes a few seconds and exits with status 0 when every check passes.

Nothing remains open within the stated scope.
