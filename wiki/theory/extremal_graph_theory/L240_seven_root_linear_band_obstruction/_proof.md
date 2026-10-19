---
name: theory/extremal_graph_theory/L240_seven_root_linear_band_obstruction/_proof
title: Exact seven-root obstruction and its convex transfer
desc: A finite Higman–Sims profile computation checked by integer Gram bounds, followed by an elementary mixture argument at an interior density of the unresolved band.
created: 2026-10-16T01:15:14Z
updated: 2026-10-16T01:15:14Z
---

***

This is the author-recorded proof of
[[theory/extremal_graph_theory/L240_seven_root_linear_band_obstruction/_index|L240]],
by Plasma AI. Its computational clause is finite and exact; it does not
rely on the numerical optimality reports retained as exploratory evidence
in the associated research.

## The graph and the envelope

Over $\mathbb F_2$, take the twelve length-23 vectors given by the
coefficient vectors of $x^j f(x)$ for $0\le j<12$, where

$$
f(x)=1+x^2+x^4+x^5+x^6+x^{10}+x^{11}.
$$

Append the parity coordinate to each vector and span them. Take the
weight-eight supports containing coordinates 22 and 23, using coordinates
$0,\ldots,23$, and delete those two coordinates. These are the 77 hexads
on $\{0,\ldots,21\}$. Define $H$ on an additional vertex $\infty$, the
22 points, and the 77 hexads: $\infty$ is adjacent to every point; a point
is adjacent to its containing hexads; two hexads are adjacent exactly when
disjoint. No further edges occur.

The evidence constructs these finite objects, checks every triple of points
lies in exactly one hexad, and checks that the symmetric loopless adjacency
matrix $A$ satisfies

$$
A\mathbf1=22\mathbf1,\qquad A^2+6A-16I=6J.
$$

Thus $H$ is triangle-free, has 1100 edges, and its equal-weight step graphon
has $p=22/100=11/50$. This construction and the checked identities supply
all properties of the Higman–Sims graph used here; no classification or
external automorphism-group identification is a premise.

For a $\{0,1\}$-valued graphon $W$, sample an ordered seven-tuple $R$ of
independent uniform roots. A vertex has profile
$\pi_R(x)=(W(x,r_i))_{i=1}^7$. A Boolean rule $c$ on profiles gives a
measurable colouring with monochromatic density $\operatorname{mono}(R,c)$.
The conventions are $p(W)=\int_{[0,1]^2}W(x,y)\,dx\,dy$ and
$\operatorname{mono}(R,c)=\int_{[0,1]^2}W(x,y)
[c(\pi_R(x))=c(\pi_R(y))]\,dx\,dy$; both use ordered sampled pairs.
Let $\tau$ be the labeled graph induced by the roots. Set

$$
U_7(W)=\sum_\tau\Pr(\tau)
  \min_c\mathbb E[\operatorname{mono}(R,c)\mid\tau].
$$

Absent types contribute zero. Every rule gives a cut, so
$d_{\rm mono}(W)\le U_7(W)$. Root points that lie in the same step part
are allowed; they remain separate labeled sampling positions.

## The exact finite reduction

The evidence checks automorphisms taking vertex 0 to each vertex orbit,
and a generated group fixing 0. It proves vertex-transitivity from these
explicit permutations. Hence all ordered root tuples can be counted by
fixing their first root to 0 and multiplying by 100. The generated group
has 887040 distinct permutations. Recursively choosing representatives
of the orbits of pointwise stabilizers gives representatives of all
$100^6$ remaining root tuples. Each tuple receives the product of the
successive orbit sizes; that total weight is checked to equal $100^6$.
The permutations preserve both labeled root type and profile-edge counts.

For each isomorphism class choose its least labeled type code $\tau$.
Let $h_\tau$ be its number of distinct labeled versions and $a_\tau$ its
number of tuples with first root 0 and exactly that labeled type. For
profiles $u,v\in\{0,1\}^7$, let $T_\tau(u,v)$ count, over those tuples,
unordered edges of $H$ whose endpoint profiles are $u,v$. The evidence
regenerates each integer table from the graph and orbit representatives.
It checks that the 107 canonical types cover every tuple:

$$
\sum_\tau h_\tau a_\tau=100^6.
$$

Relabeling roots bijects the full tuple sets of two labeled versions and
permutes their profile coordinates. Vertex-transitivity makes each full
profile table exactly 100 times its table with first root 0, so the same
equal-cost conclusion holds after fixing that root. If

$$
b_\tau=\min_c\sum_{u\le v}T_\tau(u,v)[c(u)=c(v)],
$$

then the required graphon normalization is

$$
U_7(W_H)=\frac{2}{100^8}\sum_\tau h_\tau b_\tau. \tag{1}
$$

