---
name: research/erdos_644/prime_guard_families
desc: One deleted product edge makes rare guards conjunction-prime without changing the transversal number; a sparse partial-product criterion safely removes such guards.
tags: [proved, boolean-functions, limitations, reductions]
sources: []
created: 2026-09-23T02:29:00Z
updated: 2026-10-13T05:28:09Z
---


# research/erdos_644/prime_guard_families

***

Exact conjunction-primality does not exclude an almost-independent guard of
negligible rank. A single deleted product edge makes a product conjunction-prime
while preserving its transversal number. Consequently conjunction-prime,
low-Shapley families can have critical bias tending to one, even at
near-three-quarter extremality. The construction also transfers any hypothetical
fixed-excess sequence to one with these properties. It does **not** construct a
counterexample to either assertion of Problem 644.

All families below are finite clutters of nonempty sets, on their supports.
Write $b(\mathcal H)$ for the family of inclusion-minimal transversals and
$f_{\mathcal H}(X)=1$ when $X$ contains an edge. Products have disjoint
supports.

## Blocker components describe conjunction factors

For every $X$,

$$
f_{\mathcal H}(X)=1
\quad\Longleftrightarrow\quad
X\cap T\ne\varnothing\text{ for every }T\in b(\mathcal H).
\tag{1}
$$

Indeed, if $X$ contains no edge, its complement is a transversal and contains a
minimal transversal disjoint from $X$. Thus $f_{\mathcal H}$ is the conjunction
of the clauses $\bigvee_{x\in T}x$ indexed by its blocker.

Every support vertex $v$ occurs in a minimal transversal. Choose an edge
$E\ni v$. The set $(V\setminus E)\cup\{v\}$ is a transversal because
$\mathcal H$ is a clutter, and every transversal contained in this set must
contain $v$ to hit $E$.

Let $D_1,\ldots,D_a$ be the components of the graph in which vertices are
adjacent when they occur together in a blocker edge. Grouping the clauses in (1)
gives

$$
\mathcal H=\mathcal H_1\otimes\cdots\otimes\mathcal H_a
\tag{2}
$$

with factor supports $D_i$. Conversely, a disjoint-variable conjunction
separates every minimal transversal: a set forces the conjunction to zero
exactly when its restriction forces some factor to zero. Therefore
$f_{\mathcal H}$ is conjunction-prime exactly when this blocker graph is
connected.

Also $\tau(\mathcal H)=\min_i\tau(\mathcal H_i)$. If $\tau(\mathcal H)\ge2$,
every factor in (2) consequently has at least two minterms.

## Deleting one product edge

**Lemma.** Suppose $\tau(\mathcal H),\tau(\mathcal G)\ge2$. Choose
$E_0\in\mathcal H$, $F_0\in\mathcal G$, and put

$$
\mathcal Q=(\mathcal H\otimes\mathcal G)\setminus\{E_0\cup F_0\}.
$$

Then

$$
\tau(\mathcal Q)=\min\{\tau(\mathcal H),\tau(\mathcal G)\},
\qquad f_{\mathcal Q}\text{ is conjunction-prime}.
\tag{3}
$$

Moreover, $\mathcal Q$ inherits $P_r$ from $\mathcal H$ and has rank at most the
sum of the factor ranks.

**Proof.** Write $a=\tau(\mathcal H)$ and $b=\tau(\mathcal G)$. A cover in
either factor covers $\mathcal Q$. Conversely, let $T=T_H\cup T_G$ cover
$\mathcal Q$. If neither projection covers its factor, the Cartesian product of
their nonempty collections of uncovered edges is contained in $\{(E_0,F_0)\}$.
Thus $T_H$ covers every $\mathcal H$-edge except $E_0$, and analogously for
$T_G$. Consequently

$$
|T|\ge(a-1)+(b-1)\ge\min(a,b).
$$

If a projection covers its factor, the lower bound is immediate.

Every member $S$ of $b(\mathcal H)$ remains a minimal transversal of
$\mathcal Q$. To check minimality, for each $x\in S$ take an $\mathcal H$-edge
meeting $S$ only at $x$, and pair it with an edge of $\mathcal G$ other than
$F_0$. Such an edge exists since $b\ge2$. The same argument applies to
$b(\mathcal G)$.

