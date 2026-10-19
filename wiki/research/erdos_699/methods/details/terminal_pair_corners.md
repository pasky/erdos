---
name: research/erdos_699/methods/details/terminal_pair_corners
title: "Erdős 699: closing a terminal prime-power orthant analytically"
desc: "An independently numerical cofactor estimate can eliminate the last exponent orthant without another large modular inverse."
created: 2026-09-22T18:11:06Z
updated: 2026-09-22T19:12:28Z
---

# Erdős 699: closing a terminal prime-power orthant analytically

[[research/erdos_699/_index|P699 research]] ·
[[research/erdos_699/methods/details/prime_power_strips|Prime-power strips]] ·
[[research/erdos_699/proofs/details/index_7_finite|Finite index seven]] ·
[[research/erdos_699/proofs/details/index_9_finite|Finite index nine]]

***

A weaker **global** cofactor estimate can finish a stronger **finite**
prime-pair calculation. It is enough to show that the remaining exponent
orthant contains no positive solution at the proposed height.

**Lemma.** Fix distinct primes $p,q$, a difference bound $D$, and an
independently proved numerical estimate

$$
|p^a u-q^b v|\le D,\qquad h=\min(p^a u,q^b v)\ge T
\quad\Longrightarrow\quad
u\ge h^\alpha\ \text{or}\ v\ge h^\beta,
\tag{1}
$$

where $u,v$ are positive integers and $0<\alpha,\beta<1$.
Suppose the unhandled exponents satisfy $a\ge A,b\ge B$, and write
$P_0=p^A,Q_0=q^B$. If

$$
\min(P_0,Q_0)\ge\max(T,D),\qquad
P_0>2H^{1-\alpha},\qquad Q_0>2H^{1-\beta},
\tag{2}
$$

then there is no positive solution in this orthant with both heights at
most $H$.

**Proof.** Every such solution has $h\ge\min(P_0,Q_0)\ge T,D$.
Both heights are at most $h+D\le2h$, while $h\le H$. Therefore

$$u\le\frac{2h}{P_0}<\frac h{H^{1-\alpha}}\le h^\alpha,
\qquad
v\le\frac{2h}{Q_0}<\frac h{H^{1-\beta}}\le h^\beta,$$

contradicting (1). $\square$

The global exponents in (1) need not match or exceed the exponent being
certified by the finite strip calculation. The entire remaining orthant
is impossible, so it contributes no exception to that finite calculation.

To apply the lemma after a retained strip computation, its already removed
slabs and boundary lines must cover their unbounded transverse ranges.
The continuation checks establish this: a potentially bad minimal solution
on a boundary with fixed power $P$ has height less than
$2P^{1+s/(s-r)}$. Verifying that this is below the old height cap shows that
neither the old exponent cutoff nor its height filter truncated a boundary.
The saved final exponents then specify exactly the remaining orthant.

There is no circular use of the binomial conjecture. Estimate (1) must be
a numerical theorem about prime powers and arbitrary positive cofactors.
The [retained numerical pair estimates](../../computations/erdos_699_i10_numerical_pairs.json)
provide such statements; their filename refers to an earlier application,
not to an assumption that index ten or any other binomial index is true.
Their difference bound is $100$, covering the bounds six and eight needed
here. Coincident heights are also harmless: coprimality gives $uv\ge h$,
which supplies the relevant alternative when $\alpha+\beta<1$.

For $H=10^K$, conditions (2) require only short directed logarithms:

$$
A\log p>\log2+K(1-\alpha)\log10,\qquad
B\log q>\log2+K(1-\beta)\log10.
$$

The [checker](../../computations/erdos_699_terminal_pair_corners.py)
and [output](../../computations/erdos_699_terminal_pair_corners.json)
verify these conditions against every saved final orthant and every
numerical source threshold. They perform no new modular inversions.
The resulting common extensions of the pair ranges are:

| Existing pair certificate | Pair exponent retained | Common extended height cap |
| --- | --- | ---: |
| Three pairs for index seven | $11/25$ | $10^{149\,273\,239}$ |
| Six pairs for index nine | $41/100$ | $10^{266\,368\,210}$ |

The original exception lists remain sufficient. No new lower-height gap
is introduced: entering the terminal orthant already forces the analytic
source threshold. These additional pair
ranges are available for the same weighted reductions if a larger finite
bridge is needed; the already completed index-seven and index-nine finite
aggregate certificates are not modified here.
