---
name: research/erdos_774/routes/hadamard_gluing
title: Recurrent Hadamard gluing and anchor loss
desc: Saturated Hadamard feedback gives cheap chromatic jumps from a fixed anchored source, but sufficiently large order or diagonal padding loses every next-color anchor.
tags: [E0774, proved, construction, obstruction]
sources: []
created: 2026-09-18T01:58:00Z
updated: 2026-09-18T01:58:00Z
---


# Recurrent Hadamard gluing and anchor loss

***

## Standing and scope

This is a new recurrent, overlapping gluing design, outside the long private
buffers in [triangular gluing](mobile_anchor_gluing.md). It supplies an
arbitrarily cheap chromatic jump from any **fixed** anchored source, but loses
the next anchor at all sufficiently large Hadamard orders. The sufficient
threshold depends on the source. Changing-source iterations below that
threshold remain unexcluded; no successful iteration is proved. An independent
internal audit checked the saturation, constants, full closure, scalar
transfer, and diagonal-copy scope.

## 1. Saturated construction and analytic bound

Let $B\subset\Gamma\cong\mathbb Z^d$ be finite, nonzero, and without
antipodal pairs, with $\chi(B)=q$ and universal nonzero $q$-anchor
$w$. Write

$$
M^2=\max_{b\in B}\|b\|_2^2,\qquad
R=\max_{x\in\Sigma(B)}\|x\|_2^2\in\mathbb Z_{\geq1}.
$$

For $r=2^k\geq2$, construct the Sylvester matrix recursively by $H_1=(1)$,
$H_{2r}=\bigl(\begin{smallmatrix}H_r&H_r\\H_r&-H_r\end{smallmatrix}\bigr)$.
Induction gives $H_rH_r^{\mathsf T}=rI$. Quotient $\Gamma^{2r}$ by

$$
\Lambda=\{(a,H_r^{\mathsf T}a):a\in\Gamma^r\},
$$

and let $G_r$ be the images of all source blocks. The identity half of
$(I_r,H_r)\otimes I_d$ makes this lattice saturated. Every nonzero
gluing word has at least three nonzero blocks: one occupied left block gives
$r$ occupied right blocks; two or more occupied left blocks have at least
one occupied right block, since $H_r$ is invertible. Hence the source
blocks embed without new zero, equal, or antipodal labels. The entire right
block family is independent in the quotient. Here independence of blocks
means that their copies of $\Gamma$ embed as a direct sum; it does not mean
that the source elements inside one block are rationally independent.

For the positive-real parameter $\rho$ of
[the phase argument](tensor_extraction.md),

$$
\rho(G_r)\geq\rho(B)-\frac{\pi^2M^2r}{2(r+1)^2}. \tag{1}
$$

Here is a direct verification of the saturated-basis issue. Put
$A=(I_r,H_r)\otimes I_d$, with right inverse
$P=A^{\mathsf T}/(r+1)$. Independently maximize every block polynomial.
For each of the $rd$ basis-row phases, choose a real lift of the required
correction which has mean zero and variance at most $\pi^2$: a phase
$\theta\in[0,2\pi]$ is lifted to $\theta$ and
$\theta-2\pi$ with probabilities making its mean zero. Choose these
lifts independently. Applying $P$ to the lift vector solves every row
constraint, because $AP=I$. These are all quotient constraints because
the basis is integral and saturated.

The expected squared phase change of a frequency $b$ is bounded by
$\pi^2\|P_v^{\mathsf T}b\|_2^2$, at most $\pi^2rM^2/(r+1)^2$ in any block. The
mean-zero linear term cancels in
$\operatorname{Re}(ze^{it})\geq\operatorname{Re}z -t\operatorname{Im}z-|z|t^2/2$.
Summing coefficient-weighted losses and choosing a realization at least as good
as its expectation proves (1).

