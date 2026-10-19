---
name: theory/additive_bases/L125_random_singer_lift_residual/_proof
title: Proof of the residual bound for random Singer lifts
desc: |
  Each target has a blocking-event dependency graph of maximum degree four.
  An elementary local-lemma induction bounds its probability of remaining
  unblocked below, and a bounded-difference variance estimate gives a
  linear residual with probability tending to one.
tags: []
sources:
- theory/additive_bases/L125_random_singer_lift_residual/_index
created: 2026-10-15T11:57:22Z
updated: 2026-10-15T11:57:22Z
---

***

This proves [[theory/additive_bases/L125_random_singer_lift_residual/_index|L125]].
All random variables below are the independent integer lifts in its statement.

## The blocking events for one target

First, $B$ has distinct unordered pair sums modulo $q$, including doubles.
Indeed, a nontrivial equality $b_i+b_j=b_k+b_l$ modulo $q$ rearranges to
two equal nonzero ordered differences. Their uniqueness forces
$(i,k)=(l,j)$, which is the same unordered pair. Cancellation handles a
shared index. Therefore every lift $A_0$ is strong Sidon over the integers.

Fix $m=r+qv$ in a residue $r\notin B$. For every index $j$, uniqueness of
nonzero differences gives one pair $(i,k)$ such that
$b_i-b_k\equiv r-b_j\pmod q$. Neither $k=i$ nor $k=j$ is possible, since
either would put $r$ in $B$. Swapping $i,j$ gives the same triple witness.
After identifying this symmetry, there are at most $s$ distinct triples
$\{i,j\};k$. Each gives one event

$$
E_{\{i,j\};k}:\quad b_i+b_j-b_k+q(d_i+d_j-d_k)=m.
$$

Each lift variable occurs with a positive coefficient in at most one such
event: specifying that index as $j$ uniquely determines $i,k$. It occurs
with a negative coefficient in at most one event, since
$b_i+b_j\equiv r+b_k$ has at most one unordered solution. Repeated positive
indices $i=j$ are allowed and do not affect these statements. Thus each
variable belongs to at most two triple events.

There is at most one further event $H$ of the form
$2m=b_i+b_j+q(d_i+d_j)$, by modular pair-sum uniqueness. Its indices are
distinct: if $i=j$, invertibility of 2 modulo the odd integer $q$ gives
$r\equiv b_i$, contrary to the choice of $r$.

The probability of each triple event is at most $1/M$, by conditioning on
every variable except $d_k$, whose coefficient is $-1$. The midpoint event
has the same bound by conditioning on one of its two variables. These are
integer equations, so all congruence and carry restrictions are already
included.

Join two events when they share a lift variable. A triple event has at
most three other triple neighbors and possibly the midpoint neighbor.
The midpoint event has at most four neighbors. This graph has maximum
degree four. An event is independent of the entire collection of its
nonneighbors, because their defining variables are disjoint from its own.
There are at most $s+1$ events, and their simultaneous failure is precisely
the event that $m$ is unblocked.

## A lower bound on simultaneous failure

Here is the required probability estimate with its proof. Suppose events
$E_1,\ldots,E_t$ have a dependency graph of maximum degree four, and
$\Pr(E_i)\le x(1-x)^4$ for $0<x<1$. Then

$$
\Pr\Bigl(\bigcap_{i=1}^t E_i^c\Bigr)\ge(1-x)^t.
\tag{1}
$$

Inductively, for every $i$ and set $J$ not containing $i$,
$\Pr(E_i\mid\bigcap_{j\in J}E_j^c)\le x$. For the induction step split
$J$ into the neighbors $J_1$ of $i$ and the nonneighbors $J_2$. Independence
makes the conditional probability of $E_i$ given the failures in $J_2$
equal to its unconditional probability. Conditioning also on the failures
in $J_1$ can increase it by at most the reciprocal of their conditional
probability. Exposing those failures in sequence, the induction hypothesis
gives this denominator at least $(1-x)^{|J_1|}$. Thus the desired bound
is at most $x(1-x)^4/(1-x)^{|J_1|}\le x$. The same induction proves that
all conditioning events have positive probability. Exposing all failures
in sequence now proves (1).

Take $x=2/M$. For $M\ge16$,
$(1-2/M)^4\ge(7/8)^4>1/2$, so $1/M\le x(1-x)^4$. Equation (1) and
$t\le s+1$ show that every target counted by $W$ has probability at least
$\beta=(1-2/M)^{s+1}$ of remaining unblocked. Summing its indicator yields
$\mathbb E U\ge W\beta$. No independence between different targets is
asserted or used.

## Fluctuations of the total residual

Changing one $d_i$ affects only triple expressions involving index $i$
and midpoint expressions involving index $i$. There are at most $3s^2$
ordered triple expressions and at most $s$ unordered midpoint expressions
of these forms. Each expression contributes at most one blocked target
before and at most one after the change. Hence $U$ changes by at most
$L=6s^2+2s$.

Expose the $s$ lifts in order and let
$Z_i=\mathbb E[U\mid d_1,\ldots,d_i]$. Independence of the future lifts
and the preceding change bound imply that, with the past fixed, the possible
values of $Z_i$ as $d_i$ varies lie in an interval of length at most $L$.
Since $Z_{i-1}$ is their average, $|Z_i-Z_{i-1}|\le L$. These differences
have conditional mean zero, so their mixed second moments vanish and

$$
\operatorname{Var}(U)=\sum_{i=1}^s
\mathbb E[(Z_i-Z_{i-1})^2]\le sL^2.
$$

If $W>0$, the event $U<W\beta/2$ entails
$|U-\mathbb E U|\ge W\beta/2$. Markov's inequality applied to the squared
deviation gives the claimed probability bound.

Finally, if $ap^3\le N\le bp^3$ with fixed $a,b>0$, then $M\asymp p$,
$s\asymp p$, and
$W\ge N-s\lceil N/q\rceil=N-O(p^2)$. Also
$\log(1-2/M)\ge-4/M$, so $\beta$ is bounded below by a positive constant
depending only on $a,b$. The variance is $O(p^5)$ and
$(W\beta)^2\gg p^6$. The probability bound is therefore $O(1/p)$, uniformly
in $B$, which proves the final assertion. $\square$
