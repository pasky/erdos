---
name: research/prime_binary_new_attack/matching_gap_windows
title: Matching prime-gap windows under a rationality hypothesis
desc: Exact repeated gap windows with small enough tails would force a congruence between their starting indices and, for every odd denominator including the dyadic case, between their preceding gaps modulo 4. Such windows occur in abundance unconditionally; producing them in different index classes or preceding classes remains open.
created: 2026-10-16T12:22:34Z
updated: 2026-10-17T23:52:10Z
---

***

This elementary conditional, recorded by Plasma AI, gives an alternative
precise missing input for [[problems/irrationality/E0251/_index|Problem 251]].
It uses the lattice also present in the
[[research/prime_binary_new_attack/proof_sketch|parity-prediction sketch]],
without supplying an estimate for primes.

The independent [review](evidence/verify/matching_gap_windows/review.md) of
2026-10-16, accepted by the separate
[grade](evidence/verify/matching_gap_windows/grade.md), found the conditional
identities, lattice, matching-tail conclusion, modular-order consequence and
qualified fixed-denominator criterion **refutation-failed**. This records the
grader's accepted judgment at its exact conditional scope, not independent
acceptance of the required prime-pair existence or of a solution to Problem
251. For the fixed-denominator criterion the smaller starting index must be
unbounded; the separate dyadic-denominator case remains open. The word
“Equivalently” below denotes contraposition of the order implication under all
its inherited hypotheses, not equivalence to the individual-tail sufficient
bounds.

The final warning's assertion of a necessarily nonzero finite-window
contribution was **refuted-as-stated**. In the examined argument, the
[frozen subject](evidence/assets/matching_gap_windows/subject.md) has only the
grade's authorized body correction from “nonzero” to “potentially nonzero”
in that warning; its mathematical formulas, hypotheses and proof are unchanged.
The review and grade retain the original assertion and its counterexamples.
The paragraph comparing the criterion with the step lemma and the sections
"Graded congruences", "Occurrence of equal windows" and "The preceding gap
and the reversed constraint" are unreviewed additions. The review does not extend
to those additions, other
arguments in the parity-prediction sketch or any result behind the contextual
obstruction link.

Use the same indexing:

$$
S=\sum_{n\ge1}\frac{p_n}{2^n},\qquad
g_n=p_{n+1}-p_n,\qquad
G_n=\sum_{j\ge0}\frac{g_{n+j}}{2^{j+1}}.
$$

The convergent sums satisfy $S=2+G_1$ and $G_{n+1}=2G_n-g_n$.
Suppose $S=a/(2^sd)$ in lowest terms, where $s\ge0$ and $d\ge1$ is odd.
Then $dG_n$ is an integer for $n\ge s+1$. Since $g_n$ is even for $n\ge2$,
the recurrence also gives

$$
G_n\in\frac2d\mathbb Z
\qquad\bigl(n\ge\max(s+2,3)\bigr).
\tag{1}
$$

Indeed $dG_{n+1}=2dG_n-dg_n$ is even once $dG_n$ is integral and $n\ge2$.

## A repeated-window constraint

Let $m>n\ge\max(s+2,3)$ and $K\ge1$. Suppose

$$
g_{n+j}=g_{m+j}\qquad(0\le j<K).
\tag{2}
$$

If

$$
|G_{n+K}-G_{m+K}|<\frac{2^{K+1}}d,
\tag{3}
$$

then $G_n=G_m$ and $G_{n+K}=G_{m+K}$. When $d>1$, this also implies

$$
\operatorname{ord}_d(2)\mid(m-n).
\tag{4}
$$

To prove this, iterate the tail identity and cancel the equal windows:

$$
G_n-G_m=2^{-K}(G_{n+K}-G_{m+K}).
$$

By (1) the left side lies in $(2/d)\mathbb Z$, while (3) makes its absolute
value less than $2/d$. It is zero, and the displayed identity also makes the
two later tails equal. Iterating $G_{n+1}=2G_n-g_n$ from $G_1=S-2$ gives

$$
\{G_n\}=\{2^{n-1}S\}
        =\left\{\frac{2^{n-1-s}a}{d}\right\}.
$$

Equality of $G_n,G_m$, together with $\gcd(a,d)=1$ and the oddness of $d$,
therefore gives $2^{m-n}\equiv1\pmod d$, proving (4).

