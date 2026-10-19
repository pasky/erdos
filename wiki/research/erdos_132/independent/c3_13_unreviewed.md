---
name: research/erdos_132/independent/c3_13_unreviewed
title: Unreviewed thirteen-point rotational candidate exclusion
desc: |
  Archived unreviewed argument for thirteen points with 120-degree symmetry;
  its full case analysis has not been independently checked.
sources: []
created: 2026-09-23T05:40:00Z
updated: 2026-10-13T05:28:09Z
---


# Unreviewed thirteen-point rotational candidate exclusion

***

**Superseded as a needed finite-order step.** The published complete
six-distance classification now excludes every thirteen-point $R=1$
set; see [small orders](../small_orders.md). This does not retrospectively
certify the separate argument below, which remains unreviewed.

**Unreviewed input, not an established theorem in this wiki.** The record
below is unreviewed input. Its claim concerns only thirteen-point sets
invariant under a 120-degree rotation. The author has not independently
checked its full case analysis, and it is not included in the list of
proved finite cases. Neither unrestricted question follows
even if the restricted argument is correct.

The finite special-axis script is preserved at
[evidence/util/c3_hex_candidates_exact.py](../evidence/util/c3_hex_candidates_exact.py).
A successful script run alone would not certify the geometric reductions or all
the other radial cases.

---

## A checked-locally exclusion of thirteen-point C3-symmetric candidates

**Status:** This is a new restricted argument, prepared for independent audit.
It is not an unrestricted proof of Erdős 132. No wiki changes are made here.
The only classification input is the already documented planar few-distance
classification: at most twelve points determine five distances; among
nine-point four-distance sets, the only cocircular type is the regular nonagon.

## Claim

Every thirteen-point planar set invariant under a rotation through 120 degrees
has at least two distances of unordered multiplicity at most thirteen.

Assume otherwise. Let q be its number of distinct positive distances.
The general pair budget gives q <= 6; the twelve-point bound for five distances
gives q >= 6. Thus q=6. All unordered edge orbits under the 120-degree rotation
have size three. Rich classes therefore have at least fifteen pairs, and the
diameter has at least three. Since C(13,2)=78=5*15+3, the complete multiplicity
list is

    (15,15,15,15,15,3),

where the multiplicity-three class is the diameter.

The rotation center belongs to A, and the other twelve points form four
equilateral-triangle orbits. Write a,b,... for **squared** circumradii.
A triangle of squared circumradius a supplies squared distances a (to the
center) and 3a (within the triangle).

Two triangle orbits of squared circumradii a,b have three cross squared
distances, counted with repetition, satisfying

    sum d_i = 3(a+b),
    sum d_i^2 = 3(a+b)^2 + 6ab.                 (M)

These follow from the distance formula
d_i=a+b-2 sqrt(ab) cos(theta+2*pi*i/3).

There are five radial multiplicity patterns: 4; 3+1; 2+2; 2+1+1; 1+1+1+1.

## 1. Four distinct squared radii

Let B contain the four squared radii. Since B union 3B is in the six-value
palette, B has at most two maximal consecutive multiplication-by-three chains:
indeed |B union 3B|=|B|+(number of chains).

Choose the least a in a chain containing a,3a. For these two triangle orbits
(M) gives cross squares with sum 12a and square sum 66a^2. All lie in

    I=[(4-2 sqrt(3))a, (4+2 sqrt(3))a].

The chosen chain contributes only a,3a to I. If B has one chain, B union 3B
has five elements, so at most one additional palette value is available.
Three distinct cross values would then have to include a and 3a, forcing the
third to be 8a, outside I. Repeated cross values instead have the form

    (4+sqrt(3))a twice, (4-2sqrt(3))a once,
or  (4-sqrt(3))a twice, (4+2sqrt(3))a once.

Both distinct values are irrational multiples of a, so one extra value cannot
provide them.

