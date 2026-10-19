---
name: research/erdos_644/join_layer_families
desc: Every finite hereditary complex satisfies the three-quarter deletion bound; its P7 join layers have transversal number at most three quarters of their uniformity plus eight times the seed size.
tags: [proved, constructions, restricted-upper-bounds]
sources: []
created: 2026-09-23T00:49:12Z
updated: 2026-09-24T22:12:53Z
---


# research/erdos_644/join_layer_families

***

This page studies one possible construction, not arbitrary uniform families. Its
two asymptotic parameters have exact finite descriptions, and every finite
hereditary complex satisfies

$$
\gamma_K(B(K))\le\frac34 B(K).
$$

More precisely, every $P_7$ join layer satisfies
$\tau(\mathcal H_{q,k}(K))\le3k/4+8|V(K)|$. Thus neither fixed seeds nor growing
seeds with $|V(K)|=o(k)$ can improve the asymptotic coefficient $3/4$ within
this construction. This does not settle the unrestricted seven-edge problem.

Write $P_7$ for the condition that every subfamily of at most seven edges has a
transversal of size at most two.

The extension in [Arbitrary local layers](arbitrary_local_layers.md) removes
heredity. For a finite local family containing the empty set, rank $a$, ground
size $N$, and gcd $g$ of its positive member sizes, its $P_7$ product layers
satisfy $\tau\le3k/4+51Na/g$. The proof keeps the deletion upper bound and
replaces hereditary trimming by bounded residue corrections. The stronger error
$8N$ proved on this page remains specific to hereditary seeds.

## The construction

Let $K\subseteq 2^V$ be a finite nonempty hereditary family, with $N=|V|$ and
rank

$$
a=\max_{I\in K}|I|\ge1.
$$

Discard vertices belonging to no face, so that every singleton belongs to $K$.
For $D\subseteq V$, put

$$
r(D)=\max\{|I|:I\in K,\ I\cap D=\varnothing\}.
$$


Take $q$ disjoint copies $V_1,\ldots,V_q$ of $V$. Their join consists of the
sets whose intersection with every $V_j$ is a face of the corresponding copy of
$K$. For $1\le k\le aq$, let

$$
\mathcal H_{q,k}(K)
=\left\{A\subseteq\bigsqcup_{j=1}^qV_j:
|A|=k,\quad A\cap V_j\in K\text{ for every }j\right\}.
\tag{1}
$$

Here the notation in each block uses its fixed identification with $V$. The
asymptotic formulas below first keep $K$ fixed; the final finite bound is
uniform in $K,q,k$.

## The deletion linear program

For $0\le b\le a$, define

$$
\gamma_K(b)=
\min\left\{
\sum_{D\subseteq V}\lambda_D|D|:
\lambda_D\ge0,\quad
\sum_D\lambda_D=1,\quad
\sum_D\lambda_Dr(D)\le b
\right\}.
\tag{2}
$$

Thus $\gamma_K(b)$ is the minimum expected deletion size when the expected
remaining rank is at most $b$. It is a continuous, nonincreasing, convex,
piecewise-linear function on $[0,a]$, with

$$
\gamma_K(0)=N,\qquad \gamma_K(a)=0.
$$

These assertions also follow by taking the lower boundary of the convex hull of
the finitely many points $(r(D),|D|)$ and permitting rank at most $b$.

**Proposition.** For every $q\ge1$ and $1\le k\le aq$,

$$
q\gamma_K(k/q)
\le \tau(\mathcal H_{q,k}(K))
\le q\gamma_K(k/q)+2N.
\tag{3}
$$

Consequently, whenever $k_q/q\to b\in[0,a]$ and $1\le k_q\le aq$,

$$
\frac{\tau(\mathcal H_{q,k_q}(K))}{q}\longrightarrow\gamma_K(b).
\tag{4}
$$

For $b>0$, the transversal-to-uniformity ratio tends to $\gamma_K(b)/b$.

**Proof.** A deletion set with block restrictions $D_1,\ldots,D_q$ meets all
$k$-faces exactly when

$$
\sum_{j=1}^qr(D_j)<k.
\tag{5}
$$

Indeed, the largest surviving join face has size equal to this sum; heredity
supplies a surviving face of size exactly $k$ whenever the sum is at least $k$.
The empirical distribution of the $D_j$ in (5) is feasible for (2) with
parameter $k/q$, proving the lower bound.

