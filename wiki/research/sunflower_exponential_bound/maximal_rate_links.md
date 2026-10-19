---
name: research/sunflower_exponential_bound/maximal_rate_links
title: Maximal-rate links in the substitution examples
desc: |
  Exact excess formulas show that the maximal-rate link procedure succeeds
  at its first step on L214 and L215, although these families defeat
  matching and bounded-core statements at fixed spread.
created: 2026-10-15T20:31:18Z
updated: 2026-10-15T20:31:18Z
---

***

This author-recorded argument by Plasma AI evaluates the proposed
maximal-rate link procedure on the explicit examples. It uses the
substitution and block estimates of
[[theory/set_systems/L214_spread_intersecting_families/_proof|L214]] and the
triangle-power calculation of
[[theory/set_systems/L215_spread_large_core_sunflowers/_proof|L215]],
both at tier 0. It proves no bound on the procedure for a general family.

For a family $\mathcal F$ of $n$-sets, $n\ge2$, let

$$
R_a(\mathcal F)=\max_{0<|T|<n}|\mathcal F_T|^{1/(n-|T|)}.
$$

An extremal set $T$ is a maximizer in this definition. Passing to its
link preserves absolute spread at rate $R_a(\mathcal F)$ and makes the
link's size exactly that rate to its residual uniformity. The
[[research/sunflower_exponential_bound/proof_sketch|proof sketch]] asks
whether successive such choices can be made without losing too much rate.

## An exact formula for a balanced block seed

Fix an integer $\rho\ge2$, and put

$$
B=B(\rho,\rho^\rho),\qquad a=\rho^\rho+1,
\qquad A=|B|=2\rho^{a-1}.
$$

For every $u>0$, L214's block estimate, with equality at a center and at
a full member, gives

$$
\psi_B(u)=\max\left(\frac u2,\frac{u^a}{A}\right).
\tag{1}
$$

Indeed the estimate is $\Pr[I\subseteq S]\le\rho^{1-|I|}/2$. When
$u\le\rho$ its largest possible contribution is $u/2$, attained by a
center. When $u\ge\rho$ the largest possible contribution is
$u^a/(2\rho^{a-1})$, attained by a member. The two expressions agree
at $u=\rho$.

## A link that attains the maximal rate

Let $H$ be a nonempty $b$-uniform family, $b\ge1$, with $M$ members.
Suppose that for

$$
R=(\rho M)^{1/b}
\quad\hbox{one has}\quad E_H(R)=\rho.
\tag{2}
$$

Then $R_a(B[H])=R$. Moreover, some extremal set has a link containing
$\rho$ pairwise disjoint members.

*Proof.* By (1) and the substitution identity,

$$
E_{B[H]}(R)=\psi_B(E_H(R))=\rho/2
=\frac{R^{ab}}{A M^a}.
$$

Since $|B[H]|=AM^a$, this is precisely the absolute $R$-spread bound
for every nonempty subset, and hence $R_a(B[H])\le R$.

Fix a member $S_0\in H$ and let $T=\{x\}\times S_0$, the whole fiber
over the first center of $B$. It is a nonempty proper subset of a member
of $B[H]$. Members through $T$ have a first-kind root and the fixed
fiber $S_0$ over $x$. Their number is

$$
|B[H]_T|=\rho^{a-1}M^{a-1}=R^{b(a-1)}.
$$

Thus $T$ attains rate $R$. After removing $T$, each of the $a-1$ blocks
independently chooses one of $\rho$ root points and then a member of
the corresponding copy of $H$. Choosing a different root point in every
block for each of $\rho$ members makes those members pairwise disjoint.
No disjointness inside $H$ is required. $\square$

## Application to L214

For $F=B^h$, $h\ge1$, take $H=B^{h-1}$, interpreting $B^0$ as the
one-point family. Put $d=a^{h-1}$, so $H$ has uniformity $d$ and
$M=A^{(d-1)/(a-1)}$ members. Then

$$
R_a(F)=(\rho M)^{1/d}
=\rho\,2^{(1-1/d)/(a-1)}.
\tag{3}
$$

To verify (2), set $K=A^{1/(a-1)}$. The number $R$ in (3) lies in
$[\rho,K)$, and the first $h-1$ iterates of (1) follow the branch
$u\mapsto u^a/A$. Explicitly those iterates are
$K(R/K)^{a^i}$, for $0\le i\le h-1$, decreasing to $\rho$ at the final
index. They all lie above or at the branch threshold $\rho$.
Thus $E_H(R)=\rho$, as needed.

The extremal link constructed above has $\rho$ disjoint members.
For each $k\le\rho$, the procedure can therefore find a $k$-sunflower
at its first step. This proves existence of a successful maximizer; it
does not assert that every tie-breaking rule succeeds.

## Application to L215

Now let $F=(B^j)[D^g]$, with the parameters of L215. Write $s=2^g$ and
$Q=|D^g|=3^{s-1}$. By the natural identification of nested fibers,

$$
F=B[H],\qquad H=(B^{j-1})[D^g].
$$

Put $d=a^{j-1}$. Then $H$ has uniformity $sd$ and
$M=A^{(d-1)/(a-1)}Q^d$ members. Its relevant rate is

$$
R=(\rho M)^{1/(sd)},\qquad
y=R^s/Q=\rho^{1/d}A^{(d-1)/((a-1)d)}.
$$

As above, $\psi_B^{(j-1)}(y)=\rho$ with all the iterates at least
$\rho\ge3$. Since $R^s=Qy\ge3^s$, we have $R\ge3$, and L215's
triangle formula applies:
$E_{D^g}(R)=R^s/Q=y$. Therefore
$E_H(R)=\psi_B^{(j-1)}(y)=\rho$, verifying (2). Hence

$$
R_a(F)=(\rho M)^{1/(sd)},
$$

and again an extremal link has $\rho$ pairwise disjoint members. Its
core has $sd$ points, consistent with L215's lower bound $s$ on core
size. The procedure is allowed to choose a large core.

These exact successes do not extend to arbitrary families. The
[[research/sunflower_exponential_bound/maximal_rate_chain_obstruction|chain obstruction]]
gives families of arbitrarily large exponential rate whose unique
maximal-rate choices discard a sunflower and lead to a sunflower-free
family. A general argument therefore needs more than the favorable
maximizer exhibited here, such as control of the discarded families.
