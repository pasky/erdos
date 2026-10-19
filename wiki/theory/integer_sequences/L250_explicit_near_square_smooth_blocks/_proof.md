---
name: theory/integer_sequences/L250_explicit_near_square_smooth_blocks/_proof
title: Proof of the explicit near-square construction
desc: |
  Scale m by c so that m/c is at most K^2/16, take the next square q^2 above
  m/c, and subtract the largest admissible t^2; the three factors stay below
  K and the overshoot c(2t+1) stays below 3K/4.
tags: []
sources:
- theory/integer_sequences/L250_explicit_near_square_smooth_blocks/_index
created: 2026-10-15T22:27:51Z
updated: 2026-10-15T22:27:51Z
---

# Proof of the explicit near-square construction

***

This proves the whole statement of
[[theory/integer_sequences/L250_explicit_near_square_smooth_blocks/_index|L250]].
The construction is Erdős and Sárközy's (1979, section 3); the constants are
chosen here so that every step holds for all $K\ge64$ and all $m\ge0$.

**Lemma 1 (adjustment).** Let $c\ge1$, $q\ge1$ and $m\ge0$ be integers with
$D:=cq^2-m>0$, and let $t$ be the largest integer $t\ge0$ with $ct^2<D$.
Then $N:=c(q-t)(q+t)$ satisfies

$$
0<N-m\le c(2t+1),\qquad 0\le t<q,\qquad t<\sqrt{D/c}.
$$

*Proof.* The value $t=0$ satisfies $c\cdot0^2<D$, and $ct^2<D$ bounds $t$,
so $t$ exists. Then $N-m=cq^2-ct^2-m=D-ct^2>0$. By the maximality of $t$,
$c(t+1)^2\ge D$, so $N-m\le c(t+1)^2-ct^2=c(2t+1)$. Finally
$ct^2<D\le cq^2$ because $m\ge0$, so $t<q$, and $t<\sqrt{D/c}$. $\square$

**The construction.** Let $K\ge64$ and $0\le m\le K^{5/2}/128$ be integers.
Put

$$
c:=\max\left(1,\left\lceil\frac{16m}{K^2}\right\rceil\right),\qquad
T:=\frac mc,\qquad q:=\lfloor\sqrt T\rfloor+1,\qquad D:=cq^2-m,
$$

and let $t$ and $N=c(q-t)(q+t)$ be as in Lemma 1, once $D>0$ is checked.

1. $T\le K^2/16$. If $16m/K^2\le1$ then $c=1$ and $T=m\le K^2/16$;
   otherwise $c=\lceil16m/K^2\rceil\ge16m/K^2$.
2. $1\le c\le\sqrt K/4$. Indeed
   $c\le16m/K^2+1\le16K^{1/2}/128+1=\sqrt K/8+1\le\sqrt K/4$, the last
   step because $\sqrt K\ge8$.
3. $0<D/c\le2q-1$. Since $q-1=\lfloor\sqrt T\rfloor$, we have
   $(q-1)^2\le T<q^2$, and $D/c=q^2-T$ lies in $(0,q^2-(q-1)^2]=(0,2q-1]$.
   So Lemma 1 applies.
4. $q\le K/4+1$ and $t<\sqrt K$. By step 1, $q\le\sqrt T+1\le K/4+1$. Then
   $D/c\le2q-1\le K/2+1\le K$, and Lemma 1 gives $t<\sqrt{D/c}\le\sqrt K$.
5. $1\le q-t\le q+t\le K$. Lemma 1 gives $t<q$. Next
   $q+t<K/4+1+\sqrt K\le K$, since $\tfrac34K-\sqrt K-1$ equals $39$ at
   $K=64$ and increases with $K$.
6. $0<N-m<3K/4$. Lemma 1 and step 4 give
   $N-m\le c(2t+1)<c(2\sqrt K+1)\le3c\sqrt K$, and step 2 gives
   $3c\sqrt K\le3K/4$.

So $N$ lies in $(m,m+K]$ and is the product of the three positive integers
$c$, $q-t$ and $q+t$, each at most $K$ (step 2 gives $c\le\sqrt K/4\le K$).
Every prime factor of $N$ divides one of the three factors, so it is at most
$K$. The case $m=0$ is included: there $c=1$, $q=1$, $t=0$ and $N=1$, which
has no prime factor at all. This proves the first sentence of the statement.

**The bound for $k(n)$.** Let $n\ge1$ and
$K:=\max(64,\lceil(128n)^{2/5}\rceil)$, so that $K^{5/2}\ge128n$, that is,
$n\le K^{5/2}/128$. Suppose that $k(n)\ge K$: some integers $0\le m\le n$
and $k\ge K$ have each of $m+1,\ldots,m+k$ divisible by a prime greater than
$k$. Then each of $m+1,\ldots,m+K$ has a prime factor greater than $k\ge K$,
so $(m,m+K]$ contains no integer whose prime factors are all at most $K$.
This contradicts the first part, because $0\le m\le n\le K^{5/2}/128$.
Hence $k(n)\le K-1<\max(64,(128n)^{2/5})$, using $\lceil y\rceil-1<y$. The
argument uses only $m\ge0$, so it applies unchanged when $m$ is required to
be positive. $\square$

**Remark (Erdős's notation).** Let $n_k$ be the least $n\ge0$ such that each
of $n+1,\ldots,n+k$ has a prime factor greater than $k$. The first part shows
that no $n\le k^{5/2}/128$ qualifies when $k\ge64$, so $n_k>k^{5/2}/128$ for
every $k\ge64$; Erdős and Sárközy state $n_k>k^{5/2}/16$ for $k>k_0$, with
$k_0$ unspecified.
