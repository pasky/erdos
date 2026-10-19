---
name: research/erdos_963/maximum_sum_candidate
title: 'A fixed, uncertified candidate against maximum-sum orbit matching'
desc: The eleven-set and its seventeen-color sixteen-orbit neighborhood are certified; maximum dissociation of the ambient set is not.
tags: []
sources: []
created: 2026-09-19T02:15:34Z
updated: 2026-09-19T02:15:34Z
---


# A fixed, uncertified candidate against maximum-sum orbit matching

***

This is **not** a counterexample to Erdős 963. Nor is it yet a
counterexample to the maximum-sum complement-orbit assertion: the
essential maximum-dimension claim below remains unproved.

## The fixed configuration

Let

$$
\begin{aligned}
B&=\{1463,1477,1505,1533,1603,1687\},\\
E&=B\cup\{9233\},\qquad c=35,\\
X&=\{1000000001,1000000017,1000000053,1000000061\},\\
D&=E\cup X,
\end{aligned}
$$

and

$$
C=\{1,9,11,17,19,25,27,35,43,51,59,61,71,79,87,95,131\},
\qquad O=D\cup C.
$$

All entries are positive odd, $|D|=11$, and $|O|=28$.

The construction uses

$$
F=\{9,11,15,19,29,41\},\quad B=7(200+F),\quad
\sum B=9268,\quad9233=\sum B-c.
$$

Dissociation of $F$ was proved in
[[research/erdos_963/minimum_sum_matching|the minimum-sum note]].

## Proved: $D$ is dissociated

A ternary relation on $200+F$ first forces its coefficient sum to be
zero, since $\sum F=124<200$, and then reduces to a relation on $F$.
Thus $B$ is dissociated. A representation of $9233$ on $B$ would give

$$
35=\sum_{b\in B}(1-\varepsilon_b)b,
$$

impossible because every summand is nonnegative and $\min B>35$.
Hence $E$ is dissociated.

Write $X=A+\{0,16,52,60\}$ with $A=1000000001$. In a relation on
$D$, the coefficient sum on $X$ must vanish:

$$
\sum E+0+16+52+60=18629<A.
$$

Every element of $E$ is divisible by seven. The four offsets have
distinct residues modulo seven, and their six pair sums

$$
16,52,60,68,76,112
$$

also have distinct residues modulo seven. A nonzero balanced ternary
combination of four offsets would compare either two singletons or two
disjoint pairs, so cannot vanish modulo seven. Thus all $X$ coefficients
are zero. Dissociation of $E$ eliminates the rest.

## Proved: the seventeen colors occupy exactly sixteen orbits

The relation

$$
c=\sum B-9233                                               \tag{1}
$$

uses every coordinate of $E$. The six offset differences are
$16,52,60,36,44,8$, and their balanced two-versus-two differences,
up to sign, are $96,24,8$. Consequently $C$ consists exactly of the
distinct positive absolute values of

$$
c,\quad c\pm16,\ c\pm52,\ c\pm60,\ c\pm36,\ c\pm44,\ c\pm8,
\quad c\pm96,\ c\pm24.
$$

These give the specified central square, full-support, and
four-dimensional face representations on $D$.

There are no representations with different outside signs. To check
this, let $a\in C$ have any ternary representation on $D$. The
coefficient sum on $X$ is again zero, since $a\le131$ and the
remaining terms are far smaller than $A$. The offset contribution
$\tau$ has $|\tau|\le96$. Thus its $E$ contribution satisfies

$$
|a-\tau|\le227.
$$

It is odd, since $\tau$ is even.

If the coefficient of $9233$ is zero, write the $B$ contribution as
$7(200s+t)$, where $|t|\le124$. Its absolute value at most $227$
forces $s=0$. Since the elements of $F$ are odd, $s=0$ makes $t$
even, so the contribution is even, a contradiction.

If the coefficient of $9233$ is $-1$, the contribution is

$$
35-\sum_{b\in B}(1-\varepsilon_b)b.
$$

Its absolute value at most $227$ forces every $\varepsilon_b=1$,
because $\min B=1463$. Similarly, coefficient $+1$ forces every
$\varepsilon_b=-1$. Thus every representation uses precisely the
outside sign pattern in (1), or its negative.

In the folded cube of $\Sigma(D)$, fixing those outside signs up to
reversal leaves one four-coordinate cube $Q$ of sixteen complement
orbits. Every color in $C$ has its entire neighborhood in $Q$.
The representation (1) of $c$ has all four $X$ coordinates free and
supplies every orbit of $Q$. Therefore

$$
|N(C)|=16<17=|C|.                                          \tag{2}
$$

This is Hall failure for the particular dissociated $D$.

## The unproved claim and precise next task

It is **not proved** that $d(O)=11$. The only dimension experiment
consisted of 1000 seeded greedy trials; the largest set found had size
eleven. That is not an upper bound.

The exact unresolved finite task is to produce either a dissociated
twelve-subset of $O$, or an exact relation-cover certificate for every
twelve-subset. No such certificate was obtained.

If $d(O)=11$, then $D$ is automatically the unique maximum-sum
maximum subset: its entries are the eleven largest elements of $O$.
In that event (2) would refute the maximum-sum orbit-matching route.
If a twelve-subset is found, this candidate is rejected. Neither
outcome would resolve the original cardinality bound by itself.

## Origin of the central configuration

For four variable coordinates $x_1,\ldots,x_4$, set

$$
u=x_1+x_2-x_3-x_4,\quad
v=x_1-x_2+x_3-x_4,\quad
w=x_1-x_2-x_3+x_4.
$$

The central colors are absolute values of

$$
c,\quad c\pm u,\ c\pm v,\ c\pm w,\quad
c\pm (u\pm v)/2,\quad c\pm (u\pm w)/2,\quad c\pm(v\pm w)/2.
$$

After multiplication by two these are an affine image of
$\{0,\pm2e_i,\pm e_i\pm e_j\}$, the $C_3$ root configuration
with its origin. This identity alone supplies no augmentation.

In particular, the six axial forms are not a universal replacement.
Put

$$
B_0=3F,\quad E_0=B_0\cup\{367\},\quad c_0=5.
$$

Then $E_0$ is dissociated and $c_0=\sum B_0-367$ is its unique
ternary representation. Reduction modulo three forces the coefficient
of $367$ to be $-1$, and positivity then forces all other coefficients
to be $+1$. Dissociation follows because a representation of $367$
on $B_0$ would give a nonnegative combination of its elements equal
to $5<\min B_0$.

Nevertheless both $3c_0$ and $6c_0$ remain represented after every
single deletion from $E_0$. For $3c_0$, scale by three the four
robust identities for $5$ in the minimum-sum note. For $6c_0$, use

$$
10=19-9=29-19=41+9-11-29
$$

scaled by three. Each family of supports has empty intersection.
Since the six axial forms sum to $6c_0$, these identities block
that proposed six-form augmentation even after one outside deletion.
Higher-multiple relations need not provide an additional representation
of the center itself.
