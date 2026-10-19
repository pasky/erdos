---
name: research/erdos_699/remaining/details/cubic_curves
title: "Erdős 699: finiteness on every fixed algebraic curve"
desc: "Siegel's theorem, polynomial abc, and a two-circle argument prove that every fixed algebraic curve contains only finitely many bad cubic pairs, with no restriction on the odd part of n. Global nondensity remains unproved."
created: 2026-09-22T00:15:00Z
updated: 2026-09-22T19:12:28Z
---

# Erdős 699: finiteness on every fixed algebraic curve

[[research/erdos_699/_index|P699 research]] ·
[[research/erdos_699/remaining/details/cubic_uniform|The endpoint divisibilities]] ·
[[research/erdos_699/remaining/details/cubic_elliptic|The elliptic approach]]

***

**Every fixed algebraic curve in the $(n,j)$-plane contains only finitely
many bad pairs with index three.** The odd part of $n$ may vary without
restriction. More generally, the result holds for the endpoint conditions
together with a fixed finite set of allowed denominator primes for $j/n$.

Finiteness for each fixed exponent $h$ was already known from
$3u^3<2^h$. The theorem here permits $h$ to grow without bound while
fixing an arbitrary polynomial relation $F(n,j)=0$.

The proof uses Siegel's theorem to reduce to rational curves, polynomial
abc to remove a common factor from the remaining parameterization, and
the two-circle argument below to finish.

This is not global finiteness: an infinite set in the plane can meet every
fixed curve only finitely often. It does mean that **a global Zariski
nondensity theorem would now imply finiteness of all bad cubic pairs**,
without first bounding the odd part of $n$.

## 1. A polynomial rigidity lemma

**Lemma.** Let $N(X)=aX^d$, where $a>0$ and $d\ge1$, and let
$J\in\mathbb R[X]$ have degree at most $d$. Suppose

$$
N-1\mid J(J-1),\qquad N-2\mid J(J-1)(J-2).\tag{1}
$$

Then

$$
J\in\{0,1,N,N-1,2N-2,2-N\}.\tag{2}
$$

**Proof.** Write $J(X)=\sum_{i=0}^d b_iX^i$, and let $\zeta$ range over
the $d$th roots of unity. Set

$$
R_1=a^{-1/d},\qquad R_2=(2/a)^{1/d}.
$$

For every $\zeta$, the first divisibility says that
$J(R_1\zeta)\in\{0,1\}$, while the second says that
$J(R_2\zeta)\in\{0,1,2\}$. In particular both sets of values are real.

Since the $b_i$ are real, reality on a circle of radius $R$ gives

$$\sum_{i=0}^d b_iR^i\zeta^i
=\sum_{i=0}^d b_iR^i\zeta^{-i}.$$

The characters $1,\zeta,\ldots,\zeta^{d-1}$ are linearly independent as
functions on the $d$th roots of unity. Comparing their coefficients gives

$$
b_iR^i=b_{d-i}R^{d-i}\qquad(1\le i\le d-1).\tag{3}
$$

Apply (3) at both radii. Since $R_2/R_1=2^{1/d}\ne1$, a nonzero
$b_i$ requires $i=d-i$. Thus

$$
J(X)=\lambda N(X)+\mu
$$

unless $d$ is even, in which case there can also be a term $bX^{d/2}$.

Suppose that this extra term is nonzero. On the first circle, its two
values are

$$
\lambda+\mu\pm b/\sqrt a.
$$

They are distinct and both belong to $\{0,1\}$, so their absolute
difference is one. On the second circle the two values instead have
absolute difference $\sqrt2$. This is impossible for two members of
$\{0,1,2\}$. Hence the extra term vanishes.

Finally $\lambda+\mu\in\{0,1\}$ and
$2\lambda+\mu\in\{0,1,2\}$. The six choices give exactly (2).
$\square$

In particular, no such polynomial family can satisfy
$4\le J(X)<N(X)/2$ for arbitrarily large positive $X$.

## 2. Polynomial abc removes the common factor

We use the following characteristic-zero form of Mason–Stothers:
if nonzero pairwise coprime polynomials $U,V,W$, not all constant,
satisfy $U+V=W$, then

$$\max(\deg U,\deg V,\deg W)
\le\deg\operatorname{rad}(UVW)-1.\tag{4}$$

