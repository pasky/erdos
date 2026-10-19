---
name: research/leads/totient_binary_series/integer_interpolation/phase_transference
title: Odd Kernel Cost and Phase Separation
desc: |
  A Gaussian comparison gives a quantitative converse to the odd-kernel
  phase obstruction; the totient recurrence reduces the relevant quotient
  to two dimensions and removes the polynomial loss from the asymptotic
  phase criterion on linearly growing supports.
problems:
- 249
research_state: ready
review_status: unreviewed
created: 2026-09-17T15:24:06Z
updated: 2026-10-14T00:26:52Z
---

***

The phase obstruction on the
[[research/leads/totient_binary_series/integer_interpolation/two_depth_carries|two-depth
page]] gives a lower bound on the cost of an odd scalar-kernel vector.
This page proves a converse, first for any integer row and then with a
sharper dependence for the totient row. The latter uses the explicit
small vectors with zero shadow from the
[[research/leads/totient_binary_series/integer_interpolation/shadows|shadow
construction]]. It gives another exact formulation of the remaining
arithmetic question. No required lower bound on the totient phase error
is proved. All arguments are author-recorded and unreviewed.

## The general weighted comparison

Let $V\in\mathbb Z^M$ be nonzero, let $A\in\mathbb Z^M$, and let
$w_i>0$. Suppose some $z\in K=\ker_{\mathbb Z}V$ has $A\cdot z$ odd.
In particular $M\ge2$. Put

$$
C_{\rm odd}=\min_{\substack{z\in K\\A\cdot z\ {\rm odd}}}
                 \sum_iw_i|z_i|,\qquad
\epsilon=\inf_{\theta\in\mathbb R,\ m\in\mathbb Z^M}
                 \max_i\frac{|\theta V_i-A_i/2-m_i|}{w_i}.
\tag{1}
$$

The minimum cost is attained: below each fixed cost there are only
finitely many integer vectors. The phase infimum is also attained.
One may restrict $\theta$ to $[0,1]$ because $V$ is integral, and only
finitely many $m$ can occur below any fixed error. It is positive:
zero error paired with an odd kernel vector would make a half-integer
an integer.

**Theorem 1.** With this notation,

$$
\frac1{2\epsilon}\le C_{\rm odd}
 <\frac{(M+3)\sqrt M}{\epsilon}.
\tag{2}
$$

The proof below gives the smaller upper constant
$(M+3)\sqrt M\log2/\pi$.

*Lower bound.* For any odd $z\in K$, pairing its coordinates with
the errors in (1) gives $-A\cdot z/2-m\cdot z$, a half-integer
of absolute value at least $1/2$. The triangle inequality bounds it
by the phase error times $\sum_iw_i|z_i|$. Minimize both quantities.
$\square$

For the upper bound write $W=\operatorname{diag}(w_i)$ and
$L=WK$ in its Euclidean span
$E=\ker_{\mathbb R}(VW^{-1})$, of dimension $d=M-1$.
Let $L_0=\{Wz:z\in K,\ A\cdot z\ {\rm even}\}$, an index-two
sublattice. If $P_E$ is orthogonal projection, then

$$
\Gamma=L^*=P_EW^{-1}\mathbb Z^M,\qquad
L_0^*=\Gamma\ \cup\ (\Gamma+\gamma),\qquad
\gamma=P_EW^{-1}A/2.
\tag{3}
$$

Here a dual lattice consists of the real vectors pairing integrally
with every primal vector. To justify the first equality, $K$ is a
primitive subgroup of $\mathbb Z^M$: its quotient is the free group
$V\mathbb Z^M$. Every integral functional on $K$ therefore extends
to $\mathbb Z^M$, by choosing a generator of that quotient. The
extension is pairing with an integer vector; weighting and projecting
give (3). The second equality follows because $\gamma$ pairs with
$Wz$ as $A\cdot z/2$ and is not in $\Gamma$.

Let $\delta$ be the shortest Euclidean norm in $\Gamma+\gamma$.
This is a nonzero attained minimum. Projection along $E^\perp$ gives

$$
\delta=\inf_{\theta,m}
 \|W^{-1}(\theta V-A/2-m)\|_2,\qquad
