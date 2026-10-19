---
name: theory/number_theory/L105_totient_inverse_chain_cofactors/_proof
title: The affine block identity and the small-cofactor obstruction
desc: |
  Compose the exact inverse maps for fixed cofactors, linearize one block
  at its negative fixed point, and compare 2-adic valuations. Necessary
  prime-residue conditions force a cofactor sequence bounded by 9 to
  become constant.
created: 2026-10-15T05:54:00Z
updated: 2026-10-15T05:54:00Z
---

***

We prove
[[theory/number_theory/L105_totient_inverse_chain_cofactors/_index|L105]].
All integers in a backward chain below are odd. The chain is strictly
increasing, so after its first term every term is composite: a prime is
a fixed point of $T(n)=\varphi(n)+1$.

## The cofactor map

Write an inverse step as $m\leftarrow n=aq$, where $q$ is prime and
$\gcd(a,q)=1$. Put $d=\varphi(a)$. Then

$$
m-1=d(q-1),\qquad
q=\frac{m+d-1}{d},\qquad
n=f_a(m):=\frac{a(m+d-1)}d.                         \tag{1}
$$

If an infinite chain has bounded cofactors
$a_i=m_i/P^+(m_i)$, then its largest primes tend to infinity. Eventually
they exceed every cofactor, so (1) applies at every subsequent step.
The cofactors are odd and at least $3$; hence $d$ is even and $a>d$.

## Repetition of a block

For a block $a_1,\ldots,a_r$ with $d_j=\varphi(a_j)$, put
$A_0=D_0=1$, $B_0=0$, and recursively

$$
A_j=a_jA_{j-1},\qquad D_j=d_jD_{j-1},\qquad
B_j=a_jB_{j-1}+a_j(d_j-1)D_{j-1}.
$$

Induction in (1) gives the block map

$$
F(t)=\frac{At+B}{D},\qquad
A=A_r,\quad D=D_r,\quad B=B_r>0.
$$

Here $A$ is odd, $D$ is even, and $A>D$. For
$J(t)=(A-D)t+B$ the exact identity is

$$
J(F(t))=\frac AD J(t),\qquad
J(F^k(t))=\frac{A^k}{D^k}J(t).                    \tag{2}
$$

For a positive integer $t$, $J(t)$ is a positive integer. If $F^k(t)$ is
an integer, (2) implies that $D^k$ divides $A^kJ(t)$. Taking the exponent
of $2$ and using that $A$ is odd gives

$$
k\,v_2(D)\le v_2(J(t)).                          \tag{3}
$$

Thus a fixed block can repeat only finitely many times from a fixed
positive integer. An eventually periodic cofactor sequence would be
bounded, so (1) would hold beyond some point and its repeating block would
contradict (3). This proves the first assertion.

For the special cofactor $a=3$, (1) reads $f_3(t)=3(t+1)/2$, and (2)
simplifies to

$$
f_3^k(t)+3=\frac{3^k(t+3)}{2^k}.                  \tag{4}
$$

If the endpoint is odd, its sum with $3$ is even. Consequently an odd
chain of $k$ such steps satisfies $k\le v_2(t+3)-1$. Arbitrarily large
values of this bound as $t$ varies do not supply an infinite chain from
any fixed $t$.

## Cofactors at most 9

Suppose for contradiction that an infinite chain eventually has
$a_i\le9$. Its cofactors then belong to $\{3,5,7,9\}$, and its largest
primes eventually exceed $9$. Consider consecutive cofactors $a,b$,
and let $r\mid a$ be prime. The intermediate node $m$ is divisible by
$r$. The next node is $bq$ for a prime $q>9$, so (1) gives

$$
-1\equiv\varphi(b)(q-1)\pmod r.                 \tag{5}
$$

If $\varphi(b)\equiv0\pmod r$, this is impossible. If
$\varphi(b)\equiv1\pmod r$, it forces $q\equiv0\pmod r$, also impossible
since $q>9\ge r$. Thus for each $r\mid a$ the value $\varphi(b)$ must be
neither $0$ nor $1$ modulo $r$. Since
$(\varphi(3),\varphi(5),\varphi(7),\varphi(9))=(2,4,6,6)$, the necessary
transition table is

| Current cofactor $a$ | Possible next cofactors $b$ under (5) |
| --- | --- |
| $3$ | $3$ |
| $5$ | $3,5$ |
| $7$ | $3,5,7,9$ |
| $9$ | $3$ |

This is only a necessary table, which suffices for the exclusion. A path
that leaves $7$ cannot return to $7$; a path that leaves $5$ cannot return
to $5$; and $9$ must be followed by $3$, which cannot be left. Every
infinite path in the table is therefore eventually constant, contradicting
the first assertion. Hence $a_i\ge11$ infinitely often.

## The remaining scope

Necessary residue conditions alone do not extend this argument to every
bounded cofactor set. For example the cofactors $7$ and $11$ can each
follow the other under (5): $\varphi(11)=10$ is neither $0$ nor $1$
modulo $7$, and $\varphi(7)=6$ is neither $0$ nor $1$ modulo $11$.
Self-transitions also survive this test. Periodic words are excluded by
(3), but an arbitrary nonperiodic word need not repeat one fixed block
consecutively. No bound for such words, and no construction realizing one
as an infinite chain of primes, follows from the table or (3).
