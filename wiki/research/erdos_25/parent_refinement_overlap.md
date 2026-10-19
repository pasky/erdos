---
name: research/erdos_25/parent_refinement_overlap
desc: A uniform all-scale obstruction to bounded-overlap refinements of the overlapping 0/1-parent preparations; unrestricted overlap remains open.
tags: [constructions, sieve, overlap, partial-results]
sources: []
created: 2026-09-22T12:34:00Z
updated: 2026-09-24T22:13:01Z
---


# research/erdos_25/parent_refinement_overlap

***

The [overlapping preparation](overlapping_parent_preparations.md) produces
many protected points in parents of very small conditional survivor
measure. The following theorem rules out refining these parents with
bounded overlap, at **all** cutoffs, not only polynomial-length epochs.
The later [weighted estimates](weighted_divisibility_moments.md) improve
its error and remove overlap restrictions up to a quantified cutoff.
The last section below also treats arbitrary overlap at every cutoff
when the assigned parent leaves only a small prime-factor rank.
The unrestricted case remains open.

## Statement

Let $\mathcal P=\{p:3\le p\le z\}$,
$\lambda=\sum_{p\in\mathcal P}1/p$, and, for large $\lambda$, put
$$
 r=\lfloor2\lambda-6\sqrt\lambda\rfloor,
 \quad b=\lceil2\lambda+2\sqrt\lambda\rceil,
 \quad s=b-r=O(\sqrt\lambda).
$$
Write
$$
 R(x)=\#\{p\in\mathcal P:x\bmod p\in\{0,1\}\},
 \qquad T=\{R\le b\}.
$$
Let $S$ be the full survivor set of any finite preparation with
squarefree moduli supported on $\mathcal P$, prescribing only digits
0 and 1 at those primes. A parent fixes such digits at exactly $r$
primes. Append classes $C_q=[a_q]_q$, $0\le a_q<q$, with
globally distinct moduli, each refining one chosen assigned parent.
Parents here are geometric cylinders, not potentially repeated labels.

Assume the classes assigned to each parent have pointwise multiplicity
at most $L$ on $T$. Let $U=\bigcup_q C_q$,
$\tau=\mu(S\cap U)$, and let $B$ be the appended union activated
at $n\ge q$. With $c_0=2\log2-1>0$, uniformly for $X\ge2$,
$$
 \frac{H_{S\cap T\cap B}(X)}{H_{\lfloor X\rfloor}}
 \le L\exp\{O(\sqrt\lambda\log(2\lambda))\}\tau
   +\exp\{-c_0\lambda/2+O(\sqrt\lambda\log(2\lambda))\}.
 \tag{1}
$$
All constants are absolute. In particular, $\tau\le e^{-c\lambda}$
and $L=e^{o(\lambda)}$ force the left side to tend to zero uniformly
in $X$. This includes one refinement per parent, or disjoint
refinements within each parent. The protected set $G$ in the earlier
preparation lies in $S\cap T$, so (1) applies to its trace.

## A dimension-two progression estimate

Define
$$
 V_z=\prod_{p\in\mathcal P}(1-2/p),\quad
 P_q=\prod_{\substack{p\in\mathcal P\\p\mid q}}(1-2/p)^{-1},\quad
 F_s=\sum_{\substack{J\subseteq\mathcal P\\|J|\le s}}
                 \prod_{p\in J}\frac2{p-2}.
$$
Since $\sum_{p\in\mathcal P}2/(p-2)=2\lambda+O(1)$,
$$
 F_s\le\sum_{j=0}^s\frac{(2\lambda+O(1))^j}{j!}
       =\exp\{O(\sqrt\lambda\log(2\lambda))\}.
 \tag{2}
$$
Let $j_q$ count the primes of $\mathcal P$ dividing $q$ at
which $a_q$ has digit 0 or 1. Then $j_q\ge r$. Omit classes
with $j_q>b$, which do not meet $T$. Independence at the primes
not dividing $q$ gives the exact conditional probability
$$
 \theta_q:=\mu(T\mid C_q)
 =V_zP_q
  \sum_{\substack{J\subseteq\{p\in\mathcal P:p\nmid q\}\\
                  |J|\le b-j_q}}
          \prod_{p\in J}\frac2{p-2}.
 \tag{3}
