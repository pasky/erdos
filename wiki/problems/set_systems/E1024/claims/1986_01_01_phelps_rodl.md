---
name: problems/set_systems/E1024/claims/1986_01_01_phelps_rodl
title: Phelps and Rödl's order of the independence number
desc: |
  Phelps and Rödl (1986) prove that the largest independent set guaranteed in
  every $3$-uniform linear hypergraph on $n$ vertices has order
  $\sqrt{n\log n}$. The curator credits the paper, which is refereed and
  appeared in Ars Combinatoria.
authors:
- K. T. Phelps
- V. Rödl
status: accepted
claim: answered
scope: full
evidence:
- reviewed
- refereed
submitted: null
links:
- url: https://www.erdosproblems.com/1024
  kind: discussion
created: 2026-10-07T05:59:24Z
updated: 2026-10-08T01:29:59Z
---

***

**Claim.** The function $f(n)$, the largest size of an independent set that
every $3$-uniform linear hypergraph on $n$ vertices must contain, satisfies

$$
f(n)\asymp(n\log n)^{1/2}.
$$

A hypergraph is linear when two edges share at most one vertex, and a set of
vertices is independent when it contains no edge; a $3$-uniform linear
hypergraph is a partial Steiner triple system. The estimate answers the
question as asked, the order of magnitude of $f(n)$, and improves Erdős's
bounds $n^{1/2}\ll f(n)\ll n^{2/3}$ recorded with the problem in [Er71]. The
site credits the two-sided estimate to Phelps and Rödl [PhRo86]. Füredi's
account, in Section 2 of
[[../library/discrete_geometry/furedi_1991_maximal_independent_subsets_steiner_systems_planar_sets/_index|Füredi 1991]],
says that, as a corollary of the Komlós–Pintz–Szemerédi inequality for
partial Steiner systems of girth at least five (J. London Math. Soc. 25
(1982)), Phelps and Rödl proved that every partial Steiner triple system on
$n$ vertices has an independent set of size at least $c\sqrt{n\log n}$ for an
absolute constant $c$, by the probabilistic method, and that this gives the
true order of magnitude of $f(n)$, solving the problem of Erdős and Hajnal.
The upper bound, Steiner triple systems whose independence number is
$O((n\log n)^{1/2})$, is the construction the paper's title names.

**Acceptance.** Refereed: K. T. Phelps and V. Rödl, Steiner triple systems with
minimum independence number, Ars Combin. 21 (1986), 167–172, a journal article.
The citation follows the site's record, with the volume taken from Füredi's
reference list. The record gives the year and no finer date, so the page is
dated to the first day of that year. Reviewed: Thomas Bloom, the site's curator,
labels the problem solved and credits the estimate to Phelps and Rödl. The
site's page listed no comment, proof claim or formalization. Nothing here rests
on this project's own review.
