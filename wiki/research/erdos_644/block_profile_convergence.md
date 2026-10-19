---
name: research/erdos_644/block_profile_convergence
desc: Positive-coordinate inflation proves fixed-block convergence; a dimension-free refinement also handles sublinear profile supports with growing positive-coordinate slack.
tags: [proved, amplification, restricted-convergence]
sources: []
created: 2026-09-23T00:40:22Z
updated: 2026-09-24T22:12:53Z
---


# research/erdos_644/block_profile_convergence

***

This page proves convergence of the normalized extremal transversal number for
full profile families on any fixed number of blocks. It also proves a common
limit when the permitted number of blocks tends to infinity but is sublinear in
the rank. **It does not prove unrestricted convergence in
[Problem 644](../../problems/set_systems/E0644/_index.md), or determine the seven-edge
coefficient.**

The construction inflates positive profile coordinates by a bounded amount,
leaving zero coordinates zero. Every subsequent integer scaling preserves the
local property. The rank increase and transversal loss are linear in the number
of blocks. There is no completion under convex combinations of profiles, so the
fractional-transversal obstruction for
[Convex-profile amplification](convex_profile_amplification.md) does not apply
to this construction.

## Definitions and the transversal criterion

Fix $r\ge3$. Write $P_r$ for the property that every subfamily of at most $r$
edges has a transversal of size at most two. All families and ground sets in
this page are finite, families are nonempty, and their edges are nonempty. The
exactly-$r$ convention is addressed at the end.

Let $V_1,\ldots,V_d$ be disjoint blocks, with $|V_i|=n_i$. Empty or unused
blocks are allowed. For a nonempty set of integer profiles

$$
S\subseteq\prod_{i=1}^d\{0,\ldots,n_i\},
\qquad \mathbf0\notin S,
$$

the associated **full profile family** is

$$
\mathcal H(S;n)=
\left\{E\subseteq\bigcup_iV_i:
 (|E\cap V_i|)_{i=1}^d\in S\right\}.
$$

It includes every realization of each allowed profile. Its rank is
$\max_{a\in S}\sum_i a_i$. It is $k$-uniform when every profile has coordinate
sum $k$.

A set with block counts $s_i$ is a transversal precisely when

$$
\text{for every }a\in S\text{ there is an }i
\text{ such that }a_i>n_i-s_i.
\tag{1}
$$

Indeed, a profile $a$ has a realization avoiding that set exactly when
$a_i\le n_i-s_i$ in every block.

## Positive-coordinate inflation

**Lemma.** Suppose each allowed profile $a$ is replaced by a profile $b(a)$
satisfying

$$
\begin{cases}
b_i(a)=0,&a_i=0,\\
a_i\le b_i(a)\le\min\{n_i,a_i+D\},&a_i>0,
\end{cases}
\tag{2}
$$

where $D$ is a nonnegative integer. Then the resulting full profile family
satisfies

$$
\tau(\mathcal H_b)\ge\tau(\mathcal H)-dD.
\tag{3}
$$


**Proof.** Let $s_i$ be the block counts of a transversal of $\mathcal H_b$, and
put $u_i=\min\{n_i,s_i+D\}$. These counts describe a transversal of
$\mathcal H$. Otherwise some allowed profile $a$ would satisfy $a_i\le n_i-u_i$
for every $i$. If $a_i>0$, then $u_i<n_i$, so $u_i=s_i+D$ and

$$
b_i(a)\le a_i+D\le n_i-s_i.
$$

The same final inequality holds when $a_i=0$, because then $b_i(a)=0$. By (1),
this contradicts the choice of $s$. Thus

$$
\tau(\mathcal H)\le\sum_i u_i\le\sum_i s_i+dD,
$$

which proves (3). $\square$

Leaving zero coordinates zero is essential. Giving every profile positive demand
in a previously unused small block can create a small transversal, independently
of the original transversal number.

## Inflation that permits every integer scale

Put $C=r-1$. For each original profile $a$, define

