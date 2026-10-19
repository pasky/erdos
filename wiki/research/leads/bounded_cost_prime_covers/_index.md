---
name: research/leads/bounded_cost_prime_covers
title: "Bounded-cost prime covers: constructions and intermediate-prime obstructions"
desc: An exact gain identity reduces bounded-cost covers to globally coherent residue choices with enough net saving for reserved cleanup. Centered explicit covers have cost log log log N + log 4 + o(1), still unbounded. Incidence restrictions for the first window and a small-prime linear sieve leave both full-solution routes unresolved.
problems: [1200]
research_state: ready
review_status: unreviewed
created: 2026-10-16T18:15:34Z
updated: 2026-10-17T01:22:01Z
---

# Bounded-cost prime covers: constructions and intermediate-prime obstructions

[[research/leads/_index|..]]

[[research/leads/bounded_cost_prime_covers/evidence/_index|evidence/]]: Exact sample covers, a three-prime witness that coordinated coincidences improve the union without changing class sizes, and seeded exploratory probes of the prime window, the full-class union problem and the union excess of the primes up to sqrt N.

***

[[problems/primes/E1200/_index|Problem 1200]] asks for a constant bound on
the reciprocal-prime cost of covering every sufficiently long positive
initial interval, using one residue class per selected distinct prime.
This page is the canonical proof sketch of the attack on it. Every local
deduction here is an author-recorded argument by Plasma AI without
independent review. Imported theorems are named with the version used.
Neither answer to the problem is established; the problem page records
the status search and the source scope.

## Target and whole proof sketch

For $N\ge1$ let $\mu(N)$ be the least value of $\sum_{p\in P}1/p$ over
covers of $\{1,\ldots,N\}$ by one class $a_p\pmod p$ for each prime of a
set $P\subseteq\{p:p\le N\}$, with $\mu(N)=+\infty$ if there is no cover.
For real $x$ put $N=\lceil x\rceil-1$; the positive integers and primes
below $x$ are then exactly those at most $N$. The erdosproblems.com statement
asserts

$$
\exists\, C,N_0\ \ \forall N\ge N_0:\qquad \mu(N)\le C .
$$

Its negation says that for every $C$ and $N_0$ some $N\ge N_0$ has
$\mu(N)>C$. The limit $\mu(N)\to\infty$ would suffice for the negation
but is not required by it. Cheap covers along a subsequence alone do not
prove the assertion.

**Notation.** A configuration is a set $P$ of primes at most $N$ with a
class $a_p$ for each $p\in P$. Write $A_p=\{n\le N:n\equiv a_p\pmod p\}$,
$m(n)=\#\{p\in P:n\in A_p\}$, $Z=\#\{n\le N:m(n)=0\}$ for the number of
survivors and $E=\sum_{n\le N}(m(n)-1)_+$ for the excess. Counting
incidences gives the exact identity

$$
\sum_{p\in P}|A_p|=N-Z+E,\qquad |A_p|\le\frac Np+1 .
\tag{1}
$$

For a cover $Z=0$, so its cost is at least $1+E/N-\pi(N)/N$.

**An equivalent form.** For a finite prime set $P$, let $J(P)$ be the
longest run of consecutive integers each divisible by some member of $P$.
It is finite, since every period $\prod_{p\in P}p$ contains an integer
prime to all of them. A cover of $[1,N]$ by classes for the primes of $P$
exists if and only if $J(P)\ge N$: choose $b\equiv-a_p\pmod p$, so that
$n$ is covered exactly when $b+n$ has a divisor in $P$. The translating
integer is unrestricted, so a theorem about sifting $[1,N]$ by zero
residues says nothing about this run without further uniformity.

**Where the two routes stand.**

1. *Affirmative.* The explicit cover below has cost
   $\log\log\log N+O(1)$ at every large $N$. Centering the middle
   classes at the midpoint removes the extra cost $1/2$ in (2), giving
   (27). Both constructions still have triple-logarithmic cost: the
   barrier below, which relies on the published Erdős–Ruzsa theorem,
   applies to both. A sufficient missing step is a middle block of
   bounded cost whose classes leave at most the actual unused-prime
   supply, so that the top primes can clean up. Equation (22) below gives
   an exact sufficient construction with a reserved top block. Zero residues
   leave a positive proportion. The window lemma below says what any better
   middle block must contain. A three-prime example realizes a gain from
   coordinated coincidences without any endpoint gain, but (18) rules out
   amplifying such examples in small interaction components. The exact gain
   identity (23) extends (22) to every fixed window $(N^{1/u},N/2]$ as the
   single inequality (24), at cost $\log u+o(1)$. Its first window $u=3$
   is especially constrained: without integers in four or more selected classes
   it needs realized short triangles at about $99\%$ of all forced
   intersections.
2. *Negative.* For every $C$ one needs a survivor at arbitrarily large
   $N$, whatever the classes. The held links are the core inequality,
   the uniform localization theorem and the pair-excess lemma below.
   They show that almost one unit of the mass of any bounded-cost cover
   sits on a fixed window of exponents, and that a cover of cost close
   to one has almost no mass below $N^{1/3}$. The missing step is a
   survivor bound for that middle window under arbitrary classes. The
   finite inequality (15) gives an explicit obstruction whenever the
   middle mass is below one, including every endpoint error. Lemma S, from
   the linear sieve, shows that the selected primes up to
   $N^{1/2-\delta}$, in any number and with any classes, leave a positive
   proportion of $[1,N]$; the survivor bound is therefore needed only for
   the action on that set of the primes above $N^{1/2-\delta}$, whose
   total mass is at most $\log2+O(\delta)$. The strongest
   survivor assertion is the open
   [[../library/primes/erdos_1980_small_sieve/problem_2|arbitrary-residue question of Erdős and Ruzsa]].

**Imported inputs.** The local arguments use the following standard
results in the stated forms: Mertens' estimates and the prime number
theorem; the dimension-one fundamental lemma of the combinatorial sieve
(Halberstam and Richert, *Sieve Methods*, 1974, Chapter 2; Iwaniec and
Kowalski, *Analytic Number Theory*, 2004, Chapter 6), in the form (8)
below; the arithmetic large sieve (H. L. Montgomery, *The analytic
principle of the large sieve*, Bull. Amer. Math. Soc. 84 (1978),
547–567) with the constant of Montgomery and Vaughan (*The large sieve*,
Mathematika 20 (1973), 119–134); the lower bound of the linear sieve
(the Jurkat–Richert theorem in Halberstam and Richert, *Sieve Methods*,
1974, and Iwaniec's form, *Rosser's sieve*, Acta Arith. 36 (1980),
171–202) as stated in the proof of Lemma S; Dickman's asymptotic
$\Psi(N,N^{\theta})\sim\rho(1/\theta)N$ for fixed $\theta$; and
[[../library/primes/erdos_1980_small_sieve/theorem_1|Theorem 1 of Erdős and Ruzsa]],
whose proof is not audited here and which only the zero-residue barrier
uses.
The published analytic inputs are used in these stated forms; their proofs
are not reconstructed or independently audited here.
For the fixed-$s$ linear-sieve estimate used in Lemma S, the primary proof
and the exact original-source theorem locator have not been inspected here.

## An explicit cover of triple-logarithmic cost

**Proposition 1.** For all sufficiently large $N$,

$$
\mu(N)\le\log\log\log N+\tfrac12+\log4+o(1).
\tag{2}
$$

*Construction.* Put $u=4\log\log N$ and $z=N^{1/u}$, so that
$z\to\infty$. Choose $a_2=1$, and $a_p=0$ for every prime $p$ with
$z<p\le N/2$. Let $S$ be the set of even $n\le N$ divisible by no prime
in $(z,N/2]$. Give each $s\in S$ its own prime $q_s\in(N/2,N]$ with
$a_{q_s}\equiv s\pmod{q_s}$.

*Coverage.* An odd $n$ lies in the class of $2$. An even $n$ with a prime
factor in $(z,N/2]$ lies in that prime's zero class. Every other $n$ lies
in $S$ and is covered by $q_s$. The three sets of primes are disjoint once
$z>2$, so the construction is valid as soon as the primes $q_s$ exist,
that is, as soon as $|S|\le\pi(N)-\pi(N/2)$. Each integer is assigned one
covering class here; other coincidences only waste capacity and cost
nothing extra, because the cost is a sum over the selected primes.

*Size of $S$.* An even $n\in S$ has no prime factor above $N/2$, since
such a factor $q$ would force $n=q$, which is odd. So every element of $S$
is $z$-smooth, and $|S|\le\Psi(N,z)$, the number of $z$-smooth integers
up to $N$. Rankin's method gives, for $x\ge y\ge e^2$ and
$v=\log x/\log y$,

$$
\Psi(x,y)\le C_0\,x\,e^{-v/2}\log y
\tag{3}
$$

with an absolute constant $C_0$. Indeed, with $\sigma=1-1/(2\log y)$ we
have $\sigma\ge3/4$, $\Psi(x,y)\le x^{\sigma}\prod_{p\le y}(1-p^{-\sigma})^{-1}$
and $x^{\sigma}=xe^{-v/2}$. For $p\le y$ convexity gives
$p^{1-\sigma}\le1+0.65\log p/\log y$, so Mertens' estimates bound
$\sum_{p\le y}p^{-\sigma}$ by $\log\log y+O(1)$; the higher prime powers
contribute $O(1)$ because $\sigma\ge3/4$. With $x=N$, $y=z$ and $v=u$,
(3) gives $|S|\le C_0N/(u\log N)$. Since $\pi(N)-\pi(N/2)\sim N/(2\log N)$
and $u\to\infty$, the primes $q_s$ exist for large $N$.

