---
name: research/erdos_699/archive/previous_bounds/index_12_effective
title: "Erdős 699: index 12 is effective"
desc: "Two additional asymmetric prime-pair estimates and a finite family of position-dependent interpolation certificates give an effective stopping bound at index twelve."
created: 2026-09-22T06:29:56Z
updated: 2026-10-14T00:26:52Z
---

# Erdős 699: index 12 is effective

***

This is a retained earlier research note. The [[research/erdos_699/_index|current reading guide]] gives the latest status and distinguishes completed proofs from remaining cases.

[[research/erdos_699/_index|P699 research]] ·
[[problems/factorials_binomials/E0699/_index|Erdős problem 699]] ·
[[research/erdos_699/methods/details/jet_nonvanishing|Interpolation nonvanishing]]

**Simpler follow-up.** The [off-diagonal line-product proof](../../proofs/details/index_12_ramp.md)
proves the same effectivity statement using one explicit degree-72
polynomial, with algebraic term $10^{845}$. The first proof below remains valid.

**Theorem.** There is an effectively computable integer $N_{12}$ such that
no bad triple $(n,12,j)$ has $n\ge N_{12}$, for the original threshold
$p\ge12$. Thus the entire index-twelve case reduces to a computable finite
set.

The proof is retained in the [checker](../../computations/erdos_699_index_12_effective.py)
and its [certificate data](../../computations/erdos_699_index_12_effective.json).
It uses twelve integer polynomial certificates. This establishes
effectivity; it does not yet exclude every row below the resulting bound.
Some pair-source thresholds are effective constants whose numerical values
have not been evaluated here.

**Subsequent complete result.** The [numerical tail and finite certificates](../../proofs/details/index_12_complete.md)
exclude this entire index. The effective proof below is retained as
an earlier step.

## Two asymmetric pair estimates

Choose $r_p\in\{0,\ldots,11\}$ maximizing $v_p(n-r_p)$ for each
$p\in\{2,3,5,7,11\}$, and write

$$
n-r_p=P_pu_p,\qquad P_p=p^{v_p(n-r_p)},\qquad h=n-11.
$$

The useful new estimates are the alternatives

$$
u_2>h^{.375}\quad\text{or}\quad u_7>h^{.123}, \tag{1}
$$

$$
u_2>h^{.248}\quad\text{or}\quad u_{11}>h^{.133}. \tag{2}
$$

They hold above effective thresholds. All terminating decimals in this
note denote exact rational numbers. The
[directed source checker](../../computations/erdos_699_twelve_rational_pairs.py)
proves (1) from

$$
49-3\cdot16=1,\qquad s=53/31,\qquad \log L_1=.510598,
$$

and (2) from

$$
13\cdot512-5\cdot1331=1,\qquad s=80/39,\qquad \log L_1=.694514.
$$

In each case the retained BFT coefficient-gcd formula gives
$\log L(s)>\log L_1$ with a strictly positive, certified margin.
BFT Theorem 2.2 consequently gives an effective starting value for the
coefficient-gcd estimate. The same asymmetric integral-block argument used
in the earlier pair table then gives (1) and (2). Their limiting endpoints
are, respectively,

$$(.3756069008\ldots,.1235534798\ldots),\qquad
  (.2484849136\ldots,.1333949827\ldots).$$

The nonunit coefficients in these seeds matter. Maximizing only a common
exponent for both cofactors misses useful alternatives of this kind.
The [source note](../other_approaches/twelve_rational_pairs.md) also records
rational-block refinements, but (1) and (2) already suffice for this
whole-index argument.

## Complete position division

Together with the retained old pair estimates, (1) and (2) give seventeen
pair alternatives. Their exact disjunction has thirty-eight
componentwise minimal witnessing vectors $v$: for every sufficiently large
row, at least one vector satisfies $u_p\ge h^{v_p}$ for all five primes.
The checker regenerates those vectors from the source edges.

A polynomial certificate assigns an integer row multiplicity $m_t$ to
$t\in\{0,\ldots,11\}$. A singleton selected position for prime $p$ has
capacity $1-v_p$. When several primes share a position, their selected
prime powers have product dividing $n-r$, so their **whole group** has
capacity at most one.

Three certificates handle the following uniform cases:

- repeated selected positions;
- five distinct positions other than $\{0,1,2,3,4\}$;
- the remaining thirty-two witness vectors, at arbitrary positions.

