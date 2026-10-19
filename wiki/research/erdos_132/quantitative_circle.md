---
name: research/erdos_132/quantitative_circle
title: A quantitative circular concentration threshold
desc: |
  A circle with at least C q^$31/32$ points forces many rare distances;
  rarity plus diameter inactivity is at least a power of n.
sources: []
research_state: closed
created: 2026-09-23T05:40:00Z
updated: 2026-09-24T22:12:56Z
---


# A quantitative circular concentration threshold

***

**Subsequent improvement:** [weighted_circle_energy](weighted_circle_energy.md)
replaces the sufficient exponent $31/32$ below by $7/8$ and improves
the diameter-inactivity exponent $1/96$ to $1/24$. The older proof is
retained; its conclusions remain valid but weaker.

The [circle incidence argument](circle_incidence.md) admits an explicit
sublinear threshold. This remains a restricted result, not a solution of
the two unrestricted questions.

**Theorem.** There is an absolute constant $C$ such that, if a circle
contains $m\ge C(q(A)+1)^{31/32}$ points of $A$, then


$$
R(A)\ge m/4. \tag{1}
$$


Take all the points on the circle, with angular set $B$, as the anchor.
Put


$$
Q=q(A)+1,\qquad H=2Q/m,\qquad K=|B-B|/m.
$$


The chord formula gives $1\le K\le H$. The pinned spectra used in
the circle note have size at least $m/2$. For points at different
positive radii about the anchor center, their overlap is at most


$$
C_0(K^{4/3}m^{2/3}+K^2).
$$


If $m\ge C_1H^7$, apply the union lower bound to
$L=\lceil2H\rceil\le3H$ distinct radii. Their spectra would have union
at least $Lm/2-O(H^{10/3}m^{2/3}+H^4)>Q$, a contradiction for large
enough absolute $C_1$. Thus there are $k=O(H)$ occupied positive radii.

For their angular sets $B_i$, the covering argument gives


$$
B_i\subseteq X_i+(B-B),\qquad |X_i|\le H.
$$


Set $U=B-B$, $V=2B-2B$, $W=4B-4B$, with sizes $u,v,w$.
The checked Plünnecke--Ruzsa input yields


$$
u=Km,\qquad v\le K^4m,\qquad w\le K^8m.
$$


The angular differences for any circle-pair type are covered by at most
$H^2$ translates of $V$. Compare the anchor chord spectrum with just
one such translate for a different unordered radius pair. The cosine
relation is nondegenerate, as proved in the circle note. Its overlap
lemma, using $U-U=V$ and $V-V=W$, gives at most


$$
C_2\left(\frac{(vw)^{2/3}}{(uv)^{1/3}}+\frac wu+1\right)
\le C_3(K^{19/3}m^{2/3}+K^7)
$$


common values. There are $O(H^2)$ other radius-pair types. Including the
at most $k=O(H)$ values incident with the possible center, only


$$
O(H^{31/3}m^{2/3}+H^{11}+H)
$$


anchor chord values occur outside the anchor circle. Each remaining
positive chord value has all its pairs on that circle and therefore has
unordered multiplicity at most $m\le|A|$. Consequently


$$
R(A)\ge\frac{m-1}{2}
-C_4(H^{31/3}m^{2/3}+H^{11}+H). \tag{2}
$$


The condition $m\ge C_5H^{31}$, for a sufficiently large absolute
constant, implies the earlier size requirement and makes (2) at least
$m/4$. Since $H=2Q/m$, this condition is equivalent up to an absolute
constant to $m\ge C Q^{31/32}$, proving (1).

## Diameter inactivity tradeoff

Let $t(A)$ be the number of points not incident with a diameter pair.
There is an absolute $c>0$ such that


$$
R(A)+t(A)+1\ge c |A|^{1/96}. \tag{3}
$$


Write $n=|A|$, $R=R(A)$, and $s=R+t+1$. Suppose
$s\le c n^{1/96}$. For sufficiently small absolute $c$ this implies
$t<n/2$, $q(A)+1\le n/2+R+1\le n$, and the size hypothesis below.
The $m_0=n-t$ diameter-active points lie on a constant-width boundary,
and their palette satisfies


$$
q\le n/2+R\le m_0/2+(t/2+R).
$$


Apply the [quantitative rank inverse](quantitative_rank_inverse.md) with
$L=t/2+R$. Its parameter satisfies
$E+1=\lceil2t+4R+4\rceil+1\le6s$. It produces a circle containing at least


$$
m\ge\frac{n}{155520s^3}
$$


points. The rank lemma's condition $m_0\ge1000(E+1)^3$ holds under the
assumed bound on $s$, after reducing $c$ and absorbing small orders.
The displayed $m$ exceeds $C(q(A)+1)^{31/32}$ when $c$ is sufficiently
small. Formula (1) then gives


$$
R\ge\frac{n}{622080s^3}>s,
$$


a contradiction. This proves (3), with small $n$ handled by a further
decrease of $c$.

In particular, bounded rarity forces every circle to contain
$O(n^{31/32})$ points and forces $t(A)=\Omega(n^{1/96})$. Rarity diverges
when $t(A)=o(n^{1/96})$. An arbitrary set may have linearly many inactive
points, so neither unrestricted question follows.

The author checked the exponents, the uniform cosine incidence input
and its degeneracies, and the rank-inverse application; the argument is
author-recorded. All external ingredients and their full primary passages are
already recorded in the linked source notes.
