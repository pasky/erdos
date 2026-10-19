---
name: research/erdos_409
title: Basins and step counts of the totient-plus-one map
desc: |
  The known exceptional-prime theorem gives almost every prime the basin
  {p,2p}. An affine obstruction rules out periodic cofactor inverse chains
  and cofactors eventually at most 9, but leaves the exceptional basins
  and the asymptotic order of step counts open.
problems:
- 409
created: 2026-10-15T05:22:42Z
updated: 2026-10-18T03:09:12Z
---

# Basins and step counts of the totient-plus-one map

[[research/_index|..]]

***

This folder's results that are not drawn from a cited source are Plasma
AI's, credited to Plasma AI.

## Target

[[problems/arithmetic_functions/E0409/_index|Problem 409]], status open.
Put $T(n)=\varphi(n)+1$ and let $F(n)$ be the number of applications of
$T$ needed to reach a prime from $n$. The problem asks how large $F(n)$ is,
whether infinitely many $n$ reach the same prime, and what the density of
the $n$ reaching a fixed prime is. The basin of a prime $p$ is the set of
$n$ whose orbit reaches $p$. erdosproblems.com reads the first question as
asking for good upper bounds on $F(n)$; the formal-conjectures statement
asks for the order of $F$, for a prime with an infinite basin, and for the
density of each basin.

## What is established

Every orbit reaches a prime, and
[[research/prime_basins_phi_plus_one|the basin page]] proves
$F(n)\le4(\sqrt n-\sqrt2)$ for $n\ge2$ and computes the complete basins of
the primes up to $11$, all finite. These are author-recorded and elementary,
and the [[research/leads/totient_plus_one_small_basins/_index|small-basins lead]]
records them; the square-root bound also appears on the problem's forum thread.

