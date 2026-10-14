---
name: problems/primes
title: Primes
desc: |
  Distribution of the primes, prime gaps, and prime values and patterns in
  arithmetic sequences.
created: 2026-09-04T09:17:27Z
updated: 2026-10-14T01:26:14Z
---

# Primes

[[problems/_index|..]]

[[problems/primes/E0004/_index|E0004/]]: Asks whether, for every $C>0$,
infinitely many $n$ have $p_{n+1}-p_n>C\frac{\log\log n\,\log\log\log\log
n}{(\log\log\log n)^2}\log n$, where $p_n$ is the $n$th prime.

[[problems/primes/E0005/_index|E0005/]]: Asks whether, for every $C\ge 0$, some
sequence of indices $n_i$ has $(p_{n_i+1}-p_{n_i})/\log n_i\to C$, where $p_n$
is the $n$th prime.

[[problems/primes/E0006/_index|E0006/]]: Asks whether there are infinitely many
$n$ for which three consecutive prime gaps are strictly increasing, that is,
$d_n<d_{n+1}<d_{n+2}$ with $d_n=p_{n+1}-p_n$.

[[problems/primes/E0015/_index|E0015/]]: Asks whether $\sum_{n\ge 1}(-1)^n
n/p_n$ converges, where $p_n$ is the $n$th prime; open. Tao proved convergence
conditional on a strong Hardy-Littlewood prime tuples conjecture.

[[problems/primes/E0017/_index|E0017/]]: Asks whether infinitely many primes $p$
have every even $n\le p-3$ expressible as $q_1-q_2$ with primes $q_1,q_2\le p$.

[[problems/primes/E0049/_index|E0049/]]: Asks whether a set
$A\subseteq\{1,\ldots,N\}$ on which Euler's totient function $\phi$ is strictly
increasing has $\lvert A\rvert<(1+o(1))\pi(N)$, or even $\lvert A\rvert=o(N)$.
Erdős's exact conjecture, that the primes are a largest such set, is open.

[[problems/primes/E0218/_index|E0218/]]: Asks whether the $n$ with $d_{n+1}\ge
d_n$ and those with $d_{n+1}\le d_n$ each have density $1/2$, where
$d_n=p_{n+1}-p_n$, and whether $d_{n+1}=d_n$ for infinitely many $n$.

[[problems/primes/E0233/_index|E0233/]]: Asks whether $\sum_{n\le N}d_n^2\ll
N(\log N)^2$, where $d_n=p_{n+1}-p_n$ is the gap after the $n$th prime.

[[problems/primes/E0234/_index|E0234/]]: Asks whether, for every $c\ge0$, the
density $f(c)$ of integers $n$ with $p_{n+1}-p_n<c\log n$ exists and is a
continuous function of $c$.

[[problems/primes/E0236/_index|E0236/]]: Asks whether the number $f(n)$ of
solutions of $n=p+2^k$, with $p$ prime and $k\ge0$, satisfies $f(n)=o(\log n)$.

[[problems/primes/E0237/_index|E0237/]]: Asks whether every set
$A\subseteq\mathbb{N}$ with $\lvert A\cap\{1,\ldots,N\}\rvert\gg\log N$ for all
large $N$ gives $\limsup f(n)=\infty$, where $f(n)$ counts the solutions of
$n=p+a$ with $p$ prime and $a\in A$.

[[problems/primes/E0238/_index|E0238/]]: Asks whether, for any $c_1,c_2>0$ and
all large $x$, there are more than $c_1\log x$ consecutive primes $\le x$ whose
pairwise differences all exceed $c_2$.

[[problems/primes/E0240/_index|E0240/]]: Asks whether there is an infinite set
$P$ of primes such that the gaps $a_{i+1}-a_i$ between consecutive integers
divisible only by primes in $P$ tend to infinity.

[[problems/primes/E0244/_index|E0244/]]: Asks whether, for $C>1$, the integers
of the form $p+\lfloor C^k\rfloor$, with $p$ prime and $k\ge0$, have positive
density.

[[problems/primes/E0427/_index|E0427/]]: Asks whether, for every $n$ and $d$,
some sum $p_{n+1}+\cdots+p_{n+k}$ of consecutive primes is divisible by $d$.

