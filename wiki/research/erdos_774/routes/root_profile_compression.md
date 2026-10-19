---
name: research/erdos_774/routes/root_profile_compression
title: Coefficient-safe profile compression of root colorings
desc: Finite prime-prefix colorings obey a uniform profile-deficit bound; global colorings have summable deficits, but arbitrary distinct profiles remain unexcluded.
tags: [E0774, proved, coloring, incomplete]
sources: []
created: 2026-09-18T01:12:00Z
updated: 2026-09-18T01:28:02Z
---


# Coefficient-safe profile compression of root colorings

***

## Result and exact limitation

This is a new necessary condition on a putative proper finite coloring of
the [prime tensor family](prime_tensor_extraction.md), not a proof that such
a coloring is impossible. It uses the full signed relation system and makes
no Galois-equivariance assumption.

Let $f$ be a proper $q$-coloring of the squarefree odd-root grid, viewed
as the set of finite-support tuples in $\prod_{p\geq3}[p]$ after fixing
a basepoint in each prime coordinate. Declare two symbols in coordinate
$p$ equivalent when replacing one by the other leaves the color unchanged
for **every** finite-support assignment of all other coordinates. Let
$m_p$ be the number of these coordinate profiles. Then

$$
m_p\geq2,\qquad
\sum_{p\geq3}\left(\frac1{m_p}-\frac1p\right)
\leq2\log(48q)<\infty. \tag{1}
$$

In particular, for every fixed $0<\varepsilon<1$,

$$
\sum_{p:m_p\leq(1-\varepsilon)p}\frac1p<\infty. \tag{2}
$$

The same quantitative bound holds at each sufficiently long finite prime
prefix, using profiles of that finite coloring. The equivalence classes may
change with the prefix; no compatibility between finite colorings is needed.

More precisely, the finite assertion applies to **all** odd primes through
$P\geq e^5$, with counts $m_{p,P}$ taken from that finite coloring.
It bounds $\sum_{p\leq P}(1/m_{p,P}-1/p)$ but does not assert monotonicity
as $P$ varies. For a single global coloring, its global profile classes
are valid compression blocks on each finite prefix, although the restricted
profiles may merge some of them. Apply the finite compression lemma to those
global blocks themselves; only their partial deficit sums are then passed
monotonically to the infinite sum in (1).

An arbitrary finite coloring can have $m_p=p$ everywhere. We have not
proved that properness prevents this, or otherwise forces a violation of
(1). Thus the unrestricted coloring theorem in the main argument remains
unproved.

## 1. A finite compression lemma

Let $E=\bigotimes_{i=1}^k S_{p_i}$, with simplex columns
$s_{i,1},\ldots,s_{i,p_i}$. Partition the symbols in each coordinate into
nonempty blocks $A_{i,1},\ldots,A_{i,m_i}$. Assume the color is unchanged
by replacing a symbol inside one block, with all other coordinates arbitrary.
Equivalently it is constant on every product box of these blocks.

If $m_i=1$, any full coordinate-$i$ fiber is monochromatic and its
columns sum to zero, contradicting properness. Suppose therefore all
$m_i\geq2$, and put

$$
w_{i,a}=\sum_{x\in A_{i,a}}s_{i,x}.
$$

These vectors have precisely the one rational relation
$\sum_a w_{i,a}=0$. Indeed a dependence with coefficients $t_a$
expands to a simplex dependence whose coefficient on each symbol in
$A_{i,a}$ is $t_a$; the simplex kernel consists exactly of constant
coefficient vectors. Hence all $t_a$ must be equal. The vectors are
therefore a linear copy of $S_{m_i}$.

Color the **indexed** compressed tensor
$\bigotimes_i S_{m_i}$ by the common color of each corresponding box.
Suppose a same-colored collection of its indexed columns had a nonzero
signed relation. Expanding each column $\bigotimes_iw_{i,a_i}$ sums
the original columns in its box. Distinct boxes are disjoint. Every expanded
coefficient remains $0$ or $\pm1$, and at least one coefficient
is nonzero. This is a monochromatic signed relation in $E$, impossible.

Thus the induced compressed coloring is proper. Retaining the indices matters
when $m_i=2$: antipodal factors can produce repeated tensor values, and
relations between their distinct labels must not be discarded.

## 2. Quantitative restriction on the compressed sides

For any indexed tensor with sides $m_i\geq2$, set

$$
N=\prod_i m_i,\qquad d=\prod_i(m_i-1),\qquad
R=d/N,\qquad L=\sum_i\frac{\log(m_i-1)}{m_i}.
$$

A proper $q$-coloring necessarily satisfies

$$
\frac1q<4R\left(1+\frac{2L}{\log2}\right). \tag{3}
$$

