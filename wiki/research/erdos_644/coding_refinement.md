---
name: research/erdos_644/coding_refinement
desc: A refined Fano-based affine-code criterion and a forbidden-weight polynomial obstruction to improving the three-quarter coefficient by that criterion.
tags: [proved, methods, obstruction]
sources: [fon_der_flaass_et_al_1999_transversals_uniform_hypergraphs_property_7_2]
created: 2026-09-22T21:36:22Z
updated: 2026-10-14T00:26:52Z
---


# research/erdos_644/coding_refinement

***

This page proves a stronger sufficient affine-code criterion for the local
seven-edge property than the sevenfold-XOR criterion in
[Certificates and obstructions](certificates_and_obstructions.md). It also
proves that the stronger criterion still cannot give an asymptotic
counterexample in its stated range.

[Fano classification extension](fano_classification_extension.md)
extends the classification and sufficient threefold-XOR criterion to
$n<9k/5$, using Füredi's fractional matching theorem. The polynomial
obstruction below retains its own narrower entropy hypotheses.

**Scope.** These are obstructions to particular sufficient conditions. They do
not prove the conjectured upper bound for arbitrary affine-code families
satisfying the local property, or for arbitrary set families. No counterexample
to Problem 644 is obtained.

**Comparison with the independent input.** Sections 7.2–7.5 of
[first independent record](independent/fano_ground_set_and_coding_constructions.md)
have been checked. Its sevenfold-XOR lemma is valid, but the exact obstruction
in [Certificates and obstructions](certificates_and_obstructions.md) already
forces $\tau\le\lceil3k/4\rceil$ under that criterion, even for specially
structured codes; the independent random-code entropy diagnostic is therefore
weaker. Its conditional Fano-line XOR estimate is also correct. The missing
classification is supplied below for $D=4n-7k<k/17$, and the later polynomial
argument excludes an asymptotic improvement by the refined distance criterion
throughout that range. Neither conclusion extends to arbitrary coding criteria
or asserts that the classification holds for larger deficiency.

The same comparison applies to the checked §§6.3–6.4 of
[second independent record](independent/fractional_reductions_and_good_triples.md).
Its condition that the linear code contain a word of weight exactly $k+d-1$ is
sufficient for the stated covering loss, but existence of that particular word
is not needed by the forbidden-interval argument below. The later
[nonlinear forbidden-distance theorem](forbidden_distances.md) removes affine
closure from this obstruction as well. The record's robust-classification gap is
therefore filled only in the displayed narrow-deficiency range, while its weaker
sevenfold-XOR route is excluded outright.

## Exact Fano structure sufficiently close to the threshold

**Comparison with the third record.** Its §9 correctly leaves the code
construction unproved, but the present notes have progressed beyond
its small-deficiency discussion. The checked
[fractional-matching argument](fano_classification_extension.md)
classifies all degree-four spectra whenever $n<9k/5$, equivalently
$D=4n-7k<k/5$. The threefold-XOR bound then holds throughout that
range. This does **not** extend the separate polynomial/entropy
obstruction below beyond its stated $n\le30k/17$ range. The
[nonlinear forbidden-distance argument](forbidden_distances.md)
already rules out that sufficient distance criterion in the latter
range, more strongly than the input's heuristic random-code entropy
comparison. [Distinct-seven XOR](distinct_seven_xor.md) separately
excludes a total-XOR avoidance criterion for $7k/4\le n<2k$.
None rules out every code-defined family satisfying $P_7$.

Let $A_1,\ldots,A_7$ be $k$-subsets of an $n$-point set, with no two-point
transversal. Suppose

$$
n<\frac{30}{17}k.
\tag{1}
$$

The degree of a point is its number of containing sets, and its spectrum is the
corresponding subset of $[7]$. Every degree is at most four: a point of degree
at least five, together with a point in the intersection of the at most two
remaining sets, would be a transversal. Here $n<2k$ guarantees that any two sets
intersect.

Put

$$
D=4n-7k=\sum_v(4-\deg v).
$$

In particular $D\ge0$. Call the degree-four points standard and let $N$ be the
other points. Then

$$
|N|\le D,\qquad D<k/17.
\tag{2}
$$


We prove that the spectra of the standard points are exactly the seven
complements of the lines of a Fano plane on $[7]$, with every one of these
spectra occurring. This adapts the good-pair argument in Claims 2–5 of Section 2
of the supplied 1999 paper; all estimates needed here are proved below.

Write $a_{ij}=|A_i\cap A_j|$ and $m=\max_{i\ne j}a_{ij}$. For every $i$,

$$
\sum_{j\ne i}a_{ij}
=\sum_{v\in A_i}(\deg v-1)
\ge 3k-D.
\tag{3}
$$

Hence $m\ge k/2-D/6$. Choose a maximum pair, say $a_{12}=m$. The number of
points outside its union is at least

$$
n-2k+m\ge k/4+D/12>D,
$$

