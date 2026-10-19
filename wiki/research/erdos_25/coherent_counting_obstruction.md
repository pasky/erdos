---
name: research/erdos_25/coherent_counting_obstruction
desc: A finite smooth-band construction rules out uniform counting domination of coherent delayed unions by zero-residue multiples.
tags: [coherent-residues, obstructions, finite-comparisons]
sources: []
created: 2026-09-22T00:00:00Z
updated: 2026-09-24T22:13:01Z
---


# research/erdos_25/coherent_counting_obstruction

***

## Counting domination fails: proved

For a finite set $D\subseteq\mathbb N$ and a common center
$\alpha\in\widehat{\mathbb Z}$, define
$$
 B_{D,\alpha}
 =\{n\ge1:\exists q\in D,\ q\le n,\ n\equiv\alpha\pmod q\},
 \qquad
 M(D)=\{n\ge1:\exists q\in D,\ q\mid n\}.
$$

**Theorem.** For every pair of constants $A,c\ge1$, there are a finite
primitive set $D$, an integer center $\alpha$, and an integer $X$
such that
$$
 |B_{D,\alpha}\cap[1,X]|
 >A\,|M(D)\cap[1,cX]|.
 \tag{1}
$$
In particular, no absolute constant $C\ge1$ gives the proposed bound
$$
 |B_{D,\alpha}\cap[1,X]|
 \le C\,|M(D)\cap[1,CX]|
$$
uniformly over finite coherent systems.

The proof uses a smooth-number band and an elementary slow-growth
argument and is self-contained.

### Choosing a smooth band

Let $R=2^r$, where $r\ge1$ is an integer to be chosen sufficiently
large, and put
$$
 \kappa=\lfloor R/c\rfloor.
$$
We require $\kappa\ge3$. Let $\mathcal P$ be the finite set of primes
at most $R$, and write
$$
 H(t)=\#\{d\le t:d\text{ has only odd prime factors in }\mathcal P\},
 \qquad
 w=\prod_{\substack{p\in\mathcal P\\p>2}}(1-1/p).
$$
The integer $1$ is included in $H(t)$.

If $k$ is the number of odd primes in $\mathcal P$, then
$$
 H(R^j)\le(rj+1)^k\qquad(j\ge0),
 \tag{2}
$$
because each prime exponent is at most $\log_2(R^j)=rj$.
Consequently there are arbitrarily large integers $j$ such that
$$
 H(R^{j+1})\le2H(R^j).
 \tag{3}
$$
Indeed, if (3) failed for every $j\ge j_0$, repeated doubling would
give $H(R^{j_0+m})>2^mH(R^{j_0})\ge2^m$, contradicting the polynomial
bound (2) for large $m$.

Choose such a $j$, set $T=R^j$, and define
$$
 D=\{q:T<q\le2T,\ q\text{ has all its prime factors in }\mathcal P\},
 \qquad X=\kappa T.
 \tag{4}
$$
The set $D$ is nonempty, since $2T$ is a power of two. It is
primitive: if distinct $q,q'\in(T,2T]$ satisfied $q\mid q'$, then
$q'\ge2q>2T$, a contradiction.

### Bounding the zero-residue count

Suppose $n\in M(D)$ and $n\le cX\le RT$. Write $n=qm$ with
$q\in D$. Since $q>T$, the positive integer $m$ satisfies
$m<R$. Every prime factor of $m$ therefore lies in $\mathcal P$.
Thus $n$ is $\mathcal P$-smooth and $T<n\le RT$, proving
$$
 |M(D)\cap[1,cX]|
 \le\#\{n\in(T,RT]:n\text{ is }\mathcal P\text{-smooth}\}.
 \tag{5}
$$
Write every integer counted on the right uniquely as $2^ed$, where
$d$ is odd and $\mathcal P$-smooth. Necessarily $d\le RT$.
For a fixed $d$, the condition $T<2^ed\le RT$ puts $e$ in a
half-open interval of length $\log_2R=r$. It therefore permits at
most $r$ nonnegative integer exponents. By (3),
$$
 |M(D)\cap[1,cX]|\le rH(RT)\le2rH(T).
 \tag{6}
$$

### Lower-bounding the full Haar footprint

Let
$$
 \beta_D=\mu\left(\bigcup_{q\in D}q\widehat{\mathbb Z}\right).
$$
For each odd $\mathcal P$-smooth $d\le T$, let $e(d)\ge1$ be
minimal such that $2^{e(d)}d>T$. Then
$$
 a_d:=2^{e(d)}d\in(T,2T],\qquad a_d\in D.
$$
Consider the Haar event
$$
 E_d=\{z\in\widehat{\mathbb Z}:
       v_p(z)=v_p(d)\text{ for every odd }p\in\mathcal P,
       \quad v_2(z)\ge e(d)\}.
$$
Haar prime coordinates are independent, with
$\mu(v_p(z)=a)=(1-1/p)p^{-a}$ and
$\mu(v_p(z)\ge a)=p^{-a}$.
It follows that
$$
 \mu(E_d)=\frac{w}{d\,2^{e(d)}}=\frac{w}{a_d}
 \ge\frac{w}{2T}.
