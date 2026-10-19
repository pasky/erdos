---
name: research/leads/projective_plane_bounded_blocking/parity_construction
title: A parity construction in characteristic two
desc: Three conics give cap six in PG(2,2^h) for h at least two; the proof uses additive characters, while a specified multiplicative identity for distinct conics in odd characteristic is impossible and additive graphs force cap at least p.
created: 2026-10-16T19:59:11Z
updated: 2026-10-16T20:53:47Z
---

# A parity construction in characteristic two

***

This page records the one constant-cap mechanism developed in the
[[research/leads/projective_plane_bounded_blocking/_index|bounded-blocking proof sketch]],
with a complete author proof by Plasma AI and no independent review, and
limitations of two possible extensions to other planes. The
construction is not claimed to be new. Szőnyi's survey,
[[../library/set_systems/szonyi_1992_blocking_sets_finite_planes_spaces/_index|Blocking sets in finite planes and spaces]],
reports on printed p. 102, as Theorem 4.3, the result of Illés, Szőnyi and
Wettl (*Blocking sets and maximal strong representative systems in finite
projective planes*, Mitt. Math. Sem. Giessen 201 (1991), 97–107) that
PG$(2,2^r)$ has a blocking set with at most $5$ points on a line when $r$
is even and at most $6$ when $r$ is odd, the latter from three suitably
chosen conics. That original was not read, and whether its conics are the
ones below was not checked.

## The construction

**Theorem.** Let $q=2^h$ with $h\ge2$, and let $\gamma_1,\gamma_2,\gamma_3$ be
distinct nonzero elements of $\mathbb F_q$ with
$\gamma_1+\gamma_2+\gamma_3=0$. In PG$(2,q)$ let $C_i$ be the conic
$\gamma_iX^2=YZ$ and $S=C_1\cup C_2\cup C_3$. Then $|S|=3q-1$, and every
line meets $S$ in at least $1$ and at most $6$ points.

For example $\gamma=(1,g,1+g)$ with $g\notin\{0,1\}$, which exists because
$q\ge4$.

*Proof.* Use the chart $Z=1$ with $x=X/Z$, $y=Y/Z$, and the points
$O=(0:0:1)$, $V=(0:1:0)$ and $N_0=(1:0:0)$. The conic $C_i$ consists of the
$q$ affine points $(x,\gamma_ix^2)$ and, on $Z=0$, of $V$ alone. Two of the
conics meet where $\gamma_ix^2=\gamma_jx^2$, that is only in $O$ and $V$.
Hence $|S|=3(q+1)-4=3q-1$. Let $\mathrm{Tr}:\mathbb F_q\to\mathbb F_2$ be
the absolute trace. It is additive, satisfies $\mathrm{Tr}(u^2)=\mathrm{Tr}(u)$,
and $u\mapsto\mathrm{Tr}(\lambda u)$ is a nonzero functional for every
$\lambda\ne0$. Every line is of one of four kinds.

- The line $Z=0$ meets each conic only in $V$: one point.
- A horizontal line $y=d$ passes through $N_0\notin S$ at infinity and meets
  $C_i$ where $\gamma_ix^2=d$, in exactly one point because squaring is a
  bijection of $\mathbb F_q$: between one and three points.
- A vertical line $x=a$ contains $V$ and the points $(a,\gamma_ia^2)$:
  between two and four points.
- A line $y=mx+d$ with $m\ne0$ has its point $(1:m:0)$ at infinity outside
  $S$, and meets $C_i$ where $L_i(x)=d$ for $L_i(x)=\gamma_ix^2+mx$.

In the last case $L_i$ is additive with kernel $\{0,m/\gamma_i\}$, so the
line meets $C_i$ in exactly two points when $d$ lies in the index-two
subgroup $H_i=L_i(\mathbb F_q)$, and in none otherwise. For
$\lambda=\gamma_i/m^2$,

$$
\mathrm{Tr}\bigl(\lambda L_i(x)\bigr)
=\mathrm{Tr}\bigl(\sqrt{\lambda\gamma_i}\,x\bigr)+\mathrm{Tr}(\lambda mx)=0
\qquad\text{for all }x,
$$

because $\sqrt{\lambda\gamma_i}=\gamma_i/m=\lambda m$. Both $H_i$ and the
kernel of $u\mapsto\mathrm{Tr}(\lambda u)$ have index two, so
$H_i=\{d:\varepsilon_i(d)=0\}$ with
$\varepsilon_i(d)=\mathrm{Tr}(\gamma_id/m^2)$. Now

$$
\varepsilon_1(d)+\varepsilon_2(d)+\varepsilon_3(d)
=\mathrm{Tr}\bigl((\gamma_1+\gamma_2+\gamma_3)d/m^2\bigr)=0,
$$

