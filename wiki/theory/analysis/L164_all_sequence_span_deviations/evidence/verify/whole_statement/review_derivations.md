---
name: theory/analysis/L164_all_sequence_span_deviations/evidence/verify/whole_statement/review_derivations
title: "Independent derivations for the one-sided bounds"
desc: Independent derivations and exact attempted refutations of the supplied one-sided circle discrepancy argument.
created: 2026-10-15T20:39:29Z
updated: 2026-10-15T20:39:29Z
---

# Independent derivations for the one-sided bounds

***

Examination date: 2026-10-15. Reading: all supplied mathematical extracts,
including their complete proofs, as identified in [the report](report.md).
The reasoning below assesses those frozen extracts. No external proof,
computation, earlier verdict, or corrected author text is a premise.

The three sections correspond to the three weakest-step rederivations in the
report. They include the surrounding deductions needed to check composition.

## 1. Label transport, signed error, and the continuum of scales

### The model and an attempted hypothesis substitution

Represent the prefix at real time $t$ by its label set
$Q_t=\{1,\ldots,\lfloor t\rfloor\}$ and its position map into
$\mathbb T$. An inclusion $Q_t\subseteq Q_s$ preserves labels, whether or not
their positions coincide. Counts are sums of position indicators over labels.
At a fixed integer time $n$, let the cyclic gaps be $g_i\ge0$, with
$\sum_i g_i=1$. The lifted $r$-span is

$$
S_i=\sum_{j=0}^{r-1}g_{i+j}.
$$

For $n\ge r$, each gap occurs $r$ times in the sum of all $n$ spans, giving
$\sum_i S_i=r$. This is an identity for labels, including zero gaps.

Here are exact witnesses against importing the two-sided hypothesis of Lemma
2.1 with the same constant as a one-sided hypothesis. Take any integer $r\ge2$
and $n=r^2+r$.

* For the upper-span alternative, take $r$ consecutive gaps equal to zero
  and the other $r^2$ gaps equal to $1/r^2$. Then
  $M=1/r$, $m=0$, $nM-r=1$, and $r-nm=r$.
* For the lower-span alternative, take
  $g_1=(r+n-1)/(nr)$ and $g_i=(r-1)/(nr)$ for $2\le i\le n$.
  Their sum is one and they are positive. A span avoiding $g_1$ has
  length $(r-1)/n$; a span containing it has length
  $r/n+(n-r)/(nr)$. Thus $r-nm=1$ and $nM-r=r$.

These configurations satisfy the respective one-sided inequality with $A=1$
at that time, while the two nonnegative errors in (2.1) would have to sum to
at least $r+1$. They are finite interface witnesses, not infinite sequences
satisfying a contrary eventual hypothesis. They invalidate the proposed
substitution of hypotheses, not the submitted proof: Lemma 6.2 reuses the
walk, and obtains its error from Lemma 6.1 rather than from (2.1).

To make the witnesses concrete as points, start at zero and place the next
label at each successive partial sum of the specified gaps, modulo one.
All the displayed maxima and minima follow by counting how many nonzero gaps,
or whether the exceptional gap, occur among $r$ consecutive gaps. This is a
symbolic check for every $r\ge2$, not a finite numerical sample.

If $r>n$, the periodic lift instead gives, for $r=qn+s$, $0\le s<n$,

$$
y_{i+r}-y_i=q+y_{i+s}-y_i.
$$

Such a span can exceed one; replacing it by the ordinary shorter circular
distance would be wrong. No assigned one-sided deduction makes that
replacement. Every walk or span estimate is used after
$\lfloor t\rfloor>kr\ge r$, and Lemma 6.3 after $\lfloor t\rfloor>r$.
The early prefixes in Lemma 7.2 involve counts only. The empty prefix has
$N_0(I)=0$, directly from counting the first zero labels; it invokes no
span estimate at $n=0$ or $n<r$.

### The two walks of Lemma 2.1

Write $L_t(p)$ for the lifted forward displacement by $kr$ places and let
$F_t$ be that permutation of labels. The backward permutation $B_t$ is its
inverse. A forward displacement followed by a backward displacement is
interpreted on compatible real lifts: the ending real lift is obtained by
adding the first displacement and subtracting the second. Its position
modulo one is the label's actual position. This remains true when a move
starts and ends at the same position with a displacement of a full turn.

