---
name: research/leads/complete_bipartite_size_ramsey
title: Packing Colourings and the Size Ramsey Number of K(n,n)
desc: |
  Two full-solution routes for the size Ramsey number of K(n,n). The direct
  route needs an integral overload bound (N0) for colourings of
  K(kappa n^2, C 2^n), which would give order n^2 2^n; the conjectured
  n^3 2^n needs balanced-host and arbitrary-host colourings. Both remain
  open. Affine colourings, a reduction by deleting common neighbourhoods,
  failed mechanisms and finite diagnostics are retained.
problems:
- 560
research_state: blocked
review_status: unreviewed
created: 2026-10-16T14:11:47Z
updated: 2026-10-16T15:20:26Z
---

# Packing Colourings and the Size Ramsey Number of K(n,n)

[[research/leads/_index|..]]

[[research/leads/complete_bipartite_size_ramsey/evidence/_index|evidence/]]: Exact checks of the n = 2 and n = 3 host diagnostics: stored colourings of
complete bipartite hosts and of K_17, the counting thresholds, b(2) = 5, and
the exhaustive n = 2 host class with its orbit-count completeness check.
Also checks the 30-hyperplane colouring at n = 4. A separate discovery
script writes the SAT instances.

***

This lead's results that are not drawn from a cited source are Plasma AI's,
credited to Plasma AI.

## Target and status evidence

[[problems/ramsey_theory/E0560/_index|Problem 560]] asks for the size Ramsey
number $\hat R(K_{n,n})$, the least number of edges of a graph every
red/blue colouring of which contains a monochromatic copy of $K_{n,n}$, read
there as its asymptotic order. The problem page records the status open, with

$$
\tfrac1{60}n^22^n<\hat R(K_{n,n})\le4e\,n^32^n
$$

