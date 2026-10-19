---
name: theory/ramsey_theory/L261_difference_domain_thinning/_refutation
title: Powers of four encode triangle-free colorings
desc: |
  Every Schur relation among differences of powers of four is an endpoint
  triangle, so triangle-free edge colorings become Schur-free colorings of
  difference domains and no proportion of the vertices survives a color.
created: 2026-10-15T23:12:24Z
updated: 2026-10-15T23:12:24Z
---

***

We refute
[[theory/ramsey_theory/L261_difference_domain_thinning/_index|L261]] in
the notation of its statement. A coloring of $D(X)$ is Schur-free when no
class contains $a$, $b$ and $a+b$, with $a=b$ allowed. The only outside
premise is the statement of
[[problems/ramsey_theory/E0183/claims/2026_08_01_openai|the accepted claim on Problem 183]],
$R_k(3)\ge(ck^{1/3}/\log k)^k$ for every $k\ge2$, used only at the
statement interface. The argument is author-recorded by Plasma AI.

**Lemma.** Let $X_n=\{4^0,4^1,\ldots,4^{n-1}\}$. The map
$(u,v)\mapsto4^u-4^v$ on pairs $u>v$ is injective, and every relation
$a+b=c$ in $D(X_n)$, $a=b$ allowed, has the form $a=4^v-4^z$,
$b=4^u-4^v$, $c=4^u-4^z$ with $z<v<u$, or the same with $a$ and $b$
exchanged.

*Proof.* Write $a=4^u-4^v$, $b=4^w-4^z$ and $c=4^t-4^s$ with $u>v$, $w>z$
and $t>s$. Then $a+b=c$ reads $4^u+4^w+4^s=4^t+4^v+4^z$. The base-four
digits of a sum of three powers of four are the multiplicities of the
exponents, which are at most 3, so the multisets $\{u,w,s\}$ and
$\{t,v,z\}$ coincide. Since $t>s$, $t$ is $u$ or $w$; after exchanging $a$
and $b$, $t=u$. Then $\{w,s\}=\{v,z\}$, and $w>z$ rules out $w=z$, so
$w=v$ and $s=z$. Thus $z<v<u$. Equal summands would need $(u,v)=(w,z)$,
which contradicts $w=v<u$. Injectivity is the same digit argument applied
to $4^u+4^{v'}=4^{u'}+4^v$. $\square$

**Theorem.** Given the accepted statement $R_k(3)^{1/k}\to\infty$, the
claim fails for every $\delta>0$.

*Proof.* Let $n_k=R_k(3)-1$, the largest $n$ for which the edges of $K_n$
have a $k$-coloring with no monochromatic triangle; $n_1=2$. If
$n_k\le Bn_{k-1}$ for every $k\ge2$, then $n_k\le2B^{k-1}$, which
contradicts $n_k^{1/k}\to\infty$. So for every $\delta>0$ some $k\ge2$ has
$n_{k-1}<\delta n_k$. Take a triangle-free $k$-coloring of the edges of
$K_{n_k}$ on the vertex set $\{0,\ldots,n_k-1\}$, and give $4^u-4^v$ the
color of the edge $uv$. By the lemma this is well defined, and a
monochromatic relation $a+b=c$ is a monochromatic triangle, so the coloring
of $D(X_{n_k})$ is Schur-free. If $Y\subseteq X_{n_k}$ has $D(Y)$
omitting a color, the exponents of $Y$ span a triangle-free coloring with
$k-1$ colors, so $|Y|\le n_{k-1}<\delta|X_{n_k}|$. $\square$
