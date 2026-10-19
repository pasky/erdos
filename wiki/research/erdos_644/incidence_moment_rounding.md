---
name: research/erdos_644/incidence_moment_rounding
desc: Adaptive incidence moments give low-fractional-cover residuals and prove that P7 families of sublinear VC dimension have sublinear transversal number.
tags: [proved, reductions, fractional-covers, vc-dimension]
sources: []
created: 2026-09-23T02:56:00Z
updated: 2026-09-24T22:12:53Z
---


# research/erdos_644/incidence_moment_rounding

***

This is a proved restricted result, not a resolution of the unrestricted Erdős
problem. All hypergraphs are finite families of nonempty sets; rank means
maximum edge size. Write $P_r$ when every subfamily of at most $r$ edges has
a transversal of size at most two. For a vertex set $W$, let

$$
\mathcal H_W=\{E\in\mathcal H:E\cap W=\varnothing\}.
$$

Write $\tau^*$ for fractional transversal number. All logarithms are natural.

Fractional transversal number is the minimum total nonnegative vertex weight
giving every edge weight at least one. Its linear-program dual is the maximum
total edge weight giving every vertex weighted degree at most one. The VC
dimension is the largest size of a set $D$ for which the traces $E\cap D$
realize every subset of $D$.

If the local hypothesis is instead stated for exactly $r$ distinct edges, it
implies $P_r$ whenever the family has at least $r$ edges. Families with
fewer than $r$ edges have $\tau\le r-1$ and should be handled separately;
the deletion theorem below uses the at-most-$r$ formulation.

## The deletion theorem

**Theorem.** Let $b\ge2$, and let $\mathcal H$ have rank at most $k$ and
property $P_{2b+1}$. For every real $Z>0$, there is a vertex set $X$ such
that

$$
\boxed{
|X|\le\left\lfloor\binom{2b}{b}\frac{k}{Z^{b-1}}\right\rfloor,
\qquad \tau^*(\mathcal H_X)\le Z.}
\tag{1}
$$


**Proof.** Put $B=\binom{2b}{b}$ and $a=Bk/Z^{b-1}$. Suppose every residual
obtained by deleting at most $\lfloor a\rfloor$ vertices has fractional
transversal number greater than $Z$.

For any such nonempty residual, normalize an optimal fractional matching to a
probability distribution on its edges. Finite linear-program duality shows that
the probability $p_v$ of any vertex is at most $1/Z$.

We choose $2b$ reference edges successively, maintaining maximum vertex degree
at most $b$. After $j$ choices, let $d_j(v)$ be the vertex degrees and put

$$
N_h(j)=\sum_v\binom{d_j(v)}h\quad(1\le h\le b),
\qquad
\Phi_j=\sum_{h=1}^b
\binom{2b-j}{b-h}Z^{h-1}N_h(j).
\tag{2}
$$

Binomial coefficients with negative lower argument or lower argument greater
than upper argument are zero. All coefficients in (2) are nonnegative, and the
coefficient of $N_b(j)$ is $Z^{b-1}$.

Let $D_j$ be the set of vertices currently of degree $b$. Because degrees
are at most $b$, $|D_j|=N_b(j)$. Inductively we will have $\Phi_j\le Bk$,
so $|D_j|\le a$. Sample the next edge from the fractional-matching
distribution in $\mathcal H_{D_j}$. This preserves the degree bound. Writing
$\Delta N_h=N_h(j+1)-N_h(j)$, Pascal's identity gives

$$
\mathbb E\Delta N_1\le k,\qquad
\mathbb E\Delta N_h\le\frac{N_{h-1}(j)}Z\quad(2\le h\le b).
\tag{3}
$$

Indeed, adding an edge changes $N_h$ by $\sum_{v\in E}\binom{d_j(v)}{h-1}$,
and every vertex has selection probability at most $1/Z$.

Put $c_h(j)=\binom{2b-j}{b-h}$, with $c_{b+1}(j)=0$. The identity

$$
c_h(j)=c_h(j+1)+c_{h+1}(j+1)
$$

and (3) cancel all terms involving the old $N_h(j)$, leaving

$$
\mathbb E\Phi_{j+1}\le\Phi_j+
k\binom{2b-j-1}{b-1}.
\tag{4}
$$

Choose a realization satisfying this bound. Since $\Phi_0=0$ and

$$
\sum_{j=0}^{2b-1}\binom{2b-j-1}{b-1}
=\binom{2b}{b}=B,
$$

every intermediate potential is at most $Bk$, justifying each residual
sampling step.

After $2b$ choices, $\Phi_{2b}=Z^{b-1}N_b(2b)$, so
$|D_{2b}|\le\lfloor a\rfloor$. The hypothesis gives
$\tau^*(\mathcal H_{D_{2b}})>Z>0$, so this residual contains an edge. Choose
it as one further edge. The resulting $2b+1$ edges all have vertex degrees at
most $b$; two vertices therefore meet at most $2b$ of them. This contradicts
$P_{2b+1}$. Repeated selected edges are harmless: removing repetitions
preserves the absence of a two-cover. $\square$

