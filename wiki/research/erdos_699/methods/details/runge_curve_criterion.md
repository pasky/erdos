---
name: research/erdos_699/methods/details/runge_curve_criterion
title: "Erdős 699: an effective Runge criterion for fixed curves"
desc: "Bad pairs on a fixed curve are effectively bounded when sufficiently many numerator fibers contribute poles to explicit S-integral functions; at indices four and five, three finite pole fibers suffice."
created: 2026-09-22T16:35:35Z
updated: 2026-09-22T19:12:28Z
---

# Erdős 699: an effective Runge criterion for fixed curves

[[research/erdos_699/_index|P699 research]] ·
[[research/erdos_699/remaining/details/cubic_curves|Finiteness on fixed curves]]

***

Fix an index $i\ge4$, let $S_i=\{p:p<i\}$ and $s_i=|S_i|$, and let
$C\subset\mathbf A^2_{n,j}$ be a fixed geometrically irreducible curve
over $\mathbf Q$ on which $n$ is nonconstant. Define

$$H_i=\begin{cases}i,&i\text{ is prime},\\1,&i\text{ is composite},\end{cases}
\qquad
g_t=H_i\frac{\prod_{r=0}^t(j-r)}{n-t}\quad(0\le t<i).\tag{1}$$

Work on the smooth projective normalization $\overline C$. A finite
fiber $n=t$ is called a **pole fiber** here if it contains a pole of
at least one of the functions $j,g_0,\ldots,g_{i-1}$.

**Proposition.** If at least $s_i+1$ of the fibers
$n=0,1,\ldots,i-1$ are pole fibers, then all bad triples with this
index and $(n,j)\in C$ form an effectively determinable finite set.

For indices four and five, **three finite pole fibers suffice**. More
generally, the criterion asks for the following numbers:

| Index | Required finite pole fibers |
| --- | ---: |
| $4,5$ | 3 |
| $6,7$ | 4 |
| $8,9$ | 5 |
| $12$ | 6 |
| $14$ | 7 |

This criterion applies to the given curve, with a bound depending
effectively on that curve. It does not make all fixed curves effective
and does not put all bad pairs on finitely many curves.

## The integral functions supplied by badness

For every bad triple, the values of $n,j,g_0,\ldots,g_{i-1}$ lie in
$\mathbf Z[S_i^{-1}]$.

To prove this, let $p\ge i$ and $p^A\Vert n-t$. Since $0\le t<i\le p$,
this is the unique numerator factor divisible by $p$ in $\binom ni$.
Unless $p=i$ is prime and $A=1$, the prime $p$ divides $\binom ni$.
Badness implies $p\nmid\binom nj$, so Lucas's theorem gives

$$
j\bmod p^A\in\{0,\ldots,t\}.
$$

Consequently $p^A\mid\prod_{r=0}^t(j-r)$. In the exceptional case
$p=i$, $A=1$, the factor $H_i$ clears the denominator. This proves
the assertion at every prime outside $S_i$.

The factor $H_i$ is a fixed integer multiplier. It does not add a
prime to the allowed denominator set. In particular the index-five
functions are $5\prod_{r=0}^t(j-r)/(n-t)$, and their allowed
denominator primes remain exactly $2,3$.

## Runge's condition and its effective conclusion

