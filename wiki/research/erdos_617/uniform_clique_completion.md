---
name: research/erdos_617/uniform_clique_completion
desc: A completion theorem for an entire family of light clique rows, independent of the number of rows or exceptions; extraction and suppression remain open.
tags: [graph-theory, proved, conditional, independent-transversals]
sources: []
created: 2026-09-22T16:15:00Z
updated: 2026-09-24T22:12:59Z
---


# research/erdos_617/uniform_clique_completion

***

**Proved conditional structural theorem, not a solution of E617.**
The completion argument below has no dependence on the number of rows
or on the total number of exceptions. Its hypotheses require a full
family of as many disjoint light clique rows as the independence bound.
No extraction or suppression theorem supplies that family in an
arbitrary surviving core.

Use the hereditary caps from [Reductions](reductions.md):

$$
e(H[W])\le D_r(|W|),\qquad
D_r(n)=\binom n2-(r-1)p_r(n),\qquad
p_r(rq+b)=r\binom q2+qb.
$$


## 1. An all-size row inequality and a local incidence bound

Let $Q$ be a clique of order $r-d$, with $d\ge1$. For
$x\notin Q$ put

$$
m_Q(x)=|Q\setminus N_H(x)|,\qquad
w_Q(x)=\frac{d_H(x,Q)+d-1}{r-1}
=1-\frac{m_Q(x)}{r-1}.
$$

These weights lie in $[0,1]$. For every $S\subseteq V(H)\setminus Q$,

$$
\boxed{\sum_{x\in S}w_Q(x)
\le d+\frac{\overline e_H(S)}{r-1}.} \tag{1}
$$

If $s=|S|<d$, use $w_Q\le1$. Otherwise set $u=s-d$.
The identity $p_r(r+u)=u+p_r(u)$ gives

$$
D_r(r+u)=\binom r2+\binom{u+1}{2}-(r-1)p_r(u).
$$

Subtracting the edges inside $Q$ and $S$ proves the stronger
inequality

$$
\sum_{x\in S}w_Q(x)
\le d-p_r(s-d)+\frac{\overline e_H(S)}{r-1}.
\tag{2}
$$

Thus (1) does not require $|Q\cup S|\le2r$.

If $24d<r+5$, then

$$
\boxed{\bigl|\{x\notin Q:w_Q(x)\ge1/3\}\bigr|\le4d-1.} \tag{3}
$$

Otherwise apply (1) to any $4d$ such vertices. It gives
$4d/3\le d+\binom{4d}{2}/(r-1)$, which is equivalent to
$r+5\le24d$.

The point of (3) is local: the number of substantial incidences into
one light row is controlled by its own deficit, even if there are
arbitrarily many exceptions elsewhere.

## 2. Completion from a robust transversal hypothesis

**Theorem.** Let $a\ge1$, $\varepsilon\in\{0,1\}$, and

$$
|H|=ar+\varepsilon,\qquad \alpha(H)\le a.
$$

Assume all hereditary caps. Suppose $Q_1,\ldots,Q_a$ are disjoint
cliques, with

$$
|Q_i|=r-d_i,\qquad 1\le d_i\le k,\qquad24k<r.
$$

Suppose an integer $L\ge1$ has the following properties:

* $L\le(r-1)/3$ and $3(L-1)+24k-12<r-1$;
* a vertex in one row has at most $(r-1)/3$ neighbors in any
  other single row;
* every subfamily of the rows, with an arbitrary list of at least
  $L$ vertices in each row, has an independent transversal.

Then $\varepsilon=1$ is impossible. If $\varepsilon=0$, each row
can be enlarged so that the resulting sets partition $V(H)$ into
$a$ cliques of order $r$.

**Proof.** Put $X=V(H)\setminus\bigcup_iQ_i$, $t=|X|$, and
$D=\sum_i d_i=t-\varepsilon$. Every $x\in X$ has a row
$i(x)$ with $m_{Q_{i(x)}}(x)<L$: otherwise the transversal
hypothesis would extend $x$ to an independent $(a+1)$-set.
Choose one such row as its owner.

Write $w_i=w_{Q_i}$ and

$$
S_i=\{x\in X:w_i(x)\ge1/3\}.
$$

Every exception belongs to its owner's $S_i$. Call it active if it
belongs to at least two of these sets, and let $A$ be the active
set. For an inactive exception $x$ with owner $i$,

$$
m_{Q_j}(x)>2(r-1)/3\quad(j\ne i). \tag{4}
$$


The row $Q_i$ and all its inactive owned exceptions form a clique.
Indeed, if such an $x$ is nonadjacent to $v\in Q_i$, their
common nonneighbors in every other row number more than
$2(r-1)/3-(r-1)/3\ge L$. If two inactive exceptions with owner
$i$ are nonadjacent, their common nonneighbors in $Q_j$ number
more than

