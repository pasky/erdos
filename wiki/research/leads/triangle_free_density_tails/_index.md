---
name: research/leads/triangle_free_density_tails
title: All-order density tails for triangle-free bipartization
desc: |
  A blow-up identity carries Balogh, Clemen and Lidický's large-order bounds
  to every order: every triangle-free graph on N vertices needs at most
  2N^2/47 edge deletions to become bipartite, and at most N^2/25 when 2e/N^2
  is at most 0.2486 or at least 0.3197, boundaries included. Blow-ups cannot
  reach the middle band, which needs a zero-error band bound.
problems:
- 23
research_state: blocked
review_status: unreviewed
created: 2026-10-18T03:08:34Z
updated: 2026-10-18T03:50:39Z
---

# All-order density tails for triangle-free bipartization

[[research/leads/_index|..]]

***

This lead's derivations that are not drawn from a cited source are Plasma
AI's, credited to Plasma AI. The same tail conclusions are stated in
Ferudun's earlier preprint, as recorded below. The derivations are
author-recorded at tier 0, and no independent review has examined the lead.

## Target and route

[[problems/extremal_graph_theory/E0023/_index|Problem 23]] asks whether every
triangle-free graph on $5n$ vertices can be made bipartite by deleting at most
$n^2$ edges. Write $D_2(G)$ for the fewest edges whose deletion makes a finite
simple graph $G$ bipartite, and $e(G)$ for its number of edges. The problem
page's current assessment records the problem as open, and this lead does not
change that.

[[../library/extremal_graph_theory/balogh_2021_max_cuts_triangle_free_graphs/theorem_2|Theorem 2 of Balogh, Clemen and Lidický]]
gives, for every triangle-free graph on $N\ge N_0$ vertices, the bound
$D_2(G)\le N^2/23.5$, and the bound $D_2(G)\le N^2/25$ when
$e(G)\ge0.3197\binom N2$ or $e(G)\le0.2486\binom N2$. The source gives no
explicit value of $N_0$. The route removes this large-order qualification,
as Section 2.3 of the same paper already does for the whole conjecture, by a
blow-up and Theorem 7 of Erdős, Győri and Simonovits.
The blow-up $G[t]$ replaces each vertex by an independent set of $t$ vertices
and each edge by a complete bipartite graph between the corresponding sets.
It is triangle-free when $G$ is, it has $t^2e(G)$ edges, and

$$
D_2(G[t])=t^2D_2(G).
$$

Applying the theorem to $G[t]$ for large $t$ and dividing by $t^2$ gives
bounds for $G$ itself at every order.

## Results

The
[[research/graph_ramsey_interfaces/homogeneous_triangle_deletion_bounds|homogeneous transfer page]]
is the canonical account of the route. It proves the following.

- **The blow-up identity.** $D_2(G[t])=t^2D_2(G)$ for every graph $G$ and
  every $t\ge1$. The number of crossing edges of a cut of $G[t]$, divided by
  $t^2$, is affine in each cluster's proportion on the first side, so some
  maximum cut keeps every cluster whole. Adding isolated vertices changes
  neither $D_2$ nor the edge count.
- **The general bound.** Every triangle-free $G$ on $N\ge1$ vertices has
  $D_2(G)\le2N^2/47$. On $N=5n$ vertices this is $D_2(G)\le(50/47)n^2$,
  weaker than the bound the problem asks.
- **The dense tail.** Every triangle-free $G$ on $N\ge1$ vertices with
  $2e(G)/N^2\ge0.3197$ has $D_2(G)\le N^2/25$. Here
  $e(G[t])\ge0.3197(tN)^2/2\ge0.3197\binom{tN}2$, so the theorem applies to
  $G[t]$ directly.
- **The sparse tail.** Every triangle-free $G$ on $N\ge1$ vertices with
  $2e(G)/N^2\le0.2486$ has $D_2(G)\le N^2/25$, the boundary density included.
  The theorem is applied to $G[t]$ with one isolated vertex adjoined, of order
  $tN+1$, whose edge count satisfies $t^2e(G)\le0.2486\binom{tN+1}2$. This
  gives $t^2D_2(G)\le(tN+1)^2/25$, and letting $t\to\infty$ gives the bound.
  The isolated vertex is what permits the source's $\binom N2$ normalization
  at equality.

On $5n$ vertices the two tails give $D_2(G)\le n^2$, the answer yes to the
problem's question for those graphs, at every $n$. The transfer uses the
theorem at its statement. Its source is a six-page extended abstract whose
proof is a sketch with omitted computations; the source card records a
claims-checked reading, and the proof is not reverified here.

## Relation to Ferudun's preprint

[[../library/extremal_graph_theory/ferudun_2026_erdos_max_cut_small_multiples/_index|Ferudun's unrefereed preprint]]
of 26 June 2026 states the blow-up identity as its Lemma 2.1 and the same
all-order tail bounds as its Corollary 4.2, p. 5, both boundary densities
included. That corollary's proof sends the two boundary densities to the
preprint's positive-error band certificate, which alone does not give the
sharp bound at every order. The transfer here treats the dense boundary
directly and the sparse boundary through the isolated vertex, and it does not
use the certificate.

The preprint's Theorem 1.1, the bound $n^2$ at every density for
$1\le n\le40$, is
[[problems/extremal_graph_theory/E0023/claims/2026_06_26_ferudun|a pending claim]].
Its integer-rounding step turns a band bound $2D_2(G)/N^2\le2/25+\delta$ into
$D_2(G)\le n^2$ on $5n$ vertices when $(25/2)n^2\delta<1$. The transfer page
checks that elementary deduction but not the numerical certificate behind its
$\delta$.

## Why the lead is blocked

The transfer leaves the middle band

$$
0.2486<\frac{2e(G)}{N^2}<0.3197
$$

at every order. Blow-ups preserve edge density, so repeating the transfer
cannot remove this gap. A finite census is not implied either: reducing every
middle-band obstruction to a bounded order would be an additional theorem,
and none is supplied.

Completing the problem along this route needs a middle-band inequality
$2D_2(G)/N^2\le2/25$ with zero error, or a family of valid errors tending to
zero uniformly over the band. A single positive error, such as the preprint's,
only extends a finite range by integer rounding. The two tails and the exact
density normalization must be kept when such a band bound is composed with
them.

[[research/leads/triangle_free_middle_band/_index|The middle-band lead]]
pursues that band bound through zero-error certificates on graphons coloured
by a maximum cut. It uses this lead's tails to reduce the problem to the band,
and the general bound, as $2D_2(H)\le(4/47)|V(H)|^2$, in the hereditary
comparison rows of
[[research/triangle_free_bipartization/proof_sketch|its proof sketch]], whose
held links list the tails.

## Claim and standing

The tail bounds and the general bound are Plasma AI's
[[problems/extremal_graph_theory/E0023/claims/2026_10_19_plasma_ai|pending partial claim on Problem 23]].
They are author-recorded at tier 0, without independent review or Lean proof,
and they are written arguments with no evidence program.
