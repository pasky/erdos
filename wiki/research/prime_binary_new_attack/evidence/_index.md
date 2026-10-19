---
name: research/prime_binary_new_attack/evidence
title: Evidence
desc: |
  Finite observations of the parity-prediction rule on the primes below
  2 * 10^7: the rule's two forms agree on every start, mispredicted fractions
  stay near one half, and later residues add almost nothing to predicting
  the parity of a gap; and a separately graded mathematical review of the
  conditional matching-window argument.
created: 2026-10-15T18:55:46Z
updated: 2026-10-16T16:08:36Z
---

# Evidence

[[research/prime_binary_new_attack/_index|..]]

[[research/prime_binary_new_attack/evidence/verify/_index|verify/]]: Independent reports and separate grades for precisely delimited arguments concerning the prime binary series.

***

The [entry point](main.py) computes, for the primes $p_n$ with
$X<p_n\le2X$ and $X\in\{10^6,10^7\}$, the exact phases of the
[[research/prime_binary_new_attack/proof_sketch|parity-prediction sketch]] for
$d\in\{1,3,5,7,9,11,15\}$ and $K=\lceil\log_2(d\log X)\rceil+C$ with
$0\le C\le6$. It uses numpy, the root Python environment and the shared
`Checker`, reads no files and writes no output, and finishes in a few seconds.
Run it from the repository root:

```sh
uv run --no-sync python wiki/research/prime_binary_new_attack/evidence/main.py
```

`--quick` runs $X=10^6$ only and omits the third check. The checks are:

1. rule (P) of the sketch, computed once from the phase and once from the
   parity of $h_n$ against the rule $\beta_{n,K}$, agrees on every start in
   every cell;
2. every mispredicted fraction lies in $[0.49,0.51]$;
3. at $X=10^7$, the total variation $\delta_0$ of Theorem F for $K=2,3,4$
   exceeds its value at $K=1$, the bias
   $|\Pr(h_n\text{ odd})-\Pr(h_n\text{ even})|$, by less than $0.01$.

The program prints the observed values. The fractions in check 2 lie between
$0.4968$ and $0.5046$ at $X=10^6$ and between $0.4986$ and $0.5020$ at
$X=10^7$, while a rational sum with odd denominator part $d$ would force them,
asymptotically, below $2dX/(2^KN_X)$, which at $X=10^7$ lies between $0.016$
and $0.031$ for $C=6$. At $X=10^7$ the bias at $K=1$ is $0.1174$, and
$\delta_0$ is $0.1174$, $0.1174$ and $0.1183$ for $K=2,3,4$. The program stops
at $K=4$: at $K=5$ there are $2^{14}$ residue keys for about $6\times10^5$
starts, too few starts per key for the empirical total variation to be
reliable, since sampling noise inflates it.

These are finite observations and exclude no denominator. This check supplies
neither an explicit threshold $X_0$ for Theorem C nor a bound on the
preperiod of a hypothetical rational value. It is separate from finite
tail-certificate methods that can exclude specified denominators. It shows
how far the primes in this range are from the concentration that a rational
sum would force at large scales.

The [independent matching-window review and grade](verify/matching_gap_windows/_index.md)
retain the exact subject and mathematical derivations for that conditional
argument. They do not examine or raise the standing of these finite numerical
observations. Conversely, the numerical entry point supplies no evidence for
the matching-window review's verdict.
