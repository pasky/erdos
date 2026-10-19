---
name: research/erdos_699/remaining/details/index_6_curve_obstruction
title: "Erdős 699: why more curve factors do not settle one index-six case"
desc: "An exact nine-line covering proves a degree bound for every polynomial at the remaining .31, .36, .31 cofactor profile, even when its common curve zeros can be handled effectively."
created: 2026-09-22T17:36:52Z
updated: 2026-09-22T19:12:28Z
---

# Erdős 699: why more curve factors do not settle one index-six case

[[research/erdos_699/_index|P699 research]] ·
[[research/erdos_699/archive/other_approaches/index_6_overlap_obstruction|The full-overlap column classes]] ·
[[research/erdos_699/remaining/details/index_8_curve_obstruction|The index-eight degree bound]]

***

Consider the index-six profile

$$(r_2,r_3,r_5)=(2,1,0),\qquad
(e_2,e_3,e_5)=(.31,.36,.31).$$

Its row capacities are $\alpha=(.31,.36,.31,1,1,1)$.

**Proposition.** If a nonzero polynomial $F\in\mathbf C[X,Y]$ has
multiplicity at least $m_r$ at every nonnegative integer point on row
$X+Y=r$, $0\le r\le5$, then

$$\boxed{\deg F\ge
\frac{31}{100}m_0+\frac9{25}m_1+\frac{31}{100}m_2+m_3+m_4+m_5.}\tag{1}$$

This holds in every degree, without requiring symmetry, a coprime
polynomial family, or full rank of a jet matrix. In particular, allowing
common curve zeros whose bad points can be bounded by Runge's theorem,
positivity, or a local argument does not supply the strict weighted-degree
gain at this profile: inequality (1) holds for each polynomial itself.

The proposition does not say that any bad triple realizes this profile.
Stronger cofactor estimates, additional restrictions on the Kummer
labels, and sharper bounds for polynomial values at a particular column
remain outside its scope.

## Point weights and a nine-line covering

Put $\Delta_6=\{(x,y)\in\mathbf Z_{\ge0}^2:x+y\le5\}$. Give these
points weights $w_{x,y}$ using the following numerators, all divided by
$16000$. Within row $r$, the entries are ordered by $x=0,\ldots,r$.

| Row | Weight numerators |
| ---: | --- |
| 0 | $4960$ |
| 1 | $2880,2880$ |
| 2 | $1121,2718,1121$ |
| 3 | $3635,4365,4365,3635$ |
| 4 | $3404,2283,4626,2283,3404$ |
| 5 | $0,3754,4246,4246,3754,0$ |

Their row sums are exactly $\alpha_r$. Give the following lines
coefficients $\lambda_L$ with the same denominator $16000$.

| Lines | Numerator for each line |
| --- | ---: |
| $X=0$, $Y=0$ | 2480 |
| $X=1$, $Y=1$ | 1359 |
| $X=2$, $Y=2$ | 1851 |
| $X+Y=3$ | 1155 |
| $X+Y=4$ | 924 |
| $X+Y=5$ | 2395 |

The exact incidence inequalities are

$$w_P\le\sum_{L\ni P}\lambda_L,\qquad
\sum_L\lambda_L=\frac{7927}{8000}<1.\tag{2}$$

Every covering line itself has weighted incidence at most one:
$X=2$ and $Y=2$ have incidence $7179/8000$, and the other seven
have incidence one.

For an irreducible curve $C$ different from these nine lines, Bézout
gives

$$
\sum_{P\in C\cap L\cap\Delta_6}\operatorname{mult}_P C\le\deg C
$$

for every covering line. Multiplying by $\lambda_L$, summing, and
using (2) proves

$$\sum_{P\in\Delta_6}w_P\operatorname{mult}_P C
\le\frac{7927}{8000}\deg C<\deg C.$$

The covering lines satisfy the non-strict bound separately. Since
multiplicities and degrees add under factorization, every nonzero
polynomial consequently satisfies

$$
\sum_{P\in\Delta_6}w_P\operatorname{ord}_P F\le\deg F.\tag{3}
$$

Taking the weighted sum of its row multiplicities proves (1).

The [standard-library checker](../../computations/erdos_699_index_6_curve_obstruction.py)
and [certificate](../../computations/erdos_699_index_6_curve_obstruction.json)
verify all 21 point weights, all nine line incidences, and the row sums
using exact arithmetic. No optimization solver or bounded-degree
search is needed to verify the proof.
