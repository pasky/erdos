---
name: research/erdos_25/bohr_protected_preparations
desc: A uniform finite-sieve bound rules out positive-density single-Bohr-set protection as a near-cover preparation.
tags: [finite-sieves, diophantine-approximation, obstructions]
sources: []
created: 2026-09-22T09:01:09Z
updated: 2026-09-24T22:13:01Z
---


# research/erdos_25/bohr_protected_preparations

***

One counterexample attempt sought finite sieves with all moduli at most
$N$, very small full survivor measure, but a positive proportion of
survivors across $[N,N^K]$, for fixed $K>1$. Such a preparation alone
would not yet be a counterexample: it would still need to be incorporated
into compatible infinite singleton blocks producing fixed logarithmic
overdeletion. No such preparation or infinite construction was obtained.

The following theorem rules out protecting a single interval under a
rotation as the proposed preparation, even when the slope changes
arbitrarily with $N$. It is a finite **counting** estimate, not a
general density theorem.

## Theorem

Fix an interval $I\subset\mathbb R/\mathbb Z$ of length $\ell>0$.
Let
$$
 S=\{1\le n\le H:\{n\theta\}\in I\}.
$$
Suppose a finite family has distinct moduli $q\le N$, one residue
class per modulus, and every full class avoids $S$. Let $\delta$
be the full periodic survivor density. Then
$$
 \delta\ge\frac{|S|}{H}
       -C_\ell\sqrt{\frac{N\log(2N)}H}
 \qquad(H\ge C_\ell N\log(2N)).
 \tag{1}
$$
The constant is independent of $\theta$, the residues, and the family.

The same assertion holds after translating the interval of integers
and the Bohr interval. Thus on $[N,N^K]$, $K>1$ fixed, a protected
Bohr set of positive counting proportion forces a positive full
survivor measure. This includes rational, Liouville, and
$N$-dependent slopes. It does not treat arbitrary protected sets.

## An avoided progression yields a rational approximation

Put $J=\lceil8/\ell\rceil$. If a progression modulo $q\le N$
avoids $S$, its rotation phases form at least $H/q-1$ consecutive
terms with step $q\theta$, all avoiding $I$.
The elementary pigeonhole approximation lemma gives a $1\le j\le J$
with
$$
 \|jq\theta\|\le1/(J+1)<\ell/4.
$$
For clarity, the lemma follows by putting $0,q\theta,\ldots,Jq\theta$
on the circle and choosing two of the $J+1$ points at circular
distance at most $1/(J+1)$.

The corresponding $j$-spaced subsequence has length at least
$H/(jq)-2$. If its signed step $\xi$, with
$|\xi|=\|jq\theta\|<\ell/4$, travels a full circle, consecutive
points leave gaps smaller than $\ell$, contradicting avoidance.
For $H\ge8JN$, this gives
$$
 \|jq\theta\|\le A jq/H
$$
with an absolute constant $A$, for example $A=8$.
The assertion also holds if the step is zero.
After reduction, there is consequently a rational $a/b$ satisfying
$$
 b\mid jq,\qquad b\le JN,\qquad
 |\theta-a/b|\le A/H.
 \tag{2}
$$
We may replace $\theta$ by its fractional part throughout.

Let $\mathcal A$ be all reduced fractions satisfying the last two
conditions in (2). If no forbidden class is present, (1) is immediate.
Otherwise $\mathcal A$ is nonempty. Define
$$
 \eta=\sqrt{\frac{N\log(2N)}H},
 \qquad B=\frac{\log(2N)}\eta
          =\sqrt{\frac{H\log(2N)}N},
$$
and let $b_0$ be the least denominator in $\mathcal A$.
It suffices to work when $\eta$ is smaller than a sufficiently
small constant depending on $\ell$: the other range follows from
the trivial bounds $\delta\ge0$ and $|S|/H\le1$ after increasing
$C_\ell$.

## No small denominator: the whole sieve has small cost

Suppose $b_0>B$. Fractions with denominators in $[Q,2Q)$ are
separated by at least $1/(4Q^2)$. Since the approximation interval
has length $2A/H$, their number in $\mathcal A$ is
$O(1+Q^2/H)$.

For a fixed reduced denominator $b$, condition $b\mid jq$ for
some $j\le J$ implies
$$
 \sum_{\substack{q\le N\\b\mid jq\text{ for some }j\le J}}\frac1q
 \le\sum_{j\le J}\frac{(b,j)}b
              H_{\lfloor N(b,j)/b\rfloor}
 \ll_\ell\frac{\log(2N)}b.
