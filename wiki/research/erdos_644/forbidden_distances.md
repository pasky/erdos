---
name: research/erdos_644/forbidden_distances
desc: A forbidden-distance argument for arbitrary nonlinear families, and a narrow-ground upper bound of (2k+n)/5+o(k) for the local seven-edge property.
tags: [proved, restricted-upper-bounds, methods, obstruction]
sources: []
created: 2026-09-23T00:43:37Z
updated: 2026-10-13T05:28:09Z
---


# research/erdos_644/forbidden_distances

***

[Distinct-seven XOR](distinct_seven_xor.md) gives a separate elementary
obstruction to requiring large total XOR only for seven distinct
members, throughout $7k/4\le n<2k$. It neither strengthens the
unrestricted transversal bound nor requires affine closure.

The polynomial obstruction in [Coding refinement](coding_refinement.md) does not
require an affine code when it is applied directly to a constant-weight family.
This gives two proved consequences.

First, the refined sufficient condition based on the minimum weight of a
threefold symmetric difference cannot yield an asymptotic counterexample, even
for arbitrary nonlinear families. Second, a $k$-uniform family on $n$ points
with the local seven-edge property satisfies

$$
\tau\le\frac{2k+n}{5}+o(k)
\qquad\left(\frac74k\le n\le\frac{30}{17}k\right).
\tag{1}
$$

The error is uniform throughout the displayed interval. In particular, if
$n=7k/4+o(k)$, this proves the conjectured coefficient for that restricted
ground-set regime. These results do not prove the conjecture for arbitrary
families or the convergence assertion in
[Problem 644](../../problems/set_systems/E0644/_index.md).

All families below are finite, nonempty, and $k$-uniform on a specified
$n$-point ground set. Write $P_7$ for the condition that every subfamily of at
most seven edges has a transversal of size at most two. For a family with at
least seven distinct edges this is equivalent to the exactly-seven convention.
Families with fewer than seven edges have transversal number at most six and do
not affect any asymptotic assertion here.

## A covering family must realize a prescribed distance

**Distance lemma.** Suppose $k\to\infty$,

$$
\frac74k\le n\le\frac{30}{17}k,
\qquad \frac34k\le t<\tau(\mathcal H),
$$

where $t$ is an integer, and put $w=n-t$. Then there are distinct
$A,B\in\mathcal H$ with

$$
w\le |A\triangle B|=w+o(k).
\tag{2}
$$

More precisely, if $p$ is the least prime at least $w/2$, then $\mathcal H$
realizes the distance $2p$ for all sufficiently large $k$. The error and the
sufficiently-large threshold are uniform over the stated range.

### Counting from the transversal number

Every $w$-point set contains an edge: its complement has size $t$ and is not a
transversal. In particular $w\ge k$. Counting pairs consisting of an edge and a
containing $w$-set gives

$$
|\mathcal H|\binom{n-k}{w-k}\ge\binom nw,
\qquad
|\mathcal H|\ge\frac{\binom nk}{\binom wk}.
\tag{3}
$$


### The polynomial bound for one forbidden distance

Suppose $p$ is prime, $4p>n$, and no two distinct members of a $k$-uniform
family $\mathcal A$ have symmetric difference of size $2p$. Then

$$
|\mathcal A|\le\sum_{i=0}^{p-1}\binom ni.
\tag{4}
$$


For each $A\in\mathcal A$, consider the polynomial over $\mathbb F_p$

$$
P_A(x_1,\ldots,x_n)
=1-\left(\sum_{i\in A}x_i-k\right)^{p-1}.
$$

It is one on the incidence vector of $A$. If $A\ne B$ and
$|A\cap B|\equiv k\pmod p$, then

$$
|A\triangle B|=2(k-|A\cap B|)
$$

is a positive multiple of $2p$. Since it is at most $n<4p$, it must equal $2p$,
contrary to the hypothesis. Fermat's theorem therefore gives $P_A(\mathbf1_B)=0$
for every other $B\in\mathcal A$.

Multilinearizing these polynomials preserves their values on binary vectors and
leaves their degree at most $p-1$. The resulting polynomials are linearly
independent by their evaluations on the vectors $\mathbf1_B$. The space of
multilinear polynomials of degree at most $p-1$ has dimension
$\sum_{i=0}^{p-1}\binom ni$, proving (4).

### The uniform entropy gap

Set

$$
\alpha=\frac nk,\qquad u=\frac wk,
\qquad
h(x)=-x\log x-(1-x)\log(1-x),
$$

