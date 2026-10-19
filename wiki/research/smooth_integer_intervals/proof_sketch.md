---
name: research/smooth_integer_intervals/proof_sketch
title: Smooth integers in every short block, exponent by exponent
desc: |
  Proof sketch for upper bounds on k(n) in Problem 962: the near-square
  construction gives 2/5 with one multiplier, 11/28 explicitly and
  38/97+epsilon with Bourgain's exponent pair (L250, L251, L253); exact
  limits of these estimates and the nonresidue reduction locate the gaps.
tags: [E0962, proof, incomplete]
sources:
- problems/integer_sequences/E0962
created: 2026-10-15T22:27:51Z
updated: 2026-10-15T22:27:51Z
---

# Smooth integers in every short block, exponent by exponent

***

## Target and conventions

The target is
[[problems/integer_sequences/E0962/_index|Problem 962, whose assessment records both of its questions as open; this research does not change that status]].
Let $k(n)$ be the largest $k$ for which some integer $m$ with $0\le m\le n$
has each of $m+1,\ldots,m+k$ divisible by a prime greater than $k$. In
Erdős's 1976 notation, $n_k$ is the least $n\ge0$ such that each of
$n+1,\ldots,n+k$ has a prime factor greater than $k$, and
$k(n)=\max\{k:n_k\le n\}$. Allowing $m=0$ or requiring $m\ge1$ changes no
bound below: every upper bound here is proved for all $m\ge0$, and the lower
bound of L252 uses a positive $m$.

A block $m+1,\ldots,m+K$ whose terms all have a prime factor greater than $K$
is a block with no $K$-smooth member, and its first $K'$ terms form such a
block for every $K'\le K$. Hence, for every integer $K\ge1$,

$$
k(n)<K\iff\text{every block }(m,m+K]\text{ with }0\le m\le n
\text{ contains a }K\text{-smooth integer.}
$$

This is an assertion about every block, not almost every block: a theorem
that holds outside an exceptional set of $m$ says nothing about $k(n)$,
because the one bad block may be exceptional.

Two targets are kept apart.

- **Waypoints:** $k(n)\ll n^\theta$ with $\theta<1/2$, that is,
  $n_k\gg k^{1/\theta}$.
- **The displayed question:** $\log k(n)\le(\log n)^{1/2+o(1)}$, Erdős's
  conjecture (7) in inverse form. No power waypoint proves it; it needs
  $K=n^{o(1)}$.

## Standing

| Bound | Exponent | Source | Standing |
| --- | --- | --- | --- |
| $k(n)\le(1+o(1))n^{1/2}$ | $1/2$ | forum argument on the problem page | checked there |
| $n_k>k^{5/2}/16$, $k>k_0$ | $2/5$ | Erdős and Sárközy (1979), Theorem 2 | published |
| $k(n)<\max(64,(128n)^{2/5})$ | $2/5$ | L250, explicit form of the above | tier 0 |
| $k(n)<\max(64,(2^{15}n)^{11/28})$ | $11/28$ | L251, averaged multiplier | tier 0 |
| $k(n)\ll_\varepsilon n^{38/97+\varepsilon}$ | every exponent above $38/97$ | L253, Bourgain's exponent pair | tier 0 |
| $k(p)\ge n_2(p)-1$, $p\equiv3\pmod4$ | barrier | L252, after Granville (2008) | tier 0 |

