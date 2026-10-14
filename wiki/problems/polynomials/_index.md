---
name: problems/polynomials
title: Polynomials
desc: |
  Extremal and approximation problems for polynomials, including coefficient
  and norm bounds, zero distribution, and random polynomials.
created: 2026-09-04T09:17:27Z
updated: 2026-10-12T00:09:36Z
---

# Polynomials

[[problems/_index|..]]

[[problems/polynomials/E0114/_index|E0114/]]: Asks whether, among monic complex
polynomials $p$ of degree $n$, the length of the curve $\{z:|p(z)|=1\}$ is
maximized by $z^n-1$.

[[problems/polynomials/E0115/_index|E0115/]]: Asks whether a monic polynomial
$p$ of degree $n$ with $\{z:|p(z)|\le1\}$ connected has
$|p'(z)|\le(\frac{1}{2}+o(1))n^2$ on that set. Eremenko and Lempert proved it,
and Erdős's exact bound $n^2/2$ fails for every $n$.

[[problems/polynomials/E0116/_index|E0116/]]: Asks whether a monic polynomial
$p$ of degree $n$ with all roots in the unit disc has $|p(z)|<1$ on a set of
area at least $n^{-O(1)}$; proved by Pommerenke (1961), and with area $\gg1/\log
n$ by Krishnapur, Lundberg and Ramachandran.

[[problems/polynomials/E0119/_index|E0119/]]: Asks, for unimodular $z_i$ and
$M_n=\max_{|z|=1}\prod_{i\le n}|z-z_i|$, whether $\limsup M_n=\infty$, whether
$M_n>n^c$ for infinitely many $n$, and whether $\sum_{k\le n}M_k>n^{1+c}$ for
all large $n$, for some $c>0$. The answers are yes, by Wagner, Beck, and Korsky
with GPT 5.6-Pro.

[[problems/polynomials/E0228/_index|E0228/]]: Asks whether, for all large $n$,
some degree-$n$ polynomial $P$ with coefficients $\pm 1$ has $\sqrt{n}\ll\lvert
P(z)\rvert\ll\sqrt{n}$ on $\lvert z\rvert=1$, with constants independent of $z$
and $n$; yes for every $n\ge 2$, by Balister et al. (2020).

[[problems/polynomials/E0230/_index|E0230/]]: Asks whether some $c>0$ gives
$\max_{\lvert z\rvert=1}\lvert P(z)\rvert\ge(1+c)\sqrt{n}$ for every $n\ge 2$
and every $P(z)=\sum_{k=1}^n a_kz^k$ with all $\lvert a_k\rvert=1$.

[[problems/polynomials/E0485/_index|E0485/]]: Asks whether the least number of
terms in $P(x)^2$, over $P\in\mathbb{Q}[x]$ with exactly $k$ nonzero terms,
tends to infinity as $k\to\infty$.

[[problems/polynomials/E0509/_index|E0509/]]: Asks whether, for every monic
nonconstant $f\in\mathbb{C}[z]$, the set $\{z:\lvert f(z)\rvert\le 1\}$ can be
covered by circles whose radii sum to at most $2$.

[[problems/polynomials/E0521/_index|E0521/]]: Asks whether the number $R_n$ of
real roots of a random degree-$n$ polynomial with independent uniform $\pm 1$
coefficients satisfies $R_n/\log n\to 2/\pi$ almost surely.

[[problems/polynomials/E0522/_index|E0522/]]: Asks whether the number $R_n$ of
roots in the closed unit disc of a random degree-$n$ polynomial with independent
uniform $\pm 1$ coefficients satisfies $R_n/(n/2)\to 1$ almost surely.

[[problems/polynomials/E0523/_index|E0523/]]: Asks whether some $C>0$ makes the
maximum on $\lvert z\rvert=1$ of a random degree-$n$ polynomial with independent
uniform $\pm 1$ coefficients equal $(C+o(1))\sqrt{n\log n}$ almost surely.

[[problems/polynomials/E0524/_index|E0524/]]: Asks for the order of magnitude,
for almost all $t\in(0,1)$, of $M_n(t)=\max_{x\in[-1,1]}\lvert\sum_{k\le
n}(-1)^{\epsilon_k(t)}x^k\rvert$, where $\epsilon_k(t)$ are the binary digits of
$t$.

[[problems/polynomials/E0525/_index|E0525/]]: Asks whether all but $o(2^n)$ of
the degree-$n$ polynomials $f$ with $\pm 1$ coefficients have $\lvert
f(z)\rvert<1$ somewhere on $\lvert z\rvert=1$, and how $\min_{\lvert
z\rvert=1}\lvert f(z)\rvert$ behaves.