An optimal extreme point of (2) has at most two positive coefficients. If there
are two, order their deletion types so that $r(D_0)\le r(D_1)$, and let the
coefficient of $D_1$ be $p$. Use $\lfloor qp\rfloor$ blocks of type $D_1$ and
the remaining blocks of type $D_0$. The resulting total rank is at most $k$,
since the higher-rank coefficient was rounded down. The total deletion size is
at most $q\gamma_K(k/q)+N$. The same conclusions hold without rounding when the
optimum has one type.

If the remaining rank equals $k$, completely delete the remaining vertices in
one block of positive rank. Such a block exists because $k\ge1$; this costs at
most $N$ and makes the total rank strictly less than $k$. This proves (3).
Continuity of $\gamma_K$ proves (4). $\square$

## A finite spectrum parameter for the local property

A spectrum is a subset of the row set $[7]$. Call a support
$\mathcal C\subseteq2^{[7]}$ admissible if

$$
S\cup T\ne[7]\qquad(S,T\in\mathcal C),
\tag{6}
$$

including the case $S=T$. We may restrict to nonempty downward-closed supports:
taking downward closure preserves (6) and permits every original assignment.
Such a support contains the empty spectrum.

For a fixed admissible $\mathcal C$, consider assignments

$$
\sigma:V\longrightarrow\mathcal C
$$

whose seven rows

$$
I_i(\sigma)=\{v\in V:i\in\sigma(v)\}\qquad(i\in[7])
$$

all belong to $K$. Let

$$
P_{\mathcal C}(K)
=\operatorname{conv}
\left\{\bigl(|I_1(\sigma)|,\ldots,|I_7(\sigma)|\bigr):
\sigma\text{ is such an assignment}\right\},
$$

and define

$$
B(K)=\max_{\mathcal C}
\max_{p\in P_{\mathcal C}(K)}\min_{i\in[7]}p_i.
\tag{7}
$$

There are finitely many admissible supports and assignments. For each support,
the inner optimization is a finite rational linear program, obtained by
adjoining a variable $t$ and the inequalities $p_i\ge t$. Thus $B(K)$ is
attained and rational.

One always has

$$
\frac{4a}{7}\le B(K)\le a.
\tag{8}
$$

For the lower bound, fix an $a$-face and assign every one of its vertices the
same Fano-cap spectrum, assigning the empty spectrum elsewhere. Average the
resulting seven size vectors over the seven complements of Fano lines. Every row
occurs in four caps, so the mean vector is $(4a/7,\ldots,4a/7)$. The downward
closure of the seven caps is admissible because any two Fano lines intersect.
The upper bound follows from the definition of rank.

**Proposition.** The following finite implications hold:

$$
\begin{aligned}
k>qB(K)&\quad\Longrightarrow\quad \mathcal H_{q,k}(K)\text{ has }P_7,\\
1\le k\le qB(K)-8a&\quad\Longrightarrow\quad \mathcal H_{q,k}(K)\text{ fails }P_7.
\end{aligned}
\tag{9}
$$

In particular, if $k_q/q\to b>B(K)$, the families have $P_7$ for all
sufficiently large $q$. If $0<b<B(K)$, they fail $P_7$ for all sufficiently
large $q$.

**Proof of the first implication.** Suppose an at-most-seven subfamily has no
two-point transversal. Repeat rows to obtain seven rows $A_1,\ldots,A_7$. For
every point $v$ of the joined ground set, record its spectrum

$$
S_v=\{i:v\in A_i\}.
$$

The support of these spectra satisfies (6), since otherwise the corresponding
one or two points cover every row. Take its downward closure $\mathcal C$. The
spectrum assignment in each block is one of those defining $P_{\mathcal C}(K)$.
Averaging the $q$ block size vectors gives

$$
(k/q,\ldots,k/q)\in P_{\mathcal C}(K),
$$

contradicting $k/q>B(K)$.

**Proof of the second implication.** Choose a maximizing support and a vector
$p$ with all coordinates at least $B(K)$. By Caratheodory's theorem, write $p$
as a convex combination of at most eight block-assignment size vectors $u_j$,
with coefficients $\lambda_j$. Use $\lfloor q\lambda_j\rfloor$ copies of the
corresponding assignment, and fill any remaining blocks with the empty
assignment. Every row then has size at least

$$
qp_i-\sum_j(u_j)_i\ge qB(K)-8a\ge k.
$$

Delete incidences from each row until its size is exactly $k$. Each block
restriction remains a face by heredity. Each point spectrum remains in
$\mathcal C$ by downward closure, so (6) still excludes every two-point
transversal. Removing repeated rows gives a bad subfamily of at most seven
distinct edges. $\square$

The boundary $k/q=B(K)+O_K(1/q)$ is not classified by (9). This bounded-width
uncertainty has no effect on the limiting transversal density.