$$
In particular $V_zP_q\le\theta_q\le V_zP_qF_s$.

We claim that, for $W\ge1$,
$$
 \sum_{\substack{1\le t\le W\\a_q+qt\in T}}\frac1t
 \le C\theta_q\log(2W)
       +\exp\{O(\sqrt\lambda\log(2\lambda))\}\sqrt{P_q}.
 \tag{4}
$$
Use the proved [elementary dimension-two upper sieve](local_colored_power_cutoff.md#an-elementary-upper-sieve-of-fixed-dimension),
and choose an absolute $B>B_2+2$, where $B_2$ is its length
exponent. For $Y\le z^{s+B}$, sieve at $w=Y^{1/(s+B)}$.
A counted quotient has at most $s$ successes at primes at most
$w$ not dividing $q$. Group by their exact set $J$ and their
two possible digits. Their product $d$ is at most $w^s$;
the remaining quotient interval has length $Y/d\ge w^B$, so the
upper sieve applies to the other primes. Summing its bound gives
$$
 N_q(Y):=\#\{1\le t\le Y:a_q+qt\in T\}
 \le C(s+B)^2P_qF_s\frac{Y}{(\log Y)^2}
 \tag{5}
$$
when $w\ge3$. The trivial bound $N_q(Y)\le Y$ handles the
remaining range. To see the factor in (5), the summand for a fixed
success set is
$(Y/d)2^{|J|}\prod_{p\le w,\,p\nmid qd}(1-2/p)$.
Factor out the complete avoiding product and use (2),
$\prod_{3\le p\le w}(1-2/p)\ll(\log w)^{-2}$, and
$\log w=\log Y/(s+B)$.

For $Y\ge z^{s+B}$, instead sieve at $w=z$, grouping by at
most $b-j_q$ successes. The same divisor sum is now exactly (3),
giving
$$
 N_q(Y)\le C\theta_qY.
 \tag{6}
$$
Partial summation proves (4): the short-range contribution is bounded
using $\int_0^\infty\min(1,A/u^2)\,du=2\sqrt A$, with
$A=C(s+B)^2P_qF_s$; the long range contributes
$C\theta_q\log(2W)$. No assumption is made about extra prime
factors or prime powers of $q$.

## Distinctness controls the remaining arithmetic error

Let
$$
 \beta_r=\Pr\left\{\sum_{p\in\mathcal P}
                 \operatorname{Bernoulli}(1/p)\ge r\right\}.
$$
Chernoff's inequality at parameter $\log2$ gives
$$
 \beta_r\le2^{-r}\prod_{p\in\mathcal P}(1+1/p)
        \le\exp\{-c_0\lambda+O(\sqrt\lambda)\}.
 \tag{7}
$$
Every appended modulus has at least $r$ prime factors in
$\mathcal P$. Distinctness and the exact multiples inequality from
[basic reductions](basic_reductions.md#an-exact-finite-harmonic-inequality-for-multiples-proved)
therefore imply
$$
 \sum_{q\le X}\frac1q\le\beta_rH_{\lfloor X\rfloor}.
 \tag{8}
$$
Put $\sigma_X=\sum_{q\le X}\theta_q/q$. Activation represents
every hit as $a_q+qt$ with $t\ge1$. Since
$1/(a_q+qt)\le1/(qt)$, (4) and the union bound give
$$
 \frac{H_{T\cap B}(X)}{H_{\lfloor X\rfloor}}
 \le C\sigma_X+
 \frac{\exp\{O(\sqrt\lambda\log(2\lambda))\}}
      {H_{\lfloor X\rfloor}}
       \sum_{q\le X}\frac{\sqrt{P_q}}q.
 \tag{9}
$$

The elementary bound
$$
 P_q\ll(\log\log(3q))^2
 \tag{10}
$$
is uniform. Indeed $P_q$ is bounded by a constant times
$\prod_{p\mid q}(1-1/p)^{-2}$. Split those primes at
$\log(3q)$. The smaller-prime product is
$O((\log\log(3q))^2)$; the logarithm of the remaining product
is $O(\omega(q)/\log(3q))=O(1)$.

Write $H=H_{\lfloor X\rfloor}$. If $H\le e^{2\lambda}$, (8)
and (10) bound the last factor in (9) by $O((1+\lambda)\beta_r)$.
If $H>e^{2\lambda}$, use $V_z=e^{-2\lambda+O(1)}$,
$\theta_q\ge V_zP_q$, Cauchy--Schwarz, and (8) to get
$$
 \frac1H\sum_{q\le X}\frac{\sqrt{P_q}}q
 \ll e^\lambda\sqrt{\frac{\sigma_X\beta_r}{H}}
 \le C\sqrt{\sigma_X\beta_r}.
$$
When $\sigma_X\le1$, these estimates prove
$$
 \frac{H_{T\cap B}(X)}H
 \le C\sigma_X+
 \exp\{-c_0\lambda/2+O(\sqrt\lambda\log(2\lambda))\}.
 \tag{11}
$$
When $\sigma_X>1$, the same assertion follows from the trivial
bound one.

## Comparing the low-count region to actual survivors

First discard any appended class with $S\cap C_q=\varnothing$;
this changes no hits on $S$. Apply (11) to this retained family,
and henceforth let $\sigma_X$ denote its raw mass sum.
For the union $U_X$ of the remaining
classes with $q\le X$, we claim
$$
 \mu(T\cap U_X)\le F_s\mu(S\cap U_X).
 \tag{12}
$$
Take $x\in T\cap C_q$. Let $J$ be its success primes in
$\mathcal P$ not dividing $q$. There are at most $s$ of them.
Change all their digits to arbitrary nonsuccess digits. Every resulting
point still lies in $C_q$, and now has no success prime outside
$q$. It must survive the preparation: a matching preparatory class
would use only primes dividing $q$, hence would contain all of
$C_q$, contrary to the discard step.

Thus the entire nonsuccess fiber at $J$, with all other coordinates
fixed, belongs to $E=S\cap U_X$. For each fixed $J$, let $F_J$
be the set of other-coordinate configurations whose full nonsuccess
fiber lies in $E$. Expanding these fibers to success digits has
measure
$$
 \mu(F_J)\prod_{p\in J}\frac2p
 \le \mu(E)\prod_{p\in J}\frac2{p-2}.
$$
Every point of $T\cap U_X$ occurs in one such expanded fiber.
Summing over $|J|\le s$ proves (12). All sets here are finite
unions of cylinders; no infinite-fiber measurability assertion is needed.

Finally a point of $T$ belongs to at most $\binom br$ parents:
choose their $r$ primes among its at most $b$ success primes,
after which the digits are forced. The in-parent overlap assumption
therefore gives
$$
 \sigma_X\le L\binom br\mu(T\cap U_X)
        \le L\binom br F_s\tau.
$$
Both $\binom br$ and $F_s$ are
$\exp\{O(\sqrt\lambda\log(2\lambda))\}$. Substitute in (11),
and note that the retained union covers every point counted on the
left of (1). This proves the theorem.

## Remaining gap

The progression estimate, raw-mass bound (11), and survivor comparison
(12) hold without a multiplicity hypothesis. Only the final passage
from $\sigma_X=\sum_q\mu(T\cap C_q)$ to union measure needs it.
Without the scale or residual-rank restrictions proved in the later
sections, no estimate removing that overlap loss has been proved. Nor has a
construction with enough overlapping refinements and protected active
trace been obtained. Therefore this theorem excludes a substantial
subclass of the proposed construction, not a general counterexample
or a general density theorem.

## Arbitrary overlap with bounded residual rank

There is a second all-scale theorem, which replaces the overlap
hypothesis by a rank hypothesis. Assign each appended class to one
geometric parent $C=[a]_d$, and suppose
$$
 q=dm,\qquad \Omega(m)\le K.
$$
The parent modulus is a squarefree product of exactly $r$ old
primes, and its digits are 0 or 1, as above. Uniformly in $X\ge2$,
without any overlap bound,
$$
 \frac{H_{S\cap T\cap B}(X)}{H_{\lfloor X\rfloor}}
 \le 54^K\exp\{O(\sqrt\lambda\log(2\lambda))\}\tau
      +\exp\{-c_0\lambda+O(\sqrt\lambda\log(2\lambda))\}.
 \tag{13}
$$
In particular $K=o(\lambda)$ and $\tau\le e^{-c\lambda}$,
for fixed $c>0$, exclude a protected harmonic anomaly at every
cutoff. Rank counts prime factors with multiplicity; no restriction
on the sizes or identities of the extra primes is imposed.

Retain only classes with $q\le X$, with $j_q\le b$, and
with $S\cap C_q\ne\varnothing$. Partition the counted active
hits disjointly among these classes. Within one assigned parent write
$q_i=dm_i$ and let $c_i$ be the assigned harmonic mass divided
by $H=H_{\lfloor X\rfloor}$. Put
$$
 \alpha=\sum_i c_i,\qquad \theta_0=V_zP_d.
$$
First suppose $H\ge e^{2\lambda}$.

For each divisor $e$ of some $m_i$, and $v\pmod e$, let
$$
 S_{e,v}=\sum_{\substack{i:e\mid m_i\\
              (a_{q_i}-a)/d\equiv v\pmod e}}c_i.
$$
The assigned points in this sum belong to the face $[a+dv]_{de}$.
They also satisfy $n\ge q_i\ge de$, so the face is active.
It still prescribes at least the $r$ parent successes. Apply the
progression estimate (4) to this face. Since
$$
 P_{de}\le3^K P_d,\quad
 \theta_{de}\le V_zP_{de}F_s,\quad
 \frac{\sqrt{P_d}}H\ll V_zP_d=\theta_0,
$$
it gives
$$
 S_{e,v}\le\frac{A\theta_0}{de},\qquad
 A\le3^K\exp\{O(\sqrt\lambda\log(2\lambda))\}.
 \tag{14}
$$
If the face forces more than $b$ successes it contributes zero
and needs no sieve estimate. The last displayed bound uses
$V_z=e^{-2\lambda+O(1)}$ and $P_d\ge1$.

Every retained class satisfies $\theta_{q_i}\ge\theta_0$.
Every nonempty compatible pair intersection has conditional
$T$-probability at most $B_0\theta_0$, where
$$
 B_0\le3^{2K}F_s.
$$
Indeed its modulus is $d[m_i,m_j]$, adding at most $2K$
prime factors to the parent, and it forces at least $r$
successes. An intersection forcing more than $b$ contributes zero.

On the profinite probability space put
$$
 Z=\sum_i dm_i c_i\mathbf1_{T\cap C_{q_i}}.
$$
Then $\mathbb EZ\ge\theta_0\alpha$. Expanding the second
moment, using CRT, and writing $(m_i,m_j)=\sum_{e\mid(m_i,m_j)}\varphi(e)$,
gives the upper bound
$$
 \mathbb EZ^2
 \le d B_0\theta_0\sum_e\varphi(e)\sum_v S_{e,v}^2
 \le A B_0\theta_0^2\sum_i c_i
                         \sum_{e\mid m_i}\frac{\varphi(e)}e
 \le A B_0 2^K\theta_0^2\alpha.
 \tag{15}
$$
In the first inequality it is harmless to include pairs compatible
modulo $e$ but incompatible modulo their full gcd. The second
inequality is (14), and the last uses
$\sum_{e\mid m}\varphi(e)/e\le d(m)\le2^{\Omega(m)}$.
Cauchy--Schwarz on the support $T\cap U_C$ now gives
$$
 \alpha\le54^K\exp\{O(\sqrt\lambda\log(2\lambda))\}
                       \mu(T\cap U_C),
$$
where $U_C$ is the union assigned to that parent.

Each point of $T$ lies in at most $\binom br$ geometric
parents. Sum the preceding bound over parents and apply (12):
$$
 \sum_C\mu(T\cap U_C)
 \le\binom br\mu(T\cap U_X)
 \le\binom br F_s\tau.
$$
Both new factors are $\exp\{O(\sqrt\lambda\log(2\lambda))\}$.
This proves the first term of (13) in the large-cutoff range.

For $H<e^{2\lambda}$, the overlap-free bound (3) of
[weighted divisibility moments](weighted_divisibility_moments.md)
is at most $\exp\{-c_0\lambda+O(\sqrt\lambda\log(2\lambda))\}$,
since $\kappa=2+c_0$. This proves (13) for the remaining cutoffs.
Every counting step retained original activation, and distinctness
enters the weighted cutoff for the small-cutoff range. Arbitrary
unbounded residual rank and arbitrary overlap together are not covered.
