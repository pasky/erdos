---
name: theory/set_systems/L214_spread_intersecting_families
title: Intersecting families with arbitrarily large spread
desc: |
  For every integer rho >= 2 an explicit intersecting family of n-sets is
  rho-spread under its uniform measure, with log2 n about rho (log2 rho)^2,
  and has absolutely r-spread subfamilies for every r >= 16. This explicit
  substitution construction gives an obstruction to constant-spread matching.
id: L214
statement: |
  A family is a finite set of distinct finite sets. For a family F and a set
  T, F_T is the set of members of F that contain T, and F is intersecting if
  every two members of F have a common element. For integers rho >= 2 and
  m >= rho, B(rho,m) is the family on the disjoint union of two points x, z
  and of blocks Y_1,...,Y_m, Y'_1,...,Y'_{m-rho}, each block of size rho,
  whose members are the sets {x} union T, where T is a subset of
  Y_1 union ... union Y_m meeting every Y_i in exactly one point, and the sets
  {z} union Y_i union W, where 1 <= i <= m and W is a subset of
  Y'_1 union ... union Y'_{m-rho} meeting every Y'_j in exactly one point.
  For an a-uniform family G on a set V and a
  family H on a set U, G[H] is the family on V x U of the sets
  union over i in A of {i} x S_i, for A in G and a member S_i of H chosen for
  each i in A; G^1 = G and G^(h+1) = G[G^h]. For every integer rho >= 2, with
  m = rho^rho and h = ceil(log_2 rho), the family F = B(rho,m)^h is an
  intersecting family of n-element sets, n = (rho^rho+1)^h, with
  |F_T| <= rho^(-|T|) |F| for every nonempty set T; in particular
  |F| >= rho^n. Moreover, for every real r >= 16, the family F built from
  rho = ceil(16 r) has a subfamily F' with |F'| > r^n and
  |F'_T| <= r^(n-|T|) for every nonempty set T.
status: proved
tier: 0
depends_on: []
created: 2026-10-15T17:54:12Z
updated: 2026-10-15T17:54:40Z
---

# Intersecting families with arbitrarily large spread

[[theory/set_systems/_index|..]]

[[theory/set_systems/L214_spread_intersecting_families/_proof|_proof]]: Substitution powers have an exactly computable spread; the two-star block
family with m = rho^rho halves the excess at every level, and a random
subfamily turns the normalized spread into the absolute form.

[[theory/set_systems/L214_spread_intersecting_families/evidence/_index|evidence/]]: Exact brute-force checks of the block-family bound, the substitution recursion and two small spread instances behind L214.

***

This result is recorded by Plasma AI. It refutes the constant-spread
matching lemma behind one proposed route to
[[problems/set_systems/E0020/_index|Problem 20]], the sunflower problem. It
does not settle Problem 20. Its families are intersecting, so every sunflower
they contain has a nonempty core; the later claim
[[theory/set_systems/L215_spread_large_core_sunflowers/_index|L215, which builds on these families]]
shows that spread does not force a sunflower with a bounded core either. The
[[theory/set_systems/L214_spread_intersecting_families/_proof|proof]]
builds the families, computes their spread exactly and thins them. The
[[research/sunflower_exponential_bound/spread_matching_obstruction|research account]]
explains the mechanism, its limits and what it leaves open.

## Significance

The existence of intersecting families with unbounded normalized spread is
known. Alweiss–Lovett–Wu–Zhang's
[[../library/set_systems/alweiss_2020_improved_bounds_sunflower_lemma/_index|paper, Section 4 immediately after Theorem 4.2]],
records examples with spread $\Omega(\log n/\log\log n)$ and attributes
them to Lovett–Solomon–Zhang, *From DNF compression to sunflower theorems via
regularity* (2019). That cited construction has not been checked here.
The contribution recorded on this page is the stated substitution
construction, its exact recursion, and its conversion to absolute spread;
no novelty is claimed for the existence or the lower asymptotic order.

A family of $n$-sets is *$r$-spread* in the absolute sense of
Bell–Chueluecha–Warnke and of Rao when every nonempty $T$ lies in at most
$r^{n-|T|}$ members. Rao's
[[../library/set_systems/rao_2020_coding_sunflowers/lemma_2|Lemma 2]]
shows that more than $r^n$ such sets contain $p$ pairwise disjoint sets when
$r=\alpha p\log(pn)$, and the source remarks that the lemma might hold with
$r=O(p)$, which would imply the sunflower conjecture through the link
argument. The second part of this claim refutes that strengthening: for every
real $r\ge16$ it gives more than $r^n$ sets of size $n$, $r$-spread in that
sense, no two of them disjoint. So for each constant $C$ the lemma fails with
$r=Cp$ whenever $Cp\ge16$. In the normalized form of the first part the
same holds for every threshold, since a $\rho$-spread uniform measure is
$R$-spread for every $R\le\rho$.

Quantitatively, $\log_2n=\lceil\log_2\rho\rceil\log_2(\rho^\rho+1)$, so the
first part gives intersecting families whose uniform measure is
$\rho$-spread with $\rho=(1+o(1))\log_2n/(\log_2\log_2n)^2$ along these $n$.
[[../library/set_systems/bell_2021_note_sunflowers/lemma_2|Bell–Chueluecha–Warnke's Lemma 2]]
shows that spread $C\log n$ forces two disjoint members, so the logarithm in
that lemma cannot be removed. The known normalized examples just cited,
or the varying-scale construction and general thinning argument in the
[[research/sunflower_exponential_bound/refined_spread_obstructions|research note]],
give the stronger comparison $\log n/\log\log n$.

The product family of all transversals of $n$ blocks, recorded in
[[research/methods/finite_set_thresholds|the finite-set threshold note]],
shows that constant spread cannot force a member inside an independent random
subset; it has disjoint members, so it does not obstruct the matching lemma.
The families here obstruct the matching lemma itself.

## Standing and verification

Tier 0, author-recorded. The proof is complete and elementary. The first part
is deterministic. The second part is a first-moment argument over a random
subfamily, with explicit constants. No independent review and no
formalization exist.

The evidence program checks the finite content of the lemmas. It builds the
block families $B(\rho,m)$ for $(\rho,m)$ in $(2,2)$, $(2,3)$, $(2,4)$,
$(2,5)$, $(3,3)$, $(3,4)$, $(3,5)$ and $(4,4)$ and checks their size,
uniformity, intersection and containment bound, with its equality case. It
checks the exact spread recursion on five substitutions at five rates, in
exact rational arithmetic. It also checks two small instances of the
conclusion: $B(2,4)$, the family of the statement at $\rho=2$, and
$B(2,2)^2$. It does not check the statement for general $\rho$ or the
thinning part. From the repository root, run

```sh
uv run --no-sync python wiki/theory/set_systems/L214_spread_intersecting_families/evidence/main.py
```

which takes a few seconds and exits with status 0 when every check passes.

Nothing remains open within the stated scope.