For $0<b<a$ and $k_q/q\to b$, the families in (1) eventually have at least seven
distinct edges: they contain all $k_q$-subsets of the union of $q$ fixed
$a$-faces. Thus the at-most-seven and exactly-seven conventions agree in this
regime.

## The universal finite-complex inequality

Choose a maximum face $A_1$ of $K$, then a maximum face $A_2$ disjoint from
$A_1$, and then a maximum face $A_3$ disjoint from $A_1\cup A_2$. Empty faces
are allowed. Write

$$
a_j=|A_j|,\qquad
a=a_1\ge a_2\ge a_3\ge0,\qquad
b_0=\frac{4a_1+2a_2+a_3}{7}.
\tag{10}
$$


**Theorem.** For every finite hereditary complex $K$ as above,

$$
B(K)\ge b_0,\qquad
\gamma_K(b_0)\le\frac34b_0.
\tag{11}
$$

Consequently,

$$
\boxed{\gamma_K(B(K))\le\frac34 B(K).}
\tag{12}
$$


**Proof of the spectrum bound.** Use the downward closure $\mathcal C$ of the
seven Fano caps. Identify the rows with $\mathbb Z/7\mathbb Z$, taking the Fano
lines to be the translates of $\{0,1,3\}$. Translations preserve $\mathcal C$
and act transitively on the rows.

Partition the rows into a cap $C_1$ of size four, a two-set $C_2$, and a
singleton $C_3$. Every two-set is contained in a Fano cap: at most five of the
seven lines meet the two-set, so some line avoids it. Thus all three spectra
belong to $\mathcal C$. Assign spectrum $C_j$ to every vertex of $A_j$ and the
empty spectrum to every other vertex. The faces $A_j$ are disjoint, and every
row is exactly one of them, so this is a permitted assignment.

Take its seven translates. Every row receives $A_1$ four times, $A_2$ twice, and
$A_3$ once. Their average size vector is $(b_0,\ldots,b_0)$, proving
$B(K)\ge b_0$.

**Proof of the deletion bound.** For $\lambda\ge0$, put

$$
m_\lambda=\min_{D\subseteq V}\bigl(|D|+\lambda r(D)\bigr).
$$

Finite linear-program duality applied to (2) gives

$$
\gamma_K(b)=\sup_{\lambda\ge0}\bigl(m_\lambda-\lambda b\bigr).
\tag{13}
$$

The deletion types $\varnothing,A_1,A_1\cup A_2$ show that

$$
m_\lambda\le\lambda a_1,\qquad
m_\lambda\le a_1+\lambda a_2,\qquad
m_\lambda\le a_1+a_2+\lambda a_3.
\tag{14}
$$

We prove $m_\lambda\le(\lambda+3/4)b_0$ for every $\lambda\ge0$.

If $0\le\lambda\le1$, then

$$
\frac{m_\lambda}{\lambda+3/4}
\le\frac{\lambda a_1}{\lambda+3/4}
\le\frac{4a_1}{7}\le b_0.
$$

Suppose now that $\lambda\ge1$. Successive use of the three inequalities in (14)
gives

$$
\begin{aligned}
7b_0
&\ge\left(4-\frac1\lambda\right)a_1
  +\left(2-\frac1\lambda\right)a_2
  +\frac{m_\lambda}{\lambda}\\
&\ge\left(4-\frac3\lambda+\frac1{\lambda^2}\right)a_1
  +\left(3-\frac1\lambda\right)\frac{m_\lambda}{\lambda}\\
&\ge\left(7-\frac4\lambda+\frac1{\lambda^2}\right)
  \frac{m_\lambda}{\lambda}.
\end{aligned}
\tag{15}
$$

The coefficients used in these substitutions are positive for $\lambda\ge1$.
With $x=1/\lambda\in(0,1]$, the identity

$$
\left(1-\frac47x+\frac17x^2\right)
\left(1+\frac34x\right)-1
=\frac{x(1-x)(5-3x)}{28}\ge0
\tag{16}
$$

therefore yields $b_0\ge m_\lambda/(\lambda+3/4)$. Equation (13) now proves
$\gamma_K(b_0)\le3b_0/4$.

Finally, $B(K)\ge b_0$ and monotonicity give

$$
\gamma_K(B(K))\le\gamma_K(b_0)
\le\frac34b_0\le\frac34B(K).
$$

This proves the theorem. $\square$

Only the three deletion types in (14) were used. The same dual argument
therefore proves (11) even when the deletion LP is restricted to those types; it
is feasible at $b_0$ because $b_0\ge a_3$.

## A uniform finite bound, including growing seeds

