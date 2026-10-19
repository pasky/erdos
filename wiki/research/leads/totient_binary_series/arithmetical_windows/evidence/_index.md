---
name: research/leads/totient_binary_series/arithmetical_windows/evidence
title: Exact Witnesses for Totient-Term Isolation
desc: |
  Fixed prime, semiprime, and prime-square isolation witnesses, the carry
  at 64, and the CRT data of its infinite counterfamily.
tags: []
sources: []
created: 2026-09-17T06:20:20Z
updated: 2026-09-17T06:20:20Z
---

# Exact Witnesses for Totient-Term Isolation

[[research/leads/totient_binary_series/arithmetical_windows/_index|..]]

***

The [entry point](main.py) checks fixed finite witnesses used in
[[research/leads/totient_binary_series/arithmetical_windows/_index|the owning
argument]]. Run from the repository root:

```sh
nice -n 10 uv run --no-sync python wiki/research/leads/totient_binary_series/arithmetical_windows/evidence/main.py
```

The default is the entire check; there is no reduced mode. The inputs are
the explicit integer constants in the script. It uses Python exact
integers, trial-division primality and totients for the selected numbers,
an independent totient sieve to 89013, and the recurrence for $\Phi_N$
modulo $2^{11}$. Every asserted valuation is determined exactly by the
nonzero residue at that precision. There is no record search, random
choice, file input, output file, or dependence on storage outside the repository.
Dependencies are the standard library and the repository's `tools`
package. Runtime is expected to be under a second. Failure of any named
obligation returns a nonzero exit code, including under `python -O`.
The full run passed all 20 obligations. A scratch mutation changing the
expected residue of $\Phi_{64}$ from 1024 to 1025 failed the named seed
obligation and returned exit code 1 under `python -O`.

The first two witnesses instantiate the two cases of Lemma 1:

| $N$ | Original class | Active factorization | $\varphi(N),\varphi(N-1),\varphi(N-2)$ | $v_2(\Phi_N)$ |
| --- | --- | --- | --- | --- |
| 15131 | $1\pmod5$ | prime $15131\equiv3\pmod4$ | $15130,5632,9840$ | 1 |
| 89013 | $5\pmod8$ | $3\cdot29671$, both primes $3\pmod4$ | $59340,32640,79680$ | 2 |

In both cases $17\mid N-1$ and $41\mid N-2$, so the two unwanted
totients are divisible by eight. The active totient has lower valuation,
which therefore determines the full numerator modulo eight.
Trial division certifies all the displayed prime assertions. These
witnesses were found in a bounded exploratory CRT calculation and then
fixed for replay; they are not a statistical sample.

The seed check gives $\Phi_{64}\equiv1024\pmod{2048}$, hence valuation
ten. The three values $N=125,3125,78125$ check the stated powers-of-five
family, whose infinite assertion comes from the prose proof, not the
sample. The checker also validates

$$
L=13632589333440,\qquad L/64=213009208335,
$$

and the nine fresh primes
$257,641,769,1153,1409,2689,3329,3457,4481$. The prime parameter $p$ in
the owning construction lies in the reduced class

$$
p\equiv10902871344717736470074227285488089485531
\pmod{24316165102496165371645476418278117995580}.
$$

The checker verifies its coprimality and every CRT condition. It does
not test this large representative for primality or exhibit the first
prime in the class. The infinitely many prime parameters and the
universal obstruction use Dirichlet's theorem and the recorded proof.

The prime-square instance has $p=647\equiv-1\pmod{36}$ and
$N=p^2=418609\equiv1\pmod9$. The fresh primes $17,41\equiv1\pmod8$
satisfy $p\equiv1\pmod{17}$ and $p\equiv32\pmod{41}$, so
$17\mid N-1$ and $41\mid N+1$. Exact prime factorizations give

$$
(\varphi(N),\varphi(N-1),\varphi(N+1))=(417962,124416,163200),
$$

and
$-\varphi(N)+\varphi(N-1)+\varphi(N+1)=-130346\equiv2\pmod4$.
This tests shifts on both sides of the selected position and a negative
sum. It is a fixed witness for Theorem 4, not a check of $\Phi_N$ at this
larger index. A second optimized scratch mutation changing this expected
sum to $-130345$ fails its named obligation with exit code 1.
Quadratic reciprocity guarantees the roots for the general construction;
the two roots in this particular instance are checked directly.

None of these finite checks establishes irrationality, an unbounded
valuation excess, or independent verification standing.
