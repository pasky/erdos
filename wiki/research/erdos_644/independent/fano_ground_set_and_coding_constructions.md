---
name: research/erdos_644/independent/fano_ground_set_and_coding_constructions
title: Independent notes on Erdős Problem 644
desc: Unverified independent input; selected claims were checked, corrected, or superseded in the topical research notes.
tags: [unverified, research-input]
sources: []
created: 2026-09-22T23:43:04Z
updated: 2026-10-13T05:28:09Z
---


# Independent notes on Erdős Problem 644

***

## 1. Status and scope

Neither requested assertion was resolved in this investigation. There is no
proved upper bound $(3/4+o(1))k$ for $f(k,7)$ here, no construction with
$\limsup f(k,7)/k>3/4$, and no proof of convergence of $f(k,r)/k$ for every
fixed $r$.

These notes record the concrete deductions, attempted mechanisms, and
obstructions obtained during the investigation. Results proved below are
distinguished from results taken from supplied papers and from heuristic
calculations. Only the supplied problem page and papers were consulted; there
was no browsing and no use of earlier research notes. No computational search
certified a missing classification or construction.

This is the corrected, expanded independent record of the work.

Throughout, $k$ denotes uniformity, $r$ the number of locally tested edges, and
$\tau(\mathcal H)$ the ordinary transversal number. Write $P_r$ for the local
two-point condition.

### The “exactly $r$” convention

If $|\mathcal H|\ge r$, the hypothesis for exactly $r$ distinct edges implies it
for every subfamily with at most $r$ edges, by extending the subfamily. If
$|\mathcal H|<r$, the stated hypothesis is vacuous, but
$\tau(\mathcal H)\le r-1$. Consequently these small families affect some small
numerical values, not the fixed-$r$ asymptotics. Applications of a witness
involving at most seven edges below use this extension convention, or explicitly
assume at least seven edges.

## 2. Supplied results actually checked

The relevant passages were checked in the full Markdown papers, not used solely
from their digests.

* [Erdős, 1997, §16](../../../../library/ramsey_theory/erdos_1997_some_recent_problems_results_graph_theory/_index.md)
  reports

  $$
  f(k,3,2)=2k,\quad f(k,4,2)=\lfloor3k/2\rfloor,\quad
  f(k,5,2)=\lfloor5k/4\rfloor,\quad f(k,6,2)=k.
  $$

  The original proofs are not supplied in this survey. The next two assertions
  in that passage are expectations, not theorems. Its reported formulas should
  not be used to ignore the vacuous-small-family convention above. Their
  asymptotic coefficients for $3\le r\le6$ are unaffected.

* [Fon-Der-Flaass–Kostochka–Woodall, 1999, §2, Theorem
  1](../../../../library/set_systems/fon_der_flaass_et_al_1999_transversals_uniform_hypergraphs_property_7_2/_index.md):
  for $q\ge10$, take $|S|=7q+1$, $X\subset S$ of size $4q$, and all $4q$-sets
  $B$ with $|B\cap X|$ odd. This family has $P_7$ and $\tau=3q+1$. The proof's
  Fano-pattern classification was examined. The remark suggesting $q\ge4$ is not
  a supplied proof for that enlarged range and was not needed.
* The same paper, §3, Theorem 2: if a $k$-uniform family has
  $\tau>\lceil7k/8\rceil$, it contains a subfamily of at most seven edges
  whose transversal number exceeds two. Its displayed proof treats $k\ge8$.
* [Bucić–Korándi–Sudakov, Theorem 5.7](../../../../library/set_systems/bucic_et_al_2019_covering_graphs_by_monochromatic_trees_helly_type_results_hypergraphs/_index.md)
  gives the complete-hypergraph counting lower bound reproduced in §3 below.
  Proposition 5.6 gives the initial exact case for their at-most-local-size
  convention.
* [Tuza, 1985, §2, inequality (*), and
  §4.1](../../../../library/set_systems/tuza_1985_critical_hypergraphs_intersecting_set_pair_systems/_index.md)
  give the set-pair inequality and critical-edge certificates used in §4. The
  composition in §2.1 and Construction 15 in §4.1 were also checked; neither was
  shown to preserve $P_r$.

