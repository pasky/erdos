---
name: problems/additive_combinatorics/E0138/claims
desc: The 4 claim pages of Problem 138, one per claimant's result; the problem's standing derives from them.
tags: []
sources: []
created: 2026-10-07T08:44:40Z
updated: 2026-10-14T00:16:44Z
---

# problems/additive_combinatorics/E0138/claims

[[problems/additive_combinatorics/E0138/_index|..]]

[[problems/additive_combinatorics/E0138/claims/2026_04_10_deepmind|2026_04_10_deepmind]]: Google DeepMind's AlphaProof Nexus found a Lean proof that
$W(k+1)\ge W(k)+k$, so $W(k+1)-W(k)\to\infty$. This is the second question
Erdős asked in [Er81], recorded in the site's commentary, and the paper
reporting the result is refereed.

[[problems/additive_combinatorics/E0138/claims/2026_04_10_sothanaphan|2026_04_10_sothanaphan]]: A five-page note by Nat Sothanaphan, written with GPT-5.4 Thinking and linked
from the site's thread, proves $W_r(k+1)-W_r(k)\ge k+\min\{k,F(r)\}+1$ for $r$
colors. For the problem's two colors this gives $W(k+1)-W(k)\ge k+1$, and the
result is claimed.

[[problems/additive_combinatorics/E0138/claims/2026_08_21_campos_fox_schildkraut|2026_08_21_campos_fox_schildkraut]]: Theorem 1 of Campos, Fox and Schildkraut (arXiv, August 2026) proves
$W(k)\ge(1-o(1))\,k\,2^{k-1}$ for all $k$, which improves the general lower
bound and gives $W(k)/2^k\to\infty$. The coloring was found by ChatGPT 5.6 Sol
Pro.

[[problems/additive_combinatorics/E0138/claims/2026_09_23_openai|2026_09_23_openai]]: Theorem 1.1 of the OpenAI release manuscript of 23 September 2026 proves
$W(k)>k^{k/100000}$ for all large $k$, so $W(k)^{1/k}\to\infty$, the example
question of Problem 138. It is accepted on built Lean as a partial result.

***
