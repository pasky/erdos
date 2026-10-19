---
name: analysis/pendyala_2026_radial_access_lemniscates/theorem_1_1
title: "Theorem 1.1 (p. 2): the radial-access threshold N* satisfies 4 <= N* <= 6"
desc: |
  Pendyala's main theorem, as claimed in an unrefereed preprint: every monic
  polynomial of degree at most three with all zeros in the closed unit disk
  has a radius from 0 to the unit circle on which its modulus stays at most
  1, and an explicit degree-six one has none, so the least degree at which
  length-one escape can fail is 4, 5 or 6.
created: 2026-10-14T22:51:14Z
updated: 2026-10-14T22:51:14Z
---

***

**Source.** The definitions on pp. 1--2, Theorem 1.1 on p. 2, Definition 2.1
and Proposition 2.2 on pp. 2--3 and Corollary 6.3 on p. 10 of Venkata
Siddharth Pendyala, *Radial access for polynomial lemniscates: the cubic
theorem and a degree-six obstruction*, SSRN preprint (2026),
doi:10.2139/ssrn.6850818, the edition named on the
[[analysis/pendyala_2026_radial_access_lemniscates/_index|source card]].

## Statement

**Setting** (pp. 1--2). $\mathbb D$ is the open unit disk. A polynomial is
admissible when it is monic, $f(z)=\prod_{k=1}^n(z-z_k)$, with every $z_k$ in
$\overline{\mathbb D}$. Its filled lemniscate is
$E_f=\{z\in\mathbb C:|f(z)|\le1\}$, which contains $0$ since
$|f(0)|=\prod_k|z_k|\le1$, and $C_f$ is the component of $E_f$ containing
$0$. $L(f)$ is the infimum of the lengths of rectifiable paths in $C_f$ that
begin at $0$ and end on $\partial\mathbb D$, with $L(f)=+\infty$ when there is
no such path, and $\Delta(f)=L(f)-1$. The radial-access threshold is

$$
N^*=\min\{n\ge1:\text{some admissible monic polynomial of degree }n\text{ has }\Delta(f)>0\},
$$

with $N^*=+\infty$ if no such $n$ exists.

**Definition 2.1** (p. 2). An admissible $f$ has zero detour if
$\Delta(f)=0$. A radius $[0,e^{i\theta}]=\{re^{i\theta}:0\le r\le1\}$ is safe
for $f$ if $|f(re^{i\theta})|\le1$ for $0\le r\le1$.

**Proposition 2.2** (Zero-detour criterion, p. 2). An admissible polynomial
has zero detour if and only if it has a safe radius. With the radial-barrier
functional (p. 3)

$$
\mathcal B(f)=\min_{\theta\in\mathbb R}\ \max_{0\le r\le1}|f(re^{i\theta})|,
$$

this reads: $\Delta(f)=0$ exactly when $\mathcal B(f)\le1$, and
$\Delta(f)>0$ exactly when $\mathcal B(f)>1$.

**Theorem 1.1** (Main theorem, p. 2). $4\le N^*\le6$: every admissible
polynomial of degree at most three has a safe radius, and an explicit
admissible polynomial of degree six has none.

**Corollary 6.3** (p. 10). $N^*\in\{4,5,6\}$.

The paper leaves the exact value of $N^*$ open (abstract, p. 1).

**For the problem page's $S(n)$.** A path from $0$ to $\partial\mathbb D$ has
length at least $1$, with equality only for a radius (p. 1), and a path in
$E_f$ that starts at $0$ lies in $C_f$. So the worst-case length $S(n)$ of
the problem page is $\sup_fL(f)=1+\sup_f\Delta(f)$ over admissible $f$ of
degree $n$, and $N^*=\min\{n\ge1:S(n)>1\}$. Theorem 1.1 then gives $S(n)=1$
for $n\le3$ and, through Theorem 6.2, $S(6)>1$. This translation is the
corpus's, not the paper's.

**Read depth.** Claims checked: the setting, Definition 2.1, Proposition
2.2, Theorem 1.1 and Corollary 6.3 were read clause by clause on the page
images. The proof of Proposition 2.2 (pp. 2--3) was read through and not
checked. The paper is an unrefereed preprint, and nothing here is
independently reviewed.

## Proof pointer

The paper combines (p. 10)
[[analysis/pendyala_2026_radial_access_lemniscates/theorem_5_1|Theorem 5.1]],
which gives $N^*\ge4$, with
[[analysis/pendyala_2026_radial_access_lemniscates/theorem_6_2|Theorem 6.2]],
which gives $N^*\le6$. Proposition 2.2 joins the radial and the metric
notions (pp. 2--3): a safe radius is a path of length $1$; conversely, if
$\Delta(f)=0$, paths in $C_f$ of lengths tending to $1$, parametrized
proportionally to arclength, have a uniformly convergent subsequence whose
limit $p$ satisfies $|p(t)|\le t$ and $|w-p(t)|\le1-t$ for a limit endpoint
$w$ on the circle, which forces $p(t)=tw$; as $C_f$ is closed, the radius
$[0,w]$ lies in it and is safe.

## Dependencies

[[analysis/pendyala_2026_radial_access_lemniscates/theorem_5_1|Theorem 5.1]]
(p. 7) and
[[analysis/pendyala_2026_radial_access_lemniscates/theorem_6_2|Theorem 6.2]]
(p. 9) of the same paper, with Proposition 2.2 (p. 2).

## Bears on

- [[../wiki/problems/analysis/E1120/_index|Problem 1120]]: in the problem
  page's worst-case reading $S(n)$, the theorem gives $S(n)=1$ for $n\le3$
  and $S(6)>1$, so the least $n$ with $S(n)>1$ is $4$, $5$ or $6$. It says
  nothing about the growth of $S(n)$.
