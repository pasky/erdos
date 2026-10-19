---
name: research/erdos_644/random_quotients
desc: Vertex identifications give polynomial-size uniform families preserving the local property and any fixed proportion of the transversal number, but do not proportionately reduce rank.
tags: [proved, reductions, limitations]
sources: []
created: 2026-09-23T04:51:06Z
updated: 2026-09-24T22:12:53Z
---


# research/erdos_644/random_quotients

***

This is an unrestricted approximate ground-set reduction, not a solution of
either assertion in [Problem 644](../../problems/set_systems/E0644/_index.md). It
preserves the full local parameter, unlike the linear trace core in
[Structural reductions](structural_reductions.md), at the cost of a polynomial
rather than linear ground-set bound and a fixed proportional loss in transversal
number.

## The quotient lemma

**Theorem.** Let $\mathcal H$ be a finite family of nonempty sets of rank
at most $k$, with $\tau(\mathcal H)=t$. Let $1\le s<t$ be integers, and
let $q$ be an integer satisfying

$$
q\ge s(e^2k)^{t/(t-s)}.
\tag{1}
$$

There is a map $\phi:V(\mathcal H)\to[q]$ such that

$$
\boxed{s+1\le\tau(\phi(\mathcal H))\le t,
\qquad \operatorname{rank}(\phi(\mathcal H))\le k.}
\tag{2}
$$

Every local two-cover property $P_r$ of $\mathcal H$ is preserved.

**Proof.** For each vertex set $S$ with $|S|<t$, fix an edge $E_S$
disjoint from $S$. Starting with $S=\varnothing$, branch by choosing one
vertex of $E_S$ and adjoining it to $S$, and repeat until depth $t$.
This finite tree has at most $k^t$ root-to-leaf paths. Every path consists
of $t$ distinct vertices, because the next chosen edge avoids all
previously chosen vertices.

Color every ground point independently and uniformly with a color in
$[q]$. Suppose the image family has a transversal of size at most $s$,
and extend its color set to a set $C$ of exactly $s$ colors. At every
node of the avoidance tree, $E_S$ has a point whose color belongs to $C$.
Following such a point at each step gives a root-to-leaf path all of
whose $t$ points have colors in $C$.

For a fixed path and a fixed $C$, the probability of this event is
$(s/q)^t$. A union bound therefore gives

$$
\begin{aligned}
\Pr\bigl(\tau(\phi(\mathcal H))\le s\bigr)
&\le k^t\binom qs(s/q)^t\\
&\le\exp\bigl(t\log k+s-(t-s)\log(q/s)\bigr)\\
&\le\exp(s-2t)<1,
\end{aligned}
$$

where (1) was used in the last step. A suitable coloring gives the
lower bound in (2). Images of an original minimum transversal prove the
upper bound, and images of edges cannot grow in size.

For any at-most-$r$ image edges, choose original preimages. A two-cover
of those original edges maps to an at-most-two-point cover of their
images. Repetitions and merged points cause no difficulty. Thus $P_r$
is preserved. $\square$

No criticality, uniformity, or local condition was used for the
probabilistic estimate itself.

## Restoring uniformity without an exponential ground set

Let $\mathcal G=\phi(\mathcal H)$ and $u=\tau(\mathcal G)\le t$. Add a
disjoint dummy block $D$ of size $k+t-1$, and take all sets

$$
A\cup B,\qquad A\in\mathcal G,\quad
B\in\binom D{k-|A|}.
\tag{3}
$$

This family is $k$-uniform, preserves every $P_r$ satisfied by
$\mathcal G$, and has transversal number exactly $u$.

An original $u$-point cover still covers (3). Conversely, a proposed
cover $T$ of size at most $u-1$ misses some $A\in\mathcal G$ after
restriction to the old ground. At least

$$
k+t-1-(u-1)\ge k
$$

dummy points remain outside $T$, enough to choose the padding $B$
disjoint from $T$. This proves the opposite inequality. A local cover
of the corresponding core edges covers all padded edges, proving the
local assertion.

## Polynomial ground sets suffice for fixed proportional accuracy

Fix $0<\varepsilon<1$ and $r\ge3$. A nonempty rank-$\le k$ $P_r$
family has $t\le2k$, since a maximal matching has at most two edges.
Set $s=\lfloor(1-\varepsilon)t\rfloor$. If $s\ge1$, then

$$
\frac{t}{t-s}\le\frac1\varepsilon,
$$

so the theorem and (3) produce a $k$-uniform $P_r$ family with
transversal number strictly larger than $(1-\varepsilon)t$ and ground
size at most

$$
\boxed{2k(e^2k)^{1/\varepsilon}+3k
=O_\varepsilon(k^{1+1/\varepsilon}).}
\tag{4}
$$

If $s=0$, identifying all vertices gives transversal number one, which
already exceeds $(1-\varepsilon)t$; the same padding argument applies.

The finite-witness compactness argument in
[Structural reductions](structural_reductions.md#passage-to-finite-critical-families)
extends this existence conclusion to infinite families of finite rank: first
take a finite subfamily with the same transversal number.

For the exactly-$r$ convention, a family with at least $r$ edges has
$P_r$ in the at-most sense. Families with fewer than $r$ edges have
bounded transversal number and do not affect the asymptotic question.

In particular, a hypothetical fixed-excess counterexample to the
three-quarter assertion can be replaced by one on polynomially many
vertices, with a smaller but still positive fixed excess. This is not
an assertion that a fixed finite counterexample can be amplified.

## Remaining gap

The quotient preserves almost all transversal number while merely
bounding, rather than proportionately decreasing, the rank. It creates
neither permutation invariance inside blocks nor growing profile slack.
Its singleton-block representation can still use $k$ positive
coordinates per edge. Thus the amplifier in
[Block-profile convergence](block_profile_convergence.md) does not
apply, and no unrestricted convergence theorem or $3/4$ upper bound
follows from (4).

[Quotient compression obstruction](quotient_compression_obstruction.md)
gives near-three-quarter $P_7$ families for which **every** quotient
onto $O(k^{2-\varepsilon})$ points has transversal number $o(k)$,
for each fixed $\varepsilon>0$. The obstruction also survives exact
conjunction-primality. It excludes a near-linear replacement for (4)
using vertex identifications alone, but not a prior removal of guards.
