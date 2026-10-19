---
name: research/totient_binary_new_attack/kernel_rigidity
title: Exact Shadows and Identity Rigidity for Short-Support Kernel Vectors
desc: |
  On the short support [J,2J] the shadow u of every vector is fixed by its
  window coefficients at any complementary pair. Fixed-prime robust vectors
  have u=0 for sufficiently large even J. At suitable powers of two the
  kernel shadows fill 2^J Z x 2Z, giving two quantitative implications between
  odd cost and inhomogeneous approximation of S.
tags: []
sources: []
problems:
- 249
created: 2026-10-15T19:52:41Z
updated: 2026-10-15T19:52:41Z
---

# Exact Shadows and Identity Rigidity for Short-Support Kernel Vectors

[[research/totient_binary_new_attack/_index|..]]

***

This page's results are Plasma AI's, author-recorded and without independent
review. They concern the odd scalar-kernel criterion for
[[problems/irrationality/E0249/_index|Problem 249]] on the short support
$[J,2J]$, which the corpus has shown to be equivalent to the irrationality of
$S=\sum_{n\ge1}\varphi(n)2^{-n}$ along powers of two. They prove two things
about that criterion. First, a kernel vector whose cancellation survives an
independent change of the totient at both positions of one complementary pair
has first shadow $u=0$. This applies, for sufficiently large even $J$, to
vectors robust under the multiplication laws at any fixed finite set of
primes. Second, at powers of two satisfying Lemma 4 the shadows fill exactly
the pairs $(u,v)$ with $2^J\mid u$ and $2\mid v$. Corollary 6 gives two
quantitative implications between odd cost and inhomogeneous approximation
of $S$, with different multiplier ranges. Neither result supplies the
missing asymptotic estimate. The
[[research/totient_binary_new_attack/proof_sketch|proof sketch]] places
them in the attack, and the
[[research/totient_binary_new_attack/partial_multiplicativity|fixed-prime
comparison argument]] bounds robust odd costs on supports of arbitrary
length.

## Notation

Write $\Phi_n=\sum_{m\le n}\varphi(m)2^{n-m}$, $T_n=2^nS-\Phi_n$, so that
$0<T_n\le n+2$, and

$$
U_J(n)=\Phi_{n+J}-2^J\Phi_n=\sum_{j=1}^J\varphi(n+j)2^{J-j}
=2^JT_n-T_{n+J},
$$

as on the
[[research/leads/totient_binary_series/integer_interpolation/two_depth_carries|two-depth
page]]. For $J\ge4$ let $z=(z_n)_{J\le n\le2J}$ be an integer vector and put

$$
u(z)=\sum_nz_n2^n,\qquad v(z)=\sum_nz_n\Phi_n,\qquad
\|z\|=\sum_n|z_n|(n+J+2),
$$

and let $L_J$ be the lattice of $z$ with $\sum_nz_nU_J(n)=0$. The pair
$\sigma(z)=(u(z),v(z))$ is the *shadow* of $z$, $\|z\|$ its *cost*, and $z$
is *odd* when $v(z)\equiv2\pmod4$. For $z\in L_J$ the complete-tail identity
of the two-depth page reads

$$
u(z)S-v(z)=\sum_nz_nT_n=2^{-J}\sum_nz_nT_{n+J},\qquad
|u(z)S-v(z)|\le2^{-J}\|z\|.
\tag{1}
$$

Since $\Phi_n$ is even for $n\ge3$, every $v(z)$ is even, and $2^J\mid u(z)$.
By the two-depth page's odd criterion (Corollaries 7 and 8 there), odd vectors
$z\in L_J$ with $\|z\|=o(2^J)$ along $J\to\infty$ prove that $S$ is
irrational; by Theorem 3 of the
[[research/leads/totient_binary_series/integer_interpolation/phase_localization|arithmetic
localization page]] such vectors exist along some powers of two exactly when
$S$ is irrational. Both are author-recorded corpus results.

The *window coefficients* of $z$ are, for $J+1\le m\le3J$,

$$
w_m(z)=\sum_{\substack{J\le n\le2J\\ m-J\le n\le m-1}}z_n2^{J-m+n},
\qquad\hbox{so that}\qquad
\sum_nz_nU_J(n)=\sum_{m=J+1}^{3J}\varphi(m)\,w_m(z).
$$

For $1\le r\le J$ the two window positions $J+r$ and $2J+r$ form the
*complementary pair* of $r$.

## The pair identity

**Lemma 1 (pair identity).** For every integer vector $z$ on $[J,2J]$ and
every $1\le r\le J$,

