---
name: problems/irrationality/E0267/claims
desc: The 6 claim pages of Problem 267, one per claimant's result; the problem's standing derives from them.
tags: []
sources: []
created: 2026-10-07T08:51:25Z
updated: 2026-10-12T23:28:38Z
---

# problems/irrationality/E0267/claims

[[problems/irrationality/E0267/_index|..]]

[[problems/irrationality/E0267/claims/1974_12_01_good|1974_12_01_good]]: Good's 1974 note evaluates $\sum_{k\ge0}1/F_{2^k}$ as $(7-\sqrt5)/2$, a
quadratic irrational, so the instance $n_k=2^k$ of the question has answer
yes.

[[problems/irrationality/E0267/claims/1976_12_01_hoggatt_bicknell|1976_12_01_hoggatt_bicknell]]: Hoggatt and Bicknell evaluate $\sum_{n\ge0}1/F_{2^nk}$ in closed form for
every fixed $k$, with coefficient $-1/2$ on $\sqrt5$. So every instance
$n_j=2^jk$ of the question has answer yes.

[[problems/irrationality/E0267/claims/1987_07_01_badea|1987_07_01_badea]]: Badea's 1987 Corollary 4 proves $\sum_{n\ge1}1/F_{2^n+1}$ irrational by the
paper's criterion for series of positive rationals. So the instance
$n_k=2^k+1$ of the question has answer yes.

[[problems/irrationality/E0267/claims/1993_01_01_badea|1993_01_01_badea]]: Badea's Corollary 3.2 of 1993 proves $\sum_k1/F_{n(k)}$ irrational whenever
$n(k+1)\ge2n(k)-1$ for all large $k$. This answers the problem for every ratio
constant $c\ge2$, but not for $1<c<2$.

[[problems/irrationality/E0267/claims/2026_04_24_deepmind|2026_04_24_deepmind]]: AlphaProof found a Lean proof that $\sum_{k\ge0}1/F_{2^k}$ is irrational,
which is the instance $n_k=2^k$ of the question.

[[problems/irrationality/E0267/claims/2026_07_15_snyder|2026_07_15_snyder]]: A 2026 Lean 4 development, posted by Colin Snyder through the Star Fleet Math
site and the problem's proof-claims thread, claims that $\sum_k1/F_{n_k}$ is
irrational for every index sequence with ratios $n_{k+1}/n_k$ at least some
$c>1$.

***
