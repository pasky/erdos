---
name: irrationality/openai_2026_irrationality_exponent_pi_2/theorem_1_1
title: "Theorem 1.1: the irrationality exponent of pi is 2"
desc: |
  The manuscript's main claim: for every nu > 2, all large enough
  denominators q satisfy |pi - p/q| >= q^(-nu) for every integer p, so the
  irrationality exponent of pi is 2, with an ineffective threshold. Claims
  checked only.
created: 2026-10-12T23:13:55Z
updated: 2026-10-12T23:13:55Z
---

***

## Statement

For an irrational real number $x$, the manuscript defines the irrationality
exponent $\mu(x)$ as the supremum of the real $\nu>0$ for which
$0<|x-p/q|<q^{-\nu}$ holds for infinitely many coprime integers $p,q$ with
$q\ge2$; the pigeonhole principle gives $\mu(x)\ge2$ (p. 1).

**Theorem 1.1.** $\mu(\pi)=2$. In the quantitative form the manuscript
states: for every real $\nu>2$ there is an integer $Q(\nu)$ such that

$$
\left|\pi-\frac pq\right|\ge q^{-\nu}
\qquad\text{for all integers }p\text{ and }q\text{ with }q\ge Q(\nu).
$$

The manuscript adds (p. 1) that the inequality holds for every integer
numerator and denominator, whether or not the fraction is reduced; that
$Q(\nu)$ may depend on $\nu$ and is not obtained effectively; and that
exponent $2$ is not the same as a uniform bound $|\pi-p/q|\ge c/q^2$,
equivalently bounded continued-fraction partial quotients, which it does not
claim. The proof concludes with the strict inequality for large $q$, derives
the irrationality of $\pi$ rather than assuming it, and states that no
earlier irrationality bound for $\pi$ is used (pp. 4, 19).

**Formalization.** The release's Lean page for the family describes a
formalization of this statement, with the comparator theorem
`OAI.PiExponent.main`. In words, it says two things: for every real $\nu>2$
there is an integer $Q\ge2$ with $|\pi-p/q|\ge q^{-\nu}$ for all integers
$p$ and all integers $q\ge Q$; and the supremum of the set of $\nu>0$ for
which infinitely many rationals $r$ with reduced denominator at least $2$
satisfy $0<|\pi-r|<\operatorname{den}(r)^{-\nu}$ equals $2$. The Lean page
places the Flint–Hills consequence outside the formalized statement. It was
read statically and not built or audited here, and the catalog lists no
entry for it at this revision (see the card).

**Source.** OpenAI, *The irrationality exponent of $\pi$ is $2$*, release
folder `preprints/The-irrationality-exponent-of-pi-is-2-September-24-2026`;
TeX file `build/main.tex`, label `thm:main` (lines 64--71), PDF p. 1, with
the definition of $\mu$ at lines 50--56 and the remark at lines 73--78; the
proof closes at the end of Section 4 (`build/sections/conclusion.tex`, lines
55--156, PDF pp. 18--19). Read 2026-10-12. Provenance and attestations are
on [[irrationality/openai_2026_irrationality_exponent_pi_2/_index|the card]].

**Read depth.** Claims checked: the statement, the definition and the remark
were read clause by clause in the TeX source, as were the statements of
Theorem 2.1 (separated-weight interpolation), Proposition 3.4 (determinant
comparison) and Lemma 4.1 (choice of constants). The proof in Sections 2--4
(pp. 4--19) was read for its structure only, as summarized below; no step
was checked. Nothing here is independently reviewed.

## Proof pointer

The proof is by contradiction. Fix $\nu>2$ and suppose that arbitrarily
large denominators $q$ admit some $p$ with $|\pi-p/q|\le q^{-\nu}$. Write
$\mathrm i$ for the imaginary unit.

Interpolation (Section 2, pp. 4--11). Theorem 2.1 is stated for arbitrary
complex centers and does not involve $\pi$. Given integers $m,K\ge1$ and
positive rationals $w_0$, $v_0$ and $\theta<1$ with $K\theta^m<1$ and
$Kw_0\theta^m/v_0<1$, it chooses rational weights $w_1,\dots,w_m$ in turn,
each above a threshold that depends on the fixed data and the earlier
weights but not on the centers. Then at any $K$ points
$(1,c_{j1},\dots,c_{jm})$ whose $i$th coordinates are pairwise distinct for
each $i$, any choice of packets of Taylor coefficients in $t,u_1,\dots,u_m$
of weight below $H$ (weights $v_0$ on $t$ and $w_i/\theta$ on $u_i$), one
at each point, is realized simultaneously by a single polynomial in
$Y,X_1,\dots,X_m$ of weighted degree at most $H$
(weights $w_0,w_1,\dots,w_m$), expanded along $Y=1+t$,
$X_i=c_{ji}+u_i+\log(1+t)$; this holds for all large, suitably divisible $H$.
The key step is the curve inequality (Proposition 2.3): every irreducible
curve meeting the affine chart has weighted degree at least $1+\sigma$ times
its total weighted contact with these logarithmic curves at the centers. A
violating curve would carry auxiliary polynomials with excess vanishing,
whose derivatives along the commuting fields $Y\partial_Y+\sum_i\partial_{X_i}$
and $\partial_{X_i}$ then vanish on it. A chain of derivative zero sets
stabilizes on a component, where a weighted Bézout comparison of normal
bases (Lemma 2.2) and the separation of the weights force $dX_i=dY/Y$; a
residue argument shows this is impossible unless $Y$ is constant, and the
fiber $Y=1$ is excluded by a second auxiliary polynomial and the
distinctness of coordinates. The curve inequality makes $A-(1+\sigma)E$ nef
on the blowup of the jet ideal of the centers in a weighted projective
compactification, so $A-E$ is ample and Serre vanishing gives surjectivity.

