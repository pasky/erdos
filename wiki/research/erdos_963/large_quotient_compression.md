---
name: research/erdos_963/large_quotient_compression
title: 'A lower-dimensional compression for large cyclic quotients'
desc: A proved compression theorem and its necessary small-index condition on a minimal-dimension counterexample.
tags: []
sources: []
created: 2026-09-18T23:20:00Z
updated: 2026-09-19T01:37:39Z
---


# A lower-dimensional compression for large cyclic quotients

***

This is a proved reduction, not a resolution of the target. It applies to
any finite positive real set, without a hypothesis on its rational rank.

## The quotient associated with a nearly maximum subset

Let $P\subset\mathbb R_{>0}$ be finite, let $d=d(P)\ge2$, and
choose a dissociated $D\subseteq P$ of size $d-1$. Put

$$
L=\langle P\rangle_{\mathbb Z},\qquad
L_D=\langle D\rangle_{\mathbb Z},\qquad G=L/L_D.
$$

If $G\ne0$, it is cyclic, and the nonzero images of the elements of
$P$ comprise a single signed class $\{g,-g\}$.

Indeed, take $h,h'\in P$ with nonzero images. For distinct $h,h'$,
the $d+1$ elements of $D\cup\{h,h'\}$ have a ternary relation.
It must use both $h,h'$: a relation using neither contradicts
dissociation of $D$, and a relation using just one cannot vanish in
$G$. Thus their images are equal or opposite. These images generate
$G$, proving the assertion. The case of only one nonzero image is
immediate.

## Compression theorem

Suppose $G$ is infinite or has order $q>d+1$. Then there is a finite
positive real set $C$ such that

$$
d(C)\le d-1,\qquad |C|\ge\frac{|P|-1}{2}. \tag{1}
$$

The compressed set need not be a subset of $P$.

Let $Q=P\cap L_D$. Change individual signs of the elements of
$P\setminus Q$ so that their images are all $g$, and call the
resulting set $H$. These sign changes preserve dissociation and do not
identify elements: the original set was positive. Also $H\cap Q$
is empty, since their quotient images differ. Let $h_0=\min H$ in
the real order, and put

$$
\Delta=\{h-h_0:h\in H\setminus\{h_0\}\},\qquad C=Q\cup\Delta.
$$

All elements of $C$ are positive, and

$$
|C|\ge\max\{|Q|,|H|-1\}\ge\frac{|P|-1}{2}.
$$


Suppose, to obtain a contradiction, that $B\subseteq C$ is a
dissociated $d$-set. For every element of $B\cap Q$, use its
original representative in $Q$. For an element $b\in B\setminus Q$,
use $h_0+b\in H$. Thus elements in $Q\cap\Delta$ are assigned
to $Q$. These $d$ representatives are distinct, and none equals
$h_0$. Adjoin $h_0$.

A ternary relation on these $d+1$ points projects to $s g=0$, where
$s$ is the sum of the coefficients on the points of $H$, including
$h_0$. Since $|s|\le d+1$, the order hypothesis forces $s=0$.
Subtracting the resulting zero multiple of $h_0$ turns the original
relation into a ternary relation on $B$. Dissociation of $B$ makes
all its coefficients zero, and then $s=0$ makes the coefficient of
$h_0$ zero. The $d+1$ lifted points are therefore dissociated,
contradicting $d(P)=d$. This proves (1).

## Consequence for a minimal counterexample

Assume the desired positive-set bound has been established in dimensions
at most $d-1$. Applying it to $C$ gives

$$
|P|\le2|C|+1\le2(2^{d-1}-1)+1=2^d-1.
$$

Consequently, in a counterexample of minimum dissociation dimension,
**every** dissociated $(d-1)$-subset $D$ generates either all of
$L$, or a subgroup of cyclic index at most $d+1$.
In particular, every such $D$ must span the full rational span of $P$.

The argument works in the universal rational lift from
[[research/erdos_963/corank_one|the intrinsic-rank note]] as well. Use its real evaluation
$f$ to choose the minimum in $H$, and form the positive real set

$$
f(Q)\cup\{f(h)-f(h_0):h\in H\setminus\{h_0\}\}.
$$

The two sets separately retain cardinalities $|Q|$ and $|H|-1$,
because evaluation is injective on the signed original columns.
Assign points in their intersection to $Q$, as before. Any real
ternary relation on the selected original signed columns is also a
zero relation in the universal lift. Projection therefore gives
$s=0$; evaluating after subtracting $s h_0$ contradicts dissociation
of the selected compressed real set. No claim that evaluation preserves
all relations on arbitrary compressed vectors is needed.

## Exact limitation

If the cyclic quotient has order $q\le d+1$, a relation on the lifted
points can have a nonzero coefficient sum $s\in q\mathbb Z$.
Translation then leaves $s h_0$, rather than a zero multiple of the
pivot. If $L_D=L$, there is no quotient restriction at all. Neither
case is covered by the proof. The primitive and small-index cases are
not excluded by the known rank-defect bounds, and no induction closing
them is proved here.

One stronger sufficient assertion would be that *every* positive $P$
admits a positive set $C$ satisfying (1), without the quotient
hypothesis. This assertion is unproved; it is not an established general
compression principle.

## A sharper restriction for a least-dimensional odd failure

Assume the stronger positive odd bound holds in dimensions below $d$,
and let $O$ be a violating positive odd integer set of dimension $d$.
The established small cases give $d\ge5$. Divide by its (odd) common
gcd, so $\gcd(O)=1$. For every dissociated $(d-1)$-subset $D\subset O$,
put $q=\gcd(D)$. Then

$$
\boxed{q=1\quad\hbox{or}\quad q\le d-1.}                    \tag{2}
$$

Since $q$ is odd, for odd $d$ the upper bound is actually $d-2$.
This improves the general cutoff $d+1$, but does not exclude the
primitive case.

Suppose $q>1$. By the quotient argument above, all nonzero residues
of $O$ modulo $q$ are $\pm g$, where $\gcd(g,q)=1$. Let
$Q=O\cap q\mathbb Z$, and change signs of the other elements to obtain
a set $H$ with constant residue $g$. Put

$$
h_0=\min H,\qquad
\Delta=\{h-h_0:h\in H\setminus\{h_0\}\}.
$$

The set $\Delta$ is positive and even; $H$ itself need not be positive.
Any dissociated subset of $Q$ can be extended by an element of $H$,
so $d(Q)\le d-1$ and $|Q|\le2^{d-2}$. If $d(\Delta)\le d-2$,
the lower-dimensional positive bound (deduced from the assumed odd
bounds by valuation layers) gives

$$
|H|=|\Delta|+1\le2^{d-2},
$$

contradicting $|O|>2^{d-1}$.

Thus choose a dissociated $(d-1)$-subset $B\subset\Delta$, and let
$K=\{h_0\}\cup(h_0+B)\subset H$. For any $a\in Q$, the $d+1$
elements of $K\cup\{a\}$ are dependent. In a ternary relation write
$s$ for the sum of the coefficients on $K$. Reduction modulo $q$
gives $s\in q\mathbb Z$.

If $s=0$, reduction modulo two forces the coefficient of $a$ to be
zero. Subtracting $s h_0$ then gives a relation on $B$, which is
trivial; the coefficient of $h_0$ is zero as well. Consequently
$0<|s|\le d$. This excludes $q>d$.

If $q=d$, then $d$ is odd and $s=\pm d$, so all $K$ coefficients
have the same sign. Parity forces the coefficient of $a$ to be
nonzero, and hence

$$
a=\left|\sum_{h\in K}h\right|.
$$

Only one positive $a$ can satisfy this, whereas $Q$ contains the $d-1$
distinct elements of $D$. This excludes $q=d$ and proves (2).

There is a further boundary restriction. If $d$ is even and $q=d-1$,
then $s=\pm(d-1)$. Among $d$ coefficients from $\{-1,0,1\}$, this
requires exactly one zero and all other coefficients to have the same
sign. Parity again forces the coefficient of $a$ to be nonzero. Thus

$$
Q\subseteq
\left\{\left|\sum_{u\in K}u-h\right|:h\in K\right\},
\qquad d-1\le |Q|\le d.                                    \tag{3}
$$

Neither (2) nor (3) excludes a least-dimensional failure of the strong
odd bound.
