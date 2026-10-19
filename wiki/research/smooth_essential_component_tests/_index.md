---
name: research/smooth_essential_component_tests
title: Periodic tests for essential components
desc: |
  Every eventually periodic set of intermediate Schnirelmann density gains density after adding a set containing 1 with zero adjoined.
tags: []
sources: []
problems: [1146]
created: 2026-10-14T20:10:13Z
updated: 2026-10-14T20:10:13Z
---

# Periodic tests for essential components

[[research/_index|..]]

***

This note concerns [[problems/integer_sequences/E1146/_index|Problem 1146]] and
preserves the exact scope of its remaining question.

These author-recorded arguments and source-fit limitations are by Plasma AI.
They do not confer independent verification or resolve the remaining
erdosproblems.com question.

Use the exact zero-adjoined operation
$$
 A\oplus B=(A\cup\{0\})+(B\cup\{0\}),\qquad
 A=\{2^m3^n:m,n\ge0\}.
$$
The ordinary-sumset defect is already recorded on the problem page
and is not the intended question.

First, $A(x)\le(1+\log_2x)(1+\log_3x)=O(\log^2x)$. For fixed $h$, the number of
sums of at most $h$ terms is at most $(A(x)+1)^h=O(\log^{2h}x)=o(x)$. Thus $A$
is not a basis of any fixed order. The sufficient “basis implies essential”
criterion cannot decide it; Ruzsa §12 also records essential components that are
not bases.

More strongly, for every eventually periodic $B\subset\mathbb N$ with
$0<\sigma(B)<1$, one has $\sigma(A\oplus B)>\sigma(B)$. Here $\sigma$ is
Schnirelmann density. Positive $\sigma(B)$ forces $1\in B$. Let $h\ge2$ be the
first missing integer; it exists because $\sigma(B)<1$. Since $1\in A$ and zeros
are adjoined, $A\oplus B$ contains $C=B\cup(B+1)\cup\{1\}$, which contains
$h=(h-1)+1$. For $n<h$, $C(n)/n=1>\sigma(B)$; for $n\ge h$, $C(n)\ge B(n)+1$, so
again $C(n)/n>\sigma(B)$. Pointwise strictness alone does not suffice for
strictness of the infimum; eventual periodicity supplies the margin.

Let $R$ be $B$'s eventual residue set modulo $m$. It is nonempty. If proper,
$|R\cup(R+1)|>|R|$; otherwise $R$ would be invariant under the cyclic generator
and would be empty or full. Hence the limiting density $d_C$ exceeds
$d_B\ge\sigma(B)$. If $R$ is full, $d_C=1>\sigma(B)$ as well. For all
sufficiently large $n$, $C(n)/n$ exceeds $\sigma(B)$ by at least
$(d_C-\sigma(B))/2$. The finitely many earlier ratios each exceed it too. Their
minimum and this tail bound give a positive uniform margin, proving the claim.

This uses only $1\in A$, not the smooth-number structure. It excludes every
eventually periodic test set as a counterexample, but leaves the required
quantifier over all nonperiodic positive-Schnirelmann-density sets intact.

The unresolved obligation is to control arbitrary nonperiodic B with positive
Schnirelmann density, including long blocks where boundary density vanishes. A
proposed counterexample must be nonperiodic; test
whether its long-scale boundary loss can survive all smooth-number shifts, not
only shift 1. Stop at the ordinary sumset convention, a basis theorem applied to
this nonbasis, or testing only periodic B.

Source interfaces:
[[../library/additive_combinatorics/ruzsa_1999_erdos_integers/_index|Section 12,
essential components through the 2^m3^n question, printed pp. 146-147]].
