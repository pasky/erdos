---
name: research/sunflower_exponential_bound/spread_matching_obstruction
title: Spread does not force two disjoint sets
desc: |
  Substitution powers of intersecting seeds have an exactly computable spread
  whose limit is a one-level seed quantity; block seeds give intersecting
  families with spread log n/(log log n)^2, and inner sunflower-free seeds
  force large sunflower cores.
created: 2026-10-15T17:54:12Z
updated: 2026-10-15T17:54:12Z
---

***

These author-recorded arguments are by Plasma AI. The theorems they support
are the claims
[[theory/set_systems/L214_spread_intersecting_families/_index|L214, which proves that intersecting families can be arbitrarily spread and refutes Rao's suggested r = O(p) matching lemma]],
and
[[theory/set_systems/L215_spread_large_core_sunflowers/_index|L215, which shows that spread does not force a sunflower with a bounded core]].
The [[theory/set_systems/L214_spread_intersecting_families/_proof|proof of L214]]
holds the lemmas used below. This page explains the mechanism, the further
author-recorded observations that are not part of either claim, and what
remains open. The attack it serves is recorded in the
[[research/sunflower_exponential_bound/proof_sketch|editable proof sketch for Problem 20]].

Intersecting families with unbounded normalized spread are already known:
[[../library/set_systems/alweiss_2020_improved_bounds_sunflower_lemma/_index|Alweiss–Lovett–Wu–Zhang, Section 4 after Theorem 4.2]],
records spread $\Omega(\log n/\log\log n)$, citing Lovett–Solomon–Zhang
(2019). The explicit constructions here are not a novelty claim for that
existence result or its asymptotic order.

## The route this closes

Write $n$ for the size of the sets and $k$ for the number of petals, as in
[[problems/set_systems/E0020/_index|Problem 20]]. A family $\mathcal F$ of
$n$-sets is *absolutely $R$-spread* if every nonempty $T$ lies in at most
$R^{n-|T|}$ members, and *normalized $R$-spread* if every nonempty $T$ lies in
at most $R^{-|T|}|\mathcal F|$ members, which forces $|\mathcal F|\ge R^n$.

The matching lemma $M(k)$ asks for a constant $R_k$ such that every
absolutely $R_k$-spread family of $n$-sets with more than $R_k^n$ members has
$k$ pairwise disjoint members, for every $n$. It would give
$f(n,k)\le\lfloor R_k^n\rfloor+1$, and settle the strict form of Problem 20
after enlarging the base, for example to $R_k+2$.
Given $|\mathcal F|>R_k^n$, choose an inclusion-maximal $T$ with
$|\mathcal F_T|>R_k^{n-|T|}$; the empty set qualifies, and $|T|<n$ since an
$n$-set lies in at most one member. The link
$\{S\setminus T:S\in\mathcal F_T\}$ is absolutely $R_k$-spread by maximality
and has more than $R_k^{n-|T|}$ members, and $k$ disjoint members of it lift to
a $k$-sunflower with core $T$. This is the remark accompanying Rao's
[[../library/set_systems/rao_2020_coding_sunflowers/lemma_2|Lemma 2]], whose
source says the lemma might hold with $r(p,k)=O(p)$, and
[[../library/set_systems/bell_2021_note_sunflowers/lemma_2|Bell–Chueluecha–Warnke's Lemma 2]]
is $M(k)$ with $R_k$ replaced by $Ck\log n$.

L214 gives intersecting families, hence families without two disjoint
members, that are absolutely $r$-spread with more than $r^n$ members for
every real $r\ge16$, and normalized $\rho$-spread for every integer
$\rho\ge2$. The
[[research/sunflower_exponential_bound/refined_spread_obstructions|general thinning lemma]]
extends the absolute examples to every $r\ge2$. Thus $M(k)$ fails for
every $k\ge3$: if $r<k-1$, use $k-1$ singletons, and if $r\ge k-1$,
use an intersecting example. For $k=2$ the examples refute every $r\ge2$,
but not $r=1$, where absolute spread itself forces disjointness.
The converse of the link argument
needs no lemma: Problem 20 with constant $c_k$ gives a $k$-sunflower in every
family with more than $c_k^n$ members, spread or not. So Problem 20 is
equivalent to the spread form

> **SF($k$).** For each $k\ge3$ there is $R_k$ such that every absolutely
> $R_k$-spread family of $n$-sets with more than $R_k^n$ members contains a
> $k$-sunflower,

and the families of L214 show that the sunflower in SF($k$) cannot always be
taken with an empty core.

## Substitution and the seed quantity

For an $a$-uniform family $G$ and a uniform family $H$, the substitution
$G[H]$ replaces each point $i$ of a member $A\in G$ by a member $S_i$ of a copy
of $H$ placed over $i$; its powers are $G^1=G$ and $G^{h+1}=G[G^h]$. Two members
of $G[H]$ meet whenever $G$ and $H$ are intersecting, because their root sets
share a point $i$ and their fibers over $i$ meet. The key fact is that spread
behaves exactly under substitution. With the excess
$E_{\mathcal F}(R)=\max_{T\ne\varnothing}\Pr[T\subseteq S]R^{|T|}$ of a uniform
random member $S$, and
$\psi_G(E)=\max_{I\ne\varnothing}\Pr[I\subseteq A]E^{|I|}$ for a uniform random
$A\in G$, Lemma 2 of the L214 proof gives

$$
E_{G[H]}(R)=\psi_G\bigl(E_H(R)\bigr),\qquad E_{G^h}(R)=\psi_G^{(h)}(R),
$$

and $\mathcal F$ is normalized $R$-spread exactly when $E_{\mathcal F}(R)\le1$.

**Proposition (author-recorded).** Let $G$ be an intersecting $a$-uniform
family, $a\ge2$, in which no point lies in every member, and put

$$
\rho(G)=\min_{|I|\ge2}\Pr[I\subseteq A]^{-1/(|I|-1)},
$$

the minimum over sets $I$ contained in a member. Then the largest $R$ for
which $G^h$ is normalized $R$-spread tends to $\rho(G)$ as $h\to\infty$, and
it is at most $\rho(G)$ for every $h$.

*Proof.* If $R>\rho(G)$, some $I$ with $|I|\ge2$ has
$\Pr[I\subseteq A]R^{|I|-1}>1$, so $\psi_G(E)>E$ for every $E\ge R$ and the
iterates from $R$ never fall to $1$. If $1\le R<\rho(G)$, then on $[1,R]$ every
term of $\psi_G$ is below the identity: sets with $|I|\ge2$ give
$\Pr[I\subseteq A]E^{|I|}\le E(E/\rho(G))^{|I|-1}<E$, and singletons give at most
$p_1E<E$, where $p_1<1$ is the largest point probability. By continuity
$\psi_G(E)\le E-\delta$ on $[1,R]$ for some $\delta>0$, so the iterates fall
below $1$, and they stay there because $\psi_G(E)\le E$ for $E\le1$.
$\square$

So building spread intersecting families reduces to one level: a seed must
make every set of two or more points rare, with the singletons free except for
$p_1<1$. Three seeds show the range.

- The triangle, the three $2$-subsets of a $3$-set, has $\rho=3$. Its powers
  are the minterm families of recursive majority of three, whose spread rises
  to $3$; it is $1.5$ at $h=1$ and about $2.12$, $2.52$, $2.75$ and $2.87$ at
  $h=2,3,4,5$.
- The Hilton–Milner type seed, $\{B\}$ together with all sets $\{x\}\cup B'$
  where $B'$ is an $(a-1)$-subset of a set $Y\supseteq B$ meeting the $a$-set
  $B$, has $\rho$ close to $a$ when $|Y|$ is large compared with $a^2$, so
  spread is unbounded already. Its point $x$ lies in all members but one, so
  the leaf reached through $x$ at every level of $G^h$ lies in a fraction
  $(1-1/|G|)^h$ of the members; spread $R$ needs at least $|G|\ln R$ levels,
  and the uniformity is doubly exponential in the spread.
- The two-star block seed $B(\rho,\rho^\rho)$ of L214 has
  $\rho(G)=2^{1/\rho^\rho}\rho$ and $p_1=1/2$: both centers lie in half of the
  members, the members of the first kind are a product family of spread
  exactly $\rho$, and a member of the second kind must contain a whole block
  $Y_i$, which the $\rho^\rho$ blocks make as rare as $\rho$-spread requires.
  Its excess halves at each level, so $\lceil\log_2\rho\rceil$ levels suffice.

## Rate and every large n

The block seed gives normalized spread $\rho$ at uniformity
$n=(\rho^\rho+1)^{\lceil\log_2\rho\rceil}$, so $\log_2n=(1+o(1))\rho(\log_2\rho)^2$
and the spread is $(1+o(1))\log_2n/(\log_2\log_2n)^2$. The absolute form loses
the factor $16$ of L214's thinning lemma.

**Remark (author-recorded): every large $n$.** Let $N_0=(\rho^\rho+1)^h$ with
$h=\lceil\log_2\rho\rceil$, and let $n\ge(\rho+1)N_0$. Write $n=qN_0+j$ with
$q=\lfloor n/N_0\rfloor\ge\rho+1$ and $0\le j<N_0$. The family
$B(\rho,q-1)[B(\rho,\rho^\rho)^h]$ is intersecting, $qN_0$-uniform and
normalized $\rho$-spread: the inner power is normalized $\rho$-spread by L214,
and Lemma 3 of the L214 proof gives $\psi_{B(\rho,q-1)}(E)\le E$ for
$E\le\rho$. Add to each member $j$ new points
of its own. A set $T$ meeting the new points of a member lies in that member
only, so the result is normalized $R$-spread for $R=\rho^{qN_0/n}$, which is at
least $\rho^{(\rho+1)/(\rho+2)}=(1-o(1))\rho$. Choosing the largest $\rho$ with
$(\rho+1)N_0\le n$, every large $n$ carries an intersecting family of $n$-sets
with normalized spread at least $(1-o(1))\log_2n/(\log_2\log_2n)^2$.

In the absolute form, Bell–Chueluecha–Warnke's Lemma 2 caps the spread of an
intersecting family at $C\log n$. In the normalized form, a uniformly weighted
family is spread in the weighted sense of Alweiss, Lovett, Wu and Zhang exactly
when it is normalized spread, and a uniformly random half of the ground set
contains a member of an intersecting family with probability at most $1/2$,
since the half and its complement cannot both contain one. Their
[[../library/set_systems/alweiss_2020_improved_bounds_sunflower_lemma/theorem_2_5|Theorem 2.5]]
with $\alpha=\beta=1/2$ therefore caps the normalized spread at
$O(\log n\log\log n)$, and Rao's improvement, which they record, at
$O(\log n)$. So the least spread that forces two disjoint members lies between
$c\log n/(\log\log n)^2$ and $C\log n$. Through the link argument a matching
lemma at spread $R$ gives $f(n,k)\le\lfloor R^n\rfloor+1$; at the uniformities
of L214 no valid matching lemma has $R$ below the spread of these families.

The same step appears outside the sunflower problem. Kupavskii and Zakharov's
spread-approximation method (*Spread approximations for forbidden
intersections problems*, arXiv:2203.13379v3, proof of Lemma 9, pp. 7--8) uses
that two families of $k$-sets whose measures are $r$-spread with
$r>2^{11}\log_2(2k)$ cannot be cross-intersecting, by a random halving. An
intersecting family is cross-intersecting with itself, so L214 shows that this
logarithm cannot be replaced by a constant, nor by anything below
$c\log k/(\log\log k)^2$. This bears only on the generality of that step:
their families are spread because they are homogeneous subfamilies of a
complete layer, which the families of L214 are not, and no theorem of theirs
is contradicted.

## Where the sunflowers are

For Problem 20 the relevant question is how spread families with no $k$
disjoint members still contain $k$-sunflowers. The core lemma, Lemma B in
[[theory/set_systems/L215_spread_large_core_sunflowers/_proof|the proof of L215]],
answers this for substitutions. If $G$ is intersecting and $H$ is intersecting
and free of $k$-sunflowers, $k\ge3$, then the root sets of a $k$-sunflower of
$G[H]$ form a $k$-sunflower of $G$ with a nonempty core $A_*$. Its core is the
union of the common fibers over $A_*$, so it consists of whole members of
$H$. In particular $G[H]$ is free of $k$-sunflowers when $G$ is.

Three consequences follow.

- **No sunflowers at spread below $\sqrt{10}$.** The triangle has no
  $3$-sunflower, so the recursive majority families are intersecting,
  $3$-sunflower-free and have normalized spread approaching $3$. A better seed
  is the family of ten triples of a $6$-set
  $\{012,013,024,035,045,125,134,145,234,235\}$. It contains one triple from
  each complementary pair, so it is intersecting, and every pair of points lies
  in exactly two triples. It is $3$-sunflower-free, since a core of two points
  would need three triples through one pair, and the link of each point is a
  five-cycle, which has no three disjoint edges. Its seed quantity is
  $\rho=\sqrt{10}$, from the triples, with $p_1=1/2$. Its powers are therefore
  intersecting, $3$-sunflower-free and normalized $R$-spread for every
  $R<\sqrt{10}$ once the power is large enough. So the threshold $R_3$ of
  SF($3$) is at least $\sqrt{10}$ in the normalized
  form. The same powers have $10^{(3^h-1)/2}$ members of size $3^h$; how this
  compares with the published lower bounds for three-petal sunflowers was not
  checked here.
- **Cores of every size are forced.** Substituting the triangle powers $D^g$
  into the block-family powers of L214 gives
  [[theory/set_systems/L215_spread_large_core_sunflowers/_index|L215]]: for
  every $R\ge3$ and $g$ an intersecting family with $R$-spread uniform measure
  in which every $k$-sunflower, for every $k\ge3$, has a core of at least $2^g$
  points. The outer block levels absorb the excess $3(R/3)^{2^g}$ that the
  inner triangle powers carry, halving it at each level. At fixed $R>3$ these
  cores have about $\log_2\log_2n/\log_2(R/3)$ points.
- **The block powers have one-point cores.** In $B(\rho,m)$ the members
  $\{x\}\cup T_1,\dots,\{x\}\cup T_\rho$ with pairwise disjoint transversals
  form a $\rho$-sunflower with core $\{x\}$. In $B(\rho,m)^h$, take these
  members at the root, a $\rho$-sunflower of $B(\rho,m)^{h-1}$ with a one-point
  core over $x$, and arbitrary members over the other points. The core is the
  single leaf reached through $x$ at every level.

**Remark (author-recorded): the core point can be light.** With
$B=B(\rho,\rho^\rho)$, the power $B^h$ is normalized $\rho$-spread for every
$h\ge\lceil\log_2\rho\rceil$, since the excess only decreases at further levels.
Every point of $B$ lies in at most half of its members, so every point of $B^h$
lies in at most a fraction $2^{-h}$ of the members, far below the fraction
$1/\rho$ that spread allows. So a spread family without two disjoint members
need not have any point of degree at least $|\mathcal F|/(C\rho)$, however
large $C$ is. A recursion in the style of Erdős and Rado, which passes to the
link of a point of large degree and loses only a constant factor, therefore
fails at its first step. The leaf $\ell$ reached through $x$ at every level
nevertheless carries a good link: it lies in exactly a fraction $2^{-h}$ of the
members, and since $E_{B^h}(\rho)\le\rho2^{-h}$, every $U$ outside $\ell$
satisfies $\Pr[U\cup\{\ell\}\subseteq S]\le2^{-h}\rho^{-|U|}$. So the link at
$\ell$, with its own uniform measure, is again normalized $\rho$-spread, and it
contains the sunflower petals above. The point that leads to a sunflower is
light, but no superset of it is heavier relative to its size.

So a proof of SF($k$) must produce sunflowers with nonempty cores, and in
some spread families with cores of unbounded size; the core cannot be bounded
in terms of $k$ and the spread alone.

## Open questions

- **The exact threshold for two disjoint members.** Close the gap between
  $c\log n/\log\log n$ and $C\log n$. The lower order is known from the
  source comparison above and is also attained by the
  [[research/sunflower_exponential_bound/refined_spread_obstructions|varying-scale construction]].
  A seed with $\rho(G)\ge\rho$,
  $p_1\le1/2$ and uniformity $e^{o(\rho\log\rho)}$ would improve the lower
  bound; the block seed needs $\rho^\rho$ blocks because each member of its
  second kind contains a whole block. No seed can do much better: if
  $\rho(G)\ge\rho$ and $p_1\le1/2$, then $\psi_G(E)\le\max(E/2,E^2/\rho)=E/2$
  for $E\le\rho/2$, so $G^h$ with $h=\lceil\log_2\rho\rceil$ is normalized
  $(\rho/2)$-spread, and the normalized cap of order $\log n$ above forces
  $\log a\ge c\rho/\log\rho$ for the uniformity $a$ of an intersecting seed
  $G$.
- **Many petals.** For $k$ disjoint members the products of blocks of size
  $k-1$ give spread $k-1$, and the intersecting examples give
  $c\log n/\log\log n$. The combined dependence on $k$ and $n$ is not
  determined by these constructions.
- **A core-finding lemma.** SF($k$) is equivalent to Problem 20. A route through
  spread families must replace $M(k)$ by a statement that produces a
  sunflower with a nonempty and possibly large core when the family has no $k$
  disjoint members. By L215 such a core can need about
  $\log\log n/\log R$ points; a single choice of a large core or a recursion
  into links would both be consistent with this obstruction. The
  [[research/sunflower_exponential_bound/proof_sketch|proof sketch]] records the
  candidate statements and their status.
