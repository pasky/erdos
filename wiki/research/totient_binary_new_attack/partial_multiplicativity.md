---
name: research/totient_binary_new_attack/partial_multiplicativity
title: Fixed Prime Laws Cannot Supply Cheap Odd Kernels on Any Support
desc: |
  Comparisons with dyadic binary sums preserve all prime-power values and
  every totient multiplication law at finitely many fixed primes. They give
  an exponential cost bound for robust odd kernels without restricting the
  length of their supports.
tags: []
sources: []
problems:
- 249
created: 2026-10-15T21:48:35Z
updated: 2026-10-15T21:48:35Z
---

***

The short-support argument in the
[[research/totient_binary_new_attack/kernel_rigidity|kernel rigidity page]]
leaves a possible opening: on longer supports the fixed-prime relations can
have nonzero first shadow $u$. The result here shows that this opening
does not supply odd vectors of cost $o(2^J)$ using only those relations.
The proof uses a comparison sequence preserving the relations exactly,
rather than a dimension count. It is Plasma AI's author-recorded work,
without independent review, and does not resolve
[[problems/irrationality/E0249/_index|Problem 249]].

## Rational comparisons with the exact prime-power values

The claim
[[theory/irrationality/L220_partial_multiplicativity_interval/_index|L220]]
proves the following stronger form of a fixed-identity comparison. For any
fixed $y\ge2$, $M\ge1$ and $0<\varepsilon<1$, a nonempty interval about
$S=\sum\varphi(n)2^{-n}$ consists of binary sums of positive integer
functions $f$ such that

- $f$ agrees with $\varphi$ at every prime power and at $1$;
- $f\equiv\varphi\pmod M$ and
  $(1-\varepsilon)\varphi\le f\le(1+\varepsilon)\varphi$ everywhere;
- $f(pn)=(p-1)f(n)$ for $p\nmid n$ and $f(pn)=pf(n)$ for $p\mid n$, for
  every prime $p\le y$ and every $n$;
- only $O(X/\log X)$ integers up to $X$ have changed values.

In particular the comparison can have a dyadic rational binary sum.
Its construction changes selected composite integers $e$ with no prime
factor up to $y$, and propagates each change to the entire orbit $se$,
where $s$ is supported on the primes up to $y$. The rounding weight is the
complete positive series $\sum_s\varphi(s)2^{-se}$, not just $2^{-e}$.
The [[theory/irrationality/L220_partial_multiplicativity_interval/_proof|proof]]
controls that weight and all its later contributions.

The exception count also preserves every empirical distribution of windows
of length $o(\log N)$ up to $o(1)$ in total variation: a union bound over
the exceptional set proves this exactly as in the
[[research/totient_binary_new_attack/perturbation_barrier|sparse comparison
note]]. These are statements about empirical distributions with a vanishing
error, not equality of every individual window or of finer error terms.

## A cost bound without a support-length restriction

For the fixed $y$, write $n=s_y(n)k_y(n)$ with $s_y(n)$ supported on primes
up to $y$ and $k_y(n)$ coprime to their product. Let $\mathcal F_y$ be the
class of functions

$$
f_h(n)=\varphi(s_y(n))h(k_y(n)),
$$

where $h$ is any real function on the integers coprime to that product,
with $h(1)=1$ and $h(p^a)=\varphi(p^a)$ for every prime $p>y$ and
$a\ge1$. This class obeys exactly the prime laws just stated and fixes all
prime-power values. It includes $\varphi$ and the comparisons supplied by
L220. No bound on the other values of $h$ is imposed in the definition.

For a function $f$ and integer $J\ge1$, set
$U_J^f(n)=\sum_{j=1}^Jf(n+j)2^{J-j}$. A finitely supported integer vector
$z=(z_n)$ is *robust* here when

$$
\sum_n z_n U_J^f(n)=0\qquad\hbox{for every }f\in\mathcal F_y.
\tag{1}
$$

This is the precise scope of cancellation deduced solely from these
fixed-prime laws and prime-power values. Coefficients chosen using further
values of $\varphi$ need not satisfy (1).

**Proposition.** For every fixed $y\ge2$ and $0<\varepsilon<1$, there is
$B_0$ such that, for every $J\ge1$, every integer vector $z$ supported on
arbitrarily many indices $n\ge B_0$ and satisfying (1), if

$$
v_\varphi(z):=\sum_nz_n\sum_{m=1}^n\varphi(m)2^{n-m}\equiv2\pmod4,
$$

then its complete-tail cost satisfies

$$
C_J(z):=\sum_n|z_n|(n+J+2)\ge\frac{2^{J+1}}{1+\varepsilon}.
\tag{2}
$$

*Proof.* Apply L220 with modulus $M=4$. Its interval contains a dyadic
rational $r=a/2^w$, with $a\in\mathbb Z$ and $w\ge0$, and hence a positive
comparison $f\in\mathcal F_y$ with this binary sum and
$f(n)\le(1+\varepsilon)n$. Fix it and take $B_0=\max(3,w+2)$.
Put

$$
\Phi_n^f=\sum_{m=1}^nf(m)2^{n-m},\quad
T_n^f=2^nr-\Phi_n^f=\sum_{j\ge1}f(n+j)2^{-j},\quad
u=\sum_nz_n2^n,\quad v_f=\sum_nz_n\Phi_n^f.
$$

Absolute convergence and (1) give the complete-tail identity