Here $\operatorname{rad}$ retains each distinct irreducible factor once.
For a short proof, the nonzero Wronskian $U'V-UV'$ is divisible by
$UVW/\operatorname{rad}(UVW)$: at a root of any of the three polynomials
of multiplicity $b$, it vanishes to order at least $b-1$.
Comparing degrees gives the bound for $\deg W$; permutation gives the
other two. This is also the statement proved in
[Mathlib's Mason–Stothers theorem](https://leanprover-community.github.io/mathlib4_docs/Mathlib/NumberTheory/FLT/MasonStothers.html).

**Lemma.** Let

$$N=T^rD,\qquad J=LD,\qquad r\ge1,\quad
D,L\in\mathbb Q[T]\setminus\{0\},\quad L(0)\ne0,\quad\deg L\le r.$$

Suppose

$$A=\frac{3J(J-1)}{N-1},\qquad
B=\frac{J(J-1)(J-2)}{(N-1)(N-2)}\tag{5}$$

are polynomials, and $4\le J(T)<N(T)/2$ holds for an unbounded sequence
of positive real $T$. Then $D$ is constant. In fact these hypotheses
are impossible, by the two-circle lemma.

**Proof.** Put $S=T^r$, $e=\deg D$, and $\ell=\deg L$.
The physical inequalities give $\deg(S-L)=r$. Also $J$ is nonconstant:
otherwise the first quotient in (5) would force $J\in\{0,1\}$.
Thus $\ell+e>0$.

Since $\gcd(D,(N-1)(N-2))=1$ and $D\mid J$, (5) implies $D\mid A,B$.
Consequently the normalized coefficient cubic

$$P(z)=\frac{B+(A-3B)z+(3J-2A+3B)z^2
+(N-3J+A-B)z^3}{D}\tag{6}$$

belongs to $\mathbb Q[T,z]$ and satisfies $P(1)=S$.
Its coefficients equal those of

$$\frac{6}{D(N-1)(N-2)}
\sum_{i=0}^3\binom J{3-i}\binom{N-J}{i}z^i.$$

The two polynomials

$$k=\frac{3L(S-L)}{N-1},\qquad
q=\frac{L(S-L)(S-2L)}{(N-1)(N-2)}\tag{7}$$

are also in $\mathbb Q[T]$. Indeed, modulo $N-1$ the product
$J(N-J)$ is $-J(J-1)$, and modulo $N-2$ the product
$J(N-J)(N-2J)$ is $2J(J-1)(J-2)$. The divisibilities in (5), and
coprimality with $D$, give (7). Neither polynomial is zero; for $q$
this also follows from $N-2J>0$ along the given sequence.

Write $\kappa=\deg k$ and $\lambda=\deg q$. Then

$$
\kappa=\ell-e,\qquad \lambda\le\ell-2e.\tag{8}
$$

The inequality for $\lambda$ also handles cancellation in the leading
term of $S-2L$ when $J/N$ tends to $1/2$.
The cubic discriminant identity gives

$$k^3-27q^2=T^{2r}H,\qquad
H=\frac{\operatorname{Disc}_z P}{4}\in\mathbb Q[T].\tag{9}$$

It can be checked directly from (6) and (7); equivalently,

$$H=\frac{27L^2(S-L)^2(DL-1)(D(S-L)-1)}
{(N-1)^3(N-2)^2}.$$

The displayed expression is positive on the given physical sequence,
so $H\ne0$. Moreover,
$k(0)=3L(0)^2$ and $q(0)=L(0)^3$, so $T\nmid kq$.

Let $G=\gcd(k^3,q^2)$. Since $T\nmid G$, (9) implies
$G\mid H$. Apply (4) to the pairwise coprime polynomials

$$\frac{k^3}{G},\qquad -\frac{27q^2}{G},\qquad
T^{2r}\frac HG.$$

They are not all constant, since the last has a zero at zero. Their
distinct roots lie among the roots of $k$, $q$, $T$, and $H/G$.
Apply (4) to the degree of the third polynomial. It gives

$$
2r+\deg(H/G)\le\kappa+\lambda+\deg(H/G).
$$

Cancel the common term and use (8):

$$
2r\le\kappa+\lambda\le2\ell-3e\le2r-3e.
$$

Therefore $e=0$, as required. Now $N=aT^r$ with $a>0$, and the
two-circle lemma applied to (5) excludes the physical inequalities.
$\square$

## 3. Finiteness on every fixed algebraic curve

**Theorem.** Fix a finite set $\mathcal S$ of rational primes and a
nonzero polynomial $F\in\mathbb Q[n,j]$. There are only finitely many
integer pairs $(n,j)$ satisfying

$$\begin{gathered}
4\le j<n/2,\qquad F(n,j)=0,\\
\frac jn,\quad
\frac{3j(j-1)}{n-1},\quad
\frac{j(j-1)(j-2)}{(n-1)(n-2)}
\ \in\mathbb Z[\mathcal S^{-1}].
\end{gathered}\tag{10}$$

The last two quantities may in particular be integers. Every bad pair
with index three satisfies (10) with $\mathcal S=\{2,3\}$. Indeed the
endpoint conditions make the last two quantities integers, and
$3j/u\in\mathbb Z$ for $n=2^hu$ gives
$j/n\in\tfrac13\mathbb Z[1/2]$.

**Proof.** Suppose infinitely many pairs satisfy (10). Choose an
irreducible component of $F=0$ containing infinitely many of them.
It is geometrically irreducible: otherwise its rational points lie
in finite intersections of distinct geometric conjugate components.
The function $n$ is nonconstant, since each fixed row has only finitely
many admissible columns.

Take the affine graph of the five rational functions

$$n,\quad j,\quad j/n,\quad
A=\frac{3j(j-1)}{n-1},\quad
B=\frac{j(j-1)(j-2)}{(n-1)(n-2)}.$$

It has infinitely many $\mathcal S$-integral points. Siegel's theorem
therefore says that its smooth projective model has genus zero and at
most two geometric points at infinity, meaning the union of poles of
these five functions. The precise $S$-integral statement is recalled in
[Corvaja–Zannier's primary abstract](https://annals.math.princeton.edu/2004/160-2/p09).
The model has rational points and hence is $\mathbb P^1$ over $\mathbb Q$.

First, $j/n$ cannot be constant. Otherwise $j=\theta n$ for some
$0<\theta<1/2$. The function $A$ has poles over $n=1$, and $B$ has
poles over $n=2$: their numerators there are respectively
$3\theta(\theta-1)$ and $2\theta(2\theta-1)(2\theta-2)$, both nonzero.
Together with a pole of $n$, these give at least three distinct points
at infinity, contrary to Siegel's theorem.

Let $I$ be the union of the poles of $n$ and $j$ alone. It is nonempty
and contains at most two geometric points. There are three cases.

**Two rational points in $I$.** Choose a rational parameter $T$ putting
them at zero and infinity. Then $n,j\in\mathbb Q[T,T^{-1}]$, and at
each end at least one of these Laurent polynomials has a pole.
For every prime $p$, integrality of $n,j$ bounds $v_p(T)$ both above and
below: as $v_p(T)$ tends to either infinity, the term describing the
corresponding pole uniquely dominates and has negative valuation.
Outside a fixed finite set of primes all nonzero coefficients are units,
so these bounds force $v_p(T)=0$. At the remaining primes the bounds are
fixed finite intervals. Only finitely many rational $T$ are possible,
contrary to the assumed infinite set.

**Two conjugate points in $I$.** Along an infinite subsequence $n$ tends
to infinity, so the real points approach a pole of $n$. (If both poles
are nonreal, $n$ is bounded on the compact real locus instead.) The bound
$0<j/n<1/2$ makes $j/n$ regular at this pole. Galois conjugation makes it
regular at the other pole too. The five-function graph permits no poles
elsewhere, because its two possible points at infinity are already in
$I$. Thus $j/n$ is globally regular on $\mathbb P^1$, hence constant,
contradicting the preceding paragraph.

**One point in $I$.** This point is rational. Put it at infinity, so
$n=N(T)$ and $j=J(T)$ are rational polynomials. Passing to a subsequence
and changing the sign of $T$ if needed, we have $T\to+\infty$.
The physical inequalities imply $\deg J\le\deg N$, and the ratio $J/N$
has already been shown to be nonconstant.

Therefore $J/N$ has a finite pole. There can be only one such geometric
point, since infinity is already a pole of $n$. Its singleton support
is Galois invariant, so it is rational. Translate it to zero. The reduced
denominator of $J/N$ is then a power of $T$, giving

$$
N=T^rD,\qquad J=LD,\qquad r\ge1,\quad L(0)\ne0,\quad\deg L\le r.
$$

The common factor $D$ is allowed to vanish at zero. In any case
$N(0)=0$. The only possible finite pole of either $A$ or $B$ is zero,
but their displayed denominators are nonzero there. Hence $A,B$ have
no finite poles and are polynomials. The lemma in Section 2 gives the
final contradiction. This proves the theorem. $\square$

## 4. The consequence and the remaining gap

The set of bad cubic pairs has the following dichotomy:

* it is finite; or
* every infinite subset is Zariski dense in the $(n,j)$-plane.

Thus it now suffices to put all bad pairs in one proper algebraic subset
of the plane. The theorem disposes of every curve component of such a
subset, including rational curves, with no need to fix or bound $u$.

No such global nondensity theorem has been proved here. Therefore this
does not yet constrain all bad pairs to a finite exceptional set, even
though it proves finiteness on every fixed curve. Nor does it make those
curve-wise exceptional sets effective: the proof uses Siegel's theorem
and supplies no general height bound. No finite search was used.
