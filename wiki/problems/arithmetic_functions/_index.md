---
name: problems/arithmetic_functions
title: Arithmetic Functions
desc: |
  Problems on the values, distribution and iterates of named arithmetic
  functions — Euler's totient, the sum and number of divisors, counts of prime
  factors, the largest prime factor — along with general additive and
  multiplicative functions and perfect, amicable and aliquot-type questions.
created: 2026-09-04T09:17:27Z
updated: 2026-10-13T10:25:58Z
---

# Arithmetic Functions

[[problems/_index|..]]

[[problems/arithmetic_functions/E0048/_index|E0048/]]: Asks whether
$\phi(n)=\sigma(m)$ for infinitely many pairs of integers $n,m$, where $\phi$ is
Euler's totient and $\sigma$ is the sum of divisors.

[[problems/arithmetic_functions/E0050/_index|E0050/]]: Asks whether the density
$f(c)$ of the integers $n$ with $\phi(n)<cn$, as a function of $c$, ever has a
positive derivative.

[[problems/arithmetic_functions/E0051/_index|E0051/]]: Asks whether some
infinite set $A$ of totient values has $n_a/a\to\infty$, where $n_a$ is the
least $n$ with $\phi(n)=a$.

[[problems/arithmetic_functions/E0122/_index|E0122/]]: Asks for which number
theoretic functions $f$ the shifted values $n+f(n)$ cluster unboundedly in short
intervals infinitely often.

[[problems/arithmetic_functions/E0126/_index|E0126/]]: Asks whether $f(n)/\log
n\to\infty$, where $f(n)$ is the least number of distinct prime factors of
$\prod_{a\neq b\in A}(a+b)$ over sets $A\subseteq\mathbb{N}$ of size $n$.

[[problems/arithmetic_functions/E0205/_index|E0205/]]: Asks whether every large
integer $n$ can be written as $2^k+m$ with $\Omega(m)<\log\log m$, where
$\Omega(m)$ counts prime factors with multiplicity.

[[problems/arithmetic_functions/E0239/_index|E0239/]]: Asks whether every
multiplicative function $f:\mathbb{N}\to\{-1,1\}$ has a mean value.

[[problems/arithmetic_functions/E0248/_index|E0248/]]: Asks whether there are
infinitely many $n$ with $\omega(n+k)\ll k$ for all $k\ge1$, where $\omega$
counts distinct prime factors.

[[problems/arithmetic_functions/E0334/_index|E0334/]]: Asks for the best $f(n)$
such that every $n$ is a sum of two integers with no prime factor larger than
$f(n)$; open. Erdős asked whether $n^{\epsilon}$ suffices, which is unsettled,
and whether $n^{1/3}$ does, which Balog's bound answers yes.

[[problems/arithmetic_functions/E0367/_index|E0367/]]: Asks whether, for every
fixed $k$, the product of the powerful parts of $k$ consecutive integers near
$n$ is at most about $n^2$.

[[problems/arithmetic_functions/E0368/_index|E0368/]]: Asks how large the
largest prime factor of $n(n+1)$ is.

[[problems/arithmetic_functions/E0369/_index|E0369/]]: Asks whether every large
$n$ has $k$ consecutive $n^\epsilon$-smooth integers up to $n$. As worded it is
trivially true, and it is proved in both nontrivial readings: each member $m$ is
$m^\epsilon$-smooth, or the run lies in $[n/2,n]$.

[[problems/arithmetic_functions/E0370/_index|E0370/]]: Asks whether infinitely
many $n$ have the largest prime factor of $n$ below $\sqrt{n}$ and that of $n+1$
below $\sqrt{n+1}$.

[[problems/arithmetic_functions/E0371/_index|E0371/]]: Asks whether the integers
$n$ whose largest prime factor is smaller than that of $n+1$ have density $1/2$.

[[problems/arithmetic_functions/E0372/_index|E0372/]]: Asks whether infinitely
many integers $n$ have the largest prime factors of $n$, $n+1$ and $n+2$ in
strictly decreasing order.

[[problems/arithmetic_functions/E0380/_index|E0380/]]: Asks whether the number
of $n\le x$ lying in some interval whose product has a repeated largest prime
factor is asymptotic to the number of $n\le x$ divisible by the square of their
largest prime factor.

[[problems/arithmetic_functions/E0382/_index|E0382/]]: Asks whether an interval
$[u,v]$ in which the largest prime dividing the product appears at least twice
must have $v-u=v^{o(1)}$, and whether $v-u$ can be arbitrarily large.

