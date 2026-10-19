---
name: research/erdos_644/independent/complete_family_limit_and_seven_edge_obstruction
title: Independent investigation of Erdős problem 644
desc: Unverified independent input; checked certificates, a corrected finite example, and stronger existing results are recorded in topical notes.
tags: [unverified, research-input]
sources: []
created: 2026-09-23T07:10:27Z
updated: 2026-10-13T05:28:09Z
---


# Independent investigation of Erdős problem 644

***

## 1. Outcome and scope of this record

**Neither requested assertion was proved or disproved.** No construction with
a positive proportional excess over $3k/4$ was obtained, and no argument
establishing convergence of $f(k,r)/k$ for arbitrary fixed $r$ was found.
This record separates proved
claims, source results, numerical observations, and speculative mechanisms.

Only the supplied problem page and papers were consulted; there was no web
browsing or use of earlier research notes. Results invoked from papers were
checked in their `source.md` files. The relevant source results are:

* Section 16 of the Erdős survey reports the exact coefficients for
  $r=3,4,5,6$: $2,3/2,5/4,1$.
* Theorem 1 of the 1999 Fon-Der-Flaass--Kostochka--Woodall paper gives
  $f(4q,7)\ge3q+1$ for $q\ge10$, using a parity construction.
* Theorem 2 of that paper gives
  $f(k,7)\le\lceil7k/8\rceil$ for every $k\ge8$.
* The complete-family counting lower bound in Section 2 below is also
  Theorem 5.7 of the supplied Bucić--Korándi--Sudakov paper.

Thus the established unrestricted asymptotic bounds remain

$$
\frac34\le\liminf_{k\to\infty}\frac{f(k,7)}k
\le\limsup_{k\to\infty}\frac{f(k,7)}k\le\frac78.
$$


Detailed proofs of restricted results are also retained in
`complete_family_model.md`, `scaling_and_shifting.md`,
`static_avoidance_analysis.md`, `two_profile_analysis.md`, and
`fractional_cover_analysis.md`. These are auxiliary records, not purported
solutions to the original problem.

## 2. Conventions, compactness, and elementary bounds

Write $P_r$ for the property that every subfamily with **at most** $r$
members has a transversal of size at most two. For a family having at least
$r$ members, this is equivalent to testing exactly $r$: extend a
smaller offending family. A family with fewer members has transversal number
at most $r-1$, so the convention makes no asymptotic difference.

Finite families suffice for proving a fixed transversal bound. Indeed, if
a family of nonempty finite sets has no $t$-point transversal, it has a
finite subfamily with the same property. Induct on $t$. The case $t=0$
is immediate. Choose an edge $E$. For each $v\in E$, the family of
edges avoiding $v$ has no $(t-1)$-point transversal; otherwise adding
$v$ would cover the whole family. Choose a finite witness
$\mathcal G_v$ by induction. Then
$\{E\}\cup\bigcup_{v\in E}\mathcal G_v$ is the required finite witness.

### Complete-family lower bound for seven

Put $n=\lfloor(7k-1)/4\rfloor$ and take all $k$-subsets of $[n]$.
Among seven edges, total incidence is $7k>4n$, so a point lies in at
least five. The remaining at most two edges intersect since $n<2k$.
Consequently the complete family satisfies $P_7$, while its transversal
number is

$$
n-k+1=\left\lceil\frac{3k}{4}\right\rceil.
$$

This proves the $3/4$ lower coefficient at every sufficiently large
uniformity, not only along multiples of four.

The supplied parity construction has

$$
|S|=7q+1,\quad |X|=4q,\quad
\mathcal B=\{B\in\tbinom S{4q}:|B\cap X|\text{ odd}\},
\quad\tau(\mathcal B)=3q+1.
$$

Its ratio is $3/4+1/(4q)$, which tends to $3/4$. The additive one
therefore does **not** disprove the asymptotic assertion.

### General linear order

