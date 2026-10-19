---
name: research/erdos_644/matroid_base_families
desc: An online balancing argument proves the complete-family coefficient, with bounded additive error, for matroid base families for every fixed local parameter.
tags: [proved, restricted-upper-bounds, limitations]
sources: [fon_der_flaass_et_al_1999_transversals_uniform_hypergraphs_property_7_2]
created: 2026-09-22T22:02:23Z
updated: 2026-09-24T22:12:53Z
---


# research/erdos_644/matroid_base_families

***

This page proves both proposed asymptotic conclusions **within the subclass of
matroid base families**. It does not prove either assertion for arbitrary
uniform set families.

Write $P_r$ for the property that every subfamily of at most $r$ members has a
transversal of size at most two. For fixed $r\ge3$, let $h_{\mathrm{mat}}(k,r)$
be the largest transversal number of a rank-$k$ matroid base family satisfying
$P_r$. The initial definitions and proof use finite ground sets and $k\ge1$; a
finite-restriction argument below also handles infinite ground sets of finite
rank.

Let $\lambda_r$ be the finite rational parameter from
[Complete-family asymptotics](complete_families.md):

$$
\lambda_r=\min_{\mathcal F,w}\max_{i\in[r]}
 \sum_{\substack{F\in\mathcal F\\i\in F}}w_F,
\tag{1}
$$

where $\mathcal F$ is a pairwise intersecting family of nonempty subsets of
$[r]$, the weights are nonnegative, and $\sum_Fw_F=1$. Put

$$
c_r^{\mathrm{mat}}=\frac{\lambda_r}{1-\lambda_r}.
$$

Then

$$
\boxed{h_{\mathrm{mat}}(k,r)=c_r^{\mathrm{mat}}k+O_r(1).}
\tag{2}
$$

In particular, $\lambda_7=3/7$, and an explicit bound proved below is

$$
\boxed{\left\lceil\frac{3k}{4}\right\rceil
 \le h_{\mathrm{mat}}(k,7)
 \le \frac34(k-1)+192.}
\tag{3}
$$

The constants are not claimed to be optimal.

## Transversals of bases and extension degree

Let $M$ be a matroid on $E$ of rank $k\ge1$, with base family $\mathcal B(M)$. A
hyperplane is a maximal nonspanning flat; its complement is a cocircuit. For
$T\subseteq E$,

$$
\begin{aligned}
T\text{ meets every basis}
&\iff E\setminus T\text{ contains no basis}\\
&\iff r_M(E\setminus T)<k\\
&\iff E\setminus T\text{ is contained in a hyperplane}\\
&\iff T\text{ contains a cocircuit}.
\end{aligned}
$$

Consequently

$$
\tau(\mathcal B(M))=\operatorname{cogirth}(M),
\tag{4}
$$

where the cogirth is the minimum cocircuit size.

For an independent set $I$ with $|I|<k$, define its set of one-point extensions
by

$$
L_M(I)=\{e\in E\setminus I:I\cup\{e\}\text{ is independent}\}
       =E\setminus\operatorname{cl}_M(I).
$$

The closure of $I$ is contained in a hyperplane $H$, so $L_M(I)$ contains the
cocircuit $E\setminus H$. Conversely, if $H$ is a hyperplane with smallest
complement and $I$ is a basis of $H$, then $|I|=k-1$ and $L_M(I)=E\setminus H$.
Thus

$$
\min_{\substack{I\text{ independent}\\|I|<k}}|L_M(I)|
=\operatorname{cogirth}(M)
=\tau(\mathcal B(M)).
\tag{5}
$$

Loops and parallel elements cause no difficulty.

## Online balancing lemma

The construction first applies to a general pure hereditary independence system.
Let $\mathcal I\subseteq2^E$ be hereditary on a finite set $E$, with every
maximal member of size $k\ge1$. Let $\mathcal H$ be its family of maximal
members, and write

$$
\delta(\mathcal I)=
\min_{\substack{I\in\mathcal I\\|I|<k}}
\left|\{e\in E\setminus I:I\cup\{e\}\in\mathcal I\}\right|.
\tag{6}
$$


