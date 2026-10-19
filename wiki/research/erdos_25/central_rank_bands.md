---
name: research/erdos_25/central_rank_bands
desc: Complete central-rank modulus families in fixed power bands force Haar coverage and delayed natural density one, even with arbitrary centers between ranks.
tags: [coherent-blocks, constructions, partial-results]
sources: []
created: 2026-09-22T14:20:00Z
updated: 2026-09-24T22:13:01Z
---


# research/erdos_25/central_rank_bands

***

The mixed-root coding attempt in
[the preparation notes](overlapping_parent_preparations.md#status-of-mixed-root-and-coding-attempts)
suggests assigning a different coherent center to each prime-factor rank.
The following theorem rules out keeping complete central-rank families
through a fixed power range. It does not rule out carefully selected
subfamilies, and gives no resolution of Problem 25.

## Theorem

Fix $c>1$, an unbounded set $\mathcal H$ of positive integers,
and arbitrary centers $\alpha_h\in\widehat{\mathbb Z}$ for
$h\in\mathcal H$. Put $A_h=\exp(\exp h)$. Install the class
$[\alpha_h]_q$ for every squarefree integer $q$ such that
$$
 \Omega(q)=h,\qquad A_h<q<A_h^c.
 \tag{1}
$$
Then the full Haar union has measure one. With the original activation
$n\ge q$, the delayed union has natural density one, and its
survivor set has natural and logarithmic density zero.

Distinct ranks give disjoint modulus families, so there is exactly one
residue per modulus. Their union admits a strictly increasing enumeration.

## A fresh-coordinate certificate

Set $\varepsilon=(c-1)/4$. Fix a prime cutoff $R$, and let
$$
 Y_h=A_h^{\varepsilon/h}.
$$
For large $h$, $R<Y_h<A_h$. Under Haar sampling of $x$,
let $V_h$ count primes $R<p\le Y_h$ for which
$x\equiv\alpha_h\pmod p$. Its summands are independent
Bernoulli variables of parameters $1/p$, and
$$
 \lambda_h:=\mathbb E V_h
 =h-\log h+O_{R,c}(1).
 \tag{2}
$$
This uses only $\sum_{p\le y}1/p=\log\log y+O(1)$. That
estimate follows from the elementary Euler-product estimates already
used in the wiki: the product is between $H_{\lfloor y\rfloor}$
and $C\log(2y)$, and its logarithm differs from the prime
reciprocal sum by a bounded amount.

The elementary Bernoulli lower-tail lemma in
[rank-threshold families](rank_threshold_families.md#an-elementary-independent-tail-lower-bound)
states that, for $\lambda\ge10^4$ and $r\le1.1\lambda$,
$$
 \Pr(V\ge r)\ge\frac23
   \exp\!\left[-150\left(1+
                 \frac{(r-\lambda)_+^2}{\lambda}\right)\right].
$$
Apply it with $r=h-1$. By (2), its hypotheses hold and
$(h-1-\lambda_h)_+^2/\lambda_h\le1$ for sufficiently large
$h$, depending on $R,c$. Thus
$$
 \Pr(V_h\ge h-1)\ge\kappa:=\tfrac23e^{-300}.
 \tag{3}
$$
The positive constant does not depend on $R$.

Independently, let $W_h$ count matching primes in
$(A_h,A_h^{1+\varepsilon}]$. Chebyshev's bounds
$a t/\log t\le\pi(t)\le b t/\log t$, for fixed positive
$a,b$ and sufficiently large $t$, imply by partial summation
$$
 \sum_{A<p\le A^{1+\varepsilon}}\frac1p
 \ge a\log(1+\varepsilon)-\frac b{\log A}
 \ge\frac a2\log(1+\varepsilon)
$$
for large $A$. Therefore
$$
 \Pr(W_h\ge1)\ge
 \rho_c:=1-(1+\varepsilon)^{-a/2}>0.
 \tag{4}
$$
The event $E_{h,R}=\{V_h\ge h-1,\ W_h\ge1\}$ has
measure at least $\eta_c:=\kappa\rho_c>0$. On this event choose
$h-1$ distinct matching small primes and one matching large prime.
Their squarefree product satisfies
$$
 A_h<q\le A_h^{1+\varepsilon}Y_h^{h-1}
          <A_h^{1+2\varepsilon}<A_h^c.
$$
It consequently supplies one of the installed classes in (1). The
certificate uses only prime coordinates greater than $R$.

## Infinitely many independent certificates

Choose $h_1<h_2<\cdots$ in $\mathcal H$ recursively. Starting
with $R_0=2$, choose $h_j$ large enough for (3)--(4) with
$R=R_{j-1}$, and then put
$R_j=\lceil A_{h_j}^{1+\varepsilon}\rceil$. Each event
$E_{h_j,R_{j-1}}$ depends only on primes in
$(R_{j-1},R_j]$. They are independent and each has measure at
least $\eta_c$. The probability of avoiding the first $J$ is
at most $(1-\eta_c)^J$. Their union thus has Haar measure one,
as does the full installed union containing it.

Every finite installed union is periodic, and its delayed version
differs from it only on finitely many positive integers. Its natural
density is therefore its Haar measure. Finite subfamilies with measures
arbitrarily close to one are contained in the full delayed union. This
gives lower natural density one; the upper bound one is automatic.
All uses of periodicity here are for fixed finite families, so no
interchange of an infinite union and natural density occurs.

The proof also permits $\log\log A_h=h+O(\sqrt h)$, with a fixed
implicit constant: the lower bound in (3) remains a positive constant.
It does not show that a positive-density subfamily of (1) retains its
fresh-coordinate certificates. Such a conclusion would require a new
robustness estimate, not just the complete-family argument.