*Cost.* By Mertens,
$\sum_{z<p\le N/2}1/p=\log(\log(N/2)/\log z)+O(1/\log z)=\log u+o(1)$.
The class of $2$ costs $1/2$, and the cleanup primes cost less than
$2|S|/N=O(1/(u\log N))$. This proves (2).

The smooth-number asymptotic $\Psi(N,N^{1/u})=Nu^{-(1+o(1))u}$ in the
range needed here (Hildebrand, J. Number Theory 22 (1986), 289–307)
allows $u=(1+o(1))\log\log N/\log\log\log N$ and lowers the bound to
$\log\log\log N-\log\log\log\log N+O(1)$. The construction uses the prime
$2$, so it does not give Erdős's stated lower bound for the prime window
of [[problems/integer_sequences/E0688/_index|Problem 688]], which allows
no small primes.

**Consequence for the source's Problem 2.** Fix a sufficiently large $K$.
Proposition 1 gives a cover of $[1,N]$ of cost at most $K$, with no
survivor, at every large $N$ with
$\log\log\log N+\tfrac12+\log4+o(1)\le K$. So the positive-proportion
conclusion of
[[../library/primes/erdos_1980_small_sieve/problem_2|Problem 2 of Erdős and Ruzsa]]
cannot hold for all $x$, unlike their zero-residue Theorem 1. It can only
hold for $x\ge x_0(K)$, and then
$x_0(K)\ge\exp\exp\exp\bigl(K-\tfrac12-\log4-o(1)\bigr)$.

**Centered construction.** The extra prime $2$ can be omitted by choosing
one common center for the middle classes. Put $b=\lfloor N/2\rfloor+1$,
take $z=N^{1/u}$ as above, and give every prime $z<p\le N/2$ the class
$b\pmod p$. The middle set is nonempty for large $N$, so $b$ itself is
covered. Every other $n\le N$ has $0<|n-b|\le\lfloor N/2\rfloor$.
Thus it is uncovered precisely when $|n-b|$ is $z$-smooth. The exact
survivor count is

$$
|S_b|=\Psi(b-1,z)+\Psi(N-b,z)\le2\Psi(N/2,z).
$$

With $u=4\log\log N$, apply (3) at $x=N/2$, $y=z$ and
$v=u-\log2/\log z$. It gives $|S_b|=O(N/(u\log N))$, so the same
distinct-prime cleanup in $(N/2,N]$ works for all large $N$. Its cost is
$o(1)$, and the middle-prime cost is $\log u+o(1)$. Consequently

$$
\mu(N)\le\log\log\log N+\log4+o(1).
\tag{27}
$$

In particular the preceding lower restriction on $x_0(K)$ strengthens to
$\exp\exp\exp(K-\log4-o(1))$. This construction is globally coherent
within every $N$ and requires no separately optimized index classes. For
each *fixed* $u$, however, Dickman's asymptotic gives
$|S_b|=(\rho(u)+o(1))N$, whereas $T_N\sim N/(2\log N)$. Hence no fixed
$u$ in this centered construction supplies (24) for all large $N.
The improvement in (27) is a by-product, not a bounded-cost cover.

## Where the explicit cover loses

The construction asks the top primes to clean up every survivor of a
middle block with residue $0$. That design is capped at
triple-logarithmic cost.

**Zero-residue barrier.** Suppose a cover of $[1,N]$ of cost $K$ uses
residue $0$ for every selected prime except $2$ and the selected primes in
$(N/2,N]$. Then $K\ge c_{\mathrm{ER}}^{-1}\log\log\log N-O(1)$, where
$c_{\mathrm{ER}}$ is the absolute constant of Theorem 1 of Erdős and
Ruzsa.

*Proof, relying on that published theorem.* Let $Z_0$ be the selected
primes in $[3,N/2]$, all with residue $0$, and let $F(x,A)$ count the
integers up to $x$ divisible by no member of $A$. The theorem gives
$F(x,A)\ge e^{-e^{c_{\mathrm{ER}}k}}x$ for every $x$ and every prime set
$A$ of reciprocal sum at most $k$. Let $T$ be the integers up to $N$ in
no selected class of a prime of $Z_0\cup\{2\}$. If $a_2=1$, then $T$
consists of the $2m$ with $m\le N/2$ divisible by no member of $Z_0$, so
$|T|\ge e^{-e^{c_{\mathrm{ER}}K}}N/2$. If $2$ is not selected or
$a_2=0$, then $T$ contains every integer up to $N$ divisible by no member
of $Z_0\cup\{2\}$, a set of reciprocal sum at most $K+1/2$, so
$|T|\ge e^{-e^{c_{\mathrm{ER}}(K+1/2)}}N$. In both cases at least
$e^{-e^{c_{\mathrm{ER}}(K+1/2)}}N/2$ integers must be covered by the
selected primes in $(N/2,N]$, each of whose classes meets $[1,N]$ in at
most two integers. Hence

$$
\tfrac12e^{-e^{c_{\mathrm{ER}}(K+1/2)}}N\le2\bigl(\pi(N)-\pi(N/2)\bigr)
=(1+o(1))\frac N{\log N},
$$

so $e^{c_{\mathrm{ER}}(K+1/2)}\ge\log\log N-O(1)$, which gives the claim.

With a top block $(N^{1-\eta},N]$, of capacity at most $(2\eta+o(1))N$
for $\eta\le1/2$, the same argument requires
$e^{-e^{c_{\mathrm{ER}}(K+1/2)}}\le4\eta+o(1)$. The barrier concerns
residue $0$ only. It says nothing about middle blocks with other classes,
including a common nonzero translate.

For the centered construction there is also a direct barrier. Suppose
all non-cleanup classes have a common integer center $b\in[1,N]$, with
cleanup only from $(N/2,N]$, and the total cost is $K$. One side of $b$ has
length $L\ge(N-1)/2$. On that side the surviving distances are exactly
the positive integers up to $L$ divisible by none of the middle primes.
The same Erdős–Ruzsa theorem leaves at least
$e^{-e^{c_{\mathrm{ER}}K}}L$ such distances. Every cleanup class covers
at most two points, so comparison with $2T_N=O(N/\log N)$ again forces
$K\ge c_{\mathrm{ER}}^{-1}\log\log\log N-O(1)$. This argument uses a
center inside the covered interval; it supplies no uniform bound for an
unrestricted CRT translate.

An algebraic concurrency formula can still describe a common center.
For example, if $\mu_p\equiv M\pmod p$, then the rule
$a_p\equiv\mu_p^3\pmod p$ is simply $a_p\equiv M^3\pmod p$.
Likewise, for $p=v+du$ and $a_p\equiv w-ud^3\pmod p$ with $p\nmid u$,
one has $u^2a_p\equiv u^2w+v^3\pmod p$, independent of $d$.
These identities do not forbid useful choices of the parameters. They
show why counting some concurrent triples in those coordinates does not
yet supply the net-gain estimate (24). A general rational center, or an
integer center outside $[1,N]$, is not handled by the preceding barrier.

## Exact capacity after a finite prime core

Suppose $P$ and its classes cover $[1,N]$. Choose any subset $F\subseteq P$
as a core, and write

$$
M=\prod_{p\in F}p,\qquad
\delta=\prod_{p\in F}(1-1/p)=\varphi(M)/M,
\qquad s=|P\setminus F|.
$$

Empty products are one. The core leaves exactly $\varphi(M)$ residue
classes modulo $M$, so the number $R$ of its survivors in $[1,N]$
satisfies

$$
R\ge\delta N-\varphi(M).
\tag{4}
$$

For a tail prime $p\in P\setminus F$, CRT expresses the intersection of its
class with the core survivors as exactly $\varphi(M)$ classes modulo $Mp$.
Its size in $[1,N]$ is therefore at most

$$
\delta N/p+\varphi(M).
\tag{5}
$$

Every core survivor must be covered by a tail class. Union counting of (5)
followed by (4) gives the exact necessary inequality

$$
\boxed{\quad
\sum_{p\in P\setminus F}\frac1p
\ge 1-\frac{M(s+1)}N.
\quad}
\tag{6}
$$

The classes are arbitrary throughout. The estimate holds even when its
right side is negative, and is informative only when $M$ is small: a
varying core must keep its actual product in the error. For a fixed core,
$s\le\pi(N)=o(N)$, so every sequence of covers containing that core has
cost at least

$$
1+\sum_{p\in F}\frac1p-o(1).
\tag{7}
$$

For example, covers containing $2$ have asymptotic cost at least $3/2$,
and covers containing $2$ and $3$ at least $11/6$. No cover is claimed to
contain either prime.

## Uniform localization of the reciprocal mass

The core inequality controls only cores of small product. Sieve theory
removes that restriction for every core of small primes.

**The fundamental lemma in the form used.** There are absolute constants
$C_1,C_2$ with the following property. Let $\mathcal Q$ be a set of primes
at most $w$, with one residue class chosen modulo each, and put
$V=\prod_{p\in\mathcal Q}(1-1/p)$. Let $I$ consist of $L$ consecutive
terms of an arithmetic progression whose difference is prime to every
member of $\mathcal Q$. Then for $s\ge10$ the number of $n\in I$ avoiding
every chosen class is

$$
LV\bigl(1+\vartheta C_1e^{-s}\bigr)+\vartheta'C_2w^{s},
\qquad|\vartheta|,|\vartheta'|\le1.
\tag{8}
$$

This is the dimension-one fundamental lemma at level $D=w^s$. Its
hypotheses hold: for squarefree $d$ composed of primes of $\mathcal Q$,
the members of $I$ lying in the chosen classes for all $p\mid d$ number
$L/d+r_d$ with $|r_d|\le1$, and the density $g(p)\in\{0,1/p\}$ meets the
dimension-one condition with an absolute constant by Mertens' product.

