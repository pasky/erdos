---
name: research/erdos_940/independent/quartic_pattern_elimination_and_random_omission
title: 'Independent record: Erdős Problem 940'
desc: Unverified independent record; the quartic alternative and selected claims were checked separately in the topical notes.
tags: []
sources: []
created: 2026-09-22T20:53:41Z
updated: 2026-09-22T20:53:41Z
---


# Independent record: Erdős Problem 940

***

The companion working files this record names (`positive_density_reduction.md`
and the others listed at its end) were not retained; the names are kept so
the citations stay readable, and the retained re-derivations are the topical
notes of this folder.

## 1. Scope and outcome

This investigation used only
[problem page](../../../problems/diophantine_problems/E0940/_index.md) and the supplied
papers. No web search was made, and no earlier research notes were assumed.
Assertions in digests about unspecified “current research” were not treated as
results. The full supplied Ghidelli paper and Voight chapter were read by the
collaborators using their results. The full Beyer de Ryke paper was also read
for its canonical decomposition and counting framework, not to re-audit its
known cubic theorem.

Write

$$
\mathcal P_r=\{m\geq1:p\mid m\Longrightarrow p^r\mid m\},\qquad
S_r=\bigcup_{j=1}^r j\mathcal P_r.
$$

The supplied background establishes
$\underline d(\mathbb N\setminus S_3)>0$. It does not establish
$d(S_3)=0$.

The main argument developed here is a quartic complement argument:

**Quartic theorem.** For every $\varepsilon>0$, there are integers
$M\geq1$ and $a$ such that

$$
 \limsup_{X\to\infty}\frac M X
 \#\{n\leq X:n\in S_4,\ n\equiv a\pmod M\}<\varepsilon.
 \tag{1.1}
$$

In particular,

$$
 \underline d(\mathbb N\setminus S_4)>0.
 \tag{1.2}
$$


The complete assembly of this argument is recorded below. Its new ingredients
are the elimination of every principal finite-character quartic coefficient
pattern, and a small random omission of primes that suppresses every
remaining determinant squareclass. The randomization is only an existence
device for a finite modulus.

This does **not** prove density zero or positive density for $S_4$.
No result settling either question for any $r\geq5$ was obtained.
Density zero for $S_3$ also remains unresolved here. Thus this is not a
complete resolution of all the questions in the problem.

The mathematical argument below has been checked within this investigation;
it has not been externally reviewed. One independent internal review
checked the elimination and quadratic-character lemmas but not the final
analytic note. That review's remaining question was
the uniform Gaussian conductor and $L$-function bound, proved in Section 5
below. No specific mathematical gap in the assembled quartic argument was
identified.

Two other collaborators read the completed analytic note and checked its
Gaussian lattice estimate, conductor argument, trace
bookkeeping, omission estimate, and tail bound. Neither reported a
substantive gap. This is an internal check, not external confirmation of
the new theorem.

## 2. Canonical decomposition and an exact density-zero reduction

For any $r\geq3$, put

$$
 \mathcal D_r=\{d\geq1:v_p(d)\in\{0,r+1,\ldots,2r-1\}\text{ for all }p\}.
$$

Every $m\in\mathcal P_r$ has a unique expression $m=dx^r$, with
$d\in\mathcal D_r$ and $x\geq1$. Indeed, an exponent divisible by
$r$ goes entirely into $x^r$; an exponent congruent to
$s\in\{1,\ldots,r-1\}$ is uniquely $r+s+ru$, with $u\geq0$.
Consequently

$$
 W_r:=\sum_{d\in\mathcal D_r}d^{-1/r}
 =\prod_p\left(1+\sum_{s=1}^{r-1}p^{-1-s/r}\right)<\infty,
 \qquad \#(\mathcal P_r\cap[1,X])\leq W_rX^{1/r}.                 \tag{2.1}
$$

Sums of fewer than $r$ summands therefore account for
$O_r(X^{1-1/r})$ integers up to $X$.

For fixed $B$, let $V_{r,B}$ be the union of the value sets of
$\sum_{i=1}^r d_ix_i^r$, with $d_i\in\mathcal D_r\cap[1,B]$ and
$x_i\geq1$. Counting tuples in a containing box gives

$$
 0\leq S_r(X)-V_{r,B}(X)
 \leq rW_r^{r-1}X\sum_{\substack{d\in\mathcal D_r\\d>B}}d^{-1/r}
       +O_r(X^{1-1/r}).                                      \tag{2.2}
$$

For every $0<\eta<1/[r(r+1)]$, the coefficient tail is
$O_{r,\eta}(B^{-\eta})$, because
$\sum_d d^{-1/r+\eta}<\infty$.

It follows that the following statements are equivalent:

