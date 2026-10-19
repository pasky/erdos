---
name: research/leads/square_complement_repair_frontier
title: Restricted repairs of annular square complements
desc: |
  Annular calculations, restricted repair barriers, exact counterexamples,
  and author-recorded comparisons for square complements.
problems:
- 33
research_state: candidate
review_status: unreviewed
created: 2026-09-09T02:22:43Z
updated: 2026-10-19T04:19:07Z
---

# Restricted repairs of annular square complements

[[research/leads/_index|..]]

[[research/leads/square_complement_repair_frontier/five_adic_comparison|five_adic_comparison]]: A complete author-recorded five-adic comparison with upper limit 99/20,
whose coverage and real-prefix proofs do not improve the 9/2 target.

[[research/leads/square_complement_repair_frontier/proof_sketch|proof_sketch]]: Lifted-root repair routes, a seven-adic skeleton counterexample family,
and author-recorded comparisons with no improved square complement.

[[research/leads/square_complement_repair_frontier/seven_adic_repair_failure|seven_adic_repair_failure]]: A coverage counterexample and excessive intermediate prefix for one
specified seven-adic repair, with both failures author-recorded.

[[research/leads/square_complement_repair_frontier/triadic_essential_bridge_interval|triadic_essential_bridge_interval]]: An author-recorded positive-density interval of essential bridge points
in the specified ternary set, with deletion and replacement limits explicit.

[[research/leads/square_complement_repair_frontier/triadic_one_step_barrier|triadic_one_step_barrier]]: A discrete 9/2 barrier for repairs retaining the ternary outer skeleton
and its old root class, with an author-recorded quantitative escape bound.

***

This lead's notes that cite no source are author-recorded research, not claims.

## Target and standing

The target is a set $B\subseteq\mathbb Z_{>0}$ such that every sufficiently
large integer is $m^2+b$, with $m\ge0$ and $b\in B$, and

$$
\limsup_{X\to\infty}\frac{B(X)}{\sqrt X}<\frac92,
\qquad B(X)=|B\cap[1,X]|.
$$

This is a particular improvement target within
[[problems/additive_bases/E0033/_index|Problem 33]], not a proposed value of the
infimum over all square complements. Real cutoffs and positive residuals
are used throughout.

The baseline is
[[theory/additive_bases/L3_square_complement_nine_halves/_index|L3]]:
its specified set represents every positive integer and has lower and upper
counting limits $3\sqrt2$ and $9/2$. Its
[[theory/additive_bases/L3_square_complement_nine_halves/_proof|proof]]
supplies the root transitions, coverage and uniform cutoff estimates. L3 is
author-recorded at tier 0. Its construction and proof are not repeated here.

The calculations below are also author-recorded, without independent
acceptance. The widened-annulus comparison is a completed calculation for
one specified family. The one-step mass implication is conditional; the
smaller-radius repair and seven-adic route remain incomplete, not refuted.
In particular, none of these deductions proves optimality of L3 among all
square complements, or among all multiscale repairs. The baseline statement
and proof were read; no external theorem is consumed and no new literature
or priority assessment is made here. The linked problem page records the
separate public-source assessment.

## Further author-recorded obstructions and comparisons

The [lifted-root proof sketch](proof_sketch.md) retains an explicit infinite
family missed by the seven-adic skeleton, including the witness 14851 and the
fixed-center monotonicity argument. Patching this family alone costs only an
added set with O(log X) points up to X, so it supplies no positive asymptotic
lower bound on general repairs. The sketch also records the dated source context
and the remaining construction obligations.

The following notes have complete author-recorded arguments in their stated
scopes. None has independent acceptance or supplies a square complement below
9/2.

- The [discrete ternary barrier](triadic_one_step_barrier.md) proves a 9/2
  limsup obstruction when the outer skeleton is retained and the displayed
  forced targets use the old root class. It includes all five eligible roots,
  disjoint contributions across scales, and a quantitative escape condition.
  It does not constrain every square complement or every repair policy.
- The [essential bridge interval](triadic_essential_bridge_interval.md) identifies
  q/10000+O(1) bridge points per sufficiently large ternary scale that cannot be
  deleted without replacement; each supports at least q/72000-o(q) uniquely
  represented targets. It makes no optimality or universal-essentiality claim.
