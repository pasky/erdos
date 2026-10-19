---
name: research/smooth_successor_primes/evidence/verify/conditional_chain/counting_keeper
title: "Counting and quantifiers keeper"
desc: Independent proof of the full real-variable squarefree-pair bound from Hypothesis A+, including overlap deletion and gcd fiber multiplicity.
created: 2026-10-16T04:10:53Z
updated: 2026-10-16T04:16:14Z
---

# Counting and quantifiers keeper

***

Examined on 15 October 2026 against all of
[product_reduction.md](../../assets/conditional_chain_subject/product_reduction.md.txt), including its
two final quantifier paragraphs, and the
[frozen catalog formulation](../../assets/conditional_chain_subject/catalog_statement.md.txt).
The reduction is attributed to Shisheng Li and Zhong Zhuang, following
Pollack and Pomerance after Erdos. The supplied project exposition and
parameter checks are Plasma AI's. Only that exposition was supplied; the
original draft's PDF was not inspected.

This proof needs only A+, unique factorization, multiplicativity of sigma
on coprime arguments, and elementary counting. It uses no computation,
weighted-dilation result, or independent literature theorem for the reduction.
It is reproduced below so that its strict inequalities and multiplicities can
be checked without an external proof pointer.

## 1. Fixing parameters and constructing strict-range products

First take fixed 0<epsilon<1. Choose fixed B>=8/epsilon, put eta=epsilon/16
and delta=1/(2B), then let x tend to infinity through real values. Write
L=log x and y=L^B. In particular delta<1/4 and y^delta=sqrt L. A+ supplies
at least M>=L^(B(1-eta)) primes p<=5y whose p+1 are sqrt L-smooth.
Let

$$
k=\left\lfloor\frac{L}{\log(5y+1)}\right\rfloor.
$$

Then k=L/(B log L)(1+o(1)), k>=1 and M>2k eventually. Form products of
exactly k distinct chosen primes. Unique factorization gives N=binomial(M,k)
different squarefree integers, each satisfying the strict bound

$$
a\le(5y)^k<(5y+1)^k\le x.
$$

This remains strict when x is an integer or when the final weak inequality is
an equality. No rounding of x is needed.

For M>=k, each factor (M-i)/(k-i) is at least M/k, proving
binomial(M,k)>=(M/k)^k directly. Also log k<=log L eventually. Hence

$$
\log N\ge k\log(M/k)
\ge (1-\eta-1/B)L-o(L).
$$

The coefficient is positive. The floors cost O(log L) in this estimate;
the difference between log(5L^B+1) and B log L costs o(L).

## 2. Collisions and deletion of large common support

For a squarefree product a, sigma(a)=product_(p dividing a)(p+1)<=x.
Every prime divisor of this value is at most sqrt L. Its exponent is at most
L/log 2. There are at most sqrt L possible primes, so the number of values
is at most the real number

$$
U=(1+L/\log2)^{\sqrt L},\qquad \log U=O(\sqrt L\log L)=o(L).
$$

An integer upper bound is unnecessary: if the actual number of values is v,
then v<=U and Cauchy's inequality gives at least N^2/v>=N^2/U ordered
equal-value pairs, including the diagonal.

Set t=ceil(eta k); eventually 1<=t<k. For a fixed first product, every second
product sharing at least t primes contains some t-subset of its support.
Choosing that subset and then the remaining primes bounds the number of bad
ordered pairs by N binomial(k,t) binomial(M,k-t). This deliberately
overcounts; it need not count equal-value pairs only. Dividing by N^2 gives

$$
\binom kt\frac{\binom M{k-t}}{\binom Mk}
=\binom kt\prod_{i=0}^{t-1}\frac{k-i}{M-k+t-i}
\le2^k(2k/M)^t.
$$

Here the denominator of each factor is at least M-k+1>=M/2. Since 2k/M<1
and t>=eta k, the logarithm of 2U times the last bound is at most

