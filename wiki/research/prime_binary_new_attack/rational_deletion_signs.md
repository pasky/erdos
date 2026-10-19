---
name: research/prime_binary_new_attack/rational_deletion_signs
title: Signs of periodic deletion weights under rationality
desc: |
  A rational prime binary series forces only o(N_X) downward residue
  transitions when composites are deleted from a periodic set, so the
  positive mass is the final count up to o(N_X). Gains are decided at the
  prime endpoints; high ranks cost arbitrarily little and rough sites at
  most log 2. The small-factor estimate is open. Dropping integrality
  gives too much mass, and certificates with nonnegative prime-pair costs
  fail on stationary integer transitions.
created: 2026-10-17T01:42:55Z
updated: 2026-10-17T23:52:10Z
---

***

This is Plasma AI's author-recorded conditional argument for
[[problems/irrationality/E0251/_index|Problem 251]]. It uses the integer
carry lattice and the PNT mean-tail bound (T) of the
[[research/prime_binary_new_attack/proof_sketch|canonical sketch]], at
that page's author standing. It does not prove irrationality and has not
been independently reviewed. The point of conditioning on rationality
is to keep information discarded by a bound for arbitrary integer
prefixes: the same actual prime tail controls every deletion in one gap.

## The proposed contradiction and its remaining input

Assume $S=\sum_{n\ge1}p_n2^{-n}=a/(2^sd)$ with $d$ odd. Write

$$
h_n=\frac{p_{n+1}-p_n}{2},\qquad
H_n=\sum_{j\ge0}\frac{h_{n+j}}{2^{j+1}},\qquad c_n=dH_n.
$$

For all sufficiently large $n$, the sketch gives

$$
c_n\in\mathbb Z_{>0},\qquad c_{n+1}=2c_n-dh_n.
\tag{D1}
$$

Fix an odd prime $q$ with $L=2^{q-1}-1>d$ and let
$W=\{m\ge1:m\text{ odd},\ q\nmid m\}$. Let $\sigma$ denote its
successor map. Its half-gap tails are

$$
H_i^W(m)=H^W(\sigma^im),\qquad
H_0^W(m)=1+\frac{2^e}{L}\quad(0\le e\le q-2).
\tag{D2}
$$

Indeed one half-gap in each period of length $q-1$ is $2$ and the
others are $1$. Both $dH_0^W(m)$ and $2dH_0^W(m)$ have distance at least
$1/L$ from the integers. Put

$$
\begin{gathered}
I_X=\{n:X<p_n\le2X\},\qquad N_X=|I_X|,\\
K=\lceil A\log_2\log X\rceil,\quad A>2,\quad M=2^K,\quad
R=\lfloor4d\log X\rfloor,\\
D=\lfloor\lambda_XK\log X\rfloor,\qquad
16\le\lambda_X\le\log X,\qquad J_X=(X,2X+D].
\tag{D3}
\end{gathered}
$$

The logarithm without a subscript is natural. For integer $u$, let
$r_d(u)$ be the least positive residue of $-du$ modulo $M$; a zero residue
means $M$, and $E(u)=\mathbf1[r_d(u)\le R]$.

For a finite ordered set $T\subseteq W\cap J_X$, define $C(T)$ as follows.
A root $x\in T\cap(X,2X]$ contributes $1$ if it has $K$ successors
$x=x_0<x_1<\cdots<x_K$ in $T$, their span is at most $D$, and

$$
E\left(\sum_{i=1}^K2^{K-i}\frac{x_i-x_{i-1}}2\right)=1.
\tag{D4}
$$

Otherwise it contributes $0$. The final prime count is
$B_d(X)=C(\mathbb P\cap J_X)$.
Starting from $W\cap J_X$, delete its composite sites in increasing
order. Immediately before the deletion of $m$, the set is

$$
T_m=(\mathbb P\cap(X,m))\cup(W\cap[m,2X+D]),\qquad
\Phi(m)=C(T_m\setminus\{m\})-C(T_m).
$$

The initial count is zero for large $X$. To see this, a purely periodic
block has weighted sum $U$ with
$dU/M=dH_0^W(x)-dH_K^W(x)/M$. Since $1<H_K^W<2$ and
$M>2dL$, subtraction does not cross an integer. Thus
$r_d(U)\ge M/L>R$. Its span is at most $4K\le D$.
The same argument shows that a composite root has indicator zero when
it is deleted. Telescoping therefore gives the exact identity

$$
B_d(X)=\sum_{\substack{m\in W\cap J_X\\m\text{ composite}}}\Phi(m).
\tag{D5}
$$

By (D1), the mean-tail bound (T), and the span calculation in
[[research/prime_binary_new_attack/consecutive_block_counts|Proposition U3]],

$$
B_d(X)\ge\left(\frac78-\frac1{\lambda_X}-o(1)\right)N_X.
\tag{D6}
$$

For completeness, (T) excludes at most $(1/8+o(1))N_X$ endpoints with
$c_{n+K}>R$. Every other endpoint gives
$r_d(U_{n,K})=c_{n+K}\le R$ because $c_{n+K}+dU_{n,K}=Mc_n$.
PNT telescoping gives
$\sum_{n\in I_X}(p_{n+K}-p_n)=(1+o(1))KX$, so at most
$(1/\lambda_X+o(1))N_X$ starts fail the span cutoff. The argument is
uniform for the two choices $\lambda_X=16$ and $\lambda_X=\log X$,
and indeed throughout the range in (D3).

The proof below shows that, under the same rationality hypothesis,

$$
\sum_m\max\{-\Phi(m),0\}
\le\left(\frac1{\lambda_X}+o(1)\right)N_X.
\tag{D7}
$$

In particular, at $D=\lfloor K(\log X)^2\rfloor$, the negative part
is $o(N_X)$. A contradiction would still require a new arithmetic
estimate, for example

$$
\sum_m\max\{\Phi(m),0\}
\le\left(\frac78-\varepsilon_d\right)N_X
\tag{D8}
$$

along arbitrarily large $X$, for every fixed odd $d$, with some
$\varepsilon_d>0$. This bound may itself be proved under the
rationality hypothesis. It is **unproved**, including for $d=1$.
Changing to the larger span does not import any upper estimate proved
for a smaller span. By (D16) below, (D8) is equivalent, up to
$o(N_X)$ and a reduction of the positive saving, to a direct bound
$B_d(X)\le(7/8-\varepsilon_d)N_X$. This identity supplies no upper
estimate; it does not rule out estimating the parts of the deletion sum.

## A common carry in each prime gap

