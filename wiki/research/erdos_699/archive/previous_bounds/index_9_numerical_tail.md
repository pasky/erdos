---
name: research/erdos_699/archive/previous_bounds/index_9_numerical_tail
title: "Erdős 699: a numerical stopping bound for index nine"
desc: "Explicit joint Padé constants, weaker initial pair endpoints, and exact polynomial coverage give n<10^11514327437548 for every bad triple at index nine."
created: 2026-09-22T00:00:00Z
updated: 2026-10-14T00:26:52Z
---

# Erdős 699: a numerical stopping bound for index nine

***

This is a retained earlier research note. The [[research/erdos_699/_index|current reading guide]] gives the latest status and distinguishes completed proofs from remaining cases.

[[research/erdos_699/_index|P699 research]] ·
[[research/erdos_699/proofs/details/index_9_effective|The original effective proof]] ·
[[research/erdos_699/methods/details/joint_numerical_thresholds|Joint Padé constants]]

**Theorem.** Every bad triple $(n,9,j)$ for the original prime threshold
$p\ge9$ satisfies

$$
\boxed{n<10^{11\,514\,327\,437\,548}.}\tag{1}
$$

Every source threshold is numerical. This is a stopping bound; the finite
range below it is not excluded by this note. The separate
[finite proof](../../proofs/details/index_9_finite.md) excludes
$n\le10^{241547629}$. The
[numerical-tail checker](../../computations/erdos_699_index_9_numerical_tail.py)
and [data](../../computations/erdos_699_index_9_numerical_tail.json)
combine the analytic sources with complete coverage of the root cases.

**Complete result.** The [combined proof](../../proofs/details/index_9_complete.md)
excludes every admissible bad triple at nine. The estimates below
are retained as components of that proof.

## Initial cofactor bounds

Write $h=n-8$. For each $p\in\{2,3,5,7\}$ choose a position
$r_p\in\{0,\ldots,8\}$ maximizing $v_p(n-r_p)$, and put

$$P_p=p^{v_p(n-r_p)},\quad u_p=(n-r_p)/P_p,\quad
e_p=\log u_p/\log h.$$

The proof lowers each endpoint of the original nineteen pair alternatives
by exactly $1/10000$. This modest change allows larger strict analytic
margins. Eleven numerical pair certificates imply all nineteen weakened
alternatives; the four ordinary arithmetic-progression sources used in
the original forest retain their targets.

The [initial-source checker](../../computations/erdos_699_index_9_initial_relaxed_numerical.py)
verifies every implication with rational arithmetic and matches the
nineteen edges against the relaxed baseline. Its
[data](../../computations/erdos_699_index_9_initial_relaxed_numerical.json) give
the common uniform bound

$$
h\ge10^{12\,370\,301\,901\,530}.\tag{2}
$$

The largest threshold comes from the $(2,5)$ alternative with targets
$(.2675,.2710)$. For comparison, the symmetric $(2,5)$ target
$(.2678,.2678)$ uses seed $128-125=3$ and directions $(79,18,79)$,
with exponent $2790743305738$.

The [complete initial-source interval covers](../../proofs/details/index_9_initial_height_cover.md)
lower this requirement to $h\ge10^{241547627}$. They retain 299324
witnesses for all eleven pair sources and four ordinary product sources,
joining their explicit cofactor boxes to the numerical tails above.

Coincident positions are included. The joint integer argument permits
actual gap zero; alternatively $r_p=r_q$ gives $u_pu_q\ge h$, which
rules out two cofactor upper bounds whose exponents sum to less than one.
The four ordinary AP sources have nonzero position step of absolute
value at most four, hence product gap at most sixteen.

## Joint cofactor bounds

All 790 joint sources have numerical thresholds from the
[finite-constant argument](../../methods/details/joint_numerical_thresholds.md).
The source thresholds $R$ are weakened individually, leaving every
positive-part intercept and sign condition unchanged. The exact forest
verifies these weakenings simultaneously.