Their row multiplicities are nonincreasing. Rearrangement therefore puts
the largest capacities at the earliest available rows. In the second case
the worst available position set is $\{0,1,2,3,5\}$. For repeated positions,
the checker enumerates the set partitions of the five labeled primes and
uses capacity one for each nonsingleton group. These comparisons cover
all twelve possible positions, not merely the first five.

This leaves six actual, prime-labeled witness vectors and the $120$
permutations assigning each to $\{0,1,2,3,4\}$. These $720$ cases are treated
individually. Applicable AP and equal-sum product alternatives from the
[retained product bounds](../other_approaches/additional_product_constraints.md)
are used to reduce certificate sizes. Each such rule is checked against
its actual prime positions, and every branch is retained. No implication
between differently labeled vectors is inferred from sorted prefix sums.

Nine further certificates cover all these branches. Twenty-five of the
$720$ position cases use additional product alternatives, giving $893$
position-certificate applications. Together with the $1,938$ collision
partition cases and the uniform distinct-position cases, the exact checker
verifies $2,901$ applications. The smallest gain is $3/5000$.

The modular calculations establish the polynomial hypotheses separately.
The largest matrix has $24,022$ rows and $24,025$ columns; it has full row
rank modulo $251$.

## Polynomial divisibility and a computable bound

Let $c=n-j$, so $12<j\le c$. A certificate specifies

$$H(X,Y)=\prod_{a=0}^{11}((X-a)(Y-a))^{h_a},\qquad
R_{xy}=\max\{0,m_{x+y}-h_x-h_y\}\quad(x+y<12).$$

The coordinate factor $H(j,c)$ is nonzero. For each nonempty residual
scheme, a degree-$d$ symmetric jet matrix has full row rank modulo $251$,
hence over $\mathbb Q$. The
[jet nonvanishing lemma](../../methods/details/jet_nonvanishing.md)
supplies a finite family of integer residual polynomials of degree at
most $d+1$, at least one of which is nonzero at $(j,c)$ whenever $n>11$.
Multiplying by $H$ gives a nonzero $F(j,c)$ with all prescribed row
multiplicities. For a line-only certificate use $F=H$.

Write $D=2\sum h_a+\max(0,d+1)$ and $M=\sum m_t$. Badness and Kummer's
formula imply

$$
\prod_{t=0}^{11}Q_t^{m_t}\mid F(j,c),
$$

where $Q_t$ is the part of $n-t$ supported on primes at least twelve.
The contribution from any smaller prime away from its selected position
is bounded using

$$
v_p(n-t)\le v_p(|t-r_p|)\qquad(t\ne r_p).
$$

The total such contribution is at most $(11!)^{\max m_t}$. Consequently,
if $C_t$ denotes the appropriate singleton or group capacity, the
certificate gain is

$$
\eta=M-D-\sum_t C_t m_t. \tag{3}
$$

Every gain in the complete case division is strictly positive. The
factors $n-t$ and the source height $h=n-11$ differ from $n$ by bounded
additive terms. For a computable elementary threshold depending only on
the certificate, their combined correction is at least $1/2$. It follows
that every sufficiently large bad row satisfies

$$
n^\eta\le 2\,\|F\|_1(11!)^{\max m_t}. \tag{4}
$$

The coefficient on the right is computably bounded without constructing
large rational kernels. If the symmetric jet matrix has $r$ rows, every
entry is at most $2\cdot12^d$ in absolute value. A nonzero maximal minor
and its adjugate give an explicit rational right inverse, and hence an
explicit integer nonvanishing family. The checker retains a conservative
integer power of ten bounding the right side of (4), obtained from
Hadamard's determinant bound and the coordinate factor $H$.

For example, with $r<10^5$ and $d<1000$, it is enough to take

$$
E=r(2\max(d,0)+7)+3\sum_a h_a+8\max_t m_t+9,
$$

so that the right side of (4) is less than $10^E$. Thus
$n<10^{E/\eta}$ for the applicable certificate. Taking the maximum of
these finitely many explicit algebraic bounds, the elementary correction
thresholds, and the effective pair/product source thresholds produces
$N_{12}$. The algebraic part of the certificate has the evaluated bound
$n<10^{3\,643\,130\,001}$ once its source hypotheses hold. The product
thresholds have also been evaluated; some pair-source thresholds remain
effective but unevaluated, so this is not claimed as the full numerical
stopping bound.

The retained modular ranks and exact positive gains are finite
certificates of this argument. Neither a binomial-row search nor an
assumption about unverified numerical QP solutions enters the theorem.