so there is a standard point outside $A_1\cup A_2$. Its missing spectrum has the
form $\{1,2,r\}$. Necessarily

$$
A_r\cap A_1\cap A_2=\varnothing,
\tag{4}
$$

because a point of this triple intersection would complete a two-point
transversal.

If another standard point outside $A_1\cup A_2$ had missing triple $\{1,2,s\}$,
$s\ne r$, then both $A_r$ and $A_s$ would avoid $A_1\cap A_2$. Consequently

$$
|A_r\cap A_s|\ge2k-n+m>m,
$$

a contradiction. Thus all standard points outside the union miss $A_r$. Together
with (4), this gives

$$
A_r\subseteq(A_1\triangle A_2)\cup N,
$$

and therefore

$$
m\le\frac{k+D}{2}.
\tag{5}
$$

Using (3) and (5), every pair satisfies

$$
a_{ij}\ge3k-D-5m\ge\frac{k}{2}-\frac{7D}{2}.
\tag{6}
$$


For any pair $i,j$, its outside region consequently has size at least

$$
n-2k+a_{ij}\ge\frac{k}{4}-\frac{13D}{4}>D.
$$

It contains a standard point. If two standard points there had different missing
triples $\{i,j,r\}$ and $\{i,j,s\}$, then the same argument as (4) would give

$$
|A_r\cap A_s|
\ge2k-n+a_{ij}
\ge\frac{3k}{4}-\frac{15D}{4}
>\frac{k+D}{2}\ge m,
$$

where the strict inequality is exactly $17D<k$.

It follows that every pair of indices is in exactly one missing triple of a
standard point. These triples form a Steiner triple system on seven points,
hence the Fano plane. In particular all its seven lines occur as missing
triples, as claimed.

## A threefold-XOR criterion

Continue with the preceding bad seven-tuple, and let $\mathcal L$ be its Fano
plane on the row indices. A degree-three spectrum cannot be a line
$L\in\mathcal L$: the complementary cap occurs as the spectrum of a standard
point, and these two points would cover all seven rows.

For each line $L$, define

$$
X_L=\mathop{\triangle}_{i\in L}A_i.
$$

For a point of degree $r$, the number of $X_L$ containing it is the number of
Fano lines meeting its spectrum oddly. The possibilities are

| Spectrum | Degree | Number of odd line intersections |
|---|---:|---:|
| Empty | 0 | 0 |
| Singleton | 1 | 3 |
| Pair | 2 | 4 |
| Nonline triple | 3 | 3 |
| Fano cap | 4 | 0 |

The table follows from the facts that each Fano point is on three lines and each
pair determines one line. For a nonline triple, its three pair-lines are
distinct; they have even intersection, while three other lines have singleton
intersection. The excluded line triple is the only additional degree-three
possibility.

In every row of the table, the last entry is at most $3(4-r)$. Therefore

$$
\sum_{L\in\mathcal L}|X_L|\le3D,
\qquad
\min_{L\in\mathcal L}|X_L|\le\frac{3D}{7}.
\tag{7}
$$


Now let $C=c+L\subseteq\mathbb F_2^n$ be an affine subspace, and let

$$
d=\min_{a\in C}|a|.
$$

If a $k$-uniform family $\mathcal H$ has all its incidence vectors in $C$, then
the XOR of any three members also belongs to $C$. Thus (7) proves the following
sufficient condition:

$$
\boxed{\quad n<\frac{30}{17}k,\qquad
d>\frac37(4n-7k)
\quad\Longrightarrow\quad
\mathcal H\text{ has the local seven-edge two-point property.}\quad}
\tag{8}
$$

If $n<7k/4$, the local property already follows from the degree argument,
without any condition on $C$.

## Large transversal number forces a forbidden weight interval

The next observations require no local two-point property. Suppose
$\mathcal H\subseteq C=c+L$ is $k$-uniform and $\tau(\mathcal H)>t$, with $t$ an
integer. Set

$$
w=n-t,\qquad j=w-k.
$$

Every $w$-point set contains an edge, so $j\ge0$. More generally, every set of
at least $w$ points contains an edge.

If $z\in L$ has weight $s\ge w$, choose $a\in\mathcal H$ supported inside the
support of $z$. Then $z+a\in C$ and $|z+a|=s-k\ge d$. Hence

$$
\boxed{L\text{ has no word with weight in }[w,k+d-1].}
\tag{9}
$$

Also, counting the $w$-sets containing each edge gives

$$
|L|=|C|\ge|\mathcal H|
\ge\frac{\binom nw}{\binom{n-k}{w-k}}
=\frac{\binom nk}{\binom wk}.
\tag{10}
$$


## Polynomial bound for one forbidden weight

Suppose a binary linear space $L\subseteq\mathbb F_2^n$ has no word of weight
$2p$, where $p$ is prime and $4p>n$. Then

$$
|L|\le(n+1)\sum_{i=0}^{p-1}\binom ni.
\tag{11}
$$