Take $X$ large enough that all indices used below, including the
preceding $K$ prime indices, satisfy (D1). Fix $p_r<m<p_{r+1}$ with
$m\in W$ and put $z=(m-p_r)/2$. For $0\le t<K$ the possibly affected prime root is
$p_{r-K+t+1}$. Write

$$
\begin{aligned}
V_t(m)&=\sum_{i=0}^{t-1}2^{t-1-i}
              \frac{\sigma^{i+1}m-\sigma^im}{2}
       =2^tH_0^W(m)-H_t^W(m),\\
b&=2U_{r-K+1,K-1}+z,\\
Y_m&=2c_r-dz-dH_0^W(m),\\
Y'_m&=2c_r-dz-2dH_0^W(m).
\end{aligned}
\tag{D9}
$$

Here $U_{n,j}=\sum_{i=0}^{j-1}2^{j-1-i}h_{n+i}$, with $U_{n,0}=0$.
The weighted sums at that root, before and after the deletion, are
congruent modulo $M$ to $2^tb+V_t(m)$ and $2^tb+V_{t+1}(m)$.
Iteration of (D1) gives

$$
db=Mc_{r-K+1}-2c_r+dz.
$$

Consequently their positive residues are those of the integers

$$
A_t(m)=2^tY_m+dH_t^W(m),\qquad
A'_t(m)=2^tY'_m+dH_{t+1}^W(m).
\tag{D10}
$$

These formulas are congruences with the residues, not equalities to the
least positive representatives. Keeping the reduction modulo $M$ is
essential until a separate bound excludes a wrap.

Both displayed integers are positive. Let $J_m$ be the half-gap tail of
$m$ followed by all primes larger than $m$. Then

$$
J_m=\frac{h_r-z+H_{r+1}}2,\qquad
Y'_m=2d(J_m-H_0^W(m)).
$$

Every prime successor is a successor in $W$, and the prime sequence is
a proper subsequence of those successors. For any increasing sequence
$a_0=m,a_1,\ldots$ with convergent tail, its half-gap tail is
$\sum_{j\ge1}(a_j-m)2^{-j-2}$, by summing the gaps. Termwise comparison
therefore gives $J_m>H_0^W(m)$. Also
$Y'_m\in\mathbb Z-2dH_0^W(m)$, whence $Y'_m\ge1/L$ and
$Y_m=Y'_m+dH_0^W(m)>Y'_m$.

Let $\delta_t(m)=(\sigma^{t+1}m-\sigma^tm)/2\in\{1,2\}$. The two
integers satisfy

$$
A_t(m)-A'_t(m)=d(V_t(m)+\delta_t(m))>0,
\qquad A_t(\sigma m)=A'_t(m).
\tag{D11}
$$

In the second equality the expression is evaluated with the same $r$,
also at the endpoint $\sigma m=p_{r+1}$. Thus, for fixed $r,t$, these
positive integers decrease as composite sites in the gap are deleted.
A residue indicator can decrease only when this decreasing sequence
passes a positive multiple of $M$.

## Downward residue transitions are negligible

Let $N^-_{\rm res}(X)$ count all pairs consisting of a deleted composite
and an affected prime root in $(X,2X]$ whose residue indicator changes
from $1$ to $0$. Ignore the span condition in this definition, using the
infinite periodic continuation to define successors. This only enlarges
the set of possible residue losses of the finite count.

**Conditional sign bound.** Under $S=a/(2^sd)$,

$$
N^-_{\rm res}(X)
\ll_{d,q} \frac{XR\log R}{M}=o(N_X).
\tag{D12}
$$

*Proof.* Put $Z=L(R+2d)$ and $T=\lceil\log_2Z\rceil$.
If a root of rank $t$ has its residue $a_t\le R$ before deletion,
then reduction modulo $2^t$ gives

$$
\frac{a_t-dH_t^W(m)}{2^t}\in\mathbb Z-dH_0^W(m).
$$

The distance in (D2) implies $2^t<Z$. Hence every possible downward
transition has $0\le t<T$; this conclusion uses the ordinary congruence
and does not assume that (D10) is already reduced.

Call a gap bad when

$$
c_r>\frac{M-2d}{2Z}.
\tag{D13}
$$

If it is not bad and the root is counted, (D9)--(D10) give
$0<A'_t(m)<A_t(m)<2Zc_r+2d\le M$. Its residue cannot change from
$1$ to $0$. Thus every downward residue transition lies in a bad gap.

All relevant $r$ have $X<p_r\le2X+D<3X$ for large $X$.
Applying (T) with shift zero on $(X,2X]$ and $(2X,4X]$ yields
$\sum_r c_r=O_d(X)$ over this range. Also
$\sum_r h_r=O(X)$, by telescoping and PNT. It follows from (D13)
that the number of bad gaps is $O_d(XZ/M)$.

For fixed $r,t$, (D10) can also be written

$$
A_t(m)=2^{t+1}c_r-d2^tz-dV_t(m).
$$

Since $2^t-1\le V_t(m)\le2(2^t-1)$, its total decrease over any part
of the gap is at most $d2^t(h_r+1)$. A strictly decreasing sequence
with total decrease $V$ can pass at most $1+V/M$ distinct multiples of
$M$. Each downward residue transition passes one, and different
transitions pass different ones. Summing first over $0\le t<T$ and
then over the bad gaps bounds their total by

$$
T\,\#\{\text{bad gaps}\}
+\frac{2dZ}{M}\sum_{r\text{ bad}}(h_r+1)
\ll_{d,q}\frac{XZ\log Z}{M}.
$$

This proves the first bound in (D12), since $Z\asymp_{d,q}R$.
Its ratio to $N_X\sim X/\log X$ is
$O_{d,q}((\log X)^{2-A}\log\log X)=o(1)$, because $A>2$.
$\square$

To deduce (D7), keep the span indicators as well. For each prime root,
its $K$th successor only moves right during deletion. Its span indicator
therefore falls at most once. Such a fall is possible only for a root
whose final span $p_{n+K}-p_n$ exceeds $D$. The calculation preceding
(D6) bounds these roots by $(1/\lambda_X+o(1))N_X$.
Every loss of the full indicator is either a residue loss or a span
loss. Finally the negative part of the sum of indicator changes at one
site is at most the number of indicator losses at that site. Summing
proves (D7), including the finite right boundary, which is just a span
failure for a root whose required successor leaves $J_X$.

## Positive gains at the gap endpoints