### Why the supplied parity example is not a disproof

Its parameters are

$$
k=4q,\qquad \tau=3q+1,\qquad \frac{\tau}{k}=\frac34+\frac1{4q}.
$$

The excess is bounded, not linear.

The transversal calculation itself is short. The complement $S\setminus X$ meets
every allowed edge and has size $3q+1$. For any $T$ of size $3q$, the set
$U=S\setminus T$ has size $4q+1$ and contains both a point of $X$ and a point
outside $X$. Deleting one or the other of those points changes the parity of the
intersection with $X$, so one resulting $4q$-subset of $U$ is allowed. Thus $T$
is not a transversal.

The local condition is the difficult part of the supplied theorem. It must not
be inferred just from this transversal calculation.

## 3. Elementary bounds and finite reduction

### 3.1 An all-uniformity $3/4$ lower bound

Let

$$
n=\left\lceil\frac{7k}{4}\right\rceil-1
$$

and let $\mathcal H$ consist of all $k$-subsets of an $n$-point ground set. In
any seven edges, the total incidence degree is $7k>4n$, so some point lies in at
least five edges. The at most two remaining edges can be met by one point: two
$k$-sets intersect because $n<2k$.

The complete family's transversal number is $n-k+1$. Hence

$$
f(k,7)\ge\left\lceil\frac{3k}{4}\right\rceil.
$$

Together with the checked 1999 upper bound, this gives

$$
\boxed{\left\lceil\frac{3k}{4}\right\rceil
\le f(k,7)\le\left\lceil\frac{7k}{8}\right\rceil\qquad(k\ge8).}
$$

This does not determine the limiting coefficient.

### 3.2 Linear bounds for every fixed $r$

For a family with at least $r$ edges satisfying $P_r$, there cannot be three
disjoint edges. A maximal disjoint subfamily therefore has at most two edges;
its union is a transversal. Including the vacuous case gives

$$
f(k,r)\le\max\{2k,r-1\}.
$$


For the lower bound, take all $k$-subsets of a set of size $k+t$. Each edge
misses precisely $\binom t2$ pairs. If

$$
r\binom t2<\binom{k+t}{2},
$$

the pairs missed by at least one of any $r$ edges do not exhaust all pairs. A
remaining pair meets every edge of the chosen subfamily. Since the complete
family has transversal number $t+1$, choosing $t=\lfloor ck\rfloor$ for any
fixed $0<c<1/(\sqrt r-1)$ gives

$$
\frac1{\sqrt r-1}
\le\liminf_{k\to\infty}\frac{f(k,r)}k
\le\limsup_{k\to\infty}\frac{f(k,r)}k
\le2.
$$

The sufficient asymptotic inequality is $rc^2<(1+c)^2$. This proves linear
order, not convergence.

### 3.3 Compactness for families of finite sets

**Claim.** If every finite subfamily of a family of finite sets has a
transversal of size at most $t$, so does the whole family.

**Proof.** Induct on $t$. The case $t=0$ is immediate. Fix an edge $A$. For each
$x\in A$, let $\mathcal H_x$ consist of edges missing $x$. If none of these
families has a $(t-1)$-point transversal, induction gives finite
$\mathcal F_x\subseteq\mathcal H_x$ with that property. The finite family

$$
\{A\}\cup\bigcup_{x\in A}\mathcal F_x
$$

cannot have a $t$-point transversal: choose $x$ in its intersection with $A$ and
remove $x$ to obtain a forbidden $(t-1)$-point transversal of $\mathcal F_x$.
Therefore some $\mathcal H_x$ has a $(t-1)$-point transversal, which together
with $x$ covers the whole family. $\square$

Thus passing to finite obstructions is legitimate. This compactness statement
does not supply an asymptotic scaling theorem.

## 4. Reformulations and finite critical certificates

### 4.1 Complements

For a finite ground set $V$ of size at least two, set

$$
\mathcal B=\{V\setminus E:E\in\mathcal H\}.
$$

Then:

* A chosen subfamily of $\mathcal H$ has no two-point transversal exactly when
  the corresponding complement blocks cover every pair of points of $V$.
* For $0\le t\le|V|$, $\tau(\mathcal H)>t$ exactly when every $t$-subset is
  contained in some block of $\mathcal B$.
