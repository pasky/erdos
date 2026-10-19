---
name: research/erdos_963/affine_fourteen
title: 'Fourteen real points contain an affinely dissociated six-set'
desc: Classification of seven-point affine extremizers and a proved fourteen-point extraction, yielding an affine bound with factor 13/16.
tags: []
sources: []
created: 2026-09-19T05:10:00Z
updated: 2026-09-19T05:13:23Z
---


# Fourteen real points contain an affinely dissociated six-set

***

**Theorem.** Every fourteen distinct real numbers contain an
affinely dissociated six-set.

Affine dissociation excludes all nonzero balanced ternary relations,
not merely pair-sum equalities. The proof below explicitly handles
six-term relations. It does not by itself establish ordinary
dissociation of the extracted set.

## Seven-point extremizers

**Lemma.** A seven-point real set with no affinely dissociated
five-set is a translate of

$$
\{0,\pm a,\pm b,\pm(a+b)\},\qquad a,b>0.
\tag{1}
$$

The seven displayed points are distinct.

Use the binary split from [[research/erdos_963/affine_eight|the eight-point
theorem]], annihilating all additive quadruples. Each fiber has affine dimension
at most three and hence at most four points. The fiber sizes are therefore three
and four. The four-point fiber is a parallelogram; translate it to
$U=\{-p,-q,q,p\}$, $p>q>0$, and call the other fiber $T$.

For any pair $x<y$ in $T$, every triple of $U$ must contain a
pair satisfying

$$
u+v=x+y\quad\hbox{or}\quad |u-v|=y-x.
\tag{2}
$$

Otherwise the resulting five points would have no additive
quadruple, since the coloring excludes $3+1$ quadruples.

If $x+y\ne0$ and $y-x\notin\{p-q,p+q\}$, there is at
most one pair of each kind in (2). To meet every triple they
must be disjoint. If the difference pair is $w<z$, the
complementary pair has sum $-w-z$. Hence
$x+y=-w-z$ and $y-x=z-w$, forcing
$\{x,y\}=\{-z,-w\}\subset U$, a contradiction. Thus every
pair of $T$ is centered at zero or has gap $p-q$ or $p+q$.

If no pair is centered, the three gaps force $p=3q$ and $T$
to be an arithmetic progression of gap $2q$. But then
$T\cup\{-p,p\}$ has no additive quadruple: its pair sums
cannot match the outer pair's sum zero, and its differences
$2q,4q$ cannot match $6q$. Again $3+1$ quadruples are excluded
by the coloring. This is a contradiction.

Consequently $T=\{-a,a,t\}$. The other two gaps are $p-q$
or $p+q$. If they agree, then $t=0$ and $a=p-q$ or $p+q$.
If they differ, solving for their sum and difference gives
$\{|t|,a\}=\{p,q\}$, contrary to disjointness of the fibers.
Thus the positive radii of $T\cup U$ form an additive triple,
proving (1).

## Compatible triples in parity-separated hexagons

**Lemma.** Suppose $A,B$ have form (1) up to translation, all
points of $A$ are even integers, and all points of $B$ are odd.
There are triples $A'\subset A$, $B'\subset B$ with disjoint
restricted pair-sum sets and disjoint positive pair-difference sets.

Order their centers as $\alpha<\beta$, interchanging the names
if needed, and put $g=\beta-\alpha$, an odd integer. Their
radii are twice the members of positive integer additive triples
$R,S$. Symmetric triples of half-radii $u\in R,v\in S$ have
disjoint difference sets unless $u/v\in\{1,2,1/2\}$. Their
pair sums are disjoint exactly when

$$
\{-u,0,u\}\cap\{g-v,g,g+v\}=\varnothing.
\tag{3}
$$


If one entire radius triple is even, fix an even member of the
other triple. Among the three members of the all-even triple,
one avoids the three forbidden ratios: an additive triple cannot
equal $\{v/2,v,2v\}$. Equation (3) then holds by parity.

Otherwise both triples have exactly two odd members. Odd $u,v$
satisfy both requirements if they are unequal and neither is $g$.
If no such pair can be chosen, both odd-member pairs must be
$\{g,w\}$ for the same $w$. Their remaining even members
belong to $\{g+w,|g-w|\}$. Hence $R,S$ share a member $L$
which is the largest member of at least one triple. If the
triples are identical this is immediate; otherwise $\max(g,w)$
is the largest member of the difference triple.

Suppose the lower-centered triple is $R=\{r,s,L\}$ with
$r+s=L$. Choose

$$
A'=\{\alpha-2r,\alpha-2s,\alpha-2L\},\qquad
B'=\{\beta-2L,\beta,\beta+2L\}.
$$

Every difference in $A'$ is less than $2L$, while those in
$B'$ are $2L,4L$. Every pair sum in $A'$ is at most
$2\alpha-2L$, while every pair sum in $B'$ is at least
$2\beta-2L$. If instead the upper-centered triple has largest
member $L$, use its three positive rays and the lower hexagon's
symmetric triple of radius $2L$. The same inequalities, reversed
for the pair sums, prove compatibility.

## Proof of the theorem

Suppose $|X|=14$ and $d_{\rm aff}(X)\le5$. Let $M$ have
as rows all balanced ternary relations of support at most six,
and let $K$ be its kernel over $\mathbb F_2$. The real kernel
contains the independent vectors $\mathbf1$ and the weight
vector, so $\dim K\ge2$.

Every nonconstant member of $K$ partitions $X$ into two fibers
of affine dimension at most four, by the established binary split.
Each fiber has at most seven elements; therefore each has exactly
seven. In fact $\dim K=2$. Otherwise choose
$\mathbf1,u,v$ independent. The weights of $u,v,u+v$ would
all be seven, forcing

$$
2|\operatorname{supp}u\cap\operatorname{supp}v|=7,
$$

which is impossible.

Thus $M$ has binary rank twelve and rational rank twelve. Its
real kernel is precisely the span of $\mathbf1$ and the weight
vector. Since it has a rational basis, an affine change of the
weights makes them integral. Normalize their difference gcd to
one. Parity is now a nonconstant member of $K$, splitting $X$
into seven even and seven odd points.

Both fibers have affine dimension at most four, so the first
lemma identifies them as hexagons. The second lemma selects
three points from each without a $2+2$ additive quadruple.
The character excludes $3+1$ quadruples and every balanced
six-term relation on the selection, since such a support has
three points in each parity class. No internal quadruple is
possible within a selected triple. The six points are therefore
affinely dissociated, a contradiction.

## Propagation and exact limitation

The existing binary split now gives

$$
\boxed{d_{\rm aff}(X)=d\ge5
\quad\Longrightarrow\quad |X|\le13\,2^{d-5}.}
\tag{4}
$$

This replaces the former affine factor $7/8$ by $13/16$ in
these dimensions. It improves counts for unit congruence classes
where short ordinary relations are forced to be balanced.

No general upgrade of these extracted sets to ordinary dissociation
is asserted. In particular the possible $1=5$ relation on an
affinely dissociated six-set prevents applying this theorem
directly to the odd seventeen-point problem. In the shared-maximum
construction above, positivity does exclude such a relation, but
that construction is only one case of the compatibility lemma.
