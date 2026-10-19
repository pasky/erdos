---
name: research/erdos_644/boolean_factor_reduction
desc: A hypothetical fixed-excess P7 counterexample reduces to a conjunction-prime monotone function with vanishing maximum Shapley value, losing only o(k) in transversal number.
tags: [proved, reductions, boolean-functions, limitations]
sources: []
created: 2026-09-23T02:15:00Z
updated: 2026-09-24T22:12:53Z
---


# research/erdos_644/boolean_factor_reduction

***

This route uses disjoint-variable conjunctions and an integral influence
potential, rather than direct Fano selection. It gives a new unrestricted
normalization: any hypothetical fixed-positive-excess counterexample can be made
conjunction-prime and have vanishing maximum Shapley value, with only $o(k)$
transversal loss. It does not prove the three-quarter bound or convergence.

All families here are finite clutters of nonempty sets. Removing nonminimal
edges changes neither the associated monotone function nor the transversal
number or $P_r$. The rank is the maximum edge size. Write $f_{\mathcal H}(X)=1$
when $X$ contains an edge. A zero-restriction deletes the star of a point; it
preserves $P_r$, does not increase rank, and lowers the transversal number by at
most one.

## Products and safe removal of factors

For families on disjoint ground sets define

$$
\mathcal H\otimes\mathcal G=\{E\cup F:E\in\mathcal H,\ F\in\mathcal G\}.
$$

The associated function is $f_{\mathcal H}\wedge f_{\mathcal G}$, and

$$
\operatorname{rank}(\mathcal H\otimes\mathcal G)
=\operatorname{rank}(\mathcal H)+\operatorname{rank}(\mathcal G),
\qquad
\tau(\mathcal H\otimes\mathcal G)=\min\{\tau(\mathcal H),\tau(\mathcal G)\}.
\tag{1}
$$

Indeed, a set covers the product exactly when its restriction to at least one
factor covers that factor. If neither restriction covers, independently choose
an edge avoiding each.

**Lemma.** If $\mathcal G$ has three disjoint edges, then, for every $r\ge3$,

$$
\mathcal H\otimes\mathcal G\text{ has }P_r
\quad\Longleftrightarrow\quad
\mathcal H\text{ has }P_r.
\tag{2}
$$


**Proof.** The reverse implication uses a cover in the $\mathcal H$ coordinates.
For the forward implication, let $H_1,\ldots,H_s$, $s\le r$, be a bad tuple in
$\mathcal H$. For points of its union set

$$
M_x=\{i:x\notin H_i\}.
$$

These missing sets are pairwise intersecting, because two disjoint missing sets
would give a two-cover. Each has size at least two: a point missing only one row
could be supplemented by any point of that row. Choose an inclusion-minimal
missing set $M$ and $i\in M$. It is proper because points are taken from the
union of the rows.

No missing set is contained in any of the three nonempty classes

$$
\{i\},\qquad M\setminus\{i\},\qquad [s]\setminus M.
$$

For the first class use the size condition, for the second minimality, and for
the third intersection with $M$. Assign three disjoint $\mathcal G$-edges to
these three row classes. Two guard points miss a class; two $\mathcal H$ points
fail by assumption; and a mixed pair fails because no $M_x$ is contained in one
class. The resulting product tuple is bad. $\square$

In particular a factor with $\tau>2\operatorname{rank}$ can be removed: a
maximal matching of at most two edges would give a cover of size at most twice
the rank.

## A quantitative obstruction to two remaining factors

**Lemma.** For factor ranks $a,b$ and $r\ge3$, the inequalities

$$
\tau(\mathcal H)>a+\left\lceil\frac a{r-2}\right\rceil,
\qquad
\tau(\mathcal G)>b+\left\lceil\frac b{r-2}\right\rceil
\tag{3}
$$

imply that their product fails $P_r$.

**Proof.** Choose $A\in\mathcal H$. The residual family $\mathcal H_A$ of edges
disjoint from $A$ has

$$
\tau(\mathcal H_A)\ge\tau(\mathcal H)-|A|>
\left\lceil\frac a{r-2}\right\rceil.
$$

Choose $C\in\mathcal H_A$, partition it into $r-2$ parts of size at most the
displayed ceiling, and choose a residual edge avoiding each part. These $r-1$
rows have empty common intersection and all avoid $A$. Obtain an analogous list
in $\mathcal G$, all avoiding some $B\in\mathcal G$.