If B has two chains, B union 3B has all six palette values. The other chain
contributes at most three consecutive powers b,3b,9b to I, since the quotient
of the interval endpoints is (2+sqrt(3))^2<27. In a repeated-root case both
values must come from that chain, but their ratio is irrational, impossible.
For three distinct roots at most one is a or 3a. If all three are b,3b,9b,
their square-sum/sum-square ratio is 91/169, not 66/144=11/24. Otherwise
they are ca,ub,vb, where c is 1 or 3 and {u,v} is a two-element subset of
{1,3,9}. The two moment equations require

    (u^2+v^2)/(u+v)^2 = (66-c^2)/(12-c)^2.

The left side is 5/8 or 41/50, and the right is 65/121 or 19/27. None agree.
This excludes four distinct radii using only q<=6.

## 2. Radial pattern 4

All twelve noncentral points lie on one circle. Their chord classes have at
most twelve pairs each; only the circumradius class can receive center pairs.
The circle supplies at least six chord lengths (pin one vertex and use the
at-most-two-neighbors property). Hence at least five classes are rare.

## 3. Radial pattern 3+1

Let C be the nine-point circle of squared radius a, and T the other triangle
of squared radius b. Cross C--T contribution to any length is at most six.

If C is not regular, its rotational symmetry group has order three: the group
order divides nine and is divisible by three. A chord with nine pairs has
degree two at every vertex, so its chord rotation preserves C. Consequently
the only chord with nine pairs is square 3a. All other chord multiplicities
are at most six (and divisible by three).

The extra, noncross contributions occur only at a, b, 3b. Every other chord
besides 3a therefore has at most twelve total pairs and must be the unique
diameter. Thus the circle's palette is contained in

    {3a,a,b,3b,D},

where D denotes the full squared diameter. If the circle had at most four
lengths, the nine-point classification would force it to be regular. Otherwise
it has exactly five, and all five displayed values are distinct and occur on
C. Since the full set has six lengths, there is a further length, which can
only arise from C--T cross pairs and hence has at most six pairs. It differs
from D, contradiction.

It remains that C is a regular nonagon. Its four chord squares each have nine
pairs; none is D because D has only three. Its radius square a is not a chord
square, since a unit-radius chord would need angular separation 60 degrees,
not an integer multiple of 40 degrees.

The square b must be a chord square. Otherwise its class has at most three
center--T pairs and six C--T pairs, and b is not the diameter because 3b occurs.
For a point on T the nine pinned distances to C have either nine values, or
five values when the point lies on a reflection axis of C. Indeed any equal
pinned distances force that reflection axis. The first option contradicts
q=6. Hence the entire C--T cross spectrum has five values with multiplicities
6,6,6,6,3 (the three points of T are related by a symmetry of C).

The class b already has nine circle pairs and three center--T pairs, so its
cross contribution must be three. If 3b were a chord square or a, that distinct
class would also have twelve noncross pairs (nine from C or its central star,
plus three within T), and would need another cross contribution of three.
There is only one such cross class. Thus 3b is neither a chord square nor a.
Its full multiplicity is at most nine, so it is the unique diameter and has
no cross contribution. The unique three-pair cross class is b.

The unpaired pinned vertex lies on the reflection axis. Its squared distance
to T is (sqrt(a)+sqrt(b))^2 or (sqrt(a)-sqrt(b))^2. Equality with b forces
b=a/4. But a regular nonagon's smallest chord square is
4a sin^2(pi/9)>a/4, contradiction.

## 4. Radial pattern 2+2

A six-point C3-invariant circle consists of two triangles. If it is not a
regular hexagon, its circle-plus-center palette has exactly five values

    F_a={a,3a,u,v,w},
    0<u<a<v<3a<w<4a,
    u+v+w=6a,  u^2+v^2+w^2=18a^2.

For example rotate the first triangle to phase zero and choose the second
phase in (0,pi/3); the inequalities follow directly from the three chord
cosines. Consequently sum(F_a)=10a and sum of squares(F_a)=28a^2.

If both circles are nonregular, their F_a,F_b each have five elements and
union size at most six. They cannot coincide (their sums determine the radius),
so they share exactly four. Assume b>a and write x for F_a's unique element,
y for F_b's unique element. The two moments give

    y-x=10(b-a),  x+y=(14/5)(a+b),
    x=(32a-18b)/5, y=(32b-18a)/5.