with the usual continuous endpoint values. The hypotheses imply

$$
\frac74\le\alpha\le\frac{30}{17},
\qquad 1\le u\le\frac{69}{68}.
\tag{5}
$$

The prime number theorem gives $2p=w+o(k)$ for the least prime $p\ge w/2$. Also
$4p\ge2w\ge2k>n$. If distance $2p$ were absent, (3), (4), Stirling's formula,
and the binomial-sum bound would give

$$
\begin{aligned}
\log|\mathcal H|
&\ge k\bigl[\alpha h(1/\alpha)-u h(1/u)\bigr]-O(\log k),\\
\log|\mathcal H|
&\le k\alpha h\!\left(\frac{u}{2\alpha}\right)+o(k).
\end{aligned}
\tag{6}
$$

All errors are uniform in (5).

The main terms have a uniformly positive gap. The monotonicities used in
[Coding refinement](coding_refinement.md) give the lower bound

$$
\alpha h(1/\alpha)-u h(1/u)-\alpha h\!\left(\frac{u}{2\alpha}\right)
\ge
\frac74h(4/7)-\frac{69}{68}h(68/69)-\frac{30}{17}h(23/80).
\tag{7}
$$

For completeness, $h''(x)=-1/[x(1-x)]$ gives

$$
h(4/7)\ge\log2-\frac1{96},
\qquad
h(23/80)\le\log2-\frac{289}{3200}.
$$

Also

$$
\frac{69}{68}h(68/69)
=\log(69/68)+\frac{\log69}{68}
\le\frac{\log69+1}{68}.
$$

Consequently the right side of (7) is greater than

$$
\frac{51}{320}-\frac7{384}-\frac7{68}
=\frac{1247}{32640}>0,
\tag{8}
$$

using $\log2<1$ and $\log69<5$. This contradicts (6) for sufficiently large $k$
and proves the distance lemma.

## A four-set certificate from an empty-intersection triple

**Certificate.** If a family $\mathcal H$ has $P_7$ and
$A_1,A_2,A_3\in\mathcal H$ have empty common intersection, then, for
$U=A_1\cup A_2\cup A_3$,

$$
\tau(\mathcal H)\le\left\lceil\frac{|U|}{2}\right\rceil+1.
\tag{9}
$$


Every two-point transversal of the three references lies entirely in $U$.
Indeed, an outside point meets none of them, and no single point meets all
three. Let $G$ be the graph on $U$ whose edges are these two-point transversals.

The graph $G$ is 3-colorable. Write

$$
P_i=A_j\cap A_\ell,
\qquad
S_i=A_i\setminus(A_j\cup A_\ell),
\qquad \{i,j,\ell\}=[3].
$$

The three sets $P_i$ are disjoint, as are all six displayed atoms. The pair
atoms $P_1,P_2,P_3$ form a complete tripartite graph in $G$. A point of $S_i$ is
adjacent precisely to the points of $P_i$, and there are no edges between
singleton atoms. Give $P_i$ color $i$ and give $S_i$ any color other than $i$.

Let $C_1,C_2,C_3$ be the resulting color classes and split each into two parts
of sizes differing by at most one. Assign the following two labels to those
parts:

$$
C_1:\ \{1,2\},\{3,4\};\qquad
C_2:\ \{1,3\},\{2,4\};\qquad
C_3:\ \{1,4\},\{2,3\}.
$$

For $j\in[4]$, let $T_j$ be the vertices whose assigned label contains $j$.
Labels coming from different color classes always intersect. Thus every edge of
$G$ is contained in at least one $T_j$. Furthermore

$$
|T_j|\le\sum_{i=1}^3\left\lceil\frac{|C_i|}{2}\right\rceil
\le\left\lceil\frac{|U|}{2}\right\rceil+1.
\tag{10}
$$

The last rounding bound follows by counting the odd class sizes: there are at
most three, and their number has the same parity as $|U|$.

If the right side of (9) were smaller than $\tau(\mathcal H)$, choose
$E_j\in\mathcal H$ disjoint from $T_j$ for every $j\in[4]$. By $P_7$, the three
references and these four edges have a two-point transversal. It is an edge of
$G$, hence lies in some $T_j$, and therefore misses $E_j$, a contradiction.
Repeated chosen edges cause no difficulty because the subfamily has at most
seven distinct members.

## The narrow-ground upper bound

**Theorem.** Uniformly over $k$-uniform $P_7$ families with

$$
\frac74k\le n\le\frac{30}{17}k,
$$

one has