\epsilon\le\delta\le\sqrt M\,\epsilon.
\tag{4}
$$

We use the following elementary Gaussian argument, including its constants.

**Lemma 2 (index-two Euclidean transference).** Let $\Lambda_0$ have
index two in a rank-$d$ Euclidean lattice $\Lambda$. Let $\delta$ be
the shortest norm in the nontrivial coset
$\Lambda_0^*\setminus\Lambda^*$, and let $\lambda$ be the shortest
norm in $\Lambda\setminus\Lambda_0$. Then

$$
\lambda\delta<(d+4)\log2/\pi.
\tag{5}
$$

*Proof.* Write $\rho_s(X)=\sum_{x\in X}\exp(-\pi\|x\|^2/s^2)$.
Periodizing the Gaussian on a fundamental parallelepiped, whose
Fourier coefficients are
$s^d\exp(-\pi s^2\|y\|^2)$ divided by the lattice determinant, gives

$$
\rho_s(\Lambda+c)=\frac{s^d}{\det\Lambda}
 \sum_{y\in\Lambda^*}e^{-\pi s^2\|y\|^2}
                    e^{2\pi i\langle y,c\rangle}.
\tag{6}
$$

All sums converge absolutely. In particular
$\rho_s(\Lambda+c)\le\rho_s(\Lambda)$ and
$\rho_{\sqrt2s}(\Lambda)\le2^{d/2}\rho_s(\Lambda)$.
Let $\Gamma=\Lambda^*$ and write the other dual coset as
$\Gamma+\gamma$. Splitting each Gaussian exponential in half and
using its shortest norm gives

$$
\frac{\rho_{1/s}(\Gamma+\gamma)}{\rho_{1/s}(\Gamma)}
 \le2^{d/2}e^{-\pi s^2\delta^2/2}.
$$

Set $a=(d+4)\log2/\pi$ and $s=\sqrt a/\delta$. The right side is
$1/4$. Since $\det\Lambda_0=2\det\Lambda$, applying (6) to the two
primal lattices gives

$$
\rho_s(\Lambda\setminus\Lambda_0)
=\frac{s^d}{2\det\Lambda}
 [\rho_{1/s}(\Gamma)-\rho_{1/s}(\Gamma+\gamma)]
\ge\frac38\rho_s(\Lambda).
$$

The same split in the primal lattice bounds the mass outside radius
$r$ by

$$
\rho_s(\{x\in\Lambda:\|x\|\ge r\})
 \le2^{d/2}e^{-\pi r^2/(2s^2)}\rho_s(\Lambda).
$$

At $r=s\sqrt a=a/\delta$ this is at most $\rho_s(\Lambda)/4$.
Some vector outside $\Lambda_0$ must therefore have norm strictly
less than $r$. This proves (5). $\square$

Apply Lemma 2 to $L_0\subset L$. An odd vector with Euclidean norm
$\lambda$ has weighted cost at most $\sqrt M\,\lambda$.
Equations (4)--(5) prove Theorem 1. This argument uses the nontrivial
dual coset determined by parity, not the shortest vector of an
unrelated dual lattice.

## The norm on the relevant dual coset

For the rest of the page take all $V_i>0$, as holds for totient
windows. Give $E_0=\ker_{\mathbb R}V$ the norm
$\|x\|_w=\sum_iw_i|x_i|$. The restrictions

$$
\mathcal D=\{(A/2+m)|_{E_0}:m\in\mathbb Z^M\}
$$

are precisely the nontrivial coset of $K^*$ in the dual of its even
sublattice, viewed as linear functionals on $E_0$. Moreover

$$
\epsilon=\min_{\ell\in\mathcal D}\|\ell\|_*,
\tag{7}
$$

where $\|\ell\|_*=\sup_{\|x\|_w\le1,\ x\in E_0}|\ell(x)|$.

Here is a direct justification of the norm equality, without a lattice
transference assertion. For fixed $b=A/2+m$, the least $e$ for which
the intervals

$$
[b_i/V_i-ew_i/V_i,\ b_i/V_i+ew_i/V_i]
$$

