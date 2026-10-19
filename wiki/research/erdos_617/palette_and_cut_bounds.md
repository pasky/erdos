---
name: research/erdos_617/palette_and_cut_bounds
desc: The global defect budget 5D+4K<r bounds deficient independence numbers and all missing vertex-color incidences.
tags: [graph-theory, proved, color-coupling]
sources: []
created: 2026-09-22T08:00:00Z
updated: 2026-10-14T00:26:52Z
---


# research/erdos_617/palette_and_cut_bounds

***

**Superseded.** The
[critical-component reduction](critical_component_reduction.md) proves $D=K=0$
for the original coloring: every color has independence exactly $r$, and every
vertex sees every color. The weaker palette estimates below remain valid but are
superseded. Their residual
counting arguments are retained separately from this stronger conclusion.

**Proved necessary conditions, not a resolution.** These strengthen Section 6 of
the [second independent input](independent/clique_residue_and_affine_repair.md).
Throughout an $r$-coloring of $K_{r^2+1}$, $r\ge3$, has $\alpha(G_i)\le r$ in
every color. Write $p_a(n)$ for the minimum edge count of an $n$-vertex graph
with independence at most $a$: if $n=aq+b$, $0\le b<a$, then
$p_a(n)=a\binom q2+qb$.

## A coupled minimum-degree decomposition

More generally, consider a complete-graph coloring on $n$ vertices
with independence upper bounds $a_1,\ldots,a_r\ge1$. Fix color $i$.
Repeatedly choose a minimum-degree vertex in its current induced
residual and remove its closed neighborhood $A$. If $s=|A|$, at
least

$$
\sum_{x\in A}d(x)-e_i(A)
\ge s(s-1)-e_i(A)
=\binom s2+\overline e_i(A)
\ge f_i(s):=\binom s2+\sum_{j\ne i}p_{a_j}(s)
\tag{1}
$$

color-$i$ edges are removed at this step. Degrees in (1) are in
the current residual, not the original graph. The selected vertices
are independent, so there are at most $a_i$ blocks.

Pad their sizes with zeros to $a_i$ entries. The discrete increments

$$
f_i(s+1)-f_i(s)=s+\sum_{j\ne i}\lfloor s/a_j\rfloor
$$

are nondecreasing. Balancing the entries therefore minimizes their
total cost. If $n=a_i u+v$, $0\le v<a_i$, this proves

$$
\boxed{e(G_i)\ge(a_i-v)f_i(u)+vf_i(u+1).} \tag{2}
$$

This uses the other colors on every block, rather than just their
contribution to the $(r+1)$-vertex cap.

## The incident palette is larger than four fifths of all colors

Fix a vertex $v$, let $q$ colors be absent there, and put $k=r-q$.
On the other $r^2$ vertices every absent color has independence at
most $r-1$, and every present color has independence at most $r$.
For a missing color the balanced block sizes in (2) are one $r+2$
and $r-2$ copies of $r+1$. For a present color they are $r$
copies of $r$. Thus

$$
\begin{aligned}
e(G_i-v)&\ge\frac{r^3+r+2}{2}+(q-1)(2r-1)+kr
&&\text{if $i$ is absent},\\
e(G_i-v)&\ge\frac{r^3-r^2}{2}+qr
&&\text{if $i$ is present}.
\end{aligned} \tag{3}
$$

For $r\ge4$, the other-missing-color contribution to the first
line is exactly $(r-2)p_{r-1}(r+1)+p_{r-1}(r+2)=2r-1$.
For $r=3$ that expression is six, larger than $2r-1=5$, so
the displayed lower bound remains valid.

Sum (3) and compare with $\binom{r^2}{2}$ to obtain

$$
\boxed{q(5r^2-3r+4-2q)\le r^2(r-1).} \tag{4}
$$

Since $q\le r$, the coefficient on the left is at least
$5r(r-1)+4$. If $q\ge r/5$, (4) is impossible. Consequently

