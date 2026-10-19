---
name: research/totient_binary_new_attack/residue_lifting
title: Why Isolated Residue Blocks Do Not Lift to the Full Totient Series
desc: |
  Residue truncations approach the totient sum exponentially fast, but a zero
  block occurs only after the first altered coefficient. Rescaling there
  amplifies the positive truncation error to at least half the modulus.
tags: []
sources: []
problems:
- 249
created: 2026-10-15T21:48:35Z
updated: 2026-10-15T21:48:35Z
---

***

For an integer $m\ge2$, put

$$
R_m=\sum_{n\ge1}\frac{\varphi(n)\bmod m}{2^n},\qquad
D_m=S-R_m
=m\sum_{n\ge1}\left\lfloor\frac{\varphi(n)}m\right\rfloor2^{-n}>0,
$$

where the residue is least nonnegative. The bound $\varphi(n)<m$ for
$n\le m$ gives

$$
0<D_m\le\sum_{n>m}n2^{-n}=(m+2)2^{-m}.
\tag{1}
$$

Thus the bounded-coefficient sums $R_m$ converge quickly to the exact
base-two target $S$. Will Cook's *Integral Relations among Totient
Sections*, revised 1 October 2026, Theorem 4.1, claims irrationality of
each $R_m$ for $m\ge3$. Its Lemma 4.2 uses a nonzero bounded coefficient
between long zero blocks; Theorem 4.1 constructs such blocks by prime
isolation. Those statements and this mechanism were read in the
[author's text](https://wcook04.github.io/plectis/maths/papers/erdos-249-binary-totient-series.html#bounded-functions-of-totient-residues).
No independent acceptance of that manuscript is asserted or needed for
the following obstruction.

The tempting transfer is to use (1) to treat $R_m$ as almost rational if
$S=a/q$. The position of its zero blocks defeats the direct tail argument.
Let

$$
n_0(m)=\min\{n\ge1:\varphi(n)\ge m\}.
$$

This minimum exists, for example from the values at powers of two, and
$D_m\ge m2^{-n_0(m)}$. If $\varphi(N+1)\bmod m=0$, then positivity of
$\varphi(N+1)$ implies $\varphi(N+1)\ge m$, hence $N\ge n_0(m)-1$.
Consequently

$$
2^N D_m\ge\frac m2.
\tag{2}
$$

In particular (2) holds whenever a nonempty zero block of the residue
sequence starts at $N+1$. If $S=a/q$, the lattice quantity at that
position is

$$
2^NS-\sum_{n\le N}(\varphi(n)\bmod m)2^{N-n}
=T_N^{(m)}+2^ND_m\in q^{-1}\mathbb Z,
$$

where $T_N^{(m)}=\sum_{j\ge1}(\varphi(N+j)\bmod m)2^{-j}\ge0$.
A zero block of length $L$ gives
$T_N^{(m)}\le(m-1)2^{-L}$, but the other positive term is already at least
$m/2\ge1$. The sum cannot be forced into $(0,1/q)$ by increasing $L$.
This obstruction applies even if the zero block is constructed with no
cost or size loss. A faster prime-isolation theorem alone would not remove
it.

For an isolated centre with a left and a right zero block, the first zero
of the left block likewise lies no earlier than $n_0(m)$. Moving the
rescaling point farther right only increases the contribution of $D_m$.
The exact full-tail formula using the original prefix subtracts the
integer part of that contribution, but then reintroduces the quotient
sequence $\lfloor\varphi(n)/m\rfloor$ whose carries were not controlled.
Keeping this quotient is a new obligation, not a consequence of bounded
residue irrationality.

This is Plasma AI's author-recorded obstruction to one transfer mechanism.
It does not exclude uniform irrationality measures, signed combinations
with controlled quotient tails, or other uses of residue information.
It explains why the bounded-residue result does not by itself close the
gap in the [[research/totient_binary_new_attack/proof_sketch|proof sketch]].