Banks, Ford, Luca, Pappalardi and Shparlinski, *Values of the Euler Function
in Various Sequences* (2005), [[../library/arithmetic_functions/banks_et_al_2005_values_euler_function_various_sequences/theorem_4_1|Theorem 4.1]]
([author manuscript, pp. 14–15](https://www.ford126.web.illinois.edu/wwwpapers/philam.pdf),
accessed 2026-10-15),
prove that outside at most $x/(\log x)^{2+o(1)}$ primes $p\le x$ the only
solutions of $\varphi(n)=p-1$ are $p$ and $2p$. The source states the
almost-all-primes consequence explicitly. Its definition and proof were
read; its underlying sieve and totient-counting theorems are taken as
published inputs.

[[theory/number_theory/L104_shifted_prime_totient_fibers/_index|L104]]
records the elementary basin consequence, at tier 0: $2p$ has no
predecessor, so these primes have exactly the basin $\{p,2p\}$. Thus for
almost every prime the infinitude question has the answer no and the
density question the answer zero. This is an application of the 2005
counting theorem, not a new exceptional-prime estimate. Its proof also
records a weaker-count reconstruction using the same largest-prime split.

The forum thread records further claims, listed on the problem page with
their standing. One of them, by the account ankit
([[problems/arithmetic_functions/E0409/claims/2026_07_22_ankit|its claim page]]), treats the primes
$p\equiv3\pmod4$ by $2$-adic valuation with only $O(\sqrt x)$ exceptions;
Plasma AI rederived it. The 2005 theorem treats all residue classes with a
weaker exception count. The same comment reports exact finite basins for
all primes below $30000$ and observes that Dickson's prime $k$-tuples
conjecture makes $F$ unbounded through chains with
$q_{i+1}=(3q_i+1)/2$, where
$T(3q_{i+1})=2q_{i+1}-1=3q_i$ when $q_{i+1}\ne3$. These computations were
not checked here. OEIS A229487 lists the conjectured largest element of
each basin.

## The structure of the inverse forest

The basins partition the positive integers. After removing the prime's
fixed loop, each is a finite-branching tree under $T^{-1}$: if $T(n)=m$,
the elementary inequality $\varphi(n)\ge\sqrt{n/2}$ bounds
$n\le2(m-1)^2$. An even number at least $4$ is never a value of $T$,
since $\varphi(n)$ is even for $n\ge3$, so even numbers are leaves. A basin
is infinite exactly when it contains an infinite backward chain
$p=m_0\leftarrow m_1\leftarrow m_2\leftarrow\cdots$ with $m_i$ odd
composite for $i\ge1$ and $\varphi(m_{i+1})=m_i-1$. This follows from
finite branching and König's lemma; the chain increases strictly.

The prime-density statement is weak in the units of the basin question.
The union of all two-element basins is contained in the primes and twice
the primes, and hence has natural density zero. Almost every integer
terminates at one of the exceptional primes. That gives neither
infinitude nor positive density for any single basin: a countable union
of finite sets can have density one.

Nor does the global density of totient values determine the distribution
of children of a node already reached in the inverse tree. Conditioning
on a node being a totient plus one and on its earlier ancestors changes
that distribution, and children share the same totient value. A model
based on uniform integers at each generation has no established transfer
to this conditional law. The reported numerical branching data on the
forum do not repair that missing transfer. No finiteness or survival
conclusion is drawn from such a model here.

## Discriminating step and stop rule

The discriminating step is to test whether the finite prime-chain
construction extends to one fixed terminal prime, or whether its affine
structure instead forces every backward chain in a useful class to
terminate. Write $a_i=m_i/P^+(m_i)$ for the cofactor left after deleting
the largest prime once. When that prime is coprime to $a_i$, the exact
inverse map for a fixed cofactor $a$ is

$$
f_a(t)=\frac{a(t+\varphi(a)-1)}{\varphi(a)}.
$$

The one-iteration stop rule is to continue only with a lemma controlling
**every** backward chain from an infinite explicit class of exceptional
primes, or an infinite chain under a stated substantive hypothesis. A
restriction on one pattern of cofactors is useful but does not by itself
meet this test. Finite inverse-tree enlargement is not a substitute.

## The affine obstruction and its limit

[[theory/number_theory/L105_totient_inverse_chain_cofactors/_index|L105]],
an unconditional tier-0 deduction, gives a quantitative obstruction. For
a block of odd cofactors $a_1,\ldots,a_r\ge3$, compose their maps to obtain
$F(t)=(At+B)/D$ with $A$ odd, $D$ even, $A>D$, and $B>0$. Then

$$
J(F^k(t))=\left(\frac AD\right)^kJ(t),\qquad
J(t)=(A-D)t+B>0.
$$

Integer endpoints require $k\,v_2(D)\le v_2(J(t))$. An infinite chain
therefore cannot have an eventually periodic cofactor sequence. For
$a=3$ the formula becomes
$f_3^k(t)+3=3^k(t+3)/2^k$, and an odd endpoint requires
$k\le v_2(t+3)-1$. The fixed-root chain stops even before imposing
primality. Dickson's conjecture can provide longer finite chains as the
root varies; it does not interchange the quantifiers to give one prime
with chains of every length.

L105 also proves that an infinite chain must have cofactor at least $11$
infinitely often. For cofactors $3,5,7,9$, a necessary residue test permits
only transitions that become constant, which the preceding bound
excludes. This does not generalize by the same table: $7$ and $11$ can
each follow the other and themselves under the necessary test. A
nonperiodic sequence may change blocks before any fixed-block bound is
exhausted, and arbitrarily large cofactors are another possibility.

The test stops here. Neither an infinite chain nor a class of exceptional
terminal primes for which **all** chains satisfy the excluded restrictions
has been obtained. Thus L105 is a retained obstruction to a particular
construction, not a resolution of an exceptional basin and not grounds
for repeating the same test or extending a census.

Reopen this route on a bound that applies to arbitrary cofactor words
from a specified infinite class of roots, or on a construction of
arbitrarily deep compatible inverse chains from one fixed prime. The
latter would yield an infinite chain by finite branching. A count or a
prime-tuple conjecture with the root allowed to change does not supply
this input. A density argument would additionally need uniform control of
the integers in one fixed basin up to a height, beyond mere infinitude.

## Open gaps

- Infinite basins: the exceptional-prime theorem and L105 do not control
  arbitrary inverse chains from any new fixed exceptional prime.
- Step counts: no upper bound of the form $F(n)=o(\sqrt n)$ is established
  here. A slow step requires an integer with large least prime factor;
  prime squares and balanced semiprimes are the limiting cases in the
  elementary descent estimate. Two prime-square steps are never
  consecutive, because $q^2-q+1$ lies strictly between $(q-1)^2$ and
  $q^2$ for $q\ge2$. This observation alone does not improve the
  asymptotic order. No estimate for the length of arbitrary strings of
  balanced-semiprime steps has been obtained.
- Unboundedness of $F$: the forum gives the conditional prime-tuple
  construction above; no unconditional construction is established here.

The retained deductions are author-recorded. The external source theorem
has its published standing; the forum claims and computations keep their
separate, unreviewed standing. No independent acceptance, infinite basin,
positive-density basin, or resolution of Problem 409 is asserted.
