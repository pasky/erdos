---
name: number_theory/conjectures_io_2026_lean_solutions_erdos_problems/evidence
title: Evidence for the kernel replays of sixteen Conjectures.io solutions
desc: |
  Keeps the kernel replays of sixteen Conjectures.io Lean solutions on the
  repository's pinned toolchain; the solution files themselves are fetched by
  URL.
created: 2026-10-14T02:00:00Z
updated: 2026-10-14T01:39:13Z
---

# Evidence for the kernel replays of sixteen Conjectures.io solutions

[[number_theory/conjectures_io_2026_lean_solutions_erdos_problems/_index|..]]

[[number_theory/conjectures_io_2026_lean_solutions_erdos_problems/evidence/verify/_index|verify/]]: The replay driver, the formal-conjectures ports to Lean v4.34.1 and one dated
receipt per record for the sixteen Conjectures.io solutions replayed in the
kernel from an empty environment; all sixteen passed.

***

`verify/` keeps one receipt per record and the kernel replay program
`Replay.lean`, `util/replay.sh` is the driver, and `assets/` holds its exact
inputs: the record and pin tables and the formal-conjectures ports to the pinned
toolchain; a solution file's own port is held privately beside it. There is no
`main.py`. A replay needs elan, network access and dedicated machine time, so it
is run by hand, one record at a time, with `util/replay.sh`. No solution file is
held here; each is fetched from Conjectures.io by the URL its receipt names.
