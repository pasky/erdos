---
name: analysis/debruijn_erdos_1949_sequences_points_circle/conjecture_p17
title: "Section 6 conjecture (p. 17): r(Λ_r − 1), r(1 − λ_r) and r(μ_r − 1) tend to infinity"
desc: |
  The closing conjecture of the note, that r(Λ_r − 1), r(1 − λ_r) and
  r(μ_r − 1) tend to infinity with r, with its normalization defect and the
  mean-normalized reading recorded; the question behind Problem 1221.
created: 2026-09-28T03:00:00Z
updated: 2026-10-14T01:26:25Z
---

***

## Statement

With the Section 1 constants $\Lambda_r$, $\lambda_r$, $\mu_r$ (the
infimum over sequences of $\limsup_nnM_n^r(a)$, the supremum of
$\liminf_nnm_n^r(a)$ and the infimum of $\limsup_nM_n^r(a)/m_n^r(a)$,
where $M_n^r(a)$ and $m_n^r(a)$ are the largest and smallest sums of $r$
consecutive intervals cut by $a_1,\ldots,a_n$ on the circle of
circumference $1$), Section 6 (p. 17) says that the bounds (3.3), (4.3)
and (5.7) are "probably not best possible if $r\ge2$" and conjectures that
the expressions

$$
r(\Lambda_r-1),\qquad r(1-\lambda_r),\qquad r(\mu_r-1)
$$

"tend to infinity if $r\to\infty$". The introduction (p. 14) states the
third part alone, as the conjecture that $r(\mu_r-1)$ is unbounded, and
adds that the "just distributions" theorem of van Aardenne-Ehrenfest
(Proc. 48 (1945), 266--271 = Indag. Math. 7 (1946), 71--76) would follow
from it. erdosproblems.com's Problem 1221 reproduces the Section 6 wording.

**Source.** N. G. de Bruijn and P. Erdős, *Sequences of points on a
circle*, Proc. 52 (1949), 14--17; Section 6 on printed p. 17 and the
remark on p. 14 (PDF pp. 5 and 2 of the TU/e portal PDF), read on the page
images. The edition read is identified in the
[[analysis/debruijn_erdos_1949_sequences_points_circle/_index|source digest]].

**Read depth.** Claims checked: the two passages were read clause by
clause on the page images. A conjecture has no proof to check; the
analysis below is the corpus's own.

## The normalization defect

An authored analysis, checked here. With the note's own definitions the
average $r$-span is $r/n$, so $nM_n^r(a)\ge r\ge nm_n^r(a)$ (Section 1),
and the note's own bounds place $\Lambda_r$ above $r$ and $\lambda_r$
below $r$:

- [[analysis/debruijn_erdos_1949_sequences_points_circle/inequality_3_3|Section 3]]
  gives $\Lambda_r\ge1/\log(1+1/r)>r$, so $r(\Lambda_r-1)\ge r(r-1)$ and the
  first expression is trivially unbounded;
- [[analysis/debruijn_erdos_1949_sequences_points_circle/inequality_4_3|(4.3)]]
  gives $\lambda_r<r$, but also $\lambda_r\ge r\lambda_1=r/\log4>1$ for
  $r\ge2$, since an $r$-span is at least $r$ times the smallest interval;
  so $r(1-\lambda_r)\to-\infty$ and the second expression cannot tend to
  $+\infty$;
- [[analysis/debruijn_erdos_1949_sequences_points_circle/inequality_5_7|(5.7)]]
  gives $r(\mu_r-1)\ge1$, and the third expression is a genuine question
  as written, since the ratio needs no normalization.

The reading supported by the note's own estimates normalizes the first two
constants by the mean span: with $\hat\Lambda_r=\Lambda_r/r$ and
$\hat\lambda_r=\lambda_r/r$ the three expressions become

$$
r(\hat\Lambda_r-1)=\Lambda_r-r,\qquad
r(1-\hat\lambda_r)=r-\lambda_r,\qquad
r(\mu_r-1),
$$

which the note's bounds show are at least $\tfrac12+o(1)$, $\tfrac12+o(1)$
and $1$, so that each part asks whether a bounded lower bound can be
replaced by one that grows. This is the reading the later literature
adopts (Korsky's 2026 preprint restates the conjecture as
$\bar A_r-r\to\infty$, $r-\underline A_r\to\infty$, $r(\mu_r-1)\to\infty$, a
corrected paraphrase rather than the note's wording), and the reading
the community database marks the erdosproblems.com statement as needing
("ambiguous statement"; a missing factor of $r$).

## Dependencies

The three bounds of Sections 3--5 for the analysis above; none for the
conjecture itself.

## Bears on

- [[../wiki/problems/analysis/E1221/_index|Problem 1221]]: this passage is the problem.
  The erdosproblems.com wording inherits the normalization slip; the problem
  page shows the mean-normalized form as its modified Statement and records the
  2026 preprint that claims all three parts of it.
