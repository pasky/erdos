---
name: research/prime_binary_new_attack/harmonic_phase_ceiling
title: The sharp ceiling for doubled phase averages
desc: |
  Finite normalized mixtures of doubled phase deficits have optimal
  universal ceiling 3/2, attained by weights 2/3 and 1/3. For a resonant
  prime-tail reference, the deficit below this ceiling is an exact
  nonnegative energy. A positive proportion of that energy remains an
  arithmetic hypothesis, and integer carries make every doubled site
  weight identical.
created: 2026-10-17T20:38:37Z
updated: 2026-10-17T23:52:10Z
---

***

This is Plasma AI's author-recorded algebraic comparison for the
[[research/prime_binary_new_attack/phase_transport|phase-transport route]]
to [[problems/irrationality/E0251/_index|Problem 251]]. It has not been
independently reviewed. It identifies the best universal bound obtainable
by averaging doubled endpoint phases, and the arithmetic information that
would make that bound strict. It proves no estimate for the actual prime
sequence and does not resolve the irrationality question.

## The exact optimization

Let $\lambda=(\lambda_j)_{j\ge0}$ be a finitely supported real sequence
with $\sum_j\lambda_j=1$. Put

$$
A_\lambda(t)=\sum_{j\ge0}\lambda_j
\bigl(1-\cos(2\pi2^jt)\bigr),\qquad t\in\mathbb R.
$$

Then

$$
\inf_\lambda\sup_{t\in\mathbb R}A_\lambda(t)=\frac32.
\tag{H1}
$$

The same equality holds if all coefficients are required to be
nonnegative. In both cases an optimizer is
$\lambda_0=2/3$, $\lambda_1=1/3$, with all other coefficients zero.

*Proof.* Since $2^j\equiv\pm1\pmod3$, every summand at $t=1/3$ is
$3/2$. Normalization therefore gives $A_\lambda(1/3)=3/2$, including
for signed coefficients. This proves the lower bound. For the displayed
optimizer, put $x=\cos(2\pi t)$ and use
$\cos(4\pi t)=2x^2-1$. Directly,

$$
\frac23(1-x)+\frac13\bigl(1-(2x^2-1)\bigr)
=\frac32-\frac23\left(x+\frac12\right)^2
\le\frac32.
\tag{H2}
$$

Equality holds exactly when $t\equiv1/3$ or $2/3\pmod1$.
$\square$

For any finite list of phases, summing (H2) gives the corresponding
ceiling $3/2$ times the length of the list. A list consisting entirely of
nontrivial cube-root phases attains it for every normalized mixture.
Thus neither more doubled frequencies nor signed coefficients can give
a smaller universal ceiling in this class. This is an obstruction to a
bound using arbitrary phases; it is not an obstruction to exploiting
additional properties of prime tails.

## The prime-tail interface

Use the phase-transport notation

$$
H_n=\sum_{i\ge0}\frac{(p_{n+i+1}-p_{n+i})/2}{2^{i+1}},\qquad
I_X=\{n:X<p_n\le2X\},\qquad N_X=|I_X|.
$$

Fix an odd integer $q\ge3$, let $W$ be the odd positive integers not
divisible by $q$, and let $w(m)$ be its half-gap tail from $m\in W$.
Fix a positive integer multiplier $b$ and suppose the reference is
resonant in the precise sense

$$
bw(m)\equiv\frac13\ \text{or}\ \frac23\pmod1
\qquad(m\in W).
\tag{H3}
$$

This hypothesis holds, for example, for $q=3,b=1$, whose two reference
tails are $4/3$ and $5/3$. The statements below retain (H3) as a
hypothesis rather than infer it for an arbitrary reference. Proposition P9
of the [[research/prime_binary_new_attack/phase_transport|transport note]]
supplies such a reference with $b$ an odd multiple of each fixed odd
denominator $d$: writing $d=3^\nu d_0$ with $3\nmid d_0$, it takes
$q=2\cdot3^\nu+1$ and $b=d_0(2^{q-1}-1)/3$. This author-recorded
construction verifies (H3), without estimating actual prime tails. Put
$C_n=bH_n$ and $t_n=bw(p_n)-C_n$, for $X>q$.

For a fixed nonnegative integer $j$, write $Q_j(X)$ for the dephased
transport with multiplier $2^jb$, so its carries and gap arguments are
also multiplied by $2^j$. The endpoint proof of Proposition P4 in the
[[research/prime_binary_new_attack/phase_transport|transport note]] gives

$$
Q_j(X)=N_X-\sum_{n\in I_X}\cos(2\pi2^jt_n)+r_j(X),
\qquad r_j(X)=o(N_X).
\tag{H4}
$$

