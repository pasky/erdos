---
name: theory/number_theory/L64_factorial_digit_entropy/_proof
title: Counting all prime factors across the divisor blocks
desc: |
  Small primes cost a sublinear number of bits, while the total bit budget
  permits only O(K/log K) large prime factors across all the blocks.
created: 2026-10-14T08:41:00Z
updated: 2026-10-14T08:41:00Z
---

***

We prove [[theory/number_theory/L64_factorial_digit_entropy/_index|L64]].
Fix $B,C$, write $L=L(K)$, and set $Y=\lceil K L^C\rceil$. For each tuple
of digits, first record which digits are zero. There are at most $2^u$
choices. The product of the positive digits is less than or equal to $2^K$,
since their bit widths sum to at most $K$. Every prime factor is at most
$F\le Y$.

For primes $p\le\sqrt Y$, each exponent in a positive digit is at most
$K$. There are at most $\lfloor\sqrt Y\rfloor$ such primes, without
using a prime-counting theorem. All their exponents across all slots have at
most

$$
(K+1)^{u\lfloor\sqrt Y\rfloor}
$$

possibilities. This overcounts harmlessly, including digits set to zero.

Each prime factor exceeding $\sqrt Y$ contributes more than
$\tfrac12\log_2Y$ bits. The total number of such factors, with
multiplicity and across all slots, is at most

$$
J=\left\lfloor\frac{2K}{\log_2Y}\right\rfloor.
$$

A factor is specified by a prime and its slot, giving at most $uY$ types.
The number of multisets of at most $J$ factors is at most
$\binom{uY+J}{J}$. Finally $x_0$ has at most $2^{b_0}$ choices. Unique
factorization therefore bounds the number of digit tuples, and hence $|S|$,
by

$$
|S|\le
2^{b_0+u}(K+1)^{u\lfloor\sqrt Y\rfloor}
\binom{uY+J}{J}.                                      \tag{1}
$$

For large $K$, $J\asymp K/\log K$. The elementary estimate
$\binom{N+J}{J}\le[e(1+N/J)]^J$ gives, uniformly over the allowed data,

$$
\begin{aligned}
\log_2|S|
&\le b_0+u+u\sqrt Y\log_2(K+1)
  +J\log_2\bigl(e(1+uY/J)\bigr)\\
&=O_{B,C}\left(
\log K+(\log K)^B
 +\sqrt K(\log K)^{B+C/2+1}
 +\frac{K\log\log K}{\log K}\right)
=o(K).
\end{aligned}
$$

This also covers $u=0$, with the binomial factor equal to one. The harmless
rounding of $Y$ changes only constants.

Any probability measure on at most $|S|$ residues has an atom of mass at least
$1/|S|=2^{-o(K)}$. For each fixed $\gamma>0$, this exceeds
$2^{-\gamma K}$ for all sufficiently large $K$, proving the last clause.
The argument concerns these separated digits and their total width; it places
no such bound on arbitrary sums of factorial divisors.
