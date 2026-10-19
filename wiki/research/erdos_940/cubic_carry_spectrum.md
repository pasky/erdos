---
name: research/erdos_940/cubic_carry_spectrum
title: Exact dyadic carries and persistent rational resonances
desc: Exact local uniformity, including prime-degree geometric forms, does not bound finite-height carries; primitive high-conductor cubic characters can retain rational resonances.
tags: []
sources: []
created: 2026-09-22T17:29:14Z
updated: 2026-09-23T01:47:49Z
---


# Exact dyadic carries and persistent rational resonances

***

## Status

The identities and the spectral counterexample below are proved. They describe a
failed mixing argument for the [critical carry map](energy_and_multiplicity.md),
not a density theorem. A spectral approach would have to retain the rational
resonances rather than contract all high-conductor modes.

The subsequent [major-arc analysis](cubic_major_arcs.md) now controls those
resonances in an integrated sense: their weights have tail
$O(Q^{-2/3})$, and the rational major arcs with growing denominator cutoff
have $O(N^3)$ energy. The remaining minor-arc correlation with
high-multiplicity outputs is not controlled, so this does not establish
the missing carry-entropy bound.

Write $F=x^3+2y^3+4z^3$ and $e(t)=\exp(2\pi it)$.

## Exact local uniformity

Every residue modulo $2^m$ has exactly $2^{2m}$ preimages under
$F:(\mathbb Z/2^m\mathbb Z)^3\to\mathbb Z/2^m\mathbb Z$.
For an odd target, fix $y,z$; cubing permutes the odd residues, giving
exactly one $x$. For an even target $a$, write $x=2u$ and use

$$
F(2u,y,z)=2F(y,z,u).
$$

The count is four times the count for $a/2$ modulo $2^{m-1}$, because
$y,z$ each have two lifts while $u$ ranges modulo $2^{m-1}$.
Induction from modulus one proves the assertion. Equivalently, $F$ sends
Haar probability measure on $\mathbb Z_2^3$ to Haar measure on $\mathbb Z_2$.

## Exact carry lift

Let $N=2^k$, $k\ge1$. For odd $a\in[1,N)$ and $y,z\in[1,N]$, let $x$ be
the unique odd representative in $[1,N]$ for which $F(x,y,z)\equiv a\pmod N$,
and write $F(x,y,z)=a+NC$. Define
$A_N(v)=3v^2+3Nv+N^2$.
For binary digits $\delta,\eta,\zeta$, lift

$$
a'=a+N\delta,\quad y'=y+N\eta,\quad z'=z+N\zeta.
$$

The unique root lift is $x'=x+N\xi$, where
$\xi\equiv\delta-C\pmod2$. Indeed, $A_N(x)$ is odd. Direct expansion then
gives the new carry

$$
C'=\frac{C-\delta+\xi A_N(x)}2
       +\eta A_N(y)+2\zeta A_N(z).                       \tag{1}
$$

The shifts in this four-branch expression depend on the full current
coordinates. Equation (1) is not a proved finite-state entropy contraction.

## High conductor alone does not imply cancellation

For the carries above define

$$
\phi_{a,k}(\theta)=\frac1{N^2}\sum_{y,z\le N}
 e\bigl(\theta C_{a,k}(y,z)\bigr).
$$

There are primitive characters $\theta_k$ of conductor $2^{2k+12}$,
bounded away from zero in $\mathbb R/\mathbb Z$, such that for every
sufficiently large $k$,

$$
\frac2N\sum_{\substack{1\le a<N\\a\text{ odd}}}
|\phi_{a,k}(\theta_k)|^2\ge\frac1{100}.                  \tag{2}
$$


Put $Q=2^{3k+12}$, choose an odd integer $b_k$ nearest $Q/9$, and set
$\alpha_k=b_k/Q$, $\theta_k=N\alpha_k\pmod1$.
Then $|\alpha_k-1/9|\le Q^{-1}$, and the conductor assertion follows
because $b_k$ is odd. Also $N\pmod9$ cycles through
$1,2,4,8,7,5$, so the distance of $\theta_k$ from zero is eventually
at least $1/10$.

For uniformly chosen odd $x\in[1,N]$ and independent uniform
$y,z\in[1,N]$, put $\Psi_N(\alpha)=\mathbb E e(\alpha F(x,y,z))$.
The complete cubic sums modulo nine are

