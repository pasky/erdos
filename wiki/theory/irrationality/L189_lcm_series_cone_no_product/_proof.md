---
name: theory/irrationality/L189_lcm_series_cone_no_product/_proof
title: Proof that the expanded running-lcm series has no product decomposition
desc: |
  A product decomposition would split the recession cone along rational
  subspaces; its irrational facets admit no such split for three primes.
tags: []
sources:
- theory/irrationality/L189_lcm_series_cone_no_product/_index
created: 2026-10-15T15:50:35Z
updated: 2026-10-15T15:50:35Z
---

***

This proves the entire statement of
[[theory/irrationality/L189_lcm_series_cone_no_product/_index|L189]] at
author-recorded tier 0. Write $V=\mathbb R^P\times\mathbb R^P$ with
coordinates $(m,k)$, put $n=2\lvert P\rvert=\dim V$, and write
$\langle m,L\rangle=\sum_{v\in P}m_vL_v$. The numbers $L_v$ ($v\in P$) are
linearly independent over $\mathbb Q$: a relation with integer coefficients
would equate two products of powers of distinct primes.

## The recession cone

Let

$$
C=\bigl\{(m,k)\in V:\ m_v\ge0\ (v\in P),
  \ \ell_u(m,k)\le0\ (u\in P)\bigr\},
\qquad
\ell_u(m,k)=\langle m,L\rangle-k_uL_u.
$$

For a nonempty closed convex set $K$ write $\operatorname{rec}K$ for its
recession cone, the set of $d$ with $x+td\in K$ for all $x\in K$ and $t\ge0$.
Recall that $K_1\subset K_2$ implies
$\operatorname{rec}K_1\subset\operatorname{rec}K_2$ for nonempty closed convex
sets. Let $\overline\Omega$ be the closure of the convex hull of $\Omega$. We
show $\operatorname{rec}\overline\Omega=C$.

Every integer point of $C$ lies in $\Omega$: from $m\ge0$ and
$\langle m,L\rangle\le k_uL_u$ one gets $k_u\ge0$ and
$\langle m,L\rangle<(k_u+1)L_u$. The cone $C$ has nonempty interior; it
contains the point with $m_v=1$ and $k_u=2\langle\mathbf 1,L\rangle/L_u$ in its
interior. Every rational point $x$ of the interior of $C$ has an integer
multiple $Nx$ in $C\cap\mathbb Z^n$, and $x$ lies on the segment from $0$ to
$Nx$, so $x$ lies in the convex hull of $C\cap\mathbb Z^n$. Since these points
are dense in $C$, we get $C\subset\overline\Omega$, hence
$C=\operatorname{rec}C\subset\operatorname{rec}\overline\Omega$. Conversely,
$\Omega$ lies in the closed convex set
$\{m\ge0,\ \langle m,L\rangle\le(k_u+1)L_u\ (u\in P)\}$, whose recession cone
is $C$, so $\operatorname{rec}\overline\Omega\subset C$.

## A product decomposition splits the cone

Suppose $\Omega=T(\Omega_1\times\Omega_2)$ as in the statement. Then
$d_1+d_2=n$, and $T$ extends to a linear isomorphism
$T:\mathbb R^{d_1}\times\mathbb R^{d_2}\to V$. Convex hulls and closures
commute with products and with $T$, so
$\overline\Omega=T(\overline{\Omega_1}\times\overline{\Omega_2})$, where
$\overline{\Omega_i}$ is the closed convex hull of $\Omega_i$. The recession
cone of a product of nonempty closed convex sets is the product of their
recession cones. Hence

$$
C=C_1\oplus C_2,\qquad
C_1=T\bigl(\operatorname{rec}\overline{\Omega_1}\times\{0\}\bigr)\subset W_1,
\quad
C_2=T\bigl(\{0\}\times\operatorname{rec}\overline{\Omega_2}\bigr)\subset W_2,
$$