* Equivalently, $\tau(\mathcal H)>t$ says that every $(|V|-t)$-subset contains
  an edge of $\mathcal H$.

This turns a candidate counterexample into a strong covering-design requirement,
not merely a large collection of allowed sets.

### 4.2 Dual incidence

Use the edges of $\mathcal H$ as a new ground set. Each original point $v$
defines its star

$$
S_v=\{E\in\mathcal H:v\in E\}.
$$

Every new ground point belongs to exactly $k$ stars when stars retain their
original-point indices. The local hypothesis says every $r$ new ground points
lie in the union of at most two stars; the original transversal number is the
minimum number of stars covering the whole new ground set.

This reformulation was useful for checking products. Duplicating a star changes
incidences but not the minimum number of distinct supports needed for a cover,
explaining why ordinary point cloning cannot multiply $\tau$.

### 4.3 Critical certificates

For a finite family with transversal number $t$, choose an edge-minimal
subfamily with the same transversal number. For each retained edge $E_i$, there
is a set $T_i$ of size $t-1$ such that

$$
T_i\cap E_i=\varnothing,\qquad T_i\cap E_j\ne\varnothing\quad(j\ne i).
$$

Deleting a critical edge lowers $\tau$ by exactly one: it lowers it at all by
criticality, and adding one point of the deleted edge to a cover of the
remainder gives a cover of the original family.

The checked set-pair inequality therefore gives

$$
|E(\mathcal H)|\le\binom{k+t-1}{k}.
$$

After discarding isolated ground points, Tuza's Theorem 17 also gives the vertex
bound

$$
|V(\mathcal H)|<\binom{k+t}{k}
$$

for such a uniform critical family.

These bounds permit finite reductions but are exponential when $t$ is
proportional to $k$. No additional set-pair inequality incorporating $P_r$ was
obtained.

## 5. A ground-set bound from the Fano plane

**Claim.** Suppose $|\mathcal H|\ge7$, $\mathcal H$ has $P_7$, and its finite
ground set has size $n=7q+s$, $0\le s\le6$. Then

$$
\tau(\mathcal H)\le3q+w(s),\qquad
(w(0),\ldots,w(6))=(0,1,2,2,2,3,3).
$$

Without the assumption on the number of edges, use the maximum of this bound and
$6$.

**Proof.** Partition the ground set into seven classes of size $q$ or $q+1$,
indexed by the Fano-plane points. Arrange the $s$ larger classes so that every
line contains at most $w(s)$ of their indices. The only nontrivial choices are:
for $s=3$ use a noncollinear triple, and for $s=4$ use the complement of a line.

For each Fano line $L$, let $U_L$ be the union of its three classes. Every pair
of ground points is in some $U_L$, including pairs within one class, and
$|U_L|\le3q+w(s)$. If $\tau$ exceeded this bound, choose an edge disjoint from
each $U_L$. No pair would cover these at most seven chosen edges. Extend to
seven distinct edges if necessary. $\square$

In particular,

$$
\tau(\mathcal H)\le\frac{3n}{7}+O(1).
$$

A counterexample with $\tau>(3/4+\delta)k$ would therefore need

$$
n>\left(\frac74+\frac{7\delta}{3}\right)k-O(1).
$$

The unresolved issue is controlling the ground-set size of an extremal family,
or an appropriate smaller representation. No reduction to $n\le k+\tau+o(k)$ was
proved.

## 6. Scaling attempts and exact failure points

### 6.1 Monotonicity is valid, but insufficient

Pad every edge with its own private new point. Old transversals remain
transversals. A transversal using private points can replace each such point by
an original point of its associated edge without increasing its size. Thus
$\tau$ is unchanged and $P_r$ is preserved, proving

$$
f(k+1,r)\ge f(k,r).
$$

The same argument permits private padding to a common larger rank.

Monotonicity plus linear bounds does not imply convergence of the ratio. For
comparison, the nondecreasing function $g(k)=2^{\lfloor\log_2k\rfloor}$ has
$\limsup g(k)/k=1$ and $\liminf g(k)/k=1/2$. This is only a warning about an
inference, not a proposed model for $f$.

### 6.2 Full cloning, unions, and products

