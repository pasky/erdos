---
name: research/erdos_644/convex_profile_amplification
desc: Additive-loss transversal amplification by convex or integer Minkowski profiles, with an exact fractional-transversal obstruction to preserving the local property.
tags: [proved, amplification, method-obstruction]
sources: [fon_der_flaass_et_al_1999_transversals_uniform_hypergraphs_property_7_2]
created: 2026-09-22T21:37:11Z
updated: 2026-10-16T06:44:50Z
---


# research/erdos_644/convex_profile_amplification

***

These results do not prove convergence of $f(k,r)/k$ or resolve the seven-edge
conjecture. They analyze one amplification construction completely: it scales
the transversal number with a loss of one in the seed, but preserves the local
property at every scale exactly when the seed's fractional transversal number
lies below the complete-family threshold.

Throughout, $r\ge3$, and $\mathcal H$ is a nonempty finite $k$-uniform family,
$k\ge1$, on a specified finite ground set $V$, with $n=|V|$ and
$t=\tau(\mathcal H)$. Write $P_r$ for the condition that every subfamily of **at
most** $r$ edges has a transversal of size at most two. The distinction from
testing exactly $r$ distinct edges is addressed below.

## Definition and transversal amplification

Put

$$
P=\operatorname{conv}\{\mathbf1_E:E\in\mathcal H\}\subseteq[0,1]^V.
$$

For an integer $m\ge1$, replace every $v\in V$ by a disjoint block $B_v$ of $m$
points. Define the full convex-profile family

$$
\mathcal B_m(\mathcal H)=
\left\{A\subseteq\bigsqcup_{v\in V}B_v:
|A|=mk,\quad
\left(\frac{|A\cap B_v|}{m}\right)_{v\in V}\in P
\right\}.
\tag{1}
$$

This includes every set with an allowed profile, not just one selected
realization of each profile. It is nonempty, since each original edge gives the
union of its entire blocks.

**Domination lemma.** If $u\in[0,1]^V$ satisfies

$$
\sum_{v\in V}(1-u_v)\le t-1,
\tag{2}
$$

then some $p\in P$ satisfies $p\le u$ coordinatewise.

**Proof.** Every subset $D\subseteq V$ with $|D|\le t-1$ misses some edge of
$\mathcal H$. Thus $\mathbf1_{V\setminus D}$ belongs to the upward closure
$P+\mathbb R_{\ge0}^V$. This upward closure is convex. The elementary
cube-section identity

$$
\operatorname{conv}\{\mathbf1_D:|D|\le t-1\}
=\left\{d\in[0,1]^V:\sum_vd_v\le t-1\right\}
$$

therefore implies the assertion, by taking $d=\mathbf1-u$. For completeness, the
identity follows because every vertex of the polytope on the right is integral:
two fractional coordinates allow an opposite perturbation when the sum
constraint is tight; one fractional coordinate cannot have an integral tight
sum; and an untight sum permits a one-coordinate perturbation. $\square$

**Theorem.** For every integer $m\ge1$,

$$
\boxed{\quad
\tau(\mathcal B_m(\mathcal H))
\ge m(t-1)-n(n+1)+1.
\quad}
\tag{3}
$$


**Proof.** If $m(t-1)-n(n+1)<0$, the assertion is automatic. Otherwise let $T$
be any set of at most that many clone points, and put

$$
c_v=|B_v\setminus T|,
\qquad
u_v=\max\left\{\frac{c_v-(n+1)}m,0\right\}.
$$

For each $v$,

$$
1-u_v\le\frac{|T\cap B_v|+n+1}{m},
$$

so (2) holds. Choose $p\in P$ with $p\le u$.

By Caratheodory's theorem, write

$$
p=\sum_{j=1}^{s}\alpha_j\mathbf1_{E_j},
\qquad s\le n+1,\quad \alpha_j>0,\quad \sum_j\alpha_j=1.
$$

There are nonnegative integers $a_j$ summing to $m$ with $|a_j-m\alpha_j|<1$:
round each coefficient down, and round up the required number of coefficients
with positive fractional parts. Put

$$
q=\sum_{j=1}^{s}a_j\mathbf1_{E_j}.
$$

Then $q$ is integral, $q/m\in P$, and $\sum_vq_v=mk$.

If $p_v=0$, every $E_j$ excludes $v$, so $q_v=0$. If $p_v>0$, then $u_v>0$, and

$$
q_v\le mp_v+s
\le c_v-(n+1)+s
\le c_v.
$$

Thus one can select $q_v$ points of $B_v\setminus T$ for every $v$. Their union
belongs to $\mathcal B_m(\mathcal H)$ and avoids $T$. This proves (3). $\square$

The error $n(n+1)$ depends on the fixed seed, not on $m$. Consequently, if this
construction preserved $P_r$, it would yield the asymptotic ratio at least
$(t-1)/k$. The next result identifies exactly when preservation occurs.

