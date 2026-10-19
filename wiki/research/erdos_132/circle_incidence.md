---
name: research/erdos_132/circle_incidence
title: Rare distances from an arbitrary positive-fraction circular subset
desc: |
  Translated cosine-curve incidences and additive covering give linear
  rarity from any fixed positive fraction of concyclic points.
sources: []
research_state: closed
created: 2026-09-22T22:45:00Z
updated: 2026-09-24T22:12:56Z
---


# Rare distances from an arbitrary positive-fraction circular subset

***

## Statement and scope

For a finite planar set $A$, write $n=|A|$, let $q(A)$ be the number of distinct
positive distances, and let

$$
R(A)=\#\{r>0:1\le m_A(r)\le n\},
$$

where $m_A(r)$ counts unordered pairs. The argument below proves:

**Theorem.** Fix $0<c\le1$. There is a constant $C_c$ such that, whenever
$A\subset\mathbb R^2$ has $n$ points and contains $m\ge cn$ points on one
circle,

$$
R(A)\ge \frac{m-1}{2}-C_c n^{2/3}.
\tag{1}
$$

More precisely, if $q(A)\le n$, then

$$
R(A)\ge q(A)-C_c n^{2/3}.
\tag{2}
$$

No regularity of the circular subset and no restriction on the remaining points
is assumed. Thus any fixed positive circular fraction gives linearly many rare
distances for sufficiently large $n$.

This does not solve the unrestricted problem: a hypothetical bounded-rarity
family is not yet known to contain a positive-fraction circular subset. The
theorem removes the previous circular-majority or regular-polygon assumptions,
not this remaining structural gap.

## 1. An incidence bound for translated cosine curves

Write $\mathbb T=\mathbb R/(2\pi\mathbb Z)$. Fix $a>0$, $b\in\mathbb R$, with

$$
(a,b)\ne(1,0),
$$

and consider the translates

$$
\Gamma_{u,v}=\{(x,y)\in\mathbb T^2:
\cos(y-v)=a\cos(x-u)+b\}.
\tag{3}
$$

All constants in this section are absolute and uniform in $a,b$.
If the base real curve is empty or consists of a single point, the
incidence and overlap bounds below hold directly. In the remaining
case it has a nontrivial real arc, so coincident real curves have
coincident complex algebraic closures.

### Algebraic irreducibility and coincidence

Put $X=e^{ix}$, $Y=e^{iy}$. Multiplication of the unshifted equation by $2XY$
gives

$$
F(X,Y)=X(Y^2+1)-aY(X^2+1)-2bXY.
\tag{4}
$$

As a quadratic in $Y$, its discriminant is

$$
[aX^2+2(b-1)X+a]\,[aX^2+2(b+1)X+a].
\tag{5}
$$

The two quadratic factors are coprime: their difference is $4X$, and their
constant terms are the nonzero number $a$. Consequently their product is a
square in $\mathbb C(X)$ only if both quadratics are squares. This requires

$$
(b-1)^2=a^2=(b+1)^2,
$$

which forces $b=0$, $a^2=1$, and hence $a=1$. Thus (4) is irreducible over
$\mathbb C(X)$ as a polynomial in $Y$; it is primitive over $\mathbb C[X]$, so
it is irreducible in $\mathbb C[X,Y]$. Translating angles rescales $X,Y$ by
nonzero constants and preserves irreducibility.

Two distinct translated complex curves therefore have at most nine
intersections, by the ordinary degree-three Bézout bound. Only a fixed constant
matters here.

To identify coincident translates, compare Laurent coefficients in

$$
\frac12e^{-iv}Y+\frac12e^{iv}Y^{-1}
-\frac a2e^{-iu}X-\frac a2e^{iu}X^{-1}-b.
$$

Proportionality of the coefficients of $X,X^{-1}$ forces the proportionality
constant to be $1$ or $-1$; the same holds from $Y,Y^{-1}$. If $b\ne0$, the
constant must be $1$, so the parameters agree. If $b=0$, there is exactly the
further possibility

$$
(u',v')=(u+\pi,v+\pi).
\tag{6}
$$

Thus any family indexed by distinct parameter pairs has curve-coincidence
multiplicity at most two.

The same calculation supplies the two-degrees-of-freedom condition. For a fixed
point $(x,y)$, the parameters of curves through it satisfy

$$
\cos(v-y)=a\cos(u-x)+b,
$$

which is another translate of the same curve, now in the parameter torus. Two
different points give distinct parameter curves except when $b=0$ and the points
differ by $(\pi,\pi)$. In the absence of this antipodal exception, at most nine
distinct curves pass through two points.

### Incidence estimate

