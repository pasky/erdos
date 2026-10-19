---
name: research/erdos_699/proofs/details/index_14_numerical_tail
title: "Erdős 699: a numerical stopping bound for index fourteen"
desc: "Sixty-four numerical pair sources, finite coefficient-gcd bootstraps, and the existing interpolation family give n<10^8516269 for every bad triple at index fourteen."
created: 2026-09-22T09:12:27Z
updated: 2026-09-22T19:12:28Z
---

# Erdős 699: a numerical stopping bound for index fourteen

[[research/erdos_699/_index|P699 research]] ·
[[research/erdos_699/proofs/details/index_14_effective|The interpolation family]] ·
[[research/erdos_699/methods/details/off_diagonal_numerical_thresholds|Finite Padé constants]] ·
[[research/erdos_699/proofs/details/index_14_finite|Finite-range certificate]]

***

**Theorem.** Every bad triple $(n,14,j)$ for the original threshold
$p\ge14$ satisfies

$$
\boxed{n<10^{8\,516\,269}.} \tag{1}
$$

All source thresholds in this statement are numerical. The bound lies
below the $10^{15\,170\,264}$ upper limit of the separately retained
finite-range certificate. Together they exclude every bad triple at
fourteen and complete the [cutoff-ten theorem](../../archive/previous_bounds/cutoff_10.md).

## Sixty-four sources suffice

Keep the polynomial family from the existing index-fourteen proof:

$$
\mathbf h=(33,29,26,22,19,15,10,5,0,0,0,0,0,0),
$$
$$
\mathbf m=(66,65,62,58,55,53,51,46,41,37,33,30,27,24).
$$

Its residual interpolation degree is $56$. The symmetric jet map has
rank $831$ on $841$ monomials, as verified modulo $65521$. The
nonvanishing family has residual degree at most $57$, hence total
degree $375$ after multiplication by the coordinate factors.

The numerical proof needs only $64$ pair alternatives: $61$ from the
retained off-diagonal table and the following three additional sources.
Here the targets are in the displayed prime order, and $\ell$ is the
logarithmic coefficient-gcd rate per Padé index $m$.

| Pair | Targets | Seed | Directions | $\ell$ | Numerical $m_0$ | Pair height exponent $K$ |
| --- | --- | --- | --- | --- | ---: | ---: |
| $2,7$ | $(.2747,.3213)$ | $8-7=1$ | $(32,15,32)$ | $14.21$ | $7716$ | $746378$ |
| $5,7$ | $(.3921,.2653)$ | $2\cdot25-49=1$ | $(2,1,2)$ | $.97$ | $20465$ | $141248$ |
| $11,13$ | $(.0726,.0726)$ | $13-11=2$ | $(147,59,147)$ | $57.18$ | $34417$ | $8516268$ |

These replace three earlier alternatives by slightly weaker targets,
which admit more practical numerical constants. The
[additional-source checker](../../computations/erdos_699_index_14_additional_pairs.py)
verifies their finite gcd sums, positive decay rates, and strict endpoint
margins with directed intervals. Its
[source records](../../computations/erdos_699_index_14_additional_pairs.json)
contain the complete parameters.

The selected alternatives have $543$ componentwise minimal witnessing
vectors. The checker regenerates all of them, then all $13002$ distinct
capacity lists, including every collision pattern of the selected
positions. Since the multiplicities are nonincreasing, the same
rearrangement argument covers arbitrary positions. Exact arithmetic gives

$$\sum_{r=0}^{13}m_r-375-\sum_r C_rm_r
\ge\frac{112}{10000}=\boxed{\frac7{625}}. \tag{2}$$

The worst capacity list, in decreasing order, is
$(1,.95,.9274,.83,.72)$. The complete list of selected edges and all
minimal vectors are retained in the
[numerical-tail data](../../computations/erdos_699_index_14_numerical_tail.json).

## Uniform gcd bounds with a finite bootstrap

The uniform prime-interval argument first supplies analytic numerical
starting indices for the coefficient gcds. The finite bootstrap then
checks every intervening integer index down to a smaller $m_0$ by
certifying entire intervals of indices at once. Both adjacent Padé
rectangles are included throughout.

The $61$ selected sources use the
[selected analytic inputs](../../computations/erdos_699_index_14_gcd_selected.json)
and [bootstrap records](../../computations/erdos_699_index_14_gcd_bootstrap.json).
The other three use their
[analytic inputs](../../computations/erdos_699_index_14_additional_gcd.json)
and [bootstrap records](../../computations/erdos_699_index_14_additional_bootstrap.json).
Together the $64$ records certify $5\,197\,837$ intervals of Padé
indices. Every requested rate is unchanged across its bootstrap, and
every retained minimum margin is positive.

