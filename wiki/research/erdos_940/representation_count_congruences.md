---
name: research/erdos_940/representation_count_congruences
title: Divisibility of unordered representation counts
desc: A count-divisibility criterion would bypass a first-moment floor, but Frobenius, prime-adic layers, and fixed-prime valuation actions do not supply its arithmetic hypothesis.
tags: []
sources: []
created: 2026-09-23T02:31:19Z
updated: 2026-09-23T02:31:19Z
---


# Divisibility of unordered representation counts

***

## Status

This was the last new approach attempted. The criterion, formal identities, and
counting estimates below are proved. **No required congruence for representation
counts was established**, and no target case was resolved. The finite diagnostic
excludes certain universal congruences, not eventual congruences or congruences
with untested moduli.

Write $\mathcal P_r$ for the positive $r$-powerful integers and
$U_r(n)$ for the number of unordered multisets of exactly $r$ members
of $\mathcal P_r$ summing to $n$. This is different from counting
solutions of a congruence in the summand variables.

## A count-divisibility criterion

Fix $M\ge1$ and a residue $a$, and suppose

$$
\limsup_{X\to\infty}\frac M X
\sum_{\substack{n\le X\\n\equiv a\pmod M}}U_r(n)
\le\mu<\infty.
$$

If an integer $m>\mu$ satisfies

$$
m\mid U_r(n)
$$

for all but $o(X)$ members of this progression up to $X$, then

$$
\liminf_{X\to\infty}\frac M X
\#\{n\le X:n\equiv a\pmod M,\ n\notin S_r\}
\ge1-\frac{\mu}{m}>0.                                \tag{1}
$$


Indeed, away from the exceptional targets, every positive $U_r(n)$
is at least $m$. The count of these targets is at most the sum of
$U_r(n)$ divided by $m$. Subtract from $X/M+O(1)$, and then
discard the $O_r(X^{1-1/r})$ targets with shorter representations.
This proves (1).

