---
name: problems/extremal_graph_theory/E1066
title: Problem 1066
desc: |
  Asks to estimate $g(n)$, the largest $g$ such that every graph on $n$ points
  in the plane at pairwise distance at least $1$, with edges joining the pairs
  at distance exactly $1$, has an independent set of size $g$.
tags:
- Graph theory
- Planar graphs
status: open
claim: none
created: 2026-09-04T09:17:27Z
updated: 2026-10-15T01:58:15Z
---

# Problem 1066

[[problems/extremal_graph_theory/_index|..]]

***

**Statement.** Let $G$ be a graph given by $n$ points in $\mathbb{R}^2$, where
any two distinct points are at least distance $1$ apart, and we draw an edge
between two points if they are distance $1$ apart.

Let $g(n)$ be maximal such that any such graph always has an independent set on
at least $g(n)$ vertices. Estimate $g(n)$, or perhaps $\lim \frac{g(n)}{n}$.

**Status.** Open.

**Source.** [erdosproblems.com/1066](https://www.erdosproblems.com/1066),
accessed 2026-09-04. Cite as: T. F. Bloom, Erdős Problem #1066,
https://www.erdosproblems.com/1066.

**References.**

- [Cs98] Csizmadia, G., On the independence number of minimum distance graphs.
  Discrete Comput. Geom. (1998), 179-187.
- [PaTo96] Pach, János and Tóth, Géza, On the independence number of coin
  graphs. Geombinatorics (1996), 30-33.
- [Po85] Pollack, R., Increasing the minimum distance of a set of points. J.
  Combin. Theory Ser. A (1985), 450.
- [Sw02] Swanepoel, Konrad J., Independence numbers of planar contact graphs.
  Discrete Comput. Geom. (2002), 649-670.

**Formalization.** None recorded.

## Current assessment

The [[research/graph_ramsey_interfaces/minimum_distance_independence_limit|separated-union argument]]
makes $g$ subadditive and proves
$\lim_{n\to\infty}g(n)/n=\inf_{m\ge1}g(m)/m$. This author-recorded
proof by Plasma AI establishes existence only. It does not determine the
limit, prove finite attainment, or give a rate of convergence. The source
bounds $8/31$ and $5/16$ retain the reading limits stated in the research
account; neither identifies the infimum.

<!-- BEGIN problem library links -->

## Linked library material

These entries are derived from explicit links on library pages. They are
navigation only and do not by themselves record mathematical progress.

- [[../library/discrete_geometry/csizmadia_1998_independence_number_minimum_distance_graphs/_index|csizmadia_1998_independence_number_minimum_distance_graphs]]
- [[../library/discrete_geometry/csizmadia_1998_independence_number_minimum_distance_graphs/lemma_1|csizmadia_1998_independence_number_minimum_distance_graphs / lemma_1]]
- [[../library/discrete_geometry/csizmadia_1998_independence_number_minimum_distance_graphs/remark_p187|csizmadia_1998_independence_number_minimum_distance_graphs / remark_p187]]
- [[../library/discrete_geometry/csizmadia_1998_independence_number_minimum_distance_graphs/theorem_p180|csizmadia_1998_independence_number_minimum_distance_graphs / theorem_p180]]
- [[../library/discrete_geometry/swanepoel_2002_independence_numbers_planar_contact_graphs/_index|swanepoel_2002_independence_numbers_planar_contact_graphs]]
- [[../library/discrete_geometry/swanepoel_2002_independence_numbers_planar_contact_graphs/theorem_1|swanepoel_2002_independence_numbers_planar_contact_graphs / theorem_1]]
- [[../library/discrete_geometry/swanepoel_2002_independence_numbers_planar_contact_graphs/theorem_2|swanepoel_2002_independence_numbers_planar_contact_graphs / theorem_2]]

<!-- END problem library links -->
