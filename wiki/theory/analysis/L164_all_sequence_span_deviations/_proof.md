---
name: theory/analysis/L164_all_sequence_span_deviations/_proof
title: Proof of the two all-sequence span deviations
desc: Each one-sided span hypothesis yields uniform short-arc L1 control, contradicted by the complete planar discrepancy bound after localization.
created: 2026-10-15T20:39:29Z
updated: 2026-10-15T20:39:29Z
---

# Proof of the two all-sequence span deviations

***

Use the model in
[[theory/analysis/L164_all_sequence_span_deviations/_index|L164]]. All
supporting deductions below have full proofs on the linked research pages;
their examined portions are retained with the
[[theory/analysis/L164_all_sequence_span_deviations/evidence/verify/whole_statement/_index|whole-statement record]].

For fixed $r,A$, suppose one of the following holds at every sufficiently
large integer time, keeping the same alternative throughout:

$$
nM_n^{(r)}-r\le A,\qquad\text{or}\qquad r-nm_n^{(r)}\le A.
$$

The centered spans sum to zero. Either hypothesis bounds one of their
positive or negative masses by $A$, hence their total absolute mass by
$2A$. The proof of
[[research/erdos_1221/ko26b_lemma_6_1_reconstruction|Lemma 6.1]] carries this
to $kr$-span displacements at real time, retaining the floor error.
[[research/erdos_1221/ko26b_lemma_6_2_reconstruction|Lemma 6.2]] then uses
label injections to compare integrated count errors; it does not import a
pointwise two-sided span bound. The
[[research/erdos_1221/all_sequence_composition|real-lift and covering argument]]
handles coincident labels, empty span arcs and full turns, so the terminal
estimate of
[[research/erdos_1221/ko26b_lemma_6_3_reconstruction|Lemma 6.3]] applies.

The finite scale iteration in
[[research/erdos_1221/ko26b_proposition_6_4_reconstruction|Proposition 6.4]]
therefore gives absolute $C_2,C_3$ such that, for $A\ge1$ and
$r\ge C_2A$, all sufficiently large integer $n$ satisfy

$$
\int_{\mathbb T}|N_n((x,x+D/n])-D|\,dx\le C_3A
\quad(0\le D\le S),\qquad S=\frac{\sqrt{Ar}}{\log^2(r/A)}.
$$

There is one onset threshold for every $D$ in that interval. Both alternatives
use the same constants.

The complete
[[research/erdos_1221/halasz_planar_l1_bound|planar discrepancy proof]]
establishes the lower bound $\sqrt{\log M}/41000$ for every list of $M$
points in either anchored convention used in localization. The tensor Haar
coefficient argument includes boundary points; equality of the two discrepancy
norms is neither asserted nor needed. Applied through
[[research/erdos_1221/ko26b_lemma_7_2_reconstruction|Lemma 7.2]], it yields
absolute $c_4>0,S_0$ such that a uniform short-arc bound $B\ge1$ on the
whole interval $[0,S]$, $S\ge S_0$, must satisfy

$$
B\ge c_4\sqrt{\log S}.
$$

The local planar sets retain arrival time as a second coordinate, so repeated
circle positions cause no loss. No common localization point for different
prefix lengths is required.

Choose an absolute $0<c<c_4/(2C_3\sqrt3)$ and put
$A=c\sqrt{\log r}$. A strict failure of either claimed limsup inequality
supplies its corresponding eventual alternative. For all sufficiently large
$r$, the conditions above hold, $C_3A\ge1$, $S\ge S_0$, and
$\log S\ge(\log r)/3$. Thus the upper and lower count bounds would imply

$$
C_3c\sqrt{\log r}\ge c_4\sqrt{\log S}
\ge\frac{c_4}{\sqrt3}\sqrt{\log r},
$$

contrary to the choice of $c$. This proves the two sequence inequalities
separately, with a common absolute threshold and without a simultaneous-time
assertion.

For every sequence the upper inequality gives
$\limsup_n nM_n^{(r)}\ge r+c\sqrt{\log r}$; take the infimum only now.
Since $0\le nm_n^{(r)}\le r$,

$$
\limsup_n(r-nm_n^{(r)})=r-\liminf_n nm_n^{(r)}.
$$

Every inner liminf is consequently at most $r-c\sqrt{\log r}$; taking
the supremum gives the other deficit bound. Each diverges with its own
lower bound $c\sqrt{\log r}$. No exchange of a limit with an extremum,
or equality of the distinct-point and all-sequence extrema, is used.
