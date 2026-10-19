---
name: research/erdos_617/line_graph_obstruction
desc: A least color cannot be the line graph of any loopless multigraph, with unrestricted multiplicities.
tags: [graph-theory, constructions, matchings, proved]
sources: []
created: 2026-09-22T00:27:53Z
updated: 2026-10-14T00:26:52Z
---


# research/erdos_617/line_graph_obstruction

***

**Proved.** A least color in a hypothetical counterexample cannot be the
line graph of any loopless multigraph, with no multiplicity restriction.
The heavy-pair and final-triple arguments close the earlier
unrestricted-multiplicity gap.
This excludes a construction family, not arbitrary colorings; no reduction
of general least colors to line graphs is known.

Throughout, $r\ge3$, $N=r^2+1$, and $G$ satisfies

$$
\alpha(G)\le r,\qquad \omega(G)\le r,\qquad
e(G)\le\frac{rN}{2},\qquad
e(G[W])\le D_r(|W|)\quad(W\subseteq V(G)),
\tag{1}
$$

with $D_r$ and $p_r$ as in [the reductions](reductions.md). These are
necessary conditions for a least color.

## Matching reduction

Suppose $G=L(F)$, with $F$ a simple graph or loopless multigraph. Then

$$
e(F)=N,\qquad \nu(F)=\alpha(G)\le r,\qquad \Delta(F)\le r.
\tag{2}
$$

Here multiplicities are counted in degrees and edge counts. The last
inequality follows because the edges at any vertex of $F$ form a clique
in $L(F)$.

The Tutte--Berge formula is

$$
\nu(F)=\min_{S\subseteq V(F)}
\frac{|V(F)|+|S|-o(F-S)}2,
\tag{3}
$$

