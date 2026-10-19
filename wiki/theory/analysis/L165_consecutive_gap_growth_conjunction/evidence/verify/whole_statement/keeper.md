---
name: theory/analysis/L165_consecutive_gap_growth_conjunction/evidence/verify/whole_statement/keeper
title: Independent derivations for the consecutive-gap conjunction
desc: Independent analytic attacks on the span conventions, limiting extrema, and formulation transfer in L165.
tags: []
sources: []
created: 2026-10-15T23:40:25Z
updated: 2026-10-15T23:40:25Z
---

# Independent derivations for the consecutive-gap conjunction

***

Mathematical examination and independent derivations: Plasma AI.
Examination date: 2026-10-15 UTC.

Read depth: the complete selected L165 statement, conventions and proof; the
complete supplied L163 and L164 statement/convention interfaces; their selected
standing metadata; and the supplied E1221 formulation text. The premise proofs
and original publications are outside this examination. The
[report](report.md) states the dependency reading and verdict. The exact
[claim](../../assets/whole_statement_subject/claim.md.txt),
[proof](../../assets/whole_statement_subject/proof.md.txt),
[premises](../../assets/whole_statement_subject/premises.md.txt), and
[catalog formulation](../../assets/whole_statement_subject/catalog.md.txt)
are retained for reconstruction.

This is analytic evidence. None of the examples below is used to infer a
universal asymptotic claim from finitely many cases. The universal inputs are
precisely the two premise interfaces; the deductions and attacks below are
independent checks of their composition. No executable mathematical check is
needed to reproduce these finite identities and arguments.

## 1. Object convention and its extreme cases

Fix positive integers $r\le n$. List the first $n$ labeled points in cyclic
order, using arrival order to break a position tie. Choose their ordered real
lifts within one turn and extend by $y_{i+n}=y_i+1$. Put

$$
g_i=y_{i+1}-y_i,\qquad
s_i=\sum_{j=0}^{r-1}g_{i+j}=y_{i+r}-y_i.
$$

The $g_i$ are nonnegative, periodic with period $n$, and sum to $1$ over
one period. This includes the closing gap: replacing all lifts by their
residues before subtraction would lose it. For a fixed gap index $k$ and each
$j\in\{0,\ldots,r-1\}$ there is exactly one start $i$ modulo $n$ for which
$i+j=k$. Hence, counting multiplicities,

$$
\sum_{i=1}^n s_i
=\sum_{j=0}^{r-1}\sum_{i=1}^n g_{i+j}
=r.
$$

Consequently the minimum and maximum of these $n$ spans satisfy

$$
0\le m_n^{(r)}\le\frac rn\le M_n^{(r)}\le1.
$$

In particular $M_n^{(r)}>0$, so the specified infinite ratio at zero minimum
never involves $0/0$. The last bound follows because at most one complete
period of nonnegative gaps is summed. Nothing here removes a zero gap or
identifies two starting labels.

Changing the circular cut cyclically permutes the spans. Changing the names of
labels at the same position does not change their position list; the prescribed
tie rule also fixes their order. Thus the extrema are well-defined under the
stated convention.

At $n=r$, every span is exactly $1$. Both scaled deviations are zero and the
ratio is $1$. This would refute a positive bound at every $n\ge r$, but the
claim is about limits as $n$ tends to infinity for fixed $r$. The single prefix
$n=r$ has no bearing on those limits. It also exposes an invalid convention
change: the shortest circle distance between the identical endpoint residues
would be zero, whereas the lifted span is a complete turn.

For a sequence whose every term is the same point, and $n>r$, the gap list has
one gap $1$ and $n-1$ gaps $0$. Exactly $r$ of the $n$ spans equal $1$; the
others equal $0$. Thus

$$
M_n^{(r)}=1,\quad m_n^{(r)}=0,\quad
nM_n^{(r)}-r=n-r,\quad r-nm_n^{(r)}=r,
\quad M_n^{(r)}/m_n^{(r)}=+\infty.
$$

This admissible repeated-point sequence does not invalidate the conjunction.
For every fixed positive $c$, $c\sqrt{\log r}\le r$ for all sufficiently
large $r$, so it does not contradict the lower-deviation assertion either.
The check does not claim that every repeated-point sequence behaves this way.