The [joint-source checker](../../computations/erdos_699_index_9_joint_numerical.py)
uses 739 uniform coefficient-gcd certificates. They combine BFT's prime
intervals with the retained global Chebyshev bounds of
Broadbent et al.
and the finite-range bound of
[Johnston–Yang](../../../../../library/primes/johnston_yang_2022_some_explicit_estimates_error_term_prime_number_theorem/_index.md),
patched by global estimates. The
[numerical source data](../../computations/erdos_699_index_9_joint_numerical.json.gz)
give the common height

$$
h\ge10^{27\,829\,083\,464\,213}.\tag{3}
$$

This maximum comes from `source_0406`, with directions $(32,25,45)$,
block parameter $1352650/866762331$, and uniform gcd starting index
$m_0=10^{11}$. Every factorial prefactor, integral maximum, residual
denominator cost, and exponential decay margin is included numerically.

## Adjusting the joint witness blocks

The [block adjustment lemma](../../methods/details/pade_block_adjustment.md)
keeps every source intercept and weakened threshold fixed while reducing
the denominator cost for a smaller witness block. The
[adjusted numerical checker](../../computations/erdos_699_index_9_reblocked_numerical.py)
and [certificates](../../computations/erdos_699_index_9_reblocked_numerical.json.gz)
cover all 790 clauses using 647 uniform gcd bounds. The full replay checks
every numerical clause and every uniform gcd certificate.

Their new common joint-source height is

$$
h\ge10^{11\,514\,327\,437\,547}.\tag{4}
$$

The largest threshold now comes from `source_0647`. Altogether 595
individual source bounds improve. At the polynomial height
$h\ge10^{241547627}$, 440 clauses already hold directly; lowering the
other source heights is a separate finite-cover calculation.

## Complete polynomial coverage

The [relaxed baseline](../../computations/erdos_699_index_9_relaxed_baseline.py)
uses all 128 retained polynomial certificates. It checks
$9^4\cdot16=104976$ labeled position and cofactor cases, including
prime-position collisions. Polynomial inequalities directly cover
104148 of them, leaving 828 cases.

The [relaxed forest](../../computations/erdos_699_nine_relaxed_forest.py)
and [proof data](../../computations/erdos_699_nine_relaxed_forest.json.gz)
close all 828 remaining cases. They retain 32165 nodes and 24322 exact
Farkas leaves. Each leaf uses positive rational multipliers canceling
every cofactor variable. The checker verifies a strictly negative
combined right side.

The [polynomial constants](../../computations/erdos_699_nine_newton_farkas_bound.py)
are bounded using the retained Newton basis.
The [arithmetic nonvanishing certificates](../../proofs/details/index_9_nonvanishing.md)
remove the two largest common-zero height requirements. Combining
the remaining common-zero bounds, the baseline coefficient bounds,
and the exact weighted leaf bound

$$
\frac{7465512500000}{30907}<241547627
$$

gives the polynomial starting height $h\ge10^{241547627}$.
The interpolation ranks are unchanged; this calculation uses the
existing rank and kernel certificates.

## Combining the bounds

The initial-source interval covers and polynomial argument both apply
from $h\ge10^{241547627}$. The adjusted joint bound (4) is larger.
Thus every hypothetical bad triple has $n-8<10^{11514327437547}$.
Adding one decimal power absorbs the row shift and proves (1).

The numerical-tail checker matches the initial pair list, all source
identifiers, all individual threshold weakenings, and the full relaxed
forest. It names its inputs by basename, checks that each named file is
present, replays the exact coverage without recomputing ranks, and
lists its inputs by basename in its own output as a run record, not
as a condition for running.

With the retained
[interpolation dependencies](../../evidence/assets/erdos_699_interpolation_requirements.txt)
installed, run:

```sh
.venv/bin/python wiki/research/erdos_699/computations/erdos_699_index_9_numerical_tail.py
```

The additional `--sources` option regenerates the numerical analytic
constants as well, including the adjusted joint sources. Neither command enumerates binomial rows.