* $S_r$ has density zero;
* every positive diagonal form $a_1x_1^r+\cdots+a_rx_r^r$, with
  arbitrary fixed positive integer coefficients, has a density-zero value
  set on positive integer arguments.

For the nontrivial direction involving arbitrary coefficients, multiply the
form by $\lambda=(a_1\cdots a_r)^r$. Each $\lambda a_i x_i^r$ is
$r$-powerful, so the dilated value set lies in $S_r$. In the other
direction use (2.2), first at fixed $B$, then let $B\to\infty$.

In particular, positive upper density of $S_r$ would force positive
upper density for at least one fixed critical diagonal form. Allowing
infinitely many auxiliary powerful coefficients cannot, by itself, bypass
that critical diagonal-form problem. This reduction is not a positive-density
proof. A fuller separate version is in `positive_density_reduction.md`.

For the rest of the record set

$$
 \mathcal D=\mathcal D_4,\quad
 F_{\mathbf d}(\mathbf x)=\sum_{i=1}^4d_ix_i^4,\quad
 P=\prod_{i=1}^4d_i,\quad R=\operatorname{rad}(P),\quad
 w(\mathbf d)=P^{-1/4}.
$$

The squarefree part of $P$ is denoted by $D$; it can equal 1.

Two weighted convergence facts will be used repeatedly. For every fixed
$B_0>0$ and $0\leq\eta<1/4$,

$$
 \sum_{\mathbf d\in\mathcal D^4}
     w(\mathbf d)B_0^{\omega(R)}R^\eta<\infty.                 \tag{2.3}
$$

The local Euler factor is $1+O_{B_0}(p^{-5/4+\eta})$: the smallest
nontrivial coefficient exponent is 5. In particular,

$$
 \sum_{\substack{\mathbf d\in\mathcal D^4\\P^+(R)>Y}}
     w(\mathbf d)B_0^{\omega(R)}\ll_{B_0}Y^{-1/8}.             \tag{2.4}
$$

Here the condition implies $R>Y$, so (2.4) follows from (2.3) with
$\eta=1/8$. The tuple $R=1$ never belongs to this tail.

## 3. Elimination of the principal quartic patterns

Call a tuple $\mathbf d$ **exceptional in this record** if either


$$
 P\text{ is a square},                                      \tag{3.1}
$$

or, for some permutation $(i,j,k,l)$,

$$
 d_i^2d_j^2d_kd_l^3=4t^4\quad\text{for some }t\in\mathbb Q_{>0}.
                                                               \tag{3.2}
$$

This terminology refers to the finite-character expansion below, not to
Ghidelli's differently defined exceptional family.

**Elimination lemma.** If

$$
 v_2(n)=3,\qquad v_p(n)=1\quad\text{for every odd }p\mid P,    \tag{3.3}
$$

then an exceptional tuple cannot represent $n$ by $F_{\mathbf d}$,
even with arbitrary integer variables.

We first justify the quadratic obstruction. A positive definite rational
quaternary diagonal form of square determinant is similar to
$\langle1,A,B,AB\rangle$, with $A,B>0$. This is the norm form of
$(-A,-B\mid\mathbb Q)$. Its quaternion algebra is division at the real
place. If the form were isotropic over every $\mathbb Q_p$, the algebra
would split at every finite prime. Hilbert reciprocity forbids exactly one
ramified place. This uses precisely Voight, Proposition 14.2.1 and Corollary
14.2.3. The similarity follows directly by dividing a diagonal form
$\langle a,b,c,d\rangle$ by $a$ and rescaling its last coordinate,
using $abcd\in\mathbb Q^{\times2}$.

At an odd prime, a diagonal ternary form with unit coefficients has a
nontrivial zero: the sets $\{aX^2\}$ and $\{-c-bY^2\}$ in
$\mathbb F_p$ both have size $(p+1)/2$ and intersect. Set $Z=1$
and lift. Thus a unit-coefficient quaternary form is isotropic there.
Also, if $Q(\mathbf z)=n$ and a diagonal term $a_jz_j^2$ is a unit,
then $Q$ is isotropic over $\mathbb Q_p$ whenever $p\mid n$ for
odd $p$, or $8\mid n$ for $p=2$. Replace $z_j$ by

$$
 z_j\sqrt{1-n/(a_jz_j^2)}.
$$

The required square root exists in $1+p\mathbb Z_p$ for odd $p$,
or for arguments in $1+8\mathbb Z_2$ at 2, by Hensel lifting.

Suppose first that (3.1) holds and $F_{\mathbf d}(\mathbf x)=n$.
Apply these observations to $Q=\sum d_i z_i^2$, at
$z_i=x_i^2$. Each original summand has valuation zero or at least four
at every prime. At each odd $p\mid P$, (3.3) forces a unit summand;
at 2 the same follows because otherwise $16\mid n$. Hence $Q$
is isotropic at these primes. At every other odd prime its coefficients
are units. This contradicts the quaternion obstruction.

