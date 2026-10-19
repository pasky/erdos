---
name: theory/set_systems/L215_spread_large_core_sunflowers/_proof
title: Proof that spread families can force large sunflower cores
desc: |
  Powers of the triangle are intersecting and sunflower-free with an exactly
  computable excess; substituting them into block-family powers makes every
  sunflower core a union of whole inner members, while the block levels
  absorb the excess.
created: 2026-10-15T18:17:48Z
updated: 2026-10-15T18:17:48Z
---

***

## Conventions

Families, $\mathcal F_T$, intersecting families, $B(\rho,m)$, the substitution
$G[H]$, the powers $G^h$, the excess $E_{\mathcal F}(R)$ and the function
$\psi_G$ are as in the
[[theory/set_systems/L214_spread_intersecting_families/_proof|proof of L214]],
whose Lemmas 1, 2 and 3 are used below; $D$, $D^0$ and $k$-sunflowers are as in
the
[[theory/set_systems/L215_spread_large_core_sunflowers/_index|statement of L215]].
A family is *$k$-sunflower-free* if it has no $k$-sunflower. For a member
$\bigcup_{i\in A}\{i\}\times S_i$ of $G[H]$, $A$ is its *root set* and $S_i$
its *fiber* over $i$.

## Cores of substitutions

**Lemma B.** Let $k\ge3$, let $G$ be an intersecting $a$-uniform family and
$H$ an intersecting $k$-sunflower-free $b$-uniform family. If $k$ members of
$G[H]$ form a $k$-sunflower with core $C$, then their root sets form a
$k$-sunflower of $G$ with a nonempty core $A_*$, their fibers over each
$i\in A_*$ coincide, and $C=\bigcup_{i\in A_*}\{i\}\times S^{(i)}$, where
$S^{(i)}$ is that common fiber. In particular $|C|\ge b$, and if $G$ is
$k$-sunflower-free then so is $G[H]$.

*Proof.* Let the members be $\bigcup_{i\in A_j}\{i\}\times S_j^{(i)}$,
$j=1,\dots,k$, with all pairwise intersections equal to $C$.