Keep the rationality hypothesis, $A>2$ and the enlarged span
$\lambda_X=\log X$, so $D=\lfloor K(\log X)^2\rfloor$. This section
accounts for the positive deletion mass. Its conclusion is that (D8)
is a direct upper bound for $B_d(X)$ in another form: the deletion
decomposition locates the gains but supplies no saving for them.

**The positive mass is the final count.** By (D5) and (D7),

$$
\sum_m\max\{\Phi(m),0\}
=B_d(X)+\sum_m\max\{-\Phi(m),0\}
=B_d(X)+o(N_X).
\tag{D16}
$$

Hence existence of a fixed saving in (D8) on a sequence of scales is
equivalent to existence of a fixed saving below $7/8$ for $B_d(X)$,
after reducing the saving if necessary. Either bound contradicts (D6).
Without the rationality
hypothesis the inequality $\sum_m\max\{\Phi(m),0\}\ge B_d(X)$ still
holds, since the weights sum to $B_d(X)$. So an unconditional proof of
(D8) would contain a direct bound for the final count.

Finer accounting uses the number $\Psi(m)$ of prime roots in $(X,2X]$
whose full indicator rises from $0$ to $1$ when $m$ is deleted, and
the number $\Omega(m)$ whose indicator falls. Then
$\Phi(m)=\Psi(m)-\Omega(m)$. The proof of (D7) bounds
$\sum_m\Omega(m)$ by $(1/\lambda_X+o(1))N_X$, so
$\sum_m\Psi(m)=B_d(X)+o(N_X)$ as well. Deleting a site cannot shorten
a span, so a root that gains had an admissible span before the
deletion and gains in its residue indicator.

For $p\in W$, an integer $c$ and $t\ge0$ put

$$
\phi_t(c,p)=2^t\bigl(c-dH_0^W(p)\bigr)+dH_t^W(p).
$$

As in (D12) let $Z=L(R+2d)$, and call the gap $(p_r,p_{r+1})$ good when
(D13) fails, that is, when $c_r\le(M-2d)/(2Z)$.

**Lemma D17 (one root in one gap).** Fix a gap $(p_r,p_{r+1})$ in the
range and the root $p_{r-K+t+1}$ of rank $0\le t<K$.

1. If the root gains at a site of this gap, then $2^t<Z$.
2. Suppose the gap is good, contains a site of $W$, and $2^t<Z$. Along
   the sites of $W$ in the gap, the integers (D10) for this root are the
   least positive residues themselves. They strictly decrease, from
   $\phi_{t+1}(c_r,p_r)$ before the first deletion to
   $\phi_t(c_{r+1},p_{r+1})$ after the last. The root therefore gains at
   most once in this gap, and its residue indicator becomes $1$ inside
   the gap exactly when

$$
\phi_{t+1}(c_r,p_r)>R\ge\phi_t(c_{r+1},p_{r+1}).
\tag{D17}
$$

Part 2 concerns a rise of the residue indicator. A rise of the full
indicator additionally requires that the root is in $(X,2X]$ and its
post-deletion block satisfies the span cutoff. These restrictions can
only remove gains from the residue count used for upper bounds below.

*Proof.* For part 1, let $a'\le R$ be the residue after the deletion of
$m$. Since $a'\equiv A'_t(m)\pmod M$ and $2^t\mid M$,

