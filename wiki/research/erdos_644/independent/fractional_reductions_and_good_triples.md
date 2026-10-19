---
name: research/erdos_644/independent/fractional_reductions_and_good_triples
title: Independent record on Erdős Problem 644
desc: Unverified independent record; checked overlaps, stronger parity-union failure, and qualifications are documented in topical notes.
tags: [unverified, research-input]
sources: []
created: 2026-09-23T03:40:33Z
updated: 2026-09-23T03:41:32Z
---


# Independent record on Erdős Problem 644

***

## 1. Status, conventions, and source use

**Neither requested assertion was resolved.** No family with a fixed positive
asymptotic excess over $3k/4$, matching $3/4$ upper bound, or general
convergence theorem was obtained. This record distinguishes proofs,
conditional calculations, and computational evidence.

This record collects the analysis of the canonical problem page and cited
papers.

Write $P_r$ for the condition that every subfamily of at most $r$ edges has
a transversal of size at most two. The original condition for exactly $r$
distinct members implies $P_r$ whenever the family has at least $r$ members.
A smaller family has transversal number at most $r-1$. This distinction does
not affect the asymptotic questions but matters at small uniformities.

All edges considered below are nonempty. Fractional parameters are used for
finite, nonempty hypergraphs. Rank means maximum edge size.

### Source passages checked

* Fon-Der-Flaass–Kostochka–Woodall, supplied source.md, Section 2, Theorem 1 and
  Claims 1–6: the parity construction has $P_7$ and transversal number
  $3q+1$. Section 3, Theorem 2: the $\lceil7k/8\rceil$ upper bound.
* Bucić–Korándi–Sudakov, supplied source.md, Theorem 5.7: the complete-family
  counting lower bound. Proposition 5.6 gives the initial exact endpoint.
* Tuza, supplied source.md, Section 4.1: critical transversal certificates;
  Section 2, inequality (*): the set-pairs inequality; Theorem 17: the
  critical-vertex bound.
* Erdős, supplied source.md, Section 16: reports the exact neighboring values
  for local parameters 3 through 6 and states the two questions as expectations.
  That survey does not prove the neighboring results.

The problem page supplied with the task labels the questions open. No claim
about research outside these files is made.

## 2. Verified starting bounds and elementary reductions

### 2.1 The parity family

For every integer $q\ge10$, the 1999 paper proves that

$$
 |S|=7q+1,\qquad X\subseteq S,\quad |X|=4q,\qquad
 \mathcal B=\{B\subseteq S:|B|=4q,\ |B\cap X|\text{ is odd}\}
$$

has $P_7$ and $\tau(\mathcal B)=3q+1$.

The transversal calculation can be checked directly. The set $S\setminus X$ is
a transversal of size $3q+1$, since the only $4q$-subset contained in $X$
is $X$, whose intersection with $X$ is even. If $|T|=3q$, then
$S\setminus T$ has $4q+1$ points and contains both a point of $X$ and a
point outside $X$. Deleting one or the other produces two $4q$-sets with
opposite intersection parity with $X$. One is an edge disjoint from $T$.

The local proof is substantive. For a hypothetical bad seven-tuple, every point
has degree at most four: a point in five edges and a point in the intersection
of the remaining two would cover all seven. Any two edges intersect since
$8q>7q+1$. Total degree deficiency from four is

$$
 4(7q+1)-7(4q)=4.
$$

The paper's intersection estimates force the degree-four spectra into the
Fano-complement pattern, and parity on the exceptional points gives a
contradiction. This structural classification was not proved here for arbitrary
positive linear deficiency.

### 2.2 Private padding and the asymptotic interval

Adding private points to individual edges preserves the local condition and
preserves the global transversal number. An original transversal still works;
conversely, replace every selected private point by an original point of its
edge. Thus finite rank-$k$ examples can be made $k$-uniform, and $f(k,r)$
is nondecreasing in $k$.

The parity examples imply

$$
 f(k,7)\ge3\left\lfloor k/4\right\rfloor+1=\frac34k-O(1).
$$

Theorem 2 of the 1999 paper gives, for all sufficiently large $k$,

