---
name: research/erdos_1221/all_sequence_composition
title: "The three consecutive-gap growth bounds over all sequences: the composed argument"
desc: "The composed all-sequence consecutive-gap argument, with independently graded ratio, one-sided and whole-conclusion warrants; the mean-normalized catalog claim remains pending."
problems: [1221]
created: 2026-10-15T07:30:49Z
updated: 2026-10-15T07:30:49Z
---

[[research/erdos_1221/_index|..]]

***

**Standing.** The ratio part is
[[theory/analysis/L163_all_sequence_span_ratio/_index|L163]] and the two
one-sided parts are
[[theory/analysis/L164_all_sequence_span_deviations/_index|L164]], each at
tier 1 on its own whole-statement examination and distinct passing grade.
Their conjunction is
[[theory/analysis/L165_consecutive_gap_growth_conjunction/_index|L165]],
recorded by Plasma AI at tier 1 on its own whole-conclusion examination and
[distinct passing grade](../../theory/analysis/L165_consecutive_gap_growth_conjunction/evidence/verify/whole_statement/grade.md),
examined on 2026-10-16 UTC. The accepted verdict is **refutation-failed** for
the complete conjunction and supplied mean-normalized formulation. Catalog
acceptance remains pending. The examination does not certify the original
publications or their historical interpretation.
The span-to-count mechanism and both closing arguments
are S. Korsky's, from the unrefereed preprint arXiv:2609.07196v2, which
states its theorem for sequences of distinct points; they are reconstructed on
the folder's `ko26b` pages. The finite-list input follows Larcher's range
splitting, and the planar input is Halász's theorem as Bilyk's survey
presents it. The reading for coincident terms, the finite-list bound, the
write-up of the planar bound with constants, and this composition are credited
to Plasma AI.

## Target

[[problems/analysis/E1221/_index|Problem 1221]], in its mean-normalized
reading, asks whether $\Lambda_r-r$, $r-\lambda_r$ and $r(\mu_r-1)$ tend to
infinity. The constants are taken over all sequences on the circle, coincident
terms allowed, as in the erdosproblems.com wording and Section 1 of the 1949
note.

**The all-sequence circle model.** Let $X=(x_n)_{n\ge1}$ be any sequence on
$\mathbb T=\mathbb R/\mathbb Z$. At time $n$ the labels $1,\ldots,n$ are
ordered cyclically by position, coincident terms by index. Let
$y_1\le\cdots\le y_n$ be their positions in this order on a lift to
$\mathbb R$, extended by $y_{i+n}=y_i+1$. The $n$ gaps $y_{i+1}-y_i\ge0$ sum to
$1$, and for $n\ge r$ the $r$-span from the label in place $i$ is
$y_{i+r}-y_i\in[0,1]$. Each gap lies in exactly $r$ spans, so the spans sum to
$r$ (the mean identity) and $nm_n^{(r)}\le r\le nM_n^{(r)}$, where
$M_n^{(r)}$ and $m_n^{(r)}$ are the largest and smallest $r$-spans. Counts
$N_n(I)$ of arcs count labels, that is, terms with multiplicity. Counting
intervals $(x,x+\ell]$ have $\ell<1$; the lifted span arcs in the covering
identity below may also have length $1$. All logarithms are natural unless
a base is displayed. The constants are

$$
\Lambda_r=\inf_X\limsup_{n\to\infty}nM_n^{(r)},\qquad
\lambda_r=\sup_X\liminf_{n\to\infty}nm_n^{(r)},\qquad
\mu_r=\inf_X\limsup_{n\to\infty}\frac{M_n^{(r)}}{m_n^{(r)}},
$$

with $M/0=+\infty$.

**Quantifiers.** An infimum is at least a number exactly when every member is.
So $\Lambda_r-r\ge K$ holds when every sequence has
$\limsup_n(nM_n^{(r)}-r)\ge K$; $r-\lambda_r\ge K$ when every sequence has
$\limsup_n(r-nm_n^{(r)})\ge K$; and $r(\mu_r-1)\ge K$ when every sequence has
$\limsup_nM_n^{(r)}/m_n^{(r)}\ge1+K/r$. Here
$\limsup_n(r-nm_n^{(r)})=r-\liminf_{n\to\infty}nm_n^{(r)}$. No limit is exchanged
with the infimum or the supremum.

**Theorem (composed; L165, tier 1).** There are absolute constants $c>0$
and $r_0$ such that, for every integer $r\ge r_0$ and every sequence on
$\mathbb T$, coincident terms allowed,

