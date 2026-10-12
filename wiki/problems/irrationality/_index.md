---
name: problems/irrationality
title: Irrationality and Diophantine Approximation
desc: |
  Irrationality and transcendence of series and constants, irrationality
  sequences, and how well real numbers can be approximated by rationals.
created: 2026-09-04T09:17:27Z
updated: 2026-10-12T00:09:36Z
---

# Irrationality and Diophantine Approximation

[[problems/_index|..]]

[[problems/irrationality/E0068/_index|E0068/]]: Asks whether
$\sum_{n\ge2}\frac{1}{n!-1}$ is irrational.

[[problems/irrationality/E0069/_index|E0069/]]: Asks whether
$\sum_{n\ge2}\omega(n)/2^n$ is irrational, where $\omega(n)$ is the number of
distinct prime factors of $n$.

[[problems/irrationality/E0243/_index|E0243/]]: Asks whether every increasing
integer sequence with $a_n/a_{n-1}^2\to1$ and $\sum 1/a_n$ rational must satisfy
$a_n=a_{n-1}^2-a_{n-1}+1$ for all large $n$.

[[problems/irrationality/E0247/_index|E0247/]]: Asks whether $\sum_n 2^{-a_n}$
is transcendental for every increasing integer sequence $a_n$ with $\limsup
a_n/n=\infty$.

[[problems/irrationality/E0249/_index|E0249/]]: Asks whether $\sum_n \phi(n)/2^n$
is irrational, where $\phi$ is Euler's totient function.

[[problems/irrationality/E0250/_index|E0250/]]: Asks whether $\sum_n \sigma(n)/2^n$
is irrational, where $\sigma$ is the sum-of-divisors function.

[[problems/irrationality/E0251/_index|E0251/]]: Asks whether $\sum_n p_n/2^n$ is
irrational, where $p_n$ is the $n$th prime.

[[problems/irrationality/E0252/_index|E0252/]]: Asks whether $\sum_n \sigma_k(n)/n!$
is irrational for every $k\ge1$, where $\sigma_k(n)=\sum_{d\mid n}d^k$. A 2026
kernel-checked Lean proof, rebuilt, replayed and statement-audited here, answers
yes.

[[problems/irrationality/E0257/_index|E0257/]]: Asks whether $\sum_{n\in
A}\frac{1}{2^n-1}$ is irrational for every infinite set $A\subseteq\mathbb{N}$.

[[problems/irrationality/E0258/_index|E0258/]]: Asks whether $\sum_n \tau(n)/(a_1\cdots
a_n)$ is irrational for every sequence of positive integers $a_n\to\infty$,
where $\tau(n)$ is the number of divisors of $n$.

[[problems/irrationality/E0259/_index|E0259/]]: Asks whether the sum of $n/2^n$
over all squarefree $n$ is irrational.

[[problems/irrationality/E0260/_index|E0260/]]: Asks whether $\sum_n
a_n/2^{a_n}$ is irrational for every increasing sequence $a_n$ with
$a_n/n\to\infty$.

[[problems/irrationality/E0262/_index|E0262/]]: Asks how slowly an increasing
integer sequence $a_n$ can grow if $\sum_n 1/(t_na_n)$ is irrational for every
sequence of positive integers $t_n$.

[[problems/irrationality/E0263/_index|E0263/]]: Asks whether $a_n=2^{2^n}$ makes
$\sum 1/b_n$ irrational for every sequence of positive integers $b_n$ with
$b_n/a_n\to1$, and whether every $a_n$ with this property must satisfy
$a_n^{1/n}\to\infty$.

[[problems/irrationality/E0264/_index|E0264/]]: Asks whether $a_n=2^n$ or
$a_n=n!$ makes $\sum 1/(a_n+b_n)$ irrational for every bounded sequence of
nonzero integers $b_n$ with $a_n+b_n\ne0$. The case $a_n=2^n$ is answered no.

[[problems/irrationality/E0265/_index|E0265/]]: Asks how fast an increasing
integer sequence $a_n$ can grow if $\sum 1/a_n$ and $\sum 1/(a_n-1)$ are both
rational.

