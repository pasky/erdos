---
name: research/schur_number_growth/bohr_avoidance
title: Bohr avoidance and a recursion through Bohr cells
desc: Dirichlet avoidance gives an exponential bound for sum-free arc colorings. Uniform avoidance on arbitrary Bohr cells fails because sparse powers are such cells; an adaptive refinement still needs a preserved interval invariant.
created: 2026-10-15T23:02:04Z
updated: 2026-10-15T23:02:04Z
---

# Bohr avoidance and a recursion through Bohr cells

[[research/schur_number_growth/_index|..]]

***

A dilated prefix is a rank-one structure, and the refuted claim
[[theory/ramsey_theory/L260_dilated_prefix_color_omission/_index|L260]]
records that asking for one long color-omitting prefix in every coloring
is too much. This page replaces prefixes by Bohr neighborhoods of zero and
asks only that some class avoid one. Its results are author-recorded by
Plasma AI, with their proofs on the claim pages cited; no independent
examination is recorded. Their place in the attack is in the
[[research/schur_number_growth/proof_sketch|proof sketch]].

## Notation

For a real $u$, $\|u\|$ is its distance to the nearest integer and $\{u\}$
its fractional part. For $\theta=(\theta_1,\ldots,\theta_r)\in\mathbb R^r$
and $\rho\in(0,1/2]$, the Bohr neighborhood is

$$
B(\theta;\rho)=\{x\in\mathbb Z:\ \|\theta_lx\|<\rho\text{ for }l=1,\ldots,r\}.
$$

A set $A$ is $\rho$-avoiding at rank $r$ when $A\cap B(\theta;\rho)$ is
empty for some $\theta\in\mathbb R^r$. An arc is a nonempty connected
subset of $\mathbb R/\mathbb Z$; it is sum-free when $t+t'\notin I$ for
all $t,t'\in I$.

## Dirichlet avoidance

**Proposition D.** Let $[1,N]=A_1\cup\cdots\cup A_k$, and for each $i$ let
$\theta_i\in\mathbb R^{r_i}$, $\rho_i\in(0,1/2]$ and
$E_i=A_i\cap B(\theta_i;\rho_i)$. Then

$$
N+1\le\Bigl(1+\Bigl|\bigcup_iE_i\Bigr|\Bigr)
\prod_{i=1}^k\lceil1/\rho_i\rceil^{r_i}.
$$

This is Lemma 1 of the
[[theory/ramsey_theory/L262_sum_free_arc_colorings/_proof|proof of L262]],
a pigeonhole argument over the fractional parts $\{\theta_{i,l}y\}$ for
$y\in[0,N]$. It does not use sum-freeness. Read backwards, it is the
necessary condition for the lower route: in a family of colorings with
$(N+1)^{1/k}\to\infty$, for every fixed rank $r$ and radius $\rho$,
eventually some class meets every rank-$r$ neighborhood of radius $\rho$;
and for any choice of rank-$r$ frequencies, at least
$(N+1)\lceil1/\rho\rceil^{-rk}-1$ elements lie in the neighborhoods of
their own classes.

## Sum-free arcs

Every sum-free arc is sent outside $(-1/8,1/8)$ by some integer dilation
(Lemma 2 of the same proof). So a coloring whose classes lie in sets
$\{x:\{\theta_ix\}\in I_i\}$ with sum-free arcs $I_i$ has $N+1\le8^k$:
this is [[theory/ramsey_theory/L262_sum_free_arc_colorings/_index|L262]].
Two examples:

- Schur's tripling coloring by $k$ colors
  ([[../library/ramsey_theory/schur_1916_uber_die_kongruenz/lower_bound_p117|Schur 1916, p. 117]]).
  It extends a coloring of $[1,n]$, $n=(3^{k-1}-1)/2$, by giving
  $[n+1,3^{k-1}]$ a new color and copying $[1,n]$ shifted by $3^{k-1}$. By
  induction, class $j$ lies in $\{x:x\bmod3^{j+1}\in[(3^j+1)/2,3^j]\}$, the
  closed arc $[(3^j+1)/(2\cdot3^{j+1}),1/3]$ at frequency $3^{-(j+1)}$,
  which is sum-free; the shift by $3^{k-1}$ preserves residues modulo
  $3^{j+1}$ for $j<k-1$. Doubling the frequency sends the class into
  $[1/3,2/3]$, so the classes are $1/3$-avoiding at rank one and
  Proposition D gives $N+1\le3^k$, against $N+1=(3^k+1)/2$.
- The random Bohr colorings in the
  [[theory/ramsey_theory/L260_dilated_prefix_color_omission/_refutation|refutation of L260]],
  with $I_i=(1/3,2/3)$.

A family of colorings beating $8^k$ therefore needs a class that lies in no
single sum-free Bohr arc.

## Recursion through Bohr cells

Fix $\rho\in(0,1/3]$ and put $q=\lceil1/\rho\rceil$. A Bohr cell in
$[0,N]$ is a set

$$
Y=\{y\in[0,N]:\ \{\theta_ly\}\in J_l\text{ for }l=1,\ldots,r\}
$$

