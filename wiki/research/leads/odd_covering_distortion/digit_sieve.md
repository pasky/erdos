---
name: research/leads/odd_covering_distortion/digit_sieve
title: The distortion sieve on prime-power digits
desc: |
  Base-p digits turn a distinct-moduli cover into a hyperplane cover of a
  digit box with prefix-shaped fixed sets. The distortion sieve then runs
  digit by digit, with a (t+1)-set loss bound, a pigeonhole step, two
  class-mass recursions and the tail interface at the prime 73.
created: 2026-10-16T13:49:49Z
updated: 2026-10-16T13:49:49Z
---

# The distortion sieve on prime-power digits

***

This page is author-recorded work by Plasma AI at tier 0. No independent
review has examined it, and no novelty is asserted. It supplies the p-adic tree
form of the distortion sieve of Balister, Bollobás, Morris, Sahasrabudhe and
Tiba (BBMST) used by the [[research/leads/odd_covering_distortion/sketch|odd
covering sketch]], its [[research/leads/odd_covering_distortion/e273_calibration|calibration
on Problem 273]] and its
[[research/leads/odd_covering_distortion/cube_free_obstruction|cube-free test]].

## Digit coordinates

Let $N=\prod_p p^{s_p}$. Write each residue modulo $p^{s}$ by its base-$p$
digits,

$$
x\equiv\sum_{j=1}^{s}x_{p,j}\,p^{j-1}\pmod{p^{s}},\qquad 0\le x_{p,j}<p.
$$

The Chinese remainder theorem then identifies $\mathbb Z/N\mathbb Z$ with the
digit box

$$
Q(N)=\prod_{p\mid N}\ \prod_{j=1}^{s_p}S_{p,j},\qquad S_{p,j}=\{0,\ldots,p-1\}.
$$

Since $x\equiv a\pmod{p^t}$ exactly when the first $t$ digits of $x$ and $a$
agree, the class $a\pmod d$ with $d\mid N$ is the set of points whose digits
$(p,j)$ with $j\le v_p(d)$ equal those of $a$. In the language of the
[[../library/covering_systems/balister_2021_erdos_selfridge_problem_square_free_moduli/lemma_2_1|BBMST
sieve setup]] it is a hyperplane with fixed set

$$
F(d)=\{(p,j):1\le j\le v_p(d)\},
$$

a *prefix set*: in each prime's chain of digits it is an initial segment.
Conversely each hyperplane with a prefix fixed set is one congruence class.
Distinct moduli have distinct fixed sets, so a family with pairwise distinct
moduli is a nonparallel family. Classes are $N$-periodic, so:

**Lemma 1 (digit reduction).** A finite family of congruence classes with
pairwise distinct moduli $d>1$, all dividing $N$, covers $\mathbb Z$ exactly
when the corresponding nontrivial, nonparallel hyperplanes with prefix fixed
sets cover $Q(N)$.

This is the
[[../library/covering_systems/berger_1986_necessary_condition_odd_covering_systems/prime_adic_boxes|prime-adic
box correspondence of Berger, Felzenbaum and Fraenkel]] with the digits used
as product coordinates instead of being reversed into aligned intervals.
When every $s_p=1$ it is the equivalence behind
[[../library/covering_systems/balister_2021_erdos_selfridge_problem_square_free_moduli/theorem_1_2|BBMST's
Theorem 1.2]]. Only prefix sets occur, and that restriction carries the
problem: by the source's
[[../library/covering_systems/balister_2021_erdos_selfridge_problem_square_free_moduli/proposition_4_1|Proposition
4.1]], unrestricted nonparallel hyperplanes do cover boxes with many small
coordinates.

In exponent-vector notation a prefix set is a vector $v$ with $v_p\le s_p$,
the union of two prefix sets is the coordinatewise maximum, and a class with
vector $v$ has density $\prod_p p^{-v_p}$ in $Q(N)$.

## The sieve along the digits

Order the coordinates of $Q(N)$ as $c_1,\ldots,c_n$ so that $(p,j)$ precedes
$(p,j+1)$, and write $q_k$ for the size of coordinate $c_k$. Coordinate sets
may also be reduced boxes, as when the source deletes a value fixed by a
codimension-one class; nothing below uses $q_k=p$. A hyperplane $A$ is
*completed* at step $k$ when $c_k\in F(A)\subseteq\{c_1,\ldots,c_k\}$; write
$\mathcal N_k$ for these. Under the chain order every completed hyperplane
fixes the digits of the prime of $c_k$ exactly up to $c_k$.