$$
Summing this bound over the approximants, in dyadic denominator
blocks from $b_0$ to $JN$, gives
$$
 \sum_{q\text{ selected}}\frac1q
 \ll_\ell\log(2N)\left(\frac1{b_0}+\frac NH\right)
 \ll_\ell\eta+\eta^2\ll_\ell\eta.
 \tag{3}
$$
Distinctness and one class per modulus now matter: the full Haar
union bound gives $\delta\ge1-O_\ell(\eta)$, which implies (1).

## A small denominator: a common periodic region survives

Suppose $b_0\le B$, and choose its reduced approximant $a/b$.
It is the only fraction in $\mathcal A$ when $\eta$ is sufficiently
small. Indeed any distinct one with denominator $b'\le JN$
has distance at least $1/(bJN)$ from it, whereas two approximants
are at distance at most $2A/H$. The inequality
$2ABJN/H=2AJ\eta<1$ rules this out.

Write
$$
 \theta=a/b+\varepsilon,\qquad |\varepsilon|H\le A,
 \qquad L=bN.
$$
We have $L/H\le BN/H=\eta$, so $L<H/4$ in the relevant range.

If $\varepsilon=0$, the set
$\{n:\{an/b\}\in I\}$ is $b$-periodic. Any forbidden class
intersecting it would have a common point with it in $[1,H]$,
because the combined period is at most $bN=L<H$.
Thus the whole periodic set survives. Its density differs from
$|S|/H$ by at most $b/H$, giving (1).

Assume now $\varepsilon\ne0$, and let $w=|\varepsilon|L$.
For $L\le t\le H-L$, define
$$
 R_t=\left\{r\bmod b:
 \{ar/b+\varepsilon t\}\text{ lies in }I
 \text{ at distance greater than }w\text{ from its boundary}\right\}.
$$
Every forbidden full class avoids this entire $b$-periodic region.
Otherwise CRT supplies a common integer $n$ within distance $L$
of $t$, and inside $[1,H]$, since the combined period is at most
$bq\le L$. Its actual phase differs from
$ar/b+\varepsilon t$ by at most $|\varepsilon|L=w$, so $n\in S$,
a contradiction. Consequently
$$
 \delta\ge\max_{L\le t\le H-L}|R_t|/b.
 \tag{4}
$$

Here is the averaging estimate required for (4). For each residue
$r\bmod b$, the function
$$
 f_r(t)=\mathbf1_I(\{ar/b+\varepsilon t\})
$$
is constant on at most $O_A(1)$ intervals in $[0,H]$, since the
total phase travel is at most $A$. Counting on the progression
$n\equiv r\pmod b$ therefore differs from
$b^{-1}\int_0^H f_r(t)\,dt$ by $O_A(1)$. Summing over $r$ gives
$$
 |S|=\int_0^H\frac1b\sum_r f_r(t)\,dt+O_A(b).
$$
Eroding $I$ by the margin $w$ removes, for each $r$, at most
$O_A(w/|\varepsilon|)=O_A(L)$ units of time: the phase passes
each endpoint only $O_A(1)$ times. Deleting the two boundary
time intervals also costs at most $2L$. Hence
$$
 \int_L^{H-L}\frac{|R_t|}{b}\,dt\ge |S|-O_A(L).
$$
This reasoning permits either choice of endpoint inclusion in $I$;
for nonzero $\varepsilon$, possible endpoint visits add only
$O_A(1)$ counting errors per residue. Combining the last display
with (4) yields
$$
 \delta\ge |S|/H-O_A(L/H)
          \ge |S|/H-O_\ell(\eta),
$$
which proves (1).

## Interpretation for the attempted construction

On a window entirely above all preparatory moduli, delayed avoidance
is full congruence avoidance. Translating $[N,N^K]$ to an initial
interval changes neither moduli nor full periodic density; it only
translates the Bohr interval. Applying (1) with
$H=\lfloor N^K\rfloor-N$ makes its error tend to zero.
Thus a positive-density protected single Bohr interval cannot coexist
with a preparatory survivor measure tending to zero.

The theorem neither controls high-complexity protected sets nor proves
that every finite sieve with small Haar survivor measure has few
survivors on such a window. The general preparation and the infinite
counterexample remain unconstructed.
