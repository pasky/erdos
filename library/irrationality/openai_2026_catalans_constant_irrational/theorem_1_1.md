---
name: irrationality/openai_2026_catalans_constant_irrational/theorem_1_1
title: "Theorem 1.1: Catalan's constant is irrational"
desc: |
  The manuscript's only theorem: Catalan's constant G, the sum of
  (-1)^j/(2j+1)^2 over j >= 0, is irrational; a qualitative statement with no
  irrationality measure. Claims checked only.
created: 2026-10-12T23:13:55Z
updated: 2026-10-12T23:13:55Z
---

***

## Statement

Catalan's constant is
$G=\beta(2)=\sum_{j\ge0}(-1)^j/(2j+1)^2$, where
$\beta(s)=\sum_{j\ge0}(-1)^j(2j+1)^{-s}$ for $s>0$ is the Dirichlet beta
function; equivalently $G=L(2,\chi_{-4})$ for the odd quadratic character of
conductor $4$ (p. 1).

**Theorem 1.1.** $G$ is irrational.

The statement is qualitative. The manuscript says its argument gives no
irrationality measure, which "would require additional control of rational
approximations" (p. 3). Its closing paragraph (p. 42) draws two
consequences, not separately labeled: by Agol's theorem, $4G$ is the least
volume of an orientable complete finite-volume hyperbolic 3-manifold with
exactly two cusps (curvature $-1$), attained by the Whitehead-link and
$(-2,3,8)$-pretzel-link complements, so that minimum and both link volumes
are irrational; and, by Voight's volume formula with
$\zeta_{\mathbb Q(i)}(2)=\zeta(2)G$, every orientable arithmetic
hyperbolic 3-orbifold defined over $\mathbb Q(i)$ has volume a positive
rational multiple of $G$, hence irrational, for example
$\operatorname{vol}(\mathrm{PSL}_2(\mathbb Z[i])\backslash\mathbb H^3)=G/3$.

**Formalization.** The release's Lean page for the family describes a
formalization of this statement, with the comparator theorem
`OAI.InternalCatalan.catalan_irrational`. In words, it says that the real
number given by Mathlib's unconditional sum over all natural numbers $j$ of
$(-1)^j/(2j+1)^2$ is irrational; the terms are absolutely summable, so that
sum is $G$. The hyperbolic-volume consequences are not part of it. It was
read statically and not built or audited here, and the catalog lists no
entry for it at this revision (see the card).

**Source.** OpenAI, *Catalan's constant is irrational*, release folder
`preprints/Catalans-constant-is-irrational-September-24-2026`; TeX file
`build/sections/introduction.tex`, label `thm:main` (lines 16--18), PDF p. 1;
the proof closes in Section 8 (`build/sections/conclusion.tex` lines 3--16,
PDF p. 42). Read 2026-10-12. Provenance and attestations are on
[[irrationality/openai_2026_catalans_constant_irrational/_index|the card]].

**Read depth.** Claims checked: the statement and the definition of $G$
(`introduction.tex` lines 3--8 and 16--18), the definition of $\Delta_N$, the
statements of Propositions 2.1, 3.4, 4.1 and 7.1, which the closing proof
combines, and of Proposition 2.2, which feeds the constant of
Proposition 3.4, and the closing proof itself were read clause by clause in
the TeX source. The proof (pp. 3--42) was read for its structure only, as
summarized below; no step was checked, and none of the finite certificates
(the pivots modulo $101$, the root brackets, the value bounds) was
recomputed. The
hyperbolic-volume consequences were read as stated and not checked against
Agol or Voight. Nothing here is independently reviewed.

## Proof pointer

The proof is by contradiction. Suppose $G\in\mathbb Q$. For each $N$ the
manuscript builds a determinant $\Delta_N$ of size $n=48N$ (Section 2). Its
rows come from integer polynomials $P_r$, $D_r$ (Chebyshev polynomials at
$1/t$ times $(1-t)^{2N}t^{63N-1}$), built from one rational expression and
its image under the involution $w\mapsto1/w$ of the parametrization
$t=2w/(1+w^2)$. Its columns are filtered by $s^{7N+k}(1-s)^{4N}$. Each
entry combines two double-integral moments with kernel $1/(1-ts)$, one
weighted by $|t|/\sqrt{1-t^2}$ on $(-1,1)$, the other on $(0,1)$. Each
moment is an explicit element of $\mathbb Q+\mathbb QG+\mathbb Q\zeta(2)$.
With $f=\sqrt{1-t^2}$, the rows satisfy the Taylor contact
$tP_r/f-D_r=O(t^{59N})$, so the $\zeta(2)$ part cancels in every entry
used (Proposition 2.1). Hence every $\Delta_N$ is rational.

