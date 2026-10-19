---
name: research/erdos_617/symmetry_obstructions
desc: Vertex-transitive colorings and, for r at least 100, all one-point extensions transitive on the other vertices are impossible.
tags: [graph-theory, proved, constructions, symmetry]
sources: []
created: 2026-09-22T05:15:00Z
updated: 2026-10-14T00:26:52Z
---


# research/erdos_617/symmetry_obstructions

***

**Main exclusion.** Section 3 excludes every one-point extension transitive on
the $r^2$ old vertices for $r\ge100$, without assuming a regular or
abelian action. It supersedes the abelian restriction in Section 2.

**Construction-family exclusions, not positive cases of the unrestricted
problem.** Set $N=r^2+1$. A hypothetical counterexample has
$\alpha(G_i)\le r$ for every color. A least color contains a $K_r$,
by the checked localized independence inequality in
[Packing tools](packing_tools.md). Distinct monochromatic $K_r$'s
have disjoint edge sets, even when their colors differ.

## 1. No vertex-transitive action, even with permuted colors

Suppose a group $\Gamma$ acts transitively on vertices and permutes
the colors. Choose a full clique in a least color and let its
$\Gamma$-orbit have $M$ members. Transitivity gives a common vertex
incidence $t$ and

$$
rM=Nt.
$$

Since $\gcd(r,N)=1$, $N\mid M$. Edge disjointness gives

$$
M\binom r2\le\binom N2,
\qquad M\le\frac{Nr}{r-1}<2N.
$$

Thus $M=N$. If $\ell$ is the orbit size of the chosen color, its
$\ell$ isomorphic least colors each contain $N/\ell$ of these
cliques. Hence

$$
\ell\mid N,\qquad
\frac{N}{\ell}\binom r2\le\frac{rN}{2},
\qquad r-1\le\ell\le r.
$$

For $r\ge4$, neither $r$ nor $r-1$ divides $N$:
$N\equiv1\pmod r$ and $N\equiv2\pmod{r-1}$.

For $r=3$, necessarily $\ell=2$. These two least colors each
have at least 15 edges, so all three colors have exactly 15 edges.
The remaining color is $\Gamma$-invariant and thus 3-regular on
ten vertices. Its forbidden $K_4$ and Brooks's theorem yield an
independent four-set, again a contradiction.

This excludes all vertex-transitive constructions, not merely those
in which translations preserve each individual color graph.

## 2. Abelian-equivariant one-point extensions

**Theorem.** Let $r\ge101$ and let $A$ be any abelian group of order
$r^2$. There is no counterexample on $A\cup\{\infty\}$ equivariant
under the regular action of $A$ on itself, fixing $\infty$ and possibly
permuting colors. No old-edge coloring is prescribed.

This strengthens the earlier prime-field exclusion to every abelian
regular action of the stated order, including all prime-power affine
translation actions. It still excludes only a construction family.

### The star action must be transitive on colors

Let $t$ be the number of colors used at $\infty$. These colors form one
orbit of the color action. The localized independence bound gives

$$
2e(G_i)\ge L:=r^3-r^2+3r-1+2/r
$$

for each star color. For any nonstar color, $\infty$ is isolated, so its
old graph has independence at most $r-1$. Applying the same bound to
its $r^2$ old vertices gives

$$
2e(G_j)\ge U:=r^3+r^2+\frac{2r^2}{r-1}.
$$

Here the clique-number bound is $r$ in both applications. Since
$U>L$, if $t\le r/2$ then

$$
\sum_i2e(G_i)\ge\frac r2(L+U)>r^4+r^2,
$$

contrary to the total edge count. Thus $t>r/2$.

Suppose $t<r$. The common stabilizer $H$ of a star color has order
$h=r^2/t$, where $r<h\le2r-2$ (the upper bound follows from
$t\ge\lfloor r/2\rfloor+1$). Consider a full clique $Q$ of a star
color. If a nonzero $s\in H$ stabilizes $Q$, then $Q$ lies in one
$H$-coset: for any $x,y\in Q$, the edges $\{x,x+s\}$ and
$\{y,y+s\}$ have the same color, so the translation $y-x$ fixes
that color and belongs to $H$. All $H$-translates of $Q$ then lie in
one $h$-set. Any two intersect in at least $2r-h\ge2$ vertices, so
are equal by full-clique intersection rigidity. This would make $Q$
$H$-invariant, impossible because $h>r$.

