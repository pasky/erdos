---
name: theory/integer_sequences/L252_nonresidue_blocks_without_smooth_members/_proof
title: Proof that a least nonresidue gives a block without smooth members
desc: |
  A term u of the block with all prime factors below q would be a quadratic
  residue, and so would p-u, which is below q; then -1 would be a residue,
  which fails for p = 3 (mod 4).
tags: []
sources:
- theory/integer_sequences/L252_nonresidue_blocks_without_smooth_members/_index
created: 2026-10-15T22:27:51Z
updated: 2026-10-15T22:27:51Z
---

# Proof that a least nonresidue gives a block without smooth members

***

This proves the whole statement of
[[theory/integer_sequences/L252_nonresidue_blocks_without_smooth_members/_index|L252]].
The argument is the case $k=2$ of the one Granville gives after his
Conjecture 4.4.2 (2008, section 4.4).

Let $p\equiv3\pmod4$ be prime and let $q$ be the least positive quadratic
nonresidue modulo $p$. Since $1$ is a residue, $q\ge2$. Since $-1$ is a
nonresidue for $p\equiv3\pmod4$, so is $p-1$, and $q\le p-1$. Every integer
$a$ with $1\le a<q$ is a quadratic residue modulo $p$, by the minimality of
$q$. Consequently every positive integer whose prime factors are all less
than $q$ is a quadratic residue modulo $p$: it is a product of residues, and
it is prime to $p$ because each of its prime factors is less than
$q\le p-1$.

Let $u$ be one of the integers $p-q+1,\ldots,p-1$, and suppose that every
prime factor of $u$ is less than $q$. Then $u$ is a residue. The integer
$p-u$ satisfies $1\le p-u\le q-1$, so it is a residue too (for $p-u=1$
trivially). Since $p-u\equiv-u\pmod p$ and $u$ is invertible modulo $p$,

$$
-1\equiv(p-u)\,u^{-1}\pmod p
$$

is a product of two residues, hence a residue. This contradicts
$p\equiv3\pmod4$. So every term of the block has a prime factor at least
$q$.

For the consequence, put $m:=p-q$ and $k:=q-1$. Then $1\le m\le p$ and
$k\ge1$, and each of $m+1,\ldots,m+k$, which are the integers
$p-q+1,\ldots,p-1$, has a prime factor at least $q$, that is, greater than
$k$. By the definition of $k(n)$ this gives $k(p)\ge q-1$, and the witness
$m$ is positive. $\square$
