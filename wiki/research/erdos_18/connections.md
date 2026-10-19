---
name: research/erdos_18/connections
title: "Connections of the Problem 18 reconstructions"
desc: |
  Assesses, as mathematics, what the reconstructed factorial and
  practical-number arguments give for Problems 304, 293, 1099, 673 and 859
  and for the other questions of Problem 18: four proved transfer lemmas,
  two conditional deductions from the accepted factorial bound, a counting
  floor for the extension method, and the precise obstruction where a
  transfer fails.
created: 2026-09-28T06:15:52Z
updated: 2026-10-19T04:19:07Z
---

[[research/erdos_18/_index|..]]

***

This page transports the mechanisms reconstructed in this folder to the problems
they touch. Every statement on it is *author-recorded*: written and checked by
the compilation; it changes no problem status and assigns no tier. The
statements were independently reviewed as they stood on 2026-09-28T13:50:48Z by
nine focused reviews graded in
[[research/erdos_18/evidence/verify/connections_grade|the connections grade]],
which passes all nine and accepts seventeen corrections, since applied; it
assigns no tier. After the review, the Target paragraphs were updated to the
standing their problem pages record, and the next investigations of the Problem
304, 293 and 1099 sections to match; no statement or proof changed. Each
connection section names its target with the exact question and the status the
target's own page records, states what the mechanism gives when transported,
with a proof or with the missing bridge named, what it does not give and why,
and the next investigation. Inputs are consumed at their recorded standing: the
`hughes_` pages are proved modulo the second-hand import of the Berend–Harmse
estimate, the `doorn_` pages are *claimed*, and the factorial bound of question
(b) is the Conjectures.io-accepted Lean proof described on
[[problems/divisors/E0018/_index|the Problem 18 page]] (kernel checked by the
bounty site, not refereed, not built here).

**Conventions.** For practical $N$, $h(N)$ is the least $k$ such that every
integer $1\le m\le N$ is a sum of at most $k$ distinct divisors of $N$, a fresh
set for each $m$; erdosproblems.com's $h$ ranges over $m<N$ and is at most this
one, so every upper bound below holds for erdosproblems.com's $h$ as well.
$\tau(N)$ counts the divisors of $N$, $v_p$ is the $p$-adic valuation,
$L_x=\mathrm{lcm}(1,\dots,x)$, and $\varepsilon_j$ and the windows
$[\sqrt{(j-1)!},\sqrt{j!}]$ are those of
[[research/erdos_18/hughes_corollary_3_reconstruction|the Corollary 3 page]].
For $1\le a<b$, $N(a,b)$ is the least number of distinct unit fractions with
denominators above $1$ summing to $a/b$ and $N(b)=\max_{1\le a<b}N(a,b)$; $D_k$
is the set of denominators occurring in some decomposition
$1=1/n_1+\cdots+1/n_k$ with $1\le n_1<\cdots<n_k$, and
$v(k)=\min\{m>1:m\notin D_k\}$. For $\alpha>1$,
$h_\alpha(n)=\sum_i(d_{i+1}/d_i-1)^\alpha$ over the consecutive divisors
$1=d_1<\cdots<d_{\tau(n)}=n$.

## Shared lemmas

The four lemmas below are used by several sections. Each is author-recorded
with its proof; none is in the frozen reconstruction pages.

### Lemma A: a valuation criterion for the ratio-two property

**Statement.** Let $N\ge1$ satisfy $v_2(N)\ge\lfloor\log_2p\rfloor$ for every
odd prime $p$ dividing $N$. Then consecutive divisors of $N$ have ratio at
most $2$. Consequently, by the consequence clause of
[[research/erdos_18/hughes_lemma_4_reconstruction|Lemma 4]], $N$ is practical,
the greedy expansion of every $1\le m\le N$ uses distinct divisors, and
$h(N)\le\log_2N+1$. The hypothesis holds for $N=n!$, for $N=L_x$, and for
$N=p^jM$ whenever it holds for $M$ and $p$ is an odd prime with
$\lfloor\log_2p\rfloor\le v_2(M)$.

**Proof.** Let $d<N$ divide $N$ and put $q=N/d>1$. If $q$ is even, $2d$
divides $N$. If $q$ is odd, choose an odd prime $p\mid q$ and let
$2^c<p<2^{c+1}$ (strict, since $p$ is odd). Then $v_2(d)=v_2(N)\ge c$
because $q$ is odd, and
$v_p(d)<v_p(N)$ because $p\mid q$. So $d'=dp/2^c$ is an integer dividing $N$,
and $d<d'<2d$ since $1<p/2^c<2$. Hence some divisor lies in $(d,2d]$, which is
the ratio property. For the consequence: a nonterminal greedy step at $R$ with
bracketing divisors $d<R<b$ has $d\ge b/2>R/2$, so the remainder $R-d$ is below
$R/2$; after $s$ nonterminal steps the remainder is below $m/2^s$, so there are
at most $\lfloor\log_2m\rfloor$ nonterminal steps and one terminal divisor. For
$n!$, $v_2(n!)\ge\lfloor n/2\rfloor\ge\lfloor\log_2p\rfloor$ for every prime
$p\le n$ when $n\ge4$, and $n\le3$ is checked by inspection; for $L_x$,
$v_2(L_x)=\lfloor\log_2x\rfloor\ge\lfloor\log_2p\rfloor$ for $p\le x$; and
multiplying $M$ by an odd prime $p$ leaves $v_2$ unchanged, so the hypothesis
for $p^jM$ is the hypothesis for $M$ together with
$\lfloor\log_2p\rfloor\le v_2(M)$. $\square$

### Lemma B: the greedy count from a gap profile

This is the step count of
[[research/erdos_18/hughes_theorem_1_reconstruction|the Theorem 1 page]] with
the factorial windows replaced by an arbitrary profile; only the two symmetry
facts (i) and (ii) of that page and Lemma 4 are used, and both hold for every
$N$.

**Statement.** Let $N$ have the ratio-two property, let $T\ge2$ with
$2T\le\sqrt N$, and let $\delta\colon[T,\sqrt N]\to(0,1/8]$ be nonincreasing.
Suppose that every pair of consecutive divisors $d<b$ of $N$ with
$T\le\sqrt{db}\le\sqrt N$ satisfies

$$
\log\frac bd\le\tfrac12\,\delta\bigl(\sqrt{db}\bigr).
$$

Put $\sigma(\ell)=\log\bigl(1/\delta(e^\ell/2)\bigr)$ for
$\log(2T)\le\ell\le\tfrac12\log N$, a nondecreasing function with
$\sigma\ge\log8$. Then

$$
h(N)\le3\int_{\log(2T)}^{\frac12\log N}\frac{d\ell}{\sigma(\ell)}
+\log_2\sigma\bigl(\tfrac12\log N\bigr)+2\log_2(2T)+5 .
$$

**Proof.** Fix $1\le m\le N$ and run the greedy expansion $R_0=m>R_1>\cdots$;
by the ratio property the divisors used are distinct (Lemma 4). Count the
nonterminal steps by the remainder $R$ at which they start.

