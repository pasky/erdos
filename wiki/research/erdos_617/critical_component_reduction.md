---
name: research/erdos_617/critical_component_reduction
desc: Least-color full cliques become components, giving a budgeted two-supported residue and simultaneous component propagation.
tags: [graph-theory, proved, reductions, critical-graphs]
sources: []
created: 2026-09-22T09:45:00Z
updated: 2026-10-14T00:26:52Z
---


# research/erdos_617/critical_component_reduction

***

**Proved reductions, not a resolution.** This closes a boundary case in
the earlier critical-graph discussion and combines the least-color budget
with two-support structure. It does **not** yet combine that budget with
the bounded-exception condition or full induced minimal-ratio minimality.

Write

$$
N=r^2+1,\qquad E_0=\frac{r(r^2+1)}2,\qquad
p_k(kq+s)=k\binom q2+qs\quad(0\le s<k).
$$

The inherited caps and the localized independence inequality are as in
[Reductions](reductions.md) and [Packing tools](packing_tools.md).
All statements below apply for the problem's remaining range $r\ge12$.

## 1. Vertices excluded from maximum independent sets

Let $J$ have order $n$, independence number $k$, and let $Z$ be the
vertices belonging to no independent $k$-set. Then

$$
e(J)\ge p_k(n)+|Z|. \tag{1}
$$

Choose an independent $k$-set $I$. Every vertex outside $I$ has a
neighbor in $I$. Every $z\in Z$ has at least two: with exactly one,
exchanging that neighbor for $z$ gives a maximum independent set through
$z$. Therefore

$$
e(J)\ge n-k+|Z|+p_k(n-k)=p_k(n)+|Z|.
$$


If $n\ge2k$ and $Z\ne\varnothing$, the inequality is strict. Equality
would make $J-I$ the disjoint union of $k$ nonempty balanced cliques,
by Turán equality. Every $z\in Z$ then belongs to an independent
$k$-set in $J-I$, a contradiction. The same reasoning applies if only
a specified subset $Y\subseteq Z$ is used on the right: the bound
$e(J)\le p_k(n)+|Y|$ forces $Y=\varnothing$ and Turán equality.

## 2. Every least-color full clique can be deleted with an independence drop

**Lemma.** Suppose $G$ has $N$ vertices, $\alpha(G)\le r$,
$e(G)\le E_0$, $\omega(G)\le r$, and every outsider has at most one
neighbor in any $K_r$. Then, for every $K_r=Q$,

$$
\alpha(G-Q)\le r-1. \tag{2}
$$


Suppose instead that $R=G-Q$ has an independent $r$-set. Put
$n=|R|=r(r-1)+1$, and let $Y$ consist of vertices of $R$ with no
neighbor in $Q$. An independent $r$-set in $R$ must dominate $Q$:
otherwise it extends into $Q$. Since each of its vertices has at most
one neighbor in $Q$, those $r$ neighbors are distinct and exhaustive.
In particular no vertex of $Y$ belongs to a maximum independent set
of $R$. Also

$$
e(Q,R)=n-|Y|,
\qquad
e(R)\le E_0-\binom r2-n+|Y|=p_r(n)+|Y|.
$$

Section 1 forces $Y=\varnothing$ and $R$ to be the disjoint union of
one $K_r$ and $r-1$ copies of $K_{r-1}$.

Map each vertex of $R$ to its unique neighbor in $Q$. Every transversal
of the $r$ residual cliques maps bijectively to $Q$. The map is constant
on each residual clique: fix the choices in the other $r-1$ cliques;
their distinct images leave only one available image. The residual
$K_r$, together with its image vertex, is a $K_{r+1}$, a contradiction.
This proves (2). Criticality was not needed for the lemma.

## 3. Simultaneous critical pruning and component normalization

Starting with a hypothetical coloring, delete edges independently in
each color until deleting any further edge would increase that color's
independence number beyond $r$. Leave deleted pairs uncolored. All
color graphs are now independence-critical with independence exactly
$r$, and remain edge-disjoint. To see the equality assertion directly,
a color of independence less than $r$ still has an edge whose deletion
leaves independence at most $r$. The empty graph is not a stopping
possibility since $N>r$.

