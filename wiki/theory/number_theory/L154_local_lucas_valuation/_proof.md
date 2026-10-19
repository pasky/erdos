---
name: theory/number_theory/L154_local_lucas_valuation/_proof
title: Taylor expansion on an allowed next digit
desc: The leading form stays nonzero on X+Y=d when d is a unit, and its root count supplies a Lucas-admissible next digit with no extra valuation.
created: 2026-10-15T11:42:54Z
updated: 2026-10-15T11:42:54Z
---

# Taylor expansion on an allowed next digit

***

This proves [[theory/number_theory/L154_local_lucas_valuation/_index|L154]].
Write $J\preceq_pN$ for the digitwise domination in the statement, and
put $K=N-J$. Then $0\le J\le N$, so $0\le j=s+p^eJ\le n$.
Since $0\le s\le t<p$, the lower $e$ digits of $j$ are dominated by
those of $n$, and the remaining digits are dominated by $J\preceq_pN$.
Thus $p\nmid\binom nj$. For completeness, the Lucas criterion follows
by expanding

$$
(1+X)^n\equiv\prod_{r\ge0}(1+X^{p^r})^{n_r}\pmod p,
$$

where $n_r$ are the base-$p$ digits. The coefficient of $X^j$ is
$\prod_r\binom{n_r}{j_r}$, which is nonzero exactly under domination.

Taylor expansion at the integer point $(s,t-s)$ has integer
coefficients. By the definition of $\mu$ and $H$,

$$
F(j,n-j)=p^{e\mu}H(J,K)+p^{e(\mu+1)}Z,
\qquad Z\in\mathbf Z.
$$

Set $x=J\bmod p$. Domination gives $0\le x\le d$, and
$K\equiv d-x\pmod p$. The valuation assertion and its equality
criterion follow from this display, including the convention for zero.

Because $p\nmid N$, $d\ne0$ in $\mathbf F_p$. The polynomial
$\phi(X)=H(X,d-X)\in\mathbf F_p[X]$ has degree at most $\mu$ and
is nonzero. Indeed, homogeneity gives the identity in
$\mathbf F_p(X,Y)$

$$
H(X,Y)=\left(\frac{X+Y}{d}\right)^\mu
\phi\!\left(\frac{dX}{X+Y}\right).
$$

If $\phi$ vanished identically, every coefficient of $H$ would vanish
modulo $p$, contrary to the hypothesis. It has at most $\mu$ roots.
When $d\ge\mu$, the $d+1$ distinct residues $0,\ldots,d$ therefore
include a nonroot $x$. Take $J=x$, with all higher digits zero. Then
$J\preceq_pN$, and the equality criterion gives
$v_pF(j,n-j)=e\mu$ as required. $\square$
