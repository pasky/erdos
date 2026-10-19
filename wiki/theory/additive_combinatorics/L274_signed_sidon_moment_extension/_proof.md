---
name: theory/additive_combinatorics/L274_signed_sidon_moment_extension/_proof
title: "Proof of signed linear Sidon moment extension"
desc: "Incidence Gram identities and bounded forbidden extensions give full row rank, the exact compatibility subspace, and a signed degree-four completion; a sixteen-support Sidon trade restores the parity square."
created: 2026-10-16T00:29:25Z
updated: 2026-10-16T00:29:25Z
---

***

This is Plasma AI's author-recorded proof of
[[theory/additive_combinatorics/L274_signed_sidon_moment_extension/_index|L274]],
without independent review. It establishes signed linear realizability and
an optional parity-square constraint. Its global Euclidean norm bounds do
not assert spatial localization or positive semidefiniteness.

**Statement.** Let $N\ge55$, let $0\le k\le N$ be an integer, and let $\rho$
be any probability measure on the $k$-subsets of $\{0,\ldots,N-1\}$. There
is a real linear functional $L$ on Boolean-reduced polynomials of degree at
most four such that:

1. $L$ agrees with $\mathbb E_\rho$ in degrees at most two;
2. $L(z_S)=0$ for every non-Sidon support $S$ of size at most four;
3. $L((Z-k)m)=0$ for every monomial $m$ of degree at most three, where
   $Z=\sum_i z_i$.

Strong Sidon includes sums with repeated summands. If $N\ge58$, $L$ can
also be chosen so that, for
$A=\sum_{0\le i<j<N}(-1)^{i+j}z_iz_j$,

$$
L((A-L(A))^2)=\operatorname{Var}_\rho(A).              \tag{1}
$$

Neither the signed moments nor their moment matrix are asserted to be
nonnegative. No bound for the size of an actual Sidon set follows.

## Incidence matrices with forbidden extensions deleted

Let $D_r$ have rows indexed by all $r$-sets of the interval and columns by
all $(r+1)$-sets, with entry $1$ for containment and $0$ otherwise. Direct
intersection counting gives

$$
D_rD_r^{\mathsf T}=(N-2r)I+D_{r-1}^{\mathsf T}D_{r-1}. \tag{2}
$$

The diagonal on the left is $N-r$, whereas that of the second term on the
right is $r$. Off-diagonal entries on either side are one exactly when two
$r$-sets intersect in $r-1$ elements. In particular
$D_rD_r^{\mathsf T}\succeq(N-2r)I$.

Write $\mathcal S_t$ and $\mathcal N_t$ for the strong Sidon and non-Sidon
$t$-sets. Let $B_r$ be the submatrix with rows $\mathcal S_r$ and columns
$\mathcal S_{r+1}$, and $F_r$ the submatrix with the same rows and columns
$\mathcal N_{r+1}$. Restricting (2) to these rows gives

$$
B_rB_r^{\mathsf T}\succeq(N-2r)I-F_rF_r^{\mathsf T}.  \tag{3}
$$

A pair has at most three forbidden third points: the midpoint and the two
extensions to a three-term progression. A Sidon triple has at most twelve
forbidden fourth points. Nine come from adjoining a progression point to one
of its three pairs; three come from $x+a=b+c$, choosing which triple element
is $a$. These exhaust the nontrivial repeated-sum possibilities, because the
triple itself is Sidon. Thus each row of $F_2$ has at most $3$ ones and each
row of $F_3$ has at most $12$ ones. Their columns have at most $3$ and $4$
ones respectively.

For a zero-one matrix with row degrees at most $b$ and column degrees at
most $c$, Cauchy--Schwarz gives
$\|F^{\mathsf T}u\|_2^2\le cb\|u\|_2^2$. Apply this in (3) to obtain

$$
B_2B_2^{\mathsf T}\succeq(N-13)I,\qquad
B_3B_3^{\mathsf T}\succeq(N-54)I.                    \tag{4}
$$

Both are positive definite for $N\ge55$. Hence $B_2$ and $B_3$ have full
row rank and the explicit right inverses

$$
R_r=B_r^{\mathsf T}(B_rB_r^{\mathsf T})^{-1}
\quad(r=2,3)
$$

satisfy $B_rR_r=I$ and
$\|R_2\|_{2\to2}\le(N-13)^{-1/2}$,
$\|R_3\|_{2\to2}\le(N-54)^{-1/2}$. No computation of these large matrices
is needed for the argument.

## Constructing the functional

Put $p_t(T)=\Pr_\rho(T\subseteq X)$ for the inclusion moments of the base
law. Set $g_0=p_0$, $g_1=p_1$ and $g_2=p_2$. On Sidon triples set

