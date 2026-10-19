---
name: problems/graph_coloring/E0640
title: Problem 640
desc: |
  Asks whether, for each $k\ge 3$, large enough chromatic number forces an odd
  cycle whose vertices span a subgraph of chromatic number at least $k$.
tags:
- Graph theory
- Chromatic number
status: open
claim: none
created: 2026-09-04T09:17:27Z
updated: 2026-10-15T01:58:15Z
---

# Problem 640

[[problems/graph_coloring/_index|..]]

***

**Statement.** Let $k\geq 3$. Does there exist some $f(k)$ such that if a graph
$G$ has chromatic number $\geq f(k)$ then $G$ must contain some odd cycle whose
vertices span a graph of chromatic number $\geq k$?

**Status.** Open.

**Source.** [erdosproblems.com/640](https://www.erdosproblems.com/640), accessed
2026-09-04. Cite as: T. F. Bloom, Erdős Problem #640,
https://www.erdosproblems.com/640.

**Formalization.** None recorded.

## Current assessment

The [[research/methods/chromatic_threshold_interfaces|path/BFS reduction]]
compares the proposed odd-cycle threshold $f(k)$ with the analogous
threshold $p(k)$ for a path whose vertices span a $k$-chromatic graph:
$p(k)\le f(k)\le2p(k+1)-1$, whenever the corresponding thresholds
exist. It also gives $f(3)=3$ and $f(4)\ge5$. The reduction does not
prove the needed path threshold finite. These are scoped author deductions,
not a resolution or a full literature survey.