$$
 f(k,7)\le\left\lceil\frac{7k}{8}\right\rceil.
$$

Therefore the verified interval is

$$
 \frac34\le\liminf_k\frac{f(k,7)}k
 \le\limsup_k\frac{f(k,7)}k\le\frac78.
$$

The additive $+1$ at uniformity $4q$ is not an asymptotic disproof.

### 2.3 General linear order

The complete $k$-uniform hypergraph on $k+t$ points has transversal number
$t+1$. Each edge is missed by $\binom t2$ point-pairs, so any $r$ edges
have a common two-point cover whenever

$$
 r\binom t2<\binom{k+t}2.
$$

Taking $t=\lfloor ck\rfloor$ for $c<1/(\sqrt r-1)$ proves

$$
 \liminf_k\frac{f(k,r)}k\ge\frac1{\sqrt r-1}.
$$

This is the specialization of the checked Theorem 5.7.

The local condition forbids three disjoint edges. The union of a maximal
matching of at most two edges is a transversal, giving

$$
 f(k,r)\le\max\{2k,r-1\}.
$$

These bounds establish linear order, not convergence.

The Erdős survey reports

$$
 f(k,3)=2k,\quad f(k,4)=\lfloor3k/2\rfloor,\quad
 f(k,5)=\lfloor5k/4\rfloor,\quad f(k,6)=k.
$$

These are reported background, not results reproved in this investigation. The
exactly-$r$ vacuity issue should be remembered when quoting formulas at very
small $k$.

### 2.4 Finite witnesses for infinite families

If a family of finite sets has no transversal of size at most $t$, some finite
subfamily already has this property. Induct on $t$. For $t=0$, take one
edge. For $t>0$, fix an edge $E$. For each $v\in E$, the edges avoiding
$v$ have no $(t-1)$-point transversal, since adjoining $v$ would cover the
original family. Choose a finite witness for each $v$ and adjoin $E$. A
$t$-point cover of this finite union meets $E$ at some $v$; its remaining
points would cover the corresponding witness, a contradiction.

Consequently the finite universal upper bounds extend to the possibly infinite
families in the question. This fixed-integer compactness fact does not imply any
scaling or convergence statement.

## 3. Fractional reductions proved during the investigation

Write $\tau^*(H)$ for fractional transversal number, whose linear-programming
dual is fractional matching number.

### 3.1 General rounding

For every finite, nonempty rank-$k$ hypergraph,

$$
 \tau(H)\le k(\tau^*(H)-1)+1. \tag{3.1}
$$

Let $t=\tau^*(H)$, order optimal fractional-cover weights decreasingly, and
put $\ell=\lfloor k(t-1)\rfloor+1$. If fewer than $\ell$ vertices exist, the
assertion is immediate. Otherwise the sum of the next $k$ weights, padding
with zeros, is at most

$$
 \frac{kt}{\ell+k}<1.
$$

The reason is that the average of the first $\ell$ weights is at least the
average of the next $k$. Every rank-$k$ edge avoiding the first $\ell$
points therefore has weight less than one. Those $\ell$ points form a
transversal.

An earlier proposed proof used induction on $\tau$ after deleting all edges
containing a positive-weight vertex. That induction was not justified because
the remaining transversal number can stay unchanged. Induction on the number of
edges would repair it; the direct sorting argument avoids the problem.

### 3.2 A sufficient fractional threshold

If $\tau^*(H)<7/4$, then $H$ has $P_7$. First, $\tau^*<2$ implies that
every two edges intersect. In any bad seven-edge list, every point has degree at
most four. If fewer than seven edges form the obstruction, repeat edges to
obtain such a list; the same degree argument still works. For a fractional cover
$w$ of total weight below $7/4$,

$$
 7\le\sum_{i=1}^7\sum_{v\in E_i}w(v)
   =\sum_v d(v)w(v)
   \le4\sum_vw(v)<7,
$$

a contradiction.

By (3.1), this sufficient condition cannot produce asymptotic excess over
$3k/4$.

### 3.3 Three sampled edges

If $H$ has $P_7$, then, for $t=\tau^*(H)$,

