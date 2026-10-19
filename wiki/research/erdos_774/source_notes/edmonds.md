---
name: research/erdos_774/source_notes/edmonds
title: "Edmonds: partitioning a matroid into independent sets"
desc: "Source notes for Problem 774: Edmonds: partitioning a matroid into independent sets."
tags: []
sources: []
created: 2026-09-24T22:18:19Z
updated: 2026-10-13T04:56:43Z
---

# Edmonds: partitioning a matroid into independent sets

***

[Read the full Markdown source](../../../../library/additive_combinatorics/edmonds_1965_minimum_partition_matroid_into_independent_subsets/_index.md).

Jack Edmonds, "Minimum partition of a matroid into independent subsets,"
*Journal of Research of the National Bureau of Standards, Section B* 69B
(1965), 67--72.

Edmonds proves the matroid partition criterion: the ground set of a matroid,
which the paper's definition makes finite, can be partitioned into $k$
independent sets exactly when every subset $A$ has rank at least $|A|/k$
(equivalently $|A|\le k r(A)$).  This is the exact matroid analogue of the
implication asked about in E0774.

The theorem sharply identifies what must fail in any counterexample strategy.
If dissociated subsets were the independent sets of a matroid, proportional
extraction would partition every finite subset into boundedly many dissociated
sets, and since dissociation is a property of finite subsets, a compactness
argument would extend this to a finite coloring of the whole infinite set.
Therefore a successful construction must exploit non-matroidal behavior of
signed relations—most concretely, a failure of circuit elimination—or use an
encoding for which ordinary linear/matroid rank does not control dissociated
rank.  Conversely, a positive proof could try to recover enough submodularity
or an approximate partition theorem from the special additive circuit system.