For (3.2), write $d_k=cu^2$, $d_l=cv^2$, with $c$ positive
squarefree and $u,v$ positive integers. The relation implies

$$
 d_id_jc^2uv^3=2t^2,\qquad
 2d_id_juv=(2t/(cv))^2.
$$

Use the identity

$$
 d_kx_k^4+d_lx_l^4
 =c(ux_k^2-vx_l^2)^2+2cuv(x_kx_l)^2.                          \tag{3.4}
$$

The resulting positive quaternary form

$$
 Q'=\langle d_i,d_j,c,2cuv\rangle
$$

has square determinant. At an odd $p\mid P$, a unit among the first
two original terms gives a unit term of $Q'$. If neither is a unit,
both are divisible by $p^4$. The remaining original terms must both
be units: exactly one would make their sum a unit, and neither would make
it divisible by $p^4$. Then $2cuv(x_kx_l)^2$ is a unit term of
$Q'$. At 2 at least one of the first two terms must be odd. Otherwise
the remaining terms would both be odd, and

$$
 c(u^2x_k^4+v^2x_l^4)\equiv2c\pmod8,
$$

contrary to (3.3). All remaining odd primes are unit-coefficient primes
for $Q'$. Thus $Q'$ is isotropic everywhere finite, again impossible.
This proves the elimination lemma.

Notice that it is a congruence obstruction: if all primes dividing $P$
occur in the prescribed modulus, there are no congruence solutions at all.
Indeed any residue-vector solution would give an integer
$n=F_{\mathbf d}(\mathbf x)$ satisfying (3.3).

## 4. A uniform quadratic prime-harmonic estimate

The random omission argument needs a **two-sided**, conductor-uniform
estimate, not just fixed-character convergence:

$$
 \sup_{z\geq2}\left|\sum_{p\leq z}\frac{\chi(p)}p\right|
 \ll\log(2q)                                                \tag{4.1}
$$

for every nonprincipal real Dirichlet character presented modulo $q$.
No Siegel estimate is needed. Here are the details of an elementary weak
polynomial lower bound sufficient for (4.1).

For primitive real $\chi$, fixed-character nonvanishing
$L(1,\chi)>0$ follows from the fixed-character prime number theorem
recorded in Ghidelli, Lemma 5.4: partial summation gives convergence of
$\sum_p\chi(p)/p$, hence a finite real logarithm of $L(1,\chi)$.
There is no need for uniform constants in this application.

Let $\zeta=e^{2\pi i/q}$. The Gauss sum has absolute value
$\sqrt q$. The sine Fourier series gives, for odd $\chi$,

$$
 |L(1,\chi)|=\pi q^{-3/2}\left|\sum_{a=1}^q a\chi(a)\right|
 \geq\pi q^{-3/2}.                                        \tag{4.2}
$$

The integer sum is nonzero by nonvanishing. For even $\chi$, set

$$
 U=\prod_{(a,q)=1}(1-\zeta^a)^{\chi(a)}.
$$

This is a positive algebraic unit. Indeed the factors
$(1-\zeta^a)/(1-\zeta)$ and their inverses are algebraic integers
by geometric-sum formulas; the remaining factors cancel since
$\sum_a\chi(a)=0$. Pairing $a$ and $-a$ proves positivity.
Galois automorphisms send $U$ to $U$ or $U^{-1}$, so
$U+U^{-1}$ is an integer. The cosine Fourier series gives
$\sqrt q\,|L(1,\chi)|=|\log U|$. Nonvanishing implies $U\ne1$,
so $U+U^{-1}\geq3$ and

$$
 L(1,\chi)\geq q^{-1/2}\log((3+\sqrt5)/2).
$$

Both parities give $L(1,\chi)\gg q^{-3/2}$.

Periodicity, zero mean, and partial summation give, uniformly for
$1\leq\sigma\leq2$,

$$
 |L(\sigma,\chi)|\ll\log(2q),\qquad
 |L'(\sigma,\chi)|\ll\log^2(2q).
$$

Near 1, the derivative bound preserves half the preceding lower bound.
Outside that short interval use the Euler-factor inequality

$$
 L(\sigma,\chi)\geq\zeta(2\sigma)/\zeta(\sigma)
 \gg\sigma-1.
$$

Together these give

$$
 L(\sigma,\chi)\gg q^{-3/2}\log^{-2}(2q)
 \quad(1<\sigma\leq2).                                    \tag{4.3}
$$


For $z\geq3$, set $\sigma=1+1/\log z$. Chebyshev's elementary
prime estimates show uniformly in the character that

