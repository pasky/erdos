---
name: research/leads/totient_binary_series/arithmetical_windows
title: Carries on Progressions and Exceptional Representatives
desc: |
  Isolating one totient term bounds every progression-wide valuation
  certificate, including cancellation, while leaving selected arithmetic
  subfamilies open.
tags: []
sources: []
problems:
- 249
research_state: ready
review_status: unreviewed
created: 2026-09-17T06:20:20Z
updated: 2026-09-17T08:46:27Z
---

# Carries on Progressions and Exceptional Representatives

[[research/leads/totient_binary_series/_index|..]]

[[research/leads/totient_binary_series/arithmetical_windows/classification|classification]]: Exact existence conditions for an eventual whole-progression carry
assertion, and the unique pair with actual divisibility and dyadic excess.

[[research/leads/totient_binary_series/arithmetical_windows/evidence/_index|evidence/]]: Fixed prime, semiprime, and prime-square isolation witnesses, the carry
at 64, and the CRT data of its infinite counterfamily.

***

## The supported restriction

A progression that makes the binary partial-sum numerator divisible by
$2^m$ at every sufficiently large member has a restriction on every
positive representative $N$:

$$
2^m\le\min\{4\varphi(\gcd(N,M)),\,2\varphi(N)\}.
\tag{1}
$$

Here $M$ is the progression's modulus. Thus its guaranteed precision has
$m-\log_2N<1$ for $N\ge2$, even when $N\ll M$. This is a bound on that
particular method of certifying divisibility. It is not a bound on the
actual valuation at an individual member, and it does not exclude a
construction that uses additional arithmetic properties of a selected
subfamily. The proof below allows cancellation. It does not infer (1)
from the size of $M$.

This extends the scope of the
[[research/leads/totient_binary_series/window_cost|whole-progression bounds]]
and identifies a specific research choice: an unbounded-excess
construction must use information beyond a divisibility assertion valid
on an entire progression. Prime-cofactor conditions are one possible
additional input, but no useful growing family is constructed here.
All deductions below are author-recorded and unreviewed. They do not
resolve [[problems/irrationality/E0249/_index|Problem 249]], and no novelty claim
or verification tier is attached.

## Inputs and notation

Write

$$
\Phi_N=\sum_{n=1}^N\varphi(n)2^{N-n},\qquad
W_h(N)=\sum_{i=0}^{h-1}2^i\varphi(N-i)\quad(N\ge h).
$$

Then $\Phi_N\equiv W_h(N)\pmod{2^h}$. The
[[research/leads/totient_binary_series/_index|parent sketch]] proves that
$S=\sum_{n\ge1}\varphi(n)2^{-n}=a/b$ would give positive integers

$$
I_N=bT_N=a2^N-b\Phi_N,\qquad
T_N=\sum_{j\ge1}\frac{\varphi(N+j)}{2^j},\qquad
1\le I_N\le b(N+2).
\tag{2}
$$

Consequently unbounded $v_2(\Phi_N)-\log_2N$ would prove irrationality.
For $v_2$ of a signed nonzero integer use its absolute value, and put
$v_2(0)=+\infty$.

The prime selection arguments use Dirichlet's theorem:
every reduced arithmetic progression contains infinitely many primes.
The statement was read on p. 1 of Ralf Stephan's translation of
[Dirichlet's 1837 paper, arXiv:0808.1408v2](https://arxiv.org/pdf/0808.1408v2),
version 24 November 2014. Its analytic proof was not rechecked here.
This is an explicitly consumed standard theorem, not newly compiled
proof coverage. The elementary cofactor argument that follows also
appears as Lemma A of the parent window page; its proof is included to
make the construction's hypotheses visible.

The prime-square refinement additionally uses quadratic reciprocity and
its supplementary laws. These standard statements were read in Keith
Conrad's [Background on Quadratic Reciprocity (CTNT 2024), Theorem 3.1,
p. 5, equations (3.1)--(3.2)](https://ctnt-summer-math.media.uconn.edu/wp-content/uploads/sites/1632/2024/06/CTNT-background-on-QR.pdf),
including the displayed PDF page. Their proofs were not rechecked.

## A small-valuation cofactor on any progression

**Lemma 1.** Let $M\ge1$, $r\in\mathbb Z$, and
$g=\gcd(r,M)$. Every positive $n\equiv r\pmod M$ satisfies
$v_2(\varphi(n))\ge v_2(\varphi(g))$, and infinitely many satisfy

$$
v_2(\varphi(n))\le v_2(\varphi(g))+2.
\tag{3}
$$

*Proof.* Divisibility $g\mid n$ implies
$\varphi(g)\mid\varphi(n)$, prime by prime. Set $r=gr'$ and $M=gM'$.
The class $u\equiv r'\pmod{M'}$ is reduced. For each prime $p\mid g$
not dividing $M'$, also impose $u\equiv1\pmod p$. The resulting class
$u\equiv a\pmod L$ is reduced and every member is coprime to $g$.