$$
\frac{a'-dH_{t+1}^W(m)}{2^t}\in\mathbb Z-2dH_0^W(m).
$$

By (D2) this number has distance at least $1/L$ from the integers. Also
$-2d<a'-dH_{t+1}^W(m)<R$. Hence $2^t/L<R+2d$, which is $2^t<Z$.

For part 2, $dz+dH_0^W(m)>0$ gives $Y_m<2c_r$. Since $H_t^W<2$,

$$
0<A'_t(m)<A_t(m)<2^{t+1}c_r+2d<2Zc_r+2d\le M .
$$

So the integers in (D10) lie in $(0,M]$ and are the residues. Let $m_1$
be the first site of $W$ after $p_r$ and $z_1=(m_1-p_r)/2$. Then
$z_1+H_0^W(m_1)=2H_0^W(p_r)$ and $H_t^W(m_1)=H_{t+1}^W(p_r)$, so
$A_t(m_1)=\phi_{t+1}(c_r,p_r)$. Let $m_*$ be the last site of $W$ before
$p_{r+1}$, and $z_*=(m_*-p_r)/2$. Then $z_*+\delta_0(m_*)=h_r$ and
$2H_0^W(m_*)=\delta_0(m_*)+H_0^W(p_{r+1})$. With
$2c_r-dh_r=c_{r+1}$ this gives
$Y'_{m_*}=c_{r+1}-dH_0^W(p_{r+1})$, and
$H_{t+1}^W(m_*)=H_t^W(p_{r+1})$, so
$A'_t(m_*)=\phi_t(c_{r+1},p_{r+1})$. Strict decrease is (D11). A
decreasing sequence of residues crosses the level $R$ at most once, and
it crosses it inside the gap exactly when (D17) holds. $\square$

The endpoint values chain from gap to gap. In gap $r+1$ the same root
has rank $t-1$, and its first value there is
$\phi_t(c_{r+1},p_{r+1})$, the value it had after gap $r$. For the root
$p_n$ the chain therefore runs through the integers
$\phi_{n+K-r}(c_r,p_r)$, $n\le r\le n+K$. Its last value is
$\phi_0(c_{n+K},p_{n+K})=c_{n+K}$. Its least positive residue is
$r_d(U_{n,K})$; equality with $c_{n+K}$ itself requires
$c_{n+K}\le M$. In the good regime a root's residue rises in a gap only
according to the carries and the periodic data at the two prime
endpoints. The factorization of an interior site does not enter. It
decides only which site carries the gain: by (D9)--(D10) that site has
offset $z$ within $4$ of $(2c_r-R2^{-t})/d$.

**Proposition D18 (finite ranks and single gains).** Under the
hypotheses of this section the following hold.

1. Sites in bad gaps carry total gain
   $\sum\Psi\ll_{d,q}XZ\log Z/M=o(N_X)$.
2. There is an absolute constant $C_0$ such that, for each fixed integer
   $T_0\ge1$, the gains at ranks $t\ge T_0$ in good gaps number at most
   $C_02^{-T_0}N_X+o_{T_0}(N_X)$.
3. Good gaps with $c_{r+1}<6d$ carry total gain $o(N_X)$.
4. If $R>12d$, every site of every other good gap has $\Psi(m)\le1$.
5. Consequently

$$
\sum_{\substack{m\in W\cap J_X\ \text{composite}\\P^-(m)>X^{1/3}}}\Psi(m)
\le(\log2+o(1))N_X.
\tag{D18}
$$

*Proof.* Part 1 repeats the proof of (D12) for rising crossings. In a
bad gap a gain at rank $t$ has $2^t<Z$ by Lemma D17. For fixed $r,t$ the
integers $A_t(m)$ decrease by at most $d(2^{t+1})<M$ per deletion and
by at most $d2^t(h_r+1)$ in total, so distinct gains pass distinct
levels $R+jM$ downward. There are at most $1+d2^t(h_r+1)/M$ of them.
The count of bad gaps and the sum of their $h_r$ are bounded as in the
proof of (D12).

For part 2, take a gain at rank $t$ at the site $m$ of a good gap.
Since $z\le h_r-1$ and $H_0^W<2$,

$$
Y'_m>2c_r-d(h_r-1)-4d=c_{r+1}-3d .
$$

As $A'_t(m)\ge2^tY'_m$ and $A'_t(m)\le R$, this gives
$c_{r+1}<R2^{-t}+3d$. Positivity of $c_{r+2}=2c_{r+1}-dh_{r+1}$ then
gives

$$
h_{r+1}<\frac{2c_{r+1}}d<8(\log X)2^{-t}+6 .
$$

Lemma D17 allows one gain per good gap and rank. Lemma M1 of the
[[research/prime_binary_new_attack/survivor_moments|survivor-moment
note]], with $k=2$, $L=1$ and offset $2j$, and its average (M4) of the
offset factor show that the primes $X<y\le4X$ with $y+2j$ prime, summed
over $1\le j\le u$, number $O((u+1)X/(\log X)^2)$ uniformly for
$1\le u\le5\log X$. Map the gap $r$ to $y=p_{r+1}$. Summing this bound at
$u_t=8(\log X)2^{-t}+6$ over $T_0\le t<\log_2Z$ gives at most
$C_02^{-T_0}X/\log X+O(X\log\log X/(\log X)^2)$ gains.

For part 3, such a gap has $h_{r+1}<12$, so there are
$O(X/(\log X)^2)$ of them by the same pair bound. Each carries at most
one gain per rank $t<\log_2Z$, hence $O(\log\log X)$ gains.

For part 4, suppose the site $m$ lies in a good gap with
$c_{r+1}\ge6d$. Then $Y'_m>3d$ and $Y_m=Y'_m+dH_0^W(m)<Y'_m+2d$, so
$Y_m/Y'_m<5/3$. A gain at rank $t$ needs $A'_t(m)\le R<A_t(m)$, that is,

$$
\frac{R-2d}{Y_m}<2^t<\frac R{Y'_m}.
$$

When $R>12d$ the ratio of these endpoints is below
$(5/3)(6/5)=2$, so at most one rank qualifies.

For part 5, parts 1, 3 and 4 give $\Psi(m)\le1$ except on a set of
sites whose total gain is $o(N_X)$. It remains to count the composites
$X<m\le2X+D$ with $P^-(m)>X^{1/3}$. Those with two prime factors number
$(\log2+o(1))N_X$, by the calculation of
[[research/prime_binary_new_attack/consecutive_block_counts|Corollary U17]]
at $\alpha=1/3$, since
$\int_{1/3}^{1/2}du/(u(1-u))=\log2$. A product of three primes above
$X^{1/3}$ has every factor below $3X^{1/3}$, so there are
$O(X/(\log X)^3)$ of them. No such $m$ has four factors. The buffer
$(2X,2X+D]$ has $D=o(N_X)$ sites. $\square$

The proposition removes all but a fixed number of ranks at an
arbitrarily small cost, and pays for the rough sites at
$(\log2+o(1))N_X$ without the constant of Lemma U16. It does not bound
the remaining gains. Put $\eta=17/24-\log2>0$ and let
$P_{\rm SF}^{<T_0}(X)$ be the gain at sites with $P^-(m)\le X^{1/3}$
and at ranks $t<T_0$. With $C_02^{-T_0}<\eta/2$, a bound
$P_{\rm SF}^{<T_0}(X)\le N_X/6$ on unbounded scales would contradict
(D6), since the total gain would be at most
$(7/8-\eta/2+o(1))N_X$. This sufficient test is stronger than the
direct count bound: the split charges $(\log2+o(1))N_X$ to rough sites
by counting sites rather than gains. The test remains **unknown**,
including for $d=1$. Lemma D17 locates a crossing through its endpoint
carries; it supplies no distribution theorem for the least factor of
the site where that crossing occurs. A proof must control these
carry-dependent offsets jointly with the arithmetic of the sites.
The equivalence (D16) does not prohibit such a proof. The following
calculation identifies a particular invalid relaxation of that task.

## Ordinary crossings without the integer lattice

Keep the actual prime tails $c_n=dH_n$ and the enlarged-span parameters,
but do **not** assume that $S$ is rational. The carries are now positive
real numbers and still satisfy $c_{n+1}=2c_n-dh_n$. At an actual prime
root $p_n$, for a hybrid set $T$ with $K$ successors, put

$$
\mathcal A_n(T)=Mc_n-dU_n(T),\qquad
U_n(T)=\sum_{i=1}^K2^{K-i}\frac{x_i-x_{i-1}}2,
\quad x_0=p_n.
\tag{D19a}
$$

This is an unreduced real value, not a positive residue. Define an
ordinary gain at a deletion when
$\mathcal A_n(T)>R\ge\mathcal A_n(T\setminus\{m\})$, with the same
root and post-deletion span restrictions as for a full gain. Let
$\widetilde\Psi(m)$ count these gains. A missing $K$th successor
contributes no gain. Only actual prime roots are counted.

**Proposition D19 (the continuous relaxation has too much mass).**
Unconditionally, with these real prime tails,

$$
\left(\frac78-o(1)\right)N_X
\le\sum_m\widetilde\Psi(m)\le N_X.
\tag{D19b}
$$

The gains at ranks $t\ge T_0$ cost at most
$C_02^{-T_0}N_X+o_{d,q,T_0}(N_X)$ for each fixed $T_0\ge1$, after
enlarging the absolute constant $C_0$ of D18 if necessary. Except for
total gain $o(N_X)$, each site carries at most one ordinary gain.
Consequently, if $\widetilde P_{\rm SF}^{<T_0}(X)$ counts ordinary
gains at $P^-(m)\le X^{1/3}$ and ranks $t<T_0$, then

$$
\widetilde P_{\rm SF}^{<T_0}(X)
\ge\left(\frac78-\log2-C_02^{-T_0}-o(1)\right)N_X.
\tag{D19c}
$$

In particular, choosing $C_02^{-T_0}<\eta/2$, with
$\eta=17/24-\log2>0$, makes the right side exceed $N_X/6$ by a fixed
positive proportion. Thus the proposed upper bound $N_X/6$ is false
for this unconditional continuous relaxation. This does not disprove
the conditional test for $P_{\rm SF}^{<T_0}$.

*Proof.* In terms of half-offsets $a_i=(x_i-p_n)/2$,

$$
U_n(T)=\sum_{i=1}^{K-1}2^{K-i-1}a_i+a_K.
$$

Every coefficient is positive. Deleting a successor moves the ordered
offsets right, so $U_n(T)$ strictly increases and $\mathcal A_n(T)$
strictly decreases. The span also increases. Each prime root can
therefore have at most one ordinary gain, proving the upper bound.
Its initial value is

$$
M\bigl(c_n-dH_0^W(p_n)\bigr)+dH_K^W(p_n),
$$

and its final value, when its final span is admissible, is $c_{n+K}$.
If $h_n\ge6$, then $H_n>3$ and $H_0^W(p_n)<2$, so the initial value
exceeds $dM>R$ for large $X$. By the two-form bound used in D18,
only $O(X/(\log X)^2)=o(N_X)$ roots have $h_n<6$. The mean-tail
bound (T) puts at least $(7/8-o(1))N_X$ final carries at most $R$;
PNT span telescoping loses only $O(N_X/\log X)=o(N_X)$ further roots
at $D=\lfloor K(\log X)^2\rfloor$. Every remaining root crosses $R$
while its span is still admissible. This proves the lower bound in
(D19b).

For a deletion inside $(p_r,p_{r+1})$, at rank $t$, iteration of the
real carry recurrence gives the exact identities

$$
\mathcal A_n(T_m)=A_t(m),\qquad
\mathcal A_n(T_m\setminus\{m\})=A'_t(m),
\quad n=r-K+t+1,
$$

with the expressions (D9)--(D10) now interpreted as real numbers.
Their algebra and their strict decrease require no lattice. An
ordinary gain therefore gives

$$
c_{r+1}<R2^{-t}+3d,
\qquad h_{r+1}<8(\log X)2^{-t}+6,
$$

by the same calculation as in D18. There is at most one gain per
gap and rank. Sum the pair bound over $T_0\le t<K$ to obtain
$C_02^{-T_0}N_X+O(KX/(\log X)^2)$; the second term is $o(N_X)$.
No good-gap restriction is needed for ordinary crossings.

Gaps with $c_{r+1}<6d$ have $h_{r+1}<12$, so the pair bound counts
only $O(X/(\log X)^2)$ such gaps. They carry at most $K$ ordinary
gains each. At every other site, $Y'_m>3d$ and $Y_m/Y'_m<5/3$;
the interval for $2^t$ in D18 has endpoint ratio below $2$ when
$R>12d$. Thus at most one rank gains there, without any integrality
assumption. The exceptional total is $o(N_X)$.

The same semiprime census on $X<m\le2X+D$ used in D18 now bounds
ordinary gains with $P^-(m)>X^{1/3}$ by $(\log2+o(1))N_X$.
Subtract this and the high-rank bound from (D19b), proving (D19c).
$\square$

The phase discarded by the relaxation is explicit:

$$
-dU_n(T)=\mathcal A_n(T)-Mc_n.
\tag{D20}
$$

The actual indicator reduces the right side modulo $M$ and takes its
least positive residue. Rationality makes $Mc_n$ a multiple of $M$;
the good-gap bounds then identify the relevant representatives with
their residues. Without that premise, dropping $Mc_n$ changes the
event. All real prime tails already obey the recurrence, the mean
bound, the endpoint formulas and the small-next-gap estimate. Those
facts alone cannot prove the proposed upper bound for the ordinary
crossings, since (D19c) proves the opposite inequality for the actual
primes. A proof using these ordinary crossings must therefore use the
integer condition, or another consequence of rationality, in a
substantive arithmetic step. This does not rule out an unconditional
estimate for the original residue gains which retains the full phase
in (D20).

## Locating the selected integer and testing residue information

The finite rank cutoff in D18 permits an exact rounding rule. It does
not remove the actual prime tail from that rule. This section identifies
the arithmetic input to a sieve on the selected sites and tests a proposed
replacement by single-endpoint residue frequencies. All deductions here
are author-recorded.

**Proposition D21 (the exact locator).** Keep (D9), and set

$$
\mathcal A_r=dp_r+4c_r,\qquad
F_t(m)=m+2^{1-t}V_t(m),\qquad
\xi_{r,t}=\frac{\mathcal A_r-2^{1-t}R}{d}.
$$

Here $V_0=0$, so $F_0(m)=m$. For a site in the gap with index $r$,

$$
A_t(m)-R=d2^{t-1}\bigl(\xi_{r,t}-F_t(m)\bigr).
\tag{D21a}
$$

Since $A'_t(m)=A_t(\sigma m)$, an ordinary threshold crossing is exactly

$$
F_t(m)<\xi_{r,t}\le F_t(\sigma m).
\tag{D21b}
$$

The intervals in (D21b) partition all sufficiently large real numbers.
Thus there is a unique selected site $m_t(r)$, with the upper endpoint
included. In particular, if $\xi_{r,t}=F_t(u)$, the selected site is the
predecessor of $u$ in $W$, not $u$. It satisfies

$$
\xi_{r,t}-8<m_t(r)<\xi_{r,t}.
\tag{D21c}
$$

Under the integer-carry hypothesis, the comparison can be made wholly
in integers:

$$
d2^tF_t(m)<2^t\mathcal A_r-2R
\le d2^tF_t(\sigma m).
\tag{D21d}
$$

For fixed $R,t$, divisibility of $m_t(r)$ by a positive integer $\ell$
is a periodic predicate of $\mathcal A_r$, with period $2qd\ell$.

*Proof.* Substitution of (D9) into (D10) gives

$$
A_t(m)=2^{t-1}(\mathcal A_r-dm)-dV_t(m),
$$

which proves (D21a) and (D21b). Writing $\delta_i(m)$ for the half-gaps
in $W$, the shift identity

$$
V_t(\sigma m)=2V_t(m)-2^t\delta_0(m)+\delta_t(m)
$$

gives

$$
F_t(\sigma m)-F_t(m)=2^{1-t}\bigl(V_t(m)+\delta_t(m)\bigr)>0.
$$

Also $F_t(m+2q)=F_t(m)+2q$ and
$0\le F_t(m)-m=\sum_{i<t}2^{-i}\delta_i(m)<4$.
These facts prove the partition and, since $\sigma m-m\le4$, (D21c).
Multiplication of (D21b) by $d2^t$ proves (D21d); its terms are integers
because $2^tF_t(m)=2^tm+2V_t(m)$.
Replacing $\mathcal A_r$ by $\mathcal A_r+2qd$ translates the selected
site by $2q$. Repeating $\ell$ times proves the stated period. $\square$

The orbit in this predicate obeys more than integrality:

$$
\mathcal A_{r+1}=2\mathcal A_r-dp_{r+1},\qquad
\mathcal A_{r+1}-\mathcal A_r=2c_{r+1}>0,\qquad
\mathcal A_r\equiv dp_r\pmod4.
\tag{D22a}
$$

These follow directly from (D1). In particular, $\mathcal A_r$ is an
increasing integer sequence. It is not the prime sequence.

For clarity, let $\Gamma_{r,t}(X)$ impose all the original restrictions:
the gap is good, $c_{r+1}\ge6d$, $2^t<Z$, the root index
$r-K+t+1$ belongs to $I_X$, the selected site lies strictly between
$p_r$ and $p_{r+1}$, and the post-deletion $K$-successor block exists
with span at most $D$. The integer-carry hypothesis, D17 and D18 give,
for each fixed $T_0$,

$$
P_{\rm SF}^{<T_0}(X)=
\sum_{0\le t<T_0}\sum_r\Gamma_{r,t}(X)
\mathbf1\bigl[P^-(m_t(r))\le X^{1/3}\bigr]+o(N_X).
\tag{D22b}
$$

The error removes the bad gaps and the small $c_{r+1}$ gaps. Every
remaining selected interior site is composite because the endpoints are
consecutive primes. The required $N_X/6$ budget applies to the whole sum,
not separately to each rank. Expanding a least-factor indicator also has
to retain its exclusions of smaller factors; counting every divisor as
a different site changes the quantity.

Equations (D21)--(D22) specify a possible arithmetic attack, but they do
not provide its estimate. The periodic predicate concerns the joint
sequence of $\mathcal A_r$, the prime endpoints, and the restrictions
$\Gamma_{r,t}$. The prime number theorem in a fixed progression controls
unweighted prime endpoints. Replacing the joint sequence by those
marginals is an additional, unproved step.

**A residue-class diagnostic.** Even positive integer carries, exact tail
recurrence and uniform single-endpoint residues modulo $30$ do not alone
make the selected sites rare at a small factor. The following explicit
ensemble has $5/16$ of its rank-two selected sites divisible by $5$.
It is an ensemble of artificial sequences, not of consecutive primes;
it is not a counterexample to (D22b) or to the sufficient bound in D18.

Take $d=1,q=3$, an integer $j\ge1$, and $R=120j+48$. For each
$u\in\{1,2\}$ and $b\in\{1,2,3,4\}$, use the row

| $b$ | $\rho_0$ | $\rho_1$ |
| --- | --- | --- |
| $1$ | $12$ | $18$ |
| $2$ | $9$ | $21$ |
| $3$ | $21$ | $9$ |
| $4$ | $18$ | $12$ |

to define the two-periodic positive integer sequence
$c_i=15j+\rho_{i\bmod2}$ and $h_i=2c_i-c_{i+1}$.
Choose an odd $x_0$ with $x_0\equiv u\pmod3$ and
$x_0\equiv2b\pmod5$, and set $x_{i+1}=x_i+2h_i$.
All $h_i\ge15j-3>0$. Iterating the recurrence and letting its bounded
remainder tend to zero proves

$$
c_i=\sum_{a\ge0}\frac{h_{i+a}}{2^{a+1}}.
\tag{D23a}
$$

Thus these are actual integer tails of the artificial sequences, not
freely assigned labels. Their residues satisfy

$$
\begin{array}{c|cc}
 & i\text{ even} & i\text{ odd}\\ \hline
x_i\pmod3 & u & u\\
x_i\pmod5 & 2b & -b\\
\mathcal A_i=x_i+4c_i\pmod5 & 0 & b .
\end{array}
\tag{D23b}
$$

Indeed $c_0\equiv2b$ and $c_1\equiv3b\pmod5$, while both are multiples
of $3$. The recurrence verifies the table and its repetition. The orbit
$\mathcal A_i$ satisfies all three identities in (D22a), with $p_i$
replaced by $x_i$.

For this $W$, the exact values at rank two are
$F_2(m)=m+5/2$ when $m\equiv1\pmod6$ and $F_2(m)=m+2$ when
$m\equiv5\pmod6$. Since $R/2$ is a multiple of $6$, (D21b) selects

$$
m_i=\begin{cases}
\mathcal A_i-R/2-6=x_i+4\rho_{i\bmod2}-30,&u=1,\\
\mathcal A_i-R/2-4=x_i+4\rho_{i\bmod2}-28,&u=2.
\end{cases}
\tag{D23c}
$$

This includes the equality case at an upper endpoint. These sites lie
strictly inside their gaps: their positive offsets are at most $56$, and
subtracting the displayed offset from $2h_i$ gives respectively
$30j+30-2\rho_{(i+1)\bmod2}$ or
$30j+28-2\rho_{(i+1)\bmod2}$, both positive for $j\ge1$.
They are therefore genuine ordinary crossings in these artificial gaps.
For sufficiently large $j$, the good-gap and no-wrap bounds of D17 also
hold at $X=\exp(R/4)$ and its stated $A>2$; the carries are $O(R)$
whereas the good-gap threshold has order $R^{A-1}$. The enlarged span
is sufficient since every gap is $O(R)$ and $\log X=R/4$.

Give equal weight to the eight choices $(u,b)$ and to the two phases
of each. The sixteen endpoint residues give each invertible class
modulo $30$ exactly twice. Nevertheless, when $u=1$, the even phase
has $5\mid m_i$ for all four $b$, and the odd phase has none. When
$u=2$, only the odd phase with $b=3$ has $5\mid m_i$. There are
therefore exactly five such crossings out of sixteen. If desired, the
initial endpoints may be translated by large multiples of $30$, so
all counted multiples of $5$ are composite. The elementary size
normalization is compatible as $j\to\infty$: the mean carry is
$15j+15=(\log X)/2+9$, and the mean full gap is
$30j+30=\log X+18$.

The same proportions can occur in one long finite list, with errors
$O(1/B)$, by joining $B$ periods from each of the eight sequences.
Here is an explicit way to retain the recurrence and avoid introducing
endpoint multiples of $2,3,5$ at a join. View $\mathcal A$ modulo $30$
as an odd state. A transition from state $a$ to state $b$ is allowed
when $2a-b$ is invertible modulo $30$. Between any two odd states
$a,b$ there is a two-transition path through an odd $v$: modulo each
of $3,5$, exclude $v=2a$ and $v=b/2$, and use the Chinese remainder
theorem to choose a remaining class. An odd lift then makes both
$2a-v$ and $2v-b$ invertible modulo $30$.

For each transition, select the unique next carry in
$[15j+9,15j+23]$ with
$c_{i+1}\equiv(b-a)/2\pmod {15}$. Define the actual next endpoint
by $x_{i+1}=x_i+2(2c_i-c_{i+1})$. Its state advances by
$\mathcal A_{i+1}-\mathcal A_i=2c_{i+1}$, and its residue is the
allowed $2a-b$. Its half-gap is at least $15j-5>0$.
To enter a prescribed block at its prescribed phase, first reach the
state immediately before that phase, then take its prescribed carry.
This costs at most three transitions per join. After the last block,
continue its periodic carries forever. They remain bounded, so (D23a)
holds throughout the joined list as well.

There are $16B+O(1)$ endpoints in these blocks, each invertible class
occurs $2B+O(1)$ times, and at least $5B-O(1)$ of the selected rank-two
sites are divisible by $5$. Requiring a whole $K$-successor block to
stay inside one piece discards only $O(K)$ more roots; take $B/K$ large.
This is a finite-model statement: it does not turn the joined endpoints
into consecutive primes or establish any prime correlation bound.

This calculation rejects only a deduction from the stated local data
and balanced single-endpoint residues. It supplies no sequence of actual
consecutive primes, no prime-pair or higher correlation estimates, and
no prime number theorem for a single sequence as $X\to\infty$. Those
missing properties cannot be assigned to the ensemble. In particular,
the diagnostic does not strengthen D19 into an obstruction to using
integrality. A successful bound for (D22b) must still exploit the joint
arithmetic of the actual primes and their integer carry orbit, or replace
this sufficient route. No such bound is proved here.

## A positive pair-cost certificate does not supply the saving

This section is author-recorded. It rejects one specified class of
certificates for the low-rank gains, already at $d=1$. It concerns a
pointwise enlargement of the gains and a fixed wheel, not the actual
count (D22b), and it uses no prime hypothesis.

For a fixed integer $T\ge4$, a residue $a$ of an odd $p\in W$ modulo a
fixed even $Q$ divisible by $2q$, and positive integers $c,h$ with
$c'=2c-dh>0$ and $p'=p+2h$, put

$$
v_X(a,c,h)=\sum_{0\le t<T}\mathbf1[2^t<Z]\,
\mathbf1[W\cap(p,p')\ne\emptyset]\,
\mathbf1\bigl[\phi_{t+1}(c,p)>R\ge\phi_t(c',p')\bigr].
$$

It depends on $p$ only through $a$, because $H^W_t$ has period $2q$. By
Lemma D17, in a good gap the number of ranks $t<T$ at which a root gains
is at most $v_X(p_r,c_r,h_r)$, whatever the factorization of the site.
This is an upper enlargement: the root and span restrictions of
$\Gamma_{r,t}$ are dropped.

A *positive pair-cost certificate* consists of potentials $P_X(c,a)$
with $|P_X|\le F$, costs $b_X(a)$ on the units modulo $Q$ with
$|b_X|\le B$, a constant $V>0$, and weights $\lambda_X(h)\ge0$ bounded
independently of $X$ and supported on $1\le h\le V\log X$, such that

$$
v_X(a,c,h)\le P_X(c,a)-P_X(2c-dh,a+2h)+b_X(a)+\lambda_X(h)
\tag{D24a}
$$

for every transition with $c'\ge6d$, $\gcd(c,d)=1$, $h\le V\log X$ and
both $a$ and $a+2h$ units modulo $Q$. Write $\mathfrak S(2h)$ for the
prime-pair singular series, and put

$$
\kappa_X=\operatorname*{mean}_{a}b_X(a)
+\frac{16}{\log X}\sum_{h\le V\log X}\lambda_X(h)\mathfrak S(2h)
+\frac{T+2F+B}{2V}.
\tag{D24b}
$$

The intended use was to sum (D24a) along the actual carry orbit, where
the potentials telescope, to pay the costs by the prime number theorem
modulo $Q$ and by the pair bound (R4) of the
[[research/prime_binary_new_attack/residue_switch_moments|residue-switch note]]
applied up to $2X$, which gives at most
$(16+o(1))\mathfrak S(2h)X/(\log X)^2$ gaps $2h$ with $p_r\in(X,2X]$,
and to pay the gaps above $V\log X$, the bad gaps and the gaps with
$c_{r+1}<6d$ at cost $T+2F+B$ each. That would bound the gains at ranks
$t<T$ by $(\kappa_X+o(1))N_X$. If $\limsup\kappa_X$ were below $7/8$ by
a margin exceeding the high-rank cost $C_02^{-T}$ of D18, the total gain
would fall below the forced count (D6). The proposition shows that no
certificate of this class has $\limsup\kappa_X<1$.

**Proposition D24 (stationary transitions).** Let $d=1$, and fix $q$,
$Q$ and $T\ge4$ as above. Every family of certificates satisfying (D24a)
for all large $X$ has $\liminf_{X\to\infty}\kappa_X\ge1$.

*Proof.* Here $R=\lfloor4\log X\rfloor$. Choose an interval $I$ of
$W_c$ consecutive integers inside $[5R/64,7R/64]$, with $W_c$ a multiple
of $Q$ and $W_c\ge R/32-2Q$. The states are the pairs $(c,a)$ with
$c\in I$ and $a$ a unit modulo $Q$. From $(c,a)$ there is an edge to
$(c',a+4c-2c')$ for every $c'\in I$ such that $a+4c-2c'$ is a unit; its
half-gap is $h=2c-c'\in[3R/64,9R/64]$.

*Every edge has $v_X=1$ for large $X$.* Since $0<H^W_t<2$,

$$
\phi_4(c,p)\ge16c-32\ge\tfrac{80}{64}R-32>R,\qquad
\phi_3(c',p')\le8c'+2\le\tfrac{56}{64}R+2<R,
$$

so rank $3$ qualifies; also $2^3<Z$, and $(p,p+2h)$ contains an element
of $W$ because $2h\ge6R/64>4q$. For $t\le2$ one has
$\phi_{t+1}(c,p)\le8c+2<R$, and for $t\ge4$ one has
$\phi_t(c',p')\ge16c'-32>R$, so no other rank qualifies. The conditions
of (D24a) hold, except $h\le V\log X$ when $V<9/16$.

*The edge graph is regular.* Write $Q'$ for the odd part of $Q$ and
$\rho=\varphi(Q')/Q'=2\varphi(Q)/Q$. As $c'$ runs over $I$, a union of
complete residue systems modulo $Q$, the number $a+4c-2c'$ is odd and
runs uniformly over the classes modulo $Q'$, because $2$ is invertible
there. So every state has out-degree $W_c\rho$. Solving
$a=a'-4c+2c'$ for $c\in I$ shows in the same way that every state has
in-degree $W_c\rho$. Choose an edge uniformly. Its initial and final
states are then both uniform on the $W_c\varphi(Q)$ states, so the mean
of $P_X(c,a)-P_X(c',a')$ is zero, the mean of $b_X(a)$ is the mean over
units, and the mean of $h=2c-c'$ equals the mean of $c$, at most
$7R/64\le(7/16+o(1))\log X$.

*Half-gap frequencies.* For fixed $h$, at most $W_c/2+1$ values $c\in I$
have $2c-h\in I$, and for each the number of $a$ with $a$ and $a+2h$
units is $\nu_Q(h)$. Hence the frequency of $h$ among the edges is

$$
\Pr(h)\le\frac{Q\nu_Q(h)}{\varphi(Q)^2}\cdot
\frac{W_c/2+1}{2W_c^2}.
$$

The first factor is the product over $\ell\mid Q$ of the local pair
factors. Restoring the omitted primes, those dividing $h$ contribute
factors above $1$ and the others factors at least $C_2$, the twin-prime
constant; so the first factor is at most $\mathfrak S(2h)/C_2$. Comparing
$C_2=\prod_{\ell>2}(1-(\ell-1)^{-2})$ with
$\prod_{n\ge2}(1-n^{-2})=1/2$ gives $C_2\ge1/2$. With
$W_c\ge(1/8-o(1))\log X$ this yields, uniformly in $h$,

$$
\Pr(h)\le(4+o(1))\frac{\mathfrak S(2h)}{\log X}.
$$

*Conclusion.* On every edge, $1=v_X\le P_X-P'_X+b_X+\lambda_X(h)$ when
$h\le V\log X$, by (D24a). When $h>V\log X$ the inequality
$1\le P_X-P'_X+b_X+T+2F+B$ holds trivially. Averaging over the edges,
and using Markov's inequality for $\Pr(h>V\log X)\le7/(16V)+o(1)$,

$$
1\le\operatorname*{mean}_ab_X(a)
+\frac{4+o(1)}{\log X}\sum_{h\le V\log X}\lambda_X(h)\mathfrak S(2h)
+\frac{T+2F+B}{2V}+o(1).
$$

The sum is $O(V\log X)$ because $\lambda_X$ is bounded and
$\mathfrak S(2h)$ has bounded mean, so its $o(1)$ factor contributes
$o(1)$. Since $\lambda_X\ge0$ and $4<16$, the right side is at most
$\kappa_X+o(1)$. $\square$

The transitions are artificial: integer carries with the exact recurrence
and the enlarged endpoint crossing, not consecutive primes, and they are
not asserted to satisfy the root and span flags. The proposition rejects
the stated pointwise enlargement with nonnegative pair costs, bounded
potentials and a fixed wheel. It does not refute (D22b), a certificate
that keeps the flags of $\Gamma_{r,t}$, signed costs with proved
cancellation, growing moduli, or a potential depending on further prime
correlations. The pair coefficient $16$ is not the obstruction: the
artificial edge frequencies stay below a quarter of it.

## What the signs do not estimate

The bound is conditional on the actual integer carries (D1). It is not
an unconditional estimate for arbitrary prime prefixes and does not
assert that every individual weight is nonnegative. Under rationality
and $\lambda_X=\log X$, it does show that restricting the deletion sum
to **any** subset of composite sites leaves negative part $o(N_X)$.
Thus a proposed contradiction under that hypothesis must control the
positive contributions; an order-$N_X$ cancellation against negative
weights is unavailable in this enlarged-span formulation.

There is an exact reason that summing inside each gap gives no saving.
Let $F_r(m)$ be the sum of the full indicators of the active prime roots
$p_{r-K+1},\ldots,p_r$, with out-of-range roots assigned zero, when
all sites below $m$ have been decided and $m$ begins the periodic
continuation. At an interior gap,

$$
\sum_{m\in W\cap(p_r,p_{r+1})}\Phi(m)
=F_r(p_{r+1})-F_r(\sigma p_r).
\tag{D14}
$$

At the right endpoint the oldest root has its actual $K$th prime
successor, so its indicator has reached its final value, say
$\beta_{r-K+1}$. The new root $p_{r+1}$ begins with a purely periodic
continuation and has indicator zero. Passing this prime changes no
surviving site. Therefore

$$
F_r(p_{r+1})=\beta_{r-K+1}+F_{r+1}(\sigma p_{r+1}).
\tag{D15}
$$

The potentials in (D14)--(D15) telescope. Their remaining final-root
terms are exactly the original count, with the endpoint restrictions
already handled in (D5). Even with the common carry, positivity and its
mean bound, this is an identity, not an upper estimate for that count.

Lemma D17 locates the residue gain root by root through the two prime
endpoints; the full gain also keeps its span restriction. The remaining
small-factor test asks for an upper bound on these crossings at a
specified set of composite sites. The representatives in (D10) retain
the actual tail $c_r$ and its joint relation with $p_r$ and the gap.
Neither an independence statement nor an estimate in residue classes
conditional on those quantities is proved here. D16 shows what a
successful estimate would imply, not that none can exist. Proposition
D19 rules out only the relaxation which drops the integer origin and
bounds ordinary real crossings instead. The small-factor test, (D8)
and the direct count bound remain unknown; these deductions supply
no full solution of Problem 251.

The
[[research/prime_binary_new_attack/short_span_sieve|shorter-span monotone
construction]] uses the same rational carries but a different span and
an enlarged upper event. Its actual-survivor estimate (MS), split into
the excessive local count and the truncated phase-weighted count, is
another sufficient route to the contradiction. The conditional sign
bound here estimates neither of those costs. The
[[research/prime_binary_new_attack/proof_sketch|canonical sketch]] keeps
both routes and their separate open arithmetic inputs.
