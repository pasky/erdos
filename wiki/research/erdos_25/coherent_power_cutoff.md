---
name: research/erdos_25/coherent_power_cutoff
desc: Uniform conditioned-tail bounds below a power cutoff, with new natural-density cases for coherent residues.
tags: [coherent-residues, sieve, partial-results, conditioned-tails]
sources: []
created: 2026-09-22T03:13:32Z
updated: 2026-09-24T22:13:01Z
---


# research/erdos_25/coherent_power_cutoff

***

The estimate here controls **conditioned first-kill increments**, uniformly
in the earlier period, rather than only small full footprints. It handles
arbitrarily many modulus scales below a fixed power cutoff. Coherence is
essential to the proof. The original coherent problem is reduced to
unbounded but subpower quotients, not resolved.

## A uniform selected-cell estimate: proved

Let $D$ be a finite set of moduli, with common center
$\alpha\in\widehat{\mathbb Z}$. Put
$$
 C_q=\alpha+q\widehat{\mathbb Z},\qquad
 F_q=C_q\setminus\bigcup_{\substack{r\in D\\r<q}}C_r,
 \qquad e_q=\mu(F_q).
$$
For any $J\subseteq D$, write $\tau=\sum_{q\in J}e_q$.
There is an absolute constant $C$ such that, for $0<\eta\le1/2$
and any interval $I$ of $H\ge2$ consecutive integers,
$$
 \frac1H\#\{n\in I:n\in F_q\text{ for some }q\in J,
                         \ q\le H^{1-\eta}\}
 \le f_\eta(\tau):=
 \min\left(1,\frac{C}{\eta\log(2/\tau)}\right).
 \tag{1}
$$
Set $f_\eta(0)=0$. The bound is uniform in the center, the location of
$I$, the number of moduli, and the choice of cells.

