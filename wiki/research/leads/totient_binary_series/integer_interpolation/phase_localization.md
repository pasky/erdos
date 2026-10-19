---
name: research/leads/totient_binary_series/integer_interpolation/phase_localization
title: Arithmetic Localization of Totient Phases
desc: |
  Multiplicative relations inside the short window localize every small
  phase near a dyadic phase with a controlled odd numerator, yielding
  a subsequence equivalence and a finite exact separation test.
problems:
- 249
research_state: ready
review_status: unreviewed
created: 2026-09-17T16:45:12Z
updated: 2026-10-08T01:29:59Z
---

***

The [[research/leads/totient_binary_series/integer_interpolation/phase_transference|phase
comparison]] equates a small odd-kernel cost with a large phase error
on a specified family. Its reverse implications from irrationality on
other supports do not, by themselves, give a reverse implication on
$[J,2J]$. Here the identity $\varphi(3k)=2\varphi(2k)$ for odd
$k$ coprime to $3$ supplies the missing arithmetic on that short support.

The result is an equivalence along a subsequence of powers of two,
and an exact finite sufficient test for phase separation. It proves
no unbounded sequence of successful tests and does not resolve
[[problems/irrationality/E0249/_index|Problem 249]]. These are author-recorded,
unreviewed arguments. The eventual structural assertions use the
fixed-modulus prime number theorem at the disclosed standing below.

## Notation and the structural hypotheses

Let $J=2^m\ge4$, use all indices $J\le n\le2J$, and put

$$
H=3J+2,\quad a_t=\varphi(t)/2\quad(t\ge3),\quad
A_n=\Phi_n/2,\quad V_n=U_J(n)/2,\quad w_n=n+J+2.
$$

Here $\Phi_n$, $U_J(n)$ and the complete positive tail $T_n$ are
defined on the
[[research/leads/totient_binary_series/integer_interpolation/two_depth_carries|two-depth
page]]. In particular

$$
2^JT_n=U_J(n)+T_{n+J},\qquad
0<T_{n+J}\le w_n,\qquad 0<V_n<2^{J-1}(n+2).
\tag{1}
$$

Write $\|x\|=\operatorname{dist}(x,\mathbb Z)$, and let
$\epsilon_J=\min_\theta\max_{J\le n\le2J}
\|\theta V_n-A_n/2\|/w_n$. This minimum is attained, as on the
phase comparison page. Define the finite set

$$
\mathcal K_J=\{k:\ k\text{ odd},\ 3\nmid k,\ J<2k<3k\le2J\},
\quad D_k=a_{3k+J}-2a_{2k+J}.
$$

The two structural hypotheses used below are

$$
\gcd_{J<t\le2J}a_t=1,\qquad
G:=\gcd_{k\in\mathcal K_J}D_k>0\ \hbox{and odd}.
\tag{2}
$$

The gcd is taken positive, ignoring zero entries; (2) requires a
nonzero entry. Set $D_*=\max_{k\in\mathcal K_J}|D_k|$, so
$1\le G\le D_*\le H$. Also
$a_*:=\max_{J<t\le2J}a_t\ge a_{2J}=J/2$, hence $H/a_*\le8$.

**Lemma 1.** Conditions (2) hold for every sufficiently large power
of two $J$. They also give the odd feasibility and row-rank hypotheses
of Theorem 4 on the phase comparison page.

*Proof.* The integer $a_{2J}=J/2$ is a power of two. A prime
$p\in(J,2J)$ with $p\equiv3\pmod4$ supplies the odd value
$a_p=(p-1)/2$, proving the first gcd assertion.
For the second, choose a prime

$$
5J/2<P<3J,\qquad P\equiv3\pmod4,\qquad P\equiv J+3\pmod9.
$$

These congruences specify a reduced class modulo $36$, since $J$ is
coprime to $3$. Then $k=(P-J)/3$ is odd, is $1$ modulo $3$, and
belongs to $\mathcal K_J$. Its $D_k=a_P-2a_{2k+J}$ is odd.

Both prime choices follow separately from the fixed-modulus theorem
$\pi(x;q,r)\sim x/(\varphi(q)\log x)$ for fixed coprime $q,r$.
The counts in these intervals are asymptotic to $J/(2\log J)$ and
$J/(24\log J)$, respectively. Only six reduced classes modulo $36$
arise, so their thresholds can be made common. No growing modulus or
simultaneous prime pair is used.

More generally, (2) implies that some $D_k$ is odd and some $a_t$
is odd. For such $k$, since it is odd and $3\nmid k$,
$a_{3k}=2a_{2k}$ is even, while $a_{3k+J}$ is odd. Together with
an odd $a_t$ from the first gcd assertion this gives an odd minor of
the two rows $(a_t)$ and $(a_{t+J})$. Thus they have rank two.
For $n\ge4$, $A_n\equiv a_n\pmod2$ and
$V_n\equiv a_{n+J}\pmod2$. The same two columns have an odd
minor and include an odd $V_n$. Dividing their scalar cross-product
by their odd gcd produces an odd kernel vector. $\square$