$$
 \tau(H)\le\frac{3k}{t}+\left\lfloor\frac{k+2}{3}\right\rfloor. \tag{3.2}
$$

Normalize an optimal fractional matching to a distribution on edges. If $p_v$
is the inclusion probability of $v$, then

$$
 p_v\le1/t,\qquad \sum_vp_v\le k.
$$

Sample $A,B,C$ independently, allowing repetitions, and set

$$
 T=(A\cap B)\cup(A\cap C)\cup(B\cap C).
$$

Then $\mathbb E|T|\le3\sum_vp_v^2\le3k/t$. Fix a triple attaining this bound.

The residual family $G=\{E\in H:E\cap T=\varnothing\}$ is four-wise
intersecting. Indeed, cover any at most four residual edges and $A,B,C$ with
at most two points. One covering point meets at least two of $A,B,C$, counted
with repetition, so lies in $T$. It meets no residual edge. The other point
must meet all the chosen residual edges.

For a rank-$k$, four-wise-intersecting family of transversal number $a$,
choose $E_1$, choose $E_2$ avoiding $a-1$ points of $E_1$, and choose
$E_3$ avoiding $a-1$ points of $E_1\cap E_2$. Pair and triple
intersections are transversals, so the selections are possible and

$$
 a\le|E_1\cap E_2\cap E_3|\le k-2(a-1).
$$

Thus $\tau(G)\le\lfloor(k+2)/3\rfloor$. A cover of $G$ together with $T$
covers $H$, proving (3.2). Empty residual families cause no difficulty.

The exact expectation gives, for $t\ge4/3$,

$$
 \mathbb E|T|=\sum_v(3p_v^2-2p_v^3)
 \le k\left(\frac3t-\frac2{t^2}\right),
$$

because $3x-2x^2$ increases on $0\le x\le1/t\le3/4$. Therefore

$$
 \tau(H)\le
 k\left(\frac3t-\frac2{t^2}\right)
 +\left\lfloor\frac{k+2}{3}\right\rfloor. \tag{3.3}
$$


A hypothetical sequence with $\tau(H)/k\ge3/4+\varepsilon$ consequently has

$$
 t\ge7/4+\varepsilon-1/k
$$

and bounded $t$. Dropping the positive $\varepsilon$ weakens the asymptotic
upper restriction to

$$
 t\le\frac{18+2\sqrt{51}}5+o(1)
 \approx6.45657+o(1).
$$

The endpoint solves $1/3+3/t-2/t^2=3/4$ on the relevant branch. No
contradiction was found within this interval.

### 3.4 Generalization and limitations

If every at most $q$ edges of a rank-$k$ family intersect, $q\ge2$, the
same shaving argument with $q-1$ edges proves

$$
 \tau\le\left\lfloor\frac{k+q-2}{q-1}\right\rfloor
 =\left\lceil\frac{k}{q-1}\right\rceil.
$$

For $P_r$, $r\ge5$, the three sampled edges leave an
$(r-3)$-wise-intersecting family, so

$$
 \tau(H)\le\frac{3k}{\tau^*(H)}
 +\left\lfloor\frac{k+r-5}{r-4}\right\rfloor. \tag{3.4}
$$


The local property alone does not bound $\tau^*$. In projective four-space
over a finite field of order $q$, take points as vertices and hyperplanes as
edges. Any four hyperplanes intersect, so any seven split into groups of four
and three have a two-point cover. Here

$$
 k=q^3+q^2+q+1,\quad n=q^4+q^3+q^2+q+1,\quad \tau^*=n/k\sim q.
$$

Uniform weights $1/k$ on points and on hyperplanes prove the fractional
equality by regularity. A projective line meets every hyperplane, so
$\tau\le q+1=o(k)$.

Even bounded $\tau^*$ did not yield a suitable core. Keeping only vertices of
fractional weight at least $\delta/k$ leaves $O(k/\delta)$ points but may
delete the sole local covering points. No proof that this operation preserves
$P_r$ was found.

## 4. Complete-family limit: a restricted result

For fixed $r$, define

$$
 M_r=\max\{\nu^*(\mathcal G):
 \mathcal G\text{ is an intersecting family of nonempty subsets of }[r]\}.
$$

