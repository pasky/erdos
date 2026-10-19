---
name: theory/polynomials/L144_cubic_lemniscate_length
title: Lemniscate length of monic cubics
desc: |
  A uniform ball-arithmetic family inequality and Eremenko-Hayman's
  deformation prove the cubic lemniscate bound and its equality case at
  tier 1 on an independently graded whole-claim examination.
id: L144
statement: |
  For a monic polynomial p in C[z], let l(p) be the length of the curve
  {z in C : |p(z)|=1}. For every real a with 0<a<=2^(-1/3), with
  c=sqrt(1-4a^6), l(z^3+3a^2 z-c) < l(z^3-1) = 2 pi Gamma(1/3)/Gamma(2/3)^2.
  Consequently, using Lemmas 4 and 5 of Eremenko and Hayman (1999) and the
  deformation in their proof of Lemma 5, every monic cubic p in C[z]
  satisfies l(p)<=l(z^3-1), with equality exactly when p(z)=(z-z0)^3-w for
  some z0 in C and some w with |w|=1.
status: proved
tier: 1
depends_on: []
created: 2026-10-15T11:10:00Z
updated: 2026-10-15T11:12:50Z
---

# Lemniscate length of monic cubics

[[theory/polynomials/_index|..]]

[[theory/polynomials/L144_cubic_lemniscate_length/_proof|_proof]]: Root identities give exact length integrals; a comparison with z^3-c and box-uniform ball bounds over two parameter regimes prove the family inequality.

[[theory/polynomials/L144_cubic_lemniscate_length/evidence/_index|evidence/]]: Box-uniform arb bounds cover the whole parameter range of the cubic family in two regimes, with a coverage join and a two-sided control.

***

The [proof](_proof.md) and its
[[theory/polynomials/L144_cubic_lemniscate_length/evidence/_index|ball-arithmetic evidence]]
are by Plasma AI. The [whole-claim examination and distinct PASS grade](evidence/verify/_index.md)
warrant **tier 1** for the complete statement, including uniqueness. The
external-source and arithmetic qualifications below remain in force; no Lean
proof is claimed.
The family inequality is proved here: a written analysis reduces it to
explicit integrals, and the evidence program bounds those integrals uniformly
over boxes that cover the whole parameter range, including both ends. The
consequence for every cubic also consumes two source results of a refereed
paper:
[[../library/polynomials/eremenko_1999_length_lemniscates/lemma_4|Lemma 4]],
the existence of a maximizer in each degree, and
[[../library/polynomials/eremenko_1999_length_lemniscates/lemma_5|Lemma 5]],
that some maximizer has all its critical points on its lemniscate; the
uniqueness clause also uses the deformation constructed in the proof of
Lemma 5. Their library accounts record the statements as read on the print and
the proof of Lemma 5 as read in outline; for this claim the whole proof of
Lemma 5 (pp. 5--7 of the corrected preprint) was read on the page images. Tao's
[[../library/polynomials/tao_2025_maximal_length_erdos_herzog_piranian_lemniscate/proposition_1_2|Proposition 1.2]]
restates them.

The claim is the degree-3 case of the question of
[[problems/polynomials/E0114/_index|Problem 114]], with uniqueness: $z^3-1$
maximizes the length, and up to rotation and translation it is the only
maximizer. The uniqueness argument uses the quasiconformal deformation in
the proof of Lemma 5, which the paper carries out for every extremal
polynomial, together with the strict family inequality. It settles
no other degree. The
[[research/erdos_114/cubic_extremizer_reduction|research sketch]] records how
the reduction, the deformation and the family inequality compose.

**Verification.** Read the proof and run, from the repository root,

```sh
uv run --no-sync python wiki/theory/polynomials/L144_cubic_lemniscate_length/evidence/main.py
```

which takes about five minutes on one thread. The [verification record](evidence/verify/_index.md)
retains the whole-statement report, distinct grade, exact executable inputs and
independent derivations. An initial identity-only import exposure was ruled
immaterial by the distinct grader; the later eligibility assessment found no
demonstrated unrelated-status exposure to that grader. Four failed auxiliary
endpoint-equality assertions remain failed and have no successful-calibration
weight. The accepted source interface retains Lemma 4 as an external theorem
with only partial verification of its supplied proof, and the cited Beltrami
book theorem remains an unread original-source boundary.