[[problems/primes/E0428/_index|E0428/]]: Asks whether there is a set
$A\subseteq\mathbb{N}$ with $\liminf\lvert A\cap[1,x]\rvert/\pi(x)>0$ such that,
for infinitely many $n$, $n-a$ is prime for every $a\in A$ with $0<a<n$.

[[problems/primes/E0431/_index|E0431/]]: Asks whether there are two infinite
sets $A$ and $B$ such that $A+B$ agrees with the set of primes up to finitely
many exceptions.

[[problems/primes/E0454/_index|E0454/]]: Asks whether
$f(n)=\min_{i<n}(p_{n+i}+p_{n-i})$, the least sum of two primes placed
symmetrically around $p_n$, satisfies $\limsup_n(f(n)-2p_n)=\infty$.

[[problems/primes/E0458/_index|E0458/]]: Asks whether
$[1,\ldots,p_{k+1}-1]<p_k[1,\ldots,p_k]$ for all $k\ge1$, where $[1,\ldots,n]$
is the least common multiple of $1,\ldots,n$.

[[problems/primes/E0459/_index|E0459/]]: Asks to estimate $f(u)$, the largest
$v$ such that no integer strictly between $u$ and $v$ is composed only of primes
dividing $uv$.

[[problems/primes/E0461/_index|E0461/]]: Asks whether, uniformly for all $t$ and
$n$, the $t$-smooth parts of the $t$ integers in $[n+1,n+t]$ take $\gg t$
distinct values, where the $t$-smooth part of $m$ is the product of its prime
factors below $t$, counted with multiplicity.

[[problems/primes/E0462/_index|E0462/]]: Asks whether there is a constant $C>0$
with $\sum_{x\le n\le x+Cx^{1/2}(\log x)^2}p(n)/n\gg1$ for all large $x$, where
$p(n)$ is the least prime factor of $n$.

[[problems/primes/E0463/_index|E0463/]]: Asks whether there is a function $f$
with $f(n)\to\infty$ such that, for all large $n$, some composite $m$ satisfies
$n+f(n)<m<n+p(m)$, where $p(m)$ is the least prime factor of $m$.

[[problems/primes/E0680/_index|E0680/]]: Asks whether every sufficiently large
$n$ has some $k$ with $p(n+k)>k^2+1$, where $p(m)$ is the least prime factor of
$m$.

[[problems/primes/E0681/_index|E0681/]]: Asks whether every large $n$ has some
$k$ such that $n+k$ is composite and $p(n+k)>k^2$, where $p(m)$ is the least
prime factor of $m$.

[[problems/primes/E0682/_index|E0682/]]: Asks whether, for almost all $n$, some
integer $m\in(p_n,p_{n+1})$ has least prime factor $p(m)\ge p_{n+1}-p_n$.

[[problems/primes/E0779/_index|E0779/]]: Asks whether, for the product
$P=p_1\cdots p_n$ of the first $n>1$ primes, there is always a prime $p$ with
$p_n<p<P$ such that $P+p$ is prime.

[[problems/primes/E0850/_index|E0850/]]: Asks whether there are distinct
integers $x$ and $y$ such that $x$ and $y$, $x+1$ and $y+1$, and $x+2$ and $y+2$
each have the same prime factors.

[[problems/primes/E0852/_index|E0852/]]: Asks to estimate $h(x)$, the length of
the longest run of pairwise distinct consecutive prime gaps $d_n,d_{n+1},\ldots$
starting at some $n<x$. In particular, it asks whether $h(x)>(\log x)^c$ for
some $c>0$ and whether $h(x)=o(\log x)$.

[[problems/primes/E0853/_index|E0853/]]: Asks whether $r(x)$, the least even
number that is not a prime gap $p_{n+1}-p_n$ with $n\le x$, tends to infinity,
and whether even $r(x)/\log x\to\infty$.

[[problems/primes/E0855/_index|E0855/]]: Asks whether the prime-counting
function satisfies $\pi(x+y)\le\pi(x)+\pi(y)$ for all large $x$ and $y$.

[[problems/primes/E0860/_index|E0860/]]: Asks to estimate the least $h(n)$ such
that every interval $(m,m+h(n))$ contains distinct integers
$a_1,\ldots,a_{\pi(n)}$, with $a_i$ divisible by the $i$th prime $p_i$.

