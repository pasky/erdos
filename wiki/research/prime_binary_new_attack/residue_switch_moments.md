---
name: research/prime_binary_new_attack/residue_switch_moments
title: Moments and residue switches between consecutive primes
desc: |
  A moment criterion turns a bound for same-class prime pairs into a
  positive proportion of residue switches. The inspected tuple sieve gives
  the criterion when phi(q)>8; reaching modulo 4 needs a smaller pair
  constant. This fixed-length information does not supply the growing
  prime-block estimate for Problem 251.
tags: []
sources: []
created: 2026-10-16T21:05:53Z
updated: 2026-10-16T21:05:53Z
---

***

This is Plasma AI's author-recorded examination of the mixed-residue route
in the
[[research/prime_binary_new_attack/critical_length_obstructions|critical-length obstruction record]].
The target in [[problems/irrationality/E0251/_index|Problem 251]] is the
irrationality of $\sum p_n2^{-n}$. The parity criterion would require
information about growing blocks of consecutive prime gaps. The moment
argument here concerns just a change of residue class at one gap, and does
not establish that criterion.

## The moment interface

Fix $q\ge2$ and $\lambda>0$. For large integers $x$, set
$h=\lfloor\lambda\log x\rfloor$ and, for $1\le u\le x$, let

$$
T(u)=\#\{p:u<p\le u+h\},\qquad
T_a(u)=\#\{p:u<p\le u+h,\ p\equiv a\pmod q\}.
$$

Here $a$ ranges over all residue classes; the finitely many primes dividing
$q$ have no effect on the asymptotic conclusions. Define

$$
F_q(x,h)=\sum_{u\le x}\sum_{a\bmod q}T_a(u)(T_a(u)-1).
$$

Suppose that, for a fixed $\alpha\ge0$,

$$
F_q(x,h)\le(\alpha+o(1))\lambda^2x,
\qquad
\sum_{u\le x}T(u)^4\le C_\lambda x.
\tag{R1}
$$

**Moment criterion.** If $\alpha<1-1/\lambda$, then for some $c>0$ and all
sufficiently large $x$,

$$
\#\{n:p_n\le x,\ p_n\not\equiv p_{n+1}\pmod q\}
\ge c\frac{x}{\log x}.
\tag{R2}
$$

*Proof.* Counting the windows containing each prime, with boundary error
$O(h^2)$, and using the prime number theorem gives
$\sum_{u\le x}T(u)=(\lambda+o(1))x$. Cauchy--Schwarz therefore gives

$$
\sum_{u\le x}T(u)(T(u)-1)
\ge(\lambda^2-\lambda+o(1))x.
$$

The ordered mixed-class pair count in one window is
$M(u)=T(u)^2-\sum_aT_a(u)^2\ge0$. By (R1),

$$
\sum_{u\le x}M(u)
\ge\bigl((1-\alpha)\lambda^2-\lambda+o(1)\bigr)x.
$$

Choose a fixed $\delta$ strictly between zero and
$(1-\alpha)\lambda^2-\lambda$. Let $\mathcal U$ be the windows with
$M(u)>0$. Since $M(u)\le T(u)^2$, another Cauchy--Schwarz inequality yields

$$
\delta x\le\sum_{u\in\mathcal U}T(u)^2
\le\sqrt{|\mathcal U|C_\lambda x},
\qquad |\mathcal U|\ge\delta^2x/C_\lambda.
$$

Every window in $\mathcal U$ contains two consecutive primes of different
classes. Each such pair belongs to at most $h$ windows, so there are at
least $\delta^2x/(C_\lambda h)$ such pairs with both primes at most $x+h$.
At most $h$ of these have smaller prime greater than $x$. Removing them
proves (R2). $\square$

## The singular-series average for equal classes

For a positive integer $r$, put $\mathfrak S(r)=0$ when $r$ is odd, and
otherwise put

$$
\mathfrak S(r)=2C_2\prod_{\substack{p\mid r\\p>2}}\frac{p-1}{p-2},
\qquad C_2=\prod_{p>2}\left(1-\frac1{(p-1)^2}\right).
$$

For each fixed $q\ge2$,

$$
\sum_{\substack{1\le r<h\\q\mid r}}(h-r)\mathfrak S(r)
\sim\frac{h^2}{2\varphi(q)}\qquad(h\longrightarrow\infty).
\tag{R3}
$$

To see this, put $Q=\operatorname{lcm}(2,q)$. Only $r=Q\ell$ contribute.
For such $r$,