Let $P\subset\mathbb T^2$ be finite and let $\mathcal C$ be a set of distinct
curves (3). In the case $b=0$, suppose initially that $P$ contains no pair
differing by $(\pi,\pi)$. Then

$$
I(P,\mathcal C)
\le C\bigl(|P|^{2/3}|\mathcal C|^{2/3}+|P|+|\mathcal C|\bigr).
\tag{7}
$$

Here are sufficient details to reduce (7) to the elementary planar crossing
lemma. Cut each angular coordinate at a value avoided by all points of $P$, and
work in the resulting open rectangle. Each curve meets each cut at at most two
points. It has only $O(1)$ singularities or vertical turning points: away from
them it is one of the two graphs

$$
y=v\pm\arccos(a\cos(x-u)+b),
$$

and the endpoints of their domains occur among the at most four solutions of
$a\cos(x-u)+b=\pm1$. Hence a curve splits into $O(1)$ simple arcs and isolated
points; discarded cut, singular, or isolated-point incidences contribute
$O(|\mathcal C|)$.

Join consecutive points of $P$ along every such arc. This draws a multigraph
with at least $I(P,\mathcal C)-O(|\mathcal C|)$ edges. Edge multiplicity is
bounded by an absolute constant because two points lie on at most nine curves,
and a curve has only $O(1)$ arcs. Different curves have at most nine
intersections, so the drawing has $O(|\mathcal C|^2)$ crossings. Passing to a
simple subgraph loses only a constant factor. The crossing lemma then gives (7).

For completeness, the required form of the crossing lemma follows from
$e\le3v+\operatorname{cr}$ and random vertex sampling. If a simple drawn graph
has $e\ge4v$, sample every vertex with probability $p=4v/e$. Taking expectations
gives $p^2e\le3pv+p^4\operatorname{cr}$, hence
$\operatorname{cr}\ge e^3/(64v^2)$. Adjacent-edge crossings can first be
removed, as in the standard proof. This proves the asserted estimate.
Equivalently, (7) is the $k=2$ case of the standard Pach--Sharir bounded-degree
curve-incidence theorem.

When $b=0$ and antipodal pairs are present, retain one point from each
equivalence class modulo $(\pi,\pi)$. Every curve is invariant under this shift,
so the retained point set has at least half the original incidences. Applying
(7) to it proves the same bound for all $P$, with a different absolute constant.
Alternatively partition $P$ into two half-open $x$-semicircles and apply the
non-antipodal case to each.