For $t_+=(1+q)t$, $q=E/(kr)<1$, and $\ell=E/t_+$, define
$s=t/(1-ut/(kr))$ for $0\le u\le\ell$. Then $t\le s\le t_+$ and
$kr/t-kr/s=u$. The map

$$
Q_t\xrightarrow{F_t}Q_t\hookrightarrow Q_s
\xrightarrow{B_s}Q_s\hookrightarrow Q_{t_+}
$$

is injective on labels. For $p''=B_s(F_t(p))$, its net displacement is

$$
L_t(p)-L_s(p'')
=u+\left(L_t(p)-\frac{kr}{t}\right)
-\left(L_s(p'')-\frac{kr}{s}\right).
\tag{D1}
$$

Under Lemma 2.1's own hypothesis (2.1), the displacement minus $u$ lies
between $-k(a_t+A)/t$ and $k(b_t+A)/t$. Enlarging an arc
$I=(x,x+D/t]$ by those left and right amounts gives an arc $J$ of length
at most $(D+3kA)/t$. The strict left endpoint of $I$ ensures that an image
cannot accidentally land on the excluded left endpoint of $J+u$.
Injectivity therefore gives $N_t(I)\le N_{t_+}(J+u)$ for every $u$.

For any fixed arc $J$ and any finite label measure, translation invariance
and the substitution $v=y-u$, performed separately for each atom, give

$$
\int_0^\ell N(J+u)\,du
=\int_J N((v,v+\ell])\,dv.
\tag{D2}
$$

Endpoint differences have zero integration measure. The identity is on the
circle, so it also covers an arc crossing the chosen origin. Since a length
$\ell$ arc at time $t_+$ has at most $E U_{t_+}(E)$ labels, dividing the
integrated inequality by $D\ell$ gives exactly (2.2).

For the reverse comparison, put $t_-=(1-q)t$, $\ell=E/t_-$ and
$s=t/(1+ut/(kr))$. Now $t_-\le s\le t$ and $kr/s-kr/t=u$.
The injection is

$$
Q_{t_-}\hookrightarrow Q_s\xrightarrow{B_s}Q_s
\hookrightarrow Q_t\xrightarrow{F_t}Q_t.
$$

Its displacement minus $-u$ is bounded below by
$-ka_t/t-kA/t_-$ and above by $kb_t/t+kA/t_-$. Shrink $I$ by those
amounts to obtain $J$, or the empty arc if its length is not positive.
An input label in $J+u$ maps into $I$, including the half-open endpoints
in the indicated direction. Applying (D2) and the lower count bound gives

$$
\frac{N_t(I)}D\ge\frac{t_-|J|}{D}V_{t_-}(E)
\ge\left(1-q-\frac{kA}{D}(3-q)\right)_+V_{t_-}(E).
$$

Taking the infimum proves (2.3). If the displayed coefficient vanishes,
the conclusion is just nonnegativity of a count. No positivity of a span
was used. For bounded $D$, a single sufficiently large $t$ makes all
comparison times late, ensures $kr<\lfloor t_-\rfloor$, and makes the
enlarged arcs shorter than one. This proves the assigned uniformity clause
of Lemma 2.1 under its own hypothesis.

### Lemma 6.1 supplies the different error actually needed

Let $d_i=S_i-r/n$. Since $\sum_i d_i=0$, the total positive mass equals
the total negative mass. Under $nM-r\le A$, each $d_i\le A/n$, so the
positive mass is at most $A$. Under $r-nm\le A$, each $d_i\ge-A/n$, so
the negative mass is at most $A$. Either fixed alternative therefore gives

$$
\sum_i|S_i-r/n|\le2A.
\tag{D3}
$$

For $n=\lfloor t\rfloor$, changing the center to $r/t$ adds at most
$r(t-n)/t$ to this sum. A $kr$-span is a sum of $k$ successive
$r$-spans, and each $r$-span occurs $k$ times when all starting labels
are summed. Thus

$$
\sum_{p\in Q_t}|L_t(p)-kr/t|
\le2kA+\frac{kr(t-n)}t
\le2kA+\frac{kr}t.
\tag{D4}
$$