have a common point is

$$
e_b=\max_{i<j}
\frac{|V_jb_i-V_ib_j|}{V_jw_i+V_iw_j}.
$$

Pairwise intersection suffices for finitely many intervals in one
dimension. Pairing $b-\theta V$ with a unit vector of $E_0$ shows
$\|b|_{E_0}\|_*\le e_b$. The vectors
$(V_je_i-V_ie_j)/(V_jw_i+V_iw_j)$ give the reverse inequality.
Minimizing over $m$ proves (7).

**Lemma 3 (two-dimensional normed version).** In a two-dimensional
normed real space, let $\bar K_0\subset\bar K$ be an index-two pair
of lattices. If $\bar\epsilon$ is the least dual norm in the
nontrivial dual coset, some vector of $\bar K\setminus\bar K_0$
has norm less than $3/\bar\epsilon$.

*Proof.* Choose two vectors in the compact unit ball maximizing the
absolute determinant. They form a real basis. In their coordinates
$t=(t_1,t_2)$, maximality and the triangle inequality give
$\|t\|_\infty\le\|t\|\le\|t\|_1$, hence
$\|t\|_2/\sqrt2\le\|t\|\le\sqrt2\|t\|_2$.
The least Euclidean norm in the nontrivial dual coset is at least
$\bar\epsilon/\sqrt2$. Lemma 2 at $d=2$ therefore supplies an odd
primal vector of norm less than
$12\log2/(\pi\bar\epsilon)<3/\bar\epsilon$. $\square$

## Removing the dimension loss for totient windows

Use the notation and finite support $\mathcal N=[B,R]$ of the
shadow page, with $B\ge4$, $J\ge1$, $N=R-B+1$ and $H=R+J+2$.
In (1) set

$$
V_n=U_J(n)/2,\qquad A_n=\Phi_n/2,\qquad w_n=n+J+2.
$$

Assume an odd kernel vector exists and the two rows
$(\varphi(k))_{B<k\le R}$ and $(\varphi(k+J))_{B<k\le R}$ are
linearly independent. Then $N\ge3$. Put

$$
K_*=18H^3,\qquad R_*=9(N-3)H^3.
$$

**Theorem 4 (the two-dimensional quotient).** If $\epsilon K_*<1$,
then

$$
\frac1{2\epsilon}\le C_{\rm odd}<\frac3\epsilon+R_*.
\tag{8}
$$

For every $\epsilon>0$, one consequently has the uniform bound

$$
C_{\rm odd}<
\frac3\epsilon+R_*+18(N+3)\sqrt N\,H^3.
\tag{9}
$$

*Proof.* Let $F$ be the subspace of the real kernel on which both
shadow coordinates vanish. Lemma 10 of the shadow page supplies
$N-3$ independent integer vectors $x_i$ spanning $F$, each with
$\|x_i\|_w\le K_*$. Their parity pairings are zero.
Choose a minimizer $\ell\in\mathcal D$ in (7). Since
$\ell(x_i)$ is an integer and
$|\ell(x_i)|\le\epsilon K_*<1$, it is zero for every $i$.
Thus $\ell$ annihilates $F$.

The shadow image $\bar K=\sigma(K)\subseteq\mathbb Z^2$ is a
rank-two lattice, by the row-rank calculation in Proposition 11 of
the shadow page. Give its real span the quotient norm

$$
\|\sigma(x)\|_{\rm q}=\min_{f\in F}\|x+f\|_w.
$$

The minimum is attained, and parity is well defined on $\bar K$
because $A\cdot x=v(x)/2$ vanishes on $F$.
The nontrivial dual coset on the quotient identifies with
$\mathcal D\cap F^\perp$. A functional in this intersection has
the same dual norm before and after quotienting. Therefore its
least norm $\bar\epsilon$ is at least $\epsilon$; the minimizer
just found shows equality.

Lemma 3 gives an odd shadow of quotient norm less than $3/\epsilon$.
Choose an integer lift $z\in K$ and a minimizing real correction
$f\in F$. Express $f$ in the basis $x_i$, and replace its coefficients
by nearest integers. The resulting integer lift has the same shadow
and parity and costs at most