**Lemma.** Suppose $C_1,\ldots,C_m\subseteq[r]$ is a multiset of patterns such
that

$$
C_u\cup C_v\ne[r]\qquad(u,v\in[m]),
\tag{7}
$$

and every coordinate belongs to exactly $d$ of the patterns, where $0<d<m$. Put
$a=m-d$. If $\mathcal H$ satisfies $P_r$, then

$$
\delta(\mathcal I)\le \frac ad(k-1)+2^{r-1}a.
\tag{8}
$$

For a matroid, (5) therefore gives

$$
\tau(\mathcal B(M))\le \frac ad(k-1)+2^{r-1}a.
\tag{9}
$$


**Proof.** Process the elements of $E$ in any order. Maintain independent sets
$B_1,\ldots,B_r$, initially empty. When processing $e$, form its active type

$$
A_e=\{i\in[r]:B_i\cup\{e\}\in\mathcal I\}.
$$

For each of the $2^r$ possible active types $A$, maintain a separate cyclic
counter. On the successive occurrences of type $A$, assign the patterns

$$
C_1,C_2,\ldots,C_m,C_1,C_2,\ldots
$$

in this order. If $e$ receives pattern $C_j$, add it to $B_i$ exactly when
$i\in A_e\cap C_j$. The sets $B_i$ remain independent.

Fix a row $i$. An occurrence with $i\in A_e$ is a success if $e$ is added to
$B_i$, and a failure otherwise. Denote the total numbers of successes and
failures by $S_i$ and $F_i$. Each success adds one previously unprocessed
element, so $S_i=|B_i|$ at the end.

For a fixed active type $A\ni i$, every complete cycle contributes $d$ successes
and $a$ failures. Write its totals as $S_{A,i}$ and $F_{A,i}$. Its unfinished
cycle contains at most $a$ failures, hence

$$
dF_{A,i}-aS_{A,i}\le da.
$$

There are $2^{r-1}$ active types containing $i$. Summing gives

$$
dF_i-aS_i\le 2^{r-1}da,
\qquad
F_i\le\frac ad|B_i|+2^{r-1}a.
\tag{10}
$$

This argument permits the active types to depend on all previous choices: each
type has its own counter, and only its final complete and unfinished cycles are
counted.

The final row spectrum of an element is

$$
Q_e=\{i:e\in B_i\}.
$$

It is a subset of the pattern assigned to $e$. By (7), for any two elements
$e,f$ there is a row containing neither. In particular, the final family
$B_1,\ldots,B_r$ has no transversal of size at most two. If every $B_i$ had size
$k$, all would belong to $\mathcal H$, contradicting $P_r$. Repeated rows may be
removed without creating a two-point transversal. Hence some final row $B_i$
satisfies $|B_i|\le k-1$.

Every one-point extension $e$ of this final $B_i$ was active in row $i$ when
processed. Indeed, the then-current row was a subset of the final row, and
heredity preserves the independence of its union with $e$. Since $e$ is not in
the final row, it was not added and is counted in $F_i$. Therefore

$$
\delta(\mathcal I)
\le |\{e\notin B_i:B_i\cup\{e\}\in\mathcal I\}|
\le F_i
\le \frac ad(k-1)+2^{r-1}a.
$$

This proves (8); (9) follows from (5). $\square$

Equivalently, in the matroid case one may choose a hyperplane containing the
deficient final row. Every element of its complementary cocircuit was an active
failure, so that cocircuit is contained in the set counted by $F_i$.

## Optimal rational patterns for each fixed local parameter

The parameter in (1) satisfies $0<\lambda_r<1$ and is rational. There are
finitely many possible intersecting supports, and each corresponding
optimization is a rational linear program. Nonempty support sets give
$\lambda_r\ge1/r$; the uniform distribution on the $(r-1)$-subsets gives
$\lambda_r\le(r-1)/r<1$.

For completeness, the balancing step from
[Complete-family asymptotics](complete_families.md) is as follows. Start with an
optimal rational distribution and let

