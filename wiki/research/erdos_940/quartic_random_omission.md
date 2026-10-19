---
name: research/erdos_940/quartic_random_omission
title: A random omission proof of the quartic complement theorem
desc: A checked alternative completion using a small infinite character bias, uniform quadratic bounds, and a growing exceptional-support cutoff.
tags: []
sources: []
created: 2026-09-22T20:53:41Z
updated: 2026-09-23T00:37:30Z
---


# A random omission proof of the quartic complement theorem

***

## Status and comparison

Sections 4–8 of the
[independent record](independent/quartic_pattern_elimination_and_random_omission.md)
give a valid alternative completion of the already established
[quartic complement theorem](quartic_complement.md). The elimination, analytic
estimates, infinite coefficient sum, and order of limits have been checked
separately. The argument below preserves the new mechanism without duplicating
the established local trace and reciprocity proofs.

The existing construction uses a finite multiquadratic character
distribution with a bounded reciprocal-prime budget, choosing its
parameters in the order $T,B,E$. This alternative instead starts with
all primes up to $Z$ and randomly omits a small proportion of those
congruent to $3\pmod4$. The omission probabilities contain a positive
coefficient for **every** nontrivial positive squareclass. A uniform
summable majorant permits dominated convergence over all canonical tuples.

Its additional analytic input is the checked
[two-sided quadratic prime-harmonic bound](quadratic_prime_harmonics.md).
No Chebotarev selection is needed in this alternative; the harmonic note
now also gives an elementary proof of nonvanishing at one. This is not a new
target case, a density-zero theorem, or a positive-density theorem for $S_4$.

The subsequently checked [universal selector](quartic_universal_selector.md)
fixes one infinite prime set and gives compatible nested moduli, rather
than choosing a finite outcome for each cutoff. It proves the same
theorem with the same baseline and quadratic-harmonic inputs.

## 1. Notation and established inputs

Let $\mathcal C$ be the canonical quartic coefficients, with prime
exponents in $\{0,5,6,7\}$. For $\mathbf d\in\mathcal C^4$, write

$$
F_{\mathbf d}=\sum_{i=1}^4d_ix_i^4,\quad
P=\prod_i d_i,\quad R=\operatorname{rad}(P),\quad
D=\operatorname{sf}(P),\quad w(\mathbf d)=P^{-1/4}.
$$

Here $D$ is the squarefree part, **not** the product denoted by $D$
in the original quartic proof.

A tuple is exceptional if $P$ is square or, for some permutation
$(i,j,k,l)$,

$$
d_i^2d_j^2d_kd_l^3\in4\mathbb Q^{\times4}.
\tag{1}
$$