$$
S_9(h)=3\bigl(1+2\cos(2\pi h/9)\bigr),\qquad
S_9(1)S_9(2)S_9(4)=-81.
$$

For the product identity, the three numbers
$1+2\cos(2\pi h/9)$, $h=1,2,4$, are the roots of
$T^3-3T^2+3$. Each coordinate, including odd $x$, is asymptotically uniform
modulo nine. Consequently

$$
\Psi_N(1/9)\longrightarrow-\frac19.
$$

Moreover, summing cubes gives
$\mathbb EF=\tfrac74N^3+3N^2+N$. The inequality
$|e(s)-e(t)|\le2\pi|s-t|$ therefore yields

$$
\limsup_{k\to\infty}|\Psi_N(\alpha_k)+1/9|
\le\frac{7\pi}{8192}.
$$

In particular $|\Psi_N(\alpha_k)|\ge1/10$ for all sufficiently large $k$.
On the other hand, the carry parametrization gives exactly

$$
\Psi_N(\alpha_k)=\frac2N\sum_{a\text{ odd}}
 e(\alpha_k a)\phi_{a,k}(\theta_k).
$$

Cauchy–Schwarz proves (2).

Thus even average cancellation of every primitive high-conductor carry
character is false. The counterexample is an odd-modulus resonance at
$1/9$, fully compatible with exact uniformity modulo powers of two.
It does not disprove bounded logarithmic multiplicity, nor a spectral
estimate with suitably separated rational major arcs. No such corrected
estimate was proved in this continuation.

## Prime-degree geometric forms: exact local and first-layer facts

The following statements are proved. They concern the candidate

$$
F_p(\mathbf x)=\sum_{i=0}^{p-1}p^i x_i^p
$$

for an odd prime $p$. After a fixed powerful dilation this is an
admissible degree-$p$ form for the density question. No positive-density
conclusion is drawn.

**Lemma.** Each residue modulo $p^m$ has exactly $p^{m(p-1)}$
preimages under $F_p:(\mathbb Z/p^m\mathbb Z)^p\to
\mathbb Z/p^m\mathbb Z$.

For $m=1$ this follows from $x_0^p=x_0$ modulo $p$.
For $m\ge2$, a unit modulo $p^m$ is a $p$th power precisely when
its residue modulo $p^2$ is a $p$th power, and then it has exactly
$p$ roots modulo $p^m$. This follows from the structure of the unit
group at an odd prime; equivalently, the binomial expansion shows
that the $p$th-power map sends $1+p\mathbb Z_p$ onto
$1+p^2\mathbb Z_p$.

Let the target $a$ be a unit and fix $x_2,\ldots,x_{p-1}$ modulo
$p^m$. A $p$th-power unit with a given nonzero residue modulo $p$
has one prescribed lift modulo $p^2$. Exactly one choice of
$x_1\bmod p$ makes
$a-\sum_{i\ge1}p^i x_i^p$ have this lift. There are
$p^{m-1}$ choices for $x_1$ and then $p$ for $x_0$.
The total is $p^{m(p-2)}p^{m-1}p=p^{m(p-1)}$.

For a target divisible by $p$, necessarily $p\mid x_0$. Use

$$
F_p(pu,x_1,\ldots,x_{p-1})
       =pF_p(x_1,\ldots,x_{p-1},u).
$$

Each solution modulo $p^{m-1}$ on the right has $p^{p-1}$ lifts
on the left: the last $p-1$ original coordinates each lift in $p$
ways, while $u$ determines $x_0\bmod p^m$. Induction proves the
lemma. Thus $F_p$ sends Haar measure exactly to Haar measure.

There are two finite-height consequences:

* On the first digit box $\{0,\ldots,p-1\}^p$, the map is bijective
  modulo $p^p$. Recover $x_0$ uniquely from the target modulo $p$,
  subtract its exact $p$th power, divide by $p$, and repeat for the
  remaining digits.
* For $B=p^k$, $k\ge1$, the box $\{0,\ldots,B-1\}^p$ is exactly
  uniform modulo $pB$, with $B^{p-1}/p$ preimages per residue.
  Changing a root by a multiple of $B$ changes its $p$th power by a
  multiple of $pB$. The full count modulo $pB$ from the lemma therefore
  divides by $p^p$, the number of lifts of a root tuple modulo $B$.

