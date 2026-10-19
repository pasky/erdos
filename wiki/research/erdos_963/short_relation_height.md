---
name: research/erdos_963/short_relation_height
title: 'A finite height bound for rank-one short presentations'
desc: A proved cofactor bound makes each fixed least-failure dimension a finite integer problem, without excluding any dimension.
tags: []
sources: []
created: 2026-09-19T02:15:34Z
updated: 2026-09-19T02:15:34Z
---


# A finite height bound for rank-one short presentations

***

Let $P$ be a primitive positive integer set, meaning $\gcd(P)=1$,
and put $d=d(P)\ge2$. Let $R$ be the rational span of its zero
ternary relations with support at most $d+1$ in $\mathbb Q^P$.
If

$$
\dim_{\mathbb Q}(\mathbb Q^P/R)=1,
$$

then

$$
\boxed{\max P\le
d(d+1)^{d-1}(d-1)^{(d-1)/2}.}                              \tag{1}
$$


Choose a maximum dissociated set $D=\{b_1,\ldots,b_d\}$. For each
$x\in P$, choose a ternary representation $v_x\in\{-1,0,1\}^d$
on $D$, taking $v_{b_i}=e_i$. Every defining relation
$e_x-\sum_i(v_x)_i e_{b_i}$ has support at most $d+1$, so belongs
to $R$.

Eliminating all generators outside $D$ therefore identifies the short
presentation with the quotient of $\mathbb Q^d$ by the rows

$$
u=\sum_x\varepsilon_x v_x
$$

coming from short relations. Each entry of each row has absolute value
at most $d+1$. The rows span a $(d-1)$-dimensional space, by the
rank-one hypothesis.

Choose $d-1$ independent rows as a matrix $U$. Its kernel is the line
spanned by $b=(b_1,\ldots,b_d)$. Moreover $\gcd(b_1,\ldots,b_d)=1$:
$D\subset P$ and the ternary representations show that $D$ and $P$
generate the same subgroup of $\mathbb Z$.

The nonzero vector of signed maximal minors of $U$ is consequently
an integer multiple of $b$. Every minor has $d-1$ rows of Euclidean
norm at most $(d+1)\sqrt{d-1}$. Hadamard's determinant inequality gives

$$
\max_i b_i\le(d+1)^{d-1}(d-1)^{(d-1)/2}.
$$

Finally, each positive ternary combination of $D$ is at most
$\sum_i b_i\le d\max_i b_i$, proving (1).

By the [[research/erdos_963/parity_fibers|short-relation reduction]], a
primitive least-dimensional failure of the strong odd bound satisfies the
hypothesis. For example, a least failure in dimension five would have all its
weights at most $103680$.

This makes **each fixed** least-failure dimension a finite problem.
It does not bound that dimension, provide an exclusion certificate,
or resolve the logarithmic lower bound. No search of the universe in
(1) was undertaken.
