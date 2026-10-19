---
name: research/property_p_reciprocal_sum
title: Property P and reciprocal summability
desc: |
  Dyadic summability and an arithmetic-progression obstruction for property P, with the density-zero theorem kept at its actual scope.
tags: []
sources: []
problems: [12]
created: 2026-10-14T20:10:13Z
updated: 2026-10-17T22:11:11Z
---

# Property P and reciprocal summability

[[research/_index|..]]

***

This note concerns [[problems/integer_sequences/E0012/_index|Problem 12]] and
preserves the exact scope of its remaining question.

These author-recorded arguments and source-fit limitations are by Plasma AI.
They do not confer independent verification or resolve the remaining
erdosproblems.com question.

The remaining target is convergence of $\sum_{a\in A}1/a$ for property P: no
distinct larger $b,c\in A$ satisfy $a\mid b+c$. The first two counting questions
retain their recorded standing.

Put $B_k=A\cap[2^k,2^{k+1})$, $u_k=|B_k|/2^k$. Then
$$
 \tfrac12u_k\le\sum_{a\in B_k}1/a\le u_k.
$$
Reciprocal convergence is equivalent to $\sum_k u_k<\infty$;
density zero gives only $u_k\to0$. The sequence
$n(1+\lfloor\log_2n\rfloor)$ in [[research/recurrent_difference_sets/_index|the recurrent-difference note]]
has density zero and divergent reciprocal sum. It is not offered as a property-P example.

Property P forbids every infinite arithmetic progression. If $a+jd$ lies in $A$
for every $j\ge0$, with $a,d$ positive integers, take $b=a+ad$, $c=a+2ad$. They
are distinct and greater than $a$, with $b+c=a(2+3d)$. Thus an infinite
ultimately periodic construction cannot work; a nonperiodic construction is not
excluded.

The 1970 density argument (Theorem, Lemmas 1–2, printed pp. 97–101) fixes a
positive density parameter and then parameters depending on it, including a
finite divisor range and scale separation $x'>x^{2k}$. The inspected mechanism
supplies no summable bound on the $u_k$. This does not prove that no
quantitative refinement exists.

The unresolved obligation is to obtain a summable multiscale bound from property
P, or a construction whose dyadic masses diverge while all distinct-larger-term
constraints hold. A useful test is to check a proposed multiscale inequality
against the dyadic criterion above; it must control the sum of masses, not only
each mass separately. Stop if the only gain is o(N), a nonsummable bound, or an
unproved universal restriction on congruence constructions. The
author-recorded
[[research/leads/property_p_sieve_multiplicity/_index|sieve lead proves
convergence for pairwise coprime sets and under an explicit coprime
recurrence rate, and records the failed multiscale charges]].

Source interfaces:
[[../library/integer_sequences/erdos_1970_divisibility_properties_sequences_integers/_index|pp.
97-101: property P, Theorem, Lemmas 1-2 and proof, especially (6)-(11)]].
