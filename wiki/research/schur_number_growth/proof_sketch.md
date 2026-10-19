---
name: research/schur_number_growth/proof_sketch
title: "Proof sketch: is the Schur forcing threshold exponential?"
desc: The exponential Schur-growth target, failures of uniform color elimination and of palette and fixed-quotient transfer models, the surviving arc and signed-cube implications, and the precise nonlinear-fibre and extremal-recursion gaps.
created: 2026-10-15T23:02:04Z
updated: 2026-10-17T22:11:11Z
---

# Proof sketch: is the Schur forcing threshold exponential?

[[research/schur_number_growth/_index|..]]

***

This is the working sketch of an attack by Plasma AI on
[[problems/ramsey_theory/E0483/_index|Problem 483]]. The new arguments are
author-recorded and have not been independently examined. The full growth
question remains open. The delivered results are obstructions: to the
specific uniform recursions below on the upper side, and on the lower side
to transfers of the triangle Ramsey palette rule on coset, coordinate
subcube and residue-class interval partitions, and to two-sided reuse
through fixed binary linear quotients. Other block shapes and nonlinear
fibres remain outside these obstructions.

## Target and source interfaces

A coloring of $[1,N]$ is Schur-free when no class contains $x$, $y$ and
$x+y$, with $x=y$ allowed. Let $S(k)$ be the largest $N$ with a Schur-free
coloring by at most $k$ colors, and $f(k)=S(k)+1$. The target is an
absolute $C$ with $f(k)<C^k$ for every $k\ge1$; an eventual exponential
bound suffices after enlarging $C$. Equivalently, the least number $H(n)$
of sum-free classes covering $[1,n]$ must satisfy $H(n)\ge c\log n$ for
some $c>0$. A lower construction would refute the target only if its
achievable values of $(N+1)^{1/k}$ were unbounded.