This is the [small-column entropy bound](tensor_schedule_constraints.md),
whose proof also works for indexed sides of size two. Here are the needed
details. In standard integer coordinates the average log column
$\ell_1$-norm is $L$. At least $N/2$ labels have column norm
at most $e^{2L}$ (if $L=0$, all do). Some color contains at least
$N/(2q)$ of these labels. If $s$ of them are dissociated, their
subset sums are distinct and have total coordinate-box width at most
$s e^{2L}$. Hence

$$
2^s\leq(1+s e^{2L}/d)^d.
$$

The elementary implication
$2^t\leq1+Mt\Rightarrow t<2\log_2(2M)$, for $M\geq1$, gives
$s<2d(1+2L/\log2)$. Combining the lower and upper bounds proves (3).

For example, if $2\leq m_i\leq M$ uniformly, (3) implies

$$
q>
\frac{(M/(M-1))^k}
{4\bigl(1+k\log(M-1)/\log2\bigr)}. \tag{4}
$$

Thus bounded coordinate-profile counts cannot properly color arbitrarily
many tensor factors with a fixed palette. More generally every schedule
with $R_k(1+L_k)\to0$ is excluded.

## 3. The summable prime-profile deficit

Use all odd prime coordinates $p\leq P$, and define

$$
D=D(P)=\sum_{3\leq p\leq P}\left(\frac1{m_p}-\frac1p\right)\geq0.
$$

The elementary Euler product gives

$$
\prod_{p\leq P}(1-1/p)^{-1}
\geq\sum_{n\leq\lfloor P\rfloor}\frac1n\geq\log P.
$$

Indeed every integer $n\leq P$ has all its prime factors at most $P$,
and $H_{\lfloor P\rfloor}\geq\log(\lfloor P\rfloor+1)\geq\log P$.
For $m\leq p$,
$\log(1-1/m)-\log(1-1/p)\leq-(1/m-1/p)$.
Removing the prime two from the Euler product therefore gives

$$
R\leq\frac{2e^{-D}}{\log P}. \tag{5}
$$

The [proved elementary prime estimate](prime_tensor_extraction.md)
$\sum_{p\leq P}(\log p)/p\leq\log P+5$ also gives

$$
\begin{aligned}
L&\leq\sum_{3\leq p\leq P}\frac{\log p}{m_p}\\
&\leq\log P+5+D\log P.
\end{aligned} \tag{6}
$$

No lower bound on $m_p/p$ is assumed here. For $P\geq e^5$,
substitution in (3) yields

$$
\frac1q<8e^{-D}
\left[\frac1{\log P}+\frac2{\log2}
\left(1+D+\frac5{\log P}\right)\right]
<24(D+2)e^{-D}\leq48e^{-D/2}. \tag{7}
$$

For the middle estimate one may use $2/\log2<2.9$;
the bracket is at most $0.2+2.9(D+2)\leq3(D+2)$, with strictness
from the logarithmic bound. The last estimate follows from
$D+2\leq2e^{D/2}$. Thus $D(P)<2\log(48q)$.
For a global coloring its partial deficit sums increase, proving (1).
Equation (2) follows because each summand at such a prime is at least
$\varepsilon/[(1-\varepsilon)p]$.

## 4. A rigorously excluded algorithmic class

A deterministic **fixed-order finite-state scan** with at most $s$ states
has at most $s^s$ coordinate profiles. Precisely, its successive updates
are $\delta_i:Q_{i-1}\times[p_i]\to Q_i$, with
$|Q_i|\leq s$, and its output is determined by the final state. Each
input symbol induces one of at most $s^s$ maps $Q_{i-1}\to Q_i$.
Symbols with the same map are interchangeable in every prefix/suffix context.
This applies even when the fixed reading order and transition maps vary with
the prime or the finite grid size.

With $M=s^s$, (4) rules out fixed-palette, bounded-state read-once
colorings for arbitrarily many factors. A one-state procedure is already
constant and fails on a simplex fiber. This theorem does not cover adaptive
reading orders, arbitrary algorithms, growing state spaces, or unrestricted
mathematical colorings.

The useful new mechanism is **coefficient-safe block-sum compression**.
The unsolved next step would require an additional argument from dissociation
itself, not merely from the finiteness of the palette, to produce enough
compression or another forbidden signed relation.

## Exact scope

The compression hypothesis is exact monochromaticity of every product box;
agreement in only selected contexts or approximate agreement does not suffice.
The prime-deficit constant uses the complete odd-prime prefix and is not
asserted unchanged for an arbitrary sparse prime family. The finite-state
consequence assumes the fixed-order scan model stated above. Most importantly,
the theorem does not rule out the all-distinct-profile case $m_p=p$, and
no proper coloring realizing that case has been constructed here either.
