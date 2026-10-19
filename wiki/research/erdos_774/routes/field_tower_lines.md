---
name: research/erdos_774/routes/field_tower_lines
title: Concrete field and polynomial line matching targets
desc: Field towers, linear flags, and a nested polynomial model retain uniform extraction; exact integer and Fourier formulas and an explicit mixed trade leave arbitrary-color growth unresolved.
tags: [E0774, lines, extraction, proved, coloring, incomplete]
sources: []
created: 2026-09-19T00:23:00Z
updated: 2026-09-19T00:48:35Z
---


# Concrete field and polynomial line matching targets

***

This is a concrete member of the already uniformly extracting
[linear-direction matching family](resolvable_matchings.md), not a proved
counterexample. Its arithmetic is explicit, but **unbounded actual
dissociated coloring remains unproved**. It is not being substituted for
the main ordinary-cover target on the strength of rational rank alone.

## 1. The finite configurations

Fix a prime p>=3 and finite fields
K_0=F_p strictly contained in K_1,...,K_m. Put q_j=|K_j|, so
q_j>=q_(j-1)^2. The rows are G_m=K_m^2.
Initial directions are the p+1 one-dimensional F_p subspaces

$$
 H_a=\{(x,ax):x\in F_p\}\quad(a\in F_p),\qquad
 H_\infty=\{(0,y):y\in F_p\}.
$$

At level j>=1, add the directions

$$
 H_s=\{(x,sx):x\in K_j\},\qquad s\in K_j\setminus K_{j-1}.
 \tag{1}
$$

Columns are indicators of every coset of each direction. Each direction
partitions G_m. Different direction subgroups intersect only at zero:
equality (x,sx)=(y,ty) forces x=y and then x=0 if s differs from t;
the vertical direction is immediate. Hence distinct direction cosets
intersect in at most one point. Columns are distinct and nonzero.

Let N_m=|G_m| and n_m be the number of columns. Then

$$
 \frac{n_m}{N_m}=\frac{p+1}{p}
       +\sum_{j=1}^m\left(1-\frac{q_{j-1}}{q_j}\right)
 \geq\frac{p+1}{p}+m(1-1/p).
 \tag{2}
$$

Every earlier stage occurs as a restriction to a copy of K_i^2, with its
old columns, inside a later stage. Thus actual coloring number is
nondecreasing along a tower. No proof that it tends to infinity is known.

## 2. One uniform full-dissociation extraction constant

Apply the proved phase induction for linear direction matchings, ordering
directions by level. It bounds the logarithmic loss for a size-d column
by d times the sum of -log cos(pi/D) over later direction sizes D.
Use

$$
 -\log\cos(\pi/D)\leq\frac{\pi^2}{2D(D-1)}\qquad(D\geq3).
$$

The earlier proof covers D>=4; at D=3 the inequality is the direct
comparison log 2<=pi^2/12. For a level-i column, the later-level tail
satisfies

$$
 \sum_{j>i}\frac{q_j-q_{j-1}}{q_j(q_j-1)}
 \leq\frac1{q_i^2-1}.
 \tag{3}
$$

Indeed divide a summand by 1/q_(j-1)-1/q_j. The ratio is
q_(j-1)/(q_j-1), at most q_i/(q_i^2-1), since a/(a^2-1) is decreasing
and q_j>=q_(j-1)^2. Telescope the differences of reciprocals.

For i>=1, the total loss is at most
(pi^2/2)[(q_i-q_(i-1))/(q_i-1)+q_i/(q_i^2-1)]<pi^2.
For an initial direction it is at most
(pi^2/2)[p/(p-1)+p/(p^2-1)]<=15pi^2/16.
Consequently

$$
 \boxed{\rho(E_m)\geq e^{-\pi^2}.}
 \tag{4}
$$

