---
name: diophantine_problems/ulas_2013_note_erdos_straus_erdos_graham/theorem_a_1
title: Schinzel Theorem A.1 — finitely many solutions along a progression with a > 1
desc: >
  For f(x) = ax + b with a > 1 and gcd(a, b) = 1, each n has only finitely
  many k with f(n+1)...f(n+k) | f(n+k+1)...f(n+2k); the printed choice of
  prime needs a small repair when n >= 1.
created: 2026-10-14T23:03:05Z
updated: 2026-10-14T23:03:05Z
---

***

**Source.** Published p. 597, Appendix A by A. Schinzel, Theorem A.1, with
its proof.

**Statement.** Let $a\ge2$ and $b$ be coprime integers (the condition (A.1)
of the appendix, with $a>1$), and put $f(x)=ax+b$. Then for every $n$ only
finitely many positive integers $k$ satisfy

$$
f(n+1)f(n+2)\cdots f(n+k)\mid f(n+k+1)f(n+k+2)\cdots f(n+2k).
$$

The print says "for every $n$"; the appendix addresses Question 4.1, where
$n$ is a positive integer.

**Proof sketch.** Fix $n$. For every large $k$ there is a prime $p$ with
$p\equiv b\pmod a$, $p>an+b$ and

$$
\frac{(2k+n)a+b}{a+1}<p\le ak+b,
$$

since the ratio of the two ends tends to $(a+1)/2>1$ and the primes in a
residue class prime to $a$ have their expected density in such intervals.
Put $m=(p-b)/a$, an integer with $n<m\le k$ and $f(m)=p$, so $p$ divides the
left product through its factor $f(m)$. As $p\nmid a$, $p$ divides $f(x)$
exactly when $x\equiv m\pmod p$. The arguments $x=n+k+1,\dots,n+2k$ of the
right product avoid that class: $m\le k<n+k+1$, and
$m+p=((a+1)p-b)/a>2k+n$. So $p$ divides no factor on the right, and the
divisibility fails for every large $k$.

**Source note.** The print takes $p$ in $((2ka+b)/(a+1),ak+b]$, which gives
only $m+p>2k$. That keeps $p$ off the right product when $n=0$, but for
$n\ge1$ the number $m+p$ can fall in $(2k,2k+n]$, and then the right product
contains the factor $f(m+p)=(a+1)p$. Taking $p$ above $((2k+n)a+b)/(a+1)$,
as above, closes the gap at no cost for fixed $n$.

**Dependencies.** Primes in a residue class prime to $a$ in intervals
$(cx,x]$, for fixed $c<1$ and all large $x$, which the prime number theorem
for arithmetic progressions supplies; the print uses this without a
reference.

**Read depth.** Claims checked: the statement was read clause by clause on
the page image, and the proof was followed; the gap above was found in that
reading. Nothing here is independently reviewed.

**Bears on.** [[../wiki/problems/diophantine_problems/E0389/_index|#389]]:
the problem's divisibility is the case $f(x)=x$, at $n$ shifted by one, and
the paper notes that Question 4.1 with $f(x)=x$ is Question 1.1 (p. 595).
The theorem shows that along every progression $ax+b$ with $a\ge2$ each $n$
has only finitely many solutions, unlike the infinitely many that
[[diophantine_problems/ulas_2013_note_erdos_straus_erdos_graham/theorem_2_2|Theorem 2.2]]
gives for $f(x)=x$ at $n=1,2$ and that Conjecture 2.10 predicts for every
$n$; it says nothing about the case $f(x)=x$ itself.
