---
name: research/erdos_699/archive/previous_bounds/cutoff_15
title: "Erdős 699: cutoff 15 and the remaining small indices"
desc: "The preceding cutoff-15 proof and effective small-index reductions, followed by the complete cutoff 10."
created: 2026-09-22T05:30:00Z
updated: 2026-10-14T00:26:52Z
---

# Erdős 699: cutoff 15 and the remaining small indices

***

This is a retained earlier research note. The [[research/erdos_699/_index|current reading guide]] gives the latest status and distinguishes completed proofs from remaining cases.

[[research/erdos_699/_index|P699 research]] ·
[[problems/factorials_binomials/E0699/_index|Erdős problem 699]]

**Current result: $i=1,2,7$ and every $i\ge9$ are completely excluded.**
The [cutoff-nine proof](../../proofs/details/cutoff_9.md) gives the current
classification. This note retains the preceding cutoff-fifteen proof and
its supporting arguments, which excluded $i=10,11,13$ and every $i\ge15$.
The original threshold is $p\ge i$, with $1\le i<j\le n/2$.

The remaining classification is:

| Index | Status |
| --- | --- |
| $4,5,6,8$ | Known finite, without effective row bounds here. |
| $3$ | Global finiteness remains unproved; the previous exclusions through $10^{19}$ and for $v_2(n)\le48$ remain. |

## Four new complete exclusions

| $i$ | Numerical tail bound | Inclusive interval cap | Certified intervals | Exact singleton rows |
| --- | --- | --- | ---: | ---: |
| $10$ | $10^{15\,000\,000}$ | $10^{80}$ | $43\,985$ | $2$ |
| $15$ | $10^{15\,170\,264}$ | $10^{27}$ | $575\,194$ | $0$ |
| $18$ | $10^{700\,000}$ | $10^{37}$ | $247\,058$ | $0$ |
| $20$ | $10^{27\,027\,659}$ | $10^{39}$ | $173\,071$ | $0$ |

The four finite partitions have **1,039,308 certified intervals**. At
index ten, two additional rows, $n=252,1029$, are excluded by 620 exact
admissible-column gcd checks. No row or column remains unresolved.
The minimum interval logarithmic margins at $10,15,18,20$ exceed,
respectively, $5.32\cdot10^{-5}$, $5.23\cdot10^{-6}$,
$2.83\cdot10^{-5}$, and $1.35\cdot10^{-5}$.
The analytic arguments close the infinite tails; the interval certificates
close every row below them. These are computer-assisted mathematical proofs,
not completed Lean formalizations.

The proof records are:

- Index $10$: [numerical tail and polynomial coverage](../../proofs/details/index_10_effective.md)
  and [complete interval certificate](../../computations/erdos_699_window_intervals_10.json).
- Index $15$: [numerical tail](../../proofs/details/index_15_numerical_tail.md),
  [finite pair certificate](../../computations/erdos_699_prime_pair_strips_15.json),
  and [interval certificate](../../computations/erdos_699_further_intervals_15.json).
- Index $18$: [complete proof](../../proofs/details/index_18_complete.md)
  and [interval certificate](../../computations/erdos_699_further_intervals_18.json).
- Index $20$: [numerical tail](../../proofs/details/index_20_numerical_tail.md),
  [finite pair certificate](../../computations/erdos_699_prime_pair_strips_20.json),
  and [interval certificate](../../computations/erdos_699_window_intervals_20.json).

The [combined interval proof](../../proofs/details/further_interval_certificates.md)
gives the drivers and reproduction commands. The interpolation and large
integer dependencies are pinned in the
[requirements file](../../evidence/assets/erdos_699_interpolation_requirements.txt).

## Why the large numerical bounds are manageable

The earlier finite prime-pair argument enumerated pairs of exponents.
The [strip argument](../../methods/details/prime_power_strips.md) covers entire
regions of that exponent plane with one modular inverse. At an anchor
$P=p^a,Q=q^b$, let $\mu_u$ be the least positive cofactor over the
allowed nonzero differences. Every larger solution satisfies

$$
u'\ge\mu_u/p^A\qquad(P'=Pp^A).
$$

For example, $\mu_u^2\ge Pp^{3A_0}$ proves the cube inequality throughout
the strip $0\le A\le A_0$, with no upper restriction on the other
exponent. Repeating this argument, with exact boundary checks when needed,
certifies the entire finite range using dozens of anchors.

The method also handles rational exponents $\delta\le1/2$. At $20$, seven
pair constraints with $\delta=2/5$ give a total cofactor saving of at least
$2$: two disjoint triangles on $\{2,3,5\}$ and $\{7,11,13\}$, and
the edge $\{17,19\}$. These strengthen the numerical tail to the
interval cap in the table.

Exceptional prime-pair solutions are retained individually. If their two
heights are $x,y$, they can occur in an index-$i$ row only when

$$
\max(x,y)\le n\le\min(x,y)+i-1.
$$

The interval calculation disables the corresponding constraint only on
these short intervals. It therefore retains stronger bounds on other rows,
including rows below the largest exceptional height.

## The new argument at index ten

The [index-ten proof](../../proofs/details/index_10_effective.md) uses actual
small-prime positions, rather than one polynomial for every assignment.
Forty polynomial certificates cover all 160,000 combinations of labeled
positions and minimal pair-witness vectors, including collisions. Every
required symmetric jet map has full row rank modulo a prime, and the
[surjective interpolation lemma](../../methods/details/jet_nonvanishing.md)
guarantees a nonzero evaluation throughout the physical region.

The few difficult assignments have additional arithmetic structure.
For positions in arithmetic progression,

$$
(n-r_-)(n-r_+)=(n-r_0)^2-(r_+-r_0)^2.
$$

