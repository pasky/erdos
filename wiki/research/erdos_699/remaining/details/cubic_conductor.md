---
name: research/erdos_699/remaining/details/cubic_conductor
title: "Erdős 699: conductor controlled by the cubic discriminant"
desc: "Removing an odd quadratic twist bounds the conductor by Disc(P). Bounded cubic discriminant gives an effective finite reduction; global finiteness remains open."
created: 2026-09-21T23:50:33Z
updated: 2026-09-21T23:50:33Z
---

# Erdős 699: conductor controlled by the cubic discriminant

[[research/erdos_699/_index|P699 research]] ·
[[research/erdos_699/remaining/details/cubic_elliptic|The elliptic curves]] ·
[[research/erdos_699/remaining/details/cubic_irreducibility|The integer cubics]]

***

The monic elliptic curve admits a useful normalization: its conductor is
bounded by an absolute constant times the discriminant of the coefficient
cubic. Consequently a fixed upper bound on that cubic discriminant gives
an effective finite set of possible bad triples. No uniform bound on the
cubic discriminant is proved here, so global finiteness remains open.

## 1. Removing the odd twist

For a hypothetical bad triple, use the established notation

$$n=2^h u,\quad c=n-j,\quad d=n-2j,\quad
t=v_2(j)=v_2(c),\quad m=h-t\ge2,$$

where $u$ is odd and $4\le j<n/2$. Put

$$w=u2^t,\qquad g=\gcd(u,3),\qquad v=u/g,\qquad
D_0=\operatorname{Disc}P>0.$$

Here $D_0$ is an integer. The preceding notes give odd positive integers

$$k=\frac{3jc}{2^{2t}(n-1)},\qquad
q=\frac{jcd}{2^{3t}(n-1)(n-2)},$$

and the integer moment $3j/u$. The latter implies $v\mid j$, hence
$v\mid c,d$. If $p^a\Vert v$, both $n-1$ and $n-2$ are $p$-adic units:
$p$ is odd and divides $n$. The displayed formulas therefore give

$$
v_p(k)\ge2a,\qquad v_p(q)\ge3a.
$$

Thus $k_0=k/v^2$ and $q_0=q/v^3$ are odd integers. Consider the integral
curve

$$
E_0:\quad y^2=x^3-k_0x+2q_0.
$$

The earlier curve $E_H$ is its quadratic twist by $v$. The discriminant
identity from the preceding notes becomes

$$\Delta(E_0)=64(k_0^3-27q_0^2)
=2^{2m+4}g^6D_0.\tag{1}$$

In (1), $\Delta(E_0)$ is the discriminant of the displayed equation,
which need not be minimal.

## 2. Conductor and a minimal-discriminant lower bound

Write $N_0$ for the conductor and $\Delta_{\min}$ for the minimal
discriminant. The conductor exponent at any prime is at most the
minimal-discriminant valuation, by Ogg's formula. Minimalization can only
decrease the discriminant valuation of an integral equation. Hence the
odd part of $N_0$ divides $g^6$ times the odd part of $D_0$.
The universal bound $v_2(N_0)\le8$ then gives

$$
N_0\le C D_0,\qquad C=2^8\cdot3^6.\tag{2}
$$

The local conductor bound is recorded in
[von Känel, §2.2 and the proof of Theorem 7.1](https://londmathsoc.onlinelibrary.wiley.com/doi/full/10.1112/tlms/tlu003).

Since $c_4(E_0)=48k_0$ has valuation four at two, (1) gives the exact,
model-independent identity

$$
v_2(\mathfrak j(E_0))=8-2m-v_2(D_0).\tag{3}
$$

On a minimal integral model $v_2(c_{4,\min})\ge0$. Applying
$\mathfrak j=c_{4,\min}^3/\Delta_{\min}$ therefore yields

$$v_2(\Delta_{\min})\ge2m+v_2(D_0)-8,
\qquad |\Delta_{\min}|\ge2^{2m-8}.\tag{4}$$

This remains valid when $t=0$ and $D_0$ has a nontrivial two-part.

## 3. Effective finiteness when the cubic discriminant is bounded

The exact formula for $D_0$ is

$$D_0=\frac{108j^2c^2(j-1)(c-1)}
{w^4(n-1)^3(n-2)^2}
\le\frac{384j^3}{w^4n^2}
\le\frac{48n}{w^4}=\frac{48\cdot2^m}{w^3}.\tag{5}$$

For the first inequality, use $j-1<j$, $c-1<c<n$,
$n-1\ge7n/8$, and $n-2\ge3n/4$; these hold since $n>2j\ge8$.
The second uses $j<n/2$, and the last equality uses $n=2^m w$.

**Proposition.** For every fixed $B\ge1$, the hypothetical bad triples
with $D_0\le B$ lie in an effectively bounded finite set.

**Proof.** The unconditional bound

$$\log|\Delta_{\min}(E)|\le
3N(E)(\log N(E))^2+124$$

holds for every elliptic curve over $\mathbb Q$ by
[von Känel, Corollary 6.2](https://londmathsoc.onlinelibrary.wiley.com/doi/full/10.1112/tlms/tlu003).
Combining it with (2) and (4) bounds

$$m\le M_B:=4+
\frac{3CB(\log(CB))^2+124}{2\log2}.$$

Since $D_0\ge1$, (5) gives $w^3\le48\cdot2^m$. Consequently
$n=2^m w\le48^{1/3}2^{4M_B/3}$. This is an explicit finite range for
$n$, and each row has finitely many admissible columns. $\square$

Equivalently, Shafarevich finiteness applied to (2) leaves finitely many
$\mathfrak j$-invariants. Equation (3) then bounds $m$, even if $v_2(D_0)$
varies. The displayed proof supplies an explicit bound directly.

## 4. What Szpiro would add

Assume Szpiro's conjecture
$|\Delta_{\min}(E)|\ll_\epsilon N(E)^{6+\epsilon}$; this is the conjecture
stated in [Masser's publisher abstract](https://smf.emath.fr/publications/note-conjecture-szpiro).
Equations (2), (4), and (5) then imply

$$j^{18+3\epsilon}\gg_\epsilon
n^{14+2\epsilon}w^{22+4\epsilon}.\tag{6}$$

Indeed, $(n/w)^2=2^{2m}\ll_\epsilon D_0^{6+\epsilon}$, and substituting
(5) gives (6). For every $\delta>0$, this entails

$$j\gg_\delta n^{7/9-\delta},\qquad
u2^t=w\ll_\delta n^{2/11+\delta}.$$

These are conditional restrictions, not conditional global finiteness.
When $u,t$ are fixed and $j/n$ stays inside $(0,1/2)$, one has
$D_0\asymp n$; conductor and discriminant bounds of the sizes above are
compatible with arbitrarily large $n$. Proving a uniform upper bound for
$D_0$, or obtaining another restriction that excludes this regime,
remains necessary. No enumeration was used in this note.