Here is a self-contained polynomial proof. Fix a weight layer

$$
\mathcal F_s=\{\operatorname{supp}(x):x\in L,\ |x|=s\}.
$$

For distinct $A,B\in\mathcal F_s$, one cannot have $|A\cap B|\equiv s\pmod p$.
Otherwise $|A\triangle B|$ would be a positive multiple of $2p$, and $4p>n$
would force it to equal $2p$, contrary to the hypothesis.

Over $\mathbb F_p$, associate to each $A\in\mathcal F_s$ the polynomial

$$
P_A(x_1,\ldots,x_n)
=1-\left(\sum_{i\in A}x_i-s\right)^{p-1}.
$$

On incidence vectors of $\mathcal F_s$, this polynomial is one at $A$ and zero
at every other member. Multilinearizing does not change its values on binary
vectors and leaves degree at most $p-1$. These polynomials are linearly
independent, so

$$
|\mathcal F_s|\le\sum_{i=0}^{p-1}\binom ni.
$$

Summing over the $n+1$ layers proves (11).

## An asymptotic obstruction valid throughout the range of (8)

Let $k\to\infty$. Uniformly over affine spaces and $k$-uniform families as
above, if

$$
\frac74k\le n\le\frac{30}{17}k,
\qquad t\ge\frac34k,
\qquad\tau(\mathcal H)>t,
$$

then

$$
\boxed{d\le n-k-t+o(k)=j+o(k).}
\tag{12}
$$


To prove this, suppose along a sequence that $d\ge j+\varepsilon k$ for a fixed
$\varepsilon>0$. By (9), $L$ forbids every weight from $w$ to $k+d-1$. The prime
number theorem supplies a prime

$$
p=w/2+o(k),\qquad 2p\ge w,
$$

with $2p\le k+d-1$ for large $k$. Thus weight $2p$ is forbidden. Also
$w\ge k>n/2$, so $4p>n$.

Write

$$
\alpha=n/k,\qquad c=t/k,\qquad u=w/k=\alpha-c,
$$

and use natural-log entropy

$$
h(x)=-x\log x-(1-x)\log(1-x).
$$

Here

$$
7/4\le\alpha\le30/17,\qquad 1\le u\le69/68.
$$

By (10), Stirling's formula gives

$$
\log|L|\ge k\left[\alpha h(1/\alpha)-u h(1/u)\right]-O(\log k).
\tag{13}
$$

By (11) and the usual binomial-sum entropy bound,

$$
\log|L|\le k\alpha h\!\left(\frac{u}{2\alpha}\right)+o(k).
\tag{14}
$$


There is a uniform positive gap between the main terms of (13) and (14). Indeed,
$\alpha h(1/\alpha)$ is increasing in $\alpha>1$, $u h(1/u)$ is increasing in
$u\ge1$, and $\alpha h(u/(2\alpha))$ is increasing separately in $\alpha,u$ when
$0<u<\alpha$. Consequently the gap is at least

$$
\frac74h(4/7)
-\frac{69}{68}h(68/69)
-\frac{30}{17}h(23/80).
\tag{15}
$$

For completeness, this is strictly positive without relying on a numerical
calculation. Since $h''(x)=-1/[x(1-x)]$,

$$
h(4/7)\ge\log2-1/96,
\qquad h(23/80)\le\log2-289/3200.
$$

The first follows by bounding $h''\ge-49/12$ on $[1/2,4/7]$; the second follows
from $h''\le-4$. Furthermore,

$$
\frac{69}{68}h(68/69)
=\log(69/68)+\frac{\log69}{68}
\le\frac{\log69+1}{68}.
$$

Thus (15) is at least

$$
\frac{51}{320}-\frac7{384}
-\frac{\log2+\log69+1}{68}
>\frac{51}{320}-\frac7{384}-\frac7{68}>0,
$$

using $\log2<1$ and $\log69<5$. This contradicts (13)–(14) and proves (12).

Finally, suppose a sequence of families satisfies the sufficient criterion (8),
but has $\tau(\mathcal H)>(3/4+\varepsilon)k$ for some fixed $\varepsilon>0$. If
$n<7k/4$, the universal bound $\tau\le n-k+1$ already gives a contradiction for
large $k$. Otherwise take

$$
t=\lfloor(3/4+\varepsilon)k\rfloor,
\qquad\delta=n-7k/4\ge0.
$$

Then $j=\delta-(t-3k/4)$, while (8) gives $d>12\delta/7$. Hence

$$
d-j>\frac57\delta+(t-3k/4)\ge\varepsilon k-1,
$$

contradicting (12). Therefore the stronger sufficient criterion also forces

$$
\tau(\mathcal H)\le\frac34k+o(k).
$$


This conclusion concerns the distance criterion (8), not arbitrary affine
families with the local property. A construction using more information than the
minimum weight of an affine coset remains outside the argument.
