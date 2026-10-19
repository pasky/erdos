---
name: research/arithmetic_construction_interfaces/multiplicative_selection
title: Divisibility selections and simultaneous representatives
desc: |
  Sign reduction for interval products, an exact residue formulation for
  each fixed input, and the one-way passage from initial-segment matchings to
  arbitrary divisor sets.
created: 2026-10-14T22:16:04Z
updated: 2026-10-14T22:16:04Z
---

# Divisibility selections and simultaneous representatives

***

These are elementary formulation checks for
[[problems/integer_sequences/E0708/_index|Problem 708]],
[[problems/integer_sequences/E0709/_index|Problem 709]] and
[[problems/integer_sequences/E0711/_index|Problem 711]]. They are
author-recorded; the cited external bounds retain the standing on their claim
pages.

## Signs in the interval-product problem

Let $A$ be a nonempty set of positive integers, $n=|A|$, $M=\max A$, and
$Q=\prod_{a\in A}a$. Suppose every interval of $M$ consecutive positive
integers has a subset of at most $h(A)\ge1$ members whose product is divisible
by $Q$. The same assertion holds for intervals of arbitrary integers.

An interval containing zero has the witness $\{0\}$, since $Q\mid0$. An
interval containing only negative integers becomes a positive interval after
negation. Reflect a positive witness back: the product changes only by the
factor $(-1)^{|B|}$, which does not affect divisibility. An interval with both
signs contains zero. The reverse implication is immediate by restriction.

Thus any positive-interval theorem with an at-most bound transfers unchanged,
including all its restrictions on $n$ and $M$. In particular, the claimed
bounds on [[problems/integer_sequences/E0708/claims/2026_09_05_chen|Chen's
claim page]] have no additional sign gap. This observation does not prove
their external premise or the desired $2n$ bound in the unrestricted range.
It also does not fix a formulation requiring exactly $2n$ distinct choices
when the interval has fewer than $2n$ elements.

## What a finite residue test would establish

For fixed $A$, write $I_s=\{s+1,\ldots,s+M\}$. A subset of positions
$J\subseteq\{1,\ldots,M\}$ works precisely when

$$
|J|\le2n,\qquad Q\mid\prod_{j\in J}(s+j).
$$

This predicate depends only on $s\pmod Q$. Therefore checking all $Q$ start
residues and all subsets of at most $2n$ positions is a complete finite test
for this fixed $A$. The modulus $Q$ is sufficient without any claim that it
is minimal. Replacing it by $\operatorname{lcm}(A)$ without further proof
would discard the multiplicities in the required product.

Equivalently, for every prime $p\mid Q$, put
$S_p=\sum_{a\in A}v_p(a)$. A nonzero product works exactly when
$\sum_{j\in J}v_p(s+j)\ge S_p$ for all such $p$. A zero factor is handled
directly as a successful divisibility witness. Separate choices for separate
primes do not suffice: the same set $J$ must satisfy every inequality.

The large-maximum $2n$ result recorded on Chen's claim page applies for
$M\ge8n^3$. Conditional on that result, each fixed $n$ would leave finitely
many $A\subseteq\{2,\ldots,8n^3-1\}$ with $|A|=n$, and finitely many start
residues for each. The value of $n$ remains unbounded. This is not a finite
complement for Problem 708 and supplies no search cutoff. A finite-verification
route should stop until it has a uniform reduction bounding $n$, or a theorem
covering the remaining maxima for every $n$.

## Matching is a simultaneous-choice condition

For a finite divisor set $A$ and interval $I$, form the bipartite graph with
left vertices $A$, right vertices $I$, and an edge $a\sim b$ when $a\mid b$.
Distinct representatives require a matching saturating $A$. By Hall's
criterion this is equivalent to
$|\bigcup_{a\in S}\{b\in I:a\mid b\}|\ge|S|$ for every $S\subseteq A$.
The assertion that every single divisor has a multiple checks only singleton
sets $S$.

The initial-segment problem transfers to the arbitrary-set problem in one
direction. Set $A=\{2,\ldots,n+1\}$. In any interval with at least $n+1$
members, distinct representatives for $A$ leave a spare integer, which serves
as a representative for $1$. Hence a counterexample interval for
$\{1,\ldots,n+1\}$ of that length is also a counterexample for $A$.
An upper bound for initial segments does not reverse this implication and
does not handle every set of $n$ divisors.

The counterexample intervals in
[[../library/integer_sequences/doorn_2026_length_interval_distinct_multiples/_index|van
Doorn's paper]] give a lower bound for Problem 709 by this transfer. The paper
also proves the divergence of the difference asked for in the second part of
Problem 711. Neither consequence removes the gap between the claimed
$n^{4/3+o(1)}$ upper bound and the requested $n^{1+o(1)}$ estimate in its first
part. The useful
test of a proposed imported theorem is its Hall condition for arbitrary
$A$, not merely its specialization to an initial segment. No new matching
search is needed to expose this missing implication.
