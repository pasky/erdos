---
name: research/erdos_963/reflection_obstruction
title: A counterexample to reflection augmentation
desc: A nine-point positive set refutes the proposed reflection-augmentation lemma; this is not a counterexample to the target bound.
tags: []
sources: []
created: 2026-09-18T00:00:00Z
updated: 2026-09-18T22:17:33Z
---


# A counterexample to reflection augmentation

***

The following proposed lemma is **false**: if a dissociated set
$D\subset(0,M/2)$ has size $d$, then
$\{M\}\cup D\cup(M-D)$ contains a dissociated $(d+1)$-subset.

Take

$$
D=\{2,4,10,11\},\qquad M=23.
$$

The 16 subset sums of $D$ are

$$
0,2,4,6,10,11,12,13,14,15,16,17,21,23,25,27,
$$

so $D$ is dissociated, and $D\subset(0,23/2)$. Nevertheless,

$$
P=\{2,4,10,11,12,13,19,21,23\}
$$

has dissociation dimension four. A conceptual finite certificate that every
five-subset is dependent follows.

## The underlying configuration

Write the points symbolically as

$$
\begin{array}{c|ccccccccc}
\text{label}&A&B&C&D&E&F&G&H&M\\ \hline
\text{value}&a&2a&b&c&a+b&a+c&b+c-a&b+c&a+b+c.
\end{array}
$$

The counterexample uses $(a,b,c)=(2,10,11)$. The argument below uses
only these symbolic identities; it proves the same dependence conclusion
whenever the nine displayed points are distinct.

There are four complementary pairs

$$
\{A,H\},\quad\{B,G\},\quad\{C,F\},\quad\{D,E\},
\tag{1}
$$

each summing to $M$. We shall also use

$$
\begin{array}{lll}
A+E=B+C,& A+F=B+D,& A+G=C+D,\\
B+H=E+F,& C+H=E+G,& D+H=F+G.
\end{array}
\tag{2}
$$

Reflection $x\mapsto M-x$ exchanges the members of every pair in
(1) and preserves equalities between two-element sums.

## Five-subsets containing $M$

A five-subset containing $M$ is dependent if it contains either
complete pair in (1). Otherwise it contains exactly one element of each
pair. Let $r_A,r_B,r_C,r_D\in\{0,1\}$ indicate whether the chosen
member is the reflected member, and let $x_A,x_B,x_C,x_D$ be the
chosen values. Since $M=A+C+D$, substitution gives

$$
(1-r_A-r_C-r_D)M
=(-1)^{r_A}x_A+(-1)^{r_C}x_C+(-1)^{r_D}x_D.
\tag{3}
$$

Unless $r_A=r_C=r_D=1$, every coefficient in (3) belongs to
$\{-1,0,1\}$, providing a nontrivial ternary relation.

In the remaining case the chosen set contains $H,F,E$. If its fourth
non-$M$ member is $B$, use $B+H=E+F$. If that member is
$G$, use $M+H=E+F+G$. Thus every five-subset containing
$M$ is dependent.

## Five-subsets not containing $M$

Such a set contains a complete pair in (1). If it contains two complete
pairs, their equal sums give a dependence. Otherwise it consists of one
complete pair and one member of each of the other three pairs.

If its two-element sums are all distinct, (2) restricts the remaining
three members as in the following table. The last column supplies a
dependence in every surviving case.

| Complete pair | Remaining three members | Relation |
|---|---|---|
| $A,H$ | $B,C,D$ | $C+D=H$ |
| $A,H$ | $G,E,F$ | $A+G=H$ |
| $B,G$ | $A,E,F$ | $A+B+G=E+F$ |
| $B,G$ | $H,C,D$ | $C+D=H$ |
| $C,F$ | $A,G,E$ | $A+C=E$ |
| $C,F$ | $H,B,D$ | $C+D=H$ |
| $D,E$ | $A,G,F$ | $A+D=F$ |
| $D,E$ | $H,B,C$ | $C+D=H$ |

For completeness, the restrictions in the table can be checked without
enumerating all five-subsets. If $A,H$ are present and $B$ is
chosen, the other two choices $(C,E),(F,D),(F,E)$ are excluded by
the first, second, and fourth identities in (2), leaving $C,D$.
Reflection handles the choice $G$. If $B,G$ are present and
$A$ is chosen, the choices $(C,D),(C,E),(F,D)$ are excluded
by the third, first, and second identities, leaving $F,E$;
reflection handles $H$.

If $C,F$ are present and $A$ is chosen, choosing $B$
is impossible: either choice from $\{D,E\}$ triggers one of the
first two identities. Hence $G$ is chosen; the third identity then
excludes $D$, leaving $E$. Reflection handles $H$.
Interchanging $b,c$ gives the final two rows.

This covers every five-subset of $P$. Hence $d(P)=4$, and the
reflection-augmentation lemma fails. Since $|P|=9<2^4$, this
example does **not** contradict the original extremal target.
