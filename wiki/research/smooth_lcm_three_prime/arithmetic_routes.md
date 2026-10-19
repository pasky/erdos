---
name: research/smooth_lcm_three_prime/arithmetic_routes
title: Arithmetic tails and fixed-base recoding for three primes
desc: |
  Exact block numerators and quadratic tail bounds for every three-prime
  set, with the obstruction to finite tail states and to a direct integral
  polynomial-growth fixed-base recoding.
tags: []
sources: []
created: 2026-10-15T16:35:43Z
updated: 2026-10-15T16:35:43Z
---

***

The [[research/smooth_lcm_three_prime/_index|three-prime sketch]] also admits
an arithmetic attack through a chain of integer denominators. The derivations
here retain every smooth integer and apply to every $P=\{p,q,r\}$ with
$p<q<r$. They are author-recorded by Plasma AI, without independent review.
They do not prove irrationality. Closely related tail and recoding obstructions
for $\{2,3,5\}$ appear in Will Cook's
[running-lcm manuscript](https://wcook04.github.io/plectis/maths/papers/erdos269-running-lcm-reasoning-surface--complete.html),
Sections 5.5 and 12.2, revised 5 October 2026, accessed 2026-10-15. The
arguments below make the dependence on an arbitrary ordered prime triple
explicit; no novelty is asserted for the mechanism.

## An exact integer block expansion

Put $\theta_q=\log p/\log q$, $\theta_r=\log p/\log r$, and

$$
H_n=D(p^n)=p^nq^{\lfloor n\theta_q\rfloor}
                    r^{\lfloor n\theta_r\rfloor},
\qquad b_n=H_{n+1}/H_n.
$$

Then $H_0=1$,

$$
b_n\in\{p,pq,pr,pqr\},\qquad
\frac{p^{3n}}{qr}<H_n\le p^{3n}.
$$

The radix assertion follows from $0<\theta_q,\theta_r<1$. The size bounds
follow by replacing each of the two floors by the number itself or by one
less than it, and using $q^{\theta_q}=r^{\theta_r}=p$.

Define the integer block numerator

$$
c_n=\sum_{\substack{m\ \mathrm{smooth}\\p^n\le m<p^{n+1}}}
          \frac{H_{n+1}}{D(m)}.
$$

Every denominator in the block divides $H_{n+1}$. In fact each quotient is
one of $p,pq,pr,pqr$: the exponent of $p$ in $D(m)$ is exactly $n$, and
each other exponent increases by at most one during the block. Consequently

$$
S_P=\sum_{n\ge0}\frac{c_n}{H_{n+1}},
\qquad pN_n\le c_n\le pqrN_n,
$$

where the number of smooth integers in the block is exactly

$$
N_n=\#\{(a,b)\in\mathbb Z_{\ge0}^2:
                   a\log q+b\log r<(n+1)\log p\}.
$$

Indeed, each $q^ar^b<p^{n+1}$ can be multiplied by exactly one
nonnegative power of $p$ to enter $[p^n,p^{n+1})$. A pair outside this
triangle contributes nothing. Thus block numerators preserve the original
multiplicities rather than counting just the prime-power jumps.

For example, at $P=\{2,3,5\}$ the first two numerators are $c_0=2$ and
$c_1=12/2+12/6=8$, with $H_1=2$ and $H_2=12$. At $P=\{3,5,7\}$ they are
$c_0=3$ and $c_1=315/3+315/15+315/105=129$. The right endpoint of each
block belongs to the next block.

## Why normalized tails are not finite states

Let

$$
R_n=H_n\sum_{\substack{m\ \mathrm{smooth}\\m\ge p^n}}\frac1{D(m)}.
$$

Splitting off the first block gives the exact recurrence

$$
R_0=S_P,\qquad R_{n+1}=b_nR_n-c_n.
$$

Both $c_n$ and $R_n$ grow quadratically. Here are explicit bounds requiring
no lattice-discrepancy theorem. Pairs with
$a\le\lfloor(n+1)\theta_q/3\rfloor$ and
$b\le\lfloor(n+1)\theta_r/3\rfloor$ lie in the triangle, while every pair
there has $a<(n+1)\theta_q$ and $b<(n+1)\theta_r$. Therefore

$$
\frac{\theta_q\theta_r}{9}(n+1)^2\le N_n\le(n+2)^2.
$$

On the first block $D(m)\le qrH_n$, giving $R_n\ge N_n/(qr)$. On block
$n+j$, one has $H_n/D(m)\le H_n/H_{n+j}\le qr\,p^{-3j}$. Hence, with
$t=p^{-3}$,

$$
\frac{\theta_q\theta_r}{9qr}(n+1)^2
 \le R_n\le qr(n+1)^2\frac{4-3t+t^2}{(1-t)^3}.
