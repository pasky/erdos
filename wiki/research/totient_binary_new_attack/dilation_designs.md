---
name: research/totient_binary_new_attack/dilation_designs
title: Signed Dilation Designs Need Many Primes
desc: |
  A signed combination of prime dilations that cancels the first K levels of
  the shift tail for every function uses at least K+1 distinct primes, so its
  Chinese-remainder modulus exceeds K^(K+1). When that modulus is at most
  the averaging scale, the cancelled levels form a vanishing fraction of
  a logarithmic window.
tags: []
sources: []
problems:
- 249
created: 2026-10-15T20:27:32Z
updated: 2026-10-15T20:27:32Z
---

# Signed Dilation Designs Need Many Primes

[[research/totient_binary_new_attack/_index|..]]

***

This page's result is Plasma AI's, author-recorded and without independent
review. The
[[research/leads/totient_binary_series/dilation_cube|prime dilation page]]
adapts the alternating cube of Tao and Teräväinen to
[[problems/irrationality/E0249/_index|Problem 249]]: $2^K$ prime dilations
with signs cancel the first $K$ levels of the shift tail identically, and the
Chinese remainder condition on $2^K$ primes limits $K$ to about
$\log_2\ln x$ at scale $x$ (its bound (7)). Proposition 1 below applies to
every signed design satisfying its hypotheses. Cancelling $K$ levels for
every function needs $K+1$ distinct primes larger than $K$. Thus the
modulus exceeds $K^{K+1}$. If it is at most the averaging scale $x$, this
cancels only $o(\log x)$ levels. In a method whose remaining tail bound
requires a cutoff of order $\log x$, improving the design alone therefore
leaves levels to estimate.

## Designs

A *design* is a nonempty finite set $V$ with, for each $v\in V$, a prime $p_v$, an
integer shift $s_v$ and a nonzero integer weight $c_v$, the pairs
$(p_v,s_v)$ being distinct. An integer $n$ is *admissible* when
$n\equiv s_v\pmod{p_v}$ for every $v$; then $N_v=(n-s_v)/p_v$ is an integer
and

$$
n+p_vh-s_v=p_v(N_v+h)\qquad(h\ge1).
$$

The design *cancels level $h$* when the weighted multiset
$\{p_vh-s_v\}$ vanishes, that is

$$
\sum_{v:\ p_vh-s_v=m}c_v=0\qquad\hbox{for every integer }m.
$$

Then $\sum_vc_vf(n+p_vh-s_v)=0$ for every function $f$ and every $n$, which
is the cancellation the cube uses in its Proposition 2 with
$p_\epsilon=p_0+\sum_k\epsilon_kv_k$ and $s_\epsilon=\sum_kk\epsilon_kv_k$.
Merging two vertices with the same pair $(p,s)$ adds their weights, so
distinct pairs lose no generality.

**Proposition 1 (L219).** Let a design cancel levels $1,\dots,K$, let every
$p_v$ exceed $K$, and suppose an admissible integer exists. Then the primes
$p_v$ take at least $K+1$ distinct values. Consequently their product $Q$,
the modulus of the admissible class, satisfies $Q>K^{K+1}$.

This is the claim
[[theory/irrationality/L219_dilation_design_prime_count/_index|L219]]. Its
[[theory/irrationality/L219_dilation_design_prime_count/_proof|canonical
proof]] observes that a vertex must share a fiber with some other vertex at
every cancelled level, that these partners are distinct because two vertices
with different primes share a fiber at most at one level, and that two
partners with the same prime $p'$ would make $p'$ divide the product of
$p_v-p'$ and a difference of levels, which is impossible for primes above
$K$.

The bound is about counting primes, not vertices: vertices may share a prime
when their shifts agree modulo it. The cube attains cancellation of $K$
levels with $2^K$ distinct primes, and it is not optimal. Ignoring
primality, give weight $+1$ to the integer points $(0,0),(4,10),(5,9)$ and
weight $-1$ to $(1,1),(6,12),(2,6)$, and let each point $(a,b)$ play the role
of $(p_v,s_v)$. These six points cancel levels $1,2,3$ in the sense above
and have six distinct first coordinates; at each level their fibers pair the
plus and minus points along one of three perfect matchings. The affine map
$(a,b)\mapsto(43+30a,30b)$ gives the actual prime design

$$
\begin{array}{c|ccc}
c_v=+1&(43,0)&(163,300)&(193,270)\\
c_v=-1&(73,30)&(223,360)&(103,180).
\end{array}
$$

All six first coordinates are distinct primes greater than three. The
Chinese remainder theorem supplies admissible $n$, even with the stronger
conditions $n\equiv s_v\pmod{p_v^2}$. Thus three-level prime designs can
use six vertices instead of the cube's eight. Check 8 of the
[evidence](evidence/main.py) verifies the primality and cancellation,
and verifies a twelve-point integer configuration cancelling four levels.
Primality is not established for that four-level configuration. These
examples do not determine the minimum number of primes for general $K$.

## Consequences for the window

The phase of the binary tail at $n$ depends on the totients at about
$\log_2n$ consecutive levels. The dilation page's averaged estimate takes
$n$ in one class modulo $Q$ inside $[x/2,x]$ with many representatives, so
$Q\le x$, and its prime-error analysis needs every dilation prime to exceed
the number of levels. Under those conditions Proposition 1 gives
$(K+1)\ln K<\ln x$, so

$$
K<(1+o(1))\frac{\ln x}{\ln\ln x},\qquad
\frac K{\log_2x}\longrightarrow0 .
$$

Consequently a cutoff $H\asymp\log x$ leaves $H-o(\log x)$ levels
uncancelled by this mechanism. The complete absolute tail estimate on the
dilation page requires such a cutoff in its specified regime, including
its common-divisor normalization. Its bound (8), with its extra hypotheses
on the averaging modulus, gives integrality below about
$(2-\varepsilon)\ln\ln x$ for each vertex and level separately outside
a proportion $O(1/\ln\ln x)$ of the class. It does not give simultaneous
integrality for all vertices and levels as their number grows. This is a bound on
one mechanism, cancellation of levels for every function by dilations, under
the stated conditions; it does not exclude cancellation that uses the values
of $\varphi$, a single lucky representative of a class with $Q>x$, or a
phase estimate for the remaining levels. It is consistent with the
[[research/totient_binary_new_attack/perturbation_barrier|perturbation
comparison]], whose separate scope is empirical distributions of shorter
windows up to $o(1)$ error.
