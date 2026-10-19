---
name: research/erdos_940/profinite_cubic_density
title: The complete congruence distribution of the special cubic
desc: Uniform congruence-level second moments and entropy, quantitative profinite convergence, and exact descent at three; the integer-fiber estimate remains open.
tags: []
sources: []
created: 2026-09-22T18:56:50Z
updated: 2026-09-22T18:56:50Z
---


# The complete congruence distribution of the special cubic

***

## Status

The statements below are proved. They show that even the **joint**
congruence distribution has bounded second moment and bounded entropy
deficit. They do not establish either density conclusion for the positive
integer values of

$$
F(x,y,z)=x^3+2y^3+4z^3.
$$

In particular, they do not estimate the microscopic representation
function in a growing integer box.

The subsequent [sampling theorem](congruence_preserving_thinning.md)
makes this limitation precise: synthetic integer multiplicities preserve
the actual box marginals modulo $N^2$ and every fixed modulus, converge
to this same profinite density, and retain all the established major-arc
estimates, but have support $O(N^2\log N)$ and unbounded microscopic
entropy. They are not asserted to come from a polynomial.

## A second moment uniform in every modulus

For a positive integer $q$, put

$$
\rho_q(n)=q^{-2}\#\{\mathbf x\bmod q:F(\mathbf x)\equiv n\pmod q\}.
$$

Use the complete sums and nonnegative resonance weights from the
[major-arc note](cubic_major_arcs.md):

$$
S(q,b)=\sum_{x\bmod q}e(bx^3/q),\qquad
A(q)=q^{-6}\sum_{\substack{b\bmod q\\(b,q)=1}}
       |S(q,b)S(q,2b)S(q,4b)|^2.
$$

That note proves

$$
\mathfrak S:=\sum_{d\ge1}A(d)<\infty,
\qquad \sum_{d>m}A(d)\ll m^{-2/3}.
\tag{1}
$$


**Proposition.** For every $q\ge1$,

$$
\frac1q\sum_{n\bmod q}\rho_q(n)^2
=\sum_{d\mid q}A(d)\le\mathfrak S,
\tag{2}
$$

and, with $0\log0=0$,

$$
0\le\frac1q\sum_{n\bmod q}\rho_q(n)\log\rho_q(n)
\le\log\mathfrak S.
\tag{3}
$$


**Proof.** The normalized Fourier coefficient of $\rho_q$ at $b$
is

$$
\widehat\rho_q(b)=q^{-3}S(q,-b)S(q,-2b)S(q,-4b).
$$

Parseval therefore expresses the left side of (2) as the sum of the
squares of these coefficients. Group frequencies by their exact
conductor $d=q/(b,q)$. For $b=(q/d)c$,

$$
S(q,jb)=(q/d)S(d,jc)\qquad(j=1,2,4).
$$

The conductor-$d$ group is exactly $A(d)$, proving (2).

Also $q^{-1}\sum_n\rho_q(n)=1$. Convexity of $t\log t$ gives
the lower bound in (3). Apply concavity of the logarithm to the
probability weights $\rho_q(n)/q$, restricted to their nonzero
support, to get

$$
\frac1q\sum_n\rho_q(n)\log\rho_q(n)
\le\log\left(\frac1q\sum_n\rho_q(n)^2\right).
$$

This proves the upper bound. $\square$

## Quantitative convergence on the profinite integers

Let $\mu$ be normalized Haar measure on $\widehat{\mathbb Z}$,
and view each $\rho_q$ as a function on that group. For $q\mid Q$,
counting residue lifts gives

$$
\mathbb E_\mu(\rho_Q\mid n\bmod q)=\rho_q.
\tag{4}
$$

Put $Q_m=\operatorname{lcm}(1,\ldots,m)$. Equations (2) and (4)
make $\rho_{Q_m}$ an $L^2$-bounded martingale. It consequently
converges in $L^2$ to a nonnegative function $\rho$, with
$\int\rho\,d\mu=1$. In fact

$$
\|\rho\|_2^2=\mathfrak S,
\qquad
\|\rho-\rho_{Q_m}\|_2^2
=\mathfrak S-\sum_{d\mid Q_m}A(d)
\le\sum_{d>m}A(d)\ll m^{-2/3}.
\tag{5}
$$

Here the equality of norms follows because every fixed positive integer
eventually divides $Q_m$; the identity for the difference is
orthogonality of conditional expectation. The inequality uses the fact
that every $d\le m$ already divides $Q_m$.