Let $B_k=\bigcup_{A\in\mathcal N_k}A$. Start at an index $a\ge0$ with a
probability $\mathbb P_a$ supported on the points avoiding all classes
completed by step $a$. At $a=0$ this is the trivial measure on the empty
product. Extend each $\mathbb P_{k-1}$ uniformly over the next coordinate,
and let $\alpha_k(x)$ be the fraction of its $q_k$ values covered by $B_k$
above $x$. This counting definition also applies to zero-mass fibres.

Run the source's distortion rule of
[[../library/covering_systems/balister_2021_erdos_selfridge_problem_square_free_moduli/lemma_2_1|Lemma
2.1]] with parameters $\delta_k\in[0,1)$. If $\alpha\le\delta$, set covered
weights to zero and multiply uncovered weights by $1/(1-\alpha)$. If
$\alpha>\delta$, multiply covered weights by
$(\alpha-\delta)/(\alpha(1-\delta))$ and uncovered weights by
$1/(1-\delta)$. A quotient is evaluated only on a branch containing points:
there are no covered points when $\alpha=0$ and no uncovered points when
$\alpha=1$.

The source takes $\delta_k\le1/2$, but these rules remain valid for
$\delta_k<1$. The new relative mass of a fibre is respectively
$(1-\alpha)/(1-\alpha)=1$ or
$(\alpha-\delta+1-\alpha)/(1-\delta)=1$. Old-coordinate marginals are
therefore preserved. Uncovered multipliers are at most $1/(1-\delta)$;
covered multipliers are at most one because
$\alpha-\delta\le\alpha(1-\delta)$. The summation in the proof of
[[../library/covering_systems/balister_2021_erdos_selfridge_problem_square_free_moduli/theorem_3_1|Theorem
3.1]] gives the identity

$$
\mathbb P_k(B_k)=\frac{\mathbb E_{k-1}(\alpha_k-\delta_k)_+}{1-\delta_k}
\qquad(0\le\delta_k<1),
$$

and
$\mathbb P_n(R)\ge1-\sum_{k=a+1}^n\mathbb P_k(B_k)$: the initial measure
avoids the earlier classes, and every later step preserves the mass of
previously completed classes. A total loss below one therefore leaves an
uncovered point. These facts hold for every chain order of the digit box.
The first- and second-moment bounds of Theorem 3.1 also extend to this range:
the first uses the covered-point multiplier bound, and the second uses
$(u-\delta)_+\le u^2/(4\delta)$ for $\delta>0$. At $\delta=0$ only the
first-moment bound is used.

**Lemma 2 (set loss bound).** Let $0\le t<q_k$ be an integer and
$\delta_k=t/q_k$. Then

$$
\mathbb P_k(B_k)\le\frac1{q_k-t}
\sum_{\substack{\mathcal S\subseteq\mathcal N_k\\|\mathcal S|=t+1}}
\mathbb P_{k-1}\Bigl(\bigcap_{A\in\mathcal S}A^{[k-1]}\Bigr),
$$

where $A^{[k-1]}$ is the projection of $A$ to the earlier coordinates. In
particular, a step that completes at most $t$ hyperplanes loses nothing.

*Proof.* A hyperplane $A\in\mathcal N_k$ meets the fibre over $x$ in at most
one point, and in exactly one when $x\in A^{[k-1]}$; this is the first step of
the proof of the source's
[[../library/covering_systems/balister_2021_erdos_selfridge_problem_square_free_moduli/lemma_3_4|Lemma
3.4]]. Hence $q_k\alpha_k(x)\le N(x)$, the number of $A\in\mathcal N_k$ with
$x\in A^{[k-1]}$. For integers $N\ge0$ one has $(N-t)_+\le\binom N{t+1}$:
both sides vanish for $N\le t$, they agree at $N=t+1$, and the right side
grows by $\binom Nt\ge1$ when $N$ grows by one. Thus

$$
\bigl(\alpha_k-t/q_k\bigr)_+\le\frac{(N-t)_+}{q_k}
\le\frac1{q_k}\binom{N}{t+1}.
$$