This is a maximum over finitely many families. The largest transversal number
among complete $k$-uniform families satisfying $P_r$ has asymptotic
coefficient

$$
 \frac1{M_r-1}. \tag{4.1}
$$

This does not establish the coefficient for arbitrary families.

For a bad list $A_1,\ldots,A_r$ on $n$ points, the complement spectra

$$
 C(v)=\{i:v\notin A_i\}
$$

are nonempty and pairwise intersecting. Their distribution under a uniformly
chosen point has each coordinate marginal

$$
 \mu=(n-k)/n.
$$

Dividing the type probabilities by $\mu$ gives a fractional matching of weight
$1/\mu$. Thus $\mu\ge1/M_r$.

Conversely, normalize an optimal fractional matching of size $M_r$ to a
probability distribution. Every coordinate marginal is at most $1/M_r$.
Increase each deficient marginal to equality by splitting mass and adding that
coordinate to the corresponding spectra. Enlarging spectra preserves
intersection. The resulting balanced distribution can be rational.

Repeat a denominator-sized realization to obtain integer columns; fill the
bounded remainder with the spectrum $[r]$. Whenever $(n-k)/n>1/M_r$ by a
fixed margin, all initial coordinate counts are below $n-k$ for large $n$.
Add coordinates to columns until each count equals $n-k$. This preserves
intersection and produces a bad list of $k$-sets. Repeated rows give an
obstruction on fewer than $r$ edges and can be extended inside the complete
family. Hence the complete-family threshold is $n/k=M_r/(M_r-1)+o(1)$; its
cover number $n-k+1$ proves (4.1).

For $r=7$, $M_7=7/3$. An intersecting family with an edge of size at most
two has a transversal of size at most two, so fractional matching number at most
two. Otherwise every edge has at least three points and the seven capacity
constraints give $\nu^*\le7/3$. The Fano lines attain $7/3$ with weight
$1/3$ each. Thus the complete-family coefficient is $3/4$.

The missing argument is any reduction from arbitrary families to this subclass
up to $o(k)$. The finite parity construction already disproves exact
reduction.

## 5. Good triples and the upper-bound strategy

Let $A_1,A_2,A_3$ be a good triple, meaning that their triple intersection is
empty. For $\{i,j,\ell\}=\{1,2,3\}$, write

$$
 X_i=A_j\cap A_\ell,\quad a_i=|X_i|,\quad
 S_i=A_i\setminus(A_j\cup A_\ell),\quad s=a_1+a_2+a_3.
$$

The atoms are disjoint and $|S_i|=k-s+a_i$. Candidate two-point covers are
exactly pairs between distinct $X_i$'s or between $X_i$ and $S_i$.

### 5.1 A proved four-set completion

If four sets $B_0,\ldots,B_3$, each of size at most $T<\tau(H)$,
collectively contain all candidate pairs, choose an edge disjoint from each
$B_i$. The resulting at most seven edges have no two-point cover.

Such sets exist if

$$
 s+\sum_i\max\{0,k-s+2a_i-T\}\le T,\qquad \max_i a_i\le T. \tag{5.1}
$$

Split $S_i=P_i\mathbin{\dot\cup}Q_i$, with

$$
 |P_i|=\max\{0,k-s+2a_i-T\},
$$

and use

$$
 B_0=X_1\cup X_2\cup X_3\cup P_1\cup P_2\cup P_3,\qquad
 B_i=X_i\cup Q_i.
$$

The size bounds and pair coverage are immediate from (5.1).

Expanding the positive parts shows that this construction's least real threshold
is

$$
 T_{\rm hub}=\max\left\{\frac{3k}{4},\,s,\,
 \frac{k}{2}+\max_i a_i,\,
 \max_i\frac{2k+s-2a_i}{3}\right\}. \tag{5.2}
$$

Rounding upward gives integer sets. In particular $T=3k/4$, when integral,
works if

$$
 s\le3k/4,\qquad s-2\min_i a_i\le k/4.
$$

These conditions imply $\max_i a_i\le k/4$. Balanced good triples with all
$a_i\le k/4$ are covered.

No proof was found forcing a suitable triple in every hypothetical
high-transversal family.