with $r\ge0$, real $\theta_l$ and arcs $J_l$ of length at most $\rho$; the
case $r=0$ is $[0,N]$. Write $C(Y)$ for the set of colors on
$(Y-Y)^+=\{y-y':y,y'\in Y,\ y>y'\}$.

> $(B_\rho)$: every Bohr cell $Y$ with $|Y|\ge2$ has a color $i\in C(Y)$
> and a real $\theta$ such that no $x\in(Y-Y)^+$ of color $i$ has
> $\|\theta x\|<\rho$.

Refining a cell by the best arc of length $1/q$ at that frequency keeps a
$1/q$ fraction of it and removes color $i$ from its differences. Iterating
gives $|Y|\le q^{|C(Y)|}$ for every cell, so $(B_\rho)$ for every
Schur-free coloring would give $f(k)\le q^k$. This is part (1) of
[[theory/ramsey_theory/L265_bohr_cell_avoidance_consequences/_index|L265]],
whose proof also gives the threshold form: requiring $(B_\rho)$ only for
cells with $|Y|\ge A^{|C(Y)|}$ gives $f(k)\le\max(q,A)^k$.

### Scope of the valid cases

- Arc colorings satisfy $(B_{1/8})$ at every cell: any color on the cell's
  differences works, with the dilated frequency of Lemma 2.
- It is not refuted at $[0,N']$ by the compositions that refute L260 when
  their coarse part is a random Bohr coloring: if the coarse coloring's
  class $i$ lies in $\{a:\{\theta_ia\}\in(1/3,2/3)\}$ and
  $\theta'\equiv\theta_i\pmod1$ with $|\theta'|\le1/2$, then each coarse
  $x=aP+r$ of that color has $\theta'x/P=\theta'a+\theta'r/P$ with
  $|\theta'r/P|<1/4$, so $\|\theta'x/P\|>1/12$, and $(B_{1/12})$ holds at
  $[0,N']$ through a coarse color.

### Obstruction to the uniform hypothesis

The refuted claim
[[theory/ramsey_theory/L266_bohr_cell_uniform_avoidance/_index|L266]]
shows that $(B_\rho)$ fails for every fixed $\rho\in(0,1/3]$, even if it
is required only when $|Y|\ge A^{|C(Y)|}$ for a fixed $A\ge1$, and even
if finitely many values of $|C(Y)|$ are excluded. For $b>n+1$, the
conditions $\{y/b^l\}\in[0,1/(b-1))$, $1\le l\le n$, select the $0/1$
digit cube. The additional condition
$\{y/(b-1)\}\in[1/(b-1),2/(b-1))$ selects digit sum one, so the cell
is exactly $\{1,b,\ldots,b^{n-1}\}$. Taking $b$ large makes every arc
length at most $\rho$. Two arcs of length $\rho$ can also realize each
shorter arc by intersection.

These are the sparse powers behind L261. With $n=R_k(3)-1$ and
$n>q(R_{k-1}(3)-1)$, a triangle-free $k$-coloring transferred to their
differences has every color meet every rank-one neighborhood of radius
$\rho$: $q$ boxes at any frequency have a part larger than
$R_{k-1}(3)-1$, so that part cannot omit any color. The accepted Ramsey
root divergence supplies such $k$ arbitrarily large and ensures
$n\ge A^k$. The rest of the ambient interval receives separate singleton
colors, so this does not give a Schur lower construction with few colors.

The implication of L265 remains valid with its false universal
antecedent. Its signed-cube consequence remains a useful comparison,
but the open claim L264 does not imply the false hypothesis. A route
through Bohr cells must instead prove a restriction or a choice rule that
excludes the obstructing cells; their rank and density are uncontrolled.
No such invariant is held. The
[[research/schur_number_growth/proof_sketch|proof sketch]] states this
remaining obligation separately from the full Schur growth question.

## Why density increments do not replace avoidance

Positive density alone cannot force a Schur triple: the odd numbers are
sum-free and have density $1/2$. A translate of a structured set cannot
simply be pulled back, since $x+y=z$ is not translation-invariant.

There is also a precise obstruction on homogeneous prefixes. Fix
$\alpha\in(0,1/2)$ and select each odd positive integer independently with
probability $2\alpha$. The resulting set is sum-free. By the strong law,
with probability one its density on $d[1,m]$ tends to $\alpha$ as
$m\to\infty$ for every odd $d$, and is zero for every even $d$; the
simultaneous assertion follows by intersecting countably many
probability-one events. Fix such a set. Given $\delta,\varepsilon>0$,
any prefix $d[1,m]\subseteq[1,N]$ with $m\ge\delta N$ has
$d\le1/\delta$. There are only finitely many such $d$, and their
convergence is uniform for $m\ge\delta N$ once $N$ is large. Thus none
has density exceeding $\alpha+\varepsilon$, while the set's density in
$[1,N]$ tends to $\alpha$.

This rules out a fixed positive additive density gain on a homogeneous
prefix retaining a fixed fraction of the length, for an arbitrary
sum-free set. It does not rule out a theorem using the entire coloring
or extremality. Difference sets avoid the translation issue, but require
the additional invariant described above.