Pair the two lists to obtain $r-1$ product edges with empty common intersection.
They are all disjoint from $A\cup B$. They require at least two points, and
$A\cup B$ requires a further point, giving a bad at-most-$r$ subfamily.
$\square$

**Corollary.** If both factors have matching number at most two and their
product has $P_7$, then

$$
\tau(\mathcal H\otimes\mathcal G)\le\frac34(a+b)+1.
\tag{4}
$$

To see this, write $t=\min(\tau(\mathcal H),\tau(\mathcal G))$ and $K=a+b$.
Since $t\le2a,2b$, each $x\in\{a,b\}$ is at most $K-t/2$. If $t>3K/4+1$, then

$$
t-\frac65x\ge\frac85t-\frac65K>\frac85,
$$

so (3) holds with $r=7$, a contradiction.

## Reduction to one conjunction-prime factor

Call a nonconstant monotone function conjunction-prime if it is not a
conjunction of two nonconstant monotone functions on disjoint nonempty variable
sets. A finite function can be factored into such functions by repeatedly
splitting; each split reduces the variable sets involved, so the process
terminates. Uniqueness is not needed here.

**Theorem.** If a rank-$k$ family has $P_7$ and

$$
t=\tau(\mathcal H)>\frac34k+1,
\tag{5}
$$

then one of its conjunction-prime factors has $P_7$, transversal number at least
$t$, and rank at most $k$.

**Proof.** Remove factors with matching number at least three, using (2). Some
factor remains: otherwise, after removing all but one, the remaining factor
would have both $P_7$ and three disjoint edges. Every remaining factor has
transversal number at least $t$, by (1), and rank at least $t/2$, because its
matching number is at most two. There are at most two remaining factors, since
their ranks sum to at most $k$ and $2k/t<8/3$. Two factors contradict (4) and
(5). $\square$

This is a safe, quantitatively controlled use of setting variables to one.
Arbitrary one-restrictions do not preserve $P_7$; see
[Boolean reductions](boolean_reductions.md).

## Removing high-Shapley coordinates

For a monotone Boolean function $f$, let $\mu_p(f)$ be its Bernoulli-$p$ mean
and put

$$
A(f)=\int_0^1\mu_p(f)\,dp.
$$

Write $I_i(p)=\mathbb E[f(X\cup\{i\})-f(X)]$, with $X$ Bernoulli-$p$ on the
other coordinates. The Shapley value is

$$
\phi_i(f)=\int_0^1 I_i(p)\,dp.
\tag{6}
$$

For completeness, each fixed predecessor set of size $j$ has probability
$j!(n-1-j)!/n!$ in a random ordering; the same number is
$\int_0^1p^j(1-p)^{n-1-j}\,dp$, proving (6).

Zero-restricting coordinate $i$ decreases $A$ by

$$
A(f)-A(f|_{x_i=0})=\int_0^1pI_i(p)\,dp
\ge\frac{\phi_i(f)^2}{2}.
\tag{7}
$$

For the inequality, among functions $0\le I\le1$ with integral $\phi$, the
weighted integral against $p$ is minimized by $1_{[0,\phi]}$. Equivalently,
integrate the nonnegative function $(p-\phi)(I(p)-1_{[0,\phi]}(p))$.

Consequently at most $2\delta^{-2}$ successive zero-restrictions are needed to
make every Shapley value less than $\delta$, unless the function becomes zero.
For a family with $\tau>2\delta^{-2}$, the latter alternative is impossible.
This normalization preserves $P_r$ and the rank bound and loses at most
$2\delta^{-2}$ in transversal number.

## Charging the cost of removing conjunction factors

The preceding normalization can be combined with prime-factor reduction, even
though factor removal increases $A$.

Suppose $f=h\wedge g$ on disjoint variables, the rank of $g$ is $s$, and
$\tau(g)\ge t_0$, where $\log t_0\ge4$. A maximal matching in $g$ has
$m\ge t_0/s$ edges. Its disjoint edges show

$$
1-\mu_p(g)\le(1-p^s)^m.
$$

For independent uniform $U_1,\ldots,U_m$ on $[0,1]$, Jensen's inequality gives

$$
\int_0^1(1-p^s)^m\,dp
=\mathbb E\bigl[(\min_jU_j)^{1/s}\bigr]
\le(m+1)^{-1/s}
\le(s/t_0)^{1/s}.
$$