*Lower range $2T\le R\le\sqrt N$.* Let $d<R<b$ bracket $R$. As on the Theorem 1
page, $d>R/2$ and $b<2R$ give $R/\sqrt2<\sqrt{db}<\sqrt2R$, and fact (i)
($R\le\sqrt N$ forces $db\le N$) gives $\sqrt{db}\le\sqrt N$; also
$\sqrt{db}>R/\sqrt2\ge T$. The hypothesis and the monotonicity of $\delta$
give $\log(b/d)\le\tfrac12\delta(\sqrt{db})\le\tfrac12\delta(R/2)$, and Lemma
4 gives $R'=R-d\le2R\log(b/d)\le R\,\delta(R/2)$, that is,
$\log R'\le\log R-\sigma(\log R)$. Since $\sigma$ is nondecreasing, the
charging integral of the Theorem 1 page applies verbatim: each step's interval
$[\log R',\log R]$ carries $\int d\ell/\sigma(\ell)\ge1$, the intervals have
disjoint interiors and lie in $[\log(2T),\tfrac12\log N]$ except possibly the
last, so this range has at most $1+\int_{\log(2T)}^{\frac12\log N}d\ell/\sigma$
steps.

*Upper range $\sqrt N<R\le N/(2T)$.* Put $U=N/R\in[2T,\sqrt N)$. The mirror
pair $N/b<U<N/d$ consists of consecutive divisors with the same ratio $b/d$,
and its geometric mean $N/\sqrt{db}$ lies in $(U/\sqrt2,\sqrt2U)$ and is at
most $\sqrt N$ by fact (ii) ($R>\sqrt N$ forces $db\ge N$) and at least $T$.
Hence $\log(b/d)\le\tfrac12\delta(U/2)$ and, by Lemma 4 applied to $R$,
$R'\le R\,\delta(U/2)$, i.e. $\log U'-\log U\ge\sigma(\log U)$, where $U$
increases along the expansion. Partition $[\log(2T),\tfrac12\log N)$ into the
sets $J_k=\{\ell:2^k\log8\le\sigma(\ell)<2^{k+1}\log8\}$, $0\le k<K$, each an
interval or empty, with $K\le\log_2\bigl(\sigma(\tfrac12\log N)/\log8\bigr)+1$.
Consecutive starts in $J_k$ are separated in $\log U$ by at least
$2^k\log8$, while $1/\sigma>1/(2^{k+1}\log8)$ on $J_k$; so $J_k$ holds at most
$1+|J_k|/(2^k\log8)\le1+2\int_{J_k}d\ell/\sigma$ starts, and the range has at
most $K+2\int_{\log(2T)}^{\frac12\log N}d\ell/\sigma$ steps.

*Endgames.* For $R>N/(2T)$ and for $R<2T$ each step halves the remainder, so
each endgame has at most $\log_2(2T)+1$ steps. Adding the terminal divisor
gives the bound. $\square$

### Lemma C: the unit-fraction transfer (Lemma 5.1 of the van Doorn note)

Lemma 5.1 is the one step of the note's applications that the folder did not
reconstruct; it is elementary and is reconstructed here from physical p. 6 of
the note held by
[[../library/divisors/doorn_2026_practical_numbers_egyptian_fractions/_index|van Doorn (2026)]],
read in the extracted text. The note calls it well known; it is the transfer
behind Erdős's 1950 bound and behind Vose's, as the
[[problems/unit_fractions/E0304/_index|Problem 304 page]] records.

**Statement.** Let $n\ge b\ge2$ be integers with $n$ practical, and let
$1\le a<b$. Then $a/b$ is a sum of at most $2h(n)$ distinct unit fractions,
all with denominators above $1$; the denominators divide $n$ or have the form
$bn/e$ with $e\mid n$ and exceed $n$. If $b\nmid n$, none of them equals $b$.

**Proof.** Write $an=bq+r$ with $0\le r<b$. Then $q\le an/b<n$ and $r<b\le n$,
so $q$ (if positive) is a sum of $s\le h(n)$ distinct divisors $d_1,\dots,d_s$
of $n$, and $r$ (if positive) is a sum of $t\le h(n)$ distinct divisors
$e_1,\dots,e_t$ of $n$. Dividing by $bn$,

$$
\frac ab=\sum_{i=1}^{s}\frac1{n/d_i}+\sum_{j=1}^{t}\frac1{bn/e_j}.
$$

The $n/d_i$ are distinct integers above $1$ (as $d_i\le q<n$) and at most
$n$; the $bn/e_j$ are distinct integers above $n$ (as $e_j\le r<b$); so all
$s+t\le2h(n)$ denominators are distinct and exceed $1$. If $b\nmid n$, no
$n/d_i$ equals $b$, and every $bn/e_j$ exceeds $n\ge b$. $\square$

**Lemma C′ (avoiding a prescribed denominator with factorials).** Let $b\ge2$
be large, let $n$ be the least integer with $n!\ge b$, and let $p$ be the
least prime not dividing $n$ (so $p\le n-1$: the primes dividing $n$ have
product at most $n$, whence $p\ll\log n$). Put $N=n!$ if $b\nmid n!$, and
$N=p^{j}(n-1)!$ with $j=\lceil\log n/\log p\rceil$ otherwise. Then $N$ is
practical, $N\ge b$, $b\nmid N$, and

$$
h(N)\le\max\bigl(h(n!),\ h((n-1)!)+\lceil\log_2n\rceil\bigr).
$$

*Proof.* In the first case there is nothing to show beyond Lemma A. In the
second, $p^j\ge n$ gives $N\ge n!\ge b$. Every residue $c$ modulo $p$ with
$1\le c\le p-1\le n-2$ is itself a divisor of $(n-1)!$, hence of
$p^{i}(n-1)!$, not divisible by $p$, with total $c\le p^{i}(n-1)!$; the residue
$0$ is the empty sum. So
[[research/erdos_18/doorn_lemma_3_1_reconstruction|Lemma 3.1]] with $A=p$ and
$L=1$, applied $j$ times from the practical number $(n-1)!$, shows that $N$ is
practical with $h(N)\le h((n-1)!)+j$, and $j\le\lceil\log_2n\rceil$. Finally,
if $b\mid N$ then $b$ divides $\gcd(n!,p^j(n-1)!)=(n-1)!\gcd(n,p^j)=(n-1)!$,
contradicting the minimality of $n$, which gives $(n-1)!<b$. $\square$

### Lemma D: a counting floor for iterated extensions

**Statement.** Let $n_0$ be practical and let $n_{j+1}=A_jn_j$ ($0\le j<J$)
be a chain in which each step is certified by
[[research/erdos_18/doorn_lemma_3_1_reconstruction|Lemma 3.1]] with cost
$L_j$: every residue modulo $A_j$ is a sum of at most $L_j$ distinct divisors
of $n_j$. Then

$$
\sum_{j<J}L_j\ \ge\ \sum_{j<J}\frac{\log A_j}{\log\bigl(\tau(n_j)+1\bigr)}
\ \ge\ \frac{(\log\log n_J)^2-(\log\log n_0)^2}{2(\log2+\eta)}-C(\eta)
$$

for every $\eta>0$, with $C(\eta)$ depending on $\eta$ alone. Hence, for
chains from a bounded seed, $n_0\le C$ with $C$ fixed, the bound
$h(n_0)+\sum_jL_j$ that such a chain certifies for $h(n_J)$ is at least
$(1/(2\log2)-o(1))(\log\log n_J)^2$, where the $o(1)$ tends to $0$ as
$n_J\to\infty$ uniformly over the chains with $n_0\le C$. Without a bound on
the seed the sum $\sum_jL_j$ has no floor in $n_J$ alone: the one-step chain
$n_0=2^k$, $A_0=3$, $L_0=1$ satisfies the hypothesis of Lemma 3.1 and has
$\sum_jL_j=1$.

**Proof.** Distinct residues modulo $A_j$ need distinct representing subsets,
so $A_j\le\sum_{i\le L_j}\binom{\tau(n_j)}i\le(\tau(n_j)+1)^{L_j}$, which is
the first inequality. For the second, Wigert's maximal order of the divisor
function, $\log\tau(n)\le(\log2+\eta(n))\log n/\log\log n$ with $\eta(n)\to0$,
gives $\log(\tau(n_j)+1)\le(\log2+\eta'(n_j))\log n_j/\log\log n_j$ with
$\eta'\to0$. With $\ell_j=\log n_j$ and $f(\ell)=\log\ell/\ell$, which
decreases for $\ell>e$, let $n(\eta)$ be a threshold beyond which
$\eta'(n)\le\eta$ and $\log n>e$, and let $j(\eta)$ be the least index with
$n_{j(\eta)}\ge n(\eta)$; if there is none, then $n_J<n(\eta)$ and the bound
holds with any $C(\eta)\ge(\log\log n(\eta))^2/(2\log2)$. The steps
$j\ge j(\eta)$ contribute at least
$(\log2+\eta)^{-1}\sum(\ell_{j+1}-\ell_j)f(\ell_j)$, and a left Riemann sum
of a decreasing function dominates its integral, so this is at least

$$
\frac1{\log2+\eta}\int_{\ell_{j(\eta)}}^{\ell_J}f(\ell)\,d\ell
=\frac{(\log\ell_J)^2-(\log\ell_{j(\eta)})^2}{2(\log2+\eta)}.
$$

The step $j(\eta)-1$, if it exists, costs at least
$\log(n_{j(\eta)}/n(\eta))/\log(2n(\eta))$ by the first inequality and
$\tau(n)\le n$, which exceeds $(\log\ell_{j(\eta)})^2$ once $n_{j(\eta)}$ is
large in terms of $\eta$, and the other steps contribute nonnegatively. If
$j(\eta)=0$ the subtracted term is $(\log\ell_0)^2=(\log\log n_0)^2$ and
nothing compensates it. In either case
$\sum_jL_j\ge\bigl((\log\ell_J)^2-(\log\ell_0)^2\bigr)/(2(\log2+\eta))-O_\eta(1)$,
which is the second inequality. For $n_0\le C$ the subtracted term is
$O_C(1)$, and letting $\eta\to0$ gives the floor
$(1/(2\log2)-o(1))(\log\log n_J)^2$. $\square$

This floor is an obstruction to the *method*, not a lower bound for $h$: it
says that no certificate built from Lemma 3.1 extensions alone, from a fixed
seed, can prove $h(N)\le(\log\log N)^{2-\eta}$ or even a constant below
$1/(2\log2)\approx0.72$ in front of $(\log\log N)^2$. The van Doorn chain pays
$4$ per step where the first inequality demands
$\log A_j/\log\tau(n_j)\approx6/7$, and its primes of size $k^6\log k$ keep
$\tau(n_j)$ a factor about $6$ below the maximal order in the logarithm; both
are constant losses. The reconstructed $c_0=14/\log2\approx20.2$ sits a factor
$28$ above the floor.

## Problem 304: the number of unit fractions for a/b

**Target.** [[problems/unit_fractions/E0304/_index|Problem 304]] asks to estimate
$N(b)=\max_{1\le a<b}N(a,b)$ and whether $N(b)\ll\log\log b$. Its page records
the problem as solved, with the question proved: Theorem 1.1 of the OpenAI
mathematics release's manuscript of 25 September 2026 gives
$N(b)\ll\log\log b$, accepted on its Lean evidence as
[[problems/unit_fractions/E0304/claims/2026_09_25_openai|its claim page]]
records, so $N(b)\asymp\log\log b$ with Erdős's 1950 lower bound. The note's
Theorem 1.2 is
[[problems/unit_fractions/E0304/claims/2026_09_16_van_doorn|a pending partial claim]]
that the accepted bound implies. That bound supersedes (304.1)--(304.3)
below, which stay recorded as consequences of the transfer, as the closed lead
[[research/leads/factorial_unit_fraction_transfer/_index|factorial_unit_fraction_transfer]]
records. The maximum runs over all $1\le a<b$ with no coprimality condition,
and Lemma C covers every $a$.

**What transports.** Lemma C turns any practical $N\ge b$ into
$N(b)\le2h(N)$, so every bound on $h$ along a sequence that reaches every
scale becomes a bound on $N(b)$. Three inputs are available here.

*(304.1) From the accepted factorial bound (author-recorded; premise: the
Conjectures.io-accepted proof of question (b), at its recorded standing).* For
every $\varepsilon>0$ there is $b_0(\varepsilon)$ with

$$
N(b)\le2(\log b)^{\varepsilon}\qquad(b\ge b_0(\varepsilon)).
$$

*Proof.* Let $n$ be the least integer with $n!\ge b$. Then $n\to\infty$ with
$b$, and $(n-1)!<b$ gives $n<\log b$ for large $b$, since
$\log(n-1)!\ge(n-1)(\log(n-1)-1)>n$ once $n\ge14$. Lemma C with the practical
number $n!$ (Lemma A) gives $N(a,b)\le2h(n!)$ for every $a$, and the accepted
statement, $h(n!)<n^{\varepsilon}$ for all $n\ge n_0(\varepsilon)$, gives
$N(b)\le2n^{\varepsilon}\le2(\log b)^{\varepsilon}$ once $b>(n_0-1)!$. The
accepted statement is exactly this $h$ (the fresh-set reading over
$1\le m\le n!$), as the
[[../library/divisors/jenw1n_2026_lean_proof_erdos_problem_18b/target|accepted target page]]
records. $\square$

This is below Vose's $\sqrt{\log b}$ for every $\varepsilon<\tfrac12$ and is
the first consequence of the accepted part (b) drawn in this corpus; no
search for an earlier one was made. Its standing is that of part (b):
documented independent acceptance of the formal statement by the bounty
site, a single kernel, no refereeing, nothing built here; the transfer itself
is Lemma C.

*(304.2) From Hughes's Theorem 1 (author-recorded; imports the Berend–Harmse
estimate second-hand through
[[research/erdos_18/hughes_corollary_3_reconstruction|Corollary 3]]).* With
the same $n$, $n\log n=(1+o(1))\log b$ gives
$n/\log n=(1+o(1))\log b/(\log\log b)^2$, so
[[research/erdos_18/hughes_theorem_1_reconstruction|Theorem 1]] and Lemma C
give

$$
N(b)\le(4\log2+o(1))\,\frac{\log b}{(\log\log b)^2}.
$$

This improves Erdős's 1950 bound $c_1\log b/\log\log b$ by a factor
$\log\log b$ and is weaker than Vose's; it is recorded for completeness and
as a check of the transfer against a known route.

*(304.3) From the claimed van Doorn chain (claimed; every input labeled
*claimed* on its page).* [[research/erdos_18/doorn_proposition_4_1_reconstruction|Proposition 4.1]]
at $x=b$ with $p_*=3$ gives a practical $n\in[b,b^2)$ with
$h(n)\le c_0(\log\log b)^2-1$, and Lemma C gives
$N(b)\le2c_0(\log\log b)^2-2$ for $b\ge x_0$, which is the note's Theorem 1.2
as recorded on
[[../library/divisors/doorn_2026_practical_numbers_egyptian_fractions/theorem_1_2|its result page]].
The reconstruction of Lemma 5.1 above closes the one unreconstructed step of
that application; the chain stays claimed.

**What it does not give, and why.** The conjecture $N(b)\ll\log\log b$ is out
of reach of both reconstructed mechanisms, for reasons that can be made
exact. Lemma C gives $N(b)\le2\min\{h(N):N\ \text{practical},\ N\ge b\}$, so
the conjecture would follow from practical numbers $N$ with
$b\le N\le\exp((\log b)^{O(1)})$ and $h(N)\ll\log\log N$, that is, from
question (a) of Problem 18 with exponent $1$ at every scale. Along factorials
this is impossible:
[[research/erdos_18/hughes_remark_6_reconstruction|Remark 6]] gives
$h(n!)\gg(\log n)^2$, and with $n!\approx b$ this is
$\gg(\log\log b)^2$, so no bound on $h(n!)$, however sharp, gives less than
$(\log\log b)^2$ through Lemma C. Along the extension chains of the van Doorn
note it is impossible too: Lemma D shows that every certificate built from
Lemma 3.1 extensions from a seed bounded independently of the scale, as the
note's chain is, is at least $(1/(2\log2)-o(1))(\log\log N)^2$. So both
mechanisms stop at exponent $2$ for this target, and the exponent, not the
factor $2$ of Lemma C, is the obstruction. A bound $h(N)\ll(\log\log N)^2$
along some sequence reaching every scale, which is what (304.3) claims,
would leave the conjecture open by a factor $\log\log b$.

**Falsification attempts.** The transfer is uniform in $a$ because Lemma C is;
the quantifier "for all large $b$" follows from "for all large $n$" because
$n$ is nondecreasing in $b$; the denominators are distinct and exceed $1$ as
Problem 304 requires; erdosproblems.com's $m<N$ convention only lowers $h$; and
Lemma C uses representations of $q\le n-1$ and $r\le b-1$, inside the range
of the accepted statement. No defect was found.

**Next investigation.** None toward the target, which the accepted bound
settles; the lead
[[research/leads/factorial_unit_fraction_transfer/_index|factorial_unit_fraction_transfer]],
which held the route, is closed as superseded. The mathematical question left
by this page is the exponent-one question: is there, for every large $b$, a
practical $N\in[b,\exp((\log b)^{O(1)})]$ with $h(N)\ll\log\log N$? A positive
answer would give a second proof of the bound through Lemma C. Remark 6 shows
that factorials cannot supply it and Lemma D that Lemma 3.1 chains from a
bounded seed cannot; the greedy count of Lemma B on another ratio-two family,
such as $L_x$ under Lemma A, is excluded by neither, since its counting floor
$h(N)\ge\log N/\log(\tau(N)+1)$ is only of order $\log\log N$ for $N=L_x$,
but no gap input of the required strength is known.

## Problem 293: the least denominator missing from k-term decompositions of 1

**Target.** [[problems/unit_fractions/E0293/_index|Problem 293]] asks for the growth
of $v(k)$. Its page records the status *open*, since every claim is partial,
with $e^{e^{k/600}}\le v(k)$ for all large $k$, Corollary 1.3 of the OpenAI
mathematics release's manuscript of 25 September 2026, accepted on its Lean
evidence as
[[problems/unit_fractions/E0293/claims/2026_09_25_openai|its claim page]]
records, and $v(k)\le c_0^{(2/5+o(1))2^k}$ (van Doorn–Tang; the
Elsholtz–Planitzer count), so $\log\log v(k)=\Theta(k)$, the doubly
exponential growth the monograph guessed. The earlier
$e^{ck^2}\le v(k)$ (van Doorn–Tang, Theorem 1.1) is an accepted partial claim,
and the note's Theorem 1.3 is
[[problems/unit_fractions/E0293/claims/2026_09_16_van_doorn|a pending one]].
The accepted bound supersedes (293.1)--(293.3) below, which stay recorded as
consequences of the transfer, as the closed lead
[[research/leads/factorial_unit_fraction_transfer/_index|factorial_unit_fraction_transfer]]
records.

**What transports.** Two facts drive every deduction: the nesting
$D_k\subseteq D_{k+1}$ for $k\ge2$ (van Doorn–Tang, Lemma 2.1, refereed,
recorded on
[[../library/unit_fractions/doorn_2025_smallest_denominator_not_contained_unit_fraction/theorem_1_1|the Theorem 1.1 page]]),
and the observation that a practical $N\ge b$ with $b\nmid N$ turns Lemma C,
applied to $(b-1)/b$ and followed by adjoining $1/b$, into a decomposition of
$1$ with at most $2h(N)+1$ terms containing $b$. Hence
$b\in D_k$ for every $k\ge2h(N)+1$.

*(293.1) From the accepted factorial bound (author-recorded; premise: the
Conjectures.io-accepted proof of question (b)).* For every $\varepsilon>0$ there
is $k_0(\varepsilon)$ with

$$
v(k)\ \ge\ \exp\bigl((k/5)^{1/\varepsilon}\bigr)\qquad(k\ge k_0(\varepsilon)),
$$

so $v(k)\ge\exp(k^{A})$ for every fixed $A>0$ and all large $k$.

*Proof.* Let $b\ge2$ be large and let $N$ be the practical number of Lemma
C′, so $N\ge b$, $b\nmid N$ and
$h(N)\le\max(h(n!),h((n-1)!)+\lceil\log_2n\rceil)$, with $n<\log b$ the least
integer with $n!\ge b$. The accepted statement gives
$h(N)\le n^{\varepsilon}+\log_2n+2\le2n^{\varepsilon}$ for
$n\ge n_1(\varepsilon)$, so $b\in D_{k}$ whenever $k\ge4n^{\varepsilon}+1$, in
particular whenever $k\ge5(\log b)^{\varepsilon}$. Thus every $b$ with
$b_0(\varepsilon)\le b\le\exp((k/5)^{1/\varepsilon})$ lies in $D_k$, and every
$2\le b<b_0(\varepsilon)$ lies in $D_k$ for $k\ge k_1(\varepsilon)$ because
$v(k)\ge e^{ck^2}\to\infty$. Hence $v(k)>\exp((k/5)^{1/\varepsilon})$ for
$k\ge k_0(\varepsilon)$. $\square$

This lies strictly between the published $e^{ck^2}$ (the case $A=2$) and the
claimed doubly exponential bound. Its standing is that of part (b) plus the
elementary Lemmas C and C′.

*(293.2) From Hughes's Theorem 1.* The same route with
$h(N)\le(2\log2+o(1))n/\log n+O(\log n)$ places $b$ in $D_k$ once
$(4\log2+o(1))\log b/(\log\log b)^2\le k$, giving only
$\log v(k)\ge(1/(4\log2)-o(1))\,k(\log k)^2$, weaker than $e^{ck^2}$; it is
recorded so that the transfer is calibrated against the known bound.

*(293.3) From the claimed chain.* Proposition 4.1 at $x=b$, with $p_*$ an
odd prime factor of $b$ (or $b$ a power of two above $2^E$, when
$2^E\parallel n$ gives $b\nmid n$), Lemma C and the nesting give the note's
Theorem 1.3, $v(k)\ge\exp\exp\sqrt{k/(2c_0)}$, exactly as
[[../library/divisors/doorn_2026_practical_numbers_egyptian_fractions/theorem_1_3|its result page]]
sketches; Lemma C′ is not needed there because the proposition arranges
$b\nmid n$ itself. The chain stays claimed.

**What it does not give, and why.** Doubly exponential growth
$v(k)\ge e^{e^{ck}}$ needs $b\in D_k$ for $\log\log b\ll k$, that is,
decompositions of $1$ containing $1/b$ with $O(\log\log b)$ terms, which
through this route means $h(N)\ll\log\log b$: the exponent-one question of
the Problem 304 section again. The factorial route is capped at
$\exp\exp(C\sqrt k)$: the counting argument of Remark 6, applied to $N$ (for
$N=p^{j}(n-1)!$ one has $\tau(N)\le(j+1)\tau((n-1)!)$ and
$\log N\ge\log(n-1)!$), gives $2h(N)+1\ge2c(\log n)^2=(2c+o(1))(\log\log b)^2$
for the $N$ of Lemma C′, so it can only place $b$ in $D_k$ when
$\log\log b\le(1+o(1))\sqrt{k/(2c)}$. Certificates built from Lemma 3.1
extensions of a bounded seed are capped at the same shape by Lemma D, which
is why the claimed Theorem 1.3 has the form it has. The converse implication
of van Doorn–Tang's Section 3 ($b<v(k)$ gives $N(b-1,b)\le k-1$) turns
(293.1) into $N(b-1,b)\le5(\log b)^{\varepsilon}$, which (304.1) already
gives; nothing new flows back.

**Falsification attempts.** The case $b\mid n!$ is where a naive transfer
fails (the divisor $n!/b$ can appear in a greedy representation of
$(b-1)n!/b$, which would repeat $1/b$); Lemma C′ avoids it by changing the
practical number rather than the representation, and its three requirements
($N\ge b$, $b\nmid N$, the cost $\lceil\log_2n\rceil$) were each checked. The
nesting lemma is applied only from $k\ge2$, and the constructed decomposition
has at least two terms. Small $b$ are handled by the published growth of
$v(k)$, not by the accepted statement, whose threshold $n_0(\varepsilon)$ is
unknown. No defect was found.

**Next investigation.** None through this route, which the accepted bound
supersedes; the same lead is closed. A computation cannot test (293.1), whose
content is asymptotic; the known finite values $v(3),\dots,v(8)$ on the
problem page are consistent with every bound here.

## Problem 18, question (a), along the least common multiples

**Target.** Question (a) of [[problems/divisors/E0018/_index|Problem 18]]: are there
infinitely many practical $m$ with $h(m)<(\log\log m)^{O(1)}$? The page
records it as *claimed* (the Price claim and the van Doorn note, neither
accepted; erdosproblems.com showed OPEN), with Vose's $h(m)\ll(\log m)^{1/2}$
the best accepted bound. Erdős's own candidate sequences for small divisor
ratios were $n!$, $L_x=\mathrm{lcm}(1,\dots,x)$ and the primorials (Tenenbaum
1987, p. 2, read as described in the Problem 1099 section), and the
erdosproblems.com discussion of 14 September 2026 reduces $h(L_x)=O((\log x)^2)$
to a divisor-gap bound it does not prove. Since $\log\log L_x=\log x+o(1)$, such
a bound answers (a) with exponent $2$ along an explicit classical sequence.

**What transports.** Lemma A shows that $L_x$ is practical with consecutive
divisors in ratio at most $2$ and $h(L_x)\le\log_2L_x+1=(1/\log2+o(1))\,x$,
the analog of Erdős's $h(n!)\le n$. Lemma B then converts a gap profile for
the divisors of $L_x$ into a step count. Write the hypothesis in the form
Lemma B consumes:

$(\mathrm H_c)$ *There are $c>0$ and $x_0$ such that for every $x\ge x_0$,
every pair of consecutive divisors $d<b$ of $L_x$ with
$x\le\sqrt{db}\le\sqrt{L_x}$ satisfies $\log(b/d)\le(db)^{-c/(2\log x)}$.*

*(18a.1) Transfer (author-recorded; premise $(\mathrm H_c)$, unproved).* Under
$(\mathrm H_c)$, with $c\le4$ after decreasing $c$ if necessary,

$$
h(L_x)\le\Bigl(\frac3c+o(1)\Bigr)(\log x)^2
=\Bigl(\frac3c+o(1)\Bigr)(\log\log L_x)^2 .
$$

*Proof.* Take $T=x^{4/c}$ and $\delta(g)=2g^{-c/\log x}$ on $[T,\sqrt{L_x}]$;
then $\delta$ is nonincreasing, $\delta\le2e^{-4}<1/8$, $2T\le\sqrt{L_x}$
for large $x$ because $\log L_x=\psi(x)\sim x$, and $(\mathrm H_c)$ is the
hypothesis of Lemma B with this $\delta$. Here
$\sigma(\ell)\ge(c/\log x)\ell-2$, so with $\kappa=c/\log x$ the integral is
at most

$$
\frac1\kappa\log\frac{\kappa\cdot\tfrac12\log L_x-2}{\kappa\log(2T)-2}
\le\frac{\log x}{c}\log\frac{cx}{\log x}\le\frac{(\log x)^2}{c},
$$

using $\kappa\log(2T)-2\ge2$ and $\tfrac12\log L_x\le x$, while
$\log_2\sigma(\tfrac12\log L_x)=O(\log x)$ and $2\log_2(2T)=O(\log x/c)$.
$\square$

*The comment's form of the hypothesis, and where it fails.* The
erdosproblems.com comment writes
$\Delta_x(Y)=\max_{d_i<Y}(\min\{d_{i+1},Y\}-d_i-1)$ for the largest gap between
consecutive divisors of $L_x$ below $Y$ and proposes
$\Delta_x(Y)+1\le Y^{1-c/\log x}$ for all large $x$ and all $x<Y\le L_x$. As
stated this is false in the top range: at $Y=L_x$ the pair $(L_x/2,L_x)$ gives
$\Delta_x(L_x)+1\ge L_x/2$, while $L_x^{1-c/\log x}=L_x\,e^{-c\psi(x)/\log x}$
is far smaller, and the same failure occurs on $(L_x/2+2L_x^{1-c/\log x},L_x]$
and near every $L_x/k$ with bounded $k$. The lower-half form $(\mathrm H_c)$
repairs it, because the mirror symmetry $d\mapsto L_x/d$ (facts (i) and (ii)
inside Lemma B) makes the lower half suffice; the comment's recurrence
$R'\le R^{1-c/\log x}$ is, up to a constant factor, the lower-range step of
Lemma B and gives the constant $1/c$ there; the mirror recurrence on $U=L_x/R$
gives another $1/c$ in the upper range, so the direct count gives $2/c$, and
only the factor $3/2$ between it and the $3/c$ above is a bookkeeping loss. The
comment's appeal to strictly decreasing greedy divisors for distinctness is
supplied by Lemma A.

*(18a.2) What the known gap inputs give.* Tenenbaum's 1987 paper (Ann. Inst.
Fourier 37, no. 2, 1–18, open access, not held here; read in the Numdam text
layer, where the displayed formulas are garbled and the page
images were not read; its corrigendum, Ann. Inst. Fourier 50 (2000), no. 1,
317–319, cited by Hughes for the deduction on pp. 6–7 and Theorem 4, was not
read) deduces its Théorème 1 from the admissibility, for every $\beta<3/2$,
of $\varepsilon_k=\exp(-(\log k)^{\beta})$ for each of the three sequences,
which it then establishes: for large $k$, every
$z\in(\sqrt{L_{k-1}},\sqrt{L_k}]$ has a divisor of $L_k$ in
$(z,(1+\varepsilon_k)z]$. Fed into Lemma B as the profile
$\sigma(\ell)\approx(\log\ell)^{\beta}$ at scale $\ell\approx\tfrac12\psi(k)$,
this gives $h(L_x)\ll_\beta x/(\log x)^{\beta}$ for every $\beta<3/2$, the
analog of the Tenenbaum–Yokota factorial bound and a first improvement of
Lemma A's $x/\log2$; a Berend–Harmse-strength profile,
$\sigma(\ell)\asymp(\log\ell)^2$, would give order $x/(\log x)^2$ as Theorem 1
does for $n!$, but Berend and Harmse state (p. 572) that their method does
not apply to $L$ at all. Neither input approaches $(\mathrm H_c)$, whose
descent $\sigma(\ell)=c\ell/\log x$ is linear rather than polylogarithmic in
$\ell$.

