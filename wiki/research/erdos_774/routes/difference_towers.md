---
name: research/erdos_774/routes/difference_towers
title: Difference towers preserve uniform extraction and halve relation height
desc: Global seam deletion gives a near-lossless extraction theorem for cyclic difference families; all stages halve integer-relation height, but arbitrary-color growth remains unproved.
tags: [E0774, proved, construction, incomplete]
sources: []
created: 2026-09-18T21:00:00Z
updated: 2026-09-18T21:59:00Z
---


# Difference towers preserve uniform extraction and halve relation height

***

## Standing

The difference family has an elementary, stage-uniform extraction proof. It does
not use the linear-intersection hypothesis, which this family fails. Integer
relations also admit a coefficient-halving lift through every stage. Neither
statement controls an arbitrary subsequent coloring. **No unbounded chromatic
theorem, and no E0774 counterexample, is proved here.**

## 1. Definition and distinctness

Let A=(a_v)_{v in V} be a finite indexed family of nonzero integer vectors
in Z^r, and let N>=4. Put G=(Z/NZ)^V. In the free abelian group of
Z^r-valued functions on G define

$$
 b_{v,g}=a_v\otimes(e_g-e_{g+e_v}),\qquad
 D_N(A)=(b_{v,g})_{v\in V,\ g\in G}.
 \tag{1}
$$

Here e_v denotes the coordinate step in G, whereas e_g is the standard
basis vector at the vertex g. The supports in the G coordinate are
undirected edges of a Cartesian product of N-cycles. For N>=4, two such
edges have the same unordered endpoints only when their type and initial
vertex coincide. Consequently (1) has no zero, equal, or antipodal pair,
even if the input family has repeated or proportional vectors. For the
extraction theorem below, the input's hypothesis is on its indexed family;
no extraction claim for repeated input labels is silently assumed.

Write eta(A) for the largest delta such that every subfamily F of A
contains a fully dissociated subfamily of size at least delta|F|. There
is no bound on the number of terms in a forbidden relation.

## 2. Near-lossless full-dissociation extraction

**Theorem.** For every A and N as above,

$$
 \boxed{\eta(D_N(A))\geq(1-1/N)\eta(A).}
 \tag{2}
$$

**Proof.** Fix an arbitrary edge subfamily F. For each coordinate v choose
one cyclic seam s_v uniformly in Z/NZ. Delete the edges of type v whose
initial v-coordinate is s_v-1. Each edge is deleted with probability 1/N,
so some choice retains at least (1-1/N)|F| edges.

These are **global coordinate seams**, shared across all parallel lines
of a given type. Arbitrary linewise seam choices are not needed and do
not necessarily give the acyclic order used next.

Define r_v(g) to be the representative of g_v-s_v in {0,...,N-1}, and
H(g)=sum_v r_v(g). Every retained edge g -> g+e_v strictly increases H.
For every vertex h, assign to h the retained edges with head h. Their
types are distinct: there is at most one incoming edge of any type v.
Apply the input extraction property to this set of types, and retain a
dissociated subfamily of at least eta(A) times its size. The union E of
these choices therefore has size at least eta(A)(1-1/N)|F|.

Suppose a nonzero ternary relation on E existed. Among all endpoints of
edges with nonzero coefficients choose h with maximal H(h). No supported
edge leaves h, since its head would have larger H. The row-vector equation
at h is consequently a nonzero relation with coefficients in {-1,0,1}
among its selected incoming types. Those input vectors were chosen
fully dissociated. This is a contradiction. Thus E is dissociated. QED.

The same proof allows nonnegative weights whenever the corresponding
weighted input extraction hypothesis holds: average removed weight and
extract separately at each head. No weighted hypothesis is required for
(2).

## 3. Positive-real Sidon estimate without invoking Pisier

Let rho(A) denote the positive-real Sidon lower parameter used in
[the phase arguments](tensor_extraction.md). Then

$$
 \rho(D_N(A))\geq (1-1/N)\rho(A)-1/N
 \geq\rho(A)-2/N.
 \tag{3}
$$

