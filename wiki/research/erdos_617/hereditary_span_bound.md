---
name: research/erdos_617/hereditary_span_bound
desc: Full induced density excludes independence-a cores of order ar+1 when r is at least 64a^2.
tags: [graph-theory, proved, stability]
sources: []
created: 2026-09-21T23:52:12Z
updated: 2026-09-24T22:12:59Z
---


# research/erdos_617/hereditary_span_bound

***

**Proved.** Let $a\ge2$ and $r\ge64a^2$. There is no graph $H$ with

$$
|H|=ar+1,\qquad \alpha(H)\le a
$$

such that every $W\subseteq V(H)$ satisfies

$$
e(H[W])\le D_r(|W|),\qquad
D_r(n)=\binom n2-(r-1)p_r(n),
$$

where $p_r(rq+b)=r\binom q2+qb$, $0\le b<r$.

Consequently, in a hypothetical coloring counterexample, every induced
color graph of independence number at most $a$ has at most $ar$ vertices
in this range. This is not a proof of Problem 617 for an infinite set of
parameters: it has the additional small-independence hypothesis.

## 0. A self-contained finite partition lemma

The short induction in Section 3 of the
[independent input](independent/small_independence_and_packing_obstructions.md)
checks out. It proves the precise finite stability statement used here, so no
external stability theorem is needed for the argument below.

Write $\tau_a(n)=\binom n2-p_a(n)$. If $F$ is $K_{a+1}$-free on
$n$ vertices, it has a partition into $a$ possibly empty parts with
at most $\tau_a(n)-e(F)$ internal edges.

Induct on $a$, with $a=1$ immediate; an empty graph is also immediate.
Choose a maximum-degree vertex $v$, and put $A=N_F(v)$,
$d=|A|$, $B=V(F)\setminus A$. The graph $F[A]$ is $K_a$-free.
Its inductive partition, together with $B$, has at most

$$
\tau_{a-1}(d)-e(F[A])+e(F[B])
$$

internal edges. Maximum degree gives

$$
e_F(A,B)+2e(F[B])=\sum_{x\in B}d_F(x)\le d(n-d).
$$

Also $\tau_{a-1}(d)+d(n-d)\le\tau_a(n)$, by taking a balanced
$(a-1)$-partite graph on $A$ and joining it completely to the
independent part $B$. Combining the two inequalities proves the claim.

If $T=\tau_a(n)-e(F)$ and $K$ is the complete multipartite graph
of this partition, then its number of missing cross-edges is

$$
e(K)-e(F)+\sum_i e(F[V_i])\le2T,
$$