The elementary upper bound is $f(k,r)\le\max(2k,r-1)$. Under $P_r$,
three disjoint edges are impossible, and the union of a maximal matching
of at most two edges is a transversal.

For the lower bound take all $k$-sets of a $(k+t)$-set. Each edge
misses $\binom t2$ pairs. Thus this family has $P_r$ whenever

$$
r\binom t2<\binom{k+t}2.
$$

Its transversal number is $t+1$. Taking $t\sim ck$, for any
$c<1/(\sqrt r-1)$, gives

$$
\frac1{\sqrt r-1}\le\liminf\frac{f(k,r)}k
\le\limsup\frac{f(k,r)}k\le2.
$$

This proves $\Theta_r(k)$, not the existence of a limit.

## 3. Two reformulations

### Complement covering formulation

On a finite ground set $V$, set
$\mathcal B=\{V\setminus E:E\in\mathcal H\}$. Then:

* $\tau(\mathcal H)>t$ means that every $t$-subset of $V$ is
  contained in some member of $\mathcal B$.
* $P_r$ means that no at most $r$ members of $\mathcal B$ cover
  all pairs of $V$ by containment.

Thus one seeks high-strength covering families for which the corresponding
cliques cannot cover the complete graph using $r$ members. This is an
exact reformulation, but no suitable scaling theorem for these covering
families was established.

### Incidence spectra

For labeled edges $E_1,\ldots,E_m$, the spectrum of a point is
$S(v)=\{i:v\in E_i\}\subseteq[m]$. The edges have no two-point
transversal precisely when

$$
S(v)\cup S(w)\ne[m]\quad\text{for every pair of points,}
$$

also excluding a single spectrum equal to $[m]$. Equivalently their
complement spectra form a pairwise-intersecting family.

For fixed $r$, there are only finitely many possible spectrum supports
on at most $r$ rows. This gives the complete-family result below. It
does **not** by itself give a finite description or dilation of arbitrary
families with large transversal number.

## 4. A proved limit theorem for complete families only

Let $g_r(k)$ be the minimum union size of a family of at most $r$
distinct $k$-sets with transversal number greater than two. Then the
complete $k$-uniform family on $n$ points has $P_r$ exactly when
$n<g_r(k)$. Its largest possible transversal number is therefore
$g_r(k)-k$.

For $3\le m\le r$, consider a support
$\mathcal Q\subseteq2^{[m]}\setminus\{\varnothing\}$ satisfying
$S\cup T\ne[m]$ for all $S,T\in\mathcal Q$. For every feasible
such support solve

$$
\min\sum_{S\in\mathcal Q}w_S,
\qquad
\sum_{S\ni i}w_S=1\ (i\in[m]),\qquad w_S\ge0.
$$

Let $d_r$ be the minimum over these finitely many rational linear
programs. Then

$$
\boxed{g_r(k)=d_rk+O_r(1).}
$$


For the lower bound, divide every spectrum-class size of a bad family by
$k$. For the upper bound, take an optimal solution, create
$\lfloor kw_S\rfloor$ points of each spectrum, and privately pad each
row to size $k$. Only $O_r(1)$ points are needed. Padding cannot
introduce a two-cover: an admissible support cannot contain
$[m]\setminus\{i\}$, because the row equation for $i$ supplies
another spectrum containing $i$. Hence adjoining singleton spectra
preserves the condition. Duplicate rows may be erased without changing
the transversal number. This proves the formula and rationality of the
complete-family coefficient $d_r-1$.

For $r=7$, $d_7=7/4$. To see the lower bound, suppose a bad family
has $m\le7$ edges on $n<2k$ points. All pairs of edges intersect,
so no point belongs to $m-2$ or more edges: that point and one point
in the remaining at most two edges would cover the family. Thus
$mk\le(m-3)n$, giving $n\ge7k/4$. The case $m=3$ is impossible
when $n<2k$. For the upper bound, the seven complements of the Fano
lines are four-sets on seven points with no two-cover; blowing up their
points gives union size $7k/4$ when $4\mid k$.