$$
 \sum_{p\leq z}\frac{\chi(p)}p=\log L(\sigma,\chi)+O(1).
                                                               \tag{4.4}
$$

The smoothing difference below $z$ is bounded by
$(\log z)^{-1}\sum_{p\leq z}(\log p)/p=O(1)$; the absolute tail
above $z$ is bounded by a constant times
$\int_1^\infty e^{-u}du/u$; prime powers of exponent at least two
have bounded total. Equations (4.3)--(4.4) prove (4.1). Removing Euler
factors to pass to an imprimitive character costs at most
$\sum_{p\mid q}1/p\ll\log(2q)$. Differences of endpoints give the
same estimate on every prime interval.

The same smoothing calculation with the principal character gives

$$
 \sum_{p\leq z}p^{-1}=\log\log z+O(1).
$$

Using (4.1) for $\chi_{-4}$, we obtain uniformly for $3\leq Y<Z$

$$
 \sum_{\substack{Y<p\leq Z\\p\equiv3\ (4)}}p^{-1}
 =\tfrac12\log(\log Z/\log Y)+O(1).                         \tag{4.5}
$$

A longer proof, including the Gauss-sum identities, is in
`quadratic_prime_bound.md`.

## 5. Gaussian characters: the required uniformity

The supplied Ghidelli paper provides two inputs used here:

* Proposition 5.2 identifies $\phi_t=(t/\cdot)_4$ as an order-dividing-four
  Gaussian Hecke character, with some defining ideal supported on $2t$.
  It identifies the normalized Jacobi character $\mathfrak J_4$, with
  fixed defining ideal $(16)$, and infinity type $\alpha/|\alpha|$.
* Proposition 4.3 gives the exact quartic zero-class character expansion
  written in Section 6 below. Kummer theory in Section 6.2 identifies
  $\phi_t$ as principal precisely when $t\in\mathbb Q(i)^{\times4}$.

The unspecified exponent of a defining ideal in Proposition 5.2 must not
silently be assumed uniform. The following argument supplies that uniformity.
Since $\mathbb Z[i]$ is a PID, a finite Hecke character can be regarded
as a character on the unit group of a residue ring. At an odd prime ideal,
principal units modulo a prime power form an odd-primary group, so an
order-dividing-four character kills them. At $\pi=1+i$, every unit
congruent to 1 modulo $\pi^9$ is a fourth power: Hensel applied at 1
to $T^4-u$ uses $v_\pi(4)=4$ and $v_\pi(u-1)>8$.
This also gives a fourth power in every finite quotient. Thus

$$
 \mathfrak f(\phi_t)\mid
 (1+i)^9\prod_{\substack{\mathfrak p\mid(t)\\\mathfrak p\nmid2}}
 \mathfrak p.                                               \tag{5.1}
$$

If all rational prime divisors of $t$ divide $2R$, a defining ideal
of norm $O(R^2)$ suffices. The same is true for a twist by
$\mathfrak J_4^2$, whose infinity type is 2 and whose fixed conductor
only changes the absolute constant.

Here is the uniform upper bound for the associated $L$-functions.
Let $\psi$ have a defining ideal $\mathfrak m=(\mu)$ of norm
$H$, and infinity type $k=0$ or 2. For $k=0$, assume it is
nonprincipal. Write

$$
 \psi((\alpha))=\eta(\alpha)(\alpha/|\alpha|)^k,
$$

where $\eta$ is a finite residue character, extended by zero on
nonunits. The expression is invariant under Gaussian units. For every
residue class modulo $\mathfrak m$, comparison with the square cells
of $\mu\mathbb Z[i]$ gives

$$
 \sum_{\substack{0<|\alpha|\leq T\\\alpha\equiv b\ (\mathfrak m)}}
 (\alpha/|\alpha|)^k
 =H^{-1}\int_{|z|\leq T}(z/|z|)^k\,dz
       +O_k(T/\sqrt H+1).                                  \tag{5.2}
$$

Boundary cells give the indicated boundary error. Away from the central
cells the angular function has gradient $O_k(1/|z|)$; integrating it
over the disk gives the same error. The central cells contribute $O_k(1)$.
For $k=2$ the integral vanishes. For $k=0$ its coefficient after
summing against $\eta$ vanishes because the finite character is
nonprincipal. Dividing the Gaussian integer sum by four yields

$$
 \sum_{N\mathfrak a\leq x}\psi(\mathfrak a)
 \ll\sqrt{Hx}+H.
$$

Split the Dirichlet series at $H$, and use partial summation for the
tail. The initial absolute sum is $O(\log(2H))$, and the tail is
$O(1)$, uniformly for $1<\sigma\leq2$. Therefore

