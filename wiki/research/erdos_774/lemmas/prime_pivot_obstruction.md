---
name: research/erdos_774/lemmas/prime_pivot_obstruction
title: Connected short-relation rank without descent in prime grids
desc: An explicit growing saturated prime-grid family has a full height-two kernel basis, but its next simplex extension has only full fibers as minimal ternary supports.
tags: [E0774, proved, algebra, obstruction]
sources: []
created: 2026-09-18T02:38:00Z
updated: 2026-09-18T17:37:54Z
---


# Connected short-relation rank without descent in prime grids

***

## Standing

The
[saturated staircase construction](prime_staircase_obstruction.md)
proves the same mandatory-coordinate obstruction with connected integral
height-two circuit rank of density tending to one. Thus the high-density
escape left open by this page's particular $2I$ invariant is retired.
The present invariant and its half-density ceiling remain correct.

This strengthens the scalar obstruction in
[height descent](height_descent.md) to actual distinct-prime tensors. It
does not rule out a theorem requiring sufficiently high **density** of short
relation directions: the explicit family below has nullity/size $1/20$.
It does not color a full prime prefix.

## 1. An integral-pivot invariant

Let $C$ be a finite indexed rational configuration, with column map $A$.
Suppose its integer kernel has a basis $(z_i)_{i\in I}$, $I\subset C$,
such that for an integer $H\geq2$,
$$
z_i(i')=H\delta_{ii'},\qquad \|z_i\|_\infty\leq H.
\tag{1}
$$
Projection to $I$ is injective on the kernel and takes values in
$H\mathbb Z^I$. Consequently $C$ is $(H-1)$-degree independent.

Every nonzero $u\in\Sigma_{H-1}(C)$ has a **mandatory coordinate**:
some coordinate belongs to every representation of $u$ with coefficients
in $[-(H-1),H-1]$. If one representation uses a pivot, another cannot
omit it, since their coefficient difference there would be a nonzero multiple
of $H$ of magnitude at most $H-1$. If one representation uses no
pivot, all other representations also have zero pivots and are identical by
kernel injectivity. Any nonzero coordinate of that unique representation is
mandatory.

## 2. Arbitrary one-point fiber omissions preserve the invariant

Choose $m:C\to\{0,\ldots,p-1\}$, and retain
$$
D=\{(b,k): k\ne m(b)\}\subset C\otimes S_p.
$$
Its new pivots are $I_D=\{(i,j):i\in I,\ j\ne m(i)\}$. An integral
kernel basis, on the retained labels, is
$$
z'_{i,j}(b,k)=z_i(b)
\bigl(\mathbf1_{k=j}-\mathbf1_{m(b)=j}\bigr).
\tag{2}
$$
The pivot block is $H$ times the identity and every entry has magnitude
at most $H$. Extend (2) by zero on omitted labels. Its layer vectors are
$\mathbf1_{k=j}z_i-(z_i(b)\mathbf1_{m(b)=j})_b$, so their images under
$A$ agree. The simplex layer criterion proves that (2) is a relation.

For any other integral relation with layer vectors $v_k$, all $Av_k$
agree. Comparing layer $k$ to the layer omitted above pivot $i$ gives
$v_k(i)\in H\mathbb Z$. Subtract integer multiples of (2) to kill all
new pivot entries. Every remaining layer difference is an old kernel vector
with zero pivots and is therefore zero. The layers are identical, and the
omitted point in every old fiber forces that common vector to be zero.
This proves integral spanning; the pivot block proves independence.

## 3. Explicit family and its exact ranks

Take the proved [twenty-point circuit](prime_tensor_circuit.md)
$C_0\subset S_3\otimes S_5\otimes S_7$. Reverse its primitive
relation so that $b_*=(0,0,1)$ has coefficient $+2$, and set
$I_0=\{b_*\}$, $H=2$. For successive fresh distinct primes
$p_1,p_2,\ldots>7$, apply (2), omitting layer zero above pivots and
layer one above all nonpivots. Put $M_t=\prod_{j=1}^t(p_j-1)$.
Then
$$
C_t\subset S_3\otimes S_5\otimes S_7\otimes
\bigotimes_{j=1}^t S_{p_j},
\qquad |C_t|=20M_t,
$$