$$
u(z)=2^rw_{J+r}(z)+2^{J+r}w_{2J+r}(z).
$$

More generally, if $z$ is supported on an interval $[B,R]$ and $w_m(z)$ is
defined by the same formula for $B+1\le m\le R+J$, then every residue class
$r$ modulo $J$ satisfies $\sum_{m\equiv r}2^mw_m(z)=2^Ju(z)$.

*Proof.* Substituting $m=n+j$,

$$
\sum_{m\equiv r\ (J)}2^mw_m(z)=\sum_nz_n
\sum_{\substack{1\le j\le J\\ n+j\equiv r\ (J)}}2^{n+j}2^{J-j}
=\sum_nz_n2^{n+J},
$$

because exactly one $j\in[1,J]$ lies in each residue class. On the support
$[J,2J]$ the window positions congruent to $r$ are $J+r$ and $2J+r$. $\square$

So the shadow coordinate $u$ is visible at every complementary pair, while the
kernel condition only asks for one weighted sum of the totients in the window
to vanish.

## Robust kernel vectors have zero shadow

Let $\mathcal G$ be a set of real functions on the positive integers. Call $z$
*$\mathcal G$-robust* if $\sum_mf(m)w_m(z)=0$ for every $f\in\mathcal G$.
When $\varphi\in\mathcal G$, robust vectors lie in $L_J$.

**Proposition 2 (robust vectors carry no approximation).** Suppose
$\varphi\in\mathcal G$ and, for some $1\le r\le J$, $\mathcal G$ contains two
functions differing only at $J+r$ and two functions differing only at $2J+r$
(among the window positions). Then every $\mathcal G$-robust $z$ has
$u(z)=0$ and $u(z)S-v(z)=-v(z)$. If moreover $v(z)\ne0$, then
$\|z\|\ge2^{J+1}$. Hence no $\mathcal G$-robust vector is odd with cost below
$2^{J+1}$, and all $\mathcal G$-robust vectors have proportional shadows.

*Proof.* Subtracting the robustness equations for two functions that differ
only at $J+r$ gives $w_{J+r}(z)=0$, and likewise $w_{2J+r}(z)=0$. Lemma 1 gives
$u(z)=0$. Then (1) gives $2^J|v(z)|\le\|z\|$, and a nonzero even $v(z)$ has
$|v(z)|\ge2$. All shadows lie on the line $u=0$. $\square$

**Corollary 3 (multiplicative identities).** Fix $y\ge2$, let
$P_y=\prod_{p\le y}p$, and for $m\ge1$ write $m=s_y(m)k_y(m)$, where $s_y(m)$
is the largest divisor of $m$ whose prime factors are at most $y$. Let

$$
\mathcal G_y=\bigl\{m\mapsto\varphi(s_y(m))\,h(k_y(m)):\ h\ \hbox{an arbitrary
real function}\bigr\}.
$$

Then $\varphi\in\mathcal G_y$, and $z$ is $\mathcal G_y$-robust exactly when,
for every $k$ free of prime factors up to $y$,

$$
\sum_{J<m\le3J,\ k_y(m)=k}\varphi(s_y(m))\,w_m(z)=0 .
$$

If $J$ is even and $J\ge2P_y$, every $\mathcal G_y$-robust vector on $[J,2J]$
has $u=0$, with the consequences of Proposition 2.

*Proof.* Multiplicativity gives $\varphi(m)=\varphi(s_y(m))\varphi(k_y(m))$, so
$\varphi\in\mathcal G_y$ with $h=\varphi$; the displayed condition is the
coefficient of $h(k)$. Choose $r$ with $J/2<r\le J$ such that $J+r$ and $2J+r$
have no prime factor up to $y$: as $J$ is even, $J+r$ and $2J+r$ are odd when
$J+r$ is; for each odd prime $p\le y$ it suffices that
$J+r\not\equiv0,-J\pmod p$, which excludes at most two of the $p\ge3$ classes.
These conditions define a nonempty union of classes modulo $P_y$, and the
interval $(3J/2,2J]$, of length $J/2\ge P_y$, meets each class. Put $m_1=J+r$
and $m_2=2J+r$. Then $k_y(m_i)=m_i$, and any other window position with
$y$-rough part $m_i$ would be a multiple $sm_i$ with $s\ge2$, which exceeds $3J$
because $m_1>3J/2$. Changing $h$ at $m_i$ therefore changes the function only
at $m_i$ among the window positions, and Proposition 2 applies. $\square$

