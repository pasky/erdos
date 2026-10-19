---
name: research/erdos_699/proofs/details/index_14_finite
title: "Erdős 699: the finite range at index fourteen"
desc: "A degree-90 ramp and 400,818 certified intervals exclude every index-fourteen bad triple below 10^15170264, ready to combine with a numerical infinite tail."
created: 2026-09-22T08:44:01Z
updated: 2026-09-22T19:12:28Z
---

# Erdős 699: the finite range at index fourteen

[[research/erdos_699/_index|P699 research]] ·
[[problems/factorials_binomials/E0699/_index|Erdős problem 699]]

***

**Finite-range theorem.** There is no admissible bad triple with $i=14$
and $n\le10^{15\,170\,264}$, for the original threshold $p\ge14$.
The [numerical tail](index_14_numerical_tail.md) now bounds
every possible bad row by $10^{8516269}$, inside this range. Thus index
fourteen is completely excluded. The
[combined checker](../../computations/erdos_699_index_14_complete.py)
binds both parts of this proof.

The [driver](../../computations/erdos_699_index_14_finite.py) and
[output](../../computations/erdos_699_index_14_finite.json) retain the
calculation. This file supplies the finite-range half of the proof; it does
not itself assert a numerical infinite tail.

The retained index-fifteen
[prime-power strip certificate](../../computations/erdos_699_prime_pair_strips_15.json)
applies to every pair among $2,3,5,7,11,13$, to differences at most fourteen,
and to heights through $10^{15\,170\,264}$. It therefore applies to the
index-fourteen numerator factors. Above its explicitly recorded exceptional
heights, each edge gives a cofactor exponent $1/3$.

Use the weighted ramp with $k=9$, degree $90$, and row multiplicities
$m_t=18-t$ for $0\le t<14$. The exact capacity calculation covers all
cofactor witnesses and all collisions of selected prime-power positions.
Weakening the finite exponent to $.3333$ gives minimum gain

$$
\eta=\frac{1199}{400}=2.9975.
$$

Its explicit coefficient comparison gives $n<10^{41}$. The elementary
ramp threshold and every exceptional height in the first strip certificate
are below $10^{41}$. Hence any bad triple in the stated finite range must
already lie below this smaller cap.

The new [six-prime strip certificate](../../computations/erdos_699_prime_pair_strips_14.json)
proves exponent $2/5$ on every pair through $10^{41}$, with difference bound
thirteen. Every exceptional prime-pair solution is kept, and the
[interval engine](../../computations/erdos_699_window_intervals.py)
disables its edge on precisely the corresponding exceptional row windows.

The terminal-prime lemma covers the prefix below row $523$. The remaining
range is partitioned into **400,818 certified intervals**, with no residual
singleton rows and no exact column checks. There are $801,635$ visited nodes,
$127$ active cofactor graphs, and $289$ exceptional row windows. The smallest
certified logarithmic margin is greater than $0.00000309997964345$.

All interval decisions use directed bounds. The output records the interval
partition hash and, as its own run record, the names of both finite
prime-pair inputs. Reproduction uses the pinned
dependencies already used
by the other complete small-index calculations:

```sh
.venv/bin/python wiki/research/erdos_699/computations/erdos_699_index_14_finite.py
```