**Unresolved passage:** no reduction from arbitrary extremal families to
complete families was proved. In particular the finite LP does not prove
the second assertion in the problem.

## 5. Fractional transversal calculations

For every finite rank-$k$ hypergraph,

$$
\tau(\mathcal H)
\le\lfloor k(\tau^*(\mathcal H)-1)\rfloor+1.
$$

Let a fractional cover have total weight $\alpha$, and select the
$s=\lfloor k(\alpha-1)\rfloor+1$ largest-weight vertices. If an edge
misses them, its at most $k$ weights have sum at least one, so its
largest weight is at least $1/k$. Every selected weight is at least
that large. Total weight is therefore at least $s/k+1>\alpha$, a
contradiction. If fewer than $s$ vertices exist, select all vertices.

A second proved bound uses the local property. Put $s=\lceil r/2\rceil$.
Then

$$
\boxed{\tau^*(\mathcal H)
\le\bigl(\tbinom rs k\bigr)^{1/(s-1)}.}
$$

Normalize an optimal fractional matching of total weight $W=\tau^*$
to a probability distribution on edges. Its vertex incidence probabilities
satisfy $p_v\le1/W$ and $\sum_vp_v=k$. Sample $r$ edges independently.
Their distinct members have a two-cover, so some point lies in at least
$s$ sampled edges. A union bound gives

$$
1\le\binom rs\sum_vp_v^s
\le\binom rs kW^{-(s-1)}.
$$


The exponent is attained in order by hyperplanes of projective space
$\mathrm{PG}(s,q)$. Any $s$ hyperplanes meet, so any at most $r$
can be split into two intersecting groups. Here

$$
k=(q^s-1)/(q-1),\qquad
\tau^*=(q^{s+1}-1)/(q^s-1)\asymp q.
$$

A projective line is a transversal; rounding the fractional lower bound
shows $\tau=q+1$. These examples have sublinear $\tau$ when $r\ge5$.

A bound $\tau^*\le7/4+o(1)$ would suffice for the desired upper bound,
but it is false for all $P_7$ families. Even two disjoint edges have
$\tau^*=2$, and the projective examples have unbounded $\tau^*$.
A useful version would require an additional structural hypothesis or a
decomposition distinguishing linear-transversal families. None was proved.

## 6. Scaling attempts and a concrete shifting failure

### Cloning: exact formula, but the verified local condition loses ratio

Replace each original vertex by $N$ clones. For each original edge,
include all unions of $s$-subsets of its clone classes. The new family
has uniformity $ks$ and

$$
\tau'=(N-s+1)\tau.
$$

For a candidate transversal $T$, let $Q$ consist of original vertices
whose classes contain at least $N-s+1$ points of $T$. Then $T$
covers the expanded family if and only if $Q$ covers the original one.

A sufficient condition preserving $P_r$ is $r(N-s)<N$: at most
$r$ chosen $s$-subsets in a single class have a common clone. But
with $q=N-s$, the multiplier of the transversal-to-rank ratio is
$(q+1)/(N-q)$, whose limsup under this condition is at most
$1/(r-1)$. Full-class cloning leaves $\tau$ unchanged.
This is a limitation of this verified criterion, not a proof that every
possible cloning scheme fails.

The Cartesian union product of families on disjoint ground sets has
uniformity $\sum k_i$ but transversal number $\min_i\tau_i$: a
transversal in one coordinate suffices; if none of the coordinate portions
is a transversal, choose a missed edge in each coordinate. It preserves
$P_r$ if one factor has it, but does not add transversal numbers.

Tuza's supplied ISP composition makes set-pair parameters additive, but
does not make the associated edge family's transversal number additive.
Construction 15 repairs the transversal number by adjoining complements
of small transversals. Those new edges can be much larger, and preservation
of $P_r$ was not established. This is not a Fekete argument for the
second assertion.

### Ordinary shifting does not preserve $P_7$