$$
a_i^+=
\begin{cases}
0,&a_i=0,\\
\min\{n_i,a_i+C\},&a_i>0.
\end{cases}
\tag{4}
$$

For $L\ge1$, let $\mathcal H_L^+$ be the full profile family on blocks of sizes
$Ln_i$ with allowed profiles $La^+$.

**Lemma.** If $\mathcal H$ has $P_r$, then $\mathcal H_L^+$ has $P_r$ for every
integer $L\ge1$.

**Proof.** Suppose a bad subfamily exists. Repeat rows if necessary to obtain an
ordered bad $r$-tuple. In each block, divide all incidence-pattern
multiplicities among these rows by $L$. The resulting weighted block has total
mass $n_i$ and integer row demands $a_{ij}^+$, where row $j$ comes from an
original profile $a^{(j)}$.

For a point, its spectrum is the subset of row indices containing it. If $S,T$
are any spectra appearing anywhere in the weighted realization, then

$$
S\cup T\ne[r],
\tag{5}
$$

including when $S=T$. Otherwise one or two points would cover the bad tuple.

Consider one nonempty block. By Carathéodory's theorem, its row-demand vector
can be represented using at most $r+1$ of its existing spectra, with nonnegative
multiplicities totaling $n_i$. Remove zero multiplicities. Round the remaining
multiplicities down. Their sum is an integer at most $n_i$; place all leftover
integer mass on any one of the selected spectra.

If a row is saturated in this block, meaning $a_{ij}^+=n_i$, every selected
spectrum contains that row. Its final count is therefore exactly $n_i$.

If $0<a_{ij}^+<n_i$, at least one of the selected spectra omits this row. Thus
at most $r$ selected spectra contain it. Rounding down loses less than $r$ from
its count. The prescribed count and the rounded count are integers, so this loss
is at most $r-1=C$. Since the row is not saturated, (4) gives
$a_{ij}^+=a_{ij}+C$. Its final count is consequently at least $a_{ij}$.

A row with $a_{ij}=0$ has $a_{ij}^+=0$, so every selected spectrum omits it and
its count remains zero. Empty blocks require no operation.

Apply this rounding separately in every block. Each row now has at least its
original profile coordinates, and can be trimmed to that original profile.
Trimming only replaces spectra by subsets, so it preserves (5). Because the
original family is full, the trimmed rows are original edges. Removing
repetitions, if any, gives a bad subfamily of at most $r$ edges in $\mathcal H$,
a contradiction. $\square$

The same proof excludes a weighted bad realization of the inflated profiles on
block capacities $n_i$, without an integrality assumption on its initial
multiplicities. The integer-scale formulation is sufficient below.

## Transversal amplification

For any full profile family $\mathcal F$ on $d$ blocks, let $\mathcal F_L$
denote the family obtained by multiplying all block sizes and allowed profiles
by $L$. Whether or not it has $P_r$, it satisfies

$$
\tau(\mathcal F_L)\ge
L\bigl(\tau(\mathcal F)-d\bigr)+d.
\tag{6}
$$

Indeed, if $s_i$ are the block counts of a transversal of $\mathcal F_L$, then
$\lceil s_i/L\rceil$ are the block counts of a transversal of $\mathcal F$, by
(1). Hence

$$
\tau(\mathcal F)
\le\sum_i\left\lceil\frac{s_i}{L}\right\rceil
\le\frac{\sum_i s_i+d(L-1)}L,
$$

which proves (6).

**Amplification theorem.** Let $\mathcal H$ be a full $d$-block family of rank
at most $k$, with $P_r$ and transversal number $t$. For every integer $L\ge1$,
there is a full $d$-block family $\mathcal H_L$ with $P_r$ and

$$
\boxed{
\operatorname{rank}(\mathcal H_L)\le L\bigl(k+d(r-1)\bigr),
\qquad
\tau(\mathcal H_L)\ge L(t-dr)+d.
}
\tag{7}
$$