[[problems/irrationality/E0266/_index|E0266/]]: Asks whether every sequence of
positive integers $a_n$ with $\sum 1/a_n$ convergent has an integer $t\ge1$
making $\sum 1/(a_n+t)$ irrational.

[[problems/irrationality/E0267/_index|E0267/]]: Asks whether $\sum_k 1/F_{n_k}$
must be irrational whenever $n_{k+1}/n_k\ge c>1$, where $F_n$ are the Fibonacci
numbers.

[[problems/irrationality/E0269/_index|E0269/]]: Asks whether $\sum_n
1/\operatorname{lcm}(a_1,\ldots,a_n)$ is irrational, where $a_1<a_2<\cdots$ are
the integers whose prime factors lie in a fixed finite set of at least two
primes.

[[problems/irrationality/E0270/_index|E0270/]]: Asks whether
$\sum_{n\ge1}\frac{1}{(n+1)\cdots(n+f(n))}$ is irrational whenever
$f(n)\to\infty$.

[[problems/irrationality/E0495/_index|E0495/]]: Asks whether
$\liminf_{n\to\infty} n\|n\alpha\|\|n\beta\|=0$ for all real $\alpha,\beta$,
where $\|x\|$ is the distance from $x$ to the nearest integer.

[[problems/irrationality/E0496/_index|E0496/]]: Asks whether, for every
irrational $\alpha>0$ and $\epsilon>0$, some positive integers $x,y,z$ satisfy
$|x^2+y^2-z^2\alpha|<\epsilon$. The site's wording, over every irrational
$\alpha$, fails for negative $\alpha$.

[[problems/irrationality/E0998/_index|E0998/]]: Asks whether, for irrational
$\alpha$, an interval $[u,v)$ with bounded discrepancy along the fractional
parts $\{\alpha m\}$ must have length $v-u=\{\alpha j\}$ for some integer $j$.
The site's wording, which asks this of both endpoints, is false.

[[problems/irrationality/E0999/_index|E0999/]]: Asks whether, for every
$f:\mathbb{N}\to\mathbb{N}$, almost every $\alpha$ satisfies
$|\alpha-p/q|<f(q)/q$ for infinitely many coprime $p,q$ if and only if
$\sum_{q\ge1}\phi(q)f(q)/q=\infty$.

[[problems/irrationality/E1000/_index|E1000/]]: Asks whether some infinite
integer sequence $n_1<n_2<\cdots$ has $\frac{1}{N}\sum_{k\le
N}\phi_A(k)/n_k\to0$, where $\phi_A(k)$ counts the fractions $m/n_k$ with $1\le
m\le n_k$ whose denominator in lowest terms differs from every earlier $n_j$.

[[problems/irrationality/E1001/_index|E1001/]]: Asks whether the measure of the
set of $\alpha\in(0,1)$ with $|\alpha-x/y|<A/y^2$ for some reduced $x/y$ with
$N\le y\le cN$ tends to a limit as $N\to\infty$, and what that limit is
explicitly.

[[problems/irrationality/E1002/_index|E1002/]]: Asks whether
$f(\alpha,n)=\frac{1}{\log n}\sum_{k\le n}(\frac{1}{2}-\{\alpha k\})$ has an
asymptotic distribution function over $\alpha\in(0,1)$ as $n\to\infty$.

[[problems/irrationality/E1049/_index|E1049/]]: Asks whether
$\sum_{n\ge1}1/(t^n-1)$ is irrational for every rational $t>1$.

[[problems/irrationality/E1050/_index|E1050/]]: Asks whether
$\sum_{n\ge1}1/(2^n-3)$ is irrational.

[[problems/irrationality/E1051/_index|E1051/]]: Asks whether
$\sum_{n\ge1}1/(a_na_{n+1})$ is irrational for every increasing integer sequence
$1\le a_1<a_2<\cdots$ with $\liminf a_n^{1/2^n}>1$.

***

Irrationality and transcendence of series and constants, irrationality
sequences, and how well real numbers can be approximated by rationals.

Site tags routed here: analysis, diophantine approximation, irrationality,
number theory.
