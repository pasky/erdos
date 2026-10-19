---
name: research/erdos_25/translation_dynamics
desc: A translation-dynamical dichotomy between uniform convergence and Haar-null, comeager logarithmic irregularity.
tags: [dynamics, reductions, partial-results]
sources: []
created: 2026-09-22T02:51:13Z
updated: 2026-09-24T22:13:01Z
---


# research/erdos_25/translation_dynamics

***

This is a different approach from the previous compression and first-kill
arguments. It treats the simultaneous translation of every residue as a
dynamical parameter. The resulting dichotomy is proved, but neither of
its alternatives has been established universally for singleton systems.

## The dichotomy

Fix a family $C_q=[a_q]_q$ and let $G=\widehat{\mathbb Z}$ with Haar
probability $\mu$. Put
$$
 U=\bigcup_q C_q,\qquad \beta=\mu(U).
$$
For $z\in G$, translate every residue by $z$ and retain the original
activation thresholds. Thus
$$
 B_z=\{n\ge1:\exists q\le n,\ n-z\in C_q\},\qquad
 F_N(z)=\frac1{H_N}\sum_{\substack{n\le N\\n\in B_z}}\frac1n.
$$
Each $F_N$ is continuous, indeed locally constant, on $G$. Define
$$
 \Lambda=\limsup_{N\to\infty}\max_{z\in G}F_N(z).
$$

**Theorem.** For Haar-almost every $z$, $B_z$ has natural density $\beta$.
For a comeager set of $z$ (one containing a countable intersection of
dense open sets),
$$
 \liminf_N F_N(z)=\beta,\qquad \limsup_N F_N(z)=\Lambda.
 \tag{1}
$$
Consequently exactly one of the following holds:

- $F_N\to\beta$ uniformly over all $z\in G$;
- the shifts for which logarithmic density fails form a Haar-null,
  comeager set.

The theorem also permits multiple residues at each modulus. It therefore
does not itself capture the singleton restriction needed for Problem 25.

## Uniform lower envelope and directed shifts

Write $U_{\le k}=\bigcup_{q\le k}C_q$ and $\beta_k=\mu(U_{\le k})$.
Every fixed finite delayed prefix has harmonic averages tending to
$\beta_k$, uniformly in $z$: there are only finitely many translations
modulo its common period. Since every $B_z$ contains that prefix,
$$
 \liminf_N\min_zF_N(z)\ge\beta.
$$
On the other hand, Haar translation invariance gives exactly
$$
 \int_G F_N(z)\,d\mu(z)
 =\frac1{H_N}\sum_{n\le N}\frac{\beta_n}{n}\le\beta.
$$
Thus
$$
 \min_zF_N(z)\longrightarrow\beta.
 \tag{2}
$$
In particular every individual lower limit is at least $\beta$.

The elementary shift relation is one-sided:
$$
 B_z+b\subseteq B_{z+b}\qquad(b\in\mathbb Z_{\ge0}).
$$
Indeed a class active at $n$ is still active at $n+b$. For any
$S\subseteq\mathbb N$,
$$
 0\le H_S(N)-H_{S+b}(N)\le H_{\min(b,N)}.
$$
This follows by subtracting the two weights of each $n\in S$; all
differences are nonnegative, and their sum over all integers is
$H_{\min(b,N)}$. With $H_0=0$, it follows that
$$
 F_N(z+b)\ge F_N(z)-\frac{H_b}{H_N},\qquad
 F_N(z-b)\le F_N(z)+\frac{H_b}{H_N}.
 \tag{3}
$$
Only the bound for fixed $b$ is needed below.

## Generic shifts attain the uniform extremes

Fix $\varepsilon>0$ and $N_0$. The sets
$$
 \bigcup_{N\ge N_0}\{z:F_N(z)>\Lambda-\varepsilon\},\qquad
 \bigcup_{N\ge N_0}\{z:F_N(z)<\beta+\varepsilon\}
 \tag{4}
$$
are open and dense.

To verify density of the first, fix a basic open neighborhood
$z\equiv r\pmod L$. For arbitrarily large $N$, some $z_N$ satisfies
$F_N(z_N)>\Lambda-\varepsilon/2$. There is a positive representative
$b\in\{0,\ldots,L-1\}$ for which $z_N+b$ lies in that neighborhood.
For sufficiently large $N$, (3) loses less than $\varepsilon/2$.
This proves density. For the second, choose a minimizer with
$F_N(z_N)\le\beta$, which exists by the integral bound. Move it into
the neighborhood using a nonpositive shift of magnitude at most $L-1$,
and use the other inequality in (3).

Baire's theorem, applied to (4) for all integer $N_0$ and positive
rational $\varepsilon$, now proves (1). The reverse inequalities follow
from (2) and the definition of $\Lambda$. If $\Lambda=\beta$, (2) and
the uniform upper envelope give uniform convergence. If $\Lambda>\beta$,
the comeager set in (1) consists of irregular shifts.

