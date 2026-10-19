---
name: research/leads/number_field_rare_distances
title: Number fields and rare planar distances
desc: |
  Gives a linear rare-distance bound under coordinate separation, realizes it
  over number fields, and isolates the deformation and conjugate-diameter
  obstructions to extending the argument to arbitrary planar sets.
problems:
- 132
research_state: candidate
review_status: unreviewed
created: 2026-09-22T20:37:22Z
updated: 2026-10-19T04:19:07Z
---

# Number fields and rare planar distances

[[research/leads/_index|..]]

[[research/leads/number_field_rare_distances/evidence/_index|evidence/]]: Exact distance spectra for all nonempty subsets of a four-by-four grid
after two algebraic maps, and a seven-point example with a rich distance.

***

This lead's notes that cite no source are author-recorded research, not claims.

## Target and standing

For a finite set $A\subset\mathbb R^2$, let $n=|A|$, let $m_A(r)$ count
unordered pairs at distance $r>0$, and put

$$
R(A)=\#\{r>0:1\le m_A(r)\le n\}.
$$

The intended questions of [[problems/distance_problems/E0132/_index|Problem 132]]
are whether $R(A)\ge2$ for every $n\ge5$, and whether the minimum of $R(A)$
over all $n$-point sets tends to infinity. The restriction $n\ge5$ is needed
for the first question: two unit equilateral triangles sharing an edge give
a four-point set with five unit pairs and one diametral pair.

This is an author-recorded research sketch, without independent mathematical
review or a novelty claim. The number-field reduction does not solve either
question. The initial approach separates coefficients of squared distances;
the other approach transports whole distance classes through real embeddings.
The outstanding issue is a bound that holds without choosing a favorable
coordinate pattern or field embedding.

## Proof sketch

1. Encode the equalities and inequalities between squared pair distances as
   a finite polynomial system over $\mathbb Q$. Real-closed-field transfer
   realizes the same pattern over the real algebraic numbers. Its finitely
   many coordinates generate a number field. This preserves multiplicities,
   but supplies no useful field-degree or coefficient-independence bound.
2. For a real number field $F$ and a real algebraic $s$ with $s^2\notin F$,
   consider finite subsets of $F\times sF$. Equality of squared distances
   separates the horizontal and vertical squared differences. A geometric
   count of long horizontal displacements produces linearly many rare
   classes even though some other classes can exceed $n$.
3. For coordinates in a number field, each real embedding gives a planar
   realization with exactly the same multiplicity classes. A class that is a
   diameter in any such realization has multiplicity at most $n$. Distinct
   conjugate diameters would therefore give distinct rare classes.
4. Neither coordinate separation nor distinct conjugate diameters is known
   here for arbitrary configurations. Generic deformation can split distance
   classes, so its rare classes cannot simply be transported back to the
   original metric.

