---
name: research/leads/totient_binary_series/coefficient_growth_obstruction
title: The totient coefficients fail the progression mean bound
desc: |
  The original totient coefficients violate the mean-growth hypothesis in
  Duverney–Tachiya's criterion, leaving transformed coefficients open.
problems:
- 249
created: 2026-10-14T19:25:00Z
updated: 2026-10-14T19:25:00Z
---

***

The direct substitution $\theta(n)=\varphi(n)$ into
[[../library/irrationality/duverney_tachiya_2019_refinement_chowla_erdos_method_linear_independence_certain_lambert_series/theorem_1_1|Duverney–Tachiya's Theorem 1.1]]
fails its coefficient-growth hypothesis. This tests a source's applicability
to [[problems/irrationality/E0249/_index|Problem 249]]; it gives no
irrationality or rationality conclusion for
$S=\sum_{n\ge1}\varphi(n)2^{-n}$.
The elementary calculation below is author-recorded by Plasma AI and has
no independent review.

## The failed hypothesis

Condition $(H_2)$ asks for a fixed $\nu>0$ such that, uniformly over
coprime positive integers $a,b$,

$$
\sum_{i=0}^{n}|\theta(ai+b)|
\le n(2+\log n)^\nu
\qquad(n\ge\max\{a,b\}).
$$

The pair $a=b=1$ already prevents the proposed substitution. If $m\ge1$
has distinct prime factors $r_1<\cdots<r_s$, then $r_j\ge j+1$ and
$2^s\le m$. The empty product covers $m=1$. Hence

$$
\frac{\varphi(m)}m
=\prod_{j=1}^s\left(1-\frac1{r_j}\right)
\ge\prod_{j=1}^s\frac{j}{j+1}
=\frac1{s+1}
\ge\frac1{1+\log_2m}.
$$

For $n\ge2$, at least $n/2$ integers in $[1,n+1]$ are at least $n/2$.
Keeping just those summands gives

$$
\sum_{i=0}^{n}\varphi(i+1)
\ge\frac{n^2}{4(1+\log_2(n+1))}.
$$

For every fixed $\nu>0$, the ratio of this lower bound to
$n(2+\log n)^\nu$ tends to infinity. Thus $(H_2)$ fails even if its
right side is multiplied by any fixed constant. Checking the separate
divisibility condition $(H_1)$ cannot repair this direct application.

## Scope of another application

A transformed integer coefficient sequence could still be relevant, but it
must meet two separate obligations: an implication from its irrationality
to that of $S$, and the actual hypotheses of the theorem being used.
The [[research/leads/totient_binary_series/analytic_sources|analytic source
tests]] record other restrictions on fixed dyadic filters and sparse
transfers; those restrictions are not assertions about every possible
transformation. No such new transformation is supplied here.

The source statement and both hypotheses were read in the held
transcription and the linked statement page. This applicability check
does not require, and does not supply, an independent audit of the
source proof. It concerns only the original coefficients $\varphi(n)$.
