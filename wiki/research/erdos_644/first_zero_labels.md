---
name: research/erdos_644/first_zero_labels
desc: A finite Fano obstruction to first-zero parity labels when two tests have three abundant joint types.
tags: [proved, constructions, method-obstruction]
sources: []
created: 2026-09-22T22:54:42Z
updated: 2026-09-24T22:12:53Z
---


# research/erdos_644/first_zero_labels

***

One attempted counterexample starts with every $k$-subset of an $n$-point core
and appends one new point to each edge. Fix parity tests

$$
h_j(E)=|E\cap X_j|\pmod2.
$$

Append the point $z_j$ corresponding to the first zero test; if no test is zero,
append a private point. The output is $(k+1)$-uniform. The hope was to repair
all bad seven-tuples with only one extra incidence per edge, without creating a
small global cover.

The following checked obstruction rules out a broad, explicitly specified case.
It does not rule out arbitrary nonlinear labels, all linear-test sequences, or
other sparse repairs.

**Proposition.** Suppose $k\ge116$ is even and

$$
n\ge\lceil7k/4\rceil+21.
$$

If three distinct joint point types

$$
(\mathbf1_{X_1}(v),\mathbf1_{X_2}(v))\in\mathbb F_2^2
$$

each occur at least fifty times, the output fails $P_7$, regardless of the later
tests.

## Equal-size boxes with prescribed XORs

Suppose $7q$ points have labels in $\mathbb F_2^2$, with at least thirteen
occurrences of each of three distinct labels, and $q\ge28$. They can be
partitioned into seven $q$-point boxes with any prescribed box XORs whose total
equals the XOR of all the points.

To see this, reserve seven points of each chosen type in box 7 and one of each
type in each other box, and fill the remaining places arbitrarily. The three
pairwise differences of the chosen types are the three nonzero vectors of
$\mathbb F_2^2$. For each of boxes 1 through 6, one swap with box 7 can
therefore correct any nonzero XOR discrepancy. The unprocessed box still has all
three reserved types; box 7 retains enough of each type after at most six swaps.
Box 7 is correct at the end because total XOR is invariant.

Index boxes by nonzero $p\in\mathbb F_2^3$, and denote their desired XORs by
$s_p\in\mathbb F_2^2$. One can prescribe both their total XOR and the two linear
forms

$$
a\longmapsto\sum_{p:a\cdot p=1}(s_p)_b,
\qquad b=1,2.
$$

For each component $b$, these are four independent linear conditions on seven
bits: the matrix with columns $(1,p)$ has rank four. Indeed, a relation
$c_0+c\cdot p=0$ for every nonzero $p$ first gives $c_i=c_0$ on basis vectors
and then $c_0=0$ on sums of two basis vectors.

## The bad tuple

Write

$$
q=\lfloor(k-1)/4\rfloor,\qquad k=4q+r,
\qquad r\in\{2,4\}.
$$

Among the three abundant types choose $a,b$ with first bits zero and one,
respectively. Give each of seven prospective rows its own $r$ core points: one
of type $a$ and $r-1$ of type $b$. Their joint XOR is the same vector $t=a+b$ in
every row, with $t_1=1$.

At most 21 points of either chosen type have been used. Select $7q$ further core
points containing at least thirteen of each of the three abundant types. This is
possible because

$$
7q+7r\le7k/4+21\le n.
$$

Apply the box lemma, prescribing independent standard row-linear forms
$\ell_1,\ell_2$. For each nonzero $u\in\mathbb F_2^3$, let $E_u$ consist of the
four boxes indexed by $p$ with $u\cdot p=1$, together with that row's $r$
selected private core points. Then $|E_u|=k$ and

$$
h_1(E_u)=1+\ell_1(u),\qquad
h_2(E_u)=t_2+\ell_2(u).
$$


The rows receiving label $z_1$ form the four-point Fano cap $\ell_1(u)=1$. The
three remaining rows form the line $\ell_1(u)=0$. Since $\ell_1,\ell_2$ are
independent, the second test splits this line nontrivially into parts of sizes
one and two. Thus $z_2$ occurs on one or two rows, and every later label occurs
on a subset of the remaining one or two rows. There are at least three label
classes, and no label class contains a Fano line.

Every standard core point has a Fano-cap spectrum; every private core point has
singleton spectrum; unused points have empty spectrum. Two core points cannot
cover the rows. A label combined with a standard point would require its class
to contain the complementary Fano line, which it does not. A label and a
singleton point cover at most five rows. Finally, two labels cannot cover the
three or more nonempty label classes. Hence the seven augmented edges have no
two-point transversal.

## Scope

The assumption concerns the first two tests and three large joint point classes.
It is satisfied by many balanced linear-test proposals, but is not automatic for
arbitrary tests. No construction preserving $P_7$ with a linear excess over
$3k/4$ was obtained by this method.
