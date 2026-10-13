---
name: factorials_binomials/sothanaphan_2026_resolution_erdos_problem_728_writeup_aristotle/theorem_1
title: "Theorem 1 (p. 2): logarithmic gap window for a!b! | n!(a+b-n)!"
desc: |
  For fixed 0 < C_1 < C_2 and 0 < epsilon < 1/2 there are infinitely many
  triples (a, b, n) with epsilon n <= a, b <= (1 - epsilon) n,
  a!b! | n!(a+b-n)! and C_1 log n < a+b-n < C_2 log n.
created: 2026-10-13T13:47:56Z
updated: 2026-10-13T13:47:56Z
---

***

**Source.** Theorem 1, p. 2, of Nat Sothanaphan, *Resolution of Erdős
Problem #728: a writeup of Aristotle's Lean proof*, arXiv:2601.07421v5, the
held version named on the
[[factorials_binomials/sothanaphan_2026_resolution_erdos_problem_728_writeup_aristotle/_index|source card]].

## Statement

**Theorem 1** (logarithmic gap window, p. 2). Fix $0<C_1<C_2$ and
$0<\varepsilon<1/2$. There are infinitely many $(a,b,n)\in\mathbb N^3$ with
$\varepsilon n\le a,b\le(1-\varepsilon)n$ such that

$$
a!\,b!\mid n!\,(a+b-n)!
\qquad\text{and}\qquad
C_1\log n<a+b-n<C_2\log n.
$$

The paper notes (p. 2) that its construction satisfies a much stronger
condition, with $a$ and $b$ extremely close to $n/2$, while the theorem
records only the size of $k=a+b-n$. Remark 1 (p. 2) records Tao's
observation that the result is not in its best possible form: the main
constraint of the method, in Lemma 13, allows $k$ up to
$\exp(c\sqrt{\log n})$ for some small $c>0$.

**Read depth.** Claims checked: the statement and Remark 1 were read clause
by clause on the PDF page image of p. 2. The proof (pp. 4--10) was read for
the pointer below but not checked step by step. The paper writes up a Lean
proof, the file `Erdos728b.lean` named on the source card; no local build was
run. Not independently reviewed.

## Proof pointer

Sections 3--5, pp. 4--10. With $n=2m$, $b=m$, $a=m+k$ and
$k=\lfloor c\log M\rfloor$ for $m\in[M,2M]$ (p. 4), the divisibility becomes
$\binom{m+k}{k}\mid\binom{2m}{m}$ (Lemma 1, p. 5), and by Lemmas 2 and 4
(pp. 5--6) it suffices that $V_p(m,k)\le\kappa_p(m)$ for every prime $p$,
where $V_p(m,k)=\max_{1\le i\le k}\nu_p(m+i)$ and
$\kappa_p(m)=\nu_p\binom{2m}{m}$ is the number of carries when adding $m+m$
in base $p$ (Lemma 3, p. 5). Primes $p>2k$ satisfy this for every $m$
(Lemma 5, p. 6). For $p\le2k$, Lemmas 6 and 7 (p. 7) reduce it to a carry
condition on the first base-$p$ digits of $m$ and a no-spike condition on
$V_p(m,k)$, and Lemmas 8--14 (pp. 8--10) count the failures by residue
classes and a Chernoff bound to find, for every large $M$, an $m\in[M,2M]$
good for all $p\le2k$. Section 5 (p. 10) takes $c\in(C_1,C_2)$, so that
$k/\log n\to c$, and lets $M\to\infty$.

## Dependencies

Kummer's theorem (Lemma 3, p. 5) and the Chernoff lower-tail bound (Lemma 10,
p. 8), both standard; Section 6 (pp. 10--11) maps the lemmas to the
declarations of `Erdos728b.lean`.

## Bears on

- [[../wiki/problems/factorials_binomials/E0728/_index|Problem 728]]: the
  examples the problem asks for, with $a,b\ge\varepsilon n$ and a gap
  $a+b-n$ above $C_1\log n$; the theorem also bounds the gap above by
  $C_2\log n$.
