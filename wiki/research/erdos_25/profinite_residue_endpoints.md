---
name: research/erdos_25/profinite_residue_endpoints
desc: Relative compression forces diffuse residue distributions for any bounded-quotient first-kill anomaly.
tags: [endpoints, compression, partial-results]
sources: []
created: 2026-09-22T05:40:00Z
updated: 2026-09-24T22:13:01Z
---


# research/erdos_25/profinite_residue_endpoints

***

The results here concern bounded-quotient **first kills**, not the full
delayed union. They do not resolve Problem 25. They prove logarithmic
nullity whenever the normalized residues have countable profinite closure,
and give a necessary distributional condition in general.

## Relative compression: proved

Let $S\subseteq\widehat{\mathbb Z}$ be $P$-periodic, and suppose a finite
or countable family $C_i=[a_i]_{q_i}$ satisfies
$$
 a_i\equiv c\pmod{(q_i,P)}
 \quad\text{for every }i,
$$
where $c$ is one integer. Then
$$
 \mu\left(S\cap\bigcup_i[c]_{q_i}\right)
 \le \mu\left(S\cap\bigcup_i C_i\right).
 \tag{1}
$$
Distinctness of the moduli is not needed for this lemma.

For a finite family work modulo $L=\operatorname{lcm}(P,q_i)$ and use
CRT. Fix a prime $p\mid L$, all other prime coordinates, and the low
digits $x\pmod{p^v}$, where $v=v_p(P)$. A cylinder with
$e=v_p(q_i)\le v$ is either empty or the entire remaining fiber;
replacing its center by $c$ at this prime changes neither possibility.
When $e>v$, the cylinder meets only the low fiber $c\pmod{p^v}$.
Inside that fiber its restriction is a $p$-adic ball. Moving all the
remaining centers to $c$ makes these balls nested, so their union has
measure equal to the largest ball and cannot increase. An entire-fiber
restriction, if present, also causes no problem. Since $S$ is constant
on each fixed $P$-residue, the same comparison holds after intersection
with $S$. Integrate and repeat over all prime coordinates. This proves
(1) for finite families; monotone convergence proves the countable case.

## Multiples unions intersected with a periodic set

For arbitrary $D\subseteq\mathbb N$ and a periodic set $R$, the set
$M(D)\cap R$ has logarithmic density
$$
 \operatorname{ld}(M(D)\cap R)=\mu(M(D)\cap R).
 \tag{2}
$$
Here $M(D)$ denotes the positive multiples union or its Haar version,
according to the ambient space.

