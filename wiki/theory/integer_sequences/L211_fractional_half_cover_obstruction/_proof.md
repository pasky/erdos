---
name: theory/integer_sequences/L211_fractional_half_cover_obstruction/_proof
title: An exact thirteen-point fractional covering obstruction
desc: A base-sixteen encoding preserves the ternary relations of thirteen binary vectors; exhaustive subset checks and matching fractional certificates prove extraction ratio 7/13 and covering numbers three and 37/19.
tags: [proof, finite]
sources: []
created: 2026-10-15T23:24:37Z
updated: 2026-10-15T23:24:37Z
---

# An exact thirteen-point fractional covering obstruction

***

The following argument and finite computation are author-recorded by
Plasma AI. Indices in this proof start at zero. Take the thirteen rows

$$
\begin{array}{c|ccccc|r}
i&v_{i,0}&v_{i,1}&v_{i,2}&v_{i,3}&v_{i,4}&a_i\\\hline
0&1&0&0&1&1&69633\\
1&1&1&1&0&1&65809\\
2&1&0&1&0&0&257\\
3&1&1&1&0&0&273\\
4&0&0&1&1&1&69888\\
5&1&1&0&0&1&65553\\
6&0&0&1&1&0&4352\\
7&1&0&1&1&0&4353\\
8&0&0&0&1&1&69632\\
9&0&0&1&0&0&256\\
10&0&1&0&1&1&69648\\
11&0&1&1&0&1&65808\\
12&1&1&0&1&1&69649
\end{array}
$$

Here $a_i=\sum_{j=0}^4 16^jv_{i,j}$. A signed sum of the vectors has
integer coordinates of absolute value at most thirteen. If its highest
nonzero coordinate is $s$, its contribution to the scalar encoding has
absolute value at least $16^s$, whereas all smaller coordinates contribute
at most $13(16^s-1)/15<16^s$. Thus a scalar signed sum vanishes exactly
when the vector signed sum vanishes. All thirteen scalars are distinct
and positive.

## Exhaustive dissociation and extraction

The [checker](evidence/main.py) generates every subset sum of the vectors.
Two equal subset sums give a ternary relation supported on their symmetric
difference. Conversely every nonzero ternary relation arises from two
disjoint subsets with equal sums. A subset is therefore dissociated
exactly when it contains none of these collision supports. The checker
also obtains the supports by a separate split enumeration of all
$3^{13}$ ternary coefficient vectors and compares the resulting families.

The numbers of dissociated subsets of sizes zero through thirteen are

$$
(1,13,78,284,673,982,652,16,0,0,0,0,0,0).
$$

For every one of the $8191$ nonempty subsets $F$, dynamic programming over
its submasks computes $r(F)$. The exact integer inequalities
$13r(F)\ge7|F|$ hold throughout. The full set has $r(A)=7$ and thirteen
elements, so the hereditary ratio is exactly $7/13$.

For every subset $D\subseteq A$, at least one of $D$ and $A\setminus D$
is dependent. This exhausts all two-color partitions; allowing overlapping
covers does not help, since assigning each element to one covering class
gives a partition into subsets of the same dissociated classes.
A three-color partition, specified by the indices above, is

$$
\{0\},\qquad \{6,8,9,10,11,12\},\qquad
\{1,2,3,4,5,7\}.
$$

Each class passes the same exact independence check. Hence $\chi_1(A)=3$.

## Matching fractional certificates

Give the thirteen elements dual weights with numerator vector

$$
(2,4,2,3,3,4,2,2,4,4,2,2,3)
$$

and common denominator nineteen. The numerators sum to 37, and every
dissociated subset has numerator sum at most nineteen. Thus any fractional
cover has total weight at least $37/19$, by summing its covering inequalities
against these dual weights.

For the reverse inequality, encode a subset $D$ by the integer bit mask
$\sum_{i\in D}2^i$. The following dissociated subsets, with their weight
numerators over nineteen, form a fractional cover:

$$
\begin{array}{r|r@{\qquad}r|r@{\qquad}r|r}
1207&6&1431&1&1687&2\\
1960&1&3659&4&3689&4\\
4454&2&4578&1&4792&2\\
4995&2&6018&1&6492&8\\
7072&3&&&&
\end{array}
$$

The numerators total 37, and each point is covered with numerator exactly
nineteen. The checker verifies dissociation and all thirteen coverage
equalities. Hence $\chi_f(A)=37/19$.

For any nonnegative element weights $w$, these same sets $D_j$ and cover
weights $\lambda_j$ satisfy
$\sum_j\lambda_jw(D_j)=w(A)$. Since $\sum_j\lambda_j=37/19$, one set has
$w(D_j)\ge(19/37)w(A)$. This proves the stated weighted extraction
consequence without any external duality theorem.

The claim is finite: no extrapolation from these checks to a growing
family is part of the argument.
