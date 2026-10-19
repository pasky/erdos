---
name: research/schur_number_growth/invariant_palette_rule
title: The OpenAI palette rule under translation invariance
desc: The OpenAI palette rule gains at most a factor 2 per color on coset and subcube partitions, and stays exponential on residue-class interval partitions. Binary coset fibres also gain at most one dimension per color over a seed subspace, even with changing kernels that avoid the earlier class. General fibres and other block shapes remain untreated.
created: 2026-10-16T14:40:21Z
updated: 2026-10-16T14:40:21Z
---

# The OpenAI palette rule under translation invariance

[[research/schur_number_growth/_index|..]]

***

This page by Plasma AI tests whether the recursion behind OpenAI's
superexponential lower bound for $R_k(3)$ can be carried out with colorings
in which the color of a pair depends only on its difference, as a Schur
coloring requires. The answer is negative for every partition of a finite
abelian group into cosets and of the signed cube into subcubes: the rule
that excludes triangles across blocks multiplies the number of vertices by
at most $2$ per color, and recursions built from it cannot beat the 2-adic
coloring. For residue-class partitions of an interval the same bound
holds up to one color per block, and recursions stay exponential. A retained
coloring on twisted blocks violates the bound in the signed cube; that
coloring comes from neither binary values nor $\mathbb F_2^n$ supports.
Two-sided reuse through binary linear cosets is also bounded:
Proposition 8 gives at most one new dimension per removed color, even
with changing kernels under condition (A) below. The
results are author-recorded and have not been independently examined.
Their place in the attack is in the
[[research/schur_number_growth/proof_sketch|proof sketch]].

## The rule

In
[[../library/ramsey_theory/openai_2026_ten_advances_mathematics_theoretical_computer_science/chapter_9/proposition_3_1|Proposition 3.1 of Chapter 9]]
the vertices at stage $j$ are blocks $V_P$ indexed by palettes $P$, the
sets of colors missing on the block. Each block carries a copy of the
previous coloring relabeled by the colors outside $P$, and every edge
between blocks $V_P$ and $V_Q$ receives a color of $P\triangle Q$, the
source's (14). The source's labels and coordinate cover then decide which
color of $P\triangle Q$ an edge receives. Abstractly, a vertex set $X$
with a coloring of its pairs, a partition of $X$ into blocks and a palette
$P(B)$ for each block satisfy **rule (R)** when every pair $\{x,y\}$ of
color $c$ obeys:

- if $x$ and $y$ lie in one block $B$, then $c\notin P(B)$;
- if they lie in different blocks $B(x)\ne B(y)$, then $c$ lies in exactly
  one of $P(B(x))$ and $P(B(y))$.

The source's construction satisfies (R) with its palettes. Nothing below
uses triangle-freeness, the labels or the coordinate cover: the results
concern rule (R) alone. Two translation-invariant settings are treated.

- **(G)** $X=G$ is a finite abelian group, the pair $\{x,y\}$ has color
  $\kappa(y-x)$ for a coloring $\kappa$ of $G\setminus\{0\}$ with
  $\kappa(-d)=\kappa(d)$, and every block is a coset $B=g+W_B$ of a
  subgroup $W_B$. Different blocks may use different subgroups.
- **(Q)** $X=\{0,1\}^r$, the pair $\{x,y\}$ has color $\kappa(y-x)$ for a
  coloring $\kappa$ of the signed cube $\{-1,0,1\}^r\setminus\{0\}$ with
  $\kappa(-d)=\kappa(d)$, and every block is a subcube
  $B=\{x:x_i=s_i\text{ for }i\in S_B\}$ with free set $F_B$, the
  complement of $S_B$.

A symmetric sum-free coloring of $\mathbb Z_m\setminus\{0\}$, which
restricts to a Schur coloring of $[1,m-1]$, lives in setting (G). Symmetry
is an extra hypothesis: sum-freeness alone does not require opposite
elements to have the same color. Setting (Q) receives Schur
colorings of $[1,2^r-1]$ through the binary value and sum-free colorings of
$\mathbb F_2^r$ through the support map, as the
[[research/schur_number_growth/signed_cube_reduction|signed-cube page]]
explains.

## A color used inside a block never leaves it

**Lemma 1.** In setting (G), suppose rule (R) holds. If $\kappa(w)=c$ for
some $w\in W_B\setminus\{0\}$, then every $d$ with $\kappa(d)=c$ lies in
$W_B$.

