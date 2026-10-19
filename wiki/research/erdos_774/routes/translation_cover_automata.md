---
name: research/erdos_774/routes/translation_cover_automata
title: A finite-state actual-color framework for fixed translation covers
desc: For a fixed one-dimensional voltage symbol, full ternary coloring is recognized by finite residual-state machines; infinite proper colorings periodicize, cyclic admissible degrees are ultimately periodic, and a sharp factor-two large-degree bridge holds.
tags: [E0774, covers, coloring, reduction, proved, incomplete]
sources: []
created: 2026-09-19T01:25:00Z
updated: 2026-09-19T01:25:00Z
---


# A finite-state actual-color framework for fixed translation covers

***

These are exact statements about **all** ternary relations, not selected
lift templates. They apply to one fixed integer voltage assignment.
No density-based lower bound or unbounded-color construction follows yet.
No automaton enumeration has been run.

## 1. Symbol and finite residual states

Fix an integer matrix polynomial

$$
A(z)=\sum_{g=0}^G A_gz^g.
$$

For ordinary covers each nonzero entry of the binary base is one
monomial, and the base columns are distinct and nonzero. Infinite
column labels are $V\times\mathbb Z$; cyclic labels at degree $m$
are $V\times\mathbb Z/m\mathbb Z$.
An integer coefficient sequence $f_t$ is a relation exactly when

$$
\sum_{g=0}^G A_g f_{t-g}=0\quad\hbox{at every row time }t. \tag{1}
$$

For ternary $f_t$, just before processing time $t$ store the pending
row contributions $r=(r_0,\ldots,r_{G-1})$. A transition labeled
$f\in\{0,\pm1\}^V$ is allowed when

$$
r_0+A_0f=0,\qquad
r'_k=r_{k+1}+A_{k+1}f\quad(0\leq k<G),\quad r_G=0. \tag{2}
$$

Use the finite state box

$$
S=\prod_{\substack{x\in X\\0\leq k<G}}
([-B_{x,k},B_{x,k}]\cap\mathbb Z),\qquad
B_{x,k}=\sum_{g=k+1}^G\sum_v|A_g(x,v)|,
\quad N=|S|.                                      \tag{3}
$$

Every actual residual belongs to this box. If $G=0$, use a single
state, with transition condition $A_0f=0$. Flag a transition by whether
$f\ne0$.

**Exact correspondences.**

- Finite-support ternary relations are precisely paths from state zero
  back to zero with at least one nonzero flag.
- Cyclic degree-$m$ ternary relations are precisely such nonzero closed
  paths of length $m$, starting at **any** state.

The first statement follows by accumulating pending row sums in (1).
For the second, extend a closed path periodically. Repeated substitution
in (2) forgets the initial state after $G$ steps, so the state is exactly
the contribution of its previous $G$ coefficient vectors. There are no
spurious periodic states, and (1) holds periodically.

## 2. Infinite proper colorings periodicize

Fix a palette of $q$ colors. A letter
$\sigma\in[q]^V$ specifies the colors at one sheet. For color $c$,
allow only transitions with $f_v=0$ if $\sigma_v\ne c$.

Track $U_c\subseteq S$, the endpoints of all nonzero allowed paths
begun at state zero at any earlier time. Its update is

$$
U'_c=\operatorname{Post}_{\sigma,c}(U_c)
\ \cup\ \{\text{endpoints of nonzero allowed transitions from }0\}.
\tag{4}
$$

Reject a word as soon as $0\in U'_c$ for any $c$. Otherwise the
tracked sets avoid zero. Starting from all sets empty, this is a
deterministic safety automaton with at most

$$
K=2^{q(N-1)}                                       \tag{5}
$$

safe states. Its accepted finite words are exactly proper colorings of
the corresponding finite column intervals. A finite relation contained
in the interval must have zero residual immediately after its last
supported column, since later zero coefficients cannot cancel a nonzero
pending row sum.

**Periodicization theorem.** If the infinite configuration has a proper
$q$-coloring, it has one periodic in the sheet coordinate with period
at most $K$.