$$
The events $E_d$ are pairwise disjoint, because their prescribed odd
prime valuations distinguish the integers $d$. Every $E_d$ is
contained in $a_d\widehat{\mathbb Z}$, and hence in the full union.
Therefore
$$
 \beta_D\ge\frac{wH(T)}{2T}.
 \tag{7}
$$

### Averaging the coherent center

Let $L=\operatorname{lcm}(D)$, and choose an integer $\alpha$
uniformly from $\{0,\ldots,L-1\}$. For every fixed integer
$n\ge2T$, all moduli in $D$ are active, and translation invariance
in $\mathbb Z/L\mathbb Z$ gives
$$
 \Pr(n\in B_{D,\alpha})=\beta_D.
$$
There are $(\kappa-2)T+1$ integers in $[2T,X]$. By averaging, some
integer center $\alpha$ satisfies
$$
 |B_{D,\alpha}\cap[1,X]|
 \ge(\kappa-2)T\beta_D
 \ge\frac{(\kappa-2)wH(T)}2.
 \tag{8}
$$
The neglected extra $+1$ only weakens the estimate.

### An elementary bound for the Euler product

Since the odd primes at most $R$ are a subset of the odd integers
from $3$ to $R-1$,
$$
 w\ge\prod_{i=1}^{R/2-1}\frac{2i}{2i+1}
 \ge\frac1{\sqrt{R-1}}>\frac1{\sqrt R}.
 \tag{9}
$$
For completeness, if $P_m=\prod_{i=1}^m2i/(2i+1)$, induction gives
$P_m^2\ge1/(2m+1)$. The induction step follows from
$$
 \frac1{2m-1}\left(\frac{2m}{2m+1}\right)^2
 \ge\frac1{2m+1},
$$
which is equivalent to $4m^2\ge(2m-1)(2m+1)$.

Combining (6), (8), and (9), and noting that the denominator is positive,
gives
$$
 \frac{|B_{D,\alpha}\cap[1,X]|}{|M(D)\cap[1,cX]|}
 \ge\frac{\lfloor R/c\rfloor-2}{4\sqrt R\log_2R}
 \longrightarrow\infty
 \qquad(R\to\infty\text{ through powers of two}).
 \tag{10}
$$
For the prescribed $A,c$, choose $R$ so large that the last lower
bound exceeds $A$. This proves (1). After choosing $R$, the parameter
$T$ can still be taken arbitrarily large. $\square$

## Scope

This disproves a uniform **natural-counting comparison** that might
otherwise have been integrated to obtain the finite harmonic
small-footprint estimate discussed in
[coherent power cutoffs](coherent_power_cutoff.md).
It does **not** disprove that harmonic estimate, nor construct a
logarithmic-density anomaly, nor resolve Erdős Problem 25. Each system
in the construction is finite and therefore eventually periodic.

## Separate exact-cover barriers

The following elementary facts delimit proposed amplifications to a
finite covering system. They are not additional obstructions to the
harmonic small-footprint estimate and do not rule out every possible
amplification.

**Coherence-preserving operations cannot give a cover.** Every coherent
family with moduli greater than one misses the profinite point
$\alpha+1$. For a finite family, choose an integer $a$ representing
the center modulo its common period; then $a+1$ is an integer
survivor. Thus an exact-cover reduction intended also to handle a
hypothetical coherent anomaly would have to break coherence.

**Integer-orbit coverage does not imply profinite coverage.** Given
$N\ge1$ and $0<\varepsilon<1$, enumerate
$\mathbb Z=\{z_1,z_2,\ldots\}$ and choose distinct primes
$p_j>\max(N,|z_j|)$ with $\sum_j1/p_j<\varepsilon$.
CRT supplies $\alpha\in\widehat{\mathbb Z}$ with
$\alpha\equiv z_j\pmod{p_j}$ for every $j$. The full cylinder
union contains every ordinary integer but has Haar measure less than
$\varepsilon$. Every finite subfamily consequently leaves positive
Haar measure. Compactness cannot extract a finite cover from coverage
of the dense integer orbit: it requires coverage of the whole profinite
space. This is not a delayed counterexample; the designed hits have
$p_j>|z_j|$ and are inactive, and the reciprocal sum is finite.

**Fresh-prime affine tagging leaves a surviving cylinder.** Suppose
finitely many copies are embedded as $p_jB_j+b_j$, where the primes
$p_j$ are distinct. Every class in the $j$-th copy is contained in
$b_j\pmod{p_j}$. Choose one residue different from $b_j\pmod{p_j}$
for each $j$, and apply CRT. The resulting integer residue cylinder
avoids all copies. Thus this standard way of distinguishing moduli
cannot produce an exact finite cover, even if every base set $B_j$
were all of $\mathbb Z$.

These facts explain why orbit-coverage amplification and ordinary
fresh-prime tagging do not supply the exact finite cover needed for an
application of the minimum-modulus theorem. No reduction from a
positive logarithmic tail anomaly to such a cover has been established.