To prove this, fix arbitrary complex coefficients of total absolute mass W.
Choose global seams with removed mass W_cut<=W/N. Process vertices in
increasing H. When processing h, all tails of retained edges entering h
have assigned torus phases z_g; z_h is still free. Such an edge contributes

$$
 \Re\{c_{v,g}\,\chi_{a_v}(z_g)\,
                    \overline{\chi_{a_v}(z_h)}\}
 =\Re\{\overline{c_{v,g}\chi_{a_v}(z_g)}\,
                    \chi_{a_v}(z_h)\}.
$$

The incoming types are distinct. By the definition of rho(A), choose z_h
to give at least rho(A) times the total incoming coefficient mass.
Previously completed edges have both endpoints earlier and are unchanged.
Every retained edge is completed exactly once. The removed edges, whatever
the final phases, contribute at least -W_cut. Hence the total real part is
at least rho(A)(W-W_cut)-W_cut, proving (3). The second inequality uses
rho(A)<=1.

In particular, (2) already proves proportional dissociation directly;
no new qualitative source theorem or block-dependent constant is required.

## 4. Summable-cost iteration

Let A^(0)=A and A^(j)=D_{N_j}(A^(j-1)), with N_j>=4. Induction gives

$$
 \eta(A^{(k)})\geq\eta(A)
             \prod_{j=1}^k(1-1/N_j).
 \tag{4}
$$

If sum_j 1/N_j is finite, the infinite product is positive. For example,
N_j=2^{j+3} gives sum_j 1/N_j=1/8 and

$$
 \prod_{j=1}^k(1-1/N_j)\geq1-\sum_{j=1}^k1/N_j\geq7/8.
 \tag{5}
$$

Thus starting from *any uniformly extracting family of seeds*, all these stages
have one common full-dissociation extraction constant. There is no blockwise
decay to zero. The earlier
[exact integer realization](../lemmas/rational_realization.md) and
[separated-block construction](../lemmas/finite_blocks.md) apply to these finite
integer-vector families if an unbounded coloring theorem is subsequently proved.
Perform the difference operations in vector coordinates and encode only the
completed block: an intermediate scalar encoding which preserves just ternary
relations need not preserve the height-two relations tested by the next
difference operation.

## 5. Exact divergence equation and height halving

An integer coefficient array f=(f_v(g)) is a relation on D_N(A) precisely
when, for every g in G,

$$
 \sum_{v\in V}a_v\bigl(f_v(g)-f_v(g-e_v)\bigr)=0.
 \tag{6}
$$

This follows just by taking the Z^r-valued coordinate at g in (1).

**Height-halving lemma.** For every N>=4, a nonzero integer relation
u=(u_v) of A has a nonzero lifted relation of height
ceil(||u||_infinity/2). No parity restriction on N is needed.

On Z/NZ put F(s)=1_{s=0} and w(s)=F(s)-F(s-1), so
w=delta_0-delta_1. For g in G set

$$
 p_v(g)=\prod_{z\ne v}w(g_z),\qquad
 f_v(g)=u_v p_v(g)F(g_v)
                   -\left\lfloor\frac{u_vp_v(g)}2\right\rfloor.
 \tag{7}
$$

The second term is constant along each v-line. Consequently

$$
 f_v(g)-f_v(g-e_v)=u_v\prod_z w(g_z).
$$

Equation (6) proves that f is a relation. On each v-line, write
b=u_v p_v(g). Its two possible values are ceil(b/2) and -floor(b/2),
whose maximum absolute value is ceil(|b|/2). Choosing all other coordinates
zero makes p_v=1; choosing g_v=0 and g_v=1 realizes both values.
Thus f is nonzero and

$$
 \|f\|_\infty=\lceil\|u\|_\infty/2\rceil.
 \tag{8}
$$

After k stages, any particular input relation of height h has a nonzero
lifted relation of height ceil(h/2^k). It becomes ternary after at most
ceil(log_2 h) stages. This is coefficient-safe, with no support-size bound.
Its supported columns have **not** been forced to share an actual color.