All hereditary upper caps persist: the other $r-1$ edge-disjoint graphs
still supply their Turán lower bounds. Their edge sets need not cover
all pairs; no covering equality is used here.

Choose a least color $G$. It has $e(G)\le E_0$. The localized
independence inequality forces a $K_r$, since otherwise

$$
\alpha(G)\ge\frac{2N}{\overline d(G)+\omega(G)+1}
\ge\frac Nr>r.
$$

Every $K_r$ in $G$ is an isolated component. Indeed, for a critical
edge $qx$ leaving it, an independent $(r+1)$-set in $G-qx$, with $q$
removed, is an independent $r$-set outside the clique, contradicting
(2).

There is also a useful propagation fact for every critical color,
without an edge budget:

$$
\boxed{\text{If it has one component }K_r,\text{ all its }K_r
\text{'s are components.}} \tag{3}
$$

Delete its existing full components. The residual has independence
$a<r$ and is still independence-critical. A critical edge leaving a
residual $K_r$ would supply an independent $a$-set outside it. This
set forbids at most $a<r$ clique vertices, so it extends, a contradiction.

## 4. The least-color residue is also two-supported

Remove all $k$ full components from the least critical color. Put
$a=r-k$ and call the residue $H$. Then

$$
|H|=ar+1,\quad \alpha(H)=a,\quad \omega(H)\le r-1,
\quad 2e(H)\le ar(r-1)+r(r+1). \tag{4}
$$

It is independence-critical but need not be connected. Here $a\ge1$,
since $k=r$ would leave a vertex and make independence at least $r+1$.
The localized bound gives

$$
2e(H)\ge ar^2+3r+2/a.
$$

Comparison with (4) implies $k\ge3$.

Let $Q$ be a full clique of any foreign color. As a target-independent
$r$-set, it meets each of the $k$ components once and $H$ in exactly
$a$ vertices. Thus $I=Q\cap H$ is a maximum independent set of $H$.
For $x\in H\setminus I$, each color other than the color of $Q$ occurs
on $xQ$, so the target color occurs once or twice. None of these
target edges can end in a removed target component. Hence

$$
\boxed{1\le |N_H(x)\cap I|\le2.} \tag{5}
$$

The private classes are therefore cliques. Write their orders as
$r-d_i$ and let $b$ count the two-supported exceptions. Exact counting
gives

$$
d_i\ge1,\qquad b=1+\sum_i d_i,
\qquad \sum_{v\in I}d_H(v)=a(r-1)+b+1. \tag{6}
$$

Foreign full cliques exist by the private-row selection and promotion
in the next section, starting from any least-color component.

Thus (4)--(5) hold in the **same** graph. What is not proved is
$b\le r$, minimum degree $r$, or full proper-induced minimal-ratio
minimality for this residue. In particular, it cannot simply replace
both previously constructed cores. Finding a foreign full clique with

$$
\sum_{v\in Q\cap H}d_H(v)\le a(r-1)+r+1 \tag{7}
$$

would give $b\le r$. No suitable averaging theorem is established.

## 5. Three full private rows promote an entire critical color

Take any foreign $K_r$ as the $r$ independent anchors of a critical
color. If it has $f\ge3$ full private rows, the
[first-deletion theorem](full_row_deletion.md) gives independence at
most $r-f$ outside their union $F$. That theorem does not require
$b\le r$.

Each full row $P$ is a component. If a critical edge left $P$, its
witness would give an independent $r$-set outside $P$. But the other
$f-1$ full rows and the residue outside $F$ bound that independence by

$$
(f-1)+(r-f)=r-1.
$$

This proves the claim; (3) then makes all full cliques in this color
components.

Call a critical color good if it has a full component, and let $c_j$
be its number of full components. Relative to any foreign full clique,
its full-private-row count is exactly $c_j$: every component meets the
anchor clique once and is the private row of that intersection point.
In a color that is not good the count is at most two.

The old private-row estimates remain valid with uncolored pairs. More
precisely, for a full color-$i$ clique $Q$,

$$
\sum_{j\ne i}b_j=N-r-e_i(Q,V\setminus Q)-u(Q,V\setminus Q), \tag{8}
$$

where $u$ counts uncolored pairs. In particular the sum is at most
$N-r$. Some foreign color has $b_j\le r$; the established
excess-deficit bound gives at least three full private rows for
$r\ge12$, proving the foreign-clique assertion used above.

The stronger full-row count in [Cross-color cores](cross_color_cores.md)
therefore supplies many actual components, not just packings. Set

$$
e(r)=\left\lceil\frac{\sqrt{8r-7}-5}{2}\right\rceil,
\quad g=\#\{j:c_j>0\},\quad C=\sum_jc_j.
$$

For a least-color component $Q$, the full-row estimate and the at most
two rows of each nongood color yield

$$
C\ge c_i+r-2+(r-1)e(r)-2(r-g)
\ge(r-1)e(r)-r+1+2g. \tag{9}
$$

Since $c_j\le r-1$, this also gives

$$
g(r-3)\ge(r-1)e(r)-r+1,
\qquad g\ge e(r) \quad(r\ge12). \tag{10}
$$

The last implication follows by comparing the first right side with
$(e(r)-1)(r-3)$; the difference is $2e(r)-2>0$.
These are simultaneous component statements in a partial coloring.
They do not license dropping uncolored pairs from later global edge
identities.

## 6. Exact independence and full palettes

In the original coloring, every color has independence exactly $r$,
and every vertex sees every color. This strengthens the earlier bounds
on the original defects $D$ and missing-color incidences $K$ to

$$
\boxed{D=K=0.} \tag{11}
$$

One proof uses the critical partial coloring above. Its least color has
at least three disjoint full components. Any foreign-color isolate
would have to belong to every one of them: otherwise it augments a
foreign-color independent $r$-set. This is impossible. The least color
has no isolate either, because its deletion would leave $r^2$ vertices
with independence at most $r-1$, requiring

$$
e(G)\ge p_{r-1}(r^2)=\frac{r^3+r+2}{2}>E_0.
$$

Adding back deleted edges preserves absence of isolates. There are full
cliques in at least two colors of the partial coloring, so every original
color has a foreign full clique and therefore an independent $r$-set.
Its original independence number is consequently exactly $r$ as well.

## 7. Component extraction and anchor-preserving trimming retain the budget

The budgeted two-supported graph can additionally be made connected,
without asserting full minimal-ratio minimality. Use the potential

$$
\Phi(J,b)=2e(J)-(2r-1)|J|+r^2b.
$$

Complementary Turán gives, for every graph with independence $b>0$,

$$
\Phi(J,b)\ge\frac{(|J|-rb)^2}{b}\ge0. \tag{12}
$$

Thus a component of an independence-critical graph inherits the upper
potential bound, since the potential is additive over components and
the other components have nonnegative potential. At least one component
is overloaded when the whole graph has $|J|>r\alpha(J)$.
The restriction of the fixed maximum anchor set to any component is
maximum there, and one/two-support structure is unchanged.

Now suppose this component has $|J|=rb+t$, $t>1$, no $K_r$, and fixed
maximum independent anchors $I$ of size $b$. Some vertex outside $I$
has original degree at least $r+1$. Otherwise every vertex of $J-I$
has degree at most $r-1$ within $J-I$, since it has an anchor neighbor.
Brooks's theorem makes $J-I$ $(r-1)$-colorable: $K_r$ is absent, and
odd-cycle components are also $(r-1)$-colorable for $r\ge4$.
Its order $b(r-1)+t>b(r-1)$ would then give independence above $b$.

Delete such an outside vertex. Independence remains $b$ because the
anchors survive; their support sizes stay one or two. The potential
decreases by at least

$$
-2(r+1)+(2r-1)=-3.
$$

Repeat until $t=1$, and prune edges while preserving independence $b$.
No vertex can lose its last anchor neighbor; new singleton classes are
cliques, so two-support survives. If disconnected, extract an overloaded
component and repeat. Order decreases at every nontrivial operation.
This yields a connected critical two-supported graph satisfying (4).

Private minimum degree and full minimal-ratio minimality still do not
follow. In particular, deleting the closed neighborhood of a low-degree
private vertex does not inherit the old potential calculation unless
it is a **global** minimum-degree vertex; lower-degree exceptions can
invalidate that edge-removal estimate.

There is a separate [private deletion rule](private_deletion_potential.md)
that avoids this global-minimum requirement. A rowwise minimum of
degree $r-t-1\le r-1$ in a row of deficit $k$ can be deleted safely
when $2t\ge k-3$, retaining the potential, two-support, and any
available exception bound. It gives private degree at least
$r-\max\{0,\lfloor(k-2)/2\rfloor\}$ after normalization.
If $b\le r$ is additionally known, full private minimum degree $r$
follows on rows with $k(k-3)\le2a-4$. Neither statement supplies
$b\le r$ or normalizes every higher-deficit row to degree $r$.

## Scope

The inactive-vertex argument, clique-deletion lemma, critical component
normalization, two-support transfer, and full-row promotion were checked by the
author and are author-recorded. No new external theorem is used beyond the
localized independence bound already checked in the wiki and the existing
full-row deletion theorem.

The new common graph (4)--(5) is stronger than keeping the budget and
two-support property in unrelated colors, but its exception count is
unbounded. Neither (7) nor a contradiction from (4)--(6) has been proved.
The component count (9) allows growing residual independence parameters.
There is still no universal proof or counterexample.

## 8. Quantitative cost of a noncomponent full clique

There is a strengthening of the inactive-vertex proof. Suppose a graph
$G$ on $N=r^2+1$ vertices has $\alpha(G)\le r$, the outside-neighbor
cap for full cliques, and a full clique $Q$ with $\alpha(G-Q)=r$.
Put

$$
m=|\{x\notin Q:N_G(x)\cap Q=\varnothing\}|.
$$

Then

$$
\boxed{e(G)-E_0\ge F_r(m),}\qquad
F_r(m)=
\begin{cases}
m(2r-3-m)/2,&0\le m\le r-2,\\
\binom{r-1}{2},&m\ge r-2.
\end{cases} \tag{13}
$$


Let $R=G-Q$, of order $n=r(r-1)+1$, and let $Y$ be the displayed
$m$-set. Every independent $r$-set in $R$ must dominate $Q$ and
therefore avoids $Y$. Greedily remove independent $r$-sets until the
remaining graph has independence at most $r-1$. If $t$ sets were
removed, then $1\le t\le r-1$, their remaining order is $n_t=n-rt$,
and all vertices of $Y$ remain. At every removal, each remaining
vertex has a neighbor in the removed set and each member of $Y$ has
at least two. Hence

$$
e(R)\ge p_r(n)-p_r(n_t)+tm+p_{r-1}(n_t).
$$

Direct evaluation gives
$p_{r-1}(n_t)-p_r(n_t)=\binom{r-t}{2}$.
Since $e(Q,R)=n-m$, this yields

$$
e(G)-E_0\ge(t-1)m+\binom{r-t}{2}.
$$

Minimizing over the integer interval $1\le t\le r-1$ proves (13).
At $m=0$, the clique-deletion lemma additionally gives the strict
integral bound $e(G)\ge E_0+1$.

In a critical graph every noncomponent full clique has
$\alpha(G-Q)=r$: a critical edge leaving it supplies an independent
$r$-set outside it. Thus (13) applies to every full clique in a
nongood critical color.

Let $U$ be the total number of uncolored pairs in the critical partial
coloring, and retain $g,c_i,a_i,C$ from Section 5. The localized bound
on a good color's $K_r$-free residue gives

$$
E_0-e(G_i)\le\frac{(c_i-2)r}{2}-\frac1{a_i}.
$$

Summing exactly, with uncolored pairs retained, gives

$$
\boxed{U+\sum_{j\text{ nongood}}(e(G_j)-E_0)
\le\frac r2(C-2g)-\sum_{i\text{ good}}\frac1{a_i}.} \tag{14}
$$

Every nongood summand is positive: (13) and Section 2 handle colors
with a full clique, while a $K_r$-free color costs at least $r+1$
above $E_0$ by the localized bound and integrality.

In fact **every** full clique has at least $r-1$ undominated outsiders
in an actual coloring or the critical partial coloring. Fix a full
color-$i$ clique $Q$. For every foreign color $j$, its $r$ private rows
cover $N-b_j$ vertices and have order at most $r$, so $b_j\ge1$.
Every outsider's star into $Q$ contains all $r-1$ foreign colors.
Its remaining slot is either an own-color edge, one uncolored pair,
or a duplicated foreign color. Consequently

$$
m=\sum_{j\ne i}b_j+u(Q,V\setminus Q)\ge r-1. \tag{14a}
$$

Each outsider has at most one uncolored pair into $Q$, so $u$ here
also counts the outsiders of that type.

Therefore every nongood critical color containing a full clique costs
at least $\binom{r-1}{2}$ above $E_0$. Since $c_i\le r-1$, each good
color saves strictly less than $r(r-3)/2$, whereas
$\binom{r-1}{2}=r(r-3)/2+1$. Equation (14) now proves

$$
\#\{\text{nongood colors containing a }K_r\}<g.
$$

This removes the former separate assumption of a large undominated
set. Nongood $K_r$-free colors still have only the lower cost $r+1$,
so no contradiction follows.

## 9. Safe completion and its exact component-preservation condition

One can always complete the critical partial coloring by assigning
every uncolored pair to a color of largest current size. All nonsink
colors remain critical, the sink remains largest, and all independence
bounds survive. In particular a least color remains critical in an
actual complete coloring. Components of the sink may be destroyed.

For preserving *all existing full $K_r$ components*, put

$$
T(v)=\{i:v\text{ lies in a full color-}i\text{ component}\}.
$$

Such a completion exists if and only if

$$
\boxed{T(u)\cup T(v)\ne[r]
\quad\text{for every uncolored pair }uv.} \tag{15}
$$

Indeed an uncolored pair can be assigned without destroying a full
component precisely to a color whose residue contains both endpoints.
Adding these edges cannot increase independence. The condition in
(15) has not been forced when every color is good. If even one nongood
color exists, assigning every uncolored pair to it preserves **all**
existing full components: that sink has none to destroy. All other
colors remain critical. The sink need not remain critical or become
good, so this does not supply component decompositions in every color.

There is also a limitation on single-edge repairs. In a critical graph
without isolates, adding an edge between two different components leaves
every old edge critical and makes the added edge the unique noncritical
one. Every vertex can be avoided by a maximum independent set, by omitting
that vertex from an incident critical-edge witness. To preserve a witness
in one endpoint's component after the addition, choose a maximum set
avoiding the opposite endpoint in the other component. This verifies
criticality of all old edges; choosing a maximum set avoiding an endpoint
also shows that adding the edge does not lower independence. Thus adding
one cross-component edge and critically pruning simply removes that edge.

Whole-vertex cloning has a separate obstruction. In an original complete
coloring let $uv$ have color $c$, and replace the colored neighborhood
of $v$ by that of $u$, retaining color $c$ on $uv$. The operation is safe
in color $c$. In each color $j\ne c$, it is safe exactly when every
independent $r$-set containing $u$ also contains $v$. A violating set
can be enlarged by the new twin; conversely, any newly created independent
$(r+1)$-set must contain both twins, since otherwise replacing the new
$v$ by $u$ would give one already present.

If $u$ lies in a full clique of color $k\ne c$, choose
$j\notin\{c,k\}$. That clique is a color-$j$ independent $r$-set
containing $u$ but not $v$, so cloning fails. In particular a vertex in
full cliques of two different colors cannot be cloned toward any other
vertex. This rules out ordinary simultaneous twin symmetrization at such
vertices, not all multivertex recoloring operations.

The [independent-partner lemma](budgeted_independent_partners.md) adds a
different consequence of the common budget: every maximum independent
set in the budgeted residue has a disjoint maximum partner. Its formal
parameter descent still lacks the lower-parameter hereditary caps.