Here $n_2(p)$ is the least quadratic nonresidue modulo $p$. The lower bound
$\log k(n)\ge(1/\sqrt2-o(1))\sqrt{\log n\log\log n}$ and its sources are on
the problem page. Erdős and Sárközy's theorem is P. Erdős and A. Sárközy, On
the prime factors of $\binom nk$ and of consecutive integers, Utilitas Math.
16 (1979), 197--215 (public scan in
[the Rényi Institute's Erdős archive](https://static.renyi.hu/~p_erdos/1979-15.pdf));
it proves the bound $n_k>k^{2+\varepsilon}$ that Erdős wrote in 1976 he could
not show, in the strong form $n_k>k^{5/2}/16$.
The
[[research/smooth_integer_intervals/literature|literature comparison]]
matches it and the other every-interval theorems at their exact
parameters.

## The argument

**Held link 1: the near-square adjustment.** If $c,q\ge1$ and $m\ge0$ are
integers with $0<cq^2-m\le E$, then subtracting the largest $ct^2$ below
$cq^2-m$ gives $N=c(q-t)(q+t)$ with $0<N-m\le2\sqrt{cE}+c$ and $t<q$
(Lemma 1 in the proofs of
[[theory/integer_sequences/L250_explicit_near_square_smooth_blocks/_index|L250]]
and
[[theory/integer_sequences/L251_averaged_near_square_smooth_blocks/_index|L251]]).
So a $K$-smooth member of $(m,m+K]$ exists as soon as some pair $(c,q)$ with
$c\le K$ and $q\lesssim K$ has $cq^2$ in a window $(m,m+E]$ with
$E\asymp K^2/c$. The rest of the argument finds such a pair.

**Held link 2: one multiplier (exponent $2/5$).** With $c\asymp m/K^2$
chosen from $m$, the next square $q^2$ above $m/c\le K^2/16$ lies within
$2q-1\le K/2+1$ of $m/c$, so $E\approx cK/2$ and the adjustment lands within
about $c\sqrt{2K}$ of $m$. That is at most $K$ when $c\lesssim\sqrt K$, that
is, $m\lesssim K^{5/2}$.
[[theory/integer_sequences/L250_explicit_near_square_smooth_blocks/_index|L250 proves this with explicit constants for every K >= 64]];
it is Erdős and Sárközy's construction.

**Held link 3: an averaged multiplier (exponent $11/28$).** Let $c$ range
over $(C,2C]$ with $C=\lceil16m/K^2\rceil$ and put $Y=\sqrt{m/C}\asymp K$.
The pairs $(c,q)$ with $m<cq^2\le m+E$ number
$\sum_c(\sqrt{(m+E)/c}-\sqrt{m/c})-S_C(m+E)+S_C(m)$, where

$$
S_C(X)=\sum_{C<c\le2C}\psi\Bigl(\sqrt{X/c}\Bigr),\qquad
\psi(u)=u-\lfloor u\rfloor-\tfrac12 .
$$

The main term is at least $E/((2+\sqrt2)Y)\asymp K/C$. Vaaler's inequality
turns $S_C$ into exponential sums $\sum_ce(r\sqrt{X/c})$, whose phase has
third derivative of size $rY/C^3$, and the explicit third-derivative test
of Granville and Ramaré gives

$$
|S_C(X)|\le60\,C^{4/7}Y_X^{1/7}+40\,C^{3/4}(\log C)^{3/2}
\qquad(C^{3/2}\le Y_X\le C^3/120),
$$

with $Y_X=\sqrt{X/C}$ (Lemma 3 of the L251 proof). This is below the main
term while $C\le K^{6/11}/1024$, so pairs exist for all $m$ up to
$2^{-15}K^{28/11}$.
[[theory/integer_sequences/L251_averaged_near_square_smooth_blocks/_index|L251]]
proves the resulting bound $k(n)<\max(64,(2^{15}n)^{11/28})$ completely; its
analytic inputs are the held statements of Lemmas 7.1 and 8.6 of
[[../library/factorials_binomials/granville_1996_explicit_bounds_exponential_sums_scarcity_squarefree/_index|Granville and Ramaré (1996)]],
consumed as stated, except that the proof corrects the placement of one
misprinted sign in Lemma 7.1 and derives the corrected inequality.

**Held link 4: Bourgain's exponent pair.** Theorem 6 of Bourgain's
*Decoupling, exponential sums and the Riemann zeta function*, in
[arXiv:1408.5794v2](https://arxiv.org/abs/1408.5794v2), gives
$(\kappa,\lambda)=(13/84+\eta,55/84+\eta)$ for every $\eta>0$.
The phase $-r\sqrt X\,c^{-1/2}$ has first derivative exactly
$(r\sqrt X/2)c^{-3/2}$, so it lies in the monomial class specified in
Section 5, including the range $C>\sqrt{rY_X}$. Its sum is bounded by
$\ll_\eta C^{1/2}(rY_X)^{13/84+\eta}$. Vaaler then gives
$|S_C(X)|\ll_\eta C^{\lambda/(1+\kappa)}Y_X^{\kappa/(1+\kappa)}$.
For every fixed $\delta>0$ sufficiently small this is $o(K/C)$ uniformly
when $\sqrt K/8<C\le32K^{21/38-\delta}$ and $Y_X\asymp K$.
[[theory/integer_sequences/L253_exponent_pair_smooth_blocks/_proof|L253 writes out the source interface, frequency truncation and uniform endpoint construction]],
giving $k(n)\ll_\varepsilon n^{38/97+\varepsilon}$.

The composition is complete at tier 0. L250 covers the small endpoints;
L251 proves an explicit bound for every $K\ge64$; L253 proves its stronger
asymptotic bound for every sufficiently large $K$, with the threshold
depending only on $\delta$. The claimed bounds use no unproved
mathematical premise. The cited analytic theorems are external source
inputs, and none of the project deductions has independent acceptance.

## The exponent as a function of the multiplier-sum bound

The proof of L251 uses the third-derivative test only through the bound on
$S_C$. Suppose instead that $|S_C(X)|\ll C^aY_X^b$ with $a\ge0$ and
$0\le b<1$, uniformly for
$C\le K$ and $Y_X\asymp K$. Then the same parameter choice works while
$K/C\gg C^aK^b$, that is, for $C\ll K^{(1-b)/(1+a)}$, and gives

$$
\theta=\frac{1+a}{3+2a-b},\qquad
n_k\gg k^{2+(1-b)/(1+a)} .
$$

This formula is an author derivation, not written out with constants; each
use must recheck the side conditions (the ranges of $C$ and $Y_X$ and the
secondary terms). An exponent pair $(\kappa,\lambda)$ used with Vaaler's
inequality, in the regime $rY_X/C\ge1$ that holds here, gives
$(a,b)=(\lambda/(1+\kappa),\kappa/(1+\kappa))$ and hence

$$
\theta=\frac{1+\kappa+\lambda}{3+2\kappa+2\lambda}
=\frac12-\frac{1}{2(3+2\kappa+2\lambda)} ,
$$

so only $\kappa+\lambda$ matters, and smaller is better.

| Input for $S_C$ | $(\kappa,\lambda)$ | $\theta$ |
| --- | --- | --- |
| trivial bound $C$ | $(0,1)$ | $2/5$ |
| second-derivative test | $(1/2,1/2)$ | $2/5$ |
| third-derivative test (L251) | $(1/6,2/3)$ | $11/28\approx0.3929$ |
| Bourgain's pair (2017), L253 | $(13/84+\varepsilon,55/84+\varepsilon)$ | any exponent above $38/97\approx0.3918$ |
| exponent pair conjecture | $(\varepsilon,1/2+\varepsilon)$ | any exponent above $3/8$ |

The second row explains why one-variable second-derivative attempts stall:
at the critical size the second-derivative test is no better than the
trivial bound. The fourth row is proved with its $\varepsilon$ slack in
L253; taking the infimum does not remove that slack from its conclusion.
Bounds for sawtooth sums that use the average over the frequency $r$ as
well may do better than a separate bound at each frequency. A theorem of
that kind still needs its exact hypotheses matched to this range.

## Ceilings and obstructions

**Scaling a fixed input (proved, elementary).** Suppose every interval
$(X,X+AX^\beta]$ contains an $AX^\alpha$-smooth integer, and one scales by a
$K$-smooth multiplier $c$, using the input at $X=m/c$. Containing the
whole supplied interval $c\cdot(X,X+AX^\beta]$ in the block requires
$AcX^\beta\le K$, and $cX^\beta=c^{1-\beta}m^\beta\ge m^\beta$ for $c\ge1$
and $\beta\le1$. So the diagonal exponent obtained is at least $\beta$
whatever $\alpha$ is. More precisely, take $c\asymp m^{1-s}$,
$0<s\le1$, using a power of $2$ so that $c$ is $K$-smooth for $K\ge2$.
The two exponent requirements are
$\theta\ge s\alpha$ and $\theta\ge1-s+s\beta$.
Their maximum is minimized at $s=1/(1+\alpha-\beta)$ when
$\beta\le\alpha$, giving $\alpha/(1+\alpha-\beta)$; when
$\beta>\alpha$, its minimum is $\beta$ at $s=1$.
All constant-factor changes are absorbed in the interval and smoothness
constants. No input with interval length
$x^{1/2}$ or longer can give $\theta<1/2$ this way. This covers the
square-root results matched on the literature page; Harman's 1999
Theorem 2 requires interval exponent above $3/7$ even under the
exponent-pair conjecture (its original known-pair discussion reaches
between $0.45$ and $0.46$);
Friedlander and Lagarias's $f(1/2)\le1/4$ gives
$\frac{1/2}{1+1/2-1/4}=2/5$, the Erdős--Sárközy exponent again, and their
$f(1/3)\le5/12$ gives $5/12$.

**A window of products with one multiplier (author derivation; exponent
pair conjecture still gives only $2/5$).** A different count fixes
$c\asymp m/K^2$ and looks for $ab$ with $a,b\le K$ in the window
$(m/c,(m+K)/c]$ of length $K/c\asymp K^3/m$ near $T=m/c\asymp K^2$. The
error term is a sawtooth sum $\sum_{a\asymp K}\psi(T/a)$ of divisor-problem
type. A pointwise bound $T^\delta$ for it gives
$\theta=1/(3-2\delta)$: the second-derivative test ($\delta=1/3$) gives
$3/7$, and even square-root cancellation over the $K\asymp T^{1/2}$ terms
($\delta=1/4$) gives only $2/5$. This route therefore stays at or above the
fixed-multiplier exponent. A related one-variable count with the reciprocal
phase $m/a$ and the second-derivative test is retired at its stated scope:
its requirements, as stated for that route (their derivation is not
reproduced here), are $H>U^2/K$, $\sqrt{Hm}<K$ and $U^2\ge m/K$, for window
length $H$ and factor size $U$. The first and third give $H>m/K^2$, so
$\sqrt{Hm}>m/K$, and the second then forces $m<K^2$: no gain over the
square-root bound. Its sum is a different one from the multiplier sum $S_C$.

**Limits of this construction and estimate (exact scope).** A product of
three positive integers at most $K$ is at most $K^3$. For $m\ge K^3$ it
therefore cannot lie in $(m,m+K]$, whatever method selects its factors.
Thus the three-factor conclusion of L250, L251 and L253 cannot provide a
diagonal power exponent below $1/3$. This is an exact obstruction for that
output specification; a $K$-smooth integer can have more than three such
factors.

There is a separate obstruction to improving the displayed exponent-pair
calculation. Every exponent pair in its usual range has $\kappa\ge0$ and
$\lambda\ge1/2$, so $s=\kappa+\lambda\ge1/2$. The formula
$\theta=(1+s)/(3+2s)$ is increasing in $s$, and hence gives
$\theta\ge3/8$. Even the exponent-pair conjecture reaches only the
infimum $3/8$ through this calculation. Likewise, simply inserting a
discrepancy estimate of size $C^{1/2}$ gives the sufficient condition
$K/C\gg C^{1/2}$, or $C\ll K^{2/3}$. Neither observation rules out a
smaller discrepancy, direct control of $S_C(m+E)-S_C(m)$, or a different
counting method. They are limits of these estimates, not lower bounds on
the true discrepancy.

More generally, a witness formed from $r$ positive factors at most $K$
cannot exceed $K^r$. A witness above $m$ requires
$r>\log m/\log K$ when $K>1$. At the conjectured scale
$\log K=(\log m)^{1/2+o(1)}$, the number of factors must therefore grow
at least as $(\log m)^{1/2-o(1)}$. No fixed-factor construction can
establish the displayed question.

**The nonresidue barrier (proved).**
[[theory/integer_sequences/L252_nonresidue_blocks_without_smooth_members/_index|L252 shows k(p) >= n_2(p) - 1 for primes p = 3 (mod 4)]],
by the argument Granville gives after his Conjecture 4.4.2. So a proof of
$k(n)\ll n^\theta$ with $\theta<1/(4\sqrt e)=0.1516\ldots$ would improve the
Burgess--Vinogradov exponent for the least quadratic nonresidue of these
primes, and the displayed question would give
$\log n_2(p)\le(\log p)^{1/2+o(1)}$ for them. This measures difficulty and
refutes nothing; the generalized Riemann hypothesis gives
$n_2(p)=O((\log p)^2)$.

## Gaps and next tests

1. **A stronger uniform pair count.** The next discriminating test is a
   bound for the one-sided count of pairs $(c,q)$ with $C<c\le2C$ and
   $m<cq^2\le m+E$, where $Y=\sqrt{m/C}\asymp K$,
   $E\asymp K^2/C$ and $C=K^\nu$ for some $\nu>21/38$.
   The main term is $\asymp K/C$; an error $o(K/C)$ would improve L253.
   A bound for the difference $S_C(m+E)-S_C(m)$ may exploit the short
   window more efficiently than bounding the two sums separately.
   At $C\asymp K^{2/3}$, an adequate estimate would reach the infimum
   $3/8$. Ordinary exponent-pair substitution cannot pass that infimum.
2. **Growing factor count.** Passing below $1/3$ requires changing the
   three-factor output. The Friedlander--Lagarias construction for a fixed
   $r$ has interval exponent $1-2/r+1/(r2^{r-1})$; it is already above
   $1/2$ for $r\ge4$, so merely increasing $r$ in that construction
   does not supply the needed short intervals. Moreover its fixed-$r$
   theorem gives no uniform control when $r$ grows. A useful new input
   must produce many bounded factors while retaining a gap at most $K$;
   no such unbounded-factor construction is supplied here.
3. **The displayed question.** It requires $K=n^{o(1)}$, hence smooth
   members with unboundedly many factors, in every block. By L252 any
   unconditional exponent below $1/(4\sqrt e)$ already passes through a new
   bound for quadratic nonresidues; the displayed question is far beyond
   that. No route toward it is proposed here.

The conclusions currently supported are the explicit bound
$k(n)<\max(64,(2^{15}n)^{11/28})$ and the stronger asymptotic bound
$k(n)\ll_\varepsilon n^{38/97+\varepsilon}$ for every $\varepsilon>0$,
both author-recorded at tier 0. The displayed question remains open; no
bound with a fixed exponent at most $38/97$ is proved here.
