---
name: research/erdos_774/routes/adaptive_determinant_support
title: Prescribed determinant supports need not focus
desc: Binary colorings split every determinant support from prescribed relation menus, even with same-color anchored factors; this does not exclude color-adaptive selection.
tags: [E0774, proved, obstruction, coloring]
sources: []
created: 2026-09-18T02:38:00Z
updated: 2026-09-18T02:38:00Z
---


# Prescribed determinant supports need not focus

***

## Standing

The [determinant lemma](bounded_height_flattening.md) requires the actual
product support to be monochromatic. The results here show why simply
collecting many prescribed relations, even at one common height and one
anchored color, does not supply that condition. They do **not** avoid all
ternary relations or rule out selecting relations after seeing the coloring.
The [fixed-height focusing theorem](fixed_height_focusing.md) provides one
valid adaptive mechanism, conditional on an unproved chromatic hypothesis.

## Every incidence in a minimal Hall-tight family survives

Let $R$ be minimal nonempty with $|N(R)|\leq|R|$, where
$N(J)=\bigcup_{i\in J}I_i$ is the union of coefficient magnitudes.
Assume each $I_i$ has at least two members. Then
$|N(R)|=|R|$, and $|N(J)|>|J|$ for every nonempty proper $J\subset R$.

Every incidence $(i,m)$, $m\in I_i$, belongs to a perfect matching.
Delete row $i$ and column $m$. Each remaining row subset $J$ has
at least $|N(J)|-1\geq|J|$ remaining neighbors, so the finite matching
argument already proved in the determinant lemma applies. Restore $(i,m)$.
Thus every magnitude group occurs in a nonempty permutation-product block.

## Binary splitting of prescribed relations

In each of finitely many conductor-disjoint factors, prescribe a relation
supported on $X_i$, with disjoint magnitude groups $X_{i,m}$.
Suppose each relation has at least two magnitudes and at least one
nonsingleton magnitude group. Choose $g_i$ with values in $\mathbb F_2$
which splits one such group, and extend it to the factor arbitrarily.

The additive coloring $f(x)=\sum_i g_i(x_i)$ splits every determinant
support made from a minimal Hall-tight subfamily of these prescribed relations.
Indeed, a split group in any selected row belongs to a perfect matching.
Within that matching's product block, fix every other coordinate and vary
between two oppositely colored members of the split group. Both resulting
tuples lie in the determinant support and have different colors.

There is a stronger anchored version. Choose $b_i\notin X_i$, and put
$$
f(x)=
\begin{cases}
0,&\#\{i:x_i\in X_i\}\leq1,\\
\sum_i g_i(x_i),&\#\{i:x_i\in X_i\}\geq2.
\end{cases}
\tag{1}
$$
Every axis $X_i\times\prod_{j\ne i}\{b_j\}$ is color zero.
Every Hall-tight subfamily has at least two rows, so its whole determinant
support uses the parity branch, whatever the fixed outside context.
The preceding splitting argument still applies.

These assumptions occur at height two in arbitrarily many disjoint-prime
factors. Start with the eight-point seed in the
[coefficient-two circuit lemma](../lemmas/prime_tensor_circuit.md), and
duplicate coordinate layers $2,2,0$ to obtain any desired triple of
odd-prime side sizes. Its unique coefficient-two point $001$ is not
duplicated, while its magnitude-one group is nonsingleton. Layer duplication
preserves its integral circuit relation. The resulting support is a proper
subset of its grid (for example a tuple with first two labels $1,2$
is absent), so anchors exist. Use disjoint prime triples.

Consequently, arbitrarily many same-color anchored height-two relations
do not force their prescribed determinant support. The coloring (1) is not
claimed to be a proper dissociated coloring of the whole grid.

## Exponential finite-menu bound

Suppose factor $i$ uses only primes at least $p_i$, and prescribe
$K_i$ nonzero relations of height at most $h$. Every such relation
has support size at least $p_i$: a smaller support projects properly
onto every coordinate and lies in a tensor product of independent proper
simplex subsets, which is rationally independent.

Each menu relation therefore has a magnitude group of size at least
$s_i=\lceil p_i/h\rceil$. Select one such group for each relation.
Independent binary vertex colors leave a selected group monochromatic with
probability at most $2^{1-s_i}$. The elementary union bound shows that
$$
K_i2^{1-\lceil p_i/h\rceil}<1
\tag{2}
$$
suffices for a local coloring splitting a selected group of every menu member.
The additive product coloring then splits all Hall-tight determinant supports
from all menu choices. The anchored override also works if every menu relation
has at least two magnitudes and each factor has an anchor outside its whole
support union. Without that assumption one uses the ordinary additive coloring,
not the override. In the menu version of (1), the activity test uses each
factor's support union in place of its single prescribed support.

This is a theorem about **prescribed finite menus**. It is not a lower bound
against adaptive algorithms, and does not say the menus of all useful
bounded-height relations satisfy (2). No computational search is used.

## Exact color condition for additive palettes

For completeness, let $f(x)=\sum_i g_i(x_i)$ take values in an abelian
group. On a minimal Hall-tight family its determinant support is monochromatic
exactly when every magnitude group is locally monochromatic, with label
$c_{i,m}$, and
$$
c_{i,m}=a_i+b_m\qquad(m\in I_i)
\tag{3}
$$
for some row and column labels.

Edge extendability proves the first condition is necessary. Fix a perfect
matching $i\leftrightarrow m_i$; put an arc $i\to j$ whenever
$m_j\in I_i$, with gain $d_{ij}=c_{i,m_j}-c_{i,m_i}$.
This directed graph is strongly connected: a proper nonempty terminal set
would have no neighbors beyond its own matched columns, contrary to strict
Hall. Replacing the fixed matching along any directed simple cycle gives
another matching. Equality of matching-color sums says that every such cycle
has gain zero; decomposing closed walks into cycles gives the same for all
closed walks. Path integration in the strongly connected graph now gives
$d_{ij}=b_{m_j}-b_{m_i}$, and setting
$a_i=c_{i,m_i}-b_{m_i}$ proves (3). Conversely (3) makes every matching
sum $\sum_i a_i+\sum_m b_m$, independent of the matching.

This characterizes additive colorings only. Arbitrary colorings are not assumed
to have that form.