The label argument proves this even when the cyclic shifts have common
divisors, because occurrences are counted for each shift separately.
The onset condition uses only the integer parts of the comparison times.

Apply (D4) to the two error terms in (D1). The second is summed over an
injective image in $Q_s$, so its absolute sum is no larger than the full
sum at $s$. Since $s\ge t$,

$$
\sum_{p\in Q_t}|\eta_u(p)|\le4kA+2kr/t.
\tag{D5}
$$

This derivation explicitly avoids the false hypothesis substitution exposed
by the gap witnesses above.

### Lemma 6.2 and real-time centering

For an arc of length $d<1$, translating one atom by a real displacement
$\eta$ changes the indicator, regarded as a function of the arc's starting
point, on a set of measure at most $2|\eta|$. One can use the shorter
representative of $\eta$ modulo one, whose magnitude is at most
$|\eta|$; the bound also follows by moving the two endpoints. Consequently
(D5) gives an integrated counting error at most $8kA+4kr/t$ for the walk.

Average the resulting count inequality over $0\le u\le E/t_+$ and use
(D2). After subtracting $D$, the constant term is $qD$, not zero:

$$
\Delta_t(x,D)\le qD+
\frac{1}{\ell}\int_{(x,x+D/t]}\Delta_{t_+}(v,E)\,dv+R(x),
\qquad \int R\le8kA+4kr/t.
$$

Here $R\ge0$. Taking positive parts and integrating, the middle term
contributes at most $(D/t)/\ell$ times $Z_{t_+}(E)$. This gives

$$
Z_t(D)\le\frac{(1+q)D}{E}Z_{t_+}(E)+qD+8kA+4kr/t.
\tag{D6}
$$

No mean-zero assertion was made at a noninteger time. The transports are
measurable in $u$: on this compact time interval only finitely many integer
prefixes occur, and between changes their label permutations are fixed.
The integrations are of bounded functions and finite sums, so their
interchanges introduce no convergence hypothesis. For fixed $E,k,r,A$ the
only new dependence on $D$ in the onset condition is $D/t<1$.

### Lemma 6.3, zero spans, and full turns

Fix $n=\lfloor t\rfloor>r$ and a point $x$ not at a label position. On the
periodic real lift, let $j$ be the last index with $y_j<x$. Then

$$
y_{i-r}<x\le y_i
\quad\Longleftrightarrow\quad j+1\le i\le j+r.
$$

There are exactly $r$ such indices. Grouping them by their labels modulo
$n$ proves the $r$-fold covering identity, including spans of length zero
and one. For an extreme check, if all $n$ labels coincide, precisely $r$
ending span arcs have length one and the others have length zero. The
covering multiplicity away from that position is still $r$.

Both the fixed-length arc $(y_i-r/t,y_i]$ and the ending span arc have the
same right endpoint and lengths in $[0,1]$. They are nested as measured
arcs, including the empty and full-circle cases. The measure of their
symmetric difference is exactly $|S_{i-r}-r/t|$. Pairing their indicators
therefore yields

$$
\int|\Delta_t(x,r)|\,dx\le2A+\frac{r(t-n)}t.
$$

The mean of $\Delta_t(x,r)$ is $nr/t-r=-r(t-n)/t$. Using
$f_+=(|f|+f)/2$ cancels this floor error exactly and proves $Z_t(r)\le A$.
Replacing the real-time mean by zero would lose this cancellation, but the
submitted proof does not do so.

Full turns can alternatively be excluded at the relevant late times. Under
the upper alternative every span is at most $(r+A)/n<1$ once $n>r+A$.
Under the lower alternative with $r>A$ and $n\ge2r$, a full-turn span
would leave at least $r$ consecutive zero gaps in its complement and hence
a zero $r$-span, contrary to $m\ge(r-A)/n>0$. Neither argument is needed
to make the extended covering identity valid. There is no division by $m$
in either one-sided proof.

### Explicit absolute constants in Proposition 6.4

This verifies the existential constants without assuming a uniformity claim
from finitely many values. The choices below are deliberately loose witnesses
for the supplied estimates, not alterations of the frozen subject.

Take $C_2=e^{20}$. Put