If $4\nmid L$, or $4\mid L$ and $a\equiv3\pmod4$, refine by
$u\equiv3\pmod4$. Dirichlet supplies infinitely many prime $u$ in this
reduced class, with $v_2(u-1)=1$.
Otherwise $4\mid L$ and $a\equiv1\pmod4$. Choose a prime
$q\equiv3\pmod4$ not dividing $L$. There are infinitely many primes
$p\ne q$ in $p\equiv aq^{-1}\pmod L$; they are $3\pmod4$.
Take $u=qp$. Both factors are coprime to $g$, and
$v_2(\varphi(u))=2$. In either case $n=gu$ belongs to the original
class, and multiplicativity proves (3). $\square$

## Isolating one term defeats a uniform carry assertion

**Theorem 2.** Fix distinct integers $s_1,\ldots,s_k$, nonzero integer
coefficients $c_1,\ldots,c_k$, and a progression $N\equiv r\pmod M$
with $M\ge1$.
For sufficiently large $N$, put

$$
F(N)=\sum_{j=1}^k c_j\varphi(N+s_j),\quad
g_j=\gcd(r+s_j,M),\quad
\lambda=\min_j\bigl(v_2(c_j)+v_2(\varphi(g_j))\bigr).
$$

Every such $N$ satisfies $v_2(F(N))\ge\lambda$. Infinitely many satisfy

$$
v_2(F(N))\le\lambda+2.
\tag{4}
$$

In addition, for every fixed integer $B\ge1$, a refinement of the
progression makes $2^B\mid F(N)$ at every sufficiently large member.
In particular, any eventually constant residue of $F$ modulo $2^B$ on
the original progression must be zero.

*Proof.* The lower bound follows from $g_j\mid N+s_j$ and
$\varphi(g_j)\mid\varphi(N+s_j)$.

Choose $j_*$ attaining $\lambda$ and put $B=\lambda+3$. For each
$j\ne j_*$ choose a distinct prime $q_j\equiv1\pmod{2^B}$,
not dividing $M$, and larger than every $|s_j-s_{j_*}|$. Dirichlet's
theorem permits these finitely many choices. Refine by

$$
N\equiv r\pmod M,\qquad N\equiv-s_j\pmod{q_j}
\quad(j\ne j_*).
\tag{5}
$$

The CRT gives a class modulo $D=M\prod_{j\ne j_*}q_j$.
At its positive arguments every unwanted totient is divisible by $2^B$,
since $q_j\mid N+s_j$ and $2^B\mid q_j-1$.
At the selected position,
$N+s_{j_*}\equiv s_{j_*}-s_j\not\equiv0\pmod{q_j}$.
Consequently, if $R$ represents (5),

$$
\gcd(R+s_{j_*},D)=\gcd(r+s_{j_*},M)=g_{j_*}.
\tag{6}
$$

Apply Lemma 1 to $N+s_{j_*}$ on this refined class. Infinitely many
members have selected-term valuation at most $\lambda+2<B$, whereas
all other summands are divisible by $2^B$. Their sum has exactly the
selected term's valuation, proving (4). This argument also covers
$k=1$, with no fresh primes needed.

