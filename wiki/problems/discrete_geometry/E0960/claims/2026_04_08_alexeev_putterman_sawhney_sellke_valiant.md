---
name: problems/discrete_geometry/E0960/claims/2026_04_08_alexeev_putterman_sawhney_sellke_valiant
title: Quadratically many ordinary lines without an ordinary triangle
desc: |
  For $r\ge3$ and $k\ge4$, Alexeev, Putterman, Sawhney, Sellke and Valiant give
  $n$-point sets with no $k$ on a line, at least $n^2/12-10n/3$ ordinary lines,
  and no $r$ points spanning only ordinary lines. Hence the threshold is of
  order $n^2$ and not $o(n^2)$.
authors:
- Boris Alexeev
- Moe Putterman
- Mehtaab Sawhney
- Mark Sellke
- Gregory Valiant
status: accepted
claim: disproved
scope: full
evidence:
- reviewed
published: 2026-04-08
submitted: null
links:
- url: https://arxiv.org/abs/2604.06609
  kind: preprint
  date: 2026-04-08
- url: https://www.erdosproblems.com/960
  kind: discussion
  date: 2026-04-09
created: 2026-10-07T05:47:56Z
updated: 2026-10-07T21:55:30Z
---

***

**Claim.** The answer to the question of
[[problems/discrete_geometry/E0960/_index|Problem 960]] is no: the threshold
$f_{r,k}(n)$ is neither $o(n^2)$ nor $\ll n$. Theorem 2.1 of
[[../library/discrete_geometry/alexeev_2026_short_proofs_combinatorics_probability_number_theory/_index|Alexeev, Putterman, Sawhney, Sellke and Valiant]]
gives, for every $r\geq3$, $k\geq4$ and $n\geq72$, a set of $n$ points in the
plane with no $k$ on a line and at least

$$
\frac{n^2}{12}-\frac{10}{3}\,n
$$

ordinary lines, in which no $r$ points have all their $\binom r2$ connecting
lines ordinary. The graph whose vertices are the points and whose edges are
the ordinary lines is bipartite (Proposition 2.5(2) of the paper, resting on
Proposition 2.4 for the base set), so it has no triangle, which is the case
$r=3$ and hence every $r\geq3$. Writing $n=6m+s$ with $0\leq s\leq5$, the
base set $A_0$ of $6m$ points is taken in a cyclic torsion subgroup of order
$7m$ of the real points of the elliptic curve $y^2=x^3-x+1$, with the residue
class of $0$ modulo $7$ removed, so that collinearity becomes arithmetic in
the group; when $6$ does not divide $n$, the set $A=A_0\cup T_s$ adds back
$s$ chosen points of the removed class, and Proposition 2.5 checks that no
four points of $A$ are collinear and that the ordinary-line graph stays
bipartite. Together with
the upper bound $f_{r,k}(n)\leq(1-\tfrac1{r-1})\tfrac{n^2}2+1$ from Turán's
theorem, which the erdosproblems.com commentary records, the threshold is of
order $n^2$ for every fixed $r\geq3$ and $k\geq4$; its exact value is not
determined. The remaining parameters are degenerate, as Section 2.1 of the paper
states: for $k=2$ no valid set exists, for $k=3$ every line determined by the
set is ordinary and the graph is complete, and for $r=2$ with $k\geq4$ the
Sylvester-Gallai theorem supplies an ordinary line and so the pair. The
problem's discussion notes that the lines spanned
by the $r$ points must be ordinary with respect to the whole set, which is how
the theorem reads the question.

**Claimant.** The result is Theorem 2.1 of Boris Alexeev, Moe Putterman,
Mehtaab Sawhney, Mark Sellke and Gregory Valiant, Short proofs in
combinatorics, probability and number theory II, arXiv:2604.06609, posted on
2026-04-08. The paper states that each of its proofs is due to an internal
model at OpenAI; erdosproblems.com credits the bound to that model through the
paper. Erdős posed the question in his 1984 research-problem note
([[../library/discrete_geometry/erdos_1984_research_problems/_index|card]],
p. 102), where he conjectured the $o(n^2)$ bound and suggested a linear one.

**Acceptance.** Thomas Bloom, the erdosproblems.com curator, marked the problem
disproved and credits this bound on the problem's page at erdosproblems.com. The
page was last edited 2026-04-09, and its label and credit showed on 2026-10-06.
That credit is the `reviewed` evidence. The paper is a preprint, and no refereed
version was found on 2026-10-06. No Lean proof is recorded. The claim is
therefore neither `refereed` nor `formalized`.

**What remains.** The order of $f_{r,k}(n)$ is settled at $n^2$ for
$r\geq3$ and $k\geq4$, between $n^2/12-O(n)$ and
$(1-\tfrac1{r-1})\tfrac{n^2}2+1$; the constant is open. erdosproblems.com points
to [[problems/discrete_geometry/E0209/_index|Problem 209]] as related.
