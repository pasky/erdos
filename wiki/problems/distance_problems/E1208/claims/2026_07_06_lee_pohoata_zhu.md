---
name: problems/distance_problems/E1208/claims/2026_07_06_lee_pohoata_zhu
title: Lee, Pohoata and Zhu's Minkowski grid bound for distinct distances
desc: |
  An arXiv preprint by Lee, Pohoata and Zhu claims a set of $n$ points in the
  plane in which every subset of at least $n^{1/2-\delta}$ points repeats a
  distance, so that $F_2(n)\lesssim n^{1/2-\delta}$ for an absolute $\delta>0$.
authors:
- Sungchul Lee
- Cosmin Pohoata
- Daniel G. Zhu
status: claimed
claim: proved
scope: partial
submitted: null
links:
- url: https://arxiv.org/abs/2607.05374v1
  kind: preprint
  date: 2026-07-06
- url: https://www.erdosproblems.com/1208
  kind: discussion
  date: 2026-09-07
created: 2026-10-13T13:23:17Z
updated: 2026-10-13T13:23:17Z
---

***

**Claim.** Theorem 2 of Lee, Pohoata and Zhu, *The Minkowski grid has
robustly many repeated distances*, arXiv:2607.05374v1 (6 July 2026), gives an
absolute constant $\delta>0$ and, for every positive integer $n$, a set $P$ of
$n$ points in $\mathbb{R}^2$ in which every subset $A\subseteq P$ with
$|A|\ge2$ has some distance occurring $\gtrsim|A|^2/n^{1-\delta}$ times among
its ordered pairs. A subset with all distances distinct has each distance
only twice, so its Corollary 3(3) deduces that, for all large $n$, every
subset of $P$ with at least $n^{1/2-\delta}$ points determines a repeated
distance. Hence $F_2(n)\lesssim n^{1/2-\delta}$, where $F_2(n)$, the paper's
$f_{\mathrm{dist}}(n)$, is the function of
[[problems/distance_problems/E1208/_index|Problem 1208]] for $d=2$. The paper
says that this answers negatively the question of Conlon, Fox, Gasarch, Harris,
Ulrich and Zbarsky whether $F_2(n)=n^{1/2-o(1)}$, and that the previous best
bound was $F_2(n)\lesssim n^{1/2}\exp(-c\log n/\log\log n)$, from the grid
estimate of Croot, Mao, Pohoata, Sheffer and Yip
([[../library/additive_bases/croot_2026_combinatorial_large_sieve_sidon_sets_distances/theorem_1_3|their Theorem 1.3]]).
The set is a Minkowski grid built from a totally real number field of high
degree, the construction that also answers the question of
[[problems/distance_problems/E1207/claims/2026_07_06_lee_pohoata_zhu|Problem 1207]].
The paper's acknowledgments say that the collaboration started from the first
author's manuscript, in which he used ChatGPT to find a set with this property,
recorded on
[[problems/distance_problems/E1208/claims/2026_06_14_lee|its claim page]], and
that the new point of the joint note is to obtain both bounds from one
construction with a simpler analysis. The statements are read from the PDF of
version 1 (pp. 2--3); the proof was not checked here.

**Covers.** An upper bound in the case $d=2$: $F_2(n)\lesssim n^{1/2-\delta}$.
It does not determine the order of $F_2(n)$, and nothing is claimed for
$d\ge3$.

**Depends on.** No page of this wiki. The paper uses as a black box its
Proposition 4, a mild strengthening of Proposition 2.3 of Alon, Bloom, Gowers,
Litt, Sawin, Shankar, Tsimerman, Wang and Wood (arXiv:2605.20695, 2026), on
towers of totally real fields.

**Standing.** Claimed. The result is an arXiv preprint (version 1 of 6 July
2026) with no journal publication and no Lean proof. The site's remarks (page
last edited 7 September 2026) credit the bound $F_2(n)\ll n^{1/2-c}$ to this
paper, but the site labeled the problem OPEN, and commentary on an open
problem is not acceptance.