$$
p_i=\sum_{F\ni i}w_F\le\lambda_r.
$$

For each sampled $F$, independently insert every missing coordinate $i$ with
probability

$$
\frac{\lambda_r-p_i}{1-p_i}.
$$

The resulting distribution is rational, and the load of every coordinate is
exactly $\lambda_r$. Its support remains pairwise intersecting because every new
set contains an old support set.

Clear denominators to express this distribution as the uniform distribution on a
multiset $F_1,\ldots,F_m$. Every coordinate lies in exactly

$$
a=\lambda_rm
$$

of these sets. Their complements $C_j=[r]\setminus F_j$ satisfy (7), since the
$F_j$ are pairwise intersecting. Every coordinate lies in exactly

$$
d=(1-\lambda_r)m
$$

of the complements. Applying (9) proves

$$
h_{\mathrm{mat}}(k,r)
\le \frac{\lambda_r}{1-\lambda_r}(k-1)+2^{r-1}a.
\tag{11}
$$

Here $a$ and $m$ depend only on $r$.

### Matching lower bound

Take

$$
n=\left\lceil\frac{k}{1-\lambda_r}\right\rceil-1.
$$

The complete family $\binom{[n]}k$ is the base family of the uniform matroid
$U_{k,n}$. Suppose at most $r$ of its members had no two-point transversal.
Repeat rows if needed to obtain $A_1,\ldots,A_r$ with that property. For each
$x\in[n]$, put

$$
F_x=\{i:x\notin A_i\}.
$$

These sets are nonempty and pairwise intersecting. Giving them their
multiplicities divided by $n$ defines an admissible distribution in (1). Every
coordinate has load $(n-k)/n$, which is strictly smaller than $\lambda_r$ by the
choice of $n$. This is a contradiction. Thus the uniform matroid has $P_r$.

Its transversal number is

$$
n-k+1
=\left\lceil\frac{\lambda_r}{1-\lambda_r}k\right\rceil.
\tag{12}
$$

Together, (11) and (12) prove (2), including convergence for every fixed $r$
within the matroid-base subclass.

If the local property is instead required only for exactly $r$ distinct members,
a family with at least $r$ members also has the at-most-$r$ property: extend a
smaller purported counterexample to $r$ members. A family with fewer than $r$
nonempty members has transversal number at most $r-1$. Since $2^{r-1}a\ge r-1$,
the upper bound (11) still applies without changing its constant.

## The Fano specialization

Use the seven complements of lines of a Fano plane on the row set $[7]$. Two
such complements cannot cover all seven rows because their complementary lines
intersect. Every row lies in four of the seven caps. Hence $m=7$, $d=4$, $a=3$,
and (9) becomes

$$
\tau(\mathcal B(M))\le \frac34(k-1)+192.
$$

The equality $\lambda_7=3/7$ is also elementary. If an intersecting support
family contains a set of size at most two, the coordinate loads on that set sum
to at least one, so the maximum load is at least $1/2$. Otherwise all support
sets have size at least three, so the maximum load is at least $3/7$. Uniform
weights on the seven Fano lines attain $3/7$. The lower bound (12) now gives
(3).

## Why extension degree does not control arbitrary families

The online construction itself needs only heredity. The special matroid input is
(5), which turns its extension-degree conclusion into a transversal bound. For a
general uniform family, that identity can fail by a linear amount, even when the
family satisfies $P_r$.

Here is a self-contained example. Start with any nonempty $\ell$-uniform family
$\mathcal G$, where $\ell\ge1$, and give each edge $A\in\mathcal G$ its own new
point $p_A$. Put

$$
\mathcal H=\{A\cup\{p_A\}:A\in\mathcal G\}.
$$

If $\mathcal G$ has $P_r$, then so does $\mathcal H$, since an old two-point
transversal still meets the enlarged edges. Moreover,

$$
\tau(\mathcal H)=\tau(\mathcal G).
$$

One inequality follows by retaining an old transversal. For the other, replace
every private point $p_A$ in a transversal by an arbitrary old element of $A$.
This loses no edge previously met by that private point and does not increase
the transversal size.

