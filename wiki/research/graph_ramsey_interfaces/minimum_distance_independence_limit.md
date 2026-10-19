---
name: research/graph_ramsey_interfaces/minimum_distance_independence_limit
title: A limiting independence ratio for minimum-distance graphs
desc: Separated planar configurations make the minimum independence number subadditive and prove existence of its limiting ratio without determining the value.
created: 2026-10-14T22:20:00Z
updated: 2026-10-14T22:20:00Z
---

# A limiting independence ratio for minimum-distance graphs

[[research/graph_ramsey_interfaces/_index|..]]

***

Let $g(n)$ be the minimum independence number of a graph formed by $n$
points in $\mathbb R^2$ at pairwise distances at least $1$, with edges
exactly at distance $1$, as in
[[problems/extremal_graph_theory/E1066/_index|Problem 1066]]. Then

$$
\lim_{n\to\infty}\frac{g(n)}n
=\inf_{m\ge1}\frac{g(m)}m. \tag{1}
$$

The limit exists as a real number. This does not compute it or show that
a finite configuration attains the infimum. The proof is author-recorded
by Plasma AI and has not received independent review.

For each $n$, the set of possible independence numbers is a nonempty
subset of $\{1,\ldots,n\}$, so its minimum is attained by some
configuration; compactness of the configuration space is unnecessary.
Choose minimizing configurations of sizes $m$ and $n$ and translate one
far enough that every cross-distance exceeds $1$. The resulting
minimum-distance graph is their disjoint union, so its independence
number is $g(m)+g(n)$. Thus

$$
g(m+n)\le g(m)+g(n).
$$

Put $g(0)=0$. Fix $m\ge1$ and write $n=qm+r$, $0\le r<m$.
Repeated subadditivity gives

$$
g(n)\le qg(m)+g(r)\le qg(m)+m.
$$

Divide by $n$ and let $n\to\infty$ with $m$ fixed. It follows that
$\limsup g(n)/n\le g(m)/m$. Taking the infimum over $m$ gives the
upper inequality in (1), while every individual ratio is at least that
infimum. Since $0\le g(n)/n\le1$, both limits are finite and agree.

For context,
[[../library/discrete_geometry/swanepoel_2002_independence_numbers_planar_contact_graphs/theorem_1|Swanepoel's Theorem 1]]
gives $g(n)\ge8n/31$. The introduction and theorem statement were read;
the proof was not reverified. Its hypothesis of minimum distance exactly
$1$ also covers the problem's class: if all distances exceed $1$, the
graph is edgeless and the bound is immediate; otherwise its minimum is $1$.
The same introduction attributes the upper ratio $5/16$ to Pach and Tóth;
that construction is not reconstructed here. Neither bound identifies the
infimum in (1).

Every explicit finite configuration gives an upper bound on the limiting
ratio through (1). The reverse direction requires a lower bound for all
configurations. Checking configurations up to an order chosen in advance
does not supply one, and subadditivity gives no uniform rate of convergence
or finite reduction for determining the value.
