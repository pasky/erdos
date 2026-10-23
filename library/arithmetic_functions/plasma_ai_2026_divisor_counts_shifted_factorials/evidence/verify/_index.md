---
name: arithmetic_functions/plasma_ai_2026_divisor_counts_shifted_factorials/evidence/verify
title: Verification of the factorial-divisor density theorem
desc: |
  Independent reproduction and statement-fidelity review of the external
  formalization of Problem 420's two density questions.
created: 2026-10-20T18:35:14Z
updated: 2026-10-20T19:39:30Z
---

# Verification of the factorial-divisor density theorem

[[arithmetic_functions/plasma_ai_2026_divisor_counts_shifted_factorials/evidence/_index|..]]

[[arithmetic_functions/plasma_ai_2026_divisor_counts_shifted_factorials/evidence/verify/replay_receipt|replay_receipt]]: Fresh project rebuild with cached vendored dependencies, Comparator check,
and full empty-environment kernel replay on 2026-10-20. Both density
theorems pass, with exactly propext, Classical.choice, and Quot.sound;
their types and statement dependencies agree with Challenge.

[[arithmetic_functions/plasma_ai_2026_divisor_counts_shifted_factorials/evidence/verify/statement_fidelity/_index|statement_fidelity/]]: An independent examination of the formal density statements against the
second and third questions of Problem 420, with a separate grade.

***

The build and kernel replay and the graded statement examination are separate
parts of the acceptance assessment. They concern the version retained in
[../assets/erdos_420_formalization.tar.gz](../assets/erdos_420_formalization.tar.gz).
Neither an author's build report nor the deliberate proof holes of the
challenge module replace verification of `Solution.lean`.