**Theorem A.** There is an absolute constant $C_3$ with the following
property. Let $K\ge0$, $0<\eta\le1/2$ and $0<\theta\le\eta/20$. For
$N\ge N_0(K,\eta)$, every cover of $[1,N]$ of cost at most $K$ satisfies

$$
\sum_{\substack{p\in P\\ N^{\theta}<p\le N^{1-\eta}}}\frac1p
\ \ge\ 1-C_3e^{-\eta/(2\theta)}-2e^{K+1}\eta-o(1),
\tag{9}
$$

where $o(1)\to0$ as $N\to\infty$ for fixed $K$ and $\eta$. Consequently
the selected primes up to $N^{\theta}$ have reciprocal sum at most
$K-1+C_3e^{-\eta/(2\theta)}+2e^{K+1}\eta+o(1)$.

*Proof.* Split $P$ into $P_1=P\cap[2,N^{\theta}]$,
$P_2=P\cap(N^{\theta},N^{1-\eta}]$ and $P_3=P\cap(N^{1-\eta},N]$, with
reciprocal sums $m_1,m_2,m_3$. Let $S$ be the integers in $[1,N]$ avoiding
the classes of $P_1$, and $V=\prod_{p\in P_1}(1-1/p)$. Apply (8) with
$w=N^{\theta}$ and $s=\eta/(2\theta)\ge10$, so that $w^s=N^{\eta/2}$.
With $I=[1,N]$ it gives $|S|\ge NV(1-C_1e^{-s})-C_2N^{\eta/2}$. For
$q\in P_2$, the class $A_q$ is a progression of difference $q$ with at most
$N/q+1$ terms, and (8) gives
$|A_q\cap S|\le(N/q+1)V(1+C_1e^{-s})+C_2N^{\eta/2}$. For $q\in P_3$ use
$|A_q\cap S|\le N/q+1$. The classes of $P_2\cup P_3$ must cover $S$.
Summing, dividing by $NV$ and using $|P_2|\le N^{1-\eta}$ gives

$$
1-C_1e^{-s}\le(1+C_1e^{-s})\Bigl(m_2+\frac{\pi(N)}N\Bigr)
+\frac{2C_2N^{-\eta/2}}V+\frac{m_3+\pi(N)/N}V .
$$

Mertens gives $m_3\le\log\frac1{1-\eta}+O(1/\log N)\le2\eta+O(1/\log N)$.
Since $-\log(1-1/p)\le1/p+1/(p(p-1))$ and $\sum_p1/(p(p-1))<1$, we have
$1/V\le e^{m_1+1}\le e^{K+1}$. Rearranging gives (9) with $C_3=2C_1$, and
the last statement follows from $m_1\le K-m_2$. ∎

**Corollary (exponent window).** Given $K$ and $\varepsilon\in(0,1)$, put
$\eta=\varepsilon e^{-K-1}/4$ and choose $\theta\le\eta/20$ with
$C_3e^{-\eta/(2\theta)}\le\varepsilon/2$. For large $N$, every cover of
cost at most $K$ has reciprocal mass at least $1-\varepsilon-o(1)$ on
primes in $(N^{\theta},N^{1-\eta}]$, and at most $K-1+\varepsilon+o(1)$
on primes up to $N^{\theta}$. In a bounded-cost family, almost one unit
of mass therefore lies at exponents in a fixed compact subinterval of
$(0,1)$, at every large $N$ and not only in a limit.

This recovers, up to its small error terms, the statements for fixed
cores and for primes comparable to $N$: a fixed core is part of $P_1$, and
a top block $(\alpha N,N]$ lies in $P_3$. Small primes up to $N^{\theta}$,
in any number and with any classes, followed only by primes above
$N^{1-\eta}$, cannot cover once $2e^{K+1}\eta+C_3e^{-\eta/(2\theta)}<1$.
This is the uniform survivor estimate against the top cleanup capacity.
It says nothing about the middle window, where every construction and
every obstruction must act.

**Lemma S (arbitrary classes below the square root).** Fix
$0<\delta<1/4$ and $K\ge0$. For $x\ge x_0(\delta,K)$, let $\mathcal Q$ be
any set of primes at most $x^{1/2-\delta}$ with
$\sum_{p\in\mathcal Q}1/p\le K$, with one class chosen modulo each. Then
at least

$$
\tfrac12f(s_\delta)\,e^{-K-1}x,\qquad s_\delta=\frac{2(1-\delta)}{1-2\delta}>2,
\tag{25}
$$

integers of $[1,x]$ avoid every chosen class. Here $f$ is the lower
function of the linear sieve, $f(s)=2e^{\gamma}\log(s-1)/s$ for
$2\le s\le4$, which is positive for $s>2$.

*Proof.* Apply the linear sieve lower bound to $[1,x]$ with level
$D=x^{1-\delta}$ and sifting limit $z=x^{1/2-\delta}$. For squarefree $d$
composed of primes of $\mathcal Q$, the integers of $[1,x]$ in the chosen
class for every $p\mid d$ form one class modulo $d$, so their number is
$x/d+r_d$ with $|r_d|\le1$, and the remainders with $d<D$ sum to at most
$D$. The density $1/p$ on $\mathcal Q$, and $0$ off it, satisfies the
dimension-one condition with an absolute constant by Mertens' product.
With $s=\log D/\log z=s_\delta$, the fixed-$s$ lower bound in Iwaniec's
form gives at least $xV(f(s_\delta)-o_\delta(1))-x^{1-\delta}$ survivors, where
$V=\prod_{p\in\mathcal Q}(1-1/p)\ge e^{-K-1}$ as in the proof of
Theorem A. ∎

So the positive-proportion assertion of
[[../library/primes/erdos_1980_small_sieve/problem_2|Problem 2 of Erdős and Ruzsa]]
holds when every sifting prime is at most $x^{1/2-\delta}$. In a cover of
$[1,N]$ of cost at most $K$, the selected primes above $N^{1/2-\delta}$
must therefore cover at least (25) integers that no smaller selected
prime covers, while their total mass is at most
$\log(2/(1-2\delta))+o(1)$ for every cover. This is a reduction of the
negative route, not a survivor estimate for any cover: the top primes'
capacity $(\log2+O(\delta))N$ far exceeds (25), and $f(2)=0$, so the
lemma gives nothing once the sifting primes reach $\sqrt N$.

## A finite survivor inequality with explicit errors

The localization conclusion also has an elementary version that uses no
fundamental lemma. This version retains every error and states exactly where
union counting ceases to help.

Let $F,B,T$ be the selected primes up to $y$, in $(y,z]$, and above $z$,
respectively. Set $f=|F|$ and, for an integer $j\ge0$, put

$$
H_j(F)=\sum_{\substack{D\subseteq F\\|D|\le j}}
 \frac{(-1)^{|D|}}{\prod_{p\in D}p},\qquad
D_j(f)=\sum_{i=1}^{\min(j,f)}\binom fi .
$$

Empty products are one and $D_0=0$. Define the exact capacity

$$
U(N,z)=\sum_{\substack{z<p\le N\\p\text{ prime}}}
 \left\lceil\frac Np\right\rceil .
$$

**Finite obstruction.** For every odd $h\ge1$, every choice of the classes
leaves at least

$$
Z\ \ge\ N H_h(F)-D_h(f)
-H_{h-1}(F)\sum_{q\in B}\left\lceil\frac Nq\right\rceil
-|B|D_{h-1}(f)-U(N,z)
\tag{15}
$$

survivors. In particular a positive right side rules out a cover, even if
all primes above $z$ are available for cleanup.

*Proof.* Bonferroni's inequalities and CRT give
$|S|\ge NH_h(F)-D_h(f)$ for the survivors $S$ of $F$: every nonempty
subset of $F$ specifies one class modulo its prime product, and its count
differs from $N/\prod_{p\in D}p$ by at most one. On a progression $A_q$
with $q\notin F$, the same argument with the even truncation $h-1$ gives
$|S\cap A_q|\le |A_q|H_{h-1}(F)+D_{h-1}(f)$. The upper Bonferroni
polynomial $H_{h-1}(F)$ is nonnegative. Use
$|A_q|\le\lceil N/q\rceil$ and subtract these upper bounds and the
capacity of all primes above $z$. This proves (15). No independence of
finite-interval congruences is assumed. ∎

Here is a uniform consequence with explicit choices. Fix $K\ge0$ and
$0<\varepsilon<1$, write $v_K=e^{-K-1}$, and choose any odd $h$ such that

$$
\frac{K^h}{h!}+\frac{K^{h+1}}{(h+1)!}
 \le\frac{\varepsilon v_K}{4}.
\tag{16}
$$

Such an $h$ exists. Put $\eta=\varepsilon v_K/8$ and
$\theta=\eta/(2h)$. For all sufficiently large $N$, any configuration
whose primes up to $N^\theta$ cost at most $K$ and whose primes in
$(N^\theta,N^{1-\eta}]$ cost at most $1-\varepsilon$ leaves at least
$\varepsilon v_K N/4$ integers uncovered, regardless of the classes and
of every choice of primes above $N^{1-\eta}$.

Indeed, write $V=\prod_{p\in F}(1-1/p)\ge v_K$. The elementary
symmetric sums satisfy $e_j((1/p)_{p\in F})\le K^j/j!$, and Bonferroni
applied to independent Bernoulli variables of parameters $1/p$ gives

$$
H_h(F)\ge V-\frac{K^{h+1}}{(h+1)!},\qquad
H_{h-1}(F)\le V+\frac{K^h}{h!}.
$$

