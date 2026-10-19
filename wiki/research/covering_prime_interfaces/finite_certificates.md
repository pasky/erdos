---
name: research/covering_prime_interfaces/finite_certificates
title: Finite certificates and their scope
desc: Exact finite certificates for two-generator composites, distinct prime divisors and covers, and the limits of finite-cover methods.
tags: [covering systems, CRT]
sources: []
created: 2026-10-14T22:17:53Z
updated: 2026-10-17T22:11:11Z
---

# Finite certificates and their scope

***

These are author-recorded reductions, not constructed solutions. The arguments
below need no numerical search or executable evidence.

## A sufficient certificate for Problem 203

[[problems/covering_systems/E0203/_index|Problem 203]] asks for an integer
$m$ coprime to $6$ such that $m2^k3^\ell+1$ is composite for all nonnegative
$k,\ell$. Choose a finite set $Q$ of distinct primes greater than $3$ and
nonzero residues $c_q\pmod q$. Put

$$
T_2=\operatorname{lcm}_{q\in Q}\operatorname{ord}_q(2),\qquad
T_3=\operatorname{lcm}_{q\in Q}\operatorname{ord}_q(3).
$$

The exact finite test is

$$
\text{for every }(u,v)\in\mathbb Z/T_2\mathbb Z\times\mathbb Z/T_3\mathbb Z,
\quad c_q2^u3^v\equiv-1\pmod q\text{ for some }q\in Q.\tag{1}
$$

If (1) holds, the Chinese remainder theorem gives an arithmetic progression
of $m$ satisfying $m\equiv c_q\pmod q$ for all $q\in Q$ and
$m\equiv1\pmod6$. Choose a positive member larger than every $q\in Q$.
Reduction of $(k,\ell)$ modulo $(T_2,T_3)$ supplies a divisor $q$ of
$m2^k3^\ell+1$. Since $m2^k3^\ell+1>m>q$, this is a proper divisor,
including when $k=\ell=0$. This proves the required compositeness and
coprimality, conditional only on the finite certificate (1).

Conversely, any certificate using this fixed set $Q$ to divide every term
has exactly this periodic form, with $c_q=m\bmod q$ after removing primes
dividing $m$, which cannot divide any term. Thus the reduction is exact for
finite prime covers of the stated form. It does not show that every solution
must admit one.

No $Q$ or residues satisfying (1) are supplied here. The hard step is covering
the entire product of exponent cycles with one compatible value of $m$ modulo
each prime. A bounded test must specify $Q$ and both periods, then either
retain all covering residues or identify an uncovered pair. Repeated failure
for bounded prime sets is no nonexistence theorem; stop that finite test at
its declared set of primes, without extrapolation to all $Q$.

## Finite covers and non-finite covers ask opposite questions

For [[problems/covering_systems/E0007/_index|Problem 7]], a candidate is a
finite family of classes with distinct odd moduli greater than $1$ covering
every residue modulo their least common multiple. Squarefree restrictions or
restrictions on the number of prime factors leave unrestricted odd moduli
outside their scope. For
[[problems/covering_systems/E0273/_index|Problem 273]], the moduli must
specifically be distinct numbers $p-1$ with $p\ge5$ prime. A finite-period checker
must preserve that extra condition. Neither question is resolved by a long
covered prefix shorter than the period.

A finite set of allowed moduli can instead be excluded by a sieve
certificate covering every residue choice at once. The
[[research/leads/odd_covering_distortion/e273_calibration|digit-sieve
calibration]], whose exact computation is checked by its own evidence
program, does this for the $149$ moduli $p-1$ with $5\le p\le877$: a
distortion sieve along base-$p$ digits bounds the loss of the $49$ moduli
with prime factors at most $7$ by $115/126$, and every later digit completes
fewer moduli than it has values, so it loses nothing. That count bound is
specific to this domain; it does not hold uniformly over all finite families
of distinct odd moduli. The limits of the same sieve at the small primes are
recorded on the
[[research/leads/odd_covering_distortion/cube_free_obstruction|cube-free
obstruction page]].

