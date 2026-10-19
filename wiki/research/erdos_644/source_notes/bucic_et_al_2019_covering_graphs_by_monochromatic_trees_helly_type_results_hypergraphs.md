---
name: research/erdos_644/source_notes/bucic_et_al_2019_covering_graphs_by_monochromatic_trees_helly_type_results_hypergraphs
title: "Bucić et al.: Covering graphs by monochromatic trees and Helly-type results for hypergraphs"
desc: "Source notes for Problem 644: Bucić et al.: Covering graphs by monochromatic trees and Helly-type results for hypergraphs."
tags: []
sources: []
created: 2026-09-24T22:18:20Z
updated: 2026-10-13T04:56:43Z
---

# Bucić et al.: Covering graphs by monochromatic trees and Helly-type results for hypergraphs


[Full paper in Markdown](../../../../library/set_systems/bucic_et_al_2019_covering_graphs_by_monochromatic_trees_helly_type_results_hypergraphs/_index.md).

***

[Full paper in Markdown](../../../../library/set_systems/bucic_et_al_2019_covering_graphs_by_monochromatic_trees_helly_type_results_hypergraphs/_index.md).

Matija Bucić, Dániel Korándi, Benny Sudakov, "Covering graphs by monochromatic
trees and Helly-type results for hypergraphs," arXiv:1902.05055 (2019).

## Overview

The paper studies the worst-case number $\mathrm{tc}_r(G)$ of monochromatic
connected components needed to cover the vertices of an $r$-edge-coloured graph
$G$; components may equivalently be replaced by monochromatic trees. Its central
contribution is a translation of this graph-colouring parameter into
local-to-global transversal problems for uniform hypergraphs.

For random graphs, Theorem 1.2 gives constants $c,C>0$ such that, for
$G\sim\mathcal G(n,p)$, one has w.h.p. $\mathrm{tc}_r(G)>r$ when
$p<(c\log n/n)^{\sqrt r/2^{r-2}}$, whereas $\mathrm{tc}_r(G)\le r$ when
$p>(C\log n/n)^{1/2^r}$. Theorem 1.3 shows that in the range just above the
threshold at which the cover number becomes bounded, namely
$$(C\log n/n)^{1/r}<p<(c\log n/n)^{1/(d(r+1))},$$
with fixed $d>1$, its order is $\Theta(r^2)$. More generally, for integers
$k>r\ge2$, Theorem 1.4 places $\mathrm{tc}_r(G)$ between $r^2/(20\log k)$ and
$16r^2\log r/\log k$ when $(C\log n/n)^{1/k}<p<(c\log n/n)^{1/(k+1)}$.
Theorem 3.1 supplies the direct upper bound $\mathrm{tc}_r(G)\le(3r-2)r$ above
$(C\log n/n)^{1/r}$; its proof bounds the independence number of the
transitive-closure multigraph, using the random-graph estimates in
Lemmas 2.2–2.3 and Corollary 2.4 together with the bootstrapping Claim 3.2.
Proposition 2.6 is the elementary inequality $\mathrm{tc}_r(G)\le r\alpha(G)$
used in this argument. Theorem 1.6, in a deterministic direction, proves that
in every $r$-colouring of an $n$-vertex graph of minimum degree at least
$(1-2^{-r})n$ the vertices can be covered by monochromatic components, no two
of the same colour.

The key construction appears in Section 4. Given an $r$-colouring $c$ of $G$,
the authors form an $r$-partite $r$-uniform hypergraph $H(G,c)$ whose vertices
are the monochromatic components and whose edge $m(v)$ records the one
component of each colour containing $v$. Proposition 4.1 proves exactly that
the monochromatic component-cover number equals $τ(H(G,c))$; a transversal
cover corresponds to components of distinct colours. The unnumbered Definition
of Section 1.2 introduces the $r$-partite $k$-covering property—every
subhypergraph of at most $k$ edges admits a transversal cover—and
$\mathrm{hp}_r(k)$ is the largest possible cover number under this condition.
Lemma 4.2 shows, for integers $k>r\ge2$, that if every $k$ vertices of $G$
have a common neighbour, then $\mathrm{tc}_r(G)\le\mathrm{hp}_r(k)$. Lemma 4.3
and Proposition 4.4 give a converse construction, with one additional colour,
from a sufficiently large independent set having no common neighbour for any
$k+1$ of its vertices. Together with the random-graph lemmas, these yield
Theorem 1.5: for integers $k>r\ge2$, if $np^k>C\log n$, then w.h.p.
$\mathrm{tc}_r(G)\le\mathrm{hp}_r(k)$, while if $np^{k+1}<c\log n$, then
w.h.p. $\mathrm{tc}_{r+1}(G)\ge\mathrm{hp}_r(k)+1$.

