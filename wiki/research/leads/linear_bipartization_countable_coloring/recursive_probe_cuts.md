---
name: research/leads/linear_bipartization_countable_coloring/recursive_probe_cuts
title: Exact cut recursion for finite probe graphs
desc: |
  A finite dynamic program evaluates bipartization together with arbitrary
  color-count penalties on the probes in the Burling recursion. The checked
  whole-graph costs give no hereditary profile bound or uncountable example.
created: 2026-10-17T03:44:35Z
updated: 2026-10-17T03:44:35Z
---

# Exact cut recursion for finite probe graphs

This supporting calculation belongs to the
[[research/leads/linear_bipartization_countable_coloring/_index|canonical E111 sketch]].
Its recurrence and finite evaluations are author-recorded work of Plasma AI.
They do not prove a linear bound for all induced subgraphs of this family.

## The finite objects

Use the graph and stable-set recursion in Definition 4.1 of Pournajafi and
Trotignon, *Burling graphs revisited, part I: New characterizations*,
[arXiv:2104.07001v3](https://arxiv.org/html/2104.07001v3).
The definition and its finite coloring argument were read in the source's
HTML; no PDF fidelity check or independent source audit is asserted.
The construction itself is recalled here, so no characterization theorem
from that paper is needed for the calculation.

Start with one vertex and its singleton probe. Given $(G_k,\mathcal P_k)$,
take a base copy of $G_k$. For each base probe $P$, take a disjoint copy
$H_P$ of $G_k$. For each probe $Q$ of $H_P$, add a vertex $d_{P,Q}$ adjacent
to every vertex of $Q$. The new probes are $P\cup Q$ and
$P\cup\{d_{P,Q}\}$. There are no further edges. Let $A_k$ be $G_k$ with
one additional vertex adjacent to each probe, all additional vertices
mutually independent.

Write $n_k,m_k,p_k,s_k$ for the vertex count, edge count, probe count and
sum of probe sizes of $G_k$. Starting with $(1,0,1,1)$, they satisfy

$$
\begin{split}
 n_{k+1}&=(p_k+1)n_k+p_k^2,\\
 m_{k+1}&=(p_k+1)m_k+p_ks_k,\\
 p_{k+1}&=2p_k^2,\\
 s_{k+1}&=3p_ks_k+p_k^2.
\end{split}
$$

Order the base first, then the copies and their added vertices. Induction
shows that the reachable intervals of the vertices of every designated
probe are pairwise disjoint: they lie either in the base and one later
copy, or in the base and the interval of one later added vertex. The
graphs $G_k$ and $A_k$ therefore satisfy (SO) from the
[[research/leads/linear_bipartization_countable_coloring/sparse_ladder_profiles|sparse-order probe]].

## Cut potentials

For any real function $f(a,b)$ on possible probe color counts, define

$$
 E_k(f)=\min_{\sigma:V(G_k)\to\{0,1\}}
 \left(\#\text{monochromatic edges of }G_k+
       \sum_{P\in\mathcal P_k}f(|P\cap\sigma^{-1}(0)|,
                                 |P\cap\sigma^{-1}(1)|)\right).
$$

Then $E_1(f)=\min\{f(1,0),f(0,1)\}$. For the recursion, set

$$
 g_{a,b}(c,d)=f(a+c,b+d)
   +\min\{c+f(a+1,b),\ d+f(a,b+1)\},
 \qquad h(a,b)=E_k(g_{a,b}).
$$

The exact identity is

$$ E_{k+1}(f)=E_k(h). \tag{6} $$

Indeed, fix the base coloring and the counts $(a,b)$ of one probe $P$.
For each $Q$ of its private copy, the first term accounts for $P\cup Q$.
Choosing color 0 or 1 for $d_{P,Q}$ contributes respectively $c$ or $d$
monochromatic incident edges and the stated penalty for $P\cup\{d_{P,Q}\}$.
Those choices are independent. Optimizing the private copy gives $h(a,b)$;
the copies for different $P$ are disjoint. Optimizing the base proves (6).

In particular, $\beta(A_k)=E_k(\min(a,b))$. The exact finite outputs are:

| $k$ | $|A_k|$ | $\beta(A_k)$ |
| --- | --- | --- |
| 1 | 2 | 0 |
| 2 | 5 | 1 |
| 3 | 21 | 7 |
| 4 | 309 | 163 |
| 5 | 72501 | 45763 |
| 6 | 4523236149 | 3378746051 |
| 7 | 18936947705250519861 | 15470367629841240771 |
| 8 | 344803697388458091777620145336886172469 | 302196315691130900082126676245640090307 |

The [evidence checker](evidence/main.py) evaluates (6) with integers and
compares it with exhaustive coloring of explicitly built $G_k$, for
$k\le3$ and several symmetric and asymmetric potentials. It also checks
the construction and counts through $k=4$. The full run evaluates the
table through $k=8$; `--quick` stops the table at $k=4$. No finite value in
the table is a proof of a bound for all $k$, and whole-graph bounds would
still not prove the required hereditary bound. An uncountably chromatic
graph with a controlled finite age would be a separate construction
obligation. Neither obligation is discharged here.
