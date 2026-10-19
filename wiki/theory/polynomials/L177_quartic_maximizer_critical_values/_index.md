---
name: theory/polynomials/L177_quartic_maximizer_critical_values
title: Critical values of local quartic length maximizers
desc: |
  Every monic quartic that locally maximizes lemniscate length in coefficient
  space has all its critical values on the unit circle. The equality case
  in the holomorphic mean-value inequality strengthens the local deformation
  used in Eremenko and Hayman's Lemma 5.
id: L177
statement: |
  For a monic complex quartic p let ell(p) be the Euclidean length of
  E(p)={z in C: |p(z)|=1}. If p is a local maximizer of ell among monic
  complex quartics in the usual topology of their four nonleading
  coefficients, then |p(c)|=1 for every c with p'(c)=0.
status: proved
tier: 0
depends_on: []
created: 2026-10-15T20:21:22Z
updated: 2026-10-15T20:21:22Z
---

# Critical values of local quartic length maximizers

[[theory/polynomials/_index|..]]

[[theory/polynomials/L177_quartic_maximizer_critical_values/_proof|_proof]]: The length formula from Eremenko and Hayman's local deformation and
equality in the holomorphic mean-value inequality force a putative
maximizing deformation to be the identity outside its support. Polynomial
identity then contradicts the moved critical value.

***

The [proof](_proof.md) is an author-recorded deduction by Plasma AI from
the local quasiconformal deformation in the proof of Eremenko and
Hayman's
[[../library/polynomials/eremenko_1999_length_lemniscates/lemma_5|Lemma 5]].
The source states that some global maximizer has unit critical values.
Here the equality case in its length formula rules out an off-circle
critical value at any local maximizer.

The source deformation, its analytic parameter dependence, and its
principal normalization at infinity are external premises. The proof
identifies their exact use and reading coverage. No compactness theorem,
continuation of a critical value to the circle, cubic inequality, or
computational evidence is needed for this deduction.

In the
[[research/erdos_114/quartic_critical_values|quartic length reduction]],
this result lets a strict bound for every nonunicritical quartic with
unit critical values imply the full equality classification. It does
not supply that strict bound. Standing: proved at author-recorded tier 0,
without independent review. There is no remaining gap in the stated
necessary condition; the quartic length inequality remains an obligation
of the linked research sketch.