- The [specified seven-adic repair](seven_adic_repair_failure.md) misses 26522
  and has an intermediate-prefix lower bound 195/(28*sqrt(2))>9/2. These are
  separate coverage and counting failures of that exact set.
- The [five-adic comparison](five_adic_comparison.md) supplies full coverage
  and uniform real-prefix counts with upper limit 99/20, above the target.

The discrete ternary result supplies a separate obstruction for its explicit
old-root policy; it does not retroactively prove every unestablished passage
in the conditional radial model below. The bare seven-adic skeleton's omission
family likewise leaves the broader replacement route incomplete. The existing
annular, parity and conditional calculations retain their original scope.

## Widening a fixed annular family

Use L3's notation
$R_M=\{a\in\mathbb Z_{>0}:a\equiv0,1,2\pmod M\}$, with repeated
classes identified. For a fixed real $4\le c<8$, consider exactly

$$
B_c=\bigcup_{q=3^k,\ k\ge0}
\left(
R_{2q}\cap[cq^2/9,cq^2]
\;\cup\;
R_q\cap[(c+1)q^2/9,q^2]
\right).
\tag{1}
$$

The changed bridge follows from the same root transition used in L3.
Write $a=t-m^2>cq^2$, where $0\le m\le q$ is the old bounded root.
If the next bounded root is $2q-m$, its residual
$a-4q^2+4qm$ is positive because $c\ge4$. Thus a transition to a
nonpositive residual can only use $2q+m$. Put

$$
e=a-4q^2+4qm,
\qquad b=a+2qm-q^2=\frac{a+e}{2}+q^2.
$$

The positive residual $e$ is caught by the nested outer annuli when
$e\le cq^2$. Otherwise $b>(c+1)q^2$, while the nonpositive new
residual gives $b\le3q^2+6qm\le9q^2$. Its congruence is the bridge
congruence modulo $3q$ from L3. This is precisely the bridge in (1) at
scale $3q$. L3's positive-residual descent and first-crossing argument
therefore apply with these changed endpoints; a finite initial segment
can in any case be adjoined without changing the limits below.

On a cycle $(cq^2/9,cq^2]$, the successive normalized radial intervals
and densities are

$$
\begin{array}{c|c}
X/q^2&\text{density}\\ \hline
(c/9,(c+1)/9)&3/(2q)\\
((c+1)/9,1)&3/q\\
(1,c)&3/(2q).
\end{array}
$$

Endpoints change only $O(1)$ terms. Smaller annuli end before the cycle
and larger ones start after it, apart from shared endpoints. Thus its
count is $D(c)q+O(1)$, where

$$
D(c)=\frac32\frac19+3\frac{8-c}{9}
       +\frac32(c-1)=\frac{7c+8}{6}.
\tag{2}
$$

The preceding cycles contribute $D(c)q/2+O(k+1)$ at $q=3^k$.
Consequently, with $x=X/q^2$, the normalized leading prefix is

$$
F_c(x)=\frac{D(c)}2+
\begin{cases}
\frac32(x-c/9),&c/9\le x\le(c+1)/9,\\
\frac16+3(x-(c+1)/9),&(c+1)/9\le x\le1,\\
\frac16+\frac{8-c}{3}+\frac32(x-1),&1\le x\le c.
\end{cases}
\tag{3}
$$

For fixed $c$, the error in $B_c(X)=qF_c(X/q^2)+O(k+1)$ is uniform
within the cycle: there are only three periodic interval counts. After
division by $\sqrt X\ge q\sqrt c/3$ the error tends to zero.
Each piece of $F_c(x)/\sqrt x$ has the form
$a/\sqrt x+b\sqrt x$ with $b>0$, whose interior critical point,
if present, is a minimum. Hence the only candidates for its maximum are

$$
K_0(c)=\frac{7c+8}{4\sqrt c},\qquad
K_s(c)=\frac{7c+10}{4\sqrt{c+1}},\qquad
K_1(c)=\frac{c+14}{4}.
\tag{4}
$$

The two cycle boundaries have the common value $K_0(c)$. Since

