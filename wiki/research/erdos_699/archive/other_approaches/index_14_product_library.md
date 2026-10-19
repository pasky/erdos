---
name: research/erdos_699/archive/other_approaches/index_14_product_library
title: "Erdős 699: additional product constraints at index fourteen"
desc: "Nine numerical constant-gap product bounds strengthen the cofactor restrictions involving 11 and 13. Whole-index effectivity remains unresolved."
created: 2026-09-22T06:42:00Z
updated: 2026-10-13T05:28:09Z
---

# Erdős 699: additional product constraints at index fourteen

***

This is a retained earlier research note. The [[research/erdos_699/_index|current reading guide]] gives the latest status and distinguishes completed proofs from remaining cases.

[[research/erdos_699/_index|P699 research]] ·
[[research/erdos_699/methods/details/product_thresholds|Numerical product thresholds]] ·
[[research/erdos_699/archive/other_approaches/index_14_boundary|Forced boundary divisors]]

The retained index-fourteen interpolation profiles can be strengthened by
constant-gap identities involving the primes 11 and 13. This note records
nine additional, fully numerical sources. They do not establish effectivity
for the whole index: the alternatives still require complete geometric
coverage, and some profiles remain compatible with these inequalities.

Choose the maximal small-prime positions $r_p\in\{0,\ldots,13\}$ and put

$$
u_p=(n-r_p)/p^{v_p(n-r_p)},\qquad h=n-13.
$$

A row in the following table applies when its two position sums are equal
and its two unordered position pairs are different. The conclusion is the
**disjunction** $u_p>h^{e_p}$ for at least one of the listed primes. All
terminating decimals denote exact rationals.

| Position identity | Prime order | Exponents $(e_p)$ | Seed difference |
| --- | --- | --- | --- |
| $r_2+r_5=r_3+r_{13}$ | $2,3,5,13$ | $.3139,.6365,.4685,.1542$ | $40-39=1$ |
| $r_2+r_{11}=r_3+r_{13}$ | $2,3,11,13$ | $.3325,.3651,.5376,.5055$ | $352-351=1$ |
| $r_3+r_{13}=r_7+r_{11}$ | $3,7,11,13$ | $.6399,.3638,.2165,.1621$ | $2\cdot39-77=1$ |
| $r_2+r_{11}=r_5+r_{13}$ | $2,5,11,13$ | $.2989,.4569,.5949,.1356$ | $4225-6\cdot704=1$ |
| $r_2+r_{13}=r_5+r_7$ | $2,5,7,13$ | $.2982,.4564,.3431,.1348$ | $3\cdot35-104=1$ |
| $r_2+r_{13}=r_3+r_5$ | $2,3,5,13$ | $.7611,.4349,.4481,.1216$ | $676-675=1$ |
| $r_2+r_{11}=r_7+r_{13}$ | $2,7,11,13$ | $.2998,.3447,.1929,.1369$ | $91-88=3$ |
| $r_3+r_{11}=r_5+r_{13}$ | $3,5,11,13$ | $.6172,.4402,.167,.1091$ | $2\cdot33-65=1$ |
| $r_2+r_{11}=r_5+r_7$ | $2,5,7,11$ | $.3841,.2853,.5671,.4671$ | $176-175=1$ |

Every row is valid for

$$
h\ge10^{3\,297\,191\,195}.
$$

The individual thresholds are smaller and are retained in the
[directed interval certificate](../../computations/erdos_699_fourteen_product_library.json).
The [checker](../../computations/erdos_699_fourteen_product_library.py)
reconstructs the seed components, certifies their coefficient-gcd estimates,
and applies the general numerical product bound. Its only dependency beyond
the Python standard library is the retained `mpmath` requirement.

For example, the third row uses

$$
2(3\cdot13)-7\cdot11=1,\qquad s=16/11.
$$

If $r_3+r_{13}=r_7+r_{11}$, the products

$$
(n-r_3)(n-r_{13}),\qquad(n-r_7)(n-r_{11})
$$

have a nonzero constant difference of magnitude at most $13^2$. The
quadratic-product Padé estimate gives the stated four-way alternative.
It excludes the previous profile

$$(e_2,e_3,e_5,e_7,e_{11},e_{13})
=(.1399,.3453,.2711,.3218,0,.0729)$$

at positions $(r_2,r_3,r_5,r_7,r_{11},r_{13})=(2,5,3,4,1,0)$.
This is an exclusion of that limiting cofactor profile. Each resulting
larger-cofactor branch still needs its own polynomial inequality before a
whole-index conclusion can be drawn.

A broader exploratory catalog found many more possible sources, but is
not being promoted as a proof of index fourteen. In particular, simply
counting old profile vectors that violate a new alternative is insufficient:
new componentwise minimal vectors must be recomputed after adding the
alternative. The finite position assignments are also prime-labeled; a
sorted capacity comparison cannot transfer a position identity to another
assignment of primes.