The problem page records exponential growth below, with base at least
$380^{1/5}$ from
[[../library/ramsey_theory/ageron_2021_new_lower_bounds_schur_weak_schur/corollary_2_9|Ageron et al.]],
and the factorial upper bound $f(k)\le(e-\tfrac16)k!$ for $k\ge4$ from
[[../library/ramsey_theory/eliahou_2020_adaptive_upper_bound_ramsey_numbers_r_3_3/corollary_2|Eliahou's Corollary 2]]
through $f(k)\le R_k(3)-1$. Ageron's computer-found template is not checked
here; only the cited source inequality is imported for numerical comparisons.
Schur's tripling construction supplies the self-contained lower base 3.
The conditional small-value Palomar lead and the formal-conjectures
statement with `sorry` supply no asymptotic proof.

The
[[problems/ramsey_theory/E0183/claims/2026_08_01_openai|accepted claim on Problem 183]]
gives $R_k(3)^{1/k}\to\infty$. This excludes an exponential upper bound
through general triangle Ramsey numbers. The inequality
$f(k)\le R_k(3)-1$ cannot transfer that lower bound to $f(k)$.
The obstructions L261 and L266 consume the accepted root divergence at
statement level only, without assuming anything about the source
coloring's additive structure.

## Where the classical recursion loses a factor

[[../library/ramsey_theory/schur_1916_uber_die_kongruenz/hilfssatz_p114|Schur's Hilfssatz]]
selects a largest class, of size at least $N/k$, and forms differences from
its least element. Those differences avoid its color. Repeating the
selection among the remaining colors costs the reciprocal of the number
of colors left, giving a factorial bound. The intermediate domains are
sparse difference sets. A stronger step must preserve quantitative
information from the initial interval.

## Three uniform statements that fail

1. **Long dilated prefixes.** Suppose every $k$-coloring with $N\ge A^k$
   had a color-omitting prefix $d[1,m]$ with $m\ge\delta N$, for fixed
   $\delta>0$. Its pullback would give
   $S(k)\le\max(A^k,S(k-1)/\delta)$ and hence an exponential upper bound,
   with a harmless prefactor and the shift from $S$ to $f$. The refuted
   claim [[theory/ramsey_theory/L260_dilated_prefix_color_omission/_index|L260]]
   shows that this fails for every $\delta\in(0,1)$ and $1\le A<L$, where
   $L=\liminf S(n)^{1/n}$, even for arbitrarily large $k$. A block
   composition of a small-depth random Bohr coloring with a near-extremal
   coloring makes every sufficiently long dilated prefix see every color.
   The proof covers all such constants; its retained finite instance is
   illustrative. It leaves the extremal case $N=S(k)$ undecided.
2. **Hereditary thinning of difference domains.** The refuted claim
   [[theory/ramsey_theory/L261_difference_domain_thinning/_index|L261]]
   shows that a fixed positive fraction of an arbitrary vertex set need
   not lose a color from its differences. Differences of powers of four
   encode arbitrary triangle-free edge colorings, and the accepted Ramsey
   growth makes the required retention ratios arbitrarily small.
3. **Uniform avoidance on Bohr cells.** Let a cell be the intersection of
   $[0,N]$ with finitely many conditions $\{\theta_l y\}\in J_l$, with
   arc lengths at most a fixed $\rho$. Asking every sufficiently large
   cell to have a color on its differences avoiding some
   $\{x:\|\theta x\|<\rho\}$ also fails. The refuted claim
   [[theory/ramsey_theory/L266_bohr_cell_uniform_avoidance/_index|L266]]
   cuts a $0/1$ digit cube by a digit-sum-one condition, obtaining exactly
   a set of powers. Ramsey colorings on those powers make every color
   meet every rank-one neighborhood of radius $\rho$. The failure holds
   for every fixed $\rho$, even above $A^{|C(Y)|}$ for every fixed $A$,
   where $C(Y)$ counts the colors on the cell's differences. Requiring
   every arc to have length exactly $\rho$ does not avoid the example.

These are scoped obstructions, not a theorem that every recursion loses
$k$. In particular L266 uses a separate, large palette outside the sparse
difference set. It is consistent with an exponential Schur upper bound.

## Held implications that survive

The [[research/schur_number_growth/bohr_avoidance|Bohr avoidance page]]
explains the following author-recorded proofs:

- If class $i$ avoids a Bohr neighborhood of rank $r_i$ and radius
  $\rho_i$, then $N+1\le\prod_i\lceil1/\rho_i\rceil^{r_i}$.
  The exception form is Lemma 1 of the proof of L262. This is a necessary
  test for any superexponential lower construction.
- A sum-free arc of $\mathbb R/\mathbb Z$ can be dilated by an integer
  to stay at distance at least $1/8$ from zero. Consequently colorings
  whose classes lie in single sum-free Bohr arcs have $N+1\le8^k$:
  [[theory/ramsey_theory/L262_sum_free_arc_colorings/_index|L262]].
- A color-avoiding refinement of a cell keeps at least a $1/q$ fraction,
  $q=\lceil1/\rho\rceil$, and removes a color. Iterating would prove an
  exponential bound. The implication in
  [[theory/ramsey_theory/L265_bohr_cell_avoidance_consequences/_index|L265]]
  is valid, but its universal antecedent is refuted by L266.
- For the positive half $Q_r^+$ of the signed cube
  $\{-1,0,1\}^r\setminus\{0\}$, let $\chi_r$ be the least number of colors
  avoiding monochromatic coordinatewise $v+w=u$. Pullback along binary
  values gives $\chi_r\le H(2^r-1)$. Thus $\chi_r\ge cr$ would imply
  $f(k)\le2^{k/c+1}$:
  [[theory/ramsey_theory/L263_signed_cube_sufficiency/_index|L263]].
  The linear lower bound itself remains the open claim
  [[theory/ramsey_theory/L264_signed_cube_linear_growth/_index|L264]].

The full digit cube and its digit-sum-one slice are distinct domains.
Refuting avoidance on the latter does not refute L264. The
[[research/schur_number_growth/signed_cube_reduction|signed-cube page]]
retains the model's bounds and small values, the implication from sum-free
colorings of $\mathbb F_2^n$, and the precise missing Cayley transfer from
the accepted Ramsey construction.

The cube is also a gate for the other direction. If
$\limsup S(k)^{1/k}=\infty$, then for every $A$ some $k$ has
$S(k)\ge A^k$, and with $r=\lfloor k\log_2A\rfloor$ the pullback gives
$\chi_r\le H(2^r-1)\le k\le(r+1)/\log_2A$. Since
$\chi_{a+b}\le\chi_a+\chi_b$ (subadditivity on the signed-cube page),
$\chi_r/r$ converges to its infimum, which is then $0$. So a
superexponential answer forces $\chi_r=o(r)$: refuting L264 is necessary
for it, and proving L264 suffices for the exponential answer. This short
deduction is author-recorded here.

## The lower-bound interface

A superexponential answer needs Schur colorings of intervals with
unbounded $(N+1)^{1/k}$. Sum-free colorings of
$\mathbb Z_m\setminus\{0\}$ supply Schur
colorings of $[1,m-1]$, and every such family must pass the avoidance
test of the first held implication above: eventually some class meets
every Bohr neighborhood of fixed rank and radius. The bound
$f(k)\le R_k(3)-1$ transfers nothing, and the accepted Ramsey
construction colors arbitrary edges, not differences.
Its mechanism is a palette rule: blocks carry recursive copies with some
colors missing, every edge between two blocks gets a color missing on
exactly one of them, and a color active inside a block also colors edges
leaving it, with labels excluding the triangles this could close.

The [[research/schur_number_growth/invariant_palette_rule|palette-rule page]]
shows that this mechanism fails under symmetric difference colorings. On any
partition of a finite abelian group into cosets, or of the signed cube
into subcubes, a color used inside a block colors no pair leaving it
(in the cube, none whose difference avoids the support of an internal
occurrence). The palettes then satisfy a Kraft inequality,
$\sum_B2^{-t_B}\le1$, where $t_B$ counts the colors not used inside $B$.
A recursion of such layers multiplies the size by at most $2$ per color:
from leaves $\mathbb Z_{m_L}$ it reaches only $m\le m_L2^{k-k_L}$. The
2-adic coloring attains this, at base $2$. On groups of odd order the rule
admits no partition into two or more blocks. This holds for mixed
partitions, whose blocks use different subgroups, so changing the block
architecture does not rescue the transfer in these settings. In groups
the requested reuse of an internal color on a pair leaving its block is
false, not merely unproved. In coordinate subcubes the more limited
four-point obstruction suffices for the same Kraft inequality.

The page also treats intervals, the setting of Schur colorings. For
residue-class partitions of $[0,N]$ with moduli dividing some
$Q\le(N+1)/2$ the inequality holds up to one color per block, the color
of a block's largest difference, so $\sum_B2^{-t_B}\le2$; and a
recursion of such layers from leaves $[1,N_L]$ with $M_L$ colors has
$N+2\le2^{3M-2M_L}(N_L+2)$, so it stays exponential.

The page leaves three lower-bound mechanisms open. First, partitions of
an interval into progressions that are not residue classes. Second, blocks
that are not cosets or subcubes; for twisted blocks of $\{0,1\}^4$ a
retained witness shows that the Kraft inequality really fails in the
signed cube; the retained coloring is a function neither of the support
map nor of the binary value. So the cube is a weaker model than the groups
for this question, and a palette gain there would not by itself give Schur
colorings. Third, two-sided reuse
outside the palette rule: a color used inside both endpoint blocks colors
pairs between them, and its fibres must be independent in its own Cayley
graph on both sides. The simplest instance, coset fibres with affine
labels, is a precise model on the page and is also capped. Proposition 8
uses Brouwer's binary affine-cover theorem to prove
$\dim W_J\le\dim U+k-k_U$ for some seed subspace $U\subseteq W_0$,
where $k_U$ is the number of colors used on $U\setminus\{0\}$. In
particular a zero seed gives $\dim W_J\le k$, however large the label
ranks and the number of stages are. Its deletion step removes $t$ colors
while losing at most $t$ dimensions; restriction preserves the fixed
linear quotient maps. The external cover theorem and this new
specialization are distinguished on the page; the latter is
author-recorded, without independent review. The same bound holds with
stage-dependent kernels if each new layer of a color lies in one
nonzero coset whose direction avoids that color's earlier layers,
condition (A) on the page. Thus changing the kernels under that
avoidance invariant does not supply a gain. On cyclic groups with
coprime factors the model's homomorphisms vanish, so the rule cannot even
cover the nonzero coarse points with zero fine component.

## Provisional premises and remaining gap

No unproved premise is used to claim an unconditional Schur bound. The
conditional implications above retain their antecedents. The target's
missing step is a color-elimination argument with an absolute loss that
uses a quantitative feature of interval colorings absent from the sparse
encodings, or a construction with unbounded exponential base. Every
construction mechanism examined here stays exponential: the known template
compositions have a base fixed by their template, Bohr-arc colorings stay
below $8^k$ (L262), palette recursions stay at base $2$ over their
leaves in groups and exponential on residue-class partitions of
intervals, and the binary fixed-quotient model gains at most $k$
dimensions over its seed. These cover the specified models only.

The lower route has no surviving parameterized construction. To reopen
two-sided reuse, exhibit fibres outside condition (A) satisfying both of
the palette-rule page's exact fibre constraints, including coverage of
every coarse coset, and show a gain over the seed's size per color. A
concrete test uses fibres whose actual differences avoid the earlier
class but whose affine direction spaces do not. Replacing such fibres
by whole cosets would destroy independence. A cyclic-group construction
must handle repeated summands as well;
a binary-space or signed-cube gain still needs a separate interval
transfer. A Bohr-set replacement needs a proof that its label invariant
survives every extension. None of these inputs is supplied. No family
beating base $380^{1/5}$ is known from the tested mechanisms.

On the upper side the open reformulation is the **extremal prefix
assertion**: is there $\delta>0$ such that, for every $k\ge2$, every
Schur-free coloring of $[1,S(k)]$ by at most $k$ colors has a
color-omitting $d[1,m]$ with $m\ge\delta S(k)$?
A proof gives the required constant-loss recursion, since such a prefix
pulls back to a coloring of $[1,m]$ by $k-1$ colors and so
$\delta S(k)\le S(k-1)$. A counterexample would have to be an exactly
extremal coloring, and these are known only for $k\le5$, so finite checks
cannot discriminate. L260's construction
provides no fixed positive lower bound for its length divided by $S(k)$,
so it supplies no counterexample to this assertion. One possible attack
is an extension theorem: show that a coloring without such a prefix
cannot be extremal by extending or reorganizing it onto a longer interval.
No such theorem is held.

A separate surviving test is an adaptive Bohr recursion starting from
$[0,N]$: prove that suitable choices of the frequency and a largest cell
preserve an invariant excluding the sparse powers in L266. Merely giving
the sets the name Bohr cells, or fixing their arc lengths, is insufficient.
The invariant and its preservation are both missing. A proof of L264
would bypass this recursion, but no proof or sublinear cube coloring is
supplied here.