Use the geometric form of Runge's theorem given by
Levin, *Variations on a theme of Runge*, Theorem 2 in the arXiv version.
This is Theorem 1.2 in the
[published article](https://doi.org/10.5802/jtnb.634).
For a rational function $\phi$ on a smooth projective curve over a
number field $K$, let $r_K$ be the number of $K$-irreducible components
of the support of its pole divisor: equivalently, the number of Galois
orbits of poles. If $S$ contains the archimedean places and
$r_K>|S|$, the points satisfying $\phi(P)\in\mathcal O_{K,S}$ form
an effectively determinable finite set.

Here let $D$ be the union of the poles of
$n,j,g_0,\ldots,g_{i-1}$. Choose integer coefficients in a linear
combination $\phi$ of these functions so that its pole support is
exactly $D$. This can be done effectively: at each of the finitely
many poles, cancellation of all terms of largest pole order imposes
a proper linear condition on the coefficients. Avoid those finitely
many conditions. Integer coefficients preserve $S_i$-integrality.

Each finite pole fiber contributes at least one Galois orbit to $D$.
These orbits are distinct, because their values of the rational
function $n$ are distinct rational integers. The nonconstant function
$n$ has a pole, supplying at least one further orbit, disjoint from
all finite fibers. Thus the proposition's hypothesis gives

$$r_{\mathbf Q}\ge s_i+2>
|\{\infty\}\cup S_i|=s_i+1.$$

Runge's theorem proves the proposition. Rational nonsingular points
of the original plane curve lift to rational points of its
normalization. Its finitely many singular points can be determined
separately, so they cause no gap.

The argument requires no enlargement of $S_i$ for auxiliary
coordinates. More generally, a known fixed denominator can be
cleared by scaling the corresponding rational function by an
integer, without changing its pole support.

## How a fiber supplies a pole

Let $P\in\overline C$ satisfy $n(P)=t$. If $j$ has a pole at $P$, then
$P\in D$. If $j(P)$ is finite and not in $\{0,\ldots,t\}$, then the
numerator of $g_t$ is nonzero there and its denominator vanishes, so
$g_t$ has a pole.

Even a point above the grid can contribute. If $j(P)=r\in\{0,\ldots,t\}$,
put

$$e_n=\operatorname{ord}_P(n-t),\qquad
e_j=\operatorname{ord}_P(j-r).$$

The other factors in the numerator of $g_t$ are units at $P$, giving

$$
\operatorname{ord}_P(g_t)=e_j-e_n.\tag{2}
$$

When $j-r$ is identically zero, take $e_j=+\infty$; then $g_t$ is
identically zero and contributes no pole. Otherwise (2) is an exact
valuation identity. Thus a fiber with no pole has all its branches
above grid points and must satisfy

$$
\boxed{e_n\le e_j\quad\text{on every branch.}}\tag{3}
$$

The converse holds as well for a fixed fiber: if $j$ is finite there
and (3) holds at all its grid branches, then $g_t$ is regular. For
$u\ne t$, the denominator $n-u$ is nonzero on that fiber, so every
other $g_u$ is regular too.

In particular, if the proposition's sufficient fiber count fails,
at least $i-s_i$ of these finite fibers have this complete grid
property. This is only a necessary condition for failure of the
criterion: additional pole orbits, including multiple orbits in a
single fiber, can still make Runge's inequality hold.

## A corollary for curves smooth at the grid

Let $d=[\mathbf Q(C):\mathbf Q(n)]$ be the degree of the map
$n:\overline C\to\mathbf P^1$. Suppose the plane curve is smooth at
every grid point $(t,r)$ lying on it in one fiber $n=t$.

If this fiber has no pole, (3) holds. At a smooth plane point, at
least one of $n-t,j-r$ has order one; therefore (3) forces $e_n=1$.
There is only one branch at each such grid point, so the entire fiber
contains at most $t+1$ points, all of multiplicity one. Since a fiber
has total multiplicity $d$, it follows that

$$
\boxed{d>t+1\quad\Longrightarrow\quad n=t\text{ is a pole fiber}.}\tag{4}
$$

The possibility $j=\infty$ in a finite $n$-fiber is already included:
it itself supplies a pole, so it cannot occur in the no-pole case.

Consequently, if $C$ is smooth at every point of the triangular grid
$0\le j\le n<i$, and $d\ge s_i+2$, then the first $s_i+1$ fibers
are pole fibers and all bad triples on $C$ are effectively
determinable. At index five this applies whenever $d\ge4$.

Singularities at grid points matter. Several normalized branches can
lie above one grid point, and a branch can have $e_n=e_j>1$.
Therefore the degree condition cannot be asserted for arbitrary
singular curves without the smoothness hypothesis.
