---
name: research/erdos_774/lemmas/root_height_escape
title: Exact varying-height escape inside actual odd roots
desc: Conductor-disjoint rational root circuits with doubly exponential pivot coefficients have dissociated full products and recurrent tails of exactly increasing minimum relation height.
tags: [E0774, proved, algebra, obstruction]
sources: []
created: 2026-09-18T17:23:00Z
updated: 2026-09-18T17:37:54Z
---


# Exact varying-height escape inside actual odd roots

***

## Statement and purpose

There are finite sets $X_i=\{1\}\cup Y_i$ of odd squarefree-order
roots, in pairwise coprime conductor groups, such that:

- Each $X_i$ is a rational circuit with a unique primitive relation
  whose magnitudes are $\{1,H_i\}$, where $H_i=2^{2^{i-1}}$.
- Every finite product $X_1\cdots X_n$ is dissociated.
- The nested tail-product sets
  $$
  D_j=\bigcup_{n\ge j}X_jX_{j+1}\cdots X_n
  $$
  have **least nonzero integer-relation height exactly $H_j$**.
- For each $x\in D_j$, sufficiently late $k$ satisfies
  $xD_k\subset D_j$.

Thus height-free flattening fails even for actual root units with injective
products and fresh conductors, not just for unrelated scalar configurations.
The construction realizes the precise escape in the new
[coefficient-growth bound](../routes/coefficient_growth_flattening.md).
It is not a coloring of the whole root group, and does not obstruct
color-adaptive selection under stronger quantitative hypotheses.

## 1. Moving the coefficient-two seed to arbitrary prime triples

The [eight-point seed](prime_tensor_circuit.md) in $S_3^{\otimes3}$
has primitive kernel generator
$$
(-1,1,-1,1,-1,1,-1,-2)
$$
on labels $000,012,021,102,110,211,222,001$. Its only coefficient
of magnitude two is at $001$.

For any distinct odd primes $p,q,r$, enlarge the three simplex factors
by duplicating the following layers:

1. First-coordinate layer $2$ into $p-2$ copies.
2. Second-coordinate layer $2$ into $q-2$ copies.
3. Third-coordinate layer $0$ into $r-2$ copies.

The seed's layer-duplication lemma preserves the entire one-dimensional
integer kernel: all layer supports are independent, and their coefficients
are uniquely determined by their common vector sum. None of these layers
contains the distinguished point $001$. Consequently the enlarged set
is a circuit in $S_p\otimes S_q\otimes S_r$, with one coefficient
$-2$ and all other coefficients $\pm1$.

The usual coprime cyclotomic tensor identification realizes these columns
faithfully by roots. Divide all roots by the distinguished root. The
resulting circuit has the form $\{1\}\cup L$, with $L$ rationally
independent and
$$
2=\sum_{u\in L}\epsilon_u u,\qquad \epsilon_u\in\{\pm1\}. \tag{1}
$$
All roots are distinct and $1\notin L$.

This construction works on arbitrarily fresh disjoint prime triples.
It uses the already proved algebraic seed, not a new search or certificate.

## 2. Arbitrary powers of two at a unique pivot

Take $s$ versions of (1) on disjoint conductor triples, and let $Y$
be the full product of their leaf sets $L$. Multiplication identifies
the tensor of their cyclotomic fields with the compositum. Therefore $Y$
is rationally independent, and multiplication of (1) gives
$$
2^s=\sum_{y\in Y}\epsilon_y y,\qquad \epsilon_y\in\{\pm1\}. \tag{2}
$$
The product map is injective. In particular $1\notin Y$: equality to
one would force every factor to equal one, although none belongs to its leaf
set. Thus $\{1\}\cup Y$ is a circuit. Its displayed relation is
primitive and unique up to integer multiples, because the leaves form a
basis of their span and their coefficients in (2) are all nonzero.

