---
name: research/erdos_644/distinct_seven_xor
desc: Large transversal number forces seven distinct edges with small total XOR, excluding a nonlinear total-XOR construction criterion.
tags: [proved, coding, method-obstruction]
sources: []
created: 2026-09-23T06:00:00Z
updated: 2026-09-24T22:12:53Z
---


# research/erdos_644/distinct_seven_xor

***

Avoiding small threefold XORs already fails to give an asymptotic
counterexample in the range treated in
[Forbidden distances](forbidden_distances.md). Requiring only that
seven **distinct** edges have large total XOR might appear weaker:
one can no longer insert repeated pairs to turn a three-tuple into
a seven-tuple. The following argument rules out this alternative
throughout $7k/4\le n<2k$, without an affine-code assumption.

## Statement

**Theorem.** Fix $\varepsilon>0$. For all sufficiently large $k$, every
$k$-uniform family $\mathcal H$ on $n$ points satisfying

$$
\frac74k\le n<2k,
\qquad \tau(\mathcal H)>(3/4+\varepsilon)k
\tag{1}
$$

contains seven distinct edges such that

$$
\left|A_1\triangle\cdots\triangle A_7\right|\le4n-7k.
\tag{2}
$$

No local two-cover hypothesis is used.

## An elementary small threefold XOR

Take $t=\lceil(3/4+\varepsilon/2)k\rceil$, so $t<\tau$ for
sufficiently large $k$, and write

$$
w=n-t=k+j.
$$

Every $w$-set contains an edge, since its complement has size $t$.
In particular $j\ge0$. Also $j\le k/4-\varepsilon k/2$.

Fix $A\in\mathcal H$. Choose a $w$-set $W$ with

$$
|W\cap A|=k-\lceil w/2\rceil.
\tag{3}
$$

The requested intersection is nonnegative for large $k$. The number
of requested points outside $A$ is $j+\lceil w/2\rceil$, at most
$n-k=j+t$, because $n<3t$ implies $\lceil w/2\rceil\le t$ for
large $k$. Thus (3) is feasible.

Choose $B\in\mathcal H$ with $B\subseteq W$. Its intersection with
$A$ lies between $k-j-\lceil w/2\rceil$ and
$k-\lceil w/2\rceil$. Consequently

$$
w\le |A\triangle B|\le k+3j+1.
$$

There is therefore $C\in\mathcal H$ contained in $A\triangle B$,
and

$$
|A\triangle B\triangle C|\le3j+1<k.
\tag{4}
$$

The three edges are distinct, since a repeated pair would make their
XOR have weight $k$.

## Four further edges with zero XOR

Counting $w$-sets containing an edge gives

$$
|\mathcal H|\ge\frac{\binom nk}{\binom wk}.
\tag{5}
$$

We check that this is exponentially larger than $2^{n/2}$ throughout
the needed parameter range. Let $h(x)=-x\log x-(1-x)\log(1-x)$,
and put $\alpha=n/k$. Since $t\ge3k/4$, the monotonicity of
$u h(1/u)$ for $u\ge1$ and the uniform entropy estimates for binomial
coefficients give

$$
\log|\mathcal H|-\frac n2\log2
\ge kF(\alpha)-O(\log k),
$$

where

$$
F(\alpha)=\alpha h(1/\alpha)
 -(\alpha-3/4)h(1/(\alpha-3/4))
 -\frac\alpha2\log2.
\tag{6}
$$

For $7/4<\alpha\le2$,

$$
F'(\alpha)=
\log\frac{\alpha(\alpha-7/4)}{(\alpha-1)(\alpha-3/4)}
-\tfrac12\log2<0.
$$

The denominator of the displayed ratio exceeds its numerator by
$3/4$. By continuity at $7/4$, therefore,

$$
F(\alpha)\ge F(2)=3\log2-\frac54\log5>0;
\tag{7}
$$

the last inequality follows from $2^{12}>5^5$.

Delete $A,B,C$ from the family. By (5)--(7), the remaining number of
edges is exponentially larger than $2^{n/2}$. In particular, the
number of unordered pairs exceeds $2^n-1$. Two different pairs have
the same XOR. These pairs are disjoint, because a shared endpoint
would force their other endpoints to agree. We have thus found four
distinct edges $D_1,D_2,D_3,D_4$, all different from $A,B,C$, with

$$
D_1\triangle D_2\triangle D_3\triangle D_4=\varnothing.
$$

Adjoin these edges to (4). Their sevenfold XOR has size at most
$3j+1$, whereas

$$
(4n-7k)-(3j+1)=n-4k+3t-1>0
$$

by (1) and the choice of $t$. This proves (2).

## Scope of the obstruction

For any bad seven-tuple on $n<2k$ points, each point has degree at
most four. Every point counted in the total XOR has odd degree one
or three, so it contributes at least one to the total deficiency
$4n-7k$. Thus (2) is a necessary condition for a bad tuple. Avoiding
(2) for all seven distinct members is a sufficient way to enforce
$P_7$, but the theorem proves that this strategy cannot attain a
fixed excess above three quarters in the displayed ground-size
range.

The theorem does not say that its seven edges have no two-cover.
It excludes only a criterion based on total XOR, not one using the
whole Fano incidence pattern or all seven line-triple XORs. In
particular it is not an upper bound on arbitrary $P_7$ families.
