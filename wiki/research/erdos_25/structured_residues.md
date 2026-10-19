---
name: research/erdos_25/structured_residues
desc: Logarithmic density for finite rational congruence patterns and sets stable under a fixed congruence class of multipliers.
tags: [density, partial-results]
sources: []
created: 2026-09-21T22:54:02Z
updated: 2026-09-24T22:13:01Z
---


# research/erdos_25/structured_residues

***

The following are proved special cases. They do not cover arbitrary moving
residues. Throughout, $\delta$ is the decreasing limit of the densities of
the original finite delayed survivor systems.

We use the multiples theorem and finite-periodic logarithmic approximation:
for $V\subset\mathbb N$ and finite $V_0\uparrow V$,
$$
\operatorname{ld}(M(V)\setminus M(V_0))
=\operatorname{ld}(M(V))-d(M(V_0))\longrightarrow0.
\tag{1}
$$
The relevant Davenport–Erdős 1951 source passage, equations (2), (4), and
(8)–(12), was checked. Alternatively, (1) follows from the self-contained
association proof in [basic reductions](basic_reductions.md).

## Finite rational slopes with integer translations

**Theorem.** Suppose each original congruence belongs to one of finitely
many fixed patterns
$$
n_i=dq_i,\qquad a_i\equiv b+cq_i\pmod{dq_i},
$$
where the triples $(b,c,d)$ are fixed integers with $d\ge1$ and $0\le c<d$.
Then $\operatorname{ld}(A)=\delta$.
In particular, this holds when the normalized ratios $a_i/n_i$ belong to a
fixed finite subset of $\mathbb Q\cap[0,1)$.

**Proof.** Fix a triple. Write uniquely $q=sv$, where every prime factor of
$s$ divides $d$, and $(v,d)=1$. Partition further by $s$ and
$r=v\pmod d$. Let $V$ be the set of $v$ in one such group, and define its
actual delayed union
$$
T_V=\bigcup_{v\in V}
 \{n\ge dsv:n\equiv b+csv\pmod{dsv}\}.
$$
Apart from the finitely many $n\le b$, its full congruence union is
$$
F_V=\{b+sz:z\in M(V),\ z\equiv cr\pmod d\}.
$$
Indeed, for $v\mid z$ with $v\equiv r\pmod d$, the congruence
$z\equiv cr\pmod d$ is equivalent to $z/v\equiv c\pmod d$.
For finite $V_0\subset V$, all its original congruences are active once
$n>d s\max V_0$. Therefore, up to finitely many exceptions,
$$
T_V\setminus T_{V_0}
\subseteq\{b+sz:z\in M(V)\setminus M(V_0)\}.
$$
For fixed $b,s$, summing the absolutely summable difference
$1/(b+sz)-1/(sz)=O_{b,s}(z^{-2})$ shows that a positive affine image of a
set with logarithmic density $\rho$ has logarithmic density $\rho/s$.
Thus (1) makes the last tail arbitrarily small in upper logarithmic density.

There are infinitely many possible $s$, but their omitted groups have a
uniform natural-density bound. Each deleted integer in an $s$-group
satisfies $n\equiv b\pmod s$ and $n\ge dsv\ge s$. Consequently
$$
\left|[1,X]\cap\bigcup_{s>Y}T_s\right|
\le 2X\sum_{\substack{s>Y\\p\mid s\Rightarrow p\mid d}}\frac1s.
$$
The series over these smooth $s$ converges, with total
$\prod_{p\mid d}(1-1/p)^{-1}$. First truncate $s$, then finitely approximate
each remaining $(s,r)$-group, and finally take the finite union over the
original triples. The omitted deletion set then has arbitrarily small
upper logarithmic density. An original initial segment contains every
chosen finite collection, so
$$
\lim_{k\to\infty}
\overline{\operatorname{ld}}(A^{(k)}\setminus A)=0.
$$
Finite periodic recovery proves the theorem. $\square$

## Finite fixed rational translates

**Theorem.** Suppose finitely many fixed pairs $(b_j,c_j)\in\mathbb Z\times
\mathbb N$ are given, and each modulus $n_i$ has an assigned pair satisfying
$$
(c_j,n_i)=1,\qquad c_j a_i\equiv b_j\pmod{n_i}.
$$
Then $\operatorname{ld}(A)=\delta$.

**Proof.** First, a primitive set $P$ has logarithmic density zero: its tail
is contained in $M(P)\setminus M(P\cap[1,K])$, whose logarithmic density
tends to zero by (1).

Fix one pair $(b,c)$ and its modulus set $D$. Put
$$
C=\{n\ge1:cn-b>0,\ cn-b\in M(D)\}.
$$
For a finite initial part $D_K$, define $C_K$ likewise. Substitution
$t=cn-b$ gives
$$
\overline{\operatorname{ld}}(C\setminus C_K)
\le c\,\operatorname{ld}(M(D)\setminus M(D_K))\longrightarrow0.
$$
Here one can use $c/(t+b)=c/t+O_{b,c}(t^{-2})$ and bound the sum over its
single congruence class of $t$ by the unrestricted positive sum. Hence $C$
has finite-periodic logarithmic approximation.