All tails are positive, so a sufficient condition for (3) is that both
$G_{n+K}$ and $G_{m+K}$ are less than $2^{K+1}/d$. Equivalently, if (2)
holds but (4) fails, rationality forces a separation

$$
|G_{n+K}-G_{m+K}|\ge\frac{2^{K+1}}d.
$$

## What would finish this route

For a fixed odd $d>1$, it would suffice to produce such pairs at arbitrarily
large indices with equal gap windows, small later tails, and
$\operatorname{ord}_d(2)\nmid(m-n)$. Arbitrarily large indices are needed
because the binary preperiod $s$ is unknown. This would exclude every rational
value whose reduced denominator has odd part $d$. A separate argument is
needed for $d=1$, where the congruence gives no obstruction. The step lemma
of the [[research/prime_binary_new_attack/proof_sketch|sketch]] makes every
odd part $d$ a dyadic case for the gaps $p_{n+t}-p_n$ with
$t=\operatorname{ord}_d(2)$; the congruence (4) is information about the
original gap sequence that this dyadic form does not use.

No theorem supplying these pairs is proved here. Repetition of short gap
patterns alone does not bound the later tails at the needed scale, and a
count of repeated windows alone does not put them in different index classes
modulo $\operatorname{ord}_d(2)$. The
[[research/prime_binary_new_attack/critical_length_obstructions|critical-length obstructions]]
still apply: exact cancellation of the window leaves a difference of two
infinite tails, and an upper bound for it must be justified. Congruences of
the gaps are weaker than (2); replacing equality by congruence introduces a
potentially nonzero finite-window contribution that this argument does not control.


## Graded congruences

The final warning concerns an unrestricted substitution of congruences for
equality. A specified sequence of moduli does control the finite-window
term. The following extension is author-recorded, outside the independent
review above; it supplies no occurrence theorem for prime windows.

Keep the reduced rational representation and $m>n\ge\max(s+2,3)$, and put
$h_i=g_i/2$, $H_i=G_i/2$ and
$Q_{i,K}=\sum_{j<K}h_{i+j}2^{-j-1}$. Suppose

$$
h_{n+j}\equiv h_{m+j}\pmod{2^{j+1}}
\qquad(0\le j<K).
\tag{5}
$$

Then $I=Q_{n,K}-Q_{m,K}$ is an integer. If
$|H_{n+K}-H_{m+K}|<2^K/d$, then

$$
H_{n+K}=H_{m+K},\qquad H_n-H_m=I.
\tag{6}
$$

For $d>1$ this again implies $\operatorname{ord}_d(2)\mid(m-n)$.

Indeed truncation gives

$$
H_n-H_m-I=2^{-K}(H_{n+K}-H_{m+K}).
$$

The left side lies in $(1/d)\mathbb Z$ by the odd-lattice lemma and the
integrality of $I$. The strict bound makes its absolute value less than
$1/d$, so it vanishes. Thus (6) holds, and $G_n-G_m=2I\in\mathbb Z$.
The fractional-part calculation proving (4) gives the order consequence.
Unlike exact matching, (5) need not make the initial tails equal: the
integer $I$ need not be zero.

In the original $G$ units the sufficient tail-difference bound is still
$2^{K+1}/d$. This is twice the threshold obtained in
[[research/prime_binary_new_attack/critical_length_obstructions|O5]] from
only $d(P_{n,K}-P_{m,K})\in\mathbb Z$, where $P=2Q$. The graded condition
makes $P_{n,K}-P_{m,K}$ an even integer, which permits use of the finer
lattice $(2/d)\mathbb Z$. Equal gap windows are a special case. A single
common modulus $2^{K+1}$ for every original gap also implies (5), but asks
for stronger congruences than its separate moduli $2^{j+2}$ for $g_{n+j}$.
For this index-class route, the missing input is arbitrarily late pairs
with these congruences, small following tails and incompatible index
classes. The preceding-gap constraint below gives a separate sufficient
test that also covers $d=1$.

## Occurrence of equal windows

This section is an author-recorded addition, outside the independent review
above. It shows that the occurrence part of the sufficient condition is
unconditional, so that the index classes are the whole missing input for a
fixed odd $d>1$.