**Proof.** Inflate the profiles as in (4). The rank rises by at most $d(r-1)$,
and (3) gives transversal number at least $t-d(r-1)$. All integer scales have
$P_r$ by the preceding lemma. Apply (6) to obtain (7). $\square$

## Rank-bounded convergence for each fixed number of blocks

Let $g_d(k,r)$ be the largest transversal number among full profile families on
at most $d$ blocks, of rank at most $k$, satisfying $P_r$.

This maximum exists. A $P_r$ family has matching number at most two, because
$r\ge3$. The union of a maximal matching is a transversal, so $\tau\le2k$. The
nonempty set of attainable transversal numbers is therefore a subset of
$\{1,\ldots,2k\}$. Also $g_d(k,r)$ is nondecreasing in both $d$ and $k$.

**Theorem.** For every fixed $r\ge3$ and $d\ge1$, the limit

$$
\gamma_{r,d}:=\lim_{k\to\infty}\frac{g_d(k,r)}k
\tag{8}
$$

exists. Every full $d$-block rank-$\le k$ family with $P_r$ satisfies

$$
\boxed{
\tau(\mathcal H)\le
\gamma_{r,d}\bigl(k+d(r-1)\bigr)+dr.
}
\tag{9}
$$


**Proof.** Fix a seed uniformity bound $k$, and take a family with transversal
number $t=g_d(k,r)$. Put $R=k+d(r-1)$. For any $K\ge R$, use
$L=\lfloor K/R\rfloor$ in (7). Since the resulting rank is at most $K$,

$$
\liminf_{K\to\infty}\frac{g_d(K,r)}K
\ge\frac{g_d(k,r)-dr}{k+d(r-1)}.
\tag{10}
$$

Let $k$ tend to infinity along a subsequence attaining the limsup of
$g_d(k,r)/k$. The right side tends to that limsup, because $r,d$ are fixed. Thus
the liminf is at least the limsup, proving (8). Formula (10), now with the limit
on its left, rearranges to (9). $\square$

## A sublinear number of blocks

The constants $\gamma_{r,d}$ are nondecreasing in $d$ and bounded above by two.
Define

$$
\gamma_{r,*}=\sup_{d\ge1}\gamma_{r,d}.
\tag{11}
$$


**Theorem.** If $d(k)$ is integer-valued, $d(k)\to\infty$, and $d(k)=o(k)$, then

$$
\boxed{
\frac{g_{d(k)}(k,r)}k\longrightarrow\gamma_{r,*}.
}
\tag{12}
$$


**Proof.** Applying (9) separately for each integer $d$, and using
$\gamma_{r,d}\le\gamma_{r,*}\le2$, gives

$$
g_d(k,r)
\le\gamma_{r,*}k+(3r-2)d.
\tag{13}
$$

This proves the upper limit in (12). For every fixed $d$, eventually
$d(k)\ge d$, so the lower limit is at least $\gamma_{r,d}$. Take the supremum
over fixed $d$. $\square$

No monotonicity of the function $d(k)$ is required.

## Uniformization with one extra block

Let $h_d(k,r)$ be the corresponding maximum among full profile families on at
most $d$ blocks whose edges all have size exactly $k$. Then

$$
h_d(k,r)\le g_d(k,r)\le h_{d+1}(k,r).
\tag{14}
$$

Only the second inequality needs proof. Take a rank-$\le k$ full profile family
of transversal number $t$. Add a disjoint dummy block of size $k+t-1$, and
replace each profile $a$ by

$$
(a,k-|a|).
$$

Include every realization of every new profile. All new edges have size $k$, and
every local cover of the core edges covers the padded edges, so $P_r$ remains
true.

An old $t$-point transversal still covers the new family. Conversely, a set of
at most $t-1$ points misses some core edge after restriction to the old ground.
At least

$$
k+t-1-(t-1)=k
$$

dummy points remain available, enough to pad that missed edge while avoiding the
proposed transversal. Thus the transversal number remains exactly $t$, proving
(14).

It follows from (12) and (14) that whenever $d(k)\to\infty$ and $d(k)=o(k)$,

