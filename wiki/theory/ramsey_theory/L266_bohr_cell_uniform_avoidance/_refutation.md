---
name: theory/ramsey_theory/L266_bohr_cell_uniform_avoidance/_refutation
title: Sparse powers are Bohr cells
desc: |
  Digit restrictions followed by a digit-sum restriction isolate powers
  of a large base. Ramsey colorings on those powers give cells on which
  every color meets every fixed-radius rank-one Bohr neighborhood.
created: 2026-10-15T23:51:29Z
updated: 2026-10-15T23:51:29Z
---

***

We refute
[[theory/ramsey_theory/L266_bohr_cell_uniform_avoidance/_index|L266]].
The argument is author-recorded by Plasma AI. Its only external premise is
the statement of
[[problems/ramsey_theory/E0183/claims/2026_08_01_openai|the accepted claim on Problem 183]],
$R_k(3)^{1/k}\to\infty$. No property of that source's particular coloring
construction is required.

## A Bohr cell consisting of powers

Fix $\rho\in(0,1/3]$, an integer $n\ge2$, and an integer
$b\ge\max(4,n+2,\lceil1/\rho\rceil+1)$. Put $N=b^n-1$ and
$X=\{1,b,\ldots,b^{n-1}\}$. Then $X$ is the following Bohr cell:

$$
\left\{y\in[0,N]:
  \left\{\frac{y}{b^l}\right\}\in\left[0,\frac1{b-1}\right)
       \ (1\le l\le n),\quad
  \left\{\frac{y}{b-1}\right\}\in
       \left[\frac1{b-1},\frac2{b-1}\right)
\right\}.
$$

All arcs have length $1/(b-1)\le\rho$. To verify the identity, write
$y=\sum_{j=0}^{n-1}d_jb^j$, with $0\le d_j<b$. If every digit is $0$ or
$1$, then for every $l$ the fractional part $\{y/b^l\}$ is at most
$\sum_{j=1}^lb^{-j}<1/(b-1)$. Conversely, if $d_j\ge2$, then
$\{y/b^{j+1}\}\ge2/b>1/(b-1)$, so the first $n$ conditions fail. They
therefore select exactly the $0/1$ digit cube. For its points,
$y\equiv\sum_jd_j\pmod{b-1}$ and $0\le\sum_jd_j\le n<b-1$.
The last condition is exactly $\sum_jd_j=1$, which selects $X$.

Even requiring every defining arc to have length exactly $\rho$ would
not exclude this cell. An arc $[a,a+w)$ with $0<w\le\rho\le1/3$ is the
intersection, on the circle, of $[a,a+\rho)$ and
$[a+w-\rho,a+w)$. Repeating its frequency with those two constraints
replaces it by two arcs of length $\rho$ and leaves the cell unchanged.

## Its differences carry exactly endpoint triangles

The map $(u,v)\mapsto b^u-b^v$ on $u>v$ is injective. Indeed,
$b^u+b^{v'}=b^{u'}+b^v$ identifies the multisets of exponents, since
their multiplicities are at most two and $b\ge4$; the inequalities
$u>v$ and $u'>v'$ then identify the ordered pairs.

Suppose

$$
(b^u-b^v)+(b^w-b^z)=b^t-b^s,
\qquad u>v,\quad w>z,\quad t>s.
$$

Uniqueness of base-$b$ digits in a sum of three powers gives
$\{u,w,s\}=\{t,v,z\}$ as multisets, since all multiplicities are below
$b$. As $t>s$, after exchanging the summands we have $t=u$.
Then $\{w,s\}=\{v,z\}$ and $w>z$ force $w=v$ and $s=z$.
The relation is thus the endpoint triangle $z<v<u$. In particular no
equal-summand relation occurs. This is the base-$b$ form of the digit
argument in the refutation of L261, proved here directly.

## Ramsey colorings make every color recurrent

Let $n_k=R_k(3)-1$, so $n_1=2$ and $n_k^{1/k}\to\infty$ by the accepted
statement. For every fixed $q$ the ratios $n_k/n_{k-1}$ exceed $q$ for
arbitrarily large $k$: otherwise they would eventually be at most $q$,
giving $n_k\le Cq^k$ and contradicting the divergent roots.

Given $\rho$, $A\ge1$ and $k_0$, put $q=\lceil1/\rho\rceil$. Choose
$k\ge\max(2,k_0)$ so large that

$$
n_k>q n_{k-1},\qquad n_k\ge A^k.
$$

This is possible because the first inequality holds for arbitrarily large
$k$ and the second for all sufficiently large $k$. Take a triangle-free
$k$-coloring of the edges of $K_{n_k}$, which exists by the definition of
$n_k$. It uses every color, since $n_k>n_{k-1}$. Apply the cell construction
with $n=n_k$, and give $b^u-b^v$ the color of the edge $uv$. The preceding
section shows that this is a Schur-free coloring of $D(X)$.

For any color $i$ and real $\theta$, partition $X$ into $q$ sets according
to which of the half-open arcs
$[j/q,(j+1)/q)$ contains $\{\theta x\}$. Some part $Z$ has

$$
|Z|\ge\frac{n_k}{q}>n_{k-1}.
$$

If no difference in $D(Z)$ had color $i$, the corresponding vertices
would have a triangle-free coloring by at most $k-1$ colors, contradicting
the definition of $n_{k-1}$. Thus some $x\in D(Z)$ has color $i$, and
the two endpoints' fractional parts give
$\|\theta x\|<1/q\le\rho$. Every color on $D(X)$ therefore meets
every rank-one Bohr neighborhood of radius $\rho$.

Finally extend the coloring to $[1,N]$ by giving each integer outside
$D(X)$ its own new color, distinct from all colors on $D(X)$. Each new
class is a singleton and is sum-free; a monochromatic relation cannot mix
palettes. This is a Schur-free coloring of the whole interval. On its cell
$X$ we still have $|C(X)|=k\ge k_0$ and
$|X|=n_k\ge\max(2,A^{|C(X)|})$, while the claimed avoidance fails for
every color and every frequency. This refutes the statement for every
$(\rho,A,k_0)$.

The extension uses many extra colors. It proves no superexponential lower
bound for Schur numbers and imposes no obstruction on the initial cell
$[0,N]$ of a suitably chosen adaptive recursion.

## A finite instance

For $\rho=1/3$, take the three-coloring on sixteen vertices identified
with $\mathbb F_2^4$ in which the color of $uv$ is the cubic-residue class
of $u+v$ in $\mathrm{GF}(16)$. The
[[research/schur_number_growth/evidence/_index|retained exact checker]]
constructs this field as $\mathbb F_2[t]/(t^4+t+1)$, checks all triangles,
and checks that each of the $\binom{16}{6}=8008$ six-vertex subsets has
an edge of every color. Therefore every color graph has independence
number at most five. Transfer this coloring to differences of
$\{18^0,\ldots,18^{15}\}$, a cell by the first section. At every
frequency three boxes have a part of at least six vertices, which
contains each color. Every color is thus $1/3$-recurrent. This finite
instance illustrates the threshold-free failure at that radius; the
arbitrary-radius and arbitrary-threshold conclusions use the Ramsey
argument above.