A primary source for the general incidence theorem is the original Pach--Sharir
paper, *On the Number of Incidences Between Points and Curves*, Combinatorics,
Probability and Computing 7 (1998), 121--127. A checked precise restatement is
Theorem 2.1 of Pach--de Zeeuw, *Distinct distances on algebraic curves in the
plane*,
[full paper](https://math.nyu.edu/~pach/publications/DistancesOnCurves101113.pdf).
The proof above uses only the elementary two-degrees-of-freedom case.

## 2. Small-difference-set cosine overlap

**Lemma.** Let $U,V\subset\mathbb T$ be finite nonempty sets, with

$$
u=|U|,\quad v=|V|,\quad d_U=|U-U|,\quad d_V=|V-V|.
$$

For $a>0$, $(a,b)\ne(1,0)$, put

$$
E=\#\{(x,y)\in U\times V:\cos y=a\cos x+b\}.
$$

Then

$$
E\le C\left(
\frac{(d_Ud_V)^{2/3}}{(uv)^{1/3}}
+\frac{d_Ud_V}{uv}+1\right).
\tag{8}
$$


**Proof.** Take the point set $P=(U-U)\times(V-V)$. For every
$(s,t)\in U\times V$, use the curve

$$
\cos(y+t)=a\cos(x+s)+b.
$$

Every solution $(x_0,y_0)$ counted by $E$, together with each $(s,t)$, yields
the incidence of $(x_0-s,y_0-t)\in P$ with that curve. A fixed incidence with a
distinct curve comes from at most two parameter pairs, by (6); for each
parameter pair it determines the original solution uniquely. Thus the number of
incidences with distinct curves is at least $Euv/2$. There are at most $uv$
distinct curves. Apply (7), including its antipodal extension, and divide by
$uv/2$. This proves (8). $\square$

In particular, if $U,V$ are translates of one $m$-element set $B$ with

$$
|B-B|\le Km,
$$

then

$$
E\le C\bigl(K^{4/3}m^{2/3}+K^2+1\bigr).
\tag{9}
$$

The same bound holds for phase-shifted cosines, because translating $U,V$ does
not change their sizes or difference-set sizes.

## 3. Few distances and one large circle force finitely many concentric circles

We may take all points of $A$ on the chosen circle as the anchor, increasing $m$
if necessary; proving (1) for this larger $m$ also proves the stated bound.
Assume henceforth that $q=q(A)\le n$, and take the circle containing $m\ge cn$
points as the circle of radius $R>0$ centered at the origin. Write its angular
set as $B\subset\mathbb T$, $|B|=m$, and let $D_0$ be the set of occurring
squared distances with zero adjoined, so $|D_0|=q+1\le n+1$.

Since the chord-squared map $\theta\mapsto2R^2-2R^2\cos\theta$ is at most
two-to-one,

$$
|B-B|\le2(q+1)\le K m,
\tag{10}
$$

where one may fix $K=4/c$.

For any noncentral point $p=\rho e^{i\phi}\in A$, define its pinned
squared-distance spectrum on the anchor circle by

$$
S_p=\{R^2+\rho^2-2R\rho\cos(\theta-\phi):\theta\in B\}.
$$

It is contained in $D_0$, and $|S_p|\ge m/2$. This remains valid if $p$ itself
is on the circle, because zero was adjoined.

If $p'=\sigma e^{i\psi}$ has $\rho\ne\sigma$, equality of one value in
$S_p,S_{p'}$ gives

$$
\cos(\eta-\psi)=\frac\rho\sigma\cos(\theta-\phi)
+\frac{\sigma^2-\rho^2}{2R\sigma}.
\tag{11}
$$

The coefficient $a=\rho/\sigma$ is positive and different from one. Lemma (9),
with phase-shifted copies of $B$, therefore gives

$$
|S_p\cap S_{p'}|\le C_c(m^{2/3}+1).
\tag{12}
$$

This bounds intersection cardinality because each common squared-distance value
gives at least one pair counted by the lemma.

Choose $L=\lceil4/c\rceil$. If $A$ occupied $L$ distinct positive radii about
the origin, choose one point at each radius. By the elementary union lower bound
and (12),

$$
q+1\ge\left|\bigcup_{j=1}^L S_{p_j}\right|
\ge\frac{Lm}{2}-C_c\binom L2(m^{2/3}+1)
\ge2n-O_c(n^{2/3}),
$$

contrary to $q+1\le n+1$, for sufficiently large $n$. Thus $A\setminus\{0\}$
lies on $k=O_c(1)$ concentric circles. Denote their pairwise distinct positive
radii by

$$
R_1,\dots,R_k,
$$

and their nonempty angular sets by $B_1,\dots,B_k$. Take $B_1=B$, $R_1=R$.

## 4. One common angular set with bounded doubling

For every $i$, the distance formula between radius $R_i$ and the anchor radius
$R$ gives

$$
|B_i-B|\le2(q+1)\le Km.
\tag{13}
$$

This is valid even when $i=1$, again including zero in $D_0$.

An elementary form of Ruzsa's covering lemma supplies $X_i\subset B_i$,
$|X_i|\le K$, such that

$$
B_i\subset X_i+(B-B).
\tag{14}
$$

Indeed, choose a maximal family of disjoint translates $x-B$, with $x\in B_i$.
Their union lies in $B_i-B$, so there are at most $K$ of them. Every other
translate $b-B$ meets one of the chosen translates; consequently $b\in x+(B-B)$.

Let $X=\bigcup_iX_i$, so $|X|=O_c(1)$, and define the symmetric angular set

$$
T=X-X+2B-2B.
\tag{15}
$$

Then every difference set $B_i-B_j$ is contained in $T$.

We use the standard Plünnecke--Ruzsa inequality in its two-set form:

$$
|U+V|\le K|U|
\quad\Longrightarrow\quad
|rV-sV|\le K^{r+s}|U|\qquad(r+s>1).
\tag{16}
$$

Apply it to $U=B$, $V=-B$, using (10). We obtain

$$
|2B-2B|\le K^4m,
\qquad |4B-4B|\le K^8m.
$$

Thus

$$
m\le|T|\le |X|^2K^4m=O_c(m),
\qquad
|T-T|\le|X|^4K^8m=O_c(m).
\tag{17}
$$

The lower bound follows because $T$ contains $B-B$, which has at least $m$
elements. Hence $T$ has size comparable to $m$ and bounded difference-set ratio,
with constants depending only on $c$.

For a primary checked source for (16), see Giorgis Petridis, *New Proofs of
Plünnecke-type Estimates for Product Sets in Groups*, arXiv:1101.3507v3, Theorem
1.2 (PDF p.2), whose proof is on PDF p.8. The statement holds in every Abelian
group, so it applies to $\mathbb T$, including torsion. Theorem 3.1 and Ruzsa's
triangle inequality give the proof.
[Full paper](https://arxiv.org/pdf/1101.3507).

## 5. Distinct radius-pair spectra almost never coincide

For an unordered radius pair $\tau=(i,j)$, $1\le i\le j\le k$, write

$$
u_\tau=R_i^2+R_j^2,
\qquad v_\tau=2R_iR_j>0,
$$

and define

$$
S_\tau=\{u_\tau-v_\tau\cos\theta:\theta\in B_i-B_j\}.
\tag{18}
$$

These are the squared-distance spectra for each unordered pair of circles; the
same-circle spectra include zero.

Two distinct unordered radius pairs have distinct parameter pairs
$(u_\tau,v_\tau)$. Indeed, their values determine

$$
(R_i+R_j)^2=u_\tau+v_\tau,
\qquad (R_i-R_j)^2=u_\tau-v_\tau,
$$

which determine the unordered pair of positive radii.

For $\tau\ne\upsilon$, equality of a value in $S_\tau,S_\upsilon$ gives, for
some $x,y\in T$,

$$
\cos y=\frac{v_\tau}{v_\upsilon}\cos x
+\frac{u_\upsilon-u_\tau}{v_\upsilon}.
\tag{19}
$$

The coefficient $a=v_\tau/v_\upsilon$ is positive, and $(a,b)\ne(1,0)$ by the
preceding uniqueness observation. Apply (8) with $U=V=T$, using (17), to obtain

$$
|S_\tau\cap S_\upsilon|=O_c(m^{2/3}+1)=O_c(n^{2/3}).
\tag{20}
$$

There are only $k(k+1)/2=O_c(1)$ pair types. Thus only $O_c(n^{2/3})$ positive
squared-distance values occur for two or more pair types.

If the origin belongs to $A$, distances incident with it have squared values
among $R_1^2,\dots,R_k^2$; discard these at most $k$ values as well. Every
remaining occurring positive distance is represented entirely within exactly one
unordered pair of concentric circles.

For a same-circle type $i=i$, each point has at most two neighbors at a fixed
positive distance, so the unordered multiplicity is at most $|B_i|\le n$. For a
cross-circle type $i\ne j$, each point on either circle has at most two
neighbors on the other, so the multiplicity is at most

$$
2\min\{|B_i|,|B_j|\}\le |B_i|+|B_j|\le n.
$$

Consequently every non-discarded distance is rare, proving (2):

$$
R(A)\ge q(A)-O_c(n^{2/3}).
$$


The anchor circle itself determines at least $(m-1)/2$ positive distances, by
fixing one of its points and using the same at-most-two-neighbors observation.
Therefore (2) implies (1) when $q\le n$.

Finally, when $q>n$, the number of rich classes is less than $n/2$, because each
consumes at least $n+1$ of the $\binom n2$ unordered pairs. Hence

$$
R(A)>q-n/2>n/2\ge(m-1)/2,
$$

which is stronger than (1). The proof above assumed sufficiently large $n$ only
when bounding the number of occupied radii; enlarging $C_c$ absorbs the finitely
many smaller values of $n$. This completes the proof.

## Checks of potential degeneracies

- All distances are counted as unordered pairs. The factor two in the
  cross-circle bound is an actual degree bound, and $2\min(m_i,m_j)\le n$.
- The anchor circle has positive radius. The only zero-radius circle is the
  possible singleton at its center, whose at most $k$ distance values are
  explicitly removed.
- Coincident positive-radius circles are grouped as a single radius before
  defining pair types.
- The only reducible cosine relation for $a>0$ is $(a,b)=(1,0)$. It is excluded
  in the pinned-spectrum step by different radii, and in the pair-spectrum step
  by uniqueness of the unordered radius pair from its sum of squares and
  product.
- The $b=0$ simultaneous-antipodal degeneracy is only order two. It is handled
  in both point and curve incidence counts; it never produces unbounded
  multiplicity.
- All additive-combinatorial arguments take place in the compact Abelian group
  $\mathbb T$; no torsion-free or rational-angle assumption occurs.
- Every implied constant depends only on the fixed fraction $c$, not on the
  radius ratios, angular shifts, or the particular configuration.

## Status and checks

The author checked the argument, including the uniform incidence
bound, the two uses of additive covering, the algebraic degeneracies,
and the multiplicity count; the argument is author-recorded. The cited
Plünnecke–Ruzsa statement and its application were checked in the full
primary paper. No novelty claim is made.

Together with the existing [layer reduction](layers_and_obstructions.md),
this leaves a precise necessary condition for a hypothetical
bounded-rarity sequence: it has a positive fraction of points in finitely many
outer convex layers, but every circle contains only $o(n)$ points.
There is no proved implication from that layer concentration to a
circular subset. Neither unrestricted assertion has been settled.