*Scale of the hypothesis.* $\log\tau(L_x)=(\log2+o(1))\,x/\log x$, so the
window $[\sqrt{L_x}/x,\sqrt{L_x}]$, of logarithmic width $\log x$, holds a
consecutive pair with
$\log(b/d)\ge\log x/\tau(L_x)=\exp(-(\log2+o(1))x/\log x)$, while
$(\mathrm H_c)$ allows such a pair at most $\exp(-(c/2+o(1))x/\log x)$; so
necessarily $c\le2\log2+o(1)$. With $c$ near $2\log2$, $(\mathrm H_c)$ is at
the mean-gap scale near $\sqrt{L_x}$, where the exponent $-(c/2)x/\log x$ it
allows and the exponent $-(\log2)x/\log x$ of the mean gap agree to first
order; at scale $x^m$ with $m$ fixed it allows gaps $e^{-cm}$ of constant
size against a mean gap of order $x^{-m}$ up to powers of $\log x$, so below
the top it asks much less than mean-gap matching. Near the top it is a
statement of the kind no factorial gap estimate reaches (Berend and Harmse's
Remark 2 says their bound is the best their method gives up to a bounded
power of $\log_2n$).

*Exploratory computation (author-recorded; a finite sample proves nothing).*
For $x\le64$ every divisor of $L_x$ was enumerated and, over the consecutive
pairs with $x\le\sqrt{db}\le\sqrt{L_x}$, the least value of
$\kappa(d,b)=(\log x)\log(1/\log(b/d))/\log\sqrt{db}$, the largest $c$ for
which $(\mathrm H_c)$ holds at that pair, was computed: $\kappa_{\min}(x)=$
$1.116$, $1.257$, $1.311$, $1.298$, $1.348$, $1.358$ at $x=20,30,40,50,60,64$
($\tau(L_{64})=4128768$). It shows no downward trend over this range (it dips
once, from $1.311$ at $x=40$ to $1.298$ at $x=50$) and approaches
$2\log2=1.386\ldots$ from below; the binding pairs sit at the top of the
range, within a factor of about $2.6$ of $\sqrt{L_x}$ (the middle of the full
divisor range of $L_x$), where the largest $\log(b/d)$ in the top tenth falls
from $2.8\cdot10^{-2}$ at $x=20$ to $4.5\cdot10^{-5}$ at $x=64$. This was
observed after the fact, not predicted. The script and command are retained
on the lead page.