Also $D_j(f)=O_h((1+f)^j)$, $f\le N^\theta$ and
$|B|\le N^{1-\eta}$. Thus every endpoint error in (15), divided by $N$,
tends to zero: the largest of these exponents is
$1-\eta+\theta(h-1)<1-\eta/2$. Mertens' estimate and $\pi(N)=o(N)$ give

$$
\frac{U(N,N^{1-\eta})}{N}
 \le\log\frac1{1-\eta}+o(1)\le2\eta+o(1).
$$

The lower bound in (15), divided by $N$, is consequently at least
$\varepsilon V-\varepsilon v_K/4-2\eta-o(1)
\ge\varepsilon v_K/2-o(1)$, proving the stated bound.

This is a genuine obstruction for a specified distribution of a bounded
budget, not a proof that every bounded budget fails. The middle mass must
be below one by a fixed amount. Once that mass reaches one, the leading
term $V(1-\sum_{q\in B}1/q)$ in this argument is nonpositive. Reducing
endpoint errors or increasing the Bonferroni order does not repair that
loss; an estimate for overlap among the middle classes is needed.

## Reciprocal mass that escapes every fixed cutoff

The diagonal form of the same phenomenon is elementary. Consider any
sequence of covers with $N_j\to\infty$ and bounded cost. Pass to a
subsequence on which the costs tend to $L$ and, for each fixed prime, its
inclusion and chosen residue eventually stabilize; this is possible
because each prime has finitely many choices, including absence. Let
$P_\infty$ be the primes eventually included, with stabilized residues,
and $\sigma_\infty=\sum_{p\in P_\infty}1/p$. Every finite subset of
$P_\infty$ occurs in every sufficiently late cover, so (7) gives

$$
L\ge1+\sigma_\infty,\qquad
\lim_{y\to\infty}\ \lim_{j\to\infty}
\sum_{\substack{p\in P_j\\p>y}}\frac1p=L-\sigma_\infty\ge1.
\tag{10}
$$

For each fixed $y$ the inner limit exists by stabilization and the
convergence of the costs. At least one unit of mass escapes to growing
primes, and compactness at each fixed prime loses it. The limiting
classes need not cover any particular integer, since the prime covering
it may grow with $j$. Theorem A gives the stronger, per-$N$ form: almost
one unit of mass lies at exponents bounded away from $0$ and $1$.

## Forced pair excess and cheap covers

**Lemma C (pair excess).** Fix $\delta\in(0,1/2)$. For any configuration
and each $p\in P$, let $L_p=|A_p|$ and

$$
\kappa_p=\sum_{\substack{r\in P,\ r\ne p\\ r\le L_p^{1/2-\delta}}}\frac1r .
$$

Then

$$
E\ \ge\ \frac12\sum_{p\in P}\Bigl(L_p\frac{\kappa_p}{1+\kappa_p}
-L_p^{1-2\delta}\Bigr),
\tag{11}
$$

and every cover has cost at least
$1+\frac12\sum_{p\in P}\frac1p\frac{\kappa_p}{1+\kappa_p}-o(1)$, where
$o(1)$ depends only on $\delta$.

*Proof.* Write $A_p=\{a+jp:0\le j<L_p\}$ with $1\le a\le p$. For a prime
$r\ne p$, the members of $A_p$ lying in $A_r$ are those whose index $j$
lies in one class $c_r\equiv(a_r-a)p^{-1}\pmod r$. Let $J_p$ be the set of
indices $j<L_p$ with $m(a+jp)\ge2$. It contains every $j<L_p$ in the class
$c_r$, for each $r$ counted in $\kappa_p$. So the complement of $J_p$ in
$[0,L_p)$ avoids one class modulo each such $r$. The arithmetic large
sieve bounds a set of integers in an interval of length $L$ that avoids
one class modulo each prime of a set $\mathcal R$ by
$(L+Q^2)/(1+\sum_{r\in\mathcal R,\,r\le Q}1/(r-1))$. With
$Q=L_p^{1/2-\delta}$ this gives
$|J_p|\ge L_p\kappa_p/(1+\kappa_p)-L_p^{1-2\delta}$. An integer $n$ with
$m(n)\ge2$ is counted in $J_p$ for exactly $m(n)$ primes $p$, and
$m\le2(m-1)$ when $m\ge2$; hence $\sum_p|J_p|\le2E$, which is (11). For a
cover, (1) gives cost at least $1+E/N-\pi(N)/N$. Finally $L_p\ge N/p-1$
and $\sum_{p\le N}(N/p+1)^{1-2\delta}=o(N)$. ∎

**Theorem B (cheap covers avoid primes below $N^{1/3}$).** Fix
$\tau\in(0,1/3)$ and $\lambda\in(0,1]$. For $N\ge N_0(\tau,\lambda)$,
every cover of $[1,N]$ whose selected primes up to $N^{\tau}$ have
reciprocal sum at least $\lambda$ costs at least $1+\lambda^2/7$. So for
$0<c\le1/8$ and $N\ge N_0(\tau,c)$, a cover of cost at most $1+c$ has
reciprocal mass less than $\sqrt{8c}$ on primes up to $N^{\tau}$.

*Proof.* Take $\delta=\frac12\bigl(\frac12-\frac{\tau}{1-\tau}\bigr)>0$.
For a selected $p\le N^{\tau}$ we have $L_p\ge N^{1-\tau}-1$ and
$(1-\tau)(1/2-\delta)=(1+\tau)/4>\tau$, so $L_p^{1/2-\delta}>N^{\tau}$
for large $N$. Hence $\kappa_p\ge\lambda-1/p$ for every selected
$p\le N^{\tau}$. If some selected $p_0<2/\lambda$, the core inequality
(7) for the fixed core $\{p_0\}$ gives cost at least
$1+1/p_0-o(1)>1+\lambda/2-o(1)$. Otherwise $\kappa_p\ge\lambda/2$ for each
selected $p\le N^{\tau}$, and Lemma C gives cost at least
$1+\frac12\lambda\cdot\frac{\lambda/2}{1+\lambda/2}-o(1)\ge1+\lambda^2/6-o(1)$.
For the last sentence apply this with $\lambda=\sqrt{8c}$. ∎

Thus the counting bound $\mu(N)\ge1-o(1)$ can only be approached by covers
whose mass lies, up to a vanishing amount, on primes in
$(N^{1/3-o(1)},N]$. By Theorem A it also lies below $N^{1-\eta}$ up to
$O(\eta)$. The zero-residue cover above, with mass at every scale down to
$N^{1/u}$, is far from this regime.

## Windows above N^(1/3): zero residues and rich points

Above $N^{1/3}$ no integer up to $N$ has three selected prime factors,
and every forced intersection comes from a pair. Let
$P\subseteq(N^{1/3},N]$. For $n\le N$ let $a(n)$ be the number of selected
$p\le\sqrt N$ with $n\in A_p$, let $\mathrm{sh}(n)$ be the number of pairs
$\{p,q\}\subseteq P$ with $pq\le N$ and $n\in A_p\cap A_q$, and put

$$
\mathrm{Def}(n)=\bigl(\mathrm{sh}(n)-(m(n)-1)_+\bigr)_+ .
$$

Two primes above $\sqrt N$ have product above $N$, so
$\mathrm{sh}(n)\le\binom{a(n)}2+a(n)\bigl(m(n)-a(n)\bigr)$, and
$\mathrm{Def}(n)=0$ unless $a(n)\ge2$. Call $n$ *rich* when
$\mathrm{Def}(n)>0$: it lies in at least two classes of primes up to
$\sqrt N$ and in a third class forming short pairs with two of the
others.

**Window lemma.** For every $P\subseteq(N^{1/3},N]$ and every choice of
classes,

$$
Z\ \ge\ Z_0(P)-\sum_{n\le N}\mathrm{Def}(n)-O\Bigl(\frac N{\log N}\Bigr),
\tag{12}
$$

where $Z_0(P)$ is the number of $n\le N$ divisible by no prime of $P$,
the survivor count of the zero classes. The zero classes have no rich
points.

*Proof.* By definition $(m-1)_+\ge\mathrm{sh}-\mathrm{Def}$, so (1) gives
$Z\ge N-\sum_p|A_p|+\sum_n\mathrm{sh}(n)-\sum_n\mathrm{Def}(n)$. Each
intersection $A_p\cap A_q$ with $pq\le N$ is one class modulo $pq$, so
$\sum_n\mathrm{sh}(n)\ge\sum_{pq\le N}\lfloor N/pq\rfloor$; also
$|A_p|\le\lfloor N/p\rfloor+1$. No $n\le N$ has three prime factors above
$N^{1/3}$, so inclusion–exclusion is exact for the zero classes:
$Z_0(P)=N-\sum_p\lfloor N/p\rfloor+\sum_{pq\le N}\lfloor N/pq\rfloor$.
The two bounds differ by at most $\pi(N)=O(N/\log N)$. For the zero classes
$m(n)\le2$, and a point with $m=2$ carries exactly one pair, so
$\mathrm{Def}\equiv0$. ∎

For the full window $P=(N^{\theta},N]$ with $1/3\le\theta<1/2$,
$Z_0(P)=\Psi(N,N^{\theta})=(\rho(1/\theta)+o(1))N$. So the zero classes
are optimal up to $O(N/\log N)$ among configurations without rich points,
and a cover by these primes needs a rich-point deficit
$\sum_n\mathrm{Def}(n)\ge(\rho(1/\theta)-o(1))N$. At $\theta=1/3$ the
reciprocal mass is $\log3+o(1)$ and $\rho(3)\approx0.0486$; at
$\theta=1/e$ the mass is $1+o(1)$ and $\rho(e)\approx0.0863$. A cover
of $[1,N]$ by the primes in $(N^{1/3},N]$ for every large $N$ would prove
the erdosproblems.com assertion with every fixed $C>\log3$.