The lower bound is arithmetic. For a nonzero rational $\Delta_N$, the
product formula gives $\log|\Delta_N|=\sum_pv_p(\Delta_N)\log p$, so bounds
on denominators give a lower bound. Proposition 2.2 handles $p=2$. Section 3
handles odd primes up to $65N$: digit reductions modulo $p$ of the rational
moment arrays (Lemma 3.1), pairing of columns, a central-layer reduction
(Lemma 3.2) and integral column elimination (Lemma 3.3) track
denominators $p^2$ and $p$ separately.
Summing these losses with the prime number theorem gives Proposition 3.4: the
lower limit of $\log|\Delta_N|/n^2-\tfrac12\log2$ along nonzero determinants
exceeds $-2.29084$. Nonzero determinants exist along the primes: for $N=p$
a large prime, Proposition 4.1 uses Frobenius and two palindromic bases over
$\mathbb F_p$ to reduce the scaled matrix to a block form. Its determinant
is a power of $2$ times powers of the determinants of three fixed rational
$48\times48$ matrices. Gaussian elimination modulo $101$ shows these three
determinants are nonzero, so $v_p(\Delta_p)=-96p$ exactly.

The upper bound is analytic and needs no hypothesis on $G$. Andréief's
identity turns $\Delta_N$ into a multiple integral. Cauchy's double
alternant and the change of variable $x=t/(1+\sqrt{1-t^2})$ leave a row
determinant that mixes evaluations at $x_i$ and $1/x_i$. When
$\sum_i(1-x_i^2)/(1+x_i^2)\le40N-1$, a bounded interpolating function
(Lemma 5.1) and a Hilbert-space compression bound that determinant
(Proposition 5.2); otherwise Hadamard's inequality does (Proposition 5.3).
Proposition 6.1 expands the logarithmic interactions in Chebyshev
polynomials and bounds them by quadratic terms in two trial sequences plus
two one-variable suprema. Section 7 chooses explicit rational trial
sequences and certifies those suprema exactly: Descartes root counts, root
brackets of width $2\cdot10^{-10}$, rational interval values and a
derivative bound. This gives Proposition 7.1: the upper limit is at most
$-2.290939875$.

Along large primes the two limits contradict each other, since
$-2.29084>-2.2909$. The manuscript compares only these rounded values and
states no margin. Computed for this page, not taken from the manuscript:
the exact lower constant of Proposition 3.4,
$-\tfrac{8609}{4608}-\tfrac{2809}{4608}\log2\approx-2.29081$, exceeds the
upper constant $-2.290939875$ of Proposition 7.1 by about
$1.3\cdot10^{-4}$. A margin this small leaves little room for error in the
constants of Propositions 2.2, 3.4 and 7.1.

## Dependencies

External inputs, taken at statement level; none was checked here. The prime
number theorem $\theta(y)\sim y$ (cited to Zagier's account of Newman's
proof); Andréief's integration identity (cited to Forrester); Cauchy's
double alternant (cited to Krattenthaler); the Chebyshev expansion of the
logarithmic kernel, Haagerup's identity as in Garoufalidis and Popescu
(Lemma 3.1); the Laurent formulas for Chebyshev polynomials (DLMF,
equations 18.5.1--18.5.2). Descartes' rule of signs is cited and its needed
form proved in the text, and Sarason's interpolation viewpoint is cited as
context with the finite-dimensional facts proved directly. The hyperbolic
consequences rest on Agol (2010, Theorem 3.6) and Voight (2021,
Definition 38.3.4, Theorem 39.1.13 and Example 39.1.16). Sun's preprint
announcing the same theorem is cited and explicitly not used.

## Bears on

The manuscript names no Erdős problem, and no problem page is identified as
using this result.