Since y<4b, b<3a/2. The value x cannot equal a (which forces b=3a/2), nor 3a
(which forces b=17a/18). Thus a and 3a both occur in F_b, necessarily as its
small and middle cross-chord values. Their third value is 6b-4a. The chord
square-sum identity then gives

    9(b/a)^2-24(b/a)+13=0.

The only root greater than one is (4+sqrt(3))/3>3/2, contradiction.

If both circles are regular hexagons, the full set has C6 symmetry. Under a
60-degree rotation all unordered edge orbits have size six except for the
two orbits of three antipodal edges, one on each circle. Each of the six
target multiplicities 15,15,15,15,15,3 is 3 mod 6, and would need an odd number
of antipodal orbits. Two such orbits cannot serve six classes.

If exactly one circle H is a regular hexagon, write the other as triangles
T_1,T_2. A triangle-to-H cross spectrum has six generic values; four values
when its phase is a hexagon-vertex axis; or three values when its phase is an
edge-midpoint axis. The two special cosine sets are respectively
{+/-1,+/-1/2} and {0,+/-sqrt(3)/2}. If both triangles have the same special
type, their union is a regular hexagon or the triangles coincide, contrary to
the present case. If they have different types their cross spectra give seven
values. Thus one triangle is generic, and its six cross values fill the full
palette. The other cannot be special: its cosine set contains 0 or +/-1,
absent from the generic cosine set. It too is generic and uses all six
palette values. Each value then has at least six cross pairs, contradicting
the three-pair diameter.

## 5. Radial pattern 2+1+1 with a nonregular six-point circle

Normalize that circle's squared radius to one. Its circle-plus-center palette
is

    F={1,3,u,v,w},  0<u<1<v<3<w<4,
    u+v+w=6,  uv+uw+vw=9.

Write S=F union {t} for the full six-value palette. The other distinct squared
radii b,c differ from one and force directed edges b->3b,c->3c in S.

Besides 1->3, the only possible edges wholly within F are

    u->1 (u=1/3), u->v (v=3u), v->w (w=3v).

At most one occurs: the first and second violate v>1; the first and third
would give w=17/4>4; the second and third would give w=54/13>4.

### 5a. One of the two actual radius edges lies wholly within F

If it is u=1/3 ->1, then

    v=(17-sqrt(33))/6, w=(17+sqrt(33))/6.

The other radius edge uses t, so

    t in {1/9,9,v/3,w/3,3v,3w}.

Formula (M) for radii 1 and 1/3 requires three elements of S, with repetition,
to sum to four. This is impossible. For t=v/3 or w/3, irrational coefficient
cancellation forces zero or three copies of t; three copies remain irrational,
so none occur. For t=3v or 3w, its irrational coefficient cannot be canceled
by at most two other terms. Without t, irrational terms must occur as v+w,
which already exceeds four. The value t=9 exceeds four too. The remaining
rational options, including t=1/9 if present, are odd multiples of 1/9; three
of them cannot sum to 4=36/9.

In the other two internal-edge cases the actual squared radius p is irrational
and

    F={1,3,p,3p,6-4p},
    13p^2-24p+9=0.

The extra palette value is one of

    {1/3,9,p/3,9p,(6-4p)/3,3(6-4p)}.

No three elements of S sum to 3+3p, again contradicting (M). For any of the
three fractional choices, coefficient comparison in the basis 1,p forces the
number of copies of t to be zero or three. Three copies sum to 1,p,or 6-4p,
not 3+3p; therefore t is unused. For the other three choices (or with t unused),
every constant coefficient is a nonnegative multiple of three except that of
the value 1. Thus zero or three copies of 1 occur; three fail, so none occur.
The constant coefficient three on the target then forces exactly one value 3
and two values chosen from p,3p,9p. Their p-coefficients are 1,3,9, and two of
them cannot sum to three.

### 5b. Neither actual radius edge lies wholly within F

Both use t. Injectivity of multiplication by three forces them to form
s->t->9s, with s,9s in F and t=3s not in F. Necessarily s=u. The possibility
9u=3 gives t=1 in F and is excluded. The others are:

