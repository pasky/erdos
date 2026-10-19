---
name: research/schur_number_growth/signed_cube_reduction
title: Signed cubes as a sufficient condition for exponential Schur growth
desc: A linear lower bound for signed-cube colorings would give exponential Schur growth. The relation to sum-free colorings of finite vector spaces remains useful although uniform Bohr-cell avoidance is refuted by a sparse slice.
created: 2026-10-15T23:02:04Z
updated: 2026-10-17T22:11:11Z
---

# Signed cubes as a sufficient condition for exponential Schur growth

[[research/schur_number_growth/_index|..]]

***

The [[research/schur_number_growth/bohr_avoidance|Bohr-cell recursion]]
refines $[0,N]$ through cells of growing rank. After many steps a Bohr cell
can be a digit cube, and on a digit cube the Schur structure of the
differences is exactly the vector addition of a signed cube. This page
collects what is known about the coloring number of that cube and how it
bears on the route and on the target. The results are author-recorded by
Plasma AI; no independent examination is recorded. Two web searches on
2026-10-15 for Schur-type colorings of $\{-1,0,1\}^n$ under vector
addition found no treatment of $\chi_r$; that search is not exhaustive.

## The signed cube

Let $Q_r=\{-1,0,1\}^r\setminus\{0\}$, and let $Q_r^+$ be the set of
$v\in Q_r$ whose last nonzero coordinate is $1$, so that
$Q_r=Q_r^+\cup(-Q_r^+)$. A triple of $Q_r^+$ is $(v,w,u)$ with
$v,w,u\in Q_r^+$ and $v+w=u$ coordinatewise; $v=w$ never occurs, since
$2v\notin Q_r$. Let $\chi_r$ be the least number of colors in a coloring of
$Q_r^+$ with no monochromatic triple.

Equivalently, $\chi_r$ is the least number of colors in a triangle-free
coloring of the edges of the complete graph on $\{0,1\}^r$ in which the
color of $\{x,y\}$ depends only on $\pm(y-x)$. Given a coloring of
$Q_r^+$, color $\{x,y\}$ by the positive representative of $y-x$; a
triangle $x,y,z$ gives $(y-x)+(z-y)=z-x$, and moving negative terms across
turns it into a triple of positive representatives, since a sum of two
vectors of $Q_r^+$ that lies in $Q_r$ lies in $Q_r^+$. Conversely every
triple $(v,w,u)$ is a triangle: no coordinate has $(v_c,w_c)=\pm(1,1)$, so
coordinatewise one can choose $x_c,y_c,z_c\in\{0,1\}$ with $y-x=w$ and
$z-y=v$.

For $b\ge4$ the base-$b$ value $\iota_b(v)=\sum_iv_ib^{i-1}$ is injective,
positive exactly on $Q_r^+$, and carries triples exactly to the solutions
of $x+y=z$ among its values; for $b=q+1$ with $q\ge3$, the $0/1$ digit
cube in base $b$ is the Bohr cell $\{y:\{y/b^l\}\in[0,1/q)$ for
$l\le r\}$, and its positive differences are $\iota_b(Q_r^+)$. These facts
are Lemma 2 of the
[[theory/ramsey_theory/L265_bohr_cell_avoidance_consequences/_proof|proof of L265]].

## Two implications

- A linear lower bound for $\chi_r$ would settle the target:
  [[theory/ramsey_theory/L263_signed_cube_sufficiency/_index|L263]] shows
  that $\chi_r\ge cr$ for every $r$ gives $f(k)\le2^{k/c+1}$, by pulling
  Schur colorings of $[1,2^r-1]$ back along the binary value. That linear
  bound is the open claim
  [[theory/ramsey_theory/L264_signed_cube_linear_growth/_index|L264]].
- The Bohr-cell hypothesis $(B_\rho)$ would force it: if every Schur-free
  coloring satisfies $(B_\rho)$ with $\rho\le1/3$, then
  $\chi_r\ge r\log2/\log\lceil1/\rho\rceil$, by part (2) of
  [[theory/ramsey_theory/L265_bohr_cell_avoidance_consequences/_index|L265]],
  which plants a cube coloring on the digit cube; the threshold form of the
  hypothesis would force a linear bound as well. The universal hypothesis
  is refuted in L266; its failure does not refute the signed-cube bound.