### 5.2 A rigorous obstruction to nonadaptive completion

For $8\mid k$, consider $a_i=3k/8$ and $|S_i|=k/4$. Four sets of size at
most $3k/4$ cannot collectively contain all candidate pairs.

Label a point $v$ by $L(v)\subseteq[4]$, the sets containing it. Every label
is nonempty and labels across candidate-pair adjacencies must intersect. A point
of $X_i$ cannot have a singleton label: its bin would contain both other pair
atoms, already totaling $3k/4$, plus that point. Thus pair-atom labels have
size at least two. Singleton-atom labels have size at least one. Total incidence
is at least

$$
 2(9k/8)+3k/4=3k,
$$

exactly the four-bin capacity. Hence pair labels all have size two and singleton
labels all have size one.

A singleton label on $S_i$ must meet every pair label on $X_i$, so all
labels within $X_i$ share a coordinate. Across distinct pair atoms the labels
also intersect. The union of all pair labels is therefore an intersecting edge
family on four coordinates, hence contained in a star or triangle. A star puts
all $9k/8$ pair points in one bin. A triangle confines all incidences,
including singleton labels, to three bins of total capacity $9k/4<3k$. Both
are impossible.

This refutes this nonadaptive method for some triples; it is not a
counterexample to the original conjecture.

### 5.3 Numerical evidence

The mixed-integer program was preserved as good_triple_cover.py. It distributes
each atom's mass among the fifteen nonempty subsets of four bin labels, forbids
disjoint labels across candidate-pair adjacencies using support binaries, and
minimizes maximum bin mass. Isolated singleton atoms next to empty pair atoms
are discarded.

SciPy/HiGHS reported the following normalized optima:

| Pair-atom masses | Reported optimum |
|---|---:|
| $(3/8,3/8,3/8)$ | $33/40$ |
| $(1/4,1/2,1/2)$ | $7/8$ |
| $(0,1/2,1/2)$ | $9/10$ |
| $(1/4,1/4,1/2)$ | $6/7$ |

These are not independently certified exact optima. For the first row the upper
value is explicitly attainable: assign $11k/40$ of each $X_i$ label
$\{0,i\}$, its remaining $k/10$ label $\{1,2,3\}$, and all $k/4$ of
$S_i$ label $\{i\}$. Every bin has mass $33k/40$. The proved lower
assertion is only that $3k/4$ cannot work.

The easy selection of a pair of edges intersecting in at most $k/4$, followed
by a third edge avoiding their intersection and selected portions of both, did
not force the successful region of (5.2). The computations suggested further
obstructions; they do not rule out adaptive methods.

### 5.4 Rectangle formulation of the disjoint-edge branch

For disjoint $k$-edges $A,B$, an additional edge $C$ misses the pairs in

$$
 R_C=(A\setminus C)\times(B\setminus C).
$$

Its side sizes sum to at least $k$. The local condition implies that no five
available rectangles cover $A\times B$. If $\tau(H)>T$, every rectangle
$X\times Y$ with $X\subseteq A$, $Y\subseteq B$, and $|X|+|Y|\le T$ is
contained in some $R_C$, by choosing an edge avoiding $X\cup Y$.

It was not proved that these properties are incompatible when
$T>(3/4+\varepsilon)k$. Even such a result would handle only this branch.

## 6. Failed lower constructions and amplification

### 6.1 Basic operations

Full vertex cloning multiplies rank but leaves $\tau$ unchanged. Disjoint
unions add $\tau$ but generally destroy locality. Taking all unions of one
edge from each disjoint factor gives the minimum of the factors' transversal
numbers, not their sum.

Substitution by an inner family $G$ multiplies rank and transversal number: a
set covers the substituted family exactly when the base vertices whose fibers it
fully covers form a base transversal. Lifting local witnesses is guaranteed if
$G$ is $r$-wise intersecting. But then

$$
 \tau(G)\le\left\lceil\frac{\operatorname{rank}(G)}{r-1}\right\rceil,
$$

so growing inner fibers lose roughly a factor $r-1$ in the ratio. No
ratio-preserving scaling was obtained.