$$
\limsup_{n\to\infty}\bigl(nM_n^{(r)}-r\bigr)\ge c\sqrt{\log r},\qquad
\limsup_{n\to\infty}\bigl(r-nm_n^{(r)}\bigr)\ge c\sqrt{\log r},\qquad
\limsup_{n\to\infty}\frac{M_n^{(r)}}{m_n^{(r)}}\ge1+\frac{\log r}{200\,r}.
$$

Consequently $\Lambda_r-r\ge c\sqrt{\log r}$, $r-\lambda_r\ge c\sqrt{\log r}$
and $r(\mu_r-1)\ge(\log r)/200$ for $r\ge r_0$, and all three expressions
tend to infinity. The argument runs for an arbitrary sequence, so it uses no
relation between the constants over all sequences and those over sequences of
distinct points; whether those constants agree remains unsettled and is not
needed.

## The links and their standing

The ratio part runs through these links:

- [[research/erdos_1221/ko26b_lemma_2_1_reconstruction|Lemma 2.1]], the
  cyclic-walk comparison of interval counts at nearby times;
- [[research/erdos_1221/ko26b_proposition_3_1_reconstruction|Proposition 3.1]],
  which iterates it to bound the counting error on every short arc by
  $3A+C_1A/\log(r/A)$;
- Proposition 1221.1 of the
  [[research/erdos_1221/connections|connections page]], which reads the terms
  of one short arc as a finite list, coincident terms allowed;
- Proposition FP of the
  [[research/erdos_1221/finite_list_prefix_bound|finite-list page]],
  $H_L\ge\lfloor\log_4L\rfloor/16$ for every list, in place of the imported
  Theorem 4.1;
- the comparison of Section 5, recomposed below with the coefficient $1/200$.

The one-sided parts run through these links:

- [[research/erdos_1221/ko26b_lemma_6_1_reconstruction|Lemma 6.1]],
  [[research/erdos_1221/ko26b_lemma_6_2_reconstruction|Lemma 6.2]] and
  [[research/erdos_1221/ko26b_lemma_6_3_reconstruction|Lemma 6.3]], the
  averaged comparison under one one-sided span bound;
- [[research/erdos_1221/ko26b_proposition_6_4_reconstruction|Proposition 6.4]],
  the resulting $L^1$ bound $C_3A$ on short arcs;
- [[research/erdos_1221/ko26b_lemma_7_2_reconstruction|Lemma 7.2]], the
  localization to planar point sets with insertion time as second
  coordinate;
- the [[research/erdos_1221/halasz_planar_l1_bound|planar $L^1$ bound]],
  Halász's theorem written out with $c_H=1/41000$, in place of the imported
  Theorem 7.1;
- the comparison of Section 8, recomposed below.

