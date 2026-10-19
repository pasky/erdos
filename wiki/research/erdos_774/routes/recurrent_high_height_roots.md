---
name: research/erdos_774/routes/recurrent_high_height_roots
title: Recurrent root sets do not supply a uniform height
desc: Dissociated root sets can have product-recurrent tails of increasing height independence and infinite rational coloring number; piecewise syndeticity gives an exact stronger reformulation of the unresolved premise.
tags: [E0774, proved, reduction, obstruction, incomplete]
sources: []
created: 2026-09-18T17:23:00Z
updated: 2026-09-18T18:37:35Z
---


# Recurrent root sets do not supply a uniform height

***

## Standing

Let $G=\bigoplus_{p\text{ odd}}\mu_p$, with additive relations
interpreted in $\mathbb C$. Write $\chi_h$ for coloring by
height-$h$ independent classes, and $\chi_{\mathbb Q}$ for coloring
by rationally independent classes.

This page proves that even rationally rich, product-recurrent root sets
need not have a relation at one uniform height. It gives an exact stronger
target: excluding height-$h$ independent **piecewise-syndetic** sets for
one fixed $h$ is equivalent to the premise of
[fixed-height focusing](fixed_height_focusing.md). That exclusion remains
unproved. No finite coloring of $G$ is constructed here.

## 1. A height-safe tensor extension

Let $B\subset\mathbb Z^d$ be height-$h$ independent, with all
column entries in $\{0,\pm1\}$. Let $C$ be height-$h|B|$
independent. Then the indexed tensor product $B\otimes C$ is
height-$h$ independent.

Indeed, for a relation with coefficients $a_{b,c}\in[-h,h]$, each
coordinate $u$ of $B$ gives a $C$-relation
$$
\sum_{c\in C}\left(\sum_{b\in B}a_{b,c}b_u\right)c=0
$$
with coefficient magnitudes at most $h|B|$. Every bracket therefore
vanishes. For each $c$, the equations say $\sum_ba_{b,c}b=0$;
height-$h$ independence of $B$ finishes the proof.

More generally, $|B|$ can be replaced by the maximum absolute row sum
of the integer column matrix of $B$. We use the simpler bound below.
For roots on disjoint conductor blocks, multiplication identifies the tensor
product faithfully with the actual root products. Standard prime-grid columns
have the required $0,\pm1$ entries.

## 2. Fixed-height extraction with arbitrarily large rank defect

The established [root extraction theorem](prime_tensor_extraction.md) makes $G$
Sidon in the **additive**, discrete, torsion-free group $\mathbb C$. The arXiv
v1 copy of
[Hare--Yang](../../../../library/analysis/hare_yang_2018_sidon_sets_proportionally_sidon_small_constants/_index.md)
was checked after its digest: Proposition 2, Lemma 3, and Theorem 2 in Section 3
give, for every fixed integer $H$, one $\delta_H>0$ such that every finite root
set contains a height-$H$ independent subset of relative size at least
$\delta_H$. The identity excluded by that theorem is additive $0$, not root $1$.

On any prescribed conductor tail, full grids have arbitrarily large
cardinality-to-rank ratio
$$
\frac N d=\prod_{p\in J}\frac p{p-1}.
$$
For example, take all permitted odd primes through a cutoff. These finite
products dominate the harmonic sum over **odd** integers up to that cutoff
and coprime to the fixed excluded conductor, and those sums diverge.
Thus for any fixed $H,L$ one may
choose a finite fresh grid $E$ with
$\delta_H|E|/\operatorname{rank}_{\mathbb Q}E\ge L$.
An extracted set $C\subset E$ then satisfies
$$
C\text{ is height-}H\text{ independent},\qquad
\frac{|C|}{\operatorname{rank}_{\mathbb Q}C}\ge L. \tag{1}
$$
Multiplying $C$ by the inverse of one of its roots arranges $1\in C$.
This preserves all relations, stays in the same conductor group, and
permutes the full grid's standard $0,\pm1$ columns.

