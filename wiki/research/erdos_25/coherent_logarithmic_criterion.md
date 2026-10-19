---
name: research/erdos_25/coherent_logarithmic_criterion
desc: A weighted primitive-reciprocal criterion proves logarithmic density for every coherent center, even for some modulus sets without natural density.
tags: [coherent-residues, logarithmic-density, partial-results]
sources: []
created: 2026-09-22T05:40:00Z
updated: 2026-09-24T22:13:01Z
---


# research/erdos_25/coherent_logarithmic_criterion

***

This is a proved sufficient condition for the original activation rule,
not a solution of the unrestricted coherent or arbitrary-residue problem.

## The logarithmic criterion

Let $D$ be a set of moduli, let $P$ be its primitive core, and fix a
coherent center $\alpha\in\widehat{\mathbb Z}$. Suppose
$$
 W_P(X):=\sum_{\substack{q\in P\\q\le X}}\frac{\log q}{q}
 =O(\log X).
 \tag{1}
$$
Then the delayed union
$$
 B=\{n\ge1:\exists q\in D,\ q\le n,\ n\equiv\alpha\pmod q\}
$$
has logarithmic density $\beta=\mu(\bigcup_{q\in D}[\alpha]_q)$.
It has finite-periodic approximation in upper logarithmic density.
The conclusion holds for every coherent center, not just integer centers.

Deleting nonminimal multiples changes neither the full nor the delayed
union, so work with $P$. If $q(n)$ is the least full covering modulus,
put, for $0<\eta\le1/2$,
$$
 B_\eta=\{n:q(n)\le n^{1-\eta}\},\qquad
 E_\eta=B\setminus B_\eta.
$$
The [power-cutoff theorem](coherent_power_cutoff.md#natural-density-with-any-fixed-power-delay)
proves that $B_\eta$ has natural, hence logarithmic, density $\beta$.
Every point of $E_\eta$ in the $q$-cell satisfies
$q\le n<q^{1/(1-\eta)}$. Write the normalized residue as
$0\le a_q<q$ and $n=a_q+tq$, with $t\ge1$. Summing over all possible
quotients, whether or not they are first kills, gives
$$
 \begin{aligned}
 H_{E_\eta}(X)
 &\le\sum_{\substack{q\in P\\q\le X}}
       \frac1q H_{\lfloor q^{\eta/(1-\eta)}\rfloor}\\
 &\le H_P(X)+\frac{\eta}{1-\eta}W_P(X).
 \end{aligned}
 \tag{2}
$$
The activation condition is essential to $t\ge1$ here.

Primitive sets have logarithmic density zero, as proved in
[structured residues](structured_residues.md). Thus $H_P(X)=o(\log X)$.
Writing $A=\limsup W_P(X)/\log X<\infty$, (2) yields
$$
 \overline{\operatorname{ld}}(B)
 \le\beta+\frac{A\eta}{1-\eta}.
$$
Let $\eta\downarrow0$. Fixed finite prefixes give the reverse lower
bound, proving the claimed logarithmic density. For a finite prefix
$F$, subtracting its periodic harmonic asymptotic gives
$$
 \operatorname{ld}(B\setminus B_F)=\beta-\beta_F.
$$
This tends to zero as the prefix is exhausted, proving the approximation
statement. No natural-density conclusion for $B$ is asserted.

## A finite small-footprint consequence

For a finite coherent primitive family, put
$A_X=W_P(X)/H_{\lfloor X\rfloor}$. The exact multiples comparison
gives $H_P(X)\le\beta H_{\lfloor X\rfloor}$. The finite power-cutoff
bound and (2) consequently imply
$$
 \frac{H_B(X)}{H_{\lfloor X\rfloor}}
 \le f_\eta(\beta)+\beta+\frac{\eta}{1-\eta}A_X,
 \qquad
 f_\eta(\beta)\le\min\left(1,\frac{C}{\eta\log(2/\beta)}\right).
 \tag{3}
$$
In particular, if $A_X\le A$, optimizing $0<\eta\le1/2$ gives
$$
 \frac{H_B(X)}{H_{\lfloor X\rfloor}}
 \le\min\left\{1,\,
       \beta+C'\sqrt{\frac{A+1}{\log(2/\beta)}}\right\}.
 \tag{4}
$$
For the parameter range where the suggested optimizer exceeds $1/2$,
the trivial bound one implies (4) after enlarging $C'$. An empty
family is treated separately. Thus (4) is a uniform finite harmonic
small-footprint bound under a bounded weighted reciprocal hypothesis.

## The condition permits failure of natural density

There are primitive sets satisfying (1) but failing the reciprocal-shell
condition used in the earlier natural-density theorem. Here is a
deterministic recursive example.

Fix $0<\varepsilon<1/3$. Having chosen finite blocks
$P_1,\ldots,P_{j-1}$, let $L_j$ be their common period, taking $L_1=1$.
Choose the least integer $N_j\ge2$ satisfying
$$
 L_j\mid N_j,\quad N_j>2N_{j-1},\quad
 \log N_j\ge2\log N_{j-1},\quad
 \mu(M((N_j,2N_j]\cap\mathbb N))\le\varepsilon2^{-j},
 \tag{5}
$$
omitting conditions involving $N_0$ at the first stage. Such choices
exist by the [uniform multiples-window bound](common_shift_blocks.md),
which holds along all sufficiently large multiples of $L_j$. Set
$$
 P_j=\{q\in(N_j,2N_j]:r\nmid q
                      \text{ for all }r\in P_1\cup\cdots\cup P_{j-1}\}.
$$
No two numbers in one block divide one another, and the definition
prevents divisibility from an older block. Hence $P=\bigcup_jP_j$ is
primitive. Its full multiples footprint $\beta$ is at most
$\sum_j\varepsilon2^{-j}=\varepsilon$.

The old multiples union is $L_j$-periodic with density
$\beta_{<j}\le\varepsilon$. The interval $(N_j,2N_j]$ is an exact
union of periods, so
$$
 |P_j|=(1-\beta_{<j})N_j\ge(1-\varepsilon)N_j,
 \qquad
 \sum_{q\in P_j}\frac1q\ge\frac{1-\varepsilon}{2}.
 \tag{6}
$$
On the other hand $\sum_{N<q\le2N}1/q\le\log2$. Geometric growth
of $\log N_j$ in (5) therefore gives, for all $X\ge2$,
$$
 W_P(X)
 \le(\log2)\sum_{N_j<X}\log(2N_j)
 \le4(\log2)\log X.
 \tag{7}
$$

For any fixed $\eta>0$, put $X_j=2N_j$. Eventually
$X_j^{1-\eta}<N_j$, so the entire $j$th block lies in
$(X_j^{1-\eta},X_j]$. Equation (6) shows that the reciprocal-shell
limsup is at least $(1-\varepsilon)/2$, independently of $\eta$.
Thus the natural-density criterion does not apply.

For the zero center, the multiples union itself has upper natural
density at least $(1-\varepsilon)/2>\beta$, by counting $P_j$ below
$2N_j$. Its logarithmic density equals $\beta$, so natural density
does not exist (natural density, if present, would equal logarithmic
density). Nevertheless (1) proves logarithmic density for every
coherent center on this same modulus set. This example distinguishes
the two density conclusions; it is not a counterexample to Problem 25.