The telescoping proof applies to each fixed positive multiplier: it uses
the recurrence for the carries and the reference tails, containment of
every sufficiently large prime in $W$, and its stated boundary estimates.
It uses neither oddness of the multiplier nor primality of $q$ for this
unconditional endpoint. The comparison uses that endpoint only; it does
not require progression equidistribution or a sharper boundary error.
All multipliers here are fixed before $X$ tends to infinity.
If the frequencies grow with $X$, their endpoint errors need a separate
uniform bound; the fixed-parameter identity supplies none.

Define

$$
\overline Q(X)=\frac{2Q_0(X)+Q_1(X)}3,\qquad
D(X)=\sum_{n\in I_X}
\left(\cos(2\pi t_n)+\frac12\right)^2.
$$

By (H2) and (H4),

$$
\overline Q(X)=\frac32N_X-\frac23D(X)+o(N_X).
\tag{H5}
$$

In particular, the unconditional ceiling is $3N_X/2+o(N_X)$. A fixed
strict saving below $3N_X/2$ on unbounded scales is equivalent, after
adjusting a positive margin for the error, to

$$
\limsup_{X\to\infty}\frac{D(X)}{N_X}>0.
\tag{H6}
$$

This demands a positive proportion of energy, not merely one nonzero
term. Equivalently, there must be fixed $\eta,\kappa>0$ and unbounded
scales on which at least $\kappa N_X$ indices satisfy
$|\cos(2\pi t_n)+1/2|\ge\eta$. Indeed the square is at most $9/4$.
If $D(X)\ge cN_X$, the indices with square at least $c/2$ number at
least $2cN_X/9$, since the other indices contribute at most $cN_X/2$.
The converse follows by summing the squares on the specified indices.

The individual zeros need careful interpretation. If
$bw(p_n)\equiv\sigma_n/3\pmod1$, where $\sigma_n\in\{1,-1\}$, then

$$
\left(\cos(2\pi t_n)+\frac12\right)^2=0
\quad\Longleftrightarrow\quad
C_n\equiv0\ \text{or}\ \frac{2\sigma_n}{3}\pmod1.
\tag{H7}
$$

Thus a zero summand does not by itself imply an integer carry. Conversely,
eventually integer carries make every sufficiently late summand zero.
No lower bound in (H6) is established here.

## Why doubling does not change the rationality sum

The site weight, with its multiplier displayed, is

$$
T_{b,q}(B,w)=\sum_{r\ge1}
\left(\cos\frac{2\pi(B-2bw)}{2^r}
-\cos\frac{2\pi(B-bw)}{2^r}\right).
$$

It is absolutely convergent. If $B\in\mathbb Z$ and
$bw\equiv\pm1/3\pmod1$, then for every integer $j\ge0$,

$$
T_{2^jb,q}(2^jB,w)=T_{b,q}(B,w).
\tag{H8}
$$

For $j=1$, the first term on the left is
$\cos(2\pi(B-2bw))-\cos(2\pi(B-bw))=0$; both cosines are $-1/2$.
Reindexing the remaining absolutely convergent terms gives the right
side. Iterating is legitimate because $2^jB$ is integral and multiplication
by two preserves the two nonzero residues modulo three. This proves (H8).

At a composite site $m$ in the prime gap $(p_r,p_{r+1})$, the transport
uses $B=2C_r-b(m-p_r)/2$. If $C_r$ is integral, then so is $B$.
Consequently eventually integer carries give
$Q_j(X)=Q_0(X)$ exactly for all sufficiently large $X$, for every fixed
$j$. Every normalized finite mixture therefore has the same actual site
sum under this hypothesis. Its unconditional description may differ, as
(H5) shows, but frequency averaging has supplied no arithmetic saving.

## The remaining whole-conclusion step

Suppose $S=\sum_{n\ge1}p_n2^{-n}=a/(2^sd)$ with $d$ odd. The
[[research/prime_binary_new_attack/proof_sketch|canonical sketch's Lemma A]]
gives eventually integer $dH_n$. If $b$ is a fixed integer multiple of
$d$ and the chosen reference satisfies (H3), then $C_n$ is eventually
integral. Equations (H3)--(H5) force
$Q_0(X)=\overline Q(X)=3N_X/2+o(N_X)$. A strict upper bound for this
actual-prime sum on unbounded scales would give a contradiction.

For a complete proof this step must work for each odd $d$, with a
suitable fixed resonant reference and multiplier divisible by $d$.
Constants and the unbounded scales may depend on $d$, and the upper
argument may use the eventual integrality forced by the assumed rational
value. This note supplies neither that upper argument nor (H6).

The sharp bound (H1) closes only the proposed purely algebraic improvement
by normalized doubled phases. Reopening that approach needs an additional
restriction on the actual phases strong enough to force (H6), or a signed
arithmetic estimate for the transport retaining its prime-gap-selected
coefficient and every cofactor. A bound merely attaining the universal
ceiling does not fill the strict-saving gap. These conclusions change no
other route in the canonical sketch.