$$
\boxed{
\frac{h_{d(k)}(k,r)}k\longrightarrow\gamma_{r,*}.
}
\tag{15}
$$

Indeed, for all sufficiently large $k$,

$$
g_{d(k)-1}(k,r)\le h_{d(k)}(k,r)\le g_{d(k)}(k,r),
$$

and both outer terms have the limit in (12).

## Uniform convergence with the same fixed number of blocks

For completeness, $h_d(k,r)/k$ also converges for each fixed $d$, without adding
a block. The seed losses below are larger than those in (7), but depend only on
$r,d$.

Put

$$
B_d=2^d-1+d,
\qquad \Delta=d(r-1).
\tag{16}
$$


### Increasing uniformity by a bounded amount

For every integer $s\ge0$,

$$
h_d(k+s,r)\ge h_d(k,r)-B_ds.
\tag{17}
$$

To prove this, start with a $k$-uniform full profile family of transversal
number $t$. The **positive support** of a profile $a$ is $J(a)=\{i:a_i>0\}$.

Delete profiles whose positive-support blocks have total size below $k+s$. For a
fixed nonempty support $J$, the deleted edges with that support are $k$-sets on

$$
N_J=\sum_{i\in J}n_i\le k+s-1
$$

points. If such edges exist, then $N_J\ge k$, and any $N_J-k+1$ points of their
union of blocks meet all of them. Thus this subfamily has transversal number at
most $s$. There are at most $2^d-1$ nonempty supports, so all deleted edges
together have a transversal of size at most $(2^d-1)s$.

Each remaining profile can be extended, within its existing positive support, to
coordinate sum $k+s$. Include all realizations of the extended profiles. Every
output edge contains an original edge; hence the output retains $P_r$.
Coordinate increases are at most $s$, and zero coordinates remain zero. Formula
(3) bounds the additional transversal loss by $ds$. This proves (17). If no
profiles remain, then $t\le(2^d-1)s$ and the right side of (17) is nonpositive,
so the inequality follows from any nonempty admissible family.

### A same-block uniform amplifier

Start with a $k$-uniform seed of transversal number $t$. Delete profiles whose
positive-support blocks have total size below $k+\Delta$. The preceding support
argument loses at most $(2^d-1)\Delta$ in transversal number.

Inflate each remaining profile as in (4). Its coordinate sum is at most
$k+\Delta$. Extend it within its original positive support to a profile $b$ of
sum exactly $k+\Delta$. This is possible because the retained support has
capacity at least $k+\Delta$.

Measured from the original profile, every coordinate has increased by at most
$\Delta$, and zero coordinates remain zero. By (3), the resulting uniform full
profile family $\mathcal B$ satisfies

$$
\tau(\mathcal B)\ge t-B_d\Delta.
\tag{18}
$$

Every integer scale of $\mathcal B$ has $P_r$: trim each row to the scaled
inflated profile from which it arose, and apply the all-scales lemma. Formula
(6) therefore yields, for every $L\ge1$, a full $d$-block $P_r$ family of
uniformity $L(k+\Delta)$ and transversal number at least

$$
L\bigl(t-B_d\Delta-d\bigr)+d.
\tag{19}
$$

If deletion leaves no profiles, then $t\le(2^d-1)\Delta$ and the expression in
(19) is nonpositive. In this case any nonempty one-edge family of the prescribed
uniformity supplies the stated lower bound.

### Taking the limit

**Theorem.** For every fixed $r\ge3$ and $d\ge1$, the limit

$$
\beta_{r,d}:=\lim_{k\to\infty}\frac{h_d(k,r)}k
\tag{20}
$$

exists.

**Proof.** Fix a seed $k$ with $t=h_d(k,r)$ and put $R=k+\Delta$. For a large
target uniformity $K$, write $K=LR+s$ with $0\le s<R$. Use (19), then apply (17)
to increase its uniformity by $s$. The further transversal loss is at most
$B_dR$, independent of $L$. Consequently

