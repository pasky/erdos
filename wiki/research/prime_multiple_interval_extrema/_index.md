---
name: research/prime_multiple_interval_extrema
title: Exact short-block extrema over prime sets
desc: A rectangular extension of the Erdős–Selfridge construction determines the extremal count for every u when the length ratio lies strictly between two and three.
created: 2026-10-14T18:42:37Z
updated: 2026-10-14T18:42:37Z
---

# Exact short-block extrema over prime sets

[[research/_index|..]]

***

For fixed $2<\alpha<3$, let $G_\alpha(u)$ minimize the number of
distinct multiples over sets of $u$ primes and blocks of
$\lfloor\alpha P\rfloor$ consecutive positive integers, with $P$
the largest chosen prime. The author-recorded
[[theory/number_theory/L37_prime_multiple_block_extremum/_index|L37]]
proves $G_\alpha(u)=\lceil2\sqrt u\rceil$ for every $u\ge1$.

This is a rectangular version of the
[[problems/primes/E1143/claims/1978_01_01_erdos_selfridge|recorded Erdős–Selfridge square construction]],
not a novelty claim. The lower bound counts prime incidences in the two
halves and transfers distinct multiples across their midpoint. The upper
bound finds $r$ repeated patterns of $s$ primes, with $rs\ge u$ and
$r+s=\lceil2\sqrt u\rceil$, and uses congruences to place every
multiple at one of the row or column positions. The proof checks the
floor in the block length and makes the whole block positive.

For [[problems/primes/E1143/_index|Problem 1143]], minimization over
prime sets is essential. The result is not a formula for each prescribed
set and does not address $\alpha\ge3$. Extending the interval past
three times the largest prime introduces further multiple positions;
the displayed two-position construction gives no sharp bound there.
The original claim and this author argument retain their separate
standing; no catalog acceptance is recorded by this account.