No assumption $Z\ge1$ is needed. In particular, for $P_7$, deletion of at
most $\lfloor20k/Z^2\rfloor$ vertices leaves fractional transversal number at
most $Z$.

For any integer $\ell\ge1$, the same proof applies when every
at-most-$\ell b+1$-edge subfamily has an $\ell$-point transversal: replace
$2b$ throughout by $\ell b$. The deletion budget becomes
$\lfloor\binom{\ell b}{b}k/Z^{b-1}\rfloor$.

## A hereditary fractional-to-integral consequence

Suppose additionally that for every vertex set $W$,

$$
\tau(\mathcal H_W)\le\Gamma\tau^*(\mathcal H_W).
\tag{5}
$$

Only vertex-deletion residuals are required, not arbitrary subfamilies. A set
$X$ from (1), together with a transversal of $\mathcal H_X$, covers
$\mathcal H$. Thus for every $Z>0$,

$$
t:=\tau(\mathcal H)\le\frac{Bk}{Z^{b-1}}+\Gamma Z.
\tag{6}
$$

The right side is minimized at $Z^b=(b-1)Bk/\Gamma$, giving

$$
\boxed{
t^b\le
\frac{b^b}{(b-1)^{b-1}}\binom{2b}{b}
k\Gamma^{b-1}.}
\tag{7}
$$


## A self-contained VC estimate

If a nonempty hypergraph $\mathcal F$ has VC dimension at most $d\ge1$ and
fractional transversal number $z$, then

$$
\tau(\mathcal F)\le\left\lceil16dz\log(16z)\right\rceil
\le17dz\log(16z).
\tag{8}
$$

Here VC dimension is the ordinary dimension of the edge family on its vertex
ground set.

For completeness, normalize a fractional transversal to a vertex probability
measure $\rho$, under which every edge has measure at least $1/z$. Put
$L=\log(16z)$, $m=\lceil16dzL\rceil$, and take two independent samples
$X,Y$ of size $m$, with replacement. If $X$ misses an edge $E$, its
number of occurrences in $Y$ is at least $m/(2z)$ with probability at least
$1/2$: its mean is at least $m/z$, variance is at most its mean, and
Chebyshev applies since $m/z\ge16\log16>8$.

Equivalently, first generate a pooled labeled sample of $2m$ independent
vertices and assign its positions uniformly to two halves. Conditional on this
pool, there are at most $(2em/d)^d$ edge traces, by the elementary Sauer trace
bound. Each trace of size at least $m/(2z)$ lies entirely in the second half
with probability at most $2^{-m/(2z)}$. Thus the probability that $X$ is not
a transversal is at most

$$
2(2em/d)^d2^{-m/(2z)}<1.
$$

To check the constants, $m\le17dzL$ and

$$
\log(2em/d)\le\log(34ezL)
=L+\log L+\log(34e/16)\le3L.
$$

The probability is therefore at most $2\exp(-(8\log2-3)dL)<1$. The Sauer bound
itself follows from the induction $s(n,d)\le s(n-1,d)+s(n-1,d-1)$; sample
repetitions cannot increase VC dimension. This proves (8).

Suppose now that $\mathcal H$ has $P_{2b+1}$, rank at most $k$, and VC
dimension $1\le d\le k$. A maximal matching has at most two edges, so
$t\le2k$. Every residual has VC dimension at most $d$ and transversal number
at most $t$. Consequently (5) holds with

$$
\Gamma=17d\log(32k/d).
\tag{9}
$$

Indeed, for a nonempty residual of fractional transversal number $z\le2k/d$,
apply (8). If $z>2k/d$, its transversal number is at most
$t\le2k<dz\le\Gamma z$. Empty residuals cause no issue.

Combining (7) and (9) gives

$$
\boxed{
\tau(\mathcal H)^b\le
\frac{b^b}{(b-1)^{b-1}}\binom{2b}{b}17^{b-1}
kd^{b-1}\log^{b-1}(32k/d).}
\tag{10}
$$


In particular, for $P_7$, take $b=3$:

$$
\boxed{\tau(\mathcal H)^3\le39015\,kd^2\log^2(32k/d).}
\tag{11}
$$

Every fixed $b\ge2$ therefore gives $\tau=o(k)$ when $d=o(k)$. A nonempty
family of VC dimension zero has only one distinct edge and transversal number
one.

**Robust VC consequence for $P_7$.** Suppose $\tau(\mathcal H)\ge\alpha k$,
and fix $0<\delta\le\alpha$. After deleting any vertex set $W$ of size at
most $(\alpha-\delta)k$, the residual has transversal number at least
$\delta k$. If its VC dimension is $d_W$, then, for $k>1/\delta$, it is
positive and satisfies