In particular, no fixed-height lower bound of the form
$\operatorname{rank}_{\mathbb Q}C\ge\epsilon_H|C|$ holds for actual
root subsets. This is a consequence of the checked local extraction theorem,
not a new coloring theorem.

## 3. Recurrent tails with infinite rational coloring number

Set $B_0=\{1\}$. Recursively choose disjoint finite conductor blocks
and sets $C_i$ satisfying
$$
1\in C_i,\qquad H_i=i|B_{i-1}|,
\qquad C_i\text{ height-}H_i\text{ independent},
\qquad \frac{|C_i|}{\operatorname{rank}_{\mathbb Q}C_i}\ge i+1,
\tag{2}
$$
and put $B_i=C_1\cdots C_i$. Existence follows from (1) at each
finite stage. These choices can, if desired, be made by the first successful
finite subset in a fixed enumeration; the extraction theorem guarantees
termination. No search was performed here.

Define
$$
D_j=\bigcup_{n\ge j}C_j\cdots C_n. \tag{3}
$$
Then:

1. $D_j$ is height-$j$ independent, so $D_1$ is dissociated.
2. $\chi_{\mathbb Q}(D_j)=\infty$ for every $j$.
3. The sets $D_j$ are nested and eventually lie in every fixed conductor
   tail.
4. For $x\in D_j$, sufficiently late $k$ satisfies $xD_k\subset D_j$.

For (1), induct along a finite tail product. Its prefix has at most
$|B_{i-1}|$ elements, and
$j|C_j\cdots C_{i-1}|\le i|B_{i-1}|=H_i$.
Apply the tensor lemma at height $j$, and then use finiteness of every
relation's support to pass to the union. For (2), each $C_i\subset D_j$
for $i\ge j$, since all factors contain $1$; any rationally independent
class in $C_i$ has at most its rational rank, so its coloring number is
at least $i+1$. Assertions (3)--(4) follow directly from disjoint conductor
blocks and disjoint late factor positions.

Thus arbitrary-depth monochromatic products of rationally dependent factors
can all lie in one dissociated set whose every tail has infinite rational
coloring number. The missing issue is not just choosing rationally dependent
profile classes. Each $D_j$ still has some rational dependence, but the
least relation heights have no common finite bound.

## 4. An ordinary idempotent still does not fix the quantifier

For completeness, the preceding construction supports an idempotent
ultrafilter $\mathcal U$ on $G$ such that
$$
D_j\in\mathcal U\quad\text{for every }j,
\qquad \chi_{\mathbb Q}(A)=\infty\quad(A\in\mathcal U). \tag{4}
$$
This is **not** an assertion of minimality in the ideal sense.

Here is a self-contained semigroup argument. Let
$\mathcal I=\{A\subset G:\chi_{\mathbb Q}(A)<\infty\}$.
This is a translation-invariant ideal: restriction and finite unions
preserve finite colorability. The requirements of containing all $D_j$
and all complements of members of $\mathcal I$ have the finite
intersection property. Otherwise a $D_j$ would be covered by a finite
union of finitely colorable sets, contradicting Section 3. Ultrafilter
compactness therefore makes the following a nonempty compact set:
$$
K=\{\mathcal U:D_j\in\mathcal U\ (j\ge1),\quad
\mathcal U\cap\mathcal I=\varnothing\}.
$$

Define ultrafilter multiplication by
$$
A\in\mathcal U\mathcal V
\iff\{x:x^{-1}A\in\mathcal V\}\in\mathcal U.
$$
It is associative by expanding the definition; right multiplication by a
fixed ultrafilter is continuous, since the inverse image of the basic
clopen set $\{\mathcal U:A\in\mathcal U\}$ is another such set.
For $\mathcal U,\mathcal V\in K$, tail recurrence shows that the return
set of $D_j$ contains $D_j$, so $D_j\in\mathcal U\mathcal V$.
For $A\in\mathcal I$, no translate $x^{-1}A$ belongs to
$\mathcal V$, so its return set is empty. Hence $K$ is a compact
subsemigroup.

