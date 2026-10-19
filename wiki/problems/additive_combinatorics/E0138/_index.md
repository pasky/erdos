---
name: problems/additive_combinatorics/E0138
title: Problem 138
desc: |
  Asks for better bounds on the van der Waerden number $W(k)$, the least $N$
  such that every two-coloring of $\{1,\ldots,N\}$ has a monochromatic $k$-term
  arithmetic progression, for example a proof that $W(k)^{1/k}\to\infty$.
tags:
- Additive combinatorics
status: solved
claim: proved
parts: [kth_root]
created: 2026-09-04T09:17:27Z
updated: 2026-10-18T10:11:14Z
---

# Problem 138

[[problems/additive_combinatorics/_index|..]]

[[problems/additive_combinatorics/E0138/claims/_index|claims/]]: The 5 claim pages of Problem 138, one per claimant's result; the problem's standing derives from them.

***

**Statement.** Let the van der Waerden number $W(k)$ be such that whenever
$N\geq W(k)$ and $\{1,\ldots,N\}$ is $2$-coloured there must exist a
monochromatic $k$-term arithmetic progression. Improve the bounds for $W(k)$ -
for example, prove that $W(k)^{1/k}\to \infty$.

**Formulation.** The request to improve the bounds is read against the
bounds the erdosproblems.com commentary cites as the current records:
Berlekamp's $W(p+1)\ge p2^p$ for primes $p$ [Be68], Gowers's tower upper bound
[Go01] and Kozik and Shabanov's $W(k)\gg2^k$ [KoSh16]. erdosproblems.com credits
them as the known bounds and labeled the problem OPEN. They are the baseline the
request asks to beat, and they settle none of the questions the problem and
its commentary pose. The formal-conjectures file linked under Formalization
restates Berlekamp's and Gowers's bounds as solved variants
(`erdos_138.variants.prime`, `erdos_138.variants.upper`) with no formal
proof. The example is the part `kth_root`. The request asks only to improve the bounds, with no target, so it is open-ended: it is not a part, and it never blocks the standing.

**Status.** Solved: an accepted partial claim settles the definite part, the
example question, and the open-ended request to improve the bounds does not
block the standing. The further questions that the erdosproblems.com commentary
records from [Er81] are not parts: Google DeepMind's accepted claim settles the
difference question, $W(k+1)-W(k)\to\infty$
([[problems/additive_combinatorics/E0138/claims/2026_04_10_deepmind|its claim page]]),
and the quotient question, $W(k+1)/W(k)\to\infty$, remains open. The
erdosproblems.com label was OPEN (page last edited 2 June 2026).

