---
name: research/erdos_939/connections
title: "Connections of the Problem 939 reconstruction"
desc: |
  Assesses, as mathematics, what the reconstructed binomial construction gives
  for the open cases of Problem 939 and for Problems 940, 1107 and 937: a
  proved transfer lemma for monomial substitution, a proved Mason-Stothers
  obstruction to every polynomial family with two summands for r at least 3,
  a four-term quintic identity over the cube roots of unity that is not real,
  and the precise reasons the other transfers fail.
created: 2026-09-28T06:59:01Z
updated: 2026-10-28T16:29:39Z
---

[[research/erdos_939/_index|..]]

***

This page transports the mechanism reconstructed in this folder, the binomial
identity with monomial substitution of
[[research/erdos_939/theorem_1_reconstruction|the Theorem 1 page]], to the
problems it touches. Every statement on it is *author-recorded*: written and
checked by the compilation; it changes no problem status and assigns no tier.
The statements were
independently reviewed as they stood on 2026-09-28T13:50:48Z
by eight focused reviews graded in
[[research/erdos_939/evidence/verify/connections_grade|the connections grade]],
which passes all eight and accepts sixteen corrections, C1--C16, since applied;
it assigns no tier. Since the review, the Target paragraphs of the Problem 1107
and Problem 940 sections were updated to their pages' current records and that
of the Problem 939 section was restated without a date; this touches no examined
statement, proof, code or input. Each connection section names its target with
the exact question and the status the target's own page records, states what the
mechanism gives when transported, with a proof or with the missing bridge named,
what it does not give and why, and the next investigation. Two inputs are
consumed from outside this folder at their stated standing: the
polynomial-factor proposition of the Problem 940 research folder, which that
page records as proved and author-recorded, and the Mason–Stothers and
Brownawell–Masser bounds recalled on a claims-checked library page; the
Mason–Stothers bound is reproved below as Lemma 2, the Brownawell–Masser bound
is used only to say what it does not exclude, and the proposition is consumed in
Corollary 3.1 with its proof adapted to a progression.

**Conventions.** For an integer $r\ge2$, a positive integer $n$ is
*$r$-powerful* if $v_p(n)\ge r$ for every prime $p\mid n$; $1$ is
$r$-powerful, and $\mathcal P_r$ is the set of $r$-powerful positive integers.
A finite family of positive integers is *jointly coprime* if the greatest
common divisor of all its members is $1$. Over a field $K$ of characteristic
zero, a nonzero polynomial $f\in K[t]$ is called *$r$-powerful* if every root
of $f$ in an algebraic closure has multiplicity at least $r$; constants are
$r$-powerful, and since an irreducible polynomial over $K$ is separable, $f$
is $r$-powerful exactly when every irreducible factor of $f$ over $K$ occurs
with exponent at least $r$. The same words apply to a nonzero binary form
$F\in K[U,V]$ and its linear factors over the closure. For $f\in\mathbb C[t]$,
$n_0(f)$ is the number of distinct complex roots of $f$. Throughout, $U$ and
$V$ are the variables of the binomial identity in the form in which the
substitution $X=U^r$, $Y=V^r$ has already been made, so that the Theorem 1
identity reads

$$
(U^r+V^r)^r=(U^r-V^r)^r+\sum_{j\in J\setminus\{3\}}2\binom rjU^{r(r-j)}V^{rj}
+\sum_{\ell=1}^{t}v_\ell U^{r(r-3)}V^{3r},
$$

with $J$, $t$ and $v_1,\dots,v_t$ as on the reconstruction page.

## Shared results

### Lemma 1: the monomial-substitution transfer

This is the mechanism of the reconstruction, separated from the binomial
identity: an identity among polynomials whose terms are products of powers
at least $r$, with one $r$-th power term of a special shape and one monomial
term, produces jointly coprime $r$-powerful sums under integer substitution.

**Statement.** Let $r\ge2$ and $n\ge3$, and let $A_1,\dots,A_n\in\mathbb Z[U,V]$
be nonzero polynomials with

$$
A_1+\cdots+A_{n-1}=A_n
$$

such that

- (i) each $A_i=c_i\prod_jH_{ij}^{e_{ij}}$ with $c_i\in\mathbb Z\setminus\{0\}$,
  $H_{ij}\in\mathbb Z[U,V]$ and every $e_{ij}\ge r$ (the product may be
  empty);
