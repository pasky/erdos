---
name: research/erdos_774/lemmas/galois_squaring
title: A same-conductor squaring identity with a nontriviality certificate
desc: Galois squaring transforms a coefficient-two root relation into an integral pair-product relation; character dynamics prove it is nonzero for more than four leaves, but coefficient collisions and actual colors remain uncontrolled.
tags: [E0774, proved, algebra, conditional, incomplete]
sources: []
created: 2026-09-18T18:37:35Z
updated: 2026-09-18T18:37:35Z
---


# A same-conductor squaring identity with a nontriviality certificate

***

## Standing and exact hypotheses

Suppose $w$ and the distinct roots in $B$ all have odd order,
$w\notin B$, and
$$
2w=\sum_{b\in B}\epsilon_b b,\qquad \epsilon_b\in\{\pm1\}. \tag{1}
$$
Unlike the conductor-disjoint determinant construction, this lemma works
inside one conductor. It gives a nonzero **integer** relation on pair
products and squares when $|B|>4$. It does not automatically give a
ternary relation: multiplicative collisions can increase coefficients.
Nor does it control the actual colors of the resulting roots.

These are precisely the surviving obligations. No general-height extension,
ternary-subrelation theorem, or global coloring conclusion is asserted.

## 1. The squaring identity

Choose one odd $N$ containing the conductors in (1). Squaring is a
cyclotomic Galois automorphism of $\mathbb Q(\zeta_N)$, so
$$
\sum_b\epsilon_b b^2=2w^2.
$$
Squaring (1) itself gives $(\sum_b\epsilon_b b)^2=4w^2$.
Subtract the preceding equation and divide by two to obtain
$$
\boxed{
w^2=\sum_{\epsilon_b=-1}b^2+
\sum_{\{b,c\}\subset B,\ b\ne c}\epsilon_b\epsilon_c\,bc.
} \tag{2}
$$
The second sum is over unordered pairs, counted once. Before identifying
equal root products, every listed term has coefficient $+1$ or $-1$.
Squares occur only for negative leaves.

To distinguish that indexed expression from the actual relation, work in
the group ring $\mathbb Z[\mu_N]$, writing $[g]$ for its formal basis
element at $g$. Put
$$
U=\sum_b\epsilon_b[b],\qquad
\psi_2(U)=\sum_b\epsilon_b[b^2],\qquad
\lambda_2(U)=\frac{U^2-\psi_2(U)}2.
$$
The last expression has integer coefficients by its explicit expansion in
(2). Evaluation $[g]\mapsto g$ sends
$$
R=\lambda_2(U)-[w^2] \tag{3}
$$
to zero. Colliding pair products, squares, and $w^2$ must be collected
in this group ring before discussing their coefficient height.

## 2. Nontriviality after all multiplicative collisions

**Proposition.** If $|B|>4$, then $R\ne0$ in $\mathbb Z[\mu_N]$.

Multiply every root in (1) by $w^{-1}$, so $w=1$.
This multiplies (3) by the invertible group-ring element $[w^{-2}]$;
it does not change formal nontriviality or the number of distinct leaves.
Suppose for contradiction that $\lambda_2(U)=[1]$. Then
$$
\psi_2(U)=U^2-2[1]. \tag{4}
$$
For each character $\chi$ of $\mu_N$, write $z_\chi=\chi(U)$.
Equation (4) gives
$$
z_{\chi^2}=z_\chi^2-2.
$$
Since $N$ is odd, $\chi\mapsto\chi^2$ permutes the finite character
group. Every $z_\chi$ is therefore a periodic point of $F(z)=z^2-2$.

Every complex periodic point of $F$ lies in $[-2,2]$. For a direct
proof, choose $t\ne0$ with $z=t+t^{-1}$. Induction gives
$$
F^n(z)=t^{2^n}+t^{-2^n}.
$$
If $F^n(z)=z$, the two roots of $X^2-zX+1$ show that
$t^{2^n}$ is either $t$ or $t^{-1}$. Hence $t$ is a root of
unity, so $z=2\operatorname{Re}t\in[-2,2]$.

Writing $U=\sum_g a_g[g]$, character orthogonality now gives
$$
|B|=\sum_{g\in\mu_N}|a_g|^2
=\frac1N\sum_\chi|z_\chi|^2\le4,
$$
contrary to the hypothesis. This proves the proposition. In particular it
applies to the nineteen-leaf coefficient-two circuits already constructed
in the prime grids, without rerunning their certificates.

## 3. What would make this an actual-color flattening step

If the collected nonzero coefficients of $R$ all lie in $\{\pm1\}$
and their root support has one actual color, (3) is the required
monochromatic ternary relation. A stronger sufficient collision condition
is that the indexed roots in (2), together with $w^2$, are all distinct;
then the coefficients are automatically ternary.

Neither condition has been established for the root supports that a finite
coloring can supply. Refining a color by the pair $(f(x),f(x^2))$
controls square colors, but not the colors $f(bc)$ of pair products.
Nontriviality from Section 2 prevents total formal cancellation; it does
not prevent surviving coefficients of magnitude greater than one.

Thus (2) is a proved same-conductor algebraic alternative, with an exact
nontriviality certificate, not a proof of height descent or unbounded
coloring. The identity and character argument received independent internal
checks. No computation or additional literature result was used.
