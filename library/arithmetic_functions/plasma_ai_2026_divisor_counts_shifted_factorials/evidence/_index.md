---
name: arithmetic_functions/plasma_ai_2026_divisor_counts_shifted_factorials/evidence
title: Evidence for the factorial-divisor density theorem
desc: |
  The retained formalization and the independent build, kernel replay and
  statement-fidelity records for the two density questions of Problem 420.
created: 2026-10-20T18:35:14Z
updated: 2026-10-22T19:33:06Z
---

# Evidence for the factorial-divisor density theorem

[[arithmetic_functions/plasma_ai_2026_divisor_counts_shifted_factorials/_index|..]]

[[arithmetic_functions/plasma_ai_2026_divisor_counts_shifted_factorials/evidence/verify/_index|verify/]]: Independent reproduction and statement-fidelity review of the external
formalization of Problem 420's two density questions.

***

The exact source is held in
[assets/erdos_420_formalization.tar.gz](assets/erdos_420_formalization.tar.gz),
made from commit daa3bba of the external source, excluding `paper/`, as the
replay receipt records;
[[arithmetic_functions/plasma_ai_2026_divisor_counts_shifted_factorials/_index|the source card]]
compares it with the publication tree. It retains the Lean sources, vendored libraries, licenses,
version pins and comparison configuration needed to reproduce the formal proof.

[util/replay.sh](util/replay.sh) documents the build, Comparator and
empty-environment kernel replay procedure. The
[[arithmetic_functions/plasma_ai_2026_divisor_counts_shifted_factorials/evidence/verify/replay_receipt|successful reproduction on 2026-10-20]]
rebuilt every project module in a fresh tree using checked vendored dependency
caches, then replayed both complete proof closures from empty environments.
The script also supports rebuilding the vendored sources without those caches.
The statement-fidelity extraction in `assets/statement_fidelity/extraction/`
contains the problem's Statement and the formal targets without assessment or
prior-review material. The examination concerns their mathematical
correspondence; the build and replay are separate obligations.
