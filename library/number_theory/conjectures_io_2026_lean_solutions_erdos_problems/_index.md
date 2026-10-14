---
name: number_theory/conjectures_io_2026_lean_solutions_erdos_problems
title: "Conjectures.io: sixteen Lean solutions of Erdős problems, replayed"
desc: |
  Records sixteen Conjectures.io Lean solution files by URL and SHA-256, held
  under reserved terms and so not in the library, and keeps the kernel replay
  of each on the repository's pinned toolchain on which fifteen claim pages
  rest their acceptance.
license: reserved
created: 2026-10-14T02:00:00Z
updated: 2026-10-14T01:27:55Z
---

# Conjectures.io: sixteen Lean solutions of Erdős problems, replayed

[[number_theory/_index|..]]

[[number_theory/conjectures_io_2026_lean_solutions_erdos_problems/conjectures_io_2026_lean_solutions_erdos_problems|conjectures_io_2026_lean_solutions_erdos_problems]]: Lists the sixteen Conjectures.io records whose Lean solution files were
replayed, with each file's URL, size and SHA-256, and the terms that keep
the files out of the library.

[[number_theory/conjectures_io_2026_lean_solutions_erdos_problems/evidence/_index|evidence/]]: Keeps the kernel replays of sixteen Conjectures.io Lean solutions on the
repository's pinned toolchain; the solution files themselves are fetched by
URL.

***

Conjectures.io publishes Erdős problems as Lean tasks, each pinned to a
formal-conjectures statement, and pays for kernel-checked solutions that pass
its review. Under the rule in `docs/verification.md` ("Review and
acceptance"), a Conjectures.io certification is reported, not counted: the
acceptance of such a proof rests on this repository's own rebuild of the file
on its pinned toolchain, a kernel replay from an empty environment, and a check
of the target against the problem's Statement or the claim's result. This card
records the sixteen solution files behind fifteen claim pages, on Problems 10,
14 (two files), 18, 96, 108, 196, 272, 354, 416, 579, 653, 859, 944, 1057 and
1062, and keeps their replays.

**The files.** Each solution is one Lean source file served by Conjectures.io
at `https://conjectures.io/results/<record id>/solution/download`. The
[source record](conjectures_io_2026_lean_solutions_erdos_problems.md) lists
the sixteen records with each file's URL, size and SHA-256.

**Holding terms.** The library holds none of the files. Conjectures.io's terms
of service (<https://conjectures.io/terms>, effective 13 August 2026, read
2026-10-14) leave ownership with the submitter and license the files to
Conjectures.io alone, so the term recorded is `reserved`; the source record
quotes the clause. A reader fetches each file by its URL and compares its
SHA-256 with the source record.

**The replays.** [evidence/verify/](evidence/verify/_index.md) keeps the replay
driver, the formal-conjectures ports to the pinned toolchain and one dated
receipt per record. All sixteen replays passed.

**Read status.** The files were rebuilt and replayed in the kernel, not read
as proofs. Each receipt's statement check compares the replayed target with
the Statement or the claim's result; nothing else in a file was reviewed.