For the last assertion choose fresh primes at every position instead of
leaving one position free. The same CRT construction makes every totient
divisible by $2^B$. A constant residue on the original class must equal
the zero residue attained on this infinite refinement. $\square$

The order of choices is fixed data, then a finite CRT refinement, then
infinitely many prime or semiprime cofactors from Lemma 1. There is no
claim that the first such cofactor is small. Smallness is not needed for
this counterfamily to an assertion about every sufficiently large member.
The proof uses an actual arithmetic family rather than a probability
model for independent odd parts.

The additive constant two in (4) cannot be replaced by one in this
generality. Take $F(N)=\varphi(N)$ and $N\equiv5\pmod8$, so
$g=1$ and $\lambda=0$. Every such totient is divisible by four:
an odd integer with totient valuation one must be a power of a single
prime $3\pmod4$, and such powers have residues $1,3,7\pmod8$.
The integers $N=5^{2t+1}$ have totient valuation exactly two, giving
an infinite family attaining the bound. For $t\ge1$ they also have
$v_2(\Phi_N)=2$: $N-1$ is a multiple of four exceeding four,
so $4\mid\varphi(N-1)$; also $2\mid\Phi_{N-2}$. Thus
$8\mid2\Phi_{N-1}$ and $\Phi_N\equiv\varphi(N)\pmod8$.

## A bound for the actual representative

**Corollary 3.** Suppose $m,M\ge1$ and a class $N\equiv r\pmod M$
satisfies $2^m\mid\Phi_N$ for every sufficiently large positive $N$.
Then, for every $0\le i<m$,

$$
i+v_2\bigl(\varphi(\gcd(r-i,M))\bigr)\ge m-2.
\tag{7}
$$

For every positive representative $n\equiv r\pmod M$,

$$
2^m\le4\varphi(\gcd(n,M))\le4\varphi(n)\le4n.
\tag{8}
$$

The last inequality is strict when $n\ge2$. The representative may be
smaller than $m$, smaller than $M$, or smaller than the threshold in the
hypothesis; (8) still holds.

*Proof.* For sufficiently large $N$ the hypothesis is equivalent to
$2^m\mid W_m(N)$. Apply Theorem 2 with shifts $-i$ and coefficients
$2^i$. If the minimum in (7) were below $m-2$, its infinite
counterfamily would have valuation below $m$, a contradiction.
Taking $i=0$ gives $2^{m-2}\le\varphi(\gcd(r,M))$.
For any representative $n$, this gcd equals $\gcd(n,M)$ and divides
$n$, so its totient divides $\varphi(n)$. This proves (8), including
$m=1,2$. $\square$

**Theorem 4 (prime-square isolation).** Use the distinct shifts and
coefficients of Theorem 2. Fix $M\ge1$, an integer $n_0$, and one
position $j_0$ for which $t=n_0+s_{j_0}>0$. There are infinitely many
$N\equiv n_0\pmod M$, with all arguments positive, such that

$$
v_2(F(N))=v_2(c_{j_0})+v_2(\varphi(t))+1.
\tag{8a}
$$

*Proof.* Denote the right side by $e$ and set $B=e+1$. For each
$j\ne j_0$, put $\delta_j=s_{j_0}-s_j\ne0$. Choose distinct primes
$q_j\nmid M$ with

$$
q_j\equiv1\pmod{2^{\max(B,3)}t|\delta_j|}.
$$

Dirichlet gives these finite choices. Every $q_j$ is $1\pmod8$ and
$1$ modulo each odd prime dividing $t\delta_j$. Quadratic reciprocity
makes each such odd prime a square modulo $q_j$; the supplementary
laws do the same for $-1$ and $2$. Hence $t\delta_j$ is a nonzero
square. Dividing it by the square $t^2$ shows that
$\delta_jt^{-1}$ is a nonzero square. Choose a nonzero root $a_j$,
so $ta_j^2\equiv\delta_j\pmod{q_j}$.

The class

$$
p\equiv-1\pmod{4M},\qquad p\equiv a_j\pmod{q_j}\quad(j\ne j_0)
$$

