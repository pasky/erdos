---
name: extremal_graph_theory/ferudun_2026_erdos_max_cut_small_multiples/proposition_2_2
title: Turning a graphon error bound into an exact finite range
desc: Ferudun's blow-up identity and integer rounding turn a triangle-free graphon bound 2/25 + delta into the sharp finite bound on 5n vertices whenever (25/2)n squared delta is less than one.
created: 2026-10-15T20:40:07Z
updated: 2026-10-15T20:40:07Z
---

# Turning a graphon error bound into an exact finite range

***

**Source.** Lemma 2.1, equation (2) and Proposition 2.2, p. 3, of
[[extremal_graph_theory/ferudun_2026_erdos_max_cut_small_multiples/_index|Ferudun,
arXiv:2606.28041v1]].

**Statement.** Write $\beta(G)=e(G)-\operatorname{maxcut}(G)$. For the
step graphon $W_G$ of a graph with $N$ vertices, use edge density
$p(W_G)=2e(G)/N^2$ and monochromatic-edge density
$d_{\rm mono}(W_G)=2\beta(G)/N^2$.
Suppose every triangle-free step graphon with $p(W)$ in a specified band
$B$ satisfies $d_{\rm mono}(W)\le2/25+\delta$.
Then every finite simple triangle-free graph with $N=5n$ vertices and
$2e(G)/N^2\in B$ satisfies

$$
\beta(G)\le n^2+\frac{25}{2}n^2\delta.
$$

If $(25/2)n^2\delta<1$, the integer $\beta(G)$ is at most $n^2$.
The density in this transfer is $2e/N^2$, not $e/\binom N2$.

**Proof mechanism.** A cut on the equal-cluster blow-up $G[t]$ has a
multilinear value in the proportions of each cluster on its two sides.
Its maximum on the cube occurs at a vertex, so
$\operatorname{maxcut}(G[t])=t^2\operatorname{maxcut}(G)$ and
$\beta(G[t])=t^2\beta(G)$. The normalized monochromatic density is
therefore exactly invariant under blow-up. Substituting $N=5n$ into the
graphon inequality and rounding proves the assertion.

**Read status: claims checked.**

**Standing.** The printed proof was read and its elementary
deduction checked. This conditional transfer does not verify a proposed
graphon inequality or the source's numerical certificate. It gives an
all-order sharp bound when $\delta=0$; a single fixed positive $\delta$
only supplies a bounded integer-rounding range by this argument.

**Bears on.** [[../wiki/problems/extremal_graph_theory/E0023/_index|#23]].