The coordinate-separation argument below is complete as an author-recorded
argument. The last step to arbitrary configurations remains open. The
[[problems/distance_problems/E0132/_index#current-assessment|problem assessment]]
records the literature search; this note claims no improvement to the
unrestricted problem's standing.

## A linear bound when distances separate the coordinates

Suppose a finite planar set $A$ has the following property: whenever two
pairs have the same Euclidean distance, their absolute horizontal
displacements agree and their absolute vertical displacements agree. Then

$$
R(A)\ge\left\lceil\frac{n-1}{4}\right\rceil. \tag{1}
$$

This condition permits repeated distances in two reflected directions; it
does not require that every distance already have multiplicity at most $n$.

Here is a proof. The cases $n\le1$ are immediate. If all points lie on one
vertical line, every distance
graph is a disjoint union of paths, so each multiplicity is at most $n-1$.
The distances from the lowest point supply at least $n-1$ distinct values.
Assume otherwise that the horizontal range is $[a,b]$, with $W=b-a>0$.
Choose points $p_L,p_R$ on the leftmost and rightmost vertical lines, and
let $t$ be the number of points on the vertical midline $x=(a+b)/2$.

First consider any occurring distance with absolute horizontal displacement
$u>W/2$. Every edge of its distance graph has horizontal displacement $u$,
by the separation assumption. A vertex cannot have neighbors on both its
left and its right: those neighbors would be horizontally $2u>W$ apart.
On its one possible side, it has at most two neighbors, since the absolute
vertical displacement is fixed. The graph has maximum degree at most two,
and hence at most $n$ edges. This distance is rare in the required sense.

For every point right of the midline, take its distance to $p_L$; for every
point left of it, take its distance to $p_R$. These $n-t$ assignments all
have horizontal displacement greater than $W/2$. A particular resulting
distance can be assigned by at most two points at each anchor, hence by at
most four points altogether. This supplies at least

$$
\left\lceil\frac{n-t}{4}\right\rceil
$$

rare distances. If $t\ge1$, the $t$ midline points supply at least $t-1$
further distances, using distances from the lowest one. Their entire
distance graphs are vertical by coordinate separation and are unions of
paths. They therefore have multiplicity at most $n-1$. They are distinct
from the preceding distances, whose horizontal displacement is positive.
Thus, including the case $t=0$,

$$
R(A)\ge
\left\lceil\frac{n-t}{4}\right\rceil+\max\{t-1,0\}.
$$

For $t=0$ this is at least $\lceil n/4\rceil$. For $t\ge1$, four times the
right-hand side is at least $n-t+4(t-1)=n+3t-4\ge n-1$. This proves (1).
The proof uses neither a grid shape nor a bound on the coordinate size.

### Number-field realization

Let $F\subset\mathbb R$ be a number field, and let $s$ be real algebraic
with $s^2\notin F$. Every finite subset of

$$
F\times sF
$$

satisfies the separation condition. Indeed, equality of two squared
distances has the form

$$
u^2+s^2v^2=u'^2+s^2v'^2,\qquad u,v,u',v'\in F.
$$

Linear independence of $1,s^2$ over $F$ gives $u^2=u'^2$ and $v^2=v'^2$,
which is exactly the required equality of absolute coordinate
displacements. Consequently (1) holds uniformly in $F$, $s$, and the
finite subset. Taking $F=\mathbb Q$ and $s=1+\sqrt2$ gives the concrete
family discussed in the question. For any number field $F$, a positive
rational prime $p$ with $\sqrt p\notin F$ gives another choice
$s=1+\sqrt p$; only finitely many quadratic fields can be subfields of $F$.

This proves the growth assertion on this restricted family. Bound (1)
also gives two rare distances for $n\ge6$; it alone gives only one for
$n=5$. This is not a solution for arbitrary planar sets.

The condition does not force all distances to be rare. For $s=1+\sqrt2$,
take the images of the seven integer points

$$
(0,0),(0,2),(1,1),(1,3),(2,0),(2,2),(3,1)
$$

under $(x,y)\mapsto(x,sy)$. Their squared-distance multiplicities, written
as pairs $(c,d)$ for $c+d\sqrt2$, are

| Squared distance | Multiplicity |
| --- | ---: |
| $4$ | 3 |
| $4+2\sqrt2$ | 8 |
| $12+2\sqrt2$ | 2 |
| $12+8\sqrt2$ | 3 |
| $16+8\sqrt2$ | 3 |
| $28+18\sqrt2$ | 2 |

Thus one distance occurs more than $n=7$ times, while five are rare.

## Stronger separation by an algebraic shear

There is a simpler construction if all distance classes may be changed.
Let $F\subset\mathbb R$ be a number field. Choose positive rational
$a,b$ such that $[F(\sqrt a,\sqrt b):F]=4$, and map a finite
$S\subset F^2$ by

$$
T(x,y)=(x+\sqrt a\,y,(1+\sqrt b)y).
$$

Such choices exist: take $\sqrt a\notin F$ and then
$\sqrt b\notin F(\sqrt a)$, using the finiteness of the quadratic
subfields of each finite extension. The map is invertible over $\mathbb R$.
The squared length of an image displacement is

$$
q(x,y)=x^2+(a+b+1)y^2+2\sqrt a\,xy+2\sqrt b\,y^2.
$$

The elements $1,\sqrt a,\sqrt b$ are linearly independent over $F$.
Consequently $q(x,y)=q(x',y')$ forces equality of $y^2$, $xy$, and $x^2$.
If $y\ne0$, this gives $(x',y')=\pm(x,y)$ with a common sign; if $y=0$,
the same conclusion follows from $y'=0$ and $x'^2=x^2$.

Each distance graph on $T(S)$ therefore consists of edges with one fixed
displacement up to sign. Its components are finite paths, so every
multiplicity is at most $n-1$. Choose a linear functional taking distinct
values on $S$, and a point where it is minimal. The $n-1$ displacements
from that point cannot be equal or opposite, so their image lengths are
distinct. Hence $R(T(S))\ge n-1$.

For $F=\mathbb Q$ one may use $a=2,b=3$. This is an explicit construction
over $\mathbb Q(\sqrt2,\sqrt3)$, with no increasing-degree tower.

### Why this deformation does not prove the original statement

The map can split an original distance class into many smaller classes.
The inverse map can merge all those rare classes again. Real-closed-field
transfer preserves the pattern; a generic algebraic shear does not.

Even preserving all distance equalities under an affine map can prohibit
the required freedom. If the original set contains a unit square and the
linear part of the map is $T$, put $M=T^{\mathsf T}T$. Equality of its
horizontal and vertical sides forces $M_{11}=M_{22}$. Equality of its two
diagonals forces $M_{12}=0$. Thus $M=cI$: every invertible affine map
preserving these equalities is a similarity and leaves the multiplicity
pattern unchanged. This obstruction already occurs in rational
configurations of arbitrarily large size containing a square.

There is a useful limited converse. Suppose a finite configuration admits
an invertible affine map preserving every equality of pair distances and
$T^{\mathsf T}T$ is not a scalar matrix. Diagonalize that real symmetric
matrix in orthonormal coordinates, with distinct eigenvalues $\lambda,\mu$.
For equal-length displacements $(u,v),(u',v')$ we have both

$$
u^2+v^2=u'^2+v'^2,\qquad
\lambda u^2+\mu v^2=\lambda u'^2+\mu v'^2.
$$

Solving gives $u^2=u'^2$, $v^2=v'^2$. The original configuration therefore
satisfies coordinate separation in these rotated axes, and (1) applies to
it. Any counterexample to (1) must consequently have only similarities
among its invertible affine maps preserving all distance equalities.
This is an exact limit of this deformation route, not an obstruction to
every arithmetic approach.

## Conjugate diameters and a uniform obstruction

Let $A\subset F^2$ for a number field $F\subset\mathbb R$. For each real
embedding $\sigma:F\hookrightarrow\mathbb R$, apply $\sigma$ to both
coordinates. The resulting $A^\sigma$ has $n$ distinct points. A squared
distance $q\in F$ becomes $\sigma(q)$, and injectivity of $\sigma$
preserves all equalities and inequalities of values in the sense of
equality versus nonequality. Numerical order need not be preserved.
Therefore corresponding distance classes have identical multiplicities.

Let $q_\sigma$ be the original squared-distance class that becomes the
diameter of $A^\sigma$. The planar diameter bound gives

$$
R(A)\ge\#\{q_\sigma:\sigma:F\hookrightarrow\mathbb R\}. \tag{2}
$$

The same transport permits applying a known planar sufficient condition in
any real embedding, such as the first-two-convex-layers criterion in
Clemen--Dumitrescu--Liu, Theorem 1.3. This use is conditional on that external
source theorem; no independent proof review of it is supplied here.

Increasing the field degree does not make the right-hand side of (2) grow.
For any totally real number field $F$, choose a totally positive primitive
element $\theta$: a sufficiently large rational translate of a primitive
element works. Its distinct conjugates are all positive, so their squares
are distinct and $\mathbb Q(\theta^2)=F$. Given $n\ge3$, choose an integer

$$
C>2(n-2)\max_\sigma\sigma(\theta)
$$

and take

$$
A=\{(-1,0),(1,0)\}\cup
  \{(0,j\theta/C):1\le j\le n-2\}.
$$

In every real embedding, the vertical coordinates lie strictly between
zero and $1/2$. Distances between two vertical points are less than $1/2$;
distances from an endpoint to a vertical point are less than $\sqrt{5/4}$.
Thus the two horizontal endpoints are the unique diameter in every
embedding, and the right-hand side of (2) is one. Nevertheless the squared
distance $1+\theta^2/C^2$ generates $F$. The obstruction is therefore
present for arbitrarily large actual squared-distance fields, not merely
for a field enlarged by irrelevant elements. Totally real fields have
unbounded degree, for example multiquadratic fields.

This construction does not refute Problem 132: it only refutes a proposed
lower bound on the number of conjugate diameter classes based on field
degree and set size alone.

## Exact algebraization and the remaining gap

Label any finite planar configuration by $1,\ldots,n$ and introduce real
variables $x_i,y_i$. Set

$$
Q_{ij}=(x_i-x_j)^2+(y_i-y_j)^2.
$$

Require $Q_{ij}>0$ for every distinct pair of labels. For every two
unordered pairs, require $Q_{ij}=Q_{kl}$ or $Q_{ij}\ne Q_{kl}$ according to
the original configuration. These are finitely many polynomial conditions
over $\mathbb Q$, with a real solution. Tarski's transfer principle gives
a solution over the real algebraic numbers. Its coordinates generate a
finite extension of $\mathbb Q$, and its distance partition, hence $R(A)$,
is exactly the original one. Numerical lengths need not be preserved.

For each fixed $n$, a counterexample to the two-distance assertion would
therefore have an algebraic realization. Likewise, a sequence refuting
the growth assertion could be replaced term by term with algebraic
realizations. A uniform result over all number fields would suffice for
the original questions. This deduction uses the external real-closed-field
transfer theorem, rather than a claim that arbitrary real coordinates
already belong to a number field.

What is missing is a way to derive rare classes from the preserved pattern
without changing it. Algebraization supplies no analog of
$s^2\notin F$ for the two coordinate directions, and the conjugate-diameter
construction shows that field degree alone cannot supply the missing
classes. The surviving arithmetic question is how simultaneous relations
among squared differences constrain their multiplicities in configurations
that admit only similarities as equality-preserving affine maps. No bound
for that remaining class is proved here.

## Finite checks and sources

The [exact finite probe](evidence/main.py) enumerates all 65,535 nonempty
subsets of $\{0,1,2,3\}^2$, applies $(x,y)\mapsto(x,(1+\sqrt2)y)$,
and counts squared distances by their integer coefficient pairs in
$\mathbb Q(\sqrt2)$. It checks (1), the midline-sensitive bound used in its
proof, the separated-displacement conclusion for the biquadratic shear,
and the complete seven-point spectrum above. The finite enumeration checks
the proposed mechanisms on that domain; the general conclusions rely on
the written arguments. It is not an independent review.

Run from the repository root:

```bash
uv run --no-sync python wiki/research/leads/number_field_rare_distances/evidence/main.py
```

Relevant external inputs and their reading scope:

- David Marker, *Model Theory for Algebra and Algebraic Geometry*,
  [lecture notes](https://homepages.math.uic.edu/~marker/orsay.pdf),
  Corollary 7.15: completeness of real closed fields and the elementary
  inclusion of the real algebraic numbers in $\mathbb R$. The statement
  and its short displayed deduction were read in indexed text; direct PDF
  access failed. Its underlying quantifier-elimination proof was not
  reconstructed. The polynomial-system application above is recorded here.
- Clemen, Dumitrescu, and Liu, *On multiplicities of interpoint distances*,
  [arXiv:2505.04283v2](https://arxiv.org/html/2505.04283v2), Section 1.1: the
  $n\ge5$ formulation, the classical diameter bound, and Theorems 1.2 and 1.3
  were read as statements in the HTML source. The
  [[../library/distance_problems/clemen_2025_multiplicities_interpoint_distances/_index|library
  digest]] provides the canonical local source home. No complete proof review of
  those external results is claimed.
- Alon et al., *Remarks on the disproof of the unit distance conjecture*,
  [arXiv:2605.20695v1](https://arxiv.org/html/2605.20695v1), Section 2: its
  norm-one and window construction motivates the arithmetic comparison. The
  [[../library/discrete_geometry/alon_2026_remarks_disproof_unit_distance_conjecture/_index|compiled
  source]] records its proof coverage. Its lower bound for one rich distance is
  not a premise of (1).
- Lee, Pohoata, and Zhu, *The Minkowski grid has robustly many repeated
  distances*, [arXiv:2607.05374v1](https://arxiv.org/abs/2607.05374v1):
  the abstract was screened in the status search. Its robust lower
  bound for a most frequent distance in subsets is a different question;
  no theorem or proof from it is consumed here.