For four distinct positions with equal pair sums, the difference of the
corresponding quadratic products is a fixed nonzero integer.
The [composite-base Padé argument](../../methods/details/ap_cofactors.md)
therefore gives cofactor alternatives involving three or four primes at
once. These inequalities supply information absent from the pair graph.

In the last positional case, $7$ occupies the middle of an AP whose
endpoint primes are $2,3$. The seed $7-6=1$ gives

$$u_2>h^{.428}\quad\text{or}\quad u_3>h^{.13}
\quad\text{or}\quad u_7>h^{.198},\qquad h=n-9,$$

above an explicit threshold. Every branch is included in the polynomial
coverage check.

All source constants are numerical. The
[prime-interval bootstrap](../../methods/details/bft_prime_bootstrap.md)
preserves six near-limit pair exponents while reducing their source
parameters to explicit modest starting values. It uses rigorously bounded
prime-logarithm sums on 231,306 intervals and joins the existing analytic
tails. The [sharper Dusart input](../../methods/details/dusart_gcd_bounds.md)
and [direct product thresholds](../../methods/details/product_thresholds.md)
complete the source estimates. Their common row threshold is
$10^{996149}$; the polynomial coefficient estimate dominates it and gives
$n<10^{15\,000\,000}$.

The completed finite proof first uses five $2/5$ pair estimates and the
existing $(2,7)$ estimate to obtain total saving $1.059$, reducing the
row cap to $10^{80}$. All six $2/5$ estimates are then available on that
smaller range. The interval proof handles their explicit exceptional
windows; its only two remaining rows are the exact cases recorded above.
Thus the numerical tail at ten is a complete exclusion.

## Effective finiteness at seven and nine

The [index-seven proof](../../proofs/details/index_7_effective.md) covers all
540 initial position-and-cofactor configurations. Its 258 joint cofactor
sources and 49 polynomial certificates close every branch. The final
finite proof has 3,356 exact rational Farkas certificates; no floating
optimization decision is used as evidence.

The proof also verifies a pair of coprime modular kernel polynomials and
uses the [effective common-zero bound](../../methods/details/coprime_kernels.md)
to save one interpolation degree. All polynomial and common-zero terms
are covered by $h=n-6\ge10^{19\,813\,540\,001}$. The first proof left some source thresholds unevaluated. The
[numerical follow-up](seven_nine_bounds.md) evaluates them
and completes the finite-to-infinite bridge at seven.

The [index-nine proof](../../proofs/details/index_9_effective.md) covers all
104,976 labeled initial cases, including coincident selected positions.
Seventy baseline polynomial certificates and 58 further certificates,
together with 23,973 exact rational Farkas leaves, close every case.
The polynomial and common-zero terms are covered by
$h=n-8\ge10^{5\,109\,634\,000\,001}$. The original proof left analytic source thresholds unevaluated. The
[numerical follow-up](seven_nine_bounds.md) now gives the
explicit upper bound and a completed lower finite range.

## From effective bounds to complete cases at twelve and fourteen

The [degree-72 ramp](../../proofs/details/index_12_ramp.md) first simplified
the effective proof at twelve. Its source thresholds are numerical,
and the [completed finite proof](../../proofs/details/index_12_complete.md)
excludes every remaining row.

The [universal interpolation proof](../../proofs/details/index_14_effective.md)
first made fourteen effective. The
[numerical tail](../../proofs/details/index_14_numerical_tail.md) and
[completed finite range](../../proofs/details/index_14_finite.md) exclude
that index entirely as well. Together these give the
[complete cutoff ten](cutoff_10.md).

## Remaining work

The [additional product constraints](../other_approaches/additional_product_constraints.md)
give further restrictions involving the prime $11$ and enter the new
index-twelve proof. The newer off-diagonal pair estimates now also make
index fourteen effective. They also use the cubic identity
$n(n-3)^2-(n-1)^2(n-4)=4$. Exploratory interpolation optimizations
must keep the prime labels when applying these position-dependent rules;
domination of sorted capacity profiles alone is not sufficient.

At $14$, the seeds $144-143$ and
[$65-64$](../other_approaches/fourteen_ap_source.md) give additional
conditional estimates. The subsequent off-diagonal pair table supplies a
whole-index effective proof, rather than only these conditional restrictions.

Allowing [rational residual Padé blocks](../../methods/details/bft_rational_blocks.md)
also gives a piecewise linear cofactor restriction and improves the
effective $2,3$ maximum exponent from $.2921$ to $.2926$.
This small improvement does not settle another index.

The [exact gcd localization lemma](../../methods/details/gcd_localization.md)
also strengthens the polynomial argument: a selected small-prime power
$p^A$ can be replaced by $p^{\min(A,v_p\binom nj)}$, without an extra
prime-power loss. The [transfer consequences](../../remaining/details/prime_index_transfer.md)
give useful conditional improvements, but leave a second Lucas branch.

The [quintic position theorem](../../remaining/details/index_5_maximal_positions.md)
now confines any sufficiently large index-five bad triple to the two
small-prime maxima at positions $0,1$. Four effective off-diagonal
cofactor alternatives and an upper product bound further restrict this
remaining pattern. Whole-index effectivity at five is still unproved here.

The [general row-zero reduction](../../methods/details/row_zero_effective.md)
shows that, at every fixed index, sufficiently large bad rows have a
selected small-prime maximum at position zero. It uses the effective
S-part theorem on two fixed quadratic polynomials after bounding the
reduced denominator of $j/n$.

At $4,5$, the existing congruence and prime-power criteria remain valid.
The family of nearby integers carrying different large small-prime powers
still has unbounded cofactors. The new proofs at seven, nine, twelve, and fourteen leave four indices without effective bounds;
none of the deductions above establishes them for every remaining index, and none changes the separate
cubic finiteness question.
