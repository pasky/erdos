---
name: theory/number_theory/L199_separated_grid_third_layer/evidence
title: Every block position on small separated prime grids
desc: Brute-force the counts of all core-containing blocks and all blocks near the Chinese-remainder point for small separated prime grids.
created: 2026-10-15T15:58:15Z
updated: 2026-10-15T15:58:15Z
---

# Every block position on small separated prime grids

[[theory/number_theory/L199_separated_grid_third_layer/_index|..]]

***

From the repository root run:

```sh
uv run --no-sync python wiki/theory/number_theory/L199_separated_grid_third_layer/evidence/main.py
```

The [grids](assets/grids.json) are six separated grids of primes
$q+a_i+b_j$, chosen by Plasma AI, with $q$ from $251$ to $13171$. Five
have rows and columns in arithmetic progression, so their third layers
have the largest possible number of coincidences; the sixth has
irregular offsets. Each grid is tried with its full cell set and with
smaller cell subsets, at $\alpha=3$ and at a second ratio for which
$\lfloor\alpha P\rfloor<4q$.

For each case the checker verifies the hypotheses of
[[theory/number_theory/L199_separated_grid_third_layer/_index|L199]] and
solves the congruences. It then counts directly, each integer once, the
multiples in every block of $\lfloor\alpha P\rfloor$ consecutive
integers that contains all row and column locations, and in every block
inside $[z-2q+1,z+4q-1]$. The checks are $|T_S|\ge\lceil u/2\rceil$;
that the least count over the first family equals $r_S+s_S+|T_S|$ and
is attained by $[z-q+1,z-q+K]$; and that the least count over the second
family is at least $\lceil u/2\rceil$. For the five full grids with
progression offsets it also checks the equality
$|\{a_i+2b_j\}|=rs-(r-1)\lfloor s/2\rfloor$ stated on the
[[research/prime_multiple_long_intervals/_index|research account]].

All arithmetic is exact, primality is decided by trial division, and the
run takes a few seconds at most. These instances test the statement's
block families and conventions; they prove nothing beyond themselves.
