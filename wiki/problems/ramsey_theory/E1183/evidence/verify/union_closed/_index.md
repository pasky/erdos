---
name: problems/ramsey_theory/E1183/evidence/verify/union_closed
title: Whole-proof record for the union-closed-family bounds
desc: A distinct PASS grade covers eight precise F and F_k conclusions; lower bounds have no unread theorem premise, while upper bounds retain Sauer–Shelah as an explicit external premise.
created: 2026-10-15T23:59:17Z
updated: 2026-10-15T23:59:17Z
---

# Whole-proof record for the union-closed-family bounds

[[problems/ramsey_theory/E1183/evidence/verify/_index|..]]

[[problems/ramsey_theory/E1183/evidence/verify/union_closed/grade|grade]]: Independent grade of the unchanged whole-proof examination of the eight specified arXiv v1 union-closed-family bounds, including its primary independence record and external-premise limits.

[[problems/ramsey_theory/E1183/evidence/verify/union_closed/report|report]]: Independent adversarial examination of the complete union-closed-family bounds in Theorems 1.1 and 1.2 and Corollary 1.3 of the specified arXiv version.

***

The [whole-proof examination](report.md) and [distinct independent grade](grade.md),
both dated 2026-10-15 UTC, cover Theorems 1.1 and 1.2 and all four clauses of
Corollary 1.3 of Deep Bhattacharjee, Priyabrata Mandal and Ushashi Bhattacharya,
*Resolving Erdos-Ulam Monochromatic Union-Closed Family Conjectures*,
[arXiv:2610.02833v1](https://arxiv.org/abs/2610.02833v1).
The report's verdict is **refutation-failed** for all eight precise conclusions;
the separate grade is **PASS** for all eight and the report as a whole.
The [source claim](../../../claims/2026_09_30_bhattacharjee_mandal_bhattacharya.md)
remains pending catalog acceptance. No formal execution or original-PDF fidelity
is certified, and the sublattice quantity $f$ is outside the examination.

## Scope and composition

All $2^n$ subsets are colored, unused colors are allowed, and a family need only
be closed under binary union; it need not contain the empty set. $F_k(n)$ is
the minimum over $k$-colorings of the maximum cardinality of such a monochromatic
family, with $F=F_2$. The bound counts actual members, not generators.

For every fixed integer $k\ge2$ and $t\ge1$, put
$M=t^2k^{2^t}$ and $c_{k,t}^{-1}=k^{2^t+1}t^t(4M^2)^{t+1}$.
The lower argument proves $F_k(n)\ge c_{k,t}n^{t+1}$ for every $n\ge1$;
for two colors, $\log_2 n\ge(t+2)^2 2^t$ suffices for $F(n)\ge n^t$.
Its box inequality, shape selection, slice extension, incidence count,
union rule and injection into distinct family members are all supplied and
examined. In particular, for $n\ge2$ and $\ell=\log_2\log_2n$,
$F(n)\ge n^{\ell-2\log_2(\ell+2)-1}$, with an exponent tending to infinity.
These lower conclusions have no unread external theorem premise.

The upper argument gives $F(n)\le\sum_{j<d}\binom nj$ whenever
$2^d>nd+2$, using distinct nonempty unions of a private-element system.
Its sole external theorem premise is the finite Sauer–Shelah statement:
VC dimension at most $q\ge0$ implies cardinality at most
$\sum_{j=0}^q\binom nj$, with zero terms beyond $n$.
The examination checks the supplied statement and its application at $q=d-1$;
neither original Sauer nor Shelah proof was read. That qualification survives
in the explicit bound, subexponential conclusion, exponent comparison and the
upper half of the fixed-color extension. The lower half does not consume it.

The grade preserves every floor, small case and strict inequality, including
the explicit choice
$d=\lfloor\log_2n\rfloor+\lfloor\log_2\lfloor\log_2n\rfloor\rfloor+3$
for $n\ge2$, and all-positive-$n$ strict subexponential inequalities.
The color count is fixed before the lower-growth limit; no growing-color
uniformity follows. Exact statements and eight separate grades are in the
[graded account](grade.md), with the complete deductions in the report.

## Reading, evidence and filing

The [assessed subject](../../assets/union_closed/subject/manifest.json) retains
all fifteen supplied files, including the four static figure sources.
Reproduction is analytic: the report gives the complete reading route and
independent derivations; there is no mathematical executable or numerical
certificate to replay. Gowers's method credit and the original Sauer/Shelah
references are retained. The excerpt license and authorship are in
[the attribution record](../../assets/union_closed/ATTRIBUTION.txt).
The examined arXiv version is distinct from the initial Zenodo 23050880;
related Zenodo 23067141 is not substituted for it.

The independent grader found the visible primary records sufficient to
establish the reviewer's separation and absence of consumed excluded material.
The historical inbox was unavailable, not known empty. That limitation and the
grader's content-based sufficiency ruling remain in the grade. Raw operational
records remain private and are not mathematical premises.

The [submitted assessment](../../assets/union_closed/report.md) and
[submitted grade](../../assets/union_closed/grade.md) preserve their mathematical
findings. Filing maintains their relative paths, replaces private locations by
public subject locators, omits private custody identities and operating
directives from metadata, and clarifies that raw primary records stay private.
The source mathematical payloads, deductions, verdicts, dates, premise limits
and examined scope are unchanged. Report line locators refer to the retained
assessment, whose line positions are preserved. No later repair inherits this
warrant. Source authors retain theorem/proof credit; Plasma AI receives the
extraction and independent-derivation credit.
