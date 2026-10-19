---
name: diophantine_problems/ulas_2013_note_erdos_straus_erdos_graham/theorem_a_2
title: Schinzel Theorem A.2 — powers of ak + b dividing C(2k, k), with a gap in the printed proof
desc: >
  States that for gcd(a, b) = 1 and every n infinitely many k have
  (ak+b)^n | C(2k, k); the printed proof omits the factor p - 1 of Legendre's
  formula, so it establishes only the exponent one, and not even that when
  a = 2 and b > 0.
created: 2026-10-14T23:03:05Z
updated: 2026-10-14T23:03:05Z
---

***

**Source.** Published pp. 597–598, Appendix A by A. Schinzel, Theorem A.2,
with its proof and Remark A.3.

**Statement as printed.** If $a\ge1$ and $b$ are coprime integers (the
condition (A.1) of the appendix), then for every $n$ there are infinitely
many positive integers $k$ with

$$
(ak+b)^n\mid\binom{2k}{k}.
$$

The proof takes $n$ to be a positive integer. This page does not record the
statement as proved: the printed proof has the gap described below.

**The printed proof.** It reduces the claim to one $k$ for each $n$ and
treats four cases: $a=1$, $b>0$; $a=1$, $b<0$; $a=2$; and $a>2$, noting that
the construction for $a>2$ also works for $a=2$, $b<0$. In each case it
chooses primes and a $k$ for which $ak+b$ is $p$, $pq$ or $p^2q$, computes
$2s_\ell(k)-s_\ell(2k)$ for each prime $\ell$ dividing $ak+b$, where $s_\ell$
is the base-$\ell$ digit sum, and compares the value with $n$, or with $2n$
or $6n$ in the case $a=2$. The value is $\ell-1$ in every case except at $p$
when $a=2$ and $b<0$, where it is $3p-3$.

**The gap.** By Legendre's formula
$\nu_\ell\binom{2k}{k}=(2s_\ell(k)-s_\ell(2k))/(\ell-1)$, and the paper's own
Theorem 4.3 (p. 596) states the criterion with that factor:
$f(k)\mid\binom{2k}{k}$ if and only if
$2s_\ell(k)-s_\ell(2k)\ge(\ell-1)\nu_\ell(f(k))$ for every prime $\ell$
dividing $f(k)$. The constructions therefore give $\nu_\ell\binom{2k}{k}=1$
at every prime $\ell$ dividing $ak+b$, except $\nu_p\binom{2k}{k}=3$ when
$a=2$ and $b<0$. But $(ak+b)^n$ has valuation $n\,\nu_\ell(ak+b)\ge n$ at
$\ell$, and $2n$ at $p$ when $a=2$. So the chosen $k$ satisfy the
divisibility only for $n=1$, and when $a=2$ and $b>0$ not even then, since
there $p^2$ divides $2k+b$ while $p$ divides $\binom{2k}{k}$ only once. Two
instances, worked by hand for this page:

- $a=b=1$, $n=2$ and $p=5$: the case $a=1$, $b>0$ takes $k=p-b=4$, and
  $(k+1)^2=25$ does not divide $\binom84=70$.
- $a=2$, $b=1$, $n=1$, $p=11$ and $q=13$: the case $a=2$ takes
  $k=(p^2q-b)/2=786$, whose base-$11$ digits are $6,5,5$. Adding $786$ to
  itself in base $11$ makes one carry, so $11$ divides $\binom{1572}{786}$
  once, while $11^2$ divides $2k+1=1573$.

What the printed argument establishes is the exponent one: for coprime $a$
and $b$ outside the case $a=2$, $b>0$, infinitely many $k$ have
$ak+b\mid\binom{2k}{k}$. The pair $a=1$, $b=0$, which the condition admits,
falls in none of the four cases; at the exponent one it is
[[diophantine_problems/ulas_2013_note_erdos_straus_erdos_graham/theorem_3_2|Theorem 3.2]].
Whether the stated theorem holds for $n\ge2$, and in the case $a=2$, $b>0$
at all, is not settled by the paper, and this page makes no claim either way.

**Smaller slips.** In the case $a=1$, $b<0$ the prime needs $p>-2b$, not
$p>2b$, for $-b$ and $-2b$ to be base-$p$ digits. In the case $a>2$ the
base-$q$ digits printed for $k$ and $2k$ are off: the leading digit of $k$
is $(p-a+1)/a$, and the last digit of $2k$ is $((a-2)q-2b)/a$. Neither
changes the computed value $q-1$.

**Remark A.3** (p. 598) says that bounds for the number of $k$ with
$p^a\nmid\binom{2k}{k}$, cited from Sander, together with lower bounds for
the number of $k$ the proof constructs, would remove the condition
$\gcd(a,b)=1$ except when $a=2\gcd(a,b)$ and $b>0$. It rests on the same
constructions.

**Dependencies.** Legendre's formula; the criterion of Theorem 4.3
(p. 596); primes $p<q<p+p^{1/2}$ in the case $a=2$, for which the print cites
Goldston and Graham; primes in residue classes in the case $a>2$.

**Read depth.** Claims checked: the statement, the four cases of the proof
and Remark A.3 were read clause by clause on the page images, and each
case's digit computation was followed; the gap was found in that reading.
Nothing here is independently reviewed.

**Bears on.** [[../wiki/problems/factorials_binomials/E0396/_index|#396]]:
an analogue only. The divisibility here concerns a power of one linear
factor, not a product of consecutive factors, so even as stated it settles
no instance of the problem with $k\ge1$. At the exponent one with $a=1$ it
is the single-factor divisibility that Theorems 2 and 3 of
[[factorials_binomials/pomerance_2015_divisors_middle_binomial_coefficient/_index|Pomerance's 2015 paper]]
treat.