The external prime-theorem statement was inspected in [NIST DLMF
§27.11](https://dlmf.nist.gov/27.11), closing paragraph, version 1.2.8
(2026-09-15), and the introductory fixed-$q$ formula in [Tao's 2009
exposition](https://terrytao.wordpress.com/2009/09/24/the-prime-number-theorem-in-arithmetic-progressions-and-dueling-conspiracies/).
Its analytic proof is neither reconstructed nor independently reviewed here.
This use changes the fixed moduli from the earlier $20$ to $4$ and $36$; it
makes no uniformity assertion for unbounded moduli. At an individual $J$, (2)
can instead be checked directly without this asymptotic input.

## Localizing a small phase

**Proposition 2.** Assume (2). Suppose $\delta>0$, $18\delta H^3<1$,
and some real $\theta$ satisfies

$$
\|\theta V_n-A_n/2\|\le\delta w_n
\qquad(J\le n\le2J).
\tag{3}
$$

Then there is a nonzero odd integer $q$ with

$$
|q|\le26\delta2^JH,\qquad
\left\|\frac{qV_n}{2^{J+1}}-\frac{A_n}{2}\right\|
\le31\delta H w_n\quad(J\le n\le2J).
\tag{4}
$$

There is also an integer $p$ such that

$$
\left\|q2^{J-2}S\right\|\le38\delta H^2 2^{-J},\qquad
\left|S-\frac{p}{q2^{J-2}}\right|
\le\frac{152\delta H^2}{|q|2^{2J}}.
\tag{5}
$$

*Proof.* Choose integers $m_n$ so that the errors in (3) have
absolute value at most $\delta w_n$. The recurrences give, for
$J<t\le2J$,

$$
\theta(a_{t+J}-2^Ja_t)-a_t/2-\ell_t=e_t,
\quad \ell_t=m_t-2m_{t-1}\in\mathbb Z,
\quad |e_t|\le3\delta H.
\tag{6}
$$

Subtract twice the relation at $2k$ from the one at $3k$.
The terms involving $a_t$ cancel, so integers $h_k$ satisfy
$|\theta D_k-h_k|\le9\delta H$.
If $s$ realizes $|D_s|=D_*$, every integer
$D_kh_s-D_sh_k$ has absolute value at most
$18\delta HD_*<1$, and is zero. Thus $h_k/D_k$ has one common
value on the nonzero entries. Because all $h_k$ are integers and
their corresponding $D_k$ have gcd $G$, this value is $r/G$ for
some integer $r$. Consequently

$$
|\theta-r/G|\le E,\qquad E=9\delta H/D_*.
\tag{7}
$$

This integer-minor argument includes the small-error threshold;
a gcd assertion alone would not give a quantitative approximation.

Put $\lambda=2^{J+1}G\theta$. Multiplying (6) by $2G$ and using
(7) yields integers

$$
q_t=2r a_{t+J}-Ga_t-2G\ell_t,
\qquad |\lambda a_t-q_t|\le\eta,
\qquad \eta=GH(E+6\delta).
\tag{8}
$$

For any $t,u$, the integer $a_uq_t-a_tq_u$ has absolute value
at most $H\eta$. Moreover

$$
H\eta=9\delta(G/D_*)H^3+6\delta GH^2
\le15\delta H^3<1.
$$

These integers vanish. The first gcd assertion in (2) now gives an
integer $Q$ with $q_t=Qa_t$ for every $t$. Hence
$|\lambda-Q|\le\eta/a_*$. Since $q_t\equiv Ga_t\pmod2$
and some $a_t$ is odd, $Q$ is odd. Set
$q=Q-2^{J+1}r$, also odd. Then

$$
|q|\le2^{J+1}GE+\eta/a_*
\le18\delta2^JH+120\delta H
\le26\delta2^JH,
$$

where $J\ge4$, $G\le D_*\le H$ and $H/a_*\le8$ were used.

The dyadic phase $q/2^{J+1}$ differs from $G\theta-r$ by at most
$\eta/(a_*2^{J+1})$. Because $G$ is odd, multiplying (3) by $G$
preserves the half-integer target modulo integers. Equation (1) gives

$$
\left\|\frac{qV_n}{2^{J+1}}-\frac{A_n}{2}\right\|
\le\left(G\delta+\frac{\eta}{4a_*}\right)w_n
\le(13G\delta+2GE)w_n\le31\delta H w_n.
$$

This proves (4), including its parity requirement. Oddness of $G$
cannot be dropped from this step.

For any odd integer $q$, the exact complete-tail identity (1) implies

$$
\frac{qV_n}{2^{J+1}}-\frac{A_n}{2}
\equiv q2^{n-2}S-\frac{qT_{n+J}}{2^{J+2}}\pmod1.
\tag{9}
$$

The omitted algebraic term is $(q+1)\Phi_n/4\in\mathbb Z$.
Thus (1) and (4) give
$\|q2^{n-2}S\|\le38\delta H^2$ throughout the window.
This bound is less than $1/3$, since $18\delta H^3<1$ and
$H\ge14$. Choose the nearest-integer residuals $f_n$ for these
quantities. Each $f_{n+1}-2f_n$ is an integer of absolute value
less than $1$, hence zero. Therefore
$|f_J|=2^{-J}|f_{2J}|\le38\delta H^2 2^{-J}$.
Dividing by $|q|2^{J-2}$ proves (5). $\square$

## The subsequence equivalence on the short support

**Theorem 3.** Along the powers of two $J$, the following statements
are equivalent:

1. $S$ is irrational.
2. $\limsup_{J\to\infty,\ J=2^m}\epsilon_J2^J=\infty$.
3. On some unbounded subsequence of those $J$, there are odd kernel
   vectors supported on $[J,2J]$ with cost $o(2^J)$.

*Proof.* By Lemma 1 and Corollary 5 of the phase comparison page,
2 implies 3. The complete-tail criterion on the two-depth page,
with lower cutoff $B=J\to\infty$, shows that 3 implies 1.

For the remaining implication, suppose 2 fails. Choose a fixed
$M\ge1$ such that $\epsilon_J\le M2^{-J}$ for every sufficiently
large power of two. Apply Proposition 2 with $\delta=M2^{-J}$,
which eventually meets its threshold, and write

$$
r_J=\frac{p_J}{q_J2^{J-2}},\qquad
0<|q_J|\le26MH_J,\qquad
|S-r_J|\le\frac{152MH_J^2}{|q_J|2^{3J}},
\quad H_J=3J+2.
$$

If $r_J\ne r_{2J}$, their common dyadic factors give
$|r_J-r_{2J}|\ge1/(|q_Jq_{2J}|2^{2J-2})$.
Multiplying the sum of their approximation errors by that denominator
would imply

$$
1\le988M^2\left(
\frac{H_J^2H_{2J}}{2^J}
+\frac{H_JH_{2J}^2}{2^{4J}}\right),
\tag{10}
$$

which is false for every sufficiently large $J$. Thus consecutive
powers eventually give the same rational number. Their errors tend
to zero, forcing $S$ to equal that rational number. This proves the
contrapositive of 1 implying 2. $\square$

The dyadic factors in the denominator comparison are essential:
using the product of the two denominators loses a factor $2^J$.
This proves a subsequence assertion, not
$\epsilon_J2^J\to\infty$ along all powers of two and not an
all-depth polynomial cost bound. The earlier wider-support shadow
construction still has its original scope; it was not restricted to
the short support to obtain this theorem.

## A finite exact sufficient test

Fix an integer $M\ge1$ and a power of two $J\ge4$ satisfying (2)
and $18MH^3<2^J$. If, for each positive odd integer $q\le26MH$,
there is an $n\in[J,2J]$ such that

$$
\operatorname{dist}\left(qU_J(n)-2^J\Phi_n,
                         2^{J+2}\mathbb Z\right)
>124MH(n+J+2),
\tag{11}
$$

then $\epsilon_J>M2^{-J}$.
Indeed otherwise Proposition 2 supplies an odd $q$ in this range
satisfying the opposite inequality at every index, by multiplying
(4) by $2^{J+2}$. Negative $q$ gives the same phase distances as
positive $q$ because $A_n$ is integral, so positive $q$ suffice.

This is a finite test on exact integers using totients only through
$3J$, with $O(MJ)$ candidate numerators and $O(J)$ coordinates for
each. All the infinite-tail reasoning is in Proposition 2, not in
a truncation of (11). A failure of this sufficient test says nothing
decisive about the optimal phase error. Successful tests for a finite
set of parameters prove no asymptotic claim. An unbounded sequence of
successful pairs with $M\to\infty$ would establish Theorem 3(2);
no such sequence is proved here.

For a small structural check, at $J=32$ one has
$\mathcal K_J=\{17,19\}$, $D_{17}=41-2\cdot10=21$ and
$D_{19}=44-2\cdot12=20$, hence $G=1$. Also
$a_{64}=16$ and $a_{43}=21$ give the other gcd in (2).
These exposed computations check the index and parity conventions;
they are not a phase certificate or evidence for the required growth.

The new finite test offers a concrete way to examine the arithmetic
left by the phase comparison. Proving its success in a growing family,
or obtaining separation by a different arithmetic argument, remains
open. Neither this equivalence nor its connection with runs of binary
digits rules out Fourier, lattice, signed-multiplier or other methods.