The exact sieve covers prime endpoints through $10^8$. Between that
cutoff and $10^{11}$, the checker uses the retained BFT bounds. For
larger endpoints it uses Dusart's
$|\theta(x)-x|<.01x/\log^2x$ estimate. An integer lower bound for
$\log x$, obtained from $2^k\le x$ and $\log2>69/100$, keeps these
last comparisons rational. Thus the last source's long analytic tail
does not introduce an unevaluated prime-number estimate.

## Smaller explicit integral constants

The finite-constant argument used for index twelve remains valid here,
with two improvements. For directions $(\lambda,\mu,\kappa)$, split
the base integrand at the real power

$$
m-\gamma,\qquad \gamma=2/\mu.
$$

The remaining exponents are nonnegative: the only potentially negative
one is $\mu\gamma-1-\varepsilon=1-\varepsilon$, where
$\varepsilon\in\{0,1\}$ selects the adjacent rectangle. Consequently

$$|Q|\le FmM_Q^{-\gamma}e^{qm},\qquad
|E|\le FmM_E^{-\gamma}e^{em},$$

where $F,M_Q,M_E,q,e$ have the definitions in the finite-constant note.
This gives smaller prefactors than splitting off two full powers of
the base integrand.

Also retain the two decay rates separately. With $x=\log h$,
$m=\lfloor tx\rfloor$, the nonzero-integer estimate is

$$1\le tx\left(A_1e^{C_0}e^{-tC_0x}
              +2A_2e^{K_0}e^{-(tK_0-1)x}\right),$$

where

$$A_1=13(aP)F M_Q^{-\gamma},\qquad
A_2=\frac{D_0^3}{aP}F M_E^{-\gamma}.$$

Choose a verified rational $t$ just below the available integral-block
limit. The checker bounds each displayed term by $1/2$ separately,
using directed logarithmic comparisons. Both comparisons decrease
after an explicitly checked starting point, so the resulting bound
holds at every larger height. These improvements are implemented as
options of the [explicit pair checker](../../computations/erdos_699_off_diagonal_explicit_pairs.py);
the earlier index-twelve calculations retain their original parameters.

Every source is evaluated with $h=n-13$, factor gap at most $13$, and
factor heights in $[h,h+13]$. The largest source exponent is $8516268$,
coming from the last row of the table above.

## A sharper coefficient bound for the same polynomial family

No new interpolation rank calculation is needed. A Hasse jet of one
monomial of degree at most $56$, at nonnegative coordinates at most
$13$, has absolute value at most $26^{56}$. A symmetric basis element
contains at most two monomials, so every matrix entry is at most
$2\cdot26^{56}$. The exact integer inequality

$$
831(2\cdot26^{56})^2<10^{162}
$$

bounds every row norm of an $831\times831$ minor by $10^{81}$. Thus
Hadamard's determinant bound uses $831\cdot81$ in place of the
earlier general-purpose $831\cdot118$ estimate.

Keeping the same generator, coordinate-factor, and bounded-shift
constants as in the original proof gives the explicit logarithmic bound

$$
831\cdot81+1+6\cdot66+2\cdot13\cdot66+4\cdot159+7=70067.
$$

By (2), the algebraic part of the stopping bound is therefore

$$n<10^{6\,255\,983},\qquad
6255983\cdot112>70067\cdot10000.$$

Taking the maximum with the numerical pair thresholds, and adding one
decimal power to absorb the row shift of thirteen, proves (1).

## Reproduction

The [whole numerical-tail checker](../../computations/erdos_699_index_14_numerical_tail.py)
regenerates the cofactor vectors, collision capacities, gain, coefficient
bound, and all $64$ numerical source thresholds. It also checks every
source and bootstrap binding. With the pinned interpolation dependencies:

```sh
.venv/bin/python wiki/research/erdos_699/computations/erdos_699_index_14_numerical_tail.py
```

The source and finite-prime calculations can be rebuilt separately:

```sh
.venv/bin/python wiki/research/erdos_699/computations/erdos_699_index_14_gcd_selected.py
.venv/bin/python wiki/research/erdos_699/computations/erdos_699_index_14_gcd_bootstrap.py
.venv/bin/python wiki/research/erdos_699/computations/erdos_699_index_14_additional_pairs.py
mkdir -p tmp/erdos699
.venv/bin/python wiki/research/erdos_699/computations/erdos_699_off_diagonal_gcd_bootstrap.py --input wiki/research/erdos_699/computations/erdos_699_index_14_additional_gcd.json --output tmp/erdos699/erdos_699_index_14_additional_bootstrap.json
```

The last command writes under the ignored repository `tmp/`; compare its
output with the retained
[bootstrap file](../../computations/erdos_699_index_14_additional_bootstrap.json)
on its mathematical fields, since elapsed times differ between runs.
Updating the retained record in place is a separate step: after replacing
the bootstrap files deliberately, `erdos_699_index_14_numerical_tail.py
--write` repeats the full numerical proof and then rewrites the record,
including the names of the rebuilt files as its own run record.