Two bounds for one determinant (Section 3, pp. 12--17). Choose $m$ of the
assumed approximations $p_i/q_i$, set $w_i=\lceil\log q_i\rceil$, and take
the centers $c_{ji}=2\mathrm ijp_i/q_i$, $0\le j<K$, rational approximations
in $\mathbb Q(\mathrm i)$ to the periods $2\pi\mathrm ij$ of the exponential
function. After the logarithms are replaced by Taylor polynomials of length
about $F_0w_i/v_0$, Theorem 2.1 gives the interpolation matrix (columns the
monomials of weighted degree at most $H$, rows the Taylor coefficients at
the centers) full row rank, so a square minor $\Delta_H$ using every row is
nonzero. Clearing the denominators, powers of the $q_i$ and of
$\operatorname{lcm}(1,\dots,T_i-1)$, gives a nonzero Gaussian integer and
the lower bound of Lemma 3.1,
$\log|\Delta_H|/(MH)\ge-(1-\bar b)-E_{\mathrm{ar}}$, where $M$ is the number
of rows and $\bar b$ their average normalized transverse weight. For the
upper bound, Lemma 3.2 rewrites each row exactly, using
$e^{2\pi\mathrm ij}=1$, as a combination of Taylor tests at
$z=2\pi\mathrm ij+\log(1+t)$ of the entire functions
$f_{a,P}(z)=[u^a]P(e^z,z+u_1,\dots,z+u_m)$, with scalars carrying a factor
$e^{-\nu w\cdot(a-\beta)}$ from the approximation errors. Lemma 3.3 bounds
any determinant of such tests: rows with the same transverse index $a$ test
the same functions, so terms with a repeated Taylor degree cancel, and the
rest give a factor $\exp(-c\sum_an_a^2)$ with $c=(\log2)/4$. Proposition 3.4
splits the expansion of $\Delta_H$: if at least a fraction $\eta$ of the
rows have transverse weight at most $AH$, Cauchy–Schwarz over the few such
indices gives a collision saving of order $L$; otherwise the large indices
give approximation-error factors of order $\nu(A(1-\eta)-\bar b)$. Either
way the upper bound falls below Lemma 3.1 once $g>0$,
$E_{\mathrm{ar}}+E_{\mathrm{an}}<g$ and $cL>1+E_{\mathrm{ar}}+E_{\mathrm{an}}$,
with $g=\nu(A(1-\eta)-\theta)-(1-\theta)$.

Parameters (Section 4, pp. 17--19). Lemma 4.1 chooses rationals with
$\theta<A<B<1<C$, $\nu(A-\theta)>1-\theta$, $B<1/C$ and $B<C\theta<1$, by
taking $\theta=1-\delta$ and $A=1-b\delta$ with $1/2<b<1-1/\nu$; such a $b$
exists exactly when $\nu>2$. On this page's reading, this is the one step
that needs $\nu>2$: Section 3 states $\nu>2$ as a standing assumption, but
its estimates use only $\nu\ge1$. The proof fixes $F_0$, sets
$K=\lfloor C^m\rfloor$, $w_0=B^{-m}$ and $v_0=2K\theta^mw_0$, and takes the
dimension $m$ so large that the error terms depending on $m$ are small and
$cL>2$, which is possible because $L$ grows like $(B/A)^m/m$. Only then
does it pick the $m$ approximations, in turn, with denominators large enough
for the weight thresholds of Theorem 2.1 and for the remaining error terms;
since those thresholds do not depend on the centers, the choice is not
circular. Proposition 3.4 then gives the contradiction as $H\to\infty$. The
last paragraphs recover the irrationality of $\pi$ (exact representations
would be approximations of every exponent) and the lower bound
$\mu(\pi)\ge2$ by the pigeonhole principle.

## Dependencies

External inputs, taken at statement level; none was checked here. The
Bézout bound for isolated zeros of a complete intersection counted with
local multiplicities (Mondal's notes, Corollary VIII.3 and Section IV.4.2);
smooth projective models of curves, the standard properties of blowups and
Rees algebras, and Serre vanishing (the Stacks Project, Tags 0BXX, 02OS,
02ND, 02NS, 0AG6, 0AG7 and 0B5U); and the criterion that nef plus ample is
ample on a projective scheme (Lazarsfeld, *Positivity in Algebraic Geometry
I*, Corollary 1.4.10). The cancellation of repeated Taylor degrees follows
Laurent's interpolation determinants of exponential polynomials (Theorem 1
of his 2000 paper), applied within groups of rows, and the bound
$\log\operatorname{lcm}(1,\dots,n)\le4n\log2$ is proved in the text. The
earlier upper bounds for $\mu(\pi)$ that the introduction surveys are not
inputs.

## Bears on

No problem page is identified as using this result; the card's Bears on
section records the pages read for a possible use.