In the downward closure $\mathcal I$ of $\mathcal H$, the only one-point
extension of an old edge $A$ is $p_A$: any new edge containing all of $A$ must
have old part exactly $A$. Thus $\delta(\mathcal I)=1$. Taking $\mathcal G$ to
be the complete-family lower-bound example of uniformity $\ell=k-1$ gives

$$
P_r,\qquad
\delta(\mathcal I)=1,\qquad
\tau(\mathcal H)=\left\lceil c_r^{\mathrm{mat}}(k-1)\right\rceil.
\tag{13}
$$

Consequently the extension-degree lemma cannot be applied to arbitrary $P_r$
families by simply replacing $\delta$ with $\tau$.

The same obstruction occurs without private padding. Theorem 1 in Section 2 of
[Fon-Der-Flaass, Kostochka, and
Woodall](../../../library/set_systems/fon_der_flaass_et_al_1999_transversals_uniform_hypergraphs_property_7_2/_index.md)
gives, for $q\ge10$,

$$
|X|=4q,\quad |Y|=3q+1,\qquad
\mathcal H=\{A\in\tbinom{X\cup Y}{4q}:|A\cap X|\text{ is odd}\},
$$

with $P_7$ and $\tau(\mathcal H)=3q+1$. For even $q$, choose a $(4q-1)$-set $I$
with $q-1$ elements of $X$ and $3q$ elements of $Y$. Its $X$-count is odd.
Adding the sole remaining point of $Y$ produces an edge, whereas adding any
point of $X$ makes that count even. Hence its downward closure again has
$\delta=1$. For every $q\ge10$, choosing $4q-2$ elements of $X$ and one element
of $Y$ gives a $(4q-1)$-set with exactly two extensions, the two unused points
of $X$.

These examples identify the gap in this method. They do not contradict the
conjectured transversal bound for arbitrary families.

### The active-failure sets need not be global transversals

A stronger proposed repair would ask whether the cyclic construction itself
always produces a deficient row whose entire active-failure set is a
transversal, even when its final extension set is not. This also fails, for
every element order, in the following example.

Let $k\ge965$, put

$$
n_0=\left\lfloor\frac{6k}{5}\right\rfloor-1,
$$

and take disjoint sets $V_1,V_2$ of size $n_0$. Define

$$
\mathcal H=\binom{V_1}{k}\cup\binom{V_2}{k}.
$$

Any at most six edges within one component have nonempty common intersection,
since

$$
n_0-6(n_0-k)=6k-5n_0>0.
$$

The family has $P_7$: if a subfamily uses both components, each contributes at
most six edges, so one point in each component suffices. If all its edges lie in
one component, split them into two nonempty groups of at most six and take a
common point for each group; a one-edge subfamily needs only one point. On the
other hand,

$$
\tau(\mathcal H)=2(n_0-k+1)=2\left\lfloor\frac k5\right\rfloor.
$$


Run the seven-row Fano-cap construction on the downward closure of $\mathcal H$,
with any element order and any fixed order of the seven caps in each active-type
cycle. While a row is empty, every processed element is active in that row.
Before its first success, any one of its $64$ possible active types can
contribute at most three failures, because only three of the seven caps omit
that row. Hence every row receives its first element by the $193$rd processed
element.

After that first success, the row is confined to the component containing its
first element: a set meeting both components is not independent in this downward
closure. All subsequent elements from the other component are inactive.
Consequently the row's full active-failure set has at most $192$ elements in
that other component. But

$$
\tau\!\left(\binom{V_j}{k}\right)
=\left\lfloor\frac k5\right\rfloor>192.
$$

Thus some edge of the other component avoids its active-failure set. This holds
for every row, including every deficient row. No choice of element order repairs
the proposed global-transversal property.

The example has transversal number asymptotic to $2k/5$, so it does not
challenge the conjectured $3k/4$ upper bound. It shows that the matroid proof
cannot be extended by asserting that its constructed failure sets automatically
hit all edges.