$$
\Lambda=\log(r/A)\ge20,\qquad
\theta=e^{-\Lambda/2}=\sqrt{A/r},\qquad K=\sqrt{Ar}.
$$

In the scale chain from $K$ to $r$, the number $h$ of comparisons obeys
$h\le\Lambda/(2\log2)+1\le2\Lambda$. For adjacent scales $D<E\le2D$
choose $k=\lceil D/K\rceil$. Then $q\le2\theta$ and $kA/D\le2\theta$.
Dividing (D6) by $D$ gives the recurrence

$$
z_t(D)\le(1+18\theta)z_{(1+q)t}(E)
+18\theta+\frac{8r}{Kt}.
\tag{D7}
$$

The product of all recurrence coefficients is less than three. Indeed,
$18h\theta\le36\Lambda e^{-\Lambda/2}$, which decreases for
$\Lambda\ge20$, and its value at twenty is $720e^{-10}<1$ since $e>2$.
Thus $(1+18\theta)^h\le e^{18h\theta}<e<3$.

All comparison times are at least the starting time $t$. Iterating (D7)
from the terminal value $z(r)\le A/r=\theta^2$ gives

$$
z_t(K)\le3\theta^2+54h\theta+\frac{24hr}{Kt}
\le111\theta\Lambda+\frac{24hr}{Kt}.
$$

For fixed $r,A$ the last term is at most $\theta\Lambda$ at all
sufficiently large $t$. The finitely many applications of (D6) and the
terminal bound are also then valid. Hence $C'=112$ is admissible in (6.9).

For the final descent use $E=K$, $k=1$, $q=\theta$. For
$0<D\le S=K/\Lambda^2$, (D6) now gives

$$
Z_t(D)\le8A+225D\theta\Lambda+4r/t
\le233A+4r/t,
$$

because $D\theta\Lambda\le A/\Lambda\le A$. At integers $n$ with
$4r/n\le A$, the mean of $\Delta_n(x,D)$ is exactly zero, so

$$
\int|\Delta_n(x,D)|\,dx=2Z_n(D)\le468A.
\tag{D8}
$$

Thus $C_3=468$ works with the above $C_2$. The scale chain and its onset
threshold are independent of the final $D$. In the descent, the maps,
error bounds and comparison times are also independent of $D$; requiring
$n>S$ handles all its arc lengths simultaneously. The case $D=0$ is the
empty arc. This is an all-$D$ conclusion at one late time, not an exchange
of a supremum with separately chosen thresholds.

## 2. The complete planar bound and the boundary-point attack

For a dyadic interval $I=[a,a+\ell)$, direct integration of the two
halves with signs $-1,+1$ gives

$$
\int xh_I(x)\,dx=\ell^2/4,
\qquad
\psi_I(q)=\int\mathbf1[q<x]h_I(x)\,dx
=\begin{cases}
q-a& a<q\le a+\ell/2,\\
a+\ell-q& a+\ell/2<q<a+\ell,\\
0&\text{otherwise}.
\end{cases}
$$

In particular $0\le\psi_I\le\ell/2$, and endpoints contribute zero.
For a rectangle $R=I\times J$, this proves (H0): each point contributes
$\psi_I(p_1)\psi_J(p_2)$, and the area term contributes
$-M|R|^2/16$. Repeated points contribute repeatedly; a boundary point
cannot create an omitted positive term.

Choose $n\ge2$ with $2^{n-2}\le M<2^{n-1}$. At each of the $n+1$
shapes $(k,n-k)$, at most $M$ interiors contain a point, even counting
repetitions separately. At least $2^{n-1}$ rectangles are empty in their
interiors. Choosing the sign of each Haar coefficient therefore gives an
$r$-function $f_k$ with

$$
\langle D,f_k\rangle\ge
2^{n-1}\frac{2^{n-2}2^{-2n}}{16}=\frac1{128}.
\tag{D9}
$$

For any $r$-function of a shape of total level $s$, a point contributes
to at most one coefficient, with size at most $2^{-s}/4$. The absolute
sum of the area terms is $M2^{-s}/16$. Thus

$$
|\langle D,f\rangle|\le\frac5{16}M2^{-s}.
\tag{D10}
$$

