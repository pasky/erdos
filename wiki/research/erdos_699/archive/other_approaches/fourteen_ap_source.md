---
name: research/erdos_699/archive/other_approaches/fourteen_ap_source
title: "Erdős 699: a conditional 64/65 bound at index 14"
desc: "The seed 5·13−2^6=1 gives a certified cofactor disjunction when the maximal positions for primes 5, 2, and 13 form a nonconstant arithmetic progression."
created: 2026-09-22T05:46:16Z
updated: 2026-09-22T19:12:28Z
---

# Erdős 699: a conditional 64/65 bound at index 14

***

This is a retained earlier research note. The [[research/erdos_699/_index|current reading guide]] gives the latest status and distinguishes completed proofs from remaining cases.

[[research/erdos_699/_index|P699 research]] ·
[[problems/factorials_binomials/E0699/_index|Erdős problem 699]]

For $p\in\{2,5,13\}$, write
$n-r_p=p^{a_p}u_p$, with $0\le r_p\le13$ and $u_p$ a positive integer.
Suppose the selected positions form a **nonconstant** arithmetic
progression with middle prime 2:

$$
r_5+r_{13}=2r_2,\qquad r_5\ne r_{13}.
$$

Put $h=n-13$. The
[certificate](../../computations/erdos_699_fourteen_ap_source.json)
proves that for $h\ge10^{1\,956\,927\,531}$,

$$\boxed{u_2>h^{.400}\quad\text{or}\quad
u_5>h^{.535}\quad\text{or}\quad u_{13}>h^{.260}.}$$

Indeed,

$$
(n-r_2)^2-(n-r_5)(n-r_{13})=(r_2-r_5)^2
$$

is a nonzero integer of absolute value at most 36. Apply the retained
[bounded-product argument](../../methods/details/ap_cofactors.md) with seed
$65=5\cdot13$, $64=2^6$, auxiliary coefficients $a=b=1$, and Padé
parameter $s=13/10$. The GCD estimate uses $m_0=10^8$ and 4000 interval
terms. It gives the certified value

$$
K>6.94367847019434.
$$

The resulting limiting exponents for primes $2,5,13$ exceed respectively
$0.40105477$, $0.53643074$, and $0.26121309$, leaving positive margins
above the displayed targets. The
[checker](../../computations/erdos_699_fourteen_ap_source.py)
recomputes the exact rational GCD lower bound and the directed-interval
product estimate, including a numerical threshold for $h$.

For the previously examined position assignment
$(r_2,r_3,r_5,r_7,r_{11},r_{13})=(2,5,3,4,0,1)$ with cofactor lower
profile $(.1399,.3453,.2711,.3218,0,.0729)$, the new disjunction forces at
least one of the three relevant exponent coordinates to increase. This
alone does not exclude the entire position case.
It does not apply after exchanging the positions of 11 and 13, giving
$(2,5,3,4,1,0)$. That latter profile remains compatible with every
applicable retained conditional clause in the bounded exploration.
The numerical interpolation objective there remained approximately
$1.131143$, above the value required by that construction.

This is an exploratory limitation of the current approach, not a
counterexample or an impossibility theorem. **Index 14 remains unresolved.**
