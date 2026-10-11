---
name: problems/extremal_graph_theory/E0934/claims
desc: The 5 claim pages of Problem 934, one per claimant's result; the problem's standing derives from them.
tags: []
sources: []
created: 2026-10-07T08:08:44Z
updated: 2026-10-11T22:24:14Z
---

# problems/extremal_graph_theory/E0934/claims

[[problems/extremal_graph_theory/E0934/_index|..]]

[[problems/extremal_graph_theory/E0934/claims/1990_04_01_chung_gyarfas_tuza_trotter|1990_04_01_chung_gyarfas_tuza_trotter]]: Theorem 4 of Chung, Gyárfás, Tuza and Trotter (Discrete Math. 1990, refereed)
bounds the edges of a $2K_2$-free graph of maximum degree $D$. Hence
$h_2(d)=5d^2/4+1$ for even $d$ and $(5d^2-2d+1)/4+1$ for odd $d$, the case
$t=2$.

[[problems/extremal_graph_theory/E0934/claims/2021_03_22_cambie_cames_van_batenburg_de_joannis_de_verclos_kang|2021_03_22_cambie_cames_van_batenburg_de_joannis_de_verclos_kang]]: Cambie, Cames van Batenburg, de Joannis de Verclos and Kang (SIAM J. Discrete
Math. 2022, refereed) prove $h_3(3)=23$ and $h_t(d)\le\frac32d^t+1$ for every
$t$. They also prove $h_t(d)\le d^t+1$ for graphs with no $(2t+1)$-cycle, and
$h_t(d)\ge0.629^td^t$ for large $t$ and infinitely many $d$.

[[problems/extremal_graph_theory/E0934/claims/2026_07_02_kumar_mohar_pragada|2026_07_02_kumar_mohar_pragada]]: The unrefereed July 2026 preprint of Kumar, Mohar and Pragada shows
$h_3(4)\ge71$ and $h_3(15)\ge3796$, refuting the 2022 formula for $h_3(d)$. It
also shows $\liminf h_3(d)/d^3\ge\frac{253}{225}$, refuting the upper
asymptotic at $t=3$.

[[problems/extremal_graph_theory/E0934/claims/2026_07_29_korsky|2026_07_29_korsky]]: Korsky's partial proof claim on the site's tab, later a joint arXiv preprint
with Cames van Batenburg, asserts $h_t(d)\ge(1-o(1))d^t$ as $d\to\infty$ for
every $t\ge3$. The claim rests on a bipartite construction from complete flags
and is unrefereed.

[[problems/extremal_graph_theory/E0934/claims/2026_08_17_bitterlemma|2026_08_17_bitterlemma]]: A thread post and Zenodo manuscript of 17 August 2026 by the Bitter Lemma
project claim the exact value $h_3(4)=71$. The proof combines Kumar, Mohar and
Pragada's lower bound with a certified finite search in Lean 4, was produced
with Claude, and is unreviewed.

***