### A coordinated gain and an obstruction to combining small groups

Rich points can give a genuine gain with no change in class cardinalities.
At $N=105$, take $P=\{5,7,11\}$. The zero classes have sizes $21,15,9$;
their pair intersections have sizes $3,1,1$, and their triple
intersection is empty. Their union therefore has size $40$. The classes

$$
a_5=0,\qquad a_7=6,\qquad a_{11}=0
\tag{17}
$$

have the same individual and pair-intersection sizes, but all three meet
at $55$. Their union has size $41$. All three primes exceed $105^{1/3}$,
and every class still has exactly $\lfloor105/p\rfloor$ members. This is
a boundary-free improvement for this selected prime set, not a cover and
not an improvement for the full prime window. The
[[research/leads/bounded_cost_prime_covers/evidence/_index|exact witness check]]
recounts the classes, intersections and union.

Replicating fixed-size groups of this kind does not remove a positive
proportion of the zero-class survivors. The obstruction concerns the
actual incidences, so it also applies to more complicated constructions
whenever those incidences decompose into small groups.

For $P\subseteq(N^{1/3},N]$, call a triple of distinct selected primes a
*realized short triangle* if all three pair products are at most $N$ and
their three classes meet at an integer in $[1,N]$. Form a graph on $P$
by joining any two primes that belong to such a triangle. Put
$s=|P\cap[2,\sqrt N]|$, and let $d$ be the largest degree of a vertex
in this small-prime set, with $d=0$ if the set is empty.

**Interaction obstruction.** Every such configuration satisfies

$$
Z\ \ge\ \Psi(N,N^{1/3})-|P|
-\frac{s d(d-1)}4.
\tag{18}
$$

Consequently, if $d=o(N^{1/4}\sqrt{\log N})$, then
$Z\ge(\rho(3)-o(1))N$. In particular a cover for large $N$ requires

$$
d\ \ge\ \bigl(\sqrt{2\rho(3)}-o(1)\bigr)
 N^{1/4}\sqrt{\log N}.
\tag{19}
$$

*Proof.* Fix $n$ and order the selected primes whose classes contain it as
$p_1<\cdots<p_m$. First suppose $m\ge2$. Join $p_i,p_j$ when $p_ip_j\le N$.
If $d_i$ is the number of earlier neighbors of $p_i$, those neighbors form
an initial
segment and a clique. Indeed their largest prime $q$ satisfies
$q p_i\le N$, so the product of any two of them is at most $q p_i$.
Writing $k=|\{i\ge2:d_i>0\}|\le m-1$, we obtain

$$
\begin{aligned}
\mathrm{Def}(n)
&=\left(\sum_i d_i-(m-1)\right)_+\\
&\le\sum_{i:d_i>0}(d_i-1)
\le\sum_i\binom{d_i}{2}.
\end{aligned}
$$

The last sum counts the short triangles at $n$, once each by its largest
prime. The assertion also holds for $m=0$ or $1$, when both sides are zero.
Each triple of primes above $N^{1/3}$ has product greater than $N$, so CRT
allows it to meet at at most one integer of $[1,N]$. Thus the sum of the
deficits is at most the total number of realized short triangles.

Every such triangle contains at least two primes at most $\sqrt N$. At
each small-prime vertex there are at most $\binom d2$ candidate triangles.
Counting every triangle at at least two small-prime vertices bounds their
total by $s\binom d2/2=s d(d-1)/4$. The proof of (12) gives the exact
bound $Z\ge Z_0(P)-|P|-\sum_n\mathrm{Def}(n)$, and
$Z_0(P)\ge\Psi(N,N^{1/3})$. This proves (18).

Finally, $s\le\pi(\sqrt N)=(2+o(1))\sqrt N/\log N$,
$|P|=o(N)$ and $\Psi(N,N^{1/3})=(\rho(3)+o(1))N$. Substitution gives the
survivor statement and, when $Z=0$, (19). ∎

A component containing a vertex of degree $d$ has at least $d+1$ primes.
Thus components of size $o(N^{1/4}\sqrt{\log N})$ cannot cover, and even
large components with degrees below that scale cannot cover. The conclusion
is restricted to the $N^{1/3}$ window and to the defined interaction graph.
A construction described using small groups is not excluded if cross-group
triangles create large degrees. Large degrees and components are necessary
here, not sufficient: extra intersections can waste more
capacity than the short triangles save. The unrestricted intermediate-prime
problem remains open.

The obstruction also composes with a fixed finite core $F$ of primes and
arbitrary core residues. Write $F_0=\{p\in F:a_p=0\}$,
$D=\prod_{p\in F\setminus F_0}p$ and
$c_F=D^{-1}\prod_{p\in F_0}(1-1/p)>0$. For the additional primes
$P\subseteq(N^{1/3},N]$, define $s,d$ as above. Then

$$
Z\ \ge\ (c_F\rho(3)-o_F(1))N-\frac{s d(d-1)}4.
\tag{20}
$$

To see this, let $S$ be the core survivors. For any class modulo $p$ or
$pq$, with $p,q\notin F$, CRT counts its intersection with $S$ as
$\varphi(M)N/(M p)$ or $\varphi(M)N/(M pq)$, with error at most
$\varphi(M)$, where $M=\prod_{r\in F}r$. Compare arbitrary middle classes
with zero middle classes inside $S$ in the proof of (12). The singleton
and short-pair endpoint errors sum to $O_F(N/\log N)$: there are at most
$\pi(N)$ singletons and $O(N/\log N)$ pairs of primes above $N^{1/3}$
whose product is at most $N$. The latter estimate follows by summing
$\pi(N/p)\ll N/(p\log N)$ over $N^{1/3}<p\le\sqrt N$.
The deficit inside $S$ is no greater than the same triangle bound.

For the zero-middle baseline, every number $Dt\le N$ with $t$ composed
of primes at most $N^{1/3}$ and divisible by no prime in $F_0$ survives.
Inclusion–exclusion on the fixed set $F_0$, followed by Dickman's
asymptotic, counts these numbers as

$$
\sum_{E\subseteq F_0}(-1)^{|E|}
 \Psi\left(\frac{N}{D\prod_{p\in E}p},N^{1/3}\right)
 =(c_F\rho(3)+o_F(1))N.
$$

This proves (20). It excludes low-degree interactions even after a fixed
core; it gives no uniform constant when the core grows with $N$.

In the index coordinates of Lemma C, the classes of the other selected
primes $r\le N/p$ meet $A_p$, for $p\le\sqrt N$, in full residue classes
modulo $r$ of the interval $[0,L_p)$. Every such modulus exceeds
$\sqrt{L_p}$, so the large sieve says nothing there. Coherent coincidences
among these index classes can create the short triangles that a rich point
requires; an arbitrary triple intersection need not have positive deficit.

**Lemma D (reduction to one-dimensional unions).** For $L\ge1$ and a
finite set $R$ of primes, let $u(L,R)$ be the least number of integers in
$[0,L)$ lying in at least one chosen class, over all choices of one residue
class modulo each $r\in R$. For every configuration,

$$
Z\ \ge\ N-\sum_{p\in P}|A_p|+\sum_{p\in P}u\bigl(|A_p|,\{r\in P:r<p\}\bigr).
\tag{13}
$$

*Proof.* An integer $n$ with $m(n)\ge1$ lies in the classes of its $m(n)$
selected primes, and for all of them except the smallest it also lies in
the class of a smaller selected prime. Hence
$E=\sum_{p\in P}\bigl|A_p\cap\bigcup_{r\in P,\,r<p}A_r\bigr|$. In the index
coordinates of $A_p$, the set on the right is the union of one residue
class modulo each selected $r<p$, restricted to $[0,|A_p|)$, so its size
is at least $u(|A_p|,\{r\in P:r<p\})$. Insert this into (1). ∎

For moduli below $L^{\varepsilon}$ with $\varepsilon\le1/20$, (8) gives
$u(L,R)=\bigl(1-\prod_{r\in R}(1-1/r)\bigr)L+O(e^{-1/(2\varepsilon)}L+\sqrt L)$,
the value of random classes, whatever the classes. Above $\sqrt L$ classes
can coincide and $u$ can be smaller. The zero classes intersect only at
$0$ in $[0,L)$, and have union size $\sum_{r\in R}L/r+O(|R|)$; no
configuration can exceed this leading term. Put

$$
I(\theta)=\int_{\theta}^{1/2}\Bigl(1-\frac{\theta}{t}\Bigr)\frac{dt}{t}
+\int_{1/2}^{1-\theta}\Bigl(1-\frac{\theta}{1-t}\Bigr)\frac{dt}{t},
$$

so that $I(1/3)\approx0.1288$ and $I(1/e)\approx0.0779$. Suppose that for
some $\lambda\in(0,1]$,

$$
u\bigl(L,\{r\ \text{prime}:L^a<r\le L^b\}\bigr)\ \ge\
\bigl(\lambda(1-a/b)-o(1)\bigr)L
\tag{14}
$$

uniformly for $1/2\le a<b\le1$. Apply (13) to the full window
$P=(N^{\theta},N]$ with $1/3\le\theta<1/2$. For $p=N^t$, the selected
$r<p$ above $N/p$ meet $A_p$ in at most one point; discarding those moduli
only weakens the lower bound for the union. The others are the primes in
$(L^a,L^b]$ for $L=|A_p|\approx N^{1-t}$, with $a=\theta/(1-t)\ge1/2$ and
$b=t/(1-t)$ for $t\le1/2$, $b=1$ for $t>1/2$. By Mertens' estimates (13)
and (14) give