## 2. A nested uniform-grid attack and finite extrema

Define a single infinite sequence of distinct points as follows. Start with
$0$. Once the points $j/2^k$, $0\le j<2^k$, have been inserted, append in
increasing order all their gap midpoints

$$
\frac{2j+1}{2^{k+1}},\qquad 0\le j<2^k.
$$

Every stage is finite; the next stage completes the next finer grid. Newly
inserted odd dyadic fractions have not occurred at an earlier stage, so this
defines an element of the distinct-point family without any unproved existence
claim.

Write $N=2^k$. At every prefix $N\le n<2N$ all gaps have length either
$1/N$ or $1/(2N)$. For any $r\le n$ it follows directly that

$$
\frac{r}{2N}\le m_n^{(r)}\le M_n^{(r)}\le\frac rN,
\qquad nm_n^{(r)}\ge\frac r2,
\qquad nM_n^{(r)}<2r,
\qquad \frac{M_n^{(r)}}{m_n^{(r)}}\le2.
$$

These inequalities hold at every prefix, with its appropriate $N$. Therefore
both sequence families are nonempty and, for each positive integer $r$,

$$
r\le\Lambda_r^{\mathcal F}\le2r,\qquad
\frac r2\le\lambda_r^{\mathcal F}\le r,\qquad
1\le\mu_r^{\mathcal F}\le2,
\qquad \mathcal F\in\{\mathcal A,\mathcal D\}.
$$

The witness establishes finiteness if the outer extrema are understood as real
numbers. Individual sequence limsups may still be infinite, as in Section 1;
the proof's limit manipulations are valid for those too. These auxiliary bounds
are a well-definedness check, not an optimality claim and not a replacement for
either native premise.

At the complete-grid prefixes $n=N\ge r$, every $r$-span is $r/N$.
Thus both deviations vanish and the ratio is $1$ along infinitely many
prefixes of this one infinite sequence. This is a concrete attempted
counterexample to an incorrectly strengthened all-prefix or liminf claim.

To check whether it attacks the actual limsups, inspect $n=3N/2$, after the
first $N/2$ midpoints have been inserted, taking $N\ge2r$. The first half of
the circle contains a run of $N$ gaps of length $1/(2N)$; the second half
contains a run of $N/2$ gaps of length $1/N$. Each run contains $r$
consecutive gaps. Therefore

$$
M_{3N/2}^{(r)}=\frac rN,\qquad
m_{3N/2}^{(r)}=\frac{r}{2N},
$$

and at these infinitely many prefixes

$$
nM_n^{(r)}-r=\frac r2,\qquad
r-nm_n^{(r)}=\frac r4,\qquad
M_n^{(r)}/m_n^{(r)}=2.
$$

For this example the liminf of each deviation is zero and the liminf ratio is
one; the respective limsups are at least $r/2$, at least $r/4$, and exactly
two. No monotonicity in $n$ can be assumed. The attempt fails against L165
because its limit directions are precisely the ones that retain the
intermediate-prefix excursions. No inference about other sequences follows
from this example.

## 3. Exact premise composition

Write L163's supplied universal interface as

$$
(R):\quad \exists r_R\ \forall r\ge r_R\ \forall X\in\mathcal A,
\quad\limsup_n\frac{M_n^{(r)}}{m_n^{(r)}}
\ge1+\frac{\log r}{200r}.
$$

L164 supplies one $c$ and one threshold for both inequalities:

$$
(O):\quad \exists c>0\ \exists r_O\ \forall r\ge r_O\
\forall X\in\mathcal A,\quad
\begin{cases}
\limsup_n(nM_n^{(r)}-r)\ge c\sqrt{\log r},\\
\limsup_n(r-nm_n^{(r)})\ge c\sqrt{\log r}.
\end{cases}
$$

All displayed $r$ and $n$ are integers in the positive range, and the limits
use $n\ge r$. Here $(R)$ is L163 and $(O)$ is L164; their proofs are not
claimed as part of this derivation. Their supplied conventions agree on every
object used here, including repetitions, tie order, lifted forward spans and
natural logarithms. The counting-arc convention in those interfaces is not an
additional counting lemma consumed by this composition.

