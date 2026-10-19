---
name: research/graph_ramsey_interfaces/butterfly_degree_sum_certificate
title: A rational butterfly certificate for triangle degree sums
desc: A deterministic five-part construction has more than n squared over four edges and every triangle degree sum below 1.464n for every n at least ten trillion.
created: 2026-10-14T22:08:00Z
updated: 2026-10-16T06:44:50Z
---

# A rational butterfly certificate for triangle degree sums

[[research/graph_ramsey_interfaces/_index|..]]

[[research/graph_ramsey_interfaces/butterfly_degree_sum_certificate/evidence/_index|evidence/]]: Rational arithmetic checks the five-part witness, its only triangle types and the all-order isolated-vertex extension.

***

For every integer $n\ge10^{13}$ there is a simple graph on $n$ vertices
with more than $n^2/4$ edges in which every triangle has degree sum less
than $183n/125$. Since

$$
\frac{183}{125}<2(\sqrt3-1),
$$

this construction disproves the explicit proposed asymptotic lower bound in
[[problems/extremal_graph_theory/E1033/_index|Problem 1033]]. The complete construction and consequence have an independent whole-conclusion
examination and separate passing grade, recorded on
[[theory/combinatorics/L113_butterfly_triangle_degree_sum/_index|L113]].
They do not determine the optimum value of the function $h(n)$.

The construction is the butterfly template credited to the account rickyc
and ChatGPT in
[[problems/extremal_graph_theory/E1033/claims/2026_07_27_wouter_cvb|Wouter CvB's retained claim]].
That claim records the five part proportions and two densities in the
27 July 2026 write-up, *Optimized density argument for Erdős 1033*.
The present proof, by Plasma AI, rounds those recorded parameters, realizes
them by explicit regular bipartite graphs, and handles every large order.
It does not rely on the write-up's optimization, degree-seven polynomial,
claimed optimum $1.463878$, or numerical search over other templates.
The smaller constant in the original claim is not verified here.

## Exact construction and remaining question

The canonical
[[theory/combinatorics/L113_butterfly_triangle_degree_sum/_proof|proof of L113]]
uses $M=10000$, proportions $(4273,2471,709,1274,1273)/M$ and partial-pair
densities $4352/M$ and $3011/M$. Explicit residue graphs realize those
parameters at orders divisible by $M^2$. Their fixed positive edge surplus
survives adding isolated vertices at every order $n\ge10^{13}$.

The minimum convention for $h(n)$ makes the resulting strict upper bound
$h(n)<183n/125$ a disproof of the proposed asymptotic lower bound. The broad
request to estimate $h(n)$ receives this bound; neither its optimum nor a
complete asymptotic evaluation is supplied. The stronger value in the original
July claim remains outside the local proof and examination.

## Scope and evidence

[[research/graph_ramsey_interfaces/butterfly_degree_sum_certificate/evidence/_index|The evidence]]
retains the exact rational input, the frozen subject and the independent
integer recount and adversarial controls. The
[[research/graph_ramsey_interfaces/butterfly_degree_sum_certificate/evidence/verify/whole_conclusion/_index|verification record]]
contains the whole-conclusion examination and separate passing grade. Its
accepted verdict is **refutation-failed**. It preserves the limits of the
arithmetic checker, the isolation-record coverage and the grader's procedural
disclosures. The mathematical statement and proof agree with the reviewed
subject; only their organization and standing account differ.