Replacing every point by a full $m$-point block and every edge by the union of
its blocks multiplies uniformity by $m$ but leaves $\tau$ unchanged: one
representative of each chosen block suffices.

For families on disjoint grounds, the family of all unions $E_1\cup E_2$ has

$$
\tau=\min\{\tau(\mathcal H_1),\tau(\mathcal H_2)\}.
$$

A transversal of either factor works. Conversely, if neither restriction is a
transversal of its factor, select a missed edge on each side; their union is
missed.

Disjoint union adds transversal numbers but does not preserve $P_r$ in general.
These operations do not amplify the parity example's additive surplus.

### 6.3 Lexicographic inner-family substitution

Replace each point $v$ of $\mathcal H$ by a private copy $\mathcal G_v$ of a
uniform family $\mathcal G$. For every $E\in\mathcal H$, take all unions of
independently chosen edges $F_v\in\mathcal G_v$ for $v\in E$. The resulting
family has

$$
k_{\rm new}=k_{\mathcal H}k_{\mathcal G},
\qquad
\tau_{\rm new}=\tau(\mathcal H)\tau(\mathcal G).
$$

Indeed, the indices of copies on which a proposed transversal is itself a
transversal must cover $\mathcal H$, and this condition is also sufficient.

Assume here that the base family has the local property for at most $r$ edges,
as follows from $P_r$ when it has at least $r$ edges. A sufficient preservation
condition is that every at-most-$r$ edges of $\mathcal G$ have a common point.
Given the two base points covering the projected edges, use the common
intersection in each corresponding inner copy. However, an $r$-wise-intersecting
$a$-uniform family, in this at-most-$r$ sense, has

$$
\tau(\mathcal G)\le\frac{a-1}{r-1}+1.
$$

For the elementary greedy argument, if $\tau=t$, intersections of fewer than $r$
previously selected edges cannot have size less than $t$, or another edge could
avoid the whole intersection. At each of $r-1$ steps choose an edge avoiding
$t-1$ points of the current intersection. The final nonempty intersection gives
$a-(r-1)(t-1)\ge1$.

Thus this straightforward preservation mechanism loses a factor asymptotic to
$r-1$ in the ratio when the inner family grows. It is not a ratio-preserving
blow-up.

For the special inner family of all $(m-s+1)$-subsets of an $m$-point set,
$\tau=s$, and the sufficient intersection condition is $r(s-1)<m$. The same loss
is visible directly in these parameters.

### 6.4 Replacing only one point of each edge

Another attempted operation has edges

$$
(E\setminus\{v\})\cup F,\qquad E\in\mathcal H,\ v\in E,\ F\in\mathcal G_v,
$$

where the original points remain and all inner copies are private. Its rank is
$k_{\mathcal H}+k_{\mathcal G}-1$.

There is an exact cover optimization. Let $A$ be the selected original points,
and let $B$ be the indices of inner copies on which a full transversal is
selected. Partial inner selections can be discarded. The cost is

$$
|A|+\tau(\mathcal G)|B|.
$$

For each original edge $E$, the conditions are:

* If $|E\cap A|\ge2$, no further condition is needed.
* If $E\cap A=\{v\}$, require $v\in B$.
* If $E\cap A=\varnothing$, require $E\subseteq B$.

In particular the new transversal number is at most the number needed to meet
each original edge in two points. For the complete $k$-uniform family on $n$
points, that number is $n-k+2=\tau(\mathcal H)+1$, irrespective of how large
$\tau(\mathcal G)$ is. No preservation proof for $P_7$ was obtained either.

Here “meeting each edge in two points” is a different notion from locally
meeting several edges with two points.

### 6.5 A critical-hypergraph sum: correct parameters, wrong local property

Let $\mathcal H_i$ be uniform and $\tau$-critical, with ranks $k_i$ and cover
numbers $t_i$. Choose edges $E_i$ and points $x_i\in E_i$. Identify $x_1,x_2$ as
a point $x$, delete $E_1,E_2$, and add $E_1\cup E_2$. The rank is $k_1+k_2-1$,
and

$$
\tau=t_1+t_2-1.
$$