* 9u=1: u=1/9, v,w=(53 +/- sqrt(105))/18, t=1/3. Cross squares for radii
  1 and u lie in [4/9,16/9], where S has only the value 1. Three copies of 1
  fail the required sum 10/3.
* 9u=v: the equation is (7u-3)(13u-3)=0; ordering gives u=3/13. The palette,
  multiplied by 13, is {3,9,13,27,39,48}. The required cross sum is 48.
  A term 48 is too large to occur with two positive terms, and all other
  numbers are odd, so three cannot sum to 48.
* 9u=w: ordering gives u=3/7. The palette multiplied by seven is
  {3,7,9,12,21,27}. The required cross sum is 30; its only three-term multiset
  is {9,9,12}. Its square sum is 306, whereas (M) requires 426.

This closes the nonregular six-circle case using q<=6 alone.

## 6. Radial pattern 2+1+1 with a regular hexagon

Normalize the hexagon to squared circumradius one. It and the center supply
{1,3,4}. Let b!=1 be the squared radius of either other triangle.

### Generic phase cannot occur

A generic triangle-to-hexagon cross palette has six values, and hence equals
the full palette S. Its values are paired about the mean 1+b. Since 1 and b
are in S, their partners 1+2b and 2+b also occur. Thus S contains

    T(b)={1,3,4,b,3b,1+2b,2+b}.

These seven expressions must have a coincidence. For b>0, b!=1 the complete
list of possibilities is b in {1/3,3,4,4/3,3/2,2}. Each gives six distinct
values, but their sum minus the required 6(1+b), in that order, is
13/3,5,5,7/3,5/2,3. None is zero.

### Special phases: finite quadratic certificate

On a vertex axis write x=sqrt(b)>0. The forced squared palette is

    V(x)={1,3,4,x^2,3x^2,x^2+1-2x,x^2+1-x,x^2+1+x,x^2+1+2x}.

On an edge-midpoint axis write x=sqrt(3b)>0. It is

    E(x)={1,3,4,x^2/3,x^2,x^2/3+1-x,x^2/3+1,x^2/3+1+x}.

The only positive parameters, with b!=1, for which a pair of these distinct
polynomials is equal are listed below. Thus the table exhausts all parameters
with at most six values. Equalities and cardinalities are verifiable by
substitution in quadratic fields; all other parameters give respectively nine
or eight distinct values.

For V the twelve candidate x are

    (sqrt(3)-1)/2, 1/2, 1/sqrt(3), sqrt(3)-1, 2/sqrt(3),
    (sqrt(13)-1)/2, (sqrt(3)+1)/2, sqrt(3), 2,
    (sqrt(13)+1)/2, sqrt(3)+1, 3.

Their cardinalities are eight except at x=1/2 (seven) and x=2 (six).
For E the twelve candidate x are

    (sqrt(33)-3)/4, 1, sqrt(6)/2, (sqrt(33)-3)/2,
    3(sqrt(5)-1)/2, 2, (sqrt(33)+3)/4, sqrt(6), 3,
    2sqrt(3), (sqrt(33)+3)/2, 3(sqrt(5)+1)/2.

Their cardinalities are seven except at x=1 (six) and x=3 (five).
The surviving squared radii and palettes therefore are

    vertex b=4:    {1,3,4,7,9,12};
    edge b=1/3:    {1/3,1,4/3,7/3,3,4};
    edge b=3:      {1,3,4,7,9}.

Two distinct radii can use at most six values in union only for b,c=4,3.
But triangles of radii 2 and sqrt(3) on these two different axis types have
relative phases pi/6 modulo pi/3, and their cross squares are {1,7,13}.
The new value 13 is outside the six-value union, contradiction.

For a machine-reproducible exact check of only this finite quadratic table, see
[the retained script](../evidence/util/c3_hex_candidates_exact.py). It solves
pairwise differences of the displayed polynomials and expands every substituted
quadratic radical to canonical rational-plus-radical form. An earlier unexpanded
Sympy display overcounted two rejected cardinalities; the expanded script and
all counts above use the corrected canonical form. The survivor list was
unchanged.

All radial patterns are now excluded. The claim remains subject to independent
audit, especially the nine-point classification application and the quadratic
candidate table; this report does not claim an unrestricted resolution.
