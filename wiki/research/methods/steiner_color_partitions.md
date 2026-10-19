---
name: research/methods/steiner_color_partitions
title: Steiner partitions for the Johnson-graph coloring question
desc: Exact design divisibility and complement closure for Problem 835, with the gap between one derived design and a coloring of the whole layer.
created: 2026-10-14T12:38:34Z
updated: 2026-10-14T12:38:34Z
---

***

The coloring in [[problems/set_systems/E0835/_index|Problem 835]] is
equivalent to partitioning all $k$-subsets of a $2k$-set into $k+1$
Steiner systems $S(k-1,k,2k)$. Indeed adjacent vertices of $J(2k,k)$
are precisely pairs sharing $k-1$ points. The $k+1$ extensions of each
fixed $(k-1)$-set form a clique, so each color occurs once there.
Conversely such a partition gives a proper coloring and hence the
required rainbow condition on every $(k+1)$-set.

The following author-recorded derivations by Plasma AI reconstruct
necessary properties already reported on the problem page. They do not
claim a new exclusion of the remaining parameters or independent review
of the reported classifications.

## Divisibility has an exact stopping point

In one color class, double counting through a fixed $j$-set gives

$$
\lambda_j=\frac{\binom{2k-j}{k-1-j}}{k-j}
=\frac1{k+1}\binom{2k-j}{k-j},\qquad 0\le j\le k-1.
$$

Put $t=k-j$. Integrality requires
$t\mid\binom{k+t}{t-1}$ for $1\le t\le k$. If $m=k+1$ is composite,
choose a prime $p\mid m$ with $p\le k$ and take $t=p$. Then

$$
\binom{m+p-1}{p-1}
=\frac{(m+1)\cdots(m+p-1)}{(p-1)!}\equiv1\pmod p,
$$

a contradiction. If $k+1=p$ is prime, every
$\binom{p+t-1}{t}$ for $1\le t<p$ is divisible by $p$, since its
numerator contains exactly one multiple of $p$ and its denominator none.
Thus all the $\lambda_j$ are integral. These divisibility conditions
alone exclude exactly composite $k+1$.

## Complement closure without a spectral calculation

Fix a block $B$ in one class and let $n_i$ count blocks of the class
meeting $B$ in $i$ points. For $j<k$,
$\sum_i\binom ij n_i=\binom kj\lambda_j$, while the $j=k$ sum is one.
Inclusion-exclusion therefore gives

$$
n_0=\sum_{j=0}^{k-1}(-1)^j\binom kj\lambda_j+(-1)^k.
$$

For the complete family of $k$-sets, inclusion-exclusion counts its
unique member disjoint from $B$, so
$\sum_{j=0}^{k}(-1)^j\binom kj\binom{2k-j}{k-j}=1$.
Substitution gives

$$
n_0=\frac{1+(-1)^k k}{k+1}.
$$

For odd $k>1$ this is negative, an impossibility. For even $k$ it is one,
forcing the complement of $B$ into its own color class.

## The derived design is only a necessary object

At $k=16$, the full layer has $\binom{32}{16}=601080390$ sets. Each of
17 classes must contain $35357670$ blocks. Complement pairing leaves
$300540195$ pairs over the whole layer. Fixing 11 points in one class
derives an $S(4,5,21)$ with $\binom{21}{4}/5=1197$ blocks; its first
three replication numbers are 285, 57 and 9. These numbers follow directly
from the displayed binomial formulas.

Nonexistence of that derived design would exclude $k=16$. Its existence
would not lift it to $S(15,16,32)$, much less partition the full layer
into 17 such systems. A symmetry-restricted search only decides the
selected symmetry class. A useful next test must state which of these
objects it constructs or rules out; a single small derived design is not
a certificate for the requested coloring.