so an even number of the $\varepsilon_i(d)$ equal $1$, and the line meets
one or three of the conics. It therefore contains at least the two points
of one conic and at most six points of $S$. $\square$

The [evidence entry point](evidence/main.py) checks the statement by direct
incidence counts for $h=2,\dots,7$, with six attained for $h\ge3$. As a
negative control it checks that $\gamma=(1,g,g^2)$, whose sum is nonzero
there, leaves a line uncovered for $h=3,\dots,7$. These finite checks guard
the computation; the theorem for every $h$ rests on the proof.

For $q=2$, a full line is already a blocking set with cap three, so a cap
of six also covers that remaining characteristic-two Desarguesian plane.

**The mechanism.** For each slope, whether a line meets a given conic is an
affine condition over $\mathbb F_2$ on its intercept. A linear relation
among the three conditions forces an odd number of them to hold. Loads are
then controlled exactly, not statistically: the cap is the sum of the
three conics' bounded intersections. The resulting bounded distribution
still satisfies the variance identity of the
[[research/leads/projective_plane_bounded_blocking/identities|all-plane identities]].
For even $h$ it is weaker than the reported cap $5$.

## Why it does not reach odd characteristic

**No relation among conics in odd characteristic.** Let $q$ be odd and let
$\eta$ be the quadratic character of $\mathbb F_q$. For a nondegenerate
conic $v^{\mathsf T}Mv=0$ and a line spanned by $v_1,v_2$, with coordinate
vector $u=v_1\times v_2$, the restricted binary form has discriminant

$$
(v_1^{\mathsf T}Mv_2)^2-(v_1^{\mathsf T}Mv_1)(v_2^{\mathsf T}Mv_2)
=-u^{\mathsf T}\operatorname{adj}(M)\,u,
$$

the identity of Lagrange when $M=I$. So the line meets the conic in two,
one or no points as $\eta(-Q^*(u))$ is $1$, $0$ or $-1$, where
$Q^*(u)=u^{\mathsf T}\operatorname{adj}(M)u$. Whether a line meets a conic
is thus governed by a multiplicative character of a quadratic form in the
line coordinates. The characteristic-two argument used an identity among
the hit conditions; the analogous identity for a nonempty family of
distinct conics $C_i$, $i\in I$, is $\prod_{i\in I}Q_i^*=cR^2$ for a
nonzero constant $c$ and a polynomial $R$, which
would fix the product of the characters $\eta(-Q_i^*(u))$. A
nondegenerate ternary quadratic form is absolutely irreducible, so unique
factorization pairs the $Q_i^*$ into proportional forms. If
$\operatorname{adj}(M_j)=\nu\operatorname{adj}(M_i)$, then
$\det(M_j)M_j=\operatorname{adj}(\operatorname{adj}M_j)=\nu^2\det(M_i)M_i$,
so $C_j=C_i$. Distinct conics therefore admit no such polynomial identity. The
lemma excludes only this identity; it does not by itself show that some
line misses every conic.

This lemma explains, at the level of mechanism, the theorem of Ughi
(*On $(k,n)$-blocking sets which can be obtained as a union of conics*,
Geom. Dedicata 26 (1988), 241–245) that the survey reports on p. 102: in
PG$(2,q)$, $q$ odd, a union of $c$ conics never blocks every line once $q$
is large compared to $c$, while $c\log q$ suitable conics do. The original
was not read, and turning the lemma into Ughi's theorem needs character
sum estimates not supplied here.

**Additive pieces have caps of order $p$.** Let $q=p^h$ and let $f$ be an
$\mathbb F_p$-linear map of $\mathbb F_q$. In any affine chart, a point set
containing the graph $\{(x,f(x))\}$ meets some line in at least $p$ points.

*Proof.* Fix $x_0\ne0$ and put $m=f(x_0)/x_0$. The kernel $K$ of
$x\mapsto f(x)-mx$ is an $\mathbb F_p$-subspace containing $x_0$, so
$|K|\ge p$, and the line $y=mx$ contains $(x,f(x))$ for every $x\in K$.
$\square$

The conics above are graphs of $x\mapsto\gamma_ix^2$, which is
$\mathbb F_2$-linear. Any construction of the same kind in characteristic
$p$ contains such graphs and so has cap at least $p$, in line with the
reported bounds $p+1$ of Boros and $4$ of Bruen and Fisher for $p=3$. For
$q=p$ prime the $\mathbb F_p$-linear maps are $x\mapsto cx$, whose graphs
are lines. The mechanism therefore gives no bounded cap along any family
whose characteristic grows, and in particular nothing for the prime-order
planes PG$(2,p)$. This obstructs the mechanism class only, not other
constructions.