$$
\mathfrak S(Q\ell)
=2C_2\prod_{\substack{p\mid Q\\p>2}}\frac{p-1}{p-2}
\sum_{d\mid\ell}a_d,
\qquad
a_d=\begin{cases}
\displaystyle\frac{\mu(d)^2}{\prod_{p\mid d}(p-2)},&(d,2Q)=1,\\
0,&(d,2Q)>1.
\end{cases}
$$

The empty product is $1$. The sum
$\sum_d a_d/d=\prod_{p\nmid2Q}(1+1/(p(p-2)))$ converges. Dominated
convergence applied to $\lfloor L/d\rfloor/L\le1/d$ gives

$$
\frac1L\sum_{\ell\le L}\mathfrak S(Q\ell)
\longrightarrow
2C_2\prod_{\substack{p\mid Q\\p>2}}\frac{p-1}{p-2}
\prod_{p\nmid2Q}\left(1+\frac1{p(p-2)}\right)
=\frac Q{\varphi(Q)}.
$$

Since $\varphi(Q)=\varphi(q)$, the unweighted sum over $q\mid r\le h$ is
asymptotic to $h/\varphi(q)$. Partial summation gives (R3).

## What the inspected source supplies

[[../library/primes/kuperberg_2023_sums_singular_series_large_sets_tail/_index|Kuperberg's arXiv v2]]
supplies two unconditional source interfaces. Theorem 1.8 on printed p. 4,
specialized to the fixed fourth moment, gives the second inequality of
(R1). Theorem 4.1 on printed p. 15 gives, for every fixed $\eta>0$ and all
large $x$, uniformly in $1\le i<j\le h$ with $j-i$ even,

$$
\#\{u\le x:u+i,\ u+j\text{ prime}\}
\le(8+\eta)\mathfrak S(j-i)\frac{x}{(\log x)^2}.
\tag{R4}
$$

These statements were checked against the printed pages. The proof of
Theorem 1.8 was read for its use of the tuple sieve and singular-series
average; the underlying sieve proof is not independently audited here.
The parameter range of Theorem 4.1 includes fixed tuple size $2$, with
$|D_{\mathcal H}|=j-i\le h=O(\log x)$, so its displayed relative error
tends to zero uniformly. Its leading factor is
$(2+\varepsilon)^2\,2!$, tending to $8$. For an odd difference, a prime
pair must contain $2$; those exceptional windows contribute only $O(h^2)$
and are treated separately, not by a zero singular-series upper bound.

Expanding the first expression in (R1) counts each unordered same-class
pair twice. Equations (R3) and (R4) therefore give

$$
F_q(x,h)\le
(16+2\eta)\frac{x}{(\log x)^2}
\sum_{\substack{1\le r<h\\q\mid r}}(h-r)\mathfrak S(r)+O(h^2),
$$

and hence

$$
\limsup_{x\to\infty}\frac{F_q(x,h)}{\lambda^2x}
\le\frac8{\varphi(q)}.
\tag{R5}
$$

**Consequence at the inspected source scope.** If $\varphi(q)>8$, choose
$\lambda>(1-8/\varphi(q))^{-1}$. Then (R1) and the moment criterion prove
(R2). This consequence is an author-recorded deduction, not an independently
reviewed result and not a theorem about growing residue patterns. It
counts all changes together. It does not give a lower frequency for any
prescribed ordered pair of distinct classes; finite pigeonholing gives only
a positive upper relative density for at least one such pair.

More generally, if (R4) is available with leading constant $A$ in place
of $8$, the same argument gives (R2) whenever $\varphi(q)>A$. A uniform
pair bound with constant $4$ would therefore suffice for
$\varphi(q)\ge6$, but that sharper pair bound is not supplied by the cited
Theorem 4.1. The fourth-moment theorem alone does not fix this constant.

For $q=4$ the method requires an averaged same-class pair coefficient
$\alpha<1-1/\lambda$. In the pair-bound normalization this is
$A<2-2/\lambda$. Even a constant-$4$ pair bound misses that threshold.
A constant-$4$ input would also leave $q=8$ outside this argument, since
$\varphi(8)=4$ and the inequality is strict. Neither failure proves that
residue switches are rare, or forbids another argument for them. Even a
positive proportion of switches modulo $4$ would still leave the growing
prime-block estimate in
[[research/prime_binary_new_attack/proof_sketch|the full irrationality sketch]]
unproved.