**Theorem.** For every $K,q,k$ as in (1), if $\mathcal H_{q,k}(K)$ has $P_7$,
then

$$
\boxed{\tau(\mathcal H_{q,k}(K))\le\frac34k+8N.}
\tag{17}
$$


**Proof.** Write $q=7\ell+s$, where $0\le s\le6$, and use the seven explicit
assignments from the proof of (11). Place $\ell$ complete copies of this orbit
in $7\ell$ blocks and use the empty assignment in the remaining $s$ blocks.
Every row has size

$$
\ell(4a_1+2a_2+a_3)=(q-s)b_0.
$$

All spectra belong to the same admissible support $\mathcal C$. If
$k\le(q-s)b_0$, trimming each row to size $k$ would give a bad subfamily, as in
the proof of (9). Hence $P_7$ implies

$$
k>(q-s)b_0.
\tag{18}
$$


Put $b=k/q$. If $b\ge b_0$, monotonicity and (11) give $q\gamma_K(b)\le3k/4$. If
$b<b_0$, convexity between $0$ and $b_0$, together with $\gamma_K(0)=N$, gives

$$
\begin{aligned}
q\gamma_K(b)
&\le qN\left(1-\frac{b}{b_0}\right)
  +q\frac{b}{b_0}\gamma_K(b_0)\\
&\le qN\left(1-\frac{b}{b_0}\right)+\frac34k
<sN+\frac34k,
\end{aligned}
$$

where the last inequality is (18). In either case, (3) gives

$$
\tau(\mathcal H_{q,k}(K))\le\frac34k+(s+2)N
\le\frac34k+8N.
$$

This includes $q<7$, since then (18) is simply $k>0$. $\square$

It follows directly that every fixed-seed sequence with $k\to\infty$ and $P_7$
has limiting upper transversal-to-uniformity ratio at most $3/4$, without any
assumption that $k/q$ converges. More generally, for a sequence of possibly
different seeds $K_j$ and parameters $q_j,k_j$, the hypotheses

$$
\mathcal H_{q_j,k_j}(K_j)\text{ has }P_7,
\qquad k_j\to\infty,\qquad |V(K_j)|=o(k_j)
$$

imply

$$
\limsup_{j\to\infty}
\frac{\tau(\mathcal H_{q_j,k_j}(K_j))}{k_j}\le\frac34.
$$


This settles the finite-complex inequality and excludes the stated join-layer
constructions as asymptotic improvements on $3/4$. It is not a reduction of
arbitrary uniform families to these constructions, and it does not furnish an
amplifier preserving $P_7$. In particular, for the downward closure of an
arbitrary $a$-uniform family, $\gamma_K(a)=0$ regardless of the transversal
number of its top layer; the convexified deletion inequality alone does not
bound that transversal number by $3a/4$.

## Explicit parameters for two subclasses

The following classes are now special cases of (12). Their additional parameter
formulas remain useful.

### Bipartite graph independence complexes

Let $K=\operatorname{Ind}(G)$ for a finite bipartite graph $G$, including
possible isolated vertices, and write $\mu=\nu(G)$. Then

$$
B(K)\ge\frac{3N}{7}.
\tag{19}
$$

Assign the two bipartition classes disjoint three-element spectra and average
over all row permutations. The fixed support consisting of all spectra of size
at most three is admissible, and every occupied row is independent, proving
(19).

For the independence complex of any finite graph, a maximum matching gives

$$
\gamma_K(b)\le N-b-\min\{b,\mu\},
\qquad 0\le b\le a.
\tag{20}
$$

For integral $b\le\mu$, retain the endpoints of $b$ matching edges. For integral
$\mu\le b\le N-\mu$, retain all matching endpoints and $b-\mu$ unmatched
vertices. The retained graph has independence number at most $b$ and
respectively $2b$ or $b+\mu$ vertices. Since $a\le N-\mu$, mixing consecutive
choices proves (20) throughout $[0,a]$.

### Disjoint unions of simplices

Suppose the nonempty faces of $K$ lie in one of disjoint simplices of sizes
$a_1\ge a_2\ge a_3\ge\cdots$, padded with zeros as needed. Then

$$
\gamma_K(b)=\sum_j(a_j-b)_+.
\tag{21}
$$

To leave rank at most an integer $r$, retain at most $r$ vertices from each
simplex, requiring exactly $\sum_j(a_j-r)_+$ deletions. This function is convex
and linear between consecutive integer ranks, so mixing deletion types gives
(21). The three largest simplices are successive maximum disjoint faces, and
hence (11) supplies $B(K)\ge(4a_1+2a_2+a_3)/7$ and the three-quarter bound
without a separate argument.
