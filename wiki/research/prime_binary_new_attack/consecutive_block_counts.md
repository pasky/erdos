---
name: research/prime_binary_new_attack/consecutive_block_counts
title: Upper counts for consecutive prime blocks under a rationality hypothesis
desc: |
  For Problem 251, a rational sum would make one weighted gap-tail value
  repeat about N_X/(d log X) times among starts X<p_n<=2X, and put most
  starts in a narrow carry window for about log_2 log X consecutive gaps.
  An upper comparison tolerates a loss c^K with c<2 at longer blocks.
  Exact model bounds, a signed majorant, a survivor count at the
  square-root sieve level and a signed deletion sum isolate the missing
  prime estimate.
created: 2026-10-16T18:43:22Z
updated: 2026-10-18T10:11:24Z
---

***

## Target and standing

[[problems/irrationality/E0251/_index|Problem 251]] asks whether
$S=\sum_{n\ge1}p_n2^{-n}$ is irrational. The question is open.

This page is Plasma AI's author-recorded research, not independently
reviewed. It turns the rational lattice of the
[[research/prime_binary_new_attack/proof_sketch|parity-prediction sketch]]
into two lower counts that a rational value would force, and states
upper comparisons for consecutive primes that would contradict them.
The sketch also records criteria asking for lower bounds on counts of
residue events; the criteria here ask for upper bounds, the direction in
which sieve methods give estimates. These comparisons still concern a
growing number of consecutive gaps, and none is proved. Theorem U8 allows
a comparison loss growing with the block length; a fixed factor is
sufficient, not necessary. Lemma U10 restates the count for the integers
surviving a sieve just below $\sqrt X$, and Lemma U11 and Proposition U12
show what a sieve stopped below that level leaves unestimated. Lemma U13
and Proposition U14 treat fixed nonnegative tuple majorants valid on all
finite sets, at the stated span. Proposition U15 gives a different exact
deletion sum, with a zero starting count and coefficients determined by
preceding primes and a periodic continuation. For
$K=\lceil A\log_2\log X\rceil$ with fixed $A>2$, Lemma U16 bounds those
coefficients above by a constant for sufficiently large $X$, and
Corollary U17 uses it to pay for the composites with two large prime
factors; the remaining sum is not a weaker target. The proofs below use
elementary algebra and the prime number theorem, directly and through
the mean-tail bound (T) of the sketch; the uniform additive estimate in
U12 uses a quantitative form of PNT. The independent-gap computations are about an
artificial model and are not estimates for primes.

## Notation

As on the sketch, $g_n=p_{n+1}-p_n$, $h_n=g_n/2$ for $n\ge2$, and

$$
G_n=\sum_{j\ge0}\frac{g_{n+j}}{2^{j+1}},\qquad
H_n=\frac{G_n}2,\qquad
Q_{n,L}=\sum_{0\le j<L}\frac{h_{n+j}}{2^{j+1}},\qquad
G_n=2Q_{n,L}+2^{-L}G_{n+L}.
$$

The last identity is (N) of the sketch, doubled. Put
$I_X=\{n:X<p_n\le2X\}$ and $N_X=|I_X|$. If $S=a/(2^sd)$ with $d$ odd,
Lemma A of the sketch gives $dH_n\in\mathbb Z$, that is
$G_n\in(2/d)\mathbb Z$, for every $n\ge\max(s+2,3)$. The mean-tail bound (T)
gives $\sum_{n\in I_X}G_{n+L}\le(1+\varepsilon)X$ for $X\ge X_0(\varepsilon)$
and $0\le L\le X/(\log X)^2$.

## Repeated tails

The truncation sketch's Rationality paragraph records that two equal
fractional parts $\{G_u\}=\{G_v\}$, $u<v$, already make $S$ rational. A
rational value forces many exact repetitions, at every scale of the gap
blocks.

**Proposition U1 (repeated tails).** Suppose $S=a/(2^sd)$ with $d$ odd, and
let $0<\varepsilon<1/8$. There is $X_1$, depending on $\varepsilon$ and $s$,
such that for every $X\ge X_1$ and every integer $0\le L\le X/(\log X)^2$
some $\gamma\in(2/d)\mathbb Z$ satisfies

$$
\#\{n\in I_X:\ G_n=\gamma,\ \gamma-2^{2-L}\log X\le2Q_{n,L}<\gamma\}
\ge\Bigl(\frac14-\varepsilon\Bigr)\frac{N_X}{d\log X}.
$$

In particular $S$ is rational exactly when $G_n=G_m$ for some $n\ne m$.

*Proof.* Take $X_1$ so large that $X_1\ge X_0(\varepsilon)$,
$\pi(X_1)\ge s+2$ and $N_X\ge(1-\varepsilon)X/\log X$ for $X\ge X_1$. Every
$n\in I_X$ then satisfies $n\ge\max(s+2,3)$, so $G_n\in(2/d)\mathbb Z$. By
(T) at shifts $0$ and $L$ and Markov's inequality, at most
$2(1+\varepsilon)X/(4\log X)\le(1/2+2\varepsilon)N_X$ starts in $I_X$ have
$G_n>4\log X$ or $G_{n+L}>4\log X$. The remaining starts, at least
$(1/2-2\varepsilon)N_X$ of them, have $G_n$ in
$(2/d)\mathbb Z\cap(0,4\log X]$, a set of at most $2d\log X$ points. Some
point $\gamma$ is taken at least $(1/4-\varepsilon)N_X/(d\log X)$ times.
For each such start, $0<G_{n+L}\le4\log X$ and the doubled identity (N)
place $2Q_{n,L}=\gamma-2^{-L}G_{n+L}$ in $[\gamma-2^{2-L}\log X,\gamma)$.

For the last sentence: if $S$ is rational, the count above exceeds $1$ for
large $X$; conversely $G_n=G_m$ with $n\ne m$ gives equal fractional parts,
hence rationality. $\square$

The case $L=0$ says that a single tail value is repeated at least
$(1/4-\varepsilon)N_X/(d\log X)$ times among the starts in $I_X$. For an
irrational $S$ all tails, and all their fractional parts, are distinct.

## A criterion free of the denominator

**Condition (AC).** There is a function $C:(0,1]\to[1,\infty)$ with
$\eta C(\eta)\to0$ as $\eta\to0$ such that for every $\eta\in(0,1]$ there
are arbitrarily large $X$ for which, with
$L=\lceil\log_2(4\log X/\eta)\rceil$, every real $\gamma$ satisfies

$$
\#\{n\in I_X:\ \gamma-\eta\le2Q_{n,L}<\gamma\}
\le C(\eta)\,\eta\,\frac{N_X}{\log X}.
\tag{AC}
$$

**Theorem U2.** Condition (AC) implies that $S$ is irrational.

*Proof.* Suppose $S=a/(2^sd)$ with $d$ odd. Choose $\eta\in(0,1]$ with
$\eta C(\eta)<1/(8d)$, and take $X\ge X_1(1/16)$ from Proposition U1 among
the scales of (AC), with $L\le X/(\log X)^2$. Then
$2^{2-L}\log X\le\eta$, so Proposition U1 puts at least
$(3/16)N_X/(d\log X)$ starts in one interval $[\gamma-\eta,\gamma)$, while
(AC) allows fewer than $(1/8)N_X/(d\log X)$ there. $\square$

Condition (AC) is one upper bound, the same for every denominator, on how
much the weighted block sums $2Q_{n,L}$ of consecutive primes concentrate
at a fixed small scale $\eta$. Their spread is of order $\log X$, so (AC)
asks for local densities within the factor $C(\eta)$ of the average, at a
block length $\log_2\log X+\log_2(1/\eta)+O(1)$. The function $C$ may grow
as $\eta\to0$, provided $\eta C(\eta)\to0$.

**Model computation.** Let $Z_0,Z_1,\ldots$ be independent geometric
variables on $\{1,2,\ldots\}$ with parameter $\rho\in(0,1)$, and let
$W=\sum_{j<L}Z_j2^{-j}$ be the model of $2Q_{n,L}$. For $L\ge1$,

$$
\sup_\gamma\Pr(\gamma-\eta\le W<\gamma)
\le \rho(\eta+2^{1-L})(1-\rho/2)^{-(L-1)}.
\tag{M1}
$$

To prove this, put $t=1-\rho$ and write each $Z_j$, for $j\ge1$, uniquely
as $2V_j+1+B_j$, with $V_j\ge0$ integral and $B_j\in\{0,1\}$. The joint
probability factors as

$$
\Pr(V_j=v,B_j=b)=\rho t^{2v+b}
=(1-t^2)t^{2v}\,\frac{t^b}{1+t}.
\tag{M2}
$$

Thus the bits are independent of the quotients and of one another, and
each bit value has probability at most $(2-\rho)^{-1}$. Conditional on
the quotients, the bits $B_1,\ldots,B_{L-1}$ give each residue of
$2^{L-1}W$ modulo $2^{L-1}$ exactly once. For any specified value of $W$,
at most one bit vector is possible, after which $Z_0$ is fixed and has
probability at most $\rho$. Every atom therefore has mass at most
$\rho(2-\rho)^{-(L-1)}$. An interval of length $\eta$ contains at most
$\eta2^{L-1}+1$ points of this lattice, proving (M1); the same bound is
immediate at $L=1$.

At $\rho=2/\log X$ and the length in (AC), (M1) is
$(2+o(1))\eta/\log X$ for every fixed $\eta>0$, so, for example, the
model satisfies (AC) with $C(\eta)=3$. This is a model calculation, not
an estimate for primes.

