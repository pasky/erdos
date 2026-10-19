---
name: arithmetic_functions/plasma_ai_2026_normal_order_number_iterations_euler_s_function
desc: |
  Plasma AI's 2026 preprint and Lean formalization proving that the number of
  iterations of Euler's function needed to reach $1$ has normal order
  $\alpha\log n$ for a constant $\alpha\in[1/\log3,1/\log2]$, with a variance
  bound, answering the first two questions of Problem 408 unconditionally; the
  proof replaces the Elliott--Halberstam-type hypothesis of Erdős, Granville,
  Pomerance and Spiro by shifted-prime estimates from OpenAI's zero-free
  half-plane and weighted-dilation-graph manuscripts.
license: Apache-2.0
created: 2026-10-14T20:20:13Z
updated: 2026-10-19T07:23:34Z
---

# arithmetic_functions/plasma_ai_2026_normal_order_number_iterations_euler_s_function

[[arithmetic_functions/_index|..]]

[[arithmetic_functions/plasma_ai_2026_normal_order_number_iterations_euler_s_function/evidence/_index|evidence/]]: The held Lean formalization of Plasma AI's Problem 408 preprint, as the
repository's tree at its pinned commit without the paper, and this corpus's
verification records of it.

[[arithmetic_functions/plasma_ai_2026_normal_order_number_iterations_euler_s_function/theorem_1_1|theorem_1_1]]: The number $f(n)$ of iterations of Euler's function needed to reach $1$ has
normal order $\alpha\log n$ for a constant $\alpha\in[1/\log3,1/\log2]$:
the variance about $\alpha\log n$ up to $x$ is
$O(x(\log x)^2/(\log\log x)^5)$, so $f(n)/\log n\to\alpha$ on a set of
natural density one; its Lean formalization is rebuilt and kernel-replayed
here.

***