$$
 |L(\sigma,\psi)|\ll\log(2H).                              \tag{5.3}
$$

The prime-ideal version of the smoothing calculation (4.4) gives

$$
 \sum_{N\mathfrak p\leq z}
       \frac{\Re\psi(\mathfrak p)}{N\mathfrak p}
 \leq\log\log(2H)+O(1).                                    \tag{5.4}
$$

Its constants are absolute for these two fixed infinity types. Chebyshev's
estimates for Gaussian prime ideals follow directly from those for rational
primes. Inert prime ideals have norm $p^2$, so discarding them changes
such a harmonic sum by $O(1)$.

## 6. Local counts and the full quartic trace

For an odd prime prescribe the target $p\pmod{p^2}$. Let
$\rho_{\mathbf d}(p)$ be the number of solutions modulo $p^2$,
divided by $p^6$. If $p\nmid P$, then

$$
 \rho_{\mathbf d}(p)
 =1+A_{\mathbf d}(p)(p^{-1}-p^{-2})-p^{-3},\qquad |A_{\mathbf d}(p)|\leq21.
                                                               \tag{6.1}
$$

Indeed the zero-class count modulo $p$ is
$p^3+A_{\mathbf d}(p)p(p-1)$. All solutions except the zero vector
are nonsingular and have exactly $p^3$ lifts to the specified target
modulo $p^2$. The zero vector has none.

For $p\equiv3\pmod4$, fourth powers and squares have the same
distribution in $\mathbb F_p$. The quadratic Gauss-sum evaluation
therefore gives

$$
 A_{\mathbf d}(p)=\chi_D(p).                                \tag{6.2}
$$

For $p\equiv1\pmod4$, Ghidelli's exact expansion is

$$
\begin{split}
 A_{\mathbf d}(p)={}&\chi_D(p)
 +\frac14\sum_{\sigma\in\mathfrak S_4}
     \chi_4(d_{\sigma(1)}d_{\sigma(2)}
                  d_{\sigma(3)}^3d_{\sigma(4)}^3)\\
 &+\frac12\sum_{\sigma\in\mathfrak S_4}
     \chi_4(-d_{\sigma(1)}^2d_{\sigma(2)}^2
                   d_{\sigma(3)}d_{\sigma(4)}^3)
 +2\Re\bigl(\phi_P^{-1}\mathfrak J_4^2\bigr)(\mathfrak p),
\end{split}                                                 \tag{6.3}
$$

where $\mathfrak p$ is one Gaussian prime above $p$ and
$\chi_4=\chi_{4,\mathfrak p}$. The finite terms after $\chi_D$
are three conjugate pairs and six conjugate pairs. All multiplicities are
positive. Their bounds, together with the last pair, give 21.

A positive rational number is a fourth power in $\mathbb Q(i)$
exactly when it is a rational fourth power. A negative rational number
$-A$, with $A>0$, is a fourth power there exactly when
$A=4t^4$ for rational $t$. To check this, the imaginary part of
$(x+iy)^4$ is $4xy(x^2-y^2)$. Thus a principal character in the
second term of (6.3) forces $P$ square, and a principal character in
the third term is precisely (3.2). The last character has infinity type
2 and is never principal.

Consequently, for every nonexceptional tuple all the finite characters
in this expansion are nonprincipal and $D>1$. Apply (5.4) to the
nine finite Gaussian conjugate pairs and the one infinity-type-two pair.
Combine the quadratic term $\chi_D(p)$ over **all** good rational
primes, using the elementary upper bound $L(\sigma,\chi_D)\ll\log(2D)$.
This last combination is essential: it avoids introducing an inverse
quadratic $L$-function in the full baseline. The result is

$$
 \sum_{\substack{p\leq Z\\p\nmid2P}}
       \frac{A_{\mathbf d}(p)}p
 \leq C\log\log(3R)+C\omega(R)+C.                          \tag{6.4}
$$

Removing additional primes dividing $P$ from an Euler sum costs at
most $C\sum_{p\mid2P}1/p$, explaining the $\omega(R)$ term.

At a bad coefficient prime, the following bound is crucial:

$$
 0\leq\rho_{\mathbf d}(p)\leq4\quad(p\mid P).               \tag{6.5}
$$

Call a coefficient active if it is a unit modulo $p$. If all active
variables vanish modulo $p$, the sum is zero modulo $p^2$, because
inactive canonical coefficients have valuation at least five. Thus these
singular solutions cannot lift to the target $p$. Every other solution
is nonsingular and has $p^3$ lifts. Fixing three variables bounds the
number of solutions modulo $p$ by $4p^3$, using an active variable;
if there is no active variable there are no solutions. This proves (6.5).