## Alternate probabilistic proof with a weaker error term

A useful separate inequality is the following reliability bound. If a finite
matroid $M$ has rank $k$ and cogirth at least the positive integer $t$, and $R$
includes each element independently with probability $p$, then

$$
\Pr(R\text{ spans }M)
\ge \Pr\!\left(\operatorname{Bin}(k+t-1,p)\ge k\right).
\tag{14}
$$


To prove it, write the right side as $S(k,t)$. The boundary values are
$S(0,t)=1$ and $S(k,1)=p^k$, and

$$
S(k,t)=pS(k-1,t)+(1-p)S(k,t-1).
$$

Induct on $k+t$. Rank zero is immediate; for $t=1$, retaining a fixed basis has
probability $p^k$. Otherwise choose a nonloop $e$. Since $t\ge2$, it is not a
coloop. The contraction $M/e$ has rank $k-1$ and cogirth at least $t$, while
$M\setminus e$ has rank $k$ and cogirth at least $t-1$. Indeed, cocircuits of
the contraction are cocircuits of $M$ avoiding $e$, and deletion can remove at
most $e$ from a cocircuit. Conditioning on whether $e$ is retained and using the
displayed recurrence proves (14).

Now assign each element independently and uniformly one of the seven Fano caps.
For row $i$, let $R_i$ consist of the elements whose assigned cap contains $i$.
Each $R_i$ is a Bernoulli $4/7$ subset, although the seven subsets are not
mutually independent. If

$$
7\Pr\!\left(\operatorname{Bin}(k+t-1,4/7)<k\right)<1,
\tag{15}
$$

the union bound gives an assignment in which all seven $R_i$ span. Choose a
basis inside each $R_i$. Its element spectra are cap subsets, so the seven bases
have no two-point transversal.

The binomial lower-tail estimate in (15) gives

$$
h_{\mathrm{mat}}(k,7)\le\frac34k+O(\sqrt{k}).
$$

This is weaker than the online balancing bound but gives the exact useful
criterion (15). The online argument removes the fluctuations responsible for its
square-root error by balancing separately within each of the finitely many
active types.

## Infinite ground sets of finite rank

Let $M$ have finite rank $k\ge1$, possibly on an infinite ground set, and
suppose every cocircuit has size at least a positive integer $T$. There exists a
full-rank finite restriction $M|F$ with cogirth at least $T$ and

$$
|F|\le Tk.
\tag{16}
$$


Choose $T$ pairwise disjoint independent sets $I_1,\ldots,I_T$ maximizing the
finite integer $|F|$, where $F=\bigcup_jI_j$. Such a maximum is attained because
each independent set has size at most $k$. If a hyperplane $H$ of $M$ satisfied
$|F\setminus H|<T$, some $I_j$ would lie inside $H$. Since
$|E\setminus H|\ge T$, there would be an element
$e\in(E\setminus H)\setminus F$. Adding it to $I_j$ would preserve independence
and disjointness, contradicting maximality. Thus every hyperplane has at least
$T$ elements of $F$ outside it.

In particular, $F$ spans $M$. Every hyperplane of $M|F$ extends by closure to a
hyperplane of $M$, so its complement in $F$ has size at least $T$. This proves
(16).

Bases of this full-rank restriction are bases of $M$, so they inherit $P_r$.
Applying the finite upper bound rules out every integer $T$ larger than the
right side of (11). In particular, the cogirth cannot be infinite. Taking $T$
equal to the resulting finite cogirth gives the same bound for $M$ itself. Thus
allowing infinite ground sets of finite rank does not change (2).

## Remaining unrestricted questions

The construction proves the complete-family coefficient exactly to first order
for matroid bases. No reduction of an arbitrary $P_r$ family to matroid bases
preserving its transversal number up to $o(k)$ has been proved. The
extension-degree examples show that such a reduction cannot be replaced by a
direct identification of extension degree with transversal number. Both
assertions of [Problem 644](../../problems/set_systems/E0644/_index.md) remain
unresolved for arbitrary uniform families.