$$
K_0'(c)=\frac{7c-8}{8c^{3/2}}>0,\qquad K_1'(c)=\frac14,
\qquad K_0(4)=K_1(4)=\frac92,
$$

no fixed $c>4$ in (1) improves the baseline upper limit. This rules out
improvement by this widened family, including its shortened bridge.

For the corresponding outer-only skeleton with fixed $c\ge8$, the
cycle count is $(4c/3)q+O(1)$. Its boundary count through $cq^2$ is
$2cq+O(k+1)$, giving the subsequential ratio $2\sqrt c>9/2$.
Adding repairs cannot lower that ratio. This conclusion concerns this
outer skeleton; it does not constrain arbitrary changes of residue sets
or scale rules.

## Lowering the radius: an incomplete split calculation

Put $c=4-\delta$. To state the local branch calculation concretely,
take $0<\delta<1$; this is not a verified parameter range for a complete
repaired construction. At scales $q\ge3$, let $x=m/q>0$ and
$\alpha=(t-m^2)/q^2$. The newly possible nonpositive branch at the
next root $2q-m$ has

$$
c<\alpha\le4-4x,\qquad 0<x<\delta/4.
\tag{5}
$$

The alternative root $q+m$ gives residual
$q^2(\alpha-2x-1)$. In the relaxed continuous parameter domain,
allowing the limiting endpoint $x=0$, the old residual ranges over
$(c,4]q^2$, and the alternative ranges over

$$
\left(\frac{3c}{2}-3,3\right]q^2.
\tag{6}
$$

Indeed, for fixed $x$ the latter interval is
$(c-2x-1,3-6x]q^2$; their union as
$0\le x<\delta/4$ has the endpoints in (6). This interval calculation
does not establish discrete realizability of every parameter pair.

Modulo $6q$, keeping the old residual uses two possible lift subclasses
$r+2q,r+4q$, whereas the alternative from $q+m$ uses the common
subclass $r+3q$. Here $r\in\{0,1,2\}$ is the target center, and
the next root is assumed to satisfy $t-(2q-m)^2\equiv r\pmod{6q}$.
These congruences follow by subtracting the displayed squares and using
$3\mid q$ and $3\nmid m$.

A proposed monotone split assigns a proportion $0\le\theta\le1$ of
the radial parameter to the common alternative repair. Its proposed
complete-cycle and prefix expressions are

$$
6q-\frac5{12}(2-\theta)\delta q+O(1),
\qquad
\frac{B(q^2)}q\ge\frac92+
\frac{2-\theta}{8}\delta+o(1).
\tag{7}
$$

The intended extremes are $\theta=0$, retaining the old residuals, and
$\theta=1$, using the common alternative. A complete definition of the
intermediate split sets, a derivation of both counts in (7), and the
admissible range for a whole construction are missing. Accordingly (7)
is a proposed ledger, not a proved bound on every smaller-radius repair.
If that ledger were established for a specified split, its second formula
would exclude an improvement by that split, despite the cycle saving.

There is a narrower completed obstruction to a simple deferral argument.
In (5),

$$
\frac{t}{q^2}=\alpha+x^2\le4-4x+x^2<4.
$$

Every positive residual $t-n^2$ is at most $t<4q^2$. Thus this branch
cannot be repaired by adding only residuals above $4q^2$. Merely
shortening the high bridge without handling (5) omits a root case.
This does not rule out repairs below the cutoff or a different multiscale
construction.

## Two parity diagnostics

If the parity of the bounded root is flipped between $q$ and $3q$,
the possible new positions in $[0,3q]$ are

$$
q-m,\qquad q+m,\qquad3q-m.
$$

With old residual $a>4q^2$, the first two give positive new residuals,
since their squared-root increments are at most $3q^2$. For the last
position, a nonpositive residual implies

$$
4q^2<a\le9q^2-6qm\le9q^2.
$$

Because $m=3q-(3q-m)$, the old residual has the correct center modulo
$3q$ but the parity opposite to that at the new scale. The direct repair
which retains this old residual therefore uses the opposite-parity bridge
$(4q^2,9q^2]$, wider than L3's $(5q^2,9q^2]$ bridge. This is a cost
diagnostic for that direct repair. Positivity alone does not establish
global coverage with changing parity, whose descending congruences need
their own consistent rule. No obstruction to arbitrary parity states is
proved.

