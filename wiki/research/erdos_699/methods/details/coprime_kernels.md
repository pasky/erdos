---
name: research/erdos_699/methods/details/coprime_kernels
title: "Erdős 699: effective nonvanishing from two coprime kernel polynomials"
desc: "Two full-degree coprime modular kernel polynomials remove the extra degree in interpolation, at the cost of an effectively bounded finite set of common zeros."
created: 2026-09-22T07:00:00Z
updated: 2026-09-22T19:12:28Z
---

# Erdős 699: effective nonvanishing from two coprime kernel polynomials

[[research/erdos_699/_index|P699 research]] ·
[[research/erdos_699/methods/details/jet_nonvanishing|Uniform jet nonvanishing]]

***

The surjective-jet construction gives polynomials of degree at most
$D+1$ which cannot all vanish when $X+Y$ is outside the grid rows.
For effective finiteness, one can sometimes work in degree $D$ instead.
The following criterion includes an explicit way to bound its exceptional
zeros; it does not assume that a generic pair of polynomials is coprime.

**Lemma.** Let $A$ be an integer matrix expressing a finite collection of
vanishing jets on polynomials of total degree at most $D$. Suppose that
$A$ has full row rank modulo a prime $p$. Suppose its modular kernel
contains polynomials $\overline F,\overline G$ which are coprime in
$\mathbb F_p[X,Y]$, and that at least one has total degree exactly $D$.
Then there are integer kernel polynomials $F,G$, of degree at most $D$,
which are coprime over $\mathbb Q$. Their simultaneous integer zeros have
effectively bounded $X+Y$.

**Proof.** Choose a maximal minor whose determinant is not divisible by
$p$. Solving for its pivot variables gives a right inverse over
$\mathbb Z_{(p)}$. Consequently every modular kernel vector lifts to a
kernel vector over $\mathbb Z_{(p)}$: lift its free coordinates first,
then solve for the pivot coordinates. Clearing denominators not divisible
by $p$ produces integer polynomials reducing to nonzero scalar multiples
of $\overline F,\overline G$.

Suppose the lifts had a nonconstant common rational factor. Gauss's lemma
gives a common primitive integer factor $H$. Its reduction is nonzero.
If its degree dropped modulo $p$, the degree of the reduction of the
full-degree polynomial would also drop: degrees add in both polynomial
rings, while reduction cannot increase the degree of either factor.
This contradicts $\deg\overline F=D\ge\deg F$, after exchanging $F,G$
if needed. Hence $\overline H$ is nonconstant, contradicting modular
coprimality. Thus $F,G$ are coprime over $\mathbb Q$.

Two coprime plane polynomials have only finitely many common affine zeros.
Everything here is explicit integer algebra. For example, compute the
elimination ideal of

$$
F(X,Y),\quad G(X,Y),\quad Z-X-Y.
$$

It contains a nonzero polynomial in $Z$ (or contains $1$ if there are no
common zeros). Its roots have a computable Cauchy bound, bounding $X+Y$
at every simultaneous zero. $\square$

In a binomial application the fixed coordinate and row-line factors are
nonzero on the relevant physical region. Above the finite bound in the
lemma, at least one of $F(j,n-j),G(j,n-j)$ is nonzero. Thus the usual
weighted divisibility argument may use residual degree $D$, saving one
degree relative to the uniform nonvanishing family.

The required finite certificate consists of a full-row-rank check, two
actual modular kernel vectors, their total degrees, and a polynomial gcd
equal to a nonzero constant. Full row rank alone does not prove the
coprimality condition: all degree-$D$ kernel polynomials can still share
a curve. A numerical or genericity assertion about their gcd is not a
substitute for this check.

There is also a direct numerical bound without computing an elimination
polynomial. If $\|F\|_1,\|G\|_1\le C$, substitute $Y=N-X$ and take
the resultant with respect to $X$, using the actual $X$-degrees. It is
nonzero by coprimality, and its coefficient norm is at most

$$
(2D)!\,(2^D C)^{2D}.
$$

Every simultaneous zero consequently satisfies

$$
\boxed{|X+Y|\le1+(2D)!\,(2^D C)^{2D}.}
$$

If both transformed polynomials have $X$-degree zero, their coprimality
already excludes simultaneous zeros. Otherwise the bound follows by
expanding the Sylvester determinant and then applying the Cauchy root
bound to its nonzero integer resultant. A drop in the $X$-degree does
not invalidate the bound; one uses a smaller Sylvester matrix.

For completeness, if the jet matrix has $r$ rows and $s$ columns, its
entries have absolute value at most $H\ge1$, and each basis polynomial
has coefficient norm at most two, the lifting construction above permits

$$
C=2s(s+1)p\,r!\,H^r.
$$

Indeed choose free coordinates in $\{0,\ldots,p-1\}$, multiply them by
the pivot determinant, and obtain the pivot coordinates with its
adjugate. Expanding determinants gives this conservative bound.
Thus explicit matrix data already suffice for a numerical common-zero
bound. Evaluating it is separate from excluding any bad triples below it.
