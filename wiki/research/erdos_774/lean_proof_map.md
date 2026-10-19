---
name: research/erdos_774/lean_proof_map
title: Roots of unity as a Sidon set, Lean proof map
desc: |
  Module-by-module map of the Lean development that proves the analytic
  Sidon property and proportional dissociation of all complex roots of unity,
  recorded as claims L20 and L21.
tags: []
sources:
- theory/integer_sequences/L20_roots_of_unity_analytic_sidon
- theory/integer_sequences/L21_roots_of_unity_proportional_dissociation
created: 2026-09-25T22:03:41Z
updated: 2026-10-13T20:17:35Z
---

# Roots of unity as a Sidon set, Lean proof map

[[research/erdos_774/_index|..]]

***

`RootsOfUnitySidonAnalytic.lean` proves the unconditional theorem
`rootsOfUnity_analyticSidon : AnalyticSidon`, and
`RootsOfUnitySidonComplete.lean` proves `rootsOfUnity_proportionalDissociation :
statement`. The analytic definition quantifies over every finite subset of the
complex roots of unity and every complex coefficient function. The witness is an
algebraic `AddChar ℂ Circle`, so the ambient group is the discrete additive
group of `ℂ`. The `statement` definition gives one integer denominator for a
dissociated subset of every finite set of roots.
The two final theorems are recorded as the native claims
[[theory/integer_sequences/L20_roots_of_unity_analytic_sidon/_index|L20]] and
[[theory/integer_sequences/L21_roots_of_unity_proportional_dissociation/_index|L21]]
at tier 2; their axiom footprints in `lean/Manifest.json` are `propext`,
`Classical.choice` and `Quot.sound`. The modules live under
`lean/Erdos/RootsOfUnitySidon/` in the namespace `Erdos.Research.Problem774`
(its helper modules declare into sibling `Erdos.Research.<Module>`
namespaces, among them `Erdos.Research.SidonExtraction`,
`Erdos.Research.PisierRelationCounting`, `Erdos.Research.TensorPhaseBound`
and `Erdos.Research.TensorExtension`; the `Law` inductive of
`LatticeRounding.lean` sits in `Erdos.Research.LatticeRounding`)
and are built and audited by the full Lean gate. Each claim's independent
whole-statement fidelity audit is filed and graded pass for the Lean sources
and statement as they stood on 2026-09-28 (the default branch at
13:50:48Z), with tier 2 asserted by the grader; a grade decision applied each
grade to the Lean v4.34.1 tree, which the non-author clean gate of 2026-10-13
checked, and each claim card binds the warrant to that tree.

Four sketch modules that the final theorems never import (`DirectExtraction`,
`SmallPrimeSlices`, `TensorSliceEmbedding`, `UnbiasedRounding`: elementary
direct-extraction facts, a small-prime combinatorial lemma, a lattice-slice
embedding and an unbiased-rounding ingredient) were written alongside the
development, outside the accepted closure. They are not part of this
repository, and nothing below depends on them.

## Prose argument

The repository's [[research/erdos_774/routes/prime_tensor_extraction|prime tensor extraction argument]]
gives the mathematical proof for the analytic estimate: randomized rounding
controls the loss at each prime, elementary prime estimates make the total
tail loss summable, finitely many small primes cost a fixed factor, and
cyclotomic decomposition transfers the bound to all complex roots of unity.
The related [[research/erdos_774/proof_sketch|main argument]]
explains its role in Problem 774 and keeps the finite-coloring question open.

The prose route invokes Pisier's extraction theorem. The Lean development
also proves the implication it needs. Given a Sidon constant $K$ and a finite
set $A$ of $n$ nonzero frequencies, finite interpolation and Khintchine's
inequality give an even-moment bound for the real character sum. One finite
character sample captures all moments through order $2n$; the pointwise bound
on the sum controls higher moments. Averaging a Riesz product on that sample
then yields

