---
name: analysis/pendyala_2026_radial_access_lemniscates/theorem_5_1
title: "Theorem 5.1 (p. 7): every admissible polynomial of degree at most three has a safe radius"
desc: |
  Pendyala's cubic zero-detour theorem, as claimed in an unrefereed preprint:
  every monic polynomial of degree at most three with all zeros in the closed
  unit disk has a radius from 0 to the unit circle on which its modulus is at
  most 1, so the worst-case shortest escape length S(n) is 1 for n <= 3.
created: 2026-10-14T22:51:14Z
updated: 2026-10-14T22:51:14Z
---

***

**Source.** Theorem 5.1, p. 7, proof pp. 7--8, of Venkata Siddharth Pendyala,
*Radial access for polynomial lemniscates: the cubic theorem and a degree-six
obstruction*, SSRN preprint (2026), doi:10.2139/ssrn.6850818, the edition
named on the
[[analysis/pendyala_2026_radial_access_lemniscates/_index|source card]].

## Statement

Admissible polynomials, zero detour, safe radii and $N^*$ are as on the
[[analysis/pendyala_2026_radial_access_lemniscates/theorem_1_1|Theorem 1.1 page]].

**Theorem 5.1** (Cubic zero-detour theorem, p. 7). Every admissible monic
polynomial of degree at most three has zero detour. Consequently
$N^*\ge4$.

The proof exhibits a safe radius in every case, which gives zero detour by
the easy half of Proposition 2.2. For the worst-case escape length $S(n)$ of
the problem page, the theorem gives $S(n)=1$ for $n=1,2,3$: every such
polynomial has an escape path of length exactly $1$, a radius.

**Read depth.** Claims checked: the statement was read clause by clause on
the page image. The proof (pp. 7--8) was read through, following its case
table (p. 7) to the result each case uses, and those results (Propositions
3.1 and 3.4, Lemma 3.2, Theorem 3.3 and Lemmas 4.1--4.4) were read in
statement and proof; no step was checked. The paper is an unrefereed
preprint, and nothing here is independently reviewed.

## Proof pointer

Sections 3--5, pp. 3--8, in outline. Degrees one and two are Proposition 3.4
(p. 4). A cubic with a zero at $0$ is $zg(z)$ with $g$ an admissible
quadratic, and a safe radius for $g$ is safe for it. For a cubic with three
nonzero zeros:

- if their directions lie in a closed sector of opening $2\pi/3$, the
  bisecting radius is safe, since each zero is then within distance $1$ of
  both ends of that radius (Proposition 3.1, p. 3);
- if every zero has modulus at most $2/3$, Jensen's formula gives a point of
  the circle where $|f|\le1$ (Lemma 3.2), and the radius to it is safe
  (Theorem 3.3, p. 4);
- otherwise the zeros are spread, normalized as $s$, $ae^{i\alpha}$ and
  $be^{-i\beta}$ with $0<s,a,b\le1$ and $\cos(\alpha+\beta)\le-1/2$
  (Lemma 4.1, p. 5), and a case table (p. 7) picks the ray. The ray through
  $s$ is safe when $s$ has the largest modulus, since then
  $|f(r)|\le|r^3-s^3|\le1$, and when $s\ge2/3$, by the bound
  $|r-\rho|(r^2+rq+p)\le1$ of Lemma 4.2 for an on-ray zero of modulus
  $\rho\ge2/3$, where $p$ is the modulus of the product and $q\le2-p$ the
  modulus of the sum of the other two zeros (Lemma 4.3(1)). Otherwise, with
  $a$ the largest modulus, the ray through $ae^{i\alpha}$ is safe when the
  same test passes or when $\cos\alpha\ge0$ (Lemma 4.4(2)). Failure of the
  test gives $s+b+sb>2$, hence $1/2<s<2/3$ and, by Lemma 4.4(1), $b>4/5$;
  when $\cos\alpha<0$ the ray through $be^{-i\beta}$ then passes the test by
  Lemma 4.3(2).

## Dependencies

Proposition 2.2 (p. 2), stated on the
[[analysis/pendyala_2026_radial_access_lemniscates/theorem_1_1|Theorem 1.1 page]],
Propositions 3.1 (p. 3) and 3.4 (p. 4), Lemma 3.2 and Theorem 3.3 (p. 4) and
Lemmas 4.1--4.4 (pp. 5--6) of the same paper; Lemma 3.2 rests on Jensen's
formula.

## Bears on

- [[../wiki/problems/analysis/E1120/_index|Problem 1120]]: in the problem
  page's worst-case reading $S(n)$, the theorem gives $S(n)=1$ for $n\le3$,
  the trivial lower bound attained by a radius for every admissible
  polynomial of those degrees. It says nothing about degrees four and
  higher.
