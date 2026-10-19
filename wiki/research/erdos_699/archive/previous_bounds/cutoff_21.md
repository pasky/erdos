---
name: research/erdos_699/archive/previous_bounds/cutoff_21
title: "Erdős 699: cutoff 21, further complete cases, and the remaining twelve indices"
desc: "The preceding cutoff-21 proof and eight complete index certificates, retained as inputs to the subsequent cutoff 15."
created: 2026-09-22T04:25:09Z
updated: 2026-10-14T00:26:52Z
---

# Erdős 699: cutoff 21, further complete cases, and the remaining twelve indices

***

This is a retained earlier research note. The [[research/erdos_699/_index|current reading guide]] gives the latest status and distinguishes completed proofs from remaining cases.

[[research/erdos_699/_index|P699 research]] ·
[[problems/factorials_binomials/E0699/_index|Erdős problem 699]]

**Subsequent result.** The [cutoff-15 proof](cutoff_15.md)
completely excludes $10,15,18,20$. The classification below records the
preceding cutoff-21 stage.

**There are no bad triples with $i\ge21$, or with
$i\in\{11,13,16,17,19\}$.** The threshold is the original $p\ge i$.
Together with the earlier cases $i=1,2$, these are complete exclusions
over every admissible row and column.

This improves the preceding cutoff $26$. Eight additional indices are
completely excluded in this step:

$$
11,13,16,19,21,22,24,25.
$$

It does **not** finish every $i\ge4$. The exact remaining classification is:

| Indices | Remaining question |
| --- | --- |
| $15,18,20$ | Only finitely many bad triples are possible, with effectively computable stopping bounds. Their finite ranges have not been excluded. |
| $4,5,6,7,8,9,10,12,14$ | Finiteness is known, but the present investigation still lacks effective stopping bounds. |

Thus twelve indices at least four remain unresolved, of which nine
still have an effectivity gap. The separate case $i=3$ is unchanged.

## How the complete exclusions work

Three improvements fit together.

First, the [asymmetric cofactor argument](../../methods/details/asymmetric_cofactors.md)
retains different exponents for the two endpoints in BFT's Padé proof.
For example, it gives $u_5>x^{.29}$ or $u_7>x^{.20}$ above an explicit
threshold. These alternatives reduce the numerical tail bounds at
$i=11,13,16,21$ to $10^{914},10^{1046},10^{914},10^{1732}$,
respectively. The [exact weighted checker](../../computations/erdos_699_asymmetric_ramp_caps.py)
includes all collisions of maximal small-prime positions.

Second, on an already bounded height range, the
[finite prime-power method](../../methods/details/finite_prime_pairs.md)
proves substantially stronger cofactor estimates. For fixed powers
$P=p^a,Q=q^b$ and a bounded difference $d$, modular inversion supplies
the unique minimal positive solution of $Pu-Qv=d$.
Every other positive solution satisfies the required cube inequality
automatically. Exact exponent-pair enumeration therefore proves

$$
\max(u,v)^3\ge\min(Pu,Qv)
$$

throughout the prescribed height range, apart from explicitly retained
small exceptions. This finite calculation concerns prime-power exponents,
not all integers below the stopping bound. It also works for pairs such
as $7,11$ for which the retained general Padé estimates gave no saving.

Third, those estimates strengthen the local valuation bounds on entire
row intervals. Their summed cofactor exponents often reduce the possible
range again before the interval proof begins. The directed-rounding
interval method then excludes every remaining interval. At two indices,
a few small singleton rows need direct exact gcd checks.

## Complete certificates

| $i$ | Initial numerical stopping bound | Inclusive interval cap | Certified intervals | Exact singleton cases |
| --- | ---: | ---: | ---: | ---: |
| $11$ | $10^{914}$ | $10^{19}$ | $31\,796$ | $11$ |
| $13$ | $10^{1046}$ | $10^{27}$ | $530\,441$ | $40$ |
| $16$ | $10^{914}$ | $10^{41}$ | $100\,204$ | $0$ |
| $19$ | $10^{976}$ | $10^{43}$ | $201\,640$ | $0$ |
| $21$ | $10^{1732}$ | $10^{59}$ | $344\,891$ | $0$ |
| $22$ | $10^{957}$ | $10^{957}$ | $244\,360$ | $0$ |
| $24$ | $10^{976}$ | $10^{61}$ | $312\,701$ | $0$ |
| $25$ | $10^{957}$ | $10^{957}$ | $137\,216$ | $0$ |