is reduced: its moduli are pairwise coprime and its residues are units.
Dirichlet supplies infinitely many primes $p$ in it. Omit the finitely
many dividing $t$, and set $N=tp^2-s_{j_0}$. Then
$N\equiv t-s_{j_0}=n_0\pmod M$, while
$q_j\mid N+s_j=tp^2-\delta_j$ for every unwanted position.
Their totients are divisible by $2^B$. At the selected position,

$$
\varphi(N+s_{j_0})=\varphi(tp^2)=\varphi(t)p(p-1),
$$

whose valuation is $v_2(\varphi(t))+1$, since $p\equiv3\pmod4$.
The selected summand has valuation $e<B$, so it determines the sum's
valuation. For large $p$ all arguments are positive. The case $k=1$
needs no auxiliary primes and follows from the same prime class. $\square$

Apply this to $W_m$ at position zero, using any positive representative
$n$ of a class satisfying Corollary 3. If
$m>v_2(\varphi(n))+1$, the infinite family (8a) contradicts its
eventual divisibility. Therefore the sharper representative bound is

$$
m\le v_2(\varphi(n))+1,\qquad 2^m\le2\varphi(n)<2n\quad(n\ge2).
\tag{8b}
$$

This still permits $n<m$ or $n<M$: only the selected base argument
$t=n$ needs to be positive. Equation (8b) sharpens the bound at the
representative; it does not replace the factor four in the separate
forced-gcd bound (8). The constant one added to the actual totient
valuation cannot be uniformly removed: $2\mid\Phi_N$ for all $N\ge3$,
whereas the representative $n=2$ of the modulus-one class has
$v_2(\varphi(2))=0$.

Thus no family of whole-progression divisibility certificates can have
$2^m/(n+2)\to\infty$ at its selected representatives. The conclusion
still allows an individual member to have arbitrarily many *additional*
zero bits that the progression does not certify. It also leaves
progressions carrying only a sparse prime-cofactor or other arithmetic
subfamily outside its hypothesis.

The [[research/leads/totient_binary_series/arithmetical_windows/classification|exact
classification]] applies Theorem 4 at each positive backward position.
It proves that the only pair with an eventual whole-progression
assertion, actual $2^m\mid\Phi_n$, and $2^m>n+2$ is $(n,m)=(5,3)$.
It also characterizes existence of an eventual class assertion at every
fixed $n\ge m$ by all the position inequalities. These are additional
author-recorded deductions; they do not strengthen the separate
forced-gcd constant or restrict selected subfamilies.

The same inequalities (7) extend Lemma B of the parent window page to
cancellation. Its counting proof uses only (7), so for $m\ge4$ it gives

$$
\log_2 M\ge\frac{m(m-3)}2-\frac m2-E_m,\qquad
E_m=\sum_{2<p<m}(\lceil m/p\rceil-1)v_2(p-1).
\tag{9}
$$

As in that page, $E_m=O(m\log m)$ using $\theta(x)=O(x)$, giving
$\log_2M\ge m^2/2-O(m\log m)$. Unlike a deduction from (9) to a
lower bound on a least representative, the direct inference (7)--(8)
is valid without $n\ge M$.

## An infinite counterfamily to copying a successful window

A useful finite example is $v_2(\Phi_{64})=10$ although
$v_2(\varphi(64))=5$. For every modulus $M$, infinitely many
$N\equiv64\pmod M$ have $v_2(\Phi_N)=6$. Apply Theorem 4 to
$W_{10}(N)$, with $n_0=64$ and position zero. Its family has
$N=64p^2$ and window valuation $5+1=6$, while the earlier prefix is
divisible by $2^{10}$. Its excess is $-2\log_2p$ and its full-tail
ratio is $64/(64p^2+2)<1/p^2$. No finite congruence refinement
containing 64 can preserve its ten-bit cancellation at every
sufficiently large member.

There is also an explicit prime-parameter version preserving all the
seed window's divisors. Set

$$
L=\operatorname{lcm}(55,56,\ldots,64).
$$

Choose distinct primes $q_i>64$, $q_i\equiv1\pmod{128}$ for
$1\le i\le9$. Let $p$ range over primes in the CRT class