At 2 prescribe $8\pmod{16}$, and normalize its solution count by
$16^3$. Its local factor is at most 16. These local factors multiply
by the Chinese remainder theorem.

## 7. The random omission construction

Fix a sufficiently small absolute $\delta>0$. For each positive
squarefree $E>1$, set

$$
 \epsilon_E=\frac{\delta}{16E^2},\qquad
 h(p)=\frac\delta2+\sum_{\substack{E>1\\E\ {
m squarefree}}}
                      \epsilon_E\chi_E(p).                  \tag{7.1}
$$

The series converges uniformly and absolutely,
$\sum_E\epsilon_E<\delta/4$, and
$\sum_E\epsilon_E\log(2E)\ll\delta$. In particular
$\delta/4<h(p)<3\delta/4<1$.

Let $Z\to\infty$ and put

$$
 Y=(\log Z)^{200}.
$$

For sufficiently large $Z$, $3<Y<Z$. Include every odd prime
$p\leq Y$, and every $p\leq Z$ with $p\equiv1\pmod4$.
For each $Y<p\leq Z$, $p\equiv3\pmod4$, independently omit the
prime with probability $h(p)$. For the resulting finite set
$\mathcal Q$, let

$$
 M=16\prod_{p\in\mathcal Q}p^2,
 \qquad a\equiv8\pmod{16},\quad a\equiv p\pmod{p^2}
                   \quad(p\in\mathcal Q).                  \tag{7.2}
$$

The CRT determines $a\pmod M$.

For every fixed positive squarefree $D>1$, (4.1) and (4.5) imply

$$
 -\sum_{\substack{Y<p\leq Z\\p\equiv3\ (4)}}
          \frac{h(p)\chi_D(p)}p
 \leq-\frac{\epsilon_D}{2}\log\frac{\log Z}{\log Y}
          +C\delta\log(2D)+C\delta.                         \tag{7.3}
$$

To verify this, expand (7.1). The $E=D$ term has
$\chi_E(p)\chi_D(p)=1$ off primes dividing $D$, and gives the
negative main term. For $E\ne D$, both the product character and its
twist by $\chi_{-4}$ are nonprincipal, so their window sums are
$O(\log(2DE))$. The same applies to the baseline term
$\delta\chi_D/2$. Absolute convergence justifies summing these bounds
over $E$. The primes dividing $D$ cost
$O(\epsilon_D\log(2D))$. Removing primes dividing $P$ costs at
most $C\delta\omega(R)$.

Let $\rho_{\mathbf d}(a,M)$ denote the full normalized solution
count modulo $M$, namely the number of residue-vector solutions divided
by $M^3$. At an eligible good prime, independence replaces its local
factor by

$$
 h(p)+(1-h(p))\rho_{\mathbf d}(p)
 =1+(1-h(p))\chi_D(p)/p+O(p^{-2}).                          \tag{7.4}
$$

At other good primes (6.1) applies. At bad primes use 4, and at 2 use 16.
The inequality $1+u\leq e^u$, (6.4), and (7.3) give, for each
nonexceptional tuple,

$$
 \mathbb E\rho_{\mathbf d}(a,M)
 \leq C_0^{\omega(R)+1}(\log(3R))^{C_1}R^{C_2\delta}
        \left(\frac{\log Z}{\log Y}\right)^{-\epsilon_D/2}.
                                                               \tag{7.5}
$$

All constants are absolute, independent of the tuple, $Y$, and $Z$.
Errors $O(p^{-2})$ have an absolutely bounded sum. This argument does
not require dividing by a possibly vanishing local factor.

Choose $\delta$ so small that $C_2\delta<1/16$, and absorb the
logarithmic power into, for example, $R^{1/16}$. Equation (2.3) now
provides a summable majorant for
$w(\mathbf d)\mathbb E\rho_{\mathbf d}(a,M)$ over all
nonexceptional tuples. For each such fixed tuple, $\epsilon_D>0$ and
$\log Z/\log Y\to\infty$, so (7.5) tends to zero. Dominated
convergence proves

$$
 \sum_{\mathbf d\ {
m nonexceptional}}
       w(\mathbf d)\mathbb E\rho_{\mathbf d}(a,M)\longrightarrow0.
                                                               \tag{7.6}
$$


For an exceptional tuple with $P^+(R)\leq Y$, the elimination lemma
gives $\rho_{\mathbf d}(a,M)=0$ for every outcome of the random
choices. Every remaining exceptional tuple has $P^+(R)>Y$. Uniformly
over all choices, (6.1), (6.5), and the bound 21 imply

$$
 \rho_{\mathbf d}(a,M)
 \ll 4^{\omega(R)}(\log Z)^{21}.
$$

