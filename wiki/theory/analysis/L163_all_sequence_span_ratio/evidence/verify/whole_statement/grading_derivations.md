---
name: theory/analysis/L163_all_sequence_span_ratio/evidence/verify/whole_statement/grading_derivations
title: "Mathematical checks supporting the ratio-report grade"
desc: |
  Mathematical checks used to grade the frozen ratio report: label transfers,
  finite-prefix discrepancy with repeated entries, and the absolute ratio
  threshold and extremal consequences.
created: 2026-10-15T20:39:29Z
updated: 2026-10-15T20:39:29Z
---

# Mathematical checks supporting the ratio-report grade

***

Examination date: 2026-10-15 UTC. These are the independent grader's checks of
the three vulnerable parts of the [unchanged report](report.md).
They support the grading judgment and do not amend either the report or its
subject. Each essential argument below is already present in that report.
The retained subject is the report's nine linked excerpts. No original paper,
unprovided theorem, numerical experiment, or computation is used.

## 1. Label transfers and absolute short-arc constants

For $n\ge r$, the cyclic gaps are nonnegative and sum to one. Summing the
$n$ lifted $r$-spans counts every gap exactly $r$ times. Consequently
$nm_n\le r\le nM_n$, including when positions coincide. In particular
$M_n>0$. The model is well-defined without assuming a distinct-point theorem.

Under (2.1), with $a_s,b_s\ge0$ and $a_s+b_s\le A$, a forward move by
$kr$ labels and the magnitude of a backward move by $kr$ labels are each
sums of $k$ consecutive $r$-spans. Their displacement bounds are
$[k(r-a_s)/s,k(r+b_s)/s]$. They are permutations of labels. Earlier labels
include injectively into later label sets even when their positions agree.
This distinguishes the needed injection from a false injection of positions.

Fix $q=E/(kr)<1$. For the upper comparison, take
$t_+=(1+q)t$, $0\le u\le E/t_+$, and
$s=t/(1-ut/(kr))$. The injection $B_sF_t$ has real displacement
$u+\eta$, with

$$
-k(a_t+A)/t\le\eta\le k(b_t+A)/t.
$$

An arc $I=(x,x+D/t]$ therefore maps into $J+u$, where $J$ enlarges $I$
by these errors and has length at most $(D+3kA)/t$. For a fixed multiset
$Q$, finite-sum integration on the circle gives exactly

$$
\int_0^\ell N_Q(J+u)\,du
=\int_J N_Q((v,v+\ell])\,dv.
$$

One proves it for one label using its integer translates and then adds labels.
Coincidence changes multiplicity, not the identity. Endpoint differences have
zero measure. With $Q=P_{t_+}$ and $\ell=E/t_+$, it gives

$$
N_t(I)\le(D+3kA)(1+q)U_{t_+}(E).
$$

For the lower comparison, set $t_-=(1-q)t$ and
$s=t/(1+ut/(kr))$ for $0\le u\le E/t_-$. The injection $F_tB_s$
from $P_{t_-}$ has displacement $-u+\eta$, with errors bounded by
$-ka_t/t-kA/t_-$ and $kb_t/t+kA/t_-$. Shrinking $I$ by those errors,
using an empty arc if the remaining length is nonpositive, gives

$$
N_t(I)\ge\bigl[D(1-q)-kA(3-q)\bigr]_+V_{t_-}(E).
$$

In both directions the left endpoint remains open. Real displacements are
composed before reducing positions modulo one, so crossing the cyclic cut
loses no full turn. Bounds on the choices $a_s,b_s$ are pointwise; neither
their measurability nor continuity is needed for integration of the fixed
multiset counts. At fixed $E,k$ and bounded $D$, all comparison times are
positive fixed multiples of $t$ and all arcs are $O(1/t)$. A single late
threshold works for all those $D$ and all starts, including $D\downarrow0$.

The terminal upper estimate also preserves ties. If an arc of length
$(r-A)/t$ contained $r+1$ labels, the first and its $r$th successor would
be separated by strictly less than this length, contrary to the lower span
bound. For the lower estimate, lift all labels into $(x-1,x]$ and take
the last label $p_0$. Its next $r$ labels are strictly beyond $x$, even if
some labels coincide at $x$ before the cyclic cut. The last lies at most
$p_0+(r+A)/t\le x+(r+A)/t$. Thus

$$
U_t(r-A)\le\frac r{r-A},\qquad
V_t(r+A)\ge\frac r{r+A}.
$$

To check that the report does not conceal a sequence-dependent constant, put
$\theta=\sqrt{A/r}$, $K=\sqrt{Ar}$, $\Lambda=\log(r/A)$ and
$\varepsilon=\theta\Lambda$. In a doubling chain from $K$ to $r\pm A$,
take $k=\lceil D/K\rceil$ at each comparison of $D$ with
$D<E\le2D$. Then $q\le2\theta$ and $kA/D\le2\theta$. For
$\theta\le1/12$, the upper and lower multipliers are bounded respectively
by $1+9\theta$ and $1-8\theta$. The number of comparisons is at most
$3\Lambda$ for the report's large-parameter regime. The resulting time
factors stay positive; there are finitely many for each fixed $r,A$.

