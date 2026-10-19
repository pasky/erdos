---
name: research/erdos_132/side_rank_attempt
title: The side-rank inequality and a failed matching reduction
desc: |
  A possible side-rank bound is proved only for concyclic sets;
  regular-polygon subsets disprove its proposed matching shortcut.
sources: []
research_state: blocked
created: 2026-09-23T02:33:01Z
updated: 2026-09-24T22:12:56Z
---


# The side-rank inequality and a failed matching reduction

***

Let a strictly convex $v$-gon have $q$ distinct distances, and
suppose one of its sides has descending distance rank $k$.
The proposed inequality

$$v\le q+k+1 \tag{1}$$

is **unproved for arbitrary convex polygons** in this work. No convex
counterexample to (1) was found. It was considered because applying it to a
chord as a side of its longer subpolygon would yield bounded upper rank errors
when $q=v/2+O(1)$. An upper rank bound alone would still not establish the
monotone row-error hypotheses of
[quantitative_rank_inverse](quantitative_rank_inverse.md).

## Concyclic sets satisfy the inequality

Let $\alpha$ be the empty angular gap of the chosen side $AB$.
If $\alpha\ge\pi$, all vertices occupy a closed arc of length
at most $\pi$ starting at $A$, so the $v-1$ distances from $A$
are distinct and $q\ge v-1$.

Otherwise unwrap the occupied arc from $A$ as $[0,2\pi-\alpha]$.
A chord shorter than $AB$ has minor angle $\beta<\alpha$.
Its two possible angular positions from $A$ are $\beta$ and
$2\pi-\beta$, but the latter lies in the empty gap. Thus each
distance shorter than $AB$ occurs at most once from $A$; every
distance at least $AB$ occurs at most twice. There are $q-k$
values of the former kind and $k$ of the latter. Hence

$$v-1\le(q-k)+2k=q+k,$$

proving (1) in this restricted case.

## A matching bound does not prove (1)

A proposed shortcut would bound the matching number of the
graph of edges longer than that side by $k+O(1)$. This is false,
even for concyclic sets satisfying (1) with equality.

For integers $k\ge2$ and $q\ge3k$, take consecutive vertices
$0,1,\ldots,q+k$ of a regular $(2q+1)$-gon. They determine all
$q$ chord lengths. The closing side has minor chord order
$q+1-k$, hence descending rank $k$. However the edges

$$\{i,q+2-k+i\},\qquad 0\le i\le2k-2,$$

form a matching of size $2k-1$, all at chord order $q+2-k$,
strictly longer than the side. Both endpoint intervals are
disjoint and lie in $[0,q+k]$ by $q\ge3k$.
As $k$ grows, this rules out every bound $k+C$ with absolute $C$.
It does not disprove (1) itself or all possible linear matching bounds.

## What the maximal-side source does provide

Altman's chain argument in [Some Theorems on Convex Polygons,
§III](https://www.cambridge.org/core/services/aop-cambridge-core/content/view/DA46D2AE99BE9FDFED775A10D868A2DE/S0008439500061361a.pdf/div-class-title-some-theorems-on-convex-polygons-div.pdf)
controls the minimum length in a chain of ordered internal diagonals opposite a
diameter side. It does not bound individual entries' rank errors. Replacing that
statement by a row-wise rank estimate was not justified here.

The circular proof and exact matching family were derived by a
separate author and checked by the author; they are author-recorded.
(1) and the arbitrary-convex inverse remain unresolved.
Investigating (1) further is only a provisional direction, not
an established reduction completing either Erdős-132 assertion.
