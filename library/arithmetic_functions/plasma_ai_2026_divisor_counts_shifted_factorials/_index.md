---
name: arithmetic_functions/plasma_ai_2026_divisor_counts_shifted_factorials
title: Divisor counts of shifted factorials
desc: |
  Plasma AI's Lean formalization of the two density questions in Problem 420:
  shifted-factorial divisor ratios are dense in (1, infinity) for every
  nondecreasing shift tending to infinity and eventually at most log n.
license: Apache-2.0
created: 2026-10-20T18:35:14Z
updated: 2026-10-23T17:38:29Z
---

# Divisor counts of shifted factorials

[[arithmetic_functions/_index|..]]

[[arithmetic_functions/plasma_ai_2026_divisor_counts_shifted_factorials/density_theorem|density_theorem]]: For every nondecreasing real shift f tending to infinity and eventually
bounded by log n, every tail of tau((n + floor(f(n)))!)/tau(n!) is dense in
(1, infinity).

[[arithmetic_functions/plasma_ai_2026_divisor_counts_shifted_factorials/evidence/_index|evidence/]]: The retained formalization and the independent build, kernel replay and
statement-fidelity records for the two density questions of Problem 420.

***

Plasma AI, *Erdős Problem 420: divisor counts of shifted factorials*, Lean
formalization in [plasma-ai/erdos-420](https://github.com/plasma-ai/erdos-420).
The examined version is held as
[evidence/assets/erdos_420_formalization.tar.gz](evidence/assets/erdos_420_formalization.tar.gz),
the repository's tree at commit daa3bba1d72b41c80beaa8bb2114590ac2f76c6a
without its `paper/` folder. The
[source tree prepared for publication](https://github.com/plasma-ai/erdos-420/tree/fc06276356c10f03c143aa57d13d6e58d9b8018d)
has the same proof inputs. Acceptance covers the formalization's statements
and kernel proofs. The formalization is released under the Apache License 2.0,
read in the archive's root `LICENSE` on 2026-10-22, whose copyright line is
left as the license's template placeholder. The repository's
`formalization.yaml` credits
Jacob Parish as the formalization's author and records assistance from Claude
Code, model `claude-opus-5-5`, with parallel proof development. The project
claim is attributed to Plasma AI.

The main result is
[[arithmetic_functions/plasma_ai_2026_divisor_counts_shifted_factorials/density_theorem|density for every monotone shift bounded by the logarithm]].
Writing $F(f,n)=\tau((n+\lfloor f(n)\rfloor)!)/\tau(n!)$, it states that
for every nondecreasing $f:\mathbb N\to\mathbb R$ tending to infinity and
satisfying $f(n)\le\log n$ eventually, every tail of $F(f,n)$ is dense in
$(1,\infty)$. The specialization $f(n)=\log n$ answers the other density
question. It does not address divergence for shifts $(\log n)^C$.

## Argument and dependencies

A covering by congruences leaves fixed protected offsets $kb_i$. Maynard's
sieve places primes at sufficiently many corresponding positions $a+b_i$;
the integers $k(a+b_i)$ then each contribute $\log(1+1/k)$ to the
logarithm of the factorial-divisor ratio. A Selberg upper sieve bounds the
weighted contribution of the other offsets, and Maynard's roughness estimate
controls composite protected positions. A sliding window includes prime
positions one at a time. Monotonicity of the shift bounds the number of
positions where its integer part changes, permitting the window to have
constant length throughout this construction.

The covering adapts the argument of
[[factorials_binomials/erdos_1996_number_divisors/theorem_3|Erdős, Graham, Ivić and Pomerance's Theorem 3]].
The formalization supplies its own factorial-divisor comparison in
`Erdos420/DivisorRatio.lean`. It uses neither of the incorrect normal-order
assertions on p. 5 of the 1996 manuscript; the
[[factorials_binomials/erdos_1996_number_divisors/_index|source card]]
explains their failure. This literature correction does not change the
statements or proof inputs covered by the formalization's acceptance.
Maynard's sieve is vendored from PrimeGapsLib
and generalized from its fixed small-prime modulus to a growing modulus;
`vendor/PrimeGapsLib/README.md` records the changed hypotheses and estimates.
The required uniform prime-number estimate in progressions is proved in
`Erdos420/Analytic/PrimesInAP.lean`:

$$
\theta(Y;q,c)=\frac{Y}{\varphi(q)}
  +O\!\left(Y^{15/16}(\log Y)^2\right),\qquad q\le Y,\quad(c,q)=1.
$$

Its analytic input is the Dirichlet part of
[[primes/openai_2026_quasi_riemann_hypothesis_zero_free_half_plane_7_8/theorem_1_1|OpenAI's seven-eighths zero-free theorem]].
That theorem is proved by the vendored OAI library rather than imposed as a
hypothesis of the density statements. The vendored PrimeNumberTheoremAnd and
RellichKondrachov libraries supply additional dependencies; each library's
README records its source and license.

## Formalization and reading coverage

The source pins Lean and Mathlib `v4.35.0-rc4`. `Challenge.lean` states
`Erdos420.erdos_420.parts.iii` and `Erdos420.erdos_420.parts.ii` using
Mathlib alone, with intentional proof holes. `Solution.lean` proves the same
two statements through `Erdos420.FinalAssembly`. The two versions define
`F` using natural floor, factorial, and the cardinality of the natural-number
divisor finset. The comparison configuration permits only `propext`,
`Classical.choice` and `Quot.sound`.

Read status: claims checked in `Challenge.lean`, `Erdos420/Statement.lean`
and `Solution.lean`; the mathematical construction and selected proof
interfaces were read, without independent reconstruction of the full prose
proof. This corpus accepted the two density results on
2026-10-20, following a fresh project rebuild with checked vendored dependency
caches, Comparator,
complete empty-environment kernel replays and a graded independent
statement-fidelity examination. The
[[arithmetic_functions/plasma_ai_2026_divisor_counts_shifted_factorials/evidence/_index|evidence]]
records their scope and the grader's immaterial-exposure ruling. Only the
three standard Lean axioms occur, and no native claim tier is assigned.

A byte comparison on 2026-10-21 checked all 3,211 files in the held archive
against the linked publication source. All 3,208 files other than `.gitignore`,
`README.md` and `formalization.yaml` agree exactly, including every Lean source,
`comparator.json`, the toolchain and Lake files, and all vendored inputs.
The differences are the research-folder ignore rule, the README blueprint
link, and source metadata recording the completed review and valid
source-relationship values. The publication source also includes
`blueprint/proof.md`, a module-by-module explanation of the formal proof.
This exposition has not undergone the independent examinations recorded here.
The README's informal approximation of $\log F$ by $\sum P(x)/x$ does not
preserve density values: the one-step main terms must remain
$\log(1+P(x)/x)$. For example, at a prime $x$ the term is $\log 2$, not $1$.
The blueprint and the Lean factorial comparison retain the logarithmic terms.
The retained replay and statement reviews therefore apply to the same
mathematical inputs; the archive preserves the exact input
used for those examinations.

## Bears on

- [[../wiki/problems/arithmetic_functions/E0420/_index|Problem 420]]:
  the two density questions, recorded in
  [[../wiki/problems/arithmetic_functions/E0420/claims/2026_10_23_plasma_ai|the partial claim]].
