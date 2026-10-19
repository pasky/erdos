---
name: theory/additive_bases/L239_consecutive_unique_differences/_proof
title: Proof of the consecutive unique-difference bound
desc: |
  Exact counts for overlapping and adjacent intervals give a small discrete
  energy. Averaging translates of the resulting sequences bounds their
  squared norm and gives the m^(5/3) estimate without a diameter bound.
tags: []
sources: []
created: 2026-10-15T20:36:53Z
updated: 2026-10-15T20:36:53Z
---

# Proof of the consecutive unique-difference bound

***

Let $B\subset\mathbb Z$ have $m\ge2$ elements and suppose that every
integer $1\le d\le L$ has exactly one representation $d=b'-b$ with
$b,b'\in B$. If $L=0$, the bound is immediate. Otherwise put
$u=\lfloor(L+1)/2\rfloor\ge1$, so $2u-1\le L\le2u$.

For every integer $j$ define

$$
F(j)=|B\cap[j,j+u-1]|,
\qquad
r(d)=|\{(b,b')\in B^2:b'-b=d\}|.
$$

All sums below have finite support. Counting the intervals that contain
two specified points gives

$$
\sum_j F(j)^2
 =mu+2\sum_{d=1}^{u-1}(u-d)r(d)
 =u(m+u-1).                                           \tag{1}
$$

For a point $b$ in $[j,j+u-1]$ and a point $b'$ in the adjacent interval
$[j+u,j+2u-1]$, the positive difference $d=b'-b$ lies between $1$ and
$2u-1$. There are $u-|u-d|$ choices of $j$ for this pair. Thus

$$
\sum_j F(j)F(j+u)
 =\sum_{d=1}^{2u-1}(u-|u-d|)r(d)=u^2.                 \tag{2}
$$

The only representation counts used in (1) and (2) are $r(d)=1$ for
$1\le d\le2u-1$. Translation of the index $j$ then gives

$$
\sum_j\bigl(F(j+u)-F(j)\bigr)^2=2u(m-1).             \tag{3}
$$

For each $a\in\{0,\ldots,u-1\}$ let $f_a(n)=F(a+nu)$ for $n\in\mathbb Z$.
These values count $B$ in a partition of the integers into disjoint
intervals, so $f_a\ge0$ and $\sum_n f_a(n)=m$. Write

$$
T_a=\sum_n f_a(n)^2,\qquad
E_a=\sum_n(f_a(n+1)-f_a(n))^2.
$$

The bijection $j=a+nu$ and (1), (3) yield

$$
\frac1u\sum_a T_a=m+u-1,\qquad
\frac1u\sum_a E_a=2(m-1).                            \tag{4}
$$

Fix a positive integer $k$ and average $k$ translates of each sequence:

$$
g_a(n)=\frac1k\sum_{i=0}^{k-1}f_a(n+i).
$$

Nonnegativity and the mass identity give $0\le g_a(n)\le m/k$ and
$\sum_n g_a(n)=m$. Therefore
$\sum_n g_a(n)^2\le m^2/k$. Telescoping consecutive translates and
applying the triangle inequality in $\ell^2(\mathbb Z)$ give

$$
\|f_a-g_a\|_2
 \le\frac1k\sum_{i=0}^{k-1}\|f_a-f_a(\,\cdot+i)\|_2
 \le\frac{k-1}{2}\sqrt{E_a}.
$$

Now use the triangle inequality for arrays indexed by $(a,n)$, with
squared norm $u^{-1}\sum_{a,n}|\cdot|^2$. Equation (4) gives, for every
positive integer $k$,

$$
\sqrt{m+u-1}
 \le\frac{m}{\sqrt k}+(k-1)\sqrt{\frac{m-1}{2}}.      \tag{5}
$$

Take $k=\lceil m^{1/3}\rceil$. Since $k\ge m^{1/3}$ and
$k-1\le m^{1/3}$, the right side is at most
$(1+1/\sqrt2)m^{5/6}$. Squaring and using $L\le2u$ proves

$$
L\le2u
 \le2(1+1/\sqrt2)^2m^{5/3}-2m+2
 =(3+2\sqrt2)m^{5/3}-2m+2.
$$

This proves the claim. No step bounds the support diameter or uses
uniqueness for any difference larger than $L$. $\square$