$$
\liminf_{K\to\infty}\frac{h_d(K,r)}K
\ge\frac{h_d(k,r)-B_d\Delta-d}{k+\Delta}.
\tag{21}
$$

Taking a limsup subsequence of seed values $k$ proves (20). $\square$

The argument also proves the finite inequality

$$
h_d(k,r)\le\beta_{r,d}(k+\Delta)+B_d\Delta+d.
\tag{22}
$$

The rank-bounded and uniform fixed-$d$ limits have not been identified with one
another. What follows from (14) is

$$
\beta_{r,d}\le\gamma_{r,d}\le\beta_{r,d+1},
\qquad
\sup_d\beta_{r,d}=\sup_d\gamma_{r,d}=\gamma_{r,*}.
\tag{23}
$$


## A bound independent of the total number of blocks

The additive losses above can instead be charged to the number of blocks
actually used by a transversal. This extends the convergence result to a
larger restricted class; it does not supply an unrestricted amplifier.

Put $C=r-1$. Suppose a full-profile $P_r$ family $\mathcal H$ has rank at
most $k$, transversal number $t$, and the following two properties:

- every allowed profile has at most $h$ positive coordinates;
- whenever $a_i>0$, its slack satisfies $n_i-a_i\ge B$, where $B>C$ is an
  integer.

**Amplification theorem.** For every integer $L\ge1$ there is a
full-profile $P_r$ family $\mathcal H_L$ with

$$
\operatorname{rank}(\mathcal H_L)\le L(k+Ch),\qquad
\boxed{\tau(\mathcal H_L)\ge
t\,\frac{L(B-C)+1}{B+1}.}
\tag{24}
$$

In particular, the bounds do not depend on the total number of blocks.

**Proof.** Inflate every positive coordinate to $a_i+C$, keeping zero
coordinates zero, and call the resulting family $\mathcal F$. Saturation
does not occur, because $B>C$. The all-scales lemma proved above gives
$P_r$ for every integer scale of $\mathcal F$. Inflation raises the rank
by at most $Ch$.

Write $b=B-C$. Let $s_i$ be the block counts of a minimum transversal of
$\mathcal F$, and put $s=\sum_i s_i$. Every used block has $s_i\ge b+1$.
Indeed, a count between one and $b$ exceeds none of the positive-profile
slacks, which are all at least $b$, and cannot hit a zero coordinate.
Such a count could therefore be removed without losing the transversal
property (1).

There are consequently at most $s/(b+1)$ used blocks. Increase the count
in each used block by $C$, capped at $n_i$, and leave unused blocks
unused. These counts cover the original family: an inflated profile hit
in block $i$ satisfies $s_i>n_i-a_i-C$, so the increased count exceeds
$n_i-a_i$. Thus

$$
t\le s+C\frac{s}{b+1},\qquad
\tau(\mathcal F)\ge t\frac{b+1}{B+1}.
\tag{25}
$$


Now scale $\mathcal F$ by $L$. A minimum transversal of size $u$ in this
scale uses at most $u/(Lb+1)$ blocks, by the same argument. Rounding each
used count upward after dividing by $L$ gives a transversal of
$\mathcal F$. Since an integer $z$ satisfies
$\lceil z/L\rceil\le z/L+(L-1)/L$,

$$
\tau(\mathcal F)
\le \frac uL+\frac{L-1}{L}\frac{u}{Lb+1}
=u\frac{b+1}{Lb+1}.
\tag{26}
$$

Combining (25) and (26) proves (24). $\square$

Each seed has a finite number $d$ of blocks. Apply the already proved
fixed-$d$ convergence to its amplified families and let $L\to\infty$.
Since $\gamma_{r,d}\le\gamma_{r,*}$, this gives the finite bound

$$
\boxed{t\le\gamma_{r,*}(k+Ch)\frac{B+1}{B-C}.}
\tag{27}
$$

Consequently, $h=o(k)$ and $B\to\infty$ suffice for the upper coefficient
$\gamma_{r,*}$, irrespective of the total number of blocks. For example,
the support hypothesis holds if the smallest positive profile coordinate
tends to infinity.