**What it does not give.** Nothing about $h(n!)$, hence nothing for questions
(b) and (c); nothing unconditional beyond $h(L_x)\ll x/(\log x)^{3/2-\eta}$;
and no bound on $h_\alpha(L_x)$ for Problem 1099, which needs gaps
$\ll g^{-\eta}$ at every scale rather than $g^{-c/\log x}$ (and is settled by
Tenenbaum anyway, see below).

**Next investigation.** The lead
[[research/leads/lcm_divisor_gap_greedy_route/_index|lcm_divisor_gap_greedy_route]]
holds the route. A proof of $(\mathrm H_c)$ for any $c>0$ gives exponent $2$
in question (a) along $L_x$, independently of the two AI-generated chains; a
disproof (a sequence of $x$ with $\kappa_{\min}(x)\to0$) shows that no
hypothesis of the form $(\mathrm H_c)$ with a fixed $c$ holds, so (18a.1) as
stated gives nothing along that sequence; whether a scale-dependent profile,
or one that tolerates a few exceptional pairs, still gives $(\log x)^2$
through Lemma B would remain open. The computation can be pushed to $x$ near
$100$ by enumerating only the divisors in a window around each scale instead
of all of them.

## Problem 18, question (c): what the greedy route would need

**Target.** Question (c): is $h(n!)<(\log n)^{O(1)}$? The page records it as
open, between [[research/erdos_18/hughes_remark_6_reconstruction|Remark 6]]'s
$(\log n)^2$ and the accepted $n^{o(1)}$ of question (b).