Whether the exponential bound implies $\chi_r\ge cr$ is unresolved here. A Schur
coloring of an interval pulls back to the cube; this gives no extension
theorem for cube colorings.

## What is known about the coloring number

**Upper bounds.**

1. $\chi_r\le H(2^r-1)$, where $H(n)$ is the least number of colors in a
   coloring of $[1,n]$ with no monochromatic $x+y=z$ ($x=y$ allowed); this
   is the pullback in the proof of L263. Schur's tripling coloring gives
   $\chi_r\le\lceil(r+1)\log2/\log3\rceil$, and
   [[../library/ramsey_theory/ageron_2021_new_lower_bounds_schur_weak_schur/inequality_6|inequality (6) of Ageron et al.]]
   gives $\chi_r\le(5\log2/\log380)\,r+O(1)\approx0.584\,r$.
2. If $\mathbb F_2^r\setminus\{0\}$ is a union of $k$ sum-free sets, then
   $\chi_r\le k$. The support map $\sigma(v)=\{i:v_i\ne0\}\in\mathbb F_2^r$
   is nonzero on $Q_r$ and satisfies $\sigma(v)+\sigma(w)=\sigma(u)$ on every
   triple, since a coordinate where both $v$ and $w$ are nonzero has
   opposite signs there and vanishes in $u$.
