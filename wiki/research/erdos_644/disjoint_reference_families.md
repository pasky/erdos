---
name: research/erdos_644/disjoint_reference_families
desc: Critical P7 families with disjoint edges attain coefficient five sevenths, while the fixed-disjoint-pair rectangle relaxation admits coefficient four fifths.
tags: [proved, constructions, method-obstruction]
sources: []
created: 2026-09-23T05:25:00Z
updated: 2026-10-14T00:26:52Z
---


# research/erdos_644/disjoint_reference_families

***

These results do not resolve Problem 644. They show both that disjoint reference
edges can coexist with large transversal number, even under edge criticality,
and that their anchored rectangle condition alone cannot prove the three-quarter
bound. Throughout, $P_7$ uses subfamilies of **at most** seven edges.

## A critical disjoint-edge construction with coefficient five sevenths

Fix $r\ge1$ and put $k=7r+1$. Take disjoint sets $X,Y,P,Q$ with

$$
|X|=|Y|=6r,\qquad |P|=|Q|=r+1,
$$

and put $U=X\cup Y$, $A=X\cup P$, $B=Y\cup Q$. Define

$$
\mathcal H=\{A,B\}\cup
\{C\in\tbinom Uk:X\not\subseteq C,\ Y\not\subseteq C\}.
\tag{1}
$$

Then $\mathcal H$ is $k$-uniform, has $P_7$, contains disjoint edges, is
transversal-critical, and satisfies

$$
\boxed{\tau(\mathcal H)=5r,\qquad \tau(\mathcal H)/k\longrightarrow5/7.}
\tag{2}
$$


### The local condition

It suffices to check the larger family obtained by retaining every $k$-subset of
$U$. Each selected base edge has an omission set in $U$ of size $d=5r-1$. For a
point $v\in U$, its omission support is the set of selected base-row indices
missing $v$.

With no reference edge selected, suppose $s\le7$ base edges have no two-cover.
Their omission supports are nonempty and pairwise intersecting. If one has size
at most two, every support meets those at most two indices, so one omission row
has size at least $|U|/2=6r$. Otherwise total omission incidence is at least
$3|U|=36r$, and one of the at most seven rows has size at least $36r/7$. Both
conclusions contradict $d=5r-1$.

With just $A$ selected, there are $s\le6$ base edges. If no two-cover exists,
the omission support of every $X$-point meets that of every base point. In
particular all supports are nonempty. An $X$-support of size at most two forces
some row load at least $|U|/2=6r$. A singleton $Y$-support forces its coordinate
to contain every $X$-point, again giving load at least $6r$. In the remaining
case, $X$-supports have size at least three and $Y$-supports have size at least
two. Total omission incidence is at least

$$
3|X|+2|Y|=30r,
$$

so one of the at most six rows has load at least $5r>d$. Thus a cover exists.
The argument for just $B$ is symmetric. If there are no base rows, the reference
itself has a one-point cover.

With both $A,B$ selected, use candidate pairs in $X\times Y$. Each of the at
most five base edges excludes a rectangle containing at most $d^2/4$ such pairs.
Their union contains fewer than

$$
\frac{5(5r)^2}{4}<36r^2=|X\times Y|
$$

pairs. A remaining pair covers the entire selection. This proves $P_7$.

The six-row split-ground incidence bound is sharp as a covering statement. Index
six coordinates by $E(K_4)$. Distribute $X$ equally among the four star supports
and $Y$ equally among the three perfect-matching supports. Every star meets
every star and every perfect matching. When $|X|=|Y|=m$, every coordinate has
omission load $m/2+m/3=5m/6$. Divisibility can be imposed for an exact finite
realization.

### Transversal number

Any $5r$-subset of $U$ meeting both halves covers (1), since its complement has
size $k-1$.

Conversely, let $T$ have size at most $5r-1$. If $T\subseteq U$ and misses a
half, it misses the corresponding reference. Otherwise its base part
$T_0=T\cap U$ has one of the following properties. If $T=T_0$ meets both halves,
any $k$-subset of $U\setminus T_0$ contains neither whole half and is a retained
edge. If $T$ uses a private point, then $|T_0|\le5r-2$, and $U\setminus T_0$ has
at least $k+1$ points. Both halves have at least $r+2$ remaining points. If
$T_0$ meets both halves, any surviving $k$-subset works. If it misses exactly
one half, omit one extra point from that half before choosing a $k$-subset. If
$T_0$ is empty, omit one point from each half; the remaining $12r-2\ge7r+1=k$
points still suffice. In every case a retained base edge avoids $T$. This proves
(2).

### Criticality

For a retained base edge $C$, its complement $U\setminus C$ has size $5r-1$,
meets both halves, and covers every other edge. For $A$, any $(5r-1)$-subset of
$Y$ covers $B$ and every retained base edge: its unique disjoint base $k$-set
contains $X$ and was omitted from (1). It misses $A$. The symmetric construction
applies to $B$. Thus deleting any edge decreases the transversal number by one.

This construction excludes, for example, an unrestricted $k/2+o(k)$ upper bound
based only on disjointness and transversal-criticality. It does not exceed
$3k/4$.

## The fixed-disjoint-pair relaxation admits coefficient four fifths

Fix $r\ge1$, put $k=10r$, take $|X|=|Y|=9r$, and include all $k$-subsets of
$U=X\cup Y$. Adjoin disjoint references

$$
A=X\cup P,\qquad B=Y\cup Q,
\qquad |P|=|Q|=r,
$$

where $P,Q$ are private and disjoint. The resulting family $\mathcal F$ has

$$
\tau(\mathcal F)=8r+1.
\tag{3}
$$

The complete base family gives the lower bound; a base transversal of size
$8r+1$ meeting both halves also covers the references.

Nevertheless, $A,B$ together with **any five further edges** have a two-cover. A
base edge omits $8r$ base points, and hence excludes a rectangle of area at most
$16r^2$ in $X\times Y$. Five such rectangles cannot cover its $81r^2$ candidate
pairs. This also handles selections of fewer than five further edges.

Thus the rank bound, global transversal number, and five-rectangle prohibition
anchored at one fixed disjoint pair do not imply a three-quarter transversal
bound. This answers, in the negative, the suggestion left open in
[Certificates and obstructions](certificates_and_obstructions.md#rectangles-from-two-disjoint-reference-edges).

This is not a $P_7$ counterexample. For even $r$, the complete base family
already contains seven Fano-cap blowups: take seven disjoint classes of size
$5r/2$ inside $U$, and one row for each cap. Each row has size $10r$, and no
pair of points covers all seven rows.
