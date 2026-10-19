---
name: research/erdos_699/archive/previous_bounds/further_effective_bounds
title: "Erdős 699: index 21 is effective, and seven numerical stopping bounds"
desc: "The preceding seven numerical stopping bounds, subsequently closed by complete interval proofs; sharper algebraic constants are retained."
created: 2026-09-22T03:35:00Z
updated: 2026-10-14T00:26:52Z
---

# Erdős 699: index 21 is effective, and seven numerical stopping bounds

***

This is a retained earlier research note. The [[research/erdos_699/_index|current reading guide]] gives the latest status and distinguishes completed proofs from remaining cases.

[[research/erdos_699/_index|P699 research]] ·
[[problems/factorials_binomials/E0699/_index|Erdős problem 699]] ·
[[research/erdos_699/archive/previous_bounds/small_index_effective|Cutoff 26 and the preceding reduction]]

**Completed follow-up.** The [cutoff-15 proof](cutoff_15.md) includes complete exclusions for every index in the table below, as well as $10,13,15,18,20$. This note retains the earlier stopping-bound derivation.

**Index $21$ is effective, and all six previously effective but
numerically uninstantiated cases have explicit stopping bounds.** Every bad
triple with one of the following indices satisfies the stated inequality:

| $i$ | Numerical stopping bound |
| --- | --- |
| $11$ | $n<10^{3\,639\,160\,902}$ |
| $16$ | $n<10^{163\,785}$ |
| $19$ | $n<10^{976}$ |
| $21$ | $n<10^{45\,411\,831}$ |
| $22$ | $n<10^{957}$ |
| $24$ | $n<10^{976}$ |
| $25$ | $n<10^{957}$ |

No unspecified constant occurs in this table. At this stage these were
stopping bounds; their finite ranges had not yet been exhausted. The existing
complete exclusions $i=1,2,17,23$ and $i\ge26$ remain in force.
At this stage the indices at least four still lacking effective stopping bounds were

$$
\boxed{\{4,5,6,7,8,9,10,12,13,14,15,18,20\}.}
$$

Thus this step decreased the previous list of fourteen to thirteen. The separate
cubic finiteness question is unchanged. All assertions use the original
prime threshold $p\ge i$.

## Why index 21 becomes effective

For each small prime, let $P_p$ be the largest power of $p$ dividing a
numerator factor $n-r_p$, and write $n-r_p=P_pu_p$. The bounded differences
between these factors allow Bennett–Filaseta–Trifonov (BFT) to bound the
cofactors $u_p$. Two new certified applications of their Theorem 2.2 give
the additional exponent constraints

$$\max(z_2,z_{17})\ge.3560,\qquad
  \max(z_{17},z_{19})\ge.2176,\qquad
  z_p=\frac{\log u_p}{\log(n-20)},$$

once the effective source thresholds hold. The
[prime-pair note](../other_approaches/more_prime_pairs.md) records the
parameters and interval certificates.

Use the weighted Kummer polynomial

$$
F_{14}(X,Y)=\prod_{a=0}^{13}((X-a)(Y-a))^{14-a}.
$$

Its degree is $210$ and its multiplicity on row $t\le20$ is at least
$28-t$. Combining these multiplicities with the individual cofactor
constraints, rather than just their sum, gives the exact positive gain

$$
G\ge\frac{7683}{5000}=1.5366.
$$

The [weighted-polynomial proof](../../methods/details/weighted_ramps.md)
covers every assignment of the selected positions, including collisions.
It first gives $n<\max\{10^{232},X_{21}+20\}$. For the fully numerical
version, weaker but explicitly instantiated pair estimates still give
$G\ge1711/10000>0$. Their algebraic bound is $10^{2075}$, and their
largest source threshold is below $10^{45\,411\,830}$. The next power
of ten covers the numerator shifts and proves the table's index-21 bound.

## Evaluating the source thresholds

BFT Theorem 2.4 gives a completely explicit threshold if one supplies a
lower bound for the gcd of its Padé coefficients. There are two useful
ways to do this here.

