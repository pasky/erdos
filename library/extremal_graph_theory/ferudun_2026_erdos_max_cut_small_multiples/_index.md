---
name: extremal_graph_theory/ferudun_2026_erdos_max_cut_small_multiples
title: Ferudun's finite-range triangle-free max-cut claim
desc: An unrefereed order-ten certificate claims the sharp bipartization bound on 5n vertices for n at most forty; the source's integrality transfer and its remaining all-order gap are explicit, while the supplied verification package is incomplete.
license: CC-BY-4.0
created: 2026-10-15T20:40:07Z
updated: 2026-10-15T20:40:07Z
---

# Ferudun's finite-range triangle-free max-cut claim

[[extremal_graph_theory/_index|..]]

[[extremal_graph_theory/ferudun_2026_erdos_max_cut_small_multiples/proposition_2_2|proposition_2_2]]: Ferudun's blow-up identity and integer rounding turn a triangle-free graphon bound 2/25 + delta into the sharp finite bound on 5n vertices whenever (25/2)n squared delta is less than one.

[[extremal_graph_theory/ferudun_2026_erdos_max_cut_small_multiples/theorem_1_1|theorem_1_1]]: Ferudun's Theorem 1.1 claims that every triangle-free graph on 5n vertices needs at most n squared edge deletions to become bipartite, for 1 <= n <= 40, with equality attained.

***

Alper Ferudun, *The Erdos n^2/25 max-cut conjecture for small multiples of five,
via a per-root-MaxCut envelope and blow-up integrality*,
[arXiv:2606.28041v1](https://arxiv.org/abs/2606.28041v1), 26 June 2026.
The held [PDF](ferudun_2026_erdos_max_cut_small_multiples.pdf) is the eight-page
arXiv version, accompanied by its arXiv record, TeX source, HTML and ancillary
files. The [arXiv record](https://arxiv.org/abs/2606.28041v1), read
2026-10-15, specifies Creative Commons Attribution 4.0. The preprint is
unrefereed; no independent acceptance is supplied here.

## Results and method

For a finite simple graph, write $\beta(G)=e(G)-\operatorname{maxcut}(G)$,
the fewest edges whose removal leaves a bipartite graph. Let $a(N)$ be the
maximum of $\beta(G)$ over triangle-free graphs with $N$ vertices.
[[extremal_graph_theory/ferudun_2026_erdos_max_cut_small_multiples/theorem_1_1|Theorem 1.1]],
p. 2, claims $a(5n)=n^2$ for $1\le n\le40$. This is the finite-range
claim on [[../wiki/problems/extremal_graph_theory/E0023/_index|Problem 23]],
whose complete question ranges over every positive $n$.

The argument has three parts. The two density tails are imported from
[[extremal_graph_theory/balogh_2021_max_cuts_triangle_free_graphs/theorem_2|Balogh, Clemen and Lidický]].
For the remaining band, Theorem 3.2, pp. 4–5, asserts a bound
$d_{\rm mono}(W)\le2/25+\delta$ for triangle-free $\{0,1\}$ step graphons
of edge density between $1243/5000$ and $3197/10000$, with a specified
rational $\delta\approx4.8557798\cdot10^{-5}$.
It uses cuts determined by adjacency to seven or eight sampled roots,
an order-ten flag relaxation, additional cut inequalities and a positive
semidefinite moment term. Its numerical and graphon soundness are not
independently verified here.

[[extremal_graph_theory/ferudun_2026_erdos_max_cut_small_multiples/proposition_2_2|Proposition 2.2]],
p. 3, then uses the exact identity $\beta(G[t])=t^2\beta(G)$ and
$d_{\rm mono}(W_G)=2\beta(G)/N^2$. On $N=5n$ vertices the error is
$(25/2)n^2\delta$; if it is less than one, integer rounding gives
$\beta(G)\le n^2$. The stated $\delta$ meets this test through $n=40$,
but fails it at $n=41$. The balanced blow-up of $C_5$ supplies equality.

Section 7, p. 7, leaves the zero-error graphon inequality open. It proposes
the stronger bound $\sum_{uv\in M}(d_B(u,v)+1)^2\le N^2$ for the
monochromatic edges $M$ and connected cut graph $B$ of a maximum cut.
No proof of this proposed inequality is given. The reported plateau of the
tested relaxations is not used here as a theorem excluding other orders or
other methods.

## Reading and verification limits

**Read status: claims checked.** The complete TeX exposition was read for
statements, normalization, proof structure and limitations; the printed
page 3 was inspected for Lemma 2.1 and Proposition 2.2. The elementary
blow-up and integer-rounding arguments were checked. The flag-algebra
certificate and its graphon interpretation were not independently verified,
and no ancillary program was executed. This is not a whole-proof review.

Static inspection of the supplied ancillary files finds a replay gap.
`complete_v2_cert.py` imports `prove_cert` and `flag_exact` and requires
`cp_cache.pkl`, `c5lift_cache.npz` and `horn_cert_state_it16.pkl`; none is
in this version's source archive. Other supplied moment scripts also import
the absent modules. The package says that its omitted caches can be regenerated,
but the supplied files do not give a complete replay path.
`step1_v2_independent_gate.py` checks selected quantities and trusts the saved
`valid` field for the per-state residual verdict; it does not independently
recompute those residuals. Its reported pass is therefore not a complete
certificate check under the repository's evidence rules. These findings
identify missing evidence, not a counterexample to the theorem.

The introduction, p. 2, has inconsistent range prose mentioning eleven
multiples and $n\ge12$, while Theorem 1.1 and the final calculation use forty
and $n=41$. Corollary 4.2, p. 5, states the sharp tail bound at both boundary
densities for every order, but its proof sends those endpoints to the
positive-error band certificate. That alone does not give the stated sharp
bound at every order. The corpus's
[[../wiki/research/graph_ramsey_interfaces/homogeneous_triangle_deletion_bounds|homogeneous transfer proof]]
handles the sparse endpoint by adjoining an isolated vertex before taking
the blow-up limit, and handles the dense endpoint directly. This repair does
not verify the separate middle-band certificate.

**Bears on.** [[../wiki/problems/extremal_graph_theory/E0023/_index|#23]].