[[problems/arithmetic_functions/E0383/_index|E0383/]]: Asks whether, for every
$k$, infinitely many primes $p$ are the largest prime factor of $\prod_{0\le
i\le k}(p^2+i)$.

[[problems/arithmetic_functions/E0385/_index|E0385/]]: Asks whether the maximum
of $m+p(m)$ over composite $m<n$, where $p(m)$ is the least prime factor of $m$,
exceeds $n$ for all large $n$, and whether the excess grows without bound.

[[problems/arithmetic_functions/E0408/_index|E0408/]]: Asks whether the number
of iterations of Euler's totient needed to reach 1, divided by $\log n$, has a
distribution function or is almost always constant.

[[problems/arithmetic_functions/E0409/_index|E0409/]]: Asks how many iterations
of $n\mapsto\phi(n)+1$ are needed to reach a prime, and how often a given prime
is reached.

[[problems/arithmetic_functions/E0410/_index|E0410/]]: Asks whether
$\sigma_k(n)^{1/k}\to\infty$ as $k\to\infty$ for every $n\ge2$, where $\sigma_k$
is the $k$-th iterate of the sum-of-divisors function.

[[problems/arithmetic_functions/E0411/_index|E0411/]]: Asks for which $n$ and
$r$ the iterates $g_k$ of $g(n)=n+\phi(n)$ satisfy $g_{k+r}(n)=2g_k(n)$ for all
large $k$.

[[problems/arithmetic_functions/E0412/_index|E0412/]]: Asks whether, for all
$m,n\ge2$, the iterated sum-of-divisors sequences starting at $m$ and at $n$
eventually share a value.

[[problems/arithmetic_functions/E0413/_index|E0413/]]: Asks whether infinitely
many $n$ satisfy $m+\omega(m)\le n$ for every $m<n$, where $\omega(m)$ is the
number of distinct prime factors of $m$.

[[problems/arithmetic_functions/E0414/_index|E0414/]]: Asks whether, under the
map $n\mapsto n+\tau(n)$ with $\tau(n)$ the number of divisors, the iterates of
any two starting integers eventually reach a common value.

[[problems/arithmetic_functions/E0415/_index|E0415/]]: Asks whether the largest
$k$ such that every ordering pattern of $k$ consecutive values of $\phi$ occurs
below $n$ is $(c+o(1))\log\log\log n$, and whether the decreasing pattern always
fails first.

[[problems/arithmetic_functions/E0416/_index|E0416/]]: Asks whether
$V(2x)/V(x)\to2$, where $V(x)$ counts the totient values up to $x$, and whether
$V(x)$ has an asymptotic formula. The doubling limit is proved twice in Lean,
and an asymptotic equivalent from the OpenAI release is a pending claim.

[[problems/arithmetic_functions/E0417/_index|E0417/]]: Asks whether the ratio of
the number of totient values up to $x$ to the number of distinct values
$\phi(m)$ with $m\le x$ has a limit, and whether that limit exceeds 1; open.

[[problems/arithmetic_functions/E0418/_index|E0418/]]: Asks whether infinitely
many positive integers are not of the form $n-\phi(n)$.

[[problems/arithmetic_functions/E0420/_index|E0420/]]: Asks whether
$\tau((n+\lfloor(\log n)^C\rfloor)!)/\tau(n!)$ tends to infinity for large $C$,
where $\tau$ counts divisors.

[[problems/arithmetic_functions/E0452/_index|E0452/]]: Asks for the size of the
largest interval $I\subseteq[x,2x]$ on which every $n$ has more than $\log\log
n$ distinct prime factors.

[[problems/arithmetic_functions/E0456/_index|E0456/]]: Asks three questions
comparing the least prime $p_n\equiv1\pmod{n}$ with the least $m_n$ such that
$n\mid\phi(m_n)$. A September 2026 forum claim answers them no, no and yes,
pending review.

[[problems/arithmetic_functions/E0491/_index|E0491/]]: Asks whether an additive
function whose consecutive differences stay bounded must equal $c'\log n+O(1)$
for some constant $c'$.

[[problems/arithmetic_functions/E0520/_index|E0520/]]: Asks whether, for a
Rademacher random multiplicative function $f$, the limit superior of $\sum_{m\le
N}f(m)/\sqrt{N\log\log N}$ is almost surely a positive constant. A Lean proof
built and audited here shows the ratio tends to 0, so the answer is no.

[[problems/arithmetic_functions/E0647/_index|E0647/]]: Asks whether some $n>24$
satisfies $m+\tau(m)\le n+2$ for every $m<n$, where $\tau(m)$ is the number of
divisors of $m$.