Increase the supplied thresholds to at least $2$ if necessary, which only
restricts the eventual range, and choose $r_0=\max(r_R,r_O)$. The constant
$c$ is the one in $(O)$. This gives one pair of absolute constants valid for
both families and all their members. An onset time for approaching a limsup
may depend on $X$ and $r$; no common onset time is asserted.

The conjunction is a conjunction of three statements about limsups. It is not a
limsup of a conjunction, minimum, or vector assertion. For example, the scalar
sequences $a\mathbf1_{n\text{ even}}$ and
$a\mathbf1_{n\text{ odd}}$, with $a>0$, both have limsup $a$ although their
pointwise minimum is always zero. These are a diagnostic for a false
common-subsequence inference, not proposed circle-span sequences. L165 makes
no such inference.

The ratio bound is an essential independent input. From a deviation of size
$a=c\sqrt{\log r}$ and the mean inequality alone, one would obtain bounds
such as $1+a/r$ or $r/(r-a)$, when the latter is defined. These are only of
order $1+\sqrt{\log r}/r$, not the claimed logarithmic improvement. The
proof actually invokes $(R)$ for that improvement; it does not derive it by
combining unrelated extrema or different times from $(O)$.

## 4. Tail identities, outer extrema, and adversarial optimization

Fix $r\ge r_0$, and abbreviate

$$
a=c\sqrt{\log r},\quad b=\frac{\log r}{200},\quad
u_n=nM_n^{(r)},\quad v_n=nm_n^{(r)},\quad
q_n=\frac{M_n^{(r)}}{m_n^{(r)}}.
$$

Then $u_n\ge r$, $0\le v_n\le r$, and $1\le q_n\le+\infty$.
For every sufficiently large integer $K$, the exact tail identities are

$$
\sup_{n\ge K}(u_n-r)=\sup_{n\ge K}u_n-r,
\qquad
\sup_{n\ge K}(r-v_n)=r-\inf_{n\ge K}v_n.
$$

Taking limits of tails gives

$$
\limsup_n(u_n-r)=\limsup_n u_n-r,
\qquad
\limsup_n(r-v_n)=r-\liminf_n v_n.
$$

The second identity is between finite bounded quantities. The first remains
valid when the limsup is positive infinity because the subtracted number $r$
is finite; there is no subtraction of two infinite quantities.

For each $X\in\mathcal A$ define its three limiting values

$$
U_X=\limsup_n u_n,\qquad V_X=\liminf_n v_n,\qquad
Q_X=\limsup_n q_n.
$$

The premise interfaces and the tail identities imply, pointwise in $X$,

$$
U_X\ge r+a,\qquad V_X\le r-a,\qquad Q_X\ge1+b/r.
$$

For any nonempty family $\mathcal F\subseteq\mathcal A$, every member of
the first set of values is at least $r+a$, every member of the second is at
most $r-a$, and every member of the third is at least $1+b/r$. By the
defining order properties of infimum and supremum, respectively,

$$
\inf_{X\in\mathcal F}U_X\ge r+a,\qquad
\sup_{X\in\mathcal F}V_X\le r-a,\qquad
\inf_{X\in\mathcal F}Q_X\ge1+b/r.
$$

No member attaining an extremum is selected. In particular, taking approximate
optimizers separately for every $r$ cannot evade a bound that already holds
for every sequence at that fixed $r$. An extremum strictly below its asserted
lower bound would require a member below that bound; a supremum strictly above
its asserted upper bound would require a member above that bound.

The most threatening attempted invalidation was to let the chosen sequence
have arbitrarily late excursions, thereby making every finite observation
look better. The following exact scalar diagnostic shows what this could break.
For positive integers $k$ set

$$
f_k(n)=\begin{cases}0&n<k,\\a&n\ge k.\end{cases}
$$

Then $\inf_k\limsup_n f_k(n)=a$, but
$\limsup_n\inf_k f_k(n)=0$. Likewise, if $0<a\le r$ and
$h_k(n)=r-f_k(n)$, then
$\sup_k\liminf_n h_k(n)=r-a$, whereas
$\liminf_n\sup_k h_k(n)=r$. These numerical families are not asserted to
be realizable by circle sequences. They isolate exactly the invalid exchange
that would make the attack work. L165 retains the outer extrema after the
limits, so it uses the first expression in each comparison. The direct order
argument above rules out this failure even for realizable delayed families.

