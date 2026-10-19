---
name: theory/covering_systems/L13_useful_supply_obstruction/_proof
title: Proof of the strict useful-supply obstruction
desc: |
  Exact class-support counts and a pointwise forced-excess bound limit
  the total supply available to meet all prime-power cylinder deficits.
tags: []
sources: []
created: 2026-09-09T02:22:43Z
updated: 2026-09-09T02:22:43Z
---

***

Use $N,p,a,M,S,D$ and the full profile from [L13](_index.md), with
$D>0$. Each nonunit divisor of $N$ has a unique form $p^jm$, where
$0\le j\le a$, $m\mid M$, and $(j,m)\ne(0,1)$. The cylinders are

$$
Y_t=\{x\in\mathbb Z/N\mathbb Z:x\equiv t\pmod{p^a}\},
\qquad t\in\mathbb Z/p^a\mathbb Z.
$$

They partition $\mathbb Z/N\mathbb Z$ into $p^a$ sets of $M$ points.
All masses below count class incidences, with overlaps counted repeatedly.

## The exact contribution of one class

Since $\gcd(p^a,m)=1$ for every $m\mid M$, prescribed residues modulo
$p^a$ and $m$ select exactly one class modulo $p^am$. To see this,
write $x=t+p^az$: multiplication by $p^a$ is invertible modulo $m$,
so the congruence modulo $m$ chooses exactly one residue of $z$ modulo
$m$. There are $N/(p^am)=M/m$ such points modulo $N$. This includes
$m=1$, when the congruence modulo $m$ imposes no restriction.

For a class with modulus $m>1$ coprime to $p$, the count is $M/m$ in
every cylinder. The sum of these contributions is

$$
\sum_{\substack{m\mid M\\m>1}}\frac{M}{m}
=\sum_{d\mid M}d-M=S-M.
$$

Here $m\mapsto M/m$ permutes the divisors of $M$, and the omitted
modulus $m=1$ accounts for the subtracted term $M$.

Next take a class $b_{p^jm}(p^jm)$ with $1\le j\le a$ and
$m\mid M$. It meets $Y_t$ precisely when

$$
t\equiv b_{p^jm}\pmod{p^j}.
$$

There are exactly $p^{a-j}$ such residues $t$ modulo $p^a$. On each
of these cylinders the congruence modulo $p^j$ is automatic, and the
remaining condition modulo $m$ selects exactly $M/m$ points by the
coprime count. Thus the contribution has weight $M/m$ on exactly
$p^{a-j}$ cylinders, including just one cylinder when $j=a$.

## Necessary loads and total supply

For each $t$, let $T_t$ be the total contribution in $Y_t$ from the
classes whose moduli are divisible by $p$. The full profile's incidence
mass there is

$$
(S-M)+T_t.
$$

Consequently, even the necessary cylinder mass inequalities for a cover
require

$$
(S-M)+T_t\ge M,\qquad\hbox{that is,}\qquad T_t\ge D
\quad\hbox{for every }t.
$$

Summing the exact class-support counts gives a total independent of all
residue choices:

$$
\sum_t T_t
=\sum_{j=1}^a\sum_{m\mid M}\frac{M}{m}p^{a-j}
=S\sum_{j=1}^a p^{a-j}
=S\frac{p^a-1}{p-1}.
$$

## Subtracting forced excess

Call a contribution heavy if its weight $M/m$ exceeds $D$. Define
threshold waste and useful supply by

$$
W_t=(T_t-D)_+=\max(T_t-D,0),\qquad
V=\sum_t\min(T_t,D)=\sum_t T_t-\sum_t W_t.
$$

These are quantities for the cylinder lower-bound constraints. They do
not count distinct covered points or identify the actual holes left by
the classes coprime to $p$.

At a fixed cylinder, suppose there are $h\ge1$ heavy contributions of
weights $w_1,\ldots,w_h>D$. All other contributions are nonnegative.
At least one heavy contribution is present, each exceeds $D$, and all
weights are positive. Thus $T_t\ge\sum_{\ell=1}^h w_\ell>D$, and hence

$$
W_t=T_t-D
\ge\sum_{\ell=1}^h w_\ell-D
=\sum_{\ell=1}^h(w_\ell-D)+(h-1)D
\ge\sum_{\ell=1}^h(w_\ell-D).
$$

The last inequality uses $(h-1)D\ge0$, since $D>0$.

If $h=0$, the last sum is empty and equals zero, and $W_t\ge0$ gives
the same lower bound. Thus any overlap between heavy contributions
preserves the bound. Contributions of weight at most $D$ cannot decrease
$W_t$.

Each heavy class of modulus $p^jm$ contributes its forced excess
$M/m-D$ on exactly $p^{a-j}$ cylinders. Summing the last inequality
over all cylinders yields

$$
\sum_t W_t\ge
\sum_{\substack{1\le j\le a,\ m\mid M\\M/m>D}}
  (M/m-D)p^{a-j}.
$$

Combining this with the total supply gives $V\le U$. The equivalent
formula for $U$ in the statement follows by applying
$w-(w-D)_+=\min(w,D)$ separately to every weight $w=M/m$ in the
finite sum.

If every cylinder meets its necessary load $T_t\ge D$, then
$\min(T_t,D)=D$ in all $p^a$ cylinders, so

$$
Dp^a=V\le U.
$$

This contradicts $U<Dp^a$. Therefore that strict inequality rules out
every full-profile placement satisfying even the cylinder mass
constraints, and in particular rules out every full-profile cover.

## Distinct subprofiles and the guards

Suppose a family with pairwise distinct nonunit moduli dividing $N$
were a cover. Add one arbitrarily placed residue class for each unused
nonunit divisor of $N$. The resulting full profile still covers, and
no cylinder incidence mass has decreased. This contradicts the
full-profile exclusion. The same argument shows directly that feasibility
of the cylinder lower bounds is upward closed under adding missing
classes. A cover of higher multiplicity is also a one-cover and is
excluded in this domain. Repeated moduli are not subprofiles of the full
inventory, so the argument makes no assertion about them.

If $D\le0$, the constant contribution $S-M$ is already at least $M$,
and these full-profile cylinder lower bounds supply no obstruction.
For $D>0$, the proof only gives $Dp^a\le U$ as a necessary condition.
Equality or the reverse strict inequality therefore does not decide
feasibility or coverage.

For the boundary $M=1$, the divisor sum is $S=1$ and $D=1$. There are
no nonunit moduli coprime to $p$, and every class of modulus $p^j$ has
weight one. There are no heavy terms. Thus

$$
\frac{U}{p^a}=\sum_{j=1}^a p^{-j}
=\frac{1-p^{-a}}{p-1}<1,
$$

because $p\ge2$. The strict criterion applies at every depth $a\ge1$,
including $a=1$, and excludes distinct nonunit-divisor covers of a pure
prime-power frame. No finite enumeration is used.