First, the published bounds in BFT Proposition 5.1 suffice for three new
pairs:

| Pair | Cofactor exponent | Valid for every numerator factor at least $10^K-33$ |
| --- | ---: | ---: |
| $2,17$ | $.3259$ | $K=976$ |
| $17,19$ | $.1855$ | $K=957$ |
| $11,23$ | $.1068$ | $K=940$ |

More precisely, each source threshold is strictly below the number in
the last column. The estimates apply for differences at most $100$.
The exact polynomial integrals in Theorem 2.4 are evaluated as rational
numbers, and the remaining operations use directed interval arithmetic.

The $(2,17)$ pair with the original explicit table closes $i=19$ through
the weighted polynomial. All three pairs close $i=24$. For $i=22,25$,
even the unweighted argument suffices: the disjoint pair $(17,19)$ adds
$.1855$ to the old six-prime saving $.913$, giving

$$
\gamma=1.0985>1.
$$

The [complete derivation](../other_approaches/more_prime_pairs.md)
and [weighted certificates](../../methods/details/weighted_ramps.md) give the
four bounds with exponents $957$ or $976$.

Second, at $i=11,16,21$ a new elementary lower bound for the coefficient
gcd improves the published numerical inputs. BFT Lemma 5.2 supplies
disjoint prime intervals whose products divide that gcd. Combining their
Lemma 5.4 estimates for $\theta(x)$ gives a finite rational sum bounding
the gcd for **every** parameter value $m\ge m_0$. Integer square roots
and downward rounding certify this sum. The
[numerical-threshold proof](../../methods/details/bft_numerical_thresholds.md)
derives the uniform estimate and retains all parameters. This is the step
that removes the unevaluated source constants.

## Smaller algebraic terms with the original thresholds

The same work also decreases the earlier computable bounds while keeping
their original source thresholds. Let $X_{11}$ and $X_{24}$ denote exactly
the thresholds in the preceding index-11 and index-24 notes, and let
$X=x_0(33)$ be the original BFT Corollary 2.3 threshold. Then:

| $i$ | Sharpened bound using the same source threshold |
| --- | --- |
| $11$ | $n<\max\{10^{484},X_{11}+10\}$ |
| $16$ | $n<\max\{10^{127},X+33\}$ |
| $19$ | $n<\max\{10^{222},X+33\}$ |
| $22$ | $n<\max\{10^{275},X+33\}$ |
| $24$ | $n<\max\{10^{228},X_{24}+23\}$ |
| $25$ | $n<\max\{10^{370},X+33\}$ |

For example, the index-11 algebraic term decreases from $10^{1525}$ to
$10^{484}$, and the index-24 term from $10^{10000}$ to $10^{228}$.
The improvement keeps the valuation of each individual factor away from
its selected maximum, instead of replacing all of them by the same
factorial bound. The
[index-11 proof](../../proofs/details/index_11_effective.md) checks all 63,360
position/vector patterns with outward rounding; the weighted-polynomial
checker handles the other cases with exact rational and integer arithmetic.

Each numerical bound in the first table and each corresponding bound in
this table holds independently, so their minimum may be used.

## Retained certificates

- [Weighted polynomial and collision checker](../../computations/erdos_699_weighted_ramps.py)
  and [output](../../computations/erdos_699_weighted_ramps.json).
- [Explicit BFT threshold evaluator](../../computations/erdos_699_bft_explicit_thresholds.py)
  and [output](../../computations/erdos_699_bft_explicit_thresholds.json).
- [Uniform coefficient-gcd checker](../../computations/erdos_699_bft_gcd_bounds.py)
  and [output](../../computations/erdos_699_bft_gcd_bounds.json).
- [Refined index-11 constant checker](../../computations/erdos_699_index_11_refined_bound.py)
  and [output](../../computations/erdos_699_index_11_refined_bound.json).

These computations certify analytic parameters and finite systems of proof
inequalities. They do not enumerate binomial rows, and do not claim to
exclude the finite ranges left in the first table.
