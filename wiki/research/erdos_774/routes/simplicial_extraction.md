---
name: research/erdos_774/routes/simplicial_extraction
title: Semistable simplex-boundary lattices and uniform extraction
desc: The exact exterior-root relation lattice is semistable by an elementary irreducibility proof, giving uniform full-dissociation extraction for n/k asymptotic to C log n; actual coloring growth remains unproved.
tags: [E0774, simplicial, lattice, extraction, proved, incomplete]
sources: []
created: 2026-09-19T01:23:00Z
updated: 2026-09-19T01:23:00Z
---


# Semistable simplex-boundary lattices and uniform extraction

***

## The finite family and theorem

For $2\leq k<n$, let $E_{n,k}$ consist of the oriented boundary
columns of all $k$-subsets of $[n]$, with coordinates on the
$(k-1)$-subsets. These are distinct nonzero integer vectors.
Fix $0<C<\infty$ and a sequence with

$$
\frac nk\sim C\log n.                              \tag{1}
$$

**Theorem.** These families have one positive hereditary
full-dissociation extraction constant, depending on $C$ and at most
a finite prefix, but not on the stage or subset.

This settles the extraction side of the
[earlier simplicial checks](shift_simplicial_gain_checks.md):
their extraction gap in (1) is resolved. Its arbitrary-color gap is not.
In particular, neither unbounded rational coloring nor avoidance of
only elementary simplex boundaries is substituted for actual coloring.

## 1. The exact integer relation lattice

Give exterior powers of $\mathbb R^n$ the Euclidean metric with
increasing standard wedges $e_I$ orthonormal. Put

$$
u=\sum_{i=1}^n e_i,\qquad W=u^\perp,\qquad
A_{n-1}=W\cap\mathbb Z^n,\qquad N=\binom nk.
$$

The boundary matrix is contraction $\partial=\iota_u$ from
$\bigwedge^k\mathbb Z^n$ to $\bigwedge^{k-1}\mathbb Z^n$.
The vectors $f_i=e_i-e_n$, $i<n$, together with $e_n$, form a
unimodular basis of $\mathbb Z^n$. Thus every integral $k$-vector
has a unique expression $x+e_n\wedge y$, where
$x\in\bigwedge^k A_{n-1}$ and
$y\in\bigwedge^{k-1}A_{n-1}$. Since
$\langle u,f_i\rangle=0$ and $\langle u,e_n\rangle=1$,

$$
\partial(x+e_n\wedge y)=y.
$$

Therefore the relation lattice is, as an equality of embedded lattices,

$$
K_{n,k}=\bigwedge^k A_{n-1},\qquad
m:=\operatorname{rank}K_{n,k}=\binom{n-1}{k},
\quad r:=N-m=\binom{n-1}{k-1}.                    \tag{2}
$$

The Gram matrix of the $f_i$ is $I_{n-1}+J_{n-1}$, with eigenvalues
$n,1,\ldots,1$. The Gram matrix of their $k$-fold wedges is its
$k$-th compound: diagonalize the original Gram matrix and take
exterior powers to see its eigenvalues are all products of $k$
original eigenvalues. Consequently

$$
\det(K_{n,k})^2=n^{\binom{n-2}{k-1}},\qquad
\sigma_{n,k}:=\det(K_{n,k})^{1/m}
             =n^{k/[2(n-1)]}.                    \tag{3}
$$

These determinants are Euclidean covolumes, not indices in an ambient
coordinate lattice.

## 2. Elementary irreducibility

The coordinate permutations of $S_n$ act by signed orthogonal
permutations on $\bigwedge^k\mathbb R^n$. The representation on
$\ker\partial=\bigwedge^k W$ is irreducible, as follows.

Let $B$ commute with every such permutation, with entries in the
standard wedge basis. If $|I\setminus J|\geq2$, transpose two elements
of $I\setminus J$. This fixes $e_J$ and negates $e_I$, forcing
$B_{I,J}=0$. There is one orbit of diagonal ordered pairs and one of
adjacent ordered pairs $|I\setminus J|=1$; their entries are determined
by one scalar each, up to the fixed orientation signs. The commutant
therefore has dimension at most two. It contains the independent
operators $I$ and $\partial^*\partial$; the latter has nonzero
adjacent entries, and $\partial^*$ is wedge multiplication by $u$.
Thus every commuting operator is

$$
aI+b\,\partial^*\partial.                         \tag{4}
$$