$$
\boxed{k>4r/5.} \tag{5}
$$

The decomposition, convexity, and summation were independently
checked. There is no conclusion that every vertex sees every color.

### Comparison with the independent square-root bound

The independent argument is valid under its weaker single-graph
hypotheses. For a graph on $r^2$ vertices of independence at most
$r-1$, the same greedy decomposition gives
$e(G)\ge\sum_j[\binom{s_j}{2}+h_j]$, where $h_j$ counts
nonedges within a removed block. Put $a_j=s_j-r$ after padding
to $r-1$ blocks, so $\sum a_j=r$. If $m$ entries are positive,
then $\sum a_j^2\ge r^2/m$, and the local cap gives
$h_j\ge r-1$ at each positive entry. It follows that

$$
e(G)-p_{r-1}(r^2)
\ge r\sqrt{2(r-1)}-\frac{r+2}{2}.
$$

Summing this over missing colors yields the input's
$(2\sqrt2+o(1))\sqrt r$ incident-palette bound. Equations
(1)--(5) are stronger for actual colorings, because their block
cost uses all the other independence bounds simultaneously.

## Colors across a cut

Let $X,Y$ be disjoint nonempty sets, of sizes $x,y$, and suppose
$a$ colors are absent between them. For an absent color its two
independence numbers sum to at most $r$. The continuous Turán
bound and Cauchy--Schwarz give

$$
2e_i(X)+2e_i(Y)\ge (x+y)^2/r-(x+y).
$$

For another color the corresponding lower bound is
$(x^2+y^2)/r-(x+y)$. Summing, using the exact internal edge
partition, gives

$$
\boxed{a\le\frac{r(r-1)}2\left(\frac1x+\frac1y\right).} \tag{6}
$$

In particular a balanced bipartition of the **entire** vertex set
uses at least $r-1$ colors: substitute
$x=\lfloor(r^2+1)/2\rfloor$, $y=\lceil(r^2+1)/2\rceil$
to make the right side strictly smaller than two. This is not
a claim about arbitrary small equal-sized disjoint sets.

For $x=y=r+t$ with $1\le2t\le r$, let $k$ colors occur across
the cut. Each such color needs at least $2p_r(r+t)=2t$ internal
edges. In an absent color, the disjoint union of its graphs on
the two sides has independence at most $r$, so needs at least
$p_r(2r+2t)=r+4t$ edges. Therefore

$$
\boxed{k(r+2t)\ge r(2t+1)+t-t^2.} \tag{7}
$$

This verifies the input's rounded cut bound. These inequalities
exclude bounded incident palettes and some fixed-template blowups;
they do not force either remaining core into the range of an
established exclusion theorem.

There is one further rounding improvement when $r=2u+1$ is odd
and $t=u$. Equality in the absent-color bound would require the
disjoint union on the two sides to be the Turán minimizer with
$2u$ clique components of order three and one of order two.
One side contains no order-two component, so its order would be divisible
by three, contrary to $r+t=3u+1$. Each absent color therefore
costs at least one more edge. The strengthened inequality is

$$
k(r+2t+1)\ge r(2t+2)+t-t^2.
$$

The added edge is attainable as a two-side graph bound by using
balanced unions of respectively $u$ and $u+1$ cliques on the
two sides. This is a bound on one cut, not a coloring construction.

## A global independence and palette defect budget

**Proved, author-recorded.** A further consequence of
the coupled block cost is much stronger than an individual
vertex-palette estimate. Put

$$
d_i=r-\alpha(G_i),\qquad
k_i=|\{v:d_{G_i}(v)=0\}|,\qquad
D=\sum_i d_i,\quad K=\sum_i k_i.
$$

Thus $K$ counts missing vertex--color incidences, with multiplicity.
Then

$$
\boxed{5D+4K<r.} \tag{8}
$$

In particular at least
$r^2+1-\lfloor(r-1)/4\rfloor$ vertices see every color,
and at most $\lfloor(r-1)/5\rfloor$ colors have independence
number below $r$. These are necessary conditions, not a
contradiction.

