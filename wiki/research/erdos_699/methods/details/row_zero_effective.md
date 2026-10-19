---
name: research/erdos_699/methods/details/row_zero_effective
title: "Erdős 699: an effective row-zero reduction at every fixed index"
desc: "For each fixed i>=4, bad triples whose row has bounded small-prime part form an effectively bounded set. Beyond that bound a selected small-prime maximum must occur at position zero."
created: 2026-09-22T06:54:00Z
updated: 2026-09-22T19:12:28Z
---

# Erdős 699: an effective row-zero reduction at every fixed index

[[research/erdos_699/_index|P699 research]] ·
[[research/erdos_699/archive/previous_bounds/effectivity|The effective S-part theorem]]

***

**Proposition.** Fix $i\ge4$ and $K\ge1$. There is an effectively
computable bound for every bad triple with
$[n]_{\{p:p<i\}}\le K$.

In particular, above an effective bound depending only on $i$, at least
one small prime has a strictly larger valuation in $n$ than in every
other numerator factor $n-1,\ldots,n-i+1$.

This is a reduction of possible position patterns, not effective
finiteness for an entire remaining index.

Write $S=\{p:p<i\}$ and let $H=i$ when $i$ is prime, $H=1$ otherwise.
Let $R_t$ be the part of $n-t$ supported on primes at least $i$.
Badness and Lucas's theorem give

$$
\frac{R_0}{\gcd(R_0,H)}\mid j.
$$

Consequently, if $j/n=a/q$ is reduced, then

$$
2\le q\le H[n]_S\le Q:=HK.
$$

For every $0\le t<i$, the same localization gives

$$R_t\mid H F_t(a,q),\qquad
 F_t(a,q)=\prod_{r=0}^t(at-qr).\tag{1}$$

To see this prime by prime, an active prime power dividing $n-t$ forces
$j\equiv r$ modulo that power for some $0\le r\le t$.
The identity $qj=an$ then gives $at-qr\equiv0$.
At the single possible denominator prime $p=i$, an inactive first power
is covered by $H$. No inversion of $q$ modulo a prime is needed.

Since $\gcd(a,q)=1$, the polynomial $F_t(a,q)$ is zero exactly when
$q\mid t$. For $q=2$ choose $t=1,3$; for $q\ge3$ choose $t=1,2$.
Both selected values in (1) are nonzero. As $0<a/q\le1/2$, their
product is bounded by $81Q^6$. Thus, for one of the two fixed polynomials

$$
f_2(X)=(X-1)(X-2),\qquad f_3(X)=(X-1)(X-3),
$$

we have

$$
[f_t(n)]_S\ge\frac{f_t(n)}{81H^2Q^6}.\tag{2}
$$

BEG's effective Theorem 2.2, already used in the
[effectivity note](../../archive/previous_bounds/effectivity.md), supplies computable
$C\ge1$ and $\kappa>0$ such that, for both polynomials,

$$
[f_t(n)]_S\le C f_t(n)^{1-\kappa}.
$$

Combining this with (2), and using $f_t(n)\ge n^2/4$ for $n\ge6$, gives
the effective bound

$$
\boxed{n\le2(81CH^2Q^6)^{1/(2\kappa)}.}\tag{3}
$$

For the last assertion take $K=\operatorname{lcm}(1,\ldots,i-1)$.
If $[n]_S>K$, some $p<i$ has
$v_p(n)>\lfloor\log_p(i-1)\rfloor$; otherwise $[n]_S$ divides $K$.
For every $1\le t<i$, this forces $v_p(n-t)=v_p(t)<v_p(n)$.
So its unique selected maximum is at position zero.

The stronger [index-six and index-seven result](../../archive/other_approaches/low_crt_row_zero.md)
excludes the complementary position patterns at every admissible row,
using exact fixed-slope divisibilities. The present argument supplies
the effective reduction uniformly for every fixed $i\ge4$.