Set $U=E_0\cup F_0$. The complement of $U$ covers $\mathcal Q$, since the
product is a clutter. Choose a minimal $\mathcal Q$-transversal
$T\subseteq V\setminus U$. This one blocker edge meets every original blocker
component. For example, let $D$ be a component belonging to $\mathcal H$. Its
factor in (2) has a minterm different from $E_0\cap D$. Replacing only that
component of $E_0$ gives an edge $E'\ne E_0$. All points of
$(E'\cup F_0)\setminus U$ lie in $D$, so $T$, which avoids $U$, must meet $D$.
The argument for each component belonging to $\mathcal G$ is identical.

The original blocker components remain connected in $b(\mathcal Q)$, and $T$
connects all of them. This proves primeness. A local cover in the $\mathcal H$
coordinates covers the corresponding product rows, proving the $P_r$ assertion.
$\square$

## A deletion preserving low Shapley values

Let $M=|\mathcal H||\mathcal G|$. In a uniformly random ordering of the
product's vertices, consider the first winning prefix. For each product edge
$U$, let $B_U$ be the event that $U$ is the unique minterm contained in that
prefix. These events are disjoint, so some $U$ satisfies $\Pr(B_U)\le1/M$.

Delete this $U$. Outside $B_U$, the first winning prefix, and therefore the
pivotal coordinate, is unchanged. Hence

$$
\phi_x(f_{\mathcal Q})
\le\phi_x(f_{\mathcal H\otimes\mathcal G})+M^{-1}.
\tag{4}
$$

For a variable $x$ of $\mathcal H$, independence gives

$$
\phi_x(f_{\mathcal H\otimes\mathcal G})
=\int_0^1 I_x^{\mathcal H}(p)\mu_p(f_{\mathcal G})\,dp
\le\phi_x(f_{\mathcal H}),
$$

and similarly for guard variables.

If $\mathcal G$ comprises $m$ disjoint $s$-sets, its $ms$ variables are
transitive and each has Shapley value $1/(ms)$. A suitable deletion therefore
satisfies

$$
\max_x\phi_x(f_{\mathcal Q})
\le\max\!\left\{\max_x\phi_x(f_{\mathcal H}),\frac1{ms}\right\}
+\frac1{m|\mathcal H|}.
\tag{5}
$$


## Rare prime guards

Suppose $\mathcal H_k$ has rank at most $k$, has $P_7$, satisfies
$t_k=\tau(\mathcal H_k)\ge ck$ for a fixed $c>0$, and has maximum Shapley value
tending to zero. The local property implies matching number at most two, so
$t_k\le2k$.

Discard finitely many indices so that $t_k\ge2$. Take $s_k=\lceil\sqrt{k}\rceil$
and let $\mathcal G_k$ consist of $t_k$ disjoint $s_k$-sets. After the suitable
deletion above, the family $\mathcal Q_k$ is conjunction-prime, has $P_7$,
satisfies

$$
\tau(\mathcal Q_k)=t_k,
\qquad \operatorname{rank}(\mathcal Q_k)\le k+s_k,
\qquad \max_x\phi_x(f_{\mathcal Q_k})\longrightarrow0,
$$

and, for each fixed $p<1$,

$$
\mu_p(f_{\mathcal Q_k})\le\mu_p(f_{\mathcal G_k})
\le t_kp^{s_k}\le2kp^{\sqrt{k}}\longrightarrow0.
\tag{6}
$$

Its half-reliability bias therefore tends to one. The rank cost is $o(k)$, so
any fixed positive excess above three quarters survives. Combined with
[Boolean factor reduction](boolean_factor_reduction.md), this is a conditional
transformation of hypothetical counterexamples, not evidence that such
counterexamples exist.

There is also an unconditional near-boundary example. Let $4\mid k$, $t=3k/4$,
and let $\mathcal A$ contain all $k$-subsets of $n=7k/4-1$ core vertices. Its
transversal number is $t$. Every pair of edges intersects. Seven rows have total
incidence $7k>4n$, so a point meets at least five rows; one further point covers
the remaining at most two rows. Thus $\mathcal A$ has $P_7$.

Append a guard of $t$ disjoint $\lceil\sqrt{k}\rceil$-sets and delete any one
product edge. The resulting prime family has rank $k+\lceil\sqrt{k}\rceil$,
transversal number $t$, and satisfies (6). A natural stabilizer subgroup of the
omitted edge has vertex orbits of sizes

$$
k,\quad t-1,\quad s_k,\quad(t-1)s_k.
$$

Shapley values are constant on these orbits and sum to one, so their maximum
tends to zero without a special choice of deletion.

These examples are not incidence-minimal: erasing all guard incidences recovers
the core, preserving $P_7$ and the transversal number.

[Topological guards](topological_guards.md) uses a different, rank-two path
guard to make both the ordinary intersection nerve and the nontransversal
complex contractible, while the deleted-square coindices of the latter become
unbounded. This shows why unnormalized topological invariants do not repair the
exact-primality obstruction.

## Safe removal of a sparse partial product

A robust replacement for exact factor removal works when the omitted guard
fibers have small transversal number.

**Lemma.** Let $r\ge3$, let $\mathcal H$ and $\mathcal G$ be clutters on
disjoint supports, and let $\operatorname{rank}(\mathcal G)\le s$. Choose
subfamilies $\mathcal G_E\subseteq\mathcal G$ for $E\in\mathcal H$ and set

$$
\mathcal Q=\{E\cup F:E\in\mathcal H,\ F\in\mathcal G_E\}.
$$

Suppose

$$
\tau(\mathcal G\setminus\mathcal G_E)\le d\quad\text{for every }E,
\qquad \tau(\mathcal G)>rd+2s.
\tag{7}
$$

Then $\mathcal Q$ has $P_r$ if and only if $\mathcal H$ does. Moreover
$\tau(\mathcal H)\ge\tau(\mathcal Q)$, so projection safely removes the guards
without transversal loss.

More generally, the same conclusions hold whenever the intersection of any at
most $r$ allowed fibers $\mathcal G_E$ contains three pairwise disjoint edges.

**Proof.** First, (7) implies the more general condition. For any at most $r$
core edges, take a transversal of each omitted guard fiber and let $C$ be their
union. Then $|C|\le rd$. The guard edges disjoint from $C$ belong to every
chosen allowed fiber, and their transversal number is at least

$$
\tau(\mathcal G)-|C|>2s.
$$

They therefore contain three disjoint edges: otherwise a maximal matching of at
most two edges would cover them with at most $2s$ points.

Only the implication from product to core requires work. Pad a bad core tuple to
$r$ rows. For each point in their union let $M_x$ be its set of missing rows.
These sets are pairwise intersecting, and each has size at least two: otherwise
a second point covers the only missed row.

Choose an inclusion-minimal $M=M_x$ and $i\in M$. The three nonempty classes

$$
\{i\},\qquad M\setminus\{i\},\qquad[r]\setminus M
$$

contain no missing set, respectively by the size condition, minimality, and
pairwise intersection. Assign three disjoint guard edges from the common allowed
fiber to these three classes. Two core points still fail to cover. Two guard
points miss a class. A mixed pair fails because the core point's missing set is
not contained in the guard's class. This gives a bad product tuple, a
contradiction.

The reverse implication uses a local cover in the core. Every core transversal
covers $\mathcal Q$, proving the transversal comparison. $\square$

For the one-deleted-edge guards above, every omitted fiber has transversal
number at most one, while $\tau(\mathcal G_k)=t_k$ and its rank is $s_k=o(t_k)$.
Thus (7) safely removes those guards for all sufficiently large parameters. No
extraction theorem forcing an arbitrary high-transversal $P_7$ family into this
partial-product form has been proved. Exact primeness, small influences, and
sparse-product removal therefore still do not establish the three-quarter bound
or convergence.

[Nonuniform guard fibers](nonuniform_guard_fibres.md) gives another
safe $P_7$ projection: it suffices that every guard fiber separately
has rank at most $s$ and transversal number greater than $2s$.
No common allowed edges or sparse omitted fibers are required.
The proof uses a nonbipartite 2-degenerate graph on the seven row
indices. It still does not control the total cost of exceptional
low-transversal fibers or furnish an unrestricted extraction.