In contrast, the no-finite-prime-cover requirement in
[[problems/covering_systems/E0276/_index|Problem 276]] demands escape from
every fixed finite set of primes. For a fixed positive integer sequence
$a_n>1$, no finite prime set divides at least one factor of every term if and
only if its least prime factors are unbounded. Indeed, primes at most $B$
cover every term exactly when every least prime factor is at most $B$.
The all-composite requirement is additional. Finding another finite cover
therefore cannot establish the requested escape. The construction on
[[problems/covering_systems/E1113/_index|Problem 1113]] likewise needs its
own no-finite-cover argument if that extra property is claimed; algebraic
compositeness alone does not provide it.

The restricted assertion that every non-perfect-power Sierpinski parameter
has a finite covering set is Conjecture 3 in the
[[../library/covering_systems/filaseta_2008_powers_associated_sierpinski_numbers_riesel/theorem_10|held Filaseta--Finch--Kozek account]].
Proving it would leave perfect-power parameters unresolved. A counterexample
to that assertion would instead answer Problem 1113 positively. The source
starts exponents at one; any such parameter $m$ exceeds one, so the extra
term at exponent zero is the composite even number $m+1$. Adding one term
does not change whether the least prime factors are unbounded. This is a
logical implication between the stated questions, not a counterexample or
an audit of an external formal variant.

For an exact partition of a finite group into cosets in
[[problems/covering_systems/E0274/_index|Problem 274]], subgroup indices
must remain distinct in the claimed conclusion. Passing through a normal
subgroup $N$ gives
$[G:H]=[G:HN][N:H\cap N]$. Distinct products need not have distinct first
or second factors. Results for simple and solvable groups do not compose
through this identity without an extra argument controlling repeated indices.
The discriminating test for an extension argument is precisely that index
control; stop before asserting closure under extensions if it is absent.

## Hall certificates and cover decompositions

Fix a block $n+1,\ldots,n+k$ and write $P_i$ for the set of prime divisors
of $n+i$. The distinct-prime selection in
[[problems/integer_sequences/E0375/_index|Problem 375]] is exactly a
system of distinct representatives for these finite sets. Hall's theorem
therefore gives a finite obstruction: a subset $I\subseteq\{1,\ldots,k\}$
with $|\bigcup_{i\in I}P_i|<|I|$, accompanied by complete factorizations
of the affected integers, with every member of the whole block proved composite.
Checking a fixed block answers only that block.
Having a prime factor greater than $k$ in every integer is sufficient for
distinctness, since such a prime cannot divide two numbers of the block, but
is not necessary. The existence question in
[[problems/integer_sequences/E0962/_index|Problem 962]] has a different
quantifier over blocks.

For [[problems/integer_sequences/E0467/_index|Problem 467]], fix $x$ and a
choice of one residue class for every prime $p\le x$. Make these primes the
vertices and, for each integer $1\le n<x$, make an edge consisting of the
primes whose chosen class contains $n$. This choice splits into two covers
of $[1,x)$ exactly when the vertices have a two-coloring giving both colors
to every edge. The required classes and coloring may be chosen afresh for
each sufficiently large $x$; the task is not to decompose every given double
cover. Nor is coverage of a whole common period required.

Double coverage says only that every edge has size at least two. That property
alone does not imply the required coloring: the three two-element edges on
three vertices are a counterexample for abstract hypergraphs. This is a
logical obstruction to an argument using double coverage alone, not an
arithmetic counterexample to Problem 467. A successful proof must construct
the classes together with a coloring for every sufficiently large $x$.
A bounded test checks every integer of $[1,x)$ for its declared $x$ and
residue choices. Failure of one choice, or an abstract non-colorable
hypergraph, does not refute that existential construction problem.
