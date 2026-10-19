---
name: theory/covering_systems/L13_useful_supply_obstruction
title: A strict useful-supply obstruction to distinct covers
desc: |
  Capping each prime-power cylinder's supply at its deficit gives an
  explicit sufficient obstruction for all distinct nonunit-divisor profiles.
tags: []
sources: []
id: L13
statement: |
  Let N>1 be an integer and let p be a prime divisor of N. Put a=v_p(N),
  M=N/p^a, S=sigma_1(M)=sum_{d|M}d, and D=2M-S, and assume D>0.
  Define
  U=S*(p^a-1)/(p-1)
    -sum_{1<=j<=a, m|M, M/m>D}(M/m-D)*p^(a-j).
  In the full profile with one arbitrarily placed residue class for each
  divisor n>1 of N, no placement gives incidence mass at least M in
  every cylinder modulo p^a if U<D*p^a. Consequently, under that strict
  inequality, no finite family of congruence classes with pairwise
  distinct moduli greater than one dividing N covers all integers.
  There is no restriction on the number of prime divisors of N, their
  exponents, or pointwise multiplicity. Repeated moduli are excluded.
status: proved
tier: 0
depends_on: []
created: 2026-09-09T02:22:43Z
updated: 2026-10-14T07:06:52Z
---

# A strict useful-supply obstruction to distinct covers

[[theory/covering_systems/_index|..]]

[[theory/covering_systems/L13_useful_supply_obstruction/_proof|_proof]]: Exact class-support counts and a pointwise forced-excess bound limit
the total supply available to meet all prime-power cylinder deficits.

***

Let $N>1$ be an integer and $p\mid N$ a prime. Write

$$
a=v_p(N)\ge1,\qquad M=N/p^a,\qquad
S=\sigma_1(M)=\sum_{d\mid M}d,\qquad D=2M-S.
$$

In particular, $\gcd(p,M)=1$. The notation $\sigma_1$ denotes the
positive-divisor sum; it is not an excess-mass variable. Assume $D>0$.

The full distinct nonunit-divisor profile contains one residue class
$b_n(n)=b_n+n\mathbb Z$ for each divisor $n>1$ of $N$, with every $b_n$
chosen freely. Each modulus occurs once, and modulus one is excluded.

## Statement

Define

$$
U=S\frac{p^a-1}{p-1}
-\sum_{\substack{1\le j\le a,\ m\mid M\\M/m>D}}
  (M/m-D)p^{a-j}.
$$

If

$$
U<Dp^a,
$$

no placement of the full profile has incidence mass at least $M$ in
every cylinder modulo $p^a$ inside $\mathbb Z/N\mathbb Z$.
Consequently no family of congruence classes with pairwise distinct moduli
$n>1$ dividing $N$ can cover all integers. The family may use all or only
some of those moduli.

This is a sufficient exclusion criterion for every finite prime support
and every choice of exponents. There is no oddness assumption and no cap
on pointwise multiplicity. It does not assert that the strict inequality
holds for every $N$ or every prime divisor $p$.

## Meaning of the bound

Every cylinder modulo $p^a$ contains $M$ points. The full profile's
classes with moduli coprime to $p$ contribute incidence mass $S-M$ in
each cylinder, independently of their residues. Covering therefore
requires the classes whose moduli are divisible by $p$ to contribute at
least $D$ in each cylinder.

A class of modulus $p^jm$, where $1\le j\le a$ and $m\mid M$,
contributes $M/m$ on exactly $p^{a-j}$ cylinders. Contributions greater
than $D$ already exceed the required threshold on each cylinder they
meet. Subtracting this forced excess from their total mass gives $U$.
Equivalently,

$$
U=\sum_{j=1}^a\sum_{m\mid M}\min(M/m,D)p^{a-j}.
$$

The [proof](_proof.md) defines useful supply as incidence mass capped at
$D$ in each cylinder. The subtracted waste is excess relative to that
threshold, not a count of points wasted in an actual cover. This
distinction permits the argument without any overlap or rigidity
assumption.

Adding omitted classes does not decrease any cylinder mass. Thus failure for
the full profile implies failure for every distinct subprofile. Repeated
moduli do not obey the fixed inventory used to compute $U$, and are
outside the conclusion. Exclusion of a one-cover also excludes any higher
covering multiplicity within the same distinct-modulus domain.

## Boundaries and standing

The guards are strict: when $D\le0$, or when $D>0$ but $U\ge Dp^a$,
this criterion gives no exclusion. In particular, $U=Dp^a$ is not a
contradiction. Failure of the criterion establishes neither a cover nor
feasibility of the cylinder constraints. The proof includes the valid
boundary $M=1$, when the frame is a pure prime power.

The complete proof and its subprofile consequence are author-recorded at
tier 0, with no independent whole-claim acceptance or formal verification.
They use only finite counting, the elementary coprime congruence argument
given in the proof, and a finite geometric sum. No other native claim or
source-result premise is consumed. No novelty, prior-art assessment, or
resolution of an erdosproblems.com problem is asserted.

The supplied proof has no identified gap. Its verification requires only
this statement and [proof](_proof.md), with no mathematical programs,
numerical grids, or private inputs.