$$
\tau(\mathcal H)\le\frac{2k+n}{5}+o(k).
\tag{11}
$$


Put $\tau=\tau(\mathcal H)$. If $\tau-1<3k/4$, the conclusion is immediate,
because $(2k+n)/5\ge3k/4$. Otherwise apply the distance lemma with $t=\tau-1$
and $w=n-t$. Obtain $A,B\in\mathcal H$ with

$$
s=|A\triangle B|\ge w,
\qquad s=w+o(k).
$$

Because every $w$-set contains an edge, there is $C\in\mathcal H$ contained in
$A\triangle B$. Therefore

$$
A\cap B\cap C=\varnothing,
\qquad
A\cup B\cup C=A\cup B,
\qquad
|A\cup B|=k+\frac{s}{2}.
$$

The certificate (9) gives

$$
\tau\le\left\lceil\frac{k+s/2}{2}\right\rceil+1
\le\frac{k}{2}+\frac{s}{4}+2.
$$

Substitute $s=n-\tau+1+o(k)$ and rearrange to obtain (11).

Writing $n=7k/4+\delta$ makes the bound

$$
\tau(\mathcal H)\le\frac34k+\frac{\delta}{5}+o(k).
\tag{12}
$$

Thus a fixed positive excess above $3k/4$ still remains possible in the interval
treated here; the theorem controls that excess in terms of the ground-set
excess. At the endpoint $n=30k/17$, (11) is $\tau\le64k/85+o(k)$, not the
conjectured $3k/4$.

## Nonlinear threefold-XOR families

Define

$$
d_3(\mathcal H)
=\min_{A,B,C\in\mathcal H}|A\triangle B\triangle C|,
$$

allowing repetitions. No affine or linear closure is assumed.

There is an exact forbidden-distance implication. If $t<\tau(\mathcal H)$ and
$w=n-t$, then no two members have distance in

$$
[w,k+d_3(\mathcal H)-1].
\tag{13}
$$

Indeed, if $Z=A\triangle B$ has size $s\ge w$, choose $C\in\mathcal H$ contained
in $Z$. Then

$$
|A\triangle B\triangle C|=|Z\setminus C|=s-k\ge d_3(\mathcal H),
$$

which proves (13).

Equivalently, the distance lemma and the same choice of $C$ give the following
uniform consequence throughout its parameter range:

$$
\boxed{\quad
d_3(\mathcal H)\le n-k-t+o(k).
\quad}
\tag{14}
$$

This strengthens the corresponding affine-coset conclusion in
[Coding refinement](coding_refinement.md): it applies directly to every
constant-weight family. Affinity is not used either in the covering count or in
the polynomial bound.

### The refined sufficient criterion still cannot beat three quarters

The Fano analysis in [Coding refinement](coding_refinement.md) proves the
following statement about an arbitrary bad seven-tuple of $k$-sets on $n<30k/17$
points. Put $D=4n-7k$. There is a Fano plane on the seven row indices such that

$$
\sum_{L\text{ a Fano line}}
\left|\mathop{\triangle}_{i\in L}A_i\right|
\le3D.
$$

In particular one of its threefold symmetric differences has size at most
$3D/7$. Hence the sufficient local-property criterion from that page extends to
arbitrary nonlinear families as

$$
\boxed{\quad
n<\frac{30}{17}k,\qquad
d_3(\mathcal H)>\frac37(4n-7k)
\quad\Longrightarrow\quad P_7.
\quad}
\tag{15}
$$

For $n<7k/4$, the degree argument already excludes a bad seven-tuple, without a
distance condition.

Nevertheless, families satisfying (15) obey

$$
\tau(\mathcal H)\le\frac34k+o(k).
\tag{16}
$$

To prove this, suppose $\tau>(3/4+\varepsilon)k$ along a sequence, with fixed
$\varepsilon>0$. The elementary bound $\tau\le n-k+1$ disposes of $n<7k/4$.
Otherwise take $t=\lfloor(3/4+\varepsilon)k\rfloor$ and write
$\delta=n-7k/4\ge0$. Then (15) gives

$$
d_3>\frac{12\delta}{7},
\qquad
n-k-t=\delta-(t-3k/4),
$$

and consequently

$$
d_3-(n-k-t)
>\frac{5\delta}{7}+(t-3k/4)
\ge\varepsilon k-1.
$$

This contradicts (14), proving (16).

The conclusion excludes only the specified robust threefold-XOR sufficient
condition. It does not exclude nonlinear families that have $P_7$ for other
reasons, and it does not show that every $P_7$ family satisfies that distance
condition.
