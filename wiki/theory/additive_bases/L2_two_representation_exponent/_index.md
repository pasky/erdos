---
name: theory/additive_bases/L2_two_representation_exponent
title: A two-representation set with logarithmic exponent 3/7
desc: |
  One infinite positive-integer set has at most two unordered representations
  of every sum and logarithmic lower counting exponent at least 3/7.
tags: []
sources: []
id: L2
statement: |
  There exists one infinite set A of positive integers such that, writing
  A(x)=|A intersect [1,x]| for real x and
  r_A(n)=|{(a,b) in A^2 : a <= b and a+b=n}| for integer n,
  r_A(n) <= 2 for every integer n and
  liminf as x tends to infinity of log A(x)/log x is at least 3/7.
  A diagonal representation a+a is counted once. In particular, this same
  A satisfies A(x) >= x^alpha for every sufficiently large real x, for
  each real alpha < 3/7; the threshold may depend on alpha.
status: proved
tier: 0
depends_on: []
created: 2026-09-08T22:30:28Z
updated: 2026-09-08T22:43:22Z
---

# A two-representation set with logarithmic exponent 3/7

[[theory/additive_bases/_index|..]]

[[theory/additive_bases/L2_two_representation_exponent/_proof|_proof]]: A uniform divisor count for fiber triples and simultaneous shell selection
give one set with lower exponent 3/7 and an encoding-specific zero ratio.

***

For a set $A\subseteq\mathbb Z_{>0}$, define

$$
A(x)=|A\cap[1,x]|,\qquad
r_A(n)=|\{(a,b)\in A^2:a\le b,\ a+b=n\}|.
$$

Thus representations are unordered and a diagonal $a+a$ counts once.

## Statement

There is one infinite set $A\subseteq\mathbb Z_{>0}$ such that

$$
r_A(n)\le2\quad(n\in\mathbb Z),\qquad
\liminf_{x\to\infty}\frac{\log A(x)}{\log x}\ge\frac37.
$$

The limit inferior is over real cutoffs. In particular, for every real
$\alpha<3/7$ this same set satisfies $A(x)\ge x^\alpha$ at every
sufficiently large cutoff. The set is chosen before $\alpha$; only the
threshold depends on $\alpha$.

The [proof](_proof.md) constructs shifted discrete-logarithm digits, bounds
triples in the associated congruence fibers uniformly over pairs of shells,
and chooses an independent subset of each upper shell using every lower
shell at once. It proves the bound between shell cutoffs as well as at them.

## Restricted-encoding zero endpoint ratio

Let $A_0$ be the full ambient label set defined in the proof, before any
selection, with auxiliary primes $q_j$, radix products $B_K$, and
$\gamma=3/7$. At the cutoffs

$$
x_K=(q_{K+1}+1)B_K-1
$$

one has

$$
0\le\frac{A_0(x_K)}{x_K^{3/7}}
\le2^{-(3/7)(4K+1)}\longrightarrow0.
$$

Consequently every subset $S\subseteq A_0$, including the selected $A$,
satisfies $\liminf_{x\to\infty}S(x)/x^{3/7}=0$. This is a consequence
about this particular encoding. It does not preclude a different construction
with an eventual positive constant times $x^{3/7}$.

## Scope and sources

The result bears on [E0158](../../../problems/additive_bases/E0158/_index.md), which
asks about lower density at the square-root scale. The logarithmic exponent
$3/7<1/2$ does not answer that question. No optimality or priority claim is
made here.

The method adapts the mixed-radix construction in Javier Cilleruelo's
[*Infinite Sidon sequences*](../../../../library/additive_bases/cilleruelo_2014_infinite_sidon_sequences/_index.md),
arXiv:1209.0326v2, 15 May 2013, §§2.1–2.2 and Propositions 1–2,
pp. 4–6. The auxiliary-prime intervals and label shells used here differ from
that version. All digital properties needed for this construction are proved
locally. Cilleruelo's theorem is a method relationship, not a premise of L2.

The external theorem inputs are Bertrand's postulate, cyclicity of the
multiplicative group of a prime field, and the prime number theorem, at the
interfaces stated in the proof. The proof supplies the uniform divisor bound,
the congruence and prime-factor arguments, and the finite alteration lemma.
It consumes no native L-claim.

## Current standing

The complete proof and the restricted-encoding consequence are author-recorded
at tier 0. They have not received independent whole-claim acceptance or native
Lean verification. There is no identified gap in the supplied argument, and
there is no mathematical program or computational input to run.

The author check covered the displayed construction, both determinant cases,
the estimates uniform over lower shells, the assembly of the single infinite
set, and the restricted-encoding consequence. Independent acceptance would
require scrutiny of this exact statement, proof, external interfaces, and
named consequence. This record does not claim independently accepted
literature-proof coverage.