Plasma AI, *The normal order of the number of iterations of Euler's function*,
preprint, October 14, 2026, with its Lean formalization, in the repository
[plasma-ai/erdos-408](https://github.com/plasma-ai/erdos-408) at
[4ea44bf](https://github.com/plasma-ai/erdos-408/tree/4ea44bf911f8668aec10ec25c4b309e8ed476666)
(2026-10-19 UTC). The paper is
[`paper/totient_iterates.pdf`](https://github.com/plasma-ai/erdos-408/blob/5b02bf9ab59fd813af8f19c604ba70254fced08d/paper/totient_iterates.pdf),
posted at commit 5b02bf9 (2026-10-14) and unchanged since, with its TeX source
beside it; the held PDF is retained as
[plasma_ai_2026_normal_order_number_iterations_euler_s_function.pdf](plasma_ai_2026_normal_order_number_iterations_euler_s_function.pdf).
The repository is released under the Apache License 2.0, read in its root
`LICENSE` at commit 4ea44bf on 2026-10-19, whose copyright line is left as the
license's template placeholder; the paper carries no license or copyright
statement of its own and is held under the repository's license. The
formalization is held as
[evidence/assets/erdos_408_formalization.tar.gz](evidence/assets/erdos_408_formalization.tar.gz),
the repository's tree at commit 4ea44bf without its `paper/` folder, made by
`git archive 4ea44bf -- . ':(exclude)paper' | gzip -n`. Commit 4ea44bf moves
the development to Lean and Mathlib `v4.35.0-rc3` and to Lean's module system,
adds a Palomar preflight workflow and names a second responsible maintainer;
its `Challenge.lean` and `comparator.json` are byte for byte those of 5b02bf9.

```bibtex
@misc{PlasmaAI:Erdos408,
  author = {{Plasma AI}},
  title = {{The normal order of the number of iterations of Euler's function}},
  howpublished = {Preprint with Lean formalization,
                  \url{https://github.com/plasma-ai/erdos-408}},
  year = {2026}
}
```

The result is credited to Plasma AI, the paper's author line. The
repository's `formalization.yaml` names Jacob Parish as the formalization's
author, Jacob Parish and Andrew Turner as its responsible maintainers, and
records that it was written with Claude Code (model
`claude-opus-5-5`) and parallel subagents.

**The paper.** Section 1 states
[[arithmetic_functions/plasma_ai_2026_normal_order_number_iterations_euler_s_function/theorem_1_1|Theorem 1.1]]:
a constant $\alpha\in[1/\log3,1/\log2]$ with
$\sum_{n\le x}(f(n)-\alpha\log n)^2\ll x(\log x)^2/(\log\log x)^5$, and the
$n\le x$ with $|f(n)-\alpha\log n|>\log n/\log\log n$ numbering
$O(x/(\log\log x)^3+\sqrt x)$, so that $f(n)/\log n\to\alpha$ on a set of
natural density one, answering the first two questions of
[[../wiki/problems/arithmetic_functions/E0408/_index|Problem 408]]. The value
of $\alpha$ is not determined. The paper counts
iterations from $\varphi_0(n)=n$, so its $f(1)=0$. The proof follows the moment
method of
[[arithmetic_functions/erdos_1990_normal_behavior_iterates_arithmetic_functions/_index|Erdős, Granville, Pomerance and Spiro]]:
the completely additive $F$ with $F(2)=1$ and $F(p)=F(p-1)$ satisfies
$|f-F|\le1$, and estimates for the prime factors of $p-1$ relate the first
two moments of $F$ over primes to harmonic sums of its prime values. Their
Elliott--Halberstam-type hypothesis is replaced by Theorem 2.1, a quantitative
rectangle estimate for tuples of prime factors of $p-1$ with bounded weights
and an explicit error, which extends Theorem 7.1 of OpenAI's
[[arithmetic_functions/openai_2026_poisson_dirichlet_law_prime_predecessors/_index|Poisson--Dirichlet manuscript]]
and rests on the zero-free half-plane of
[[primes/openai_2026_quasi_riemann_hypothesis_zero_free_half_plane_7_8/_index|OpenAI's Quasi-Riemann Hypothesis manuscript]]
and the graph arguments of its
[[arithmetic_functions/openai_2026_weighted_dilation_graphs_smooth_shifted_primes_totient_fibers/_index|weighted-dilation-graph manuscript]].
Section 3 sums over an auxiliary prime factor, Sections 4--5 deduce the prime
moments and the normal order, and Section 6 outlines the proof of the
rectangle estimate. On the third question of Problem 408, Section 7 records a
consequence of Ford, Konyagin and Luca (2010, Theorem 5): for every
integer-valued $k(n)\to\infty$, the largest prime factor of
$\varphi_{k(n)}(n)$ is $n^{o(1)}$ on a set of natural density one.

**The formalization.** Lean 4 at `v4.35.0-rc3` with Mathlib `v4.35.0-rc3`.
`Challenge.lean` states three theorems with deliberate `sorry` bodies:
`Erdos408.normal_order_rate`, Theorem 1.1's two bounds, and
`erdos_408.parts.i` and `erdos_408.parts.ii`, the first two questions as
formal-conjectures states them at its commit of 2026-10-14, with `f` copied
verbatim and formal-conjectures' `Set.HasDensity` inlined relative to all of
$\mathbb N$. `Solution.lean` proves the three through the development
`Erdos408/` (274 files), with vendored copies, each under the Apache License
2.0 with its provenance recorded, of OpenAI's Lean proof of the zero-free
half-plane (`openai/math`), Yao Xu's `totient-fibers-lean4` for the
weighted-dilation-graph results, and code from `PrimeNumberTheoremAnd` and
`rellich-kondrachov`. `comparator.json` permits only the axioms `propext`,
`Quot.sound` and `Classical.choice`. The repository's README and the
`blueprint/` folder write up the method in prose, module by module.

Attestation, recorded as the source's own statements and not as this
corpus's review: `formalization.yaml` gives the review status as
self-assessed, a `sorry` count of zero and the three standard axioms, and
records that its Comparator check, run with the toolchain's `lake comparator`,
accepted the three theorems with the Lean, NanoDa and con-ron kernels, and in
its paranoid mode also with lean4lean and con-leche, on macOS without
Comparator's sandbox. This corpus rebuilt the formalization in its own
sandbox, checked it with Comparator and replayed its three theorems in the
kernel
([[arithmetic_functions/plasma_ai_2026_normal_order_number_iterations_euler_s_function/evidence/verify/replay_receipt|the replay receipt]]), and its
[[arithmetic_functions/plasma_ai_2026_normal_order_number_iterations_euler_s_function/evidence/verify/statement_fidelity/_index|statement-fidelity audit]]
passed, graded, on 2026-10-14. The paper's own proof is not independently
reviewed.

Read status: claims checked for Theorem 1.1, read clause by clause in the TeX
source (`paper/totient_iterates.tex`, Section 1), and the statements of
`Challenge.lean` read against formal-conjectures'
`FormalConjectures/ErdosProblems/408.lean` and its `Set.HasDensity` at the
commit of 2026-10-14; the proof was not read.

## Methods

The proof combines four inputs, each recorded on its own card or section:

- **The Erdős–Granville–Pomerance–Spiro moment method.** The completely
  additive $F$ with $F(2)=1$ and $F(p)=F(p-1)$ satisfies $|f-F|\le1$ and
  $\log n/\log3\le F(n)\le\log n/\log2$. Since $F(p)=F(p-1)$, the first two
  moments of $F$ over primes satisfy relations through the prime factors of
  $p-1$, and solving them gives the normal order. In
  [[arithmetic_functions/erdos_1990_normal_behavior_iterates_arithmetic_functions/_index|the 1990 paper]]
  ([[arithmetic_functions/erdos_1990_normal_behavior_iterates_arithmetic_functions/theorem_2_2|Theorem 2.2]])
  the relations rest on a strong Elliott–Halberstam hypothesis. Here they rest
  on the next three inputs, so the conclusion holds without it.
- **The quantitative rectangle estimate (Theorem 2.1 of the paper).** For
  $1\le k\le3$ prime intervals $I_i=(x^{u_i},x^{v_i}]$ with
  $u_i\ge c(\log\log x)^{-20}$ and $\sum v_i\le1-c(\log\log x)^{-20}$, and any
  coefficient $b(q_1,\dots,q_{k-1})$ of absolute value at most $1$, the
  average over primes $p\in(x,2x]$ of the sum of $b$ over distinct
  $q_i\in I_i$ with $q_1\cdots q_k\mid p-1$ equals the harmonic sum
  $\sum b/(q_1\cdots q_k)$ up to $O((\log\log x)^{-300})$. It extends
  [[arithmetic_functions/openai_2026_poisson_dirichlet_law_prime_predecessors/theorem_7_1|Theorem 7.1 of the Poisson–Dirichlet manuscript]]
  in two ways: to weights that depend jointly on all but one of the prime
  factors, and to an explicit error near the boundary of the region. Section 3
  of the paper then sums over an auxiliary prime factor, to handle arbitrary
  bounded weights on one or two prime factors.
- **The weighted-dilation-graph transference.** The graph and ideal-kernel
  estimates of
  [[arithmetic_functions/openai_2026_weighted_dilation_graphs_smooth_shifted_primes_totient_fibers/_index|the weighted-dilation-graph manuscript]],
  carried through the Poisson–Dirichlet manuscript's extraction of primes,
  with the changes Section 6 outlines for the weights and the error term.
- **The zero-free half-plane.** The Dirichlet part of
  [[primes/openai_2026_quasi_riemann_hypothesis_zero_free_half_plane_7_8/theorem_1_1|Theorem 1.1 of the Quasi-Riemann Hypothesis manuscript]],
  $\operatorname{Re}s>7/8$, supplies the analytic input to the rectangle
  estimate.

The formalization proves the inputs as it uses them. It vendors Lean proofs of
the half-plane, from `openai/math`, and of the weighted-dilation-graph
results, from `totient-fibers-lean4`. Extensions of the Poisson–Dirichlet
manuscript's Theorems 3.1 and 6.1 are proved inside `Erdos408/`.

## Bears on

Every row below except the first records an inference drawn on this card. The
paper does not state them, nothing here is verified, and each page's status
rests on its own acceptance evidence.

- [[../wiki/problems/arithmetic_functions/E0408/_index|Problem 408]]: the
  resolution of the first two questions,
  [[../wiki/problems/arithmetic_functions/E0408/claims/2026_10_14_plasma_ai|its claim page]],
  accepted on this corpus's replay of the formalization and the graded review
  of its statements. On the third question, the paper's
  Section 7 records the consequence of Ford, Konyagin and Luca (2010,
  [[integer_sequences/ford_2010_prime_chains_pratt_trees/theorem_5|Theorem 5]])
  for $k(n)\to\infty$; it is not part of the claim, and the part it answers is
  open-ended.
- [[arithmetic_functions/erdos_1990_normal_behavior_iterates_arithmetic_functions/theorem_2_1|Theorem 2.1 of the 1990 paper]],
  the average order $\alpha\log n$ of $f$ under hypothesis $A_\epsilon$: this
  follows from Theorem 1.1 without the hypothesis, by Cauchy–Schwarz, since
  $\bigl|\sum_{n\le x}(f(n)-\alpha\log n)\bigr|\le
  \bigl(x\cdot Cx(\log x)^2/(\log\log x)^5\bigr)^{1/2}=O(x\log x/(\log\log x)^{5/2})$.
  The deduction is drawn here.
- [[../wiki/problems/arithmetic_functions/E0417/_index|Problem 417]]: background
  only. Counting totient values rests on the multiplicative structure of the
  shifted primes $p-1$ for the primes $p$ that divide the preimages, as in
  Ford's theorem $V\asymp V'$, which the problem page quotes. The rectangle
  estimate controls the joint divisibility of $p-1$ by prime tuples in
  prescribed ranges, with bounded weights and an explicit error. That is the
  kind of input that comparisons of products of shifted primes use, as in
  section 4 of the
  [[arithmetic_functions/openai_2026_asymptotic_formula_number_totients/_index|asymptotic-formula card]]
  the problem page cites. No deduction is recorded, and nothing here suggests
  that the estimate decides the limit.
- [[../wiki/problems/arithmetic_functions/E0410/_index|Problem 410]],
  [[../wiki/problems/arithmetic_functions/E0412/_index|Problem 412]] and
  [[../wiki/problems/arithmetic_functions/E0955/_index|Problem 955]]: not
  reached. They are statements (iii) and (vi) of the 1990 paper's list on
  p. 169 and its Conjecture 4, which that paper neither proves nor derives from
  its hypotheses. Removing the hypothesis from Theorem 2.2 therefore says
  nothing about them.