### Convergence with sparse profile supports and growing slack

Let $h(K),B(K)$ be positive integer functions tending to infinity, with
$h(K)=o(K)$ and $B(K)=o(K)$. Maximize the transversal number over finite
full-profile $P_r$ families of rank at most $K$ in which every profile
uses at most $h(K)$ blocks and every positive coordinate has slack at
least $B(K)$. There is no bound on the total number of blocks. Write this
maximum as $M(K)$; it is well defined for all sufficiently large $K$.
Indeed, all $K$-sets on a single block of size $K+B(K)$ satisfy the
requirements eventually: any $r$ have a common point when
$K>(r-1)B(K)$. The universal bound $\tau\le2K$ ensures a maximum exists.

**Theorem.**

$$
\frac{M(K)}K\longrightarrow\gamma_{r,*}.
\tag{28}
$$


The upper bound follows immediately from (27). For the lower bound fix
$d$ and an integer $B_0>C$. Take a full $d$-block rank-$\le k$ seed with
$P_r$ and transversal number $t=g_d(k,r)$. Delete profiles having a
positive coordinate with slack less than $B_0$. All deleted profiles
together have a transversal of size at most $dB_0$: in block $i$, any
$\min(B_0,n_i)$ points meet every realization of any such coordinate.
The remaining family therefore has transversal number at least
$t-dB_0$, and all its positive-coordinate slacks are at least $B_0$.
For large enough $k$ this remaining family is nonempty whenever
$\gamma_{r,d}>0$; if $\gamma_{r,d}=0$, the desired lower bound for this
$d$ is trivial.

Apply (24) with $h=d$ and
$L=\lfloor K/(k+Cd)\rfloor$. The outputs have rank at most $K$, use at
most $d$ blocks per profile, and have positive-coordinate slacks at least
$L(B_0-C)$. With the seed fixed, these satisfy the prescribed support and
slack bounds for all sufficiently large $K$, because $h(K)\to\infty$
and $B(K)=o(K)$. Hence

$$
\liminf_{K\to\infty}\frac{M(K)}K
\ge \frac{g_d(k,r)-dB_0}{k+Cd}\frac{B_0-C}{B_0+1}.
$$

First let $k\to\infty$, then $B_0\to\infty$, and finally take the
supremum over fixed $d$. This proves (28).

Arbitrary singleton-block representations have $h=k$ for a $k$-uniform
family and slack zero at every positive coordinate. Thus neither (24)
nor (28) includes unrestricted families. No reduction to the hypotheses
of (27) has been established, and $\gamma_{7,*}=3/4$ remains unproved.

## Convention and remaining scope

For a family with at least $r$ distinct edges, testing exactly $r$ distinct
edges is equivalent to $P_r$: a smaller bad subfamily can be extended to $r$
edges. A family with fewer than $r$ edges has transversal number at most $r-1$.
Thus replacing the at-most-$r$ convention by the exactly-$r$ convention does not
change any of the normalized limits proved here.

An arbitrary finite family can be represented as a full profile family using
singleton blocks. That observation does not give unrestricted convergence: the
number of blocks can be much larger than the rank, and the losses in (7) then
give no useful estimate. No reduction of an arbitrary near-extremal family to
$o(k)$ blocks has been proved. Completing an arbitrary family under block
permutations need not preserve $P_r$.

The constants $\gamma_{r,d}$, $\beta_{r,d}$, and $\gamma_{r,*}$ are not
determined here. Since rank-bounded families can be privately padded to
uniformity without changing their transversal numbers or local properties, the
unrestricted lower limit is at least $\gamma_{r,*}$. The complete-family lower
bound and the established unrestricted upper bound, recorded in
[Research](_index.md) and [Complete families](complete_families.md), imply only

$$
\frac34\le\gamma_{7,*}\le\frac78.
$$

In particular, neither $\gamma_{7,*}=3/4$ nor unrestricted fixed-$r$ convergence
follows from this page.
