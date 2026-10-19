---
name: primes/montgomery_vaughan_2006_multiplicative_number_theory_i/theorem_3_9
title: Brun–Titchmarsh on the domain y at least 2q
desc: |
  Theorem 3.9 and its historical note give the error-free upper bound
  2y/(phi(q) log(y/q)) for primes in a reduced residue class in an interval
  of length y>=2q; only that domain and the statement are extracted.
tags: []
sources: []
created: 2026-10-16T21:06:06Z
updated: 2026-10-16T21:06:06Z
---

***

In the Chapter 3 artifact identified on the
[[primes/montgomery_vaughan_2006_multiplicative_number_theory_i/_index|source card]],
Theorem 3.9 is on printed p. 90 and the error-free sharpening is stated
in Section 3.5's notes on Section 3.3, printed p. 102.

Let $q\ge1$ be an integer, let $a\in\mathbb Z$ satisfy $(a,q)=1$, and let
$x,y$ be real with $x\ge0$ and $y\ge2q$. If $\pi(t;q,a)$ counts primes
$p\le t$ with $p\equiv a\pmod q$, then

$$
\pi(x+y;q,a)-\pi(x;q,a)
\le \frac{2y}{\varphi(q)\log(y/q)}.
$$

Theorem 3.9 itself includes a relative error factor. The notes state that
this factor can be omitted and attribute the sharpening to Montgomery and
Vaughan (1973). The error-bearing proof begins on p. 90 and continues on
p. 91; the original 1973 proof has not been examined here. The extracted
error-free assertion is claims checked, not proof verified.

Taking $x=0$ covers $y=t\ge q^2$ when $q\ge2$, and covers $q=1$, $t\ge3$.
The condition $(a,q)=1$ must still be checked in every such application.
The empty modulus product $q=1$ causes no exception to the displayed bound.

**Bears on.**
[[../wiki/problems/integer_sequences/E0012/_index|Problem 12(iii)]]:
this is an analytic input for prime-class reciprocal estimates, not a
bound for the total reciprocal mass of a set with property P. No
normalization induction or answer to Problem 12 follows from this statement
alone.