Indeed its positive half-line is an infinite safe path and contains a
directed cycle of length at most $K$. Repeat that cycle's word from the
empty tuple. Each update (4) is monotone, and the empty tuple is contained
in the cycle's initial tuple, so every repetition is safe. Its bi-infinite
periodic extension is proper: a finite witness anywhere would translate
into the safe positive half-line.

**Finite-obstruction corollary.** If the infinite family has no proper
$q$-coloring, the interval of $K$ sheets is already uncolorable.
Otherwise its $K+1$ visited states would contain a repeat and give the
periodic coloring above. For ordinary covers, this obstruction projects
to every cyclic degree $m\geq K$: column labels stay distinct, and
identifying rows preserves the ternary relation.

## 3. An exact finite decision problem for cyclic degrees

For each letter $\sigma$ and color $c$, form an $N\times N$
transfer matrix. Its entries are subsets of $\{0,1\}$, recording whether
paths with zero-only or nonzero coefficient flag exist. Concatenation
combines flags by logical OR and takes unions over intermediate states.
There are at most

$$
D=4^{qN^2}                                         \tag{6}
$$

possible $q$-tuples of these matrices.
A cyclic word is proper precisely when its product has no diagonal
entry containing flag one, in any color, by the closed-path correspondence.

Thus the proper cyclic coloring words form a regular language.
To track only lengths, let $R_j$ be the set of all transfer tuples
realizable by length-$j$ words. The evolution $R_j\mapsto R_{j+1}$
is deterministic on at most $2^D$ subsets. Hence the set of degrees
admitting a proper $q$-coloring is ultimately periodic, with preperiod
plus period at most $2^D$. If any degree is uncolorable, one is
uncolorable by that bound.

This is finite and exact for the **fixed symbol $A(z)$**. It is not
a practical search bound, and no computation of these state spaces is
claimed. It does not decide a supremum over unbounded voltage assignments.

## 4. Wrapped relations are real, not an automaton artifact

An infinite proper coloring prohibits nonzero zero-to-zero paths.
It need not prohibit nonzero cycles at other residual states.
For example,

$$
A(z)=
\begin{pmatrix}
1&0&0&z\\
1&1&0&0\\
0&1&1&0\\
0&0&1&1
\end{pmatrix},
\qquad \det A(z)=1-z.
$$

This is an ordinary four-cycle incidence symbol with one shifted
incidence. Its infinite cover is an infinite path, so every finite
subfamily is rationally independent. Every cyclic cover is an even
cycle and has a nonzero alternating ternary relation. Thus its infinite
coloring number is one, while every finite cyclic coloring number is two.
Periodicization alone does not remove wrapped relations.

## 5. A sharp factor-two bridge

Let $\chi_\infty$ be the dissociated coloring number of the infinite
ordinary translation cover. It is finite, since coloring by base type
works. For every positive $m\geq2G$,

$$
\chi_1(\widetilde A_m)\leq2\chi_\infty.             \tag{7}
$$

Split the cyclic sheets into two consecutive arcs of lengths
$\lfloor m/2\rfloor,\lceil m/2\rceil$. Each length $L$ is at most
$m-G$, so its columns and their supporting rows, spanning $L+G$
consecutive sheet positions, unroll injectively into the infinite cover.
Use disjoint copies of a $\chi_\infty$-palette on the two arcs.

The finite-obstruction corollary gives the eventual opposite bound:

$$
\boxed{\chi_\infty\leq\chi_1(\widetilde A_m)
                  \leq2\chi_\infty
       \quad\hbox{for all sufficiently large }m.} \tag{8}
$$

The preceding four-cycle attains the factor two.
For a growing family of fixed symbols, unbounded infinite coloring
would therefore give the required unbounded finite cover coloring.
The missing theorem is still a lower bound for $\chi_\infty$ under
an extraction-compatible choice of symbols; rational rank does not
supply it.

The finite-state and cyclic statements are author-recorded; they were
derived by a separate contributor and checked by the author, including
initial/final residuals, the flag semiring, periodic-state consistency,
and interval projection. No experiments or external theorems are used.

A second separate reviewer checked the residual bounds, acceptance
conditions, monotone periodicization, cyclic flags, ultimate periodicity,
and unrolling bound, finding no gap. No search or computation was
performed.
