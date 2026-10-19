---
name: research/leads/odd_covering_distortion/e273_calibration
title: Calibration on the moduli p-1 with p at most 877
desc: |
  The digit-coordinate distortion sieve proves, with an exact certificate,
  that the 149 moduli p-1 with 5 <= p <= 877 cover the integers for no
  choice of residues: the 7-smooth block loses at most 115/126 and every
  later digit loses nothing.
created: 2026-10-16T13:49:49Z
updated: 2026-10-16T13:49:49Z
---

# Calibration on the moduli p-1 with p at most 877

***

This page is author-recorded work by Plasma AI at tier 0, with no independent
review. It calibrates the [[research/leads/odd_covering_distortion/digit_sieve|digit
form of the distortion sieve]] on a finite domain of
[[problems/covering_systems/E0273/_index|Problem 273]], which asks for a
covering system whose moduli are distinct numbers $p-1$ with $p\ge5$ prime.
The domain was fixed as a calibration benchmark for the
[[research/leads/odd_covering_distortion/_index|odd-covering route]]: it
exercises prime powers up to $2^8$, $3^5$ and $5^3$, and its moduli are all
even, so it is not an instance of Problem 7.

## Statement

Let $D=\{p-1:p\text{ prime},\ 5\le p\le877\}$, a set of $149$ moduli. For
every choice of residues $a_d$ ($d\in D$) the classes $a_d\pmod d$ do not cover
$\mathbb Z$. Equivalently, every covering system whose moduli are pairwise
distinct numbers $p-1$ with $p\ge5$ prime uses a modulus $p-1$ with $p>877$.

The equivalence holds because a covering system using only some moduli of $D$
stays a cover when one class is added for each missing modulus. The statement
is finite and does not decide unrestricted Problem 273. It coincides with
Theorem 1.1 of the note on the
[[problems/covering_systems/E0273/claims/2026_07_11_ideal_ombrer|pending ideal_ombrer
claim page]]; that note, its certificates and its proof were not used or
consulted here. This page gives a separate author-recorded derivation, not
an independent review of that note.

## Proof

Let $N=\operatorname{lcm}(D)$. Its largest prime powers are $2^8$, $3^5$,
$5^3$, $7^2$, $11^2$ and $13^2$, and every other prime divides $N$ exactly
once. By the digit reduction (Lemma 1 of the digit page) the classes become
$149$ nonparallel hyperplanes with prefix fixed sets in the digit box $Q(N)$,
which has $63$ coordinates. Expose them in the order

$$
\begin{gathered}
(2,1),(2,2),(3,1),(2,3),(5,1),(2,4),(3,2),(3,3),(3,4),\\
(3,5),(2,5),(2,6),(2,7),(2,8),(5,2),(5,3),(7,1),(7,2),
\end{gathered}
$$

then $(11,1),(11,2),(13,1),(13,2)$, then $(q,1)$ for the primes $q\ge17$
dividing $N$ in increasing order. Start from the trivial measure and use the
distortion $\delta_k=t_k/q_k$ with the thresholds $t_k$ below.

The first $18$ coordinates complete exactly the $49$ moduli of $D$ whose prime
factors are at most $7$. Their reciprocal sum is about $1.0436$, so the union
bound alone does not leave an uncovered point. Lemma 2 of the digit page
bounds each step's loss, with the source's Lemma 3.3 recursion (the first
display of Lemma 3) for the class masses:

| digit | completed moduli | $t$ | certified loss |
| --- | --- | ---: | ---: |
| $(2,2)$ | 4 | 0 | $1/4$ |
| $(3,1)$ | 6, 12 | 0 | $1/4$ |
| $(5,1)$ | 10, 30, 40, 60 | 3 | $1/48$ |
| $(2,4)$ | 16, 240 | 1 | $1/48$ |
| $(3,2)$ | 18, 36, 72, 180 | 0 | $1/9$ |
| $(3,3)$ | 108, 270, 432, 540 | 0 | $1/36$ |
| $(3,4)$ | 162, 810 | 2 | $0$ |
| $(3,5)$ | 486 | 1 | $0$ |
| $(2,5)$ | 96 | 0 | $1/48$ |
| $(2,6)$ | 192, 576 | 0 | $1/72$ |
| $(2,7)$ | 640 | 1 | $0$ |
| $(2,8)$ | 256, 768 | 1 | $1/96$ |
| $(5,2)$ | 100, 150, 400, 600 | 4 | $0$ |
| $(5,3)$ | 250, 750 | 2 | $0$ |
| $(7,1)$ | 28, 42, 70, 112, 126, 210, 280, 336, 378, 420, 448, 630, 672, 700, 756 | 0 | $377/2016$ |
| $(7,2)$ | 196, 490 | 2 | $0$ |

The digits $(2,1)$ and $(2,3)$ complete no modulus and take $t=0$. The total
is $115/126<1$. The four moduli completed at $(5,1)$ form a single $4$-set,
whose projections meet in at most one class modulo $24$; this step's bound
$1/48$ replaces a first moment near $0.175$. Several steps complete fewer
moduli than their size and lose nothing, at the price of larger class-mass
bounds for the later steps; the table's losses include that price.

Each of the remaining $45$ coordinates completes fewer moduli than its size;
the largest ratio is the digit $(11,1)$, which completes the ten moduli $22$,
$66$, $88$, $198$, $330$, $352$, $396$, $462$, $616$, $660$. Taking
$t_k=|\mathcal N_k|$ there, Lemma 2 gives zero loss. The total loss is
therefore $115/126$, so $\mathbb P_n(R)\ge11/126>0$ and some point of $Q(N)$,
hence some integer, is uncovered. Every bound used is uniform in the residues,
so this holds for every residue choice. $\square$

## What the calibration shows

The route's two new ingredients both carry weight here: the digit order makes
most high prime powers complete in steps with spare room, and the set bound of
Lemma 2 handles the steps where moduli collide. The source's own class-mass
recursion suffices. The compatibility-weighted recursion of Lemma 3, with a
schedule differing only at the digit $(2,3)$, certifies the smaller total
$538793/604800$; it is a second check of the same statement, not needed for
it.

The calibration does not test the arbitrary-exponent and large-prime
difficulties of Problem 7. Here every digit at a prime above $7$ completes
fewer moduli than its size, so no large-prime tail estimate is needed. No
such count bound holds uniformly over all finite families of distinct odd
moduli.

## Evidence

The lead's [evidence program](evidence/main.py) rebuilds $D$, checks the
exponent pattern, reads the order and thresholds from the
[schedule asset](evidence/assets/e273_schedule.json), recomputes both totals
exactly, and checks that each later digit completes fewer moduli than its
size. A control with every $t_k=0$ returns the union bound, which exceeds one.
Run from the repository root:

```sh
uv run --no-sync python wiki/research/leads/odd_covering_distortion/evidence/main.py
```

It uses exact rational arithmetic and runs in about a second. The order and
thresholds were found by a local search over digit orders and thresholds;
the search is not part of the evidence, which checks the retained schedule
directly.