### 6.2 An operation with additive transversal number but failed locality

Take three disjoint parity examples with parameter $a\ge10$, each on $7a+1$
points. Let $\mathcal H$ be all $12a$-sets containing a good $4a$-edge in
at least one block. Then

$$
 \tau(\mathcal H)=9a+3.
$$

Each block has independence number $4a$. A set of size at least $12a$ is
independent in $\mathcal H$ precisely when each of its block intersections
contains no good base edge. Thus $\alpha(\mathcal H)=12a$ on $21a+3$ points.

However, it fails $P_7$. Form seven groups of $3a$ points, split each
equally among the three blocks, and add one isolated point per block. The seven
Fano-line complements give seven global $12a$-sets $A_i$, each containing
$4a$ points in every block, with transversal number three.

Choose the prescribed $X$'s of size $4a$ so that every $A_i$ is good in
some block. Let $M$ be the binary incidence matrix of the seven Fano
complements. Its column space is the dimension-three simplex code. Choose three
independent columns; their supports cover all seven row positions. For a chosen
column $Me_j$, prescribe the parities of the seven group intersection counts
of $X$ to be $\mathbf1+e_j$. Since $M\mathbf1=0$, this produces that
column. Six counts are odd and one even. Counts between $0$ and $a$,
totaling $4a$, exist by starting with six ones and increasing by twos; for
$a\ge10$ their maximum available even total exceeds $4a$.

Every $A_i$ consequently contains a good base edge in at least one block and
belongs to $\mathcal H$. But any two group points lie on some Fano line, whose
complement avoids both; isolated points do not help. Thus the desired additive
ratio comes with a false local hypothesis.

### 6.3 Affine binary codes: a proved sufficient condition

Consider the weight-$k$ words of an affine coset
$b+C\subseteq\mathbb F_2^n$, with minimum coset weight $d$, and assume
$n<2k$. In a bad seven-tuple all point degrees are at most four. Let

$$
 D=4n-7k.
$$

The XOR of all seven words belongs to $b+C$. Its weight is the number of
odd-degree points and is at most $D$: degree three costs deficiency one and
degree one costs deficiency three. Therefore

$$
 d>D
$$

is sufficient for $P_7$.

The global transversal lower bound was not established. With
$n=(7/4+\delta)k$, the criterion requires $d>4\delta k$. A random
parity-check construction using a union bound to exclude small coset vectors
asks for redundancy approximately

$$
 nH_2(d/n)\sim4\delta k\log_2(1/\delta).
$$

After deleting $(3/4+\varepsilon)k$ points, only

$$
 \binom{(1+\delta-\varepsilon)k}{k}
 =2^{(\delta-\varepsilon)k\log_2(1/(\delta-\varepsilon))+O(\delta k)}
$$

candidate words remain. These estimates do not make the random-coset approach
work. They do not prove that structured codes are impossible.

### 6.4 Conditional stronger Fano calculation and covering loss

Assume additionally that degree-four spectra are the seven Fano complements and
all seven types occur. This classification was not extended to arbitrary linear
$D$.

XOR the three edge rows indexed by each Fano line. All standard points cancel,
and each of the seven XORs belongs to $b+C$, so has weight at least $d$. An
exceptional degree-three spectrum cannot itself be a Fano line, since the
complementary standard point would give a two-point cover. A spectrum of size
$0,1,2,$ or a nonline $3$ contributes respectively $0,3,4,3$ occurrences
across the seven line XORs. These are at most three times its deficiency.
Therefore

$$
 7d\le3D.
$$

Conditionally this would prohibit bad tuples for $n<7k/4+7d/12$. The
structural assumption is an unresolved requirement, not a proved lemma in this
range.

There is also a precise conditional covering obstruction. If $C$ has a word
$W$ of weight $k+d-1$, then $W$ contains no weight-$k$ word of $b+C$:
deleting such a word would leave a coset word of weight $d-1$. Hence

$$
 \tau(H)\le n-k-d+1.
$$

The possible gain $7d/12$ is less than the potential loss $d-1$. Existence
of $W$ at that exact weight is not universal or proved here, so this is a
barrier, not an impossibility theorem.

### 6.5 Graph encoding

