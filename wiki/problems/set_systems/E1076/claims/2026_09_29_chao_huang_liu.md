---
name: problems/set_systems/E1076/claims/2026_09_29_chao_huang_liu
title: The (k, k-2) limits refute the site's wording at every k ≥ 5
desc: |
  Answers the site's wording (the single families $F_k$), not the corrected
  Statement (the cumulative family), so it does not count toward the problem's
  standing. An arXiv preprint shows that the $(k,k-2)$ limit is $1/5$ for every
  odd $k\ge5$ and exceeds $1/6$ for every even $k\ge6$.
authors:
- Ting-Wei Chao
- Xinqi Huang
- Hong Liu
status: rejected
claim: disproved
scope: full
submitted: null
links:
- url: https://arxiv.org/abs/2609.38115v1
  kind: preprint
  date: 2026-09-29
created: 2026-10-13T11:30:10Z
updated: 2026-10-13T11:30:10Z
---

***

**Claim.** Write $f^{(r)}(n;s,j)$ for the largest number of edges of an
$r$-uniform hypergraph on $n$ vertices containing no $j$ distinct edges that
span at most $s$ vertices, and $\pi(r,t,j)$ for the limit of
$n^{-t}f^{(r)}(n;(r-t)j+t,j)$, the paper's notation with its $k$, the number
of edges, written $j$ here to keep the site's $k$. Theorem 1.1 of Chao, Huang
and Liu states that $\pi(r,t,j)=2/(t!\,(2\binom rt-1))$ for all integers
$r>t\ge2$ and every odd $j\ge3$, which at $r=3$, $t=2$ is $1/5$. Theorem 1.2
states that $\pi(3,2,j)>1/6$ for every even $j\ge4$; its proof bounds
$\liminf_{n\to\infty}n^{-2}f^{(3)}(n;j+2,j)$ below by $1/6+1/(2|J_\ell|)$, with
$J_\ell$ the reserved pairs of an explicit recursive seed (Definition 3.19,
Proposition 3.20), so it does not need the existence of the limit, which
Delcourt and Postle proved. A $3$-graph contains a member of the site's
$\mathcal F_k$, the $3$-graphs with $k$ vertices and $k-2$ edges, exactly when
some $k-2$ of its edges span at most $k$ vertices, so
$\mathrm{ex}_3(n,\mathcal F_k)=f^{(3)}(n;k,k-2)$, the case $j=k-2$, of the same
parity as $k$. Hence

$$
\mathrm{ex}_3(n,\mathcal F_k)=\Bigl(\frac15+o(1)\Bigr)n^2
\quad\text{for odd }k\ge5,
\qquad
\liminf_{n\to\infty}\frac{\mathrm{ex}_3(n,\mathcal F_k)}{n^2}>\frac16
\quad\text{for even }k\ge6,
$$

and the displayed asymptotic fails at every $k\ge5$ with $\mathcal F_k$ the
single family the site's wording defines, so the site's wording, an assertion
about every $k\ge5$, is false. The transfer from the theorems to the site's
wording is the identification of the forbidden families just made. The values
agree with the refereed ones: the limit $1/5$ at $k=5$, $7$ and $9$, and the
limits $7/36$ and $61/330$ and the lower bound $3/16$ at $k=6$, $8$ and $10$,
all above $1/6$. For even $k$ the paper's concluding remarks place the limit in
$(1/6,1/5]$, and its Question 5.1 leaves the value open from $k=10$ on. The
theorems are new on this problem at every $k\ge11$; the refutations at $k=5$
to $10$ are on
[[problems/set_systems/E1076/claims/2018_09_06_glock|Glock's page]],
[[problems/set_systems/E1076/claims/2022_09_28_glock_joos_kim_kuhn_lichev_pikhurko|the (6,4) page]],
[[problems/set_systems/E1076/claims/2024_03_07_glock_kim_lichev_pikhurko_sun|the (7,5), (8,6) and (9,7) page]]
and
[[problems/set_systems/E1076/claims/2025_06_02_pikhurko_sun|the (10,8) page]],
and the case $k=11$ was proved independently on
[[problems/set_systems/E1076/claims/2026_10_02_bodnar_pikhurko_sun_wang_zeng|the (11,9) page]].

The refutation uses only the lower bounds: $1/5-o(1)$ for odd $k$, from the
paper's Theorem 3.6, and the bound above $1/6$ for even $k$. Both come from
seeds fed to the paper's Lemmas 3.4 and 3.5, its form of the packing theorem of
Glock, Joos, Kim, Kühn, Lichev and Pikhurko (their Theorem 3.1). The paper's AI
statement says that the lower bounds were obtained without AI assistance and
that the authors used ChatGPT-5.6 as a collaborative tool for the upper bounds
and the manuscript.

**Why it is rejected.** It answers the site's wording, the single families
$\mathcal F_k$, not the corrected Statement of
[[problems/set_systems/E1076/_index|Problem 1076]], whose family is
cumulative: under the corrected Statement a $3$-graph avoiding
$\mathcal F_4\cup\dots\cup\mathcal F_k$ is linear, so the theorems say nothing
against it at any $k$, and the page does not count toward the problem's
standing. The problem page's Notes credit the result.

**Acceptance.** None documented. The paper is an arXiv preprint, read in its
first version (29 September 2026, 22 pages): the abstract, Theorems 1.1 and 1.2
(p. 2), the AI-usage paragraph (p. 5), the statements of Lemmas 3.4 and 3.5 and
Theorem 3.6 (p. 12), the proof of Theorem 1.2 (Subsection 3.2) and the
concluding remarks (Section 5). The site does not cite it on this problem, and
its curator makes no statement about it. The proof is unreviewed, and no
formalization is known.
