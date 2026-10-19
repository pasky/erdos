---
name: theory/ramsey_theory/L265_bohr_cell_avoidance_consequences/_proof
title: Refining Bohr cells and planting signed cubes
desc: |
  Refinement by the best arc keeps a 1/q fraction of a Bohr cell and
  removes a color from its differences; digit cubes in base q+1 are Bohr
  cells that carry the signed cube's vector addition exactly.
created: 2026-10-15T23:12:24Z
updated: 2026-10-15T23:12:24Z
---

***

We prove
[[theory/ramsey_theory/L265_bohr_cell_avoidance_consequences/_index|L265]]
in the notation of its statement. For a set $Y$ let $C(Y)$ be the set of
colors occurring on $D(Y)$. The proof is author-recorded by Plasma AI.

**Lemma 1 (refinement).** If a coloring of $[1,N]$ has property (B), every
Bohr cell $Y$ in $\{0,\ldots,N\}$ satisfies $|Y|\le q^{|C(Y)|}$.

*Proof.* Start from $Y_0=Y$. Given a cell $Y_j$ with $|Y_j|\ge2$, take the
color $i_j\in C(Y_j)$ and the frequency $\theta_j$ that property (B)
supplies. Of the $q$ half-open arcs of length $1/q$ covering
$\mathbb R/\mathbb Z$, one arc $J$ has
$|Y_j\cap\{y:\{\theta_jy\}\in J\}|\ge|Y_j|/q$; let $Y_{j+1}$ be that set.
It is a Bohr cell, since $1/q\le\rho$. Its differences satisfy
$\|\theta_jx\|<1/q\le\rho$, so they avoid color $i_j$, and
$C(Y_{j+1})\subseteq C(Y_j)\setminus\{i_j\}$. Every element of $D(Y_j)$
is colored, so a cell with at least two points has $C(Y_j)$ nonempty.
Hence the process stops at some $T\le|C(Y)|$ with $|Y_T|\le1$, and
$|Y|\le q^T|Y_T|\le q^{|C(Y)|}$. $\square$

*Proof of (1).* Take a coloring of $[1,S(k)]$ by at most $k$ colors with no
monochromatic $x+y=z$. By hypothesis it has property (B). The set
$\{0,\ldots,S(k)\}$ is a Bohr cell (the case $r=0$), and its differences
carry at most $k$ colors, so Lemma 1 gives $S(k)+1\le q^k$. $\square$

**Lemma 2 (digit cubes).** Let $b\ge4$ and
$\iota_b(v)=\sum_{i=1}^rv_ib^{i-1}$ for $v\in\{-1,0,1\}^r$.

1. $\iota_b$ is injective, $\iota_b(v)>0$ exactly when $v\in Q_r^+$, and
   $\iota_b(Q_r^+)\subseteq[1,b^r-1]$.
2. For $v,w,u\in Q_r^+$, $\iota_b(v)+\iota_b(w)=\iota_b(u)$ if and only if
   $v+w=u$.
3. If $b=q+1$, the digit cube $Y_r=\{\iota_b(\delta):\delta\in\{0,1\}^r\}$
   equals $\{y\in\{0,\ldots,b^r-1\}:\{y/b^l\}\in[0,1/q)\text{ for }
   l=1,\ldots,r\}$, and $D(Y_r)=\iota_b(Q_r^+)$.

*Proof.* A relation $\sum_ic_ib^{i-1}=0$ with $|c_i|\le3<b$ forces every
$c_i=0$, because the lowest nonzero $c_i$ would be divisible by $b$. This
gives injectivity, and part 2, since $v+w-u$ has entries in $[-3,3]$. The
last nonzero term of $\iota_b(v)$ dominates the others, because
$b^{j-1}>\sum_{i<j}b^{i-1}$; this gives the sign and the range. For part 3
let $d_0,d_1,\ldots$ be the base-$b$ digits of $y$. Then
$\{y/b^l\}=(d_{l-1}+\{y/b^{l-1}\})/b$, which is below $1/q$ exactly when
$d_{l-1}+\{y/b^{l-1}\}<b/q=1+1/q$. Since $1+1/q<2$, induction on $l$ shows
that all $r$ conditions hold exactly when every digit is $0$ or $1$; a
finite sum of distinct powers $b^{-j}$ stays below $1/(b-1)=1/q$.
Differences of vectors in $\{0,1\}^r$ are exactly the vectors in
$\{-1,0,1\}^r$, and part 1 identifies the positive ones. $\square$

*Proof of (2).* Fix $r\ge1$ and a coloring $\gamma$ of $Q_r^+$ by
$\chi_r$ colors with no monochromatic triple. Put $b=q+1\ge4$ and
$N=b^r-1$. Color $x=\iota_b(v)$ by $\gamma(v)$ for $v\in Q_r^+$, and color
every other $x\in[1,N]$ by the restriction of a coloring of $[1,N]$ with no
monochromatic $x+y=z$, using a disjoint palette. A monochromatic solution
of $x+y=z$ in the first palette has all three terms in $\iota_b(Q_r^+)$,
so by Lemma 2(2) it is a monochromatic triple of $\gamma$, which does not
exist; in the second palette it would be monochromatic for the restricted
coloring. So the coloring has no monochromatic $x+y=z$, and by hypothesis
it has property (B). By Lemma 2(3), $Y_r$ is a Bohr cell with arcs of
length $1/q\le\rho$, $|Y_r|=2^r$, and $D(Y_r)=\iota_b(Q_r^+)$ carries at
most $\chi_r$ colors. Lemma 1 gives $2^r\le q^{\chi_r}$, that is,
$\chi_r\ge r\log2/\log q$. $\square$

The same argument with property (B) required only for cells with
$|Y|\ge A^{|C(Y)|}$, for some $A\ge1$, gives $S(k)+1\le\max(q,A)^k$ and
$\chi_r\ge r\log2/\log\max(q,A)$: run the refinement only while
$|Y_j|\ge\max(2,A^{|C(Y_j)|})$, and at the stopping time
$|Y|\le q^T\max(1,A^{|C(Y)|-T})\le\max(q,A)^{|C(Y)|}$.