Let $P$ be the minimal generators of $D$ under divisibility. Then $P$ is
primitive and $M(P)=M(D)$. If $n\in C$ is not deleted by any active modulus,
choose $p\in P$ dividing $cn-b$. Necessarily $p>n$. Writing
$cn-b=\ell p$ gives $1\le\ell<c+|b|/n$, so all sufficiently large such
exceptions belong to a finite union of affine images
$$
\{(\ell p+b)/c:p\in P\}\cap\mathbb N.
$$
Each has logarithmic density zero. The actual delayed union is contained
in $C$ outside the finitely many $n$ with $cn-b\le0$, and the reverse
inclusion fails only on the null exceptional set just bounded. Finite
unions preserve both conclusions. Finite truncations have the same
eventual periodic densities as the corresponding $C_K$, so the limiting
survivor density is $\delta$. $\square$

## Rational congruence patterns without coprimality

**Theorem.** Fix finitely many pairs $(C_j,v_j)\in\mathbb Z\times\mathbb N$.
Suppose each modulus $q_i$ is assigned a pair satisfying
$$
 v_j a_i\equiv C_j\pmod{q_i}.
 \tag{2}
$$
No assumption on $(v_j,q_i)$ is needed. The delayed union has
finite-periodic approximation in upper logarithmic density, and the
survivor set has logarithmic density $\delta$.

This strengthens the preceding rational-translate theorem and subsumes
the finite rational-slope theorem. It results from checking the affine
endpoint argument in Section 8 of the
[[research/erdos_25/independent/harmonic_bounds_and_common_shifts|independent input]].

**Proof.** Fix $(C,v)$. Write $q=hr$, where every prime factor of $h$
divides $v$ and $(r,v)=1$. Partition further by the normalized residue
$t=a_q\bmod h$, $0\le t<h$. Necessarily $vt\equiv C\pmod h$, so
for each $h$ there are at most $(v,h)\le v$ possible $t$.

For fixed $(h,t)$, write $a_q=t+hA_q$, with $0\le A_q<r$.
The substitution $n=t+hm$ identifies the exclusions exactly with
$$
 m\ge r,\qquad m\equiv A_q\pmod r,
 \qquad vA_q\equiv (C-vt)/h\pmod r.
$$
Activation is exact because $0\le t<h$. The quotient moduli $r$ are
distinct in this group, and are coprime to $v$. Thus the preceding
rational-translate theorem gives finite-periodic logarithmic
approximation for the group. Its positive affine image retains that
property.

The groups with $h>Y$ have a uniform counting bound. Each deleted
integer in such a group satisfies $n\ge q\ge h$ and $n\equiv t\pmod h$,
so there are at most $X/h$ hits below $X$ for each possible $t$. Hence
$$
 |B_{h>Y}\cap[1,X]|
 \le vX\sum_{\substack{h>Y\\p\mid h\Rightarrow p\mid v}}\frac1h.
$$
The sum tends to zero, being a tail of the finite Euler product
$\prod_{p\mid v}(1-1/p)^{-1}$. First truncate $h$, then finitely
approximate the remaining groups. A finite union over the pairs $(C_j,v_j)$
proves the assertion. $\square$

### Consequence for affine endpoints

Suppose $q_i$ increase, $q_i\le b_i<2q_i$, and
$b_j\not\equiv b_i\pmod{q_i}$ for $j>i$. If the pairs $(q_i,b_i)$ lie
in finitely many fixed rational affine relations
$$
 vb_i=uq_i+c\qquad(u,v\in\mathbb N,\ c\in\mathbb Z),
$$
then $E=\{b_i\}$ has logarithmic density zero.

For one relation put $a_i=b_i-q_i$. Then $va_i\equiv c\pmod{q_i}$,
so (2) applies to its delayed union $B$. Every endpoint is in $B$,
whereas every fixed finite prefix $B_F$ meets $E$ in only finitely many
points by the avoidance condition. Finite-periodic approximation gives
$$
 \overline{\operatorname{ld}}(E)
 \le\overline{\operatorname{ld}}(B\setminus B_F)\longrightarrow0.
$$
Take the finite union of the relation-subsequences. This verifies the
independent note's special case, including bounded choices of $b_i-q_i$
or $2q_i-b_i$, but not arbitrary or approximately affine endpoints.

## Stability under multipliers congruent to one

The abstract lemma in Section 8.6 of
the [[research/erdos_25/independent/bounded_quotient_blocks_and_recentering|second independent record]]
is valid. Its application to bounded residue orders is already covered
by (2), but the following formulation also permits nonperiodic sets.

