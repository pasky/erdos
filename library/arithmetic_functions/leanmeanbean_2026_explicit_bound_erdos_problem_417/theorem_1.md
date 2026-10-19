---
name: arithmetic_functions/leanmeanbean_2026_explicit_bound_erdos_problem_417/theorem_1
title: "Theorem 1 (p. 1): the limit superior of V(x)/V'(x) is at most e^{M_*} < 2.195202"
desc: |
  Claims limsup V(x)/V'(x) <= e^{M_*} < 2.195202 for the two totient counts of
  Problem 417, where M_* = (log 2)/2 + sum over primes p >= 3 of
  p/(p-1)^2 log(p/(p-1)); unreviewed, and resting on Proposition 5.3 of an
  unrefereed manuscript.
created: 2026-10-14T22:07:06Z
updated: 2026-10-19T06:04:51Z
---

***

## Statement

The note works with the set $\mathcal T=\varphi(\mathbb N)$ of values of
Euler's function, the two counts

$$
V(x)=\#\{v\in\mathcal T:v\le x\},\qquad V'(x)=\#\{\varphi(n):n\le x\},
$$

and the least preimage $\ell(v)=\min\{n:\varphi(n)=v\}$ of a totient $v$
(p. 1). These are the two counts of Problem 417.

**Theorem 1** (p. 1). Let

$$
M_*=\frac{\log2}{2}+\sum_{p\ge3\text{ prime}}\frac{p}{(p-1)^2}\log\frac p{p-1}.
$$

Then

