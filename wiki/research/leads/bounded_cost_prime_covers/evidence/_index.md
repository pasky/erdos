---
name: research/leads/bounded_cost_prime_covers/evidence
title: Evidence
desc: Exact sample covers, a three-prime witness that coordinated coincidences improve the union without changing class sizes, and seeded exploratory probes of the prime window, the full-class union problem and the union excess of the primes up to sqrt N.
tags: []
sources: []
created: 2026-10-16T19:43:38Z
updated: 2026-10-16T19:43:38Z
---

# Evidence

[[research/leads/bounded_cost_prime_covers/_index|..]]

***

The [entry point](main.py) builds the cover of Proposition 1 on the
[research page](../_index.md) at $N=10^4$, $10^5$ and $10^6$ from its
recipe: the class $1\bmod2$, residue $0$ for the primes in
$(N^{1/u},N/2]$ with $u=4\log\log N$, and one prime of $(N/2,N]$ for each
remaining integer. It checks that the cleanup primes exist, that the
integers left before cleanup are exactly the even $N^{1/u}$-smooth
integers, recomputed from largest prime factors, and that every integer in
$[1,N]$ lies in a selected class. It then repeats the check with the
largest tested prime cutoff at most $\sqrt N$ for which the cleanup primes
still suffice, and checks by integer arithmetic that each resulting cost
is less than $33/20$. These are
finite checks of a recipe whose validity for all large $N$ is proved on the
research page; they prove nothing asymptotic.

Two further clauses are seeded finite probes. In the window $(N^{1/3},N]$,
with every class forced to have exactly $\lfloor N/p\rfloor$ points, the
probe checks that the zero classes leave exactly the $N^{1/3}$-smooth
integers and that no change of one prime's class lowers that number, at
$N=3\cdot10^4$ and $10^5$; the same two checks run in the windows
$(N^{1/4},N]$ and $(N^{1/5},N]$, with $N^{1/4}$- and $N^{1/5}$-smooth
integers. It then runs a local search from a seeded random
choice of classes and checks that it ends above the zero count. At
$N=3\cdot10^4$ it also runs seeded Metropolis annealing by single-class
moves: from the zero classes it never reaches fewer survivors than the zero
classes, and from random classes it ends above them. The union probe chooses
one full residue class modulo each prime in $(L^{1/2},L^{9/10}]$ inside
$[0,L)$ for $L=3000$, $10^4$, $3\cdot10^4$, $10^5$ and $3\cdot10^5$, and
reports the union sizes of the zero, random, greedy and locally improved
choices after checking the maintained counts against a recount. The research
page records the observed values and their limited bearing.

A separate exact witness at $N=105$ uses $0\bmod5$, $6\bmod7$ and
$0\bmod11$. The checker verifies that the class sizes and all pair
intersection sizes equal those for zero residues, while a triple
intersection at $55$ increases the union from $40$ to $41$. The cost is
exactly $167/385$. This is a finite improvement for a selected three-prime
set; it is neither a cover nor an improvement for the full prime window.

A sixth clause probes the excess $X_S$ of display (26) of the research
page: the union of one class modulo each prime in $(N^{1/3},\sqrt N]$,
every class with exactly $\lfloor N/p\rfloor$ points, against its zero-class
value, at $N=10^6$ and $10^7$. It checks that the zero-class union equals
$\sum_p\lfloor N/p\rfloor-\sum_{p<q}\lfloor N/pq\rfloor$ exactly, since
every pair of these primes has product at most $N$ and every triple more.
From a seeded random start, coordinate ascent gives each prime in turn
the class covering the most integers missed by the others; the probe
checks the maintained counts against a recount and that
the union never decreases, and reports the final excess and the number of
integers in four or more classes. The comparison mean
$N(1-\prod_{p\in S}(1-1/p))$ is for unrestricted uniform residues;
the seeded searches use only classes of $\lfloor N/p\rfloor$ points. At
$N=10^6$ a seeded annealing run by single-class moves is a second search,
with its maintained union checked against a recount. The research page
records the values and their limited bearing.

A seventh clause checks the centered construction (27). It chooses
$b=\lfloor N/2\rfloor+1$ and uses $b\pmod p$ for the primes in
$(z,N/2]$, with $z=N^{1/(4\log\log N)}$. It independently factors the
distances $|n-b|$ to check that the survivors are exactly the integers
with positive $z$-smooth distance from $b$. The center is already covered.
The checker assigns distinct unused primes from $(N/2,N]$ to these
survivors, then checks coverage from the complete list of residues.
It also repeats the construction with the largest tested prime cutoff
up to $\sqrt N$ fitting the cleanup supply, and checks the resulting
cost is below $131/100$ by integer arithmetic. These are exact finite
covers at $N=10^4$, $10^5$ and $10^6$, not a constant bound for all $N$.

Run from the repository root:

```sh
uv run --no-sync python wiki/research/leads/bounded_cost_prime_covers/evidence/main.py
```

The full run takes about two minutes; `--quick` drops $N=10^6$, the
second window order of each window and the three largest union sizes,
shortens the annealing, and runs the sixth clause at $N=10^5$ only. The run is
deterministic, reads no inputs and writes no files. Every failed check
exits nonzero.