**What transports.** Lemma B is the only mechanism of this folder aimed at
$n!$. To obtain $h(n!)\le(\log n)^{C}$ from it one needs
$\int_{\ell_0}^{\frac12\log n!}d\ell/\sigma(\ell)\ll(\log n)^{C}$ over a
range of length $\tfrac12\log n!\sim\tfrac12n\log n$; the natural profile is
$\sigma(\ell)=\ell/(\log n)^{C-1}$, that is, consecutive divisors with
geometric mean $g$ in ratio $1+O(g^{-1/(\log n)^{C-1}})$. At the middle,
$g=\sqrt{n!}$, this is a gap $\exp(-n/(2(\log n)^{C-2}))$. But the window of
index $n$ has logarithmic width $\tfrac12\log n$ and holds at most $\tau(n!)$
divisors, so some consecutive pair there has
$\log(b/d)\ge\tfrac12\log n/\tau(n!)=\exp(-O(n/\log n))$, because
$\log\tau(n!)\asymp n/\log n$ (the upper bound is on the Remark 6 page; the
primes in $(n/2,n]$ give the lower bound). Hence the natural profile with
$C=2$ is inadmissible, and no admissible profile does better than exponent
$2$: the pair above forces $\sigma\le\log\tau(n!)$ on all but the last
$\tfrac12\log n+O(1)$ of the range, so the integral is at least
$(\tfrac12\log n!-O(\log n)-\log(2T))/\log\tau(n!)\gg(\log n)^2$ whenever
$\log T\le(\tfrac12-\eta)\log n!$, and otherwise the term $2\log_2(2T)$ is
$\gg n\log n$; this is consistent with Remark 6. Whether a profile capped at
$\sigma=cn/\log n$ for a small constant $c$, whose integral is
$O((\log n)^2)$, satisfies the hypothesis of Lemma B is a maximal-gap
question that this counting leaves open. The natural profile with $C=3$ asks
the largest gap to match this mean gap up to a constant in the exponent
throughout the windows of index $j\asymp n$, while asking much less below
them: the factorial analog of $(\mathrm H_c)$, with the same mean-gap
character near the top. The Berend–Harmse window,
$\exp(-(\log n)^2/(2\log2))$, is exponentially wider, which is why Theorem 1
stops at $n/\log n$.