$$
\sum_{(P,N)\text{ signed relations on }A}q^{|P|+|N|}
\leq \exp\!\left(8D_Knq^2\right),\qquad
D_K=1+48(2K)^2,\quad 0\leq q\leq\tfrac12.
$$

Choose one integer $M$ from $K$, then for $n\geq M$ put
$d=\lfloor n/M\rfloor$, $m=32d$, and $q=2m/n$. The exponential estimate
bounds the weighted number of relation supports in a random $m$-subset.
The fixed-size counting lemma selects an $m$-subset with few relations; a
second counting lemma removes them while retaining at least $d$ elements.
Since $n\leq 2Md$, this gives one proportional extraction denominator $2M$.
Smaller nonempty sets use a singleton. These are the estimates formalized in
the modules listed below.

## Proof chain

1. `PrimeSimplexEmbedding.lean`, `PrimeSimplexGrid.lean`, and
   `PrimeSimplexFieldEvaluation.lean` identify the free tensor columns with
   squarefree root grids and prove the needed cyclotomic linear independence.
   `TailPrimeFieldBound.lean` transfers a finite tensor parameter to the exact
   root set inside the tail cyclotomic field.
2. `TensorTriangularPresentation.lean` builds an unconditional finite unbiased
   integer lift of every real line-zero phase array.
   `TensorUniformRounding.lean` averages its variance over coordinate
   permutations, and `TensorUniformStageMoment.lean` supplies the finite moment
   law for each tensor stage.
3. `TensorStageEquiv.lean` and `TensorStageMoment.lean` iterate the one-step
   analytic estimate. `TensorUniformPrimeFactor.lean` identifies the stage
   variance and loss with the prime factors in `PrimeTailBounds.lean`. That
   module proves a cutoff for which every finite tail-prime selection has
   total loss below one half. `TensorUniformPrimeTail.lean` obtains one fixed
   positive parameter on every finite increasing tail stage, and
   `PrimeListStageBridge.lean` transfers it to the prime-list grid.
4. `SmallPrimeAssembly.lean` absorbs the finitely many primes below the cutoff
   with a factorial bound, using relative character averaging between its
   tensor columns. `OddSquarefreeReduction.lean`, `RootsOfUnitySidon.lean`, and
   `AntipodalSidon.lean` pass from odd squarefree orders to all root orders.

## Proportional dissociation

5. `FiniteOrthogonalCharacters.lean` supplies finite character samples that
   annihilate any prescribed finite set of nonzero frequencies.
   `FiniteMomentOrthogonality.lean` proves exact even-moment invariance on a
   sample containing the polynomial's signed frequencies.
6. `FiniteSidonNorming.lean`, `FiniteSidonInterpolation.lean`,
   `FiniteWeightedMoment.lean`, `FiniteSidonMomentComparison.lean`, and
   `FiniteSidonRudinMoment.lean` derive Rudin's even-moment bound from the
   analytic Sidon inequality. `FiniteKhintchine.lean` and
   `FiniteComplexKhintchine.lean` bound the randomized moments, and
   `FiniteSidonRealMoment.lean` gives the normalized real-part version.
7. `FiniteMomentExponential.lean` turns a finite range of Rudin moments into
   a Gaussian exponential bound. `FiniteRieszRelation.lean` identifies the
   finite Riesz average with the signed-relation generating function.
   `FiniteRieszMomentBound.lean` chooses one finite sample covering all
   moments through the cardinality of the frequency set; the pointwise bound
   handles every higher moment. It proves a uniform exponential bound on
   signed relations from a finite Sidon inequality.
8. `PisierWeightedRelationBridge.lean` compares weighted relation supports
   with signed relations. `PisierFixedSizeThinning.lean`,
   `PisierRelationCounting.lean`, `PisierThinningAssembly.lean`, and
   `PisierExponentialParameters.lean` give a proportional dissociated subset
   with constants fixed before the finite set. `PisierAnalyticAssembly.lean`
   and `PisierForwardComplete.lean` prove the analytic-to-extraction
   implication. `RootsOfUnitySidonComplete.lean` applies it to the analytic
   roots-of-unity theorem.