The relations covered by Corollary 3 are homogeneous linear consequences
of multiplicativity at the primes up to a fixed $y$, for instance
$\varphi(3k)=2\varphi(2k)$ for odd $k$ prime to three, which is the identity
used on the arithmetic localization page. The bound applies on $[J,2J]$
when $J$ is even and $J\ge2P_y$. It makes no assertion for arbitrary
growing $y$ or for cancellations using additional arithmetic information.

**Remark (fixing every prime-power value).** The same eventual conclusion
holds for the smaller class with $h(1)=1$ and
$h(p^a)=\varphi(p^a)$ for every $p>y$ and $a\ge1$. Here is an elementary
sufficient threshold. Choose four distinct primes $r_1,t_1,r_2,t_2>y$
and put $D=P_yr_1t_1r_2t_2$. For any even $J\ge2D$, use the Chinese
remainder theorem to choose $m$ in $(3J/2,2J]$ satisfying

$$
m\equiv0\pmod{r_1t_1},\qquad
m\equiv-J\pmod{r_2t_2},\qquad
m\not\equiv0,-J\pmod p\quad(p\le y).
$$

The last choices are compatible because $J$ is even and each odd prime
excludes at most two classes. The interval has length at least $D$, so
it contains a representative. Both $m$ and $m+J$ are $y$-rough, are
divisible by two distinct primes and exceed $3J/2$. Changing $h$ at either
of them preserves all fixed prime-power values and changes only that
position in the window. Proposition 2 applies again. The threshold is
sufficient, not optimal; individual smaller $J$ can be checked directly.

**What Proposition 2 leaves open.** A kernel vector on $[J,2J]$ with
$u\ne0$ must have $(w_{J+r},w_{2J+r})\ne(0,0)$ for every $r$. Its cancellation
cannot therefore survive independent variation at both members of any pair.
For large even $J$, the preceding remark produces a pair with two distinct
prime factors above the fixed $y$ in each member. A construction escaping
this obstruction must use information beyond the stated fixed-prime laws
and prime-power values; this could be further relations, rather than
individual evaluations. Proposition 2 itself says nothing about longer
supports. The argument needs one
residue class modulo $J$ with only two window positions; on a support of at
least $2J+1$ consecutive integers every class has three or more, and Lemma 1
no longer isolates a pair. Check 5 of the evidence confirms that on $[4,3J]$,
for $y\in\{7,13\}$ and $J\in\{16,24,32\}$, the functional $u$ is not in the span
of the structural relations, so robust vectors with $u\ne0$ exist there. The
[[research/totient_binary_new_attack/partial_multiplicativity|comparison
argument]] addresses those longer supports by a different method. It still
requires a fixed prime set; the growing primes of the
[[research/leads/totient_binary_series/dilation_cube|prime dilation page]]
are outside that conclusion.

## The exact shadow image at powers of two

Put $a_t=\varphi(t)/2$ for $t\ge3$.

**Lemma 4 (generating columns).** Let $J=2^m$ with $m\ge3$. The vectors
$(a_k,a_{k+J})$, $J<k\le2J$, generate a sublattice of $\mathbb Z^2$ whose
index is a power of two. If there are primes $p\in(J,2J)$ with
$p\equiv3\pmod4$ and $P\in(2J,3J]$ with $P\equiv3\pmod4$ and $15\mid P-J$,
these vectors generate $\mathbb Z^2$. Such primes exist for all sufficiently
large $m$.

*Proof.* The index divides every $2\times2$ minor. At $k=3J/2$ and $k=2J$ the
vectors are $(\varphi(3\cdot2^{m-1})/2,\varphi(5\cdot2^{m-1})/2)=(2^{m-2},2^{m-1})$
and $(\varphi(2^{m+1})/2,\varphi(3\cdot2^m)/2)=(2^{m-1},2^{m-1})$, with minor
$-2^{2m-3}$, so no odd prime divides the index. For the prime two, the vector
at $k=p$ has $a_p=(p-1)/2$ odd. The vector at $k=P-J\in(J,2J]$ has
$15\mid k$, so $8\mid\varphi(k)$ and $a_k$ is even, while $a_{k+J}=a_P=(P-1)/2$
is odd. Their minor $a_pa_P-a_ka_{p+J}$ is odd. So the index is one. The
congruences on $P$ define a reduced class modulo $60$, since $J$ is prime to
$15$, and the prime number theorem for the fixed moduli $4$ and $60$ supplies
both primes once $J$ is large. $\square$

