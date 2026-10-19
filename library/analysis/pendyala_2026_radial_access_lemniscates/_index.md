---
name: analysis/pendyala_2026_radial_access_lemniscates
title: "Pendyala: Radial access for polynomial lemniscates: the cubic theorem and a degree-six obstruction"
desc: |
  Claims that every monic polynomial of degree at most three with all zeros
  in the closed unit disk has a whole radius from 0 to the unit circle on
  which its modulus is at most 1, while an explicit degree-six one, certified
  by exact rational inequalities, has none; so the least degree at which such
  a radius can fail to exist is 4, 5 or 6.
license: unstated
created: 2026-10-14T22:51:14Z
updated: 2026-10-14T23:06:55Z
---

# Pendyala: Radial access for polynomial lemniscates: the cubic theorem and a degree-six obstruction

[[analysis/_index|..]]

[[analysis/pendyala_2026_radial_access_lemniscates/theorem_1_1|theorem_1_1]]: Pendyala's main theorem, as claimed in an unrefereed preprint: every monic
polynomial of degree at most three with all zeros in the closed unit disk
has a radius from 0 to the unit circle on which its modulus stays at most
1, and an explicit degree-six one has none, so the least degree at which
length-one escape can fail is 4, 5 or 6.

[[analysis/pendyala_2026_radial_access_lemniscates/theorem_5_1|theorem_5_1]]: Pendyala's cubic zero-detour theorem, as claimed in an unrefereed preprint:
every monic polynomial of degree at most three with all zeros in the closed
unit disk has a radius from 0 to the unit circle on which its modulus is at
most 1, so the worst-case shortest escape length S(n) is 1 for n <= 3.

[[analysis/pendyala_2026_radial_access_lemniscates/theorem_6_2|theorem_6_2]]: Pendyala's degree-six obstruction, as claimed in an unrefereed preprint
with a rational certificate: the monic polynomial with double zeros at
-rho e^{2 pi i 927/960} and -rho e^{2 pi i 317/960} and simple zeros at
-rho e^{2 pi i 697/960} and -rho e^{2 pi i 547/960}, rho = 1999999/2000000,
has modulus greater than 1 somewhere on every radius, so the worst-case
shortest escape length S(6) exceeds 1.

***

Venkata Siddharth Pendyala, *Radial access for polynomial lemniscates: the
cubic theorem and a degree-six obstruction*, SSRN preprint (2026), 14 pp.,
doi:10.2139/ssrn.6850818. The print has no author line, no date, no
affiliation and no acknowledgment, and says nothing about AI assistance; its
information dictionary leaves the author field empty and gives a creation
timestamp of 28 May 2026, 05:17 UTC. The attribution is the author's own: on
18 June 2026, in the erdosproblems.com thread of Problem 1120, Venkata
Siddharth Pendyala announced it as "a secondary paper I have written", with
the DOI link, as the
[[../wiki/problems/analysis/E1120/claims/2026_06_17_pendyala_radial|claim page]]
records. No notice is printed in the fourteen pages, and SSRN's terms were not
read for this card; the term is unstated.

The copy read for this card is that PDF, downloaded from SSRN, which hosts it
under the DOI; it carries no version marker and is identified by its fourteen
pages and the timestamp above. SSRN lets an author replace a paper's file
under the same DOI, so the card describes the copy downloaded on 2026-10-14. An admissible polynomial is a monic
$f(z)=\prod_{k=1}^n(z-z_k)$ with every $z_k$ in the closed unit disk;
$E_f=\{z:|f(z)|\le1\}$ contains $0$, and $C_f$ is its component containing
$0$ (p. 1). The paper asks when $C_f$ contains a whole radius
$[0,e^{i\theta}]$. It sets $L(f)$, the infimum of the lengths of rectifiable
paths in $C_f$ from $0$ to the unit circle ($+\infty$ if there is none),
$\Delta(f)=L(f)-1$, and the threshold $N^*$, the least $n\ge1$ for which some
admissible $f$ of degree $n$ has $\Delta(f)>0$ ($+\infty$ if there is none)
(p. 2). Proposition 2.2 (pp. 2--3) shows that $\Delta(f)=0$ exactly when some
radius is safe, $|f(re^{i\theta})|\le1$ for $0\le r\le1$. Theorem 1.1 (p. 2),
the main theorem, asserts $4\le N^*\le6$. Its lower half, Theorem 5.1
(p. 7), gives every admissible polynomial of degree at most three a safe
radius, through a sector theorem (Proposition 3.1, p. 3), a small-radius
theorem for zeros of modulus at most $2/3$ (Theorem 3.3, p. 4), the
quadratic case (Proposition 3.4, p. 4) and a case analysis of the spread
cubic (Sections 4 and 5, pp. 5--8). Its upper half, Theorem 6.2 (p. 9), is an
explicit monic polynomial of degree six, all of whose zeros have modulus
$1999999/2000000$, with no safe radius: by Lemma 6.1 (p. 9), in every
direction its modulus exceeds $1$ at distance $1$, $1/300$ or $439/1000$
from $0$. Corollary 6.3 (p. 10) restates the main
theorem as $N^*\in\{4,5,6\}$, and the exact value is left open.