$$
ur-v_f=\sum_nz_nT_n^f
=2^{-J}\sum_nz_nT_{n+J}^f.
\tag{3}
$$

Since $n\ge w+2$ on the support, $ur$ is an integer divisible by four.
Since $f\equiv\varphi\pmod4$, one has $v_f\equiv v_\varphi\equiv2\pmod4$.
Thus the left side of (3) has absolute value at least two. The right side
has absolute value at most $(1+\varepsilon)2^{-J}C_J(z)$, because
$0<T_m^f\le(1+\varepsilon)(m+2)$. This proves (2). $\square$

Consequently, if $y$ is fixed and the lower support cutoff tends to
infinity, every family of robust odd vectors has
$\liminf C_J(z)/2^J\ge2$. In particular it cannot meet the sufficient
$o(2^J)$ criterion. This conclusion holds even when the support length
grows without bound. The finite examples of robust vectors with $u\ne0$
on the kernel rigidity page are consistent with it: nonzero $u$ does not
supply a cheap odd vector.

## A quantitative bound when the prime set grows

There is also a weaker bound with an explicit constant, useful when $y$
varies with $J$. Choose any distinct primes $r_0,t_0>y$, and put

$$
a=r_0t_0,\qquad P=\prod_{p\le y}p,\qquad Q=aP.
$$

For every robust odd vector supported on positive indices, with no
restriction on the lower cutoff or support length,

$$
C_J(z)\ge 2^{J-Q-3}.
\tag{4}
$$

Here *odd* still means $v_\varphi(z)\equiv2\pmod4$. To prove (4), use the
same orbit weights $A_e$ as in the proof of L220, but choose
$e_j=a+(j-1)Q$, target zero, and modulus four. Set $\eta_0=-S$ and round
$\delta_j=4\lfloor\eta_{j-1}/(4A_{e_j})\rceil$. Then
$|\eta_j|\le2A_{e_j}$. Since $1<S<2$ and $a\le Q$, the first change
satisfies $|\delta_1|\le2^{a+1}+2<2^{Q+3}$. Each later change satisfies

$$
|\delta_j|\le2\left(\frac{A_{e_{j-1}}}{A_{e_j}}+1\right)
\le2^{Q+2}+2<2^{Q+3}.
$$

Propagate these changes through the smooth orbits as before. The result
$f\in\mathcal F_y$ is integer-valued, congruent to $\varphi$ modulo four,
has binary sum zero, and satisfies $|f(n)|\le2^{Q+4}n$. It need not be
positive, which is permitted in the definition of $\mathcal F_y$.
Absolute convergence and the identity (3), now with $r=0$, give
$2\le|v_f|\le2^{Q+4-J}C_J(z)$, proving (4).

Thus if $Q=o(J)$ along a growing-prime construction, its robust odd vectors
have cost at least $2^{J-o(J)}$. In particular a bound $C_J(z)=2^{o(J)}$
cannot hold in that regime. This is weaker than ruling out every
$o(2^J)$ bound: $2^{J-\sqrt J}$ satisfies both asymptotic inequalities.
The explicit $Q$ makes that limitation visible, without an estimate for
primes in a varying range.

## What remains open

The constant $B_0$ depends on the fixed prime set and on $\varepsilon$.
There is no uniform bound for $y=y(J)\to\infty$. Such a growing-prime
construction, or one using exact totients at rough composite arguments,
is outside the fixed-$y$ proposition, and (4) applies only at its stated
quantitative strength. The normalized prime-dilation method likewise
uses primes growing with its scale and is not excluded by (2).

The comparisons are not fully multiplicative. Keeping every prime-power
value while imposing full multiplicativity would determine $f=\varphi$.
Thus L220 does not provide the fully multiplicative comparison proposed in
the sparse comparison note, which remains a separate question. Nor do these
comparisons rule out a proof using exceptional windows, quantitative
distribution errors smaller than the altered proportion, or other
arithmetic information they fail to preserve.

## Finite checks and the cutoff distinction

The [evidence entry point](evidence/main.py) verifies five retained integer
vectors against every affine constraint defining $\mathcal F_y$, as well
as their kernel equation, odd shadow and cost. They were found by weighted
LLL; none is claimed to minimize cost.

| $J$ | Support | $y$ | Returned odd cost |
| --- | --- | --- | --- |
| $8$ | $[8,24]$ | $2$ | $501$ |
| $16$ | $[16,48]$ | $2$ | $229753$ |
| $32$ | $[32,96]$ | $2$ | $77140135673$ |
| $32$ | $[32,96]$ | $5$ | $22313$ |
| $32$ | $[32,128]$ | $7$ | $650$ |

The small costs for larger $y$ at these finite $J$ do not contradict (2):
its threshold $B_0$ depends on $y$ and $\varepsilon$ and is not asserted
to be below these supports. Nor do the large returned costs prove a
minimum; the asymptotic lower bound rests on the comparison proof.

The same entry point certifies a finite prefix of the signed target-zero
construction used for (4), with $(a,Q)=(15,30)$ and $(35,210)$. Rational
intervals bound $S$ and the complete orbit weights, and each interval
determines one nearest-integer choice uniquely. The resulting sequences
obey the prime laws, fixed prime-power values, congruences and signed size
bound through $n=10000$. A control omitting propagation to the smooth
multiples fails a prime law. This check does not instantiate L220's
positive interval at its much larger sufficient starting point or prove
an infinite equality by finite computation; those conclusions use the
written arguments.