The bound is independent of the prime, tower length, and extension degrees. The
single direct-sum application of
[Pisier's Theorem 2](../../../../library/analysis/pisier_1983_arithmetic_characterizations_sidon_sets/_index.md)
already justified in the [matching theorem](resolvable_matchings.md) therefore
supplies one positive full-dissociation extraction constant for all these finite
sets and all their subsets. It is not weakened to any fixed relation order.

## 3. Initial prime-torsion arithmetic

In any initial affine F_p plane and at any point z,

$$
 p\,1_{\{z\}}=
   \sum_{\text{all }p+1\text{ directions }a}1_{\ell_a(z)}
       -1_{F_p^2}.
 \tag{5}
$$

Choose one direction and express the last term by its parallel class.
Its line through z cancels. The resulting preimage has coefficients
plus one on the other p pencil lines and minus one on the p-1 other
parallel lines. Thus it is ternary on 2p-1 old columns.

In particular the whole configuration has full rational row rank N_m,
and its integer image contains p Z^(G_m). Equations (2) and (5) give
unbounded **rational** covering number, not unbounded dissociated covering.

More exactly, the initial plane's integer image modulo p is the evaluation
code of F_p-polynomials of total degree at most p-1. Each line indicator
is 1-(ax+by-c)^(p-1), proving containment. Conversely parallel classes
span every function of a linear form; Vandermonde expansion of
(x+t y)^j for 0<=j<=p-1 gives every homogeneous monomial of degree j.
The monomials of total degree at most p-1 are independent as functions
on F_p^2, since their individual degrees are below p. Thus the integer
cokernel is (Z/p)^(p(p-1)/2). Across initial planes the construction is
a direct sum. Adding later columns preserves the assertion that the
integer image is determined completely by its reduction modulo p.

A genuinely new line meets every initial affine plane in at most one
point. Summing (5) in its occupied planes gives a ternary old-column
preimage of p times that new column. This is an unrestricted lift: the
old columns need not share the new column's actual color.

### A precise warning about color support

Even singleton lifting need not be flat on a prescribed rationally
independent class. In a full affine p-plane, every representation of
p delta_z has coefficients

$$
 a_{D,b}=1_{b=b_D(z)}+c_D,
 \qquad\sum_Dc_D=-1.
 \tag{6}
$$

To see completeness, a zero relation among full affine-line indicators
has coefficients constant on each parallel class, with those constants
summing to zero. This follows by evaluating nonzero additive Fourier
frequencies, each of which lies in the annihilator of exactly one
direction. Subtract (5) to obtain (6).

For (6) to be ternary, every c_D is either -1 or zero, so exactly one
direction is exceptional. Choose a column class containing one whole
parallel class, two other parallel classes with their z-lines deleted,
and only the z-line in every remaining direction. It is rationally
independent: any supported zero relation would need two complete parallel
classes. It has a rational preimage of p delta_z, using c=1 on the full
class, c=-1 on the two deleted-pencil classes, and c=0 elsewhere; one
coefficient is two. No ternary preimage exists. This is why (5) cannot
be used as a color-safe lifting theorem.

## 4. Exact last-level relation equations

Write L=K_m, q=|L|, and let B(x,y) be the point sum of chosen old-line
coefficients. Newest lines are y=sx+b with s in L minus K_(m-1).
If their coefficients are a_s(b), a relation is exactly

$$
 B(x,y)+\sum_{s\in L\setminus K_{m-1}}a_s(y-sx)=0.
 \tag{7}
$$

Use unnormalized Fourier transforms for a fixed nontrivial additive
character of L. The transform of a_s(y-sx) is zero off
D_s={(-sv,v):v in L}, and equals q times hat a_s(v) on D_s.
The nonzero sets D_s are disjoint. Therefore (7) holds precisely when

* hat B vanishes at every nonzero frequency outside the union of the D_s;
* hat a_s(v)=-hat B(-sv,v)/q for v nonzero;
* hat B(0,0)+q sum_s hat a_s(0)=0.

This determines all nonconstant parts of a_s. In real-space form, let
R_sB(b)=sum_x B(x,sx+b) and let mean B=q^(-2)sum B. Then

$$
 a_s(b)=-R_sB(b)/q+c_s,
 \qquad \sum_sc_s=(h-1)\operatorname{mean}B,
 \tag{8}
$$

where h is the number of newest directions, together with the first
Fourier support condition above. For integer a_s, all Radon values in
each direction must be congruent modulo q. Ternary values require their
oscillation to be at most 2q and an admissible shift; an off-color new
line additionally pins a_s(b) to zero. None of these actual-color
conditions follows merely from real Fourier support or from (5).

The remaining task is to satisfy this coupled system for some nonzero
monochromatic coefficient array under **every** prescribed finite palette.
No such theorem is proved. The candidate, extraction estimate, and
integer-image formulas have internal checks only; no numerical search or
external validation is claimed.

## 5. A necessary old-column mass in a genuinely mixed relation

Let q=|K_m| and let the old coefficients be epsilon_E. Summing a full
relation over two parallel newest lines gives exactly

$$
 q(a_s(b)-a_s(b'))=
 -\sum_{E\ {
m old}}\epsilon_E
   (1_{E\cap\ell_{s,b}\ne\varnothing}
    -1_{E\cap\ell_{s,b'}\ne\varnothing}).
$$

Every old column meets each newest line in at most one point. Other
newest directions contribute a constant to these two line sums and
cancel. Therefore

$$
 \sum_{E\ {
m old}}|\epsilon_E|
 \geq q\max_s\operatorname{osc}(a_s).
 \tag{9}
$$

In particular a relation with a nonconstant newest coefficient function
needs at least q old columns when all coefficients are ternary. Fewer
than 2q old columns also forbids one newest direction from taking both
plus and minus one. Below q, all newest functions are constant and the
relation splits into old relations and complete-parallel-class relations.
This rules out bounded-old-support amplification as q grows, not
coordinated larger witnesses. It is an exact inequality, not an
enumeration or random-color estimate.

## 6. Denser linear flags and a genuinely nested polynomial model

Field closure is unnecessary for the extraction proof. In L=F_(p^(m+1))
choose a full F_p-linear flag V_0=F_p contained in ... contained in
V_m=L. For s in V_j minus V_(j-1), give that slope the direction
H_s={(x,sx):x in V_j}. Include the initial p+1 directions as before.
Now q_j=p^(j+1), with the same direction counts q_j-q_(j-1).
Different slopes still give intersections of size at most one.

The phase bound remains rho>=exp(-pi^2) for p>=3. In place of (3),
divide its summand by 1/q_(j-1)-1/q_j; the ratio is now
q_(j-1)/(p q_(j-1)-1)<=1/(p-1). The tail loss for a level-i column is
therefore at most pi^2/[2(p-1)], while its same-level loss is at most
pi^2/2. The initial loss is at most pi^2(p+1)/[2(p-1)]<=pi^2.
All newest full-line equations and (9) remain valid.

Old subfield-plane decompositions do **not** survive this replacement:
V_j need not be closed under multiplication. Nor are configurations over
varying ambient fields asserted to be nested.

An alternative avoids that nesting issue. Work in the polynomial ring
F_p[t], let V_j be its polynomials of degree at most j, and take rows

$$
 X_m=V_m\times V_{2m}.
$$

For every slope r of exact degree j<=m, use all cosets of
H_r={(x,rx):x in V_j}; zero and constant slopes have j=0. Add the
initial vertical direction. Products have degree at most 2m, so these
are actual partitions of X_m. The integral-domain property gives the
same pairwise intersection bound, and the same counts and phase estimate
apply. Both the row sets and the columns are now genuinely nested.
Their union is a concrete countable uniformly extracting vector family.
The existing finite integer encoding and separated-block construction
apply if unbounded actual coloring can be proved.

The polynomial version also permits p=2, with a fixed modified constant.
In each initial four-point plane its six distinct edge characters have
positive-real Sidon parameter at least 1/6: align a largest coefficient
and average on that character's phase fiber, annihilating the other five.
Separate initial planes use independent phases. The later direction
sizes are at least four, and the same tail calculation gives
rho>=(1/6)exp(-pi^2). Thus the binary diagnostic below is inside a
uniformly extracting family as well.

Newest polynomial columns are not full lines in X_m. Consequently the
full-line Fourier parametrization and (9) are not silently transferred
to this last model.

## 7. An explicit mixed mechanism, still not arbitrary-color growth

The [bounded binary diagnostic](../evidence/polynomial_checksum/_index.md)
found a monochromatic eight-column trade for one natural linear-intercept
checksum coloring. Its exact reconstruction extends to **every** binary
linear-intercept checksum, as proved on that evidence page: a four-,
six-, or eight-column relation already occurs by stage one.

The eight-column mechanism uses two new directions and six old star
edges. It is an actual color-respecting preimage of a **difference** of
new columns, not a flat point preimage and not a monochromatic elementary
two-direction bundle. This supplies a concrete mixed relation shape to
test in future color arguments. No theorem currently forces such shapes
under every finite palette; even failure of all these two-valued checksums
does not rule out a different two-coloring. Indeed the same evidence page
now gives an explicit direction-offset coloring of the entire binary
stage one into **two rationally independent classes**, each a 32-column
basis with determinant of absolute value 2^8. This is a positive finite
coloring theorem, not an unbounded-color obstruction or an all-depth
coloring theorem.


### All common-linear affine offsets fail, not all colors

The [offset theorem](../lemmas/polynomial_offset_trades.md) shows that
every binary coloring c_r=L(v-ru)+h_r, c_inf=L(u)+h_inf fails by stage two,
for arbitrary direction offsets and one arbitrary common linear functional.
Singular Hankel matrices give monochromatic hyperplane-bundle trades;
consecutive nonsingular matrices give an adaptive four-direction character
identity. Full auxiliary graphs are partitioned into actual columns, with
no coefficient collision. The stage-one proper coloring is not contradicted:
it simply has no extension within that palette class. Arbitrary stage-two
two-coloring and unbounded actual coloring remain open.
