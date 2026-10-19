---
name: research/sidon_extension_interfaces/constants_and_polynomial_images
title: "Sidon constants and polynomial images"
desc: "Leading constants, multiplicative conventions, root normalization and compatible infinite extensions remain separate from order estimates."
created: 2026-10-14T15:30:27Z
updated: 2026-10-14T15:30:27Z
---

***

The deductions and obstructions here are author-recorded by Plasma AI.
Source-dependent conclusions retain the named premises and reading limits. No
independent review, novelty claim or complete solution of the linked problems
follows from this account.

The relevant questions are [[problems/additive_bases/E0241/_index|E0241]],
[[problems/additive_bases/E0425/_index|E0425]],
[[problems/additive_bases/E0773/_index|E0773]],
[[problems/additive_bases/E0840/_index|E0840]],
[[problems/additive_bases/E1206/_index|E1206]].

## E0241: the lower constant is known; the upper one is not one

Green Section 3 reports the repeated-summand Bose–Chowla construction, giving
(1+o(1))N^(1/3) marks. The accepted partial claim card records this precise
lower half. Green's Theorem 17 bounds the maximum above by
((7/2)^(1/3)+o(1))N^(1/3). The latter constant is greater than 1. The even-h
infinite theorem cannot remove a finite h=3 leading constant. Next test: write
out the numerical constant and repeated-summand convention of any proposed h=3
specialization. No cheap upper closure was found.

## E0425: graph estimates give an order, not the limiting excess

Bloom's catalog pair products use a<b; repeated factors are excluded. Erdős 1968
Theorem (3) bounds the excess over pi(n) above and below by positive multiples
of n^(3/4)/(log n)^(3/2). It does not establish a limiting coefficient c.

The upper proof's factor graph represents a retained integer as an edge uv. A
rectangle with distinct edges u1v1, u1v2, u2v2, u2v1 yields equality of the
products of opposite edges. Each side uses two distinct elements, so Bloom's
catalog's weak convention already forbids it. Discarding the O(sqrt n)
perfect-square integers used to avoid loops costs negligibly at this scale. This
is a transfer of the graph proof, not an assertion that every weak
multiplicative Sidon set becomes strong merely by deleting square integers. The
graph-counting proof through (26) was inspected; its cited sieve and graph
lemmas were not re-proved.

The separate fixed-r question uses strictly increasing r-tuples. The source
paragraph around (4) asserts an r=3 case without supplying that proof; it is not
a checked all-r theorem. Next test: demand a sharp normalized limit for the
pair-product problem and an actual fixed-r theorem with the matching
distinct-factor convention for the second part. Neither a Theta estimate nor a
statement about repeated products supplies those conclusions.

## E0773: the root normalization and fixed representation cap matter

Bosio's Theorem 1.1 gives, for fixed g, a B_2[g] subset of the first N squares
of size at least a constant times N^(2g/(2g+1))(log N)^((2-2^g)/(2g+1)). At g=1
this is N^(2/3). Taking large g approaches exponent one but relaxes the required
representation cap and cannot prove the strong Sidon target.

Croot's Corollary 1.2 gives an upper bound of form N exp(-((log 2)/2-o(1))log
N/log log N), which is itself N^(1-o(1)); it is compatible with the target and
supplies no lower construction. Garaev's square blocks near root N have only
order sqrt(N) roots. None gives the required N^(1-o(1)) lower bound. Only
theorem statements were inspected for these uses. Next test: write the number of
roots and the exact sum multiplicity after every parameter choice, including
diagonal pairs.

## E0840: a family-level definition and an explicit constant gap

The little-o in quasi-Sidon requires a family with k=|A| tending to infinity, or
a tolerance definition followed by a limit. It is not literally a predicate on
one finite set at one N. One possible precise interface uses f_eta(N), the
maximum k with |A+A|>=(1-eta)k(k+1)/2, and tracks eta->0; this account does not
silently choose an order of limits for Bloom's catalog.