Use $abc$ for $\{a,b,c\}$. The family

$$
\mathcal H=\{015,024,025,034,123,125,134,234\}
$$

has $P_7$. On deleting the listed edges in order, respective two-covers
are

$$
23,\ 35,\ 14,\ 12,\ 45,\ 03,\ 02,\ 01.
$$

The $0\leftarrow1$ shift replaces only $123$ by $023$. The shifted
family contains

$$
\{015,023,024,034,125,134,234\},
$$

whose complements are

$$
234,145,135,125,034,025,015.
$$

Their pair-shadows cover all fifteen pairs, so these seven edges have no
two-cover. Padding extends this failure to every $k\ge3$: share padding
within $025,125$ and within $034,134$, and use separate padding
elsewhere. In the bad seven, a padding point hits at most two edges and
an original point at most four, so pairs involving padding also fail.

These examples only refute preservation under shifting. Their transversal
numbers stay bounded and do not refute the asymptotic assertion.

## 7. A seven-edge obstruction method and its limitation

Call $A_1,A_2,A_3$ a good triple when their common intersection is empty.
Put

$$
X_i=A_j\cap A_\ell,\qquad
P_i=A_i\setminus(A_j\cup A_\ell),\qquad
\{i,j,\ell\}=\{1,2,3\}.
$$

Write $x_i=|X_i|$, $s=x_1+x_2+x_3$; then
$|P_i|=k-s+x_i$. The graph of pairs covering the triple is exactly

$$
G=K_{X_1,X_2,X_3}\ \cup\ \bigcup_i K_{X_i,P_i}.
$$

If its edges are covered by four vertex subsets $B_1,\ldots,B_4$,
each of size at most $t<\tau(\mathcal H)$, choose an original edge
avoiding each $B_i$. Together with the triple they form at most seven
edges with no two-cover.

### A small-union triple is sufficient

Let $m=|A_1\cup A_2\cup A_3|$. Assign each vertex to one set it
misses, giving a proper three-coloring of $G$. Split each color class
into halves and assign the halves membership types

$$
12\mid34,\qquad13\mid24,\qquad14\mid23
$$

in four avoidance subsets. Types from different color classes intersect,
so every candidate pair lies in one subset. Each subset has size at most
$\lceil m/2\rceil+1$. Hence

$$
\tau(\mathcal H)\le\left\lceil\frac m2\right\rceil+1
\quad\text{under }P_7.
$$

A good triple of union size $(3/2+o(1))k$ would therefore prove the
target bound. No theorem forcing such a triple was obtained.

Another explicit sufficient condition for four subsets of size $t$ is

$$
x_i\le t,
\qquad
s+\sum_i\max(0,k-t-s+2x_i)\le t.
$$

Take one subset containing all three core classes plus the overflow of
each private class, and three subsets containing $X_i$ plus the portion
of $P_i$ fitting alongside it. This works at $t=3k/4$ for symmetric
triples $x_i=ak$ with $a\le1/4$.

### An actual obstruction to four static avoidance sets

If $x_i=ak$, $|P_i|=(1-2a)k$, and $1/4<a<1/2$, four subsets
of size $3k/4$ cannot cover all edges of $G$.

A core point belonging to just one subset forces all its neighbors into
that subset; its neighborhood has size $k$. Thus every core point
has at least two memberships, and every private point at least one.
These use at least
$6ak+3(1-2a)k=3k$ memberships, exhausting all four capacities.
Hence each core point has exactly two memberships and each private point
exactly one. The two-element type families of the three core groups are
cross-intersecting. Each has a common index, forced by its private class.
Three such families on four indices either have a global common index or
all lie in a triangle of three indices. In the first case one subset
contains all core points, of size $3ak>3k/4$. In the second, only three
subsets must accommodate all $3k$ memberships, exceeding their total
capacity $9k/4$. Both are impossible. The elementary type classification
is proved in `static_avoidance_analysis.md`.