$$
Z\ \ge\ \bigl(1-\log(1/\theta)+\lambda I(\theta)-o(1)\bigr)N .
$$

So (14) with $\lambda>0.766$ would show that the primes in $(N^{1/3},N]$
cannot cover $[1,N]$ for large $N$. With any $\lambda>0$ the bound is
positive at $\theta=1/e$ and, by continuity, on some interval
$(\theta^*,1/e]$; together with counting above $1/e$, this would improve
the bound $\limsup\epsilon_n\le1/e$ of Problem 688 to
$\limsup\epsilon_n\le\theta^*<1/e$. The zero classes give the value
$\Pi(\theta)=\rho(1/\theta)-1+\log(1/\theta)$ in place of
$\lambda I(\theta)$, and (13) is lossy because the minimizing classes for
different $p$ need not be compatible.

## A fractional cover is already cheap

The direct fractional relaxation does not supply the missing construction.
Let $x_{p,a}\ge0$ be a fractional choice of a class, impose
$\sum_{a\bmod p}x_{p,a}\le1$ for each prime, and ask for
$\sum_px_{p,n\bmod p}\ge1$ for every $n\le N$, at cost
$\sum_pp^{-1}\sum_ax_{p,a}$. For every $N\ge5$ the point
$x_{2,a}=1/2$, $x_{3,a}=1/3$, $x_{5,a}=1/6$ for every residue of the
respective prime, with all other variables zero, is feasible of cost
exactly one. Any integral choice supported on those three primes misses a
class modulo $30$. A rounding theorem using more primes at uniformly
bounded cost would itself prove the erdosproblems.com assertion, so the relaxation
leaves the difficulty intact. Theorem B shows more: integral covers of
cost near one cannot use the small primes that this fractional point uses.
The fractional optimum need not equal one at finite $N$. At $N=6$, put
$x_{2,0}=x_{2,1}=4/9$, $(x_{3,0},x_{3,1},x_{3,2})=(2/9,2/9,5/9)$ and
$x_{5,1}=x_{5,3}=x_{5,4}=1/3$, with the other weights zero. Each integer
receives weight one and the cost is $44/45$. Union counting still bounds
the fractional optimum below by $1-\pi(N)/N$, so it tends to one.

## Finite probes

The [[research/leads/bounded_cost_prime_covers/evidence/_index|seeded checks and probes]]
verify the recipe of Proposition 1 exactly at $N=10^4$, $10^5$ and $10^6$.
With the cutoff tuned to the cleanup capacity, the same design gives
actual covers of cost about $1.6367$, $1.6376$ and $1.6430$, so
$\mu(N)<1.65$ at these three orders. Finite values say nothing about the
growth of $\mu$. The centered construction (27), with the largest tested
prime cutoff up to $\sqrt N$ fitting the reserved cleanup supply, gives
costs about $1.303720$, $1.296358$ and $1.269080$ at the same orders.
The evidence checks each cover and the strict bound $131/100$ by integer
arithmetic. These values also have only the stated finite scope.

Two probes bear heuristically on the next test. In the window $(N^{1/3},N]$
with every class forced to have exactly $\lfloor N/p\rfloor$ points, so that
only rich points can beat zero residues, no change of a single prime's class
improves the zero classes at $N=3\cdot10^4$ or $10^5$. A local search from
random classes stalls near $0.20N$ survivors, against $0.087N$ for the zero
classes at $N=10^5$. Seeded annealing at $N=3\cdot10^4$ never goes below the
zero classes when started there, and from random classes it ends near
$0.22N$, against $0.109N$. In the union problem of Hypothesis H for the
primes in $(L^{1/2},L^{9/10}]$, of reciprocal sum about $0.56$ to $0.58$,
greedy and local search reach unions of $0.274L$, $0.298L$, $0.301L$,
$0.309L$ and $0.320L$ at $L=3000$, $10^4$, $3\cdot10^4$, $10^5$ and
$3\cdot10^5$, against about $0.43L$ to $0.44L$ for random classes and
$0.53L$ to $0.57L$ for zero classes. Full classes do concentrate, but the
best union found is a constant proportion of the interval, rising from about
$0.64$ to $0.72$ of the random value as $L$ grows. A search only bounds $u$
from above. The observed ratio to the main term $(1-a/b)L=4L/9$ of (14)
reaches about $0.72$, but no finite sample bounds its asymptotic constant
$\lambda$ without a quantified remainder. Whether the ratio keeps rising
is open. The probes are consistent with zero residues being extremal in the
first window, which is the direction of the negative answer, and decide
nothing asymptotic. A last probe measures the excess $X_S$ of (26) for the
primes in $(N^{1/3},\sqrt N]$ alone. Coordinate ascent from seeded random
classes of exactly $\lfloor N/p\rfloor$ points reaches $0.0063N$ at
$N=10^6$ and $0.0065N$ at $N=10^7$, a little above the expected excess
for unrestricted uniform residues, $0.0041N$ and $0.0053N$; about $0.001N$
integers then lie in four
or more of the classes. Seeded annealing at $N=10^6$ ends at $0.0065N$.
In the wider windows $(N^{1/4},N]$ and $(N^{1/5},N]$ the zero classes
admit no improving single change of class at $N=3\cdot10^4$ or $10^5$.

## The open input and the next discriminating test

**The gap.** Both routes stop at the same place: the classes of the
primes in a middle window of exponents $(N^{\theta},N^{1-\eta}]$, acting
on the survivors of the small primes. By (8) those survivors have the
expected count, up to the error in (8), in every progression of modulus
up to $N^{1-\eta}$. Any gain over a random choice of classes must
therefore come from coincidences among the middle classes. The zero
classes coincide at integers with several middle prime factors and leave
the smooth integers, a positive proportion. The affirmative route needs
middle classes that coincide in another pattern and leave fewer than
about $N/\log N$ survivors at bounded cost. The negative route needs a
proof that no pattern does. Both are open. The positive-proportion
assertion in Erdős–Ruzsa Problem 2 would supply a stronger uniform
survivor estimate; it is not a premise here.

**Working conjecture.** $\mu(N)\asymp\log\log\log N$. The upper bound is
Proposition 1. The lower bound says that a configuration of cost $K$ leaves
a survivor once $N\ge\exp\exp\exp(CK)$ for a constant $C$, a quantitative
statement stronger than the negation of the erdosproblems.com assertion. It is
supported by the zero-residue barrier, the window lemma and the finite probes
above, and is not proved.

**Hypothesis H (a union bound for full prime classes).** Let
$0<\beta<1/10$ and $\kappa>0$. There are $c_H>0$ and $L_0$ such that for
$L\ge L_0$ the following holds: if $\mathcal R$ is a set of primes in
$(L^{1/2-\beta},L^{1-\beta}]$ with $\sum_{r\in\mathcal R}1/r\ge\kappa$,
and $U\subseteq\{0,\ldots,L-1\}$ contains, for each $r\in\mathcal R$,
every element of $\{0,\ldots,L-1\}$ in some residue class modulo $r$,
then $|U|\ge c_HL$. For primes below $L^{1/2-\beta}$ the large sieve
gives $|U|\ge(\kappa/(1+\kappa)-o(1))L$, as in Lemma C. For moduli
above $\sqrt L$, each pair of points belongs to at most one of their
classes: two distinct such primes cannot both divide a nonzero difference
smaller than $L$. Thus

$$
\binom{|U|}{2}\ge
\sum_{\substack{r\in\mathcal R\\r>\sqrt L}}
 \binom{\lfloor L/r\rfloor}{2}.
$$

For the full block $(\sqrt L,L^{9/10}]$, the sum has order
$L^{3/2}/\log L$, giving only $|U|\gg L^{3/4}/\sqrt{\log L}$.
For an arbitrary selected set, the right side depends on its prime scales;
this argument supplies no linear lower bound for H.

