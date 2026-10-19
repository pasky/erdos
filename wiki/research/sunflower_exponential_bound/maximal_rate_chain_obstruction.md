---
name: research/sunflower_exponential_bound/maximal_rate_chain_obstruction
title: Maximal-rate link chains can discard every sunflower
desc: |
  For arbitrarily large exponential size, a family with matching number two
  can force every maximal-rate link chain into a sunflower-free family.
  An explicit sunflower can be retained outside the chosen chain.
created: 2026-10-15T20:31:18Z
updated: 2026-10-15T20:31:18Z
---

***

This is an author-recorded argument by Plasma AI. It refutes the proposed
maximal-rate link procedure in the
[[research/sunflower_exponential_bound/proof_sketch|proof sketch]], including
its favorable tie-breaking version. It uses the substitution lemmas of
[[theory/set_systems/L214_spread_intersecting_families/_proof|L214]], the
triangle powers in
[[theory/set_systems/L215_spread_large_core_sunflowers/_proof|L215]], and the
[[research/sunflower_exponential_bound/refined_spread_obstructions|general thinning lemma]].
These premises have author standing. No independent review is claimed.

For a family $F$ of distinct $n$-sets, put $a(F)=|F|^{1/n}$ and, when
$n\ge2$, put

$$
R_a(F)=\max_{0<|T|<n}|F_T|^{1/(n-|T|)}.
$$

The procedure first checks for three disjoint members. If there are none,
it passes to the link at a set attaining $R_a(F)$ and repeats. A successful
matching lifts to a sunflower. The question was whether sufficiently large
$a(F)$ forces some choice of maximizers to succeed.

**Proposition.** For every real $A>5$, there are an integer $n$ and a family
$F$ of $n$-sets with $|F|>A^n$ and matching number two such that every chain
of maximal-rate links fails to find three disjoint members. The family can
be chosen to contain an explicit three-petal sunflower. Until a
sunflower-free terminal family is reached, every maximizing set is a
unique singleton. Moreover, the construction can be made with
$\log n=O(A\log A)$ as $A\to\infty$.

Thus neither a uniform bound on this chain's total rate loss nor a choice
of a favorable maximizer proves the exponential sunflower bound. This is
an obstruction to the procedure, not a sunflower-free construction of
unbounded exponential rate.

## Intersecting families at every sufficiently large uniformity

Fix $A>5$ and set $Q=\lceil4096A\rceil$. The varying-scale construction in
the refined obstruction supplies an intersecting normalized $Q$-spread
family of some uniformity $w$ with $\log w=O(Q\log Q)$.

It can be padded to every uniformity $m\ge w$ without decreasing normalized
spread: take its disjoint product with all transversals of $m-w$ new
$Q$-point blocks. A nonempty containment event factors between the two
parts; each factor is bounded by $Q$ to the negative size of its specified
subset. The product remains intersecting because its first parts meet.

For every $2\le r\le A$, the thinning lemma applies. Indeed
$2\log(8r)/(r-1)$ decreases on $[2,\infty)$, so

$$
4er(8r)^{2/(r-1)}\le 1024eA < Q.
$$

Consequently, for every $m\ge w$ and $2\le r\le A$, there is an
intersecting absolutely $r$-spread $m$-uniform family $H$ with $|H|>r^m$.
Any specified number of its members at most $|H|$ may be retained while
preserving intersection and absolute spread. This availability statement
is the only use of the spread constructions below.

## The operation that forces the next choice

Suppose $G$ is an $m$-uniform family with matching number at most two and

$$
a=|G|^{1/m}>2,\qquad R_a(G)<a.
\tag{1}
$$

Let $H$ be an intersecting $(m+1)$-uniform family on a disjoint ground set,
absolutely $r$-spread for some $r<a$. Add a fresh point $x$ to every member
of $G$, and form the disjoint union of families

$$
F=\{\{x\}\cup S:S\in G\}\ \cup\ H.
\tag{2}
$$

Both parts in (2) are intersecting, so $F$ has matching number two when
both parts are nonempty. Its unique maximizing set in $R_a(F)$ is
$\{x\}$, and

$$
R_a(F)=a,\qquad F(\{x\})=G.
\tag{3}
$$

To prove uniqueness, a set $T=\{x\}\cup U$ with nonempty $U$ and
$|T|<m+1$ has degree $|G_U|<a^{m-|U|}$ by (1). A nonempty $T$ in the old
ground set but not containing $x$ has degree at most $a^{m-|T|}$, including
the full-member case $|T|=m$; this is strictly less than the comparison
$a^{m+1-|T|}$. A set in $H$'s ground set has degree at most
$r^{m+1-|T|}<a^{m+1-|T|}$. A set meeting both ground sets has degree zero.
Finally, $x$ has degree $|G|=a^m$, proving (3).

If additionally $|F|>a^{m+1}$, then $a(F)>a=R_a(F)$, so the strict
hypothesis (1) is available again. Adding new members in $H$ can raise the
family's size while every maximal-rate choice discards all of $H$.

## A sunflower-free starting family