For the lower bound, a cover containing $x$ restricts to covers of both original
families. A cover excluding $x$ must have at least $t_i-1$ points on each side.
If equality holds on both sides, both restrictions miss $E_i$, so the new edge
is missed. For the upper bound, take critical $(t_i-1)$-point covers missing
$E_i$ and add $x$. Private padding uniformizes the remaining edges without
changing $\tau$.

But this operation fails $P_7$. Take each original family to consist of all
$8$-subsets of a $13$-point set. It has $P_7$ because $7\cdot8>4\cdot13$. Choose
the deleted edge to contain $x$. On each side, partition the other twelve points
into three four-point sets and take their three complements within those twelve
points. These are three retained $8$-edges with empty common intersection,
requiring two points. The two triples have disjoint grounds, so their six edges
require four points. Adding the joined edge gives a seven-edge violation.
Private padding introduces no common points and does not repair it.

Thus a tempting numerical amplification has an explicit local-condition failure.

### 6.6 Minkowski-type count expansion

A further attempted scaling allowed the count vector in clone blocks to be a sum
of incidence vectors of original edges. Such convexification does not preserve
even $P_3$.

For an explicit two-fold example, start with the graph consisting of two
disjoint triangles, viewed as a $2$-uniform family. It has $P_3$ because its
matching number is two. Replace every vertex by two clones and admit every
four-point set whose block counts equal the sum of two original edge vectors. In
the first triangle, use the three edges $ab,ac,bc$; use the analogous three
edges in the second triangle. For each of the three pairs of corresponding
edges, choose one clone of each of its four vertices, using different clones at
the two occurrences of any original vertex. The resulting three admitted
four-point sets are disjoint. Hence the expanded family fails $P_3$.

### 6.7 Tuza's set-pair composition is not a scaling theorem for this problem

In the checked §2.1 composition, first-coordinate sets have the form
$A'_i\cup A''_j$, where the $A'_i$ range over all $a'$-subsets of a fixed
$(a'+b')$-point set. For $a'>0$, any $b'+1$ points of that outer set meet every
first-coordinate set. The cover number is therefore at most $b'+1$, not the sum
suggested by the two certificate parameters.

Construction 15 completes a set-pair system to a generally nonuniform critical
hypergraph. The construction was not shown to preserve $P_r$. The certificate
parameters alone cannot supply the required amplification.

### 6.8 Sampling and identification

Identifying ground points preserves the local condition, because the image of a
two-point cover still covers the image edges. It can collapse the transversal
number. Restricting the ground set or shrinking edges can destroy the local
witnesses. No random restriction, quotient, or interpolation lemma was
established that scales uniformity and transversal number proportionally while
preserving $P_r$.

## 7. Coding constructions: a proved lemma and the missing cover estimate

### 7.1 Spectra of a bad seven-tuple

For seven edges $E_1,\ldots,E_7$, define

$$
S_v=\{i:v\in E_i\},\qquad T_v=[7]\setminus S_v.
$$

There is no two-point transversal exactly when the $T_v$ are pairwise
intersecting, including the requirement that no single point covers all rows.
Equivalently, no two spectra $S_v,S_w$ have union $[7]$.

If all edges have size $k$ on $n<2k$ points, a bad seven-tuple has $|S_v|\le4$
for every $v$. A point in at least five rows would leave at most two
intersecting edges. Therefore, putting $d_v=|S_v|$,

$$
7k\le4n,\qquad D:=\sum_v(4-d_v)=4n-7k.
$$

The binary sum of the seven edge vectors is supported on odd-degree points. Each
such point contributes at least one to $D$, so

$$
\left|E_1\triangle\cdots\triangle E_7\right|\le D.
$$


### 7.2 Robust parity lemma

**Lemma.** Let $n<2k$, let $M:\mathbf F_2^n\to\mathbf F_2^h$ be linear, and let
$b\ne0$. Suppose every vector $z$ with $Mz=b$ has weight greater than $4n-7k$.
Then the family

$$
\mathcal H=\{x\in\mathbf F_2^n:|x|=k,\ Mx=b\}
$$

has $P_7$.

**Proof.** A bad seven-tuple would have binary sum $z$ of weight at most $4n-7k$
by the preceding calculation. But $Mz=7b=b$, a contradiction. $\square$