The report's choice $C_0=e^{32}$ ensures, whenever $r/A\ge C_0$,
$\varepsilon\le1/120$, $\theta\Lambda^2\le1$, and $\Lambda\ge1$.
Indeed $u e^{-u/2}$ and $u^2e^{-u/2}$ decrease for $u\ge32$, and
$e^{16}>2^{16}$. The chain estimates give

$$
U_t(K)\le(1+2\theta^2)e^{27\varepsilon}\le1+60\varepsilon,
\qquad
V_t(K)\ge(1-\theta^2)(1-24\varepsilon)\ge1-60\varepsilon.
$$

For the first inequality, $e^z\le1+2z$ for $0\le z\le1/2$ and
$\theta^2\le\varepsilon$ leave more than the claimed slack. The second
uses the nonnegative Bernoulli bound. These estimates concern all eligible
parameter values, not finitely tested ones.

For $0<D\le S=K/\Lambda^2$, use $E=K,k=1$ in the unnormalized
comparisons. The upper estimate is
$(D+3A)(1+66\varepsilon)$. For the lower estimate let
$Q=D(1-\theta)-(3-\theta)A$. If $Q>0$, then $Q\le D$ and

$$
N_t(I)\ge Q(1-60\varepsilon)
\ge D-3A-61D\varepsilon.
$$

If $Q\le0$, then
$D\le A(3-\theta)/(1-\theta)\le3A+3A\theta$, so the zero lower
bound suffices. Both cases imply

$$
|N_t(I)-D|\le3A+200(D+A)\varepsilon
\le3A+400A/\Lambda.
$$

The last step uses $S\varepsilon=A/\Lambda$ and
$A\varepsilon\le A/\Lambda$. The $D=0$ arc is empty. Thus the absolute
constants and uniform small-$D$ claim used downstream are justified by the
report itself. This checks the complete supplied Proposition 3.1, not only
the existence of unspecified constants.

## 2. Exact extraction and the complete finite-prefix bound

Assume the integer-time count estimate for $n\ge n_0$, all starts, and
$0\le D\le S$. Put $L=\lfloor S\rfloor$ and choose $N$ large enough
that $w=L/N<1$ and $n_0w<1$. The starts of arcs $(a,a+w]$ meeting an
early position have total measure at most $n_0w$. Excluding finitely many
endpoint coincidences with the first $N$ labels still leaves a choice.
This selection is available for every sequence; it is not an exclusion of a
null class of sequences.

The selected arc contains $L'\in[L-B,L+B]$ labels at time $N$. In arrival
order, their normalized positions are in $(0,1)$, with no distinctness
condition. At the $j$th selected arrival $n=m_j$, let $C(u)$ count the
selected positions at most $u$. The errors on the two complementary arcs are

$$
f(u)=C(u)-nuw,\qquad
g(u)=j-C(u)-n(1-u)w.
$$

Their scaled lengths are at most $Nw=L\le S$, and both errors have absolute
value at most $B$. The exact identity

$$
C(u)-ju=(1-u)f(u)-ug(u)
$$

