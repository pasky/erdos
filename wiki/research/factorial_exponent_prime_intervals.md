---
name: research/factorial_exponent_prime_intervals
title: Factorial exponents and occupied prime intervals
desc: Exact prime-bin representation of factorial exponent counts and a conditional derivation of the square-root-two-pi asymptotic constant.
problems: [912]
created: 2026-10-14T22:15:30Z
updated: 2026-10-14T22:15:30Z
---

# Factorial exponents and occupied prime intervals

***

Let $h(n)$ count the distinct exponents in the prime factorization of $n!$,
as in [[problems/factorials_binomials/E0912/_index|Problem 912]]. Plasma AI's
following argument gives an exact representation and a conditional asymptotic.
The asserted prime-occupancy law is an unproved premise, not a theorem or a
numerically fitted conclusion.

Legendre's formula gives $v_p(n!)=\sum_{j\ge1}\lfloor n/p^j\rfloor$.
For $p>\sqrt n$ this equals $\lfloor n/p\rfloor$. Put
$m=\lfloor\sqrt n\rfloor$. The values $\lfloor n/j\rfloor$ decrease
strictly for $1\le j\le m+1$: for $j<m$, use $n\ge j(j+1)$; for $j=m$,
split at $n=m(m+1)$ to obtain a drop from at least $m$ to at most $m-1$,
or from at least $m+1$ to at most $m$. The higher-power summands decrease
weakly with $p$, so small-prime valuations are distinct and exceed all
large-prime valuations. The same separation holds for the floor quotients.
Consequently

$$
h(n)=\#\{\lfloor n/p\rfloor:p\le n,\ p\text{ prime}\}.
$$

Equivalently, this counts small primes separately and the occupied bins
$(n/(j+1),n/j]$ containing a prime above $\sqrt n$. Write
$H=\sqrt{n/\log n}$. The small-prime count is
$O(\sqrt n/\log n)=o(H)$. At $j=tH$ for fixed $t>0$, the bin length is
asymptotic to $\log n/t^2$ and its location to $\sqrt{n\log n}/t$.
A Poisson heuristic assigns occupancy $1-e^{-2/t^2}$, but that heuristic
alone proves nothing about these particular intervals.

The precise sufficient premise is that, for every fixed $0<a<b<\infty$,

$$
\frac1H\sum_{aH<j\le bH}
 \mathbf1_{\{(n/(j+1),n/j]\text{ contains a prime}\}}
 \longrightarrow\int_a^b(1-e^{-2/t^2})\,dt.
$$

Here $n$ tends to infinity through every integer. Under this premise the
remaining tails are controlled: $j\le aH$ contributes at most $aH$;
occupied bins with $j>bH$ inject into primes at most $n/(bH)$, whose number
is $(2/b+o(1))H$ by the prime number theorem. Letting $a\downarrow0$ and
$b\to\infty$, and integrating by parts, gives

$$
\frac{h(n)}H\longrightarrow
\int_0^\infty(1-e^{-2/t^2})\,dt=\sqrt{2\pi}.
$$

This is a complete conditional deduction at author standing. The held
[[../library/factorials_binomials/erdos_1982_miscellaneous_problems_number_theory/theorem_1|Erdős order bound]]
gives $h(n)\asymp H$, not the occupancy premise. Its statement and proof
sketch were inspected; no independent source-proof audit is asserted.
A usable advance must control averaged occupancy in this reciprocal
partition at logarithmic interval lengths, with errors summable over the
bins. A usual prime-number-theorem estimate on much longer intervals does
not decide their emptiness.