The fixed-modulus prime number theorem has the disclosed external standing
recorded on the arithmetic localization page; no growing modulus is used.
Check 1 of the evidence verifies generation directly for $3\le m\le13$, and
the explicit primes for $6\le m\le13$; at $m=4,5$ no such $P$ exists, but the
vectors still generate $\mathbb Z^2$.

**Proposition 5 (exact shadow image).** If $J=2^m$ and the vectors of
Lemma 4 generate $\mathbb Z^2$, then

$$
\sigma(L_J)=\{(u,v)\in\mathbb Z^2:\ 2^J\mid u,\ 2\mid v\}.
$$

*Proof.* The inclusion $\subseteq$ was noted above. Conversely let
$2^J\mid u$ and $2\mid v$, and put $z^0=(u/2^J)e_J$. For $J<k\le2J$ let
$r_k=e_k-2e_{k-1}$, the recurrence coordinates of Lemma 10 of the
[[research/leads/totient_binary_series/integer_interpolation/shadows|shadows
page]]. From $\Phi_k-2\Phi_{k-1}=\varphi(k)$ and
$U_J(k)-2U_J(k-1)=\varphi(k+J)-2^J\varphi(k)$,

$$
u(r_k)=0,\qquad v(r_k)=\varphi(k),\qquad
\sum_n(r_k)_nU_J(n)=\varphi(k+J)-2^J\varphi(k).
$$

Hence $z=z^0+\sum_kc_kr_k$ has $u(z)=u$, and it lies in $L_J$ with $v(z)=v$
exactly when

$$
\sum_kc_k\varphi(k)=X:=v-v(z^0),\qquad
\sum_kc_k\varphi(k+J)=Y:=2^JX-\frac u{2^J}U_J(J).
$$

Both $X$ and $Y$ are even, because $v$, $\Phi_J$ and $U_J(J)$ are, and the
vectors $(\varphi(k),\varphi(k+J))$ generate $2\mathbb Z^2$ by Lemma 4. $\square$

This settles, on $[J,2J]$ at these $J$, the lattice condition that Corollary 13
of the shadows page leaves as a hypothesis for unscaled realization.

**Corollary 6 (the odd cost is Diophantine).** Let $J=2^m\ge16$ admit the
primes $p,P$ of Lemma 4, and put $x_k=k2^{J-2}S$ for integers $k$.

1. If $z\in L_J$ is odd with $\|z\|<2^{J+1}$, then $k=u(z)/2^J$ is a nonzero
   integer with $|k|\le2^J\|z\|/(2J+2)$ and
   $\|x_k-\tfrac12\|\le2^{-J-2}\|z\|$, where $\|\cdot\|$ applied to a real
   number is the distance to the nearest integer.
2. Conversely, for every integer $k$ with $1\le|k|<2^{J-1}$ there is an odd
   $z\in L_J$ with $u(z)=2^Jk$ and
   $\|z\|\le160J^6\bigl(1+2^J\|x_k-\tfrac12\|\bigr)$.

*Proof.* For the first part, $u(z)=0$ would give $|v(z)|\le\|z\|2^{-J}<2$
by (1), impossible for $v(z)\equiv2\pmod4$. Then
$|u(z)|\le2^{2J}\sum_n|z_n|\le2^{2J}\|z\|/(2J+2)$, and $v(z)/4\in\frac12+\mathbb Z$
with $|x_k-v(z)/4|=|u(z)S-v(z)|/4\le2^{-J-2}\|z\|$.

For the second part let $\mu\in\frac12+\mathbb Z$ be nearest to $x_k$, put
$u=2^Jk$, $v=4\mu\equiv2\pmod4$ and $\varepsilon=uS-v$, so
$|\varepsilon|=4\|x_k-\frac12\|$. Write $k$ in balanced binary with digits in
$\{-1,0,1\}$ at positions $0,\dots,J$, possible because $|k|<2^{J-1}$, and let
$z^0$ carry these digits at $J,\dots,2J$. Then $u(z^0)=u$ and
$\|z^0\|\le C_0:=(J+1)(5J/2+2)$. Define $X$ and $Y$ as in the proof of
Proposition 5 with this $z^0$, that is $X=v-v(z^0)$ and
$Y=2^JX-\sum_nz^0_nU_J(n)$. From $T_n=2^nS-\Phi_n$ and
$U_J(n)=2^JT_n-T_{n+J}$,

$$
X=-\varepsilon+\sum_nz^0_nT_n,\qquad
Y=-2^J\varepsilon+\sum_nz^0_nT_{n+J},
\qquad |X|\le|\varepsilon|+C_0,\quad |Y|\le2^J|\varepsilon|+C_0 .
$$

