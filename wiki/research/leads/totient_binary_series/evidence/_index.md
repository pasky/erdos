---
name: research/leads/totient_binary_series/evidence
desc: |
  Exploratory recomputation of the 2-adic tail valuations through ten
  million, the excess-positive indices and a coarse progression-certificate
  filter, the one-large-prime windows, and a certified
  continued-fraction prefix of the binary totient series, with fixed finite
  expectations.
tags: []
sources: []
created: 2026-09-17T04:07:06Z
updated: 2026-10-03T08:06:56Z
---

# research/leads/totient_binary_series/evidence

[[research/leads/totient_binary_series/_index|..]]

[[research/leads/totient_binary_series/evidence/verify/_index|verify/]]: The blind first review of the binary totient lead as it stood on
2026-10-03 and its distinct grade, which records pass and assigns no tier.

***

The [entry point](main.py) recomputes $v_2(\Phi_N)$ for $1\le N\le10^7$,
where $\Phi_N=\sum_{n\le N}\varphi(n)2^{N-n}$, records the indices at which
$v_2(\Phi_N)-\log_2N$ reaches a new maximum or exceeds $0,1,2,3$, checks
that every record arises through a carry tie
$v_2(\varphi(N))=1+v_2(\Phi_{N-1})$, counts the excess-positive indices
$16\le N\le10^7$, those with $2^{v_2(\Phi_N)}>N+2$, lists the ones with
$2^{v_2(\varphi(N))+2}>N+2$, counts the one-large-prime windows defined
below, and certifies a prefix of the regular continued fraction of
$S=\sum\varphi(n)2^{-n}$ from the bounds $\Phi_M/2^M\le S\le(\Phi_M+M+2)/2^M$
with $M=40000$. Run it from the repository root:

```sh
uv run --no-sync python wiki/research/leads/totient_binary_series/evidence/main.py
```

The default is the full declared domain; `--quick` uses $N\le10^6$ and
$M=4000$ with its own fixed expectations. Both modes recompute everything
from the totient and prime-factor sieves, read no files and write none, and
exit nonzero on any failed obligation, including under `python -O`. The
observed full run takes about ten seconds. The accumulator holds $\Phi_N$
modulo $2^{64}$, so a valuation is exact whenever it is below $64$; the run
checks that the largest observed valuation, $29$, is below the cap. The
failure protocol was checked by mutating one expected hit count and, after
the extension, one expected window count in scratch copies; each produced a
named failed obligation and exit code $1$.

The fixed expectations are the observed results stated on
[[research/leads/totient_binary_series/_index|the owning page]]: the record list
$(16,4),(28,6),(64,10),(88,12),(2146743,28),(2786632,29)$ of pairs
$(N,v_2(\Phi_N))$; hit counts $72,45,21,9$ at excess thresholds $0,1,2,3$
over $16\le N\le10^7$; $71$ excess-positive indices in the same range, of
which exactly $64,204,512,1632$ satisfy $2^{v_2(\varphi(N))+2}>N+2$; $240$
one-large-prime windows, the last at $N=31790$, with truncated-run statistic $20$ over
$N\ge2^{15}-1$; a certified prefix of $11759$ partial quotients beginning
$1;2,1,2,1,1,2,1,12$ with largest quotient $15531$ at index $7055$; and
$6018$ decimal digits in the denominator of the last common convergent,
which bounds the denominator of any rational value of $S$ because $S$ lies
in the interval between the two bounds and hence in the cylinder of the
common prefix. Record comparisons, threshold tests and the excess-positive
and certificate conditions use integer comparisons; logarithms appear only
in descriptive output. The empirical valuation distribution is printed as
an observation and is not checked. This is author-checked finite coverage
of a stated domain; it supplies no statement about all $N$, no standing for
the target, and no independent review.

## What the counts mean

The owning page proves that a dyadic rational value $S=a/2^{v}$ forces
$2^{v_2(\Phi_N)}\le N+2$ once $N-v>\log_2(N+2)$, so each excess-positive
index excludes the exponents $v<N-\log_2(N+2)$, and infinitely many would
exclude all of them. The finite count $71$ says nothing about infinitely
many. The page also proves that a residue class on which $2^m\mid\Phi_N$
holds for every sufficiently large member forces $2^{m-2}\mid\varphi(n)$ at
every positive member $n$, so an excess-positive index that such a class
could deliver must satisfy $2^{v_2(\varphi(N))+2}>N+2$. The list of the
four indices meeting this necessary condition is a finite observation about
the indices found, not a statement about the classes themselves. The
[[research/leads/totient_binary_series/arithmetical_windows/classification|stronger
classification]] proves separately that only $(n,m)=(5,3)$ can have
actual divisibility, excess $2^m>n+2$, and an eventual whole-progression
certificate together. Thus the four retained indices are candidates
only for the coarser filter, and all fail the full class criterion.
The checker retains that weaker diagnostic; its finite scan is not the
proof of the classification.

An integer is called one-large-prime for a threshold $J$ when it has
exactly one distinct prime factor above $J$. If $n=sq^a$ with $s$
$J$-smooth and $q>J$ prime, then
$\varphi(n)=\varphi(s)q^{a-1}(q-1)$. The label describes a factorization
pattern, not the general availability of exact factorization or of
cancellation information. The window of $N$ is $N+1,\dots,N+J$ with
$J=\lceil\log_2(N+2)\rceil$, a lower bound for the block length needed
by the stated crude-tail certificate.

The script computes the largest and second-largest distinct prime factors
of every integer up to $10^7+24$, controlled against $257$,
$258=2\cdot3\cdot43$ and $264=2^3\cdot3\cdot11$. It reports the count
and last index of full one-large-prime windows. Its additional run
statistic is explicitly truncated: in the block
$2^{J-1}-1\le N\le\min(2^J-2,L)$, it scans a run starting at $N+1$
only as far as $\min(2^J-2,L)+J$, where $L$ is the run's declared limit.
The maximum of these truncated lengths for $N\ge2^{15}-1$ is $20$
when $L=10^7$. No claim about longer unscanned extensions is needed for
the full-window test. The absence of full windows above $N=31790$ is a
fact about this finite range only.

## Why the denominator exclusion follows

Let $p/q$ be the convergent at the end of the common prefix and let
$p'/q'$ be its predecessor. The closed cylinder has endpoints $p/q$ and
$(p+p')/(q+q')$, in the order determined by parity, and
$|pq'-p'q|=1$. The script checks that determinant and uses exact rational
comparisons to place both tail bounds strictly between these endpoints.
Every rational strictly inside the cylinder is
$(pu+p'v)/(qu+q'v)$ for coprime integers $u>v\ge1$. The mediant
endpoint has $u=v=1$; the convergent endpoint $p/q$ is treated separately.
The determinant shows that the displayed numerator and denominator are
coprime. Its denominator is therefore at least $q$; the convergent
endpoint has denominator $q$ as well. This justifies the
retained lower bound without inferring irrationality from a finite prefix.

## Separate interpolation certificates

The
[[research/leads/totient_binary_series/integer_interpolation/evidence/_index|integer
interpolation evidence]] has its own entry point and retained exact
inputs. It checks nine least full-image endpoints and all 36 specified
central-zero target solutions, including their weighted full-tail costs.
Its computation account gives the domain, commands and failure controls.
The entry point on this page does not run those checks. Neither finite
product establishes the uniform interpolation-cost estimate needed for
irrationality.