where $W_1=T(\mathbb R^{d_1}\times\{0\})$ and $W_2=T(\{0\}\times\mathbb
R^{d_2})$. These are nonzero complementary subspaces of $V$. Each is rational,
that is, spanned by vectors with rational coordinates, because it is spanned by
images under $T$ of integer unit vectors. Since $C$ has nonempty interior,
$C_1$ spans $W_1$ and $C_2$ spans $W_2$.

## Facets of a split cone

Let $\ell$ be a linear form with $\ell\le0$ on $C$ such that
$F=C\cap\{\ell=0\}$ has dimension $n-1$. We show that $\ell$ vanishes on $W_1$
or on $W_2$. Write $\ell_1$ and $\ell_2$ for the restrictions of $\ell$ to
$W_1$ and $W_2$. Since $0$ lies in both $C_1$ and $C_2$, we have $C_1\subset C$
and $C_2\subset C$, so $\ell_i\le0$ on $C_i$. For $x=x_1+x_2$ with $x_i\in C_i$
the two terms of $\ell(x)=\ell_1(x_1)+\ell_2(x_2)$ are nonpositive, so
$\ell(x)=0$ exactly when both vanish. Thus $F=F_1\oplus F_2$ with
$F_i=C_i\cap\{\ell_i=0\}$, and the dimension of $F$ is the sum of the
dimensions of $F_1$ and $F_2$. If $\ell_1\ne0$, then $F_1$ lies in the
hyperplane $\{\ell_1=0\}$ of $W_1$; likewise for $\ell_2$. If both were
nonzero, $F$ would have dimension at most $n-2$. Hence $\ell_1=0$ or
$\ell_2=0$.

## The irrational facets

Fix $u\in P$. The set $C\cap\{\ell_u=0\}$ has dimension $n-1$: the point
$x^{(u)}$ with $m_v=1$ for all $v$, $k_u=\langle\mathbf 1,L\rangle/L_u$ and
$k_v=2\langle\mathbf 1,L\rangle/L_v$ for $v\ne u$ satisfies $\ell_u=0$ and
every other defining inequality of $C$ strictly, so a neighbourhood of
$x^{(u)}$ in the hyperplane $\{\ell_u=0\}$ lies in $C$. By the previous
section, $\ell_u$ vanishes on $W_1$ or on $W_2$.

A rational subspace $W$ contained in the kernel of $\ell_u$ is spanned by
rational vectors $(m,k)$ with
$(m_u-k_u)L_u+\sum_{v\ne u}m_vL_v=0$. Linear independence over $\mathbb Q$
gives $m_v=0$ for $v\ne u$ and $m_u=k_u$. Hence

$$
W\subset R_u=\{(m,k)\in V:\ m_v=0\ (v\ne u),\ m_u=k_u\}.
$$

## Conclusion

Suppose first that $\ell_u$ vanishes on $W_2$ and $\ell_w$ vanishes on $W_1$
for some distinct $u,w\in P$. Then $W_2\subset R_u$ and $W_1\subset R_w$, so
$V=W_1+W_2\subset R_u+R_w$. Since $\lvert P\rvert\ge3$ there is a prime
$x\in P$ other than $u$ and $w$, and every vector of $R_u+R_w$ has $m_x=0$, a
contradiction.

Otherwise, since every $\ell_u$ vanishes on $W_1$ or on $W_2$ and $P$ has at
least two elements, all the forms $\ell_u$ vanish on the same subspace, say on
$W_2$. Then $W_2\subset\bigcap_{u\in P}R_u$. A vector of this intersection has
$m_v=0$ for every $v$, since each $v$ differs from some $u\in P$; then
$k_u=m_u=0$ for every $u$. So $W_2=\{0\}$, contradicting $d_2\ge1$. The case of
$W_1$ is symmetric. Hence no decomposition $\Omega=T(\Omega_1\times\Omega_2)$
exists.

For two primes the argument stops at the first case: $R_p+R_q=V$, and the
decomposition described on the claim page realizes $W_1=R_q$ and $W_2=R_p$.