A full clique containing $\infty$ cannot occur either. Its translation
stabilizer acts freely on its $r-1$ old points, so its order divides
both $r-1$ and $r^2$ and is one. Its $r^2$ distinct translates would
use $r^2(r-1)>r^2$ distinct edges at $\infty$.

Consequently a star-color full clique, if one existed, would have
trivial stabilizer in $A$: its stabilizer must preserve its color and
therefore lie in $H$. Its $r^2$ translates consume
$r^2\binom r2$ pairwise disjoint edges, all in star colors. Only
$r^2(r+1)/2$ edges remain, fewer than $U/2$ needed by even one
nonstar color. Thus no star color contains a full clique.

Using clique number at most $r-1$ improves its bound to

$$
2e(G_i)\ge L'=r^3+3r+2/r.
$$

For $r\ge3$, $U>L'$, so already
$\sum_i2e(G_i)\ge rL'>r^4+r^2$, a contradiction. We have proved
$t=r$. Hence $H$ has order $r$, fixes every color, and every color
has exactly $r(r^2+1)/2$ edges.

### A free orbit gives an independent transversal

No full clique contains $\infty$, as proved above. If every full
clique were $H$-fixed, it would be an $H$-coset. Each old vertex
would then lie in full cliques of at most one color, contrary to
$\sum_v m(v)\ge2(r^2+1)$ from
[Packing tools](packing_tools.md). Choose a non-$H$-fixed full clique
$Q$. The same edge-translation argument shows its $H$-stabilizer is
trivial: a nontrivial stabilizer would place its $r$ vertices in one
$H$-coset and therefore make it $H$-fixed. Its orbit consists of $r$
edge-disjoint cliques of one color.

Let $m$ be the number of $H$-cosets missed by $Q$. The union of these
cosets consists of $mr$ vertices outside all orbit cliques. Turán's
lower bound on this union and the internal orbit-clique edges give

$$
r\binom m2+r\binom r2\le\frac{r(r^2+1)}2,
\qquad m(m-1)\le r+1.
$$

If an occupied coset contains $k$ points of $Q$, each such point lies
in $k$ orbit cliques. The occupancies sum to $r$ over $r-m$ cosets;
hence their excess over one totals $m$, and at most $2m$ points in
each orbit clique are shared. Delete the shared points and its at
most one neighbor of $\infty$ in this color. The remaining $r$
parts are disjoint, avoid $N_i(\infty)$, and have size at least

$$
w=r-2m-1\ge r-2\sqrt r-3.
$$

Their cross edges lie outside the orbit-clique edge sets and number
at most $B=r(r+1)/2$. For $r\ge100$, $w\ge0.77r$ and
$B\le0.505r^2<w^2$. Independent uniform representatives have expected
target-edge count at most $B/w^2<1$. Some choice is an independent
$r$-set, which $\infty$ augments to a forbidden $(r+1)$-set.

The orbit, stabilizer, edge-budget, and numerical steps received a
separate check. Nothing here excludes arbitrary asymmetric colorings
or unrestricted nonabelian one-point actions. The latter limitation is
removed by the following theorem.

## 3. Arbitrary transitive one-point extensions

**Theorem.** For $r\ge100$, no E617 counterexample admits a group
fixing a vertex $\infty$, acting transitively on the other $r^2$
vertices, and possibly permuting colors. No regular subgroup is assumed.

Write $E_0=r(r^2+1)/2$. We use the full palettes and safe-clique
deletion lemma from [Critical components](critical_component_reduction.md),
the localized independence inequality, and the
[full-clique extension lemma with overlaps](packing_tools.md).
The last lemma extends an independent set $I$ outside $f$ full cliques
by one representative from each whenever $|I|+f\le r$. Its representatives
are chosen only among vertices private to their clique in the family;
ordinary greedy selection on overlapping cliques would not suffice.

### Star fibers and clique orbits

Every color occurs at $\infty$. Transitivity on the old vertices
therefore implies transitivity on colors. Every color has $E_0$ edges,
each star fiber $S_i=N_i(\infty)$ has order $r$, and its color stabilizer
$H_i$ is transitive on $S_i$. Every color has a full clique: otherwise
its average degree $r$ and clique number at most $r-1$ would give
$\alpha(G_i)\ge(r^2+1)/r>r$.

No full clique contains $\infty$. If its orbit has $L$ members,
old-vertex transitivity gives $L(r-1)=r^2t$ for a positive integer
$t$. Hence $r^2\mid L$. The orbit cliques have disjoint star-edge
sets, so $L(r-1)\le r^2$, a contradiction.