## The complete-family threshold as a weighted obstruction

Use the parameter from [Complete-family asymptotics](complete_families.md):

$$
\lambda_r=
\min_{\mathcal F,a}
\max_{i\in[r]}\sum_{F\ni i}a_F,
\qquad
\rho_r=\frac1{1-\lambda_r},
\tag{4}
$$

where $\mathcal F$ ranges over pairwise intersecting families of nonempty
subsets of $[r]$, and $a_F\ge0$, $\sum_Fa_F=1$. Each support gives a rational
linear program, and there are finitely many supports. Hence $\lambda_r$ is
attained and rational. Also $0<\lambda_r<1$: nonemptiness gives the lower bound
$1/r$ by averaging, while uniform weights on the $(r-1)$-subsets give a value
below one. In particular $\rho_r$ is rational and greater than one.

Two consequences of (4) will be used.

**Weighted obstruction lemma.** Suppose a finite weighted ground set has total
nonnegative weight $W$, and $A_1,\ldots,A_r$ have weight at least one each and
have no transversal of size at most two. Then $W\ge\rho_r$.

**Proof.** For every point $x$ define

$$
F_x=\{i:x\notin A_i\}.
$$

These sets are nonempty and pairwise intersecting; otherwise one or two points
cover all rows. Normalize the point weights by $W$, which is positive since each
row has weight at least one. The resulting distribution on the $F_x$ has
coordinate loads

$$
\frac{W-w(A_i)}W\le1-\frac1W.
$$

Thus $\lambda_r\le1-1/W$, giving $W\ge\rho_r$. If there are fewer than $r$ bad
rows, repeat rows to reach $r$; repetitions do not create a transversal.
$\square$

**Balanced bad-pattern lemma.** There is a rational probability distribution
$(b_S)$ on subsets $S\subseteq[r]$ such that

$$
\sum_{S\ni i}b_S=\frac1{\rho_r}\quad(i\in[r]),
\tag{5}
$$

and no two spectra in its support have union $[r]$, even when the two chosen
spectra coincide.

**Proof.** Take a rational optimizer in (4), with loads $p_i\le\lambda_r$.
Whenever coordinate $i$ is absent from a sampled set $F$, insert it
independently with probability

$$
\frac{\lambda_r-p_i}{1-p_i}.
$$

The denominator is positive because $p_i\le\lambda_r<1$. All probabilities are
rational, the new loads equal $\lambda_r$, and enlarging the original
intersecting sets preserves pairwise intersection and nonemptiness. Take
complements of the resulting sets. Their distribution is rational, has row
marginals $1-\lambda_r=1/\rho_r$, and has the required prohibition on unions.
The empty spectrum is permitted. $\square$

## Exact local-property criterion

The fractional transversal number is

$$
z=\tau^*(\mathcal H)
=\min\left\{\sum_v w_v:w_v\ge0,\ \sum_{v\in E}w_v\ge1\ (E\in\mathcal H)\right\}.
$$

Its dual is the maximum total weight of a fractional matching, with weighted
degree at most one at each point. Both optima are attained and rational, since
these are finite rational linear programs.

**Theorem.** The following are equivalent:

1. $\mathcal B_m(\mathcal H)$ has $P_r$ for every integer $m\ge1$.
2. $\mathcal B_m(\mathcal H)$ has $P_r$ for every sufficiently large integer
   $m$.
3. $\tau^*(\mathcal H)<\rho_r$.

If $\tau^*(\mathcal H)\ge\rho_r$, there is an integer $m_0\ge1$ such that
$\mathcal B_m(\mathcal H)$ fails $P_r$ for every positive multiple of $m_0$.

**Proof when $z<\rho_r$.** Let $w$ be an optimal fractional transversal of the
seed. Give every point in $B_v$ weight $w_v/m$. Total weight is $z$. If a new
edge has normalized profile $p\in P$, its weight is $w\mathbin\cdot p\ge1$, by
convexity of the original edge inequalities. The weighted obstruction lemma
excludes every bad subfamily of at most $r$ edges. This works for every $m$.

**Proof when $z\ge\rho_r$.** Choose a rational optimal fractional matching
$(y_E)_{E\in\mathcal H}$ of total weight $z$. Normalize it to a probability
distribution on edges and let

$$
p_v=\frac1z\sum_{E\ni v}y_E.
$$

Then $p\in P$ is rational and

$$
0\le p_v\le\frac1z\le\frac1{\rho_r}.
$$

Use the rational bad-pattern distribution $(b_S)$ from (5). In block $v$,
prescribe the fraction

$$
\rho_r p_v b_S
$$

of its points to have incidence spectrum $S$ among the $r$ new rows. Assign the
remaining fraction $1-\rho_r p_v$ to the empty spectrum. All fractions are
nonnegative and rational. The fraction of block $v$ lying in any particular row
is

$$
\rho_r p_v\sum_{S\ni i}b_S=p_v.
$$

