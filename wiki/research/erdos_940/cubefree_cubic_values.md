---
name: research/erdos_940/cubefree_cubic_values
title: Cube-free outputs and cubic multiplicity
desc: Positive input density of cube-free outputs, a bounded logarithmic cube-part moment, and primitive collisions that survive this restriction.
tags: []
sources: []
created: 2026-09-22T04:00:00Z
updated: 2026-09-22T04:00:00Z
---


# Cube-free outputs and cubic multiplicity

***

## Status

The elementary statements below are proved and author-recorded. They concern
$F(x,y,z)=x^3+2y^3+4z^3$. A positive proportion of **input triples** have
cube-free output; this is not a positive-density theorem for distinct outputs.
The remaining issue is still [multiplicity](energy_and_multiplicity.md).

## A cube-free sieve at the critical scale

**Theorem.** Put

$$
\rho_p=p^{-9}\#\{\mathbf u\bmod p^3:F(\mathbf u)\equiv0\pmod{p^3}\}.
$$

Then

$$
\#\{\mathbf x\in[1,N]^3\cap\mathbb Z^3:F(\mathbf x)\text{ is cube-free}\}
=\delta_F N^3+o(N^3),\qquad
\delta_F=\prod_p(1-\rho_p)>0.
\tag{1}
$$

Every triple counted in (1) is primitive.

For $p\ge5$, first count the triples with all coordinates divisible by $p$:
there are at most $(N/p)^3$. Otherwise choose a unit coordinate. Its
coefficient and the derivative of its cube term are units modulo $p$. For
fixed other coordinates there are at most three possible unit residues modulo
$p^3$, each lifting uniquely from a root modulo $p$. Union over the three
possible choices of coordinate gives

$$
B_p(N):=\#\{\mathbf x\in[1,N]^3:p^3\mid F(\mathbf x)\}
\le 10N^3p^{-3}+9N^2.
\tag{2}
$$

Since $0<F(\mathbf x)\le7N^3$, only primes $p\le7^{1/3}N$ occur.
The elementary bound $\pi(t)\ll t/\log t$ consequently gives, for $P\ge3$,

$$
\#\{\mathbf x:\exists p>P,\ p^3\mid F(\mathbf x)\}
\ll N^3P^{-2}+\frac{N^3}{\log N}.
\tag{3}
$$

The same unit-coordinate argument in a complete residue box gives
$\rho_p\le10p^{-3}$ for $p\ge5$. Every factor $1-\rho_p$ is positive,
because $F(1,0,0)=1$. Thus the product in (1) converges to a positive number.

For fixed $P$, CRT and elementary box counting give

$$
\#\{\mathbf x\in[1,N]^3:p^3\nmid F(\mathbf x)\ (p\le P)\}
=N^3\prod_{p\le P}(1-\rho_p)+O_P(N^2).
$$

Use (3), let $N\to\infty$, and then let $P\to\infty$. This proves (1).
If a prime divided all coordinates, its cube would divide the output, proving
primitivity. At $p=2$, more explicitly, $8\mid F(\mathbf x)$ if and only if
all three coordinates are even: the valuations of the nonzero terms are distinct
modulo three. Hence $\rho_2=1/8$.

## Bounded average logarithm of the cube part

For a positive integer $n$, define

$$
D(n)=\prod_p p^{\lfloor v_p(n)/3\rfloor}.
$$

Thus $D(n)^3$ is the largest perfect cube dividing $n$.

**Theorem.** Uniformly for $N\ge2$,

$$
\sum_{\mathbf x\in[1,N]^3}\log D(F(\mathbf x))\ll N^3.
\tag{4}
$$


First restrict to primitive triples. At every prime, at least one coordinate is
a unit. For $p\ge5$, the corresponding one-variable congruence modulo $p^k$
has at most three unit roots. This remains true at $p=3$, since cubing on
$(\mathbb Z/3^k\mathbb Z)^\times$ has kernel of order at most three. The
coefficients of $F$ are units there. At $p=2$, a primitive triple has
$v_2(F(\mathbf x))\le2$, by the distinct-valuation argument above, so it
contributes no cube factor. Consequently for every odd prime and $k\ge1$,

$$
\#\{\mathbf x\in[1,N]^3:\gcd(\mathbf x)=1,\ p^k\mid F(\mathbf x)\}
\ll N^3p^{-k}+N^2.
\tag{5}
$$

The absolute constant in (5) does not depend on $p,k,N$.