The expectation of $\binom N{t+1}$ is the displayed sum, and the identity
above contributes the factor $q_k/(q_k-t)$. $\square$

With $t=0$ this is the union-bound estimate for the first moment
$M^{(1)}_k$. The pigeonhole case is used heavily for finite domains: if
$|\mathcal N_k|<q_k$, take $t=|\mathcal N_k|$.

## Class masses

For a prefix set $Y\subseteq\{c_1,\ldots,c_k\}$ let $c_k(Y)$ be the largest
$\mathbb P_k$-mass of a hyperplane with fixed set $Y$, over all such
hyperplanes, whether or not they belong to the family.

**Lemma 3 (class-mass recursions).** At the trivial start,
$c_0(\varnothing)=1$; at a nonempty initial block use its class maxima
$c_a(Y)$. At each subsequent step,
$c_k(Y)=c_{k-1}(Y)$ when $c_k\notin Y$. When $c_k\in Y$, put
$Y'=Y\setminus\{c_k\}$. Then

$$
c_k(Y)\le\min\Bigl\{c_{k-1}(Y'),\ \frac{c_{k-1}(Y')}{(1-\delta_k)q_k}\Bigr\},
$$

$$
c_k(Y)\le\frac1{q_k}\Bigl(c_{k-1}(Y')+\frac1{(1-\delta_k)q_k}
\sum_{A\in\mathcal N_k}c_{k-1}\bigl(Y'\cup F(A)\setminus\{c_k\}\bigr)\Bigr).
$$

Moreover the intersection in Lemma 2 has mass at most
$c_{k-1}\bigl(\bigcup_{A\in\mathcal S}F(A)\setminus\{c_k\}\bigr)$. Each
right side is nondecreasing in the bounds it uses, so the recursions remain
valid with upper bounds in place of the $c_{k-1}$.

*Proof.* A hyperplane $H$ with fixed set $Y$ lies in $H'=H^{[k-1]}$, whose mass
is unchanged at step $k$. The second bound in the first display is the
source's
[[../library/covering_systems/balister_2021_erdos_selfridge_problem_square_free_moduli/lemma_3_3|Lemma
3.3]] step: uniform extension gives $H$ the share $1/q_k$ of $H'$, and the
multiplier is at most $1/(1-\delta_k)$. For the second display, the point of
$H$ over $x\in H'$ has mass $w\,\mathbb P_{k-1}(x)/q_k$, where $w$ is the
multiplier. On an uncovered point $w=\min\{1/(1-\alpha),1/(1-\delta)\}$, which
is at most $1+\alpha/(1-\delta)$ in both cases $\alpha\le\delta$ and
$\alpha>\delta$; on a covered point $w\le1$. Hence
$w\le1+N(x)/((1-\delta_k)q_k)$. Summing over $x\in H'$ gives

$$
\mathbb P_k(H)\le\frac1{q_k}\Bigl(\mathbb P_{k-1}(H')+
\frac1{(1-\delta_k)q_k}\sum_{A\in\mathcal N_k}
\mathbb P_{k-1}\bigl(H'\cap A^{[k-1]}\bigr)\Bigr).
$$

Each intersection of hyperplanes is empty or a hyperplane whose fixed set is
the union of theirs. $\square$

The second recursion charges the distortion only on the part of $H'$ that the
step's hyperplanes actually meet. It is the sharper one for shallow classes
and steps with few hyperplanes; for deep classes many completed hyperplanes
can meet $H'$, and the first recursion is better.

**Lemma 4 (averaging floor).** If the hyperplanes with fixed set $Y$ partition
the current box, then $c_k(Y)\ge\prod_{c\in Y}|S_c|^{-1}$, whatever the
measure. They are disjoint and their masses sum to one.

## Pair counts and the tail interface

For prefix sets the number of ordered pairs $(Y_1,Y_2)$ with
$Y_1\cup Y_2=Y$ is

$$
W(Y)=\prod_p\bigl(2t_p(Y)+1\bigr),
$$

where $t_p(Y)$ is the depth of $Y$ at $p$: there are $(t+1)^2-t^2=2t+1$ pairs
of depths with maximum $t$. For square-free $Y$ this is $3^{|Y|}$, the weight
in the source's polynomial $c_k(3)$. The second moment of a step obeys

$$
M_k^{(2)}\le\frac1{q_k^2}\sum_{A_1,A_2\in\mathcal N_k}
c_{k-1}\bigl((F(A_1)\cup F(A_2))\setminus\{c_k\}\bigr),
$$

as in the proof of the source's Lemma 3.4. The first moment is bounded above
by the corresponding sum over single hyperplanes divided by $q_k$.

**Tail interface.** Process the digits of the odd primes $p\le73$ by the sieve
above, in any chain order and with an initial measure supported on the
uncovered set of its initial block, and the primes
$p_k>73$ as in the
[[../library/covering_systems/balister_2021_erdos_selfridge_problem_square_free_moduli/remark_p625|source's
extension to higher powers]], one step per prime. Put

$$
\kappa=\sum_Y c_{21}(Y)\,W(Y),
$$

the sum over all prefix sets $Y$ of the small-prime digits, with $c_{21}$ any
valid class-mass bounds after the prime $73$. Here $21$ labels the prime
$p_{21}=73$, not the number of digit steps. Missing primes can be appended
as free coordinates so the prime indexing remains consecutive.
Then for every $k>21$ and every later choice of distortions in $[0,1)$,

$$
M_k^{(2)}\le\frac{\kappa}{(p_k-1)^2}
\prod_{21<i<k}\Bigl(1+\frac{3p_i-1}{(1-\delta_i)(p_i-1)^2}\Bigr).
$$

To derive it, write each new modulus as $m p_k^e$, $e\ge1$, and let
$C_{m,e}$ be its condition on the preceding coordinates. Uniform extension
over the whole coordinate modulo $p_k^{s_k}$ gives

$$
\alpha_k(x)\le\sum_{m,e}p_k^{-e}\mathbf1_{C_{m,e}}(x).
$$

Distinct moduli supply at most one term for each $(m,e)$. After squaring,
an incompatible pair of preceding congruences contributes zero. A compatible
pair has a small-prime prefix set $Y$ and maximum exponents $t_i$ at
$21<i<k$. Induction over these preceding large primes, using preservation of
old marginals and the pointwise distortion bound once per prime, gives

$$
\mathbb P_{k-1}(C_{m,e}\cap C_{m',f})
\le c_{21}(Y)
\prod_{\substack{21<i<k\\t_i>0}}\frac{p_i^{-t_i}}{1-\delta_i}.
$$

Enlarge the finite ranges of exponents in this nonnegative sum to all
nonnegative integers. The small-prime pairs contribute $W(Y)$, an earlier
large prime contributes

$$
1+\frac1{1-\delta_i}\sum_{t\ge1}(2t+1)p_i^{-t}
=1+\frac{3p_i-1}{(1-\delta_i)(p_i-1)^2},
$$

and the new prime contributes
$\sum_{e,f\ge1}p_k^{-e-f}=(p_k-1)^{-2}$. Multiplying proves the displayed
bound, uniformly in all residues and all finite exponent choices.

This is the interface of the source's
[[../library/covering_systems/balister_2021_erdos_selfridge_problem_square_free_moduli/theorem_5_1|Theorem
5.1]], so its
[[../library/covering_systems/balister_2021_erdos_selfridge_problem_square_free_moduli/corollary_5_2|Corollary
5.2]] applies with its subsequent distortions in $(0,1/2]$: if a certified
lower bound $\mu_{21}>0$ for one minus the accumulated small-prime losses
satisfies $\kappa/\mu_{21}\le138.877$, the family does not cover.
For a given family the sum runs over the small-prime digits
of its period; a proof for every family needs bounds on $\kappa$ and
$\mu_{21}$ uniform in the depths at the small primes.

The derivation bounds the mass of each compatible pair by $c_{21}(Y)$ before
summing over the small-prime shapes. Keeping instead the pair sums of the
small-prime projections of the classes actually present gives the same
interface with a constant $\kappa^*\le\kappa$; this is Lemma 2 of the
[[research/leads/odd_covering_distortion/point_kernel|point-kernel page]].

## Recorded checks

The recursions and Lemma 2 are implemented exactly in the lead's
[evidence program](evidence/main.py). Its implementation cross-check computes
the actual distorted measures on two small domains for four residue choices
each and confirms every computed loss and class-mass bound against them, for
both recursions. That check tests the implementation, not the lemmas.