3. $\chi_{a+b}\le\chi_a+\chi_b$ and $\chi_r\le\chi_{r+1}$. For the first,
   color $(v',v'')\in Q_{a+b}^+$ by a coloring of $Q_b^+$ at $v''$ when
   $v''\ne0$, and by a coloring of $Q_a^+$ with a disjoint palette at $v'$
   when $v''=0$; a triple with both summands in the first palette and
   $u''\ne0$ is a triple of $Q_b^+$, and one with $u''=0$ changes palette.
   For the second, append a zero coordinate.
4. The coloring by the position of the last nonzero coordinate has no
   monochromatic triple, since two such vectors sum to a $2$ there, so
   $\chi_r\le r$.

**Ramsey lower bound.** The equivalent description gives a triangle-free
$\chi_r$-coloring of $K_{2^r}$, so $2^r<R_{\chi_r}(3)$. With
$R_k(3)\le ek!+1$, the classical bound that
[[../library/ramsey_theory/eliahou_2020_adaptive_upper_bound_ramsey_numbers_r_3_3/_index|Eliahou's card]]
records, this gives $\chi_r\ge(1-o(1))\,r\log2/\log r$. By
[[problems/ramsey_theory/E0183/claims/2026_08_01_openai|the accepted claim on Problem 183]],
$R_k(3)^{1/k}\to\infty$, so no argument through general triangle-free
colorings can give more than $o(r)$: they need only $o(r)$ colors on
$K_{2^r}$, and L264 asks whether invariance under differences forces
$\Omega(r)$.

**Sum-free colorings of $\mathbb F_2^n$.** Let $n_2(k)$ be the largest $n$
such that $\mathbb F_2^n\setminus\{0\}$ is a union of $k$ sum-free sets. By
upper bound 2, $\chi_{n_2(k)}\le k$, so L264 forces $n_2(k)=O(k)$, and so
does $(B_\rho)$ by L265: $n_2(k)\le k\log\lceil1/\rho\rceil/\log2$.
The elementary bounds used here are $n_2(3)=4$, from the three
cubic-residue classes of $\mathrm{GF}(16)$ and $2^5\ge R_3(3)$;
$n_2(k)\ge4\lfloor k/3\rfloor$ by superadditivity; and the Cayley
coloring of $K_{2^n}$ gives
$2^{n_2(k)}<R_k(3)\le ek!+1$, so $n_2(k)=O(k\log k)$. A coloring of
$\mathbb F_2^n\setminus\{0\}$ into sum-free sets is exactly a coloring of
the points of $\mathrm{PG}(n-1,2)$ with no monochromatic line. A.
Bishnoi, W. Cames van Batenburg and A. Ravi, *The chromatic number of
finite projective spaces*,
[arXiv:2512.01760v3](https://arxiv.org/abs/2512.01760v3) (24 May 2026;
abstract only, not held by the library), state that the
least number of colors $\chi_2(n)$ for such a coloring satisfies
$\chi_2(n)\le\lfloor2n/3\rfloor+1$ for $n\ge2$, with equality for
$n\le7$, and $\chi_2(n)\ge(1-o(1))\,n/\log n$. Hence
$n_2(k)\ge\lceil3k/2\rceil-1$, which improves the superadditive bound;
the abstract leaves a linear lower bound for $\chi_2(n)$ open. Z. Hunter
and C. Pohoata, *On off-diagonal Ramsey numbers for vector spaces over*
$\mathbb F_2$, [arXiv:2309.02424v2](https://arxiv.org/abs/2309.02424v2)
(23 December 2024), Section 4 and its footnote 2 on p. 11 (read in the
arXiv PDF text; not held by the library), discuss the same covering
question for the punctured spaces $\mathbb F_p^n\setminus\{0\}$:
$O(n\log p)$ sum-free sets suffice, the Ramsey connection rules out
$o(n/\log n)$, and
$\Omega(n\log p)$ sets are conjectured to be needed, a conjecture they tie to
the growth of the multicolor triangle Ramsey numbers. An exponential bound
$R_k(3)\le C^k$ would have given $n_2(k)\le k\log_2C$; the accepted claim on
Problem 183 rules that bound out, so that argument for the linear
conjecture is unavailable. No linear bound or superlinear lower family
for $n_2$ is established here. Their Theorem 4.1 finds a subspace avoiding
all of
$r$ solution-free sets once $n>C_pr(\log r+d)^7$, a subspace analogue of the
Bohr-cell recursion with a polylogarithmic loss per color.

For the superadditivity used above, color a nonzero vector in a direct
sum by its first block when that block is nonzero, and otherwise by its
second block, using disjoint palettes. A monochromatic sum staying in
one palette would contradict the corresponding block coloring; a sum
whose first block cancels changes palette. Thus color counts add while
dimensions add.

**Small values.** $\chi_1,\ldots,\chi_7=1,2,3,3,4,5,5$.

- Lower bounds: $\chi_2\ge2$, since $(1,0)+(0,1)=(1,1)$ is a triple;
  $\chi_3\ge3$ by exhaustion (also $8\ge R_2(3)=6$); $\chi_5\ge4$ from
  $32\ge R_3(3)=17$; $\chi_6\ge5$ from $64>62\ge R_4(3)$
  ([[../library/ramsey_theory/fettes_kramer_radziszowski_2004_upper_bound_62/theorem_5_6|Fettes, Kramer and Radziszowski]]);
  the others by monotonicity. The values $R_2(3)=6$ and $R_3(3)=17$ are
  the classical ones recorded on
  [[../library/ramsey_theory/eliahou_2020_adaptive_upper_bound_ramsey_numbers_r_3_3/_index|Eliahou's card]].
- Upper bounds: $\chi_3\le3$ by the last-nonzero-coordinate coloring;
  $\chi_4\le3$ from the cubic-residue classes of $\mathrm{GF}(16)$, which
  are sum-free in $\mathbb F_2^4$, through the support map; $\chi_5\le4$
  and $\chi_6\le5$ from the tripling colorings of $[1,40]$ and $[1,121]$
  through the binary value; $\chi_7\le5$ from a Schur-free five-coloring
  of $[1,133]$, the composition (Lemma A of the
  [[theory/ramsey_theory/L260_dilated_prefix_color_omission/_refutation|refutation of L260]])
  of one color on $[1,1]$ with a four-coloring of $[1,44]$, through the
  binary value, since $2^7-1\le133$; Exoo's five-coloring of $[1,160]$
  would serve as well.
- $\chi_8\in\{5,6\}$ is the first value these arguments leave undecided:
  the tripling coloring of
  $[1,364]$ gives 6, while $S(5)=160<255$ and the bound $R_5(3)\le307$
  that Eliahou's card records decide nothing. A five-coloring would give
  $R_5(3)>256$ by the Ramsey lower bound above, far beyond the bound
  $R_5(3)\ge162$ recorded there; in general a cube coloring that beats the
  binary-value pullback improves the lower bound $R_k(3)\ge S(k)+2$.

The [[research/schur_number_growth/evidence/_index|retained evidence]]
checks the base-$b$ facts for $r\le5$, the digit-cube cells for $r\le4$,
the binary-value and support maps for $r\le6$, the exhaustion for
$\chi_3$, and the colorings behind $\chi_4\le3$, $\chi_5\le4$,
$\chi_6\le5$ and $\chi_7\le5$, with the four-coloring of $[1,44]$
retained as an input.

## The hierarchy and its scope

For $N=2^r$, with $R^{-1}(N)$ the least $k$ with $R_k(3)>N$,

$$
R^{-1}(2^r)\le\chi_r\le\min\bigl(H(2^r-1),\ \min\{k:n_2(k)\ge r\}\bigr).
$$

The left end is $o(r)$. The exponential conjecture asserts
$H(2^r-1)\ge cr$. A linear bound for $\chi_r$ would imply both that
conjecture and $n_2(k)=O(k)$. The uniform Bohr-cell hypothesis would
imply the linear bound, but its refutation is logically independent of
whether the linear bound is true.

The refutation in
[[theory/ramsey_theory/L266_bohr_cell_uniform_avoidance/_index|L266]]
uses a digit-sum-one slice of a digit cube, whose differences encode
arbitrary triangle-free edge colorings. Coloring that slice does not
supply a coloring of all of $Q_r^+$. Hence it neither constructs sublinear
$\chi_r$ nor resolves the Schur target. Conversely a sublinear family for
$\chi_r$ would require a further extension theorem to give interval
colorings. A proof of linearity would prove the Schur upper bound by L263.

## The missing Cayley transfer

A coloring of the nonzero elements of a finite abelian group $G$ into
sum-free classes gives a triangle-free edge coloring by differences,
provided opposite elements have the same color. For $G=\mathbb F_2^r$
this symmetry is automatic, and the support map above would transfer the
coloring to $Q_r^+$. Thus an accepted Ramsey lower construction on
$\mathbb F_2^r$ with a difference-only coloring and $k=o(r)$ would refute
L264. The accepted theorem for arbitrary edge colorings does not assert
this additional structure.

The held reconstruction of OpenAI's August 6, 2026 report,
[[../library/ramsey_theory/openai_2026_ten_advances_mathematics_theoretical_computer_science/chapter_9/proposition_3_1|Chapter 9, Proposition 3.1, printed pp. 233–234]],
describes the actual coloring rule. Its vertices are recursive blocks
$V_P$ indexed by a separated family of palettes $P$. Internal copies use
colors outside $P$. For each ordered block pair $P<Q$, the construction
chooses lists in $Q\setminus P$ and $P\setminus Q$. A cross edge's color
is selected by equalities involving separate proper-color labels of its
two endpoints and the fixed maps $f,g$ of Lemma 2.2. The
[[../library/ramsey_theory/openai_2026_ten_advances_mathematics_theoretical_computer_science/chapter_9/lemma_2_3|palette lemma]]
supplies a separated family of subsets, not a group operation on blocks.
The
[[../library/ramsey_theory/openai_2026_ten_advances_mathematics_theoretical_computer_science/chapter_9/theorem_1_1|final theorem]]
uses the product of the block counts to obtain its size bound.

These pages provide no identification of vertices with an abelian group
under which the edge color depends only on the difference. In particular,
the choices depend on the block pair and on the endpoint labels; no
translation-equivariance identity is proved. Even regularity of each
individual color graph, a necessary condition for a Cayley coloring, is
not part of the stated construction properties. This is a missing
transfer, not a proof that no choices or relabeling could produce one.
The reading covers the held mathematical reconstruction of the coloring
rule and palette interface, not a new proof audit of the source report.
No sublinear cube coloring follows from the inspected interface.

The remaining model questions are whether $\chi_r\ge cr$, whether
$n_2(k)=O(k)$, and whether $\chi_8=5$. A family with $n/k\to\infty$ in
$\mathbb F_2^n$ would give $\chi_n/n\to0$ along that family by the support
map; subadditivity would then give $\chi_r=o(r)$ for all $r$. None of
these questions is settled by the sparse-cell obstruction.
