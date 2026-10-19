---
name: research/leads/totient_binary_series/window_cost
title: Residue-Class Bounds for Binary Totient Windows
desc: |
  Modulus bounds for termwise divisibility on whole progressions, with
  explicit limits on their implications for selected representatives.
tags: []
sources: []
problems:
- 249
review_status: unreviewed
created: 2026-09-17T04:06:54Z
updated: 2026-09-17T04:07:32Z
---

# Residue-Class Bounds for Binary Totient Windows

[[research/leads/totient_binary_series/_index|..]]

***

This page uses the notation of
[[research/leads/totient_binary_series/_index|the binary totient sketch]]. Its
proofs are author-recorded and have not received independent review.
Dirichlet's theorem on primes in a reduced arithmetic progression is an
external input to Lemma A. The asymptotic simplification in Lemma B also
uses the standard elementary bound $\theta(x)=O(x)$.

## The distinction between a modulus and its representative

A lower bound for a modulus $M$ does not give a lower bound for the least
positive representative $N$ of a residue class modulo $M$. For example,
$N=1$ belongs to $1\pmod{10^6}$. For any fixed integer $N$, one can also
choose arbitrarily large moduli and their representative $r=N$.
Only with the additional hypothesis $N\ge M$ does
$\log_2N\ge\log_2M$ follow. A class has at most one positive member below
$M$, but a construction can select that member for each new modulus.

The earlier inference that the modulus bound below closes single-index
CRT methods was therefore invalid. It is withdrawn. These lemmas concern
properties holding at every sufficiently large member of a full class;
they do not bound exceptional representatives, carry coincidences, or
methods using arithmetic information beyond one fixed class.

## Forcing two-adic valuations on a full class

**Lemma A.** Let $M\ge1$, $r\in\mathbb Z$, and $g=\gcd(r,M)>0$.
Every positive $n\equiv r\pmod M$ satisfies
$v_2(\varphi(n))\ge v_2(\varphi(g))$. Infinitely many such positive $n$
satisfy $v_2(\varphi(n))\le v_2(\varphi(g))+2$.

*Proof.* The first claim follows prime by prime from $g\mid n$ and
$\varphi(g)\mid\varphi(n)$. Write $r=gr'$, $M=gM'$, so
$\gcd(r',M')=1$. For each prime $p\mid g$ not dividing $M'$, impose
$u\equiv1\pmod p$ as well as $u\equiv r'\pmod{M'}$. These compatible
conditions give a reduced class $u\equiv r''\pmod{M''}$ with
$M''=M'\prod_{p\mid g,\ p\nmid M'}p$. Every integer in it is coprime to
$g$, and $n=gu$ belongs to the original class.

If $4\nmid M''$, or if $4\mid M''$ and $r''\equiv3\pmod4$, the class
can be combined with $u\equiv3\pmod4$. Dirichlet gives infinitely many
primes in this combined reduced class. They have $v_2(\varphi(u))=1$.
In the remaining case $4\mid M''$ and $r''\equiv1\pmod4$, choose a prime
$q_1\equiv3\pmod4$ not dividing $M''$. There are infinitely many primes
$q_2\ne q_1$ in the reduced class
$q_2\equiv r''q_1^{-1}\pmod{M''}$; each is $3\pmod4$. Set $u=q_1q_2$.
Then $v_2(\varphi(u))=2$. In both cases
$\varphi(gu)=\varphi(g)\varphi(u)$ proves the upper bound. $\square$

**Lemma B (a modulus lower bound).** Let $m\ge4$. Suppose every
sufficiently large $N\equiv r\pmod M$ satisfies

$$
v_2(\varphi(N-i))\ge m-i\qquad(0\le i<m).
$$

Then, with an absolute implied constant,

$$
\log_2M\ge\frac{m^2}{2}-O(m\log m).
$$

More explicitly, writing
$E_m=\sum_{2<p<m}(\lceil m/p\rceil-1)v_2(p-1)$, the proof gives
$\log_2M\ge m(m-3)/2-m/2-E_m$. The same asymptotic lower bound holds
for a class forcing $v_2(\varphi(N+j))\ge j+1$ for $1\le j\le m$.

*Proof.* Put $g_i=\gcd(r-i,M)$. The infinitely many small-valuation
members supplied by Lemma A imply
$v_2(\varphi(g_i))\ge m-i-2$. Therefore

$$
\sum_{i<m}v_2(\varphi(g_i))\ge\frac{m(m-3)}2.
$$

An odd prime $p\mid M$ divides at most $\lceil m/p\rceil$ of the $g_i$.
Count one occurrence for each such prime first; its contribution is at
most $\sum_{p\mid M,\ p>2}\log_2p\le\log_2M_{\rm odd}$. Any additional
occurrences come from $p<m$ and contribute at most $E_m$. This treats
shared factors explicitly instead of multiplying separate moduli.
For $a=v_2(M)$, the powers of two contribute at most