$$
p\equiv1\pmod{L/64},\qquad p\equiv3\pmod4,\qquad
p\equiv i\,64^{-1}\pmod{q_i}\quad(1\le i\le9),
\tag{10}
$$

and put $N=64p$. Since $v_2(L)=6$, the first modulus is odd.
The moduli in (10) are pairwise coprime, and each prescribed residue
is coprime to its modulus. There are infinitely many such primes $p$.
Every resulting $N$ satisfies $N\equiv64\pmod L$, so
$64-i\mid N-i$ throughout the seed window. But

$$
\varphi(N)=32(p-1)\equiv64\pmod{128},\qquad
128\mid\varphi(N-i)\quad(1\le i\le9).
$$

Therefore $\Phi_N\equiv64\pmod{128}$ and

$$
v_2(\Phi_N)=6,\qquad
v_2(\Phi_N)-\log_2N=-\log_2p\longrightarrow-\infty.
\tag{11}
$$

Only one varying prime is used; no prime-tuple conjecture enters.
This family refutes preservation of the original carry by preserving its
known divisor pattern. It does not say that no other members of the same
class have large carries.

The [[research/leads/totient_binary_series/arithmetical_windows/evidence/_index|finite
evidence]] checks the seed and two explicit small instances of the
isolation argument, and a signed three-term prime-square instance.
It also checks the CRT data for (10), without
asserting that the least residue in the prime parameter is itself prime.

## The infinite tail and the remaining construction

Equation (2) retains the entire positive tail. A valuation certificate
at $N\ge4$ with $m\le N$ would contradict denominator $b$ only when
$2^m>b(N+2)$. For precision guaranteed by an eventual whole-progression
assertion, equation (8b) gives

$$
\frac{2^m}{N+2}\le\frac{2\varphi(N)}{N+2}<2.
\tag{12}
$$

Thus this particular class-wide mechanism cannot exclude arbitrarily
large denominators. No discarded-tail approximation is being used.
For the explicit family (10), its actual ratio is
$64/(64p+2)<1/p$, so it provides no such contradiction even for
$b=1$.

The constructive criterion remains open. One exact remaining sufficient
lemma is to produce a selected arithmetic family $(N_k,m_k)$ with
$N_k\ge4$, $m_k\le N_k$,

$$
2^{m_k}\mid W_{m_k}(N_k),\qquad
\frac{2^{m_k}}{N_k+2}\longrightarrow\infty,
\tag{13}
$$

where the first assertion is certified by additional information about
the selected indices, not only by a theorem valid for every sufficiently
large member of a containing progression. A construction of odd cofactor
residues, prime-factor patterns, or a different signed tail certificate
could supply that information. No impossibility for such constructions
follows from Theorems 2 or 4. Conversely, describing a class and appealing to
infinitely many prime cofactors supplies neither the size estimate in
(13) nor the needed odd-part cancellation.

Partial termwise control does not satisfy the whole-window hypothesis.
For every $m\ge1$, the last term
$2^{m-1}\varphi(N-m+1)$ is divisible by $2^m$ for every $N\ge m+2$,
because $\varphi(n)$ is even for $n\ge3$. This holds on the class of
modulus one. At the seed $N=64$, $m=10$, its last term is
$2^9\varphi(55)=2^9\cdot40$, even though the whole numerator has
excess four. Thus forcing some late positions to vanish cannot alone
give a lower bound such as $M\ge N/8$ for a partially controlled window.

Nor does Dirichlet's theorem supply arbitrary odd parts within a fixed
prime-cofactor class. For example, a prime $p\equiv3\pmod8$ has
$v_2(\varphi(p))=1$ and $\varphi(p)/2\equiv1\pmod4$. A proposed
odd-part prescription must be compatible with the cofactor conditions;
the isolation theorems assert only the valuation control stated there.

The next useful decision is whether a proposed arithmetic subfamily can
control those odd parts and its actual representative size together.
The whole-progression hypothesis has a proved obstruction; the selected
subfamily question has an explicit unsupplied lemma. A broad retirement
of all arithmetic windows is not supported by these results.
