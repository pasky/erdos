---
name: research/erdos_774/routes/coefficient_growth_flattening
title: Coefficient-growth flattening beyond the Hall condition
desc: Weighted-simplex subset counting gives a sufficient flattening criterion and a necessary double-exponential height escape; actual-color focusing still lacks the required growth control.
tags: [E0774, proved, algebra, incomplete]
sources: []
created: 2026-09-18T17:23:00Z
updated: 2026-09-18T18:37:35Z
---


# Coefficient-growth flattening beyond the Hall condition

***

## Standing

This is a positive extension of
[Hall/determinant flattening](bounded_height_flattening.md). It permits
differing coefficient heights and does not require a Hall-tight subfamily. It
still requires the product in question to have **one actual color**. The
presently available focusing argument supplies no coefficient growth bound
meeting the new criterion, so the main coloring theorem remains unproved.

All relations have unrestricted finite support. Coefficient height is not
the fixed-order notion of freeness.

## 1. An exact sufficient inequality

For $1\le i\le r$, let $X_i$ be finite sets of roots in pairwise
coprime conductor groups, with nonzero relations
$$
\sum_{x\in X_i}c_{i,x}x=0,
\qquad c_{i,x}\in\mathbb Z\setminus\{0\}.
$$
Assume $X_1\cdots X_r$ is monochromatic. Put
$$
I_i=\{|c_{i,x}|:x\in X_i\},\quad m_i=|I_i|.
$$
If some $m_i=1$, dividing that relation by its common magnitude gives
a ternary relation; fix arbitrary points in the other factors. Otherwise
all $m_i\ge2$. Write
$$
b_i=\min I_i,\quad d_i=m_i-1,\quad
N=\prod_i m_i,\quad D=\prod_i d_i,
$$
and, for $t\in\prod_i(I_i\setminus\{b_i\})$, put
$$
W_t=\prod_i(b_i+t_i).
$$

**Theorem.** There is a nonzero monochromatic ternary relation if
$$
2^N>\prod_t(1+W_t). \tag{1}
$$
In particular, the simpler sufficient condition is
$$
\boxed{
\prod_i\frac{m_i}{m_i-1}
\ge 1+\sum_i\frac1{m_i-1}
\sum_{a\in I_i\setminus\{b_i\}}\log_2(b_i+a).
} \tag{2}
$$
The weak inequality in (2) is intentional.

### Proof

Group the given relation as
$$
w_{i,a}=\sum_{|c_{i,x}|=a}\operatorname{sign}(c_{i,x})x,
\qquad \sum_{a\in I_i}a w_{i,a}=0.
$$
In $\mathbb Z^{d_i}$, with coordinates indexed by
$I_i\setminus\{b_i\}$, define
$$
u_{i,a}=b_i e_a\quad(a\ne b_i),\qquad
u_{i,b_i}=-\sum_{a\ne b_i}a e_a.
$$
The rational linear map $e_a\mapsto w_{i,a}/b_i$ sends every
$u_{i,a}$ to $w_{i,a}$, including the distinguished column.

Consider the $N$ **indexed** integer tensor columns
$$
u_{1,a_1}\otimes\cdots\otimes u_{r,a_r}\in\mathbb Z^D.
$$
If they have no nonzero indexed ternary relation, their $2^N$ subset
sums are distinct. At coordinate $t$, the sum of the absolute values
of all column entries is exactly $W_t$: in factor $i$ the two
nonzero contributions have absolute values $b_i,t_i$, and these sums
multiply under tensoring. The subset sums therefore occupy an integer
interval of width $W_t$ in that coordinate. Consequently
$$
2^N\le\prod_t(1+W_t).
$$
Its contrapositive proves the existence of a nonzero indexed ternary
relation under (1).

Apply the tensor product of the displayed rational maps, followed by
multiplication in the compositum. The resulting relation is between the
products $\prod_i w_{i,a_i}$. Expand their signed root sums. Different
magnitude tuples use disjoint, nonempty Cartesian blocks of the $X_i$.
Multiplication on root tuples is injective because the conductor groups
form a direct product. Thus a nonzero formal coefficient survives, and all
expanded coefficients are $0,\pm1$. The support lies in the specified
monochromatic product. Extra linear dependencies among the grouped sums do
not affect this support argument.

Finally $W_t>1$, and
$$
\log_2(1+W_t)<1+\log_2W_t.
$$
Summing over the $D$ coordinates gives
$$
\frac1D\sum_t\log_2(1+W_t)
<1+\sum_i\frac1{d_i}\sum_{a\ne b_i}\log_2(b_i+a).
$$
Thus (2) implies the strict inequality (1). This proves the theorem.

## 2. Two magnitude groups and an example beyond Hall

If $I_i=\{a_i,b_i\}$, the universal columns are, up to sign,
the indexed scalar products choosing one of $a_i,b_i$ at each factor.
Every ternary relation on that indexed scalar family lifts by the proof
above. In this case (1) becomes
$$
2^{2^r}>1+\prod_i(a_i+b_i). \tag{3}
$$
This is a sufficient, not a necessary, test.