Let $G$ have no odd cycle of length at most seven, and let $\mathcal I$ be
its maximal independent sets. Define

$$
 A_v=\{I\in\mathcal I:v\in I\}.
$$

Any seven graph vertices induce a bipartite graph; extend its two color classes
to maximal independent sets. These cover the corresponding $A_v$'s, so the set
family has $P_7$. Also

$$
 \tau(\{A_v\})=\chi(G),
$$

because covering vertices by independent sets is equivalent to coloring. Private
padding gives uniformity

$$
 k=\max_v|\{I\in\mathcal I:v\in I\}|.
$$

No graph sequence with the necessary asymptotic ratio $\chi(G)/k>3/4$ was
found. The construction verifies its parameters but supplies no counterexample.

Other sparse, projective-incidence, and random-alteration ideas did not
establish the required ratio. No unverified numerical or probabilistic estimate
is asserted here as a lower-bound theorem.

## 7. Criticality and the convergence question

### 7.1 Critical certificates are finite but not small enough

An edge-minimal family with transversal number $u$ has, for every edge
$E_i$, a certificate $T_i$ of size $u-1$ disjoint from $E_i$ and meeting
all other edges. The checked Tuza passages imply

$$
 |E(H)|\le\binom{k+u-1}{k},\qquad
 |V(H)|<\binom{k+u}{k},
$$

for a $k$-uniform critical family with isolated vertices omitted. For
$u=\Theta(k)$, these bounds are exponential. They do not supply a bounded
template or asymptotic coefficient. The ISP completion constructions were not
shown to preserve $P_r$.

### 7.2 Splitting demand does not split rank

If $T$ is a minimum transversal and $S\subseteq T$, let

$$
 H_S=\{E\in H:E\cap T\subseteq S\}.
$$

Then $\tau(H_S)=|S|$: $S$ covers it, while a smaller cover together with
$T\setminus S$ would contradict minimality of $T$. Its edge ranks need not
shrink.

A ground partition in which every $(k+\ell)$-edge has at most $k$ points on
one side and at most $\ell$ on the other would force an exact split on every
edge; complete uniform families already obstruct such partitions. Taking
arbitrary traces can also lose local covering points. These ideas did not prove
upper subadditivity.

### 7.3 Sufficient inequalities that remain unproved

For fixed $r$, an estimate

$$
 f(mk,r)\ge m(f(k,r)-C_r)
$$

with $C_r$ independent of $m,k$ would prove convergence. For fixed $k$,
take $m=\lfloor n/k\rfloor$ and use monotonicity to obtain

$$
 \liminf_{n\to\infty}\frac{f(n,r)}n
 \ge\frac{f(k,r)-C_r}{k}.
$$

Let $k$ approach a sequence realizing the limsup. No valid construction
establishing this inequality was found.

Similarly, an upper inequality

$$
 f(k+\ell,r)\le f(k,r)+f(\ell,r)+O_r(1)
$$

would allow subadditivity after adding a constant. It was not proved. Fekete's
lemma therefore cannot simply be invoked.

Normalized compactness did not repair the issue. Local two-point witnesses can
have normalized mass tending to zero; deleting them can destroy the local
condition while normalized transversal numbers stay nonzero. No quantitative
approximation theorem overcoming this was established.

## 8. Remaining uncertainties

The substantive gaps are:

1. An upper bound $3k/4+o(k)$ for every $P_7$ family, or a verified family
   with $(3/4+\varepsilon)k$ transversal number for fixed positive
   $\varepsilon$.
2. A proof or disproof of convergence of $f(k,r)/k$ for every fixed $r$.
3. A legitimate scaling or upper-subadditivity operation, rather than one that
   changes the local hypothesis.
4. A local-property-preserving structural reduction using the bounded fractional
   interval.
5. A way around the demonstrated nonadaptive good-triple obstruction, perhaps
   adaptive avoidance sets.
6. For the code approach, both the necessary robust Fano classification and a
   global transversal lower bound that pays less than the available slack.

The finite additive parity improvement, the complete-family limit, the
fractional reduction, solver-reported optima, and conditional coding
calculations do not answer either original assertion.
