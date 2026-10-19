---
name: theory/integer_sequences/L123_odd_root_arc_colorings/_proof
title: Proof that argument arcs give dissociated colorings
desc: |
  A signed relation inside an arc is a flat multiple of the cyclotomic
  polynomial of low degree, the largest arc absorbs a rotated shortest
  relation, and substituting a power of x transports flat multiples.
tags: []
sources:
- theory/integer_sequences/L123_odd_root_arc_colorings/_index
created: 2026-10-15T11:14:17Z
updated: 2026-10-15T11:14:17Z
---

# Proof that argument arcs give dissociated colorings

***

This proves the whole statement of
[[theory/integer_sequences/L123_odd_root_arc_colorings/_index|L123]].

**Dissociation and signed relations.** For a finite set $S$ of complex
numbers, distinct subsets $X\ne Y$ with equal sums give the nonzero signed
relation $\sum_{x\in X\setminus Y}x-\sum_{y\in Y\setminus X}y=0$ with
coefficients in $\{-1,0,1\}$; conversely the positive and negative parts of
a nonzero relation with coefficients in $\{-1,0,1\}$ are distinct subsets
with equal sums. A set is therefore dissociated exactly when it carries no
nonzero relation with coefficients in $\{-1,0,1\}$, here called a signed
relation. Every set of $N$-th roots of unity is finite, and $D(N)$ is
defined, since $1+x+\cdots+x^{N-1}$ is a multiple of $\Phi_N$ with all
coefficients equal to one.

**Signed relations in consecutive powers.** Let $f$ be a nonzero map from
$\{a,a+1,\ldots,a+\ell-1\}$ to $\{-1,0,1\}$ with
$\sum_jf(j)z^j=0$. The polynomial $P(x)=\sum_{i<\ell}f(a+i)x^i$ is nonzero,
has degree at most $\ell-1$ and satisfies $P(z)=z^{-a}\sum_jf(j)z^j=0$.
Since $\Phi_N$ is the minimal polynomial of $z$ over $\mathbb Q$, it divides
$P$, so $\ell-1\ge D(N)$. Conversely, if $P=\sum_{i\le D}c_ix^i$ is a
nonzero multiple of $\Phi_N$ with coefficients in $\{-1,0,1\}$ and degree
$D=D(N)$, then $\sum_ic_iz^{a+i}=z^aP(z)=0$ for every integer $a$, a signed
relation among the $D(N)+1$ consecutive powers $z^a,\ldots,z^{a+D(N)}$.
Exponents are read modulo $N$; distinct exponents below $N$ give distinct
roots, and $D(N)+1\le N$ by the multiple displayed above.

**Part (1).** The class $C_j$ consists of $z^e$ for the integers $e$ in the
half-open interval $[jN/q,(j+1)N/q)$, which has length $N/q$. So $C_j$ is a
set of at most $\lceil N/q\rceil$ consecutive powers, and some class has
exactly $\lceil N/q\rceil$ of them, because the class sizes are $\lfloor
N/q\rfloor$ or $\lceil N/q\rceil$ and sum to $N$ (when $q>N$ the sizes are
$0$ or $1$, and a class of size one has $\lceil N/q\rceil=1$ powers). If
$qD(N)\ge N$ then $\lceil N/q\rceil\le D(N)$, since $D(N)$ is an integer at
least $N/q$; a signed relation inside a class would lie in at most $D(N)$
consecutive powers, which the previous paragraph excludes. So every class is
dissociated. If $qD(N)<N$, then $D(N)<N/q$ gives
$D(N)+1\le\lceil N/q\rceil$, and the class with $\lceil N/q\rceil$
consecutive powers $z^a,\ldots$ contains $z^a,\ldots,z^{a+D(N)}$, which carry
a signed relation; that class is not dissociated.

**Part (2).** Let $P$ be a nonzero multiple of $\Phi_M$ with coefficients
in $\{-1,0,1\}$ and degree $D(M)$, and put $Q(x)=P(x^{N/M})$. Its
coefficients are those of $P$, placed at the multiples of $N/M$, so they lie
in $\{-1,0,1\}$, and $\deg Q=(N/M)D(M)$. The number $z^{N/M}$ is a primitive
$M$-th root of unity, so $P(z^{N/M})=0$, and $\Phi_N$ divides $Q$. Hence
$D(N)\le(N/M)D(M)$, which is the claim.

**Part (3).** Fix $q$ with $qc\ge1$ and suppose that one color class
carries a nonzero signed relation. Its support is a finite set of roots of
unity of odd squarefree orders; let $M$ be the least common multiple of
these orders, which is odd and squarefree. A single root of unity is not
zero, so the support has at least two elements, and $M>1$. Every element of
the support is an $M$-th root of unity $\exp(2\pi ie/M)$, $0\le e<M$, whose
color is the integer part of $qe/M$; so the support lies in one of the
classes of part (1) for $N=M$. By definition of $c$, $qD(M)\ge qcM\ge M$,
and part (1) says that class is dissociated, a contradiction. Every root of
unity of odd squarefree order receives exactly one of the $q$ colors, so
the classes partition that set. $\square$