Choose $m_0$ clearing the denominators of all prescribed block fractions. For
every multiple $m$ of $m_0$, this gives $r$ rows with normalized profile exactly
$p$, hence with size $mk$ and belonging to $\mathcal B_m(\mathcal H)$. No two
points cover the rows: their spectra come from the bad-pattern support or are
empty. Removing repeated rows, if any, gives a bad subfamily of at most $r$
distinct edges. This proves the assertions. $\square$

### Exactly $r$ distinct edges

For a family with at least $r$ distinct edges, $P_r$ is equivalent to the
condition on exactly $r$ distinct edges, since a smaller bad subfamily can be
extended. The criterion in the theorem also remains true if each occurrence of
$P_r$ is replaced by that exactly-$r$ condition, even when some small blow-ups
have fewer than $r$ edges.

Indeed, the implication from $z<\rho_r$ is unchanged. If $z\ge\rho_r>1$, the
seed contains two distinct edges $E,F$. For every $m$, the integral profile

$$
(m-1)\mathbf1_E+\mathbf1_F\in mP
$$

gives at least $m$ distinct members of $\mathcal B_m$: fix all other block
choices and vary the one selected clone in a block indexed by a point of
$F\setminus E$. Thus $|\mathcal B_m|\ge r$ whenever $m\ge r$. The bad tuples at
arbitrarily large multiples of $m_0$ can therefore be extended to $r$ distinct
edges.

## Integer Minkowski profiles have the same obstruction

Section 6.6 of
[first independent record](independent/fano_ground_set_and_coding_constructions.md)
considers the smaller family $\mathcal C_m(\mathcal H)$ obtained by allowing
only block-count vectors

$$
q=\mathbf1_{E_1}+\cdots+\mathbf1_{E_m},\qquad E_j\in\mathcal H,
$$

with repetitions allowed, and including every realization of each such profile.
One has $\mathcal C_m\subseteq\mathcal B_m$, but failure of the larger family
alone would not prove failure of the smaller one.

Nevertheless, both main theorems above extend to $\mathcal C_m$. The proof of
(3) already constructs an avoiding profile as an integer sum of exactly $m$
seed-edge vectors, so its transversal lower bound holds unchanged. When
$z<\rho_r$, the local property is inherited from $\mathcal B_m$. When
$z\ge\rho_r$, choose the scale in the bad-pattern proof also to clear the
denominators of the rational coefficients $y_E/z$. Then its common profile
satisfies

$$
mp=\sum_E(my_E/z)\mathbf1_E,\qquad
my_E/z\in\mathbb Z_{\ge0},\qquad \sum_E my_E/z=m.
$$

Every bad row thus belongs to $\mathcal C_m$. This works at every positive
multiple of that scale and proves the same all-scales preservation criterion
$\tau^*(\mathcal H)<\rho_r$. The exactly-$r$ convention is handled by the same
profile $(m-1)\mathbf1_E+\mathbf1_F$ as above.

The independent note also gives a direct scale-two failure even for $P_3$. Take
the seed to be two disjoint triangles on $a,b,c$ and $a',b',c'$. Any three seed
edges have a two-cover, since a three-edge graph requires three covering
vertices only when its edges are disjoint. With two clones of each vertex, the
three output edges

$$
\{a_1,b_1,a'_1,b'_1\},\quad
\{a_2,c_1,a'_2,c'_1\},\quad
\{b_2,c_2,b'_2,c'_2\}
$$

are disjoint. Each has the block-count vector of one edge from each seed
triangle. Hence $\mathcal C_2$ fails $P_3$.

## Limitation of the amplification method

The general fractional inequality recorded in
[Structural reductions](structural_reductions.md) is

$$
\tau(\mathcal G)\le K(\tau^*(\mathcal G)-1)+1
\tag{6}
$$

for a finite rank-$K$ family. One proof chooses the $\tau(\mathcal G)-1$
heaviest points of an optimal fractional cover and an edge avoiding them. The
edge has weight at least one and contains a point of weight at least $1/K$; each
selected point is at least that heavy. The two disjoint weight contributions
prove (6).

In particular, any seed with

$$
t\ge k(\rho_r-1)+1
$$

has $z\ge\rho_r$ and fails the preservation criterion. More generally, when
$z<\rho_r$, the cloned fractional cover in the proof gives
$\tau^*(\mathcal B_m)\le z$, so (6) gives

$$
\tau(\mathcal B_m)\le mk(z-1)+1<mk(\rho_r-1)+1.
$$

Thus this amplification cannot produce an asymptotic coefficient exceeding
$\rho_r-1$, the complete-family coefficient.

Complete families approach this coefficient within the preservation regime. If
the seed consists of all $k$-subsets of an $n$-point set with $n/k<\rho_r$, then
$z=n/k$,

$$
P=\{p\in[0,1]^n:\textstyle\sum_vp_v=k\},
$$