The known small-union constructions do not settle H. In
[[../library/primes/green_2017_arithmetic_kakeya_conjecture_katz_tao/proposition_4_1|Green–Ruzsa Proposition 4.1]],
the prime construction uses an interval of length $L=kp_{\max}$ and
primes in $[(1-\delta)X,X]$, with $0<\delta<1/2$. Even allowing $k$ and
$\delta$ to vary, their total reciprocal mass is at most
$\sum_{X/2<p\le X}1/p=O(1/\log X)=o(1)$. H instead asks for mass at
least $\kappa$ and class lengths at least $L^\beta+O(1)$. The same mass obstruction
applies to the primes in $(\alpha L,\beta' L)$ used in
[[../library/primes/ruzsa_1995_few_multiples_many_primes/theorem|Ruzsa's 1995 small-union construction]].
These parameter checks prevent importing those constructions as
counterexamples to H. They are not barriers to other uses of arithmetic
Kakeya ideas. The statements and these parameter choices were read; the
external Green–Tao input to Proposition 4.1 was not checked and is not a
premise here.

Hypothesis H with $\kappa=1/10$ and some $\beta\le1/30$ implies
$\mu(N)\ge1+c'$ for large $N$, with $c'>0$ depending on $c_H$. Put
$\tau=(1-\beta)/(3-\beta)<1/3$. If a cover has cost at most
$1+10^{-3}$, then by Theorem B its mass up to $N^{\tau}$ is below $0.09$;
the mass above $\sqrt N$ is at most $\log2+o(1)$, the mass in
$(N^{1/2-\beta},\sqrt N]$ is at most $3\beta$, and the total is at least
$1-o(1)$. So the primes in $(N^{\tau},N^{1/2-\beta}]$ carry mass at least
$0.1$. For each such $p$, the other selected primes in $(N^{\tau},\sqrt N]$
have mass at least $1/10$ and lie in $(L_p^{1/2-\beta},L_p^{1-\beta}]$,
and the set $J_p$ of Lemma C contains a full class modulo each of them.
Hypothesis H gives $|J_p|\ge c_HL_p$, so $E\ge c_HN/20-o(N)$ and the cost
is at least $1+c_H/20-o(1)$. Conversely, covers with cost tending to one
would make Hypothesis H fail for these parameters.

**A first-window test.** Decide whether classes for the full
window $(N^{1/3},N]$ can leave $o(N)$ survivors. The quantity to test is
net overlap saving, not the number of rich points alone. Write

$$
G=\sum_{n\le N}\left(\mathrm{sh}(n)-(m(n)-1)_+\right),
$$

and put

$$
B_1=\sum_p\left(|A_p|-\left\lfloor\frac Np\right\rfloor\right),\qquad
B_2=\sum_{\substack{p<q\\pq\le N}}
 \left(|A_p\cap A_q|-\left\lfloor\frac N{pq}\right\rfloor\right).
$$

The exact incidence identity gives

$$
Z=Z_0-B_1+B_2-G.
\tag{21}
$$

Both $B_1$ and $B_2$ are $O(N/\log N)$: each summand lies in $\{0,1\}$,
and the short-pair count was bounded in the proof of (20). Thus this test
asks whether $G\ge(\rho(3)-o(1))N$ is attainable. Its positive summands
contribute $\sum_n\mathrm{Def}(n)$, but points with excess larger than their
short-pair count subtract from it. A proposed construction must charge
those losses too.

The witness (17) realizes a positive saving for three primes, but (18)
shows why combining small groups cannot answer this test: a successful
configuration must have a small prime joined through realized short
triangles to at least
$(\sqrt{2\rho(3)}-o(1))N^{1/4}\sqrt{\log N}$ other primes. This is a
necessary condition on coherent global residues, not on separately chosen
unions in Lemma D. The uniform union bound (14) with $\lambda>0.766$
would instead decide the test negatively; that bound remains unproved.

A positive answer to the $o(N)$ test would overcome the zero-residue
barrier in this first window, but would not yet prove E1200. The positive
route must then produce covers at every sufficiently large $N$, with an
actual construction for the residual set. In particular, one-prime-per-point
cleanup from a reserved top block requires $O(N/\log N)$ residual points
with a proved bound below the number of unused primes, not merely $o(N)$.
A negative answer would leave the same question at smaller fixed exponents,
where higher-order coincidences enter. No finite passing sample decides
either asymptotic conclusion. Equation (21) separates endpoint gains from
the tested saving, so a finite experiment can report them without mistaking
$O(N/\log N)$ for a positive-density improvement.

### A sufficient construction with reserved cleanup primes

The exact identity (21) gives a full-solution target with cleanup included.
For each sufficiently large integer $N$, reserve the primes

$$
Q_N=\{q:N/2<q\le N\},\qquad T_N=|Q_N|,
$$

and choose one globally consistent residue class for every prime in

$$
P_N=\{p:N^{1/3}<p\le N/2\}.
$$

The residues may depend on $N$; no consistency between different
interval lengths is required. Define $B_1,B_2,G$ as in (21), using only
$P_N$. Since every prime in $P_N$ exceeds $N^{1/3}$, the zero classes
have no triple intersection in $[1,N]$, and the same count proves (21)
for this subwindow. Its zero-class survivor count is exactly

$$
Z_0(P_N)=\Psi(N,N^{1/3})+T_N.
$$

To see this, an integer with no prime divisor in $P_N$ is either
$N^{1/3}$-smooth or has a prime divisor $q>N/2$. In the latter case the
integer is $q$ itself. These alternatives are disjoint for large $N$.
Consequently (21) gives the equivalence

$$
Z\le T_N
\quad\Longleftrightarrow\quad
G\ge\Psi(N,N^{1/3})-B_1+B_2.
\tag{22}
$$

If residues satisfying (22) exist for every sufficiently large $N$, give
each survivor a different prime $q\in Q_N$ and choose its residue to
contain that survivor. These primes have not yet been used. The resulting
configuration covers $[1,N]$ and, by Mertens' estimate and the prime
number theorem, has cost at most

$$
\sum_{p\in P_N}\frac1p+\frac{2T_N}{N}
=\log3+o(1).
$$

Thus a uniform construction attaining (22) would prove the catalog
assertion with every fixed $C>\log3$. This deduction is author-recorded;
no residue construction attaining (22) is known here. The remaining
problem is to construct the global classes, with the large interactions
required by (18), and control their net saving including the endpoint
terms. Choices minimizing separate index unions in Lemma D need not
come from any such global classes.

An estimate $G\ge(\rho(3)-o(1))N$ only controls $Z$ to $o(N)$ and need
not attain (22), since $T_N\sim N/(2\log N)$. The terms $B_1,B_2$ and the
error below the linear scale must therefore remain in the closing
argument. A construction at selected values of $N$ also needs an explicit
interpolation argument before it proves the required every-large-$N$
statement. For this route the next full-solution test is a uniform
construction attaining (24) below for one fixed $u$, of which (22) is the
most constrained case, rather than another finite gain or an obstruction
to one restricted interaction pattern.

### One inequality for every fixed window

The identity (21) is the window $u=3$ of an exact identity for every
configuration. Call a set $F$ of selected primes *short* when
$\prod_{p\in F}p\le N$, and put $A_F=\bigcap_{p\in F}A_p$. For short $F$
this is one class modulo $\prod F$, so
$|A_F|=\lfloor N/\prod F\rfloor+\beta_F$ with $\beta_F\in\{0,1\}$, and
$\beta_\emptyset=0$. For $n\le N$ let $D_n=\{p\in P:n\in A_p\}$. When
$D_n\ne\emptyset$, let $p_1$ be its least member and put

$$
e(n)=\sum_{\substack{F\subseteq D_n\setminus\{p_1\}\\
 N/p_1<\prod F\le N}}(-1)^{|F|}.
$$

**Lemma E (exact gain identity).** For every configuration,

$$
Z=Z_0(P)+B-\sum_{\substack{n\le N\\ D_n\ne\emptyset}}e(n),\qquad
B=\sum_{F\ \text{short}}(-1)^{|F|}\beta_F,
\tag{23}
$$

where $Z_0(P)$ is the number of $n\le N$ divisible by no prime of $P$.

*Proof.* For each $n$, $\sum_{F\subseteq D_n}(-1)^{|F|}$ is $1$ when
$D_n=\emptyset$ and $0$ otherwise. Summing over $n\le N$ and splitting
the subsets into short and long ones gives

$$
Z=\sum_{F\ \text{short}}(-1)^{|F|}|A_F|
+\sum_{n\le N}\ \sum_{\substack{F\subseteq D_n\\ \prod F>N}}(-1)^{|F|}.
$$

Applied to the zero classes, for which no long $A_F$ meets $[1,N]$ and
every $\beta_F$ vanishes, the same expansion gives
$Z_0(P)=\sum_{F\ \text{short}}(-1)^{|F|}\lfloor N/\prod F\rfloor$. So the
first sum is $Z_0(P)+B$ for every choice of classes.
When $D_n\ne\emptyset$ the inner sum is
$-\sum_{F\subseteq D_n\ \text{short}}(-1)^{|F|}$. Pair each short
$F\not\ni p_1$ for which $F\cup\{p_1\}$ is short with $F\cup\{p_1\}$.
Every short set containing $p_1$ is paired, since removing $p_1$ keeps it
short, and paired sets cancel. The unpaired sets are the short
$F\not\ni p_1$ with $p_1\prod F>N$, whose signed count is $e(n)$. ∎

In the window $(N^{1/3},N]$ the nonempty short sets are the singletons and
the pairs of product at most $N$, so $B=-B_1+B_2$,
$e(n)=\mathrm{sh}(n)-(m(n)-1)$ when $D_n\ne\emptyset$, and (23) is (21).
In general a set $F$ in the sum for $e(n)$ gains one when $|F|$ is even
and costs one when it is odd. A class meeting $n$ with $p_1q>N$ is the
case $F=\{q\}$ and costs one; a realized short triangle is the case
$F=\{q,r\}$ with $qr\le N<p_1qr$ and gains one. The zero classes have
$e\equiv0$ and $B=0$.

**The general sufficient construction.** Fix $u\ge3$. For each large $N$
reserve $Q_N$ as in (22) and choose one class for every prime of

$$
P_N(u)=\{p:N^{1/u}<p\le N/2\}.
$$

An integer up to $N$ with no prime factor in $P_N(u)$ is
$N^{1/u}$-smooth or is a prime of $Q_N$, and for large $N$ not both, so
$Z_0(P_N(u))=\Psi(N,N^{1/u})+T_N$. Lemma E gives

$$
Z\le T_N\quad\Longleftrightarrow\quad
\sum_{D_n\ne\emptyset}e(n)\ \ge\ \Psi(N,N^{1/u})+B .
\tag{24}
$$

Distinct nonempty short sets have distinct products, each an integer up
to $N$ with no prime factor up to $N^{1/u}$. By (8) with
$w=N^{1/(10u)}$ there are $O(uN/\log N)$ such integers, so
$|B|=O(uN/\log N)$. This is the order of $T_N$, so $B$ stays in the
closing argument. If one fixed $u$ attains (24) at every large $N$, the
cleanup of (22) gives covers of $[1,N]$ of cost

$$
\sum_{p\in P_N(u)}\frac1p+\frac{2T_N}N=\log u+o(1),
$$

and the erdosproblems.com assertion follows with every fixed $C>\log u$. The case
$u=3$ is (22). This deduction is author-recorded; no construction
attaining (24) is known here for any $u$.

**Gain requirements in the first window.** In the window of (22) the short
pairs are forced:
$\sum_n\mathrm{sh}(n)=\sum_{p<q,\,pq\le N}|A_p\cap A_q|=(F_2+o(1))N$,
where $F_2=\log3-1+\rho(3)\approx0.14722$ by the zero-class count in the
proof of (12). An integer lying in at most three selected classes has
$e(n)\le1$, with equality only at a realized short triangle, which carries
three short pairs. So if no integer lies in four or more selected
classes, (24) with $u=3$ needs at least $(\rho(3)-o(1))N$ triangle points.
They carry the fraction $3\rho(3)/F_2\approx0.9905$ of all short pairs,
and all negative values of $e$ together may total at most
$(F_2/3-\rho(3)+o(1))N\approx0.0005N$. An integer in $k$ mutually short
classes gains $\binom{k-1}2$ from $\binom k2$ short pairs, so integers in
four or more classes are the only slack.

The gain can be sorted by the primes up to $\sqrt N$. Split $P_N$ into
$S=P_N\cap(N^{1/3},\sqrt N]$ and $L=P_N\cap(\sqrt N,N/2]$, let $U_S$ be the
union of the classes of $S$, and let $s(n)$ and $\ell(n)$ count the
classes of $S$ and of $L$ containing $n$. For $r\in L$ and $n\in A_r$, let
$d(n,r)$ count the classes of $S$ at $n$ whose primes $p$ have $pr\le N$.
At an integer with $s(n)\ge1$ the summand of $G$ is
$\binom{s(n)-1}2+\sum_{r}(d(n,r)-1)$, over the classes of $L$ at $n$,
since every pair of primes of $S$ is short and no pair of $L$ is. At an
integer with $s(n)=0$ it is $-(\ell(n)-1)_+$. Sum these terms, and use
(21) for the classes of $S$ alone in the form
$\sum_{n:s(n)\ge1}\binom{s(n)-1}2=X_S+B_{2,S}-B_{1,S}$, where
$B_{1,S},B_{2,S}$ are
the parts of $B_1,B_2$ from $S$. This gives exactly

$$
G-B_2+B_1=X_S+B_{1,L}
+\sum_{\substack{p\in S,\ r\in L\\ pr\le N}}\Bigl\lfloor\frac N{pr}\Bigr\rfloor
-\sum_{r\in L}|A_r\cap U_S|-\sum_{n\notin U_S}(\ell(n)-1)_+,
\tag{26}
$$

where $B_{1,L}=B_1-B_{1,S}$ and
$X_S=|U_S|-\sum_{p\in S}\lfloor N/p\rfloor+\sum_{p<q\in S}\lfloor N/pq\rfloor$
is the excess of $U_S$ over its zero-class value. Condition (22) is
$G-B_2+B_1\ge\Psi(N,N^{1/3})$. The two middle terms of (26) equal
$\sum_{r\in L}\sum_{n\in A_r\cap U_S}(d(n,r)-1)$ minus the part of $B_2$
from pairs $p\in S$, $r\in L$. If every such $d(n,r)$ is at most $2$, then
$d-1\le d/2$ termwise, and the middle terms are at most
$\tfrac12\sum_{p,r}\lfloor N/pr\rfloor=(F_{SL}/2+o(1))N$, where
$F_{SL}=F_2-\tfrac12\log^2\tfrac32\approx0.0650$ is the share of the
short pairs with one prime in each part. Then (22) needs
$X_S\ge(\rho(3)-F_{SL}/2-o(1))N\approx0.0161N$. Otherwise some classes of
$L$ meet integers lying in three or more classes of $S$. There are at
most $X_S+O(N/\log^2N)$ such integers, since each has
$\binom{s(n)-1}2\ge1$ and $B_{2,S}$ is at most the number of pairs of
primes up to $\sqrt N$.

The
[[research/leads/bounded_cost_prime_covers/evidence/_index|small-prime union probe]]
raises $X_S$ by coordinate ascent only to about $0.0063N$ at $N=10^6$ and
$0.0065N$ at $N=10^7$, and by annealing to $0.0065N$ at $N=10^6$, against
$0.0161N$. Unrestricted uniform residues give expected excesses $0.0041N$ and
$0.0053N$.
At those finite values of $X_S$, the asymptotic threshold alone decides
nothing. A possible source of further gain is incidences with $d(n,r)\ge3$:
each contributes $d(n,r)-1\ge2$ to the cross term in (26). Merely meeting
an integer in three classes of $S$ does not ensure this, since the three
products with $r$ must also be at most $N$. The construction would still
have to control its other intersections and the final excess term in (26).
These finite values bound nothing asymptotically.

In a larger window the required net gain is a far smaller proportion of
$N$: $\Psi(N,N^{1/u})\sim\rho(u)N$ with $\rho(4)\approx0.0049$ and
$\rho(5)\approx0.00035$, while every intersection forced in the first
window stays forced. This is the reason to pose the constructive test as
(24) for some fixed $u$ rather than at $u=3$. It does not make (24)
easier to attain locally. Changing one class from the zero class abandons
the multiples $jp$ with $j$ an $N^{1/u}$-smooth number, while a typical
new class has only about a proportion $\rho(u)$ of its points among the
uncovered integers. In the windows $(N^{1/4},N]$ and $(N^{1/5},N]$ at
$N=3\cdot10^4$ and $10^5$, the
[[research/leads/bounded_cost_prime_covers/evidence/_index|window probe]]
finds no single change of class, among classes of $\lfloor N/p\rfloor$
points, that lowers the zero-class survivor count, as at $u=3$. A
construction must therefore differ globally from the zero classes at
those tested orders under that cardinality restriction. The tests do not
establish local optimality when endpoint gains are allowed.

**Which changes could supply the missing gain.** Let $R$ be the primes
whose classes differ from zero in a configuration for $P_N(u)$. Any point
newly covered relative to the zero classes must lie in a new class of a
prime in $R$. Therefore, for every such configuration,

$$
Z_0(P_N(u))-Z
\le\sum_{p\in R}\left\lceil\frac Np\right\rceil
\le N\sum_{p\in R}\frac1p+|R|.
\tag{28}
$$

Since $Z_0=\Psi(N,N^{1/u})+T_N$, attaining $Z\le T_N$ requires
$\sum_{p\in R}1/p\ge\rho(u)-o(1)$ for each fixed $u$. Thus changing
only $o(N^{1/u})$ primes below $cN$, together with any primes above $cN$
for a fixed $c>0$, cannot attain (24): the first group's mass is $o(1)$,
the second's is $O(1/\log N)$, and $|R|\le\pi(N)=o(N)$. This rules out
that specific extension of endpoint improvements. It does not exclude
changes of positive reciprocal mass, or a different initial configuration.

The centered configuration is a different global starting point, but its
exact smooth-distance count above shows why it also stops before a
uniform cover. Improving the finite cleanup balance at fixed $u$ is not
enough: the missing construction must remove a positive multiple of $N$
survivors for all large $N$, and then control the remainder to the actual
$T_N$ scale. Neither the midpoint construction nor boundedly many changes
of middle classes supplies that step. On the negative route, restricting
a cover to a shorter interval does not remove its larger prime classes:
they may still cover individual points there, and the smaller interval
need not have enough unused primes to replace them. No all-scale
induction on the reciprocal budget follows from that restriction.

### Routes that fail, with their scope

- The fractional relaxation has a feasible point of cost one at every
  $N\ge5$ and supplies no rounding. It would reopen with a rounding scheme
  that controls the survivors of the small primes.
- The CRT translation gives no uniformity for translated intervals. It
  would reopen with a zero-residue survivor theorem uniform in the
  translate.
- Small primes of any number up to $N^{\theta}$ with top cleanup above
  $N^{1-\eta}$ fail by Theorem A, for every choice of classes.
- Zero residues in the middle are capped at triple-logarithmic cost, by
  the barrier, which relies on the published Erdős–Ruzsa theorem. Centering
  those residues inside the interval improves the upper bound to (27),
  but the common-center barrier still applies. For any fixed $u$ the
  exact survivor count is asymptotic to $\rho(u)N$, which exceeds the
  reserved cleanup supply. A uniformly stronger nonzero configuration
  remains unknown.
- Endpoint changes together with a set of changed middle primes of
  reciprocal mass $o(1)$ fail by (28). Their missing input is a family
  of changes with positive reciprocal mass and the net gain in (24).
  Such a family is unknown here; this restriction does not rule it out.
- Combining small groups of primes in the first window fails by (18).
  The missing input is a coherent family with large interaction degrees
  and positive net saving (21). Its existence is unknown; crossing the
  degree threshold alone does not establish it.
- Under $d(n,r)\le2$ at every large-prime incidence in (26), attaining
  (22) needs $X_S\ge(\rho(3)-F_{SL}/2-o(1))N$, about $0.0161N$.
  Under the different condition $m(n)\le3$ everywhere, triangle points
  need about $99\%$ of all forced short pairs. The probed excess is
  about $0.0065N$ and supplies no upper bound. The required construction
  is unknown, not refuted. It would reopen with a family of classes up to
  $\sqrt N$ whose union exceeds the zero-class value by a fixed proportion
  well above that of random classes, or with many integers in four or
  more selected classes; a larger fixed window (24) relaxes the count.
- Random or greedy middle classes: the averaging argument only brings
  the survivors down to $N\prod_p(1-1/p)$, which the top capacity of
  about $N/\log N$ absorbs only at cost about $\log\log N$.
- Finite tables decide nothing about eventual behavior. At finite $N$, the
  explicit endpoint error $|P|$ in (12) must be compared with the actual
  smooth-number count; the asymptotic notation alone does not make it small.