For comparison, splitting each core class into portions of sizes
$(1+a)k/5$ and $(4a-1)k/5$ gives a four-subset construction of
maximum size $3(1+a)k/5+O(1)$. A complementary-pair construction gives
$3(1-a)k/2+O(1)$. Their minimum is at most $6k/7+O(1)$ over the
symmetric intermediate range. These are restricted triple calculations,
not universal bounds on $f$.

A mixed-integer search reported restricted optima $33/40,5/6,7/8$ for
core triples $(3/8,3/8,3/8)$, $(1/4,3/8,3/8)$, and
$(1/4,1/2,1/2)$, with $k=1$ as normalization. No exact lower-bound
certificates were extracted; these reported optimality values are not used
as proofs.

## 8. A restricted lower-construction class that can be excluded

A proved restricted theorem is recorded in `two_profile_analysis.md`:

> Partition the ground set into two groups, and include every $K$-set
> with either of two specified group-count profiles. If the resulting
> family has $P_7$, its transversal number is at most
> $(3/4+o(1))K$, uniformly over the parameters.

This does not treat three or more profiles or arbitrary families.

Normalize the group sizes to $u,v$, the profiles to
$(a,1-a),(b,1-b)$, with $a<b$, and set $g=b-a$, $n=u+v$.
When both profiles have positive counts in both groups, the exact finite
formula is

$$
\tau=\min\{U-A+1,\ V-K+B+1,\ U+V-K-(B-A)+2\}.
$$

Thus a limiting ratio $t$ satisfies
$t\le\min(u-a,v-1+b,n-1-g)$. If $A=0$, the first term must be
omitted; if $B=K$, omit the second. These endpoint corrections were
essential. An earlier draft had them wrong and is explicitly superseded.

The proof uses the following concrete seven-row obstructions, with strict
budget inequalities so that integer rounding is valid.

1. Seven identical profiles are bad if
   $a<4u/7$ and $1-a<4v/7$, by the Fano spectra and incidence deletion.
2. Three rows of profile $a$ on a Fano line and four of profile $b$
   are bad if

   $$
   1-2v/3<a<2u/3,\qquad 7-4v<3a+4b<4u.
   $$

   The roles of $a,b$ can be interchanged.
3. Six rows of one profile and one of the other are bad if

$$
   (6/5)a+b<u,\qquad(6/5)(1-a)+(1-b)<v.
$$

   Use the singleton last row and the six five-subsets of the first six
   rows as spectra.
4. The pair-union-free spectra

$$
   123,\ 4,\ 1456,\ 2457,\ 3467,\ 567
$$

   realize three rows of count $x$ and four of count $y$ using
   $\max(x+y,2y-2x)$ points. Give the three four-spectra weight
   $z=\min(x,y/3)$, and the other three weights
   $x-z,y-3z,y-2z$. Thus a bad family exists when

   $$
   2-v<a+b<u,\qquad 2g<\max(u,v).
   $$


Here is the main algebra in the interior case. If $t>3/4$, normalized
group sizes may be bounded by $7/4$; otherwise an identical-profile
Fano construction either exists or gives a transversal bound already at
most $3K/4+O(1)$. Avoiding the Fano tests then forces

$$
a\le1-2v/3,\qquad u\le3b/2.
$$

The sum $a+b$ must lie strictly between $2-v$ and $u$; otherwise
the transversal bounds and these inequalities contradict $t>3/4$.
Test 4 consequently gives $u,v\le2g$.

Put $S_1=(6/5)a+b$, $S_2=a+(6/5)b$. Neither lies in
$(11/5-v,u)$. If both are below this interval, the inequalities give
simultaneously $b<9/14$ and $b>7/10$. Both above is symmetric.
If they straddle the interval, then
$n\le11/5+g/5$ and $n\le4g$, whereas $n-g>7/4$. These force
$g<9/16$ and $g>7/12$, a contradiction.

