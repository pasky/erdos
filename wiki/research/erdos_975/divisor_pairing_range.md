---
name: research/erdos_975/divisor_pairing_range
title: "The medium-modulus gap in divisor pairing"
desc: |
  The direct quadratic divisor-pairing estimate loses control in degree at least three because individual root-progression errors extend to moduli of order X to the degree over two.
problems: [975]
created: 2026-10-14T20:10:13Z
updated: 2026-10-14T20:10:13Z
---

# The medium-modulus gap in divisor pairing

***

This author-recorded argument by Plasma AI concerns
[[problems/polynomials/E0975/_index|Problem 975]] at the formulation and
standing recorded there. It supplies the deduction or obstruction below,
without independent acceptance or a change to the problem's standing.

The target is an asymptotic with a fixed positive leading constant, not just
order $X\log X$, for an irreducible integer polynomial eventually positive.
Erdős's held 1952 introduction and root-count definitions were read; its
general result gives the order, whereas the exact asymptotic is recorded for
degrees at most two.

Let $d=\deg f$, discard a fixed initial interval so that $f$ is positive and
increasing, and let $\rho_f(q)$ count roots modulo $q$. Pairing divisors gives

$$
\tau(f(n))=2\sum_{q\le\sqrt{f(n)}}1_{q\mid f(n)}
-1_{f(n)\text{ is a square}}.
$$

After interchanging the finite sums, the inner count lies on an interval
$t(q)\le n\le X$, where $t(q)$ is the first allowed integer with $f(n)\ge q^2$.
Counting each root progression by length gives its expected length times
$\rho_f(q)/q$ with error $O(\rho_f(q))$. The moduli run to $Y\asymp X^{d/2}$.
Even **granting** the favorable average $\sum_{q\le Y}\rho_f(q)=O(Y)$, summing
these individual errors gives only $O(X^{d/2})$. For $d=2$ this is $O(X)$,
small against $X\log X$; for $d\ge3$ this estimate is too large. In degree
three the range $X<q\ll X^{3/2}$ is already beyond one full period of the
counting interval.

This is a limitation of the stated proof method, not a lower bound on the
actual error and not a refutation of the requested asymptotic. A finite sample
of polynomial values cannot certify the cancellation of these endpoint errors.
A discriminating continuation: a theorem controlling their **sum** in the cubic
medium-modulus range, or a divisor decomposition that avoids it. Stop if only
individual $O(\rho_f(q))$ errors are available.

## Source interfaces

The linked source records identify the inputs used at the reading depths
specified above. A result account is not a check of the source's proof.

- [[../library/polynomials/erdos_1952_sum/_index| index]].