and $\mathcal B_m$ is the complete $mk$-uniform family on $mn$ points. Its
transversal number is exactly $m(n-k)+1$. Taking seed ratios $n/k$ tending to
$\rho_r$ from below approaches coefficient $\rho_r-1$.

This characterizes the reach of this particular construction. It does not bound
arbitrary $P_r$ families by the complete-family coefficient, nor provide a
different amplification for them.

## Explicit failure for the seven-edge parity construction

For $r=7$, [Complete-family asymptotics](complete_families.md) gives
$\lambda_7=3/7$, hence $\rho_7=7/4$.

Take the family from Theorem 1 of [Fon-Der-Flaass, Kostochka, and
Woodall](../../../library/set_systems/fon_der_flaass_et_al_1999_transversals_uniform_hypergraphs_property_7_2/_index.md),
Section 2:

$$
q\ge10,\quad |V|=7q+1,\quad |X|=4q,
\qquad
\mathcal H=\{E\in\tbinom V{4q}:|E\cap X|\text{ is odd}\}.
$$

The cited theorem proves that this family has $P_7$ and $\tau(\mathcal H)=3q+1$.
There are more than seven edges, so its stated exactly-seven property implies
the at-most-seven convention used here.

The constant profile

$$
p_v=\frac{4q}{7q+1}\qquad(v\in V)
\tag{7}
$$

belongs to $P$. To see this, let

$$
a=\frac{16q^2}{7q+1}.
$$

The feasible odd $X$-counts range from the least odd integer at least $q-1$ to
$4q-1$. Their minimum is at most $q$, and

$$
q<a<4q-1.
$$

Mix two allowed odd counts bracketing $a$ with rational probabilities to obtain
mean $a$, and choose uniformly within each selected profile. Each point of $X$
then has marginal $a/(4q)=4q/(7q+1)$; each point of $V\setminus X$ has marginal

$$
\frac{4q-a}{3q+1}=\frac{4q}{7q+1}.
$$

This proves (7). Scaling this edge distribution by $(7q+1)/(4q)$ gives a
fractional matching of that total weight, while constant point weights $1/(4q)$
give a fractional transversal of the same weight. Therefore

$$
\tau^*(\mathcal H)=\frac{7q+1}{4q}>\frac74.
$$


The resulting failure at scale $m=7q+1$ is explicit. In every original-point
block, use seven classes of $q$ clones with the seven Fano-cap spectra, and one
clone with the empty spectrum. Every row uses $4q$ clones in every block, so its
normalized profile is (7). Its total size is $m(4q)$, and it belongs to
$\mathcal B_m(\mathcal H)$. The seven rows are distinct, and no two clone points
cover them, because two Fano caps never have union $[7]$.

Thus full convex-profile completion destroys the local property even for the
known parity lower-bound families. A convergence proof by amplification would
need a different construction or a nonconvex restriction whose transversal loss
can be controlled. No such construction is proved here.

## Uniform upward shadows of disjoint parity copies

Section 6.2 of
[second independent record](independent/fractional_reductions_and_good_triples.md)
correctly gives a different failed amplifier, using three disjoint parity
families. In fact **two copies already fail**, and the obstruction extends to
every number $m\ge2$ of copies.

Fix $a\ge10$. In disjoint blocks $B_j$ of size $7a+1$, choose $X_j$ of size $4a$
and let

$$
\mathcal P_j=\{E\subseteq B_j:|E|=4a,\ |E\cap X_j|\text{ odd}\}.
$$

Each seed has $P_7$ and transversal number $3a+1$ by the checked 1999 theorem.
Consider the uniform upward shadow

$$
\mathcal U_m=\left\{A\subseteq\bigcup_{j=1}^m B_j:
|A|=4am,\quad E\subseteq A\text{ for some }E\in\bigcup_j\mathcal P_j\right\}.
$$

Then

$$
\tau(\mathcal U_m)=m(3a+1),\qquad
\mathcal U_m\text{ fails }P_7\quad(m\ge2).
\tag{U}
$$


For the transversal number, every $(4a+1)$-subset of a block contains a seed
edge. Such a set meets both $X_j$ and its complement; deleting one point from
either part yields $4a$-sets of opposite parity. Therefore an independent set of
size greater than $4am$ has a block intersection containing a seed edge, which
extends inside that set to a member of $\mathcal U_m$. Conversely,
$\bigcup_jX_j$ is an independent set of size $4am$. Its complement has size
$m(3a+1)$, proving the first assertion.

Here is an explicit bad seven-tuple. Index seven groups by
$x\in\mathbb F_2^3\setminus\{0\}$, and put $p=e_1$, $q=e_2$, $r=e_3$. Leave one
point of each block unused. In block 1 give group $p$ size $a+1$, group $q$ size
$a-1$, and every other group size $a$. In block 2 reverse these two exceptional
sizes. Every further block gives each group size $a$. Thus each global group
$G_x$ has size $ma$.

For every nonzero $u\in\mathbb F_2^3$, let

