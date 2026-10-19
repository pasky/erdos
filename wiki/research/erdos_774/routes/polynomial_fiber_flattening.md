---
name: research/erdos_774/routes/polynomial_fiber_flattening
title: Polynomial flat representations and their extraction cost
desc: Prouhet identities flatten bounded coefficients on a profile-monochromatic progression, but that fiber already has its own ternary relation and full polynomial fibers lose uniform extraction; a sparse signed-span target is exactly height-three coloring.
tags: [E0774, flattening, proved, scoped-obstruction]
sources: []
created: 2026-09-19T01:50:00Z
updated: 2026-09-19T01:50:00Z
---


# Polynomial flat representations and their extraction cost

***

## Standing

The identity below is genuinely coefficient-safe and can preserve an
actual color after profile focusing. **It is not an extraction-preserving
color amplifier.** The focused progression already has a ternary relation
inside one fiber, independently of any seed, and the full fibers have
vanishing extraction in the required parameter regimes.

The critical moment palette-height theorem therefore remains unflattened
within a uniformly extracting family.

## 1. Exact common-moment representations

Fix $t\geq1$, and write

$$
w_t(j)=(1,j,\ldots,j^t),\qquad b=2^{t+1}.
$$

For $s\geq0$ and $h\geq1$, define

$$
P_s(z)=\prod_{i=0}^t(1-z^{2^i b^s}),\qquad
R_h(z)=\sum_{s=0}^{h-1}(1-P_s(z)),\qquad R_0=0.   \tag{1}
$$

Binary subset sums are distinct, so $P_s$ has coefficients $\pm1$
at precisely the exponents $mb^s$, $0\leq m<b$. Its constant
coefficient is one. The nonconstant supports of $1-P_s$ lie in

$$
[b^s,(b-1)b^s],
$$

which are disjoint for different $s$. Thus $R_h$ is flat, has
constant coefficient zero, and degree $(b-1)b^{h-1}$.

Each $P_s$ has a zero of order $t+1$ at $z=1$. If
$R_h(z)=\sum_m r_h(m)z^m$, evaluation of Euler derivatives gives

$$
\sum_m r_h(m)=h,\qquad
\sum_m r_h(m)m^j=0\quad(1\leq j\leq t).
$$

By the binomial theorem, for all integers $a,d$,

$$
\boxed{\sum_m r_h(m)w_t(a+dm)=h\,w_t(a).}        \tag{2}
$$

## 2. What complete-profile focusing does and does not prove

Let $A=(a_v)_{v\in V}$ be a finite family of nonzero integer vectors,
$n=|V|$, and suppose every $q$-coloring of $A$ has a monochromatic
nonzero relation of height at most $H$. Set

$$
T=1+(b-1)b^{H-1},\quad
B_{t,L}(A)=\{a_v\otimes w_t(j):v\in V, 0\leq j<L\}.
$$

Take $L$ at least a van der Waerden threshold for $q^n$ colors and
progression length $T$. In an arbitrary $q$-coloring of these indexed
columns, color $j$ by its complete vector of type colors. A progression
$a,a+d,\ldots,a+(T-1)d$, $d>0$, has a constant profile. Its type
colors give a monochromatic seed relation $u$. Formula (2) makes

$$
f(v,a+dm)=\operatorname{sgn}(u_v)r_{|u_v|}(m)
$$

a nonzero ternary relation in one actual color. The tensor sum is
$(\sum_vu_va_v)\otimes w_t(a)=0$. Distinct nonzero seed vectors
give distinct lifted vectors: the first moment coordinate determines
$a_v$, and the degree-one coordinate then determines $j$.

However, $T\geq b$. The coefficients of $P_0$, on the first $b$
nodes of that progression, already annihilate every degree-at-most-$t$
moment. They give a monochromatic ternary relation in **any one type's
fiber**. The seed's relation and height hypothesis are unnecessary for
color forcing in this construction. This correction was identified by a
separate reviewer and is part of the current standing.

The finite progression statement was checked, after the supplied digest, in
[Graham--Rothschild, Corollary 8](../../../../library/ramsey_theory/graham_rothschild_1971_ramseys_theorem_n_parameter_sets/_index.md).
No other Ramsey theorem is being substituted for its exact conclusion.

## 3. Full fibers destroy uniform extraction