### A preliminary linear bound

Write $\ell_i=d_i+k_i$, $L=D+K$. Removing the $k_i$ isolated
vertices of color $i$ leaves $N-k_i$ vertices of independence
$a_i=r-\ell_i\ge1$, where $N=r^2+1$. Positivity follows
because the original graph cannot be edgeless. Every other
color still has independence at most $r$.

Apply (1) with the common block cost
$f(s)=\binom s2+(r-1)p_r(s)$. For integer $s\ge0$,

$$
\binom s2\ge rs-\frac{r(r+1)}2,\qquad
p_r(s)\ge s-r.
$$

Thus

$$
f(s)\ge(2r-1)s-\frac{3r^2-r}{2}.
$$

There are at most $a_i$ nonempty blocks. Summing this supporting
line gives

$$
e(G_i)\ge p_r(N)+r-1
+\frac{3r^2-r}{2}\ell_i-(2r-1)k_i.
$$

Comparison of the sum with the complete edge count yields

$$
(3r^2-r)L-(4r-2)K\le r(r-1)(r-2).
$$

Since $K\le L$,

$$
L\le\frac{r(r-2)}{3r-2}<\frac{r-1}{3}. \tag{9}
$$


### A common residual when K is positive

Suppose $K\ge1$. Delete every vertex isolated in some color,
then additional vertices as needed so that exactly $K$ vertices
are deleted. This is possible even if the isolate sets overlap.
The common residual has

$$
n=r^2+1-K,\qquad \alpha(G_i[W])\le a_i=r-\ell_i.
$$

Indeed an independent set in this residual can be united with
all the original $k_i$ color-$i$ isolates.

In the balanced block decomposition for color $i$, the cost
from color $j$ is at least
$[n-a_i a_j]_+$, using $p_{a_j}(s)\ge[s-a_j]_+$
and convexity. The own-color binomial cost is $p_{a_i}(n)$.
Consequently

$$
e(G_i[W])\ge p_{a_i}(n)+\sum_{j\ne i}[n-a_i a_j]_+.
\tag{10}
$$

Only this lower bound is needed; no equality assertion about
the block costs is required.

Both terms are minimized by spreading the $L$ units of
defect over $L$ distinct colors. For the first term, use

$$
p_a(n)=\max_{t\ge0,\ t\in\mathbb Z}
\left(tn-\frac{a\,t(t+1)}2\right),
$$

which is convex as a function of $a$, hence also of $\ell=r-a$.
Discrete convexity gives

$$
\sum_i p_{a_i}(n)\ge(r-L)p_r(n)+Lp_{r-1}(n).
\tag{11}
$$


For the pair term, let $q$ count positive $\ell_i$ and put
$S_2=\sum_i\ell_i^2$. A pair with both defects zero has
$n-a_i a_j=1-K\le0$. Every other pair has this expression
positive, since $a_i a_j\le r(r-1)$ and $K<r$.
Expansion therefore gives

$$
\begin{aligned}
\sum_{i\ne j}[n-a_i a_j]_+
={}&r(r-1)(1-K)+2r(r-1)L-L^2+S_2\\
&+(K-1)(r-q)(r-q-1).
\end{aligned}
$$

Here $S_2\ge L$, $q\le L$, and $K-1\ge0$.
The minimum is therefore attained at $L$ unit defects, and is

$$
2L(r-L)(r+1-K)+L(L-1)(2r-K). \tag{12}
$$

The integer bound (9) ensures $L<r$, as needed for this
comparison configuration.

For the base terms,

$$
p_r(n)=\frac{(r-1)(r^2+2-2K)}2,\qquad
p_{r-1}(n)\ge\frac{r(r^2+3-2K)}2.
$$

The latter follows by taking $t=r$ in the preceding maximum
formula; it loses one edge when $K=1$ and is exact for
$K\ge2$ in this range. Summing (10), substituting (11)--(12),
and comparing with $\binom n2$ gives

