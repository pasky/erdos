---
name: research/erdos_940/cubic_split_prime_counts
title: Split prime factors on typical cubic outputs
desc: A normal-order theorem prevents retaining positive input mass by restricting the special cubic to bounded split-prime complexity.
tags: []
sources: []
created: 2026-09-22T23:49:00Z
updated: 2026-09-22T23:56:58Z
---


# Split prime factors on typical cubic outputs

***

## Statement and scope

Put $F=x^3+2y^3+4z^3$, and define

$$
\Omega(n)=\#\{p\parallel n:\ p\equiv1\pmod3,\
                                  2\text{ is a cube modulo }p\}.
$$

For uniform $\mathbf x\in[1,N]^3\cap\mathbb Z^3$,

$$
\frac{\Omega(F(\mathbf x))}{\log\log N}
\longrightarrow\frac16
\quad\text{in probability}.                           \tag{1}
$$

The proof below uses Chebotarev for the fixed splitting field of
$T^3-2$, the Hasse bound for an elliptic curve, and elementary
residue-box counting.

This is an arithmetic statistic on inputs, not a bound for
representation multiplicity. It arose in an attempted secant-orbit
descent: deleting outputs with more than a fixed number of these
prime factors cannot retain positive input mass.

## First and second moments

Let $\mathcal P$ denote the displayed prime set. These are
exactly the completely split primes of the degree-six splitting
field of $T^3-2$. Chebotarev gives

$$
\sum_{\substack{p\le Z\\p\in\mathcal P}}\frac1p
=\frac16\log\log Z+O(1).
$$

At each such prime, scaling the coordinates identifies the
projective curve $F=0$ with the Fermat cubic. The Hasse bound gives

$$
\beta_p:=p^{-3}\#\{\mathbf u\bmod p:F(\mathbf u)=0\}
=p^{-1}+O(p^{-3/2}).
$$

For $d=p$ or $pq$ with distinct primes in $\mathcal P$, CRT and
counting residue classes in the box imply

$$
\Pr(d\mid F(\mathbf x))
=\prod_{p\mid d}\beta_p+
O\!\left(N^{-1}+dN^{-2}+d^2N^{-3}\right).              \tag{2}
$$

For the error, there are $O(d^2)$ root classes modulo $d$,
and each class has
$(N/d)^3+O((N/d)^2+N/d+1)$ representatives.

Take $Z=N^{1/8}$ and put

$$
T=\sum_{\substack{p\le Z\\p\in\mathcal P}}
       \mathbf1_{p\mid F(\mathbf x)}.
$$

The errors in (2), summed over single primes or pairs, tend to
zero. Since $\sum_p(\beta_p-p^{-1})$ and $\sum_p\beta_p^2$
converge, it follows that

$$
\mathbb ET=\frac16\log\log N+O(1),\qquad
\operatorname{Var}T=\frac16\log\log N+O(1).            \tag{3}
$$


## Exact valuations and the large primes

The only singular zero of $F$ modulo these primes is the origin.
Every nonsingular zero has $p^2$ lifts to a zero modulo $p^2$;
the origin has $p^3$ such lifts. Consequently

$$
\#\{\mathbf u\bmod p^2:F(\mathbf u)=0\}\ll p^4.
$$

Using the same box estimate with modulus $p^2$ gives

$$
\mathbb E
\sum_{\substack{p\le Z\\p\in\mathcal P}}
       \mathbf1_{p^2\mid F(\mathbf x)}
\ll \sum_p p^{-2}
\;+\;\frac ZN+\frac{Z^3}{N^2}+\frac{Z^5}{N^3}
 =O(1).                                             \tag{4}
$$

Also $F(\mathbf x)\le7N^3$, so the number of distinct prime
divisors greater than $Z$ is bounded by
$\log(7N^3)/\log Z=O(1)$. Subtract (4) from the small-prime
count and use (3), Chebyshev's inequality, and Markov's
inequality. This proves (1).

## Exact limitation for the orbit approach

For every fixed $K$, restricting to $\Omega(F(\mathbf x))\le K$
retains $o(N^3)$ inputs. More generally, convergence (1) persists
after conditioning on any sequence of subsets of the root box
with a fixed positive lower proportion. This includes the
[established positive-mass cube-free restriction](cubefree_cubic_values.md);
it would also include any positive-mass squarefree restriction.

Thus an orbit argument cannot simply discard all outputs of
unbounded split-prime complexity. This statement does not
assert that each prime yields a small integral partner, that
different local classes lift simultaneously to rational points,
or that any such lifts have height $O(n^{1/3})$. No global
generator count or integer multiplicity bound was proved.
The unresolved step is height-sensitive control of the integral
representations, not the normal-order calculation above.