For fixed $M,a$, the relative mean exists by the previously established
[progression first-moment calculation](generating_function_positivity.md#1-the-exact-boundary-limits).
Thus the missing hypothesis is the count divisibility, not existence of the
mean. Unlike a first-moment deficit, (1) could work with $\mu>1$, including
above the [quintic floor](quintic_first_moment_barrier.md). No $m,M,a$
satisfying its hypotheses was obtained for an unresolved exponent.

## Why Frobenius does not determine the unordered count

For $r=5$, put

$$
A(z)=\sum_{b\in\mathcal P_5}z^b,\qquad
H(t,z)=\prod_{b\in\mathcal P_5}(1-tz^b)^{-1}
      =\sum_{j\ge0}h_j(z)t^j.
$$

All products are formal: each coefficient of $t^jz^n$ involves
finitely many parts. Then $[z^n]h_5=U_5(n)$.

Taking the logarithmic derivative with respect to $t$ gives

$$
jh_j=\sum_{i=1}^j A(z^i)h_{j-i},
\qquad h_0=1.
$$

In particular,

$$
5h_5=\sum_{i=1}^5 A(z^i)h_{5-i}.                     \tag{2}
$$

Reduction modulo five eliminates $h_5$; it does not determine it.
Similarly $A(z)^5\equiv A(z^5)\pmod5$ concerns ordered counts.
Outside the density-zero set of targets with repeated summands, their
factor $5!$ already accounts for this divisibility.

More explicitly, let $e_j(z)$ count subsets of $j$ distinct parts.
The formal relation $H(t,z)\sum_{j\ge0}(-1)^je_j(z)t^j=1$ gives

$$
\begin{aligned}
h_5={}&e_1^5-4e_1^3e_2+3e_1e_2^2+3e_1^2e_3\\
     &-2e_2e_3-2e_1e_4+e_5.                         \tag{3}
\end{aligned}
$$

The coefficient of $e_5$ is one, even after reduction modulo any integer
greater than one. This statement about the universal identity does not assert
algebraic independence of the actual specialized series.

Moreover, $h_5-e_5$ is supported on $O(X^{4/5})$ targets up to
$X$. Any repeated-summand representation is determined by at most
four independent fifth-powerful integers, and
$\#(\mathcal P_5\cap[1,X])=O(X^{1/5})$.
Thus the surviving five-distinct-part count is the density-relevant
unknown, not a lower-order exception that can be discarded.

## Exact prime-adic layers

Fix a prime $p$ and set

$$
B_p=\{b\in\mathcal P_5:p\nmid b\},\qquad
F(t,z)=\prod_{b\in B_p}(1-tz^b)^{-1}
      =\sum_{j\ge0}f_j(z)t^j.
$$

The disjoint decomposition

$$
\mathcal P_5=B_p\ \sqcup\ \bigsqcup_{e\ge5}p^eB_p
$$

gives $H=FT$, where

$$
T(t,z)=\prod_{e\ge5}F(t,z^{p^e})
      =\sum_{j\ge0}\tau_j(z)t^j.
$$

Consequently

$$
h_5=f_5+f_4\tau_1+f_3\tau_2+f_2\tau_3+f_1\tau_4+\tau_5. \tag{4}
$$

The exact recursion

$$
T(t,z)=F(t,z^{p^5})T(t,z^p)
$$

and coefficientwise Frobenius in characteristic $p$ imply

$$
\tau_5-\tau_5^p
=f_5(z^{p^5})
 +\sum_{j=1}^4 f_j(z^{p^5})\tau_{5-j}^{p}.            \tag{5}
$$

Thus the layer recursion retains the unknown $f_5$ rather than
removing it.

The mixed terms in (4) are not negligible. In fact,

$$
B_p(X)\sim c_p X^{1/5},\qquad
c_p=(1-p^{-1})
\sum_{\substack{d\in\mathcal C_5\\p\nmid d}}d^{-1/5}>0.
$$

To see this, use the canonical decomposition $dx^5$, require $p\nmid d,x$,
and apply dominated convergence with the convergent core weights. The same
simplex counting argument as in the
[tuple asymptotic](finite_core_reduction.md#unrestricted-tuple-counting-has-a-growing-constant)
then gives, with $\gamma=\Gamma(6/5)$,

$$
\sum_{n\le X}[z^n]f_5(z)
 \sim\frac{c_p^5\gamma^5}{120}X,
$$

whereas

$$
\sum_{n\le X}[z^n]\bigl(f_4(z)f_1(z^{p^5})\bigr)
 \sim\frac{c_p^5\gamma^5}{24p}X.                     \tag{6}
$$

For the second formula, count four ordered $B_p$-parts and one
$p^5B_p$-part. Scaling the last coordinate contributes $1/p$;
divide by $4!$. Tuples with repeated first four parts contribute
only $O(X^{4/5})$, so they do not affect the leading constant.
For $p=5$, the two displayed leading constants are equal.
Discarding the mixed layers would therefore lose critical mass.

## The scope of prime-power carry actions

For a fixed prime $p$ and any fixed $r\ge3$, only
$O_{r,p}(X^{1-1/r})$ targets up to $X$ admit an $r$-term
representation containing two summands with the same $p$-free part.
Indeed, after orienting such a pair, it has the form
$(b,p^kb)$, $k\ge0$. The number of possible pairs is at most

$$
2\sum_{k\ge0}\#(\mathcal P_r\cap[1,X/p^k])
\ll_r X^{1/r}\sum_{k\ge0}p^{-k/r}\ll_{r,p}X^{1/r}.
$$

Choose the other $r-2$ terms freely and sum over the finitely many
positions of the pair.

Outside this exceptional set, every exactly-$r$-term representation
has $r$ distinct $p$-free parts. Ordinary splitting and merging
within a $p$-power tower preserve the total assigned to each
$p$-free part. A final representation with at most $r$ terms
must still have at least one term for each of the original $r$
parts; hence it has exactly one for each, with the same value as
before. Such carries supply no nontrivial orbit, even if intermediate
partitions are allowed more terms.

There is also a bound for fixed-prime valuation changes that are not
required to preserve each tower's total. Fix a finite prime set $S$.
Count ordered source tuples $(a_1,\ldots,a_r)\in\mathcal P_r^r$
with total at most $X$, for which a distinct matched tuple
$(a'_1,\ldots,a'_r)$ has the same total and all ratios
$c_i=a'_i/a_i$ supported on $S$. There are at most

$$
O_{r,S}\bigl((1+\log X)^{r|S|}\bigr)
$$

possible ratio vectors, since every prime valuation difference lies
between $-\log_pX$ and $\log_pX$. For a nonidentity vector,

$$
\sum_i(c_i-1)a_i=0
$$

determines one $a_i$ after the other $r-1$ are fixed. The source
count is therefore

$$
O_{r,S}\bigl(X^{1-1/r}(1+\log X)^{r|S|}\bigr)=o(X).   \tag{7}
$$

Allowing coordinate matchings costs only a factor $r!$.
These estimates exclude extra generic multiplicity from the specified
fixed-prime actions. They do not exclude actions changing the
prime-free parts, or involving a prime set growing with $X$.

## The bounded diagnostic and its exact limitation

A single exact dynamic-programming calculation, with $X=100000$,
was run once. The
[preserved script](evidence/util/representation_count_congruences.py)
lists the fifth-powerful parts and counts unordered exactly-five-part
representations; rerun it to reproduce the computation.

There are 32 allowed parts up to this bound. The computation found

$$
\max_{n\le X}U_5(n)=31,\qquad
\sum_{n\le X}U_5(n)=157125.
$$

For each pair $(M,\ell)$ below, every residue class modulo $M$
contains a tested $n$ with $U_5(n)\not\equiv0\pmod\ell$:

| Target modulus $M$ | Count modulus $\ell$ | Minimum, over classes, of the largest witness |
|---:|---:|---:|
| 8 | 2 | 99973 |
| 32 | 2 | 99803 |
| 25 | 5 | 99881 |
| 125 | 5 | 99480 |
| 49 | 7 | 99882 |
| 121 | 11 | 99503 |

Every prime factor of a fifth-powerful number at most $100000$
belongs to $\{2,3,5,7\}$, since $11^5>100000$. Enumerating
exponent zero or exponents at least five therefore gives the complete
part list. Processing each part once, with part count increasing from
one to five, gives the usual unordered-partition recurrence and permits
repetitions. Every intermediate count is bounded by
$\binom{36}{5}<2^{63}$, so the signed 64-bit arithmetic cannot
overflow.

These witnesses disprove a congruence $U_5(n)\equiv0\pmod\ell$
holding for every positive $n$ in any one of these residue classes.
They do **not** exclude a congruence beginning after a larger threshold,
nor anything for an untested modulus.

## Remaining gap

Neither the formal identities nor the tested valuation actions establish
the arithmetic hypothesis of (1). An action coupling different
prime-free parts, or a different theorem on the actual count coefficients,
would be additional input; neither has been found. This is only a
provisional possibility, not an established next step.
The density questions and complement infinitude for $r\ge5$ remain
unresolved.