Indeed, the [exact multiples theorem](basic_reductions.md#an-exact-finite-harmonic-inequality-for-multiples-proved)
gives $\operatorname{ld}(M(D))=\beta:=\mu(M(D))$. For finite
$D_j\uparrow D$, put $\beta_j=\mu(M(D_j))$. Subtracting the finite
periodic harmonic sum gives
$$
 \operatorname{ld}(M(D)\setminus M(D_j))=\beta-\beta_j\longrightarrow0.
$$
The periodic sets $M(D_j)\cap R$ thus approximate $M(D)\cap R$ in
upper logarithmic density. Their densities converge to the right side
of (2) by Haar monotone convergence. This proves (2); no natural-density
assertion for the infinite multiples union is being made.

## A residue-cylinder bound for first endpoints

Use strictly increasing moduli $q_i$, normalized residues
$0\le a_i<q_i$, and notation
$$
 C_i=[a_i]_{q_i},\quad U=\bigcup_i C_i,\quad
 B_i=\{a_i+tq_i:t\ge1\},\quad
 E_i=B_i\setminus\bigcup_{h<i}B_h.
$$
Fix $K\ge1$, write $m=\lfloor K\rfloor$, and define
$$
 T_K=\bigcup_i(E_i\cap[q_i,Kq_i]).
$$
Every point in $T_K$ has a unique witnessing index $i(n)$ and an
integer quotient $1\le t=(n-a_{i(n)})/q_{i(n)}\le m$.

For a prefix $j$, put
$$
 U_j=\bigcup_{i\le j}C_i,\quad
 \tau_j=\mu(U\setminus U_j),\quad
 P_j=\operatorname{lcm}(q_1,\ldots,q_j).
$$
For every residue $c\pmod{P_j}$,
$$
 \overline{\operatorname{ld}}
 \{n\in T_K:a_{i(n)}\equiv c\pmod{P_j}\}
 \le m\tau_j.
 \tag{3}
$$
The coefficient does not depend on the old period.

To prove this, discard the finitely many points with $i(n)\le j$ and
write $S=\widehat{\mathbb Z}\setminus U_j$ and $R=S-c$. Every
remaining first kill lies in $S$: at $n\ge q_{i(n)}>q_j$, all old
congruences are active. For each $t\le m$, let $D_t$ consist of the
moduli of points $n=a_i+tq_i$ under consideration. Then
$tq_i\in R$ and $n\ge tq_i$. Distinctness makes $q_i\mapsto tq_i$
injective, so
$$
 H_{\{n\in T_K:i(n)>j,\ a_{i(n)}\equiv c\ (P_j)\}}(X)
 \le\sum_{t=1}^m H_{M(tD_t)\cap R}(X).
 \tag{4}
$$
By (2), each right-hand term has logarithmic density equal to its Haar
measure. Since $M(tD_t)\subseteq M(D_t)$, translation and (1) give
$$
 \begin{aligned}
 \mu(M(tD_t)\cap R)
 &\le\mu((c+M(D_t))\cap S)\\
 &\le\mu\left(S\cap\bigcup_{q_i\in D_t}C_i\right)
 \le\tau_j.
 \end{aligned}
$$
Here $a_i\equiv c\pmod{P_j}$ is stronger than the compatibility
hypothesis of (1). Summing (4) proves (3), with the original activation
rule unchanged.

## Diffuse limiting residues and a logarithmic-nullity criterion

For $X\ge2$ define a finite measure on $G=\widehat{\mathbb Z}$ by
$$
 \nu_X=\frac1{\log X}\sum_{\substack{n\le X\\n\in T_K}}
                         \frac1n\,\delta_{a_{i(n)}}.
 \tag{5}
$$
**Every weak limit along $X\to\infty$ of these measures is nonatomic.**
Their masses are bounded and $G$ is compact metrizable. For a weak
limit $\nu$, residue-cylinder indicators are continuous, so (3) gives
$$
 \nu([c]_{P_j})\le m\tau_j\qquad\text{for every }j,c.
$$
For any $\alpha\in G$,
$$
 \nu(\{\alpha\})\le\nu([\alpha]_{P_j})\le m\tau_j\longrightarrow0.
$$
The periods $P_j$ need not exhaust all finite moduli for this deduction.

**Corollary.** If the normalized residues $\{a_i\}$ have countable
closure in $\widehat{\mathbb Z}$, then
$$
 \operatorname{ld}(T_K)=0\qquad\text{for every fixed }K.
 \tag{6}
$$
In particular, this holds if $a_i$ converges profinitely.

Every measure (5), and hence every weak limit, is supported on that
closed countable set. A nonatomic measure supported there is zero.
If the masses $H_{T_K}(X)/\log X$ did not tend to zero, compactness
would give a weak limit with positive mass, a contradiction. A
convergent sequence together with its limit has countable closure,
proving the last assertion.

For arbitrary residues the closure may be uncountable, and diffuse
limits are possible in principle. Nothing here controls that case or
first kills with unbounded quotient. In particular, (6) alone does not
give logarithmic density for the original survivor set.

The [binary-colored private-witness construction](binary_colored_private_witnesses.md)
shows a further limitation of purely profinite endpoint arguments.
Even locally $0/1$-colored idempotent congruences can have private
profinite witnesses, a modulus set of natural density $1/4$, and
positive survivor density $1/2$. Its actual delayed union does have
natural density. Short positive integer witnesses, not merely
profinite privacy or a bounded local color alphabet, remain essential.