Neither estimate assumes that points avoid dyadic boundaries.

To verify the product rule, order distinct indices
$k_1<\cdots<k_j$. On a rectangle of shape $(k_j,n-k_1)$, every sign
coefficient of the factors is fixed. Every binary-digit factor is fixed
except the $(k_j+1)$st digit in the first coordinate and the
$(n-k_1+1)$st digit in the second. Their product is the Haar function
of that rectangle. The remaining coefficient is a sign. Thus the
product is an $r$-function of total level $n+d$, where
$d=k_j-k_1$. This argument is specific to the two coordinates and
requires no independence of the factors. Dyadic ambiguity affects a null
set only.

Set $\Gamma=\prod_{k=0}^n(1+i\alpha f_k)-1$. Because every $f_k^2=1$
almost everywhere,

$$
\|\Gamma\|_\infty\le e^{(n+1)\alpha^2/2}+1.
$$

For a subset of $j\ge2$ indices whose extremes differ by $d$, there
are $(n-d+1)\binom{d-1}{j-2}$ choices. The product rule and (D10)
therefore bound the nonlinear pairing by

$$
\begin{aligned}
|\langle D,\Gamma_2\rangle|
&\le\frac5{16}M2^{-n}\alpha^2
\sum_{d=1}^n(n-d+1)2^{-d}(1+\alpha)^{d-1}\\
&\le\frac5{16}(n+1)\alpha^2,
\end{aligned}
\tag{D11}
$$

using $M2^{-n}<1/2$ and the geometric sum
$\sum_{d\ge1}2^{-d}(1+\alpha)^{d-1}=1/(1-\alpha)\le2$ for
$0<\alpha\le1/2$. The inner binomial sum is precisely
$\alpha^2(1+\alpha)^{d-1}$; it includes all subset sizes, including even
ones, so the estimate needs no cancellation assumption.

Take $\alpha=1/(80\sqrt{n+1})$ and put $s=\sqrt{n+1}$. By (D9), the
linear pairing is purely imaginary, of modulus at least $s/10240$.
By (D11), all other terms together have modulus at most $1/20480$.
The reverse triangle inequality is sufficient to control cancellation.
Also

$$
\|\Gamma\|_\infty\le e^{1/12800}+1
\le\frac{12800}{12799}+1<\frac{20001}{10000}.
$$

Pointwise $|D\Gamma|\le|D|\|\Gamma\|_\infty$, so integration yields

$$
\int|D|\ge
\frac{s/10240-1/20480}{20001/10000}
\ge\frac{s}{41000}.
\tag{D12}
$$

For the last inequality, $s\ge1$ gives $2s-1\ge s$, and the exact
integer comparison is
$20480\cdot20001=409620480<41000\cdot10000$.
Finally $\log M<(n-1)\log2<n+1$, with $M=1$ giving the trivial
target zero. This proves the specified constant for every $M\ge1$,
without a numerical experiment or a cited substitute proof.

The endpoint attack is real against a careless convention transfer:
with the single point $(0,0)$, the discrepancy for the boxes
$[0,u)\times[0,v)$ is $1-uv$ almost everywhere and its norm is $3/4$;
for $(0,u]\times(0,v]$ it is $-uv$ and its norm is $1/4$. The functions
are not equal almost everywhere. The frozen proof explicitly does not
assert that equality for this domain.

For a point with first coordinate zero, the first counting term minus
the second is independent of $u$ off boundary lines. For a point with
second coordinate zero it is independent of $v$. A tensor Haar
function integrates either difference to zero. Positive-coordinate
points give identical counts almost everywhere, including coordinates
equal to one. Hence both discrepancies have identical coefficients
(H0), with the same total $M$ in the area term. Subtracting one in
the definition of $\Gamma$ removes its zeroth-degree term. Every
remaining term is an $r$-function by the verified product rule (and
the single-factor definition), so (D9)--(D12) apply unchanged. The
zero-coordinate witness therefore does not defeat the submitted lower
bound.

## 3. Localization, absolute quantifiers, and the two extrema

### Lemma 7.2 without a common localization point