Neither statement gives uniformity for this box modulo $B^p$.
In particular the first-layer bijection has not been iterated.
For a unit $u$, an integer $v\ne0$, and $j\ge1$, the binomial expansion
gives exactly

$$
v_p((u+p^jv)^p-u^p)=j+1+v_p(v).
$$

The first binomial term has this valuation and every later term has
strictly larger valuation. A high input digit consequently starts
affecting output near position $j+1$, not $pj$ as in characteristic-$p$
Frobenius interleaving. The carries retain the earlier root data.
No height-preserving correction or bounded-multiplicity induction was
proved. Small-box observations are not used as evidence for such an
induction.

## Averaging the lower-degree coefficients does not control the required trace

A subsequent attempt enlarged the state to include all quadratic and
linear coefficients. The following operator identity is exact, but its
norm is over the enlarged coefficient space, not the required cubic
frequency line.

Fix positive integers $a_1,a_2,a_3$ and define, on the seven-dimensional
torus,

$$
G_N(\alpha,\boldsymbol\beta,\boldsymbol\gamma)
=N^{-3}\sum_{0\le x_i<N}
 e\left(\alpha\sum_i a_ix_i^3+
        \sum_i\beta_ix_i^2+\sum_i\gamma_ix_i\right).
$$

Writing $x_i=2y_i+\epsilon_i$ gives $G_{2N}=TG_N$, where

$$
\begin{split}
(Tf)(\alpha,\boldsymbol\beta,\boldsymbol\gamma)
={}&\frac18\sum_{\boldsymbol\epsilon\in\{0,1\}^3}
 e\left(\alpha\sum_i a_i\epsilon_i^3+
        \sum_i\beta_i\epsilon_i^2+\sum_i\gamma_i\epsilon_i\right)\\
&\quad\cdot f\left(8\alpha,
  (4\beta_i+12a_i\epsilon_i\alpha)_i,
  (2\gamma_i+4\epsilon_i\beta_i+6a_i\epsilon_i^2\alpha)_i\right).
\end{split}
\tag{8}
$$

With normalized Haar measure on this torus,

$$
\|Tf\|_2^2=\frac18\|f\|_2^2\qquad(f\in L^2).
\tag{9}
$$

Indeed, each branch in (8), before its coefficient $1/8$, preserves
the norm: its linear substitution is a surjective integral torus
endomorphism, and its scalar phase has modulus one. A Fourier mode
whose $\boldsymbol\gamma$ frequency is $\mathbf w\in\mathbb Z^3$
has frequency $2\mathbf w+\boldsymbol\epsilon$ after that branch.
The eight branches therefore have disjoint Fourier supports, proving
(9), first for trigonometric polynomials and then by density.

For $N=2^k$, one has $G_N=T^k1$. Thus (9) recovers the ambient
identity $\|G_N\|_2^2=N^{-3}$. The estimate needed for a cubic
energy proof would instead be

$$
\int_0^1|G_N(\alpha,\mathbf0,\mathbf0)|^2\,d\alpha
\ll N^{-3}.
\tag{10}
$$

Its left side is the normalized equal-value count in $[0,N)^3$.
It restricts to a measure-zero coefficient subspace, so (9) supplies
no such estimate. An $O(N^3)$ energy bound here would suffice for
positive density of positive values after discarding the $O(N^2)$
input tuples with a zero coordinate; no such bound was obtained.

For completeness, on real coefficient lifts each coordinate satisfies

$$
D_i=\beta_i^2-3a_i\alpha\gamma_i,
\qquad D_i'=16D_i
$$

under the substitutions in (8). This identity concerns the real lifts;
it is not asserted as a well-defined invariant after arbitrary changes
of torus representatives. In particular, one cannot replace the
special starting trace by an independent Haar-distributed coefficient
box without an additional argument. The needed restriction estimate,
or an entropy substitute for it, remains unproved.

## What averaging integer root translations actually proves

The following gives a rigorous orbit average, not the missing
critical restriction. Use positive roots $1\le x_i\le N$ in
the definition of $G_N$, which leaves its ambient norm unchanged.
Let $\mu_H$ be the distribution on $\mathbb T^7$ of

$$
\left(\alpha,(3a_i\alpha h_i)_i,(3a_i\alpha h_i^2)_i\right),
\qquad
\alpha\text{ Haar-uniform},\quad
\mathbf h\in\{0,\ldots,H-1\}^3\text{ uniform}.
$$