Fix an odd $d$ and $A>1$, put $K=\lceil A\log_2\log X\rceil$, and use the
notation $I_X=\{n:X<p_n\le2X\}$, $N_X=|I_X|$ of the
[[research/prime_binary_new_attack/proof_sketch|parity-prediction sketch]].
Call $n\in I_X$ *good* when $G_{n+K}<2^K/d$ and
$p_{n+K}-p_n\le4KX/N_X$.

**Lemma (repeated windows).** For large $X$, at least $(3/4-o(1))N_X$
starts in $I_X$ are good, and all but at most $(6\log X)^K=X^{o(1)}$ good
starts share their window $(g_n,\ldots,g_{n+K-1})$ with another good start.

*Proof.* The sketch's mean-tail bound (T), written for $G=2H$, gives
$\sum_{n\in I_X}G_{n+K}\le(1+\varepsilon)X$, so at most
$(1+\varepsilon)dX/2^K=o(N_X)$ starts have $G_{n+K}\ge2^K/d$, because
$2^K\ge(\log X)^A$. Next,
$\sum_{n\in I_X}(p_{n+K}-p_n)=\sum_{j<K}\sum_{n\in I_X}g_{n+j}$ is at most
$K$ times the length of an interval from $X$ to $2X+o(X)$, so at most
$(1/4+o(1))N_X$ starts have span above $4KX/N_X$. A good window consists
of $K$ even gaps whose halves are positive integers with sum at most
$L=2KX/N_X=(2+o(1))K\log X$. There are at most
$\binom{\lfloor L\rfloor}{K}\le(eL/K)^K\le(6\log X)^K$ such windows, and
$K\log(6\log X)=O((\log\log X)^2)$. A window occurring at only one good
start accounts for one start, which gives the bound. $\square$

For a pair of good starts $m>n$ with equal windows, both later tails lie
in $(0,2^K/d)$, so (3) holds. Under $S=a/(2^sd)$ with
$n\ge\max(s+2,3)$, the constraint above gives $G_n=G_m$, and for $d>1$
also $\operatorname{ord}_d(2)\mid(m-n)$. Thus a rational value with odd
part $d>1$ makes the index class of $n$ modulo $\operatorname{ord}_d(2)$
constant on each window class of good starts, which is all but $X^{o(1)}$
of at least $(3/4-o(1))N_X$ starts. Its refutation needs only one late pair
of good starts with equal windows in different index classes. No theorem
inspected for this route relates a window of consecutive prime gaps to the
index of its first prime modulo a fixed integer, so this remains unknown.
For $d=1$ the index congruence gives no constraint; the preceding-gap
congruence of the next section gives one for every odd $d$.

## The preceding gap and the reversed constraint

This section is an author-recorded addition, outside the independent review
above. It replaces the index-class condition, and the separate dyadic case,
by a residue of the gap just before the windows. It supplies no occurrence
theorem for that residue.

Keep the reduced representation $S=a/(2^sd)$, put $n_0=\max(s+2,3)$, and
let $c_i=dH_i$, a positive integer for $i\ge n_0$ by the odd-lattice lemma.
For $r\ge1$ write

$$
\Psi_r(i)=\sum_{k=1}^{r}2^{k-1}h_{i-k}.
$$

Iterating $c_{i+1}=2c_i-dh_i$ gives $c_i=2^rc_{i-r}-d\Psi_r(i)$, hence

$$
c_i\equiv-d\,\Psi_r(i)\pmod{2^r}\qquad(i-r\ge n_0).
\tag{7}
$$

For $r=1$ this says $c_i\equiv h_{i-1}\pmod2$: the parity of the integer
carry at $i$ records the class of the preceding gap $g_{i-1}$ modulo $4$.

**Proposition (forward windows fix the past).** Let $m>n>n_0$, assume the
graded congruences (5) and $|H_{n+K}-H_{m+K}|<2^K/d$, so that (6) gives
$H_n-H_m=I$. Then for every $r$ with $1\le r\le n-n_0$,

$$
\Psi_r(m)-\Psi_r(n)\equiv I\pmod{2^r}.
\tag{8}
$$

In particular $g_{n-1}-g_{m-1}\equiv2I\pmod4$. For equal windows (2) one
has $I=0$, so $g_{n-1}\equiv g_{m-1}\pmod4$. This holds for every odd
$d$, including $d=1$, and uses no index class.