Choose a minimal nonempty compact subsemigroup $M\subset K$, using
the intersection property of chains of compact sets. For $a\in M$,
the set $Ma$ is a nonempty compact subsemigroup, and therefore is $M$.
The nonempty set $\{x\in M:xa=a\}$ is also a compact subsemigroup,
so it is $M$. In particular $a^2=a$. This proves (4); the ultrafilter
is nonprincipal because finite sets belong to $\mathcal I$.

It contains the dissociated set $D_1$, and for every $h$ it contains
the height-$h$ independent set $D_h$. Thus idempotence and even
infinite rational coloring number in every member cannot replace the common
height in the earlier idempotent focusing proposition.

## 5. The exact additional global-color condition

A set $T\subset G$ is **thick** if every finite $E\subset G$ has
a translate $Et\subset T$. A set $A$ is **piecewise syndetic** if
$FA$ is thick for some finite $F\subset G$.

**Proposition.** For every fixed finite $h$,
$$
\boxed{\chi_h(G)<\infty
\quad\Longleftrightarrow\quad
G\text{ has a height-}h\text{ independent piecewise-syndetic subset}.}
\tag{5}
$$

For the forward direction, first prove that a cell in every finite partition
of $G$ is piecewise syndetic. Suppose $A\cup B$ is piecewise
syndetic, with $F(A\cup B)$ thick, and $A$ is not piecewise
syndetic. Since $FA$ is not thick, choose finite nonempty $K$ such
that $Kx\not\subset FA$ for every $x$. Given finite $E$, take
$t$ with $KEt\subset FA\cup FB$. For every $e\in E$, some
$k\in K$ has $ket\notin FA$, so $ket\in FB$. Therefore
$Et\subset K^{-1}FB$. The fixed finite set $K^{-1}F$ witnesses
that $B$ is piecewise syndetic. Induction, starting from $G$, proves
the partition assertion; apply it to a finite height-$h$ coloring.

Conversely, suppose $A$ is height-$h$ independent and $FA$ is
thick. For any finite $E\subset G$, choose $t$ with $Et\subset FA$.
Assign each $x\in E$ an $f\in F$ with $f^{-1}xt\in A$.
Within a color, multiplication by $f^{-1}t$ preserves all additive
relations and is injective. This is a proper height-$h$ coloring with
at most $|F|$ colors. Finite-color compactness gives a coloring of $G$.
This proves (5).

The sets $D_j$ from Section 3 are **not** piecewise syndetic. Each
$C_i$ is a proper subset of its full conductor group $E_i$, since
the full group has a ternary prime-polygon relation. Given finite $F$,
choose a later block disjoint from all conductor primes in $F$. Projection
of $FD_1$ to that block is precisely $C_i\ne E_i$. No translate
of the finite subgroup $E_i$ can be contained in $FD_1$, since its
projection would be all of $E_i$. Thus $FD_1$ is not thick. Its
subsets $D_j$ cannot be piecewise syndetic either.

### Syndetic and uniformly recurrent normalization

The same existence question can use a **syndetic** independent set, meaning
one with $FB=G$ for finite $F$, without enlarging a given thick-cover
witness. Suppose $A$ is height-$h$ independent and $FA$ is thick.
Exhaust $G$ by increasing finite $E_n$, choose $t_n$ with
$E_nt_n\subset FA$, and take a coordinatewise convergent subsequence of
$t_n^{-1}A$ in $\{0,1\}^G$. Its limit $B$ is height-$h$
independent: every forbidden relation has finite support. Also $FB=G$:
for each $x$, the covering disjunction over the fixed finite set $F$
persists under pointwise convergence. Thus (5) is equivalent to existence
of a syndetic height-$h$ independent set.

Let $H=\langle F\rangle$, a finite multiplicative root subgroup.
Since $HB=G$, choosing one point of $B$ in each $H$-coset gives
an independent global transversal. This agrees with the earlier
[selector formulation](roots_coloring_structure.md); it does not restrict
the tail color labels beyond that formulation.

