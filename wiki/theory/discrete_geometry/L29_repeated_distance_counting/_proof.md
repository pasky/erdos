---
name: theory/discrete_geometry/L29_repeated_distance_counting/_proof
title: Counting shared and disjoint endpoints
desc: Count extensions of equal-side triples and separate equal-length pairs by their number of distinct endpoints.
created: 2026-10-14T15:30:27Z
updated: 2026-10-14T15:30:27Z
---

***

Use the definitions in
[[theory/discrete_geometry/L29_repeated_distance_counting/_index|L29]].
Each of the $I(P)$ triples extends in $n-3$ ways to a bad four-set. Each
four-set contains at most four such triples. Therefore

$$
(n-3)I(P)\le4D(P).
$$

In every bad four-set, choose two distinct unordered pairs of equal
length. If they share an endpoint, their three endpoints are one of the
triples counted by $I(P)$. All four-sets containing any such triple number
at most $(n-3)I(P)$. Otherwise their four endpoints are distinct, and the
equality is counted by $Q(P)$. Each ordered quadruple has only one
underlying four-set, so the number of four-sets of this second type is at
most $Q(P)$. Overlap between the types only enlarges this upper bound.