$$
\delta^3\le39015\left(\frac{d_W}{k}\right)^2
\log^2\left(\frac{32k}{d_W}\right).
$$

Since $x\log(32/x)\to0$ as $x\downarrow0$, this forces $d_W\ge c_\delta k$
for some $c_\delta>0$, uniformly over all such deletions. Thus a putative
linear-transversal counterexample retains linear VC dimension under every
deletion that leaves a fixed positive linear transversal number.

## Checks on scope and sharpness

The local threshold five for the conclusion $d=o(k)\Rightarrow\tau=o(k)$
cannot be lowered to four: projective-plane lines have $P_4$, VC dimension
two, and $\tau=k=q+1$.

For fixed $b$, the power $k^{1/b}$ in (10) is sharp up to logarithmic
factors when VC dimension is bounded. Take the hyperplanes of
$\mathrm{PG}(b+1,q)$, where $q$ is a prime power. Their rank is
$k_q=(q^{b+1}-1)/(q-1)=\Theta(q^b)$, their transversal number is $q+1$, and
their VC dimension is $b+1$. Any $b+1$ hyperplanes intersect, so the family
even has $P_{2b+2}$. A projective line is a transversal. There are
$N_q=(q^{b+2}-1)/(q-1)$ hyperplanes and each point is on $k_q$ of them;
since $qk_q=N_q-1$, at most $q$ points cannot meet all hyperplanes. For VC
dimension, a shattered collection must be linearly independent and lie in a
hyperplane, so has size at most $b+1$; the coordinate points of one hyperplane
attain this bound.

### A caution about VC-sensitive set-pair compression

The VC reduction suggested replacing the usual exponential critical set-pair
bound by a polynomial depending on VC dimension. Formal cross-intersection
certificates alone do not justify this. In a full binary tree of depth $h\ge2$,
let $A_x$ be the $h$ nonroot vertices on the path to leaf $x$, and let $B_x$
contain the sibling of each vertex on that path. Then

$$
|A_x|=|B_x|=h,\quad A_x\cap B_x=\varnothing,\quad
A_x\cap B_y\ne\varnothing\quad(x\ne y).
$$

The cross-intersection occurs at the first divergence of the paths. There are
$2^h$ pairs, but the family of the $A_x$ has VC dimension one: comparable
vertices cannot realize the descendant-only trace, while incomparable vertices
cannot occur together. Thus even a fixed-degree polynomial bound in
$|A_x|+|B_x|$ fails at VC dimension one for general set-pair systems.

The actual transversal number of the path family is two, witnessed by the two
children of the root, and it is not transversal-critical. This does **not**
refute a stronger bound assuming genuine transversal-criticality and certificate
size $\tau-1$. No such stronger bound was proved here.

The transversal inequalities also extend to infinite families by the
[finite-witness compactness argument](structural_reductions.md#passage-to-finite-critical-families),
since every finite subfamily has no larger VC dimension. The deletion theorem
itself was proved above only for finite families.

No bound here controls the remaining regime $d=\Theta(k)$, which includes the
complete-family examples at the conjectured three-quarter scale. Neither
unrestricted assertion of the original problem follows.

## An unconditional stronger deletion target is false

One proposed strengthening was that deleting $o(k)$ vertices from any
$P_7$ family should leave fractional transversal number at most
$7/4+o(1)$. This assertion, without a high-transversal hypothesis, is
false.

For sufficiently large $k$, let $n=\lfloor6k/5\rfloor-1$, take two
disjoint $n$-point blocks, and let $\mathcal H$ consist of all
$k$-sets in either block. Every at-most-six edges in one block have a
common point, since $6k-5n>0$. A selection of at most seven edges
meeting both components therefore has a one-point cover in each
component. A selection lying in one component is covered by one point
for its first at-most-six rows and one for the remaining row. Thus
$\mathcal H$ has $P_7$.

For a complete $k$-uniform family on $N\ge k$ points, the fractional
transversal number is $N/k$. Uniform weights $1/k$ give the upper
bound; summing all edge constraints gives the lower bound. Consequently

$$
\tau(\mathcal H)=2(n-k+1)=(2/5+o(1))k,\qquad
\tau^*(\mathcal H)=2n/k=12/5+o(1).
$$

After deleting any $o(k)$ vertices, both residual components are still
complete $k$-uniform families on $n-o(k)$ points. Their fractional
transversal numbers still sum to $12/5+o(1)$, rather than $7/4+o(1)$.

This rules out only the unconditional deletion target. It does not rule
out a theorem assuming $\tau>(3/4+\varepsilon)k$, nor an estimate
balancing the deletion cost against the residual fractional transversal
number. No such estimate sufficient for Problem 644 was proved.