This is a sufficient local condition, not a counterexample: $\mathcal H$ could
be empty or have a small transversal.

### 7.3 Exact global requirement for a proposed code example

Suppose $n=(7/4+\varepsilon)k+O(1)$ and the target is

$$
\tau(\mathcal H)>(3/4+\delta)k,\qquad\delta>0.
$$

Then every set of size

$$
k+(\varepsilon-\delta)k+O(1)
$$

must contain a weight-$k$ vector of the chosen coset. This is a strong punctured
constant-weight extension requirement.

The transversal number of the family of supports of all vectors in the coset is
not a lower bound for the transversal number of the weight-$k$ subfamily:
restricting the edge family can only decrease $\tau$.

### 7.4 Random-code entropy diagnostic — not an impossibility theorem

Write $H(u)=-u\log u-(1-u)\log(1-u)$, with natural logarithms. For a random
binary parity-check matrix with $h$ rows, the usual first-moment estimate to
exclude syndrome-$b$ vectors up to weight $w$ asks approximately for

$$
h\log2>nH(w/n).
$$

The robust parity lemma needs $w>4\varepsilon k+O(1)$. On the other hand, inside
a fixed set of size $k+s$, the expected number of weight-$k$ vectors of the
coset is

$$
2^{-h}\binom{k+s}{k}.
$$

The desired cover property needs
$s=(\varepsilon-\delta)k+O(1)<\varepsilon k+O(1)$.

For small $\varepsilon$, the first estimate costs roughly

$$
4\varepsilon k\log(1/\varepsilon),
$$

whereas $\log\binom{k+s}{k}$ is at most roughly

$$
\varepsilon k\log(1/\varepsilon).
$$

Thus these straightforward probabilistic sufficient conditions do not overlap.
This does not rule out specially structured codes or a different local
obstruction criterion.

### 7.5 Conditional Fano refinement

In the supplied parity proof, after a separate classification, the standard
degree-four spectra are the seven complements of Fano lines. These seven vectors
are the nonzero words of the binary $[7,3,4]$ simplex code. Every Fano-line
triple of row indices has even intersection with each standard spectrum, so the
XOR of those three rows is supported on nonstandard points.

Assume, conditionally, that this standard-pattern description holds and all
seven types occur. A nonstandard three-element spectrum cannot itself be a Fano
line, since it and the standard complementary spectrum would cover all seven
rows.

Let $Z_L$ be the XOR of the three rows indexed by a Fano line $L$. A nonstandard
spectrum of size $d=0,1,2,3$ contributes, respectively, $0,3,4,3$ to
$\sum_L|Z_L|$, where the $d=3$ count uses the exclusion of a line. These are at
most $3(4-d)$. Hence

$$
\sum_L|Z_L|\le3D.
$$

If all seven rows have syndrome $b$ and every syndrome-$b$ vector has weight at
least $w$, then $MZ_L=b$ for each line and

$$
7w\le3D.
$$

With the total-weight parity and the odd-$X$ parity both included, the supplied
construction has target syndrome $(0,1)$, minimum possible weight $w=2$, and
deficiency $D=4$. The inequality would give $14\le12$, recovering a
contradiction once the source's structural classification is available.

**Unresolved qualification:** the supplied classification concerns the
bounded-deficiency setting of that proof. It was not proved for deficiency
proportional to $k$. It cannot simply be assumed in a proposed linear
improvement. Analysis of the four-dimensional quotient by the simplex code was
considered, but no usable distance-versus-extension theorem was established.

## 8. Random subfamilies and deletion of bad tuples

A separate attempted construction sampled $k$-sets on approximately $7k/4$
points and tried to delete one edge from each bad seven-tuple.

Here is the concrete entropy obstruction to the simplest first-moment
implementation. Put $k=4q$, $n=7q$. Assign the $n$ points equally among the
seven Fano-complement spectrum types. This produces bad ordered seven-tuples
with all rows of size $k$. Their number has exponential rate

$$
\frac{n!}{(q!)^7}=\exp(n\log7+o(n)).
$$

The total number of ordered seven-tuples has rate $\exp(7nH(4/7)+o(n))$. Thus
these Fano-pattern obstructions alone have probability on the scale

