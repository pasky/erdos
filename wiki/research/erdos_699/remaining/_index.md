---
name: research/erdos_699/remaining
title: "Erdős 699: the five remaining indices"
desc: "What is known at indices 3, 4, 5, 6, and 8, and the precise gaps in the current arguments."
created: 2026-09-22T19:09:27Z
updated: 2026-10-16T06:44:50Z
---

# Erdős 699: the five remaining indices

[[research/erdos_699/_index|..]]

[[research/erdos_699/remaining/details/_index|details/]]: Proofs of the current restrictions and obstructions at indices three, four, five, six, and eight.

[[research/erdos_699/remaining/index_three|index_three]]: Rational abc implies cubic finiteness; unconditional residue restrictions and the nonexistence question remain open.

***

Call $(n,i,j)$ **bad** if $1\le i<j\le n/2$ and no prime $p\ge i$
divides both $\binom ni$ and $\binom nj$. The completed arguments leave
only $i\in\{3,4,5,6,8\}$.

For each of $4,5,6,8$, van Doorn and Rocca prove that there are only
finitely many bad triples. No effective upper bound on all their rows
has been established here. Their finiteness argument uses an ineffective
$S$-part estimate; the available effective version saves too little in
these cases. The [index-three guide](index_three.md) explains the different
situation there: even global finiteness remains open.

Assuming rational $abc$, the [cubic argument](details/cubic_abc.md) proves
finiteness at $i=3$, and hence finiteness of all bad triples. Unconditional
finiteness at $i=3$ remains open.

The results below restrict infinite families of possible counterexamples.
They do not complete any of these four indices. An **effective threshold**
means that the proof provides an algorithm to compute it; several such
thresholds have not been evaluated numerically.

## Indices four and five

The following necessary row conditions hold without a height restriction:

$$
i=4:\quad 4\mid n\ \text{or}\ 9\mid n,
\qquad
i=5:\quad 8\mid n\ \text{or}\ 9\mid n.
$$

The [proof by fixed rational slopes](details/indices_4_5_row_zero.md)
excludes the complementary congruence classes completely. Its difficulty
in the remaining classes is concrete: the denominator of $j/n$ can grow
with the large powers of two or three dividing $n$.

Choose positions $r_2,r_3$ maximizing $v_2(n-r)$ and $v_3(n-r)$ among
the numerator factors, and write

$$
n-r_2=2^a u,\qquad n-r_3=3^b v.
$$

At index four, sufficiently large bad triples must have distinct
positions and satisfy

$$2^a u-3^b v=r_3-r_2\in\{-3,-2,-1,1,2,3\},
\qquad uv<4n^{5/6}.$$

The cofactors remain unbounded. The
[effective small-cofactor theorem](details/small_cofactors_effective.md)
does exclude every range $\min(u,v)\le(\log n)^A$, for each fixed $A$.
It gives a computable lower bound of the form
$\exp(c\log n/\log\log n)$ for both cofactors. The intermediate range
is still too large for the current argument.

At index five, the confinement is stronger. Beyond an effective threshold,

$$
\{r_2,r_3\}=\{0,1\},\qquad
(n-4)^{1/100}<u,v<(n-4)^{57/100},
\qquad uv<\frac{240}{4^{6/5}}n^{3/5}.
$$

The [quintic cofactor bounds](details/index_5_cofactor_range.md)
include the proof and link the position-confinement argument. They leave
an explicit range of intermediate cofactor sizes. Merely allowing more
polynomial factors does not close it: the
[index-five obstruction](details/five_curve_obstruction.md)
proves that every polynomial with row multiplicities $m_r$ satisfies

$$
\deg F\ge .13m_0+.34m_1+m_2+m_3+m_4.
$$

Thus the strict degree saving needed by the current divisor argument
cannot hold at that profile. This is an all-degree theorem, not a failed
search through a small catalog of polynomials.

The tested column refinements do not yet exclude this profile. The
[higher-digit note](details/index_5_higher_digits.md) writes the complete
Lucas condition as exact inequalities in the slope $j/n=A/q$. On a
candidate branch, including odd columns with $j\equiv2\pmod3$
when $8\mid n$, the two- and three-adic overlaps equal the selected
powers up to a factor two. A one-prime lemma identifies why higher digits
do not automatically improve polynomial valuations; it does not establish
compatibility across primes for an actual column. On that branch
$q>n^{43/100}$ and $A$ is bounded below by a positive power of $n$.
No uniform effective upper bound for these parameters is obtained, and
the branch is not proved to occur.

## Indices six and eight

Here it helps to distinguish row information from information about the
actual column. Put $H=n-i+1$, select maximal positions $r_p$, and write
$P_p=p^{v_p(n-r_p)}$, $u_p=(n-r_p)/P_p$ for each $p<i$.

At six, consider $(r_2,r_3,r_5)=(2,1,0)$. If

$$H^{.31}\le u_2\le H^{.4},\qquad
H^{.36}\le u_3\le H^{.4},\qquad u_5\ge H^{.31},$$

then a bad triple with $H\ge10^{425}$ must satisfy

$$
j\bmod P_2>2,\qquad j\bmod P_3>1,\qquad j\bmod P_5>0.
$$

The [carry restriction at six](details/index_6_carry_constraints.md)
uses a degree-twelve product and an exact valuation identity. It also
forces the five-part of $\binom nj$ above $\sqrt H$, while the five-parts
of $j$ and $n-j$ lie below $\sqrt H$. The remaining branches, where all
three displayed residue inequalities hold, have not been excluded.

At eight, consider $(r_2,r_3,r_5,r_7)=(1,3,0,2)$ with
$u_2,u_3,u_5\ge H^{.3}$. For $H\ge10^{850001}$, the
[carry restriction at eight](details/index_8_carry_constraint.md)
forces $j\bmod P_7>2$. It also forces the seven-part of $\binom nj$
above $\sqrt H$ and the seven-parts of $(j)_3$ and $(n-j)_3$ below
$\sqrt H$. Again, the remaining branch is open.

These are difficult configurations, not a claim that every possible bad
triple lies in the displayed cofactor boxes. Two exact geometric
obstructions explain why further row-only interpolation is insufficient:

| Index and row capacities | Degree bound for every polynomial |
| --- | --- |
| [Six](details/index_6_curve_obstruction.md): $(.31,.36,.31,1,1,1)$ | $\deg F\ge .31m_0+.36m_1+.31m_2+m_3+m_4+m_5$ |
| [Eight](details/index_8_curve_obstruction.md): $(.3,.3,.3,.3,1,1,1,1)$ | $\deg F\ge .3\sum_{r=0}^3m_r+\sum_{r=4}^7m_r$ |

Both bounds hold in every degree and permit arbitrary curve factors.
They do not show that the profiles occur arithmetically. Stronger cofactor
estimates or restrictions on the column could exclude them.

## What a new argument still has to supply

For these four indices, numerical improvements to existing source bounds
are not enough by themselves: some permitted configurations have no
strict asymptotic saving. The useful remaining targets are stronger
cofactor inequalities, additional restrictions from the actual column,
or a new relation confining bad pairs to manageable algebraic curves.

The [effective Runge criterion](../methods/details/runge_curve_criterion.md)
would handle many such fixed curves. At four and five, three suitable
finite fibers of the map $(n,j)\mapsto n$, together with infinity, suffice.
The missing global step is to put all remaining bad pairs on finitely
many curves satisfying that criterion. No such confinement has been proved.