The same reasoning handles nonattainment: values can approach a bound strictly
from one side without crossing it, but their infimum or supremum cannot cross
it either. There is no ratio of separately optimized numerator and denominator
anywhere in the inference; $Q_X$ is formed from the actual paired spans of
one sequence before its infimum is taken.

## 5. Subclass restriction and divergence

For the nonempty subclass $\mathcal D\subseteq\mathcal A$, restriction
can only increase an infimum and decrease a supremum. Applied separately to
$U_X,V_X,Q_X$, this yields exactly

$$
\Lambda_r^{\mathcal D}\ge\Lambda_r^{\mathcal A},\qquad
\lambda_r^{\mathcal D}\le\lambda_r^{\mathcal A},\qquad
\mu_r^{\mathcal D}\ge\mu_r^{\mathcal A}.
$$

The second sign reverses once more upon subtracting from $r$, so all three
claimed deviations are bounded below for the subclass as well. A reversed
infimum/supremum sign would be fatal; none occurs. This argument establishes
inequalities only and does not establish equality of the two families' extrema.

All quantities here use a fixed $r$ until the final step. For any real target
$T>0$, all integers $r$ larger than $r_0$ and sufficiently larger than both
$\exp((T/c)^2)$ and $\exp(200T)$ satisfy $a>T$ and $b>T$. The three
extremal deviations therefore exceed $T$ for every such $r$ in either
family. This proves divergence to positive infinity through the integers. No
monotonicity of the extrema in $r$, no interchange of limits in $r$ and $n$,
and no fixed optimizing sequence across different $r$ are needed.

## 6. Transfer to exactly the supplied formulation

In the supplied E1221 modified Statement together with its Notes, the circle
has circumference $1$, the first $n$ terms are cyclically ordered, and the
observable is a forward span of $r$ consecutive gaps. The Notes identify the
displayed maximum and minimum as the largest and smallest such spans. This
specifies extrema over the $n$ starting labels, despite the displayed
$\max_r$ and $\min_r$ subscripts. The phrase concerning consecutive points
is resolved by the supplied $r$-gap convention, not by changing it to an
$(r-1)$-gap or shortest-distance convention.

The outer family is all infinite sequences, with no distinctness restriction.
Repeated points remain labeled, giving zero gaps when appropriate; the same
cyclic sum is retained. Therefore, under the supplied conventions, each of its
three limiting functionals and each outer extremum agrees with the
$\mathcal A$ version above. The requested expressions are

$$
\Lambda_r-r,\qquad r-\lambda_r,\qquad r(\mu_r-1),
$$

exactly those bounded in Sections 4 and 5. In mean-normalized notation the first
two are $r(\Lambda_r/r-1)$ and $r(1-\lambda_r/r)$. They are not the
printed $r(\Lambda_r-1)$ and $r(1-\lambda_r)$.

This comparison needs no theorem or claim about the cited publications. It
establishes correspondence with the supplied modified mathematical question
only. It does not establish that this is the wording, intended normalization,
scope, or historical interpretation of an original publication. The historical
inequalities, quotations, bibliographic claims and source-credit assertions
within the catalog snapshot are not premises of this deduction and were not
independently certified.

## 7. Reconstruction and limits

To reproduce this analytic examination from an ordinary clone containing the
filed package, read the four linked mathematical snapshots and the selected
dependency records identified by the report. Recompute the cyclic double sum
in Section 1 and the two types of dyadic prefixes in Section 2. Check every
quantifier in the two interfaces of Section 3, derive the two exact tail
identities of Section 4, and then apply the defining order properties of
infimum and supremum. Finally compare the catalog's modified Statement and
Notes term by term with Section 6. The separate report gives the complete
checklist and current-at-examination premise standing.

The dyadic sequence, constant repeated sequence, and scalar diagnostic families
are specified in full in this file; no private data or numerical output is
needed. The scalar diagnostics disprove particular invalid inference rules,
not L165. The derivation establishes the conjunction from the two native
interfaces, without re-proving them, improving their constants, establishing
optimality or attainment, equating sequence-family extrema, or performing any
kernel or historical-source fidelity audit.
