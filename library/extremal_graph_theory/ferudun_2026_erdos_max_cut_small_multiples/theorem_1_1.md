---
name: extremal_graph_theory/ferudun_2026_erdos_max_cut_small_multiples/theorem_1_1
title: The sharp bipartization claim through forty blocks
desc: Ferudun's Theorem 1.1 claims that every triangle-free graph on 5n vertices needs at most n squared edge deletions to become bipartite, for 1 <= n <= 40, with equality attained.
created: 2026-10-15T20:40:07Z
updated: 2026-10-15T20:40:07Z
---

# The sharp bipartization claim through forty blocks

***

**Source.** Theorem 1.1, p. 2, of
[[extremal_graph_theory/ferudun_2026_erdos_max_cut_small_multiples/_index|Ferudun,
arXiv:2606.28041v1]].

**Statement.** Let $a(N)$ be the largest, over finite simple triangle-free
graphs on $N$ vertices, of the minimum number of edges whose deletion makes
the graph bipartite. For every integer $1\le n\le40$,

$$
a(5n)=n^2.
$$

**Argument.** The balanced $C_5$ blow-up attains the lower bound. For the
upper bound, Sections 2–5 combine the claimed graphon bound
$d_{\rm mono}\le2/25+\delta$ on edge densities
$[1243/5000,3197/10000]$, the two imported density tails, and
[[extremal_graph_theory/ferudun_2026_erdos_max_cut_small_multiples/proposition_2_2|the integer-rounding transfer]].
The stated rational certificate value is approximately
$4.8557798\cdot10^{-5}$, making $(25/2)n^2\delta<1$ throughout the claimed
range. The theorem gives no bound of $n^2$ for every $n>40$.

**Read status: claims checked.**

**Standing.** Unrefereed and not independently
accepted here. The card describes the incomplete supplied replay package,
the range inconsistency in the introduction, and the repair available for
the tail endpoints. None supplies verification of the middle-band certificate.

**Bears on.** [[../wiki/problems/extremal_graph_theory/E0023/_index|#23]],
for the stated finite range only.