For even N there is a simpler alternative:
f_v(g)=ceil(u_v/2) on even total parity and -floor(u_v/2) on odd total
parity. Its divergence is u_v times the common parity sign, proving the
same conclusion.

### 5.1 Sharp first non-cycle height

Call a relation *cyclewise constant* if every f_v is constant along each
v-coordinate line. These are exactly the arrays with zero divergence
in every component. They are integer combinations of the obvious
coordinate-cycle relations.

If A is rationally dependent, let lambda(A) be the minimum infinity norm
of a nonzero integer relation on A. Among relations on D_N(A) which are
not cyclewise constant, the minimum height is exactly
ceil(lambda(A)/2). For the lower bound, some nonzero local divergence
vector is an A-relation of height at most twice the lifted height.
For the upper bound apply (7) to a minimizing input relation: its divergence
is nonzero at g=0. If A is rationally independent, every relation is
cyclewise constant.

### 5.2 Exact linewise integrability

An integer array q_v(g), with q(g) an A-relation at every vertex, is a
divergence of an integer f exactly when each q_v has sum zero along every
v-line. Necessity telescopes. For sufficiency, take cyclic cumulative sums
on each line; the zero-sum condition makes them consistent.

Under these zero-sum conditions, a ternary f with this divergence exists
exactly when those cumulative
sums on every line have oscillation at most two. Indeed each solution on
a line differs from its cumulative-sum solution by a constant integer.
Its values can be translated into {-1,0,1} precisely when max-minus-min
is at most two. This condition is stronger than the pointwise bound
|q_v(g)|<=2. An additional color-support requirement would demand that
the same translated profile vanish at every forbidden-color edge; that
condition is not supplied by integrability alone.

## 6. Rational-rank limitation for a fixed seed

The seam proof also holds with linear independence over any field K in
place of dissociation. Define

$$
 \alpha_K(A)=\min_{\varnothing\ne F\subseteq A}
                     \frac{\operatorname{rank}_K(F)}{|F|}.
$$

Then

$$
 \alpha_K(D_N(A))\geq(1-1/N)\alpha_K(A).
 \tag{9}
$$

Indeed choose a basis among the incoming types at each vertex, using the
input hereditary rank bound. A nonzero linear relation is excluded at its
maximal vertex just as in Section 2; this works also in characteristic two.

For a **fixed finite** nonzero integer seed, alpha_Q(A)>0. If
P=prod_j(1-1/N_j)>0, the matroid partition theorem therefore gives

$$
 \chi_1(A^{(k)})\leq\chi_{\mathbb Q}(A^{(k)})
 \leq\left\lceil\frac1{P\alpha_{\mathbb Q}(A)}\right\rceil
 \quad\text{for every }k.
 \tag{10}
$$

The relevant
[Edmonds statement](../../../../library/additive_combinatorics/edmonds_1965_minimum_partition_matroid_into_independent_subsets/_index.md)
is checked in the source: partition into m independent classes is possible
exactly when every subset has size at most m times its rank. Consequently the
summable-cost iteration cannot by itself turn **one fixed finite seed** into
unbounded chromatic numbers. Varying seeds with alpha_Q tending to zero,
including the uniformly extracting line families, are not excluded.

## 7. Exact remaining target

One possible sufficient theorem would produce, for each q, a uniformly
extracting seed and finitely many stages whose product loss is at least a fixed
positive constant and whose final chi_1 exceeds q. No such theorem follows from
(7). The
[valuation coloring theorem](../lemmas/difference_tower_color_limits.md)
actually disproves a universal small-loss comparison with seed rational
coloring: powers-of-p seeds have arbitrarily large rational coloring number, but
every small-loss tower stays exactly two-colorable. The same page shows that the
canonical height-halving witnesses contain complete cycles and can all be split
by two colors. These obstructions do not color line-seed towers.

A relation-dependent choice of lift and
an arbitrary subsequent coloring have different quantifiers.

Thus this route repairs the recorded extraction gap and supplies a new
arithmetic flattening mechanism, but the required arbitrary-color
amplification remains open.