where $o$ counts odd-order components. Its statement and proof were checked in
Douglas B. West, *A short proof of the Berge--Tutte Formula and the
Gallai--Edmonds Structure Theorem*, European Journal of Combinatorics **32**
(2011), 674--676,
[Theorem 4, author preprint p. 3](https://dwest.web.illinois.edu/pubs/galledm.pdf).
West defines $\operatorname{def}(F)=\max_S(o(F-S)-|S|)$ and states
$\nu(F)=(|V(F)|-\operatorname{def}(F))/2$, exactly (3). For multigraphs, apply
this theorem to the underlying simple graph.

Choose a minimizing $S$. If $C$ ranges over the components of $F-S$,
then

$$
\nu(F)=|S|+\sum_C\left\lfloor\frac{|C|}{2}\right\rfloor.
\tag{4}
$$

Edges having an endpoint in $S$ number at most $r|S|$, and an even
component $C$ has at most $r|C|/2$ edges. Since $e(F)>r\nu(F)$, some
odd component must satisfy

$$
|C|=2a+1,\qquad m=e(C)=ar+b,\qquad
1\le a\le r,\qquad 1\le b\le\lfloor r/2\rfloor.
\tag{5}
$$

Otherwise summing the component bounds in (4) would give
$e(F)\le r\nu(F)$. The upper bound on $b$ follows from $\Delta(F)\le r$.
The vertices of $G$ corresponding to $E(C)$ induce exactly $L(C)$.

## Simple line graphs

Assume first that $F$ is simple. An adjacent pair of its edges has a
unique common endpoint, so Cauchy--Schwarz gives

$$
e(L(C))=\sum_{x\in C}\binom{d_C(x)}2
\ge\frac{2m^2}{2a+1}-m.
\tag{6}
$$

For the parameters in (5),

$$
2D_r(ar+b)=ar^2+a(a-2)r+b(b-1)+2ab.
\tag{7}
$$

We show that $a\le r-1$ makes (6) exceed this inherited cap. Put

$$
P(a,r,b)=2(2a+1)
\left(\frac{2(ar+b)^2}{2a+1}-(ar+b)-D_r(ar+b)\right).
$$

Direct expansion yields

$$
P(a,r,b)-P(a,r,1)
=(b-1)(-4a^2-2ab+8ar-6a+3b+2).
$$

Since $b\le r/2$ and $r\ge a+1$, the second factor is at least
$a(7r-4a-6)+3b+2>0$. Writing $t=r-a-1\ge0$ gives

$$
P(a,r,1)=3a^2+a+2+a(2a^2+a+6)t+a(2a-1)t^2>0.
$$

This proves the required strict violation. Hence $a=r$.

Equation (4) now forces $S=\varnothing$ and every other component of
$F$ to be a singleton. Thus all $N$ edges lie in $C$, of order $2r+1$.
By (6),

$$
e(G)\ge\frac{2N^2}{2r+1}-N>\frac{rN}{2},
$$

where the strict inequality is equivalent to

$$
4N-(r+2)(2r+1)=(2r-1)(r-2)>0.
$$

This contradicts (1) and proves the simple-line-graph obstruction.

## Bounded multiplicity

For a loopless multigraph, the correct edge identity is

$$
e(L(F))=\sum_x\binom{d_F(x)}2
-\sum_{xy}\binom{\mu_{xy}}2.
\tag{8}
$$

The subtracted term is essential: $C_5[K_t]$ is the line graph of a five-cycle
with edge multiplicity $t$. Therefore the preceding simple proof does not
already exclude the [local-cap counterfamily](local_cap_obstruction.md).

Assume every multiplicity is at most $h$ and $r\ge8h$. The matching
reduction still gives (5), and (8) implies

$$
e(L(C))\ge\frac{2m^2}{2a+1}-\frac{h+1}{2}m.
\tag{9}
$$

The case $a=1$ is impossible: any two edges of a loopless multigraph on
three vertices are incident, so $m\ge r+1$ would give a forbidden clique.
Thus $a\ge2$.

If $a\le r-2h$, define, on $0\le b\le r/2$,

$$
f(b)=\frac{2(ar+b)^2}{2a+1}
-\frac{h+1}{2}(ar+b)-D_r(ar+b),
$$

interpreting the last term by the polynomial (7). Its derivative

$$
f'(b)=\frac{4(ar+b)}{2a+1}-a-b-\frac h2
$$

decreases with $b$, and even at $b=r/2$ is
$3r/2-a-h/2>0$. Also

$$
f(0)=\frac{ar}{2}
\left(\frac{(2a-1)r}{2a+1}-a+1-h\right)>0,
$$

because $r\ge a+2h$ and

$$
(2a-1)(a+2h)-(2a+1)(a+h-1)=h(2a-3)+1>0.
$$

Thus inherited density forces $a>r-2h\ge3r/4$.

In particular $2a+1>r$, so $m\ge ar$ gives

$$
\frac{2m}{2a+1}-\frac{h+1}{2}
>r-\frac{h+3}{2}>0.
$$

Factoring (9) into $m$ times this positive bracket yields

$$
e(G)>r(r-2h)\left(r-\frac{h+3}{2}\right)
>\frac{r(r^2+1)}2.
$$

The final comparison follows from

$$
r^2-(5h+3)r+2h^2+6h-1>0:
$$

for $r\ge8h$, we have $r-5h-3\ge0$ and $2h^2+6h-1>0$.
This again contradicts (1).

Consequently all line-graph construction families with maximum
multiplicity $o(r)$ fail for sufficiently large parameters.

## Unrestricted multiplicity: constraints on a minimal odd core

The following established reductions are used in the unrestricted proof below,
which closes the concentration gap they leave. Within the component from
(5), choose an inclusion-minimal odd vertex set $U$ with

$$
|U|=2a+1,\qquad m=e(F[U])=ar+b>ar.
$$

Then $a\le r$ and $1\le b\le r/2$. All degrees below refer to $F[U]$.
Set

$$
\delta_u=r-d(u),\qquad \sum_{u\in U}\delta_u=r-2b.
\tag{10}
$$

Deleting any pair leaves a proper odd set, so minimality gives

$$
d(u)+d(v)-\mu_{uv}\ge r+b.
\tag{11}
$$


For $\mu=\mu_{uv}\ge1$, the two star cliques in $L(F[U])$ have orders
$r-\delta_u,r-\delta_v$, intersect in $\mu$ vertices, and their union
has $r+s$ vertices, where

$$
s=r-\delta_u-\delta_v-\mu\ge b\ge1.
$$

Its edge count is at least the sum of the two clique edge counts minus
$\binom\mu2$. Applying inherited density and using
$D_r(r+s)=\binom r2+\binom{s+1}{2}$ gives exactly

$$
(\mu-1)s\le\delta_u\delta_v.
\tag{12}
$$

If $\mu\ge2$, the concave quadratic
$(\mu-1)(r-\delta_u-\delta_v-\mu)$ has minimum
$r-\delta_u-\delta_v-2$ on
$2\le\mu\le r-\delta_u-\delta_v-1$. Thus

$$
(\delta_u+1)(\delta_v+1)\ge r-1
\qquad\text{whenever }\mu_{uv}\ge2.
\tag{13}
$$

In particular, parallel edges require substantial endpoint deficits,
while their total is only $r-2b$.

There is also an averaged edge lower bound. Include the whole star at
$u$, together with $\delta_u+1$ edges at $v$ not incident with $u$;
(11) ensures that enough exist. This $(r+1)$-set has at most
$(d(u)-\mu_{uv})(\delta_u+1)$ nonedges. The local cap therefore gives

$$
\mu_{uv}\le d(u)-\frac{r-1}{\delta_u+1}.
$$

Using this in (8) and averaging the endpoint bounds yields

$$
e(L(F[U]))\ge\frac14\sum_{u\in U}
\left(d(u)^2-d(u)+\frac{(r-1)d(u)}{r+1-d(u)}\right).
$$

The summand has second derivative
$2+2(r^2-1)/(r+1-d)^3>0$. Jensen's inequality consequently gives

$$
e(L(F[U]))\ge
\frac{m^2}{2a+1}-\frac m2+
\frac{(2a+1)(r-1)m}{2(2a+1+r-2b)}.
\tag{14}
$$

The next two reductions show that a surviving core must have $a<\sqrt{r/2}$.
Below that range the concentration argument in the final section applies.

### No degree-$r$ vertex in the minimal core

Suppose $d(u)=r$ for some $u\in U$. If $v$ is a neighbor of $u$,
(11) gives

$$
d(v)-\mu_{uv}\ge b\ge1.
$$

Thus an edge at $v$ exists outside the star at $u$. The latter star is a
$K_r$ in $G$, and an external vertex can have at most one neighbor in
such a clique. It follows that $\mu_{uv}=1$. The same property forbids
an edge between any two distinct neighbors of $u$: that edge would have
two neighbors in the star clique.

Hence $N_F(u)$ is an independent set of exactly $r$ vertices, and its
complement in $U$ is a vertex cover of size $2a+1-r$. Consequently

$$
ar+b=e(F[U])\le r(2a+1-r),
$$

which forces $a=r$ because $a\le r$ and $b>0$.

When $a=r$, (10) shows that at least

$$
(2r+1)-(r-2b)=r+2b+1\ge r+3
$$

vertices have degree $r$. Their star cliques have pairwise disjoint
edge sets in $L(F[U])$: each edge incident with a degree-$r$ vertex has
multiplicity one, so two such stars intersect in at most one vertex.
Therefore

$$
e(G)\ge(r+3)\binom r2>\frac{r(r^2+1)}2,
$$

the difference being $r(r-2)>0$. This contradicts (1).

Thus every vertex of the minimal core has degree at most $r-1$.
Equation (10) now yields

$$
2a+1\le r-2b\le r-2,\qquad a\le\frac{r-3}{2}.
\tag{15}
$$


### The core has $a<\sqrt{r/2}$

Let $L(b)$ denote the right side of (14), and set
$D(b)=D_r(ar+b)$. Regarding these as real functions on $1\le b\le r/2$,

$$
(L-D)'(b)=
\frac{2(ar+b)}{2a+1}-a-b+
\frac{(r^2-1)(2a+1)^2}{2(2a+1+r-2b)^2}>0.
$$

Indeed, the first three terms decrease with $b$ and at $b=r/2$
equal $r/2-a>0$ by (15). Thus it suffices to compare $L(1)$ and $D(1)$.

Put

$$
P=2(2a+1)(2a+r-1)\bigl(L(1)-D(1)\bigr).
$$

Expansion gives

$$
\frac Pr=
ar(2a^2+3a+7-r)-4a^4+5a^2-6a+2
-\frac{8a^3+8a^2-2a+2}{r}.
\tag{16}
$$

Suppose, contrary to the claimed bound, that $r\le2a^2$. Together
with (15), this puts $r$ in $[2a,2a^2]$. The concave function
$ar(2a^2+3a+7-r)$ has its minimum over this interval at an endpoint.
The endpoint at $2a^2$ exceeds that at $2a$ by
$2a^2(a-1)(a+7)\ge0$. Hence the first term in (16) is at least
$4a^4+2a^3+14a^2$.

Since $r\ge2a$ and $8a^3+8a^2-2a+2>0$, (16) now gives

$$
\frac Pr\ge
2a^3+15a^2-10a+3-\frac1a>0.
$$

Thus (14) exceeds inherited density, a contradiction. We conclude

$$
a<\sqrt{\frac r2}.
\tag{17}
$$


Combining this with the [hereditary span bound](hereditary_span_bound.md)
further restricts a possible core to

$$
\sqrt{\frac r{64}}<a<\sqrt{\frac r2}.
$$

For the lower bound, if $r\ge64a^2$, any $ar+1$ of the core's edge
vertices give an induced graph of independence at most $a$, contradicting
that theorem. This intermediate range is eliminated in the final section.

## Heavy near-perfect matchings in the root are excluded

Here $F$ is the minimal odd root above: $|F|=2a+1$,
$m=e(F)=ar+b$, $1\le b\le r/2$, and $\Delta(F)\le r$.
For $r\ge4$, it cannot have a matching $u_iv_i$, $1\le i\le a$,
whose multiplicities $\mu_i$ are all at least $r/2$.

Write

$$
t_i=\delta_{u_i}+\delta_{v_i},\quad
c_i=r-\mu_i,\quad s_i=c_i-t_i\ge b,\quad T=\sum_i t_i.
$$

The two-star cap (12) gives

$$
\delta_{u_i}\delta_{v_i}\ge(\mu_i-1)s_i\ge(r/2-1)b.
$$

Thus $t_i^2\ge2(r-2)b$ and
$t_it_j\ge2(r-2)b$. Every matched endpoint has positive
integer deficit, so $T\ge2a$. The unmatched vertex $z$ has
degree $T+2b$, by (10).

Call all pairs outside the matching light. The total light
multiplicity at $u_i$ is $\delta_{v_i}+s_i$, and vice versa.
Every light pair has at least one matched endpoint. Squaring these
residual degrees consequently gives

$$
\sum_{\text{light }uv}\mu_{uv}^2
\le\sum_i\bigl((\delta_{u_i}+s_i)^2+
(\delta_{v_i}+s_i)^2\bigr).
$$

Use the identity $2e(L(F))=\sum_v d(v)^2-\sum_{uv}\mu_{uv}^2-m$
to obtain

$$
\begin{aligned}
2e(L(F))\ge{}&ar^2+T^2-\sum_i t_i^2+4bT+4b^2\\
&+\sum_i s_i(2r-4t_i-3s_i)-ar-b.
\end{aligned}
$$

Since $t_i+s_i=c_i\le r/2$, the summands on the second
line are at least $s_i^2$. Also
$T^2-\sum_i t_i^2\ge2a(a-1)(r-2)b$. Subtracting the
inherited cap (7) gives

$$
\begin{aligned}
2e(L(F))-2D_r(ar+b)\ge{}&
a(a-1)((2b-1)r-4b)\\
&+4bT+3b^2-2ab+\sum_i s_i^2>0.
\end{aligned}
$$

The first bracket is nonnegative, and $T\ge2a$ makes the
remaining expression positive. This proves the exclusion without
using the least-color budget in this final step.

The minimal odd root is also **factor-critical**. If $F-z$ had
no perfect matching, Tutte's theorem would give a set $S$ with
$q=o(F-z-S)\ge|S|+2$. Put $K=S\cup\{z\}$ and $k=|K|$.
Each odd component $C$ of $F-K$ is a proper odd set, so minimality
gives $e(C)\le r(|C|-1)/2$; even components have at most
$r|C|/2$ edges. Edges incident with $K$ number at most $rk$.
Therefore

$$
m\le\frac r2(|F|+k-q)\le ar,
$$

a contradiction. This is the Tutte--Berge input already checked
above, applied to the underlying simple graph.

These two additional arguments were checked by the author and are
author-recorded. Heavy edges
form a matching because the root has maximum degree at most $r-1$.
The next argument forces all but three vertices into this matching and
then excludes that last possibility.

## Unrestricted multiplicities: concentration and the last three vertices

**Theorem.** No graph satisfying (1) is the line graph of a loopless
multigraph.

It remains to exclude the minimal odd root above. The case $a=1$ gives
a clique of order at least $r+1$ in its line graph. The case $a=2$ is
excluded by the hereditary independence-two span bound: any $2r+1$ edge
vertices have independence at most two. For $r=3$ it is already excluded
by (15). Thus assume

$$
a\ge3,\qquad r>2a^2,\qquad r\ge19.
$$

Call a root pair heavy if its multiplicity is at least $r/2$. These
pairs form a matching, of size $h\le a$. For each heavy pair $u_iv_i$
put

$$
t_i=\delta_{u_i}+\delta_{v_i},\quad
s_i=r-t_i-\mu_i\ge b,\quad c_i=t_i+s_i\le r/2,
\qquad T=\sum_i t_i,\quad S=\sum_i s_i.
$$

The two-star cap implies

$$
t_i^2\ge4\delta_{u_i}\delta_{v_i}
\ge4(\mu_i-1)s_i\ge2(r-2)b>(2a-1)^2.
$$

Since $t_i$ is integral, $t_i\ge2a$.

### At least $a-1$ heavy pairs

Write $Q=\sum_u\delta_u^2$. The exact line-graph identity and
$\sum_u\delta_u=r-2b$ give

$$
\sum_{uv}\mu_{uv}^2\ge
(a-1)r^2-a(a-1)r+Q+4br-b^2-2ab. \tag{18}
$$

This follows by rearranging

$$
2e(L(F))=\sum_ud(u)^2-\sum_{uv}\mu_{uv}^2-m
\le2D_r(ar+b).
$$

On the other hand, heavy pairs contribute
$hr^2-2r(T+S)+\sum_i c_i^2$. Light pairs have total multiplicity
$(a-h)r+b+T+S$, each less than $r/2$. Since $c_i^2\le rc_i/2$,

$$
\sum_{uv}\mu_{uv}^2\le
\frac{a+h}{2}r^2-r(T+S)+\frac{br}{2}. \tag{19}
$$

Combining (18)--(19) yields

$$
0\ge\frac{a-h-2}{2}r^2-a(a-1)r+r(T+S)+Q
+b\left(\frac{7r}{2}-b-2a\right). \tag{20}
$$

The last term is positive. If $h\le a-3$, the first two terms
already have positive sum, since $r>2a^2$. If $h=a-2$, then
$T\ge2a(a-2)$, and
$rT-a(a-1)r\ge a(a-3)r\ge0$. Both cases are impossible.
Therefore $h\ge a-1$. The heavy near-perfect matching lemma above
excludes $h=a$, leaving exactly $h=a-1$.

### Three unmatched root vertices

Let $Z$ be these three vertices, and write

$$
\tau=e(F[Z])=r-k,\qquad k\ge0.
$$

Here $k\ge0$ follows from minimality applied to the proper odd set $Z$.
For $z\in Z$, let $\ell_z$ count edges from $z$ to the matched
endpoints, with multiplicity, and put $B=\sum_{z\in Z}\ell_z$.
The total degree in $Z$ is $2r+2b+T$, so

$$
B=T+2b+2k.
$$

The residual degrees at matched endpoints are
$\delta_{v_i}+s_i$ and $\delta_{u_i}+s_i$, totaling $T+2S$.
Thus $k\le S-b$. The two-star cap also gives

$$
s_i\le\frac{t_i^2}{2(r-2)},\qquad
S\le\frac{rT}{4(r-2)}\le\frac{2T}{7},
\qquad 0\le k\le\frac{2T}{7}. \tag{21}
$$

The last numerical inequality holds for $r\ge16$.

Every light pair not contained in $Z$ has a matched endpoint. Its
squared multiplicity is therefore accounted for at least once in the
sum of squared residual degrees at matched endpoints. For a heavy
pair with endpoint deficits $x,y$, $t=x+y$, and parameter $s$,

$$
\begin{aligned}
&(r-x)^2+(r-y)^2-(r-t-s)^2-(y+s)^2-(x+s)^2\\
&\hspace{15mm}=r^2-t^2+s(2r-4t-3s)
\ge r^2-t^2+s^2,
\end{aligned}
$$

because $t+s\le r/2$. Consequently

$$
2e(L(F))\ge(a-1)r^2-\sum_i t_i^2+\sum_i s_i^2
+\sum_{z\in Z}d(z)^2-\sum_{uv\subset Z}\mu_{uv}^2-ar-b.
\tag{22}
$$

Let $w_z$ be the multiplicity on the pair opposite $z$ in $Z$,
allowing zero. Then $\sum_z w_z=\tau$ and
$d(z)=\tau-w_z+\ell_z$. Direct expansion gives

$$
\sum_{z\in Z}d(z)^2-\sum_{uv\subset Z}\mu_{uv}^2
=\tau^2+2\sum_z(\tau-w_z)\ell_z+\sum_z\ell_z^2.
$$

No pair in $Z$ is heavy, so $w_z<r/2$ and
$\tau-w_z\ge r/2-k$. By Cauchy--Schwarz the last display is at least

$$
(r-k)^2+(r-2k)B+\frac{B^2}{3}.
$$

Substitute $B=T+2b+2k$ into (22) and subtract (7). The resulting
lower bound for $2e(L(F))-2D_r(ar+b)$ is

$$
\begin{aligned}
&rT-a(a-1)r-\sum_i t_i^2
+\frac{T^2-2kT-5k^2}{3}\\
&\qquad+\frac{4b}{3}(T-k)+\frac{b^2}{3}
+2b(r-a)+\sum_i s_i^2. \tag{23}
\end{aligned}
$$

By (21), the quadratic term is at least $T^2/147$, and all the
following terms are nonnegative. Also

$$
\sum_i t_i^2\le\frac{rT}{2},\qquad
T\ge2a(a-1)>0.
$$

Thus (23) is at least

$$
\frac{rT}{2}-a(a-1)r+\frac{T^2}{147}>0,
$$

contradicting the hereditary cap. This finishes the unrestricted
multigraph proof.

## Checks and limitations

The simple and bounded-multiplicity proofs, (10)--(14), and the two core
reductions (15)--(17) were checked by the author and are author-recorded. The
unrestricted concentration and three-vertex argument were also checked by the
author; its three polynomial identities were verified symbolically as well as by
expansion. The earlier symbolic expansions were also checked directly. No random
or exhaustive construction search was used.

These arguments concern a **least** color: the global edge budget in
(1) is essential. They do not show that an arbitrary selected color
cannot be a line graph. Nor do they reduce general color graphs to line
graphs, or prove the corresponding statement for all claw-free graphs.

## Budget-free span for K_r-free line graphs

**Theorem.** If $J=L(F)$ is the line graph of a loopless multigraph,
is $K_r$-free, and satisfies every inherited upper cap, then

$$
|J|\le r\alpha(J).
$$

There is no restriction on $|J|$ or $\alpha(J)$, and no edge budget.

Suppose instead $e(F)>r\nu(F)$. The Tutte--Berge decomposition used
above supplies a minimal odd overfull root $U$, of order $2a+1$ with
$ar+b$ edges, $b\ge1$. Every root star is a clique, so now
$\Delta(F)\le r-1$ directly. Hence all deficits are positive and

$$
\sum_{u\in U}(r-d(u))=r-2b,\qquad 2a+1\le r-2b.
$$

This gives (15) without the degree-$r$-vertex argument, which was the
only use of the least-color budget in the unrestricted proof. The
Jensen estimate, the reduction $r>2a^2$, and the heavy-pair and final
triple inequalities then apply unchanged. They exclude every such
root, a contradiction. The small cases $a=1,2$ are treated as above.

Thus either normalized core would be excluded by a valid line-graph
reduction. The obstacle is not transferring the least-color budget;
it is obtaining that structural reduction. The theorem also yields
the general [odd-clique inequalities](clique_family_span.md).
