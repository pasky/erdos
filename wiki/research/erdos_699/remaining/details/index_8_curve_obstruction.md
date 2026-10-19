---
name: research/erdos_699/remaining/details/index_8_curve_obstruction
title: "Erdős 699: an all-degree polynomial obstruction at index eight"
desc: "Thirteen lines prove that no polynomial can have a positive weighted multiplicity-versus-degree gain at the remaining uniform .3 cofactor profile. Controlling common curve zeros does not remove this obstruction."
created: 2026-09-22T17:37:34Z
updated: 2026-09-22T19:12:28Z
---

# Erdős 699: an all-degree polynomial obstruction at index eight

[[research/erdos_699/_index|P699 research]] ·
[[research/erdos_699/archive/other_approaches/index_8_next_obstruction|The remaining cofactor profile]] ·
[[research/erdos_699/remaining/details/five_curve_obstruction|The corresponding quintic obstruction]]

***

Consider the remaining index-eight profile

$$
(r_2,r_3,r_5,r_7)=(1,3,0,2),\qquad
(e_2,e_3,e_5,e_7)=(.3,.3,.3,.3).
$$

Its row capacities are

$$
\alpha=(.3,.3,.3,.3,1,1,1,1).
$$

**Proposition.** If a nonzero polynomial $F\in\mathbf C[X,Y]$ has
multiplicity at least $m_r$ at every nonnegative integer point on row
$X+Y=r$, $0\le r\le7$, then

$$
\boxed{\deg F\ge\frac3{10}(m_0+m_1+m_2+m_3)+m_4+m_5+m_6+m_7.}
\tag{1}
$$

This holds in every degree and does not assume symmetry, coprime sections,
or surjectivity of a jet matrix. Thus the strict weighted-degree gain
required by the present polynomial divisor argument cannot hold at this
profile. Finding a polynomial whose common curve zeros are effectively
bounded, through Runge's theorem or a local nonvanishing argument, does not
by itself change (1).

The statement does not assert that the profile is realized by any bad
triple. Stronger cofactor estimates, restrictions on the actual Kummer
labels, or sharper estimates for polynomial values at the particular
column remain outside this obstruction.

## Point weights

Let $\Delta_8=\{(x,y)\in\mathbf Z_{\ge0}^2:x+y\le7\}$. Give its points
weights $w_{x,y}$ as follows. The entries are numerators with denominator
100; within row $r$, they are ordered by $x=0,\ldots,r$.

| Row | Weight numerators |
|---:|---|
| 0 | $30$ |
| 1 | $15,15$ |
| 2 | $11,8,11$ |
| 3 | $3,12,12,3$ |
| 4 | $15,20,30,20,15$ |
| 5 | $16,15,19,19,15,16$ |
| 6 | $10,13,11,32,11,13,10$ |
| 7 | $0,17,16,17,17,16,17,0$ |

Their row sums are exactly $\alpha_r$. We prove the stronger universal
inequality

$$
\sum_{P\in\Delta_8}w_P\operatorname{ord}_P F\le\deg F.
\tag{2}
$$

## A thirteen-line covering

Assign the following coefficients $\lambda_L$ to lines. Again, all
numerators have denominator 100.

| Lines | Numerator for each line |
|---|---:|
| $X=0$, $Y=0$ | 8 |
| $X=1$, $Y=1$ | 7 |
| $X=2$, $Y=2$ | 5 |
| $X=3$, $Y=3$ | 6 |
| $X+Y=4$ | 7 |
| $X+Y=5$ | 8 |
| $X+Y=6$ | 6 |
| $X+Y=7$ | 11 |
| $X=Y$ | 14 |

The exact incidence checks give

$$
w_P\le\sum_{L\ni P}\lambda_L,\qquad
\sum_L\lambda_L=\frac{49}{50}<1.
\tag{3}
$$

Each covering line itself has weighted incidence at most one:
$X=2,Y=2$ have incidence $99/100$; $X=3,Y=3$ have incidence $91/100$;
the other nine lines have incidence one.

Let $C$ be an irreducible curve different from these thirteen lines.
Bézout's theorem gives

$$
\sum_{P\in C\cap L\cap\Delta_8}\operatorname{mult}_P C\le\deg C
$$

for every covering line. Combining these inequalities with (3) yields

$$
\sum_{P\in\Delta_8}w_P\operatorname{mult}_P C
\le\frac{49}{50}\deg C<\deg C.
$$

The covering lines obey the non-strict bound separately. Factoring an
arbitrary nonzero polynomial into irreducible factors therefore proves
(2). Its row-multiplicity consequence is (1).

The [integer/rational checker](../../computations/erdos_699_index_8_curve_obstruction.py)
and [certificate](../../computations/erdos_699_index_8_curve_obstruction.json)
verify all 36 point weights, all thirteen line incidences, and the row
sums. No optimization solver or bounded-degree search is needed to
verify the proof.