**Relation to the conditional comparison.** The comparison assumed in
[[problems/irrationality/E0251/claims/2026_09_07_ringer|Ringer's conditional claim]],
as recorded on the
[[research/prime_binary_series/truncation_certificates|truncation sketch]],
bounds nonnegative tests of the first $L$ consecutive offsets, within a
stated span, above by a fixed multiple of its model, at a length $L$ near
$\log_2\log X+\sqrt{\log_2\log X}$. Applied to the indicator of the event in
(AC) it would give (AC) if its model obeys a bound like the one just
computed; that matching is not carried out here, and the comparison is a
hypothesis, not a premise.

## The consecutive block count

Fix an odd $d$ and $\theta\in(0,1/8]$. For large $X$ put

$$
K=\Bigl\lceil\log_2\frac{4d\log X}{\theta}\Bigr\rceil,\quad M=2^K,\quad
R=\lfloor4d\log X\rfloor,\quad D=\lfloor16K\log X\rfloor,\quad
U_{n,K}=\sum_{0\le j<K}2^{K-1-j}h_{n+j}.
$$

Then $R/M\le\theta$. Let $r_d(u)\in\{1,\ldots,M\}$ be the least positive
residue of $-du$ modulo $M$, so $r_d(u)=M$ when $u\equiv0\pmod M$, and let

$$
B^\theta_d(X)=\#\{n\in I_X:\ p_{n+K}-p_n\le D,\ r_d(U_{n,K})\le R\}.
$$

**Proposition U3 (forced block count).** If $S=a/(2^sd)$ for some $a$ and
$s$, then $B^\theta_d(X)\ge(13/16-o(1))N_X$ as $X\to\infty$.

*Proof.* For large $X$ and $n\in I_X$ the numbers $c_j=dH_{n+j}$ are
positive integers with $c_{j+1}=2c_j-dh_{n+j}$, and iteration gives
$c_K+dU_{n,K}=Mc_0$. If $c_K\le R$, then, since $R<M$, the integer $c_K$ is
the least positive residue of $-dU_{n,K}$ modulo $M$, that is,
$c_K=r_d(U_{n,K})\le R$. By (T) at shift $K$ and Markov's inequality, at
most $d(1+o(1))X/(2R)=(1/8+o(1))N_X$ starts have $c_K>R$. Here (T),
valid for every fixed $\varepsilon>0$, gives the uniform $o(1)$ on its
whole stated range. If
$I_X=\{A,\ldots,B\}$, telescoping gives

$$
\sum_{n=A}^B(p_{n+K}-p_n)=\sum_{0\le j<K}(p_{B+j+1}-p_{A+j})=(1+o(1))KX,
$$

by the prime number theorem, since $K=O_{d,\theta}(\log\log X)$. So at most
$(1/16+o(1))N_X$ starts have span above $D$, and the remaining starts are
counted. $\square$

**Corollary U4.** If for some $\theta\in(0,1/8]$ and some constant
$\kappa<13/16$ the bound $B^\theta_d(X)\le\kappa N_X$ holds for arbitrarily
large $X$, then $S\ne a/(2^sd)$ for every $a$ and $s$. $\square$

In the independent model the counted event has probability at most
$\theta+o(1)$; the computation is Lemma U6 below. An upper comparison
within the factor $3/(4\theta)$ would therefore give
$B^\theta_d(X)\le(3/4+o(1))N_X$, and Corollary U4 applies with any
$\kappa\in(3/4,13/16)$. This factor can be made as large as desired by
shrinking the fixed $\theta$. The case $\theta=1/8$ has factor $6$.
Theorem U8 below also permits a shrinking window and a growing comparison
factor.

## An exact majorant keeping consecutiveness

Put $J=\lfloor D/2\rfloor$, $\Omega=\{2,4,\ldots,2J\}$ and $L_0=128K$, an
even integer. For $A=\{a_1<\dots<a_K\}\subseteq\Omega$ and $a_0=0$ let

$$
U(A)=\sum_{0\le j<K}2^{K-1-j}\frac{a_{j+1}-a_j}2,\qquad
V(A)=\{2,4,\ldots,a_K-2\}\setminus A,
$$

and call $A$ compatible when $r_d(U(A))\le R$. For a finite set
$H\subseteq\Omega$ put
$P_X(H)=\#\{x\in(X,2X]:x\text{ and }x+h\ (h\in H)\text{ are prime}\}$.
For any array $C(H)$ define

$$
F(C)=\sum_{A\text{ compatible}}\ \sum_{E\subseteq V(A),\,|E|\le L_0}
(-1)^{|E|}C(A\cup E)
=\sum_{j=K}^{K+L_0}(-1)^{j-K}\sum_{H\subseteq\Omega,\,|H|=j}w(H)C(H),
$$

where $w(H)$ counts the compatible $A\subseteq H$ with $|A|=K$ and
$\max A=\max H$, so $0\le w(H)\le\binom{|H|-1}{K-1}$.

**Lemma U5 (majorant).** $B^\theta_d(X)\le F(P_X)$. Moreover, for every set
$P\subseteq\Omega$ with $t$ elements, the polynomial
$\sum_{A\text{ compatible}}\sum_{E\subseteq V(A),|E|\le L_0}(-1)^{|E|}
\mathbf 1[A\cup E\subseteq P]$ exceeds the indicator that the first $K$
elements of $P$ form a compatible set (zero if $t<K$) by at least $0$ and at most
$\binom{K+L_0}{K-1}\binom t{K+L_0+1}$.

*Proof.* The regrouping uses $H=A\cup E$: then $\max H=\max A$, and every
$E=H\setminus A$ with this property lies in $V(A)$. For a set $P$, a
compatible $A\subseteq P$ with $m$ further elements of $P$ in $V(A)$
contributes $\sum_{e\le L_0}(-1)^e\binom me$, which is $1$ when $m=0$ and
$\binom{m-1}{L_0}\ge0$ when $m\ge1$, as $L_0$ is even. Only the first $K$
elements of $P$ have $m=0$. Since $\binom{m-1}{L_0}\le\binom m{L_0+1}$,
the excess is at most the number of pairs $(A,E)$ with $A,E\subseteq P$,
$|A|=K$, $|E|=L_0+1$ and $E\subseteq V(A)$. The union of such a pair has
$K+L_0+1$ elements and its maximum in $A$, and $A$ is fixed by its other
$K-1$ elements, which gives the bound. For a prime root $x\in(X,2X]$, with
$X>2$, let $P$ be the set of even $h\in\Omega$ with $x+h$ prime. If
$x=p_n$ and the span $p_{n+K}-p_n$ is at most $D$, its first $K$ elements
are $p_{n+j}-p_n$, $1\le j\le K$, since an even span at most $D$ is at
most $2J$; and $U$ of them is $U_{n,K}$. Summing the
pointwise inequality over prime roots gives $B^\theta_d(X)\le F(P_X)$.
$\square$

**Lemma U6 (reference value).** For independent geometric variables
$Z_0,\ldots,Z_{K-1}$ with parameter $\rho\in(0,1)$ put
$U=\sum_{j<K}2^{K-1-j}Z_j$ and $M=2^K$. Every residue $u$ satisfies

$$
\left(\frac{1-\rho}{2-\rho}\right)^K
\le\Pr(U\equiv u\pmod M)\le(2-\rho)^{-K}.
\tag{M3}
$$

In particular, for odd $d$ and $1\le R<M$,

$$
\Pr(r_d(U)\le R)\le\frac{R}{M}(1-\rho/2)^{-K}.
\tag{M4}
$$

For $\rho=2/\log X$ and $M_X(H)=N_X\rho^{|H|}$, the reference moments of
independent successes at the even offsets, the fixed-$\theta$ parameters
above consequently give

$$
\frac{F(M_X)}{N_X}\le
\frac{R}{M}(1-\rho/2)^{-K}
+\frac12\Bigl(\frac{32e}{129}\Bigr)^{K+L_0+1}
\le\theta+o(1).
\tag{M5}
$$

*Proof.* Apply (M2) to every $Z_j$ and condition on all its quotients.
Then
$U=C+\sum_{j<K}2^{K-1-j}B_j$ for a fixed integer $C$. The binary sum
maps the $2^K$ bit vectors bijectively onto the residues modulo $M$.
The probability of each vector lies between
$((1-\rho)/(2-\rho))^K$ and $(2-\rho)^{-K}$. Averaging over the quotients
proves (M3). Multiplication by $-d$ permutes the residues, giving (M4).
The bound is relative even for a very small set of residues; it is not
an additive discrepancy estimate.

For (M5), drop the span restriction when bounding the compatibility
probability by (M4). By Lemma U5 the excess has expectation at most
$\binom{K+L_0}{K-1}\binom J{K+L_0+1}\rho^{K+L_0+1}$. Use
$\binom{K+L_0}{K-1}\le2^{K+L_0}$, $\binom Jm\le(eJ/m)^m$ and
$J\rho\le16K$. Finally $K\rho\to0$ and $R/M\le\theta$. $\square$

This is a calculation for an artificial model. It omits every correlation
of the primes at odd primes and is not the Hardy–Littlewood model.

## The signed estimate and its size

With these parameters put $\Delta_d(X)=F(P_X)-F(M_X)$. Lemmas U5 and U6
give $B^\theta_d(X)\le(\theta+o(1))N_X+\Delta_d(X)$. Proposition U3 then
shows that a rational $S$ with odd denominator part $d$ forces
$\Delta_d(X)\ge(13/16-\theta-o(1))N_X$, while

$$
\Delta_d(X)\le\Bigl(\frac34-\theta\Bigr)N_X
\qquad\text{for arbitrarily large }X
\tag{SB}
$$

would contradict it. Statement (SB) is open for every odd $d$, including
$d=1$, and it is stronger than the count in Corollary U4. Through Lemmas
U5 and U6 it would give $B^\theta_d(X)\le(3/4+o(1))N_X$, which is the
hypothesis of Corollary U4 with any $\kappa\in(3/4,13/16)$. Write
$F(P_X)=B^\theta_d(X)+E_{\mathrm{act}}$ and
$F(M_X)=N_X\Pr(\text{compatible start})+E_{\mathrm{mod}}$, with both
excesses nonnegative. Lemma U6 bounds $E_{\mathrm{mod}}$; nothing here
bounds $E_{\mathrm{act}}$, which rare roots followed by many primes could
dominate.

The phase weights do not remove the large terms in this particular
expansion. The following count establishes that fact without assuming
equidistribution of the weights.

**Lemma U7 (a weighted layer and adverse errors).** At the fixed-$\theta$
parameters, the $j=K$ layer of $F(M_X)$ is
$\gg_{d,\theta}(\log X)^4N_X$. Moreover the termwise adverse-error sum

$$
\mathcal A_X=
\sum_{j=K}^{K+L_0}\ \sum_{|H|=j}
w(H)\,[(-1)^{j-K}(P_X(H)-M_X(H))]_+
$$

satisfies $\mathcal A_X\gg_{d,\theta}(\log X)N_X$. In particular the
always-valid inequality $\Delta_d(X)\le\mathcal A_X$ cannot establish
(SB) through an $O(N_X)$ bound on $\mathcal A_X$.

*Proof.* Write the half-offsets of a $K$-set as
$1\le x_1<\dots<x_K\le J$. Then

$$
U=x_K+\sum_{i=1}^{K-1}2^{K-1-i}x_i.
$$

Choose the first $K-1$ half-offsets in $[1,J-M]$ and the last in
$[J-M+1,J]$. For each first choice, the $M$ last choices run through
all residues of $U$ modulo $M$, exactly $R$ of which are compatible.
There are therefore at least $R\binom{J-M}{K-1}$ compatible sets.
This construction is available for large $X$, because $M/J=O_{d,\theta}(1/K)$.
Its proportion among all $K$-sets is

$$
\frac{R\binom{J-M}{K-1}}{\binom JK}
=\frac{RK}{J}
\prod_{i=0}^{K-2}\left(1-\frac{M-1}{J-1-i}\right)
=\frac{RK}{J}\exp\left(-\frac{MK}{J}+o(1)\right).
\tag{M6}
$$

Here $RK/J\to d/2$ and $MK/J\le d/\theta+o(1)$, so (M6) is bounded
below by a positive constant depending only on $d,\theta$. The unweighted
layer obeys

$$
\binom JK\rho^KN_X\ge\Bigl(\frac{J\rho}K\Bigr)^KN_X
=(1-o(1))16^KN_X
\ge(1-o(1))\Bigl(\frac{4d\log X}{\theta}\Bigr)^4N_X.
$$

The equality uses $J=\lfloor8K\log X\rfloor$ and
$\rho=2/\log X$. Combining it with (M6) proves the first assertion.

For the second, force half-offsets $1,2$ into $A$, omit half-offset $3$,
choose its other $K-3$ early half-offsets from
$[1,J-M]\setminus\{1,2,3\}$, and choose its last half-offset in the same
terminal interval of length $M$. There are exactly
$R\binom{J-M-3}{K-3}$ compatible choices of this form. For each put
$H=A\cup\{6\}$, in physical offsets. These are distinct $(K+1)$-sets,
$6\in V(A)$, and $w(H)\ge1$. Since $H$ contains $2,4$, the root and
these two shifts cover every residue modulo $3$. Thus $P_X(H)=0$ for
$X>3$. The layer $j=K+1$ has negative sign, so each of these sets
contributes at least $N_X\rho^{K+1}$ to $\mathcal A_X$. Consequently

$$
\frac{\mathcal A_X}{N_X}
\ge R\binom{J-M-3}{K-3}\rho^{K+1}
\gg_{d,\theta}\frac{\binom JK\rho^K}{(\log X)^3}
\gg_{d,\theta}\log X.
\tag{M7}
$$

For the middle inequality, the ratio of binomial coefficients is
$(K/J)^3\exp(-MK/J+o(1))$, while
$RK/J\to d/2$, $K/J\sim1/(8\log X)$ and $\rho=2/\log X$.
All these statements concern sufficiently large $X$, so $K\ge3$ and
the displayed choices exist. $\square$

Thus cancellation is essential for this reference and this expansion.
The first conclusion also shows that a bound obtained by assigning the
same relative error budget to every weighted layer and then taking
absolute values can have an $O(N_X)$ total budget only if that relative
budget is $O((\log X)^{-4})$, and possibly smaller because of higher
layers. This is a limitation of that error accounting, not a necessity
theorem for every proof of (SB). The second conclusion is stronger for
the precise adverse-error sum above: already known zero tuple counts
make its desired bound false. A uniform termwise approximation by
$M_X(H)$ is impossible for the same reason. A Hardy--Littlewood
reference carries the singular series and makes these inadmissible
tuples zero; the Bernoulli array does not.

No implication from (SB) to a uniform prime-tuples conjecture has been
proved. Nor does a uniform tuples hypothesis automatically identify this
Bernoulli reference with the required arithmetic reference: their
weighted difference would still have to be estimated. Lemma U7 excludes
neither a direct signed estimate nor a different majorant.

Two shortcuts are invalid. Replacing every tuple count by an upper bound
fails, because the layers with $j-K$ odd enter with a negative sign and need
lower bounds; the first such layer already prescribes $K+2$ primes.
Dropping the factors that exclude intervening primes counts arbitrary
$K$-subsets of nearby primes:
[[research/prime_binary_new_attack/critical_length_obstructions|Proposition O6
bounds that total count below]] by a quantity of order $4^KK^{-3/2}N_X$,
against at most $N_X$ consecutive blocks.

## What the upper comparisons need

The following extension makes the tolerable loss explicit.

**Theorem U8 (comparison with a growing loss).** Fix an odd $d$. Let
$K=K(X)$ be positive integers with $K=o(\log X)$ and
$2^K>R=\lfloor4d\log X\rfloor$ for large $X$, and put
$D=\lfloor16K\log X\rfloor$. Write $B_d(X;K)$ for the same block count
as $B^\theta_d(X)$, using these $K,R,D$. Let $\mathcal E_{d,X,K}$ be
the corresponding event for independent geometric half-gaps of parameter
$\rho=2/\log X$: their first $K$ physical gaps have sum at most $D$
and their least positive endpoint residue is at most $R$.

Suppose that along arbitrarily large $X$ there are factors $F_X\ge1$
such that

$$
\frac{B_d(X;K)}{N_X}
\le F_X\Pr(\mathcal E_{d,X,K})+o(1),
\qquad
\frac{F_X\log X}{2^K}\longrightarrow0.
\tag{GC}
$$

Then $S\ne a/(2^sd)$ for every $a$ and $s$. In particular, it is
sufficient to prove the first inequality with $F_X=Cc^K$ for any fixed
$1\le c<2$, $C>0$, at

$$
K=\lceil A\log_2\log X\rceil,\qquad
A>\frac1{\log_2(2/c)}.
\tag{M8}
$$

Such a statement for every fixed odd $d$, with constants allowed to
depend on $d$, proves irrationality.

*Proof.* If $S=a/(2^sd)$, the proof of Proposition U3 gives
$B_d(X;K)\ge(13/16-o(1))N_X$ at these parameters too: (T) is uniform at
shift $K$, and $K=o(\log X)$ is well within both its range and the
uniform PNT telescoping estimate for the span. On the other hand,
(M4), with the span dropped, gives

$$
\Pr(\mathcal E_{d,X,K})
\le\frac{R}{2^K}(1-1/\log X)^{-K}
\le(4d+o(1))\frac{\log X}{2^K}.
$$

Together with (GC), this makes $B_d(X;K)/N_X=o(1)$, a contradiction.
For (M8), the second quantity in (GC) is at most
$C(\log X)^{1-A\log_2(2/c)}$, which tends to zero. Choose the scales
past the arbitrary preperiod $s$; $d=1$ is included. $\square$

The theorem does not require an actual model comparison if a direct
bound $B_d(X;K)/N_X\le Cc^K R/2^K+o(1)$ is available at (M8); the same
proof applies. It permits every fixed exponential loss below $2^K$ by
increasing the coefficient of $\log_2\log X$. At a loss $2^K$ the
displayed estimate is only $O(\log X)$ and does not yield a
contradiction. That threshold concerns this comparison argument, not
every possible irrationality proof.

## A reference incorporating small odd primes

The relative phase estimate is not restricted to independent gaps at
every even offset. It survives a periodic restriction on allowable
locations, followed by independent thinning. This gives a way to remove
the specific arithmetic obstruction of Lemma U7 from the reference;
it supplies no comparison with actual primes.

**Lemma U9 (odd-period reference).** Let $q$ be odd, let
$\mathcal R\subseteq\mathbb Z/q\mathbb Z$ be nonempty with
$|\mathcal R|=a$, and start at any residue in $\mathcal R$. In the
half-offset coordinate, each later site with residue in $\mathcal R$
is independently a success with probability $p\in(0,1)$; other sites
are forbidden. Let $Z_0,\ldots,Z_{K-1}$ be the first $K$ successive
gaps between successes, and put $t=(1-p)^a$. For odd $d$ and
$1\le R<2^K$,

$$
\Pr\!\left(r_d\!\left(\sum_{j<K}2^{K-1-j}Z_j\right)\le R\right)
\le\frac{R}{2^K}\left(1-\frac{1-t}{2}\right)^{-K}.
\tag{M9}
$$

In particular, choose $p=2q/(a\log X)$. If $qK=o(\log X)$, the right
side is $(1+o(1))R/2^K$, uniformly in the starting residue and in the
choice of $\mathcal R$. The conclusions of Theorem U8 therefore also
hold with this reference event in place of its independent-gap event,
provided the stated comparison with actual primes is proved.

*Proof.* From a current allowed residue, list the $a$ allowed positive
offsets in one period as $r(1)<\cdots<r(a)\le q$. A next gap has the
form $Z=qV+r(\ell)$, where

$$
\Pr(V=v,\ell=l)=p(1-p)^{av+l-1}
=(1-t)t^v\frac{p(1-p)^{l-1}}{1-t}.
$$

Thus $V$ has the geometric law on $\{0,1,\ldots\}$ with parameter
$1-t$, independently of the rank $\ell$ and the current residue.
Successive future sites are independent. Consequently the variables
$V_j$ are independent of one another and of the entire path of
residues, which depends only on the ranks. Write $V_j=2T_j+B_j$.
As in (M2), the bits are independent of the quotients and the residue
path, and their two probabilities are $1/(1+t)$ and $t/(1+t)$.
After conditioning on that path and all $T_j$, the weighted sum is

$$
C+q\sum_{j<K}2^{K-1-j}B_j.
$$

Since $q$ is odd, the bit vectors map bijectively to the residues
modulo $2^K$. Each vector has probability at most $(1+t)^{-K}$.
Multiplication by $-d$ also permutes these residues, proving (M9).
Finally $1-t\le ap=2q/\log X$, so the correction factor in (M9)
is $1+o(1)$ when $qK=o(\log X)$. This condition also makes $p<1$
eventually. The argument for Theorem U8 uses only this phase bound
and drops the reference span restriction, so it applies unchanged.
$\square$

For example, take $q$ to be a product of small odd primes and
$\mathcal R$ the units modulo $q$. A prime root $x>q$ has starting
half-coordinate $x\,2^{-1}\pmod q$ in $\mathcal R$, and forbidden
sites correspond exactly to shifts divisible by a prime factor of
$q$. Thus the model assigns zero probability to the tuples used in
(M7) whenever $3\mid q$. The lemma permits fixed $q$, or growing $q$
with $qK=o(\log X)$; it does not permit an unrestricted product of
all primes up to the square root of $X$. Independent thinning after
these exclusions is a model assumption, not a theorem about primes.

## Survivors at the square-root cutoff

The count $B_d(X;K)$ of Theorem U8 can be posed for any finite set of odd
integers. At a sieving level just below $\sqrt X$ the surviving integers
differ from the primes by $O(N_X/K^2)$ elements, and each deleted element
changes the count by at most $K+1$. This gives an exact survivor form of
step 5 of the sketch. Lemma U11 and Proposition U12 then record what a sieve
stopped below that level would have to supply. None of the three results
estimates the count.

Fix an odd $d$ and the parameters $K,M,R,D$ of Theorem U8, and assume
moreover $K\to\infty$ and $K^2\le\log X$; the choice
$K=\lceil A\log_2\log X\rceil$ qualifies. Put $J_X=(X,2X+D]\cap\mathbb Z$.
For a finite set $T$ of odd integers and $x\in T$, let $t_1<t_2<\cdots$ be
the elements of $T$ above $x$, put $t_0=x$, and let $\beta_T(x)=1$ when
$t_K$ exists, $t_K-x\le D$ and

$$
r_d\Bigl(\sum_{0\le j<K}2^{K-1-j}\,\frac{t_{j+1}-t_j}2\Bigr)\le R ;
$$

otherwise $\beta_T(x)=0$. Put
$C(T)=\sum_{x\in T,\ X<x\le2X}\beta_T(x)$.

For the primes, $C(\mathbb P\cap J_X)=B_d(X;K)$, where $\mathbb P$ is the
set of primes. If a prime $p_n\in(X,2X]$ has $p_{n+K}-p_n\le D$, its next $K$
primes lie in $J_X$ and are the first $K$ elements of $\mathbb P\cap J_X$
above it; otherwise both counts give the start zero. Moreover $\beta_T(x)$
depends only on $T\cap[x,x+D]$, since the event asks for $K$ elements of $T$
in $(x,x+D]$ and uses the first $K$ of them.

**Lemma U10 (survivor transfer).** Put $z=X^{1/2-1/K^2}$, and let $T_z$ be
the set of $m\in J_X$ with no prime factor at most $z$. Then, for large $X$,

$$
\bigl|C(T_z)-B_d(X;K)\bigr|\le(K+1)E_X\ll\frac{N_X}K ,
$$

where $E_X\ll N_X/K^2$ is the number of composite elements of $T_z$. The
implied constants are absolute, so the bound is uniform in $d$.

*Proof.* Deleting one element $m$ from a finite set $T$ can change
$\beta_T(x)$ only at $x=m$ and at the elements $x<m$ of $T$ for which $m$
is one of the first $K$ elements above $x$. There are at most $K$ of the
latter, and every $\beta$ lies in $\{0,1\}$, so one deletion changes $C$ by
at most $K+1$. For large $X$ every prime in $J_X$ exceeds $z$ and lies in
$T_z$, and the other elements of $T_z$ are composite; deleting them one at a
time gives the first inequality.

For large $X$ one has $D\le X$, so $J_X\subseteq(X,3X]$, and $z^3>3X$ since
$K\ge3$. A composite element of $T_z$ therefore has exactly two prime
factors $q\le r$, both above $z$, with $q\le\sqrt{3X}$. By the prime number
theorem $\pi(t)\le2t/\log t$ for large $t$, and $3X/q\ge\sqrt{3X}$ gives
$\log(3X/q)\ge\frac12\log X$, so

$$
E_X\le\sum_{z<q\le\sqrt{3X}}\pi\Bigl(\frac{3X}q\Bigr)
\le\frac{12X}{\log X}\sum_{z<q\le\sqrt{3X}}\frac1q ,
$$

with $q$ running over primes. Partial summation and
$\pi(t)\ll t/\log t$ bound the last sum by
$O(1/\log X+\log(\log\sqrt{3X}/\log z))$. Indeed, with
$b=\sqrt{3X}$ it is at most
$\pi(b)/b+\int_z^b\pi(t)t^{-2}\,dt$; the omitted lower endpoint is
nonpositive. Here
$\log\sqrt{3X}/\log z=(1+\log3/\log X)/(1-2/K^2)$, whose logarithm is at
most $4/K^2+2/\log X$ for $K\ge2$. Since $K^2\le\log X$, this gives
$E_X\ll X/(K^2\log X)\ll N_X/K^2$. $\square$

Hence, under rationality, the forced count $(13/16-o(1))N_X$, which the proof
of Proposition U3 gives at these parameters (Theorem U8), holds for $C(T_z)$ as
well, and an upper bound $C(T_z)\le\frac34N_X$ along arbitrarily large $X$
would contradict it. The two counts differ by $o(N_X)$, so this is a change of
setting, not progress on the estimate. Primality enters only through the
deleted composites, and the sieving level $z$ lies far beyond the range in
which a sieve evaluates configurations of $K$ survivors.

In indicator form, with $\chi(m)=\mathbf 1[m\in T_z]$ and the offset sets
$A=\{a_1<\dots<a_K\}\subseteq\{2,4,\ldots,2\lfloor D/2\rfloor\}$ and
$V(A)=\{2,4,\ldots,a_K-2\}\setminus A$ of Lemma U5,

$$
C(T_z)=\sum_{X<x\le2X}\chi(x)\sum_{A\text{ compatible}}
\prod_{a\in A}\chi(x+a)\prod_{v\in V(A)}\bigl(1-\chi(x+v)\bigr).
$$

For each odd $x$ at most one inner term is nonzero, the one listing the
first $K$ survivors above $x$, and every even $x$ contributes zero.
Consecutiveness enters only through the factors $1-\chi(x+v)$.

## Stopping the sieve below the square root

**Lemma U11 (deletions by one prime).** Let $\ell>D$ be a prime, let
$T_{<\ell}$ be the set of $m\in J_X$ with no prime factor below $\ell$, and
let $T_{\le\ell}$ be its subset of elements not divisible by $\ell$. For
$m\in T_{<\ell}$ put
$\Psi_\ell(m)=C(T_{<\ell}\setminus\{m\})-C(T_{<\ell})$. Then

$$
C(T_{\le\ell})=C(T_{<\ell})+\sum_{m\in T_{<\ell},\ \ell\mid m}\Psi_\ell(m),
\qquad|\Psi_\ell(m)|\le K+1 .
$$

If moreover $\ell<X$ and $\ell^3>3X$, every $m\in T_{<\ell}$ divisible by
$\ell$ is $\ell r$ with $r\ge\ell$ prime. Consequently, if $D<y<z<X$ and
$y^3>3X$, and
$T_w$ denotes the set of $m\in J_X$ with no prime factor at most $w$, then

$$
C(T_z)=C(T_y)+\sum_{y<\ell\le z}\ \sum_{\substack{r\ge\ell\ \text{prime}\\
\ell r\in J_X}}\Psi_\ell(\ell r),
\tag{BD}
$$

with $\ell$ running over primes.

*Proof.* Two odd multiples of $\ell$ differ by at least $2\ell>D$, so a
window $[x,x+D]$ contains at most one element of
$E=\{m\in T_{<\ell}:\ell\mid m\}$. Since $\beta_T(x)$ depends only on
$T\cap[x,x+D]$, deleting all of $E$ changes $\beta(x)$ exactly as deleting
the element of $E$ in that window would, and not at all if there is none.
Summing over $x$ gives the identity, and the bound on $\Psi_\ell$ is the
one-deletion bound from the proof of Lemma U10. If $\ell\mid m$ with
$m\in T_{<\ell}$, then $m=\ell r$, where $r$ has no prime factor below $\ell$
and $r\le3X/\ell<\ell^2$; also $r>1$, since $m>X>\ell$. So $r$ is a prime at
least $\ell$. Applying the identity to the primes of $(y,z]$ in increasing
order gives (BD). $\square$

For example $y=X^{2/5}$ satisfies $D<y$ and $y^3>3X$ for large $X$. The
function $\Psi_\ell(m)$ is explicit. It is $-\beta(m)$ when $m\in(X,2X]$,
plus the change of $\beta(x)$ at each of the at most $K$ survivors $x$ below
$m$ that have $m$ among their first $K$ successors. If $m$ is the $j$th
successor of $x$, $1\le j\le K$, its deletion merges the two gaps beside $m$
and brings in the old $(K+1)$st successor. In the half-gaps
$h_0,\ldots,h_K$ of the old block of $K+1$ gaps after $x$, the weighted sum
changes from $\sum_{0\le i<K}2^{K-1-i}h_i$ by
$\sum_{j\le i<K}2^{K-1-i}h_i+h_K$, the sum being empty when $j=K$, and the
span must be checked again.

**Proposition U12 (what a stopped sieve leaves).** Let $y=X^{2/5}$, and let
$w=X^{1/s}$ with $3\le s\le\log\log X$.

1. The double sum in (BD) has $(\log(3/2)+o(1))N_X$ terms, each of absolute
   value at most $K+1$.
2. At least $(\log(s-1)-o(1))N_X$ elements of $T_w\cap(X,2X]$ are
   composite, uniformly in $s$. So $C(T_w)$ and $B_d(X;K)$ are joined by at
   least that many single deletions, each changing the count by at most
   $K+1$.

*Proof.* Both parts count products $\ell r\in(X,2X]$ of primes $\ell\le r$
with $\ell\in(X^a,X^b]$, $b\le1/2$. For each such $\ell$, every prime
$r\in(X/\ell,2X/\ell]$ qualifies, because $X/\ell\ge\sqrt X\ge\ell$. The
quantitative prime number theorem
$\pi(t)=\operatorname{Li}(t)+O(t/(\log t)^3)$, applied to $r$ and, by
partial summation, to $\ell$, gives the number of such products as

$$
\sum_{X^a<\ell\le X^b}\frac{X}{\ell\log(X/\ell)}+o(N_X)
=\frac X{\log X}\int_a^b\frac{du}{u(1-u)}+o(N_X)
=N_X\left(\log\frac{b(1-a)}{a(1-b)}+o(1)\right),
$$

uniformly in the two ranges used below, where $a\ge1/\log\log X$ and
$b\le1/2$. For completeness, with $L=\log X$, the error after division by
$X/L$ is
$O((1+\log(1/a))/L+1/(a^2L^2))=o(1)$ in these ranges. The first term
includes replacing each interval prime count by its leading term and
$X/L$ by $N_X$; the second follows by integrating the error in the prime
count for $\ell$. Thus the error is additive $o(N_X)$ even when
$\log(s-1)$ grows; qualitative PNT alone would not justify that uniform
additive error. With
$a=2/5$ and $b=1/2-1/K^2$ the count is
$(\log(3/2)+o(1))N_X$; the products in $(2X,2X+D]$ number at most $D+1$.
With $a=1/s$ and $b=1/2$ it is $(\log(s-1)+o(1))N_X$, and every such product
is a composite element of $T_w$. The bounds on single deletions are those of
Lemmas U10 and U11. $\square$

So the stopped identity (BD) at $y=X^{2/5}$ has a correction whose trivial
bound is of order $KN_X$. Its base term $C(T_y)$ counts the same event on
the primes together with the products of two primes above $X^{2/5}$, and no
estimate for that count is available either. At a cutoff $X^{1/s}$ with
$s$ growing, the semiprimes alone contribute at least
$(\log(s-1)-o(1))N_X$ deletions. Charging $K+1$ for each of these already
gives an allowance of order $KN_X\log s$; further composite survivors
increase that allowance. This is not a lower bound for the actual total
variation. A useful estimate must improve this accounting, for example by
bounding how often a deletion changes the event or by cancellation in the
signed sum. Each $\Psi_\ell(\ell r)$ in (BD) is a
function of the survivor pattern in $[\ell r-D,\ell r+D]$, so estimating the
sum is an estimate for the joint law of about $K$ survivors near the
semiprimes $\ell r$: the same kind of input as step 5 of the sketch.
Bilinear (Type II) estimates bound sums $\sum\alpha_\ell\beta_rf(\ell r)$
for specified classes of coefficients $f$, such as additive characters or
indicators of progressions. Here $f=\Psi_\ell$ is itself determined by the
survivors near $\ell r$, and it depends on $\ell$ as well. No estimate for
this class of coefficients is supplied by the inspected sources. The
stopped decomposition therefore re-expresses the missing estimate; no
bound for its base term or correction is proved here.

**Rooting at every integer.** For every integer $x\ge1$ put
$F(x)=\sum_{k\ge0}2^{-(\pi(x+k)-\pi(x))}$. Then

$$
2^{\pi(x)}S=\sum_{p\le x}p\,2^{\pi(x)-\pi(p)}+x+F(x),\qquad
F(x+1)=2^{\mathbf 1_{\mathbb P}(x+1)}\bigl(F(x)-1\bigr),
$$

and $F(p_n)=2G_n$. At $x=1$ the first identity reads
$S=1+\sum_{m\ge1}2^{-\pi(m)}$, the tail-sum form of the mean of the least
quadratic nonresidue recorded on the problem page. For the first identity,
split $2^{\pi(x)}S$ at $x$; for the primes $p>x$ write $p=x+(p-x)$ and
$p-x=\#\{k\ge0:x+k<p\}$, and use
$\sum_{p>x+k}2^{\pi(x)-\pi(p)}=2^{-(\pi(x+k)-\pi(x))}$. The recurrence
follows by separating the term $k=0$. So a rational value with odd
denominator part $d$ puts $dF(x)$ in $\mathbb Z$ at every large integer $x$,
prime or not, and the block event could be rooted at every integer, removing
the primality of the root. This does not help as it stands. The integers of
$[p_n,p_{n+1})$ all have the same next $K$ primes, so a count rooted at
integers weights the start $n$ by the gap $g_n$. The analogue of Proposition
U3 then needs bounds of order $X\log X$ for sums such as
$\sum_{n\in I_X}g_nH_{n+K}$ and $\sum_{n\in I_X}g_n(p_{n+K}-p_n)$, which
correlate a gap with itself and with later gaps. The prime number theorem
does not give them, and
[[../library/primes/stadlmann_2022_mean_square_gap_between_primes/theorem_1|Stadlmann's unconditional mean-square bound $x^{1.23+\varepsilon}$]],
the input for a Cauchy–Schwarz bound, exceeds $X\log X$ by a power of $X$.

## Nonnegative majorants

Lemma U5 keeps consecutiveness through signed layers, and Lemma U7 shows
that the signs matter. The next two results concern fixed nonnegative
combinations of tuple indicators which majorize the event on every finite
set. Such a majorant counts every root whose window contains some
compatible set of later elements, and in the reference model almost every
root qualifies. The universal majorization assumption and the span
$D=\lfloor16K\log X\rfloor$ are part of the result.

Keep the parameters of Theorem U8, let $J=\lfloor D/2\rfloor$ and
$\Omega=\{2,4,\ldots,2J\}$, and use $C$, $\beta_T$ and the compatible sets
of Lemmas U5 and U10. A *nonnegative tuple majorant* is a function

$$
F_T(x)=\sum_{H\subseteq\Omega}w_H\prod_{h\in H}\mathbf 1_T(x+h),
\qquad w_H\ge0\ \text{fixed},
$$

with $F_T(x)\ge\beta_T(x)$ for every finite set $T$ of odd integers and
every $x\in T$. Then
$B_d(X;K)\le\sum_Hw_H\#\{x\in\mathbb P\cap(X,2X]:x+H\subseteq\mathbb P\}$,
an estimate that needs only upper bounds for counts of prime tuples.

**Lemma U13 (majorants see every compatible subset).** Let $F$ be a
nonnegative tuple majorant, $T$ a finite set of odd integers and $x\in T$.
If $\{h\in\Omega:x+h\in T\}$ contains a compatible $K$-set $A$, then
$F_T(x)\ge1$, whether or not $x+A$ consists of the first $K$ elements of $T$
above $x$.

*Proof.* Put $T'=\{x\}\cup(x+A)$. The first $K$ elements of $T'$ above $x$
are $x+A$, their span is $\max A\le2J\le D$, and $A$ is compatible, so
$\beta_{T'}(x)=1$ and $F_{T'}(x)\ge1$. Every product equal to one in
$F_{T'}(x)$ is equal to one in $F_T(x)$, because
$T'\cap(x+\Omega)\subseteq T\cap(x+\Omega)$, and the weights are
nonnegative. So $F_T(x)\ge F_{T'}(x)\ge1$. $\square$

**Proposition U14 (every phase from alternating parities).** Let $K\ge3$
and let $I_1<I_2<\cdots<I_K$ be sets of positive integers, each element of
$I_i$ below each element of $I_{i+1}$, such that $I_1$ meets all four
classes modulo $4$, $I_i$ meets both parities for $2\le i\le K-1$, and $I_K$
is nonempty. Then for every residue $u$ modulo $2^K$ there are $x_i\in I_i$
with

$$
x_K+\sum_{1\le i<K}2^{K-1-i}x_i\equiv u\pmod{2^K}.
$$

Consequently, in the independent reference of Lemma U6, with each even
offset in $\Omega$ a success independently with probability
$\rho=2/\log X$, the successes contain a compatible $K$-set with
probability at least $1-O(e^{-K/6})$. Every nonnegative tuple majorant
therefore has reference expectation at least $1-O(e^{-K/6})$.

*Proof.* Choose any $x_K\in I_K$. For $b=0,1,\ldots,K-3$ in turn, the term
$2^bx_{K-1-b}$ is the only one not yet chosen that can change bit $b$ of the
sum, since the remaining terms have weights at least $2^{b+1}$; choose
$x_{K-1-b}\in I_{K-1-b}$ with the parity that makes bit $b$ agree with $u$.
Finally $2^{K-2}x_1$ modulo $2^K$ depends only on $x_1$ modulo $4$ and
takes each of the values $0,2^{K-2},2\cdot2^{K-2},3\cdot2^{K-2}$ as $x_1$
runs over $I_1$, so a choice of $x_1$ sets the top two bits. In half-offsets
$x_i=a_i/2$, the displayed sum is $U(A)$ by the formula in the proof of
Lemma U7. Taking $u\equiv-d^{-1}\pmod{2^K}$ gives $r_d(U(A))=1\le R$, so
$A=\{2x_1,\ldots,2x_K\}$ is compatible, and $A\subseteq\Omega$ when every
$I_i\subseteq\{1,\ldots,J\}$.

For the reference, let $Y\subseteq\{1,\ldots,J\}$ be the set of
half-offsets $y$ with $2y$ a success. For large $X$, $J\ge7K\log X$. Take
$I_1=Y\cap[1,K\log X]$; each class modulo $4$ has at least
$K\log X/4-1$ sites there, so $I_1$ misses a class with probability at most
$4(1-\rho)^{K\log X/4-1}\le5e^{-K/2}$. Split $(K\log X,J]$ into at least
$5K$ consecutive disjoint blocks of $W=\lceil\log X\rceil$ integers. A block
contains at least $W/2-1$ sites of each parity, so it meets both parities
of $Y$ with probability at least $(1-e^{-\rho(W/2-1)})^2\ge(1-e^{-0.9})^2>1/3$
for large $X$, independently of the other blocks. By Hoeffding's
inequality, fewer than $K-1$ of $5K$ independent blocks meet both parities
with probability at most $\exp(-2(2K/3)^2/(5K))\le e^{-K/6}$. Otherwise
take $I_2,\ldots,I_K$ to be $Y$ intersected with the first $K-1$ such
blocks. The first part then gives a compatible $K$-set, so the failure
probability is at most $5e^{-K/2}+e^{-K/6}$. The last claim follows from
Lemma U13. $\square$

The same proof applies to the periodic reference of Lemma U9: since $q$ is
odd, the allowed sites of a block of $W$ integers split almost equally
between the two parities and among the classes modulo $4$, and their
expected number of successes per block is again about $2W/\log X$.

So a bound for $B_d(X;K)$ of this form evaluates, with the reference
count $N_X\rho^{|H|}$ for each tuple, to at least $(1-O(e^{-K/6}))N_X$, and
any loss in the tuple bounds only raises it. It can prove the bound
$(13/16-\varepsilon)N_X$ of the sketch only if the prime tuple counts it uses
fall far below the reference counts in aggregate over its weights. This is
not a proof that every such majorant fails for the actual primes, which
would need those counts. The Hardy–Littlewood heuristics predict counts
equal to the reference counts times singular series that average to one,
and the proof above uses only parities in short blocks, which those
heuristics leave balanced; they predict no deficit of that size. The
majorant class studied here must therefore be enlarged, or such an
arithmetic deficit proved. Signed coefficients, majorization restricted to
arithmetically admissible sets, or a different span are not covered by
this argument. This generalizes the
overcount of the all-subsets majorant in
[[research/prime_binary_new_attack/critical_length_obstructions|Proposition O6]]
to every nonnegative tuple majorant; it says nothing about signed majorants
such as Lemma U5's, whose odd layers need lower bounds.

## A periodic starting set with zero count

The base term in (BD) can be removed by a different deletion order. This
gives an exact signed arithmetic target whose coefficients depend on
preceding primes and a fixed periodic continuation. It does not estimate
that target.

Fix an odd $d$. Choose an odd prime $q$ such that
$L_q=2^{q-1}-1>d$, and put
$W_q=\{m\ge1:m\text{ odd},\ q\nmid m\}$. Keep the parameters of
Theorem U8 with $K=\lceil A\log_2\log X\rceil$, $A>1$, and the
definitions of $J_X$, $\beta_T$ and $C(T)$ above. In particular the
ordinary zero residue still means the positive residue $M$.

**Proposition U15 (increasing-order deletions).** For sufficiently large
$X$, depending on $d$ and $q$,
$C(W_q\cap J_X)=0$. For $m\in W_q\cap J_X$ define

$$
T_m=(\mathbb P\cap(X,m))\ \cup\ (W_q\cap[m,2X+D]),\qquad
\Phi(m)=C(T_m\setminus\{m\})-C(T_m).
$$

Then

$$
B_d(X;K)=
\sum_{\substack{m\in W_q\cap J_X\\m\text{ composite}}}\Phi(m),
\qquad |\Phi(m)|\le K.
\tag{PD}
$$

The weight is determined by $m$, the last at most $K$ actual primes below
$m$ in $J_X$, and the fixed periodic set above $m$. It requires no
primality information above $m$.

*Proof.* In the infinite ordered set $W_q$, the half-gaps have period
$q-1$: there is one half-gap $2$ and all the others are $1$. The weighted
half-gap tail $H^{W_q}(x)$ at any $x\in W_q$ is therefore

$$
H^{W_q}(x)=1+\frac{2^e}{L_q},\qquad 0\le e\le q-2.
$$

Indeed the additional unit in the half-gap recurs every $q-1$ terms,
so its geometric sum is of the displayed form. Since $L_q$ is odd and
$L_q>d$, none of $dH^{W_q}(x)$ is an integer. Its fractional part lies
between $1/L_q$ and $1-1/L_q$.

Let $x_K$ be the $K$th successor of $x$ in $W_q$. The truncation identity
gives
$dU/M=dH^{W_q}(x)-dH^{W_q}(x_K)/M$, where $1<H^{W_q}(x_K)<2$.
For $M>2dL_q$ the subtraction does not cross an integer. Hence

$$
r_d(U)=M\bigl(1-\{dU/M\}\bigr)\ge M/L_q>R
$$

for all sufficiently large $X$, since $R/M\to0$. Every physical gap
in $W_q$ is at most $4$, and $D\ge4K$ eventually. Thus all the
successors needed for a root in $(X,2X]$ belong to $J_X$, proving the
zero count for the finite starting set.

For $X>q$, the primes in $J_X$ form a subset of $W_q\cap J_X$. Delete
its composite elements in increasing order. Immediately before deleting
$m$, the survivors below $m$ are exactly the primes in $(X,m)$, and
the survivors at and above $m$ are still $W_q\cap[m,2X+D]$. The set is
therefore $T_m$. Telescoping the changes in $C$, whose initial value is
zero and final value is $B_d(X;K)$, proves (PD).

If $m\le2X$, its successors in $T_m$ belong to the unchanged periodic
set, so $\beta_{T_m}(m)=0$ by the same calculation. If $m>2X$, it is
not a counted root. All other affected roots are among the last $K$
primes below $m$; each contributes a change in $\{-1,0,1\}$. This proves
the bound and the stated dependence of $\Phi$. The finite right
endpoint causes no additional dependence: missing successors simply
make the corresponding indicator zero. $\square$

The signs in (PD) cannot be discarded as a monotonicity assertion. Small
exact examples use the same definition of the event at
$(K,M,R,d,D,q)=(2,4,1,1,16,3)$; these are finite examples, not the
asymptotic choice $R=\lfloor4d\log X\rfloor$.

- For $X=17$ and $m=25$, the affected prime roots are $19$ and $23$.
  Their weighted sums $U$ change from $5,4$ to $7,7$, respectively.
  Their positive residues change from $3,4$ to $1,1$, so $\Phi(25)=2$.
- For $X=50$ and $m=95$, the affected roots are $83$ and $89$.
  Their weighted sums change from $9,7$ to $10,10$, with positive
  residues changing from $3,1$ to $2,2$. Thus $\Phi(95)=-1$.

All the displayed spans are at most $16$. These exposed calculations
show both signs and attainment of the bound at $K=2$; they prove no
asymptotic statement about the weights.

The exact remaining arithmetic estimate in this formulation is

$$
\sum_{\substack{m\in W_q\cap J_X\\m\text{ composite}}}\Phi(m)
\le\frac34N_X
\quad\text{along arbitrarily large }X.
\tag{PD*}
$$

Together with the rationality lower bound $13N_X/16-o(N_X)$, this would
exclude the fixed odd denominator part $d$. The choice of $q$ is fixed
after $d$ and before $X$; the scales can pass every preperiod $s$.
Proving (PD*) for every odd $d$, including $1$, would finish the
contradiction. It is unproved even for $d=1$, where $q=3$ is enough.

A least-prime-factor decomposition makes (PD*) a concrete next sieve
test. Its left side is exactly

$$
\sum_{\substack{\ell\le\sqrt{2X+D}\\\ell\text{ prime},\ \ell\ne2,q}}
\ \sum_{\substack{r\ge\ell,\ P^-(r)\ge\ell\\
\ell r\in W_q\cap J_X}}\Phi(\ell r),
\tag{PF}
$$

where $P^-(r)$ is the least prime factor of $r$. Each composite is
counted once. In the range $\ell>X^{2/5}$ the cofactor is prime for
large $X$, so this includes a sum over two prime factors with an
explicit coefficient. The first test is a signed estimate in that
range retaining the preceding-prime dependence of $\Phi$; the other
least-factor ranges would still have to be controlled. The prime number
theorem in progressions and Bombieri--Vinogradov do not, as stated,
estimate coefficients chosen from the preceding $K$ primes. Replacing
them by periodic or independent data would change (PF). Thus (PD)
removes an unknown base term and specifies the weights, but supplies
no arithmetic saving and no theorem reducing the full target to that
first range.

One term shows exactly why a congruence count does not yet estimate (PF).
Fix a root $p_n$, put $p_r=p_{n+K-1}$ and $a=U_{n,K-1}$, and consider a
deleted $m\in W_q\cap(p_r,p_{r+1})$. At that time $m$ is the root's
$K$th successor. Let $m^+$ be the next element of $W_q$, and put
$\Delta=(m^+-m)/2\in\{1,2\}$. When both spans are at most $D$, this
root's contribution to $\Phi(m)$ is exactly

$$
E\left(2a+\frac{m-p_r}{2}+\Delta\right)
-E\left(2a+\frac{m-p_r}{2}\right),\qquad
E(v)=\mathbf1[r_d(v)\le R].
\tag{PE}
$$

The indicator $E$ tests the cyclic interval $1,\ldots,R$ after
multiplication by $-d$ modulo $M$. For fixed $\Delta$ its difference
in (PE) is supported on at most $2d\Delta$ residue classes modulo $M$,
the classes near the two ends of the interval. Since $d$ is odd, the
corresponding condition on $m$ uses at most $2d\Delta$ classes modulo
$2M$. Allowing both values of $\Delta$ gives at most $6d$ classes.
They are translated by $p_r-4a$, so they depend on the preceding
$K-1$ actual gaps; they are not fixed progressions as $n$ varies.

Counting integers in these classes inside $(p_r,p_{r+1})$ gives only
$O_d(g_r/M+1)$. Summing over $n\in I_X$ and using PNT telescoping
gives $O_d(X/M+N_X)$. A change caused solely by crossing the span
cutoff is nonpositive, so omitting it preserves this upper estimate.
Although $X/M=o(N_X)$, the estimate still has an $O_d(N_X)$ endpoint
term with no constant saving, even before the other ranks are accounted for.
This calculation makes the first missing input explicit: an averaged
estimate for these preceding-prime-dependent classes inside actual
prime gaps, or signed cancellation retaining that dependence. It is
not supplied by replacing each interval count with its length divided
by the modulus. The same issue remains after restricting $m$ to the
range of (PF) with two prime factors.

## A bounded positive deletion change

The weights in (PD) are bounded above, independently of $K$, once $K$
grows faster than $2\log_2\log X$. This pays for the composites with two
large prime factors. It does not reduce the remaining part of (PD*),
which keeps the full strength of the missing estimate.

Keep the setting of Proposition U15 with $A>2$. Thus $d$ is odd, $q$ is
an odd prime with $L_q=2^{q-1}-1>d$, $K=\lceil A\log_2\log X\rceil$,
$M=2^K$, $R=\lfloor4d\log X\rfloor$, and $E(v)=\mathbf 1[r_d(v)\le R]$
as in (PE). Let $\sigma$ be the successor map of $W_q$. For $x\in W_q$
write $H_i(x)=H^{W_q}(\sigma^ix)$ and
$\delta_i(x)=(\sigma^{i+1}x-\sigma^ix)/2\in\{1,2\}$, and put

$$
V_t(x)=\sum_{0\le i<t}2^{t-1-i}\delta_i(x),\qquad V_0(x)=0 .
$$

Splitting the geometric tail $H_0(x)=\sum_{i\ge0}\delta_i(x)2^{-i-1}$ at
$i=t$, and $V_s(x)$ at $i=t$, gives

$$
V_t(x)=2^tH_0(x)-H_t(x),\qquad
V_s(x)=2^{s-t}V_t(x)+V_{s-t}(\sigma^tx)\quad(0\le t\le s).
\tag{VW}
$$

By the proof of U15, $H_0(x)=1+2^e/L_q$ for some $0\le e\le q-2$. The
fractional parts of $dH_0(x)$ and $2dH_0(x)$ are those of $d2^e/L_q$ and
$d2^{e+1}/L_q$. Since $L_q$ is odd and larger than $d$, it divides
neither numerator, so both numbers lie at distance at least $1/L_q$ from
$\mathbb Z$. Put

$$
C_{d,q}=\bigl\lceil\log_2(1+2dL_q)\bigr\rceil,\qquad Z=L_q(R+2d).
$$

**Lemma U16 (bounded positive change).** Suppose

$$
R>4d^2L_q+2d,\qquad (1+2dL_q)R<2^{C_{d,q}}(R-2d),\qquad
M>Z(R+2dZ).
\tag{K2}
$$

Then $\Phi(m)\le C_{d,q}$ for every composite $m\in W_q\cap J_X$. All
three conditions hold for all sufficiently large $X$, depending on $d$
and $q$: the odd number $1+2dL_q>1$ is below $2^{C_{d,q}}$, and $A>2$
gives $M/R^2\to\infty$.

*Proof.* Let $p_r$ be the last prime below $m$. Only $m$ and the primes
$p_{r-K+t+1}$, $0\le t<K$, can change their indicators when $m$ is
deleted; the root $m$ has indicator zero before deletion by the proof of
U15, and roots at most $X$ are not counted. Put
$b=2U_{r-K+1,K-1}+(m-p_r)/2$, an integer, where the index notation may
use primes below $X$; they do not enter any counted root's sum. The block
of $p_{r-K+t+1}$ consists of $K-t-1$ prime gaps, the gap from $p_r$ to
$m$, and $t$ periodic gaps; after the deletion the middle gap ends at
$\sigma m$ and $t$ periodic gaps follow it. Multiplying the prefix sum
by $2^{t+1}$ discards its first $t$ gaps modulo $M$, so the weighted sums
before and after the deletion are congruent modulo $M$ to

$$
u_t=2^tb+V_t(m),\qquad u'_t=2^tb+V_{t+1}(m).
\tag{K1}
$$

Deleting $m$ moves successors only to the right. A root counted after
the deletion therefore has its $K$th successor and span at most $D$
before it as well. Call $t$ positive when the root $p_{r-K+t+1}$ exceeds
$X$ and gains its indicator. Then $E(u_t)=0$ and $E(u'_t)=1$; changes at
the right end of $J_X$ and at the span cutoff are nonpositive. It
suffices to show that at most $C_{d,q}$ indices are positive.

For a positive $t$ put $a_t=r_d(u_t)>R$ and $a'_t=r_d(u'_t)\le R$.
Reducing $-du'_t\equiv a'_t$ modulo $2^t$ and using (VW) gives
$k-2dH_0(m)=(a'_t-dH_{t+1}(m))/2^t$ for an integer $k$. The left side has
absolute value at least $1/L_q$, and $1<H_{t+1}(m)<2$, so

$$
2^t\le L_q\,|a'_t-dH_{t+1}(m)|<Z .
\tag{K3}
$$

The difference $w_t=V_{t+1}(m)-V_t(m)=V_t(m)+\delta_t(m)$ lies in
$[2^t,2^{t+1}]$. Since $0<a'_t+dw_t\le R+2dZ<M$, no reduction occurs and

$$
a_t=a'_t+dw_t,\qquad R<a_t\le R+2dZ .
\tag{K4}
$$

For positive indices $t<s$, (VW) gives
$u_s=2^{s-t}u_t+V_{s-t}(\sigma^tm)$, so
$a_s\equiv2^{s-t}a_t-dV_{s-t}(\sigma^tm)\pmod M$. The right side exceeds
$2^{s-t}(R-2d)>0$, because $V_j\le2(2^j-1)$, and it is at most
$2^s(R+2dZ)<Z(R+2dZ)<M$ by (K3) and (K4). The congruence is therefore an
equality, and (VW) at $\sigma^tm$ turns it into
$(a_s-dH_s(m))/2^s=(a_t-dH_t(m))/2^t$. Thus every positive index has the
same value

$$
y=\frac{a_t-dH_t(m)}{2^t}.
$$

Writing $a_t=-d(2^tb+V_t(m))+kM$ with $t<K$ shows
$y\in\mathbb Z-dH_0(m)$. Put $z=y-dH_0(m)\in\mathbb Z-2dH_0(m)$, so
$|z|\ge1/L_q$. By (VW) and (K4), every positive index satisfies

$$
a_t=2^ty+dH_t(m),\qquad a'_t=2^tz+dH_{t+1}(m).
\tag{K5}
$$

If $z<0$, then $a'_t\ge1$ forces $2^t<2dL_q$, and $y<dH_0(m)<2d$, so
$a_t<4d^2L_q+2d<R$, contrary to (K4). Hence $z\ge1/L_q$, $y>0$ and
$y/z=1+dH_0(m)/z<1+2dL_q$. Now $a_t>R$ and $a'_t\le R$ in (K5) give

$$
\frac{R-2d}y<2^t<\frac Rz ,
$$

an open interval whose endpoints have ratio less than
$(1+2dL_q)R/(R-2d)<2^{C_{d,q}}$. It contains at most $C_{d,q}$ powers
of $2$. $\square$

The proof uses nothing about the primes below $m$: the integer $b$ is
arbitrary. For $d=1$ one may take $q=3$, so $L_q=3$ and $C_{1,3}=3$.

The bound is one-sided, but the same argument also limits the negative
part. Let $t<s$ be indices whose roots are counted in $T_m$, with
residues $a_t,a_s\le R$. Reducing modulo $2^s$ as in (K3) gives $2^s<Z$.
The integer $2^{s-t}a_t-dV_{s-t}(\sigma^tm)$ is congruent to $a_s$
modulo $M$, is less than $ZR<M$, and exceeds $-2dZ$; if it were not
positive, $a_s$ would exceed $M-2dZ>R$. So it equals $a_s$, and as
before all counted indices share one $y\in\mathbb Z-dH_0(m)$ with
$1\le2^ty+dH_t(m)\le R$. If $y>0$ this gives $2^t<R/y\le RL_q$; if
$y<0$ it gives $2^t<2d/|y|\le2dL_q$. Hence at most
$\lceil\log_2(RL_q)\rceil$ of the $K$ preceding primes are counted in
$T_m$, and

$$
\Phi(m)\ge-\bigl\lceil\log_2(RL_q)\bigr\rceil
=-\log_2\log X-O_{d,q}(1).
$$

This improves the bound $|\Phi(m)|\le K$ of Proposition U15 by the
factor $A$ on the negative side, but its magnitude still grows with
$X$.

**Corollary U17 (two large prime factors).** Under (K2), for each fixed
$\alpha\in(1/3,1/2)$,

$$
\sum_{\substack{m\in W_q\cap J_X\ \text{composite}\\P^-(m)>X^\alpha}}
\Phi(m)\le\Bigl(C_{d,q}\log\frac{1-\alpha}\alpha+o(1)\Bigr)N_X .
\tag{HF}
$$

With $\alpha_{d,q}=1/(1+e^{1/(4C_{d,q})})$, which lies in $(1/3,1/2)$,
the right side is $(1/4+o(1))N_X$. For $d=1$ and $q=3$,
$\alpha_{1,3}=0.479\ldots$.

*Proof.* For large $X$ a composite $m\le2X+D<X^{3\alpha}$ with
$P^-(m)>X^\alpha$ is a product $\ell r$ of primes
$X^\alpha<\ell\le r$; it lies in $W_q$ because $q$ is fixed. Counting
by the smaller factor $\ell$ counts each such $m$ once, squares
included. For $X^\alpha<\ell\le\sqrt X$ the number of partners $r$ is
$\pi(2X/\ell)-\pi(X/\ell)=(1+o(1))X/(\ell\log(X/\ell))$, uniformly, by the
prime number theorem. Summing over primes $\ell$ by partial summation
gives

$$
(1+o(1))\frac X{\log X}\int_\alpha^{1/2}\frac{du}{u(1-u)}
=\Bigl(\log\frac{1-\alpha}\alpha+o(1)\Bigr)N_X .
$$

The primes $\ell\in(\sqrt X,\sqrt{2X+D}]$ contribute $O(X/\log^2X)$, and
the integers in $(2X,2X+D]$ number $D=o(N_X)$. Lemma U16 bounds each
weight by $C_{d,q}$; negative weights only lower the sum. $\square$

### What the split leaves

Write $\mathrm{LF}$ for the left side of (HF) at $\alpha=\alpha_{d,q}$ and
$\mathrm{SF}$ for the sum of $\Phi(m)$ over the composites
$m\in W_q\cap J_X$ with $P^-(m)\le X^{\alpha_{d,q}}$. Then
$B_d(X;K)=\mathrm{SF}+\mathrm{LF}$ exactly, by (PD). Under rationality,
Proposition U3 and Corollary U17 give
$\mathrm{SF}\ge(9/16-o(1))N_X$. Conversely, for each odd $d$, a bound

$$
\mathrm{SF}\le\Bigl(\frac9{16}-\varepsilon_d\Bigr)N_X
\quad\text{along arbitrarily large }X
\tag{SF}
$$

would give $B_d(X;K)\le(13/16-\varepsilon_d+o(1))N_X$ and exclude the
denominator part $d$. It is not a weaker form of the missing estimate.

- The identity $\mathrm{SF}=B_d(X;K)-\mathrm{LF}$ holds for every set of
  primes, and Corollary U17 bounds $\mathrm{LF}$ only from above. Inside
  one prime gap $(p_r,p_{r+1})$ let $F_r(m)$ be the number of counted
  roots among $p_{r-K+1},\ldots,p_r$ in $T_m$. Then
  $\Phi(m)=F_r(\sigma m)-F_r(m)$ at each composite $m$ of the gap. Summing
  by parts against the indicator of $P^-(m)\le X^{\alpha_{d,q}}$
  expresses the gap's part of $\mathrm{SF}$ through the values of $F_r$
  where that indicator changes. Collecting the terms gives back the gap
  total $F_r(p_{r+1})-F_r(m_0)$, with $m_0$ the first site of the gap,
  minus the gap's part of $\mathrm{LF}$: the same identity, gap by gap.
  No estimate of $\mathrm{SF}$ follows from this rearrangement.
- Fix a small prime $\ell\ne2,q$ and consider the part of
  $\mathrm{SF}$ at sites divisible by $\ell$. Inside the gap these sites
  satisfy $m-p_r\equiv-p_r\pmod\ell$. By (K1) and the span conditions,
  the weights of the gap's sites depend on $r$ only through the
  preceding $K-1$ gaps, the gap $g_r$ and the residue of $p_r$ modulo
  $2q$, apart from the two ends of $J_X$. Replacing this part by a fixed
  proportion of the gap total would therefore need
  $p_r\bmod\ell$ to be uncorrelated with the preceding $K-1$ gaps and
  with $g_r$, in this weighted sense. The primes $p_{r-i}$ all avoid the
  class $0\bmod\ell$, so such correlations are present. A main term would
  need local factors as in Lemma U9, and the error would need an estimate
  for consecutive primes jointly with the weighted block sum. The other
  residues of $m$ modulo $\ell$ make up the rest of each gap total, so
  such an estimate for every class would also estimate $B_d(X;K)$.

Thus Lemma U16 is deterministic, and Corollary U17 adds only the prime
number theorem. They locate where primality enters (PD): in the
preceding prefix $b$, in the offset of the deleted site from $p_r$, and in
the prime endpoints at which each gap's deletions stop. They do not
supply the arithmetic input of step 5 of the sketch.

The
[[research/prime_binary_new_attack/short_span_sieve|shorter-span construction]]
changes the upper event instead of rearranging (SF). At span
$(6/5)K\log X$, rationality still gives a positive lower count, and
the existence of any compatible $K$-subset gives a monotone upper
event that may be bounded on actual sieve survivors. Its reference
probability tends to zero, so U14's large-span conclusion is not an
obstruction to that event. Counting its certificates with multiplicity
still fails in the reference. The actual survivor count remains open;
its centered local-count moment and truncated phase count specify the
next two arithmetic obligations.

## Comparison with available inputs

Condition (AC), Corollary U4 and (GC) still need estimates for actual
consecutive primes. No bound examined here proves any of them. The
available upper bounds for prime tuples have a different loss:
[[../library/primes/kuperberg_2023_sums_singular_series_large_sets_tail/_index|Kuperberg's sieve bound]]
for $k$ shifts, Theorem 4.1 of arXiv:2210.09775v2, carries
$(2+\varepsilon)^kk!$ and the singular series. Its statement permits
$k=o((\log X)^{1/4})$, so it includes $k=O(\log\log X)$, but this
factor cannot be bounded by $Cc^K$ with $c<2$ when $k=K+1$.
It also counts tuples rather than consecutive primes; the exclusions
and the signed terms remain. This is a comparison of stated bounds,
not a lower bound on the loss of all sieve methods. The theorem was
read at statement depth; its analytic proof is not reconstructed here.

The rough-number estimates of
[[../library/primes/gafni_2025_rough_numbers_between_consecutive_primes/_index|Gafni and Tao]]
give a different kind of information. In arXiv:2508.06463v1, Theorem 1.1
bounds by $O(X/\log^2X)$ the prime gaps in $[X,2X]$ containing no
integer whose least prime factor is at least the gap length. Lemmas
2.1 and 3.1 estimate rough-number counts in intervals of length
$\lfloor(\log X)^\alpha\rfloor$, with roughness threshold
$\exp((\log X)^\beta)$, fixed $0<\beta<\alpha<1$ and fixed moment
order. These statements were read; their proofs are not independently
verified here. They neither identify which rough sites are consecutive
primes nor give the upper comparison in (GC). Passing from those counts
to independent thinning in Lemma U9 is still an unsupported step.

No implication is established between these upper criteria and the lower
count CPS($d$) of the sketch or the hypothesis of its Theorem F.

## Failure log

- **Condition (AC).** Missing: a fixed-factor upper bound for the local
  density of $2Q_{n,L}$ at scale $\eta$, at length
  $\log_2\log X+\log_2(1/\eta)+O(1)$. Unknown for the actual primes; it holds
  in the independent model. Reopens with an upper bound for consecutive
  prime blocks uniform in a growing block length, or with a reduction of
  the event to boundedly many primes.
- **Corollary U4.** Missing: $B^\theta_d(X)\le\kappa N_X$ with
  $\kappa<13/16$, for one $\theta$. Unknown for every odd $d$, including
  $d=1$; same reopening condition.
- **Condition (GC).** Missing: the upper comparison for its single phase
  event, with $F_X\log X/2^K\to0$. Unknown for every odd $d$, including
  $d=1$. A loss $Cc^K$, $c<2$, suffices at (M8); the claim that every
  sufficient comparison must have bounded loss is false.
- **Statement (SB).** The signed bound is unknown. Its first weighted
  model layer is at least a constant times $(\log X)^4N_X$ by Lemma U7.
  This requires cancellation in this expansion, not termwise
  asymptotics as a logical prerequisite. Reopens with a direct signed
  estimate, an arithmetic reference with controlled error, or a different
  majorant.
- **Statement (SB) through $\Delta_d\le\mathcal A_X$.** The proposed
  $O(N_X)$ adverse-error bound is false: the odd layer of tuples
  forbidden modulo $3$ gives (M7). Those errors must cancel or be
  removed by changing the reference; stronger upper tuple estimates
  cannot repair this bound around the Bernoulli array.
- **The excess $E_{\mathrm{act}}$.** Bounded pointwise by Lemma U5, not in
  mean for the actual primes. Unknown.
- **Termwise upper bounds and dropped exclusions.** Invalid, for the sign
  and inflation reasons above. More generally (Lemma U13, Proposition U14),
  every nonnegative combination of tuple indicators that majorizes the
  block event for all sets is at least one at every root whose window
  contains some compatible $K$-set, and in the independent and periodic
  references that holds with probability $1-O(e^{-K/6})$. Proved. Such a
  bound can succeed only through an aggregate deficit of prime tuples
  relative to the reference, which the Hardy–Littlewood heuristics do not
  predict. Reopens with a majorant outside the specified class, a changed
  span with its rationality lower count checked, or such a deficit.
- **The survivor form (Lemma U10).** Proved equivalent up to $O(N_X/K)$:
  the count for the integers with no prime factor up to
  $X^{1/2-1/K^2}$ differs from $B_d(X;K)$ by at most $(K+1)E_X$. Missing:
  an upper estimate for that survivor count, which is the same estimate.
  Unknown. Reopens only with an estimate for the survivor count itself.
- **A sieve stopped below the square root (Lemma U11, Proposition U12).**
  The deletion identity (BD) is exact. Its base term at $X^{2/5}$ counts the
  same event on primes and large semiprimes, and its correction has
  $(\log(3/2)+o(1))N_X$ terms of size up to $K+1$. At a cutoff $X^{1/s}$ at
  least $(\log(s-1)-o(1))N_X$ composite survivors must be deleted. Missing:
  a bound substantially below the uniform deletion allowance for the
  signed sums of $\Psi_\ell(\ell r)$, each a function of the survivors
  within $D$ of $\ell r$. No applicable bilinear bound for these
  coefficients is supplied by the inspected sources. Unknown. This
  decomposition gives no estimate for step 5.
  Reopens with a signed estimate for those sums in one range of $\ell$ that
  uses the structure of $\Psi_\ell$, together with an estimate for the base
  term.
- **Increasing-order deletions (U15).** The periodic set $W_q$ has count
  zero, and deleting its composites in increasing order gives (PD)
  exactly. Proved. This removes the unknown base count in (BD), but the
  signed bound (PD*) is unknown. The coefficients use the last $K$
  actual primes before the deleted integer; a periodic continuation
  does not make that preceding-prime data periodic or independent.
  Both signs occur, even in the displayed small examples. For the
  $K$th-successor term, (PE) isolates at most $6d$ residue classes
  modulo $2M$ determined by preceding primes. Counting by interval
  length leaves an additive $O_d(N_X)$ endpoint contribution with no
  saving; this estimate does not prove (PD*).
- **Least-factor split of (PD) (U16, U17).** For $A>2$ every weight
  satisfies $\Phi(m)\le C_{d,q}$, independently of $K$ and of the
  preceding primes, and the composites with two prime factors above
  $X^{\alpha_{d,q}}$ then contribute at most $(1/4+o(1))N_X$. Proved,
  using only the prime number theorem. Missing: the bound (SF) for the
  remaining composites, with coefficient $9/16-\varepsilon_d$. Unknown
  for every odd $d$, including $d=1$. The split supplies no saving:
  $\mathrm{SF}=B_d(X;K)-\mathrm{LF}$ identically, summation by parts
  inside the prime gaps restates that identity, and the part at sites
  divisible by a fixed small prime $\ell$ needs $p_r\bmod\ell$ jointly
  with the preceding $K-1$ gaps and $g_r$. Such an estimate for every
  class modulo $\ell$ would estimate $B_d(X;K)$ itself. Reopens with an
  estimate for consecutive primes jointly with the weighted block sum,
  or with a starting set or deletion order whose remaining weights a
  known theorem controls.
- **Rooting the block at every integer.** The identity
  $F(x)\equiv2^{\pi(x)}S\pmod1$ is proved, but the forced lower count then
  needs bounds of order $X\log X$ for gap-weighted sums such as
  $\sum_{n\in I_X}g_nH_{n+K}$. The prime number theorem does not give them,
  and Cauchy–Schwarz with the conditional mean-square bound $x(\log x)^3$
  gives only $O(X(\log X)^3)$. Unknown; reopens with such a bound.
- **The independent model as a statement about primes.** Unjustified; the
  model computations here are references only. Lemma U9 incorporates
  exclusions from small odd primes without losing the phase bound, but
  its independent thinning and the comparison (GC) remain unproved for
  actual primes.