$$
A_u=\bigcup_{u\cdot x=1}G_x.
$$

These seven distinct rows have size $4am$. Their first two block sizes are

$$
|A_u\cap B_1|=4a+u_1-u_2,\qquad
|A_u\cap B_2|=4a-u_1+u_2,
$$

where the coordinates $u_i$ on the right are ordinary zero-one integers. If
$u_1\ne u_2$, the larger block contains a seed edge by the preceding
$(4a+1)$-set observation.

Choose the group intersection counts of $X_1$ to have parity vector
$\mathbf1+e_p$, and those of $X_2$ to have parity vector $\mathbf1+e_r$,
excluding the unused points. Such choices of total size $4a$ exist. Each
prescription has six odd counts and one even count, with minimum total six. The
maximum permitted total with these parities is even and at least $7a-7\ge4a$.
Increasing the counts by twos realizes every even total between these extremes.

Each row uses four groups, so these prescriptions give

$$
|A_u\cap X_1|\equiv u_1,\qquad
|A_u\cap X_2|\equiv u_3\pmod2.
$$

When $u_1=u_2$, both block sizes are exactly $4a$ and at least one of $u_1,u_3$
is nonzero. Hence one block intersection is itself a seed edge. Every $A_u$
therefore belongs to $\mathcal U_m$. The choices of $X_j$ do not restrict the
result: all block families with $|X_j|=4a$ are isomorphic under blockwise
permutations.

Finally, any two group indices $x,y$ have a common nonzero orthogonal vector
$u$, so the corresponding pair of points misses $A_u$. Unused points meet no row
and cannot help. Thus the seven rows have no two-cover, proving (U).

The operation would have kept the seed ratio $3/4+1/(4a)$ as $m$ grows, but it
loses the local property already at $m=2$. It is not the product-layer
construction in [Join-layer families](join_layer_families.md): in terms of the
seed independence complexes, $\mathcal U_m$ is the **complement** of their
join's $4am$-layer, not that layer itself.

## The unrestricted amplification target needs a seed loss

An amplifier preserving $P_7$ with rank $mk+O_{\mathcal H}(1)$ and transversal
number at least $m(\tau(\mathcal H)-1)-O_{\mathcal H}(1)$ cannot work for
**every** seed. The rank-one family $\{\{a\},\{b\}\}$ has $P_7$ and transversal
number two. The proposed amplifier would have ratio tending to one,
contradicting the established $7/8$ upper bound.

A sufficient, but unproved, convergence statement is the same target with a loss
$C_r$ depending only on $r$, or an appropriate restriction to large seeds:

$$
\operatorname{rank}(\mathcal H_m)\le mk+O_{\mathcal H}(1),
\qquad
\tau(\mathcal H_m)\ge m(\tau(\mathcal H)-C_r)-O_{\mathcal H}(1).
$$

Padding to arbitrary larger uniformities would then yield

$$
\liminf_{K\to\infty}f(K,r)/K
\ge (f(k,r)-C_r)/k
$$

for each admissible seed uniformity $k$. Taking a limsup subsequence of $k$
would prove convergence. No construction realizing this corrected target is
known here.

Fixed-layer concatenations do not provide it: if every output edge restricts in
each fixed layer to a seed edge, a seed transversal placed in any one layer
already covers the output, regardless of which concatenations are allowed. The
final section of [Polarized blocker powers](polarized_blocker_powers.md) gives a
separate obstruction to all genuine polarizations in a fixed number of
variables.

## Substitution and critical-sum attempts

The following elementary checks incorporate §§6.3–6.5 of the independent note.
All input families here are finite, nonempty, and have nonempty edges. They do
not provide a general $P_r$ amplifier.

### Full inner-family substitution

Replace each point $v$ of a $k$-uniform family $\mathcal H$ by a disjoint copy
$\mathcal G_v$ of an $a$-uniform family $\mathcal G$. For each $E\in\mathcal H$,
include all unions of independently chosen $F_v\in\mathcal G_v$, $v\in E$. Then

$$
k_{\rm new}=ka,\qquad
\tau_{\rm new}=\tau(\mathcal H)\tau(\mathcal G).
$$

Indeed, a proposed cover works exactly when the indices of the inner copies on
which it is a transversal cover $\mathcal H$. If those indices miss $E$, choose
independently an inner edge missed in each of its copies; the resulting union is
missed.

If $\mathcal H$ has $P_r$ and every at-most-$r$ edges of $\mathcal G$ have a
common point, the output has $P_r$: lift each point of a two-cover of the
projected edges to a common point of the relevant inner edges. But the
intersection hypothesis gives

$$
\tau(\mathcal G)\le\left\lceil\frac{a}{r-1}\right\rceil.
$$