There are **1,903,249 certified intervals**, all with strictly positive
logarithmic margins, and 51 exact row/index cases. The latter have
$n\le2060$ and require 11,510 admissible-column gcd checks in total.
After removing the primes below $i$, every checked gcd still exceeds
one. The interval partitions and singleton cases cover the whole bounded
range; the analytic bounds cover the infinite tails.

Detailed proofs and records are retained in:

- [Complete index-eleven proof](../../proofs/details/index_11_complete.md),
  with [certificate](../../computations/erdos_699_index_11_complete.json).
- [Complete index-sixteen proof](../../proofs/details/index_16_complete.md),
  with [certificate](../../computations/erdos_699_index_16_complete.json).
- [Further complete interval proofs](../../proofs/details/further_interval_certificates.md),
  with [four-index records](../../computations/erdos_699_further_intervals.json),
  [index-21 records](../../computations/erdos_699_further_intervals_21.json),
  and [index-13 records](../../computations/erdos_699_further_intervals_13.json).

The preceding complete cases $17,23$ and $i\ge26$ remain inputs. Thus
the new interval proofs give the stated cutoff $21$ and additional cases.
These are computer-assisted mathematical proofs; they have not been
formalized in Lean.

## New effective cases: 15, 18 and 20

The new finite-dimensional interpolation argument supplies nonvanishing,
not merely a polynomial that might vanish at the putative bad pair.

Prescribe the needed Hasse jets at the finite Kummer grid. If symmetric
polynomials through degree $D$ map onto the symmetric jet algebra, let
$T$ denote multiplication by $X+Y$ on that algebra. A rational right
inverse produces integer polynomials of degree at most $D+1$ whose
simultaneous vanishing at $(j,n-j)$ would make $n$ an eigenvalue of $T$.
But all eigenvalues belong to $\{0,\ldots,i-1\}$, the grid's row labels.
Thus at least one polynomial is nonzero throughout the physical region.
The [full lemma](../../methods/details/jet_nonvanishing.md) proves this directly.

Exact modular rank certificates and positive weighted gains give:

| $i$ | Symmetric jet matrix | Modulus | Positive gain |
| --- | --- | ---: | --- |
| $15$ | $16768\times16770$ | $251$ | $43/5000$ |
| $20$ | $2399\times2401$ | $65521$ | $713/5000$ |

Both matrices have full row rank. The
[interpolation proof and constants](interpolation_extensions.md)
give the whole-index bounds

$$\begin{aligned}
i=15:&\quad n<\max\{X_{15}+15,10^{1\,100\,000\,000}\},\\
i=20:&\quad n<\max\{X_{20}+20,10^{4\,000\,000}\}.
\end{aligned}$$

Here the $X_i$ are the specified, effectively computable BFT thresholds.
The explicit powers of ten bound all polynomial coefficients and
elementary losses. No exceptional algebraic curve remains.
The same lemma first gave the numerical bound $10^{56000}$ at index 13;
the subsequent simpler asymmetric argument and interval proof exclude
that index completely.

At index $18$, two asymmetric alternatives improve the weighted
polynomial $F_{12}$ enough to give gain $186/625$. The
[index-18 proof](../../proofs/details/index_18_effective.md) verifies all 65
cofactor vectors and 5707 collision cases, giving

$$
n<\max\{X_{18},10^{2\,405\,782}\}+17.
$$

Its algebraic term is only $10^{814}$; the displayed larger term includes
the explicit asymmetric source thresholds. The remaining $X_{18}$ is
effectively computable as specified in that proof.

## What remains difficult below 15

At $i=4,5$, an elementary endpoint argument completely excludes
additional congruence classes:

$$i=4\Longrightarrow4\mid n\ \text{or}\ 9\mid n,
\qquad
i=5\Longrightarrow8\mid n\ \text{or}\ 9\mid n$$

for any bad triple. The [proof and exact finite certificate](../../remaining/details/indices_4_5_row_zero.md)
reduce the complementary classes to finitely many rational slopes and
divisors of fixed constants.

The remaining cases include nearby integers
$n=2^a u$, $n-1=3^b v$ with both cofactors unbounded. The present
cofactor estimates and interpolation constructions do not give a
positive uniform exponent in every such case. In particular, the
results above do not establish the conjecture for all $i\ge4$.