For every nonzero Fourier frequency $\nu$,

$$
0\le\widehat\mu_H(\nu)\le 2/H.                         \tag{11}
$$

Indeed, integrating over $\alpha$ counts the zeros of

$$
k+3\sum_i a_i(\ell_i h_i+m_i h_i^2).
$$

If some $(\ell_i,m_i)\ne(0,0)$, fixing the other coordinates
leaves a nonconstant polynomial with at most two roots. If all
such pairs vanish, a nonzero frequency has $k\ne0$ and gives
no zeros. Thus $\mu_H$ converges weakly to ambient Haar measure.

Put

$$
A_{N,H}=H^{-3}\sum_{\mathbf h\in\{0,\ldots,H-1\}^3}
\#\{(\mathbf x,\mathbf y)\in[1,N]^6:
              F(\mathbf x+\mathbf h)=F(\mathbf y+\mathbf h)\}.
$$

Expanding the cubic and discarding its constant phase gives

$$
N^{-6}A_{N,H}=\int |G_N|^2\,d\mu_H.
$$

All Fourier coefficients of $|G_N|^2$ are nonnegative, and
their sum is $|G_N(0)|^2=1$. Its zero coefficient is $N^{-3}$.
Consequently (11) implies

$$
A_{N,H}\le N^3+2N^6/H.                                \tag{12}
$$

For these particular positive cubic differences, the factor two
can be replaced by one: if $x_i\ne y_i$, then
$(x_i+h_i)^3-(y_i+h_i)^3$ is strictly monotone for $h_i\ge0$.
Thus each fixed off-diagonal pair allows at most $H^2$
translations.

### A sharper bound from the checked quadratic estimates

For $H\ge N$ and every $\varepsilon>0$,

$$
A_{N,H}\ll_{\mathbf a,\varepsilon}
N^3+N^6H^{-2+\varepsilon}.                            \tag{13}
$$

For fixed endpoints, put $d_i=x_i-y_i$. The translation equation
is exactly

$$
3\sum_i a_i d_i(2h_i+x_i+y_i)^2=-\sum_i a_i d_i^3.
$$

When all three differences are nonzero, the
[uniform ternary-quadratic estimate](cubic_collision_ranges.md#a-uniform-ternary-quadratic-bound)
gives $O_{\mathbf a,\varepsilon}(H^{1+\varepsilon})$ translations. Its
coefficient-height hypotheses hold uniformly since $N\le H$. Summing over
endpoint pairs proves the second term of (13).

If exactly two differences are nonzero and their cubic sum
$a_i d_i^3+a_jd_j^3$ is nonzero, use the binary-quadratic
estimate and then allow the free translation in the shared
coordinate. This also gives $O(H^{1+\varepsilon})$ translations.
If that cubic sum vanishes, the differences have a fixed rational
ratio $d_j=-c d_i$, with $c^3=a_i/a_j$; otherwise this case is empty.
There are $O_{\mathbf a}(N^4)$ endpoint pairs. Positivity of
$2h_i+x_i+y_i$ makes the remaining homogeneous quadratic relation
a single line, so there are $O_{\mathbf a}(H^2)$ translations.
Its averaged contribution is $O(N^4/H)=O(N^3)$.
One nonzero difference is impossible by positivity. The diagonal
contributes exactly $N^3$. This proves (13).

For fixed $\eta>0$, (13) gives critical average energy when
$N\le H^{2/3-\eta}$, after choosing $\varepsilon$ sufficiently
small. This recovers the previously controlled short-difference
range in translated-box language; it is not a new critical range.

### Exact limitation

A translated box provides at most $N^3$ values below
$O_{\mathbf a}((H+N)^3)$. Extracting positive global density
from a single box therefore requires $H/N$ bounded. Neither
(12) nor (13) gives critical energy there.

Indeed, for even $N$, every collision whose endpoints lie in
$[N/2,N]^3$ is present in at least $(N/2)^3$ of the windows
with $\mathbf h\in[0,N)^3$. Hence

$$
A_{N,N}\ge\tfrac18 E_{[N/2,N]^3}.
$$

An $O(N^3)$ bound at bounded aspect ratio would already supply
the desired positive-density theorem. The proved orbit
equidistribution has not supplied that estimate, nor a sufficient
weaker bound for neighbor existence or entropy.
