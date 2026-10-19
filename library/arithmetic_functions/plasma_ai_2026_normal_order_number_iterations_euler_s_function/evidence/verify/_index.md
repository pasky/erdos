---
name: arithmetic_functions/plasma_ai_2026_normal_order_number_iterations_euler_s_function/evidence/verify
title: Verification records for the Problem 408 formalization
desc: |
  This corpus's verification records for the held Lean formalization of
  Plasma AI's Problem 408 preprint: the receipt of its rebuild, Comparator
  check and kernel replay, and the statement-fidelity audit of its three
  challenge statements with the audit's distinct grade.
created: 2026-10-14T20:39:30Z
updated: 2026-10-19T07:08:38Z
---

# Verification records for the Problem 408 formalization

[[arithmetic_functions/plasma_ai_2026_normal_order_number_iterations_euler_s_function/evidence/_index|..]]

[[arithmetic_functions/plasma_ai_2026_normal_order_number_iterations_euler_s_function/evidence/verify/replay_receipt|replay_receipt]]: Build, Comparator check and kernel replay of Plasma AI's Problem 408
formalization at 4ea44bf on Lean v4.35.0-rc3, on 2026-10-19: Comparator
accepts its three theorems against the challenge, each replays in the kernel
from an empty environment, and each depends only on propext,
Classical.choice and Quot.sound.

[[arithmetic_functions/plasma_ai_2026_normal_order_number_iterations_euler_s_function/evidence/verify/statement_fidelity/_index|statement_fidelity/]]: Accepted independent statement-fidelity audit, on 2026-10-14, of the three
statements in the Problem 408 formalization's challenge file, with its
distinct grade: all three faithful, coverage partial, no tier awarded.

***

The records here check the formalization held in the
[archive](../assets/erdos_408_formalization.tar.gz) one step at a time. The
statement-fidelity audit compares the three statements of its
`Challenge.lean` with the questions and the theorem they formalize. The replay
receipt records the rebuild of the formalization, Comparator's check of the
three theorems against `Challenge.lean`, and their kernel replay from an empty
environment.