Let $A,B$ be the vectors of Lemma 4 at $k=3J/2,2J$, with determinant
$D_1=-2^{2m-3}$, and $C,E$ those at $k=p,P-J$, with odd determinant $D_2$,
$|D_2|\le9J^2/2$ because $0<a_t\le3J/2$ in the window. For $t\in\mathbb Z^2$,
Cramer's rule gives $D_1t$ as an integer combination of $A,B$ with
coefficients of absolute value at most $(J/2)\|t\|_1$, and $D_2t$ as one of
$C,E$ with coefficients at most $(3J/2)\|t\|_1$. Choosing integers with
$\rho D_1+\tau D_2=1$, $|\rho|\le|D_2|$ and $|\tau|\le|D_1|$, the vector
$t=\rho D_1t+\tau D_2t$ becomes an integer combination of the four vectors with
coefficient sum at most $5J^3\|t\|_1$. Applied to $t=(X/2,Y/2)$ this gives
integers $c_k$, supported on four indices, solving the system of Proposition 5
with $\sum|c_k|\le\frac52J^3(|X|+|Y|)$. Each $r_k$ costs at most $9J+4\le10J$.
Therefore $z=z^0+\sum_kc_kr_k$ is an odd vector of $L_J$ with $u(z)=u$ and

$$
\|z\|\le C_0+25J^4\bigl(2C_0+(2^J+1)|\varepsilon|\bigr)
\le160J^6\bigl(1+2^J\|x_k-\tfrac12\|\bigr),
$$

using $C_0\le3J^2$ for $J\ge16$ and
$(2^J+1)|\varepsilon|\le2^{J+3}\|x_k-\frac12\|$.
$\square$

Write $\gamma_J=\min_{1\le k<2^{J-1}}\|k2^{J-2}S-\frac12\|$ and let
$\kappa_J$ be the least cost of an odd vector in $L_J$. Corollary 6 gives

$$
\kappa_J\le160J^6\bigl(1+2^J\gamma_J\bigr),
$$

and, when $\kappa_J<2^{J+1}$, some $1\le|k|\le2^J\kappa_J/(2J+2)$ has
$\|k2^{J-2}S-\frac12\|\le2^{-J-2}\kappa_J$. So along these powers of two,
$\gamma_J=o(J^{-6})$ on a subsequence gives the odd-cost criterion
$\kappa_J=o(2^J)$ there; conversely $\kappa_J=o(2^J)$ gives a multiplier
$1\le|k|=o(2^{2J}/J)$ with $\|k2^{J-2}S-\frac12\|=o(1)$. The two directions
differ in the range of $k$ and in the threshold, and in neither does the
totient enter except through $S$. If $S=a/(q2^w)$ with $q$ odd,
then $k2^{J-2}S\in q^{-1}\mathbb Z$ for $J\ge w+2$, so
$\|k2^{J-2}S-\frac12\|\ge1/(2q)$ and $\kappa_J\ge2^{J+1}/q$, recovering
Proposition 6 of the two-depth page on this support.

## What this changes in the route

The odd-cost criterion on $[J,2J]$ is, in both directions of Corollary 6, a
statement about how well $\frac12$ is approximated modulo one by multiples
$k2^{J-2}S$ of controlled size. The upper implication does not establish
that such approximations occur for this $S$. Check 4 records a verified
LLL basis of $L_J$ at $J\in\{16,32,64,128\}$, every vector of cost at most
$2J^2$, with at least one odd vector. These are returned vectors, not
certified minima, and no asymptotic bound follows from these instances.
Corollary 3 and its remark exclude the stated fixed-prime robust
construction for sufficiently large even $J$. A cheap odd family using
additional arithmetic information remains open.

## Finite checks

The [evidence entry point](evidence/main.py) checks, in exact arithmetic:
generation by the columns of Lemma 4 for $J=2^m$, $3\le m\le13$, with the
power-of-two minor and, for $6\le m\le13$, the explicit odd minor; the shadow
image of Proposition 5 for $J\in\{8,12,16,20,24,32,48,64\}$ from a verified
kernel basis, including non-powers of two where the lemma is not proved; that
$u$ lies in the span of the $y$-structural relations for $y\in\{5,7,13\}$ and
$J\in\{16,32,48,64\}$, below the threshold of Corollary 3 except at
$y=5$, $J=64$, where the complementary pair of the proof is exhibited; the
cost profile of a verified basis of $L_J$ for $J\in\{16,32,64,128\}$; and the
control on $[4,3J]$ described above. These finite checks do not establish the
asymptotic statements, which rest on the proofs.