- (ii) $V^r$ divides $A_i$ in $\mathbb Z[U,V]$ whenever $|c_i|>1$;
- (iii) $A_1=K^r$ for some $K\in\mathbb Z[U,V]$ with $K(U,0)=\pm U^{d}$ and
  $K(0,V)=\pm V^{d'}$ for some $d,d'\ge0$;
- (iv) $A_2=c_2U^aV^b$ is a monomial with $a+b\ge1$ (so, by (i), each of
  $a,b$ is $0$ or at least $r$).

Let $B\ge1$ be an integer divisible by every prime that divides some $c_i$,
$1\le i\le n$, and let $m\ge1$ be coprime to $B$ with $A_i(m,B)>0$ for every
$i$. Then $A_1(m,B),\dots,A_{n-1}(m,B)$ are jointly coprime $r$-powerful
integers whose sum $A_n(m,B)$ is $r$-powerful. If, for such a $B$, every
$A_i(U,B)$ is a polynomial in $U$ with positive leading coefficient, the
positivity holds for all sufficiently large $m$; if $A_n(U,B)$ is nonconstant
the sums $A_n(m,B)$ then take infinitely many values; and if
$A_i(U,B)\ne A_j(U,B)$ as polynomials in $U$ for all $i\ne j$ below $n$, the
summands are pairwise distinct for all but finitely many $m$.

**Proof.** *Powerfulness.* Fix $i$ and a prime $p$ dividing $A_i(m,B)$. If
$p\nmid c_i$, then $p$ divides some $H_{ij}(m,B)$ and
$v_p(A_i(m,B))\ge e_{ij}\,v_p(H_{ij}(m,B))\ge r$. If $p\mid c_i$, then
$|c_i|>1$, so (ii) gives $A_i(m,B)=B^rA_i'(m,B)$ with $A_i'\in\mathbb Z[U,V]$,
and $p\mid B$ gives $v_p(A_i(m,B))\ge r$. This applies to every $i$, including
$i=n$.

*Joint coprimality.* Let a prime $p$ divide $A_i(m,B)$ for every $i\le n-1$.
From (iv), $p\mid c_2m^aB^b$; if $p\mid c_2$ then $p\mid B$ by the choice of
$B$; so in every case $p\mid mB$. From (iii), $p\mid K(m,B)$. If $p\mid m$,
then $K(m,B)\equiv K(0,B)=\pm B^{d'}\pmod p$, which is prime to $p$ because
$\gcd(m,B)=1$; if $p\mid B$, then $K(m,B)\equiv K(m,0)=\pm m^{d}\pmod p$,
prime to $p$ for the same reason. Both cases contradict $p\mid K(m,B)$.

*The rest.* The sum is the identity evaluated at $(m,B)$. A polynomial in $U$
with positive leading coefficient is positive for all large $U$; a nonconstant
one takes infinitely many values on the integers coprime to $B$, which form an
infinite set; and $A_i(U,B)-A_j(U,B)$, a nonzero polynomial in $U$, has
finitely many roots. $\square$

The Theorem 1 identity satisfies (i)–(iv) with $A_1=(U^r-V^r)^r$, $K=U^r-V^r$
($d=d'=r$), $A_2=2rU^{r(r-1)}V^r$ (the $j=1$ term), the other binomial and
split terms as monomials with exponents that are multiples of $r$, and
$A_n=(U^r+V^r)^r$; (ii) holds because every coefficient other than $1$ sits on
a term carrying $V^{rj}$ with $j\ge1$. With $B=B_0:=\prod_{p\in P}p$ and $m=q$
a prime above $B_0$, the lemma is the reconstruction's proof minus the
distinctness step.

**Corollary 1.1 (two free parameters).** Let $r\ge6$. For every positive
multiple $B$ of $B_0$ and every integer $m>B$ coprime to $B$, the Theorem 1
identity at $(U,V)=(m,B)$ is a tuple of $r-2$ pairwise distinct, positive,
jointly coprime $r$-powerful integers with $r$-powerful sum
$N=(m^r+B^r)^r$, and the number of such tuples with $N\le X$ lies between
$c_rX^{2/r^2}/\log\log X$ and $C_rX^{2/r^2}$ for all large $X$, with
constants depending only on $r$.

*Proof.* Lemma 1 applies with the positivity supplied by $m>B$. Distinctness
follows as on the reconstruction page with a prime divisor $p$ of $m$ in the
role of $q$: $p\nmid B$, so the $p$-adic valuations of the binomial terms are
$r(r-j)v_p(m)$, distinct for distinct $j$, the split terms share valuation
$r(r-3)v_p(m)$ and have distinct coefficients, $(m^r-B^r)^r$ and the $j=r$
term $2B^{r^2}$ have valuation $0$, and $(m^r-B^r)^r=2B^{r^2}$ is impossible
because $2$ is not the $r$-th power of a rational number. Distinct pairs
$(m,B)$ give distinct tuples, since $N$ and the first summand determine
$m^r+B^r$ and $m^r-B^r$. For the count, $N\le X$ forces
$m,B\le X^{1/r^2}$, giving the upper bound. For the lower bound put
$M=\lfloor X^{1/r^2}/2\rfloor$; every pair with $B\le M/2$ and $M/2<m\le M$
has $N\le(2M^r)^r\le X$, and for each such $B$ the number of $m\in(M/2,M]$
coprime to $B$ is $\tfrac M2\,\phi(B)/B+O(2^{\omega(B)})$, which is
$\gg M/\log\log M$ because $\phi(B)/B\gg1/\log\log B$ and
$2^{\omega(B)}\ll B^{o(1)}$; summing over the $\asymp M/B_0$ multiples $B$ of
$B_0$ below $M/2$ gives $\gg M^2/\log\log M$. $\square$

### Lemma 2: the Mason–Stothers inequality

**Statement.** Let $a,b,c\in\mathbb C[t]$ be nonzero, pairwise coprime and not
all constant, with $a+b=c$. Then

$$
\max(\deg a,\deg b,\deg c)\le n_0(abc)-1 .
$$

This is the three-summand bound recalled on
[[../library/diophantine_problems/corvaja_zannier_2011_abcd_function_fields/recalled_abc_abcd_bounds|the Corvaja–Zannier source page]]
in its genus-zero normalization: for polynomials without a common factor the
height is the maximal degree, and the support $S$ is the set of distinct roots
of $abc$ together with the point at infinity, so $|S|-2=n_0(abc)-1$. The same
statement is used on the
[[research/erdos_699/remaining/details/cubic_curves|cubic-curves page of the Problem 699 folder]].
Because the library reading is at claims level, the classical proof is
recorded here.

**Proof.** Put $W=ab'-a'b$. Since $c=a+b$, also $W=ac'-a'c$, because
$a(a'+b')-a'(a+b)=ab'-a'b$. If $W=0$ then
$(a/b)'=0$, so $a/b$ is constant, and coprimality forces $a$ and $b$, hence
$c$, to be constant, which is excluded; so $W\ne0$. A root $\alpha$ of $a$ of
multiplicity $\mu$ is a root of $a$ and of $a'$ of multiplicities $\mu$ and
$\mu-1$, so $(t-\alpha)^{\mu-1}$ divides $W=ab'-a'b$; the same holds for the
roots of $b$ through $W=ab'-a'b$ and for the roots of $c$ through
$W=ac'-a'c$. Since $a,b,c$ are pairwise coprime, these roots are distinct, so
$\prod_\alpha(t-\alpha)^{\mu_\alpha-1}$ over all roots of $abc$ divides $W$,
and comparing degrees,

$$
\deg a+\deg b+\deg c-n_0(abc)\le\deg W .
$$

From $W=ab'-a'b$, $\deg W\le\deg a+\deg b-1$, which gives
$\deg c\le n_0(abc)-1$; the other two expressions of $W$ give the bounds for
$\deg a$ and $\deg b$. $\square$

### Theorem 3: no polynomial family with two summands for r at least 3

**Statement.** Let $r\ge2$ and let $a,b,c\in\mathbb C[t]$ be pairwise coprime
$r$-powerful polynomials, not all constant, with $a+b=c$. Then $r=2$ and none
of $a,b,c$ is constant. More generally, if $a$, $b$ and $c$ are respectively
$r_a$-, $r_b$- and $r_c$-powerful with $r_a,r_b,r_c\ge2$, then the sum of
$1/r_f$ over the nonconstant $f\in\{a,b,c\}$ exceeds $1$.

**Proof.** Let $D$ be the maximal degree and let $k$ be the number of
nonconstant polynomials among $a,b,c$; the identity forces $k\ge2$. An
$r_f$-powerful polynomial $f$ has $n_0(f)\le\deg f/r_f$, and constants have no
roots, so by pairwise coprimality $n_0(abc)\le\sum_f\deg f/r_f\le D\sum_f1/r_f$,
the sums over the nonconstant $f$. Lemma 2 gives $D\le D\sum_f1/r_f-1$, so
$\sum_f1/r_f>1$. With a common $r$ this reads $k/r>1$; since $k\le3$ this
forces $r=2$ and $k=3$. $\square$

The $r=2$, $k=3$ case is realized by $(t^2-1)^2+(2t)^2=(t^2+1)^2$, so the
theorem is sharp.

**Corollary 3.1 (arithmetic form).** Let $r\ge2$ and let $a,b\in\mathbb Z[t]$,
$c=a+b$, not all constant, be such that for every sufficiently large integer
$t$ in some arithmetic progression the values $a(t),b(t),c(t)$ are positive
$r$-powerful integers, and $\gcd(a(t),b(t))=1$ for infinitely many such $t$.
Then $r=2$ and $a,b,c$ are all nonconstant. In particular, for $r\ge3$ there
is no one-parameter polynomial family of coprime $r$-powerful solutions of
$a+b=c$, and for $r=2$ none in which a term is constant.

**Proof.** The polynomial-factor proposition of the Problem 940 folder,
[[research/erdos_940/finite_core_reduction|"Independent polynomial summands still reduce to fixed forms"]]
(proved there, author-recorded), states that a nonconstant $f\in\mathbb Z[t]$,
eventually positive and $r$-powerful at every sufficiently large integer
input, has every nonconstant irreducible factor over $\mathbb Q$ with
multiplicity at least $r$. Its proof chooses a prime $p$ outside a finite bad
set and a residue class modulo $p^2$ on which $v_p(f)$ equals the multiplicity
of one factor; if the inputs are restricted to a progression modulo $M$,
choose $p\nmid M$ as well and intersect the two classes by the Chinese
remainder theorem, which still leaves arbitrarily large inputs. So each of
$a,b,c$ is $r$-powerful as a polynomial (the irreducible factors over
$\mathbb Q$ are separable). If $a$ and $b$ had a nonconstant common factor in
$\mathbb Q[t]$, a primitive associate $D_0\in\mathbb Z[t]$ would divide both in
$\mathbb Z[t]$ by Gauss's lemma, so $D_0(t)$ would divide $\gcd(a(t),b(t))$
for every integer $t$, and $|D_0(t)|\ge2$ for all large $t$ would contradict
the coprimality hypothesis. Hence $\gcd(a,b)=1$, and then
$\gcd(a,c)=\gcd(b,c)=1$ by the identity. Theorem 3 applies. $\square$

The corollary covers exactly the device of this folder: a fixed polynomial
identity evaluated on integer parameters. In two parameters $(m,B)$ the device
runs along the lines $B$ fixed, and any polynomially parametrized curve in the
parameter space on which the hypotheses hold reduces to the one-parameter
statement. What it does not cover is a polynomial identity whose terms share
a nonconstant factor $D$ and whose members are taken only at the integer
points where $D=\pm1$: there the mechanism has become the solution of a
Diophantine equation, which is a construction of a different kind.

### Proposition 4: a four-term identity of fifth powers of quadratics

**Statement.** Let $\omega$ be a primitive cube root of unity and let
$Q=aU^2+bUV+cV^2\in\mathbb C[U,V]$ satisfy $ac=-2b^2$. Then

$$
\sum_{k=0}^{2}Q(\omega^kU,\omega^{-k}V)^5=(3b\,UV)^5 .
$$

**Proof.** The substitution $U\mapsto\omega U$, $V\mapsto\omega^{-1}V$
multiplies $U^{10-j}V^j$ by $\omega^{10-2j}$, which is $1$ exactly when
$j\equiv2\pmod3$, that is for $j\in\{2,5,8\}$. Summing over $k$ therefore
triples these three monomials of $Q^5$ and kills the others, since
$1+\omega^e+\omega^{2e}=0$ for $3\nmid e$. By the multinomial theorem,

$$
[U^8V^2]Q^5=5a^4c+10a^3b^2=5a^3(ac+2b^2),\qquad
[U^2V^8]Q^5=5ac^4+10b^2c^3=5c^3(ac+2b^2),
$$

$$
[U^5V^5]Q^5=30a^2bc^2+20ab^3c+b^5 ,
$$

and under $ac=-2b^2$ the first two vanish while the third is
$120b^5-40b^5+b^5=81b^5$; three times $81b^5U^5V^5$ is $(3bUV)^5$. $\square$

**Corollary 4.1.** With $(a,b,c)=(1,1,-2)$ the three forms
$Q_k=\omega^{2k}U^2+UV-2\omega^kV^2=\omega^{2k}(U-\omega^kV)(U+2\omega^kV)$,
$k=0,1,2$, satisfy

$$
Q_0^5+Q_1^5+Q_2^5=(3UV)^5
$$

in $\mathbb Q(\omega)[U,V]$; no proper subsum vanishes and the four forms have
no common factor, so the Fermat quintic surface $x^5+y^5+z^5=w^5$ contains
the conic $(Q_0:Q_1:Q_2:3UV)$ defined over $\mathbb Q(\omega)$. However, no
projective linear change of variables over $\mathbb C$ and no rescaling of
the four forms makes all four of them real polynomials. Consequently the
identity has no version with four terms in $\mathbb Q[U,V]$, and Lemma 1 does
not apply to it over $\mathbb Z$.

*Proof of the last two sentences.* If $g\in\mathrm{PGL}_2(\mathbb C)$ made
all four forms real up to scalars, the root set of each form would be stable
under $\tau=g\circ\overline{\phantom{z}}\circ g^{-1}$, an anti-holomorphic
involution of $\mathbb P^1$ with a circle of fixed points. The root pairs are
$\{0,\infty\}$, $\{1,-2\}$, $\{\omega,-2\omega\}$ and
$\{\omega^2,-2\omega^2\}$. Stability of $\{0,\infty\}$ forces
$\tau(z)=\lambda\bar z$ with $|\lambda|=1$ or $\tau(z)=\lambda/\bar z$ with
$\lambda$ real. In the first case $\tau(1)=\lambda\in\{1,-2\}$ gives
$\lambda=1$, and then $\tau(\omega)=\omega^2\notin\{\omega,-2\omega\}$. In the
second case $\tau(1)=\lambda$ and $\tau(-2)=-\lambda/2$ must both lie in
$\{1,-2\}$, so $\lambda=-2$; then $\tau(z)=-2/\bar z$ does preserve all four
pairs, but it has no fixed point, since $|z|^2=-2$ has no solution. So no
anti-holomorphic involution with fixed points preserves the four pairs. A
four-term identity in $\mathbb Q[U,V]$ would in particular be real. $\square$

The complex identity was found by the multi-start numerical search described
in the Problem 939 section at $r=5$ and then recognized and proved in this
form; whether conics on the Fermat quintic surface are recorded in the
literature was not searched.

## Problem 939 at r = 4: the two-summand case

**Target.** [[problems/diophantine_problems/E0939/_index|Problem 939]], first and
second questions at $r=4$: can a sum of two coprime $4$-powerful numbers be
$4$-powerful, and are there at most finitely many such sums? The problem page
records both as open at $r=4$, with no example known and a forum-reported
exhaustive search giving $\max(a,b)>10^{14}$ for any solution; the
erdosproblems.com question's coprimality is joint, which for two summands is the
same as pairwise.

**What transports.** Nothing positive; the transported mechanism is excluded.
Corollary 3.1 shows that no polynomial family, in the sense of a fixed
identity $a(t)+b(t)=c(t)$ in $\mathbb Z[t]$ evaluated on all large integers of
a progression, produces coprime $4$-powerful solutions, whatever the shape of
its terms, and the same holds along every line of a multi-parameter identity.
This sharpens the folder index's count of monomials into a theorem: the
binomial identity fails at $r=4$ not because it has one term too many but
because every identity of the polynomial kind fails.

**What the target's literature says.** The abc conjecture implies finiteness
at $r=4$: with $a+b=c$ coprime and $4$-powerful,
$\operatorname{rad}(abc)\le(abc)^{1/4}<c^{3/4}$, so, for any fixed
$\eta<1/3$, $c^{(1-3\eta)/4}<\kappa(\eta)$ bounds $c$. This is Theorem 2.1 of
[[../library/diophantine_problems/crowdmath_2020_applications_abc_conjecture_powerful_numbers/_index|the CrowdMath note (2020)]]
(a bibliographic card, statement transcribed there, proof not read here), and
[[../library/diophantine_problems/walsh_2024_question_erdos_powerful_numbers_elliptic_curve/_index|Walsh (2024)]]
makes the same remark; Walsh (2024) is entry [Wa24] of the problem page's
References, cited there for its $r=3$ construction, and the CrowdMath note
is cited in the page's Current assessment for this finiteness. Together with
Theorem 3 the picture at $r=4$ is that of a Fermat-type equation: any
solution is sporadic, and infinitely many would contradict abc.

**Next investigation.** None through this folder's mechanism. An existence
proof at $r=4$ would have to be a non-polynomial construction of a single
solution or a search far beyond $10^{14}$; a finiteness proof would have to
be unconditional where only abc is known. Neither an example nor an infinite
family at $r=4$ can come from a polynomial identity, by Corollary 3.1.

## Problem 939 at r = 5: three summands

**Target.** The same two questions at $r=5$: examples exist (the two recorded
on the problem page, both recomputed there), so the first question is settled
at $r=5$ and the second, at most finitely many, is open; the page records a
forum-reported search finding no further solution with $d<10^{16}$ except
possibly ones in which every pair of summands shares a factor.

**What transports.** Lemma 1 gives the exact bridge. A polynomial identity
$A_1+A_2+A_3=A_4$ in $\mathbb Z[U,V]$ with $r=5$ that satisfies (i)–(iv), the
positivity clause and the nonconstancy of $A_4(U,B)$ would give infinitely
many jointly coprime $5$-powerful triples with $5$-powerful sum and answer
the second question, read with joint coprimality, negatively at $r=5$.
Theorem 3 constrains its shape: the summands cannot include two proportional
polynomials (combining them leaves a three-term identity that still contains
a rational multiple of $A_1=K^5$ beside a rational multiple of the monomial
$A_2$, which are coprime by (iii) and (iv), so its three terms are pairwise
coprime; positivity at an admissible point excludes the merges with a
vanishing coefficient; and Theorem 3 applies after specializing $V$, or $U$
when $a=0$, to a generic complex value, which preserves $5$-powerfulness,
pairwise coprimality and the nonconstancy of the monomial), so all four
terms are genuinely distinct and the four-summand Brownawell–Masser bound
recalled on
[[../library/diophantine_problems/corvaja_zannier_2011_abcd_function_fields/recalled_abc_abcd_bounds|the Corvaja–Zannier page]],
$\max\deg\le3(n_0-1)$, applies; it allows such identities as soon as the
degree is at least $3$, so the polynomial abc inequalities do not exclude
them. Proposition 4 shows that they exist over $\mathbb C$ in the smallest
possible degree, $10$ (degree $5$ would need four fifth powers of linear
forms with zero sum, which the Vandermonde determinant of their roots
excludes except with vanishing subsums), but Corollary 4.1 shows that this
one is not real. The gap is therefore: *does a four-term identity in
$\mathbb Z[U,V]$ satisfying (i)–(iv) with $r=5$ exist?* Lemma 1 does not
need homogeneity; the homogeneous case, a four-term identity of $5$-powerful
binary forms with rational terms, is the case the searches below and the
lead treat.

**Falsification attempts.** Two numerical searches were run while writing
this page; the scripts are retained in the lead folder named below, as
exploratory computations and not as evidence. Every $5$-powerful binary form
of degree $10$ is a constant times the fifth power of a quadratic form, so at
degree $10$ the question is whether $Q_1^5+Q_2^5+Q_3^5+Q_4^5=0$ has a solution
in quadratic forms with no vanishing proper subsum and no common factor,
constants being absorbed into fifth roots over $\mathbb C$ and into signs and
absolute values over $\mathbb R$. Fixing $Q_4$ to a representative of each
orbit of the projective linear group and solving the eleven coefficient
equations by Levenberg–Marquardt from thousands of random starts, the search
over $\mathbb C$ found, besides degenerate limits, one class of nondegenerate
solutions, whose invariants match the family of Proposition 4, and the search
over $\mathbb R$ found only degenerate limits. At degree $15$ the search was
restricted to the shape "fifth power of a cubic" (the shapes $L^6M^9$ and
$L^7M^8$, and identities mixing shapes among the four terms, were not
searched; $L^5M^{10}=(LM^2)^5$ lies inside the searched shape); over both
fields every converged point was a degenerate limit, the nearly exact ones
over $\mathbb C$ being the degree-$10$ family multiplied by a common linear
factor. A separate search for the cyclic shape
$\sum_{k=0}^2(Q\circ M^k)^5=I^5$, with $M(U,V)=(-V,U-V)$ the rational
order-three substitution and $I$ an $M$-invariant form, reproduces the
Proposition 4 family over $\mathbb C$ for quadratics (this substitution is
the diagonal one of the proposition in rational coordinates), finds for
quadratics over $\mathbb R$ only the degenerate case of an invariant $Q$, and
did not converge at all for cubics. A finite search leaves the universal
question open; the reported counts are in the lead.

**What it does not give.** No solution at $r=5$ and no bound on their number.
The two known examples are not values of any identity found here. The
forum-reported search bound is mild evidence against a low-degree rational
identity, since a degree-$10$ identity with small coefficients would place
solutions below $10^{16}$ unless the constants absorbed by $V$ are large.

**Next investigation.** The lead
[[research/leads/quintic_powerful_identity_route/_index|quintic_powerful_identity_route]]
records the route: the exact premise, the transfer, the obstruction shape, and
the bounded searches that would decide the low-degree cases. A rational
identity found by such a search, checked against (i)–(iv) and positivity,
would refute finiteness at $r=5$; a proof that no real four-term identity of
$5$-powerful binary forms exists would close the homogeneous case of the
polynomial route, leaving inhomogeneous identities of the shape (i)–(iv),
which nothing here examines, and constructions of the kind that settled
$r=3$.

## Problem 939, the remaining parts

**The third question ($r=3$).** Resolved in the refereed literature, as the
problem page records. Corollary 3.1 is consistent with how it was resolved:
no polynomial family of coprime $3$-powerful $a+b=c$ exists, and the
constructions of
[[../library/diophantine_problems/nitaj_1995_conjecture_erdos_3_powerful_numbers/_index|Nitaj]],
[[../library/diophantine_problems/cohn_1998_conjecture_erdos_3_powerful_numbers/_index|Cohn]]
and
[[../library/diophantine_problems/walsh_2024_question_erdos_powerful_numbers_elliptic_curve/_index|Walsh]]
are non-polynomial (Walsh's runs through multiples of a point on
$Y^2=X^3-432p^2$, whose heights grow quadratically in the multiplier). The
mechanism of this folder adds nothing at $r=3$.

**The second question at $r\ge6$.** Settled negatively by Theorem 1;
Corollary 1.1 records the size of the family it produces, between
$X^{2/r^2}/\log\log X$ and $X^{2/r^2}$ tuples with sum at most $X$, up to
constants. This is far below the trivial upper bound $X^{(r-2)/r}$ for
$(r-2)$-tuples of $r$-powerful numbers with sum at most $X$; the Problem 940
comparison below records the gap.

## Problem 940: sums of at most r r-powerful numbers

**Target.** [[problems/diophantine_problems/E0940/_index|Problem 940]]: for
$r\ge3$, are there infinitely many integers that are not sums of at most $r$
$r$-powerful numbers, and does the set of such sums have density $0$? Its
Current assessment records the density question as open for every $r$ and
the infinitude question as open for $r\ge5$. At $r=3$ and $r=4$ positive lower
density of the complement, hence infinitude, is accepted on a separate Lean
formalization, in
[[problems/diophantine_problems/E0940/claims/2026_07_26_beyer_de_ryke|Beyer de Ryke's accepted partial claim]]
and the
[[problems/diophantine_problems/E0940/claims/2026_10_28_plasma_ai|accepted quartic claim]]; the prose argument at $r=4$ is the
[[research/erdos_940/quartic_complement|quartic complement argument]].

**Outcome: fails.** The construction produces, for each $r\ge6$, integers
$N=(m^r+B^r)^r$ that are $r$-th powers, hence $r$-powerful, hence trivially
representable with one summand; the identity says that such an $N$ is also a
sum of $r-2$ $r$-powerful numbers, which is a second representation of an
integer that was never a candidate for the complement. Nothing follows for
the complement or for the density of the representable set: the $N$ produced
number $O(X^{1/r})$ below $X$, against the linear mass that a density
statement concerns. The $r=3$ and $r=4$ arguments are unaffected, as the
reconstruction page already records.

**Two comparisons recorded for later use.** First, the folder's
[[research/erdos_940/powerful_subsum_counts|shifted-target bound]] states
that the number of ordered $k$-tuples in $\mathcal P_r^k$ with sum at most
$X$ and $r$-powerful sum is $O(X^{k/r-\delta_r+\varepsilon})$ with
$\delta_r=(r-1)/(r^2(2r+1))$. Corollary 1.1 gives, for $k=r-2$ and $r\ge6$,
the lower bound $X^{2/r^2-o(1)}$ for the same count. At $r=6$ the exponents
are $0.0556$ against $0.6560$; the two bounds are consistent and far apart,
and neither is threatened. Second, the folder's
[[research/erdos_940/linear_collision_families|rank theorem for linear collision identities]]
concerns relations among $r$-th powers of linear forms and shows that a
fixed finite list of identities cannot supply collisions of linear mass. The
binomial identity is not of that shape (its terms are $r$-th powers of
monomials in $U$, $V$ and of the binomials $U^r\pm V^r$), and by the count
above it is even further from linear mass. No route from this folder to
either question of Problem 940 was found, and none is proposed.

## Problem 1107: every large integer as a sum of at most r+1 r-powerful numbers

**Target.** [[problems/diophantine_problems/E1107/_index|Problem 1107]]: for
$r\ge2$, is every sufficiently large integer the sum of at most $r+1$
$r$-powerful numbers? Its page records the status open for every $r\ge3$;
at $r=2$ the question coincides with
[[problems/diophantine_problems/E0941/_index|Problem 941]], whose page records the
problem as solved, and Heath-Brown's 1988 theorem that settles that case is
[[problems/diophantine_problems/E1107/claims/1988_01_01_heath_brown|an accepted partial claim]]
on the Problem 1107 page (the paper is not held here).

**Outcome: fails.** A fixed identity produces sums whose totals are the
values of one polynomial at integer points. In any device of Lemma 1 every
total $A_n(m,B)$ is an $r$-powerful integer, and the $r$-powerful integers
up to $X$ number $O_r(X^{1/r})$, so the totals have density zero for every
$r\ge2$, whatever the degree of $A_n$; for the Theorem 1 total
$(U^r+V^r)^r$ the count is $O(X^{2/r^2})$, since $N\le X$ forces
$m,B\le X^{1/r^2}$. An identity in any number of parameters whose total is
$c\prod_jH_j^{e_j}$ with every $e_j\ge r$, as (i) requires, has totals of
density zero as well: its positive values are $|c|\prod_j|h_j|^{e_j}$ with
nonzero integers $h_j$, and there are $O(X^{1/r}(\log X)^{k-1})$ such
products up to $X$. Without that shape the total is only the sum of its
$r$-powerful summands, and representing a positive proportion of the
integers by it is the Waring-type problem for $r$-powerful numbers itself,
not a consequence of an identity. The mechanism therefore says nothing about
representing all large integers, and no next investigation is proposed.

## Problem 937 and progressions of powerful numbers

**Target.** [[problems/diophantine_problems/E0937/_index|Problem 937]]: are there
infinitely many four-term arithmetic progressions of pairwise coprime
powerful numbers? Its page records the status proved, by the elliptic-curve
construction of
[[../library/diophantine_problems/bajpai_2024_arithmetic_progressions_squarefull_numbers/proposition_5_2|Bajpai–Bennett–Chan, Proposition 5.2]].
The folder index asked whether the monomial device could give progressions of
$r$-powerful numbers for $r\ge3$.

**Outcome: fails, with the obstruction proved.** A three-term progression
$a,b,c$ of $r$-powerful numbers is the equation $a+c=2b$, and $2b$ is
$r$-powerful as a polynomial exactly when $b$ is; so, once $a$, $b$ and $c$
are $r$-powerful as polynomials and $\gcd(a,c)=1$ in $\mathbb Q[t]$, which
the first two steps of the proof of Corollary 3.1 give from the values on
the progression, Theorem 3 applies to the triple $(a,c,2b)$ and excludes
every polynomial family of pairwise coprime three-term progressions, in the
sense of Corollary 3.1, for every $r\ge3$, whatever the shape of the terms.
At $r=2$ the theorem allows three nonconstant terms, and the polynomial
family $X^2+Y^2=2Z^2$ of
[[../library/diophantine_problems/bajpai_2024_arithmetic_progressions_squarefull_numbers/theorem_1_2|Theorem 1.2]]
realizes it; the four-term case needed the elliptic curve. For $r\ge3$ the
non-polynomial constructions are the only ones possible, and
[[../library/diophantine_problems/bajpai_2024_arithmetic_progressions_squarefull_numbers/corollary_1_3|Corollary 1.3]]
of the same paper records that, under abc, the largest length $A^\infty(k)$
for which infinitely many primitive progressions of $k$-powerful numbers
exist is $A^\infty(3)=3$ and $A^\infty(k)=2$ for $k\ge4$: primitive
three-term progressions of $k$-powerful numbers with $k\ge4$ are finite
under abc. The lead named in the folder index is closed in the negative for
the polynomial mechanism; the target itself is settled and needs nothing.

## Other powerful-number problems examined

The search of the problems, research and theory trees for the objects of the
proofs ($r$-powerful numbers, binomial identities among powers, monomial
substitution, valuation arguments for powerfulness and coprimality) surfaced
the following further pages. Each is a resemblance without a transfer, for
the reason given; where Theorem 3 says something exact, it is stated.

- [[problems/diophantine_problems/E0364/_index|Problem 364]],
  [[problems/diophantine_problems/E0365/_index|Problem 365]] and
  [[problems/diophantine_problems/E0366/_index|Problem 366]] (consecutive powerful
  numbers). Theorem 3 with a constant term: an identity $a+1=c$ with $a,c$
  $r$-powerful polynomials has only two nonconstant terms, so it is
  impossible for every $r\ge2$; for Problem 366 the mixed version gives
  $1/2+1/3<1$, impossible as well. No polynomial family of consecutive
  powerful numbers exists, consistent with the Pell-equation families of
  Problem 365 growing exponentially. The problems ask for specific pairs and
  triples, which polynomial identities cannot supply.
- [[problems/diophantine_problems/E0938/_index|Problem 938]] (three-term
  progressions of consecutive terms of the powerful sequence). The
  consecutiveness is a gap condition on the sequence; identities produce
  progressions of squares, not gaps.
- [[problems/diophantine_problems/E0943/_index|Problem 943]] (the number of
  representations of $n$ as a sum of two powerful numbers is $n^{o(1)}$). At
  $r=2$ the binomial identity is the Pythagorean parametrization
  $(m^2+B^2)^2=(m^2-B^2)^2+(2mB)^2$, which gives representations of squares
  as sums of two squares, of divisor-function size; it neither strengthens
  nor threatens the conjectured bound.
- [[problems/diophantine_problems/E1081/_index|Problem 1081]] (counting sums of two
  squarefull numbers; disproved) and
  [[problems/diophantine_problems/E0941/_index|Problem 941]] (sums of three powerful
  numbers; proved): settled targets on which one-parameter families have no
  bearing.
- [[problems/diophantine_problems/E0942/_index|Problem 942]] (powerful numbers
  between consecutive squares), [[problems/diophantine_problems/E0935/_index|Problem 935]],
  [[problems/arithmetic_functions/E0367/_index|Problem 367]] and
  [[problems/diophantine_problems/E0137/_index|Problem 137]] (powerful parts of
  products of consecutive integers),
  [[problems/diophantine_problems/E0936/_index|Problem 936]] ($2^n\pm1$ and
  $n!\pm1$ powerful) and [[problems/factorials_binomials/E1108/_index|Problem 1108]]
  (sums of distinct factorials that are powerful): short intervals,
  consecutive products, and special sequences, none of which an identity
  among $r$-powerful values addresses.

## Leads created

One connection amounts to a route someone could take up now:
[[research/leads/quintic_powerful_identity_route/_index|quintic_powerful_identity_route]]
records the conditional deduction at $r=5$, its premise (a rational four-term
identity of $5$-powerful binary forms with the shape Lemma 1 needs), the
proved transfer, the shape constraints from Theorem 3 and the polynomial abc
bounds, the complex identity of Proposition 4 with its non-reality, and the
bounded searches with their counts. The $r=4$ obstruction is not a lead: it
closes the polynomial route rather than opening one. The Problem 940 and 1107
comparisons and the progression obstruction are recorded above and need no
folder.

## Sources read for this page

Beyond the folder's index and reconstruction page and the four problem pages
named in the index, this page read the problem pages listed in the previous
section; the Problem 940 research pages on the finite-core reduction, the
powerful-subsum counts and the linear collision families; the source pages
of Bajpai–Bennett–Chan's Theorems 1.1 and 1.2 and Corollary 1.3; the
Corvaja–Zannier page recalling the Mason–Stothers and Brownawell–Masser
bounds; the CrowdMath, Cushing–Pascoe, Nitaj, Cohn and Walsh cards; and the
Conjectures.io card. No page outside the repository was read. The numerical
searches were run with the scripts retained in the lead folder; their
outcomes are reported there with the numbers of starts.