The reconstruction pages were independently reviewed, as reconstructions of
the distinct-point argument relative to its two imports, by the focused reviews
and grades that the [[research/erdos_1221/_index|folder index]] lists; the
statements of the connections page, Proposition 1221.1 among them, by the
focused reviews graded in
[[research/erdos_1221/evidence/verify/connections_grade|the connections
grade]]. Those reviews cover their own subjects as they then stood. The
complete ratio chain, including the finite-list page and its reading for
coincident terms, is examined and graded in
[[theory/analysis/L163_all_sequence_span_ratio/evidence/verify/whole_statement/_index|L163's record]].
The complete one-sided chain, including the planar page and its reading for
coincident terms, is examined and graded in
[[theory/analysis/L164_all_sequence_span_deviations/evidence/verify/whole_statement/_index|L164's record]].
Both records retain the exact mathematical subjects and their independence
qualifications. They examine the supplied local deductions; the original
publications remained unread by the reviewers and graders. The [whole-conclusion report](../../theory/analysis/L165_consecutive_gap_growth_conjunction/evidence/verify/whole_statement/report.md)
examines the conjunction and supplied formulation using those interfaces.
Its distinct whole-contract grade is **PASS** at that full scope, supporting
L165 at tier 1. The source attributions above and their original-publication
reading limits remain explicit.

## Reading the chain for coincident terms

The ko26b pages are written for distinct points. The following points make
each step valid for an arbitrary sequence. The earlier checklist on the
connections page made the same reading. The lower terminal bound and the
full-turn case of the covering identity below are arguments that the checklist
does not give.

**Labels and lifts.** The moves $F_s$ and $B_s$ by $kr$ places are bijections
of labels. The displacement of $F_s$ at the label in place $i$ is the lifted
difference $y_{i+kr}-y_i$, a sum of $k$ consecutive $r$-spans. Lemmas 2.1 and
6.2 use only these displacements as real numbers, positions modulo $1$ for
membership in arcs shorter than $1$, injectivity of maps between label sets,
and counts with multiplicity, so their proofs apply as written. Lemma 6.1 uses
only the mean identity, the decomposition of a $kr$-span into $k$ consecutive
$r$-spans, and the triangle inequality.

**The terminal bounds (3.2) of Proposition 3.1.** Let (2.1) hold at time $t$
with $a_t+b_t\le A$, and let $n=\lfloor t\rfloor$ be large.

- An arc $(x,x+(r-A)/t]$ holds at most $r$ labels. The labels in an arc form a
  contiguous block of the cyclic order. If there were $r+1$ of them, the first
  label of the block and the label $r$ places after it would both lie in the
  arc, and the $r$-span between them, which is the difference of their
  positions within the arc, would be less than $(r-A)/t\le(r-a_t)/t$, contrary
  to (2.1).
- An arc $I=(x,x+(r+A)/t]$ holds at least $r$ labels. Choose the lift so that
  $y_1\le\cdots\le y_n$ lie in $(x-1,x]$. The last label has position
  $y_n\le x$, and the next $r$ labels have lifted positions
  $y_1+1,\ldots,y_r+1$, which exceed $x$ and are at most
  $y_n+(r+b_t)/t\le x+(r+A)/t$, by (2.1) for the span from the last label. So
  these $r$ labels lie in $I$.

**The covering identity of Lemma 6.3.** For coincident terms a lifted span arc
$(y_{i-r},y_i]$ can have length $0$, an empty arc, or length $1$, a full turn.
Read each lifted arc modulo $1$. For $x$ at no position, with lift $\tilde x$,

$$
\sum_{i=1}^n\mathbf 1_{(y_{i-r},y_i]}(x)
=\sum_{i\in\mathbb Z}\mathbf 1\bigl[y_{i-r}<\tilde x\le y_i\bigr]=r,
$$

since the translates by integers of the arcs with $1\le i\le n$ are the lifted
arcs with $i\in\mathbb Z$, and if $j$ is the largest index with
$y_j<\tilde x$, exactly the indices $i=j+1,\ldots,j+r$ qualify. In the pairing
step, the arc of length $r/t$ ending at $y_i$ and the lifted arc of length
$y_i-y_{i-r}\in[0,1]$ ending at $y_i$ have indicators differing on a set of
measure $|y_i-y_{i-r}-r/t|$. So Lemma 6.3 holds as stated, without its
assumption that every span is shorter than $1$. That assumption also holds at
large times under either one-sided hypothesis: under $nM_n^{(r)}-r\le A$ every
span is at most $(r+A)/n<1$; under $r-nm_n^{(r)}\le A$ with $r>A$ and
$n\ge2r$, a span of length $1$ would leave $n-r\ge r$ consecutive zero gaps and
hence a zero $r$-span, contrary to $m_n^{(r)}\ge(r-A)/n>0$.

**Localization and extraction.** In Lemma 7.2 the planar points
$((x_i-a)/w,\,i/N)$ have distinct second coordinates, and the planar bound holds
for lists in any case. The least-distance step of Lemma 4.2 is replaced by
Proposition 1221.1, which chooses the short arc away from the positions of the
first $n_0$ terms by a measure argument.

**Positivity.** The one-sided hypotheses need no positive spans. Under the ratio
hypothesis every late $r$-span is positive, since a vanishing span makes the
ratio $+\infty$.

## The ratio part

Put $\alpha=1/200$ and $c_0=1/(16\log4)$, so that $3\alpha<c_0/2$ (already
$\log4<2$ suffices). Let $r$ be
large, put $A=\alpha\log r$, and suppose that some sequence has
$\limsup_nM_n^{(r)}/m_n^{(r)}<1+A/r$. Then there is $C<A$ with
$M_n^{(r)}/m_n^{(r)}\le1+C/r$ for all large $n$, and the mean identity gives
$n(M_n-m_n)\le C$ and $nM_n\le r+C$. As on the
[[research/erdos_1221/ko26b_theorem_1_1_reconstruction|Theorem 1.1 page]],
$a_t=r-nm_n$ and $b_t=tM_n-r$ with $n=\lfloor t\rfloor$ are nonnegative,
bound every $r$-span of the time-$t$ set between $(r-a_t)/t$ and $(r+b_t)/t$,
and satisfy $a_t+b_t\le C+(r+C)/n<A$ for all large $t$. This is hypothesis
(2.1).

For large $r$ we have $A\ge1$ and $r\ge C_0A$, so Proposition 3.1 gives, at
all late integer times and for every arc of length $D/n$ with $0\le D\le S$,
counting error at most $B$, where

$$
\Lambda=\log\frac rA,\qquad S=\frac{\sqrt{Ar}}{\Lambda^2},\qquad
B=3A+\frac{C_1A}\Lambda .
$$

Its hypotheses $B\ge1$ and $S\ge2$ hold for large $r$. Also
$\lfloor S\rfloor>B$ eventually, because $B=O(\log r)$ and
$S/(\log r)\to\infty$. Thus Proposition 1221.1 gives a nonempty list of
length $L'\ge\lfloor S\rfloor-B$ with $H_{L'}\le B$, and Proposition FP
gives

$$
B\ \ge\ c_0\log L'-\frac1{16}.
$$

As $r\to\infty$, $A/\Lambda\to\alpha$, so $B=3\alpha\log r+O(1)$, and

$$
\log S=\tfrac12\log r-\tfrac32\log\log r+O(1).
$$

Since $B=O(\log r)$ is much smaller than $S$, $L'\ge S/2$ for large $r$.
Therefore

$$
3\alpha\log r+O(1)\ \ge\ \frac{c_0}2\log r-\frac{3c_0}2\log\log r-O(1),
$$

which fails for all large $r$ because $3\alpha<c_0/2$. The implied constants
depend only on $\alpha$ and the absolute constants $C_0$, $C_1$, so the
threshold $r_0$ is independent of the sequence. The time thresholds inside the
argument depend on the sequence, but only their existence is used. This proves
$\limsup_nM_n^{(r)}/m_n^{(r)}\ge1+\log r/(200r)$ for $r\ge r_0$.

## The one-sided parts

Let $C_2,C_3$ be the absolute constants of Proposition 6.4 and $c_4,S_0$ those
of Lemma 7.2 with the planar constant $c_H=1/41000$, and fix an absolute $c$
with $0<c<c_4/(2C_3\sqrt3)$. Let $r$ be large and suppose that some sequence
has $\limsup_n(nM_n^{(r)}-r)<c\sqrt{\log r}=:A$. Then $nM_n^{(r)}-r\le A$ for
all large $n$, the first alternative of hypothesis (6.1).

For large $r$: $A\ge1$, $C_3A\ge1$, $r\ge C_2A$,
$S=\sqrt{Ar}/\log^2(r/A)\ge S_0$, and $\log S\ge(\log r)/3$, because
$\log S=\frac12\log r+O(\log\log r)$. Proposition 6.4 gives hypothesis (7.1)
of Lemma 7.2 with $B=C_3A$ at all late integer times, and Lemma 7.2 gives

$$
C_3c\sqrt{\log r}=C_3A\ \ge\ c_4\sqrt{\log S}\ \ge\ c_4\sqrt{(\log r)/3},
$$

that is, $c\ge c_4/(C_3\sqrt3)$, contrary to the choice of $c$. If instead
$\limsup_n(r-nm_n^{(r)})<c\sqrt{\log r}$, the same argument runs with the second
alternative $r-nm_n^{(r)}\le A$; Lemmas 6.1--6.3 and Proposition 6.4 use one
alternative at a time, with the same constants. This proves the two one-sided
bounds for $r\ge r_0$.

## What remains

- **The conjunction and formulation.** No mathematical gap is identified in
  either separately examined part or in their composition. L165's
  whole-conclusion examination covers the common conventions, absolute
  quantifiers, separate limits, extremum directions, and exact match to the
  supplied mean-normalized statement, with verdict refutation-failed. Its
  distinct whole-contract grade is **PASS** for that entire scope. The
  conjunction's warrant is separate from the two input grades; catalog
  acceptance is still pending.
- **Constants.** $c$ is absolute but very small and is not computed; $r_0$ is
  very large, since the ratio part already needs $(\log r)/200\ge1$. The
  coefficient $1/200$ comes from the constant of Proposition FP. Korsky's
  coefficient $1/100$ would follow with the constant $1/16$ of his Theorem 4.1,
  which rests on Larcher's unchecked optimized lemmas.
- **An independent qualitative route.** The
  [[research/erdos_1221/larcher_finite_prefix_interface|interface page]]
  derives a uniform qualitative finite-list bound from compactness and
  Schmidt's countability corollary. Used in place of Proposition FP, it gives
  $r(\mu_r-1)\to\infty$ without a rate.
- **Standing of the problem.** The
  [[theory/analysis/L165_consecutive_gap_growth_conjunction/_index|proposed full conclusion]]
  has its independent whole-conclusion warrant at tier 1. The catalog record
  carries a pending full claim for the modified Statement; no accepted
  catalog solution is recorded. The printed first two expressions and the normalization
  issue remain explicitly distinguished on the problem page.
