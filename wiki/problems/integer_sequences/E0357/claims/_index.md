---
name: problems/integer_sequences/E0357/claims
desc: The 4 claim pages of Problem 357, one per claimant's result; the problem's standing derives from them.
tags: []
sources: []
created: 2026-10-07T07:23:56Z
updated: 2026-10-11T22:24:14Z
---

# problems/integer_sequences/E0357/claims

[[problems/integer_sequences/E0357/_index|..]]

[[problems/integer_sequences/E0357/claims/1984_10_02_hegyvari|1984_10_02_hegyvari]]: Hegyvári's refereed paper (Acta Math. Hungar., 1986) proves that the largest
number of integers in $[1,n]$, not required to increase, with all consecutive
sums distinct lies between $(1/3+o(1))n$ and $(2/3+o(1))n$. So
$f(n)\le(2/3+o(1))n$.

[[problems/integer_sequences/E0357/claims/1996_05_01_coppersmith_phillips|1996_05_01_coppersmith_phillips]]: In a refereed paper (SIAM J. Discrete Math., 1996), Coppersmith and Phillips
bound the size of sets in which no sum of 2 to 4 adjacent elements is an
element. This gives $f(n)\le(2/3-1/512)n+O(\log n)$.

[[problems/integer_sequences/E0357/claims/2026_07_27_lenthall_cleary|2026_07_27_lenthall_cleary]]: Lenthall-Cleary's partial proof claim of 27 July 2026 gives the upper bound
$f(n)\le n/2+O(n^{2/3})$ by blocks of adaptive length, with the finite
inequality in Lean 4, not built here. The bound leaves $f(n)=o(n)$ open.

[[problems/integer_sequences/E0357/claims/2026_08_31_pickhardt|2026_08_31_pickhardt]]: Pickhardt's manuscript, written with the Paratelligent Research Agent, claims
$f(n)\ge(4/\sqrt3-o(1))\sqrt n$ by a sequence omitting one residue class
mod 3. It also claims $f(n)\le n/2+((3/2)2^{-2/3}+o(1))n^{2/3}$ by layer packing.

***
