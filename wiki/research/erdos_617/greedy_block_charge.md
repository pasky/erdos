---
name: research/erdos_617/greedy_block_charge
desc: Minimum-residual-degree blocks and independent-pair expansion give the uniform least-budget core bound a at most floor of three r over four.
tags: [graph-theory, proved, potential, critical-graphs]
sources: []
created: 2026-09-22T14:30:00Z
updated: 2026-09-24T22:12:59Z
---


# research/erdos_617/greedy_block_charge

***

**Proved range contraction, not a resolution.** A
[least-budget minimal-ratio core](minimal_ratio_potential.md) for
$r\ge12$ necessarily satisfies

$$
\boxed{a\le\lfloor3r/4\rfloor.}
$$

This still leaves an unbounded range above the
[hereditary span threshold](hereditary_span_bound.md).

Throughout, $n=ar+1$, $\alpha(H)=a$, $\delta(H)\ge r$,
$H$ is $K_r$-free, and

$$
2e(H)\le ar(r-1)+r(r+1).
$$

We use the hereditary caps and the independent-set expansion
$|N_H[I]|\ge r|I|+1$. Independence-criticality is unnecessary.
Write

$$
p_a(ar+1)=a\binom r2+r,\quad
T=e(H)-p_a(ar+1),\quad s(v)=d_H(v)-r,
$$

and $S(W)=\sum_{v\in W}s(v)$, $S=S(V(H))$. Thus

$$
T\le\binom r2,\qquad S=2T-r(a-1),\qquad s(v)\ge0. \tag{1}
$$


## 1. An ordered partition with controlled holes

Repeatedly choose a minimum-degree vertex in the remaining graph
and remove its closed neighborhood. Let the resulting blocks be
$C_1,\ldots,C_k$, with $b_i=|C_i|$, and let $M_i$ count their
internal nonedges. If $R_i$ is the residual just before block $i$,
put

$$
\sigma_i(v)=d_{R_i}(v)-(b_i-1)\ge0\qquad(v\in C_i).
$$

The edges removed at this step number exactly

$$
\sum_{v\in C_i}d_{R_i}(v)-e(H[C_i])
=\binom{b_i}{2}+M_i+\sum_{v\in C_i}\sigma_i(v). \tag{2}
$$

Consequently $2e(H)+n\ge\sum_i b_i^2\ge n^2/k$.
The budget gives

$$
n^2-(a-1)(2e(H)+n)
\ge r^2+(a+1)r+2-a>0.
$$

Thus $k\ge a$, while the chosen pivots are independent, so $k=a$.

Set $t_i=b_i-r$, $M=\sum_iM_i$, and

$$
B=\frac{\sum_i t_i^2-1}{2}\ge0.
$$

Here $\sum_i t_i=1$, so nonnegativity of $B$ follows from
integrality. Summing (2) gives the exact identity

$$
T=B+M+\sum_i\sum_{v\in C_i}\sigma_i(v),
\qquad M\le T-B. \tag{3}
$$


## 2. A matching charge for an arbitrary induced set

Let $C\subseteq V(H)$ have order $b$, and let
$F=\overline{H[C]}$ have $M_C$ edges. If $F$ has a matching
of size $m$, then

$$
\boxed{S(C)+M_C\ge m(b-1-m).} \tag{4}
$$

For a matched pair $xy$, the number of common neighbors in $H[C]$
is $b-d_F(x)-d_F(y)+c_F(x,y)$. Independent-pair expansion therefore
gives

$$
s(x)+s(y)\ge b-1-d_F(x)-d_F(y)+c_F(x,y).
$$

Let $U$ be the matching endpoints. Then

$$
\sum_{x\in U}d_F(x)\le M_C+e_F(U),\qquad
e_F(U)-\sum_{xy\text{ matched}}c_F(x,y)\le m^2. \tag{5}
$$

For the second inequality, the matched edges contribute $m$.
Between two matched pairs, the number of cross edges minus their
contributions to the two common-neighbor counts is at most two:
for zero through four cross edges the respective maxima are
$0,1,2,1,0$. Common neighbors outside $U$ only reduce the expression.
Summing and using $s\ge0$ proves (4).

## 3. Charging all blocks

Every block satisfies

$$
S(C_i)+M_i\ge(r-2)(t_i+1). \tag{6}
$$

For $t_i\le-1$, this is immediate. If $t_i=0$, $K_r$-freeness
supplies a missing edge; apply (4) with $m=1$.

If $t_i=1$, the cap on $r+1$ vertices gives $M_i\ge r-1$.
A graph with matching number at most one has all its edges in
a star or a triangle. The star case would leave an independent
$r$-set in $F$, hence a $K_r$ in $H[C_i]$. The triangle case
has at most three edges, less than $r-1$. Therefore $F$ contains
a matching of size two, and (4) gives $2(r-2)$.

For $t_i\ge2$, minimum residual degree implies

$$
S(C_i)\ge(r+t_i)(t_i-1).
$$

The hereditary cap gives
$M_i\ge(r-1)p_r(r+t_i)\ge(r-1)t_i$; the final inequality holds
at every size at least $r$, since $p_r(r)=0$ and every subsequent
increment is at least one. The sum exceeds the right side of (6) by

$$
r(t_i-2)+t_i^2+2\ge0.
$$


Summing (6) and using (1) and (3) yields

$$
(r-2)(a+1)\le S+M\le3T-r(a-1)-B.
$$

Thus

$$
\boxed{3T\ge2a(r-1)-2+B.} \tag{7}
$$

Since $T\le r(r-1)/2$, we obtain
$a\le3r/4+1/(r-1)$. For $r\ge12$ the last summand is less
than $1/4$, and integrality gives the stated theorem.

## 4. Why this has not produced an iteration

Before block $i$, write the remaining order as $br-k$, with
independence exactly $b$. The original proper-induced ratio bounds give

$$
|N_R[I]|\ge r|I|-k
$$

for independent $I$ in that residual. If the next block has order
$r+t$ and its complementary graph has a matching of size $m$, the
calculation in (5) instead gives

$$
M_C+\sum_{v\in C}\bigl(d_R(v)-(r+t-1)\bigr)
\ge m(r-t-k-m). \tag{8}
$$

In particular a block of order $r$ costs at least $r-k-1$ in
the exact edge decomposition (2).

Initially $k=-1$; deleting a block updates $k$ to $k+t$.
For proper nonempty suffixes $k\ge0$, and after the last block it
is zero. Positive deviations can accumulate and weaken (8), so the
range contraction cannot simply be repeated with a smaller parameter.
No universal contradiction from these suffix charges has been proved.

The exact removal count, the matching charge, and all four cases of
(6) were checked separately. No search or external theorem is used.

### Status of the renewed closure attempt

No stronger valid descent was obtained. The complementary stability
partition has at most $2T\le r^2-r$ target cross edges, but this total
alone does not extend an internal nonedge to a larger independent set:
its endpoints may remove a whole neighboring list. Concentrating on
parts incident with many cross edges did not handle dependency chains
through many lighter parts. No safe suppression or termination theorem
for those chains was proved.

Several proposed scalar block schedules were discarded because they
omitted the final clique condition or the global minimum-degree
constraint. They are not counterexamples or certificates of feasibility.
The established obstruction to naive iteration remains exactly (8):
prefix deletion weakens expansion by the accumulated deficiency $k$.