**What it does not give.** The accepted proof of (b) does not run through a
gap profile: its structure, read only at the level of theorem statements on
[[../library/divisors/jenw1n_2026_lean_proof_erdos_problem_18b/target|the accepted target page]],
is a Fourier-decay property of product measures on $\mathbb Z/2^J$, closer in
spirit to the character-sum criterion of
[[research/erdos_18/doorn_lemma_3_2_reconstruction|Lemma 3.2]] than to the
greedy count, and nothing about divisor gaps can be extracted from this
folder's reading of it. Outcome: open; the greedy route to (c) is a
mean-gap problem for the divisors of $n!$ at least as hard as $(\mathrm H_c)$.

## Problem 1099: sums of powers of consecutive divisor ratios

**Target.** [[problems/divisors/E1099/_index|Problem 1099]] asks whether
$\liminf_nh_\alpha(n)\ll_\alpha1$ for $\alpha>1$. Its page records the problem
as solved, with the question proved, on
[[problems/divisors/E1099/claims/1984_10_01_vose|Vose's accepted claim page]],
and records Tenenbaum's 1987 theorem, which settles the question along the
factorials, the least common multiples and the primorials, on
[[problems/divisors/E1099/claims/1987_01_01_tenenbaum|its own claim page]].
The erdosproblems.com page attributes the
solution to Vose's construction, quotes Erdős's remark that $n!$ or
$\mathrm{lcm}(1,\dots,n)$ "would be good candidates", and states that it
remains unknown whether those two sequences have the property; its discussion
carries a comment of 2 July 2026 that the problem was also solved by
Tenenbaum in 1987. Tenenbaum's paper (cited above; read in the Numdam text
layer, page images not read) states this as its Théorème 1 with
$h(u)=u^\alpha$: $F_\alpha(N)=O_\alpha(1)$ uniformly for $N$ in the factorials,
the least
common multiples and the primorials, "la seconde partie de la conjecture
d'Erdős", and Berend and Harmse's introduction (p. 570) records the same. So
the factorial and lcm cases erdosproblems.com calls unknown are theorems of
1987, and the connection below reproves the factorial case with explicit
constants from the reconstructed Corollary 3; it changes no status.

**What transports (author-recorded; imports the Berend–Harmse estimate
second-hand through
[[research/erdos_18/hughes_corollary_3_reconstruction|Corollary 3]]).**
Let $\alpha>1$, $j_0=2^{16}$, $T=\sqrt{(j_0-1)!}$, and

$$
C(\alpha)=4\sum_{j\ge j_0}(4\varepsilon_j)^{\alpha-1}
\Bigl(\tfrac12\log j+\log2\Bigr),
$$

a convergent series since $\log(1/\varepsilon_j)=(1-o(1))(\log j)^2/(2\log2)$.
Then for every integer $n\ge T$,

$$
2\sum_{d=1}^{n-1}d^{-\alpha}\ \le\ h_\alpha(n!)\ \le\ 2\zeta(\alpha)+C(\alpha),
$$

so
$2\zeta(\alpha)\le\liminf_nh_\alpha(n!)\le\limsup_nh_\alpha(n!)\le2\zeta(\alpha)+C(\alpha)$.
The correction is small only when $\alpha$ is bounded away from $1$: for
every $j$, $(4\varepsilon_j)^{\alpha-1}\le2^{-62(\alpha-1)}$, so
$C(\alpha)\le2^{62\eta}C(1+\eta)\,2^{-62(\alpha-1)}$ for $\alpha\ge1+\eta$,
with $C(2)<10^{-10}$ and $C(3/2)<10^{-3}$; but $C(5/4)\approx20$ exceeds
$2\zeta(5/4)$, and $C(\alpha)\to\infty$ as $\alpha\to1^+$.

*Proof.* Write $N=n!$ and $r=b/d$ for a pair of consecutive divisors $d<b$;
$r\le2$ by Lemma A. Sort the pairs into three zones. *Bottom:* $d<T$. Every
integer up to $\lceil T\rceil\le n$ divides $N$, so $b=d+1$ and the pair
contributes $d^{-\alpha}$; the zone contributes less than $\zeta(\alpha)$.
*Top:* $b>N/T$. The mirror pair $(N/b,N/d)$ is consecutive with $N/b<T$, so
$N/d=N/b+1$ and $r-1=1/(N/b)$; the zone contributes less than $\zeta(\alpha)$.
The two zones are disjoint, since a pair in both would have $r>N/T^2>2$.
*Middle:* $d\ge T$ and $b\le N/T$. If $db\le N$ then
$g=\sqrt{db}\in[T,\sqrt N]$; otherwise the mirror pair has geometric mean
$N/g\in[T,\sqrt N]$ and the same
ratio. The windows of index $j_0\le j\le n$ cover $[T,\sqrt N]$, so Corollary
3 gives $\log r\le3\varepsilon_j$ at the window index $j$ of $\min(g,N/g)$.
Then $r-1\le e^{3\varepsilon_j}-1\le4\varepsilon_j$ and $r-1\le2\log r$, so
$(r-1)^\alpha\le(4\varepsilon_j)^{\alpha-1}\cdot2\log r$. The pairs assigned
to window $j$ through their own geometric mean have spans $[\log d,\log b]$
with disjoint interiors inside an interval of length $\tfrac12\log j+\log2$
(as $d>g/\sqrt2$ and $b<\sqrt2g$), and the pairs assigned through their mirror
likewise; summing $\log r$ over each family gives at most that length, so
window $j$ contributes at most
$4(4\varepsilon_j)^{\alpha-1}(\tfrac12\log j+\log2)$ and the zone at most
$C(\alpha)$. The lower bound counts the pairs $(d,d+1)$,
$1\le d\le n-1$, and their mirrors, which are distinct pairs for $n\ge4$.
$\square$

*Corollary (Erdős's companion question (1.2) of 1981, along $n!$).* Since
$\sum_i(r_i-1)-\log N=\sum_i(r_i-1-\log r_i)$ and
$0\le r-1-\log r\le\tfrac12(r-1)^2$,

$$
-1\ \le\ \sum_i\frac{d_{i+1}}{d_i}-\tau(n!)-\log n!
\ \le\ \zeta(2)+\tfrac12C(2)-1\qquad(n\ge T),
$$

so the difference Erdős asked about is bounded along the factorials.

**What it does not give.** Nothing for the least common multiples (Corollary
3 is a factorial statement; Tenenbaum's theorem covers them) and nothing for
$\liminf$ over all $n$ beyond what Vose and Tenenbaum proved. The argument is
Tenenbaum's Théorème 2, the principle Tenenbaum attributes to Vose, that
$F(N_k;h)\le\sum_{j\le k}(1+\varepsilon_j)h'(\varepsilon_j)\log(N_j/N_{j-1})$
for an admissible sequence along a divisor sequence, run with the
Berend–Harmse $\varepsilon_j$ in place of $\exp(-(\log j)^\beta)$ and with
the small divisors counted exactly instead of through $\varepsilon_j=1$;
Berend and Harmse (p. 572) note that their estimate could extend Tenenbaum's
class of $h$ along $n!$ without pursuing it. Only the explicit bound
$2\zeta(\alpha)+C(\alpha)$, with $C(\alpha)=O_\eta(2^{-62(\alpha-1)})$ for
$\alpha\ge1+\eta$, appears to be new, and no search for it in the later
literature was made.

**Falsification attempts.** The boundary $n\ge T$ is where "every integer up
to $T$ divides $n!$" is used; below it the bottom zone is not a run of
consecutive integers and the bound is not claimed. The window bound is applied
only to pairs whose relevant geometric mean lies in $[T,\sqrt N]$, and the
mirror map is a bijection of consecutive pairs, so no pair is dropped or
counted twice. The convergence of $C(\alpha)$ for $\alpha$ near $1$ uses the
superpolynomial decay of $\varepsilon_j$ recorded on the Corollary 3 page, not
the weaker $\varepsilon_j\le j^{-4}$. No defect was found; the imported
Berend–Harmse statement is the one Hughes prints and was not checked against
the 1993 paper's page images.

**Next investigation.** None toward the target, which is settled. Tenenbaum's
1987 theorem, which settles the two candidate sequences erdosproblems.com calls
unknown, has its own claim page on the problem page, linked above; this page's
reading of the exact statement should be checked on the page images of the
open-access paper (doi:10.5802/aif.1083) rather than in its text layer.

## Problem 673: the sum of consecutive divisor ratios

**Target.** [[problems/divisors/E0673/_index|Problem 673]] asks whether
$G(n)=\sum_{i<\tau(n)}d_i/d_{i+1}\to\infty$ for almost all $n$ and for an
asymptotic formula for $\sum_{n\le X}G(n)$. Its page records the problem as
solved, with both questions proved, on
[[problems/divisors/E0673/claims/1983_01_01_erdos_tenenbaum|Erdős and Tenenbaum's accepted 1983 claim page]],
whose Théorème 2 gives $\sum_{n\le x}G(n)=x\log x\,(1+o(1))$; the
erdosproblems.com page records Erdős's 1982 remark that the almost-all statement
is trivial, an erdosproblems.com comment's bounds
$\tau(n/m)/m\le G(n)\le\tau(n)$ for $1<m\mid n$ (the lower bound fails at $m=1$,
since $G(n)<\tau(n)$ for every $n$), and the Erdős–Tenenbaum result that
$G(n)/\tau(n)$ has a continuous distribution function.

**Outcome: fails.** Both questions quantify over almost all $n$ or average
over $n\le X$, while every mechanism of this folder concerns a single thin
sequence: $n!$, $L_x$, or the constructed $2^EV_j$, all inside the practical
numbers, which have density zero (their counting function is
$\sim cx/\log x$ by
[[../library/divisors/weingartner_2015_practical_numbers_distribution_divisors/_index|Weingartner's theorem]]).
Along $n!$ the statement is trivial without any gap estimate: Lemma A gives
$d_i/d_{i+1}\ge\tfrac12$ for every pair, so $G(n!)\ge(\tau(n!)-1)/2\to\infty$,
and the erdosproblems.com comment's bound already gives $\tau(n)/4\le G(n)$ for
even $n$. Nothing here bears on the average. No transfer exists, and no next
investigation is proposed.

## Problem 859: the density of n representing a fixed t

**Target.** [[problems/divisors/E0859/_index|Problem 859]] asks whether the density
$d_t$ of the integers $n$ for which $t$ is a sum of distinct divisors of $n$
satisfies $d_t\sim c_1/(\log t)^{c_2}$. Its page records the problem as
solved, with the answer disproved, on
[[problems/divisors/E0859/claims/2026_09_18_kruer_kohlmeyer|Kruer and Kohlmeyer's accepted Lean disproof]],
which the bounty site approved on 21 September 2026 and certified on 23
September 2026: $-\log d_t/\log\log t$ has lower limit $\delta=0.0860\ldots$
while $(\log t)^{\delta}d_t\to0$.

**Outcome: fails.** The target is resolved, and the mechanisms do not bear on
it in either direction. A practical $N\ge t$ makes every multiple of $N$ a
member of the set counted by $d_t$, so the constructions of this folder give
$d_t\ge1/N$ for the least practical $N\ge t$ of the construction, which is
at least $1/t^{2}$ (Proposition 4.1 places $N$ in $[t,t^2)$ once $t\ge x_0$)
and at most $1/t$ for any seed $N\ge t$, so polynomial in $1/t$ whatever the
construction, and says nothing at the scale $(\log t)^{-\delta}$. The
accepted disproof's lower estimate does use "practical seeds" inside a tilted
prime-pattern law (read only at the level of structure, as the problem page
says), but as seeds of a density argument, not through $h$; the reconstructed
bounds on $h$ neither supply nor replace that step. No transfer exists.

## Other divisor problems examined

The search of the problems, research and theory trees for the objects of the
proofs (practical numbers, sums of distinct divisors, consecutive divisor
ratios, divisors of $n!$ and of $L_x$, residue covering by short divisor
sums, greedy expansions) surfaced the following further pages; each is a
resemblance without a transfer, for the reason given.

- [[problems/divisors/E0144/_index|Problem 144]] (proved): almost every $n$ has
  divisors $d_1<d_2<2d_1$. For $n,x\ge3$ the divisors $2<3<4$ of $n!$ and
  $L_x$ give the property outright (Lemma A's non-strict ratio bound alone
  does not, as $N=2^k$ shows); the target is a density-one statement over all
  $n$.
- [[problems/divisors/E0886/_index|Problem 886]] and
  [[problems/divisors/E0887/_index|Problem 887]] (open): the number of divisors of
  $n$ in $(\sqrt n,\sqrt n+n^{1/2-\eta})$ or $(\sqrt n,\sqrt n+Cn^{1/4})$.
  For $n!$ these are multiplicative windows of relative width $(n!)^{-\eta}$
  or $(n!)^{-1/4}$, exponentially narrower than the Berend–Harmse window
  $\varepsilon_n=\exp(-(\log n)^2/(2\log2)(1-o(1)))$; the reconstructed
  estimate says nothing at those scales. (Berend and Harmse's Theorems 3
  and 4 concern the most balanced factorization of $n!$ and are not
  reconstructed here.)
- [[problems/divisors/E1100/_index|Problem 1100]] (open): the number of coprime
  consecutive divisor pairs. The pairs $(d,d+1)$, $d<n$, give
  $\tau_\perp(n!)\ge n-1$, far below the question's $\exp((\log n!)^{o(1)})$;
  the mechanisms bound gaps, not coprimality.
- [[problems/divisors/E0468/_index|Problem 468]],
  [[problems/divisors/E0469/_index|Problem 469]],
  [[problems/divisors/E0470/_index|Problem 470]] and
  [[problems/divisors/E1054/_index|Problem 1054]]: representation by partial sums of
  the divisor chain, pseudoperfect and weird numbers, and sums of the smallest
  divisors. Each concerns whether $n$ itself, or a given $n$, has one
  representation of a prescribed shape, not whether every $m\le N$ has a
  short one; the practical-number mechanism does not address them.
- [[problems/additive_combinatorics/E0350/_index|Problem 350]] (proved) and
  [[problems/divisors/E0882/_index|Problem 882]] (solved): distinct subset sums and
  divisibility among subset sums, the opposite of the many-representations
  property that practicality asserts.
- [[problems/divisors/E0446/_index|Problem 446]],
  [[problems/divisors/E0448/_index|Problem 448]],
  [[problems/divisors/E0449/_index|Problem 449]] and
  [[problems/divisors/E0450/_index|Problem 450]]: density statements about divisors
  of typical $n$ in short multiplicative intervals; the sequences here have
  density zero.

## Leads created

Two connections amount to routes someone could take up now, and each has a
lead folder:
[[research/leads/factorial_unit_fraction_transfer/_index|factorial_unit_fraction_transfer]]
records (304.1) and (293.1), the conditional deductions from the accepted
factorial bound with Lemma C and Lemma C′, and the fresh-context review they
need before the problem pages can carry them;
[[research/leads/lcm_divisor_gap_greedy_route/_index|lcm_divisor_gap_greedy_route]]
records the greedy route to exponent $2$ in question (a) along $L_x$ with its
explicit premise $(\mathrm H_c)$, the retained exploratory script, and the
obstruction at the mean-gap scale. The Problem 1099 reproof is not a lead:
its target is settled, and its literature question is a reading task noted
above.

## Sources read for this page

Beyond the folder's reconstruction pages and the six problem pages, this
page read: physical p. 6 of the van Doorn note in the text extracted from the
held PDF (Lemma 5.1 and the proofs of Theorems 1.2 and 1.3); the
erdosproblems.com pages of Problems 1099 and 673 and the discussion threads of
Problems 18 and 1099 on 2026-09-28; and the text layers of Tenenbaum's 1987
paper (doi:10.5802/aif.1083) and of Berend and Harmse's 1993 paper
(doi:10.5802/aif.1348) on Numdam, both open access, neither held in the library,
with displayed formulas garbled and page images not read. Statements taken from
those text layers are marked as such above and should be verified on the page
images before any problem page relies on them. The 2000 corrigendum to
Tenenbaum's paper (Ann. Inst. Fourier 50, no. 1, 317–319), which Hughes cites
for the deduction on pp. 6–7 and Theorem 4 of the 1987 paper, was not read.