$$
g_3=R_2((k-2)p_2),
$$

and put $g_3=0$ on non-Sidon triples. On Sidon four-sets set
$g_4=R_3((k-3)g_3|_{\mathcal S_3})$, and put $g_4=0$ on the other
four-sets. Define $L(z_T)=g_{|T|}(T)$ and extend linearly.

The right-inverse identities say
$\partial g_3=(k-2)g_2$ on every pair and
$\partial g_4=(k-3)g_3$ on every Sidon triple, where
$\partial g_t(T)=\sum_{x\notin T}g_t(T\cup\{x\})$.
For a forbidden triple, the latter margin is zero automatically: no Sidon
four-set contains it. The identities in degrees zero and one already hold
for $p_0,p_1,p_2$. Finally Boolean reduction gives
$L((Z-k)z_T)=\partial g_{t+1}(T)-(k-t)g_t(T)$ for $t=|T|$. This proves
all three asserted linear properties, for every $k$ in the stated range.

## The exact compatibility subspace for fourth moments

The same argument identifies the obstruction to the square inverse used in
the tentative local construction. Define

$$
\mathcal U_4=\left\{f:\mathcal N_4\to\mathbb R:
 \sum_{S\supset T}f(S)=0\text{ for every }T\in\mathcal N_3\right\}.
                                                               \tag{5}
$$

The restriction to $\mathcal N_4$ of any function with zero three-set
margins lies in $\mathcal U_4$, because every four-set containing a
forbidden triple is itself forbidden. Conversely, for $N\ge55$ every
$f\in\mathcal U_4$ has a zero-margin extension to all four-sets: use $f$
on forbidden four-sets and $-R_3F_3f$ on Sidon four-sets. Equation (5)
handles forbidden triples, and $B_3R_3=I$ handles the remaining triples.
Thus (5) is the complete compatibility condition in this range.

For triples, any prescribed $f$ on $\mathcal N_3$ has a zero-two-margin
extension, using $-R_2F_2f$ on Sidon triples. The corrections on the Sidon
supports obey

$$
\|R_2F_2f\|_2\le\frac{3}{\sqrt{N-13}}\|f\|_2,
\qquad
\|R_3F_3f\|_2\le\sqrt{\frac{48}{N-54}}\|f\|_2.      \tag{6}
$$

These give a global alternative to local kernels. A square matrix indexed by
all forbidden four-sets, each of whose columns has zero three-set margins,
is necessarily singular. For each forbidden triple its column entries over
all containing four-sets sum to zero, a nonzero left-null relation. A right
inverse is possible on the compatible space (5), rather than on the whole
space of forbidden four-set data.

## Restoring the parity square

For $N\ge58$ the interval contains the strong Sidon set

$$
H=\{0,1,4,9,16,27,40,57\}.
$$

Its $28$ positive differences, all distinct, are

$$
1,3,4,5,7,8,9,11,12,13,15,16,17,18,23,24,26,27,
30,31,36,39,40,41,48,53,56,57.
$$

Distinct positive differences imply strong Sidonicity: a nontrivial equality
of two sums would repeat a positive difference, including the case of a
three-term progression.

Pair its elements as $(0,1),(4,9),(16,27),(40,57)$, each with an even and
an odd member. Define a signed function $\tau$ on four-sets by taking one
point from each pair and giving the resulting set weight $(-1)^j$ when
$j$ of the chosen points are odd; put zero on every other four-set. Its
$16$ supports are Sidon. Every three-set margin is zero: if a triple
selects one point from each of three pairs, its two extensions in the last
pair cancel, and every other triple has no extension in the support.
Furthermore

$$
\sum_{|S|=4}(-1)^{\sum_{x\in S}x}\tau(S)=16.           \tag{7}
$$

Every summand on these supports is one. The degree-four coefficient of
$A^2$ is $6(-1)^{\sum_{x\in S}x}$, by its three pairings in two orders.
Adding $c\tau$ to $g_4$ therefore changes $L(A^2)$ by $96c$, without
changing any lower moment, Sidon zero or cardinality identity. Choose

$$
c=\frac{\mathbb E_\rho A^2-L(A^2)}{96}.
$$

The resulting functional satisfies (1), since $L(A)=\mathbb E_\rho A$
is already fixed. This uses neither evenness of $N$ nor a special form of
$\rho$.

The trade restores just this square. Its effect on every other matrix
direction must still be assessed before any positive-semidefinite
completion is claimed. Likewise (6) controls Euclidean norms of moment
vectors, not the eigenvalues of the full quadratic moment matrix. The
[[research/sidon_extremal_error/proof_sketch|extremal proof sketch]] keeps
those positivity gaps and the separate all-$N$ lower construction visible.