For example, magnitude pairs $\{1,2\},\{1,3\}$ satisfy
$16>1+3\cdot4=13$. More directly, from
$$
w_{1,1}+2w_{1,2}=0,\qquad w_{2,1}+3w_{2,3}=0
$$
one obtains
$$
w_{1,2}w_{2,3}-w_{1,1}w_{2,3}+w_{1,2}w_{2,1}=0.
$$
Its three Cartesian blocks are disjoint. The Hall test fails: the
one-row unions have size two and the two-row union has size three.
Rescaling the two original rows cannot make their magnitude pairs coincide,
because their ratios are two and three.

This example is a **conditional algebraic example**: no assertion is made
here that an arbitrary coloring supplies actual root factors with these
two magnitude pairs.

## 3. A necessary growth rate for dissociated products

Put $h_i=\max I_i$. Since $b_i+a\le2h_i-1$, a dissociated
full product necessarily satisfies
$$
\sum_{i=1}^r\log_2(2h_i-1)
>\prod_{i=1}^r\frac{m_i}{m_i-1}-1. \tag{4}
$$
If all $m_i\le M$, this implies
$$
\sum_{i=1}^r\log_2(2h_i-1)>
\left(\frac M{M-1}\right)^r-1,
$$
and hence
$$
\max_{i\le r}h_i>
\frac{1+2^{((M/(M-1))^r-1)/r}}2. \tag{5}
$$
Only the maximum height among the first $r$ factors is forced to
escape at this scale, not every individual height.

This broadens the target for adaptive focusing: one can now seek
monochromatic products violating (4), instead of insisting on one common
height or a Hall-tight subfamily. No such growth control has been proved.
The present full-profile palette $q^{|F|}$ allows much faster height
growth, and the only automatic magnitude-count bound is $m_i\le h_i$.

## 4. Exact escape and actual roots

In the universal scalar model, take
$$
I_i=\{1,H_i\},\qquad H_i=2^{2^{i-1}}.
$$
The indexed scalar products, up to signs, are exactly
$\{2^a:0\le a<2^r\}$, a dissociated set. The identity
$$
\prod_{i=1}^r(1+H_i)=2^{2^r}-1
$$
attains equality in the exact subset-counting bound. Thus a counting proof
cannot replace the strict inequality in (1) by a weak one.

The scalar calculation alone is not an actual-root construction. The
separate [root-circuit construction](../lemmas/root_height_escape.md)
realizes this escape with conductor-disjoint root circuits and exactly
these magnitude pairs. The stronger
[recurrent-root construction](recurrent_high_height_roots.md) also shows
that infinite rational coloring number in every tail does not itself repair
the missing coefficient-growth control.

## 5. Different actual colors on partially monochromatic blocks

The full product need not have one color for the following extension.
Keep the relations and universal integer columns $u_\gamma$ from
Section 1. Let $\Gamma$ be any collection of magnitude tuples whose
Cartesian blocks are **individually monochromatic** in a putative proper
dissociated $q$-coloring. Different blocks may have different colors.
Set
$$
K=|\Gamma|,\qquad
W_t(\Gamma)=\sum_{\gamma\in\Gamma}|(u_\gamma)_t|.
$$
Then necessarily
$$
\boxed{2^K\le\prod_t\left(1+\frac{W_t(\Gamma)}q\right)^q.}
\tag{6}
$$
A strict violation forces a monochromatic ternary relation supported only
on the good blocks.

Indeed split $\Gamma$ into actual block-color classes $\Gamma_c$,
and put $W_{c,t}=\sum_{\gamma\in\Gamma_c}|(u_\gamma)_t|$.
Each indexed integer family $(u_\gamma)_{\gamma\in\Gamma_c}$ must be
dissociated: the proof of Section 1 would lift a ternary dependence to
disjoint root blocks of color $c$. Consequently
$$
2^{|\Gamma_c|}\le\prod_t(1+W_{c,t}).
$$
Multiply these inequalities and apply arithmetic--geometric mean to the
$q$ factors at each coordinate, using $\sum_cW_{c,t}=W_t(\Gamma)$.
This proves (6), including empty classes and zero widths.
For all $N$ blocks, $W_t(\Gamma)=\prod_i(b_i+t_i)$.

For the constant-ratio-two circuits $2w_i=\sum_{b\in B_i}\epsilon_b b$,
there is a sharper elementary statement. Index the binary product blocks
by the coordinates $J$ using the full leaf set rather than singleton
$\{w_i\}$. The signed sum on that block is
$$
2^{|J|}\prod_iw_i.
$$
Two distinct good blocks of the same Boolean rank and the same actual
color therefore give a nonzero ternary relation by subtraction. Their
supports are disjoint and multiplication is injective. Hence every rank
has at most $q$ good blocks, and
$$
K\le q(r+1). \tag{7}
$$

These inequalities broaden the actual-color target beyond a monochromatic
rectangle. They do not produce good blocks: a coloring that splits every
local leaf set can leave just the all-pivot singleton good. No lower bound
on $K$ contradicting (6) or (7) has been forced for arbitrary colorings.

The theorem, coefficient-safe expansion, strictness, growth consequences,
and partial-block extension received independent internal review.
No numerical experiment was used. None establishes the required
counterexample.