Section 5 and Appendix A treat the nonpartite Helly-type parameter directly
relevant to set systems. The unnumbered Definition of Section 1.4 says that an
$s$-uniform hypergraph has the $(q,\ell)$-covering property when every
subhypergraph with at most $q$ edges has a vertex cover of size at most
$\ell$; $\mathrm h_s(q,\ell)$ is the largest possible global cover number.
Observation 5.1 records that $\mathrm h_s(\ell,\ell)=\infty$, the bound
$\mathrm h_s(\ell+1,\ell)\le s\ell$, monotonicity in $q$, and the trivial
lower bound $\ell$. Proposition 5.6, which the paper credits to the earlier
observation of Erdős et al., shows that the second of these is attained:
$$\mathrm h_s(\ell+1,\ell)=s\ell.$$
Theorem 5.2, an observation the paper attributes to Füredi, proves the exact
Helly threshold $\mathrm h_s(q,\ell)=\ell$ for $q\ge\binom{s+\ell}{\ell}$. Its
critical-hypergraph reduction rests on Corollary 2.9, credited to Bollobás and
derived here from Alon’s cited set-pairs theorem (Theorem 2.7): a critical
$s$-uniform hypergraph of cover number $t+1$ has at most $\binom{s+t}{t}$
edges.

The main general upper estimate is Theorem 5.3. If $\ell\le t\le s\ell$ and
$$q\ge \binom{s+t}{t}^{1/\lfloor t/\ell\rfloor}\,2s\ell\log(s\ell),$$
then $\mathrm h_s(q,\ell)\le t$. The proof combines the critical-edge bound
with random sampling (Claim 5.4) and iteratively removes $\ell$ vertices
covering a fixed positive fraction of the remaining edges. For lower bounds,
Theorem 5.7 uses the complete $s$-uniform hypergraph on $s+t$ vertices to
prove, for integers $s\ge2$ and $t\ge\ell$,
$$q<\frac{\binom{s+t}{\ell}}{\binom{t}{\ell}}\quad\Longrightarrow\quad \mathrm h_s(q,\ell)>t.$$
Lemma 5.8 abstracts the counting step: if an auxiliary $\ell$-uniform
hypergraph has $e$ edges and every edge of the original hypergraph meets at
least $δ$ of them, then any $\lfloor(e-1)/(e-δ)\rfloor$ original edges are
covered by one auxiliary edge. Lemma 5.10 supplies a second lower construction
using disjoint complete uniform hypergraphs.

Section 6 develops the corresponding partite theory. Theorem 6.3 proves
$\mathrm{hp}_r(k)=r$ for $k\ge2^r$ and, more strongly, produces a transversal
cover. Theorem 6.4 gives $\mathrm{hp}_r(k)\le16r^2\log r/\log k$ for
$2\le r<k\le e^r$. The construction $H_{r,t,m}$ has cover number $(t+1)m$ by
Proposition 6.5 and yields the lower bounds in Theorems 6.6, 6.7, and 6.9,
including $\mathrm{hp}_r(k)\ge r^2/(12\log k)$ for $k>r\ge2$ and
$\mathrm{hp}_r(k)\ge r^3/(50k)$ for every $k$ and $r\ge2$.

Finally, Proposition A.1 in Appendix A recasts the nonpartite problem through
the $\ell$-covering hypergraph $\mathrm{ch}_\ell(H)$: the least number of
edges of $H$ failing to have an $\ell$-cover equals $τ(\mathrm{ch}_\ell(H))$,
while $τ(H)>t\ell$ is equivalent to $\mathrm{ch}_\ell(H)$ being
$t$-intersecting. By Theorem A.2, if a hypergraph on $n$ vertices is
$t$-intersecting and its maximum degree is $d$, then its cover number is at
most $n^{1/t}(1+\log d)$. This supplies an alternative derivation of
Theorem 5.3 using the cited Lovász integral-versus-fractional cover inequality
displayed in Appendix A. The paper therefore gives broad quantitative
local-to-global bounds and exact endpoint thresholds, but generally leaves
logarithmic gaps in the middle range, as explicitly noted in Section 7.

## Relation to E644

This source bears on [Problem 644](../../../problems/set_systems/E0644/_index.md).

