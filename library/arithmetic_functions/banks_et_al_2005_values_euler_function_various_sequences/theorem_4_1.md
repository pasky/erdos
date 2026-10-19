---
name: arithmetic_functions/banks_et_al_2005_values_euler_function_various_sequences/theorem_4_1
title: "Theorem 4.1: exceptional shifted-prime totient values"
desc: |
  An upper bound of x/(log x)^2 times a subpower of log x for primes p
  admitting phi(n)=p-1 with n other than p or 2p.
created: 2026-10-15T05:59:54Z
updated: 2026-10-15T05:59:54Z
---

***

For $x\ge1$, let

$$
\mathcal L(x)=\{p\le x:p\text{ prime},\ \varphi(n)=p-1
\text{ for some positive integer }n\notin\{p,2p\}\}.
$$

**Theorem 4.1.** The
[[arithmetic_functions/banks_et_al_2005_values_euler_function_various_sequences/_index|source]]
proves

$$
|\mathcal L(x)|\ll\frac{x}{(\log x)^2}
\exp\!\left((\kappa+o(1))(\log\log\log x)^2\right)
\qquad(x\to\infty).
$$

Here $\kappa=(2\log(1/\rho))^{-1}=0.8178\ldots$, where
$\rho\in(0,1)$ solves

$$
\sum_{i\ge1}\bigl((i+1)\log(i+1)-i\log i-1\bigr)\rho^i=1.
$$

**Locator and scope.** The definition is on p. 3 and the theorem and proof
on pp. 14--15 of the 25-page author manuscript. These definitions and the
statement are claims checked. The proof separates smooth preimages and
preimages divisible by a large prime square, then uses a two-prime sieve and
a reciprocal sum over distinct totient values; those external estimates were
not reverified here.

**Bears on.** [[../wiki/problems/arithmetic_functions/E0409/_index|Problem 409]]:
the displayed bound is $o(\pi(x))$, since
$(\log\log\log x)^2=o(\log\log x)$. Thus almost every prime has only the
two indicated totient preimages. This is a known source theorem; a basin
conclusion additionally requires the inverse-orbit argument.
[[../wiki/theory/number_theory/L104_shifted_prime_totient_fibers/_index|L104]]
records that elementary deduction at tier 0, using that $2p$ has no
predecessor under $\varphi+1$. It says nothing about each exceptional
prime.