Appendix A (pp. 10--14) reduces Lemma 6.1 to 8192 inequalities between
rational numbers, one for each angle interval of length $1/8192$ of a turn,
and prints the nine-block table of radii that is the certificate (Table 1,
p. 11), an audit of the smallest margin in each block with SHA-256 hashes of
the exact margins (Table 2, p. 12), and a Wolfram Language listing of a
checker that recomputes every inequality in exact rational arithmetic
(pp. 12--14). The listing is part of the paper; it was not run for this card.

Relation to the author's arXiv paper. Pendyala announced this note together
with
[[analysis/pendyala_2026_shortest_paths_polynomial_lemniscate_sublevel_sets/_index|the arXiv preprint on shortest paths in lemniscate sublevel sets]],
which claims $c\sqrt{\log n}\le S(n)\le\pi n$ for all sufficiently large $n$
for the worst-case escape length $S(n)$. This note treats the length-one end
of the same quantity: $S(n)=\sup_fL(f)=1+\sup_f\Delta(f)$ over admissible
$f$ of degree $n$, and $\Delta(f)\ge0$ because every path from $0$ to the
unit circle has length at least $1$, so $S(n)=1$ exactly when every such $f$
has zero detour, and $N^*$ is the least $n$ with $S(n)>1$. This translation
is the corpus's, not the paper's. The note works in the whole set $E_f$ and
the arXiv paper in its part in the closed disk; the lengths agree, since a
path from $0$ stays in the closed disk until it first meets the circle.

Read status: claims checked. The definitions of pp. 1--2, Theorem 1.1,
Definition 2.1 and Proposition 2.2 (pp. 2--3), Theorem 5.1 (p. 7), the
construction of the degree-six polynomial and (6.1) (pp. 8--9), Lemma 6.1 and
Theorem 6.2 (p. 9), Corollary 6.3 and Remark 6.4 (p. 10), and the
definitions and Tables 1 and 2 of Appendix A (pp. 10--12) were read clause by
clause on the page images. The proofs of Proposition 2.2 and Theorem 5.1,
with the results Theorem 5.1 uses, were read through and not checked. Of the
certificate only its bookkeeping was recomputed here, in exact arithmetic and
without the printed checker: the leading coefficient of the product, the
directions of the zeros, the coverage of the angle intervals by the blocks of
Table 1, and the radii those blocks give to the intervals containing the zero
directions. None of the 8192 inequalities was checked, the printed
checker was not run, and nothing here is independently reviewed.

## Contents

- [[analysis/pendyala_2026_radial_access_lemniscates/theorem_1_1|Theorem 1.1]]
  (p. 2), with the definitions of pp. 1--2, Proposition 2.2 and Corollary
  6.3 (p. 10): $4\le N^*\le6$.
- [[analysis/pendyala_2026_radial_access_lemniscates/theorem_5_1|Theorem 5.1]]
  (p. 7): every admissible polynomial of degree at most three has zero
  detour, so $N^*\ge4$.
- [[analysis/pendyala_2026_radial_access_lemniscates/theorem_6_2|Theorem 6.2]]
  (p. 9), with Lemma 6.1 (p. 9) and the certificate of Appendix A
  (pp. 10--14): an explicit admissible polynomial of degree six, with all
  zeros in the open disk, has no safe radius, so $N^*\le6$.

Source: <https://doi.org/10.2139/ssrn.6850818>.

**Bears on.** [[../wiki/problems/analysis/E1120/_index|#1120]]: in the
problem page's worst-case reading $S(n)$, Theorem 5.1 gives $S(n)=1$ for
$n\le3$ and Theorem 6.2 gives $S(6)>1$, so the least $n$ with $S(n)>1$ is
$4$, $5$ or $6$. The note gives no lower bound for $S(6)-1$ and says nothing
about $S(n)$ for $n=4$, $n=5$ or $n\ge7$, or about its growth.

No file of this source is held: no license on record permits its redistribution,
and the card cites the edition it names above.