$$

For the upper bound use $N_{n+j}\le(n+j+2)^2\le(n+1)^2(j+2)^2$ and sum
$\sum_{j\ge0}(j+2)^2t^j=(4-3t+t^2)/(1-t)^3$. In particular, $R_n$ is
unbounded; rationality would not put these tails into a finite set.

More precisely, if $S_P=A/D$ is rational, write $D=D_PB$ with all prime
factors of $D_P$ in $P$ and $\gcd(B,pqr)=1$. Eventually $D_P\mid H_n$.
Every earlier summand's denominator divides $H_n$, so then $BR_n$ is an
integer. Conversely, $BR_n\in\mathbb Z$ for any positive integer $B$ at
any index implies that $S_P$ is rational, by adding back the finite prefix.
This is an equivalent integrality question, not a solution of it.

Positivity, the actual radices, and quadratic growth alone are insufficient.
For the same $b_n,H_n$, set

$$
K_n=(n+3)^2,\qquad \widetilde c_n=b_nK_n-K_{n+1}.
$$

Since $b_n\ge2$,
$\widetilde c_n\ge n^2+4n+2>0$, and these integer numerators have quadratic
growth. Nevertheless telescoping gives

$$
\sum_{n\ge0}\frac{\widetilde c_n}{H_{n+1}}
 =K_0-\lim_{N\to\infty}\frac{K_N}{H_N}=9.
$$

These are different numerators from the smooth-count numerators $c_n$.
Any irrationality argument using the recurrence must exploit that difference.

## A direct fixed-base substitution loses a necessary hypothesis

For a fixed integer $g\ge2$, the termwise recoding is

$$
S_P=\sum_{n\ge0}\frac{e_n(g)}{g^{n+1}},\qquad
e_n(g)=\frac{c_ng^{n+1}}{H_{n+1}}.
$$

No such $g$ makes the coefficients both eventually integral and of polynomial
growth. If $pqr\mid g$, then $g\ge pqr>p^3$, and

$$
e_n(g)\ge p\left(\frac g{p^3}\right)^{n+1},
$$

which grows exponentially. If some $u\in P$ does not divide $g$, cancellation
of its power in $H_{n+1}$ can come only from $c_n$. The reduced denominator
therefore satisfies

$$
\operatorname{den}(e_n(g))
 \ge\frac{u^{\lfloor(n+1)\log_u p\rfloor}}{c_n}
 >\frac{p^{n+1}}{u\,pqr\,(n+2)^2}\longrightarrow\infty.
$$

In particular, the base $g=p^3$ matches the exponential size of $H_n$ and
gives polynomial-size rational coefficients, but their denominators grow
exponentially. The base $g=pqr$ gives integer coefficients of exponential
size. Regrouping or carrying could change the coefficients; this obstruction
concerns the displayed termwise substitution only.

Allowing a fixed algebraic base $\beta$ with $|\beta|>1$ does not repair this
particular substitution. If $c_n\beta^{n+1}/H_{n+1}$ is an integer at two
consecutive sufficiently large indices, their ratio forces $\beta\in\mathbb Q$.
Write $\beta=a/b$ in lowest terms with $b>0$. If $b>1$, the reduced denominator
of the $n$th coefficient is at least $b^{n+1}/c_n$, which tends to infinity.
Thus eventual integrality forces an integer base; negative integer bases have
the same absolute-value bounds as the positive ones. There is no fixed
algebraic base giving this termwise recoding both eventually integral
coefficients and polynomial growth.

Luca, Ouaknine and Worrell's
[arXiv:2412.07908v2](https://arxiv.org/html/2412.07908v2), Definition 4 and
Theorem 5, give a fixed-base transcendence criterion for polynomially growing
integer sequences with specified sparse shifted differences and uniform
variation bounds. Its statement was inspected; its proof is not imported.
The substitutions above fail the integrality or growth requirement before
the sparse-difference requirement is considered. Finitely many possible
radices do not supply a finite coefficient alphabet either.

## The remaining arithmetic step

This route needs a property of the actual triangle counts and their weights
that contradicts the possible integer carries $BR_n$ for every denominator
multiplier $B$. One concrete possibility is a family of integer linear
combinations of shifted tails whose values are nonzero but tend to zero;
under rationality their denominators would be uniformly bounded. Such a
construction must control the boundary strips of the counting triangles as
well as the changes in $H_n$. A quadratic leading term or a small change in
the floor phases does not establish that control. No such family is supplied
here. Alternatively, a value theorem for the actual variable denominator
chain would need its own non-cancellation and height estimates. These are
open obligations, distinct from the finite cone-partition obstruction.