Otherwise it is regular, and $D>1$. This is exactly the exceptional family in
the established proof, not Ghidelli's smaller exceptional family. The
[elimination lemma](quartic_complement.md#2-elimination-of-the-principal-character-cases)
excludes every exceptional tuple whenever

$$
v_2(F_{\mathbf d}(\mathbf x))=3,\qquad
v_p(F_{\mathbf d}(\mathbf x))=1\quad(p\mid P,\ p\text{ odd}).
\tag{2}
$$


For odd $p$, let $\rho_{\mathbf d}(p)$ be the number of solutions of
$F_{\mathbf d}\equiv p\pmod{p^2}$ divided by $p^6$.
The checked local formulas are

$$
\rho_{\mathbf d}(p)=1+A_{\mathbf d}(p)(p^{-1}-p^{-2})-p^{-3},
\quad |A_{\mathbf d}(p)|\le21\quad(p\nmid P),             \tag{3}
$$


$$
A_{\mathbf d}(p)=\chi_D(p)\quad(p\equiv3\pmod4, p\nmid P),
\qquad 0\le\rho_{\mathbf d}(p)\le4\quad(p\mid P).        \tag{4}
$$

The modulus-$16$ factor for target $8$ is at most $16$. For regular tuples, the
sharpened
[Euler majorant](quartic_euler_majorant.md#a-conductor-bound-in-terms-of-the-coefficient-radical)
gives, uniformly in $Z$,

$$
\sum_{\substack{p\le Z\\p\nmid2P}}\frac{A_{\mathbf d}(p)}p
\le11\log\log(3R)+O(1).                                \tag{5}
$$

This uses the full-prime quadratic term and ten nonprincipal Gaussian
characters, all with positive multiplicities. It introduces no inverse
$L$-function into the baseline.

For every fixed $B_0>0$ and $0\le\eta<1/4$,

$$
\sum_{\mathbf d\in\mathcal C^4}
w(\mathbf d)B_0^{\omega(R)}R^\eta<\infty.               \tag{6}
$$

Indeed its local Euler factor is
$1+B_0p^\eta[(1+p^{-5/4}+p^{-6/4}+p^{-7/4})^4-1]
=1+O_{B_0}(p^{-5/4+\eta})$.
In particular, since a prime divisor greater than $Y$ implies $R>Y$,

$$
\sum_{\substack{\mathbf d\\\exists p>Y:\ p\mid P}}
w(\mathbf d)B_0^{\omega(R)}\ll_{B_0}Y^{-1/8}.             \tag{7}
$$

The original proof has the stronger $Y^{-1/4}$ support tail; this
weaker estimate suffices here.

## 2. A single bias for all squareclasses

For every positive squarefree $E>1$, let $\chi_E$ be the primitive
quadratic character of $\mathbb Q(\sqrt E)$. Fix $0<\delta<1$,
to be made smaller below, and set

$$
\epsilon_E=\frac{\delta}{16E^2},\qquad
h(p)=\frac\delta2+\sum_{\substack{E>1\\E\text{ squarefree}}}
\epsilon_E\chi_E(p).
\tag{8}
$$

The series converges uniformly and absolutely, with
$\sum_E\epsilon_E<\delta/4$ and
$\sum_E\epsilon_E\log(2E)\ll\delta$. Thus
$\delta/4<h(p)<3\delta/4<1$.

For each fixed positive squarefree $D>1$, and uniformly in $3\le Y<Z$,

$$
-\sum_{\substack{Y<p\le Z\\p\equiv3\ (4)}}
\frac{h(p)\chi_D(p)}p
\le-\frac{\epsilon_D}{2}\log\frac{\log Z}{\log Y}
+C\delta\log(2D).                                     \tag{9}
$$

To prove this, expand (8). The $E=D$ term has
$\chi_D(p)^2=1$ off primes dividing $2D$, and hence contributes
the displayed main term by (7) of the
[quadratic harmonic note](quadratic_prime_harmonics.md), with error
$O(\epsilon_D\log(2D))$.

For $E\ne D$, both $\chi_E\chi_D$ and
$\chi_{-4}\chi_E\chi_D$ are nonprincipal real characters, presented
modulo $O(ED)$. The first has a nontrivial positive squareclass; its
twist has a negative squareclass, so neither can be trivial.
Writing the indicator of $p\equiv3\pmod4$ as
$(1-\chi_{-4}(p))/2$, the two-sided bound gives window sums
$O(\log(2DE))$. The same argument applies to the baseline
$\delta\chi_D/2$. Summing these errors with the absolutely convergent
weights proves (9). Primes where a character vanishes are included
through its presented modulus; no orthogonality assumption at those
primes is made.

If the sum in (9) omits primes dividing $P$, the extra error is at most
$C\delta\sum_{p\mid R}1/p\ll\delta\log(2R)$.
This includes coefficient primes that do not divide the squarefree part $D$.

## 3. Finite random moduli

Let $Z\to\infty$ and put $Y=(\log Z)^{200}$, so eventually
$3<Y<Z$. Include every odd prime $p\le Y$ and every prime
$p\le Z$ with $p\equiv1\pmod4$. Independently omit each prime
$Y<p\le Z$, $p\equiv3\pmod4$, with probability $h(p)$.
For the resulting finite set $\mathcal Q$, prescribe

$$
M=16\prod_{p\in\mathcal Q}p^2,\qquad
a\equiv8\pmod{16},\qquad a\equiv p\pmod{p^2} (p\in\mathcal Q).
\tag{10}
$$

CRT determines $a\pmod M$. Let
$\rho_{\mathbf d}(a,M)=M^{-3}\#\{\mathbf x\bmod M:
F_{\mathbf d}(\mathbf x)\equiv a\pmod M\}$.

At an eligible good prime, independence replaces its local factor by

$$
h(p)+(1-h(p))\rho_{\mathbf d}(p)
=1+\frac{(1-h(p))\chi_D(p)}p+O(p^{-2}).                  \tag{11}
$$

At other good primes use (3), at bad primes use $4$, and at $2$ use
$16$. Apply $1+u\le e^u$ to these nonnegative factors. Equations
(5) and (9), including the coefficient-prime error, give for every
regular tuple

$$
\mathbb E\rho_{\mathbf d}(a,M)
\le C\,4^{\omega(R)}(\log(3R))^{11}R^{C_1\delta}
\left(\frac{\log Z}{\log Y}\right)^{-\epsilon_D/2}.
\tag{12}
$$

All constants are absolute and fixed before $\delta$ is chosen.
There is no division by a local factor, so vanishing factors present
no difficulty. Although $M,a$ are random, CRT expresses their normalized
count as exactly the product of the independently selected local factors.

Choose $\delta$ with $C_1\delta<1/16$. Bounding the logarithmic power
by $C R^{1/16}$, (6) supplies a summable majorant
$Cw(\mathbf d)4^{\omega(R)}R^{1/8}$ for the weighted expectation.
For each regular tuple, $\epsilon_D>0$ and
$\log Z/\log Y\to\infty$. Dominated convergence yields

$$
\sum_{\mathbf d\text{ regular}}
w(\mathbf d)\mathbb E\rho_{\mathbf d}(a,M)\longrightarrow0.
\tag{13}
$$

The rates may be arbitrarily small; no lower bound uniform in $D$ is
needed.

## 4. The exceptional infinite tail

Every exceptional tuple whose coefficient primes are all at most $Y$
has zero local factor for **every** random outcome, by (2).
For any tuple, the crude bounds (3)–(4) and the prime harmonic estimate
give, uniformly in the outcome,

$$
\rho_{\mathbf d}(a,M)\ll4^{\omega(R)}(\log Z)^{21}.
$$

All remaining exceptional tuples have a coefficient prime greater than
$Y$. By (7), their total weighted expectation is

$$
\ll(\log Z)^{21}Y^{-1/8}=(\log Z)^{-4}\longrightarrow0.
\tag{14}
$$

The growing deterministic cutoff is essential: eliminating each fixed
exceptional tuple eventually would not by itself justify summing them.

Tonelli and (13)–(14) now give

$$
\mathbb E\left[\sum_{\mathbf d\in\mathcal C^4}
w(\mathbf d)\rho_{\mathbf d}(a,M)\right]\longrightarrow0.
\tag{15}
$$

For each $Z$ there are only finitely many outcomes. At least one has its
entire weighted local sum no larger than the expectation. Randomization
therefore proves the existence of an ordinary finite modulus and residue.

## 5. Fixing the modulus before counting

Choose an outcome for which the sum in (15), multiplied by
$V=\Gamma(5/4)^4$, is less than a given $\varepsilon>0$.
Now fix $M,a$. The established lattice limit gives for each tuple

$$
\#\{\mathbf x\in\mathbb N^4:F_{\mathbf d}(\mathbf x)\le X,
F_{\mathbf d}(\mathbf x)\equiv a\pmod M\}
=\frac{VX}{M}w(\mathbf d)\rho_{\mathbf d}(a,M)+o_{M,\mathbf d}(X).
$$

The count divided by $X$ is at most $w(\mathbf d)$ by the coordinate
box bound, and these weights are summable. Thus dominated convergence
sums this limit over every canonical tuple; after normalization by
$X/M$ the majorant is $Mw(\mathbf d)$, with $M$ already fixed.
The full ordered four-term representation mean is less than
$\varepsilon$. Distinct values are no more numerous than
representations, and at most three summands give $O(X^{3/4})$ values.
Consequently

$$
\limsup_{X\to\infty}\frac M X
\#\{n\le X:n\in S_4,\ n\equiv a\pmod M\}<\varepsilon.
$$

Taking $\varepsilon=1/2$ yields positive lower density of the complement,
exactly as in the original theorem. The changing moduli do not yield
global density zero, and no step extends the conclusion to $r\ge5$.
