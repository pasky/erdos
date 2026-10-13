---
name: problems/number_theory
title: Other Number Theory
desc: |
  The general number theory problems fitting none of the three themed folders,
  including questions about real numbers, reciprocal sums as points,
  irrational rotations and floor sequences, quadratic residues and character
  sums, and other one-off constructions.
created: 2026-09-04T09:17:27Z
updated: 2026-10-12T23:28:38Z
---

# Other Number Theory

[[problems/_index|..]]

[[problems/number_theory/E0034/_index|E0034/]]: Asks whether every permutation
of $\{1,\ldots,n\}$ has only $o(n^2)$ distinct sums of consecutive terms. False:
Hegyvári's 1986 construction and Konieczny's explicit permutation with at least
$n^2/4$ such sums refute it, and the maximum lies between $0.286n^2$ and
$0.446n^2$.

[[problems/number_theory/E0268/_index|E0268/]]: Asks whether the points
$\bigl(\sum_{n\in A}1/n,\sum_{n\in A}1/(n+1),\sum_{n\in A}1/(n+2)\bigr)$, over
infinite $A\subseteq\mathbb{N}$ with $\sum_{n\in A}1/n<\infty$, contain an open
set.

[[problems/number_theory/E0362/_index|E0362/]]: Asks whether $\ll2^N/N^{3/2}$
subsets of a set of $N$ naturals have sum $t$, and $\ll2^N/N^2$ if their size is
fixed too. Sárközy and Szemerédi proved the first (Stanley found the exact
maximizers), and Halász the second, via a bound on signed sums of $1$-separated
plane vectors in a unit ball.

[[problems/number_theory/E0464/_index|E0464/]]: Asks whether every lacunary
sequence ($n_{k+1}\ge(1+\epsilon)n_k$) has an irrational $\theta$ with $\{\theta
n_k\}$ not dense in $[0,1]$; proved by Pollington and de Mathan. Peres and
Schlag give a separation of order $\epsilon/\log(1/\epsilon)$, and the site's
wording is trivially true.

[[problems/number_theory/E0465/_index|E0465/]]: Asks whether the largest number
$N(X,\delta)$ of points in a disc of radius $X$ with all pairwise distances at
least $\delta$ from the integers is $o(X)$, and even below $X^{1/2+o(1)}$;
proved by Sárközy (the first bound) and Konyagin (the sharp exponent $1/2$).

[[problems/number_theory/E0466/_index|E0466/]]: Asks whether, for some
$\delta>0$, the largest number $N(X,\delta)$ of points in a disc of radius $X$
with all pairwise distances at least $\delta$ from the integers tends to
infinity with $X$. The site misprints the limit variable; Sárközy's power lower
bound proves the corrected statement.

[[problems/number_theory/E0480/_index|E0480/]]: Asks whether every sequence
$x_1,x_2,\ldots$ in $[0,1]$ satisfies
$\inf_n\liminf_{m\to\infty}n|x_{m+n}-x_m|\le5^{-1/2}$; proved by Chung and
Graham with the sharp constant $0.3944\ldots$.

[[problems/number_theory/E0482/_index|E0482/]]: Asks for analogs, for $\sqrt{m}$
and other algebraic numbers, of the Graham–Pollak recurrence
$a_{n+1}=\lfloor\sqrt{2}(a_n+1/2)\rfloor$, whose differences
$a_{2n+1}-2a_{2n-1}$ are the binary digits of $\sqrt{2}$; solved by Stoll's
families for every positive real and every base.

[[problems/number_theory/E0492/_index|E0492/]]: Asks whether, for real
$a_i\to\infty$ with $a_{i+1}/a_i\to1$, the positions of $\alpha n$ in the gaps
$[a_i,a_{i+1})$ are uniformly distributed for almost every $\alpha$; LeVeque's
question, disproved by Schmidt. The site's wording takes integer $a_i$, where
the Davenport–Erdős theorem gives yes.

[[problems/number_theory/E0951/_index|E0951/]]: Asks whether every real sequence
$1<a_1<a_2<\cdots$ whose products $\prod_i a_i^{k_i}$ for different exponent
tuples differ by at least $1$ satisfies $\#\{a_i\le x\}\le\pi(x)$. The
quantifier over $x$ is implicit, and the readings for every $x$ and for all
large $x$ are separate parts.

[[problems/number_theory/E0952/_index|E0952/]]: Asks whether there is an
infinite sequence of distinct Gaussian primes with consecutive terms a bounded
distance apart. This is the Gaussian moat problem, answered negatively by an
accepted 2026 claim with a Lean proof.

[[problems/number_theory/E0963/_index|E0963/]]: Asks to estimate $f(n)$, the
size of the largest dissociated subset guaranteed in any set of $n$ reals, and
in particular whether $f(n)\ge\lfloor\log_2 n\rfloor$.

[[problems/number_theory/E0972/_index|E0972/]]: Asks whether, for irrational
$\alpha>1$, infinitely many primes $p$ have $\lfloor p\alpha\rfloor$ prime;
open. The one-prime statement is classical, and the two-prime statement is known
only for almost all $\alpha$.

[[problems/number_theory/E0981/_index|E0981/]]: Asks whether
$\sum_{p<x}f_\epsilon(p)\sim c_\epsilon x/\log x$, where $f_\epsilon(p)$ is the
least $m$ with $\sum_{n\le N}(\frac{n}{p})<\epsilon N$ for all $N\ge m$. Elliott
(1969) proved it for the two-sided threshold, with the one-sided form covered
only by Elliott's remark.

[[problems/number_theory/E1005/_index|E1005/]]: Asks to estimate $f(n)$, the
largest $d$ such that Farey fractions of order $n$ at most $d$ places apart are
similarly ordered, and whether $f(n)=(c+o(1))n$. Marked solved on Cipollini's
2026 preprint, which gives $c=1/4$, matching van Doorn's upper bound.

[[problems/number_theory/E1096/_index|E1096/]]: Asks whether, for every $q$
slightly above $1$, the gaps between consecutive finite sums of distinct powers
of $q$ tend to $0$; proved by Erdős and Komornik (1998), Akiyama and Komornik
(2013) and Feng (2016), each for a range of $q$.

[[problems/number_theory/E1135/_index|E1135/]]: Asks whether every orbit of the
shortcut Collatz map reaches $1$; open, with verification below $2^{71}$, no
nontrivial cycle with at most $91$ local minima, and Tao's almost-all theorem.
The site adds a caveat on the reported Erdős prize figure.

[[problems/number_theory/E1180/_index|E1180/]]: Asks whether, for each
$\epsilon>0$, every residue modulo every prime $p$ is a sum of boundedly many
inverses of integers up to $p^\epsilon$; proved by Shparlinski, Croot and
Glibichuk, whose bound has order $\epsilon^{-2}$.

***

The general number theory problems fitting none of the three themed folders,
including questions about real numbers, reciprocal sums as points, irrational
rotations and floor sequences, quadratic residues and character sums, and other
one-off constructions.

Site tags routed here: iterated functions, number theory.