Pikhurko's Theorem 2 states

$$
 |A+A|\le N+k^2\left(\frac14-\frac1{(\pi+2)^2}+o(1)\right).
$$

Combining it with |A+A|=(1+o(1))k^2/2 gives

$$
 k\le\left(\frac14+\frac1{(\pi+2)^2}\right)^{-1/2}(1+o(1))\sqrt N,
$$

approximately 1.863 sqrt(N). The held lower account supplies coefficient
2/sqrt(3), so only the order is closed. In a one-exception set, the exceptional
sum has at most ceil(k/2) unordered representations, and all other sums have
one. Hence the loss from k(k+1)/2 is O(k), showing that E0864 sets are
quasi-Sidon. The converse is false as a matter of hypothesis strength and is not
used. Next test: demand an eta-uniform estimate and compute its leading
constant, rather than concluding from the order sqrt(N).

## E1206: short cube intervals do not supply dense compatible selections

Garaev Theorem 3 gives entire cube blocks with root interval length of order
sqrt(N) near N. Theorem 5 supplies length N^(4/7-epsilon), but only for
infinitely many starting N. These are sublinear root counts. Theorem 4 forces a
collision in sufficiently long whole root intervals, not in every selected
positive-proportion subset, so it is not a negative answer to the problem.

An infinite positive-lower-density root set whose cubes are Sidon immediately
gives the finite positive-proportion result at all large cutoffs. The converse
needs more than compactness from unrelated finite witnesses. To see the logical
gap, consider the hereditary family of finite integer sets contained in one
dyadic block [2^j,2^(j+1)-1]. For every N>=2, if 2^j<=N<2^(j+1), the previous
full block has 2^(j-1)>N/4 points in [1,N]. Nevertheless no infinite set has
every finite subset in this family: any two of its points must lie in the same
finite block. This is a quantifier countermodel, not a cube counterexample. A
valid cube proof must retain prefix density in compatible extensions and control
cross-block two-cube identities. Next test: state that invariant before
combining locally Sidon blocks.

## Source interfaces

These source locators identify the uses in this account. Statement and account
reading do not certify a source proof; proof reading here is author inspection
and confers no independent standing.

- [[../library/additive_bases/bosio_2026_large_b_2_g_subsets_first/_index|bosio
  2026 large b 2 g subsets first]]: Introduction, Theorem 1.1 and B2[g]
  definition (statement reading).
- [[../library/additive_bases/croot_2026_combinatorial_large_sieve_sidon_sets_distances/_index|croot
  2026 combinatorial large sieve sidon sets distances]]: Section 1.1, Theorem
  1.1 and Corollary 1.2 (statement reading).
- [[../library/additive_bases/erdos_1968_applications_graph_theory_number_theoretic_problems/_index|erdos
  1968 applications graph theory number theoretic problems]]: Theorem (3),
  conjectural paragraph (4); rectangle model (12) and upper proof (13)-(26)
  (proof reading).
- [[../library/additive_bases/garaev_2026_sidon_sets_squares_cubes_quartics_short/_index|garaev
  2026 sidon sets squares cubes quartics short]]: Section 2, Theorems 1-2 on
  squares (statement reading). Sections 1-2, especially cube Theorems 3-5
  (statement reading).
- [[../library/additive_bases/green_2001_number_squares_b_h_g_sets/_index|green
  2001 number squares b h g sets]]: Section 3 Bose-Chowla statement; Lemma 16
  and Theorem 17 (statement reading).
- [[../library/additive_bases/obryant_2026_thickness_infinite_generalized_sidon_sets_ii/_index|obryant
  2026 thickness infinite generalized sidon sets ii]]: Theorem 1, even-h
  restriction (statement reading).
- [[../library/additive_bases/pikhurko_2006_dense_edge_magic_graphs_thin_additive/_index|pikhurko
  2006 dense edge magic graphs thin additive]]: Introduction, Theorems 2-3
  (statement reading).