Every gluing row with $a_i=w$ at one left block and zero elsewhere gives
an obstruction to a $q$-coloring: each of its $\pm w$ entries has a
signed representation in every restricted source color, and the blocks are
disjoint. Thus $\chi(G_r)>q$.

## 2. Full-closure anchor loss at large order

If

$$
2q(2dr+1)^R\exp\left(-\frac{r}{(2q+1)R}\right)<1, \tag{2}
$$

then

$$
\chi(G_r)=q+1,\qquad
\tau_{q+1}(L(G_r))\leq2(q+1) \tag{3}
$$

for every linear scalar encoding $L$ preserving ternary relations exactly.
In particular no next-color universal anchor survives such an encoding.
Condition (2) holds for every sufficiently large power of two, with $B$
fixed.

### Counting every realizable gluing word

Any induced relation has block sums
$(a,b)=(a,H_r^{\mathsf T}a)\in\Sigma(B)^{2r}$. Orthogonality gives
$r\|a\|_2^2=\|b\|_2^2\leq rR$, hence $\|a\|_2^2\leq R$.
There are at most $(2dr+1)^R$ possible integer vectors $a$:
$\|a\|_1\leq\|a\|_2^2\leq R$, so at most $R$ signed coordinate
steps, padded with zero steps, encode each one. A nonzero such word satisfies

$$
|\operatorname{supp}_{\rm blocks}b|
\geq\frac{\|b\|_2^2}{R}
=\frac{r\|a\|_2^2}{R}\geq\frac rR.
$$

Partition the right blocks randomly into $2q+1$ bins: one unused bin
and bins $S_{t,c}$ for $t=1,2$, $c\in[q]$. A nonzero bounded
word misses a given designated bin with probability at most
$e^{-r/((2q+1)R)}$. The union bound and (2) give a partition in which
every nonzero bounded word meets every designated bin. This covers all
rationally induced ternary relations, not only the displayed Hadamard rows.

### Two colorings with disjoint extra-color spans

Fix a proper source partition $B=P_1\sqcup\cdots\sqcup P_q$.
For coloring $t$, use it on every block, but on right blocks in
$S_{t,c}$, replace the color of $P_c$ by the new color $q+1$.
A relation in an old color $c$ must vanish on $S_{t,c}$, contrary
to the hitting property unless its block-sum word is zero. A zero word is
excluded by source dissociation. The new color is also dissociated, since it
lies in the independent right family of blocks, each with a dissociated
source subset. Thus both are proper $(q+1)$-colorings.

Their new classes occupy disjoint right blocks, so their vector signed spans
intersect only at zero. The assertion also survives exact scalar encoding:
representations of a common scalar on these disjoint classes differ by a
ternary relation; exactness makes their vector lifts equal, and disjoint
right-coordinate spans make that lift zero. Take all $q+1$ cyclic
relabelings of both colorings. For each color the intersection is then zero,
proving (3). Restriction and the anchor obstruction give the exact chromatic
number.

## 3. Fixed-order diagonal padding does not preserve the anchor

Repeat every column of $(I_r,H_r)$ $s$ times, equivalently replacing each source
block by $s$ independent copies and gluing along the diagonal copy of $\Gamma$,
which contains the diagonal anchor. This repeats columns, not rows; applying
Section 1 to the entire group $\Gamma^s$ would be a different construction. The
repeated row matrix still has an identity minor and is saturated. Its right
inverse spreads the correction among the $s$ copies, giving

$$
\rho(G_{r,s})\geq\rho(B)-
\frac{\pi^2M^2r}{2s^2(r+1)^2}.
$$

If $s\geq2q$, assign one copy of each right coordinate to each of
$2q$ disjoint designated bins. Every nonzero right word is repeated in
each such bin, so the hitting property holds without a probabilistic count.
The preceding two-coloring construction gives
$\chi(G_{r,s})=q+1$ and the same threshold bound (3).

The construction therefore does not provide a fixed-source cheap restart via
large order or diagonal padding. It does not exclude all correlated gluing,
nor changing-source orders below the quantified threshold (2).