The pushforward of Haar measure on $\widehat{\mathbb Z}^3$ under
$F$ is exactly $\rho\,d\mu$. Indeed its mass on each cylinder
$n\equiv a\pmod q$ is $\rho_q(a)/q$, and (4) gives the same
mass for $\rho\,d\mu$. These cylinder sets determine a measure.
Moreover

$$
0\le\int\rho\log\rho\,d\mu\le\log\mathfrak S.
\tag{6}
$$

For example, the upper bound follows directly from Jensen under the
probability measure $\rho\,d\mu$, using $\int\rho^2=\mathfrak S$.
All quantities are integrable because $\rho\in L^2$.

## Exact descent and density at the prime three

Write $r_F(n)$ for the number of all positive integral
representations of $n$, without a box restriction.

**Proposition.** One has

$$
9\mid F(x,y,z)\quad\Longrightarrow\quad3\mid x,y,z,
\tag{7}
$$

and hence

$$
r_F(27n)=r_F(n),\qquad
r_F(n)=0\quad\text{if }v_3(n)\equiv2\pmod3.
\tag{8}
$$

The pushforward of normalized Haar measure on $\mathbb Z_3^3$
under $F$ has density, away from zero,

$$
f_3(n)=
\begin{cases}
1,&v_3(n)\equiv0\pmod3,\\
4/3,&v_3(n)\equiv1\pmod3,\\
0,&v_3(n)\equiv2\pmod3.
\end{cases}
\tag{9}
$$


**Proof.** Every cube modulo nine is $0,1$, or $-1$. For
$\epsilon_i\in\{-1,0,1\}$, the integer
$\epsilon_1+2\epsilon_2+4\epsilon_3$ lies between $-7$ and
$7$. If it is zero modulo nine it is zero as an integer. Since
$4>2+1$ and $2>1$, this forces all three $\epsilon_i$ to
vanish. This proves (7). Dividing all three coordinates by three
proves the bijection in (8); iterating it proves the vanishing assertion.

The 27 choices of coordinate residues modulo three give the following
numbers of output occurrences modulo nine, in order from residue zero
through residue eight:

$$
(1,3,3,4,3,3,4,3,3).
\tag{10}
$$

These counts follow by multiplying
$(1+t+t^{-1})(1+t^2+t^{-2})(1+t^4+t^{-4})$ modulo $t^9-1$.
The sole input class giving output zero modulo nine is the all-zero
class. Every other class has a unit coordinate. For $s\in\{1,-1\}$,

$$
\frac{(s+3u)^3-s^3}{9}=s^2u+3su^2+3u^3
$$

is a bijection of $\mathbb Z_3$: it reduces to $u$ modulo
three and its derivative is a unit everywhere, so every residue lifts
uniquely. Varying this unit coordinate therefore distributes the
output uniformly within its fixed residue class modulo nine, even
after the other two coordinates are fixed.

Each input residue triple has measure $1/27$; each output class
modulo nine has measure $1/9$. Thus (10) gives density one on
unit outputs and $4/3$ on outputs of valuation one. All remaining
inputs have all coordinates divisible by three. Scaling them down
costs a factor $1/27$ in input measure and scales output by 27,
also a factor $1/27$ in output Haar measure. Their normalized
density is consequently unchanged. Iterating proves (9). There is
no atom at zero, since (7) forces an exact zero in $\mathbb Z_3^3$
to be the zero vector. $\square$

In particular, the measures of the three valuation classes modulo
three are respectively $9/13,3/13,1/13$. Consequently

$$
\mu_3(F(\mathbb Z_3^3))=\frac{12}{13},\qquad
\int f_3^2\,d\mu_3=\frac{43}{39},\qquad
\int f_3\log f_3\,d\mu_3=\frac4{13}\log\frac43.
\tag{11}
$$

The second identity agrees with the independently computed local
resonance factor in the [major-arc note](cubic_major_arcs.md).

## What remains unproved

For a growing integer box, the required estimate would instead be,
for example,

$$
\sum_n R_N(n)\log R_N(n)\ll N^3,
\qquad
R_N(n)=\#\{\mathbf x\in[1,N]^3:F(\mathbf x)=n\}.
\tag{12}
$$

Equations (2)--(6) average over **complete residue boxes**, not over
$[1,N]^3$ at moduli of the size of the output range $N^3$.
No comparison supplying (12) has been proved. Taking a limit over
fixed congruences cannot by itself control concentration on a sparse
set of ordinary integers. The corresponding minor-arc correlation
term in the [major-arc note](cubic_major_arcs.md) remains uncontrolled.

Thus the exact descent at three and the bounded joint congruence
entropy do not settle the density question or any higher-exponent
infinitude case.
