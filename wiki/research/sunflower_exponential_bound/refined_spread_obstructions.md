---
name: research/sunflower_exponential_bound/refined_spread_obstructions
title: Varying substitution scales and thinning spread families
desc: |
  Decreasing block scales give intersecting families with spread of order
  log n/log log n. An anchored first-moment argument converts normalized
  spread to absolute spread without a bound on the original family size.
created: 2026-10-15T20:31:18Z
updated: 2026-10-15T20:31:18Z
---

***

These are author-recorded deductions by Plasma AI. They use the elementary
substitution and block-family lemmas in
[[theory/set_systems/L214_spread_intersecting_families/_proof|the proof of L214]],
at tier 0. They sharpen this substitution construction's obstruction to
finding disjoint members from spread alone and transfer
[[theory/set_systems/L215_spread_large_core_sunflowers/_index|L215's large-core construction]]
to the absolute convention. They do not produce sunflower-free families
of unbounded exponential rate, and hence do not settle
[[problems/set_systems/E0020/_index|Problem 20]].

The order $\log n/\log\log n$ for intersecting normalized-spread families
is already recorded by
[[../library/set_systems/alweiss_2020_improved_bounds_sunflower_lemma/_index|Alweiss–Lovett–Wu–Zhang, Section 4 after Theorem 4.2]],
with attribution to Lovett–Solomon–Zhang (2019). The derivation below is
an alternative construction at that known order, not an improved lower
bound over the literature. The cited original construction is not a
premise of this proof and has not been checked here.

## Decrease the scale after each contraction

For an integer $R\ge2$, put $h=\lceil\log_2R\rceil$ and

$$
q_i=\left\lceil R/2^i\right\rceil,\qquad
B_i=B(q_i,q_i^{q_i}),\qquad 0\le i<h.
$$

Every $q_i\ge2$. Start with the family $F_0$ whose only member is a
one-point set, and define $F_{i+1}=B_i[F_i]$. By L214's substitution lemma,
every $F_i$ is intersecting. With $E$ denoting normalized excess, the block
lemma gives

$$
E_{F_{i+1}}(R)=\psi_{B_i}(E_{F_i}(R))\le\tfrac12E_{F_i}(R)
\quad\hbox{whenever }E_{F_i}(R)\le q_i.
$$

Starting from $E_{F_0}(R)=R$, induction gives
$E_{F_i}(R)\le R/2^i\le q_i$ for each required step. Thus $F_h$ is an
intersecting normalized $R$-spread family, of uniformity

$$
n_R=\prod_{i=0}^{h-1}(q_i^{q_i}+1).
\tag{1}
$$

In fact the excess halves exactly: the center of the first kind attains
$\psi_{B_i}(u)=u/2$ on $0<u\le q_i$.

This choice avoids paying the largest block scale at every level. In
natural logarithms,

$$
\log n_R=2R\log R-2R\log2+O((\log R)^2).
\tag{2}
$$

To check (2), write $x_i=R/2^i$. Replacing $x_i$ by its ceiling in
$x_i\log x_i$ changes each summand by $O(\log R)$, over $O(\log R)$
indices. Also
$\log(q_i^{q_i}+1)=q_i\log q_i+O(1)$, and the omitted tail of the infinite
sum $\sum_{i\ge0}x_i\log x_i$ is bounded. The geometric identities
$\sum2^{-i}=2$ and $\sum i2^{-i}=2$ give (2).

Consequently, along the uniformities (1), the spread is

$$
R=\left(\frac12+o(1)\right)
  \frac{\log n_R}{\log\log n_R}.
\tag{3}
$$

Thus the lower obstruction is of order $\log n/\log\log n$, rather than
the order $\log n/(\log\log n)^2$ obtained by using the same block family
at every level. This concerns matching thresholds, not the exponential
base needed for sunflower existence.

## Thinning without a family-size cap

**Thinning lemma.** Let $r\ge2$ and $n\ge2$, and suppose a nonempty family
$\mathcal H$ of distinct $n$-sets is normalized $Q$-spread. If

$$
Q\ge4er(8r)^{2/(r-1)},
\tag{4}
$$

then it has a subfamily $\mathcal H'$ with $|\mathcal H'|>r^n$ and
$|\mathcal H'_T|\le r^{n-|T|}$ for every nonempty $T$. In particular,
$Q\ge32r$ suffices when $r\ge16$.

There is no upper bound on $|\mathcal H|$ or its ground-set size in this
statement. All properties inherited by subfamilies, such as being
intersecting or excluding specified sunflower core sizes, survive.

*Proof.* Write $M=|\mathcal H|$. The normalized bound at a member gives
$M\ge Q^n$. Keep each member independently with probability
$p=2r^n/M<1$. The resulting size has mean $2r^n$ and

$$
\Pr(|\mathcal H'|\le r^n)\le e^{-r^n/4}\le e^{-1}.
\tag{5}
$$

For $1\le t<n$, put $a_t=\lfloor r^{n-t}\rfloor$ and
$d_T=|\mathcal H_T|$ for a $t$-set $T$. A bad set has at least $a_t+1$
retained members through it. Counting these witnesses, and first
distinguishing one of their original members, gives

$$
\begin{aligned}
\Pr(\exists T,\ |T|=t:\ |\mathcal H'_T|>r^{n-t})
&\le\sum_{|T|=t}p^{a_t+1}\binom{d_T}{a_t+1}\\
&\le\sum_{|T|=t}p\,d_T
       \left(\frac{epd_T}{a_t}\right)^{a_t}\\
&\le 2r^n\binom nt
       \left(4e(r/Q)^t\right)^{a_t}.
\end{aligned}
\tag{6}
$$

For the last step use $d_T\le M Q^{-t}$,
$\sum_{|T|=t}d_T=M\binom nt$, and
$a_t\ge(1-1/r)r^{n-t}$. The sum over $T$ is finite; sets outside all
members have $d_T=0$. The identity for the sum of $d_T$ replaces the
cruder estimate counting every possible $T$ separately.

Set $\delta=\log(Q/(4er))>0$. Since
$4e(r/Q)^t\le(4er/Q)^t$, and since

$$
t a_t\ge (1-1/r)t r^{n-t}\ge(n-1)(r-1),
$$

the sum of (6) over $1\le t<n$ is at most

$$
2(2r)^n\exp[-\delta(n-1)(r-1)]
\le2(2r)^n(8r)^{-n}
=2\,4^{-n}\le\frac18.
\tag{7}
$$

Here $t r^{n-t}$ is nonincreasing for $1\le t<n$ when $r\ge2$, and
(4) gives $\delta(r-1)\ge2\log(8r)$. There is no bad set of size $n$,
because each $n$-set is contained in at most one distinct member, and
larger sets have degree zero. Equations (5) and (7) have sum less than
one, proving existence.

Finally, $2\log(8r)/(r-1)$ decreases for $r\ge2$, and at $r=16$ it is
less than $\log(8/e)$. Thus $32r$ satisfies (4) for all $r\ge16$.
$\square$

The lemma generalizes the use of random thinning in L214's Lemma 4. That
lemma's stated hypotheses and proof remain sufficient for L214 itself;
the estimate above additionally applies when the original family has
arbitrarily many members.

## Consequences in the absolute convention

For every real $r\ge2$, choose an integer $R$ satisfying (4), and apply
the first construction followed by the thinning lemma. This gives an
intersecting absolutely $r$-spread family of $n_R$-sets with more than
$r^{n_R}$ members. If $r\ge16$, one may take $R=\lceil32r\rceil$; (2)
then gives intersecting absolute-spread examples at spread of order
$\log n_R/\log\log n_R$.

The quantifier matters for the proposed matching lemma. For every fixed
$k\ge3$ and every real $r>0$, the assertion that every absolutely
$r$-spread $n$-uniform family with more than $r^n$ members contains $k$
disjoint members fails for some $n$. If $r<k-1$, take $k-1$ singletons;
if $r\ge k-1\ge2$, use the intersecting construction just given.
For $k=2$ the same construction refutes every $r\ge2$. It does not
refute $r=1$: absolute $1$-spread itself forces distinct members to be
disjoint. This degenerate case must not be included in a claim that all
absolute matching constants fail.

For large cores, let $r\ge2$ and $g\ge0$. Choose $Q\ge3$ satisfying
(4), and apply L215 at normalized spread $Q$. Its family consists of
$n$-sets for $n\ge2$, is intersecting, and has no $k$-sunflower with core
smaller than $2^g$ for any $k\ge3$. The thinning lemma produces an
absolutely $r$-spread subfamily with more than $r^n$ members and exactly
the same exclusion. Thus a bounded-core replacement for the matching
lemma fails in the absolute convention as well.

These conclusions do not rule out finding a sunflower with an unbounded
core. The remaining obligation is the general core-finding argument in
the [[research/sunflower_exponential_bound/proof_sketch|proof sketch]].