The first-divisor and smooth-factor decomposition is adapted from
[Erdős--Hall--Tenenbaum, *On the densities of sets of multiples*, Section 2,
equations (2.7)--(2.8)](https://tenenb.perso.math.cnrs.fr/PPP/dens-som.pdf#page=7).
Those passages were checked in the author-hosted paper. The proof below
supplies the needed uniform translated smooth-part estimate; it never
assumes $|n-\alpha|\le H$.

### Two elementary sieve ingredients

For $y\ge2$ and any real interval $K$ of length $M\ge y^5$,
$$
 \#\{h\in K\cap\mathbb Z:h\ne0,\ p\nmid h\ (p\le y)\}
 \ll\frac M{\log y}.
 \tag{2}
$$
This includes negative intervals. Here is a proof to fix the uniformity.
Choose Selberg weights supported on squarefree $d\le y$, with
$\lambda_1=1$. Squaring their divisor sum majorizes the rough-integer
indicator, and progression counting gives the upper bound
$$
 M\sum_{d,e\le y}\frac{\lambda_d\lambda_e}{[d,e]}
       +O\left(\left(\sum_{d\le y}|\lambda_d|\right)^2\right).
$$
Write $G(y)=\sum_{d\le y}\mu^2(d)/\varphi(d)$. The quadratic form
diagonalizes as
$$
 \sum_r\varphi(r)\left(\sum_{r\mid d}\lambda_d/d\right)^2.
$$
Its minimum subject to $\lambda_1=1$ is $1/G(y)$, attained by
$$
 \lambda_d=\frac{\mu(d)d}{\varphi(d)G(y)}
       \sum_{\substack{m\le y/d\\(m,d)=1}}\frac{\mu^2(m)}{\varphi(m)}.
$$
Indeed Möbius inversion turns the constraint into
$\sum_r\mu(r)\sum_{r\mid d}\lambda_d/d=1$, and Cauchy--Schwarz
gives this minimum and optimizer. In particular $|\lambda_d|\le d$.
Also $G(y)\gg\log y$: squarefree integers have counting function at
least $(2-\zeta(2))\lfloor x\rfloor$, by the union bound over square divisors, and
$\varphi(d)\le d$. Thus the bound is $O(M/\log y+y^4)$, proving (2).

We also use
$$
 \sum_{p\le y}\frac{\log p}{p-1}\ll\log y,
 \qquad Z_H:=\prod_{p\le H}(1-1/p)^{-1}\ll\log H.
 \tag{3}
$$
The first follows by partial summation from Chebyshev's elementary
$\sum_{p\le y}\log p\ll y$: primes in $(m,2m]$ divide
$\binom{2m}{m}$, and dyadic summation proves that estimate. The Euler
product bound is the passage immediately before equation (12) in the
[Davenport--Erdős 1951 full source](../../../library/divisors/davenport_1951_sequences_positive_integers/_index.md),
checked again for this application.

### Uniform control of the shifted smooth part

Discard moduli above $H^{1-\eta}$, which does not change any retained
first-kill cell, and choose an integer $b$ realizing the retained center
residues. Fix
$$
 0<\delta\le\eta/10,\qquad y=H^\delta\ge2.
$$
For $p\le y$, let $k_p$ be minimal with $p^{k_p}>H^{\eta/4}$.
The proportion of $n\in I$ for which any $p^{k_p}$ divides $n-b$ is
at most
$$
 H^{\delta-\eta/4}+H^{\delta-1}.
$$
Outside this set, $n\ne b$ and the logarithm of the $y$-smooth part of
$|n-b|$ is
$$
 T(n)=\sum_{p\le y}\sum_{1\le k<k_p}
                     (\log p)\mathbf1_{p^k\mid n-b}.
$$
Its average over $I$ is at most
$$
 \sum_{p\le y}\frac{\log p}{p-1}
       +\frac1H\sum_{p\le y}(k_p-1)\log p
 \ll\delta\log H+\eta H^{\delta-1}\log H.
$$
Markov's inequality therefore shows that the smooth part is at most
$H^{\eta/2}$, except on a proportion
$$
 \ll\delta/\eta+H^{-3\eta/20}.
 \tag{4}
$$
All counting here is in translated progressions, so the size of $b$
does not enter the estimates.

### Charging good points to their actual first-kill cells

For a remaining point first killed by $q$, write
$$
 n-b=qsh,
$$
where $s>0$ is the entire $y$-smooth part of $(n-b)/q$ and $h$ is
possibly negative and $y$-rough. Then $s\le H^{\eta/2}$ and
$qs\le H^{1-\eta/2}$. Moreover $q$ is the first $D$-divisor of $qs$:
any earlier divisor of $qs$ would divide $n-b$.

For each admissible $s$, the quotient $h$ lies in an interval of length
$H/(qs)\ge H^{\eta/2}\ge y^5$. By (2), the number of good points in
this cell is at most
$$
 \frac{CH}{\log y}
 \sum_{\substack{P^+(s)\le y\\\operatorname{first}_D(qs)=q}}
                         \frac1{qs}.
 \tag{5}
$$
Here $P^+(1)=1$, and enlarging the sum by dropping its size restrictions
only increases the bound.

The geometric valuation model on primes at most $H$ gives the exact
identity
$$
 Z_H e_q=
 \sum_{\substack{P^+(m)\le H\\\operatorname{first}_D(m)=q}}\frac1m.
 \tag{6}
$$
Indeed coherence translates all full first-kill cells to those of the
zero-residue system. Every integer in this smooth model has mass
$1/(Z_Hm)$, and the relevant divisibility event has Haar probability
$e_q$. Every admissible $qs$ in (5) occurs in (6).
Combining (3)--(6) and summing only the selected cells proves
$$
 \frac NH\ll\frac\tau\delta+\frac\delta\eta+H^{-3\eta/20},
 \tag{7}
$$
where $N$ denotes the count on the left of (1).

### Optimization with no hidden interval-length restriction

If $F_q\ne\varnothing$, no earlier modulus divides $q$. The atom $q$
in the geometric model on primes at most $q$ therefore shows
$$
 e_q\ge\frac1{qZ_q}\ge\frac1{q^2},
$$
since $Z_q\le\prod_{m=2}^q(1-1/m)^{-1}=q$. If the counted set is
nonempty, a selected $q\le H^{1-\eta}$ consequently gives
$\tau\ge H^{-2(1-\eta)}$.

Set $L=\log(1/\tau)$. If $L\ge20/\eta$, take $\delta=2/L$.
Then $\delta\le\eta/10$ and
$$
 y=H^{2/L}\ge e^{1/(1-\eta)}>2.
$$
All three terms in (7) are $O(1/(\eta L))$: the first is
$Le^{-L}/2$, and the last is at most
$\exp(-3\eta L/(40(1-\eta)))$. For smaller $L$, the trivial bound
suffices after enlarging the absolute constant. This proves (1).

## Natural density with any fixed power delay

For every infinite coherent family and every $0<\eta\le1/2$, the set
$$
 B_\eta=\{n\ge1:\exists q\le n^{1-\eta},\ n\equiv\alpha\pmod q\}
$$
has **natural density**
$\beta=\mu(\bigcup_q C_q)$, uniformly over the coherent center.
Equivalently, every activation rule $n\ge q^{1+\varepsilon}$,
$\varepsilon>0$, has this conclusion. Exponents corresponding to
$\eta>1/2$ follow by squeezing between a fixed finite prefix and
$B_{1/2}$.

To prove the assertion, let $q(n)$ be the least full covering modulus.
If some modulus is power-active at $n$, so is $q(n)$. The difference
from a fixed finite power-delayed prefix is therefore contained in the tail
first-kill cells with $q(n)\le n^{1-\eta}$. Their total Haar mass tends
to zero as the prefix increases. Apply (1) on $[1,X]$, with selected
tail cells and cutoff $q\le X^{1-\eta}$. This makes the omitted upper
counting density uniformly small. Finite prefixes have their periodic
densities, uniformly in the center, proving the claim.

For a finite family, the same argument with all cells selected gives
$$
 |B_\eta\cap[1,X]|\le f_\eta(\beta)X,
 \qquad H_{B_\eta}(X)\le f_\eta(\beta)H_{\lfloor X\rfloor}.
$$
The second inequality follows from the first by partial summation.

## A new natural-density case for the original activation

Let $P$ be the primitive core of a coherent modulus family; deleting
nonminimal multiples changes neither the full nor the delayed union.
The original set with activation $n\ge q$ has natural density $\beta$
if
$$
 \lim_{\eta\downarrow0}\limsup_{X\to\infty}
 \sum_{\substack{q\in P\\X^{1-\eta}<q\le X}}\frac1q=0.
 \tag{8}
$$
In particular,
$$
 |P\cap[1,t]|\ll t/\log t
 \tag{9}
$$
suffices, with no bound on prime-factor rank.

Indeed, after a fixed prefix, the first kills with $q\le X^{1-\eta}$
are bounded by (1). The remaining active classes contribute at most
$$
 X\sum_{\substack{q\in P\\X^{1-\eta}<q\le X}}1/q
$$
points up to $X$. First let $X\to\infty$, then exhaust the prefix,
and finally let $\eta\downarrow0$. Condition (8) proves finite-periodic
natural approximation. For (9), partial summation bounds the reciprocal
shell by
$O(\log(1/(1-\eta)))+O(1/\log X)$, establishing (8).

## The remaining subpower-quotient layer

For the original coherent union $B$, write
$$
 E_\eta=B\setminus B_\eta
       =\{n:n^{1-\eta}<q(n)\le n\}.
$$
Since every fixed $B_\eta$ has density $\beta$,
$$
 \overline{\operatorname{ld}}(E_\eta)
 =\overline{\operatorname{ld}}(B)-\beta
 \qquad(0<\eta\le1/2).
$$
Thus any excess persists in **every** arbitrarily thin power band next
to $q=n$. On the other hand, bounded-quotient first kills in a coherent
family are already logarithmically null by the primitive-core argument.
Any remaining excess must therefore occur at unbounded but subpower
quotients $n/q(n)$.

Neither primitive-core logarithmic nullity nor the estimate
$$
 H_{E_\eta}(X)
 \le\frac{\eta}{1-\eta}
          \sum_{\substack{q\le X\\q\in P}}\frac{\log q}{q}
       +O\left(\sum_{\substack{q\le X\\q\in P}}\frac1q\right)
$$
controls this layer after division by $\log X$. No continuity of
logarithmic density under the decreasing limit $\eta\downarrow0$ is
available. The unrestricted coherent case remains open here.

## A quotient-only natural estimate cannot close the gap

There are finite zero-residue systems with Haar footprint tending to
zero but a fixed positive proportion of first kills at unbounded,
subpower quotients. Thus the missing boundary layer requires a
specifically logarithmic argument, not merely an improvement of (1)
depending on the minimum quotient.

For an integer $K\ge2$, choose a finite prime pool $\mathcal P$ with
$p\ge K$ for every $p\in\mathcal P$ and
$\sum_{p\in\mathcal P}1/p\ge1$. Set
$$
 L=2\max\mathcal P,\qquad M=L/K,\qquad
 D=[N,NM]\cap\mathbb N,\qquad X=NL.
$$
Use the zero class at each modulus in $D$. If $X/2\le n\le X$ and
$p\in\mathcal P$ divides $n$, then
$$
 N\le n/p\le NM,\qquad n/(n/p)=p\ge K.
$$
The least $D$-divisor $q(n)$ is no larger than $n/p$ and no smaller
than $N$. Its quotient therefore lies in $[K,L]$. By finite periodic
counting, for fixed $\mathcal P$ these points occupy an asymptotic
fraction of $[1,X]$ at least
$$
 \frac12\left(1-\prod_{p\in\mathcal P}(1-1/p)\right)
 \ge\frac{1-e^{-1}}2.
$$
On the other hand, for fixed $M$ the Haar footprint of $D$ tends to
zero as $N\to\infty$: cover $D$ by finitely many dyadic modulus
windows and apply the proved [window bound](common_shift_blocks.md).
Replacing $D$ by its primitive core preserves the full union and the
least divisor at each point.

For each $K\to\infty$, choose $N$ sufficiently large that the footprint
is at most $1/K$, the displayed counting proportion is at least
$(1-e^{-1})/4$, and $\log L/\log N\le1/K$. All choices are finite
and can be made by taking the least integer satisfying these conditions.
The first-kill quotients now tend to infinity but satisfy
$\log(n/q(n))/\log n\to0$ uniformly on the counted points.
All moduli are distinct and all hits are active.

This is not a logarithmic-density anomaly: these are zero-residue
systems, for which the exact harmonic comparison is already proved.
The final interval supplies only bounded unnormalized harmonic mass.

## An unconditioned finite estimate would suffice: proved reduction

The following reduction removes conditioning on earlier first-kill cells
from a possible logarithmic estimate. The finite estimate assumed here
is **unproved**; neither the power-cutoff theorem nor the one-block
estimate establishes it.

Suppose there is a nondecreasing function $f:[0,1]\to[0,1]$, with
$f(t)\to0$ as $t\downarrow0$ and $f(0)=0$, such that every finite
coherent family $D$, every center $\alpha$, and every $X\ge2$ satisfy
$$
 H_{B_{D,\alpha}}(X)
 \le f(\beta_D)H_{\lfloor X\rfloor},
 \qquad
 \beta_D=\mu\left(\bigcup_{q\in D}
                   (\alpha+q\widehat{\mathbb Z})\right).
 \tag{10}
$$
Here $B_{D,\alpha}$ uses the original activation $n\ge q$.
Monotonicity of $f$ entails no loss: replace any proposed bound tending
to zero at zero by its nondecreasing envelope, and use the trivial bound
one where necessary.

**Conditional conclusion.** If (10) holds, every infinite coherent
family has finite-periodic approximation in upper logarithmic density,
and its delayed union has logarithmic density equal to its full Haar
measure. The reduction incurs no constants depending on the earlier
period in its final tail bound.

**Proof.** Let $U$ be the full union, $B$ its delayed integer union,
and $\beta=\mu(U)$. Fix a finite prefix $D_0$, with full union $U_0$,
delayed union $B_0$, Haar measure $\beta_0$, and period
$L=\operatorname{lcm}(D_0)$. Put $\tau=\beta-\beta_0$.
Except for finitely many integers, $B\setminus B_0$ lies in the
residues $r\pmod L$ that avoid $U_0$. Normalize $0\le r<L$ and fix
one such surviving residue.

Write $n=r+Lm$. A modulus $q$ can meet this residue precisely when
$$
 \alpha\equiv r\pmod{g_q},\qquad g_q=(q,L).
$$
For each compatible $q$, its pullback is one congruence in $m$ modulo
$d_q=q/g_q$, because $(L/g_q,d_q)=1$. These pullback congruences
are coherent. Indeed, for any finite compatible collection $q_j$, put
$Q=\operatorname{lcm}_j q_j$. Primewise comparison of valuations gives
$$
 (Q,L)=\operatorname{lcm}_j(q_j,L).
$$
Individual compatibility therefore implies
$\alpha\equiv r\pmod{(Q,L)}$, so the congruence
$Lm+r\equiv\alpha\pmod Q$ has an integer solution. Thus every finite
collection of pullbacks has a common solution; compactness supplies a
common center $\gamma_r\in\widehat{\mathbb Z}$. This argument does not
assume that $\alpha-r$ is divisible by $L$ in all profinite coordinates.

Collapse duplicate effective moduli $d_q$ and let $P_r$ be their
primitive core. Every effective modulus has a divisor in $P_r$, since
it has only finitely many positive divisors. Let $W_r$ be the standard
delayed union for $P_r$ and center $\gamma_r$, and let
$$
 V_r=\{m\ge1:r+Lm\in B\}
$$
be the actual projected deletion set. Taking the primitive core leaves
the full projected union and its standard delayed union unchanged.

For each $p\in P_r$, some original modulus $q_p$ has effective modulus
$p$; hence $q_p=(q_p,L)p\le Lp$. Consequently $m\ge p$ makes
$r+Lm\ge Lp\ge q_p$, proving $W_r\subseteq V_r$.
Conversely, if $m\in V_r\setminus W_r$, choose an active original
witness $q$, with effective modulus $d$, and then a primitive $p\mid d$.
The congruence $m\equiv\gamma_r\pmod p$ holds. Since $m\notin W_r$,
$$
 1\le m<p\le d\le q\le Lm+r\le L(m+1).
 \tag{11}
$$
For each $p$, at most one integer $m$ satisfies its congruence and
$0<m<p$. For $p>2L$, (11) also gives $1/m\le2L/p$. Therefore
$$
 H_{V_r\setminus W_r}(T)
 \le C_L+2L
     \sum_{\substack{p\in P_r\\p\le L(T+1)}}\frac1p
 =o(\log T).
 \tag{12}
$$
The last equality uses the proved logarithmic nullity of primitive sets
from [structured residues](structured_residues.md). Thus the discrepancy
caused by the changed activation is logarithmically null, despite the
possibly large fixed period $L$.

Let $\beta_r$ be the Haar measure of the full projected union. The map
$m\mapsto r+Lm$ identifies normalized Haar measure on
$\widehat{\mathbb Z}$ with conditional Haar measure on
$r+L\widehat{\mathbb Z}$. Hence
$$
 \frac1L\sum_{r\text{ surviving}}\beta_r=\tau.
 \tag{13}
$$
For each finite cutoff $T$, $W_r$ agrees below $T$ with the delayed
union of the finite family $P_r\cap[1,T]$. That finite family's Haar
footprint is at most $\beta_r$. Applying (10) and monotonicity of $f$ proves
$$
 \overline{\operatorname{ld}}(W_r)\le f(\beta_r),
 \qquad
 \overline{\operatorname{ld}}(V_r)\le f(\beta_r),
 \tag{14}
$$
where the second bound follows from (12). This is the complete passage
from the assumed finite estimate to the infinite projected family.

A fixed positive affine image $E\mapsto r+LE$ divides upper logarithmic
density by $L$: the difference between $1/(Lm+r)$ and $1/(Lm)$ is
absolutely summable. Summing (14) over the finitely many surviving
residues, and discarding the finitely many terms with $m=0$, gives
$$
 \overline{\operatorname{ld}}(B\setminus B_0)
 \le\frac1L\sum_{r\text{ surviving}} f(\beta_r).
$$
For any $0<\lambda\le1$, split this sum at $\beta_r=\lambda$.
Equation (13) shows that at most $L\tau/\lambda$ residues have
$\beta_r>\lambda$. Since $f\le1$, it follows that
$$
 \overline{\operatorname{ld}}(B\setminus B_0)
 \le f(\lambda)+\tau/\lambda.
$$
Taking $\lambda=\sqrt\tau$ when $\tau>0$ yields the period-independent
bound
$$
 \overline{\operatorname{ld}}(B\setminus B_0)
 \le f(\sqrt\tau)+\sqrt\tau.
 \tag{15}
$$
When $\tau=0$, every $\beta_r=0$, and (14) gives the same conclusion
with right side zero. Exhausting the prefix makes $\tau\to0$.
Thus the omitted logarithmic mass tends to zero, and finite periodicity
gives $\operatorname{ld}(B)=\beta$. $\square$

The primitive-root error in (12) may have constants depending on $L$;
they disappear before the prefix is exhausted because $L$ is fixed
when logarithmic density is taken. The remaining finite estimate (10)
must still be uniform over families and centers. No such estimate has
been proved here.