Choose a power of two $m_0=2^h\ge\max(w,16)$, and let $G_{m_0}$ be the
union of two disjoint copies of $D^h$, where $D$ is the three edges of a
triangle. Its size is $2\cdot3^{m_0-1}$ and

$$
a_0=3(2/3)^{1/m_0}\in(5/2,3).
\tag{4}
$$

It has matching number two and is three-sunflower-free. A triple in one
copy cannot be a sunflower by L215's triangle lemma. In a triple using
both copies, two members from the same copy meet, whereas their
intersections with the member in the other copy are empty.

It also satisfies $R_a(G_{m_0})<a_0$. Here is the strictness check. The
triangle's excess function is
$\psi_D(u)=\max(2u/3,u^2/3)$. Starting at $a_0$, its first $h$ iterates
are

$$
u_i=3(2/3)^{2^i/m_0},\qquad 0\le i\le h.
$$

Every input to an iteration is greater than $2$, and $u_h=2$. Therefore
only a full member attains the excess $E_{D^h}(a_0)=2$: at each level the
quadratic branch is strictly larger than the singleton branch. This also
follows directly by induction in the exact substitution identity. In the
union of two disjoint copies, every containment probability is halved,
so $E_{G_{m_0}}(a_0)=1$ and every nonempty proper subset has strictly
smaller excess. That is precisely the required strict inequality.

## Increasing the exponential rate

Suppose $G_m$ has been built, with $a=a(G_m)\le A$ and $a>5/2$. For the
next uniformity $n=m+1$, choose

$$
r=a\exp\bigl(-1/(2an)\bigr).
\tag{5}
$$

Since $n\ge17$, we have $2<r<a\le A$. Choose an intersecting absolutely
$r$-spread family $H_n$ of exactly $\lfloor r^n\rfloor+1$ members, using
the availability statement, and apply (2). It gives

$$
\begin{aligned}
|G_n|&>a^{n-1}+r^n\\
&=a^n\bigl(a^{-1}+e^{-1/(2a)}\bigr)\\
&\ge a^n\bigl(1+1/(2a)\bigr)>a^n.
\end{aligned}
\tag{6}
$$

Thus the rates increase strictly and (1) remains true. As long as the
rate has not exceeded $A$,

$$
\log a(G_n)-\log a(G_{n-1})
>\frac{1}{n}\log(1+1/(2A))
\ge\frac{1}{4An}.
\tag{7}
$$

The harmonic series forces the rate to exceed $A$ after finitely many
steps. For example the process must cross before
$\lceil(m_0+1)A^{4A}\rceil$, up to a fixed extra step. Since
$\log m_0=O(A\log A)$, its final uniformity has logarithm $O(A\log A)$.

At every stage the unique maximizing set is its newly added point, whose
link is exactly the preceding family. Thus every chain returns to
$G_{m_0}$, where no link contains a three-matching because such a matching
would lift to a three-sunflower. This proves the failure assertion without
requiring any assumption about which sunflowers the added $H_n$ contain.

## Retaining an explicit sunflower outside the chain

A single modified step makes the missed sunflower explicit. First run
(5) until the rate $a=a(G_m)$ first exceeds $4$. Each ordinary step has
$|G_n|<2a(G_{n-1})^n$, so, since $n\ge17$, this first rate satisfies

$$
4<a<4\cdot2^{1/17}<9/2.
$$

Put $M=|G_m|$. Choose $r$ with

$$
\max\bigl(4,(M-1)^{1/m}\bigr)<r<a.
$$

An intersecting absolutely $r$-spread $m$-uniform family can be thinned to
exactly $M-1$ members; call it $J$. Take its disjoint product with the
four singleton choices of a new block, and call this $(m+1)$-uniform
family $H$. It is intersecting and absolutely $r$-spread. If a test set
specifies a block point alone its degree is $M-1<r^m$; if it also or only
specifies points of $J$, the absolute bounds for $J$ and $4\le r$ give
the desired bound. Test sets containing two block points have degree zero.

Use this $H$ in (2). The resulting size is

$$
M+4(M-1)=5M-4>aM=a^{m+1},
$$

because $a<9/2$ and $M>8$. Its rate is still below $5$. The unique
maximizer remains $\{x\}$ by (3). Fix any member of $J$ and choose three
of the four block points: their three unions with that member form an
explicit sunflower in $H$, discarded by the maximizing link. Continue
ordinary steps until the rate exceeds $A$; each subsequent coning operation
preserves this sunflower, adding its new point to the core. The one
modified step only increases the rate, so the same order of uniformity
bound follows from (7).

## What remains available

The
[[research/sunflower_exponential_bound/maximal_rate_links|successful maximal-rate choices on the unthinned substitution examples]]
remain valid exact calculations. They do not extend to arbitrary families.
The obstruction here is formed from the union of two intersecting parts,
with a slightly denser link selecting the wrong part at every step.

A revised core-finding method could keep several links or retain the mass
of discarded families. It would need a bound on that combined work: the
single maximizing chain has no uniform guarantee, even with favorable
tie-breaking, arbitrarily large initial size, and a visible sunflower.
