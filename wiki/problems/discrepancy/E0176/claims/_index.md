---
name: problems/discrepancy/E0176/claims
desc: The 3 claim pages of Problem 176, one per claimant's result; the problem's standing derives from them.
tags: []
sources: []
created: 2026-10-07T07:13:08Z
updated: 2026-10-14T00:13:33Z
---

# problems/discrepancy/E0176/claims

[[problems/discrepancy/E0176/_index|..]]

[[problems/discrepancy/E0176/claims/2026_06_21_kitamura|2026_06_21_kitamura]]: Kenta Kitamura's Lean 4 development, prepared with Codex and ChatGPT, proves
$N(k,2)\le\lfloor 2(k^2-1)(k-1)(2k+1)/(k-3)\rfloor+1$ for every $k\ge5$. So
$N(k,2)=O(k^3)$, and the displayed question $N(k,2)\le C^k$ has the answer
yes.

[[problems/discrepancy/E0176/claims/2026_06_23_kitamura|2026_06_23_kitamura]]: Kenta Kitamura's Lean 4 development, prepared with Codex and ChatGPT, proves
$N(k,\sqrt k)\le\lfloor\frac43(k^2-k+1)(k-1)(k(k-1)+1)\rfloor+1$ for every
$k\ge2$. So $N(k,\sqrt k)=O(k^5)$, and the displayed question
$N(k,\sqrt k)\le C^k$ has the answer yes.

[[problems/discrepancy/E0176/claims/2026_09_23_openai|2026_09_23_openai]]: The superexponential lower bound for van der Waerden numbers in the OpenAI
release, read through the site's identity $N(k,k)=W(k)$, makes the first
displayed question false at $c=1$, and so answers it no as stated. The
bound is accepted on Problem 138; the identity follows from the definition
and was checked by Plasma AI, and the claim's acceptance is pending.

***