[[problems/polynomials/E0975/_index|E0975/]]: Asks whether, for an irreducible
nonconstant $f\in\mathbb{Z}[x]$ with $f(n)\ge 1$ for large $n$, there is a
constant $c=c(f)>0$ with $\sum_{n\le X}\tau(f(n))\sim cX\log X$.

[[problems/polynomials/E1039/_index|E1039/]]: Asks how $\rho(f)$, the radius of
the largest disc inside $\{z:\lvert f(z)\rvert<1\}$, behaves for monic $f$ of
degree $n$ with all roots in the closed unit disc, and whether $\rho(f)\gg 1/n$
always holds.

[[problems/polynomials/E1041/_index|E1041/]]: Asks whether every monic
polynomial $f$ with all roots in the open unit disc has a path of length less
than $2$ inside $\{z:\lvert f(z)\rvert<1\}$ joining two of its roots.

[[problems/polynomials/E1114/_index|E1114/]]: Asserts that if the roots
$a_0<\cdots<a_n$ of a real polynomial $f$ form an arithmetic progression, then
the gaps between consecutive zeros of $f'$ increase from the midpoint of
$(a_0,a_n)$ toward the endpoints.

[[problems/polynomials/E1129/_index|E1129/]]: Asks which nodes
$x_1,\ldots,x_n\in[-1,1]$ minimize $\max_{x\in[-1,1]}\sum_k\lvert l_k(x)\rvert$,
where the $l_k$ are the fundamental Lagrange interpolation polynomials.

[[problems/polynomials/E1130/_index|E1130/]]: For nodes
$x_1,\ldots,x_n\in[-1,1]$, let $\Upsilon$ be the least, over the intervals
between consecutive points of $-1,x_1,\ldots,x_n,1$, of the maximum of
$\sum_k\lvert l_k(x)\rvert$ on the interval. Asks whether $\Upsilon\ll\log n$
and which nodes maximize $\Upsilon$.

[[problems/polynomials/E1131/_index|E1131/]]: Asks for the minimum over
$x_1,\ldots,x_n\in[-1,1]$ of $I=\int_{-1}^1\sum_k\lvert l_k(x)\rvert^2\,dx$,
where the $l_k$ are the Lagrange basis polynomials, and whether $\min
I=2-(1+o(1))/n$.

[[problems/polynomials/E1132/_index|E1132/]]: For a sequence of nodes in
$[-1,1]$, let $L_n(x)=\sum_{k\le n}\lvert l_k(x)\rvert$. Asks whether some
$x\in(-1,1)$ has $L_n(x)>\frac{2}{\pi}\log n-O(1)$ for infinitely many $n$, and
whether $\limsup_n L_n(x)/\log n\ge 2/\pi$ for almost all $x$.

[[problems/polynomials/E1133/_index|E1133/]]: Asks whether each $C>0$ has an
$\epsilon>0$ such that, for large $n$ and any $x_1,\ldots,x_n\in[-1,1]$, some
$y_i\in[-1,1]$ give $\max_{[-1,1]}\lvert P\rvert>C$ whenever $\deg
P<(1+\epsilon)n$ and $P(x_i)=y_i$ for at least $(1-\epsilon)n$ values of $i$.

[[problems/polynomials/E1150/_index|E1150/]]: Asks whether some constant $c>0$
makes every polynomial $P$ of large degree $n$ with coefficients $\pm 1$ have
$\max_{\lvert z\rvert=1}\lvert P(z)\rvert>(1+c)\sqrt{n}$; answered no by the
OpenAI release's construction of 2026-09-23.

[[problems/polynomials/E1151/_index|E1151/]]: Asks for a proof that, with
Chebyshev nodes, every closed $A\subseteq[-1,1]$ is the set of limit points of
$\mathcal{L}^nf(x)$ for some continuous $f$, where $\mathcal{L}^nf$ is the
Lagrange interpolation polynomial of degree $n-1$.

[[problems/polynomials/E1152/_index|E1152/]]: Asks whether, for any array of
distinct nodes in $[-1,1]$ and any $\epsilon(n)\to 0$, some continuous $f$ makes
every sequence of interpolants $p_n$ of $f$ with $\deg p_n<(1+\epsilon(n))n$
fail to converge to $f(x)$ for almost all $x$.

[[problems/polynomials/E1153/_index|E1153/]]: Asks whether, for fixed $-1\le
a<b\le 1$, the sum $\lambda(x)=\sum_k\lvert l_k(x)\rvert$ of the fundamental
Lagrange polynomials for $n$ nodes in $[-1,1]$ satisfies
$\max_{x\in[a,b]}\lambda(x)>(\frac{2}{\pi}-o(1))\log n$.

***

Extremal and approximation problems for polynomials, including coefficient and
norm bounds, zero distribution, and random polynomials.

erdosproblems.com tags routed here: analysis, divisors, number theory,
polynomials, probability.
