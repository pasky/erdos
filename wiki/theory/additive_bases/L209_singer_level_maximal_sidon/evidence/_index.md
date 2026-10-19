---
name: theory/additive_bases/L209_singer_level_maximal_sidon/evidence
title: Greedy Singer-level sets for twelve small cases
desc: Build Singer sets for primes from 13 to 53, run the greedy rule of the proof for odd groups of order at most p/4, and verify maximality and the strong Sidon property by brute force.
created: 2026-10-15T18:15:30Z
updated: 2026-10-15T18:15:30Z
---

# Greedy Singer-level sets for twelve small cases

[[theory/additive_bases/L209_singer_level_maximal_sidon/_index|..]]

***

From the repository root run:

```sh
uv run --no-sync python wiki/theory/additive_bases/L209_singer_level_maximal_sidon/evidence/main.py
```

For each prime $p\in\{13,17,19,23,29,31,37,41,43,47,53\}$ the program
builds a Singer set $B$ modulo $q=p^2+p+1$ from the trace-zero powers of a
primitive element of $\mathbb F_{p^3}$, and checks directly that its
differences cover every non-zero residue exactly once. As a control it
checks that $B$ alone is maximal strong Sidon in $\mathbb Z_q$. For twelve
pairs $(p,H)$ with $H$ of odd order $h\le p/4$, eleven cyclic and
$H=\mathbb Z_3\times\mathbb Z_3$ for $p=37$, it runs the greedy rule of
the [proof](../_proof.md), confirms that a value is always available, and
verifies by brute force that the resulting set has $p+h$ elements and is
strong Sidon and maximal in $\mathbb Z_q\times H$. A further control
replaces the level map by a constant and confirms that the set is then not
Sidon. Finally it checks two retained level maps outside the proved range,
for $(p,h)=(5,7)$ and $(11,13)$ with cyclic $H$, which were found by a
randomized backtracking search and are recorded in the program: both give
maximal strong Sidon sets. They are finite observations and do not extend
the statement.

All arithmetic is exact. The program uses the repository's evidence harness
and the Python standard library; it runs in a few seconds and has no quick
mode. Any failed obligation gives a nonzero exit, also under optimized
Python. The check covers these cases only; the statement for every prime
power $p$ and every admissible $H$ rests on the proof.