$$
\|\sigma(z)\|_{\rm q}+\frac12\sum_i\|x_i\|_w
\le\|\sigma(z)\|_{\rm q}+R_*.
$$

This proves (8). If instead $\epsilon K_*\ge1$, Theorem 1 gives
$C_{\rm odd}<(N+3)\sqrt N\,K_*$, which together with (8) implies
the uniform bound (9). $\square$

**Corollary 5 (the phase criterion without a polynomial loss).**
Consider a family with $J\to\infty$, $B\to\infty$, $R=O(J)$,
and the two hypotheses of Theorem 4 at every member. Then

$$
\frac{C_{\rm odd}}{2^J}\longrightarrow0
\quad\Longleftrightarrow\quad
\epsilon\,2^J\longrightarrow\infty.
\tag{10}
$$

Either condition proves irrationality of $S$ by the full-tail
criterion of the two-depth page.

*Proof.* The lower bound in (2) proves the forward implication.
For the reverse implication divide (9) by $2^J$. The two polynomial
terms tend to zero because $N,H=O(J)$, and the remaining term is
$3/(\epsilon2^J)$. The increasing cutoff supplies the valuation gap
needed to exclude every fixed denominator. $\square$

For $[J,2J]$ along sufficiently large $J=2^m$, the two prime choices
in Proposition 9 of the two-depth page give both an odd kernel and
two independent normalized totient rows: their parity pairs are
$(1,0)$ and $(0,1)$. Neither index equals the lower endpoint for
large powers of two, so they belong to the recurrence index set.
Thus (10) applies on this specific support, at that proposition's
disclosed fixed-modulus prime-theorem standing. The same hypotheses
hold on $[B_J,3J]$ along those powers, with $B_J$ from Corollary 7a
of the shadow page.

This removes the factor of order $J^{3/2}$ from the sufficient phase
growth condition obtained by applying Theorem 1 alone. It does not
prove $\epsilon_J2^J\to\infty$, even along a subsequence. Under
hypothetical rationality with odd denominator $b$, the explicit phase
$\theta=b/2^{J+1}$ on the two-depth page still gives
$\epsilon_J\le b/2^{J+2}$, consistently with (10).

A separate
[[research/leads/totient_binary_series/integer_interpolation/phase_localization|arithmetic
localization]] supplies the reverse implication on $[J,2J]$.
It uses $\varphi(3k)=2\varphi(2k)$ for odd $k$ coprime to $3$,
two small integer-minor arguments, and the shared dyadic factors of
rational approximants. It proves

$$
S\notin\mathbb Q
\quad\Longleftrightarrow\quad
\limsup_{J\to\infty,\ J=2^m}\epsilon_J2^J=\infty.
$$

Together with (10), this is equivalent to a short-support odd family
of cost $o(2^J)$ along some subsequence of powers of two. The reverse
implication requires that additional arithmetic argument; it does not
follow by restricting the shadow page's wider-support constructions.
No divergence along all powers of two or unbounded successful family
is proved. The localization also reduces a sufficient finite test to
explicit odd dyadic numerators, with all constants and the complete tail
retained on that page.

## Scope and a normalization check

For $V=(2,3)$, $A=(1,0)$ and unit weights, the odd kernels are
$(3t,-2t)$ with $t$ odd, so $C_{\rm odd}=5$.
The phase $\theta=3/10$, $m=(0,1)$ has errors $(1/10,-1/10)$.
The half-integer lower bound gives $\epsilon\ge1/10$, proving
$\epsilon=1/10$ and equality in the lower bound of (2).
This exposed exact example checks the factor two; it is not an
experiment on totients or evidence for an asymptotic estimate.

The open quantitative target is the actual separation
$\epsilon_J2^J\to\infty$ on a permitted unbounded subsequence.
The short-support equivalence above identifies it as a formulation of
the original target, with a new finite arithmetic test available.
Theorems 1 and 4
give no distribution law for totient windows and no positive
odd-vector count by themselves. They do show why estimates on the
relevant dual phase, and not only searches for short kernel vectors,
remain a mathematically viable way to attack the original cost bound.