$$
(k+1)\log2+\log U
-\eta k\{B(1-\eta)\log L-\log(2L)\}
=-\eta(1-\eta-1/B)L+o(L).
$$

This tends to negative infinity. Bad pairs are therefore fewer than N^2/(2U),
and at least N^2/(2U) equal-value ordered pairs share fewer than t primes.
An identical pair shares k primes, so the retained pairs are all off-diagonal.
No independence or random-support heuristic is being used.

## 3. Cancelling the gcd and its fibers

For a retained pair write a=gu, b=gv with g=gcd(a,b). Squarefreeness implies
that g,u,v are pairwise coprime and squarefree. Thus

$$
\sigma(g)\sigma(u)=\sigma(a)=\sigma(b)=\sigma(g)\sigma(v),
$$

and sigma(g)>0 permits cancellation. It follows that sigma(u)=sigma(v),
gcd(u,v)=1, u!=v, and u,v<x. The use of squarefreeness is essential here:
gcd cancellation alone would not in general give the two multiplicative
identities for nonsquarefree a,b.

There are at most t-1<eta k primes in g, so

$$
g<(5y+1)^{\eta k}\le x^\eta.
$$

For a fixed unordered reduced pair {u,v} and a fixed positive integer g,
there are at most two ordered preimages, (gu,gv) and (gv,gu). Since g<x^eta,
the entire fiber has size at most 2 floor(x^eta)<=2x^eta. Some of these
candidate preimages fail the original support conditions, which only makes
the bound safer. Each reduced unordered pair gives exactly one representative
with 1<=u<v<x in h_sf(x). Therefore

$$
h_{\rm sf}(x)\ge\frac{N^2}{4U x^\eta},\qquad
\log h_{\rm sf}(x)\ge(2-3\eta-2/B)L-o(L).
$$

The two factors of two have different sources: discarding bad pairs and
forgetting the ordering of a reduced pair. Both are accounted for.

Because 3eta+2/B<=7epsilon/16<epsilon, the positive exponent margin absorbs
the o(L) and gives h_sf(x)>x^(2-epsilon) eventually. The inequality is strict.
Finally h(x)>=h_sf(x), because the squarefree pairs form a subset of the
catalog pairs. For epsilon>=1, use any fixed smaller loss in (0,1); for
x>1 its lower bound is stronger than the one requested.

## 4. Quantifier and formulation checks

The complete order is epsilon, then B,eta,delta, then x. Only one fixed
specialization of A+ is needed for each epsilon, evaluated at the unbounded
real argument y=(log x)^B. An assertion for infinitely many y would not be
enough, but the successor extraction establishes the required eventual
statement for every real y. No constants need to be uniform as epsilon or
delta tends to zero.

For integer b and real x, b<x is equivalent to b<ceil(x), so
h(x)=h(ceil(x)) and h_sf(x)=h_sf(ceil(x)). If one starts with an integer
version with 0<epsilon<1, the exponent 2-epsilon is positive and
ceil(x)^(2-epsilon)>=x^(2-epsilon); the same identity then extends that
version to real x. The displayed construction already treats real x directly.
Both final quantifier paragraphs of the frozen exposition are correct.

The catalog's informal exponent notation is satisfied in the stated eventual
sense: for every fixed positive loss the corresponding strict lower bound
holds for all sufficiently large x. Also h(x)<x^2, so these lower bounds
force log h(x)/log x to tend to 2; if a literal strict expression with a
single o(1) function is desired, choose a positive loss tending to zero
strictly larger than 2-log h(x)/log x. The same applies to h_sf.

The count is of pairs represented by a<b, not of possible divisor-sum values.
Every retained pair meets coprimality, equality of the sums of positive
divisors, squarefreeness and the strict upper endpoint. The attempted attacks
on the diagonal, common support, multiplicity, floors and real endpoints
fail for the explicit reasons above.