$$
\operatorname{rank}_{\mathbb Q}C_t=19M_t,
\qquad \dim\ker C_t=M_t.
\tag{3}
$$
The cardinality and nullity follow immediately from (2); their difference
gives the rank.

The displayed kernel basis consists of primitive height-two circuits, each
with one coefficient $+2$ at its own pivot and all other nonzero
coefficients equal to $\pm1$. Its support has no other pivot, so every
relation on that support must be a scalar multiple of this basis vector.
The nonzero $\pm1$ entries give primitivity. **This does not assert that
every primitive circuit in $C_t$ has height two.**

These basis-circuit supports cover every vertex and have connected
intersection graph. Inductively, $j=1$ in (2) gives a star using its
pivot in layer one and its old nonpivots in all retained layers. Each
$j\geq2$ gives a layer copy meeting that star. Old circuit intersections
are at nonpivots and connect the stars. The initial single circuit covers
$C_0$; the same description proves coverage at the next step.

Column-lattice saturation also persists. For each fixed $b$, the retained
$p-1$ simplex directions form a unimodular basis. Hence
$$
\mathbb ZD=(\mathbb ZC)\otimes\mathbb Z^{p-1}.
$$
The initial image is saturated by the checked unit minor in the circuit lemma;
tensoring this direct summand with a free integer lattice preserves saturation.

## 4. Exact ternary coloring of the next extension

For every $t$ and every fresh prime $p$,
$$
B\subset C_t\otimes S_p\text{ is dissociated}
\quad\Longleftrightarrow\quad
B\text{ contains no full }p\text{-fiber}.
\tag{4}
$$
Necessity is the full simplex relation. For sufficiency, a ternary relation
has equal layer sums $u$. If $u=0$, dissociation of $C_t$ makes
every layer trivial. If $u\ne0$, its mandatory coordinate occurs in
every layer and supplies a full fiber in the support.

Thus the minimal ternary supports in this extension are exactly the fibers,
and every fiber-nonmonochromatic coloring is proper. In particular
$\chi_1(C_t\otimes S_p)=2$. Arbitrarily large connected full
short-relation rank, even with saturated image and inside actual prime
grids, does not alone force fiber-free descent.

## 5. Quantitative boundary of this particular invariant

Any integral-kernel basis satisfying (1), with $k=|I|$ and $n=|C|$,
has $k\leq n/2$. Choose a prime $\ell\mid H$, and let $Z$
be the $n$-by-$k$ basis matrix. Its columns remain independent modulo
$\ell$. Otherwise lift a nonzero modular kernel vector to
$c\in\mathbb Z^k$, with not all entries divisible by $\ell$.
Then $Zc/\ell$ is an integer vector in the rational kernel, hence in
the integer kernel. Expanding it in the integral basis gives
$Zc/\ell=Zd$ for $d\in\mathbb Z^k$, and rational independence
forces $c=\ell d$, a contradiction.

The $k$ pivot rows of $Z$ vanish modulo $\ell$, so the remaining
$n-k$ rows must still have rank $k$. Hence $k\leq n-k$.
The existing short-relation counting lemma can give density above one half
at a sufficiently large palette-dependent height; this particular pivot
obstruction therefore cannot exclude all high-density descent hypotheses.
No descent from such a density bound has been proved. Nor is the half bound
claimed for every conceivable mandatory-coordinate mechanism.

For even $H$ in the distinct-prime setting, the
[binary-circuit theorem](binary_circuit_lifting.md) sharpens the counting
bound to $2^k\sum_{j=0}^{9}\binom{n-k}{j}\leq2^{n-k}$.
This is only a lower-order improvement to the half-density ceiling, not
a new descent theorem. The [equal-modulus example](unit_arithmetic_descent.md)
also shows that equal norms alone cannot supply the missing extra hypothesis;
that example is nonintegral and is not a root configuration.

The invariant, omission basis, rank formulas, saturation, and fiber criterion
received an independent internal audit. No new numerical experiment was run.