If $H\subseteq\ker\partial$ is invariant, its orthogonal projector
on the entire exterior space commutes with the group. By (4), its
restriction to $\ker\partial$ is $aI$. A projection has $a=0$
or $a=1$, so $H$ is zero or the whole kernel.

## 3. Integral irreducible lattices are semistable

Here is the needed general elementary observation. Suppose an integral
Euclidean lattice $L$ has a finite group of orthogonal automorphisms
acting irreducibly on its real span. Then

$$
\det M^{1/\operatorname{rank}M}
\geq\det L^{1/\operatorname{rank}L}
\quad(0\ne M\subseteq L).                         \tag{5}
$$

To prove it, let $\alpha$ be the minimum normalized covolume of its
nonzero sublattices. It is attained: squared covolumes are positive
integers and there are only finitely many possible ranks.
Every minimizer is saturated, since proper saturation lowers covolume.
For saturated $M_1,M_2$,

$$
\det(M_1+M_2)\det(M_1\cap M_2)
\leq\det M_1\det M_2.                             \tag{6}
$$

Extend a basis of the intersection in each lattice and project off its
span. The volume of the combined projected vectors is at most the
product of their separate volumes, proving (6). The intersection is
primitive in both lattices, as required for the basis extensions.

If both lattices minimize normalized covolume, rank additivity and the
defining lower bound $\det M\geq\alpha^{\operatorname{rank}M}$ force
their sum to be another minimizer. The maximal-rank minimizer is
therefore unique and invariant under every lattice automorphism.
Irreducibility makes its real span full; saturation then makes it $L$.
This proves (5).

Apply this argument to the integral lattice in (2), using Section 2.
It follows that $K_{n,k}$ is semistable and that
$K_{n,k}/\sigma_{n,k}$ is stable, for every $2\leq k<n$.

## 4. A fixed theta estimate in the critical range

Along (1), equations (2)--(3) give

$$
\sigma_{n,k}\longrightarrow e^{1/(2C)}>1,\qquad
\frac mN=\frac{n-k}{n}\longrightarrow1.
$$

Fix $1<\sigma_0<e^{1/(2C)}$. Choose $T$ in the
[weak stable-lattice theorem](../lemmas/stable_lattice_free_energy.md)
with $\epsilon(T)\leq\frac12\log\sigma_0$, and put
$s=1/(\sigma_0T)<1$. Eventually $\sigma_{n,k}\geq\sigma_0$, so the
theorem and monotonicity give

$$
\theta_{K_{n,k}}(s)\leq T^m e^{\epsilon(T)m}.
$$

Consequently

$$
\log s+\frac1N\log\theta_{K_{n,k}}(s)
\leq\frac rN\log s-\frac mN(\log\sigma_0-\epsilon(T))
\leq-\tfrac14\log\sigma_0<0                       \tag{7}
$$

once $m/N\geq1/2$.
The [finite phase-entropy criterion](moment_phase_entropy.md) supplies
a fully dissociated subfamily of at least $\delta N$ columns for one
positive constant.

The $S_n$-action is transitive on column indices and carries columns
to columns up to signs, through an ambient signed coordinate
permutation. These operations preserve all ternary relation supports.
Averaging intersections of a dissociated index set with its translates
therefore gives the same $\delta$ for every subset. This proves the
theorem; a finite prefix is absorbed by its positive singleton fractions.

## 5. Scope and continuation

For one explicit sequence, take
$k=\lfloor n/(C\log n)\rfloor$ for sufficiently large $n$.
The rational partition number is $\lceil n/k\rceil$, which grows.
That fact alone says nothing sufficient about the actual partition
number. The earlier entropy bound gives only
$\limsup\alpha(E_{n,k})/N\leq1/(2C\log2)$, a fixed-density restriction,
not divergence of $\chi_1$.

Letting $C$ grow without bound to force a larger entropy lower bound
on colors would make that extraction upper bound tend to zero. Such a
change cannot supply the required uniform family.

The lattice identity, determinant, irreducibility, and semistability
proofs are elementary and author-recorded; a separate reviewer derived
them independently. No computation or external representation theorem was
used. The still-open task is a color-adaptive flat cycle under every
fixed finite palette at one fixed $C$.

A second separate reviewer checked the exact embedded kernel, compound
determinant, commutant, saturation argument, and signed transitivity,
finding no gap. No verification record is filed, so the result remains
author-recorded.