## Almost every shift: an elementary maximal argument

No pointwise ergodic theorem is needed for the measure assertion. We use
the following periodic maximal inequality. If $g\ge0$ is periodic with
period $L$ and mean $m$, then the proportion of starting residues $a$
for which
$$
 \sup_{N\ge1}\frac1N\sum_{n=0}^{N-1} g(a+n)>\varepsilon
$$
is at most $2m/\varepsilon$.

If $m>\varepsilon$ this is immediate. Otherwise any witnessing interval
can be reduced modulo $L$ to one of length at most $L$, still with mean
greater than $\varepsilon$. For the bad starting positions in one period,
greedily select the leftmost uncovered starting position $a$ and one such
half-open interval $[a,a+\ell)$. The selected intervals are disjoint,
cover all bad starting positions, and lie within $[0,2L)$. Their total length is at
most $2Lm/\varepsilon$, which bounds the number of bad starts.

Fix $k$ and let $V_k=U\setminus U_{\le k}$. Its indicator is the
increasing limit of periodic indicators
$\mathbf1_{U_{\le j}\setminus U_{\le k}}$. Strict-threshold maximal
events pass to this increasing limit, so
$$
 \mu\left\{z:\sup_N\frac1N
       \sum_{n=1}^N\mathbf1_{V_k}(n-z)>\varepsilon\right\}
 \le\frac{2(\beta-\beta_k)}\varepsilon.
 \tag{5}
$$
The finite-prefix part of the full trace of $U$ has density $\beta_k$
at every $z$. If the full trace has upper density greater than
$\beta+\varepsilon$, its $V_k$ part has upper density greater than
$\varepsilon$. Its exceptional measure is therefore bounded by (5)
for every $k$, hence is zero. Finite prefixes also bound its lower
density below by $\beta$ at every $z$.

Thus the full trace of $U$ has natural density $\beta$ almost surely.
The delayed union lies between its fixed finite delayed prefixes and
the full trace, so it has the same density almost surely. This completes
the dichotomy proof.

## Ordinary integer shifts preserve logarithmic behavior

There is an additional exact obstruction to replacing Haar randomness
by a fixed ordinary integer translation. For every fixed $z$ and integer
$b$, $B_z$ and $B_{z+b}$ have the same lower and upper logarithmic
densities.

It suffices to prove this for $b=1$. Let
$$
 D_z=\{q:a_q+z\equiv-1\pmod q\},
$$
and let $P_z$ be its minimal generators under divisibility, a primitive
set. Any point newly admitted to the deletion set by the earlier
activation in $B_{z+1}$, compared with $B_z+1$, must be $n=q$ for some
$q\in D_z$. If a proper divisor $d\in D_z$ divides $q$, then
$n-1=q-1\equiv-1\pmod d$ and $q-1\ge d$, so that older class already
deletes $n-1$. Consequently
$$
 B_{z+1}\setminus(B_z+1)\subseteq P_z.
$$
Primitive sets have logarithmic density zero by the established multiples
theorem, and physical translation by one changes the harmonic sum by at
most one. Hence $F_N(z+1)-F_N(z)\to0$. Iteration proves the assertion
for any fixed integer $b$.

Thus, if one center is exceptional, its entire dense integer orbit is
exceptional. Almost-everywhere regularity cannot repair it by choosing
a fixed integer shift.

## What this changes, and what it does not

For a fixed family, it is enough for a negative construction to find
arbitrarily late translated finite-prefix peaks with a fixed excess over
$\beta$. The centers need not be compatible between peaks: (3) and Baire's
theorem produce one center exhibiting oscillation. The missing condition
is still a positive *normalized* harmonic excess, not a bounded finite
anomaly.

In particular, any original excess
$\overline{\operatorname{ld}}(B_0)>\beta$ produces an oscillating common
profinite translate of the **same entire family**. Unlike the earlier
[subfamily extraction](basic_reductions.md#why-the-finite-periodic-candidate-is-the-right-universal-target),
this preserves all moduli and all compatibility relations between the
full cylinders, as well as their Haar union measure.

Conversely, proving existence at every common profinite shift of one
family would automatically prove uniform convergence over those shifts.
Almost-sure existence is much weaker: it holds even for multi-residue
families and allows a comeager exceptional set.

No uniform upper bound $\Lambda\le\beta$ has been obtained for arbitrary
singleton families. The finite-sharp counterexamples have only bounded
harmonic excess and do not supply the peaks required here.

The same dichotomy also holds for ordinary counting averages: replace
$F_N$ by $|B_z\cap[1,N]|/N$ and $H_b/H_N$ in (3) by $b/N$.