Fix $S,B$ as in (7.1), choose an integer onset $n_0\ge1$, put
$L=\lfloor S\rfloor$, and let $N>\max(L,n_0)$ tend to infinity.
The localization width is $w=L/N<1$. For each starting point $a$, the
$M_a$ labels in $(a,a+w]$ give planar points
$((x_i-a)/w,i/N)$, with the first coordinate measured along that arc.
Each coordinate is in $(0,1]$, and the distinct time coordinates make
the planar points distinct even if circle positions coincide.

The condition $i/N\le v$ is exactly $i\le\lfloor Nv\rfloor$.
Consequently the discrepancy of this planar set differs from

$$
G_a(u,v)=N_{\lfloor Nv\rfloor}((a,a+uw])-Luv
$$

by $(L-M_a)uv$. Its norm differs by at most $|L-M_a|/4$.
Condition (7.1) at $n=N,D=L$ gives
$\int|M_a-L|\,da\le B$.

If $B<L/4$, the set where $|M_a-L|>L/2$ has measure at most
$2B/L<1/2$, since its contribution to that integral alone is at least
$L/2$ times its measure. On the complementary set, for $L\ge4$,
$M_a\ge L/2\ge2$. The planar lower bound and the reverse triangle
inequality imply

$$
\int\|G_a\|_1\,da
\ge\frac{c_H}{2}\sqrt{\log(L/2)}-\frac B4.
\tag{D13}
$$

For an upper bound, set $n=\lfloor Nv\rfloor$. When $n\ge n_0$,
apply (7.1) with $D=nuw\le L\le S$. The centering error is
$Lu(n/N-v)$, of magnitude at most $L/N$. On the remaining strip
$v<n_0/N$, counts are at most $n_0$ and $|G_a|\le n_0+L$.
It follows that

$$
\int\|G_a\|_1\,da
\le B+\frac LN+\frac{n_0(n_0+L)}N.
\tag{D14}
$$

All floors, zero prefixes and wrapped arcs are accounted for here. The
good set of $a$ can change with $N$. No common $a$ is asserted or
needed: (D13) and (D14) bound the same scalar integral separately for
each $N$. With $L,n_0$ fixed, letting the explicit error in (D14) tend
to zero gives

$$
B\ge\frac{2c_H}{5}\sqrt{\log(L/2)}.
$$

For $S\ge64$, $L\ge S/2$ and $L/2\ge S/4\ge\sqrt S$.
Thus the preceding bound implies
$B\ge(c_H/5)\sqrt{\log S}$. In the other case,
$B\ge L/4\ge S/8\ge\sqrt S\ge\sqrt{\log S}$, which is stronger.
Consequently the simultaneous absolute choices

$$
c_4=\frac{c_H}{5}=\frac1{205000},\qquad S_0=64
\tag{D15}
$$

are admissible. They depend on neither the sequence nor its onset $n_0$.

### The upper-span closing comparison

Use $C_2=e^{20}$, $C_3=468$ from section 1 and (D15), and choose

$$
c=\frac{c_4}{4C_3},\qquad
R=\max(64,c^{-2}),\qquad r_0=\lceil e^R\rceil.
\tag{D16}
$$

These are witnesses for existence of absolute constants; optimal values
are not claimed. This $c$ also satisfies the strict upper bound on $c$
chosen in the frozen closing comparison.

Fix any integer $r\ge r_0$ and any sequence. Write $H=\log r$ and
$A=c\sqrt H\ge1$. If its upper-span limsup were less than $A$, then
$nM_n^{(r)}-r\le A$ at every sufficiently large integer time. Its
onset is allowed to depend on this sequence and $r$.

Here $A\ge1$ gives $\Lambda=\log(r/A)\le H$, while
$\log A\le\tfrac12\log H\le H/2$ gives $\Lambda\ge H/2\ge32$.
In particular $r\ge C_2 A$. Moreover

$$
\log S=\tfrac12(H+\log A)-2\log\Lambda
\ge H/2-2\log H\ge H/3.
\tag{D17}
$$

The last inequality holds for all $H\ge64$: $H-12\log H$ is
increasing there, and $\log64=6\log2<9/2$ already makes it positive
at sixty-four. The inequality $\log2<3/4$ follows, for example, from
$e^{3/4}>1+3/4+(3/4)^2/2>2$.
Thus $S\ge S_0$, and $B=C_3A\ge1$.