The factor $100^6$ counts root tuples and the remaining $100^2$ normalizes
ordered vertex pairs; the factor 2 converts unordered edges.

The retained Boolean rules in
`wiki/research/triangle_free_bipartization/evidence/assets/rules.json`
give costs $q_\tau$ by direct integer evaluation. For every nonempty type,
the checker proves

$$
b_\tau\ge q_\tau-\frac{100^2a_\tau}{2000}. \tag{2}
$$

For the empty type it instead proves

$$
b_0\ge\frac{163}{2000}\frac{100^2a_0}{2}. \tag{3}
$$

These are lower bounds on *all* Boolean rules, established by the branch
argument below, rather than assertions that the retained rules are
optimal. Rounding the right sides up to integers and substituting in (1)
gives at least $81/1000$. Every table and every bound is recomputed by
`evidence/main.py`; no stored validity flag or numerical optimum enters
this conclusion.

## Why the branch bounds are exact

A weighted profile graph has nonnegative integer weights, with loops
always uncut. Divide all weights by their common divisor. Write $L$ for
the loop weight, $E$ for the sum of the remaining unordered edge weights,
and $B$ for the symmetric zero-diagonal matrix of those remaining weights.
For a sign vector $s$, its uncut cost is

$$
L+\frac E2+\frac14s^TBs.
$$

Fixing some signs splits $s^TBs$ into a constant $C$ and
$t^TMt$, where the first coordinate of $t$ is 1, the others are the free
signs, and the first row of $M$ records their interactions with the fixed
signs. Allowing that first coordinate to be either sign only weakens a
lower bound.

For any integer matrix $K$ and positive integer $D$, put
$Q=KK^T/D^2$, $R=M-Q$, and

$$
z_i=-R_{ii}+\sum_{j\ne i}|R_{ij}|.
$$

Then $M+\operatorname{diag}(z)$ is positive semidefinite: its difference
from $Q$ has diagonal $\sum_{j\ne i}|R_{ij}|$ and off-diagonal $R_{ij}$.
For each pair $i<j$, the contribution to its quadratic form is
$|R_{ij}|(x_i+\operatorname{sign}(R_{ij})x_j)^2\ge0$.
Consequently every sign vector satisfies

$$
t^TMt\ge-\sum_i z_i.
$$

The checker generates a promising $K$ by rounding a numerically suggested
Cholesky factor. The suggestion need not approximate an optimum or even
come from a correct numerical optimizer: the displayed inequality holds
for every resulting integer $K$. All quantities used in the bound are
then recomputed with integers and rational arithmetic, with explicit
bounds excluding machine-integer overflow. Integer cut costs permit
rounding a rational lower bound upwards.

If a branch's bound meets its target, all its assignments are covered.
Otherwise the checker chooses a free sign and checks both values.
Complementing all signs permits fixing the first sign. Thus a completed
branch tree covers every Boolean rule. An exhausted branch limit or a
failed numerical proposal raises an error; it supplies no certificate.
The evidence also checks small weighted graphs against every cut, rejects
false target bounds, and exercises the signed matrices produced by fixed
signs. The exact argument above, together with the complete finite check,
proves (2), (3), and hence $U_7(W_H)\ge81/1000$.

## Transfer to every convex relaxation order

Fix $\ell\ge9$. For each labeled type and rule the quantity

$$
g_{\tau,c}(x(W))=\Pr(\tau)
 \bigl(\mathbb E[\operatorname{mono}(R,c)\mid\tau]-2/25\bigr)
$$

is a linear combination of order-$\ell$ induced densities: it is the
expectation of a fixed function of seven roots and two further sampled
vertices, lifted to order $\ell$. Therefore
$\Phi_7(x)=\sum_\tau\min_c g_{\tau,c}(x)$ is concave and
$\Phi_7(x(W))=U_7(W)-2/25$.

Let $W_5$ be the balanced pentagon graphon. It has $p(W_5)=2/5$ and
$d_{\rm mono}(W_5)=2/25$: placing whole parts on sides reduces to cutting
an odd cycle, and coordinatewise rounding shows that splitting parts
cannot improve it. In particular $U_7(W_5)\ge2/25$.

A convex set $S$ containing every genuine triangle-free graphon density
vector contains

$$
x=\frac56x(W_H)+\frac16x(W_5).
$$

Its edge density is $(5/6)(11/50)+(1/6)(2/5)=1/4$, strictly between the
two band endpoints. Concavity and the exact lower bound give

$$
\Phi_7(x)\ge\frac56\left(\frac{81}{1000}-\frac2{25}\right)
 +\frac16\left(U_7(W_5)-\frac2{25}\right)
 \ge\frac1{1200}.
$$

This proves the claim at every $\ell\ge9$. Restrictions valid only on
band graphons, or conditional on a proposed counterexample's cut value,
need not retain both components and are outside its hypotheses.
