---
name: problems/integer_sequences/E0361/claims
desc: The 4 claim pages of Problem 361, one per claimant's result; the problem's standing derives from them.
tags: []
sources: []
created: 2026-10-07T07:23:56Z
updated: 2026-10-11T22:24:14Z
---

# problems/integer_sequences/E0361/claims

[[problems/integer_sequences/E0361/_index|..]]

[[problems/integer_sequences/E0361/claims/1986_09_08_alon|1986_09_08_alon]]: Alon's refereed Corollary 2.6 (J. Number Theory, 1987) shows that the largest
subset of $\{1,\ldots,n\}$ with no subset summing to $2n$ has $(1/3+o(1))n$
elements. So the extremal size at $c=1/2$ is $(1/6+o(1))n$ along even $n$.

[[problems/integer_sequences/E0361/claims/2026_07_23_principia_math|2026_07_23_principia_math]]: Principia Math's 2026 manuscript and Lean development claim that for $0<c<1$
the normalized extremal size does not converge, and that for $c\ge1$ the size
equals $\lfloor cn\rfloor-\lceil n/2\rceil$. Filed as full, it covers the
second question and the first for $c\ge1$.

[[problems/integer_sequences/E0361/claims/2026_07_25_beyer_de_ryke|2026_07_25_beyer_de_ryke]]: Beyer de Ryke's note, dated 25 July 2026 and posted under Principia Math's
claim, claims that for $0<c<1$ the normalized extremal size does not converge,
with explicit limits along arithmetic subsequences. It also gives the exact
formula for $c\ge1$.

[[problems/integer_sequences/E0361/claims/2026_08_08_principia_math|2026_08_08_principia_math]]: Principia Math's second claim is that a dense subset of $[1,xT]$ has a subset
summing to $sT$, so for $c=x/s$ the extremal size is
$(c/\operatorname{snd}(s)+o(1))n$ along multiples $n$ of $s$ not divisible by
$\operatorname{snd}(s)$. The Lean files state the $s=2$ bound for $1/3<c<1/2$.

***