$$
P(r,K,L)\ge0, \tag{13}
$$

where

$$
\begin{aligned}
P(r,K,L)={}&r^3-(5L+1)r^2+(4KL-2K-L+2)r\\
&+K^2-2KL^2-K+4L^2-2L.
\end{aligned}
$$


### The polynomial comparison

For $0\le K,L<r/3$, the derivative

$$
P_L=-5r^2+(4K-1)r-4KL+8L-2
$$

is negative. At $L_0=(r+K)/5<r/3$,

$$
\begin{aligned}
25P(r,K,L_0)={}&-2K^3+16K^2r+29K^2-7Kr^2\\
&-47Kr-35K-26r^2+40r<0.
\end{aligned}
$$

For the strict sign use $K<r/3$:
$16K^2r-7Kr^2\le-5Kr^2/3$,
$29K^2-47Kr\le-112Kr/3$, and
$-26r^2+40r<0$ for $r\ge3$.
Thus (13) forces $L<L_0$, or $5L-K=5D+4K<r$.

If $K=0$, use the whole vertex set. All pair expressions
$N-a_i a_j$ are positive, and the same convex spreading
gives directly

$$
R(L):=r(r-1)(r-2)-L(5r^2-3r+6)+2L^2\ge0.
$$

This polynomial decreases on $0\le L<r/3$, while
$R(r/5)=-2r(29r-10)/25<0$. Hence $5L=5D<r$.
This completes the proof of (8).

The initial bound, common deletion, defect spreading, and two
polynomial comparisons were checked by the author and are
author-recorded. This is a
side result of the later investigation, using the already
established block method; it is distinct from the new
[semidefinite critical-witness approach](critical_semidefinite_gap.md).

## A common-deletion bound for maximum independent sets

**Proved necessary condition.** The preceding argument extends from
isolated vertices to an arbitrary common deletion. Let $X$ be a vertex
set, put $m=|X|$, and define

$$
L_X=\sum_{i=1}^r\bigl(r-\alpha(G_i-X)\bigr).
$$

For $1\le m\le r$, one has

$$
\boxed{
r^3-(5r^2-4mr)L_X-2mL_X^2>0.
} \tag{14}
$$

In addition,

$$
\boxed{5L_X-m<r\qquad(1\le m\le r/3).} \tag{15}
$$

In particular, deleting any $r$ vertices decreases the sum of the
color independence numbers by less than $r/2$. Equivalently, this
total decrease is at most $\lfloor(r-1)/2\rfloor$. The interpretation
as a decrease uses the stronger result $\alpha(G_i)=r$ for every
original color, proved in the
[critical-component reduction](critical_component_reduction.md).
For $X=\varnothing$, that result gives $L_X=0$ directly.

These inequalities bound simultaneous vertex sets meeting every maximum
independent set in several colors. They do not prove that a violating
common deletion exists.

### Preliminary bound and the exact polynomial

Write $W=V\setminus X$, $n=r^2+1-m$, $a_i=\alpha(G_i[W])$,
$\ell_i=r-a_i$, and $L=\sum_i\ell_i=L_X$. All $a_i$ are positive.
The continuous Turán bound, summed over the exact edge partition on
$W$, gives

$$
\sum_i\frac1{a_i}\le\frac{n+r-1}{n}.
$$

Cauchy--Schwarz therefore implies

$$
\frac{r^2}{r^2-L}\le\frac{n+r-1}{n},\qquad
L\le\frac{r^2(r-1)}{r^2+r-m}\le r-1<r. \tag{16}
$$

Thus spreading the $L$ integral defect units over distinct colors is
an available comparison configuration; no preliminary isolate bound
is needed.

Apply the coupled block estimate (10) on $W$:

$$
e(G_i[W])\ge p_{a_i}(n)
 +\sum_{j\ne i}[n-a_i a_j]_+.
$$

The convex representation of $p_a(n)$ used in (11) gives