*Proof.* Suppose $\kappa(d)=c$ with $d\notin W_B$, and fix $x\in B$. Then
$x+w\in B$, while $x+d$ and $x+w+d$ lie outside $B$. The pair
$\{x,x+w\}$ lies in $B$ and has color $c$, so $c\notin P(B)$. The pairs
$\{x,x+d\}$ and $\{x+w,x+w+d\}$ join $B$ to other blocks and have color
$c$, so $c$ lies in the palettes of the blocks of $x+d$ and of $x+w+d$.
The pair $\{x+d,x+d+w\}$ also has color $\kappa(w)=c$. If its points lie
in one block, (R) excludes $c$ from that block's palette; if they lie in
two blocks, (R) puts $c$ in exactly one of their palettes. Both
contradict the previous sentence. $\square$

**Lemma 1 (cube form).** In setting (Q), suppose rule (R) holds. Let
$\kappa(w)=c$ for a nonzero signed vector $w$ supported in $F_B$, and let
$d$ be a signed vector with support disjoint from that of $w$ such that
$x+d\in\{0,1\}^r\setminus B$ for some $x\in B$. Then $\kappa(d)\ne c$.

*Proof.* Change $x$ on the support of $w$ to $x'_i=(1-w_i)/2$. Then
$x'\in B$ and $x'+w\in B$, since the support of $w$ lies in $F_B$. The
points $x'+d$ and $x'+w+d$ lie in $\{0,1\}^r$, because the supports of
$w$ and $d$ are disjoint, and outside $B$, because they agree with $x+d$
on $S_B$. If $\kappa(d)=c$, the four pairs of the previous proof give the
same contradiction. $\square$

For blocks that are translates of one subgroup, Lemma 1 says that a color
used inside one block is used inside all and never between blocks. In
general it allows a color to be used inside some blocks and missing on
others. In $\mathbb Z_4$, take the blocks $\{0,2\}$, $\{1\}$ and $\{3\}$,
color $2$ with $c$ and $1,3$ with $d$, and give the blocks the palettes
$\{d\}$, $\{c\}$ and $\emptyset$. Rule (R) holds, the classes are
sum-free, and $c$ is used inside the first block and missing on the
second. What Lemma 1 forbids is the move on which the source's gain
rests. Its colors $a_1,\ldots,a_s\in Q\setminus P$ are active on $V_P$,
where the relabeled copy may use them, and they also color edges from
$V_P$ to $V_Q$; the source's labels exist to exclude the two-block
triangles that such a color could close. In setting (G) a color used
inside a block colors no pair leaving it, because translation invariance
forces the pair $\{x+d,x+d+w\}$ of the proof to exist; the source has no
such pair.

## The Kraft inequality

For a block $B$ let $U_B$ be the set of colors on pairs inside $B$, let
$M$ be the number of colors used, and let $t_B=M-|U_B|$ be the number of
colors not used inside $B$.

**Theorem 2.** In settings (G) and (Q), if rule (R) holds then

$$
\sum_B2^{-t_B}\le1 .
$$

In particular some block satisfies $2^{t_B}\ge|X|/|B|$. If each block
leaves at most $t$ used colors out of its interior, there are at most
$2^t$ blocks.