and $e(K)\ge\tau_a(n)-2T$. This is the finite content of
[Füredi's Theorem 1 and Corollary 2](../../../library/extremal_graph_theory/furedi_2015_proof_stability_extremal_graphs_simonovits_stability_from_szemeredis_regularity/_index.md).
The supplied theorem and proof were checked; the induction above is the same
maximum-degree mechanism in recursive form.

## 1. Quadratic-scale extraction

The span theorem and its equality case can be proved together. Set
$n=ar+\varepsilon$, where $\varepsilon\in\{0,1\}$, and assume
$\alpha(H)\le a$ and all inherited caps. Put $F=\overline H$.
Its Turán deficit is

$$
T=e(H)-p_a(n)\le D_r(n)-p_a(n)\le a^2r/2.
$$

For $\varepsilon=1$ the exact difference is
$(\binom a2-1)r+a$; for $\varepsilon=0$ it is $\binom a2r$.
The finite partition lemma gives $a$ parts $V_i$, at most $T$
internal $F$-edges, and at most

$$
C\le2T\le a^2r
$$

target edges between parts. Comparing squared part sizes gives

$$
\sum_i(|V_i|-n/a)^2\le4T+1\le2a^2r+1.
$$

Since $r\ge64a^2$, every part has order at least $4r/5$.

Mark vertices whose target cross-degree is at least $r/3$, obtaining
$X$ with $t=|X|\le6a^2$. Suppose an internal $F$-edge $uv$ has two
unmarked endpoints. In each other part, their common $F$-neighborhood
has at least $4r/5-2r/3=2r/15$ vertices. Independent uniform choices
from these neighborhoods have expected target-edge count at most

$$
\frac{225a^2}{4r}\le\frac{225}{256}<1.
$$

Some choice, together with $u,v$, is a forbidden $K_{a+1}$ in $F$.
Thus $Q_i=V_i\setminus X$ are nonempty target cliques. The local
cap forbids $K_{r+1}$, so write

$$
|Q_i|=r-d_i,\quad d_i\ge0,\qquad
D=\sum_i d_i=t-\varepsilon<r.
$$

If $t=0$, the overloaded case is already impossible, and the balanced
case already consists of $a$ full cliques. Hence assume $t\ge1$.

## 2. Assigning owners

For $x\in X$, put $m_i(x)=|Q_i\setminus N_H(x)|$ and
$c_{ij}=e_H(Q_i,Q_j)$. Applying the cap to $Q_i\cup Q_j\cup\{x\}$
and subtracting its clique and incident edges gives

$$
c_{ij}\le m_i(x)+m_j(x)+(d_i-1)(d_j-1)
\le m_i(x)+m_j(x)+d_id_j
$$

when $d_i+d_j\ge1$. When both deficits vanish, the stronger bound
$c_{ij}\le m_i(x)+m_j(x)-r+2$ gives the same final inequality.
The relevant set sizes lie between $r+1$ and $2r+1$ since $D<r$.

Set $L=a^2+D$. Every exception has an owner $i(x)$ with
$m_{i(x)}(x)\le L$. Otherwise random representatives from all its
nonneighbor lists have expected target-edge count less than

$$
\frac{a(a-1)}L+\frac{D^2}{2L^2}<1.
$$

For $D>0$, setting $u=D/(a^2+D)$ bounds this by
$1-u+u^2/2<1$; for $D=0$ the first term is $1-1/a$.
An independent choice together with $x$ contradicts $\alpha(H)\le a$.

## 3. Weighted completion without a concentration loss

For $x\in X$, define

$$
w_i(x)=\frac{d_H(x,Q_i)+d_i-1}{r-1}
=1-\frac{m_i(x)}{r-1},\qquad
S_i=\{x\in X:w_i(x)\ge1/3\}.
$$

All weights are at most one. They can be negative outside $S_i$ when
$d_i=0$; none of the following counts uses such negative incidences.
Every owner incidence belongs to $S_{i(x)}$, since
$L\le7a^2$ and $1-L/(r-1)>1/3$.

Call an exception active if it belongs to at least two of the sets
$S_i$. An inactive exception belongs only to its owner's set. If $x$
is inactive with owner $i$, then, for every $j\ne i$,

$$
d_H(x,Q_j)<(r+2)/3-d_j. \tag{1}
$$


Every inactive exception is complete to its owner core, and the inactive
exceptions with a common owner form a clique. To prove both assertions,
consider a nonadjacent pair consisting either of such an $x$ and
$u\in Q_i$, or of two inactive exceptions with owner $i$. In the first
case $u$ has cross-degree below $r/3$ by the marking rule. Equation (1)
therefore leaves at least $(r-4)/3\ge r/4$ common target nonneighbors
in every other core, in both cases. Uniform representatives from these
$a-1$ lists have expected target-edge count at most
$16a^2/r<1$. They extend the pair to an independent $(a+1)$-set,
a contradiction.

For every $S\subseteq X$ the row-plus-exception cap is

$$
\sum_{x\in S}w_i(x)
\le d_i+\frac{\overline e_H(S)}{r-1}, \tag{2}
$$

where $\overline e_H(S)$ counts nonedges within $S$. For $|S|<d_i$,
this follows from $w_i\le1$. Otherwise $Q_i\cup S$ has order
between $r$ and $2r$, and substitution in $D_r$ gives (2) exactly.

Let $B$ be the sum of weights over nonowner incidences $x\in S_i$,
and let $K$ count these incidences. If $A$ is the active set, then

$$
K\le3B,\qquad |A|\le K.
$$

Put

$$
M=\sum_{x\in X}m_{i(x)}(x),\qquad
E=\sum_i\overline e_H(S_i).
$$

Inactive exceptions have no owner holes, whence $M\le L|A|\le3LB$.
Every nonedge within $S_i$ meets an active exception, because its
inactive vertices form a clique. Thus

$$
E\le(t-1)\sum_i|A\cap S_i|
=(t-1)(|A|+K)\le6(t-1)B.
$$

Summing (2), the owner weights sum to $t-M/(r-1)$, so

$$
t-\frac M{r-1}+B\le D+\frac E{r-1}.
$$

Consequently

$$
\boxed{\varepsilon+B\le
\frac{3L+6(t-1)}{r-1}B.} \tag{3}
$$

But

$$
3L+6(t-1)=3a^2+9t-3\varepsilon-6
\le57a^2-3\varepsilon-6<r-1.
$$

For $\varepsilon=1$, (3) is impossible, proving the span theorem.
The argument pays for all owner holes and exceptional nonedges using
the additional owner incidences, rather than bounding their product
by $O(a^4)$.

## 4. Equality rigidity at the same quadratic threshold

**Theorem.** If $r\ge64a^2$, $|H|=ar$, $\alpha(H)\le a$, and all
inherited caps hold, then $H$ partitions into $a$ cliques of order $r$,
with a matching between every pair.

For $t=0$ this was already proved. Otherwise (3) with
$\varepsilon=0$ forces $B=0$. Every exception is inactive, so every
core together with its assigned exceptions is a clique. These $a$
cliques partition $ar$ vertices and each has order at most $r$;
therefore each has order exactly $r$. The cap on a full clique plus
an outsider gives the asserted matching property.

## Checks, improvement, and remaining gap

Both quadratic theorems received a separate audit of extraction,
random transversals, negative-weight boundary cases, and the final
incidence accounting. No additional external theorem is used beyond
the self-contained finite partition lemma above.

These results supersede the previous $64a^4$ span and $256a^4$
equality thresholds. The [eighth-power proof](small_independence_rigidity.md)
and the [independent comparison](independent_comparison.md) remain as
historical records of weaker methods and differing hypotheses.

A hypothetical overloaded core must now have

$$
a>\sqrt r/8.
$$

This still leaves an unbounded range in both main core reductions.
Neither an unconditional reduction to this small-independence range
nor a universal proof or counterexample has been obtained.
