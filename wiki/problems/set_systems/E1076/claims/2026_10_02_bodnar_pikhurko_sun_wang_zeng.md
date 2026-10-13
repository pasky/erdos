---
name: problems/set_systems/E1076/claims/2026_10_02_bodnar_pikhurko_sun_wang_zeng
title: The (11,9) limit 1/5 refutes the site's wording at k = 11
desc: |
  Answers the site's wording (the single family $F_{11}$), not the corrected
  Statement (the cumulative family), so it does not count toward the problem's
  standing. An arXiv preprint proves that the $(11,9)$ limit is $1/5$,
  independently of Chao, Huang and Liu, and bounds the $(10,8)$ limit above by
  $5053/26544$.
authors:
- Levente Bodnár
- Oleg Pikhurko
- Shumin Sun
- Yan Wang
- Jiasheng Zeng
status: rejected
claim: disproved
scope: full
submitted: null
links:
- url: https://arxiv.org/abs/2610.03323v1
  kind: preprint
  date: 2026-10-02
created: 2026-10-13T11:30:10Z
updated: 2026-10-13T11:30:10Z
---

***

**Claim.** Write $f^{(3)}(n;s,j)$ for the largest number of edges of a
$3$-uniform hypergraph on $n$ vertices containing no $j$ edges on at most $s$
vertices, and $\pi(j)$ for the limit of $n^{-2}f^{(3)}(n;j+2,j)$, which exists
by Delcourt and Postle; this is the paper's notation with its $k$, the number of
edges, written $j$ here to keep the site's $k$. Theorem 1.1 of Bodnár,
Pikhurko, Sun, Wang and Zeng states that $\pi(9)=1/5$. The $3$-graphs with no
nine edges on at most eleven vertices are exactly the $3$-graphs with no member
of the site's $\mathcal F_{11}$, the family with $11$ vertices and $9$ edges, so

$$
\mathrm{ex}_3(n,\mathcal F_{11})=\Bigl(\frac15+o(1)\Bigr)n^2,
$$

not $(1+o(1))n^2/6$: the displayed asymptotic fails at $k=11$ with
$\mathcal F_k$ the single family the site's wording defines, so the site's
wording, an assertion about every $k\ge5$, is false. The transfer from the
theorem to the site's wording is the identification of the two forbidden
families.

The refutation needs only the lower bound $\pi(9)\ge1/5$, which Section 3 of
the paper proves by a finite-field construction: a $3$-graph built from blocks
of diamonds sharing a private pair, in which every $h$ edges span at least
$h+2$ vertices for $3\le h\le8$ and every nine edges span at least twelve
(Lemma 3.3), fed to the packing theorem of Glock, Joos, Kim, Kühn, Lichev and
Pikhurko (the paper's Theorem 3.1). The matching upper bound comes from linear
programs that a computer generates and solves, with the code and certificates
in the arXiv ancillary folder. The paper says the result was obtained
independently of
[[problems/set_systems/E1076/claims/2026_09_29_chao_huang_liu|Chao, Huang and Liu]],
whose Theorem 1.1 contains it. Its Theorem 1.2, $\pi(8)\le5053/26544$, is an
upper bound at $k=10$ and refutes nothing; with the lower bound $3/16$ on
[[problems/set_systems/E1076/claims/2025_06_02_pikhurko_sun|the (10,8) page]]
it places the limit at $k=10$ between $3/16=0.1875$ and
$5053/26544\approx0.19036$.

**Why it is rejected.** It answers the site's wording, the single family
$\mathcal F_{11}$, not the corrected Statement of
[[problems/set_systems/E1076/_index|Problem 1076]], whose family is
cumulative: under the corrected Statement a $3$-graph avoiding
$\mathcal F_4\cup\dots\cup\mathcal F_{11}$ is linear, so the theorem says
nothing against it, and the page does not count toward the problem's standing.
The problem page's Notes credit the result.

**Acceptance.** None documented. The paper is an arXiv preprint, read in its
first version (2 October 2026): the abstract, the introduction with Theorems
1.1 and 1.2 (pp. 1--3) and the lower-bound proof of Section 3. The site does
not cite it on this problem, and its curator makes no statement about it. The
proof is unreviewed, the computer certificates were not run here, and no
formalization is known.