has total absolute coefficient one. It proves $H_{L'}\le B$; replacing it
by an unrelated triangle inequality with error $2B$ would destroy the
closing margin. Left limits supply strict prefix counts, and the excluded
endpoints supply the values at zero and one. The later use ensures $L'>0$.

For FP, define the strict discrepancies $D_j(x)$ and integrated range $P_N$
as in the retained report. Pointwise range splitting for the early indices
$1,\ldots,m$ and late indices $3m+1,\ldots,4m$ yields half of each
within-block range plus half of each absolute difference of block maxima and
minima. Let those two differences be $f$ and $g$.

Between coordinates of the list, active discrepancies are affine with slope
$-j$, and hence $2m+1\le-f',-g'\le4m-1$ almost everywhere. Changes of
active indices create continuous corners; finitely many affine pieces suffice.
At a coordinate $v$ with early, middle, late multiplicities $q_0,q_1,q_2$,
every late discrepancy jumps by at least $q_0+q_1$ and every early one by
at most $q_0$. The maximum or minimum of functions whose increments lie in
$[a,b]$ also increments by an amount in $[a,b]$. Therefore each of $f,g$
jumps by at least $q_1$. This argument explicitly allows active indices to
change at the same coordinate as the collision.

For either function, write its jump as $h(v)\ge q_1(v)\ge0$ and use
$F(s)=s|s|/2$, with $F'(s)=|s|$. The values at zero and one are zero
under the strict convention; the right jump at zero must be included. Summing
the piecewise chain rule gives

$$
\int_0^1 |f|(-f')\,dx
=\sum_v\int_{f(v)}^{f(v)+h(v)} |s|\,ds
\ge\frac14\sum_v h(v)^2
\ge\frac14\sum_v q_1(v)=\frac m2.
$$

The interval centered at zero minimizes the integral of $|s|$ for a given
length $h$, with value $h^2/4$; negative-to-positive crossings are therefore
covered. Integer multiplicity gives $q_1^2\ge q_1$. Since $-f'<4m$
almost everywhere, this proves $\int|f|\ge1/8$, and likewise for $g$.
The late block's common offset $D_{3m}$ cancels from its internal range.
Thus

$$
P_{4m}\ge\tfrac12P_m(\text{early})+\tfrac12P_m(\text{late})+\tfrac18.
$$

Starting with $P_1=0$, ordinary induction gives $P_{4^h}\ge h/8$ for
every list. Since $P_N\le2H_N$, and the prefixes of the initial
$4^{\lfloor\log_4 L\rfloor}$ entries are among those defining $H_L$,

$$
H_L\ge\frac{\lfloor\log_4L\rfloor}{16}
\ge\frac{\log L}{16\log4}-\frac1{16}
\quad(L\ge1).
$$

This verifies the full finite-prefix proof, including $1\le L<4$, rounding,
all coincident entries, and the endpoints. It consumes neither the unprovided
Theorem 4.1 nor its stronger constant.

The strongest endpoint diagnostic is the report's exact family
$z_1=\cdots=z_{4m}=0$. On $0<x\le1$, both functions are
$3m(1-x)$; at zero both equal zero. The jump is $3m$ and
$\int|f|(-f')=9m^2/2$. Omitting the initial jump would make the right side
of the identity zero. The frozen proof and report include it. Coalescing only
middle entries also cannot break the inequality: a multiplicity $q$ has at
least the contribution $q^2/4\ge q/4$. The diagnostic has a concrete failure
mode; it is not offered as a finite verification of the universal result.

## 3. Absolute ratio threshold and the exact extremal consequences

Fix $r$, $A=(\log r)/200$, and a sequence strictly violating the claimed
limsup bound. Every finite ratio is at least one, so some $0<C<A$ makes
$M_n/m_n\le1+C/r$ eventually. Minima are then positive. The mean identity
gives

$$
n(M_n-m_n)\le C,\qquad nM_n\le r+C.
$$

For $n=\lfloor t\rfloor$, choose
$a_t=r-nm_n$ and $b_t=tM_n-r$. They are nonnegative, the resulting lower
endpoint is $nm_n/t\le m_n$, and the upper endpoint is exactly $M_n$.
Their sum is bounded by $C+(r+C)/n<A$ eventually. The strict margin controls
only a finite time threshold for this sequence; it is not assumed uniform.

For all large $r$, the absolute restrictions of Proposition 3.1 hold. With
$\alpha=1/200$, $u=\log r$, and the report's $S,B,\Lambda$,

$$
\Lambda=u-\log u-\log\alpha,\qquad
B=3\alpha u+O(1),\qquad
\log S=\tfrac12u-\tfrac32\log u+O(1).
$$

All constants here depend only on the fixed $\alpha,C_0,C_1$. In particular
$S/u\to\infty$, so $\lfloor S\rfloor-B\ge S/2>0$ eventually. The
extraction may choose $N$ beyond any finite sequence-dependent threshold.
It produces an actual list with $L'\ge S/2$ and $H_{L'}\le B$.

FP then requires

$$
3\alpha u+O(1)\ge\frac{u}{32\log4}
-\frac{3\log u}{32\log4}-O(1).
$$

The coefficients satisfy the exact comparisons
$3/200<1/64<1/(32\log4)$, the first by $192<200$ and the second by
$\log4<2$. The positive linear margin eventually exceeds the logarithmic
and bounded errors. One absolute $r_0$ therefore excludes every failing
sequence, while allowing sequence-dependent times. No interchange of those
quantifiers has occurred. Infinite limsup ratios satisfy the bound directly.

Finally fix any integer $r\ge r_0$. Each extended-real number in
$\{\limsup_n M_n^{(r)}/m_n^{(r)}:X\}$ is at least
$1+\log r/(200r)$. The class is nonempty. Its infimum has the same lower
bound, whether or not it is finite or attained. Subtracting one and multiplying
by positive $r$ gives $r(\mu_r-1)\ge\log r/200$; comparison with every
fixed real bound proves divergence through the integers. Separate extrema of
$M_n$ and $m_n$ are never substituted. This is the claimed consequence in
ratio units, not an assertion of an exact optimal coefficient.

The frozen report contains all three derivations and their composition. None
of these grading checks fills a missing required report part. The resulting
mathematical assessment remains **refutation-failed** on the assigned scope.
Korsky's cited source remains unrefereed and unread as an original paper;
Larcher's range-splitting attribution and Plasma AI's credit for the local
mathematics are preserved in the retained report and provenance input.