Indeed an included good-prime factor is at most
$\exp(21/p+O(p^{-2}))$; an omitted one is 1. Equation (2.4) gives

$$
 \sum_{\mathbf d\ {
m exceptional}}
       w(\mathbf d)\mathbb E\rho_{\mathbf d}(a,M)
 \ll (\log Z)^{21}Y^{-1/8}
       =(\log Z)^{-4}\longrightarrow0.                     \tag{7.7}
$$

Combining (7.6)--(7.7), and using Tonelli for nonnegative terms,

$$
 \mathbb E\left[\sum_{\mathbf d\in\mathcal D^4}
             w(\mathbf d)\rho_{\mathbf d}(a,M)\right]
 \longrightarrow0.                                         \tag{7.8}
$$

For each $Z$ there are only finitely many random choices. Thus there
is a deterministic outcome making this entire weighted local sum arbitrarily
small. This handles the infinite coefficient family, not merely a finite
diagonal subsystem.

## 8. From the weighted local sum to actual density

This step is included explicitly to avoid confusing a narrower equation
or a local estimate with the required assertion about $S_4$.

Fix any outcome $(a,M)$ of (7.2). For a fixed tuple $\mathbf d$,
lattice-point counting in the compact region
$\sum d_i t_i^4\leq X$, $t_i\geq0$, in each residue class gives

$$
 \#\{\mathbf x\in\mathbb N^4:F_{\mathbf d}(\mathbf x)\leq X,
                     F_{\mathbf d}(\mathbf x)\equiv a\pmod M\}
 =\frac{VX}{M}w(\mathbf d)\rho_{\mathbf d}(a,M)+o_{M,\mathbf d}(X),
 \quad V=\Gamma(5/4)^4.                                    \tag{8.1}
$$

For completeness, the number in each vector residue class is its region's
volume divided by $M^4$, plus $o(X)$, by ordinary Riemann-sum
approximation of this Jordan-measurable region after dilation by $X^{1/4}$.
The positive-orthant unit $\ell^4$-ball has volume
$\Gamma(5/4)^4/\Gamma(2)=V$; scaling coordinate $i$ by
$d_i^{-1/4}$ multiplies it by $w(\mathbf d)$. Multiplication by
the number $M^3\rho_{\mathbf d}(a,M)$ of allowed vector residues
proves (8.1).

For every $X$, the left side of (8.1), divided by $X$, is at most
$w(\mathbf d)$, by counting in the containing coordinate box.
These weights are summable. Therefore dominated convergence legitimately
sums (8.1) over **all** canonical tuples. The total number of ordered
four-term representations in the progression, divided by $X/M$, tends to

$$
 V\sum_{\mathbf d\in\mathcal D^4}
           w(\mathbf d)\rho_{\mathbf d}(a,M).                \tag{8.2}
$$

By (7.8), choose an outcome for which (8.2) is less than $\varepsilon$.
Distinct represented integers are no more numerous than ordered
representations. Representations with one, two, or three summands account
for only $O(X^{3/4})$ integers by (2.1), and $M$ is now fixed.
This proves (1.1). Taking, for example, $\varepsilon=1/2$, the progression
contains at least $X/(2M)+o(X)$ nonvalues, proving (1.2).

## 9. Failed approaches and calculations retained

### Elementary tuple counting does not settle the problem

For fixed $r$, the ordered tuple count is

$$
 \Gamma(1+1/r)^rW_r^rX+o(X),
$$

by the same finite-coefficient lattice count and summable tails. Dividing by
$r!$ gives the unordered leading constant; tuples with equal summands
are only $O(X^{1-1/r})$. This does not give an $o(X)$ support estimate.
Nor does its constant eventually become less than one: just the Euler factors
at 2 and 3 give

$$
 W_r\geq(1+(r-1)/4)(1+(r-1)/9)\geq r^2/36.
$$

Since $\Gamma(1+1/r)\geq e^{-1}$ and $r!\leq r^r$, the unordered
constant is at least $(r/(36e))^r$, which tends to infinity.

### Simultaneously splitting all quartic coefficients fails

The Fermat quartic has a useful deficit at primes $p\equiv5\pmod8$.
But if the canonical core contains $2^5$, making that coefficient a
fourth power forces 2 to be a fourth power, hence a quadratic residue, and
therefore forces $p\equiv1\pmod8$ among primes $1\pmod4$.
Thus the cubic all-coefficients-splitting construction cannot simply be
copied in degree four.

### A finite quadratic-character mask has a circular tail problem

At primes $3\pmod4$, the trace is $\chi_D(p)$. For finitely many
nontrivial squareclasses one can exclude completely split primes in their
multiquadratic field; every nontrivial character then has negative mean.
However, the saving can be as small as the reciprocal of the size of the
squareclass group. The reciprocal-prime mass needed to suppress the core
then grows with that group, while the crude uncontrolled tail grows
exponentially in the same mass. Choosing the core first does not resolve this
circular dependence. The infinite small omission mask in Section 7 replaces
this with a uniform integrable majorant.