[[problems/primes/E0890/_index|E0890/]]: Asks whether $\liminf_n\sum_{0\le
i<k}\omega_k(n+i)\le k$ for every $k\ge1$, where $\omega_k$ counts the distinct
prime factors above $k$, and whether $\limsup_n\bigl(\sum_{0\le
i<k}\omega(n+i)\bigr)\log\log n/\log n=1$, where $\omega$ counts all distinct
prime factors.

[[problems/primes/E0950/_index|E0950/]]: Asks whether $f(n)=\sum_{p<n}1/(n-p)$,
summed over primes $p<n$, has $\liminf f(n)=1$ and $\limsup f(n)=\infty$, and
whether $f(n)=o(\log\log n)$.

[[problems/primes/E1055/_index|E1055/]]: Primes are sorted into classes by the
prime factors of $p+1$, with class $1$ holding the primes $p$ for which $p+1$
has no prime factor other than $2$ and $3$. The problem asks whether every class
is infinite and how $p_r^{1/r}$ behaves, where $p_r$ is the least prime in class
$r$.

[[problems/primes/E1059/_index|E1059/]]: Asks whether infinitely many primes $p$
have $p-k!$ composite for every $k$ with $1\le k!<p$.

[[problems/primes/E1137/_index|E1137/]]: Asks whether, with $d_n=p_{n+1}-p_n$,
the ratio $\max_{n<x}d_nd_{n-1}/(\max_{n<x}d_n)^2$ tends to $0$ as $x\to\infty$.

[[problems/primes/E1138/_index|E1138/]]: Asks whether $\pi(y+Cd)-\pi(y)\sim
Cd/\log y$ for $x/2<y<x$ and $C>1$, where $d=\max_{p_n<x}(p_{n+1}-p_n)$ is the
largest prime gap below $x$.

[[problems/primes/E1139/_index|E1139/]]: Asks whether the sequence
$u_1<u_2<\cdots$ of integers with at most two prime factors has $\limsup
(u_{k+1}-u_k)/\log k=\infty$.

[[problems/primes/E1141/_index|E1141/]]: Asks whether infinitely many $n$ have
$n-k^2$ prime for every $k$ coprime to $n$ with $k^2<n$.

[[problems/primes/E1142/_index|E1142/]]: Asks whether infinitely many $n$, or
any $n>105$, have $n-2^k$ prime for every $k$ with $1<2^k<n$.

[[problems/primes/E1143/_index|E1143/]]: Asks to estimate, for given primes
$p_1<\cdots<p_u$, how many integers divisible by some $p_i$ every interval of
$k$ consecutive positive integers must contain.

[[problems/primes/E1184/_index|E1184/]]: Asks whether, for $n=k^{\alpha+o(1)}$
with $\alpha>1$, the number of integers among $n+1,\ldots,n+k$ whose largest
prime factor exceeds $k$ is $(1-\rho(\alpha)+o(1))k$, with $\rho$ the Dickman
function.

[[problems/primes/E1200/_index|E1200/]]: Asks for a constant $C$ such that, for
every large $x$, there are primes $p_1<\cdots<p_k<x$ with $\sum 1/p_i<C$ and
congruences $a_i\pmod{p_i}$ that cover every integer $n<x$.

[[problems/primes/E1201/_index|E1201/]]: Asks whether, for all
$\epsilon,\eta>0$, some $k$ makes the largest prime factor of
$n(n+1)\cdots(n+k)$ exceed $n^{1-\epsilon}$ on a set of $n$ of lower density at
least $1-\eta$, as the erdosproblems.com curator reads the density.

[[problems/primes/E1202/_index|E1202/]]: Asks whether some $k$ ensures that, for
any $k$ primes $p_i<n^{1-\epsilon}$, removing $(p_i-1)/2$ residue classes modulo
each $p_i$ leaves at most $\epsilon n$ integers $m\le n$.

[[problems/primes/E1212/_index|E1212/]]: Asks whether some path to infinity,
changing one coordinate by $\pm1$ per step, stays among coprime pairs $(x,y)$
with $\min(x,y)>1$ and a composite coordinate. Stewart quickly answered yes to
Erdős's first version, without the composite condition.

***

Distribution of the primes, prime gaps, and prime values and patterns in
arithmetic sequences.

erdosproblems.com tags routed here: number theory, primes.
