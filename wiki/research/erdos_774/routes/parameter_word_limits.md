---
name: research/erdos_774/routes/parameter_word_limits
title: A precise limit of fixed-alphabet root-word focusing
desc: A finite coloring makes every monochromatic parameter-word image rationally independent under any fixed-alphabet coordinatewise encoding into conductor-disjoint odd-root groups.
tags: [E0774, proved, Ramsey, obstruction]
sources: []
created: 2026-09-18T16:44:29Z
updated: 2026-09-18T16:44:29Z
---


# A precise limit of fixed-alphabet root-word focusing

***

## Scope

The source reassessment checked Karagiannis's Theorems 1--3,
Prömel--Voigt's definitions of parameter words and Theorems C.3/C.7, and
Voigt's product canonization Theorems 2--3 in their full reading copies,
after the digests. These are genuine Ramsey structure theorems. They do not
assert that evaluating a variable word at root labels preserves an additive
relation of the alphabet.

The theorem below identifies an exact obstruction to that transfer. It does
not color all signed relations on roots, and does not exclude
[fixed-height adaptive focusing](fixed_height_focusing.md), increasing
alphabets, or non-coordinatewise encodings.

## Theorem

Fix an alphabet $A$ of size $m\geq2$, and a finite set of coordinates
$J$. For each $j$, choose a map
$a\mapsto x_{j,a}\in\mu_{n_j}$, where the odd integers $n_j$
are pairwise coprime. The local maps need not be injective. Evaluate words by
$$
\pi((a_j)_{j\in J})=\prod_{j\in J}x_{j,a_j}.
$$
There is a coloring of $\pi(A^J)$, with a number of colors depending
only on $m$, for which the **set of distinct values** of every
monochromatic parameter-subspace image is rationally independent.

A parameter subspace fixes some coordinates and partitions the others into
nonempty variable blocks; each block takes one common letter, independently
of the other blocks. This is the point-subspace conclusion to which a
word-based relation-forcing argument would have to apply.
The conclusion is uniform in finite word length; it does not assert
independence of a union of subspace images at different lengths or domains.

## Proof

Put $L=m-1$, and let $P_j$ be the equality partition of $A$
induced by the values $x_{j,a}$. For every partition $P$ of $A$
and every class $C\in P$ except one fixed omitted class, record
$$
\#\{j\in J:P_j=P,\ a_j\in C\}\pmod L.
\tag{1}
$$
There are at most
$L^{\sum_P(|P|-1)}$ records, with the one-color interpretation for
$L=1$. These records depend only on the evaluated root: the product of
the conductor groups is direct, so the local root values are determined by
their product, and a local root value determines its equality class.

Let $B$ be one variable block in a monochromatic parameter subspace.
For any nontrivial partition type $P$, choose a recorded class and
letters respectively inside and outside it. Comparing their substitutions
in that block in the corresponding record (1) gives
$$
t_P:=\#\{j\in B:P_j=P\}\equiv0\pmod L.
\tag{2}
$$
Thus a nontrivial type that occurs in the block occurs at least $m-1$
times. For $m=2$ this just says that an occurring type occurs at least
once, as required.

Consider the distinct diagonal outputs $y_a=\prod_{j\in B}x_{j,a}$.
Fix a target output and representatives for its at most $m-1$
competitors. Each competitor is separated from the target by some partition
type. Assign each competitor a different coordinate of a separating type;
(2) supplies enough copies, even if all competitors require the same type.
At an assigned coordinate choose a rational linear functional that kills
the competitor's local root but not the target's. Such a functional exists:
distinct odd-order roots are never rationally proportional. At unused
coordinates choose a rational functional nonzero on the target. Tensoring
the functionals isolates its diagonal output.

Multiplication identifies
$\bigotimes_{j\in B}\mathbb Q(\zeta_{n_j})$ with their compositum:
the usual cyclotomic degree $\varphi(\prod_jn_j)=\prod_j\varphi(n_j)$
equals the tensor dimension, and the multiplication map is surjective.
Hence this is a separating rational functional on the actual root values.
All distinct diagonal outputs are rationally independent.

Different variable blocks use disjoint conductor factors. The products of
their independent output sets remain independent by the same tensor-field
identification. Fixed coordinates multiply the set by one nonzero scalar,
which does not change independence. This proves the theorem.

## Consequence for the live route

Fixed-alphabet coordinatewise word focusing can guarantee a monochromatic
structure whose evaluated values are all independent. It therefore cannot,
without an additional encoding ingredient, transfer an alphabet relation to
the required monochromatic determinant support.

Karagiannis's increasing-alphabet theorem lies outside this obstruction,
but its statement does not bound variable multiplicities or the locations
of the chosen words. In ordinary multiplicative evaluation a variable word
takes the form $c a^r$; repetition can annihilate the finite conductor
of a root alphabet. In conductor-disjoint evaluation the theorem above
exhibits the different problem of becoming independent. A useful repair must
prove a relation-preserving, noncollapsing encoding for the structures the
Ramsey theorem actually returns. No such repair is supplied here.

This finite theorem has no computational input. It is a scoped obstruction,
not a proof or disproof of finite dissociated colorability of the full root
group. The fixed-height premise in the main argument remains unproved.
The finite theorem and its scope received independent internal review.