### Eliminating only square determinants is insufficient

The nonsquare determinant tuple $(1,1,1,32)$ has a principal finite
character in the third term of (6.3). A baseline proof that assumes all
nonsquare-determinant tuples have only nonprincipal finite characters is
false. This example is itself excluded by $n\equiv8\pmod{16}$.
The general repair is identity (3.4), which eliminates every principal
third-term character, not just this example.

### Fixed prime-power valuation gaps are not enough

For example, the canonical tuple $(1,1,64,64)$ leads to a positive
square-determinant quadratic form, but its quartic values can exhibit every
valuation class modulo four at 2: the first pair gives valuations 0 or 1,
and the second gives 6 or 7, with fourth-power scaling. Thus one cannot
simply assert that quaternion anisotropy produces a missing valuation class.
The successful obstruction instead prescribes valuation one at every odd
coefficient prime and valuation three at 2, forcing local *isotropy* of
the associated positive square-determinant quadratic form.

### Crude inverse $L$-bounds need a small coefficient

A direct selected-prime Euler product can involve inverse quadratic
$L$-factors with fixed large exponents. Polynomial lower bounds then
produce a coefficient loss too large for the canonical weight. The successful
argument first bounds the complete quartic baseline using only positive
$L$-powers, and introduces inverse-type estimates solely through an
omission probability of size $\delta$. The resulting radical loss is
$R^{C\delta}$, which can be made summable. Neither a uniform Siegel
bound nor an unproved zero-free hypothesis is being substituted here.

### Numerical calculation was diagnostic only

A finite Euler-product computation over primes up to $10^6$ gave
approximately $W_4\approx9.5971$. For the weight restricted to square
determinant products, the local factor is

$$
 \tfrac12\bigl[(1+p^{-5/4}+p^{-3/2}+p^{-7/4})^4
              +(1-p^{-5/4}+p^{-3/2}-p^{-7/4})^4\bigr].
$$

The corresponding truncated product was about 142.515, giving an unordered
weighted volume about 4.008. These are truncated numerical values, not
certified infinite-product values and not used in the proof. They discouraged
the idea that simply retaining all square-determinant tuples would have
total representation constant less than one.

## 10. Remaining uncertainties and continuation points

The density-zero question is untouched by the quartic complement argument.
Making one progression very sparse, with its modulus changing with
$\varepsilon$, does not imply global density zero. It is equally
compatible with positive density of $S_4$. The same distinction applies
to the supplied cubic theorem.

No unconditional positive-density construction was found. The exact
reduction in Section 2 shows that such a construction would yield positive
upper density for some fixed positive diagonal form in the critical number
of variables. Conditional six-variable cubic energy bounds from the supplied
Wang paper were not treated as unconditional results, and no statement about
the narrower powerful equation $a+b=c$ was promoted to a statement about
arbitrary target integers in $S_r$.

For $r\geq5$, the quartic mechanism does not automatically extend.
The useful zero-class local fluctuations are no longer of divergent
reciprocal-prime size, and the four-dimensional positive quadratic norm-form
obstruction is special. No replacement for either ingredient was established.

For further checking, the most sensitive parts of the quartic proof are:

1. preserving the full-prime quadratic term when deriving (6.4);
2. eliminating both kinds of principal finite-character pattern, not just
   square determinants;
3. keeping the conductor estimate (5.1) explicit and uniform;
4. using a two-sided bound in (4.1) for the omission cross terms;
5. retaining the growing support cutoff $Y$, so the exceptional infinite
   tail is bounded by (7.7), rather than silently discarding it;
6. fixing the final modulus before using the counting limit (8.2).

Each of these has a stated argument above.

Supporting files created during this investigation, none of which is
retained here:

* `positive_density_reduction.md` — the general exact density-zero reduction;
* `quartic_elimination.md` — the complete quadratic/quaternion elimination;
* `quadratic_prime_bound.md` — detailed uniform quadratic harmonic estimates;
* `quadratic_harmonic_bound.md` — an independently written version of that
  lemma;
* `quartic_analytic.md` — the uniform Gaussian and randomized local estimates.

The sources actually needed by the quartic proof are Ghidelli's supplied
paper (the exact character formula, the Hecke-character correspondence,
Kummer theory, and fixed-character nonvanishing) and Voight's supplied chapter
(quaternion reciprocity). The canonical decomposition and lattice framework
are also developed explicitly above, consistent with the supplied Beyer de
Ryke paper. No purported later research note is an input.