$$
\exp(-In+o(n)),\qquad
I=7H(4/7)-\log7\approx2.83445.
$$

For a random family of expected size $M$, asking the expected number of these
obstructions to be $o(M)$ forces the usual deletion calculation onto the scale

$$
\log M<\frac{I}{6}n+o(n)\approx0.47241n.
$$


But if every $(k+s)$-subset is to contain an edge, simple double counting
requires

$$
M\ge
\frac{\binom n{k+s}}{\binom{n-k}s}
=\frac{\binom nk}{\binom{k+s}k}.
$$

For $s=o(n)$ this requires

$$
\log M\ge nH(4/7)-o(n)\approx0.68291n.
$$

The gap prevents this crude expected-count/delete-one-per-tuple argument from
reaching the boundary cover number.

This calculation does not show that all random methods, correlated selections,
or efficient deletions fail. Nor was a classification of all bad tuples used:
the explicitly counted Fano tuples already obstruct this particular first-moment
criterion.

## 9. Upper-bound proof attempts

### 9.1 A small-intersection observation

For a fixed edge $A$, let $m=\min_{E\in\mathcal H}|A\cap E|$. Any
$(k-m+1)$-subset of $A$ meets every edge, so

$$
\tau(\mathcal H)\le k-m+1.
$$

In particular, $\tau>(3/4)k$ forces a pair with intersection at most $k/4+O(1)$.
This supplies an initial pair but does not control the later intersections
needed for a seven-edge obstruction.

### 9.2 Candidate pairs after a good triple

Let $A_1,A_2,A_3$ have empty common intersection. Put

$$
X=A_1\cap A_2,\quad Y=A_1\cap A_3,\quad Z=A_2\cap A_3.
$$

Let $U_3,U_2,U_1$ be the respective unique parts of the opposite edges. Every
two-point cover of the triple is an edge of the graph consisting of the complete
cross-pairs

$$
XY,\ XZ,\ YZ,\ XU_3,\ YU_2,\ ZU_1.
$$


If four subsets $S_1,\ldots,S_4$ of this graph's vertex set cover all its edges
in the sense that both endpoints of every graph edge lie in some $S_i$, and
$|S_i|<\tau(\mathcal H)$, choose four hyperedges avoiding them. Together with
the initial triple these have no two-point transversal.

This is a valid sufficient mechanism. A universal four-subset cover with each
size at most $3k/4$ is false.

### 9.3 Exact continuous obstruction for that mechanism

Normalize $k=1$. Write $|X|=x$, $|Y|=y$, $|Z|=z$, $s=x+y+z$, and denote the
opposite unique-atom weights by

$$
u_X=1-s+x,\qquad u_Y=1-s+y,\qquad u_Z=1-s+z.
$$

Allow atoms to be split into arbitrary real weights. Assume all six weights are
positive.

**Claim.** Four subsets of weight at most $3/4$ cover all candidate graph edges
if and only if

$$
s-2x\le\frac14,\qquad
s-2y\le\frac14,\qquad
s-2z\le\frac14.
$$


**Proof.** Give each point the signature of covering-subset indices containing
it. An overlap point cannot have a singleton signature: its entire opposite
edge, of weight one, would then have to lie in that one covering subset. Every
overlap point therefore appears at least twice, and every unique point appears
at least once. Total appearances are at least

$$
2s+(3-2s)=3.
$$

The total capacity is exactly three, forcing equality: overlap signatures have
size two, unique signatures size one, and every subset has weight $3/4$.

All overlap signatures intersect pairwise. Across different atoms this follows
from graph edges; within one atom it follows from a singleton signature in its
nonempty opposite unique atom. An intersecting family of two-subsets of $[4]$ is
a star or is contained in a triangle. A triangle leaves the fourth subset empty,
impossible.

Thus the signatures form a star. If an overlap atom uses two arms, its opposite
unique atom must lie at the center. The center would then have weight at least
$s+u_X=1+x$, or its cyclic analog. Hence each overlap atom uses one fixed arm,
and all three arms must be different to fill all four subsets.

The outer subset for $X$ must contain $X$ plus $3/4-x$ of its unique atom. This
is possible exactly when $u_X\ge3/4-x$, namely $s-2x\le1/4$, and cyclically.

