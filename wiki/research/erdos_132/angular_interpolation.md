---
name: research/erdos_132/angular_interpolation
title: Angular interpolation identities and failure of shell-sign arguments
desc: |
  Complex barycentric weights retain angular information, but an exact
  rich-shell example defeats fixed-sign holomorphic and Hermitian charges.
sources: []
research_state: closed
created: 2026-09-23T01:43:51Z
updated: 2026-09-24T22:12:56Z
---


# Angular interpolation identities and failure of shell-sign arguments

***

This was a different approach from convex layers, valuations, and scalar radial
positivity. Its exact identities are valid, but neither of the proposed sign
arguments solves [Problem 132](../../problems/distance_problems/E0132/_index.md).

## Identities retaining the edge directions

Identify $A$ with distinct complex numbers $z_1,\ldots,z_n$, and put

$$f(z)=\prod_i(z-z_i),\qquad w_i=1/f'(z_i).$$

Lagrange interpolation, followed by taking the coefficient of
$z^{n-1}$, gives

$$M_\ell:=\sum_i w_i z_i^\ell=0\quad(0\le\ell\le n-2),
\qquad M_{n-1}=1.$$

For an occurring distance $r$ and integer $k\ge1$, define

$$B_r(k)=\sum_{\substack{i<j\\|z_i-z_j|=r}}
w_iw_j(z_i-z_j)^{2k}.$$

The even exponent makes this independent of how unordered pairs
are oriented. Expanding the power yields

$$2\sum_r B_r(k)=
\sum_{a=0}^{2k}(-1)^a\binom{2k}{a}M_{2k-a}M_a.$$

For $1\le k\le n-2$, at least one exponent in every product is
at most $n-2$, so the sum is zero. For $k=n-1$, only
$a=n-1$ survives. Consequently

$$\sum_rB_r(k)=0\quad(1\le k\le n-2),$$
$$\sum_rB_r(n-1)=
\frac{(-1)^{n-1}}2\binom{2n-2}{n-1}. \tag{1}$$

Under a direct similarity $z\mapsto az+b$, the weights acquire
the factor $a^{-(n-1)}$. Hence each terminal charge
$B_r(n-1)$ is unchanged for its corresponding transformed class.
Reflection conjugates it. These charges retain angular information
discarded by scalar radial averaging.

A real Hermitian alternative is

$$H_r=\operatorname{Re}\sum_{\substack{i<j\\|z_i-z_j|=r}}
w_i\overline{w_j}.$$

For $n\ge3$, expanding the full ordered sums and using
$\sum_iw_i=\sum_iw_iz_i=0$ gives

$$\sum_rH_r=-\frac12\sum_i|w_i|^2,$$
$$\sum_r r^2H_r=-\frac12
\left|\sum_i w_i\overline{z_i}\right|^2. \tag{2}$$

## A rich class can have either sign

Let $\omega=e^{\pi i/3}$ and

$$A_p=\{0,1,2,\omega,1+\omega,p\}.$$

Among the five fixed points there are exactly seven unit pairs:
$01,0\omega,12,1\omega,1(1+\omega),2(1+\omega),
\omega(1+\omega)$. Along any fixed nonzero ray $p=\varepsilon v$
with $\varepsilon\to0^+$, no additional unit pair occurs for all
sufficiently small $\varepsilon>0$. For the fixed points of modulus
one this follows directly from

$$|\varepsilon v-a|^2=1
\iff \varepsilon^2|v|^2-2\varepsilon
\operatorname{Re}(v\bar a)=0;$$

the other fixed points follow by continuity. Thus the unit class
has $7>6$ pairs throughout these small configurations.

Put

$$F(z)=z(z-1)(z-2)(z-\omega)(z-1-\omega),\qquad
u_a=1/F'(a).$$

Using $\omega^2=\omega-1$ gives

$$u_0=\frac1{2(2\omega-1)},\qquad u_1=1,
\qquad u_\omega=-\frac{1+\omega}{3}.$$

The new weight at a fixed point $a$ is $u_a/(a-p)$. Only the
unit pairs $01$ and $0\omega$ have weights singular as $p\to0$.
Their contributions give

$$B_1(5)=\frac{C}{p}+O(1),
\qquad C=u_0(u_\omega-1)=\frac\omega2-\frac13,$$
$$H_1=\operatorname{Re}\frac{\omega}{6p}+O(1). \tag{3}$$

For the second identity the coefficient is
$-u_0(1+\overline{u_\omega/\omega})=\omega/6$.
All other unit-pair terms stay bounded.

Taking $p=\pm\varepsilon C$ makes
$\operatorname{Re}B_1(5)\to\pm\infty$; taking
$p=i\varepsilon C$ makes its imaginary part unbounded.
Taking $p=\pm\varepsilon\omega$ similarly makes
$H_1\to\pm\infty$.

Thus richness alone gives no fixed sign, even for the real part,
in either proposed charge. The failure is established by exact
algebra, not by numerical examples.

## Exact conclusion

The example does not have bounded total rarity and is not an Erdős
counterexample. It rules out the proposed inference that each rich
class contributes a charge of a prescribed sign to (1) or (2).
It does not rule out a future argument controlling several classes
jointly under a bounded-rarity hypothesis. No such joint control
was proved here; proposing it is not a reduction of the original
problem to an established lemma.

The author checked the interpolation expansions, similarity
normalization, seven-edge count, and both coefficients in (3); the
argument is author-recorded.
