---
name: problems/extremal_graph_theory/E0617/claims
desc: The 10 claim pages of Problem 617, one per claimant's result; the problem's standing derives from them.
tags: []
sources: []
created: 2026-10-07T08:08:44Z
updated: 2026-10-11T22:24:14Z
---

# problems/extremal_graph_theory/E0617/claims

[[problems/extremal_graph_theory/E0617/_index|..]]

[[problems/extremal_graph_theory/E0617/claims/1978_01_01_chung_liu|1978_01_01_chung_liu]]: Theorem 3.6 of Chung and Liu (Discrete Math. 1978) shows that every
three-coloring of $K_{10}$ has four vertices missing a color, the case $r=3$
of Problem 617. A coloring of $K_9$ shows that it is sharp, and the paper is
refereed.

[[problems/extremal_graph_theory/E0617/claims/1999_04_01_erdos_gyarfas|1999_04_01_erdos_gyarfas]]: Lemmas 1 and 2 of Erdős and Gyárfás (Discrete Math. 1999) show that every
three-coloring of $K_{10}$ and every four-coloring of $K_{17}$ has $r+1$
vertices missing a color. These are the cases $r=3$ and $r=4$ of Problem 617,
and the paper is refereed.

[[problems/extremal_graph_theory/E0617/claims/2026_07_18_sneiderman_r5|2026_07_18_sneiderman_r5]]: A preprint by Robert Sneiderman of 18 July 2026 claims the fixed case $r=5$ of
Problem 617: every five-coloring of $K_{26}$ has six vertices missing a color,
while $K_{25}$ has a five-coloring without such a set. Kara has formalized the
argument in Lean and LRAT.

[[problems/extremal_graph_theory/E0617/claims/2026_07_18_sneiderman_r6|2026_07_18_sneiderman_r6]]: An unrefereed preprint by Robert Sneiderman of 18 July 2026 claims the fixed
case $r=6$ of Problem 617: every six-coloring of $K_{37}$ has seven vertices
missing a color. The argument uses clique lemmas on $18$, $19$, $24$ and $25$
vertices and an edge count on $31$.

[[problems/extremal_graph_theory/E0617/claims/2026_07_20_sneiderman_r7_r8|2026_07_20_sneiderman_r7_r8]]: A preprint by Robert Sneiderman of 20 July 2026 claims the fixed cases $r=7$
and $r=8$ of Problem 617 ($K_{50}$ with seven colors, $K_{65}$ with eight).
The argument is a colored-density reduction closed by an exhaustive lemma and
$862$ LRAT-checked instances.

[[problems/extremal_graph_theory/E0617/claims/2026_07_21_silverstein|2026_07_21_silverstein]]: An unrefereed write-up by Conner Silverstein of 21 July 2026 claims the fixed
case $r=5$ of Problem 617 by a one-color count, with twelve DRAT-certified
formulas. Each color class needs $66$ edges, so five need $330$, more than the
$325$ edges of $K_{26}$.

[[problems/extremal_graph_theory/E0617/claims/2026_07_21_sneiderman_r9|2026_07_21_sneiderman_r9]]: An unrefereed preprint by Robert Sneiderman of 21 July 2026 claims the fixed
case $r=9$ of Problem 617: every nine-coloring of $K_{82}$ has ten vertices
missing a color. The argument is a density recursion reduced to finite
statements on $26$ and $27$ vertices.

[[problems/extremal_graph_theory/E0617/claims/2026_07_25_rose|2026_07_25_rose]]: An unrefereed paper of 25 July 2026 by Anthony Rose claims the fixed case
$r=5$ of Problem 617. It scales the Erdős–Gyárfás minority-color technique to
$r=5$, reducing the case to $458$ SAT instances, all refuted with DRAT proofs.

[[problems/extremal_graph_theory/E0617/claims/2026_07_31_winter|2026_07_31_winter]]: A repository and write-up of 31 July 2026 by Nick Winter claim the fixed case
$r=5$ of Problem 617 with a Lean 4 proof built on a hitter lemma and a
minority-color lemma. The proof's SAT certificates rest on native_decide.

[[problems/extremal_graph_theory/E0617/claims/2026_08_11_terpstra|2026_08_11_terpstra]]: A preprint draft and artifact, written by OpenAI Codex under the direction of
Adam Lee Terpstra and released by him on 11 August 2026, claim the fixed cases
$r=10$ and $r=11$ of Problem 617. They give no certificate and are unrefereed.

***