$$
\sum_i p_{a_i}(n)\ge(r-L)p_r(n)+Lp_{r-1}(n).
$$

For completeness, the pair term is also minimized by unit defects.
Let $q$ count positive $\ell_i$, and let $S_2=\sum_i\ell_i^2$.
A pair with both defects zero has $n-a_i a_j=1-m\le0$;
every other pair has this expression positive, since $m\le r$.
Consequently

$$
\begin{aligned}
\sum_{i\ne j}[n-a_i a_j]_+
={}&r(r-1)(1-m)+2r(r-1)L-L^2+S_2\\
&+(m-1)(r-q)(r-q-1).
\end{aligned}
$$

Here $S_2\ge L$, $q\le L<r$, and $m-1\ge0$. Substituting the
unit-defect comparison therefore yields the lower bound

$$
2L(r-L)(r+1-m)+L(L-1)(2r-m).
$$

Throughout $1\le m\le r$,

$$
p_r(n)=\frac{(r-1)(r^2+2-2m)}2,\qquad
p_{r-1}(n)\ge\frac{r(r^2+3-2m)}2.
$$

The second estimate is the supporting line with integer parameter
$t=r$ in the maximum formula for $p_a(n)$; it loses one edge at
$m=1$ and is exact for $2\le m\le r$.

Summing the edge lower bounds and comparing with $\binom n2$ gives
the same polynomial as in (13), now with an arbitrary deletion size:

$$
\boxed{P(r,m,L)\ge0,} \tag{17}
$$

where

$$
\begin{aligned}
P(r,m,L)={}&r^3-(5L+1)r^2+(4mL-2m-L+2)r\\
&+m^2-2mL^2-m+4L^2-2L.
\end{aligned}
$$


### Polynomial comparisons

For $1\le m\le r$, the polynomial is strictly decreasing in $L$
on $0\le L\le r$, because

$$
P_L=-5r^2+(4m-1)r+(8-4m)L-2<0.
$$

If $m\ge2$, drop the nonpositive $L$ term and use $m\le r$;
if $m=1$, use $L\le r$ to obtain
$P_L\le-5r^2+7r-2<0$.

At $L_0=(2r+3m)/10$ one has the exact evaluation

$$
\begin{aligned}
100P(r,m,L_0)=-2\bigl[&3m(m-r)(3m-13r)
 +m(91r-68m)\\
&+80m+52r^2-80r\bigr]<0.
\end{aligned}
$$

Indeed the first term in brackets is nonnegative for $m\le r$,
the second is positive, and $52r^2-80r>0$ for $r\ge3$.
Together with (16)--(17), monotonicity gives

$$
10L-3m<2r,\qquad L<r/2. \tag{18}
$$


Let

$$
F(r,m,L)=r^3-(5r^2-4mr)L-2mL^2.
$$

The remaining terms satisfy

$$
\begin{aligned}
P-F
&=4L^2-(r+2)L-r^2+2r+m^2-2mr-m\\
&\le4L^2-(r+2)L-r^2+2r<0
\end{aligned}
$$

for $0\le L\le r/2$. For the last strict sign, the expression is
convex in $L$, and its endpoint values are $-r^2+2r$ and
$-r^2/2+r$, both negative for $r\ge3$. Thus (17) implies
$F>0$, proving (14).

Finally suppose $m\le r/3$. At $L_1=(r+m)/5$, the exact evaluation
already used for the isolate argument reads

$$
\begin{aligned}
25P(r,m,L_1)={}&-2m^3+16m^2r+29m^2-7mr^2\\
&-47mr-35m-26r^2+40r<0.
\end{aligned}
$$

The strict sign follows from
$16m^2r-7mr^2\le-5mr^2/3$,
$29m^2-47mr\le-112mr/3$, and
$-26r^2+40r<0$. Monotonicity and (17) give $L<L_1$, proving
(15). No hypothesis about isolated vertices or original independence
defects is used in this common-deletion proof.