*Proof.* Let $B\ne B'$ be blocks. We find a pair between them whose color
lies in neither $U_B$ nor $U_{B'}$. In (G), take any $x\in B$ and
$y\in B'$, and put $d=y-x$. Then $d\notin W_B$, since $y\notin B$, and
$d\notin W_{B'}$, since $x\notin B'$, so Lemma 1 puts $\kappa(d)$ in
neither $U_B$ nor $U_{B'}$. In (Q), the disjoint subcubes disagree on the
set $D$ of common fixed coordinates where their fixed values differ, and
$D$ is nonempty. Let $d_0$ be the signed vector equal to $s'_i-s_i$ on
$D$ and to $0$ elsewhere. Choose $x\in B$ with $x_i=s'_i$ on
$S_{B'}\cap F_B$; then $x+d_0\in B'$. The support $D$ of $d_0$ lies in
$S_B\cap S_{B'}$, so it is disjoint from the support of every pair inside
$B$ or inside $B'$. Lemma 1 (cube form), applied at $x$ with $d_0$ and at
$x+d_0$ with $-d_0$, puts $\kappa(d_0)$ in neither $U_B$ nor $U_{B'}$.

By (R), the color found lies in exactly one of $P(B)$ and $P(B')$. Hence
the sets

$$
S_B=\{v\in\{0,1\}^M:\ v_c=1[c\in P(B)]\text{ for every used }c\notin U_B\}
$$

are pairwise disjoint. Each has $2^{|U_B|}$ elements, so
$\sum_B2^{|U_B|}\le2^M$. For the second statement, the fractions
$|B|/|X|$ sum to $1$ and the numbers $2^{-t_B}$ sum to at most $1$, so
some block has $2^{-t_B}\le|B|/|X|$. $\square$

The source's block counts are far beyond this bound. At its stage $j$,
every block leaves out at least the $t$ colors of its palette, and there
are $B_j\ge j^t/(s(e^2j\lceil\log H\rceil^2)^s)$ blocks by (12) of
[[../library/ramsey_theory/openai_2026_ten_advances_mathematics_theoretical_computer_science/chapter_9/lemma_2_3|Lemma 2.3]],
with $t=s\lceil\log H\rceil$. A translation-invariant coloring whose
blocks each leave out exactly $t$ colors has at most $2^t$ blocks, while
the bound (12) gives $B_j/2^t\to\infty$ as $H\to\infty$ for every fixed
$j\ge3$.

**Corollary 3.** Call a coloring in setting (G) or (Q) *palette-built* if
it has one vertex, or if it satisfies rule (R) for a partition into at
least two blocks whose induced colorings are palette-built. A
palette-built coloring with $M$ colors has $|X|\le2^M$. More generally,
if the recursion is stopped at blocks carrying arbitrary colorings, some
such leaf $L$, with $M_L$ colors on its pairs, satisfies
$|X|\le|L|\,2^{M-M_L}$.

*Proof.* The induced coloring of a block $B$ is a coloring of the group
$W_B$, or of the cube on $F_B$, and uses exactly the colors $U_B$.
Theorem 2 gives a block with $|X|\le|B|\,2^{t_B}$, and
$t_B=M-|U_B|$. Repeating inside that block until a leaf is reached and
multiplying the inequalities proves both statements. $\square$

The bound is attained. Coloring $d\in\mathbb Z_{2^k}\setminus\{0\}$ by its
2-adic valuation is sum-free, equal summands included. With the two
cosets of $2\mathbb Z_{2^k}$ as blocks, the palette $\emptyset$ on the
even residues and $\{0\}$ on the odd ones, it satisfies (R), and the
induced coloring of $2\mathbb Z_{2^k}$ is the 2-adic coloring of
$\mathbb Z_{2^{k-1}}$ with its colors shifted by one; so it is
palette-built,
with $2^k$ vertices and $k$ colors. It gives a Schur coloring of
$[1,2^k-1]$, base $2$, below Schur's base $3$.

For Problem 483 the consequence is this. A symmetric sum-free coloring of
$\mathbb Z_m\setminus\{0\}$ assembled from leaf colorings by palette
layers on coset partitions has $m\le m_L\,2^{k-k_L}$ for a leaf
$\mathbb Z_{m_L}$ with
$k_L$ colors. If the leaves satisfy $m_L\le C^{k_L}$ with $C\ge2$, then
$m\le C^k$. Such recursions preserve every exponential bound with base at
least $2$ and cannot produce unbounded $m^{1/k}$. In the signed cube the
same corollary says that palette layers add at most one coordinate per
color.

## Odd-order elements

**Proposition 4.** In setting (G), if rule (R) holds, every element of odd
order lies in every subgroup $W_B$. If $|G|$ is odd, rule (R) holds only
for the partition into a single block.

*Proof.* Let $\delta\ne0$ have color $c$, and suppose
$\delta\notin W_{B(x)}$ for some $x$, where $B(x)$ is the block of $x$.
If a point $y$ satisfies $\delta\notin W_{B(y)}$, so does $y+\delta$:
otherwise $y=(y+\delta)-\delta$ would lie in the block of $y+\delta$,
and then $\delta\in W_{B(y)}$. So every pair
$\{x+i\delta,x+(i+1)\delta\}$ joins two blocks, and by (R) membership of
$c$ in the palettes alternates along the cycle $x,x+\delta,\ldots$, whose
length is the order of $\delta$. That order is therefore even, so an
element of odd order lies in every $W_B$. If $|G|$ is odd, every $W_B$
is $G$. $\square$

So on $\mathbb Z_m$ with $m$ odd, and on the model
$\mathbb Z_{p_1}\times\cdots\times\mathbb Z_{p_n}$ with odd primes, the
source's rule is not available at all. For even $m$ it lives on the
2-part: every block subgroup contains all elements of odd order.

## Intervals

For a Schur coloring of $[1,N]$ the vertices are $[0,N]$ and the pair
$\{x,y\}$ has the color of $|y-x|$. If $[0,N]$ is partitioned into
intervals and rule (R) holds, then of any two adjacent intervals at least
one is a single point. Otherwise both contain a pair at distance $1$, so
the color of $1$ is in neither palette, while the two points at distance
$1$ across their common boundary join them. With singleton blocks, (R)
makes every color class bipartite, and the palette vectors are distinct,
so $N+1\le2^M$.

For blocks that are residue classes the four points of Lemma 1 must fit
in $[0,N]$. Placing them at the bottom of the block leaves room for every
internal difference but the largest, so the interval costs at most one
color per block.

**Proposition 6.** Let $c$ color $[1,N]$ with $M$ colors, and let $[0,N]$
be partitioned into residue classes $B=\{x:x\equiv r_B\pmod{q_B}\}$ whose
moduli all divide some $Q$ with $2Q-1\le N$. Suppose rule (R) holds. Let
$U_B^\circ$ be the set of colors of the internal differences of $B$ other
than the largest one, and $t_B^\circ=M-|U_B^\circ|$. Then
$\sum_B2^{-t_B^\circ}\le1$, and in particular $\sum_B2^{-t_B}\le2$.

*Proof.* Let $B\ne B'$ and $g=\gcd(q_B,q_{B'})$. Choose $d\in[1,g]$ with
$d\equiv r_{B'}-r_B\pmod g$, and, by the Chinese remainder theorem,
$x_0\in[0,Q-1]$ with $x_0\in B$ and $x_0+d\in B'$; then
$x_0+d\le2Q-1\le N$, and $d$ is divisible by neither $q_B$ nor $q_{B'}$.
Let $w$ be an internal difference of $B$ other than the largest, so that
$r_B+w+q_B\le N$, and suppose $c(w)=c(d)$. Apply the four pairs of
Lemma 1 at $x=r_B$, the least element of $B$, with $d$ if $r_B<d$ and
with $-d$ otherwise. The four points lie in $[0,N]$, since
$r_B+w+d\le N$ when $d\le q_B$, and $r_B-d\ge0$ in the other case; the
two points shifted by $\pm d$ lie outside $B$. This is the same
contradiction, so $c(d)\notin U_B^\circ$, and likewise
$c(d)\notin U_{B'}^\circ$. The rest of the proof of Theorem 2 applies.
Finally $t_B^\circ\le t_B+1$. $\square$

So on an interval a palette layer on residue classes loses at most one
bit against the group bound, through the color of a block's largest
difference. These losses do not accumulate beyond a constant factor per
color. The induced coloring of a block $B$ is $j\mapsto c(q_Bj)$ on
$[1,n_B]$, where $n_B=\lfloor(N-r_B)/q_B\rfloor$.

**Corollary 7.** Suppose a Schur coloring of $[1,N]$ with $M$ colors is
assembled from leaf colorings by layers as in Proposition 6, each layer
satisfying the hypotheses of Proposition 6 on its own interval, and each
block's induced coloring being a leaf or again so assembled. Then some
leaf, a coloring of $[1,N_L]$ with $M_L$ colors, satisfies
$N+2\le2^{3M-2M_L}(N_L+2)$.

*Proof.* Discard one-block layers: they have modulus $1$ and change
neither the interval nor its coloring. At each remaining layer choose a
block $B$ with $2^{-t_B^\circ}\le1/q_B$;
it exists because $\sum_B2^{-t_B^\circ}\le1=\sum_B1/q_B$, the residue
classes covering each residue modulo $Q$ once. Since $N<r_B+q_B(n_B+1)$
and $r_B<q_B$, we have $N+2\le q_B(n_B+2)$. Following the chosen blocks
down to a leaf gives $N+2\le2^{\sum_i(t_i+e_i)}(N_L+2)$, where $t_i$ is
the number of colors that the chosen block at level $i$ leaves out of its
interior, $e_i=t_i^\circ-t_i\in\{0,1\}$, and $\sum_it_i=M-M_L$. When
$t_i\ge1$, $e_i\le t_i$. When $t_i=0$ and $e_i=1$, every color is used
inside the chosen block, so a separating color $c_i(d)$ of Proposition 6,
with $d\le q_B$ and $c_i$ the coloring at level $i$, lies in
$U_B\setminus U_B^\circ$; it is therefore the color of the block's
largest difference, and it occurs in the induced coloring $c_{i+1}$ only
at its last position. Such colors are distinct for distinct levels. For a
later level $i'$ of this kind, $c_{i'}(j)=c_{i+1}(Dj)$ for the product $D$
of the intermediate moduli, and its separating difference $d'$ is smaller
than the length of $c_{i'}$, since $d'\le Q'$ and $2Q'-1$ is at most that
length; so its color $c_{i+1}(Dd')$ sits at a position of $c_{i+1}$ before
the last, and differs from the color found at level $i$. Hence at most $M$
levels have $t_i=0$ and $e_i=1$, and
$\sum_i(t_i+e_i)\le2(M-M_L)+M$. $\square$

So residue-class palette recursions on intervals are at most exponential,
like their counterparts in groups, although the constant here is crude.
Partitions into progressions that are not residue classes are not
treated.

## What remains outside rule (R)

The failed step is the source's cross-edge rule. Its consumed input, a
color used inside a block that also colors pairs leaving the block, is
false in setting (G) by Lemma 1, not merely unproved. In setting (Q) it
survives only for pairs whose difference meets the support of every
internal occurrence of the color, and Theorem 2 shows that such pairs
cannot raise the number of blocks. This closes the palette transfer for
all coset and subcube partitions, including the mixed partitions whose
blocks use different subgroups or free sets. It does not close:

- on intervals, partitions into progressions that are not residue
  classes;
- blocks that are not cosets or subcubes, such as sets
  $\{a+\sum_ix_iv_i:x\in\{0,1\}^{r'}\}$ with signed generators $v_i$
  of disjoint supports, whose parallelograms do not fit in the cube;
- constructions outside rule (R), in which a color used inside both
  endpoint blocks colors the pairs between them, and two-block triangles
  are excluded on both sides.

Theorem 2 does fail for the second kind of block. Split $\{0,1\}^4$ into
the four blocks
$\{(x_1,x_2,y_1,y_2):x_1+y_1=s_1,\ x_2+y_2=s_2\}$, sums taken mod $2$.
The [[research/schur_number_growth/evidence/_index|retained evidence]]
holds a Schur-free four-coloring of the signed differences, with palettes
obeying rule (R), in which the block $s=(0,0)$ uses all four colors on its
internal pairs while three other blocks exist; the sum of $2^{-t_B}$ is
$7/4$. Its colors depend on the signs of the differences: the coloring is
a function neither of the support nor of the binary value, and in
$\mathbb F_2^4$ these blocks are translates of one subgroup, where Lemma 1
applies. So the signed cube admits palette layers that no coset partition
of a group allows, and a gain found there would not transfer to Schur
colorings without a further argument.

The third kind is the only identified mechanism for a superexponential
translation-invariant family. In $G=A\oplus B$ with the cosets of $B$ as
blocks, let $\kappa$ be symmetric, and write $C_c$ for the class of $c$
inside $B$ and
$F_{\gamma,c}=\{\beta:\kappa(\gamma,\beta)=c\}$ for $\gamma\ne0$. A
coloring is sum-free exactly when $\kappa$ is sum-free on $B$ and

$$
\bigl(F_{\gamma,c}-F_{\gamma,c}\bigr)\cap C_c=\emptyset,
\qquad
\bigl(F_{\gamma,c}+F_{\gamma',c}\bigr)\cap F_{\gamma+\gamma',c}=\emptyset
$$

for all colors $c$ and all $\gamma,\gamma'\in A$ with $\gamma$,
$\gamma'$ and $\gamma+\gamma'$ nonzero; the first condition is the
triangles with two vertices in one block, the second those meeting three
blocks. These conditions describe every coloring of $A\oplus B$, so they
are a reformulation, not a construction. Reusing an old color $c$
between blocks needs fibres $F_{\gamma,c}$ that are independent sets of
the Cayley graph of $C_c$, and the condition binds at both ends of every
such pair, where the source needs labels only at the end on which the
color is active.

## Coset fibres

The simplest way to meet both conditions uses subgroups. Suppose each
class $C_c$ of $B$ avoids a subgroup $K_c$, and let $\pi_c$ be the
quotient map onto $L_c=B/K_c$. A fibre inside one coset of $K_c$ meets
the first condition, since its differences lie in $K_c$. Putting
$F_{\gamma,c}$ inside the coset $\pi_c^{-1}(M_c\gamma+\mu_c)$, with $M_c$
a homomorphism from $A$ to $L_c$ and $\mu_c\ne0$, also meets the second,
since the sum of the cosets for $\gamma$ and $\gamma'$ is the coset of
$M_c(\gamma+\gamma')+2\mu_c$, not of $M_c(\gamma+\gamma')+\mu_c$. The
extended class then avoids the subgroup
$\{(\gamma,\beta):\pi_c(\beta)=M_c\gamma\}$, with the same quotient, so
the step can be repeated without enlarging the quotients.

Over $\mathbb F_2$ the repeated construction is the following model. Let
$E=\bigoplus_{c=1}^kL_c$ with $L_c=\mathbb F_2^{d_c}$, and write $v_c$ for
the components of $v\in E$. A *coset-fibre structure* is a chain of
subspaces $W_0\subseteq W_1\subseteq\cdots\subseteq W_J$ of $E$, with
vectors $\mu^{(1)},\ldots,\mu^{(J)}\in E$ whose components are all
nonzero, such that

- the nonzero vectors $w\in W_0$ can be colored by colors $c$ with
  $w_c\ne0$ so that every class is sum-free, and
- for $1\le j\le J$, every $w\in W_j\setminus W_{j-1}$ has some
  component $w_c=\mu^{(j)}_c$.

Color each $w\in W_j\setminus W_{j-1}$ by such a $c$. The result is a
sum-free $k$-coloring of $W_J\cong\mathbb F_2^{\dim W_J}$, in which every
vector of color $c$ has a nonzero $c$-component. Indeed, let $w\ne w'$
have color $c$. If both lie in $W_0$, the coloring of $W_0$ handles
$w+w'$. Otherwise let $w$ lie in a stage $j\ge1$ at least as late as that
of $w'$. If $w'$ lies in an earlier stage, then $w+w'$ lies in stage $j$
and its $c$-component $\mu^{(j)}_c+w'_c$ differs from $\mu^{(j)}_c$, so
it does not have color $c$. If $w'$ lies in stage $j$ too, then
$(w+w')_c=0$, so $w+w'$ does not have color $c$ either. One step
$G=A\oplus B$ above is one stage: $W_j$ is the image of
$(\gamma,\beta)\mapsto(\pi_c(\beta)-M_c\gamma)_c$.

**Proposition 5.** In a coset-fibre structure, for each color $c$ let
$m_c$ be the least number of affine hyperplanes of $L_c$ avoiding $0$
that cover $\{\mu^{(1)}_c,\ldots,\mu^{(J)}_c\}$, so that
$m_c\le\min(d_c,J)$. Then

$$
\dim W_J-\dim W_0\le\sum_cm_c,
\qquad
\dim W_J\le\sum_cd_c .
$$

In particular one stage adds at most $k$ dimensions.

*Proof.* Choose linear functionals $\varphi_{c,1},\ldots,\varphi_{c,m_c}$
on $L_c$ with every $\mu^{(j)}_c$ in some $\{\varphi_{c,i}=1\}$, and a
complement $A$ of $W_0$ in $W_J$. Each nonzero $a\in A$ lies in some
$W_j\setminus W_{j-1}$ with $j\ge1$, so $\varphi_{c,i}(a_c)=1$ for some
$c$ and $i$. The product $\prod_{c,i}(1+\varphi_{c,i}(a_c))$ is therefore
the indicator of $a=0$ on $A$. That indicator has degree $\dim A$ as a
reduced polynomial over $\mathbb F_2$, and the product of $\sum_cm_c$
linear forms has degree at most $\sum_cm_c$. For the second bound, a
vector of color $c$ has $w_c\ne0$, so the subspaces
$\{w\in W_J:w_c=0\}$, of codimension at most $d_c$, meet only in $0$.
$\square$

The dependence on $d_c$ and $J$ in Proposition 5 can be removed. The
following argument closes this fixed-quotient model even when these
parameters grow. It uses a binary affine-cover theorem, not an extension
of the palette rule. The same deletion also treats stage-dependent
kernels when their cosets avoid the earlier class, as stated below.

## A sharp bound for the coset-fibre model

The source input is
[[../library/group_theory/brouwer_1986_inequality_binary_vector_spaces/_index|Brouwer's binary affine-cover theorem]],
*An inequality in binary vector spaces*, Discrete Mathematics **59**
(1986), 315--317, Theorem on p. 315 with proof on pp. 315--316: if a finite
binary vector space $H$ is irredundantly covered by $t$ affine subspaces
$a_c+D_c$, then

$$
\operatorname{codim}_H\bigcap_{c=1}^t D_c\le t-1. \tag{B}
$$

Irredundant means that deleting any member destroys the cover. The
subspaces may have different dimensions and need not be hyperplanes.
This is the specialization $V=X=H$ of the source theorem. The source
card records the statement as claims checked against the printed page.
Its proof was read in the institutional copy's PDF text, without an
independent reconstruction or proof verification. The theorem is the
external premise for Proposition 8.

**Proposition 8.** In every coset-fibre structure there is a subspace
$U\subseteq W_0$ such that, writing $k_U$ for the number of colors used
by the seed coloring on $U\setminus\{0\}$,

$$
\dim W_J\le\dim U+k-k_U.
$$

Consequently $\dim W_J-\dim W_0\le k$. If $W_0=0$, then
$\dim W_J\le k$, and this bound is attained. If every subspace of the
seed satisfies $\dim U\le Ck_U$ with $C\ge1$, the whole structure
satisfies $\dim W_J\le Ck$.

*Proof.* It is convenient to write the coordinate maps as linear maps
$\pi_c:V\to L_c$, initially with $V=W_J$. They remain fixed as the
stage varies; only the nonzero values $\mu_c^{(j)}$ vary. We give a
restriction step that preserves this description.

Suppose $V\not\subseteq W_0$, and restrict the original chain to $V$.
Let $j$ be the largest nonempty layer, so $V\subseteq W_j$ and
$V\cap W_{j-1}$ is a proper subspace of $V$. Choose a hyperplane
$H\le V$ containing $V\cap W_{j-1}$, and choose $a\in V\setminus H$.
Every point of the affine half $a+H$ lies in stage $j$. Hence the sets

$$
F_c=(a+H)\cap\pi_c^{-1}(\mu_c^{(j)})
$$

cover $a+H$. Choose an irredundant subcover indexed by $I$, put
$t=|I|$, and omit empty fibres. Each $F_c$ is a coset inside $a+H$ of
$D_c=H\cap\ker\pi_c$. Translate the cover to $H$ and apply (B). For

$$
K=H\cap\bigcap_{c\in I}\ker\pi_c
$$

we obtain $\dim V-\dim K\le1+(t-1)=t$.

All colors in $I$ disappear on $K\setminus\{0\}$: their coordinate
is zero there, whereas a vector assigned color $c$ has a nonzero
$c$-coordinate, both in the seed and at every later stage. Restrict the
chain and the seed coloring to $K$, retain the other coordinate maps,
and keep their stage values. For every vector in a nonempty restricted
layer, its original covering color is still available, so every defining
condition of the model survives. Projection onto the remaining
coordinates is injective: a nonzero vector has its surviving assigned
color's coordinate nonzero. Thus the restricted object can again be
viewed as a subspace of the direct sum of the remaining label spaces.

Repeat until the remaining space is some $U\subseteq W_0$. At least
one color is removed at each step, so termination takes at most $k$
steps. If $r$ colors remain, the sum of the dimension losses is at most
$k-r$, and $k_U\le r$. Therefore
$\dim W_J\le\dim U+k-r\le\dim U+k-k_U$.
For sharpness with $W_0=0$, take $V=\mathbb F_2^k$, the complete
coordinate flag, the $k$ coordinate maps to $\mathbb F_2$, and all stage
values equal to $1$; color by the last nonzero coordinate. The final
assertion follows from
$\dim U+k-k_U\le k+(C-1)k_U\le Ck$. $\square$

This gives an exact answer to the proposed growth mechanism. The stage
values can vary, the label ranks can be arbitrarily large, and the
increments need not have dimension one; nevertheless a fixed seed can
gain at most $k$ dimensions in total. Equivalently, some seed subspace
satisfies $|W_J|\le|U|\,2^{k-k_U}$. The obstruction uses affine cosets
whose direction subspaces avoid the entire corresponding color class,
and preservation under restriction. It does not
bound general sum-free colorings of $\mathbb F_2^n$, for which no such
flag and quotient maps have been supplied, and does not prove
[[theory/ramsey_theory/L264_signed_cube_linear_growth/_index|L264]].
The three-coloring of $\mathbb F_2^4$ by the cubic-residue classes of
$\mathrm{GF}(16)$, checked in the
[[research/schur_number_growth/evidence/_index|finite evidence]],
already lies outside the zero-seed model for every choice of flag and
linear maps: its dimension is $4>3$. Thus the model restriction is
substantive even at the smallest known improvement over one dimension
per color.

**Stage-dependent kernels.** The same conclusion holds in a broader
model. Let $V_0\subseteq\cdots\subseteq V_J=V$ be a flag of binary
subspaces, and let $C_1,\ldots,C_k$ partition $V\setminus\{0\}$.
Suppose the seed restriction to $V_0$ is sum-free. For every $j\ge1$
and every color $c$ occurring in $V_j\setminus V_{j-1}$, suppose there
is a coset $a_{c,j}+K_{c,j}\subseteq V_j$ such that

$$
a_{c,j}\notin K_{c,j},\qquad
C_c\cap(V_j\setminus V_{j-1})\subseteq a_{c,j}+K_{c,j},\qquad
C_c\cap V_{j-1}\cap K_{c,j}=\emptyset. \tag{A}
$$

The subgroups $K_{c,j}$ may vary with $j$ and need not be nested. Then
the coloring is sum-free and, for some $U\subseteq V_0$, still
$\dim V\le\dim U+k-k_U$.

For sum-freeness, two same-color vectors in the same new layer sum into
$K_{c,j}$, which avoids that color throughout $V_j$ by (A). If the
second vector is in an earlier layer, it lies outside $K_{c,j}$, so
adding it leaves the coset $a_{c,j}+K_{c,j}$ while staying in the later
layer. The seed handles the remaining case.

For the bound, repeat Proposition 8 using the cosets in (A) to cover the
highest affine half. Each selected direction avoids its color on the
whole current space, so their common intersection removes the selected
colors. On restriction to any subspace, a nonempty intersection with
$a_{c,j}+K_{c,j}$ is an affine coset with direction equal to the
restricted $K_{c,j}$, it still avoids zero, and the earlier-class
avoidance persists. Thus the same loss of at most $t$ dimensions for $t$
colors can be iterated. Merely changing the kernels while retaining (A)
does not reopen the route.

The argument uses Brouwer's binary theorem only. The general abelian
exponential-cover claim in Nagy, Pach and Tomon,
[arXiv:2205.03389v2](https://arxiv.org/abs/2205.03389v2), was withdrawn
because of an error in Claim 4.5; it supplies no premise here.

## Remaining transfer gap

The one-sided palette transfer is blocked on cosets and coordinate
subcubes by Theorem 2, and on the stated residue partitions by
Corollary 7. Two-sided reuse by binary coset fibres is blocked by
Proposition 8, including changing kernels under (A). These obstructions
compose as failures of
specified construction models, not as an upper bound for every Schur
coloring. No tested construction raises the Schur growth rate above
$380^{1/5}$.

Reopening the two-sided route requires fibres outside (A). The precise
test is whether a construction can use independent fibres whose affine
direction spaces meet the earlier class, while their actual difference
sets avoid it. Such fibres cannot be replaced by their whole affine
cosets. Construct a
symmetric coloring of $(A\oplus B)\setminus\{0\}$ whose fibres cover
every coarse coset and satisfy both displayed two-block and three-block
conditions, and whose new size per added color improves a seed bound.
For a cyclic Schur construction, the group must be cyclic and repeated
summands must also be controlled; a binary example alone would still
need an interval transfer. In
$\mathbb Z_m=\mathbb Z_{m_1}\oplus\mathbb Z_{m_2}$ with coprime factors,
the affine homomorphisms $M_c:A\to B/K_c$ all vanish, so the present
nonzero-coset rule misses every $(\gamma,0)$ with $\gamma\ne0$.
Bohr-set or other nonlinear labels would need their own covering and
preservation theorem. Neither that theorem nor a construction is
provided here.