*Proof.* By (6), $c_n-c_m=dI$. Subtracting the two instances of (7) gives
$d(\Psi_r(m)-\Psi_r(n))\equiv dI\pmod{2^r}$, and $d$ is invertible
modulo $2^r$. At $r=1$ this is $h_{m-1}-h_{n-1}\equiv I\pmod2$.
$\square$

With the occurrence lemma, a rational value with any odd part $d$ makes the
class of $g_{n-1}$ modulo $4$ constant on each window class of good starts
$n>n_0$. One pair of good starts with equal windows and preceding gaps in
different classes modulo $4$ refutes every rational value with odd part $d$
whose preperiod satisfies $\max(s+2,3)<n$. More generally a pair satisfying
(5) and the later-tail bound refutes it when (8) fails for some
$r\le n-n_0$. A refutation of every rational value needs such pairs at
unbounded indices for each odd $d$; the constants may depend on $d$.

The same congruence (7) also runs in the other direction.

**Proposition (past residues fix the tail).** Let $r\ge1$ and $n\ne m$
with $\min(n,m)-r\ge n_0$. Suppose

$$
h_{n-k}\equiv h_{m-k}\pmod{2^{r-k+1}}\qquad(1\le k\le r)
\tag{9}
$$

and $\max(H_n,H_m)<2^r/d$. Then $H_n=H_m$, and consequently
$|h_n-h_m|<\max(H_{n+1},H_{m+1})-1$.

*Proof.* Each term $2^{k-1}(h_{n-k}-h_{m-k})$ is divisible by $2^r$, so
$\Psi_r(n)\equiv\Psi_r(m)\pmod{2^r}$, and (7) gives
$c_n\equiv c_m\pmod{2^r}$. Both carries lie in $(0,2^r)$, so they are
equal. From $H_i=h_i/2+H_{i+1}/2$ one gets $h_n-h_m=H_{m+1}-H_{n+1}$.
Every tail exceeds $1$, because every half-gap is at least $1$ and not all
of them equal $1$. $\square$

So a rational value makes $H$ constant on each class of (9) among the
starts whose tails lie below $2^r/d$. There are at most $2^{r(r+1)/2}$
classes. For $r=\lceil A\log_2\log X\rceil$ with $A>1$ this is
$X^{o(1)}$, and the mean-tail bound (T) leaves only $o(N_X)$ starts in
$I_X$ with $H_n\ge2^r/d$. Thus all but $X^{o(1)}+o(N_X)$ starts of $I_X$
share their class with another start below the tail bound. A refutation
needs one late pair in a common class whose next half-gaps differ by at
least the larger following tail minus one. A large difference of next
gaps alone is insufficient: both following tails must obey that same
inequality, as well as the initial-tail bounds used in (9).

Both forms ask that about $A\log_2\log X$ consecutive gaps on one side of
a start leave something free on the other side: the class modulo $4$ of the
adjacent gap, or the size of the next gap. These are statements about the
joint distribution of consecutive primes across one index at the critical
length. The repeated windows supply the pairs, but no information about
their neighbours. The inspected cluster and residue-string theorems
(Maynard--Tao, Shiu, Banks--Freiberg--Turnage-Butterbaugh) leave the relevant
prime positions unprescribed and supply no such joint pattern at growing
length. In the
[[../library/primes/lau_2024_prime_residue_patterns/_index|prescribed-residue extension]],
Theorem 1.5 of arXiv:2409.12819v2 supplies at least one word in its
specified family for fixed squarefree modulus and fixed word length.
Its statement and the fixed-pattern lower count preceding it were
inspected on printed pp. 3--4; the proof of Theorem 1.5 was not checked
here. It supplies neither an exact
gap window nor a quantitative joint count with its adjacent gap at this
growing length. Occurrence of fixed windows alone does not suffice:
with $K$ fixed, the bound
$|H_{n+K}-H_{m+K}|<2^K/d$ asks two following tails to agree within a fixed
constant. No inspected occurrence theorem pays that tail condition;
the related nested-cluster attempt is recorded in the
[[research/prime_binary_new_attack/critical_length_obstructions|critical-length obstructions]].
No inspected theorem supplies either form. This describes the inspected
inputs; it is not a proof that the forms are out of reach.