$$
\sum_{k=2}^{a}\left\lceil\frac{m}{2^k}\right\rceil
\le\frac m2+a.
$$

Thus the total is at most $\log_2M+E_m+m/2$, giving the explicit bound.
Finally
$E_m\le m\sum_{p<m}(\log_2p)/p=O(m\log m)$, by partial summation from
$\theta(x)=O(x)$. The forward version replaces $g_i$ by
$\gcd(r+j,M)$; its required lower bounds are $j-1$, and the same upper
count applies. $\square$

At any individual $N\ge2$ satisfying the backward window, its $i=0$
condition already implies $2^m\le\varphi(N)<N$, hence $m<\log_2N$.
Thus no such window can reach $m\ge\log_2N$, even at an exceptional
representative. Lemma B supplies the different constraint
$m\le(1+o(1))\sqrt{2\log_2M}$ for whole classes as $m\to\infty$;
it is not a substitute for arithmetic cancellation in the valuation
criterion of the main sketch.

If a chosen representative additionally satisfies $N\ge M$, this yields
$m\le(1+o(1))\sqrt{2\log_2N}$ along families with $m\to\infty$.
Without $N\ge M$, it yields no such bound. Even under that additional
hypothesis it only applies to termwise clearing; divisibility of a sum
through cancellation has a different hypothesis. No matching upper bound
on the least primes in the necessary progressions is supplied by Dirichlet's
theorem alone.

## Divisor positions and prescribed cofactors

**Lemma C.** For a fixed class $N\equiv r\pmod M$ and a prime $p$, the
residue of $N+j$ modulo $p$ is constant throughout the class if and only if
$p\mid M$. If $p\nmid M$, it takes every residue as the class is traversed.
Consequently, a modulus that determines these residues for every prime
$p\le w$ is divisible by $\prod_{p\le w}p$.

*Proof.* In $N+j=r+j+kM$, multiplication by $M$ is zero modulo $p$
when $p\mid M$ and is invertible otherwise. $\square$

This is about residues throughout the class, not complete information about
a selected integer. For example, a specified integer can be factored even
if the progression containing it did not force those factors. Also a
modulus below $X$ need not contain every prime below the largest cutoff
whose primorial is below $X$; containing those primes is a separate choice.

**Lemma D.** Suppose $w\ge2$ and
$N+j=c_jq_j$ for $1\le j\le w$, with positive integers $c_j$ and primes
$q_j>w$. Then every prime $p\le w$ divides
$\operatorname{lcm}(c_1,\ldots,c_w)$. If the divisibilities
$c_j\mid N+j$ hold for every member of $r\pmod M$ with the same $c_j$,
then each $c_j\mid M$ and $M\ge\prod_{p\le w}p$.

*Proof.* Some member of a window of $w$ consecutive integers is divisible
by $p\le w$. Since its prime factor $q_j$ is larger than $w$, $p\mid c_j$.
For the second assertion subtract two consecutive class members in
$c_j\mid r+j+kM$. $\square$

The lemma does not exclude a window at a selected representative, and the
congruences certifying the cofactors do not themselves certify primality
of the remaining factors. No impossibility of such windows follows.

## Approximation and counting remain construction questions

An approximation $B_N$ with
$|T_N-B_N|\le\varepsilon_N$ and
$\operatorname{dist}(bB_N,\mathbb Z)>b\varepsilon_N$ is a sufficient
certificate against denominator $b$. Bounding each term separately is one
way to obtain $\varepsilon_N$; a correlated estimate can do better. Counting
hypothetical independent bits does not prove an information lower bound.
The positive-tail bounds on the sketch page apply only when that tail is
left unsubtracted.

For the elementary many-index pigeonhole attempt, fix odd $q$ and
$r=\operatorname{ord}_q(2)$. Under $S=a/b$, indices $N,N'\le X$ with
$N\equiv N'\pmod r$ and $\Phi_N\equiv\Phi_{N'}\pmod q$ satisfy
$I_N\equiv I_{N'}\pmod q$. If $q>b(X+2)$, the size bound forces equality
of these integers. However, the count $O(X/r)$ of available indices is
smaller than this number of residue boxes, so the elementary pigeonhole
principle alone supplies no collision. It does not show that collisions
are absent or that arithmetic refinements fail.

Likewise a probabilistic model for carry residues can motivate a search
but proves neither the existence nor the sparsity of the witnesses needed
by Proposition 3. The finite data are kept separately in the
[[research/leads/totient_binary_series/evidence/_index|evidence account]].