Dropping parity gives a different restricted profile. Take the outer
skeleton $R_q\cap[q^2/9,q^2]$ at each scale $q=3^k$. Its cycle
count is $(8/3)q+O(1)$ and its boundary ratio is $4$. The specified
one-step repair retains $r+q\pmod{3q}$ for each $r=0,1,2$ on the
old-scale interval $[q^2,2q^2]$. Indeed, with least old root
$0\le m\le q/2$, the hard position is $q+m$. If the alternative
from $q-m$ is not already caught, its residual and the old residual
both lie in $(q^2,2q^2]$ and occupy the two nontrivial lift classes
$r+q,r+2q\pmod{3q}$ in some order. Retaining the specified class
handles this case. At the next scale it doubles the density on
$[q^2/9,2q^2/9]$. For this profile the two densities are
$6/q$ on $(q^2/9,2q^2/9)$ and $3/q$ on $(2q^2/9,q^2)$.
The resulting cycle count is $3q+O(1)$; earlier cycles contribute
$3q/2+O(k+1)$. At $X=2q^2/9$ the normalized prefix is therefore

$$
\frac{3q/2+(6/q)(q^2/9)+O(k+1)}{\sqrt2q/3}
\longrightarrow\frac{13}{2\sqrt2}>\frac92.
\tag{8}
$$

Thus this skeleton with this doubled-density repair cannot improve the
target. Equation (8) does not prohibit other parity-free complements.

## A conditional one-step mass bound

Retain the original parity convention and radius $4$. In L3's hard
transition, the new root is $2q+m$, its residual is nonpositive, and
both old-parity alternatives exceed $4q^2$. Set $x=m/q$ and
$\alpha=(t-m^2)/q^2$. Their exact inequalities imply

$$
\frac12<x\le1,\qquad 8-4x<\alpha\le4+4x.
\tag{9}
$$

The upper endpoint $x=1$ is a limiting endpoint at large scales. The
four old root representatives yield

$$
\begin{array}{c|c|c}
\text{root}&\text{residual divided by }q^2&
\text{residue modulo }6q\\ \hline
m&\alpha&r+2q\text{ or }r+4q\\
2q-m&\alpha-4+4x&r+4q\text{ or }r+2q\\
q-m&\alpha+2x-1&r+3q\\
q+m&\alpha-2x-1&r+q\text{ or }r+5q.
\end{array}
\tag{10}
$$

In the first two rows the subclasses occur in opposite orders. These
congruences use $t-(2q+m)^2\equiv r\pmod{6q}$,
$3\mid q$, and $3\nmid m$. In particular, the first two normalized
residuals exceed $4$, and the third lies in $(5,9]$.

Restrict the repair model as follows. For $1\le j\le5$ fix a bounded
Jordan-measurable radial set $S_j\subset(0,\infty)$, independent of
$q$ and common to all three centers. At transition $q$, select points
with $n/q^2\in S_j$ and $n\equiv r+jq\pmod{6q}$ for
$r=0,1,2$. Only the four residuals in (10) may cover the transition.
This deliberately excludes the root $3q-m$, even when its residual is
positive; the four rows are not an exhaustive list of same-transition
options. The model also excludes digit-dependent radial sets and routing
through later transitions.

If $x\to1$ and $\alpha\to y\in(4,8)$, the four radial values in
(10) tend to $y,y,y+1,y-3$. Assume the limiting coverage requirement

$$
(4,8)\subseteq
S_2\cup S_4\cup(S_3-1)\cup(S_1+3)\cup(S_5+3).
\tag{11}
$$

An inclusion outside a set of length zero would also suffice. Translation
invariance and subadditivity of length immediately give

$$
\sum_{j=1}^5|S_j|\ge4.
\tag{12}
$$

For these fixed Jordan sets, counting each residue grid is a Riemann-sum
calculation with mesh $6/q$. For sufficiently large $q$ the fifteen
residue classes are distinct, so the selected set at this transition has

