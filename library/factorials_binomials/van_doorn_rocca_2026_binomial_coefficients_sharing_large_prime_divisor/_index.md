---
name: factorials_binomials/van_doorn_rocca_2026_binomial_coefficients_sharing_large_prime_divisor
title: "Binomial coefficients sharing a large prime divisor"
desc: |
  Proves that only finitely many triples with i at least 4 fail to have a
  common prime divisor strictly larger than i, while leaving i = 3 open.
license: unstated
created: 2026-09-21T17:40:00Z
updated: 2026-10-08T01:50:54Z
---

# Binomial coefficients sharing a large prime divisor

[[factorials_binomials/_index|..]]

[[factorials_binomials/van_doorn_rocca_2026_binomial_coefficients_sharing_large_prime_divisor/evidence/_index|evidence/]]: Replays the finite and analytic inequalities that strengthen the manuscript's
explicit large-index cutoff from i at least 1000 to i at least 906.

***

Wouter van Doorn and Stefano Rocca, “Binomial coefficients sharing a large prime
divisor,” unpublished working manuscript, 2026. Public
[Overleaf project](https://www.overleaf.com/read/ywsndhgyrzsx), captured
2026-09-21. The manuscript's text carries no license notice, and no arXiv
record for it was found (title and author queries read 2026-10-07); the term is
unstated.

For integers $i<j\le n/2$, put $G=\gcd\!\left(\binom ni,\binom nj\right)$. The
manuscript proves the following strict form of the desired conclusion outside a
finite set.

## Quantitative gcd bound

Lemma 1 gives

$$
G>e^{-2i}\left(\frac ni\right)^{i/4}
\qquad(4\le i<j\le n/2).
$$

Its proof evaluates a Toeplitz determinant of shifted binomial coefficients by
the Desnanot--Jacobi identity, then uses

$$
\binom nj\binom{j}{i-h}\binom{n-j}{h}
 =\binom ni\binom ih\binom{n-i}{j-i+h}
$$

to force a large power of $\binom nj/G$ into the determinant. Theorem 1 then
shows that the largest prime factor of $G$ is at least $\min(q,ci\log i)$ for an
absolute $c>0$, where $q$ is the largest prime at most $n$. In particular it
exceeds $i$ for all sufficiently large $i$. The proof combines Lemma 1 with
Baker--Harman--Pintz in the range $i\ge n^{21/40}$ and with a small-prime upper
bound for $G$ in the complementary range.

Corollary 1 gives only finitely many strict-threshold exceptions with $i\ge121$,
using $G\le n^{\pi(i)}$ when $G$ is $i$-smooth and $\pi(i)<i/4$.

## Fixed-index finiteness

Theorem 2 lowers the fixed-index range to every $i\ge4$. For fixed $i\ge5$, the
Bugeaud--Evertse--Győry $S$-part theorem bounds the part of
$n(n-1)\cdots(n-i+1)$ supported on primes at most $i$, contradicting Lemma 1 for
large $n$ when $G$ has no prime factor above $i$. The case $i=4$ uses the
explicit integer $H$ displayed in the proof: if no prime $q\ge5$ divides $G$
and $p^a$ divides the rough part of $\binom n4$, then $p^{6a}\mid H$, and
$H<n^{17}$ gives the needed exponent gap.

The fixed-index theorem is ineffective. The sentence after Corollary 1 that
there are no counterexamples for $i\ge1000$ is not accompanied by its numerical
calculation in the manuscript. The calculation below both supplies that gap and
strengthens the cutoff to $i\ge906$. The manuscript gives no conclusion for
$i=3$ and does not enumerate the remaining finite exceptional set.

## Explicit cutoff $i\ge906$

The assertion follows by retaining the factorial product discarded in the last
simplification of Lemma 1. Put

$$
k=\left\lceil\frac i2\right\rceil,
\quad
A_i=i-k+\frac{k(k-1)}2,
\quad
B_i=i-k+ki-\frac{k(k-1)}2,
\quad
H_k=\prod_{r=1}^k r!.
$$

The penultimate estimate and divisibility argument in Lemma 1 give

$$
G>
\frac{n^{\alpha_i}}
 {\operatorname{lcm}(1,\ldots,i)\,2^{\beta_i}H_k^{1/(k+1)}},
\qquad
\alpha_i=\frac{A_i}{k+1},
\quad
\beta_i=\frac{B_i}{k+1}.
\tag{1}
$$

If $G$ has no prime divisor exceeding $i$, then $G\le n^{\pi(i)}$. Together with
$\operatorname{lcm}(1,\ldots,i)<e^{1.04i}$, (1) yields

$$
n<N_i:=
\exp\!\left(
 \frac{1.04i+\beta_i\log2+(k+1)^{-1}\log H_k}
      {\alpha_i-\pi(i)}
\right).
\tag{2}
$$

For $906\le i<1476$, direct evaluation puts $N_i$ below the first lower endpoint
of a prime gap longer than $i$, using Table 8 of Oliveira e
Silva--Herzog--Pardi. The smallest logarithmic margin is $0.2643551524\ldots$ at
$i=912$. In particular, $N_{906}<5.64\cdot10^{14}$, while the first gap longer
than $906$ begins at $1{,}189{,}459{,}969{,}825{,}483$. This is the first
uniform cutoff obtained by this confinement comparison: at $i=905$, it gives
$N_{905}>5.50\cdot10^{14}$, while the first gap longer than $905$ begins at
$218{,}209{,}405{,}436{,}543$. Thus a further improvement would need an
additional argument for $i=905$, not just the same record-gap comparison.

For $1476\le i<10^6$, (2) gives $N_i<4\cdot10^{18}$; the smallest logarithmic
margin is $11.4813820357\ldots$ at $i=1500$. All prime gaps below
$4\cdot10^{18}$ are at most $1476$.

For $i\ge10^6$, use $k\le(i+1)/2$, $\alpha_i\ge i/4$, $\beta_i\le3(i+1)/4$,

$$
\frac{\log H_k}{k+1}\le\frac{k}{2}\log k,
\qquad
\pi(i)<\frac{1.25506i}{\log i}.
$$

Writing $L=\log i$, the resulting elementary estimate is

$$
\log N_i-\log i
 < \frac{(4C+4\cdot1.25506)L+L^2/i}{L-4\cdot1.25506}
 <16.597823
 <\log(28{,}314{,}000),
$$

where $C<1.386575$; the fraction decreases in $i$, so its value at $i=10^6$
bounds it. The term $L^2/i$ comes from the factor $(i+1)/4$ in front of
$\log i$; the evidence program's tail check leaves it out, and it adds less
than $3\cdot10^{-5}$ to that check's bound $16.597796$, against a margin above
$0.56$. Hence $N_i<28{,}314{,}000i$. Ramaré--Saouter Theorem 3
places a prime in $(n(1-1/28{,}314{,}000),n]$ for $n>10{,}726{,}905{,}041$;
below that point their computation gives maximum gap $381$. Thus in every range
there is a prime $n-i<p\le n$, and such a prime divides both $\binom ni$ and
$\binom nj$ for $i<j\le n/2$.

The calculation is reproducible from `evidence/main.py`; its default full run
checks all $906\le i<10^6$ and the analytic tail.

## Relation to Problem 699

The variables and gcd are exactly those of
[[../wiki/problems/factorials_binomials/E0699/_index|Problem 699]], but the paper generally
asks for the stronger inequality $p>i$. Thus Theorem 2 implies that all but
finitely many eligible triples with $i\ge4$ satisfy Problem 699, and Theorem 1
closes an unspecified uniform large-$i$ range. A failure of the strict version
when $i$ is prime need not fail Problem 699, since the problem permits $p=i$.

Lemma 1 is the main reusable estimate: any possible counterexample must make its
very large gcd entirely $(i-1)$-smooth. The determinant construction is uniform
in $j$, while the special $i=4$ divisor is a model for turning the absence of a
common rough prime into simultaneous congruence conditions on $j$, $n-j$, and
$n$.

Read status (author-recorded): claims checked for the core finiteness theorem
and its cited analytic inputs; the bounded exact computations behind that
reading are not retained, so its proofs count as not verified. The omitted
$i\ge1000$ calculation is retained as the
[[factorials_binomials/van_doorn_rocca_2026_binomial_coefficients_sharing_large_prime_divisor/evidence/_index|evidence
leg]] beside this card, strengthened to $i\ge906$. This paper still does not
settle Problem 699 because $i=3$ remains and the possible finite exceptional set
for $4\le i\le905$ is not eliminated.

No file of this source is held: no license on record permits its redistribution,
and the card cites the edition it names above.
