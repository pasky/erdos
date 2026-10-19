---
name: problems/divisors
title: Divisors and Multiples
desc: |
  Divisor functions and the distribution of divisors, multiplication tables,
  sets of multiples, primitive sets in which no element divides another, and
  other sets of integers defined by divisibility or coprimality conditions.
created: 2026-09-04T09:17:27Z
updated: 2026-10-19T10:58:49Z
---

# Divisors and Multiples

[[problems/_index|..]]

[[problems/divisors/E0018/_index|E0018/]]: Asks how small $h(m)$ can be, the number of distinct divisors of a practical
number $m$ that always suffice to write each smaller integer as a sum,
especially for $m=n!$. The bound $h(n!)<n^{o(1)}$ is proved (Conjectures.io,
2026), the $(\log\log m)^{O(1)}$ part is claimed (van Doorn and GPT-6 Astra Pro, 2026, graded sound by Plasma AI's internal review, its sign-off pending), and the rest is open.

[[problems/divisors/E0026/_index|E0026/]]: Asks whether every infinite set
$A\subset\mathbb{N}$ has a shift $k\ge1$ such that almost all integers have a
divisor of the form $a+k$ with $a\in A$.

[[problems/divisors/E0056/_index|E0056/]]: Asks whether the multiples of the
first $k$ primes form the largest subset of $\{1,\ldots,N\}$ with no $k+1$
pairwise relatively prime elements.

[[problems/divisors/E0143/_index|E0143/]]: Asks whether a countably infinite set
$A\subset(1,\infty)$ with $\lvert kx-y\rvert\ge1$ for all distinct $x,y\in A$
and all integers $k\ge1$ must be sparse.

[[problems/divisors/E0144/_index|E0144/]]: Asks whether the density of integers
with two divisors $d_1<d_2<2d_1$ exists and equals $1$, so that almost every
integer has such a pair.

[[problems/divisors/E0164/_index|E0164/]]: Asks whether the sum of $1/(n\log n)$
over a primitive set $A$, one in which no member divides another, is largest
when $A$ is the set of primes.

[[problems/divisors/E0381/_index|E0381/]]: Asks whether the number $Q(x)$ of
highly composite numbers up to $x$ grows faster than every fixed power of $\log
x$.

[[problems/divisors/E0444/_index|E0444/]]: Asks whether, for every infinite
$A\subseteq\mathbb{N}$ and every $k$, the ratio of $\max_{n<x}d_A(n)$ to
$\bigl(\sum_{a\in A,\,a<x}1/a\bigr)^k$ is unbounded, where $d_A(n)$ counts the
elements of $A$ dividing $n$.

[[problems/divisors/E0446/_index|E0446/]]: Asks for the growth rate of the
density $\delta(n)$ of integers with a divisor in $(n,2n)$, and whether those
with exactly one such divisor have density $o(\delta(n))$.

[[problems/divisors/E0448/_index|E0448/]]: Asks whether, for every $\epsilon>0$,
almost all $n$ have fewer than $\epsilon\tau(n)$ dyadic intervals
$[2^k,2^{k+1})$ containing a divisor of $n$, where $\tau(n)$ is the number of
divisors.

[[problems/divisors/E0449/_index|E0449/]]: Asks whether, for every $\epsilon>0$,
almost all $n$ have fewer than $\epsilon\tau(n)$ pairs of divisors
$d_1<d_2<2d_1$, where $\tau(n)$ is the number of divisors.

[[problems/divisors/E0450/_index|E0450/]]: Asks how large $y=y(\epsilon,n)$ must
be for at most $\epsilon y$ of the integers in $(x,x+y)$ to have a divisor in
$(n,2n)$.

[[problems/divisors/E0468/_index|E0468/]]: Concerns the set $D_n$ of partial
sums $d_1,d_1+d_2,\ldots$ of the divisors $1<d_1<d_2<\cdots$ of $n$. It asks how
many elements of $D_n$ lie in no earlier $D_m$, and whether the least $n$ with
$N\in D_n$ is $o(N)$.

[[problems/divisors/E0469/_index|E0469/]]: Asks whether $\sum 1/n$ converges
over the integers $n$ that are sums of distinct proper divisors of themselves
while no proper divisor of $n$ has that property.

[[problems/divisors/E0470/_index|E0470/]]: Asks whether there are odd weird
numbers and infinitely many primitive ones, where $n$ is weird if
$\sigma(n)\ge2n$ but $n$ is not a sum of distinct proper divisors of $n$, and
primitive if no proper divisor of $n$ is weird.

[[problems/divisors/E0486/_index|E0486/]]: Asks whether, for any
$A\subseteq\mathbb{N}$ and sets $X_n\subseteq\mathbb{Z}/n\mathbb{Z}$, the
integers $m$ with $m\notin X_n\pmod n$ for all $n\in A$ with $m>n$ must have a
logarithmic density.

[[problems/divisors/E0534/_index|E0534/]]: Asks for the largest
$A\subseteq\{1,\ldots,N\}$ that contains $N$ and has $\gcd(a,b)>1$ for all
distinct $a,b\in A$.

[[problems/divisors/E0673/_index|E0673/]]: Asks whether the sum $G(n)$ of the
ratios $d_i/d_{i+1}$ of consecutive divisors of $n$ tends to infinity for almost
all $n$, and seeks an asymptotic formula for its average.

[[problems/divisors/E0692/_index|E0692/]]: Asks whether the density
$\delta_1(n,m)$ of integers with exactly one divisor in $(n,m)$ is unimodular in
$m$ for $m>n+1$; disproved by Cambie, who also shows it has many local maxima.

[[problems/divisors/E0693/_index|E0693/]]: Asks for an estimate of the largest
gap between consecutive integers in $[n,n^k]$, for fixed $k\ge2$, that have a
divisor in $(n,2n)$, and whether it is at most $(\log n)^{O(1)}$.

[[problems/divisors/E0696/_index|E0696/]]: Asks for estimates of $h(n)$ and
$H(n)$, the lengths of the longest chains of prime divisors and of divisors of
$n$ in which each term is $1$ modulo the previous one, and whether
$H(n)/h(n)\to\infty$ for almost all $n$.

[[problems/divisors/E0697/_index|E0697/]]: Asks whether there is some
$\beta\in(1,\infty)$ such that, as $m\to\infty$, the density of integers with a
divisor $d\equiv1\pmod m$ in $(1,\exp(m^\alpha))$ tends to $0$ for
$\alpha<\beta$ and to $1$ for $\alpha>\beta$.

[[problems/divisors/E0844/_index|E0844/]]: Asks whether the even numbers
together with the odd non-squarefree numbers form a largest
$A\subseteq\{1,\ldots,N\}$ in which no product $ab$ with $a,b\in A$ is
squarefree.

[[problems/divisors/E0858/_index|E0858/]]: Asks for an estimate of the maximum
of $(1/\log N)\sum_{n\in A}1/n$ over $A\subseteq\{1,\ldots,N\}$ with no solution
to $at=b$ in which $a,b\in A$ and every prime factor of $t$ exceeds $a$.

[[problems/divisors/E0859/_index|E0859/]]: Asks whether the density $d_t$ of the
integers $n$ for which $t$ is a sum of distinct divisors of $n$ satisfies
$d_t\sim c_1/(\log t)^{c_2}$ for some constants $c_1,c_2>0$. A Lean disproof,
certified by the bounty site Conjectures.io in 2026, shows that it does not.

[[problems/divisors/E0872/_index|E0872/]]: Asks how long a game can be
guaranteed to last in which two players alternately add integers from
$\{2,\ldots,n\}$ to a shared set with no member dividing another, and whether it
lasts at least $\epsilon n$ or $(1-\epsilon)n/2$ moves.

[[problems/divisors/E0882/_index|E0882/]]: Asks for the size of the largest
$A\subseteq\{1,\ldots,n\}$ whose nonempty subset sums form a set in which no
element divides another.

[[problems/divisors/E0884/_index|E0884/]]: Asks whether the sum of $1/(d_j-d_i)$
over all pairs of divisors $d_i<d_j$ of $n$ is at most an absolute constant
times $1+\sum_i 1/(d_{i+1}-d_i)$, the sum over consecutive divisors.

[[problems/divisors/E0885/_index|E0885/]]: Asks whether, for every $k\ge1$,
there are integers $N_1<\cdots<N_k$ whose factor difference sets $D(N)=\{\lvert
a-b\rvert : N=ab\}$ share at least $k$ common values.

[[problems/divisors/E0886/_index|E0886/]]: Asks whether, for each fixed
$\epsilon>0$, every large $n$ has only boundedly many divisors in
$(n^{1/2},n^{1/2}+n^{1/2-\epsilon})$.

[[problems/divisors/E0887/_index|E0887/]]: Asks whether there is an absolute
constant $K$ such that, for every $C>0$, every large $n$ has at most $K$
divisors in $(n^{1/2},n^{1/2}+Cn^{1/4})$.

[[problems/divisors/E0892/_index|E0892/]]: Asks for a necessary and sufficient
condition on an increasing sequence $(b_n)$ of integers for there to be a
primitive sequence $(a_n)$, in which no term divides another, with $a_n\ll b_n$.

[[problems/divisors/E0893/_index|E0893/]]: Asks whether $f(2n)/f(n)$ tends to a
limit, where $f(n)=\sum_{k\le n}\tau(2^k-1)$ sums the divisor counts of $2^k-1$.

[[problems/divisors/E0945/_index|E0945/]]: Asks for an estimate of the longest
run of consecutive integers up to $x$ with all divisor counts distinct, and
whether, for some constant $C>0$, every interval $[x,x+(\log x)^C]$ with $x$
large repeats a divisor count.

[[problems/divisors/E0946/_index|E0946/]]: Asks whether there are infinitely
many $n$ such that $n$ and $n+1$ have the same number of divisors.

[[problems/divisors/E0964/_index|E0964/]]: Asks whether the ratios
$\tau(n+1)/\tau(n)$ of consecutive divisor counts are dense in $(0,\infty)$.

[[problems/divisors/E1054/_index|E1054/]]: Asks whether $f(n)=o(n)$, or whether
this holds only for almost all $n$ and $\limsup f(n)/n=\infty$, where $f(n)$ is
the least $m$ such that $n$ is the sum of the $k$ smallest divisors of $m$ for
some $k$.

[[problems/divisors/E1099/_index|E1099/]]: Asks whether, for each $\alpha>1$,
the sum $\sum_i(d_{i+1}/d_i-1)^\alpha$ over consecutive divisors $d_i<d_{i+1}$
of $n$ has limit inferior bounded in terms of $\alpha$ as $n\to\infty$.

[[problems/divisors/E1100/_index|E1100/]]: Asks whether the number
$\tau_\perp(n)$ of coprime consecutive divisor pairs of $n$ satisfies
$\tau_\perp(n)/\omega(n)\to\infty$ for almost all $n$ and
$\tau_\perp(n)<\exp((\log n)^{o(1)})$ for all $n$, and how its maximum over
squarefree $n$ with $\omega(n)=k$ grows.

[[problems/divisors/E1196/_index|E1196/]]: Asks whether every primitive set
$A\subset[x,\infty)$, in which no element divides another, has $\sum_{a\in
A}1/(a\log a)<1+o(1)$ as $x\to\infty$.

[[problems/divisors/E1217/_index|E1217/]]: Asks whether a sequence of positive
lower logarithmic density contains a divisibility chain whose count below $x$,
divided by $\log\log x$, has $\limsup$ at least that of $\sum_{a_n<x}1/(a_n\log
a_n)$ divided by $\log\log x$; answered yes in 2026 by Alexeev and seven
coauthors.

***

Divisor functions and the distribution of divisors, multiplication tables, sets
of multiples, primitive sets in which no element divides another, and other sets
of integers defined by divisibility or coprimality conditions.

erdosproblems.com tags routed here: divisors, factorials, intersecting family,
number theory, primitive sets.