[[problems/arithmetic_functions/E0648/_index|E0648/]]: Asks to estimate the
length of the longest chain of integers $2\le a_1<\cdots<a_t<n$ whose greatest
prime factors strictly decrease.

[[problems/arithmetic_functions/E0649/_index|E0649/]]: Asks whether, for any two
primes $p$ and $q$, some integer $n$ has greatest prime factor $p$ while $n+1$
has greatest prime factor $q$.

[[problems/arithmetic_functions/E0663/_index|E0663/]]: Asks whether, for fixed
$k$ and large $n$, the least prime not dividing $(n+1)\cdots(n+k)$ is less than
$(1+o(1))\log n$.

[[problems/arithmetic_functions/E0679/_index|E0679/]]: Asks whether, for fixed
$\epsilon>0$, infinitely many $n$ have $\omega(n-k)<(1+\epsilon)\log k/\log\log
k$ for all large $k<n$, where $\omega$ counts distinct prime factors.

[[problems/arithmetic_functions/E0690/_index|E0690/]]: Concerns the density
$d_k(p)$ of the integers whose $k$th smallest prime factor is $p$, and asks
whether it is unimodal in $p$ for each fixed $k$.

[[problems/arithmetic_functions/E0694/_index|E0694/]]: Asks for an estimate of
$\max_{n\le x}f_{\max}(n)/f_{\min}(n)$, the largest ratio of the largest to the
smallest $m$ with $\phi(m)=n$ over totient values $n\le x$.

[[problems/arithmetic_functions/E0821/_index|E0821/]]: Asks whether, for every
$\epsilon>0$, infinitely many $n$ have more than $n^{1-\epsilon}$ integers $m$
with $\phi(m)=n$. A proof is claimed by the OpenAI release of September 2026.

[[problems/arithmetic_functions/E0822/_index|E0822/]]: Asks whether the integers
of the form $n+\phi(n)$ have positive lower density.

[[problems/arithmetic_functions/E0823/_index|E0823/]]: Asks whether, for every
real $\alpha\ge1$, there are pairs $n_k,m_k$ with $\sigma(n_k)=\sigma(m_k)$ and
$n_k/m_k\to\alpha$, where $\sigma$ is the sum of divisors.

[[problems/arithmetic_functions/E0824/_index|E0824/]]: Asks whether the number
$h(x)$ of coprime pairs $a<b<x$ with $\sigma(a)=\sigma(b)$ satisfies
$h(x)>x^{2-o(1)}$. An AI-assisted write-up of August 2026 claims
$h(x)>x^{\gamma}$ for every $\gamma<13/8$, and a draft of October 2026 claims
the answer yes under a hypothesis on primes $p$ with $p+1$ free of large prime
factors.

[[problems/arithmetic_functions/E0825/_index|E0825/]]: Asks whether there is a
constant $C$ such that every integer $n$ with $\sigma(n)>Cn$ is a sum of
distinct proper divisors of $n$.

[[problems/arithmetic_functions/E0826/_index|E0826/]]: Asks whether infinitely
many $n$ have $\tau(n+k)\ll k$ for every $k\ge1$, where $\tau$ is the number of
divisors.

[[problems/arithmetic_functions/E0828/_index|E0828/]]: Asks whether, for every
integer $a$, there are infinitely many $n$ with $\phi(n)\mid n+a$.

[[problems/arithmetic_functions/E0830/_index|E0830/]]: Asks whether there are
infinitely many amicable pairs, and whether the number $A(x)$ of them up to $x$
satisfies $A(x)>x^{1-o(1)}$.

[[problems/arithmetic_functions/E0878/_index|E0878/]]: Compares $f(n)$, the sum
over the primes $p\mid n$ of the largest power of $p$ not exceeding $n$, with
$F(n)$, the largest sum of distinct pairwise coprime integers from $2$ to $n$
built from those primes.

[[problems/arithmetic_functions/E0889/_index|E0889/]]: Asks whether
$\max_{k\ge0}v(n,k)\to\infty$, where $v(n,k)$ counts the prime factors of $n+k$
that exceed $k$, that is, those dividing none of $n,n+1,\ldots,n+k-1$.

[[problems/arithmetic_functions/E0891/_index|E0891/]]: Asks whether, for each
$k\ge2$ and every large enough $n$, the interval $[n,n+p_1\cdots p_k)$ contains
an integer with more than $k$ distinct prime factors, where $p_i$ is the $i$th
prime.