$$
4(r-1)/3-(r-d_j)=(r-4)/3+d_j\ge(r-1)/3\ge L.
$$

In either case a transversal in the remaining rows augments the pair
to size $a+1$, a contradiction. For $a=1$ the pair itself is
already the contradiction.

Let $B$ be the sum of $w_i(x)$ over all nonowner memberships
$x\in S_i$, and let $K$ be their number. Then

$$
K\le3B,\qquad |A|\le K.
$$

Only active vertices can have owner holes, so

$$
M:=\sum_{x\in X}m_{Q_{i(x)}}(x)
\le(L-1)|A|\le3(L-1)B. \tag{5}
$$

By (3), $|S_i|\le4d_i-1\le4k-1$. Every nonedge within $S_i$
meets an active vertex, because all inactive members of $S_i$
have owner $i$ and form a clique. Consequently

$$
\begin{aligned}
E:=\sum_i\overline e_H(S_i)
&\le(4k-2)\sum_i|A\cap S_i|\\
&=(4k-2)(|A|+K)\le(24k-12)B. \tag{6}
\end{aligned}
$$

Summing (1) over the $S_i$, and separating owner from nonowner
memberships, gives

$$
t-\frac M{r-1}+B\le D+\frac E{r-1}.
$$

Thus

$$
\boxed{\varepsilon+B\le
\frac{3(L-1)+24k-12}{r-1}B.} \tag{7}
$$

Its coefficient is strictly less than one. The overloaded case is
impossible. In the balanced case $B=0$, so every exception is
inactive. The owner extensions are disjoint cliques covering $ar$
vertices. Each has order at most $r$, by the cap on $r+1$
vertices, and hence each has order exactly $r$. $\square$

## 3. Explicit sufficient transversal conditions

The robust hypothesis has several parameterized sufficient conditions.
Here all degrees refer to the cross graph on $\bigcup_i Q_i$, with
edges within the rows ignored.

**Self-contained local-lemma version.** Let $\Delta$ be its maximum
total degree. It is enough, in addition to the numerical conditions
of the theorem, that

$$
L^2\ge6r\Delta.
$$

In arbitrary lists of size at least $L$, a cross edge is selected
with probability at most $L^{-2}$. A bad event has at most
$2r\Delta-1$ dependent other bad events, since each row has at
most $r\Delta$ incident cross edges. The symmetric local lemma
applies because $e(2r\Delta)/L^2\le e/3<1$. If there are no
events, the assertion is immediate. These inequalities also imply
$\Delta<(r-1)/54$, so the theorem's individual-row degree
condition is automatic.

**Haxell version.** One may instead use

$$
L\ge2\Delta
$$

with the other numerical conditions unchanged. Haxell's independent
transversal theorem applies to every list restriction. Its precise
statement is Theorem 1, and its topological proof is supplied by
Theorems 7, 14 and Corollary 15, in
[Haxell--Wdowinski, *Degree criteria and stability for independent
transversals*](https://arxiv.org/html/2305.10595).
Those passages were checked in the primary text. The local degree
condition follows from $\Delta\le L/2\le(r-1)/6$.

**Total-edge/local-degree version.** Let $E_\times$ count all cross
edges, and let $d$ bound the number of neighbors a vertex has in
any one other row. For $L\ge8$, it is enough that

$$
d\le(r-1)/3,\qquad
E_\times<\frac{L^3}{128\max\{d,1\}}.
$$

Apply the elementary transversal theorem in
[Packing tools](packing_tools.md) to every subfamily and list
restriction. In particular the completion theorem applies
asymptotically when $k=o(r)$, $d=o(r)$, and
$E_\times=O(r^2)$: choose, for example, $L=\lfloor r/6\rfloor$.
This statement still assumes all $a$ rows exist.

## 4. Exact unresolved step

The earlier completion argument in
[Hereditary span](hereditary_span_bound.md) paid for exceptional
nonedges using the *total* exception count. Equations (3) and (6)
remove that loss. The theorem above therefore works with an unbounded
number of rows and exceptions, once the stated row family and
transversal control are available.

The existing cluster extractions can instead leave fewer than $a$
light rows, or rows with large deficits or concentrated cross degrees.
The owner existence argument then fails: one exception and a transversal
of only $q<a$ rows need not exceed the independence bound. Likewise
a nonadjacent same-owner pair need not augment to size $a+1$.
No deletion of those light rows, preservation of caps under folding,
or extension across a heavy residual has been proved here.

The local-lemma proof and all incidence and endpoint calculations were checked
by the author and are author-recorded. No finite search was used. This is
neither an unrestricted infinite family of solved parameters nor a
counterexample to the problem.
