---
name: research/erdos_940/cartesian_extraction
title: Cartesian restrictions cannot be extracted from almost full input mass
desc: A proved output-defined restriction retains almost all inputs but has only small Cartesian rectangles; even vanishing relative entropy can erase an exponential sieve weight.
tags: []
sources: []
created: 2026-09-22T19:21:57Z
updated: 2026-09-22T19:21:57Z
---


# Cartesian restrictions cannot be extracted from almost full input mass

***

## Status and reason for considering this question

The propositions below are proved. They concern every fixed diagonal
form of degree $r$ in $r$ variables, $r\ge3$. They do **not**
settle either target question about $S_r$.

The [bounded-fiber criterion](energy_and_multiplicity.md) would give positive
density from a positive fraction of input tuples lying in bounded fibers. Those
tuples need not form a Cartesian product. The distinction matters for a new
possible method: Croot, Mao, Pohoata, Sheffer, and Yip's
[weighted entropic sieve, Section 4](https://arxiv.org/html/2606.17487v2#S4)
assumes independent coordinate laws in Proposition 4.3. Its Theorem 4.1 assumes
Cartesian input sets and a uniform bound on every output fiber; the proof uses
these hypotheses separately in equations (12)--(14). Theorem 1.7 bounds a
$B_3[g]$ subset of the first $N$ cubes by
$O(g^{1/9}N\exp(-c\sqrt{\log N}/\log\log N))$. These statements and the
relevant proof passages were checked in the full primary text. None asserts
bounded typical multiplicity for all triples, or a density estimate for their
values.

The next construction shows, within the exact diagonal-form setting,
why one cannot automatically replace those hypotheses by high input
mass or even by a vanishing relative-entropy deficit.

## An almost full set with small Cartesian rectangles

Fix $r\ge3$ and nonzero integers $a_1,\ldots,a_r$, and put

$$
F(\mathbf x)=\sum_{i=1}^r a_i x_i^r,
\qquad g=\gcd(r,2),\qquad Y=\frac{\log N}{10}.
$$

For sufficiently large $N$, let

$$
\mathcal P_N=\{p\in[Y,2Y]:p\equiv-1\pmod{2r},\quad
                         p\nmid a_1\cdots a_r\},
\quad \ell_N=|\mathcal P_N|,
\quad \Delta_N=\prod_{p\in\mathcal P_N}p.
$$

The prime number theorem in this fixed progression gives

$$
\ell_N\sim\frac{\log N}{10\varphi(2r)\log\log N},
\qquad \log\Delta_N\sim\frac{Y}{\varphi(2r)}.
\tag{1}
$$

In particular, $\Delta_N\le N^{1/5}$ eventually. Define the
output-dependent input restriction

$$
\Gamma_N=\{\mathbf x\in[N]^r:
                p\nmid F(\mathbf x)\text{ for all }p\in\mathcal P_N\}.
$$


**Theorem.** One has

$$
|\Gamma_N|=\left(1-O_r\left(\frac1{\log\log N}\right)\right)N^r.
\tag{2}
$$

Nevertheless, every Cartesian rectangle
$B_1\times\cdots\times B_r\subseteq\Gamma_N$, with
$B_i\subseteq[N]$, satisfies

$$
\prod_{i=1}^r|B_i|
\le(1+o_r(1))N^r(g/r)^{\ell_N}.
\tag{3}
$$

If $B^r\subseteq\Gamma_N$, the stronger common-set conclusion is

$$
|B|\le(1+o_r(1))N(g/r)^{\ell_N}.
\tag{4}
$$

Thus (3) saves $\exp(-c_r\log N/\log\log N)$ in volume, and
(4) saves such a factor in the root-set size, for some $c_r>0$.

**Proof.** For each selected prime,
$\gcd(r,p-1)=\gcd(r,2)=g$. The power map on $\mathbb F_p$
therefore has fibers of size at most $g$, including its fiber at zero.
After fixing $x_2,\ldots,x_r$, the congruence $F=0\pmod p$
allows at most $g$ residue classes for $x_1$. Hence

$$
\#\{\mathbf x\in[N]^r:p\mid F(\mathbf x)\}
\le g(N/p+1)N^{r-1}.
$$

The union bound, (1), and $p\ge Y$ prove (2), since
$\sum_{p\in\mathcal P_N}p^{-1}=O_r(1/\log Y)$.

For a nonempty rectangle as in the theorem, write
$s_{i,p}=|B_i\bmod p|$ and
$T_{i,p}=\{a_i b^r:b\in B_i\bmod p\}$.
The sum $T_{1,p}+\cdots+T_{r,p}$ omits zero. Indeed, any choice
of these residues has independent representatives in the corresponding
$B_i$, and a zero sum would contradict the restriction defining
$\Gamma_N$. Iterated Cauchy--Davenport therefore gives

$$
\sum_i|T_{i,p}|\le p+r-2.
$$

Since $|T_{i,p}|\ge s_{i,p}/g$,

$$
\sum_i s_{i,p}\le g(p+r-2).
\tag{5}
$$

Assign each $p$ to an index $i$ for which
$s_{i,p}\le g(p+r-2)/r$. Let $\mathcal P_i$ be the resulting
partition and $\Delta_i=\prod_{p\in\mathcal P_i}p$, allowing
$\Delta_i=1$. CRT and interval counting imply

$$
|B_i|\le (N+\Delta_i)
       \prod_{p\in\mathcal P_i}\frac{g(p+r-2)}{rp}.
$$

Multiply over $i$. Every $\Delta_i\le\Delta_N\le N^{1/5}$,
and

$$
\prod_{p\in\mathcal P_N}\left(1+\frac{r-2}{p}\right)=1+o_r(1).
$$

This proves (3). Empty rectangles are trivial. If every $B_i=B$,
then all the $s_{i,p}$ are equal, so (5) gives the same bound for
$|B\bmod p|$ at every prime. Applying CRT once proves (4).
Finally $g<r$, and (1) gives the stated exponential savings.
$\square$

## Vanishing relative entropy is not sufficient for the weighted step

Specialize to $F=x^3+2y^3+4z^3$. The preceding prime progression
is $p\equiv5\pmod6$, equivalently $p\equiv2\pmod3$ for the
large primes being used. Let $U_N$ be uniform on $[N]^3$, and
let $\mu_N=U_N(\,\cdot\mid\Gamma_N)$. If
$\varepsilon_N=1-|\Gamma_N|/N^3$, then exactly

$$
D(\mu_N\Vert U_N)=-\log(1-\varepsilon_N)
                 =O(1/\log\log N)=o(1).
\tag{6}
$$

Here $D$ is relative entropy, with natural logarithms. The identity

$$
D(\mu_N\Vert U_N)
=\left(\sum_{i=1}^3H((\mu_N)_i)-H(\mu_N)\right)
 +\sum_{i=1}^3D((\mu_N)_i\Vert\operatorname{Unif}[N])
\tag{7}
$$

shows that the total correlation and all marginal entropy deficits
also tend to zero; $H$ denotes Shannon entropy with the same logarithm.

Define nonnegative weights

$$
m_p(\mathbf x)=p\,1_{p\mid F(\mathbf x)},\qquad
K_N(\mathbf x)=\prod_{p\in\mathcal P_N}(1+m_p(\mathbf x)).
$$

Cubing permutes $\mathbb F_p$, so $F=0\pmod p$ has exactly
$p^2$ solutions. Fixing any one coordinate leaves precisely $p$
solutions in the other two. Thus $m_p$ has mean one and each
one-coordinate marginal mean is one. CRT gives

$$
\Delta_N^{-3}\sum_{\mathbf x\bmod\Delta_N}K_N(\mathbf x)=2^{\ell_N}.
$$

Every residue vector has
$(N/\Delta_N)^3(1+O(\Delta_N/N))$ representatives in the box,
uniformly. Positivity of the weights permits summing these relative
errors, yielding

$$
\mathbb E_{U_N}K_N=(1+O(\Delta_N/N))2^{\ell_N},
\qquad \mathbb E_{\mu_N}K_N=1.
\tag{8}
$$

The latter identity holds because every factor is one on $\Gamma_N$.

Consequently a product-law lower bound cannot automatically extend to
correlated laws in the form

$$
\mathbb E_\mu K_N\ge
2^{\ell_N}\exp(-C D(\mu\Vert U_N))
$$

with fixed $C$: (6) and (8) contradict it. By (7), replacing the
entropy penalty by marginal deficits plus total correlation does not
repair this assertion. This example tests such an extension; it does
not contradict a theorem stated for independent coordinates.

## Consequence for the density problem

A set of bounded-fiber input tuples of size $cN^r$, if obtained,
could be intersected with $\Gamma_N$ at a cost of only $o(N^r)$
tuples. Thus the [positive-density criterion](energy_and_multiplicity.md)
remains viable on these non-Cartesian restrictions. Conversely, (3)--(4)
show that high input mass alone cannot supply the Cartesian hypothesis
required by the cited bounded-multiplicity sieve. No estimate for the
actual integer fibers of $F$, and no new infinitude case, follows
from this construction.