Conversely these inequalities imply $s\le3/4$. Put each overlap atom in the
center and its own outer subset. Fill that outer subset to $3/4$ from the
opposite unique atom and put the remainder in the center. The center also has
weight $3/4$, and every graph edge is covered. $\square$

For example, $x=y=z=1/3$ fails. Discretely, take all six atoms of size $k/3$,
with $3\mid k$; the signature argument proves impossibility of four subsets of
size at most $3k/4$ directly. This is a counterexample to the proposed auxiliary
lemma, not to the Erdős assertion.

The boundary $x=y=z=1/2$, with no unique atoms, behaves differently. Split each
overlap atom in half, and use the four even-parity binary triples to choose one
half of each atom. Each chosen subset has size $3k/4$, and any two half choices
from distinct atoms occur together in one subset. Thus the all-positive-atoms
assumption in the characterization is essential.

### 9.4 What the supplied $7/8$ argument does not automatically improve

The 1999 proof uses a good triple and four carefully chosen avoidance sets.
Writing its displayed size estimates in normalized form, with proposed threshold
$c$ and ordered overlap sizes $x\ge y\ge z$, gives a final-set expression

$$
3(1-c)+x
$$

in one case and

$$
\max\{3(1-c)+x,\ 2(1-c)+y+z,\ (1-c)+2y\}
$$

in the other. Requiring these to be at most $c$ leads to

$$
x\le4c-3,\qquad y+z\le3c-2,\qquad y\le c-\frac12.
$$

At $c=7/8$ these reproduce the source's useful bounds $x\le1/2$, $y+z\le5/8$,
$y\le3/8$. At $c=3/4$, the first becomes $x\le0$. This calculation diagnoses why
merely changing the numerical threshold in that construction is not enough. It
is not a new general theorem asserting that those estimates are necessary for
all upper-bound strategies.

### 9.5 Another seven-edge obstruction template

Partition an edge $A=A_1\sqcup A_2\sqcup A_3$. Choose $B_i$ disjoint from
$A\setminus A_i$, and put

$$
P_i=B_j\cap B_\ell,\qquad \{i,j,\ell\}=\{1,2,3\}.
$$

Then $P_i\cap A=\varnothing$. If $|A_i|+|P_i|<\tau(\mathcal H)$, choose $C_i$
disjoint from $A_i\cup P_i$.

The seven edges $A,B_1,B_2,B_3,C_1,C_2,C_3$ have no two-point transversal. One
point of any proposed cover must lie in some $A_i$; it misses $B_j,B_\ell$,
forcing the other point into $P_i$. Both points then miss $C_i$.

This template also fails to reach $3/4$ automatically. In a complete-family
model on $n=7k/4-1$ points, take balanced $|A_i|=k/3$. Every $B_i$ has at least
$2k/3$ points outside $A$, so

$$
|B_j\cap B_\ell|
\ge\frac{4k}{3}-(n-k)
=\frac{7k}{12}+1.
$$

The desired $|A_i|+|P_i|\le3k/4$ would instead need $|P_i|\le5k/12$. Thus this
particular template does not even match the dense examples at the conjectured
boundary.

## 10. Remaining uncertainties

The first question still requires one of two fundamentally missing statements:

1. A proof that every $P_7$ family has $\tau\le(3/4+o(1))k$, using more than the
   fixed-triple four-set covering mechanism; or
2. A verified family with $P_7$ and $\tau\ge(3/4+\delta)k$ for some fixed
   $\delta>0$ along an unbounded sequence.

No candidate considered satisfies the second requirement. In particular, the
supplied parity surplus is bounded, the code lemma has no adequate
constant-weight cover estimate, and critical sums fail the local condition.

For the second question, no superadditivity, subadditivity, interpolation, or
structural theorem was proved that forces

$$
\liminf_{k\to\infty}\frac{f(k,r)}k
=\limsup_{k\to\infty}\frac{f(k,r)}k.
$$

The finite critical reductions, monotonicity, and linear bounds do not imply
that equality.

The conditional Fano refinement must not be used outside its established
structural hypotheses. The random-code and random-subfamily entropy calculations
describe failures of specific elementary implementations, not impossibility
theorems for those broad approaches. No claim of resolution is supported by this
record.