For any nonzero $a_v$, its fiber is linearly isomorphic to

$$
W_t(L)=\{w_t(j):0\leq j<L\}.
$$

If $D\subseteq W_t(L)$ is dissociated, all $2^{|D|}$ subset sums
are distinct. Coordinate $\ell$, $0\leq\ell\leq t$, has integer
values between zero and $L^{\ell+1}$. Therefore

$$
2^{|D|}\leq\prod_{\ell=0}^t(L^{\ell+1}+1)
\leq(L+1)^{\binom{t+2}2},
$$

and consequently

$$
\boxed{\eta(B_{t,L}(A))\leq
\binom{t+2}2\frac{\log_2(L+1)}L.}                \tag{3}
$$

This upper bound uses one genuine subset of the lift, so an arbitrarily
good seed cannot remove the obstruction.

For the displayed representations, $L\geq T\geq2^{(t+1)(H-1)}$.
Writing $u=t+1\geq2$, monotonicity of
$\log_2(x+1)/x$ bounds (3) by

$$
u^2[u(H-1)+1]2^{-u(H-1)}.
$$

For $H\geq4$ this is decreasing in $u\geq2$: its logarithmic
derivative is at most $3/u-(H-1)\log2<0$. Thus

$$
\eta(B_{t,L}(A))\leq4(2H-1)4^{-(H-1)}\longrightarrow0,
\tag{4}
$$

uniformly in the chosen degree $t\geq1$.

### A loss for any complete-profile progression implementation

A uniformly random $Q$-coloring of $[0,L-1]$ has expected number
of monochromatic length-$T$ progressions at most $L^2Q^{1-T}$.
If this is less than one, some coloring avoids them all. Universal
progression focusing therefore requires

$$
L\geq Q^{(T-1)/2}.                               \tag{5}
$$

For a flat representation of $h\,w_t(0)$, $h\geq2$, using the
nodes $0,\ldots,T-1$, one must have $T\geq t+2$. Otherwise their
Vandermonde columns are independent, whereas subtracting the target gives
a nonzero relation (the coefficient at zero cannot cancel $h\geq2$).
The same statement holds on a translated progression.

Taking $Q=q^n$, (5) yields $L\geq q^{n(t+1)/2}$. The calculation
above with $H-1$ replaced by $n\log_2q/2$ gives, when
$n\log_2q\geq6$,

$$
\eta(B_{t,L}(A))\leq4(n\log_2q+1)q^{-n}.         \tag{6}
$$

Thus making Prouhet templates more efficient does not repair **full
intervals with complete-profile progression focusing**. This is not a
bound against sparse or nonpointwise lifts.

## 4. An exact sparse signed-span target

For a finite indexed nonzero vector family $C=(c_i)$, let
$\Sigma(C)=\{\sum_i\epsilon_ic_i:\epsilon_i\in\{0,\pm1\}\}$.
Then

$$
\boxed{\exists w\ne0:\ w,2w\in\Sigma(C)
\quad\Longleftrightarrow\quad
C\text{ has a nonzero relation of height at most three}.} \tag{7}
$$

If $w=\epsilon\cdot C$ and $2w=\delta\cdot C$, then
$2\epsilon-\delta$ is a nonzero height-three relation. It is nonzero
because coordinatewise $2\epsilon=\delta$ would force both to vanish.

Conversely, write a height-three relation $z$ coordinatewise as
$z=2\epsilon-\delta$, with both vectors ternary. If
$w=\epsilon\cdot C\ne0$, the desired representations follow.
If $w=0$, either $\epsilon$ is a nonzero ternary relation, or
$\epsilon=0$ and $\delta=-z$ is one. For any nonzero ternary
relation $\sum_i s_ic_i=0$, choose $s_j\ne0$. Then

$$
w=c_j\ne0,\qquad
2w=c_j-s_j\sum_{i\ne j}s_ic_i\in\Sigma(C).
$$

This proves (7). Forcing the signed-span property in some class of every
$Q$-coloring is therefore exactly a height-three chromatic lower bound,
not a weaker route around coefficient height. It still would not by
itself prove extraction for a tensor with such a carrier.

The algebraic identities, actual-color quantifiers, extraction bounds, and
Vandermonde scope are author-recorded; a separate reviewer checked them, and (7)
was checked separately. No computation was used; no extraction-preserving
flattening theorem is claimed.
