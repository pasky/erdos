---
name: arithmetic_functions/plasma_ai_2026_divisor_counts_shifted_factorials/density_theorem
title: Density of shifted-factorial divisor ratios
desc: |
  For every nondecreasing real shift f tending to infinity and eventually
  bounded by log n, every tail of tau((n + floor(f(n)))!)/tau(n!) is dense in
  (1, infinity).
created: 2026-10-20T18:35:14Z
updated: 2026-10-20T18:35:14Z
---

***

**Source.** The main theorem in the source's `README.md`, stated as
`Erdos420.erdos_420.parts.iii` in `Challenge.lean` and proved in
`Solution.lean` of
[[arithmetic_functions/plasma_ai_2026_divisor_counts_shifted_factorials/_index|Plasma AI's formalization]].
Its specialization to the logarithm is `Erdos420.erdos_420.parts.ii`.

**Statement.** Let $\tau(m)$ count positive divisors of a positive integer
$m$. Let $f:\mathbb N\to\mathbb R$ be nondecreasing, with
$f(n)\to\infty$ and $f(n)\le\log n$ for all sufficiently large $n$.
For every $R>1$, $\varepsilon>0$ and $N\in\mathbb N$, there is $n\ge N$
such that

$$
\left|\frac{\tau((n+\lfloor f(n)\rfloor)!)}{\tau(n!)}-R\right|
 <\varepsilon.
$$

Only sufficiently large $n$, where $f(n)\ge0$, are needed. The Lean
function uses $\max(0,\lfloor f(n)\rfloor)$ to define the shift at every
natural input; this convention leaves the asserted tail density unchanged.
In particular, the values with $f(n)=\log n$ are dense in $(1,\infty)$.
The source states the conclusion as containment of $(1,\infty)$ in the
closure of the set of values, allowing the values themselves to equal $1$.

**Proof pointer.** `Erdos420/FinalAssembly.lean` assembles the protected
covering, prime-producing weights and small-tail estimate through
`Erdos420/GoodAnchor.lean` and `Erdos420/SlabWeights.lean`. The source card
identifies their analytic and sieve dependencies. The final theorem has no
unproved analytic hypothesis.

**Read status.** Claims checked against the formal statements, with an
independently graded statement-fidelity examination; no independent
reconstruction of the prose proof is claimed.

**Standing.** Accepted on 2026-10-20 through the
[[arithmetic_functions/plasma_ai_2026_divisor_counts_shifted_factorials/evidence/verify/replay_receipt|independent rebuild and complete kernel replay]]
and the
[[arithmetic_functions/plasma_ai_2026_divisor_counts_shifted_factorials/evidence/verify/statement_fidelity/_index|graded statement-fidelity examination]].
The rebuild used checked vendored dependency caches; the replay checked the
full proof closures, allowing only the three standard Lean axioms. No native
claim tier is assigned.

**Bears on.**

- [[../wiki/problems/arithmetic_functions/E0420/_index|Problem 420]]:
  settles the logarithmic and general monotone density questions;
  the polylogarithmic divergence question is outside the statement.
