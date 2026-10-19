---
name: research/ulam_sequence/periodic_tail_certificates
title: Periodic tails of the Ulam sequence
desc: |
  An exact finite certificate for a supplied ultimately periodic Ulam membership set, without an asserted candidate for U(1,2).
tags: []
sources: []
problems: [342]
created: 2026-10-14T20:10:13Z
updated: 2026-10-14T20:10:13Z
---

# Periodic tails of the Ulam sequence

***

This note concerns [[problems/integer_sequences/E0342/_index|Problem 342]] and
preserves the exact scope of its remaining question.

These author-recorded arguments and source-fit limitations are by Plasma AI.
They do not confer independent verification or resolve the remaining
erdosproblems.com question.

Use $U(1,2)$ with distinct summands. Gap 2, periodic consecutive differences,
and density zero are separate questions.

Fix $K\ge3$, $m\ge1$, $P\subset[1,K-1]$ containing 1 and 2,
and nonempty $R\subset\mathbb Z/m\mathbb Z$. Set
$$
 S=P\cup\{n\ge K:n\bmod m\in R\},\quad B=2K+5m,\quad
 C_r=\#\{p\in P:r-p\bmod m\in R\}.
$$
Then $S=U(1,2)$ if and only if:

1. For each integer $3\le n<B$, membership in $S$ is equivalent
   to exactly one unordered representation $n=x+y$, $x\ne y$, in $S$.
2. $R=\{r\notin R+R:C_r=1\}$.

For $n\ge B$, prefix-prefix pairs are impossible. If its residue $r\notin R+R$,
there are no tail-tail pairs; exactly $C_r$ prefix-tail pairs remain, since
every $n-p\ge K$. If $r\in R+R$, choose $u+v=r$ in $R$ and their least
representatives $L_u,L_v\ge K$, both less than $K+m$. Write $n=L_u+L_v+tm$; the
bound ensures $t\ge3$. For $u\ne v$, two distributions of $tm$ give distinct
unordered pairs, distinguished by their endpoint residues. For $u=v$,
distributions $(0,t)$ and $(1,t-1)$ give two distinct pairs with unequal
summands. Thus such a residue has at least two representations and is never
selected. This proves the tail rule. Induction on $n$, whose positive summands
are always smaller than $n$, proves the certificate.

This verifies a specified candidate. It does not produce a candidate or prove
that the actual history has bounded memory. Eventually periodic gaps with period
length $q$ and sum $m$ give $a_{n+q}=a_n+m$, and conversely a periodic
membership tail gives periodic gaps. Its density is positive rational $|R|/m$.

A source finding is Clément–Steinerberger, [Small Gaps in the Ulam Sequence,
arXiv:2501.16285v1](https://arxiv.org/html/2501.16285v1), §1.2. Theorem 1 gives
$a_n\le1.454^n$ eventually. Theorem 2, stated for $n\ge2$, gives $\min_{k\le
n}a_{k+1}/a_k\le1+c\log n/n$. Small relative gaps do not imply gap 2.
Proposition 1's short proof of Eggleton's $a_{n+1}\le a_n+a_{n-2}$ was read; the
new theorem proofs were not audited.

The unresolved obligation is to construct an actual periodic tail satisfying the
certificate, or establish a different invariant on the exact Ulam history. A
useful test is to check, for a proposed candidate period, all n<2K+5m and R={r
outside R+R with exactly one prefix-to-tail representation}. Stop if periodicity
is inferred only from numerical repetition; small relative gaps do not imply
absolute gap 2.