Proposition 6.4 supplies (7.1) with this $S,B$, and Lemma 7.2 gives

$$
\frac{c_4}{4}\sqrt H=C_3A
\ge c_4\sqrt{\log S}\ge\frac{c_4}{\sqrt3}\sqrt H,
$$

which is impossible. This proves the first assigned all-sequence bound.
The passage to a contradiction applies to every sequence; it never
selects a common onset time for all sequences.

### The lower-span closing comparison

Keep exactly the constants (D16). If instead
$\limsup_n(r-nm_n^{(r)})<A$, then the second alternative of (6.1)
holds at every sufficiently large integer time. In (D3) it controls
the negative mass rather than the positive mass; their equality
still gives the same (D4), hence (D6), (D8) and (7.1) with the same
$B=C_3A$. The localization argument does not refer to which
alternative supplied (7.1). The identical contradiction above proves
the second assigned all-sequence bound. Neither proof alternates
between the two hypotheses with $n$, nor needs their large deviations
to occur at the same times.

### The two extremal consequences in their stated units

For fixed $r$, set $a=c\sqrt{\log r}$. For every $X$ the first theorem
gives

$$
\limsup_n nM_n^{(r)}\ge r+a.
$$

Taking the infimum over exactly that same family gives
$\Lambda_r-r\ge a$. For the second theorem, $0\le nm_n^{(r)}\le r$
at every sufficiently large time, so subtraction reverses liminf and
limsup without an indeterminate extended-real subtraction:

$$
\limsup_n(r-nm_n^{(r)})
=r-\liminf_n nm_n^{(r)}.
$$

Consequently every sequence has $\liminf_n nm_n^{(r)}\le r-a$;
the supremum over sequences gives $r-\lambda_r\ge a$. The infimum
and supremum are taken after the sequence limits throughout. No
attainment, compactness, common optimizing sequence, or exchange of
operations is needed. In particular a choice of different $X$ for
each $r$ cannot defeat a bound already universal in $X$.

There is also no hidden finiteness issue in these extrema. Enumerate
zero and then, at each stage, all the midpoints of the current dyadic
grid, in clockwise order starting from the gap at zero. If
$m=2^j\le n<2m$, the first $n$ labels include the entire grid of
mesh $1/m$. The maximum gap is at most $1/m$ and the minimum gap
is at least $1/(2m)$. For $n\ge r$, this gives
$nM_n^{(r)}\le2r$ and $nm_n^{(r)}\ge r/2$. Together with the mean
identity this proves $r\le\Lambda_r\le2r$; it also confirms the
supremum is over a nonempty family of finite values. Directly, the
mean identity gives $0\le\lambda_r\le r$ for all sequences.

This sequence supplies a more exact attack on the limit conventions.
Keep $r$ fixed and let $m=2^j$ tend to infinity with $m>r$. At
$n=m$, both scaled span extrema equal $r$. At $n=2m-r$ there are
$r$ consecutive unsplit gaps, each of length $1/m$, so
$nM_n^{(r)}=(2m-r)r/m\longrightarrow2r$. At $n=m+r$, the first
$r$ original gaps have been split and give $2r$ consecutive gaps
of length $1/(2m)$, so
$nm_n^{(r)}=(m+r)r/(2m)\longrightarrow r/2$.
The global bounds just proved imply the exact limits

$$
\liminf_n nM_n^{(r)}=r,\quad \limsup_n nM_n^{(r)}=2r,
\qquad
\liminf_n nm_n^{(r)}=r/2,\quad \limsup_n nm_n^{(r)}=r.
$$

Thus the deviations vanish at infinitely many complete-grid times
but their limsups are $r$ and $r/2$. In particular, the incorrect
subtraction $r-\limsup_n nm_n^{(r)}$ would give zero in place of
$r/2$. The submitted consequence uses the correct liminf. These are
checks in the exact span units of the claim, not ratio or count
surrogates, and they do not purport to compute either optimum.

Finally $a=c\sqrt{\log r}$ tends to positive infinity as integers
$r$ tend to infinity, with the same fixed $c>0$. Each of the two
extremal lower bounds therefore proves its own assigned divergence.