$$
\frac q2\sum_{j=1}^5|S_j|+o(q)\ge2q+o(q)
\tag{13}
$$

points. For interval pieces the error is $O(1)$. The choice
$S_3=(5,9]$ and all other $S_j=\varnothing$ satisfies (11) and
attains the leading mass $2q$; this is the bridge already used by L3.

The implication from (11) to (13) is complete. Its proposed application
to every discrete one-step repair is not: no proof is supplied that each
$y\in(4,8)$ is realized by discrete hard transitions with $m/q\to1$,
or that discrete coverage forces (11), or an adequate version outside a
null set, for the claimed class of Jordan-measurable repairs. Those are
the missing limiting-realizability and discrete-to-radial justifications.
The fixed-set Riemann sum does not supply either one.

Even with (11), this bounds the selected mass at one transition, not the
upper counting limit of a global union. Moving mass changes prefixes,
and any sharing between scales needs separate accounting. Thus (13)
is neither a universal repair-cost theorem nor a proof that every
one-step repair has limsup at least $9/2$.

## Seven-adic skeleton and missing recycling lemma

The elementary center identity is

$$
\{0,1,5\}+\{1,2,4\}=\mathbb Z/7\mathbb Z.
\tag{14}
$$

Indeed the three translates are $\{1,2,4\}$, $\{2,3,5\}$ and
$\{6,0,2\}$. They cover all seven classes. Hence for each target
$t$ one can choose a center $r\in\{0,1,5\}$ so that $t-r$ is a
nonzero square modulo $7$. This is only a modular interface.

To make the counting comparison precise, take the parity-preserving
formal skeleton

$$
T_M=\{a\in\mathbb Z_{>0}:a\equiv0,1,5\pmod M\},
\qquad
\mathcal A_7=\bigcup_{q=7^k,\ k\ge0}
T_{2q}\cap[4q^2/49,4q^2].
\tag{15}
$$

This is a specified candidate skeleton, not an asserted square complement.
At large scales its cycle count is
$(3/(2q))(4q^2-4q^2/49)+O(1)=(288/49)q+O(1)$.
Summing the geometric series through scale $q$ gives

$$
\mathcal A_7(4q^2)=\frac{48}{7}q+O(k+1),\qquad
\frac{\mathcal A_7(4q^2)}{2q}\longrightarrow\frac{24}{7}.
\tag{16}
$$

Repeated classes at $q=1$ affect only the bounded initial contribution.
No coverage conclusion follows from (16).

For the chosen $r$, elementary lifting of a nonzero square root modulo
$7^k$ works because $2m$ is invertible modulo $7$. Fixing its parity
gives a bounded root $0<m_q<q$ modulo $2q$ at $q\ge7$. At the
next scale, reduction modulo $2q$ places the bounded root in

$$
\{m_q,\ 2q-m_q,\ 2q+m_q,\ 4q-m_q,\ 4q+m_q,
  6q-m_q,\ 6q+m_q\}.
\tag{17}
$$

Writing $x=m_q/q$, $\alpha=(t-m_q^2)/q^2$, and $h=m_{7q}/q$,
the exact state update is

$$
x'=\frac h7,\qquad
\alpha'=\frac{\alpha+x^2-h^2}{49}.
$$

The skeleton catches the new residual when
$4/49\le\alpha'\le4$; its congruence is already fixed by the chosen
center and root. The outstanding interface is a rule that handles these
seven lift positions over two or more scales, together with a proof that every
sufficiently large target reaches a positive retained residual. It must
also specify any added repair set $D$ and prove the all-prefix target

$$
\limsup_{X\to\infty}
\frac{|(\mathcal A_7\cup D)\cap[1,X]|}{\sqrt X}<\frac92.
\tag{18}
$$

The difference $9/2-24/7=15/14$ is only the nominal boundary margin
suggested by (16); it does not bound repair cost or control intervening
cutoffs. No multiscale routing rule, termination proof, or uniform repair
prefix estimate is supplied. The seven positions alone do not prove that
every possible one-step bridge is inadequate. Establishing the recycling
and counting lemma, or finding a precise obstruction to a specified rule,
remains the substantive missing mathematics.