Writing $L=\log t_0$, this integral is at most $s/L$. For $s\ge L$ use the bound
one. Otherwise $\log(t_0/s)\ge L/2$ and

$$
(s/t_0)^{1/s}\le e^{-L/(2s)}\le s/L,
$$

the last inequality following from $2u e^{-u}\le2/e<1$. Thus

$$
A(h)-A(f)
=\int_0^1\mu_p(h)(1-\mu_p(g))\,dp
\le\frac{s}{\log t_0}.
\tag{8}
$$


Ranks add under independent conjunction, and zero-restrictions never increase
rank. Hence the sum of the ranks of all stripped factors, even if decompositions
change during the process, is at most the initial rank $k$.

## Simultaneous prime and low-influence normalization

**Theorem.** Fix $\varepsilon>0$. For sufficiently large $k$, every finite
rank-at-most-$k$ family with $P_7$ and

$$
\tau(\mathcal H)>(3/4+\varepsilon)k
$$

can be transformed into a family $\mathcal H'$ such that

$$
\begin{gathered}
\mathcal H'\text{ has }P_7,\qquad
\operatorname{rank}(\mathcal H')\le k,\\
\tau(\mathcal H')\ge\tau(\mathcal H)
-O\!\left(\frac{k}{\sqrt{\log k}}\right),\\
f_{\mathcal H'}\text{ is conjunction-prime},\qquad
\max_i\phi_i(f_{\mathcal H'})<(\log k)^{-1/4}.
\end{gathered}
\tag{9}
$$


**Proof.** Put $\delta=(\log k)^{-1/4}$ and $t_0=k/2$. Alternate prime-factor
reduction with zero-restricting a coordinate of Shapley value at least $\delta$
whenever one exists. Each operation removes variables, so a finite run
terminates.

Provisionally stop if the number $q$ of zero-restrictions reaches
$\lfloor\varepsilon k/2\rfloor$. Before and at this stop the current transversal
number is greater than $(3/4+\varepsilon/2)k$. This exceeds both $t_0$ and three
quarters of the current rank plus one, for large $k$. Prime-factor reduction is
therefore always legitimate, and every removed factor has transversal number at
least $t_0$.

Equations (7), (8), the rank budget, and $0\le A\le1$ give

$$
q\frac{\delta^2}{2}
\le1+\frac{k}{\log(k/2)}.
\tag{10}
$$

The resulting bound $q=O(k/\sqrt{\log k})$ rules out the provisional stop. The
process ends with both required properties. Only zero-restrictions can lower the
transversal number, and each loses at most one. $\square$

Since $P_7$ implies matching number at most two,
$\tau(\mathcal H')\le2\operatorname{rank}(\mathcal H')$. Thus the output rank
remains $\Theta(k)$, and (9) preserves any fixed positive excess over three
quarters.

## Scope of the Boolean route

The normalized function is not proved to have a threshold minor preserving its
certificate ratio. The low-Shapley threshold-minor theorem examined in this
route gives threshold functions of arbitrarily large fixed arity, but not a
comparison of their ranks and transversal numbers with the original ones; an
AND-type minor is allowed. See [Brakensiek--Guruswami--Sandeep, Lemma
13](https://eccc.weizmann.ac.il/report/2021/026/download).

The explicit guard example in
[Boolean reductions](boolean_reductions.md#small-rank-guards-can-push-the-critical-bias-to-one)
shows that low Shapley values alone do not control threshold location, even near
three-quarter extremality. The factor theorem removes that exact product.
However, [Prime guard families](prime_guard_families.md) proves that deleting
one product edge makes the example conjunction-prime without changing its
transversal number. Its maximum Shapley value still tends to zero and its
critical bias tends to one. The same negligible-rank transformation applies
conditionally to any hypothetical fixed-excess sequence. Thus exact
conjunction-primality does not exclude almost-independent guards.

A safe partial-product projection is available when omitted guard fibers have
bounded transversal number and the guard's transversal number is sufficiently
large relative to that bound and its rank. It removes the new explicit examples.
No theorem extracting such structure from an arbitrary normalized family has
been established, nor any theorem linking the normalized hypotheses to the
needed certificate-ratio bound.

Neither (9) nor the finite promise-relation formulation supplies an amplifier or
a comparison between arbitrary uniformities. The fixed-$r$ convergence assertion
remains unresolved.