Otherwise partition one inner edge into $r-1$ parts, each of size at most
$\lceil a/(r-1)\rceil$ (empty parts are allowed), and choose an edge avoiding
each part. This produces at most $r$ edges with empty common intersection. Thus,
for fixed seed and $a\to\infty$, this sufficient preservation condition permits
at most a $1/(r-1)+o(1)$ multiplier on the seed's transversal-to-rank ratio. The
independent bound $(a-1)/(r-1)+1$ is equivalent after integrality, not a
different estimate.

### Exact universal condition for complete clone classes

Section 6 of
[third independent record](independent/complete_family_limit_and_seven_edge_obstruction.md)
substitutes all $s$-subsets of an $N$-point class for each original vertex,
where $1\le s\le N$. For a nonempty $k$-uniform seed,

$$
k'=ks,\qquad \tau'=(N-s+1)\tau.
$$

Indeed, a selected set $T$ meets every expanded edge exactly when the
original vertices whose classes contain at least $N-s+1$ points of $T$
form a transversal of the seed. If these vertices miss an original edge,
choose an $s$-subset avoiding $T$ in every class of that edge.

The input's condition $r(N-s)<N$ is sufficient but not sharp. The
[exact substitution theorem](boolean_reductions.md#finite-promise-relations-and-the-exact-substitution-restriction)
gives the following universal equivalence:

$$
\boxed{\text{Every }P_r\text{ seed remains }P_r
\quad\Longleftrightarrow\quad (r-1)(N-s)<N.}
$$

Here $r\ge3$. To check it directly, the inner family is
$(r-1)$-wise intersecting exactly under the displayed inequality:
at most $r-1$ complements, each of size $N-s$, cannot cover the class.
Tuples of one row are trivial. For a larger tuple, if the inner family
is intersecting to this order, a two-cover of the original rows
partitions them into two nonempty groups of at most $r-1$ rows, each
covered by a common clone. If one original point covers all rows,
split its at-most-$r$ inner edges into two such groups instead.
Conversely, when the inequality fails, at most $r-1$ inner edges have
empty intersection. Use them in one of two disjoint singleton seed
edges, and one inner edge in the other. This at-most-$r$ tuple needs
at least three covering points.

Writing $q=N-s$, admissibility is $(r-2)q<s$. Hence the largest
universally admissible ratio multiplier at fixed $s$ is exactly

$$
\max_N\frac{\tau'/k'}{\tau/k}
=\frac{\lceil s/(r-2)\rceil}{s}.
$$

As $s\to\infty$ this tends to $1/(r-2)$, rather than the input's
$1/(r-1)$ for its stronger criterion. For $r=7$ the improved factor
is still only $1/5$. For $r=3$, $N=2s-1$ preserves the ratio exactly;
for $s=1$ universal preservation forces $N=1$. Necessity is asserted
for **all** seeds, not for a particular special seed. Thus this does
not rule out every seed-specific cloning mechanism.

### Each fixed seed and the parity construction

[[theory/combinatorics/L187_complete_cloning_obstruction/_index|L187]]
gives the seed-specific obstruction and its full proof. For any nonempty
seed with nonempty edges, $N\ge7\lceil s/4\rceil$ forces the complete
clone-class expansion to fail $P_7$, by seven Fano-cap incidence spectra.
Thus a $P_7$ expansion has

$$
\frac{\tau'}{k'}\le\frac\tau k\left(\frac34+\frac{21}{4s}\right).
$$

For the parity family defined above there is a stronger obstruction:
$3N\ge4s$ forces failure of $P_7$. Seven distinct cyclically constructed
parity rows can be expanded so that every clone point lies in at most
three rows. Consequently a $P_7$ expansion must have $N<4s/3$.
For $s\ge2$ its ratio is at most $31/80<3/4$; for $s=1$ it must have
$N=1$, the unchanged seed. No nontrivial complete clone-class substitution
preserves both the local property and a ratio above $3/4$.

The general universal-preservation criterion above remains distinct:
L187's first obstruction applies to each seed individually, and its second
uses the parity family's explicit structure. Restricted inner families and
other operations remain possible; no such replacement is supplied here.

### Replacing just one point per edge

Retain the old vertices and include

$$
(E\setminus\{v\})\cup F,
\qquad E\in\mathcal H,\ v\in E,\ F\in\mathcal G_v.
$$

The rank is $k+a-1$. Write $A$ for the selected old vertices and $B$ for the
indices of fully covered inner copies. The exact transversal optimization
minimizes

$$
|A|+\tau(\mathcal G)|B|
$$

subject, for every $E\in\mathcal H$, to: no constraint when $|E\cap A|\ge2$;
$v\in B$ when $E\cap A=\{v\}$; and $E\subseteq B$ when $E\cap A=\varnothing$.
These conditions follow by testing separately every choice of the replaced
point. Partial inner covers can be discarded: if the old part misses $A$,
covering all corresponding replacement edges requires a full transversal of that
inner copy.

Consequently any set meeting each old edge in at least two points covers the
output using only old points. For the complete $k$-uniform seed on $n$ points
with $k\ge2$, such a set has minimum size $n-k+2=\tau(\mathcal H)+1$,
independently of the inner transversal number. Thus increasing the inner family
cannot give unbounded transversal amplification for this seed. No $P_r$
preservation is claimed here.

### A critical sum has the desired arithmetic but fails locally

Let $\mathcal H_i$ be $k_i$-uniform and $\tau$-critical, with transversal
numbers $t_i$, on initially disjoint grounds. Choose
$x_i\in E_i\in\mathcal H_i$, identify $x_1,x_2$ as $x$, delete the two chosen
edges, and add $E_1\cup E_2$. The resulting rank and transversal number are

$$
K=k_1+k_2-1,\qquad \tau=t_1+t_2-1.
$$

A cover containing $x$ restricts to covers of both original families, giving the
stated lower bound. A cover avoiding $x$ needs at least $t_i-1$ points on each
side; if both attain equality, both miss $E_i$, and their union misses the new
edge. Conversely, the two critical covers of size $t_i-1$ missing $E_i$,
together with $x$, attain the bound. Private padding makes the family
$K$-uniform and preserves the transversal number of every subfamily.

For a local failure, take each input to be all eight-subsets of a thirteen-point
set. These families are critical and have $P_7$, since $7\cdot8>4\cdot13$ and
any two eight-sets intersect. Choose $E_i$ containing $x_i$. On each side
partition the other twelve points into three four-sets and take their three
complements within those twelve points. They are retained eight-edges with empty
common intersection and transversal number two. The two triples have disjoint
grounds, so their six edges have transversal number four. Adding the joined edge
gives seven distinct edges with no two-cover. Private padding cannot repair this
failure. Thus the arithmetic does not furnish the required amplifier.

## Canonical dual and blocker complexes do not repair join amplification

The following obstruction concerns the six canonical complexes specified below.
It does **not** exclude an arbitrary complex selected from a seed, auxiliary
vertices, or a different complex operation.

For a clutter $\mathcal F$ on a specified ground set $V$, write

$$
\Delta(\mathcal F)=\{I\subseteq V:I\subseteq E\text{ for some }E\in\mathcal F\},
\qquad
\operatorname{Ind}(\mathcal F)=\{I\subseteq V:E\nsubseteq I\text{ for all }E\in\mathcal F\}.
$$

Let $b(\mathcal F)$ be its blocker, the clutter of inclusion-minimal
transversals. The Alexander dual of a hereditary complex $K$ is

$$
K^*=\{I\subseteq V:V\setminus I\notin K\}.
$$

For $1\le a\le n$, put $U_{a,n}=\{I\subseteq[n]:|I|\le a\}$. The join-layer
notation $\mathcal H_{q,\ell}(K)$ is as in
[Join-layer families](join_layer_families.md): its edges are the $\ell$-sets
whose restriction to each of $q$ disjoint blocks is a face of $K$.

### A complete seed with bad subfaces one level below its edges

Fix $r\ge3$, and let $\rho=\rho_r$ be the rational threshold defined earlier on
this page. The balanced bad-pattern lemma gives a rational distribution $(b_S)$
on spectra $S\subseteq[r]$, with row marginals $1/\rho$, such that no two
spectra in its support have union $[r]$.

Choose an integer $Q$ clearing the denominators of all $b_S$. Then $d=Q/\rho$ is
an integer, since it equals $\sum_{S\ni i}Qb_S$. For every sufficiently large
integer $L$, put

$$
k=Ld,\qquad N_0=LQ=\rho k,\qquad n=N_0-1.
$$

Realize $LQb_S$ points with each spectrum $S$. The resulting $r$ rows have size
$k$ and have no two-point transversal. Delete one point and trim each row to
size $k-1$. Trimming only removes incidences, so the resulting rows still have
no two-point transversal. Thus there is a bad $r$-tuple of $(k-1)$-sets on $n$
points.

On the other hand, the complete seed

$$
\mathcal H=\binom{[n]}k
$$

has $P_r$. Indeed, give each ground point weight $1/k$. Every edge has weight
one, while the total weight is $n/k<\rho$, so the weighted obstruction lemma
excludes a bad tuple. Its transversal number is

$$
t=n-k+1=(\rho-1)k.
\tag{D1}
$$

This supplies an infinite sequence of admissible seeds with $k\to\infty$.

More generally, if a hereditary complex $K$ contains a bad $r$-tuple whose rows
all have size $c\ge1$, then

$$
1\le\ell\le qc
\quad\Longrightarrow\quad
\mathcal H_{q,\ell}(K)\text{ fails }P_r.
\tag{D2}
$$

To prove this, repeat the same tuple in every block. The concatenated rows have
size $qc$. Points in different blocks still use the same admissible spectrum
support, so no two points cover the rows. Trim each row to size $\ell$; heredity
preserves membership in the join, and removing incidences preserves the failure
of a two-cover.

Applying this observation to the bad subfaces just constructed gives

$$
1\le\ell\le q\min\{a,k-1\}
\quad\Longrightarrow\quad
\mathcal H_{q,\ell}(U_{a,n})\text{ fails }P_r.
\tag{D3}
$$

In particular, if $a\le k-1$, **every nonempty join layer fails**, for every
$q\ge1$.

### Exact transversal number of a skeleton join layer

For arbitrary $1\le a\le n$ and $1\le\ell\le qa$, write

$$
\ell=pa+h,\qquad 1\le h\le a.
$$

Then

$$
\boxed{\tau(\mathcal H_{q,\ell}(U_{a,n}))=(q-p)n-h+1.}
\tag{D4}
$$


To prove (D4), let $x_j$ be the number of points remaining in block $j$ after a
proposed transversal is deleted. It is a transversal precisely when

$$
\sum_{j=1}^q\min\{a,x_j\}\le\ell-1=pa+h-1.
$$

If $f$ blocks have $x_j\ge a$, then $f\le p$, and

$$
\sum_jx_j
\le fn+(p-f)a+h-1
\le pn+h-1.
$$

Equality is attained by retaining $p$ complete blocks and $h-1$ points of one
further block. Subtracting from $qn$ proves the formula.

Consequently,

$$
\tau(\mathcal H_{q,\ell}(U_{a,n}))
=qn\left(1-\frac{\ell}{qa}\right)+\varepsilon,
\qquad
1\le\varepsilon=h(n/a-1)+1\le n.
\tag{D5}
$$

The deletion linear program from [Join-layer families](join_layer_families.md)
is therefore exactly

$$
\gamma_{U_{a,n}}(b)=n(1-b/a),\qquad 0\le b\le a.
$$

One can also check this directly: the remaining rank after deleting $D$ is
$\min\{a,n-|D|\}$, every deletion type lies on or above the line joining $(a,0)$
to $(0,n)$, and mixing no deletion with complete deletion attains that line.

For one of the complete seeds in (D1), suppose $a\ge k$ and a sequence of join
layers has $P_r$ and uniformities $\ell\to\infty$. Equation (D3) forces
$\ell>q(k-1)$. Hence (D5) gives

$$
\boxed{\limsup\frac{\tau(\mathcal H_{q,\ell}(U_{a,n}))}{\ell}
\le\frac{n}{k-1}-\frac na.}
\tag{D6}
$$

Here the seed, and therefore $n,k,a$, is fixed while the layer uniformity tends
to infinity. For $a\le k-1$ there is no such sequence, by (D3).

### The six canonical choices

For the seed $\mathcal H=\binom{[n]}k$, its blocker is $\binom{[n]}t$. The
canonical complexes are the following skeletons:

| Complex | Skeleton rank $a$ |
|---|---:|
| $\Delta(\mathcal H)$ | $k$ |
| $\operatorname{Ind}(\mathcal H)$ | $k-1$ |
| $\Delta(\mathcal H)^*$ | $t-2$ |
| $\Delta(b(\mathcal H))$ | $t$ |
| $\operatorname{Ind}(b(\mathcal H))$ | $t-1$ |
| $\Delta(b(\mathcal H))^*$ | $k-2$ |

The Alexander duals of the two independence complexes repeat entries in this
table. All displayed ranks are positive for sufficiently large seeds in the
sequence.

For $a=k$, (D6) bounds the asymptotic output ratio by

$$
\frac{n}{k(k-1)}=O_r(1/k).
$$

For $a=k-1$ or $k-2$, no nonempty join layer has $P_r$.

For the remaining ranks $a=t,t-1,t-2$, recall that $t=(\rho-1)k$. If $\rho<2$,
these ranks are at most $k-1$ for sufficiently large seeds, so again every
nonempty layer fails. If $\rho=2$, the only additional possible rank is $a=k$,
with the same $O_r(1/k)$ ratio bound. If $\rho>2$, taking $k\to\infty$ in the
right side of (D6) gives

$$
\rho-\frac{\rho}{\rho-1}.
$$

This is strictly below the seed ratio $\rho-1$, with difference $1/(\rho-1)$.

It follows that **no choice among these six canonical complexes gives a
universal join-layer amplifier with limiting ratio at least $(t-C_r)/k$**, for
any fixed constant $C_r$. Indeed, that target tends to $\rho-1$ on the
complete-seed sequence, whereas the preceding bounds leave a positive constant
gap. Private padding of a layer to larger uniformity cannot improve its
transversal-to-uniformity ratio.

For $r=7$, take $k=4L$, $n=7L-1$, and $t=3L$. Every canonical complex in the
table except $\Delta(\mathcal H)$ has rank at most $k-1$, and therefore has no
nonempty $P_7$ join layer at all. The original downward closure has only the
$O(1/k)$ asymptotic ratio bound above. This is an obstruction to the specified
constructions, not an upper bound for arbitrary $P_7$ families or a resolution
of unrestricted convergence.