**Source.** [erdosproblems.com/138](https://www.erdosproblems.com/138), accessed
2026-09-04. Cite as: T. F. Bloom, Erdős Problem #138,
https://www.erdosproblems.com/138.

**References.**

- [Be68] Berlekamp, E. R., A construction for partitions which avoid long
  arithmetic progressions. Canad. Math. Bull. 11 (1968), no. 3, 409-414.
- [Er80] Erdős, Paul, A survey of problems in combinatorial number theory. Ann.
  Discrete Math. (1980), 89-115.
- [Er81] Erdős, P., On the combinatorial problems which I would most like to see
  solved. Combinatorica (1981), 25-42.
- [FoHu26] J. Fox and Z. Hunter, Three-color van der Waerden numbers grow
  super-exponentially. arXiv:2606.02541 (2026).
- [Go01] Gowers, W. T., A new proof of Szemerédi's theorem. Geom. Funct. Anal.
  (2001), 465-588.
- [KoSh16] Kozik, Jakub and Shabanov, Dmitry, Improved algorithms for colorings
  of simple hypergraphs and applications. J. Combin. Theory Ser. B (2016),
  312-332.

**Formalization.** Statement in
[formal-conjectures](https://github.com/google-deepmind/formal-conjectures/blob/3dfd999dfe5a3a1c739d362d3189daf9e08d9fa8/FormalConjectures/ErdosProblems/138.lean)
at its commit of 2026-10-11, linked, which states the example question
$W(k)^{1/k}\to\infty$ as `erdos_138` with a `sorry` body. Until that commit
`erdos_138` had `answer(sorry)`, the category `research open` and no
`formal_proof` attribute; the commit marked it `research solved` with
`answer(True)`, cited the OpenAI release's manuscript and added a `formal_proof`
attribute linking the release's
[`uniform_lower_bound`](https://github.com/openai/math/blob/adc7f1241b42e322a6451854ab7e4b4c146bf78a/lean/OAI/Combinatorics/ProgressionColoring/Main.lean#L12)
at the revision pinned on
[[problems/additive_combinatorics/E0138/claims/2026_09_23_openai|its claim page]].
That declaration states the uniform bound
$W_r(k)>k^{k\lfloor\log_2r\rfloor/100000}$; the limit is the release's
`kthRoot_tendsto` in the same file, and this corpus built both. Two of the
file's variants, $W(k+1)-W(k)\to\infty$ and $W(k)/2^k\to\infty$, are marked
solved with `formal_proof` attributes pointing to Lean files outside the
repository: a proof by the DeepMind prover agent, AlphaProof Nexus (Tsoukalas et
al., Science 2026; arXiv:2605.22763), in a fork of formal-conjectures, and a
Lean proof derived from the Atlas proofs of facebookresearch/atlas-lean. Neither
was built by this corpus, neither is a formalization of the accepted OpenAI
claim under Claims, and each is linked from its claim page.

**Claims.** Five results have claim pages. The OpenAI mathematics release of 23
September 2026 proves $W_r(k)>k^{k\lfloor\log_2r\rfloor/100000}$ for every
$r\ge2$ and every $k$ above an absolute threshold, so $W(k)^{1/k}\to\infty$, the
example question the problem names; the result is accepted as a partial claim on
[[problems/additive_combinatorics/E0138/claims/2026_09_23_openai|its claim page]],
on Lean declarations this corpus built and audited, and the open-ended request
to improve the bounds stays open, with no upper bound touched. The curator's
blog post
[[../library/number_theory/bloom_2026_erdos_problems_openai_proofs/_index|Erdős problems in the OpenAI proofs]]
(8 October 2026) lists the claim, as a claim and not an endorsement, and says
that its proof has been formalized. Google DeepMind's $W(k+1)\ge W(k)+k$, found
by its AlphaProof Nexus system, answers the difference question of [Er81] and is
accepted as a partial claim on the refereed publication of the paper that
reports it
([[problems/additive_combinatorics/E0138/claims/2026_04_10_deepmind|claim page]];
[[../library/additive_combinatorics/tsoukalas_2026_advancing_mathematics_research_ai_driven_formal_proof_search/erdos_138_difference|library page]]).
Three further results on the questions the erdosproblems.com entry records are
claimed on their own pages: Campos, Fox and Schildkraut's lower bound
$W(k)\ge(1-o(1))k2^{k-1}$, which also gives $W(k)/2^k\to\infty$
([[problems/additive_combinatorics/E0138/claims/2026_08_21_campos_fox_schildkraut|claim page]]);
a Lean proof of $W(k)/2^k\to\infty$ in Meta's atlas-lean repository
([[problems/additive_combinatorics/E0138/claims/2026_08_28_meta|claim page]]);
and the notes that Nat Sothanaphan linked from the erdosproblems.com thread on
2026-04-10, written with GPT-5.4 Thinking, which refine the difference bound to
$W_r(k+1)-W_r(k)\ge k+\min(k,F(r))+1$ for $r$ colors with an explicit
$F(r)=\Theta(r\log\log r)$; at $r=2$ this is $W(k+1)-W(k)\ge k+1$
([[problems/additive_combinatorics/E0138/claims/2026_04_10_sothanaphan|claim page]]).
The record bounds named under Formulation have no claim pages; the results that
improve them do. Fox and Hunter's $W_3(k)^{1/k}\ge C^{\log_*k}$ [FoHu26]
concerns three colors, not the problem's two-color number, and has no page.

## Current assessment

The accepted uniform lower bound recorded on the
[[problems/additive_combinatorics/E0138/claims/2026_09_23_openai|OpenAI claim page]]
gives $W(k)^{1/k}>k^{1/100000}$ for all sufficiently large $k$, answering
the displayed root-growth question. This uses the bound at its recorded
standing and does not add a proof examination.

The separate question whether $W(k+1)/W(k)\to\infty$ needs information
comparing adjacent values. Plasma AI's
[[research/arithmetic_construction_interfaces/progression_transfers|formulation check]]
constructs an increasing numerical sequence whose roots and successive
differences tend to infinity but whose consecutive quotients approach one
along a subsequence. Thus neither root growth nor a growing difference
alone supplies that further limit. The example concerns an implication
between numerical properties, not the van der Waerden numbers themselves;
it is author-recorded and unreviewed.
<!-- BEGIN problem library links -->

## Linked library material

These entries are derived from explicit links on library pages. They are
navigation only and do not by themselves record mathematical progress.

- [[../library/additive_combinatorics/berlekamp_1968_construction_partitions_which_avoid_long_arithmetic/_index|berlekamp_1968_construction_partitions_which_avoid_long_arithmetic]]
- [[../library/additive_combinatorics/berlekamp_1968_construction_partitions_which_avoid_long_arithmetic/theorem_1|berlekamp_1968_construction_partitions_which_avoid_long_arithmetic / theorem_1]]
- [[../library/additive_combinatorics/berlekamp_1968_construction_partitions_which_avoid_long_arithmetic/theorem_2|berlekamp_1968_construction_partitions_which_avoid_long_arithmetic / theorem_2]]
- [[../library/additive_combinatorics/erdos_1979_old_new_problems_results_combinatorial_number/_index|erdos_1979_old_new_problems_results_combinatorial_number]]
- [[../library/additive_combinatorics/fox_2026_three_color_van_der_waerden_numbers/_index|fox_2026_three_color_van_der_waerden_numbers]]
- [[../library/additive_combinatorics/kozik_2016_improved_algorithms_colorings_simple_hypergraphs_applications/_index|kozik_2016_improved_algorithms_colorings_simple_hypergraphs_applications]]
- [[../library/additive_combinatorics/kozik_2016_improved_algorithms_colorings_simple_hypergraphs_applications/theorem_1|kozik_2016_improved_algorithms_colorings_simple_hypergraphs_applications / theorem_1]]
- [[../library/additive_combinatorics/kozik_2016_improved_algorithms_colorings_simple_hypergraphs_applications/theorem_2|kozik_2016_improved_algorithms_colorings_simple_hypergraphs_applications / theorem_2]]
- [[../library/additive_combinatorics/openai_2026_quantitative_superexponential_bounds_van_der_waerden_numbers/_index|openai_2026_quantitative_superexponential_bounds_van_der_waerden_numbers]]
- [[../library/additive_combinatorics/openai_2026_quantitative_superexponential_bounds_van_der_waerden_numbers/corollary_7_3|openai_2026_quantitative_superexponential_bounds_van_der_waerden_numbers / corollary_7_3]]
- [[../library/additive_combinatorics/openai_2026_quantitative_superexponential_bounds_van_der_waerden_numbers/theorem_1_1|openai_2026_quantitative_superexponential_bounds_van_der_waerden_numbers / theorem_1_1]]
- [[../library/additive_combinatorics/tsoukalas_2026_advancing_mathematics_research_ai_driven_formal_proof_search/_index|tsoukalas_2026_advancing_mathematics_research_ai_driven_formal_proof_search]]
- [[../library/additive_combinatorics/tsoukalas_2026_advancing_mathematics_research_ai_driven_formal_proof_search/erdos_138_difference|tsoukalas_2026_advancing_mathematics_research_ai_driven_formal_proof_search / erdos_138_difference]]
- [[../library/distance_problems/graham_1994_recent_trends_euclidean_ramsey_theory/_index|graham_1994_recent_trends_euclidean_ramsey_theory]]
- [[../library/distance_problems/graham_1994_recent_trends_euclidean_ramsey_theory/conjecture_p127|graham_1994_recent_trends_euclidean_ramsey_theory / conjecture_p127]]
- [[../library/number_theory/bloom_2026_erdos_problems_openai_proofs/_index|bloom_2026_erdos_problems_openai_proofs]]
- [[../library/ramsey_theory/beck_1980_remark_concerning_arithmetic_progressions/_index|beck_1980_remark_concerning_arithmetic_progressions]]
- [[../library/ramsey_theory/brown_1999_monochromatic_arithmetic_progressions_large_differences/_index|brown_1999_monochromatic_arithmetic_progressions_large_differences]]
- [[../library/ramsey_theory/green_2022_new_lower_bounds_van_der_waerden/_index|green_2022_new_lower_bounds_van_der_waerden]]
- [[../library/ramsey_theory/hunter_2022_improved_lower_bounds_van_der_waerden/_index|hunter_2022_improved_lower_bounds_van_der_waerden]]
- [[../library/ramsey_theory/schoen_2021_subexponential_upper_bound_van_der_waerden/_index|schoen_2021_subexponential_upper_bound_van_der_waerden]]
- [[../library/set_systems/erdos_1981_combinatorial_problems_which_i_would_most/_index|erdos_1981_combinatorial_problems_which_i_would_most]]

<!-- END problem library links -->