**Theorem.** Fix $M\ge1$ and put
$S_M=\{k\ge1:k\equiv1\pmod M\}$. Suppose $E\subseteq\mathbb N$
satisfies
$$
 n\in E,\ k\in S_M\quad\Longrightarrow\quad nk\in E.
 \tag{3}
$$
Then $E$ can be approximated from within, in upper logarithmic density,
by finite unions of rays $nS_M$ with $n\in E$. In particular $E$ has
logarithmic density. No natural-density conclusion is asserted.

**Proof.** Let $\mathcal D_M$ consist of the positive integers supported
on primes dividing $M$, including $1$. Write each integer uniquely as
$du$, with $d\in\mathcal D_M$ and $(u,M)=1$. For a fixed $d$ and a
unit residue $r\pmod M$, put
$$
 T_{d,r}=\{u\ge1:u\equiv r\pmod M,\ du\in E\},
 \qquad W_{d,r}=M(T_{d,r}).
$$
Then
$$
 T_{d,r}=W_{d,r}\cap[r]_M.
 \tag{4}
$$
Indeed, if $u=vk$, with $v\in T_{d,r}$ and $u\equiv r\pmod M$,
invertibility of $r$ gives $k\equiv1\pmod M$, so (3) applies.
The reverse inclusion in (4) is the only nontrivial one.

By the multiples approximation (1), choose finite $G\subset T_{d,r}$
so that $W_{d,r}\setminus M(G)$ has arbitrarily small logarithmic
density. Intersecting with $[r]_M$ can only decrease its harmonic mass,
and
$$
 M(G)\cap[r]_M=\bigcup_{v\in G}vS_M.
$$
After dilation by $d$, this gives the required approximation in one
stratum: dilation divides upper logarithmic density by $d$.

The unretained strata with $d>Y$ have harmonic mass at most
$$
 H_{\lfloor X\rfloor}
 \sum_{\substack{d\in\mathcal D_M\\d>Y}}\frac1d.
$$
This tail tends to zero after normalization, since
$$
 \sum_{d\in\mathcal D_M}\frac1d
 =\prod_{p\mid M}(1-1/p)^{-1}<\infty.
$$
There are finitely many remaining $(d,r)$-strata. Approximate each by
finitely many rays, then take their union. Every ray is eventually
periodic, so these approximations squeeze the upper and lower
logarithmic densities of $E$ to the same value. For $M=1$, take the
single stratum $d=1$; this recovers the multiples theorem. $\square$

**Congruence consequence.** Suppose $q_i\mid Ma_i$ for a fixed $M$.
More generally than in Problem 25, allow repeated moduli and any finite
activation thresholds $T_i$, and set
$$
 B_i=\{n\ge1:n\ge T_i,\ n\equiv a_i\pmod{q_i}\}.
$$
Each $B_i$ satisfies (3): multiplication by $k\equiv1\pmod M$
preserves its congruence and cannot move a positive integer below its
threshold. Hence $B=\bigcup_iB_i$ has the ray approximations above.
For each selected ray $nS_M$, choose one original $B_i$ containing
$n$. That entire ray lies in $B_i$, so any finite ray approximation is
contained in a finite original prefix. The prefixes therefore approximate
$B$ in upper logarithmic density. Its density equals their limiting
periodic density.

For the original activation, this is not a new positive regime:
$q_i\mid Ma_i$ is (2) with $(C,v)=(0,M)$, or equivalently
$a_i/q_i\in\{0,1/M,\ldots,(M-1)/M\}$ for normalized residues.
Likewise Section 8.5's bounded representatives are already covered by
the finitely many pairs $(C,v)=(a,1)$. The multiplier theorem supplies
an alternative structural proof, not a resolution for arbitrary residues.

## Coherent profinite residues: only a partial reduction

If all residues come from one $\alpha\in\widehat{\mathbb Z}$, any modulus
that is a multiple of an earlier modulus is redundant, even with delayed
activation. Thus the modulus set may be replaced by its primitive core.
Its logarithmic density is zero by (1). For each fixed $K$, the union of
its first $K$ activated hits per modulus has harmonic mass at most
$H_K\sum_{q\le X,\ q\in P}1/q=o(\log X)$.
This controls bounded quotients only; it does not prove the full coherent
case.

The later [coherent power-cutoff estimate](coherent_power_cutoff.md) controls
conditioned tails with $q\le n^{1-\eta}$ for every fixed $\eta>0$.
It proves natural density under power-delayed activation, and under the
original activation when the primitive core has counting function
$O(t/\log t)$. Unrestricted coherent residues remain unresolved; the
possible excess is confined to unbounded but subpower quotients.

One cannot simply remove activation for a general profinite $\alpha$.
Choose increasing primes $p_m>m$ with $\sum_m1/p_m<\varepsilon$, and
prescribe $\alpha\equiv m\pmod{p_m}$ by CRT. The fully active integer trace
contains every positive integer. The delayed union instead has natural
density $1-\prod_m(1-1/p_m)\le\varepsilon$, by the summable case.