For the endpoint $a=0$, an additional obstruction takes four low-profile
edges with empty common second-group intersection and three high-profile
edges with pairwise-disjoint second-group parts. Its inequalities are
$v>4/3$ and $1-b<v/3$. Together with the six-plus-one test it excludes
the endpoint case; the other endpoint is symmetric. Both endpoints give
disjoint complete families and an even smaller upper coefficient.

Rounding is justified by using only strict limiting budget inequalities:
floor the finitely many spectrum-class masses and repair each row with
private singleton spectra, costing $O(1)$ points. The full note uses
non-strict inequalities when excluding these open obstruction regions,
so boundary cases are not silently assumed to have slack.

One discarded numerical candidate illustrates why local checks matter:
$K=120$, group sizes $104,179$, and profiles $(0,120),(70,50)$
have transversal number $93>90$. Nevertheless they fail $P_7$: choose
four low edges with empty intersection in the second group and three high
edges with disjoint 50-point second-group portions. Two first-group points
miss the low edges; a mixed pair cannot hit all four low edges; two
second-group points cannot hit the three disjoint high portions.

## 9. Parity/code amplification: explored but not established

The 1999 construction exploits a bounded incidence deficit. If seven
$k$-sets on $n<2k$ points have no two-cover, every point has degree
at most four, so the total deficit is

$$
D=4n-7k.
$$

At $n=7k/4+1$, this is only four. The source classifies the standard
degree-four spectra into the Fano pattern and uses parity to contradict
the possible exceptional vertices. That argument is specific to its
small deficit; no general linear-slack stability theorem was established.

An attempted scalable replacement was to require edge indicator vectors
to lie in a nonzero affine binary-code coset, with minimum coset weight
$d$ linear in $k$. In a Fano-like configuration, XORs of suitable
triples of rows are supported on exceptional vertices, so a large coset
distance could exclude such configurations. However, one must also prove
that every sufficiently large residual vertex set contains an allowed
weight-$k$ edge. That second requirement was never obtained with a
favorable loss.

The rough random-code comparison was unfavorable: obtaining coset distance
$d$ typically uses redundancy of order $d\log(n/d)$, while finding
an allowed edge in every $(k+s)$-set has only
$\log\binom{k+s}{s}\approx s\log(k/s)$ of combinatorial choice. This
suggests deletion slack $s$ comparable to $d$, not smaller than the
available ground-set gain. These are exploratory entropy comparisons,
not an impossibility theorem for codes or arbitrary constructions.

Imposing independent parity conditions on many small blocks has a direct
problem: if every edge must meet each block, an entire smallest block is
a global transversal. Ordinary clone blowups, the product operations in
Section 6, and this blockwise parity idea therefore do not amplify the
source's additive one into a positive asymptotic excess.

Other unproved ideas were a linear-size structural core for high-transversal
$P_r$ families, a continuous incidence-limit model, and a dichotomy
separating dense extremizers from projective-type sublinear examples. The
supplied critical-hypergraph bounds only give much larger cores; no
appropriate stronger kernel theorem or discretization theorem was proved.

## 10. Precise remaining uncertainties

1. There is no proof that arbitrary $P_7$ families have
   $\tau\le(3/4+o(1))k$, nor a construction proving an asymptotic excess.
2. The small-union good-triple criterion is sufficient, but no theorem
   forces such a triple in a hypothetical counterexample. The static
   four-subset obstruction shows why an arbitrary good triple is not
   enough for that particular argument.
3. The finite LP proves convergence for complete families only. No
   ratio-preserving amplification, subadditivity/superadditivity theorem,
   or general realization theorem transfers it to $f(k,r)$.
4. The two-profile result excludes only a narrow exchangeable construction
   class. Passing to two profiles from a larger profile family can lower
   its transversal number, so it is not a reduction of the general problem.
5. The code route lacks both a sufficiently general Fano stability theorem
   and a simultaneous local-condition/global-covering construction with
   favorable quantitative parameters.

The finite parity improvement and all restricted obstructions in this
record must not be presented as answers to the original two assertions.
