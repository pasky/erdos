---
name: research/erdos_774/lemmas/full_relation_rank
title: Full relation rank is compatible with two dissociated colors
desc: An explicit saturated signed-relation lattice disproves a uniform span-dimension gap for proportionately dissociated integer sets.
tags: [E0774, proved, obstruction]
sources: []
created: 2026-09-17T23:53:25Z
updated: 2026-09-17T23:53:25Z
---


# Full relation rank is compatible with two dissociated colors

***

## Example — proved

For $n\geq4$, put

$$
a_1=1,\quad a_2=2,\quad a_3=3,\quad a_4=4,\qquad
a_i=a_{i-1}+a_{i-2}\quad(i\geq5).
$$

The distinct positive integers $A_n=\{a_1,\ldots,a_n\}$ have a
dissociated partition into their two index parities. Indeed, successive terms
of either parity have ratio at least two. A finite positive sequence with
successive ratio at least two is superincreasing: all preceding terms sum to
strictly less than its last term. Such a sequence is dissociated, by considering
the largest participating term in a signed relation. Thus every subset of
$A_n$ contains a dissociated half. The relation $1+2=3$ shows that
$\chi(A_n)=2$.

Nevertheless its signed relations generate the full saturated lattice

$$
L_n=\{z\in\mathbb Z^n:\sum_i a_iz_i=0\}.
$$

To see this, use the following $n-1$ signed relations:

$$
\begin{aligned}
r_1&=e_1+e_2-e_3,\\
r_2&=e_1+e_3-e_4,\\
r_3&=e_1-e_2-e_3+e_4,\\
r_i&=e_{i-2}+e_{i-1}-e_i\quad(5\leq i\leq n).
\end{aligned}
$$

Their matrix restricted to columns $2,\ldots,n$ has determinant $\pm1$.
The initial $3\times3$ block is
$\bigl(\begin{smallmatrix}1&-1&0\\0&1&-1\\-1&-1&1\end{smallmatrix}\bigr)$,
of determinant $-1$; the remaining block is triangular with diagonal
entries $-1$. Projection of $L_n$ to columns $2,\ldots,n$ is an
integer isomorphism, because $a_1=1$. Hence these rows generate $L_n$.
They also have rank $n-1$ after reduction over **every** field.

## Scope of the obstruction

Lewko's Theorem 4.3 (checked in the full reading copy, Section 4) colors
relation supports from a uniform local span-dimension gap. This example proves
that proportional dissociation over the integers does not itself provide that
gap, even if one saturates the relation lattice or chooses the reduction prime
adaptively. It does not contradict Lewko's bounded-torsion result.

There is also a coefficient-independent version. Keep only the supports of
$r_1,r_2,r_5,\ldots,r_n$. Assign any nonzero coefficients to those exact
supports over any field. The resulting rows have rank $n-2$, by their
triangular restriction to columns $3,\ldots,n$. Thus arbitrary
support-preserving changes of the field coefficients do not recover a uniform
dimension gap either.

The valid positive special case is different: if every rational dependence
support contains a signed dependence, dissociation equals rational linear
independence, and Rado–Horn applies directly. The example shows that a saturated
signed generating lattice does **not** imply that special case.
