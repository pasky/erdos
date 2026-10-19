---
name: research/erdos_699/remaining/details/cubic_after_cutoff_9
title: "Erdős 699: what the later arguments suggest for index three"
desc: "The actual-overlap bound saturates on odd columns of power-of-two rows. Higher Lucas digits give a simultaneous approximation problem in the cofactors, but no fixed finite set of odd primes can cover all rows."
created: 2026-09-22T18:55:43Z
updated: 2026-09-22T19:12:28Z
---

# Erdős 699: what the later arguments suggest for index three

[[research/erdos_699/_index|P699 research]] ·
[[research/erdos_699/proofs/details/cutoff_9|The completed indices]] ·
[[research/erdos_699/remaining/details/cubic_uniform|The earlier cubic argument]]

***

The complete proofs for indices seven and nine do not supply a cubic
proof. Their new block choices and numerical covers make existing strict
asymptotic inequalities usable at lower heights. At index three, the
[polynomial obstruction](cubic_weighted.md) remains:
the critical certificate has no strict gain and is independent of the
column. Changing numerical constants cannot repair that obstruction.

The more relevant recent idea is to keep the actual column in the local
valuation calculation, as in the
[index-six carry argument](index_6_carry_constraints.md).
Here is precisely what transfers, what fails, and one possible next target.
No new global finiteness or exclusion theorem is claimed.

## The two-adic overlap can already be maximal

For a putative bad cubic triple, write

$$
n=2^h u,\qquad u\text{ odd},\qquad t=v_2(j)<h.
$$

The actual-overlap refinement replaces the discarded row power $2^h$ by

$$
E_2=2^{\min\{h,v_2\binom nj\}}.
$$

On the still unresolved subfamily $u=1$, one has exactly

$$
v_2\binom{2^h}{j}=h-v_2(j),\qquad E_2=2^{h-t}. \tag{1}
$$

Indeed,
$j\binom{2^h}{j}=2^h\binom{2^h-1}{j-1}$, and the last binomial is odd
by Lucas's theorem, since $2^h-1$ has every binary digit equal to one.
For odd $j$, (1) gives $E_2=2^h=n$: there is no improvement at all over
discarding the full row power. Thus the successful overlap refinement at
the larger indices does not by itself handle even this cubic subfamily.

## The higher odd-prime digits supply extra conditions

Call an odd prime active if it divides $\binom n3$. For a full active
component $P=p^a\Vert n-r$, with $r\in\{0,1,2\}$, write

$$
n=PA+r,\qquad j=Pk+b,\qquad 0\le b<P.
$$

The endpoint conditions used to construct the integer cubic give only
$b\le r$. The complete Lucas condition says exactly

$$
b\le r,\qquad k\preceq_p A, \tag{2}
$$

where $k\preceq_p A$ means that every base-$p$ digit of $k$ is at most
the corresponding digit of $A$. Equivalently, $p\nmid\binom Ak$.
This follows by separating the bottom $a$ digits from the remaining
digits in Lucas's theorem. The lower block of $n$ is the integer $r<p$.

In particular, for active components

$$
n-1=PA,\qquad n-2=QB,\qquad P=p^a,\quad Q=q^b,
$$

a bad column requires integers $k,\ell$ and residues
$\varepsilon\in\{0,1\}$, $\delta\in\{0,1,2\}$ satisfying

$$
\boxed{
PA-QB=1,\qquad Pk-Q\ell=\delta-\varepsilon,
\qquad k\preceq_p A,\quad \ell\preceq_q B.
} \tag{3}
$$

The same $j=Pk+\varepsilon=Q\ell+\delta$ must satisfy (2) at every
active component. This is additional arithmetic information; the
coefficient cubic, its discriminant, and the six-point polynomial
conditions retain only the initial blocks.

There is already a limited success in this direction: the
[two-prime criterion](cubic_uniform.md) uses a higher
prime power to exclude suitably sized pairs $P,Q$ and to constrain the
adjacent product range. The following extension lets the decisive higher
digit come from a third prime.

**Proposition.** Suppose active odd prime-power components
$P\mid n-1$ and $Q\mid n-2$ satisfy

$$
\frac{2n}{3}\le T:=PQ\le n-3.
$$

If a power $U$ of any active odd prime satisfies

$$
T+1<U\le n,
$$

then the row has no bad cubic column.

**Proof.** Put $R=n-T$, so $3\le R\le T/2$. The initial Lucas
conditions at $P,Q$ put $j$ in the following six classes modulo $T$,
listed by their least nonnegative representatives:

$$
0,\quad1,\quad R-1,\quad R,\quad2R-2,\quad T-R+2.
$$

Indeed, $\delta(n-1)-\varepsilon(n-2)$ represents the class with
residues $\varepsilon$ modulo $P$ and $\delta$ modulo $Q$.
Every listed representative except $0,1$ is at least $R-1$.
On the other hand, $n/2<U\le n$ and the full Lucas condition at the
prime underlying $U$ imply $j\le n-U<R-1$. To see this, $j<U$ has
zero digits at and above the position of $U$, and its lower digits
are bounded by those of $n\bmod U=n-U$. Also $j<T$, so the only
remaining columns are $0,1$, outside the admissible range. $\square$

Unlike the earlier criterion, this statement does not require
$P,Q\le\sqrt n$, and $U$ need not have either of their base primes.
It is a sufficient row criterion, not a theorem that every large row
supplies such $P,Q,U$.

A further concrete experiment in proof construction
would be to extend that argument to smaller $PQ$ using the digit
conditions in (3), rather than just the initial residues. Such an extension
would still need to address rows lacking suitably sized components before
it could establish global finiteness.

## A fixed finite list of odd primes cannot suffice

**Proposition.** For every finite set $S$ of odd primes, infinitely many
exponents $h$ satisfy

$$
p\nmid\binom{2^h}{3}\qquad\text{for every }p\in S. \tag{4}
$$

**Proof.** Let $L$ be a common multiple of $6$ and all multiplicative
orders $\operatorname{ord}_p(2)$ with $p\in S$, $p\ge5$. Choose any
$h\equiv-1\pmod L$ with $h\ge2$. For $p\ge5$ in $S$,

$$
2^h\equiv2^{-1}\pmod p.
$$

The residue $2^{-1}$ is none of $0,1,2$ modulo such a prime. Therefore
$p$ divides none of $2^h,2^h-1,2^h-2$, proving (4) for $p\ge5$.
Also $h\equiv5\pmod6$, so $2^h\equiv5\pmod9$. Hence
$v_3(2^h-2)=1$, while the other two numerator factors are prime to $3$.
The denominator $6$ cancels this single factor of $3$. This proves (4)
at $3$ as well. The progression contains infinitely many positive $h$.
$\square$

Consequently, an argument using higher Lucas digits must allow its active
odd primes to vary with the row. On the rows in (4), none of the primes in
$S$ imposes a condition on the column through badness. This rules out a
fixed finite prime list as a complete implementation of that proposed
route; it does not rule out using auxiliary congruences for another purpose.

## Assessment

The new work makes higher Lucas digits a more concrete direction to test,
because it demonstrates at other indices that actual-column information
can strengthen a row-only polynomial argument. Formula (1) also identifies
why a direct transfer fails. A uniform incompatibility theorem for the
simultaneous digit conditions would be new input, not a numerical
optimization of the existing cubic certificate. The elliptic arguments
still lack the same uniform control of the varying curves that they lacked
before the cutoff-nine proof.
