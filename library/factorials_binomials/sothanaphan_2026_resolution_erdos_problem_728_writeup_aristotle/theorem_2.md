---
name: factorials_binomials/sothanaphan_2026_resolution_erdos_problem_728_writeup_aristotle/theorem_2
title: "Theorem 2 (p. 13): density-one valuation gap and its deductions"
desc: |
  For absolute c_1, c_2 > 0 the set of m for which nu_p(C(2m,m)) -
  nu_p(C(m+k,m)) >= c_2 (log m / log p) [p <= 2k] for every prime p and every
  0 <= k <= exp(c_1 sqrt(log m)) has density 1; the appendix deduces Problems
  728, 729 and 401 from it.
created: 2026-10-13T13:47:56Z
updated: 2026-10-13T13:47:56Z
---

***

**Source.** Theorem 2 and the deductions after it, appendix "beyond this
proof", pp. 13--14, of Nat Sothanaphan, *Resolution of Erdős Problem #728: a
writeup of Aristotle's Lean proof*, arXiv:2601.07421v5, the held version
named on the
[[factorials_binomials/sothanaphan_2026_resolution_erdos_problem_728_writeup_aristotle/_index|source card]].

## Statement

**Theorem 2** (p. 13). There are absolute constants $c_1,c_2>0$ such that
the set $S$ of $m\in\mathbb N$ for which, for every integer $k$ with
$0\le k\le\exp(c_1\sqrt{\log m})$ and every prime $p$,

$$
\nu_p\!\left(\binom{2m}{m}\right)-\nu_p\!\left(\binom{m+k}{m}\right)
\ge c_2\frac{\log m}{\log p}\,[p\le2k],
$$

has asymptotic density $1$. Here $[p\le2k]$ is $1$ when $p\le2k$ and $0$
otherwise.

**Deductions** (p. 14). The paper derives three problem consequences for
$m\in S$; the chosen $k$ lies in the theorem's range once $m$ is large (an
observation of this page).

- For Problem 728, the left side of the display is nonnegative, which gives
  $\binom{m+k}{m}\mid\binom{2m}{m}$.
- For Problem 729, for every $c>0$ take $k=\lfloor c\log m\rfloor$. There is
  a threshold $p_{\min}(c)$ such that no prime $p\ge p_{\min}(c)$ divides the
  denominator of $(2m)!/(m!\,(m+k)!)$; by Theorem 2 it suffices that
  $c_2\frac{\log m}{\log p}[p\le2k]-\nu_p(k!)\ge0$, which the paper checks
  from $\nu_p(k!)\le k/(p-1)$ for large $p$, depending only on $c$.
- For Problem 401, the same examples work with the extra condition
  $\nu_p(m!)+\nu_p((m+k)!)-\nu_p((2m)!)\le2m$ for the small primes, depending
  on $c$, which holds because Legendre's formula makes the left side
  $O(\log m)$.

The paper then compares these results with Pomerance's density-one
divisibility theorems for $\binom{2m}{m}$ (p. 14), as context.

**Read depth.** Claims checked: Theorem 2 and the three deductions were read
clause by clause on the PDF page images of pp. 13--14. The proof of Theorem 2
was read but not checked step by step. Not independently reviewed.

## Proof pointer

pp. 13--14. Following the reductions of Sections 3--4 (see
[[factorials_binomials/sothanaphan_2026_resolution_erdos_problem_728_writeup_aristotle/theorem_1|Theorem 1]]),
$m\in S$ follows from $\kappa_p(m)-V_p(m,k)\ge c_2\log m/\log p$ for the
primes $p\le2k$. On $[M,2M]$ the proof leaves the spike threshold $t(M)$
open; Lemma 7 then gives a gap of this form, and the union bound of Lemma 13
still gives $|\mathrm{Bad}(M)|=o(M)$ once $t(M)$ is of order
$\sqrt{\log M}$, a choice that Lemma 7 still allows.

## Dependencies

Lemmas 7 and 13 (pp. 7 and 9) and the reductions of Sections 3--4, on the
[[factorials_binomials/sothanaphan_2026_resolution_erdos_problem_728_writeup_aristotle/theorem_1|Theorem 1]]
page; Legendre's formula.

## Bears on

- [[../wiki/problems/factorials_binomials/E0728/_index|Problem 728]]: the
  binomial divisibility behind the problem's examples, for a density-one set
  of $m$.
- [[../wiki/problems/factorials_binomials/E0729/_index|Problem 729]]: its
  deduction's examples, with gap $\lfloor c\log m\rfloor$ for every $c>0$.
- [[../wiki/problems/factorials_binomials/E0401/_index|Problem 401]]: its
  deduction, the same examples under the extra small-prime condition.