For factor $i$, take $s_i=2^{i-1}$ such seeds. Reserve distinct prime
triples for all seeds in all factors. This gives
$$
X_i=\{1\}\cup Y_i,\qquad
H_i=2^{s_i}=\sum_{y\in Y_i}\epsilon_i(y)y. \tag{3}
$$

## 3. The full products really are independent at the claimed height

Fix a finite index set $I\subset\{j,j+1,\ldots\}$, and a relation
with coefficients $a_x\in[-H_j+1,H_j-1]\cap\mathbb Z$ on
$\prod_{i\in I}X_i$. The tensor leaf products are a rational basis
of the span. For a leaf tuple $y=(y_i)_{i\in I}$ and $S\subset I$,
let $x^S(y)$ be the root tuple using $1$ at positions in $S$ and
$y_i$ at the other positions. Expand $1=H_i^{-1}\sum\epsilon_i(y)y$
and multiply the coefficient of the basis tuple $y$ by $\prod_iH_i$.
It is
$$
0=\sum_{S\subset I}a_{x^S(y)}
 \left(\prod_{i\in S}\epsilon_i(y_i)\right)
 \prod_{i\in I\setminus S}H_i. \tag{4}
$$
Put $B=H_j$. The last products in (4) are distinct nonnegative
integer powers of $B$, since their exponents are subset sums of the
distinct powers $2^{i-j}$. An integer combination of distinct powers
of $B$, with coefficient magnitudes at most $B-1$, cannot vanish
unless every coefficient vanishes: divide by its least participating power
and reduce modulo $B$.

Hence $a_{x^S(y)}=0$ for every $S,y$. Every product column occurs
in this form (fill the unused leaf positions arbitrarily), so the original
relation is trivial. Each such product is $(H_j-1)$-independent.

Because every $X_i$ contains $1$, the finite products defining $D_j$
are nested. Every relation has finite support, so $D_j$ is
$(H_j-1)$-independent. The relation on $X_j\subset D_j$ has height
$H_j$, proving the exact minimum. In particular $D_1$ is dissociated.

For $x\in D_j$, take $k$ beyond the largest factor used in $x$.
Then $xD_k\subset D_j$ simply uses disjoint sets of factors. Also the
$D_j$ eventually avoid every prescribed finite conductor-prime set.

## 4. Rescaling does not manufacture Hall tightness

Every nonzero relation on $X_i$ is a multiple of (3). Its magnitude
pair is therefore $\{t_i,t_iH_i\}$ for some positive integer $t_i$.
View these pairs as edges joining positive real labels. A cycle among
distinct edges would imply
$$
\prod_iH_i^{\sigma_i}=1,
\qquad \sigma_i\in\{-1,0,1\},\quad \sigma\ne0,
$$
and thus $\sum_i\sigma_i2^{i-1}=0$, impossible. This also excludes
parallel edges. The graph is a forest, so every nonempty subfamily has
strictly more incident vertices than edges. No rescaling produces the
Hall-tight condition needed for determinant flattening.

This is compatible with the stronger subset-counting theorem: the associated
scalar model attains equality at its exact threshold, as computed on that
page.

## 5. Scope

The supports above have product recurrence and a rational dependence in
every tail, but they do not cover the whole root group. Indeed $D_1$
is not piecewise syndetic. Given finite multipliers $F$, take a factor
whose conductor is disjoint from all conductors in $F$. Its projection
of $FD_1$ is the proper subset $X_i$ of its full conductor group.
It cannot contain a translate of that finite subgroup, so $FD_1$ is
not thick. The properness follows, for example, from dissociation of $X_i$
and a full prime polygon in the conductor group.

The
[Hare-based recurrent construction](../routes/recurrent_high_height_roots.md)
strengthens this diagnostic by making the rational coloring number infinite in
every tail. That additional property still does not imply piecewise syndeticity
or the actual-color growth inequality.

Fresh-prime duplication, product injectivity, the basis expansion, and tail
independence received independent internal checks. No computation was run.
