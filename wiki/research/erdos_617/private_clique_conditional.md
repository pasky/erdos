---
name: research/erdos_617/private_clique_conditional
desc: Conditional private-clique and local-lemma route to a bounded exceptional core; the essential private-clique hypothesis is unproved.
tags: [graph-theory, conditional, packing]
sources: []
created: 2026-09-21T23:52:12Z
updated: 2026-09-24T22:12:59Z
---


# research/erdos_617/private_clique_conditional

***

**Status: proof outline, not an established reduction.** The elementary
inequalities below are checked. The proposed local-lemma completion argument and
its numerical constants have not received a complete written audit. More
fundamentally, its near-full-private-clique hypothesis is unproved. This page
records a possible bridge between the tools in [packing-tools](packing_tools.md)
and the proved [hereditary span bound](hereditary_span_bound.md); it does not
close that bridge.

## Setup and the missing hypothesis

Let $G$ be a least color graph in a hypothetical counterexample, with
$N=r^2+1$, $e(G)\le rN/2$, and $\alpha(G)=r$. Choose a maximum independent
set $I$ minimizing $\sum_{u\in I}d_G(u)$. For $u\in I$, define

$$
P_u=\{u\}\cup\{x\notin I:N_G(x)\cap I=\{u\}\}.
$$

Each $P_u$ is a clique: two nonadjacent private neighbors could replace
$u$ in $I$. The $P_u$ are disjoint. Moreover,

$$
d_G(x)\ge d_G(u)\qquad(x\in P_u),
$$

because replacing $u$ by $x$ preserves a maximum independent set.

The additional hypothesis used throughout the outline is

$$
|P_u|\in\{r-1,r\}\quad\text{for every }u\in I. \tag{H}
$$

It is not enough to know that $u$ belongs to some large clique: that clique
need not consist of private neighbors relative to this $I$. Neither the
new independence inequality nor the current stability arguments establish
(H), even for a suitable choice among minimum-degree-sum maximum independent
sets.

The later [two-supported reduction](two_supported_private_cliques.md)
does prove a weaker total-deficit bound, and allows degree-sum minimality
while retaining a controlled total support excess. Its selected color
need not be a least color, and individual private deficits are not
bounded by one. Therefore that result does not supply (H) or justify
applying the edge-budget argument below to the selected color.

## Checked counting facts

For disjoint target cliques $P,Q$ of orders $r-t,r-u$, with
$t+u\le r$, the full induced-density bound gives

$$
e_G(P,Q)\le r-t-u+tu. \tag{1}
$$

Indeed, their union has $2r-t-u$ vertices and
$p_r(2r-t-u)=r-t-u$; subtracting their internal edges from
$D_r(2r-t-u)$ gives (1). In particular, cross edges between two
$K_{r-1}$'s number at most $r-1$, and between any two private cliques
satisfying (H) number at most $r$.

Suppose (H) holds, and let $a$ private cliques have order $r-1$. Set
$W=V(G)\setminus\bigcup_{u\in I}P_u$. Then

$$
|W|=a+1,
\qquad k_w:=|N_G(w)\cap I|\ge2\quad(w\in W).
$$

Writing $k_u=|N_G(u)\cap W|$, degree-sum minimality gives

$$
\begin{aligned}
2e(G)
&\ge\sum_{u\in I}|P_u|\bigl(|P_u|-1+k_u\bigr)
   +\sum_{w\in W}d_G(w)\\
&\ge\sum_{u\in I}|P_u|(|P_u|-1)+r\sum_{w\in W}k_w.
\end{aligned}
$$

Consequently,

$$
\sum_{w\in W}k_w
\le r+1+2a(1-1/r)\le3r-1. \tag{2}
$$


For a target $K_{r-1}$ denoted by $P$ and distinct external vertices
$x,y$, the $(r+1)$-set cap says

$$
d_P(x)+d_P(y)+\mathbf1_{xy\in E(G)}\le r. \tag{3}
$$

Thus at most one external vertex has more than $r/2$ neighbors in $P$.
An external vertex has at most one neighbor in a target $K_r$.

A second capacity bound will be useful: for sufficiently large $r$, a
$K_{r-1}$ admits at most four external vertices having more than $r/4$
neighbors in it. Otherwise its union with five such vertices contradicts

$$
e_G(P,T)+e(G[T])\le r-1+\binom52=r+9,
$$

which follows from $D_r(r+4)$.

## Proposed local-lemma completion

The following is the retained outline. All local-lemma uses require a
single consistent sufficiently-large-$r$ threshold and a written check
of rounding and dependency bounds before they can be promoted to a theorem.

Choose $K=\lfloor r/10000\rfloor$. A vertex $w\in W$ with $k_w\le K$
should have more than $r/2$ neighbors in some deficient private clique.
Otherwise, for every $u\in N_G(w)\cap I$, the list
$P_u\setminus N_G(w)$ has order at least $r/2-1$. Choose representatives
independently. By (1), a pair-conflict event has probability $O(1/r)$;
its dependency degree is $O(k_w)$. The symmetric Lovász Local Lemma gives
an independent transversal, which, with $w$ and $I\setminus N_G(w)$,
would augment $I$.

By (2), only constantly many $w$ have $k_w>K$. By (3), there are at most
$a$ high-adjacency incidences into deficient private cliques, whereas
$|W|=a+1$. Hence only constantly many of the remaining vertices can
have multiple high incidences, and only constantly many deficient cliques
are left without a uniquely assigned ordinary vertex $w$.

For an ordinary vertex assigned to $P$, a second local-lemma application
should force

$$
|P\setminus N_G(w)|<r/10.
$$

If that list had order at least $r/10$, all lists used in the preceding
augmentation would still have linear order, and pair-conflict probability
would remain $O(1/r)$.

If $P\setminus N_G(w)$ is nonempty, choose $x$ in it. For another
ordinarily assigned private clique $P'$, (3) and its assigned vertex's
near-complete adjacency bound each of $d_{P'}(w)$ and $d_{P'}(x)$ by
roughly $r/10$. For an unassigned deficient clique, $w$ has at most
$r/2$ neighbors. Unless $x$ has more than $r/4$ neighbors in one of the
unassigned cliques, the lists avoiding both $w,x$ still have linear
order. Another local-lemma transversal would replace $N_G(w)\cap I$
by one more independent vertex.

Thus a noncompletion block should supply a vertex $x$ having more than
$r/4$ neighbors in an exceptional deficient clique. Vertices $x$ from
different blocks are distinct. The four-vertex capacity bound above then
limits noncompletion blocks to a constant multiple of the exceptional
cliques. All other assigned sets $P\cup\{w\}$ are disjoint $K_r$'s.

The preliminary bookkeeping proposed fewer than $30000$ high-$k_w$
vertices, fewer than $60000$ exceptional vertices/cliques, and at least
$r-300000$ completed $K_r$'s. These are **provisional constants**, not a
certified theorem statement.

## What a completed argument would accomplish

If (H) and the completion outline yielded $r-C$ disjoint target $K_r$'s
for an absolute $C$, the failed-transversal edge bound in
[packing-tools](packing_tools.md) would force independence number at most
$r-k$ outside a sufficiently large maximal packing of $k\ge r-C$ blocks.
That outside graph has order $r(r-k)+1$. The
[hereditary span bound](hereditary_span_bound.md) excludes it when $r$ is
sufficiently large relative to $C$.

The decisive unresolved step is obtaining (H), or a replacement with
controlled private-clique deficits that supports the same completion
argument. The current global weighted inequalities do not supply it.