for all $n\ge1$: the lower bound is
[[../library/ramsey_theory/erdos_rousseau_1993_size_ramsey_number_complete_bipartite/theorem_1|Erdős and Rousseau's Theorem 1]],
and the upper bound is
[[../library/ramsey_theory/conlon_2023_three_early_problems_size_ramsey_numbers/proposition_2_1|Proposition 2.1]]
of Conlon, Fox and Wigderson (CFW). Their
[[../library/ramsey_theory/conlon_2023_three_early_problems_size_ramsey_numbers/proposition_2_2|Proposition 2.2]]
extends the lower-bound method to $t\ge s+2$, with a different constant.
Their
[[../library/ramsey_theory/conlon_2023_three_early_problems_size_ramsey_numbers/conjecture_5_1|Conjecture 5.1]]
predicts $\hat R(K_{n,n})=\Theta(n^32^n)$, and
[[../library/ramsey_theory/conlon_2023_three_early_problems_size_ramsey_numbers/theorem_1_1|their Theorem 1.1]]
gives only $\Omega(n^22^n)$ on the diagonal. A status check made on
2026-10-16 (the erdosproblems.com problem page and proof-claim tab, the
erdosproblems.ai discussion, the Palomar registry, an arXiv title and abstract
search for size Ramsey results on bipartite graphs since 2023, and this
record) found no claim that determines the order.

This page is the editable proof sketch of two routes to the order. The
direct route is the primary one: prove the integral overload assertion (N0)
below for complete bipartite hosts with one side of order $n^2$ and the other
of order $2^n$. With the cited Erdős--Rousseau lower bound this would give
$\hat R(K_{n,n})=\Theta(n^22^n)$, against Conjecture 5.1. The opposite route
aims at the lower half of Conjecture 5.1: colour every host with at most
$cn^32^n$ edges without a monochromatic $K_{n,n}$.

The page contains no proof or disproof of the target. Its findings are the
following. (N0) is open, and a proof of it must exclude integral families
although the balanced fractional family is feasible; several natural proof
mechanisms fail at stated scopes, and a Harris-product argument cannot
decouple the colours (Lemma 8). Affine colourings obey a stronger overload
bound when $a\ge8n^2$ (Proposition 7), excluding linear-code cosets in
that range. Lemma 9 reduces (N0) to families in which every $n-1$ columns
have fewer than $\lceil(2+\delta)n\rceil$ common neighbours in either
colour, after deleting $O_\delta(n)$ points. It supplies no overload bound
for those remaining families. The lower-bound
route cannot pass the order $n^22^n$ without lower bounds for bipartite and
ordinary Ramsey numbers of $K_{n,n}$ beyond the random-colouring bounds
checked here (Proposition 3 and Corollary 5). That is a necessary
consequence, not a proof that such colourings cannot exist. Everything here is
author-recorded and not independently reviewed.

## Conventions

Graphs are finite and simple. A host $H$ is Ramsey for $K_{n,n}$, written
$H\to K_{n,n}$, when every red/blue colouring of $E(H)$ has a monochromatic
copy of $K_{n,n}$, not necessarily induced; $\hat R(K_{n,n})$ is the least
$e(H)$ over such $H$. The Ramsey number $r(K_{n,n})$ is the least $N$ with
$K_N\to K_{n,n}$, and the bipartite Ramsey number $b(n)$ is the least $N$ with
$K_{N,N}\to K_{n,n}$. For integers $a,n\ge1$, let
$B(a,n)=\sup\{b\in\mathbb Z_{\ge0}:K_{a,b}\not\to K_{n,n}\}$, taking
the value $\infty$ when this set is unbounded. Thus $B(a,1)=0$, and
$B(a,n)=\infty$ when $a\le2n-2$. We use $\binom un=0$ for integers
$0\le u<n$. Logarithms without a base are natural. Host sizes in asymptotic
formulas are rounded to integers, without changing the stated estimates.

## The route as a proof sketch

There are two complete possible determinations, with distinct missing
proofs. The upper-bound route below would decide the order without an
arbitrary-host reduction. The lower-bound route has three further
obligations beyond a local packing construction; they cannot be omitted
from its conclusion.

**Upper-bound route.** Choose fixed $\kappa,C>0$ and prove that, for all
sufficiently large $n$, any multiset of more than $C2^n$ subsets of an
$a=\lceil\kappa n^2\rceil$ element set has an $n$-set contained in at
least $n$ members or disjoint from at least $n$ members. Multiplicities
count in both loads. This is the structural overload assertion (N0).
By Lemma 1 it makes
$K_{a,\lfloor C2^n\rfloor+1}$ Ramsey, with $O(n^22^n)$ edges.
Together with the cited Erdős--Rousseau lower bound it determines
$\hat R(K_{n,n})=\Theta(n^22^n)$. The implication is elementary; the
structural overload assertion is unproved.

The integral family is essential. In the balanced fractional family
described after Lemma 2, a total weight $C2^n$ gives each colour load
$C2^np_n(a)=(C+o(1))e^{-1/(2\kappa)}$, below $n-1$ for every fixed
$C$ and large $n$. Thus a proof of this route must exclude integral
families even though the symmetric fractional family remains feasible.
Another use of that fractional capacity cannot supply the missing
overload. A finite construction is useful here only through a mechanism
that could control every sufficiently large $n$; success or failure of
one such construction decides neither (N0) nor (N1).

The held links of this route are Lemma 1, the Erdős--Rousseau theorem at its
library standing, and the elementary edge count. Its only gap is (N0) itself,
whose one-colour form (N0$'$) below implies it. Lemma 9 permits imposing its
two common-neighbourhood bounds, with a change in the fixed constant
$\kappa$; proving overload even with these extra
hypotheses is open. The section on attacks on (N0) records the mechanisms
tried for it, the class of colourings where it is proved, and the reasons
the other mechanisms fail.

**Lower-bound route.**
Target (T): there is $c>0$ such that for all large $n$ every host $H$ with
$e(H)\le cn^32^n$ has a colouring without a monochromatic $K_{n,n}$. The
proposed argument has four steps, each a gap:

1. Hosts $K_{a,b}$ with $a\le b$, $ab\le cn^32^n$ and $a$ of order $n^2$:
   integral packings near the capacity of Lemma 2. This contains (N1) below.
   Open.
2. Every other $K_{a,b}$ with $a\le b$ and $ab\le cn^32^n$, including the
   balanced host $a=b=\lfloor\sqrt c\,n^{3/2}2^{n/2}\rfloor$. Step 1 says
   nothing here. Open, and at the balanced host it is (N2).
3. Complete hosts $K_N$ with $\binom N2\le cn^32^n$. Open; also (N2).
4. A structure step reducing an arbitrary host to pieces of the kinds in steps
   1 to 3, with compatible colours on shared edges and control of copies that
   use several pieces. Open; no mechanism is proposed here.

Steps 1 to 4 together give (T), and (T) gives the conclusions of steps 1 to 3
directly, so each of those is necessary. The held links are Lemmas 1 and 2,
Propositions 3 and 4 and Corollary 5 below, author-recorded and elementary,
and the cited source results at their library standing (statements checked,
proofs followed but not checked). No provisional premise is adopted. The
route still faces step 2 at its balanced end even if step 1 is supplied:
by Corollary 5(a) step 2's conclusion is a lower bound for the bipartite
Ramsey number $b(n)$ a factor of order $\sqrt n$ above the literature lower
bound quoted below. That input
is unknown, not known false. Proposition 4 explains why two natural
first-moment arguments do not supply it.

## The packing form of complete bipartite hosts

Colour $K_{a,b}$ with parts $X$ ($|X|=a$) and $Y$ ($|Y|=b$), and let
$R_y\subseteq X$ be the red neighbourhood of $y\in Y$. The family
$(R_y)_{y\in Y}$ may repeat sets.

**Lemma 1 (packing form).** For $n\ge1$ the colouring has no monochromatic
$K_{n,n}$ if and only if every $n$-set $S\subseteq X$ satisfies

$$
\#\{y:S\subseteq R_y\}\le n-1
\quad\text{and}\quad
\#\{y:S\cap R_y=\emptyset\}\le n-1 .
$$

*Proof.* A copy of $K_{n,n}$ is connected and bipartite, so its bipartition is
unique up to exchange. The host's bipartition restricts to one, so each
copy is $S\times T$ with $S\subseteq X$, $T\subseteq Y$ and $|S|=|T|=n$. It
is red exactly when $S\subseteq R_y$ for every $y\in T$, and blue exactly when
$S\cap R_y=\emptyset$ for every $y\in T$. $\square$

Call the two counts the red and blue loads of $S$. Write
$m(a,n)=\min_{0\le r\le a}\bigl[\binom rn+\binom{a-r}n\bigr]$; the summand is
convex in $r$, so the minimum is at $r=\lfloor a/2\rfloor$.

**Lemma 2 (capacity).** If $b\,m(a,n)>2(n-1)\binom an$, then
$K_{a,b}\to K_{n,n}$. Hence $B(a,n)\le\operatorname{cap}(a,n)$, where
$\operatorname{cap}(a,n)=\lfloor2(n-1)\binom an/m(a,n)\rfloor$ when
$m(a,n)>0$, that is when $a\ge2n-1$.

*Proof.* Each $y$ is counted in the loads of at least $m(a,n)$ pairs (an
$n$-set and a colour), and there are $2\binom an$ pairs, each of load at most
$n-1$ in a good colouring. $\square$

This is the counting behind Proposition 2.1. When $a\le2n-2$, repeat any
column whose red and blue parts both have fewer than $n$ points to obtain
$B(a,n)=\infty$. For even $a\ge2n$,
$m(a,n)=2\binom{a/2}n$ and $\operatorname{cap}(a,n)=\lfloor(n-1)/p_n(a)\rfloor$
with

$$
p_n(a)=\frac{\binom{a/2}n}{\binom an}
=2^{-n}\prod_{i<n}\Bigl(1-\frac i{a-i}\Bigr)
=2^{-n}\exp\Bigl(-\frac1{2\kappa}+O\bigl(\tfrac1n\bigr)\Bigr)
\quad(a=\kappa n^2+O(1),\ \kappa>0\text{ fixed}).
$$

For odd $a\ge2n-1$, choose between the two middle column sizes with equal
probability, uniformly within each size, and set
$p_n(a)=m(a,n)/(2\binom an)$. Each colour has this containment probability;
the same asymptotic formula holds. So for $a=\kappa n^2+O(1)$ the count
forces $K_{a,b}\to K_{n,n}$ once $b$ exceeds
$(1+o(1))(n-1)2^ne^{1/(2\kappa)}$, and the cheapest host it certifies has
$(\kappa e^{1/(2\kappa)}+o(1))n^32^n$ edges, least at $\kappa=1/2$, which is
the $(e/2+o(1))s^2t2^s$ of CFW p. 4 at $s=t=n$.

**The local packing question (N1).** Is there a fixed $\kappa>0$ and
$\varepsilon>0$ with $B(\lceil\kappa n^2\rceil,n)\ge\varepsilon n2^n$ for all
large $n$, that is, an integral family reaching a fixed fraction of the
capacity? The lower half of Conjecture 5.1 implies a yes for every $\kappa$:
if $\hat R(K_{n,n})\ge cn^32^n$, then every $K_{\lceil\kappa n^2\rceil,b}$
with fewer than $cn^32^n$ edges has a good colouring, so
$B(\lceil\kappa n^2\rceil,n)\ge(c/\kappa-o(1))n2^n$. If instead
$B(\lceil\kappa n^2\rceil,n)=o(n2^n)$ along a sequence of $n$ for a single
$\kappa$, the conjecture fails, since
$K_{\lceil\kappa n^2\rceil,B+1}$ then has $o(n^32^n)$ edges along it. The
question is open here.

**The opposite extreme (N0).** If for one fixed $\kappa$ there is a constant
$C$ with $B(\lceil\kappa n^2\rceil,n)\le C2^n$ for all large $n$, then
$K_{\lceil\kappa n^2\rceil,\lfloor C2^n\rfloor+1}\to K_{n,n}$ and
$\hat R(K_{n,n})=O(n^22^n)$. With the Erdős--Rousseau lower bound the order
would be $n^22^n$: the problem would be settled, against Conjecture 5.1,
with no new Ramsey lower bound. The bounds established here are only
$c_\kappa2^n\le B(\lceil\kappa n^2\rceil,n)\le(1+o(1))(n-1)e^{1/(2\kappa)}2^n$:
the lower bound is the first moment computed below, and deleting one row from
each monochromatic copy, or using the local lemma, improves its constant but
not the order $2^n$. The growth of $B(\lceil\kappa n^2\rceil,n)/2^n$ decides
between (N0), bounded, and (N1), linear in $n$; intermediate growth is not
excluded.

The fractional relaxation reaches the unrounded bound
$2(n-1)\binom an/m(a,n)$ exactly when $m(a,n)>0$: weight the middle-sized
columns symmetrically, so every load equals the total weight times $p_n(a)$.
The integer capacity is its floor. For $b$ independent balanced columns
chosen by this distribution, the expected number of monochromatic $K_{n,n}$ is
$2\binom an\binom bnp_n(a)^n$. With $a=\kappa n^2$ and $b=C2^n$ it is at
most $2\bigl(e^2\kappa Ce^{-1/(2\kappa)+o(1)}\bigr)^n$, which tends to $0$
when $C<e^{1/(2\kappa)}/(e^2\kappa)$, so these hosts with order $n^22^n$
edges have good colourings. With $b=\varepsilon n2^n$ it is at least
$\bigl(\kappa\varepsilon ne^{-1/(2\kappa)+o(1)}\bigr)^n\to\infty$ for every
fixed $\varepsilon>0$. Each $n$-set has a binomial load of mean order $n$;
when the coefficient of that mean is strictly below $1$, its tail beyond
$n$ is $e^{-\Theta(n)}$, against $\binom an=e^{n\log n+O(n)}$ sets. For
larger coefficients that tail need not be small. The diverging expectation
defeats this first-moment criterion, not the existence of a packing.

## The balanced-host obstruction

**Proposition 3.** For every $n\ge1$,

$$
\hat R(K_{n,n})\le b(n)^2
\quad\text{and}\quad
\hat R(K_{n,n})\le\binom{r(K_{n,n})}2 .
$$

Hence if $f(n)\ge0$ and $\hat R(K_{n,n})\ge f(n)\,n^22^n$, then
$b(n)\ge\sqrt{f(n)}\,n2^{n/2}$ and
$r(K_{n,n})>\sqrt{2f(n)}\,n2^{n/2}$.

*Proof.* $K_{b(n),b(n)}$ and $K_{r(K_{n,n})}$ are Ramsey for $K_{n,n}$ by
definition, with $b(n)^2$ and $\binom{r(K_{n,n})}2<r(K_{n,n})^2/2$ edges.
$\square$

**Proposition 4 (the first-moment level).** For every $n\ge1$,
$b(n)>(n/e)2^{(n^2-1)/(2n)}$. For every fixed $C>0$ and
$N=\lceil Cn^{3/2}2^{n/2}\rceil$, the expected number of monochromatic
$K_{n,n}$ in a uniformly random colouring of $K_{N,N}$, and in the colouring
where each vertex of one side picks a uniformly random set of
$\lfloor N/2\rfloor$ red neighbours on the other, tends to infinity.

*Proof.* For $n=1$, the first claim follows from $b(1)=1$. For positive
integer $N$, there are $\binom Nn^2$ copies, and a uniform colouring makes each
monochromatic with probability $2^{1-n^2}$. Since $\binom Nn<(eN/n)^n$, the
expectation is below $1$ when $N\le(n/e)2^{(n^2-1)/(2n)}$, and a good colouring
exists. Taking the integer part of the threshold proves the first claim
for $n\ge2$. At $N=\lceil Cn^{3/2}2^{n/2}\rceil$, the inequality
$\binom Nn\ge(N/n)^n$ gives an expectation at least $2(C^2n)^n$. For all
sufficiently large $n$, in the side-balanced colouring a copy $S\times T$
is red with probability $p^n$, where
$p=\binom{\lfloor N/2\rfloor}n/\binom Nn\ge2^{-n}(1-(2n+1)/N)^n$, and blue
with at least that probability; so the expectation is at least
$2(C^2n)^n(1-n^2(2n+1)/N)$, which tends to infinity. $\square$

The literature sits at the same order. Souza
([arXiv:1910.13912v2](https://arxiv.org/abs/1910.13912v2), 2021, introduction,
read there) states the best bounds known to him as
$(1+o(1))(\sqrt2/e)\,n2^{n/2}\le b(n)\le(1+o(1))(\log_2n)2^{n+1}$, the lower
bound due to Hattingh and Henning (Utilitas Math. 53 (1998), 217--230; not
read here) and the upper bound to Conlon, and he remarks that the local lemma
improves the first-moment method only by a constant factor. Two 2026
preprints, cited in the section on attacks on (N0), claim $b(n)=O(2^n)$; an
upper bound does not change the comparison here. For
$r(K_{n,n})$, Chung and Graham's
[[../library/ramsey_theory/chung_graham_1975_multicolor_ramsey_numbers_complete_bipartite/theorem_4|Theorem 4]]
is a counting bound of order $n2^{n/2}$. No source read here gives
$b(n)/(n2^{n/2})\to\infty$ or $r(K_{n,n})/(n2^{n/2})\to\infty$; this is a
bounded reading, not a literature survey.

**Corollary 5 (scope).**

- (a) The lower half of Conjecture 5.1, $\hat R(K_{n,n})\ge cn^32^n$, implies
  $b(n)\ge\sqrt c\,n^{3/2}2^{n/2}$ and
  $r(K_{n,n})>\sqrt{2c}\,n^{3/2}2^{n/2}$: the Hattingh--Henning order
  improved by a factor of order $\sqrt n$.
- (b) Any lower bound with $\hat R(K_{n,n})/(n^22^n)\to\infty$ along a
  sequence of $n$ gives $b(n)/(n2^{n/2})\to\infty$ and
  $r(K_{n,n})/(n2^{n/2})\to\infty$ along it.
- (c) Every determination $\hat R(K_{n,n})=\Theta(g(n))$ either has
  $g(n)=O(n^22^n)$, and then its upper half exhibits Ramsey hosts with
  $O(n^22^n)$ edges, or has $g(n)/(n^22^n)$ unbounded, and then its lower
  half proves (b) along a sequence.

So the problem cannot be settled at the conjectured order without a lower
bound for bipartite and ordinary Ramsey numbers of $K_{n,n}$ beyond the first
moment by a factor of order $\sqrt n$. The balanced host $K_{N,N}$ with
$N=\lfloor\sqrt c\,n^{3/2}2^{n/2}\rfloor$ has at most $cn^32^n$ edges; it
is complete bipartite, but its sides are far larger than $n^2$. Packings on
hosts with a side of order $n^2$ alone supply no colouring of this host;
an additional implication is needed. By Proposition 4 the
uniform and side-balanced colourings have unbounded first moment there.
The latter distribution illustrates hypergeometric sampling but is not the
full interval colouring of CFW, so Proposition 4 alone is not a barrier to
all such colourings. In CFW's proof
of Theorem 2.4 the hypergeometric choices are made only inside the dyadic
intervals of the first $2^{L+1}$ vertices of the degree order, with
$2^L=s^2t/(50(t-s))$, with the paper's rounding conventions; the quantity is
undefined at $t=s$. Theorem 2.4 assumes $t\ge s+2$, and its specialization
at $s=n-2$, followed by containment in $K_{n,n}$, gives only
$\Omega(n^22^n)$ on the diagonal. This first-moment limitation at balanced
hosts is also discussed in the remark after Erdős--Rousseau's Theorem 1;
the necessary implication in Proposition 3 is elementary, not asserted to
be a new Ramsey bound.

What the conjecture needs therefore splits into necessary local statements,
none of which is proved:

- (N1) near-capacity packings with a side of order $n^2$, as above;
- (N2) for some $c'>0$ and all large $n$, colourings of $K_{N,N}$ and of
  $K_N$ with $N=\lceil c'n^{3/2}2^{n/2}\rceil$ without a monochromatic
  $K_{n,n}$.

In the packing form of Lemma 1, (N2) for $K_{N,N}$ asks for
$B(N,n)\ge N$: $N$ subsets of an $N$-set, every $n$-set inside at most $n-1$
of them and disjoint from at most $n-1$. This is the problem of (N1) in the
opposite regime. The mean load $Np_n(N)\approx N2^{-n}$ tends to $0$, far
below the capacity, and the difficulty is the number of $n$-sets, not the
capacity. No implication between (N1) and (N2) is known here, and together
they still leave every other host. A refutation of (N1) for one $\kappa$
would give $\hat R(K_{n,n})=o(n^32^n)$ along a sequence. (N2) fails only if
$b(n)$ or $r(K_{n,n})$ is $o(n^{3/2}2^{n/2})$ along a sequence,
exponentially below the known upper bounds. CFW recall in their Section 3.1
that some have conjectured $r(k)\ge(\sqrt2+\varepsilon)^k$ for the classical
diagonal Ramsey numbers; an
exponential gain of that kind for both $b(n)$ and $r(K_{n,n})$ would give
(N2) with room to spare. A gain for $r(K_{n,n})$ alone suffices too, since
$r(K_{n,n})\le2b(n)$: $K_{2b(n)}$ contains the Ramsey host
$K_{b(n),b(n)}$. No implication from the classical diagonal conjecture to
these bipartite targets is asserted. The obstruction is to proving (N2), not
evidence against it.

## What an independence heuristic suggests

This section is a heuristic, not a bound. Let $E$ be the expected number of
monochromatic copies under independent balanced columns, and let $M$ be the
number of colourings in that sample space. For even $a$,
$M=\binom a{a/2}^b$, so $\log M\sim ab\log2$ as $a\to\infty$. Pretending
that the forbidden-copy events behave independently suggests
$M e^{-E}$ good colourings. Its threshold is $E\approx\log M$, not $E=1$;
there is no justification here for that independence assumption.

For $K_{a,b}$ and a target $K_{s,t}$ whose $s$-side is among the $a$ vertices,
the expectation for this orientation is
$E=2\binom as\binom btp_s(a)^t$. In the regime $s\to\infty$, $t>s$ and
$a\ge c s^2$, the leading factorial and hypergeometric approximations give

$$
ab\approx
\left(\tfrac{\log2}{2}s!t!2^{st}\right)^{1/(t-1)}
a^{(t-s)/(t-1)}
\exp\left(\frac{s^2t}{2a(t-1)}\right)
$$

at the guessed threshold. This expression is minimized at
$a=s^2t/(2(t-s))$ and has order $s^{2-s/t}t2^s$ there. This is the scale of
CFW's Theorem 1.1, whose proof uses dyadic intervals of size about
$s^2t/(t-s)$. It is a comparison of scales, not an alternative proof of that
theorem: arbitrary hosts and, where present, the other orientation of
$K_{s,t}$ still require control. For $t\ge Cs\log s$, CFW's Corollary 1.2
rigorously matches the counting upper bound up to constants.

On the diagonal the same formal calculation gives

$$
ab\approx\left(\frac2{e^2}+o(1)\right)n^22^n
\exp\left(\frac{n^2}{2a}\right).
$$

For $a=\kappa n^2$ this suggests the smaller order $n^22^n$, and for
$a=b=N$ it suggests $N=(\sqrt2/e+o(1))n2^{n/2}$, the constant in the
Hattingh--Henning lower bound. These are only predictions of the model.
Its predicted count of good balanced colourings is unsupported, and it does
not count all colourings. A proof of the conjectured order $n^32^n$ would
require structured colourings that this approximation misses, while a proof
of order $n^22^n$ would require actual Ramsey hosts at that scale, for example
(N0).

## The arbitrary-host step

CFW colour an arbitrary host by one global rule: order the vertices by
degree; inside the first $2^{L+1}$ vertices, cut into dyadic intervals, each
later vertex picks a uniformly random half of every earlier interval as its
possible red neighbours, and edges inherit these choices; all other edges are
coloured uniformly. Compatibility on overlaps is automatic. A reduction to
complete bipartite pieces coloured separately is weaker in an essential way:
compatible colours on shared edges do not prevent a monochromatic copy whose
edges lie in several pieces, so the step must control such copies or impose a
global invariant. Corollary 5 shows that no form of this step avoids the
balanced obstruction, since it appears already for the single host $K_{N,N}$,
and the complete host $K_N$ adds the same requirement on $r(K_{n,n})$.

## Constructions tried for near-capacity packings

These attempts at (N1) fail at the stated scope. Only the affine item is a
nonexistence theorem, for the class and parameters of Proposition 7.

- *Independent columns, and the local lemma.* The first moment reaches
  $b$ of order $2^n$ only, as computed above. A forbidden-copy event has
  probability $2p_n(a)^n$ and depends only on its $n$ columns. Its number
  of dependent events, including itself, is at most
  $n\binom an\binom{b-1}{n-1}$. Applying the symmetric local lemma with
  this bound replaces the first-moment expression by at most $en^2/b$
  times that expression. At $a=\kappa n^2+O(1)$ the resulting sufficient
  criterion still reaches only $b=C_\kappa2^n$, for a constant
  $C_\kappa$. This diagnoses this dependency bound, not every possible
  use of the local lemma.
- *Linear and affine codes.* Take the rows to be a coset $c+C$ of a binary
  code $C\subseteq\mathbb F_2^a$ of dimension $k$, so $b=2^k$. If the
  generator columns indexed by $S$ have rank $\rho_S$, each pattern on $S$
  occurs $0$ or $2^{k-\rho_S}$ times. If a constant pattern occurs on
  $S$, a good family therefore needs $2^{k-\rho_S}\le n-1$; no such
  restriction follows when neither constant pattern occurs. Proposition 7
  shows that an overload occurs for every code once $a\ge8n^2$ and
  $k\ge\lceil\log_2n\rceil+1$:
  some $n$ generator columns indexed inside one colour class of a fixed row
  lie in a subspace of codimension $\lceil\log_2n\rceil$, and then at least
  $n$ rows agree with that row on them. This excludes the affine class at
  those parameters; nonlinear codes are not covered.
- *Exact designs.* A family in which every $n$-set has the same red load,
  with nonzero load and all rows of one size $k\approx a/2$, is an
  $n$-design. Put $h=\lfloor n/2\rfloor$. Its incidence matrix between
  rows and $h$-subsets has a Gram matrix proportional to that for all
  $k$-subsets: each entry counts a union of at most $2h\le n$ points.
  The full incidence matrix has column rank $\binom ah$ when
  $h\le k\le a-h$, so the design needs at least $\binom ah$ rows, far
  above the capacity when $a=\kappa n^2$. Repeated rows do not change
  this rank bound. Upper bounds on loads, as in (N1), give no proportional
  Gram matrix, so this argument does not exclude the required packings.
- *Random greedy addition.* At mean load of order $n$ the $n$-sets already
  at load $n-1$ number $e^{n\log n-O(n)}$, so a new column must properly
  2-colour that hypergraph of $n$-sets on $\kappa n^2$ points, far beyond the
  edge counts that guarantee such a colouring. This is a heuristic count, not
  a proof.

For completeness, the full-incidence rank fact follows by induction on $h$.
If coefficients $x_S$ sum to zero over the $h$-subsets of every $k$-set,
subtract the equations for $U\cup\{i\}$ and $U\cup\{j\}$. Induction on
the remaining $a-2$ points, with parameters $(k-1,h-1)$, gives
$x_{A\cup\{i\}}=x_{A\cup\{j\}}$ for every $(h-1)$-set $A$ disjoint
from $i,j$. Thus all $x_S$ are equal, and a $k$-set equation forces them
to be zero. The base $h=0$ is immediate.

An attempted two-stage count for (N0) also supplies no improvement at the
parameter choices tested. First seek $n-j$ common red columns and $L$
rows; then seek $n$ of those rows with $j$ further common red columns.
Using the balanced averaging estimates at both stages suggests sufficient
sizes of order $j2^n$ columns, $L$ of order $n^2$, and therefore
$n^22^{n-j}$ initial rows. For $1\le j\le n$ their product is of order
$jn^24^n2^{-j}\ge n^32^n$. This parameter calculation does not rule out
a sharper two-stage argument or prove a necessary size for such hosts.

## Attacks on (N0)

(N0) asks for a reason why loads cannot all stay below $n$ when the mean load
is a large constant. The required precision is high. For $b=C2^n$
independent balanced columns with $C$ large, the first-moment estimate puts
the largest load near $n\bigl(1+\log(e^2\kappa Ce^{-1/(2\kappa)})/\log n\bigr)$,
only a factor $1+O(1/\log n)$ above $n$. This is a heuristic estimate,
not a theorem about the maximum. It suggests testing candidate overload
arguments on random-like families as well as structured ones.

The same tightness holds for every host, not only for this one. By
[[../library/ramsey_theory/erdos_rousseau_1993_size_ramsey_number_complete_bipartite/lemma_1|Erdős and Rousseau's Lemma 1]],
at its library standing, a graph with $q=Cn^22^n$ edges has at most
$(2eq/n)(2e^2q/n^2)^n$ copies of $K_{n,n}$. Under a uniform colouring the
expected number of monochromatic copies is therefore at most
$4eCn(4e^2C)^n$, which is $e^{O(n)}$. So the upper half of a
$\Theta(n^22^n)$ answer must show that some host is Ramsey although a
uniform colouring of it has only exponentially many monochromatic copies in
expectation, whereas a balanced host with $c2^n$ vertices in each part, as in
the density theorems below, has $2^{(1-o(1))n^2}$ of them. The lower half of
Conjecture 5.1 faces the mirror problem: hosts with $cn^32^n$ edges can have
about $e^{n\log n}$ expected monochromatic copies, so it needs colourings far
better than uniform ones.

**The one-colour form (N0$'$).** There are $\kappa,C>0$ such that, for all
sufficiently large $n$ and $a=\lceil\kappa n^2\rceil$, every multiset of more
than $C2^n$ subsets of $[a]$, each of size at least $a/2$, has an $n$-set
contained in at least $n$ of its members.

**Lemma 6.** If (N0$'$) holds with constants $\kappa,C$, then (N0) holds with
$\kappa$ and $2C$.

*Proof.* Take a colouring of $K_{a,b}$ with $b>2C2^n$. Each column $y$ has a
red or a blue neighbourhood with at least $a/2$ points, so for one colour more
than $C2^n$ columns have a neighbourhood of that colour with at least $a/2$
points. By (N0$'$) some $n$-set lies in at least $n$ of those
neighbourhoods, which is a monochromatic $K_{n,n}$. $\square$

The converse is not claimed: (N0$'$) bounds families whose complements may
be heavily loaded. It is the unbalanced density form of the problem: a
bipartite graph with parts of sizes $\lceil\kappa n^2\rceil$ and more than
$C2^n$, in which every vertex of the larger part has degree at least half
the smaller part, contains $K_{n,n}$. The Kővári--Sós--Turán count (Lemma 2
for one colour) proves this only when the larger part has order $n2^n$. That
count is Lemma 1 of D. Conlon, *A new upper bound for the bipartite Ramsey
problem*, J. Graph Theory 58 (2008), 351--356 (the author's preprint was read
at statement and proof depth). He remarks there that a random construction
with $r^2$ vertices on the small side has density $p$, no $K_{r,s}$, and a
large side of order $p^{-r}s/(e(er)^{r/s})$; at $r=s=n$ and $p=\frac12$ that
is order $2^n$. Average density alone is weaker than the column-degree
condition in (N0$'$). The balanced-column first-moment argument above,
using columns of size $\lceil a/2\rceil$, gives the same order $2^n$ under
that degree condition, leaving a factor-$n$ gap for (N0$'$) itself.

Two 2026 preprints claim that this kind of count can be beaten on balanced
hosts. D. Mubayi, *Sharper Zarankiewicz and diagonal bipartite Ramsey
bounds* ([arXiv:2609.32937v1](https://arxiv.org/abs/2609.32937v1), 2026),
claims in Theorem 2.1 that a bipartite graph with $N$ vertices in each part
and at least $N^2/2$ edges contains $K_{t,t}$ once $N\ge2^{t+81}$, so
$b(t)=O(2^t)$. Y. Person, *Another proof that the two color bipartite
Ramsey number is $O(2^t)$*
([arXiv:2609.40288v1](https://arxiv.org/abs/2609.40288v1), 2026),
claims $b(t)\le128\cdot2^t$ by a related argument whose density form needs
both parts of size at least $128p^{-t}$ for $0<p\le1/2$ (Theorem 1.1).
Both were read at statement and
outline depth; their proofs are not checked here, and neither is used as a
premise. They do not apply to $K_{\lceil\kappa n^2\rceil,\lfloor C2^n\rfloor}$.
Mubayi's process repeatedly passes to the common neighbourhoods of a chosen
edge. At density about $1/2$, the heuristic loss is a halving of both parts
at each step. Here the smaller part has
only $\kappa n^2$ vertices, so after about $\log_2(\kappa n)$ steps fewer than
$n$ of its vertices remain. Mubayi's potential, essentially the harmonic mean
of the part sizes times the density to the power $t$, starts near
$2\kappa n^22^{-n}$ here, far below the constant threshold his argument
needs. Person instead alternates spines between the two classes and reduces
the remaining target sizes logarithmically (Section 3). His density theorem
still requires both initial classes to have exponential size. These facts
explain why the stated theorems do not supply (N0$'$); they do not rule out
an adaptation. Their claimed improvement over the balanced counting bound
is a factor of order $t$, the factor the direct route seeks in its different
parameter regime.

**Proposition 7 (affine colourings).** Let $n\ge2$, $c=\lceil\log_2n\rceil$,
$k\ge c+1$ and $a\ge8n^2$. Take vectors $g_x\in\mathbb F_2^k$ and bits
$c_x\in\mathbb F_2$ for $x\in[a]$, and colour the edge between $x$ and
$u\in\mathbb F_2^k$ red exactly when $\langle u,g_x\rangle+c_x=1$. This
colouring of $K_{a,2^k}$ contains a monochromatic $K_{n,n}$.

*Proof.* Fix $u_0\in\mathbb F_2^k$ and let $Z$ be a colour class of its
neighbourhood with $|Z|\ge a/2$; say it is red. Choose a uniformly random
subspace $V\le\mathbb F_2^k$ of dimension $k-c$. For $x\in Z$, the
probability that $g_x\in V$ is $1$ when $g_x=0$ and
$(2^{k-c}-1)/(2^k-1)\ge2^{-c-1}$ otherwise, the inequality because
$2^k\ge2^{c+1}$. Since $2^{c+1}<4n$, the expected number of $x\in Z$ with
$g_x\in V$ is greater than $|Z|/(4n)\ge n$. Fix such a $V$, and let $S$ be
$n$ of these points. Let $V^\perp$ be the set of $w$ with
$\langle w,v\rangle=0$ for all $v\in V$, a subspace of dimension $c$. For
$u\in u_0+V^\perp$ and $x\in S$ we have
$\langle u,g_x\rangle=\langle u_0,g_x\rangle$, so $u$ is joined in red to
all of $S$, as $u_0$ is. Since $2^c\ge n$, the set $S$ and $n$ vertices of
$u_0+V^\perp$ span a red $K_{n,n}$. $\square$

The colourings in Proposition 7 are exactly those whose neighbourhood
multiset is the image of an affine map $\mathbb F_2^k\to\mathbb F_2^{a}$, that
is, a coset of a binary linear code with every codeword repeated equally
often. So with a side of at least $8n^2$ such colourings fail already at
$b=2^{c+1}<4n$ columns, far below the random order $2^n$. Such cosets cannot
witness (N1) at $\kappa\ge8$, and cannot refute (N0), whose constant
$\kappa$ is existential. The proof is a pigeonhole on a
low-dimensional space of column functions; a general family has no such
space, so the argument does not extend. For colourings by quadratic
polynomials $P_x$ in $u$, the analogous step needs $n$ points $x$ whose
polynomials are all constant on one affine subspace of dimension $\log_2n$.
That is a condition of codimension about $(\log_2n)^2/2$ on each $P_x$, so
the pigeonhole needs far more than $\kappa n^2$ points. That class is not
excluded.

There is also a direct counterexample to extending this particular
certificate to all quadratic families. Fix $\kappa>0$, put
$d=\lceil\log_2n\rceil$,
take $k=n+O(\log n)$, and choose the $a=\lceil\kappa n^2\rceil$
polynomials independently and uniformly from the Boolean polynomials of
degree at most two in $k$ variables. On a fixed affine $d$-subspace their
restrictions are uniform among $2^{D_d}$ polynomials, where
$D_d=1+d+\binom d2$. Surjectivity of restriction follows by extending
affine coordinates on that subspace to coordinates on the whole space.
There are at most $2^{k(d+1)}$ affine $d$-subspaces. The union bound for
some $n$ of the polynomials all being the same constant on one of them is

$$
2^{k(d+1)+1}\binom an\,2^{-nD_d}
=2^{-\frac12n(\log_2n)^2+O_\kappa(n\log n)}=o(1).
$$

Thus some such quadratic families have no monochromatic rectangle with
$n$ points and an affine subspace of at least $n$ columns. A larger affine
subspace would contain one of dimension $d$. This does not say that the
colouring has no monochromatic $K_{n,n}$: its $n$ columns may be an
arbitrary set, and the calculation leaves those sets uncontrolled. The
quadratic construction question remains open here; an affine-subspace
witness alone cannot exclude the whole class.

**Lemma 8 (marginal avoidance probabilities).** Fix $\kappa,C>0$, let
$a=\lceil\kappa n^2\rceil$ and $b=\lfloor C2^n\rfloor$, and colour $K_{a,b}$
uniformly at random. There is $c_1=c_1(\kappa,C)$ such that, for all large
$n$, the probability that there is no red $K_{n,n}$ is at least
$2^{-c_12^n}$, and the same holds for blue.

*Proof.* Write $N=ab$ and colour each edge red independently with
probability $p=\min\{\tfrac12,(n^2/(2e^2N))^{1/n}\}$. The expected number of
red $K_{n,n}$ is at most $\binom an\binom bnp^{n^2}\le(e^2Np^n/n^2)^n\le2^{-n}$,
so the event $E$ of no red $K_{n,n}$ has probability at least $1-2^{-n}$.
By Chebyshev's inequality at most $1/4$ of this measure has fewer than
$m_0=pN-\sqrt N$ red edges, so $E$ together with at least $m_0$ red edges
has probability at least $1/2$. For a colouring $\omega$ with $m$ red edges,
the ratio of its uniform probability $2^{-N}$ to its probability under the
biased measure is $(2p)^{-m}(2(1-p))^{-(N-m)}$, which is nondecreasing in $m$
since $p\le1/2$. At $m\ge m_0$ it is at least
$2^{-N(1-H(p))}(p/(1-p))^{\sqrt N}$, where $H$ is the binary entropy, so the
uniform probability of $E$ is at least half of that. Since $N$ has order
$n^22^n$, $\frac12-p=O(1/n)$, so $N(1-H(p))=O(N/n^2)=O(2^n)$ and
$(p/(1-p))^{\sqrt N}\ge2^{-O(\sqrt N/n)}$. Blue is symmetric. $\square$

No red copy is a decreasing event in the red edge set and no blue copy an
increasing one, so Harris's inequality bounds the number of good colourings
by $2^N$ times the product of the two probabilities. By Lemma 8 that product
bound is at least $2^{N-2c_12^n}>1$, because $N$ has order $n^22^n$. Even
exact values of the two marginal probabilities therefore cannot make this
particular bound certify zero good colourings. This does not exclude a
one-colour argument with further hypotheses: (N0$'$), for example, imposes
a lower bound on every column degree. Nor does it exclude a joint estimate
stronger than the Harris product.

**Homomorphism counts.** Sidorenko's inequality, which holds for $K_{n,n}$,
gives at least $2(ab2^{-n})^n$ homomorphisms of $K_{n,n}$ into the two colour
classes together. A homomorphism whose $n$ column images are not distinct is
not a copy, and the hypothesis of (N0) restricts only tuples of $n$ distinct
columns. For $b=C2^n$ independent balanced columns, tuples with about
$n/\log n$ distinct columns already give more homomorphisms than this lower
bound by a factor larger than any exponential in $n$ (an estimate through
the moments $\sum_jS(n,j)C^j$ of a Poisson variable, with $S(n,j)$ the
Stirling numbers). This comparison leaves no deduction of an injective
copy from the raw homomorphism lower bound; additional control of the
degenerate maps is needed.

**Greedy choices.** Choosing points one at a time, each with the largest red
degree into the columns red on all points chosen so far, roughly halves the
surviving columns at each step. For independent balanced columns the best
choices improve on halving only by a total factor $e^{O(\sqrt{\log n})}$
while many columns survive. Once $m$ columns remain, they have about
$a2^{-m}$ common red points, so the process can end with $n$ points and
about $\log_2(\kappa n)$ common columns: loads of order $\log n$ are found
greedily, but not loads of order $n$. In such families the overloaded
$n$-sets come only from the count over all $\binom an$ sets. This is an
estimate for one family model. It supplies no greedy proof of (N0), and
does not exclude a different greedy rule or potential argument.

### Deleting unusually large common neighbourhoods

The next reduction uses both colours and the distinct column indices. It
does not change the asymptotic size of the small part, and repeated
neighbourhoods are allowed.

**Lemma 9.** Fix $\delta,C>0$, put $c=2+\delta$, and choose an integer
$\ell\ge\max\{1,4/\delta\}$. For all sufficiently large $n$, a
colouring of $K_{a,b}$ with $b\ge C2^n$ and no monochromatic $K_{n,n}$
has a set $W$ of at most $2(\ell-1)\lceil cn\rceil$ points in its
$a$-vertex part such that every $n-1$ columns have fewer than
$\lceil cn\rceil$ common red neighbours outside $W$, and fewer than
$\lceil cn\rceil$ common blue neighbours outside $W$. The threshold
for $n$ depends only on $\delta,C$; there is no restriction on $a$.

*Proof.* Write $u=\lceil cn\rceil$. Suppose that there are $\ell$
pairwise disjoint $u$-sets $U_1,\ldots,U_\ell$, each joined in red to
a set $T_i$ of $n-1$ distinct columns. The $T_i$ may overlap. Exclude
their union, leaving at least $M=b-\ell(n-1)$ columns. Each remaining
column has at most $n-1$ red neighbours in every $U_i$: $n$ such
neighbours together with $T_i$ and that column would form a red
$K_{n,n}$. Consequently each of these columns has at least
$k=\ell(u-n+1)$ blue neighbours in $U=\bigcup_iU_i$, where
$|U|=m=\ell u$.

Counting blue stars with $n$ leaves in $U$, as in Lemma 2, gives

$$
M\binom{k}{n}\le(n-1)\binom{m}{n}.
$$

For $0\le i<n$ and all sufficiently large $n$,

$$
\frac{k-i}{m-i}\ge\frac{k-n+1}{m}
=1-\frac{(\ell+1)(n-1)}{\ell u}
\ge1-\frac{1+1/\ell}{c}
\ge\frac12+\frac{\delta}{4c}=: \beta>\frac12.
$$

It follows that $M\beta^n\le n-1$. But $M\ge(C/2)2^n$ for all
large $n$, so $M\beta^n\ge(C/2)(2\beta)^n>n-1$, a contradiction.
Thus fewer than $\ell$ disjoint red $u$-sets of this kind exist.

Take a maximal disjoint collection and delete its union, at most
$(\ell-1)u$ points. Any $u$ common red neighbours of $n-1$ columns
among the remaining points would extend that collection. Repeat the same
argument for blue on the remaining points and delete at most another
$(\ell-1)u$ points. Deleting points preserves the red conclusion and
the absence of a monochromatic $K_{n,n}$. This proves the lemma.
$\square$

**How it composes with (N0).** Fix any $\delta>0$. It is enough to prove
the overload assertion for families that already have the two additional
common-neighbourhood bounds of Lemma 9. Indeed, suppose this restricted
assertion holds at $a=\lceil\kappa n^2\rceil$ with threshold
$C_0 2^n$. Start a putative counterexample at
$a=\lceil2\kappa n^2\rceil$, retain exactly
$b=\lfloor C_0 2^n\rfloor+1$ columns, and apply Lemma 9 with $C=C_0$.
For all large $n$ at least $\lceil\kappa n^2\rceil$ points remain.
Restrict to that many; the two extra bounds and both original load bounds
survive. This contradicts the restricted assertion. The reverse
implication is immediate. Thus, allowing a change of $\kappa$, the
restriction is equivalent to (N0), not a proved substitute for its missing
overload step.

**Where the attempted continuation fails.** The deletion proof obtains a
blue density above $1/2$ from many disjoint red common neighbourhoods
larger than $2n$. Once those neighbourhoods have size at most roughly
$2n$, its forced blue density is no longer above $1/2$. This is a genuine
limit of that local inference. On $2n-2$ points one may take $n-1$ all-red
columns and arbitrarily many further columns, each with exactly $n-1$
red and $n-1$ blue entries. No $n$-set has red or blue load $n$, yet the
first $n-1$ columns have $2n-2$ common red neighbours. This example has
only $O(n)$ points; it does not refute (N0) or the possibility of a
stronger deletion theorem using global information.

In particular, the attempted next implication, from the pruned
common-neighbourhood bounds to $b=O(2^n)$, is unproved. Applying the
capacity count on the remaining points still gives order $n2^n$.
Applying it separately to small neighbourhoods does not control $n$-sets
spread over several of them. A proof must supply that global step or a
different mechanism; it cannot treat the deletion lemma itself as the
integral overload.

## Finite diagnostics at n = 2 and n = 3

The [evidence](evidence/_index.md) checks every witness colouring below by
direct enumeration and recomputes every counting bound; solver verdicts and
cited theorems are marked as such.

**$n=2$, every host (exhaustive).** $\hat R(K_{2,2})=15$, attained by $K_6$.
A vertex of degree at most $2$ can be removed from a host without changing
whether it is Ramsey for $K_{2,2}=C_4$ (colour its two edges differently), so
a smallest Ramsey host has minimum degree at least $3$, hence at most $9$
vertices when it has at most $14$ edges. Every graph with minimum degree at
least $3$ and at most $14$ edges (313 isomorphism classes on $4$ to $9$
vertices) has a good colouring, and $K_6\to C_4$ by enumeration of all $2^{15}$
colourings.

**$n=2$, complete bipartite hosts (exhaustive).** $B(2,2)=\infty$,
$B(3,2)=B(4,2)=6$ (the capacity), and $B(a,2)\le4$ for $a\ge5$ because
$K_{5,5}\to K_{2,2}$, that is $b(2)=5$. The cheapest complete bipartite
Ramsey host is $K_{3,7}$ with $21$ edges.

**$n=3$, complete bipartite hosts (exhaustive over the class).**

| $a$ | $\operatorname{cap}(a,3)$ | $B(a,3)$ | standing |
| --- | --- | --- | --- |
| 3, 4 | none | $\infty$ | general colouring |
| 5, 6 | 40 | 40 | witness at 40; capacity |
| 7, 8 | 28 | 28 | witness at 28; capacity |
| 9 | 24 | 22 | witness at 22; 23 refuted by the solver only |
| 10 to 14 | 24, 22, 22, 20, 20 | at least 20, 18, 16, 15, 14 | witnesses |

The cheapest complete bipartite Ramsey host for $K_{3,3}$ is $K_{7,29}$ with
$203$ edges: it is Ramsey by Lemma 2, and every $K_{a,b}$ with $ab\le202$ has
a witness colouring (by symmetry $a\le b$, so $a\le14$). The counting
capacity is reached for $5\le a\le8$; the solver verdict indicates a
deficit at $a=9$. Neither observation predicts the behaviour for large $n$.

**$n=3$, complete hosts.** $K_{17}$ has a colouring without a monochromatic
$K_{3,3}$ (a checked witness), so no host on at most $17$ vertices is
Ramsey. $K_{18}\to K_{3,3}$ is the theorem $r(K_{3,3})=18$ of Harborth and
Mengersen (in Graph Theory, Combinatorics, and Applications, Vol. 2, Wiley,
1991, 639--644; not read here, cited from Wu, Magnant, Salehi Nowbandegani and
Xia, [arXiv:1710.10455v1](https://arxiv.org/abs/1710.10455v1), Theorem 6). The
SAT search returned no verdict for $K_{18}$, and no checked unsatisfiability
certificate is retained. Given that theorem, $\hat R(K_{3,3})\le153<203$.

**$n=4$, translation symmetry and its scope.** Translation-invariant
families on $\mathbb F_2^4$ need not have loads divisible by $4$. In fact,
the $30$ affine hyperplanes give a good colouring of $K_{16,30}$. Write
$R_{u,c}=\{x\in\mathbb F_2^4:u\mathbin{\cdot}x=c\}$ for
$u\ne0$, $c\in\mathbb F_2$. A $4$-set has affine dimension $d\ge2$;
exactly $2^{4-d}-1\le3$ hyperplanes contain it. Complements are hyperplanes
too, so the blue load has the same bound. Translation permutes these $30$
sets. The evidence constructs them and checks every load and translation.
This proves $B(16,4)\ge30$, below the capacity $78$; it makes no assertion
of optimality.

The invalid obstruction to all translation-invariant families argues that
the four translations preserving an affine plane force its load to be
divisible by $4$. That needs a free action on the rows containing the plane.
Hyperplanes have nontrivial stabilizers, and a plane's load in this example
is $3$, not a multiple of $4$.

No nonempty good family exists in the narrower model used by the translation
search: take all $16$ translates of each base row as a multiset, retaining
repeats.
For a fixed plane $P$, its four preserving translations act freely on the
translation indices, so each base row contributes a multiple of $4$ to
$P$'s load. Every base row and its complement would therefore have to contain
no plane. A plane-free subset has all unordered pair sums distinct, so it
has at most $6$ points, since $\binom72>15$; two such sets cannot partition
$16$ points. This also excludes a row with trivial stabilizer in any good
translation-invariant family, since its orbit has $16$ distinct members.
It does not exclude shorter orbits with their members included once, as in
the hyperplane construction. The distinction between an orbit and a multiset
of all indexed translates is essential to the search's scope.

No near-capacity value of $B(a,4)$ was decided. The bounded cyclic-orbit
searches on $13$ columns at $65$ rows and $17$ columns at $51$ or $68$ rows,
and the unrestricted instance on $16$ columns at $40$ rows, were undecided.
There is no nonexistence conclusion from those searches.

So at $n=2$ and $n=3$ a complete host beats every complete bipartite host.
The comparison does not bear on the order: $\binom{r(K_{n,n})}2$ is $15$ and
$153$ against $n^32^n=32$ and $216$, and whether complete hosts stay
competitive as $n$ grows is exactly the size of $r(K_{n,n})$ relative to
$n^{3/2}2^{n/2}$ in Proposition 3. The choice to compare these two classes
at $n=3$ is heuristic; no exhaustive search of arbitrary hosts is supplied.

## Consequential gaps and next tests

- (N0), or its one-colour form (N0$'$), is the only gap of the direct route.
  A bounded ratio $B(\lceil\kappa n^2\rceil,n)/2^n$ for one $\kappa$ settles
  the problem at order $n^22^n$; a ratio of order $n$ for every fixed
  $\kappa$ is necessary for Conjecture 5.1; a ratio that is $o(n)$ along a
  sequence for one $\kappa$ refutes the conjecture. Unknown. The
  independence and random greedy heuristics on this page suggest a bounded
  ratio, that is, (N0); they are predictions, not proof steps. The affine
  result excludes only its stated class. The marginal-probability product
  does not suffice (Lemma 8). The estimate for the largest load in random
  families places it within a factor $1+O(1/\log n)$ of $n$, a useful test
  for proposed quantitative arguments. The homomorphism and greedy
  calculations recorded here supply no overload theorem. Neither cited
  density theorem covers the required unbalanced host.
- On the direct route, Lemma 9 allows one to impose its common-neighbourhood
  bounds after deleting only $O(n)$ points. The next discriminating step is
  a global integer inequality for these remaining families that forces a
  load of $n$ at $b>C2^n$. A deduction from one small neighbourhood alone
  has the explicit $2n-2$-point example above. An argument for several
  neighbourhoods must control $n$-sets spread over them; no such argument
  is supplied here.
- On the construction side: colourings by quadratic
  polynomials over $\mathbb F_2$, the first algebraic class that the pigeonhole
  of Proposition 7 does not exclude. Decide whether such colourings can keep
  every load below $n$ with $b/2^n\to\infty$. Such colourings for every
  $\kappa$ would refute (N0) for complete bipartite hosts with a side of
  order $n^2$; an argument that they cannot would be the first structured
  class beyond the affine one, and its mechanism is a candidate for (N0).
  The calculation after Proposition 7 rules out insisting that the column
  witness be an affine subspace; it does not exclude other witnesses.
- Another possible test is the random greedy process that adds balanced
  columns one at a time, each uniform among those keeping every load below
  $n$. In the
  triangle-free analogue for $R(3,k)$ such a process beats the first-moment
  order. For a fixed $\kappa$, an unbounded ratio $b/2^n$ would exclude
  (N0) at that $\kappa$, but intermediate growth would still fall short of
  (N1). Refuting (N0) itself requires unbounded ratios for every fixed
  $\kappa$. A random-like heuristic predicts that the process stops
  near twice the first-moment threshold, when the saturated $n$-sets, about
  $(e^2\kappa\lambda)^n$ of each colour at mean load $\lambda$, stop admitting
  a balanced column that contains none of the red ones and meets every blue
  one. The test is whether the process corrects itself
  beyond that prediction, as the triangle-free process does. The heuristic
  count for random greedy addition in the list of constructions concerns
  mean load of order $n$ and does not decide this.
  Finite values of $B(a,4)$ and $B(a,5)$ near $a=n^2$ matter only as checks
  on such mechanisms.
- (N2), for the lower-bound route: colourings of $K_{N,N}$ and $K_N$ with
  $N$ of order $n^{3/2}2^{n/2}$ without a monochromatic $K_{n,n}$, beating
  the Hattingh--Henning order by a factor of order $\sqrt n$. Unknown here;
  the random-colouring bounds checked here have only the first-moment order.
  Any proof of the lower half of Conjecture 5.1 contains a proof of (N2), so
  every route to that half must supply it. It is a missing input, not a
  proved impossibility of packing routes.
- The arbitrary-host step of the lower-bound route, which must control copies
  spread over several pieces, and (N1).

The direct route needs only (N0); nothing else on this page is a premise of
it. The lower-bound route is reopened by colourings of $K_{N,N}$ and $K_N$ of
the strength in (N2), beyond the first moment, for instance through a
reduction of the balanced case to the unbalanced one, which this page does
not have. Even then it needs (N1) and a mechanism for arbitrary hosts, which
it also lacks.

## Current review

Unreviewed. Lemmas 1, 2, 6, 8 and 9, Propositions 3, 4 and 7, Corollary 5,
the quadratic affine-subspace calculation and the diagnostics are
author-recorded; no independent review covers them. The
statements marked as estimates in the section on attacks on (N0) are not
proofs, and the preprints cited there are outside claims whose proofs are not
checked. The solver verdict at $(a,b)=(9,23)$ and the cited theorem for
$K_{18}$ are not checked by the evidence.