Write $C=7^{1/3}$ and
$J_p=\lfloor\log(7N^3)/(3\log p)\rfloor$. Expanding
$\log D(n)=\sum_p\sum_{j\ge1}(\log p)\mathbf1_{p^{3j}\mid n}$, equation (5)
bounds the primitive contribution to (4) by a constant times

$$
N^3\sum_p\frac{\log p}{p^3-1}
+N^2\sum_{p\le CN}J_p\log p.
$$

The first series converges. The second prime sum is at most
$\tfrac13\log(7N^3)\pi(CN)\ll N$. The primitive contribution is therefore
$O(N^3)$.

For an arbitrary triple write $\mathbf x=g\mathbf y$, with $\mathbf y$
primitive. Homogeneity gives $D(F(\mathbf x))=gD(F(\mathbf y))$. Sum the
primitive estimate at $N/g$, together with the term $\log g$, and use
$\sum_g g^{-3}(1+\log g)<\infty$. This proves (4). In particular,

$$
\#\{\mathbf x\in[1,N]^3:D(F(\mathbf x))>H\}
\ll\frac{N^3}{\log H}\qquad(H>1).
\tag{6}
$$

This controls the output's cube part, not the logarithm of its representation
multiplicity.

## Primitive collisions at cube-free outputs remain

The split identity already proved in the
[energy note](energy_and_multiplicity.md) is

$$
\begin{aligned}
F(27m+92s,212m+480s,171m+515s)\\
=F(27m+12s,212m+642s,171m+391s).
\end{aligned}
\tag{7}
$$

Its common value is

$$
G(m,s)=39076783m^3+310349304m^2s
+837996084ms^2+768326188s^3.
\tag{8}
$$

There are $\gg T^2$ pairs $1\le m,s\le T$ for which (8) is cube-free.
Here is a sieve proof, including the local conditions.

The binary cubic $G$ has no rational projective zero: the rank-two linear map
on either side of (7) would turn such a zero into a nonzero rational zero of
$F$, contrary to its distinct $2$-adic valuations. Thus $G$ is irreducible
over $\mathbb Q$, and its discriminant is nonzero. Also

$$
\gcd(G(1,0),G(0,1))=\gcd(39076783,768326188)=1.
$$

For each prime, at least one of these two values is a unit, so $G$ has no
fixed prime-cube divisor.

Outside finitely many primes dividing its discriminant, every nonzero zero of
$G$ modulo $p$ has a nonzero partial derivative. Split off the pairs with
$p\mid m,s$; these contribute at most $(T/p)^2$. For the other pairs,
choose a coordinate with nonzero derivative and fix the other coordinate.
There are at most three simple roots modulo $p^3$ for either choice. Hence

$$
\#\{1\le m,s\le T:p^3\mid G(m,s)\}
\le T^2p^{-2}+6T(Tp^{-3}+1).
\tag{9}
$$

Only primes $p\ll_G T$ can occur. Once $P$ contains the finitely many bad
primes, (9) gives the tail bound

$$
\#\{(m,s):\exists p>P,\ p^3\mid G(m,s)\}
\ll_G T^2P^{-1}+\frac{T^2}{\log T}.
$$

In complete residue boxes the local excluded proportions are
$O(p^{-2})$. Their product of complements is positive by local
nonobstruction. Finite CRT, followed by this tail estimate, proves the asserted
positive input density of cube-free $G$-values.

For these parameters the two triples in (7) are positive, primitive and
distinct. They lie in $[1,854T]^3$. The map from parameters to collision pairs
is injective: their difference is $(80s,-162s,124s)$, which determines $s$,
and then the first coordinate determines $m$. Thus this fixed split plane
supplies $\gg N^2$ primitive collisions with cube-free output in a box of
side $N$.

## Consequence for the density route

The restriction to cube-free outputs retains $\gg N^3$ input triples, and
$8F(\mathbf x)\in S_3$. A bound $O(N^3)$ for their restricted collision
count would therefore give positive lower density of $S_3$. No such bound,
nor the weaker bounded-fiber positive-mass criterion, has been established.
Equations (4) and (7) show why merely deleting common dilations does not
complete the argument: primitive split collisions survive, and the critical
average over large directions is still uncontrolled.

The [primitive-fiber analysis](primitive_cubic_fibers.md) now separates the
bounded entropy of common dilations from primitive multiplicity. It also
shows that every curve defined over $\mathbb Q$ on the special cubic's output
surface has degree divisible by three, excluding rational lines and
conics even without cube-freeness. No uniform estimate for its
higher-degree curves or primitive fibers was obtained.
