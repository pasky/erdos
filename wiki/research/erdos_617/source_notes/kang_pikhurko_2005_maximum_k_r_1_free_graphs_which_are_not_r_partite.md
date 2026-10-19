---
name: research/erdos_617/source_notes/kang_pikhurko_2005_maximum_k_r_1_free_graphs_which_are_not_r_partite
title: "Maximum $K_r+1$-free graphs which are not $r$-partite"
desc: "Source notes for Problem 617: Maximum $K_r+1$-free graphs which are not $r$-partite."
tags: []
sources: []
created: 2026-09-24T22:18:26Z
updated: 2026-10-13T04:56:43Z
---

# Maximum $K_r+1$-free graphs which are not $r$-partite


[Full paper in Markdown](../../../../library/extremal_graph_theory/kang_pikhurko_2005_maximum_k_r_1_free_graphs_which_are_not_r_partite/_index.md).

***

M. Kang and O. Pikhurko, "Maximum $K_{r+1}$-free graphs which are not
$r$-partite," *Matematychni Studii* **24** (2005), 12--20.
[DOI 10.30970/ms.24.1.12-20](https://doi.org/10.30970/ms.24.1.12-20).

The complete local
[Full paper in Markdown](../../../../library/extremal_graph_theory/kang_pikhurko_2005_maximum_k_r_1_free_graphs_which_are_not_r_partite/_index.md)
is the source used for this digest. Page locators below are the printed journal
pages 12--20.

## Exact nonpartite Turán problem

For $n\geq r+3$ and $r\geq2$, the paper writes

$$
\mathcal G_{n,r}=\{G:v(G)=n,\ K_{r+1}\not\subseteq G,\ \chi(G)>r\}
$$

and $p_r(n)=\max\{e(G):G\in\mathcal G_{n,r}\}$ (Introduction, printed
pp. 12--13).

**Theorem 1 (p. 13).** If $n\geq r+3$ and $r\geq2$, then

$$
p_r(n)=
\begin{cases}
t_r(n)-2,&r>(n-1)/2,\\[2mm]
t_r(n)-\lfloor n/r\rfloor+1,&r\leq(n-1)/2,
\end{cases}
$$

where $t_r(n)=e(T_r(n))=\operatorname{ex}(n,K_{r+1})$. The theorem points
to Theorem 4 and Lemma 5 for all equality cases. The paper also observes that
$\mathcal G_{n,r}$ is empty for $n\leq r+2$ and for $r=1$.

The equality construction (pp. 13--14) starts with integers

$$
1\leq n_1\leq\cdots\leq n_r,\qquad
\sum_{i=1}^r n_i=n-1,\qquad n_{r-1}\geq2. \tag{3}
$$

Let $s,t$ be the two smallest indices with $n_i>1$, choose a nonempty proper
set $A\subset N_s$ and $y\in N_t$, and start from the complete $r$-partite
graph on parts $N_i$ of sizes $n_i$. Add a vertex $x$ adjacent to all parts
other than $N_s,N_t$, and also to $A\cup\{y\}$, while deleting every edge
between $y$ and $A$. The resulting graph $G(\mathbf n)$ is $K_{r+1}$-free
and has chromatic number greater than $r$, with

$$
e(G(\mathbf n))=
\sigma_2(\mathbf n)+\sigma_1(\mathbf n)-n_s-n_t+1. \tag{4}
$$

Its isomorphism type can depend on $|A|$, and on the choice of $s,t$ when the
corresponding part sizes differ, although its edge count does not.

**Theorem 4 (pp. 15--16).** For $r\geq2$ and $n\geq r+3$, $p_r(n)$ is the
maximum of (4) over all sequences satisfying (3), and every graph attaining
$p_r(n)$ is one of the constructions $G(\mathbf n)$ above.

**Lemma 5 (p. 17).** If $r>(n-1)/2$, the unique optimizing sequence is

$$
\mathbf n=(1^{(2r-n+1)},2^{(n-r-1)}).
$$

If $r\leq(n-1)/2$, the optimizing sequences are exactly those satisfying
(3) and

$$
n_1\geq2,\qquad n_2\leq n_1+1,\qquad
n_r\leq n_1+2,\qquad n_r\leq n_3+1. \tag{7--10}
$$

Depending on $n,r$, there are between one and three such sequences. The short
proof of Theorem 1 immediately after Lemma 5 chooses an optimizer with
$n_r\leq n_1+1$, identifies these as the part sizes of $T_r(n-1)$, and
compares the cost of inserting the last vertex.

## Extremal mechanism

Lemma 3 (pp. 14--15) handles a graph $G\in\mathcal G_{n,r}$ for which
$G-y$ is $r$-colorable. After separating the singleton color classes and the
larger classes $N_i$, the proof lets $M_i\subseteq N_i$ consist of vertices
adjacent to the clique formed by $y$ and the singleton classes. Potential
$K_{r+1}$s force at least $m_1m_2$ missing edges between the $N_i$. Optimizing
the resulting bound makes $m_1=1$ and $m_i=n_i$ for $i\geq3$, producing
exactly the edge count of a graph $G(\mathbf n)$.

Theorem 4 then uses an Erdős--Turán symmetrization. For a maximum-degree
vertex $x$, put $D=\Gamma(x)$ and $C=V(G)\setminus D$; delete the edges inside
$C$ and complete all pairs between $C$ and $D$. The new graph is still
$K_{r+1}$-free and degreewise dominates $G$. If its graph on $D$ is not
$(r-1)$-partite, induction applies. Otherwise, the proof calls a part of
$D$ good when it contains a vertex complete to its outside, shows that all
but exactly one part must be good, and finds a vertex whose deletion makes
the graph $r$-partite, returning to Lemma 3. Following equality through both
branches pins down all missing edges and yields the classification by
$G(\mathbf n)$. Thus the result is an exact finite stability statement one
step below Turán's bound, rather than only an asymptotic stability theorem.

## Specialization to Problem 617

Fix $r\geq3$, put $N=r^2+1$, and suppose an $r$-edge-coloring of $K_N$ were a
counterexample to
[Problem 617](../../../problems/extremal_graph_theory/E0617/_index.md). For each color
$i$, let $C_i$ be its color graph and let

$$
H_i=K_N-C_i=\bigcup_{j\ne i}C_j.
$$

Every $(r+1)$-set uses color $i$, so $H_i$ is $K_{r+1}$-free. Since
$r\leq(N-1)/2$ and $\lfloor N/r\rfloor=r$, Theorem 1 specializes to

$$
\chi(H_i)>r
\quad\Longrightarrow\quad
e(H_i)\leq t_r(N)-r+1. \tag{*}
$$

Here

$$
t_r(N)=\frac{r(r-1)(r^2+2)}2.
$$

Consequently, if $t_i=t_r(N)-e(H_i)$ is the Turán deficit, then
$t_i\leq r-2$ forces $H_i$ to be $r$-partite, while a non-$r$-partite
$H_i$ has $t_i\geq r-1$. Equality in (*) is completely explicit. Substituting
$\sum n_j=N-1=r^2$ in Lemma 5 gives the possible ordered part-size vectors

$$
(r^{(r)}),\qquad
(r-1,r^{(r-2)},r+1),
$$

and, when $r\geq4$,

$$
((r-1)^{(2)},r^{(r-4)},(r+1)^{(2)}).
$$

For each vector, Theorem 4 describes every non-$r$-partite graph at deficit
$r-1$ by the single added vertex and switched $A$--$y$ edges above. This
turns a near-Turán missing-color graph in a hypothetical balanced coloring
into a small, exact family rather than an unspecified exceptional case.

There are two important limits to this transfer. First, the theorem treats
the graphs $H_i$ separately. It does not make their $r$-partitions compatible
or use the fact that the complementary color graphs $C_i$ partition one
common edge set. Second, an $r$-partition of $H_i$ makes every pair *within*
a part an edge of color $i$. A split coloring instead asks for a partition
$S_1,\ldots,S_r$ in which $S_i$ contains no color-$i$ edge. Thus the
partitions supplied here point in the opposite local direction and are not a
split certificate. Nor does the paper control all $H_i$ at once, so it does
not settle the extra-vertex obstruction for balanced $(r,2)$-colorings.

The paper's other principal result, Theorem 2 (p. 13), gives a new proof of
the value, due to Andrásfai and independently to Erdős and Gallai, of the
maximum number of edges in a nonbipartite $n$-vertex graph whose shortest odd
cycle has length $2l+1$, and adds the characterization of the extremal graphs:

$$
b_l(n)=\left\lfloor\frac{(n-2l+3)^2}{4}\right\rfloor+2l-3
\qquad(l\geq2,\ n\geq2l+1),
$$

with every equality graph given by the construction at the start of Section
3 (p. 17). This includes $b_2(n)=p_2(n)$ but is not used in the E0617
specialization.

Read status: the complete nine-page Markdown reading copy was inspected.
Claims were checked clause by clause for Theorems 1, 2 and 4, Lemmas 3 and 5,
the constructions (3)--(4), and the equality descriptions at printed
pp. 13--20. Their proofs were read for the extremal and equality mechanisms
summarized above, but were not independently verified.