There is also a minimal-shift normalization. The orbit closure of $B$
consists of independent sets $C$ satisfying the same $FC=G$:
both conditions are closed, and $G$ is abelian. Choose a minimal nonempty
closed invariant subsystem by compactness. Every point $C$ in it is
uniformly recurrent. Explicitly, for a nonempty clopen pattern neighborhood
$U$, minimality makes its inverse shifts cover the subsystem; a finite
subcover makes the occurrence set of $U$ syndetic. Taking
$U=\{D:X\subset D\}$ for finite $X\subset C$ shows that
$$
\bigcap_{x\in X}x^{-1}C
$$
is syndetic.

The covering witness for this last intersection depends on the entire
pattern $X$. **No bound on that dependence is proved.** Fixed initial
coverage therefore does not keep coefficient heights or magnitude-group
counts under control during focusing. In particular this normalization does
not upgrade the ordinary idempotent in Section 4 to a minimal-ideal
idempotent containing its constructed $D_1$.

Combining (5) with fixed-height focusing gives a precise sufficient proof
target: for **one fixed $h$**, prove that every piecewise-syndetic
subset of $G$ has a height-$h$ relation. This is an equivalent
reformulation of the unresolved premise, **not a proof of it**. Existing
bounds allow the height to depend on the finite thick-cover size.

### Positive patterns themselves force cover growth

The growth of return-cover witnesses is not merely caused by intersecting
with a conductor tail. Let $B\ne\varnothing$ be height-$h$
independent for $h\ge1$, and put
$R_X=\{t:Xt\subset B\}$ for a finite $X\subset B$.

First, $Bk\subset B$ implies $k=1$. Finite order turns that
inclusion into equality. A nonidentity stabilizer then contains an element
of prime order, whose orbit on any point of $B$ is a forbidden
ternary prime-polygon relation.

Consequently, given any nonempty finite $F\subset G$, there is a
pattern $X\subset B$ with $|X|\le|F|$ such that
$FR_X\ne G$. Choose $t\notin F$. For each $f\in F$,
the preceding fact supplies $b_f\in B$ with
$b_f f^{-1}t\notin B$. Taking $X=\{b_f:f\in F\}$
excludes $t$ from $FR_X$. Thus even the initial covering
**set** need not persist through finitely many positive-pattern constraints.

There is also an arbitrarily large lower bound on covering **cardinality**.
Suppose $FB=G$, and choose a finite subgroup $K\supset F$.
Translate $B$ so that $X=B\cap K$ has maximal size among all
its $K$-coset sections. Then
$$
|X|\ge\lceil |K|/|F|\rceil,
\qquad R_X\text{ meets each }K\text{-coset at most once}. \tag{6}
$$
The first claim follows by covering $K$ with the sets
$f(B\cap K)$. For a return $r$, maximality gives
$B\cap Kr=Xr$. Two different returns in the same coset would
therefore yield a nontrivial stabilizer of the independent set $X$,
which the preceding argument excludes.

If $ER_X=G$ for a finite $E$, choose a finite subgroup
$H\supset E\cup K$. Then
$H=E(R_X\cap H)$ and
$|R_X\cap H|\le |H|/|K|$, proving
$$
|E|\ge |K|. \tag{7}
$$
If the maximizing translation was $B'=Ba^{-1}$, transport its
pattern back as $Xa\subset B$; commutativity gives
$R_{Xa}(B)=R_X(B')$. Hence this conclusion concerns patterns inside
one original $B$. If $B$ is uniformly recurrent, all these
positive-pattern returns are syndetic, but their minimum cover sizes are
unbounded. This proves no coefficient-height growth or coloring theorem;
it specifies why minimal recurrence alone does not fix that gap.
Both pattern statements received independent internal review.

The source hypotheses, tensor lemma, tail construction, ultrafilter argument,
and piecewise-syndetic equivalence received independent internal checks.
No numerical experiment was used.