$$
\limsup_{x\to\infty}\frac{V(x)}{V'(x)}\le e^{M_*}<2.195202.
$$

The theorem has no hypotheses. Its proof argues for the equivalent lower bound
$\liminf V'(x)/V(x)\ge e^{-M_*}$ and ends with the numerical bound
$M_*<0.786274052$ (p. 2).

**Source.** *An explicit bound for Erdős problem 417*, two-page note (2026)
with no author line; Theorem 1 on p. 1, its proof on pp. 1--2. The edition
read is identified on the
[[arithmetic_functions/leanmeanbean_2026_explicit_bound_erdos_problem_417/_index|source card]].

**Read depth.** Claims checked: the statement and the definitions before it
were read clause by clause on the page images of the PDF. The proof was read
for its structure only and is not verified here; its exact rational prime sum
was not recomputed.

## Proof pointer

pp. 1--2. Write $W(x)$ for the sum of $v/\ell(v)$ over the totients $v\le x$
and $C_p(x)$ for the number of totients $v\le x$ with $p\mid\ell(v)$.

1. **Display (1).** For a fixed cut $H$, the common-prefix estimates of the
   manuscript's Proposition 5.3 leave, after an error
   $O(\varepsilon_HV(x))+o_H(V(x))$ with $\varepsilon_H\to0$, totients of the
   form $v=D(p-1)$ with $\ell(v)=Ap$, where the prime $p\ge x^{0.9}$ varies
   and the prefix fixes $D\le A$. For each prefix the prime number theorem
   makes the sum of $v/\ell(v)=(D/A)(1-1/p)$ over $p$ asymptotic to the
   number of these $p$ with $Ap\le x$, that is, of these $v$ counted by
   $V'(x)$. The note sums the errors using $(x/\log x)\sum D^{-1}=O_H(V(x))$
   over the prefixes and lets $H\to\infty$, which gives
   $W(x)=V'(x)+o(V(x))$.
2. **Displays (2)--(4).** Removing the exact power $p^a$ of $p$ from
   $\ell(v)$ leaves a preimage of $v/(p^{a-1}(p-1))$, so
   $C_p(x)\le\sum_{a\ge1}V(x/(p^{a-1}(p-1)))$. The fixed-scale limit
   $V(cx)/V(x)\to c$ for fixed $c>0$, with the bound
   $V(x/k)/V(x)\ll k^{-1/2}$ uniform in $k\ge1$ that iterating it at $c=2$
   gives, yields $\limsup C_p(x)/V(x)\le p/(p-1)^2$ by dominated
   convergence, the sum of the limits $1/(p^{a-1}(p-1))$. For $p=2$,
   minimality makes a least preimage divisible by $2$ divisible by $4$, so
   $v/2=\varphi(\ell(v)/2)$ is a totient, $C_2(x)\le V(x/2)$ and the limit
   superior is at most $1/2$.
3. **The mean of $\log(\ell(v)/v)$.** Since $\ell(v)/v$ is the product of
   $p/(p-1)$ over the primes $p\mid\ell(v)$, this mean over the totients
   $v\le x$ equals $\sum_pC_p(x)\log(p/(p-1))/V(x)$. Each term is
   $\ll p^{-3/2}$ uniformly in $x$, so the bounds of step 2 pass through the
   sum, and the mean has limit superior at most $M_*$: the weight $1/2$ at
   $p=2$ and $p/(p-1)^2$ at odd $p$, times $\log(p/(p-1))$.
4. **Jensen's inequality.** The mean of $v/\ell(v)$, which is $W(x)/V(x)$, is
   at least the exponential of minus the mean of $\log(\ell(v)/v)$. With
   step 1 this gives $\liminf V'(x)/V(x)\ge e^{-M_*}$, which is the theorem.
5. **The constant (p. 2).** At $z=1/(2p-1)$ one has
   $\log(p/(p-1))=\log((1+z)/(1-z))$, which the note bounds above by $U(z)$,
   the odd power series truncated after $z^{17}$ plus a geometric bound for
   the remainder. It reports that exact rational summation of
   $\tfrac12U(1/3)$ and the terms $p(p-1)^{-2}U(1/(2p-1))$ for the primes
   $3\le p\le N$, with $N=999990$, stays below $0.786273785$, and it bounds
   the primes above $N$ by the integers prime to $30$ and an integral, for
   $M_*<0.786274052$ and $e^{M_*}<2.195202$.

## Dependencies

- [[arithmetic_functions/openai_2026_asymptotic_formula_number_totients/theorem_2_1|Theorem 2.1]]
  of OpenAI, *An asymptotic formula for the number of totients* (p. 4),
  through its last clause only: $V(cx)/V(x)\to c$ for every fixed $c>0$.
  That clause is
  [[../wiki/problems/arithmetic_functions/E0416/claims/2026_09_25_openai|accepted on Problem 416]]
  with formalized evidence.
- Proposition 5.3 of the same manuscript (p. 27), its common prefix for all
  preimages: outside a small exceptional set, with bounds for the exceptional
  values and their tuples, every totient up to $t$ has a unique tuple
  $(p_0,\ldots,p_R,d)$, every preimage shares its prefix, and
  $\ell(v)=p_0\cdots p_R\,\ell(d)$. It has no result page here and was not
  checked; the manuscript, unrefereed, is filed as
  [[arithmetic_functions/openai_2026_asymptotic_formula_number_totients/_index|openai_2026_asymptotic_formula_number_totients]].
- The prime number theorem, dominated convergence and Jensen's inequality.

The note cites the manuscript (its reference [1]) by title, date and its
folder on the release's main branch, not by a fixed revision; the two labels
it uses carry the content it attributes to them in the edition the
manuscript's card identifies.

## Standing

Claimed and unreviewed. The theorem rests on Proposition 5.3 through step 1,
while the fixed-scale limit it takes from Theorem 2.1 is the accepted clause.
A review would have to check at least the derivation of display (1) from
Proposition 5.3, including the bound $(x/\log x)\sum D^{-1}=O_H(V(x))$ that the
note states without a reference, Proposition 5.3 itself, and the exact prime
sum; none of this was done here. The proof of the project's conditional claim
[[../wiki/theory/number_theory/L44_finite_prime_totient_phase/_index|L44]]
writes out its own versions of displays (1)--(4) from premises taken from the
same manuscript; it is author-recorded at tier 0 and is not a review of the
note.

## Bears on

- [[../wiki/problems/arithmetic_functions/E0417/_index|Problem 417]]: the
  theorem claims an explicit upper bound, $e^{M_*}<2.195202$, for the limit
  superior of the problem's ratio $V(x)/V'(x)$. It does not show that the
  limit exists, so it settles neither question.