*Each point of $G$'s ground set lies in none, one or all of the root sets.* If
$i\in A_j\cap A_{j'}$ with $j\ne j'$, the fibers $S_j^{(i)}$ and
$S_{j'}^{(i)}$ are members of $H$ and meet, so $C$ contains a point over $i$.
Every member contains $C$, so every root set contains $i$.

*Fibers over a common point.* Let $i$ lie in every root set. The fibers over
$i$ pairwise intersect in the fiber $C^{(i)}$ of $C$ over $i$. If two of them
coincide, that fiber equals $C^{(i)}$, so it is contained in every fiber over
$i$; all fibers have $b$ points, so all coincide. Otherwise they are $k$
distinct members of $H$ with all pairwise intersections equal to $C^{(i)}$, a
$k$-sunflower of $H$, which is excluded. So the fibers over $i$ coincide.

*The root sets are pairwise distinct.* If $A_j=A_{j'}$ for some $j\ne j'$, every
point of $A_j$ lies in two root sets, hence in all, so $A_j\subseteq A_l$ for
every $l$ and, all root sets having $a$ points, all coincide. Then the fibers
coincide over every point of the common root set, and the $k$ members coincide,
a contradiction.

*Conclusion.* By the first step, every two distinct root sets intersect exactly
in $A_*=\bigcap_jA_j$, so the root sets form a $k$-sunflower of $G$ with core
$A_*$, nonempty because $G$ is intersecting. By the second step the fibers over
each $i\in A_*$ coincide, so $C$ contains $\{i\}\times S^{(i)}$. A point of a
member over $i\notin A_*$ lies in no other of the $k$ members, so $C$ has no
such point, and $C=\bigcup_{i\in A_*}\{i\}\times S^{(i)}$. The last assertion
follows because the root sets of a $k$-sunflower of $G[H]$ would form one of
$G$. $\square$

## Powers of the triangle

**Lemma A.** For every $g\ge0$, $D^g$ is an intersecting family of
$2^g$-element sets with $3^{2^g-1}$ members that is $k$-sunflower-free for
every $k\ge3$, and $E_{D^g}(R)=3(R/3)^{2^g}$ for every real $R\ge3$.

*Proof.* $D^0$ has one member, of one point, so it is intersecting, has no $k$
distinct members, and $E_{D^0}(R)=R$. The triangle $D$ is intersecting; its
only three members pairwise meet in three different points, so it has no
$3$-sunflower, and it has no $k$ distinct members for $k\ge4$. Since
$D^g=D[D^{g-1}]$ for $g\ge1$, Lemma 1 of L214 and Lemma B give the first
assertions by induction; the size follows from $|D^g|=3\,|D^{g-1}|^2$. Each
point of $D$ lies in two of the three members and each pair in one, so
$\psi_D(E)=\max(2E/3,E^2/3)$, which equals $E^2/3$ for $E\ge3$ and maps
$[3,\infty)$ into itself. By Lemma 2 of L214,
$E_{D^g}(R)=\psi_D(E_{D^{g-1}}(R))$, and induction from $E_{D^0}(R)=R$ gives
$E_{D^g}(R)=3(R/3)^{2^g}$. $\square$

## Proof of the claim

Let $g\ge0$, $R\ge3$, $\rho=\lceil3(R/3)^{2^g}\rceil$, $j=\lceil\log_2\rho\rceil$
and $B=B(\rho,\rho^\rho)$; then $\rho\ge3$ and $j\ge2$. The family $B^j$ is
intersecting and $(\rho^\rho+1)^j$-uniform by Lemmas 1 and 3 of L214, and $D^g$
is intersecting and $2^g$-uniform by Lemma A. So
$\mathcal F=(B^j)[D^g]$ is an intersecting family of $n$-sets with
$n=2^g(\rho^\rho+1)^j$, by Lemma 1 of L214.

*Spread.* For every $E>0$, $\psi_{B^j}(E)=E_{B^j}(E)=\psi_B^{(j)}(E)$ by the
definition of $\psi$ and Lemma 2 of L214. Lemma 2 applied to $(B^j)[D^g]$ and
Lemma A give

$$
E_{\mathcal F}(R)=\psi_B^{(j)}\bigl(E_{D^g}(R)\bigr)
=\psi_B^{(j)}\bigl(3(R/3)^{2^g}\bigr).
$$

Since $3(R/3)^{2^g}\le\rho$ and, by Lemma 3 of L214 with $\kappa=1$,
$\psi_B(E)\le E/2$ for $0<E\le\rho$, the right side is at most
$\rho\,2^{-j}\le1$. Hence $|\mathcal F_T|\le R^{-|T|}|\mathcal F|$ for every
nonempty $T$.

*Cores.* Let $k\ge3$. The family $D^g$ is intersecting and
$k$-sunflower-free by Lemma A, and $B^j$ is intersecting, so by Lemma B every
$k$-sunflower of $\mathcal F$ has a core of at least $2^g$ points. $\square$

## Size of the forced cores

For fixed $R>3$ and $s=2^g$, $\log_2\rho=s\log_2(R/3)+O(1)$ and
$\log_2n=\log_2s+j\log_2(\rho^\rho+1)=(1+o(1))\,\rho(\log_2\rho)^2$, so
$\log_2\log_2n=(1+o(1))\,s\log_2(R/3)$ as $g\to\infty$. Along these families
every sunflower core has at least $(1-o(1))\log_2\log_2n/\log_2(R/3)$ points
while the uniform measure stays $R$-spread. Cores of exactly $2^g$ points
occur. In $B$, three members of the first kind with pairwise disjoint
transversals form a $3$-sunflower with core $\{x\}$, which needs $\rho\ge3$.
In $B^j$, take such members at the top level, a $3$-sunflower of $B^{j-1}$ with
a one-point core over $x$, and arbitrary members over the other points; this is
a $3$-sunflower of $B^j$ whose core is the single point reached through $x$ at
every level. Choosing one member of $D^g$ as the common fiber over that point,
and arbitrary fibers elsewhere, gives a $3$-sunflower of $\mathcal F$ with a
core of $2^g$ points.
