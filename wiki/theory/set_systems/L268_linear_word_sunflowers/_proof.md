---
name: theory/set_systems/L268_linear_word_sunflowers/_proof
title: Proof of the affine linear word bound
desc: |
  Maximize the deficit between the desired dimension and the span of
  coordinate dual spaces, contract that span, and apply linear Hall
  selection. Dualizing gives a subspace whose coordinates are zero or
  injective and whose affine cosets are sunflowers.
created: 2026-10-15T21:21:39Z
updated: 2026-10-15T21:21:39Z
---

***

Use the notation and sunflower convention in the
[[theory/set_systems/L268_linear_word_sunflowers/_index|statement of L268]].
Distinct words give distinct transversal sets. Their sets form a sunflower
exactly when every coordinate's symbols are either all equal or all
distinct: if a symbol appears in two words, the corresponding point must
belong to the common core and hence appear in all the words.

## Linear independent representatives

**Lemma.** Let $E_1,\ldots,E_N$ be subspaces of a finite-dimensional vector
space $W$. There are linearly independent vectors $v_i\in E_i$, one for
each $i$, if and only if

$$
\dim\Bigl(\sum_{i\in I}E_i\Bigr)\ge |I|
\quad\text{for every }I\subseteq[N].
\tag{1}
$$

*Proof.* Necessity follows by counting the selected independent vectors
in each sum. For sufficiency, induct on $N$. The cases $N=0,1$ are
immediate. If a nonempty proper set $I$ attains equality in (1), apply
induction to its subspaces. Their selected vectors form a basis of
$W_I=\sum_{i\in I}E_i$. In $W/W_I$, any collection indexed by
$J\subseteq[N]\setminus I$ spans dimension at least

$$
\dim(W_I+W_J)-\dim W_I\ge |I|+|J|-|I|=|J|.
$$

Induction in the quotient, followed by lifting the selected vectors,
completes the choice.

Otherwise every nonempty proper $I$ has sum dimension at least $|I|+1$.
Choose a nonzero $v_N\in E_N$, and quotient by its span. For the first
$N-1$ subspaces, each nonempty sum loses at most one dimension and still
satisfies (1). Select their representatives by induction in the quotient
and lift them; together with $v_N$ they are independent. $\square$

By repeating each $E_i$ exactly $s$ times, the lemma also gives $s$
independent representatives from each $E_i$, all jointly independent,
whenever every collection of the original subspaces spans dimension at
least $s$ times its cardinality. Indeed a collection of repeated indices
has at most $s|I|$ entries when its distinct indices are $I$.

## Contracting an obstructing collection of coordinates

Write $V=C$ and $t=\dim V$. Let $L_i:V\to A_i$ be its coordinate maps,
and let

$$
E_i=\operatorname{im}(L_i^*)\le V^*.
$$

Their sum is $V^*$: a vector annihilated by every $E_i$ has every
coordinate zero and is therefore zero. For $I\subseteq[n]$, put

$$
W_I=\sum_{i\in I}E_i,\qquad d(I)=s|I|-\dim W_I.
$$

Choose $J$ maximizing $d(I)$, and among maximizers choose one with least
cardinality. Since $d(\varnothing)=0$ and
$d([n])=sn-t\le0$, this $J$ is a proper subset of $[n]$. This includes
the equality case $t=sn$: if the maximum is zero, the empty set is the
chosen maximizer; if it is positive, the full set is not a maximizer.

For every $K\subseteq[n]\setminus J$, maximality gives

$$
\dim(W_J+W_K)-\dim W_J\ge s|K|.
\tag{2}
$$

Apply the lemma in $V^*/W_J$ to the images of the $E_i$ for $i\notin J$.
Choose vectors $e_{i,1},\ldots,e_{i,s}$ in those images that are all
linearly independent. Define a linear map

$$
\phi:V^*/W_J\longrightarrow\mathbb F_q^s
$$

by sending $e_{i,j}$ to the $j$th standard basis vector, for every
$i\notin J$, and extend it from these independent vectors to a basis of
the quotient. This assignment is consistent even though different
selected vectors have the same image. Since $[n]\setminus J$ is
nonempty, $\phi$ is onto.

Compose $\phi$ with the quotient map to obtain
$\Phi:V^*\to\mathbb F_q^s$. Its dual embeds $(\mathbb F_q^s)^*$ as an
$s$-dimensional subspace $U$ of $V^{**}=V$. If $i\in J$ then
$\Phi(E_i)=0$, so $L_i|_U=0$. If $i\notin J$ then
$\Phi(E_i)=\mathbb F_q^s$, so the dual of $L_i|_U$ is onto and
$L_i|_U$ is injective.

For any distinct words in $a+U$, a zero coordinate map gives one common
symbol and an injective coordinate map gives distinct symbols. Thus all
$q^s$ transversal sets from $a+U$ form a sunflower, including the case
of an empty core. This proves the subspace assertion.

## The exponential bound

Let $k\ge3$ and suppose the affine word family $a+C$ has no
$k$-sunflower. With $s=\lceil\log_q k\rceil$, a dimension at least
$sn$ would supply a $q^s$-sunflower by the subspace assertion. Any $k$
of its members would be a $k$-sunflower, because $q^s\ge k$.
Consequently

$$
\dim C<sn,\qquad |C|\le q^{sn-1}.
\tag{3}
$$

If $q\ge k$ and $C\ne\{0\}$, choose a nonzero $v\in C$. The affine
line $a+\mathbb F_qv$ is a $q$-sunflower: in coordinate $i$ it is
constant when $v_i=0$, and its symbols are distinct when $v_i\ne0$.
This is a contradiction, so $C=\{0\}$ in this case and
$|C|=1<k^{2n}$.

If $q<k$, the definition of $s$ gives $q^s<qk<k^2$. Equation (3)
therefore implies $|C|<k^{2n}$ in this case as well. The estimates do
not depend on the dimensions of the coordinate spaces. $\square$
