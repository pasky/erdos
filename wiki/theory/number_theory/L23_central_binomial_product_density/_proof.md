---
name: theory/number_theory/L23_central_binomial_product_density/_proof
title: Proof of the shifted-product density comparison
desc: |
  An exact valuation identity outside finitely many primes and an elementary
  count of base-p digits prove the fixed-length density comparison.
tags: []
sources: []
created: 2026-10-14T10:23:26Z
updated: 2026-10-14T10:23:26Z
---

# Proof of the shifted-product density comparison

***

This proves the statement of
[[theory/number_theory/L23_central_binomial_product_density/_index|L23]].
All parameters denoted $k,p,r,H,L$ below are fixed before the counting limit
unless a later limit is explicitly taken. The proof is author-recorded.

## Valuations at a fixed prime

For every prime $p$ and nonnegative integers $r,H$,

$$
\big|\{1\le n\le x:v_p(B(n+r))\le H\}\big|=o(x).                 \tag{1}
$$

Indeed, Legendre's formula gives

$$
v_p(B(t))=
\sum_{a\ge1}\left(\left\lfloor\frac{2t}{p^a}\right\rfloor
-2\left\lfloor\frac{t}{p^a}\right\rfloor\right),
$$

the number of carries in the base-$p$ addition $t+t$. Each digit of $t$
at least $\lceil p/2\rceil$ forces a carry, regardless of an incoming carry.
Consequently $v_p(B(t))\le H$ implies at most $H$ such digits. We do not
identify the valuation with the number of those digits: other digits can
propagate carries.

Put $h=\lceil p/2\rceil<p$. Among all strings of $d$ base-$p$ digits,
including leading zeroes, the number with at most $H$ digits at least $h$
is at most

$$
\sum_{j=0}^{\min(H,d)}\binom dj(p-h)^j h^{d-j}
=O_{p,H}(d^Hh^d).
$$

Choose $d=\lfloor\log_p(x+r)\rfloor+1$, so that
$x+r<p^d\le p(x+r)$. This bounds the count in (1) by

$$
O_{p,H,r}\big((\log x)^H x^{\log_p h}\big)=o(x).
$$

The same estimate covers $p=2$, when $h=1$.

For a fixed prime $p$, each of the following conditions holds outside a set
of density zero:

$$
v_p(B(n))\ge2v_p(Q_k(n)),\qquad
v_p(B(n+k))\ge v_p(Q_k(n)).                                    \tag{2}
$$

To see this, fix a nonnegative integer $L$. Except on a union of $k$
residue classes modulo $p^{L+1}$, each $v_p(n+i)$ is at most $L$.
The upper density of that union is at most $k/p^{L+1}$, and outside it
$v_p(Q_k(n))\le kL$. By (1), the integers with $v_p(B(n))<2kL$ or
$v_p(B(n+k))<kL$ have density zero. Thus the upper density of the
exceptional set for either condition in (2) is at most $k/p^{L+1}$.
First take $x\to\infty$ with $L$ fixed, and then take $L\to\infty$.
The resulting upper density is zero. This proves (2).

## The exact comparison at larger primes

Define

$$
O_k(n)=\prod_{i=1}^k(2n+2i-1).
$$

Cancellation of factorials gives the identity

$$
B(n+k)=B(n)\frac{2^kO_k(n)}{Q_k(n)}.                           \tag{3}
$$

If a prime $p>2k$ divides $Q_k(n)$, it divides some $n+i$.
It cannot also divide any $2n+2j-1$, because it would then divide the
nonzero integer $2(j-i)-1$, whose absolute value is at most $2k-1$.
Therefore $v_p(O_k(n))=0$, and (3) gives

$$
v_p(B(n+k))=v_p(B(n))-v_p(Q_k(n)).
$$

It follows that

$$
v_p(B(n+k))\ge v_p(Q_k(n))
\quad\Longleftrightarrow\quad
v_p(B(n))\ge2v_p(Q_k(n)).                                     \tag{4}
$$

If $p>2k$ does not divide $Q_k(n)$, both conditions in (4) hold
automatically. Thus (4) holds for every prime $p>2k$ and every $n\ge1$.

## Completion

Outside the finite union of the density-zero exceptions in (2), taken over
primes $p\le2k$, the local conditions defining both $S_k$ and $T_k$
hold at every such prime. At all larger primes their local conditions
are equivalent by (4). The global divisibility conditions therefore agree
outside a set of density zero, proving L23.

In particular,
$\big||S_k\cap[1,x]|-|T_k\cap[1,x]|\big|=o(x)$.
Translation by the fixed $k$ changes either counting function by $O_k(1)$,
which proves the density consequences stated on the claim card. Nothing in
this estimate prevents either solution set, or their difference, from being
an infinite set of density zero.