Write $K$ for the size of each set in E644 and $q$ for the number of locally
tested sets, to avoid collision with the paper’s notation. Regard the family
$\{A_i\}$ as the edge set of a $K$-uniform hypergraph $H$. A pair $\{x,y\}$
intersecting every member of a subfamily is precisely a vertex cover of that
subhypergraph of size at most $2$ (a one-point cover can be padded if
necessary). Thus E644’s local hypothesis is the paper’s $(q,2)$-covering
property from the Definition of Section 1.4, and, in the paper’s notation,
$$f(K,q)=\mathrm h_K(q,2).$$
This is the direct connection; the partite parameter $\mathrm{hp}_r(k)$ and
most of the monochromatic-tree results impose additional partiteness or
transversal-cover structure and should not be identified with E644.

Several results specialize immediately:

- Proposition 5.6 with $s=K$ and $\ell=2$ gives $f(K,3)=2K$.

- Observation 5.1(2)–(3) gives the uniform upper bound $f(K,q)\le2K$ for every
  fixed $q\ge3$.

- Theorem 5.7 gives, for every integer $t\ge2$,
  $$q<\frac{\binom{K+t}{2}}{\binom{t}{2}}=\frac{(K+t)(K+t-1)}{t(t-1)}\quad\Longrightarrow\quad f(K,q)>t.$$
  Taking $t\sim cK$ shows
  $$\liminf_{K\to\infty}\frac{f(K,q)}K\ge\frac1{\sqrt q-1}.$$
  In particular,
  $$\liminf_{K\to\infty}\frac{f(K,7)}K\ge\frac1{\sqrt7-1}=\frac{\sqrt7+1}{6}\approx0.607625.$$
  The construction is explicit: the complete $K$-uniform hypergraph on $K+t$
  vertices has cover number $t+1$, and the counting argument in Theorem 5.7
  verifies its local two-cover property. This falls well short of the
  conjectured coefficient $3/4$.

- Theorem 5.3 translates to
  $$q\ge \binom{K+t}{t}^{1/\lfloor t/2\rfloor}\,4K\log(2K)\quad\Longrightarrow\quad f(K,q)\le t,$$
  for $2\le t\le2K$. This can be useful when the local parameter $q=q(K)$ grows,
  but it gives no improvement for E644’s fixed $q$: its right-hand condition is
  already at least of order $K\log K$.

- Theorem 5.2 gives the far-end exact statement $f(K,q)=2$ once
  $q\ge\binom{K+2}{2}$. It does not bear directly on fixed $q$.

Two constructions may be useful inside a future E644 argument. First,
Corollary 2.9 says that a cover-critical $K$-uniform obstruction with
$τ(H)=t+1$ has at most $\binom{K+t}{t}$ edges. This permits an upper-bound
proof to pass to a finite minimal obstruction before applying counting or
sampling. Claim 5.4 and the deletion argument proving Theorem 5.3 then provide
a template: show that some pair covers a sufficiently large fraction of every
remaining subhypergraph and iterate. The quantitative estimate presently
obtained by that method is too weak when $q=7$ is fixed.

Second, Lemma 5.8 is a flexible lower-bound device. For an auxiliary graph $G$
on $V(H)$, if every $K$-edge of $H$ meets at least $δ$ of the $e(G)$ graph
edges, then any $\lfloor(e(G)-1)/(e(G)-δ)\rfloor$ edges of $H$ have a common
two-point cover which is itself an edge of $G$. Designing $H$ and $G$ so that
this quantity is at least $7$ while $τ(H)\sim3K/4$ would prove the lower-bound
half of the first E644 conjecture; the paper’s complete-hypergraph choice
reaches only $(\sqrt7+1)K/6$ asymptotically.

Proposition A.1 gives a particularly exact reformulation. Define
$\mathrm{ch}_2(H)$ on vertex set $E(H)$, with one hyperedge consisting of all
members of $H$ disjoint from each two-set $S\subseteq V(H)$. Then $H$ has the
$(q,2)$-covering property exactly when
$$τ(\mathrm{ch}_2(H))\ge q+1,$$
and $τ(H)>2t$ exactly when $\mathrm{ch}_2(H)$ is $t$-intersecting.
Consequently E644 asks for the largest $τ(H)$ among $K$-uniform $H$ satisfying
$τ(\mathrm{ch}_2(H))\ge q+1$. This is a plausible insertion point for
fractional-cover or intersecting-hypergraph estimates such as Theorem A.2,
although the theorem as stated does not yield the desired fixed-$q$ constants.

Overall, the paper's results give $f(K,q)=\Theta_q(K)$ for every fixed
$q\ge3$—combining Theorem 5.7 with Observation 5.1—but it neither proves
convergence of $f(K,q)/K$ nor determines its limit. In particular, it does not
prove $f(K,7)=(3/4+o(1))K$, and it does not establish the existence of
constants $c_q$ for all fixed $q$.