Suppose a full color-$i$ clique meets $S_i$. It meets it exactly once,
by the outsider cap at $\infty$. Every clique in its $H_i$-orbit
does likewise. Transitivity on $S_i$ gives orbit size $L=rt$ with
$t\ge1$. Since $L\binom r2\le E_0$, one has $L<2r$ and therefore
$L=r$.

Let $D$ be the number of old vertices outside the union of these
$r$ cliques. It is also their total overlap, since their total vertex
incidence is $r^2$. Tur\'an on the uncovered vertices gives

$$
r\binom r2+\frac{D^2/r-D}{2}\le E_0.
$$

Thus $x=D/r$ satisfies $x(x-1)\le r+1$, and $x\le\sqrt r+1$.
Orbit transitivity makes the shared-vertex count $h$ the same in each
clique. If $d_v$ counts orbit cliques through a vertex, then

$$
rh=\sum_{d_v\ge2}d_v\le2D,
\qquad h\le2x.
$$

Remove the shared vertices and the unique vertex in $S_i$ from each
clique. The $r$ remaining disjoint parts have order at least

$$
w=r-2x-1\ge r-2\sqrt r-3\ge0.77r.
$$

Their cross edges lie outside all orbit-clique edge sets, so number at
most $r(r+1)/2\le0.505r^2<w^2$. Uniform independent representatives
have expected conflict count below one. Some transversal is independent
and avoids $S_i$; adjoining $\infty$ is a contradiction.

Consequently all color-$i$ full cliques lie in

$$
U_i=V\setminus(S_i\cup\{\infty\}),
\qquad |U_i|=r(r-1),\quad \alpha(G_i[U_i])\le r-1. \tag{1}
$$


### Divisible overlap forces disjointness

Let $F>0$ be the common number of full cliques per color and let $u$
be the common order of their union. Old-vertex transitivity makes the
number $c$ of these color unions through an old vertex constant.
Counting gives $ru=r^2c$, hence $u=rc$. Thus the total same-color
overlap

$$
M=rF-u
$$

is a nonnegative multiple of $r$.

If $F\ge r-2$, choose $r-2$ full cliques in $U_i$ with overlap
$M'$. The overlap extension lemma makes their remainder have independence
at most one: an independent pair would extend to $r$ vertices in $U_i$.
That remainder has order $r+M'$. The clique cap forces $M'=0$ and
makes the remainder a $K_r$. Thus $U_i$ partitions into $r-1$ full
cliques. Any other full clique, if different from all these blocks,
meets each block in at most one vertex and cannot have order $r$.
These are therefore all the full cliques, and they are disjoint.

If $F\le r-3$, remove all full cliques from $U_i$ and put
$s=r-1-F\ge2$. The remainder $R$ satisfies

$$
|R|=rs+M,\qquad \alpha(R)\le s,\qquad \omega(R)\le r-1.
$$

The first independence bound again uses extension at total size $r$,
not $r+1$. The localized inequality gives

$$
2e(R)\ge r^2s+3rM+2M^2/s.
$$

The $r$ star edges and the edge-disjoint clique-internal edges give

$$
2e(R)\le r(r^2+1)-2r-Fr(r-1).
$$

Upper minus lower is

$$
r(r-1+F-3M)-2M^2/s,
$$

negative if $M\ge r$. Divisibility forces $M=0$.
Thus every color's full cliques are disjoint, and (1) gives $F\le r-1$.

### Safe isolation and the final incidence equation

In each color sequentially delete all edges leaving its full cliques,
leaving those pairs uncolored. The safe-clique lemma preserves independence
at most $r$; the budget only decreases, and same-color disjointness
preserves every other full clique. The outsider cap and hereditary caps
persist. Every original full clique becomes a component.

A foreign full clique is an independent $r$-set in the target color.
It must meet every target full component, since omitting a component
would allow one more independent vertex. The intersections have order
exactly one.

The original invariant family has $rF$ cliques of order $r$ on $r^2$
old vertices. Old-vertex transitivity gives exactly $F$ full cliques
through each old vertex, now known to have distinct colors. Counting
intersecting pairs of differently colored full cliques gives

$$
\binom r2 F^2=r^2\binom F2.
$$

As $F>0$, this forces $F=r$, contradicting $F\le r-1$.

The full proof, including the removal of the regular-action assumption,
was checked by the author and is author-recorded. It excludes the
nonabelian one-point template
in [Construction attempts](construction_attempts.md) for every $r\ge100$.
It does not exclude asymmetric colorings or prove any new unrestricted
positive case of E617.