[[problems/arithmetic_functions/E0897/_index|E0897/]]: Asks whether an additive
function $f$ with $\limsup f(p^k)/\log p^k=\infty$ must have
$\limsup(f(n+1)-f(n))/\log n=\infty$, or even $\limsup f(n+1)/f(n)=\infty$.

[[problems/arithmetic_functions/E0928/_index|E0928/]]: Asks whether the integers
$n$ with $P(n)<n^{\alpha}$ and $P(n+1)<(n+1)^{\beta}$ have a density, where $P$
is the largest prime factor. The OpenAI release of September 2026 shows the
density is a Dickman product; this is accepted because its Lean proof was built.

[[problems/arithmetic_functions/E0955/_index|E0955/]]: Asks whether every set
$A$ of density zero has a preimage $s^{-1}(A)$ of density zero, where
$s(n)=\sigma(n)-n$ is the sum of proper divisors. Known results cover the
primes, sums of two squares, integers with unusually many prime factors,
palindromes, and sparse and missing-digit sets.

[[problems/arithmetic_functions/E0976/_index|E0976/]]: Asks for estimates of the
greatest prime factor $F_f(n)$ of $\prod_{m\le n}f(m)$ for an irreducible
polynomial $f$, in particular whether $F_f(n)\gg n^{1+c}$ for some $c>0$.

[[problems/arithmetic_functions/E0977/_index|E0977/]]: Asks whether
$P(2^n-1)/n\to\infty$, where $P(m)$ is the greatest prime factor of $m$.

[[problems/arithmetic_functions/E1003/_index|E1003/]]: Asks whether
$\phi(n)=\phi(n+1)$ for infinitely many $n$, where $\phi$ is Euler's totient
function.

[[problems/arithmetic_functions/E1004/_index|E1004/]]: Asks whether, for every
fixed $c>0$ and all large $x$, some $n\le x$ has the values $\phi(n+k)$ distinct
for $1\le k\le(\log x)^c$.

[[problems/arithmetic_functions/E1052/_index|E1052/]]: Asks whether there are
only finitely many unitary perfect numbers, the integers $n$ equal to the sum of
their proper divisors $d$ with $(d,n/d)=1$.

[[problems/arithmetic_functions/E1053/_index|E1053/]]: Asks whether every $k$
with $\sigma(n)=kn$ must satisfy $k=o(\log\log n)$.

[[problems/arithmetic_functions/E1060/_index|E1060/]]: Asks whether the number
$f(n)$ of solutions $k$ of $k\sigma(k)=n$ satisfies $f(n)\le n^{o(1/\log\log
n)}$, or perhaps even $f(n)\le(\log n)^{O(1)}$.

[[problems/arithmetic_functions/E1061/_index|E1061/]]: Asks whether the number
of solutions of $\sigma(a)+\sigma(b)=\sigma(a+b)$ with $a+b\le x$ is $\sim cx$
for some constant $c>0$. Li's preprint of June 2026 claims it exceeds $x(\log
x)^R$ for every fixed $R>0$, and the claim is pending.

[[problems/arithmetic_functions/E1064/_index|E1064/]]: Asks whether
$\phi(n)>\phi(n-\phi(n))$ for almost all $n$ and the reverse inequality holds
for infinitely many $n$. Luca and Pomerance (2002) proved the first part, and
Grytczuk, Luca and Wójtowicz (2001) the second.

[[problems/arithmetic_functions/E1106/_index|E1106/]]: Asks whether the number
$F(n)$ of distinct prime factors of $p(1)p(2)\cdots p(n)$, with $p$ the
partition function, tends to infinity, and whether $F(n)>n$ for all large $n$.

[[problems/arithmetic_functions/E1122/_index|E1122/]]: Asks whether an additive
function $f$ with $f(n+1)<f(n)$ only for a density-zero set of $n$ must be
$c\log n$ for some real $c$.

[[problems/arithmetic_functions/E1144/_index|E1144/]]: Asks whether a random
completely multiplicative function $f$ with values $\pm1$ almost surely has
$\limsup_{N\to\infty}\sum_{m\le N}f(m)/\sqrt{N}=\infty$.

[[problems/arithmetic_functions/E1203/_index|E1203/]]: Asks whether
$F(n)=\max_k\omega(n+k)\log\log k/\log k$ tends to infinity as $n\to\infty$,
where $\omega$ counts distinct prime factors.

***

Problems on the values, distribution and iterates of named arithmetic functions
— Euler's totient, the sum and number of divisors, counts of prime factors, the
largest prime factor — along with general additive and multiplicative functions
and perfect, amicable and aliquot-type questions.

erdosproblems.com tags routed here: divisors, iterated functions, number theory,
powerful, probability, unit fractions.
