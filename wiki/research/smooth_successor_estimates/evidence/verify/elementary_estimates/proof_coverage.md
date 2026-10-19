---
name: research/smooth_successor_estimates/evidence/verify/elementary_estimates/proof_coverage
title: "Proof coverage and consumer interfaces"
desc: Clause-by-clause examination of the block sieve, Section 2 tools, Type I application, and all consumer interfaces of the frozen elementary premise.
created: 2026-10-16T04:10:53Z
updated: 2026-10-16T04:16:14Z
---

# Proof coverage and consumer interfaces

***

This is part of the [examination report](report.md), dated 2026-10-15.
Line locators refer to the [retained frozen excerpts](subject_map.md),
not to later versions of their native pages. The three longest independent
rederivations are in [weak steps](weak_steps.md). The source methods are
OpenAI's; the reconstruction being examined and its uniformity accounting
are Plasma AI's.

## E1: statement defect and the entire operative proof

The unrestricted statement in block_sieve.md 19–53 has the following
counterexample. Choose the prime set empty, $z=1/2$,
$\eta_0=1/2$, $C=1$, and one object with weight 1.
There are no bad events. The only squarefree product is $d=1$;
set $g(1)=1$, $X=0$, and $r(1)=1$.
Every required intersection count is $Xg(1)+r(1)=1$.
All prime-density and block-sum conditions are vacuous.
Avoidance has weight $\mathcal S=1$, and $G=1$.
For every positive even $h$, including every possible $h\ge h_0$,

$$
 c_1e^{-h}XG+\sum_{d\le z^{4h+2}}|r(d)|=0.
$$

The displayed estimate would say $1\le0$. Its fixed-$h=2$
upper bound fails for the same reason. The polynomial clause also
fails: a polynomial in no indicators is a constant, but its constant
monomial has $d_\emptyset=1>z^{4h+1}$, so the stated support
condition forces $U=0$, incompatible with $U\ge1$.
This is an exact witness, requiring no machine computation.

Neither the supplied source's conventions nor Lemma 2.9 explicitly
imposes a lower bound on $z$. If the usual sieve convention $z\ge2$
is intended, the witness is outside that convention. The distinction
is material to the literal statement and immaterial to the five
applications, whose cutoffs all tend to infinity. The report does
not silently add that convention to the frozen statement.

Here is the deduction-by-deduction examination for $z\ge1$, the entire
range needed by every consumer. At $z=1$ the prime set is empty,
the constant polynomials $U=V=1$ are supported at $d=1$, and
the conclusion follows from the $r(1)$ term. For $z>1$:

1. The alternating-binomial identity follows by applying Pascal's
   relation to adjacent partial sums. If the truncation index exceeds
   the available number of conditions, the binomial coefficient is
   zero. At $t=0$ the partial sum is 1, as required.
2. In block $j$, the even truncation $h_j=(j+1)h$ gives
   $U_j\ge I_j\ge0$. Its error is
   $\binom{t-1}{h_j}\le\binom t{h_j+1}=E_j$ for $t\ge1$;
   both sides of the error comparison vanish for $t=0$.
3. Product telescoping is valid with arbitrary dependent bad events.
   Nonnegativity permits replacement of each trailing $I_k$ by
   $U_k$, giving $0\le U-I\le\sum_jE_j\prod_{k\ne j}U_k$.
   Thus $V=U-\sum_jE_j\prod_{k\ne j}U_k\le I\le U$.
4. There is at most one way to obtain a given monomial in $U$.
   A correction monomial has degree exactly $h_j+1$ in one block
   and degree at most $h_k$ in all others. Correction supports
   are mutually disjoint and disjoint from $U$'s support.
   Hence $U,V,U-V$ all have coefficients in $\{-1,0,1\}$.
   Pointwise nonnegativity of $U-V$ follows from its expression
   as a sum of products of nonnegative functions, not from the signs
   of its expanded coefficients.
5. Since $\sum_{j\ge0}(j+1)2^{-j}=4$, a monomial in $U$
   has product at most $z^{4h}$. A correction adds at most one
   prime of size $z$, so $z^{4h+1}$ suffices.
   The stated remainder cutoff $z^{4h+2}$ is therefore valid
   for $z\ge1$.
6. Independent Bernoulli events with probabilities $g(p)$ are
   introduced only to evaluate a polynomial's prescribed main term.
   This does not assume independence of the actual objects.
   Their block avoidance probability $a_j$ is at least
   $\exp(-C/\eta_0)$, and
   $e_j\le C^{h_j+1}/(h_j+1)!$.
7. For $n\ge e^2C$, $C^n/n!\le e^{-n}$.
   Consequently
   $R_h=\sum e_j/a_j\le2e^{C/\eta_0-1}e^{-h}$
   for all sufficiently large even $h$, irrespective of the
   number of nonempty blocks. Increase $h_0$ until $R_h\le1$.
   The upper expectation differs from $G$ by at most
   $(e^{R_h}-1)G\le eR_hG$.
   Since $V\le I$, its deficit from $G$ is at most
   $\mathbb E(U-V)\le R_he^{R_h}G$.
   These prove the advertised $c_1=2e^{C/\eta_0}$ bound.
8. At $h=2$ the relevant factorial indices are $3,5,\ldots$.
   Their sum is bounded by $\sinh C$, so
   $R_2\le e^{C/\eta_0}\sinh C$.
   The stated upper constant
   $c_2=\exp(e^{C/\eta_0}\sinh C)$ follows. It is large,
   but finite and independent of every later extraction parameter.
9. Evaluation in the actual weighted population gives
   $X\mathbb EP+\sum c_Sr(d_S)$ for either polynomial.
   Each integer product identifies its squarefree set uniquely,
   and $|c_S|\le1$ gives the exact unit-coefficient remainder
   sum. This also covers $X=0$; no division by $X$ occurs.

The $h$-uniform bound has therefore been checked for arbitrarily
many blocks and growing $h$, not inferred from a finite trial.

### All five sieve instances

| Instance | Local density, error, and level | Interface finding |
| --- | --- | --- |
| Ordinary cells and reduced residue classes | $g(p)=1/p$, omit $p\mid r$; CRT remainder at most 1 for every real subinterval; $X=\vertJ\vert/r$; $\eta_0=1/2$; $h=2\lceil T^2\rceil$; $D_W=\exp(O(\sqrt L T^2))$ | All $r\le L^B<W$ fit, including nonsquarefree moduli. The product converts the main term to $\vertJ\vertV(W)/\varphi(r)$. Short intervals require only absolute errors. |
| Composite subtraction for a fixed prime $p$ | $p>x^\gamma>W$; $X=X_A/(p-1)$, $g(l)=1/(l-1)$ for odd $l\le W$; $r_{\rm sieve}(d)=r(pd)$ | $\varphi(pd)=(p-1)\varphi(d)$. Every $pd\le x^{1/2-\kappa+o(1)}<x^{1/2-\kappa/2}$. Distinct $(p,d)$ give distinct products because $p$ is the unique prime factor above $W$. No unaccounted multiplicity is paid when summing Type I errors. |
| Preliminary sieve | Odd primes up to $x^{b_1}$, $g(p)=1/(p-1)$; $X=X_A$; $h=2\lfloor1/(40b_1)\rfloor$ | $h\ge h_0$ requires sufficiently small $b_1$, as the consumers say. The level exponent is at most $1/5+2b_1$, below $1/2-\kappa/2$ for the stated small choices. The relative error is at most $c_1e^2e^{-1/(20b_1)}$. |
| Ordinary rough integers in $(x,2x]$ | $g(p)=1/p$, $X=x$, remainder at most 1; same $b_1,h$ | Total error $O(x^{1/5+2b_1})=o(x/L)$ for sufficiently small $b_1$. This is the ordinary upper count used in E3, not a distribution statement for the weighted candidate. |
| Balanced lattice box | $g(l)=\nu(l)/l^2\le(3l-2)/l^2\le7/9$, $l\ge3$; $\eta_0=2/9$; block mass at most $3\sum1/l$; $h=2$, $D=x^{10\theta}$ | The fixed-$h$ constant is independent of mask, assignment, $\kappa,b_1,j_{**},S$. The actual lattice remainder and its summed size are checked below. |

For $g(p)=1/(p-1)$ on odd primes, the block-mass bound follows
from that for $1/p$, plus the convergent sum of
$1/[p(p-1)]$; its constants are absolute.

## E2, E3, and E4: remaining clauses and source scope

The [three independent derivations](weak_steps.md) supply the main
analytic details. The following records clauses which might otherwise
be hidden by a successful final substitution.

| Subject passage | Checked deduction and boundary |
| --- | --- |
| proxy_discrepancy.md 19–84 | The full-cell definition is used before restriction. Positivity is eventual for each fixed $S$; coefficient bound 1 is exact and independent of $S$. The range contains both unbalanced cofactor dyads and balanced prime dyads with exponent slack. The proposition's $S\ge2B+2$ is stronger than the source's requested $S>2B+3$, and the extra factor $L$ for a whole ambient interval is explicitly paid. |
| proxy_discrepancy.md 91–110, 166–193 | All harmonic character parameters and both endpoints are uniform. The class-count loss and the twist loss are included. Nondecreasing lists include repeated primes; only prefixes with a nonempty terminal interval need be counted. Source Corollary 2.4 also allows $c>1$, where the interval is eventually empty, and an upper exponent smaller than 1, covered by enlarging it to 1. |
| proxy_discrepancy.md 195–244 | The residue-class sieve is an absolute-error assertion on every subinterval. Its main term cancels for all nonprincipal characters, without primitivity. The cell count $L^{S+1}$ is retained in the $D_W$ error. Each fixed $B,S$ is absorbed by a later threshold. |
| proxy_densities.md 24–53 | The $1/l!$ normalization and coordinate measure are consistent. Only finitely many terms occur on a fixed compact domain. Continuity includes higher-factor thresholds and does not assert a density at $w=\gamma$. The unused Buchstab identification follows from the defining delay equation as checked in the keeper. |
| proxy_densities.md 57–146 | $A=S+2$ in PNT gives relative error $O(L^{-1})$ on the short cells. Prime-square loss, ordered lists, the terminal interval, reciprocal-prime cube errors, and both hyperplane strips all have the stated scope. Uniformity is over fixed positive-distance compact sets, not over $b$ or $\varepsilon$ tending to zero with $x$. |
| proxy_densities.md 148–173 | The stated prime-cofactor condition implies the needed compact range. The proof uses only the size of that factor, so it also supplies source (7.17) for a nonprime factor in the same exponent bin. The reconstruction states a narrower application, but no additional prime-specific inference obstructs the source's size-only formulation. |
| proxy_densities.md 177–252 | The minimum-coordinate identity retains $l/l!$. The lower count weights each integer by at most one, even with repetitions. Its limit inferior, the sieve limit superior, and the Mertens limit give the upper bound for the fixed number $D_{b_1}(1)$, with absolute $b_0,c'$. |
| proxy_densities.md 257–282 | The mesh is fixed in $b_1,\kappa$ before $S,x$; its error is weighted by $d\alpha/\alpha$. The preliminary-minus-composite consequence keeps $b_1^{-1}e^{-1/(20b_1)}$, and needs $b_1$ sufficiently small, not merely $b_1<1/10$. |
| candidate_mass.md 19–37 | Bands and groups at the same and adjacent scales are disjoint because $c_2<c_3<c_4<2c_1$. Each type of group occurs at $(1/10)\log_2 L+O(1)$ scales; its harmonic mass is $\log(6/5)+O(L^{-1/10})$. Band masses have uniform error $O(T^{-1})$, enough for two-sided powers of $L$. |
| candidate_mass.md 63–96 | Fixing the exceptional divisor leaves at most $r_0!$ permutations per band and at most $(r_0-1)!$ in its own band. Divisor count bounds $a_Q$. For $q=1/2$, $t2^{1-t}\le1$ for integer $t\ge1$, bounding each marked group factor by $1/V_g$. An exceptional divisor is supported on primes above $W$; for $u\le2x$ that part has $O(\sqrt L)$ prime factors with multiplicity and at most $2^{O(\sqrt L)}$ divisors. These give both pointwise bounds. |
| candidate_mass.md 93–137 | Every prime of a supported $u$ is at least $L^{20}$ and at most $x^\delta$ eventually. Exceptional integers may have prime divisors outside every band; only their size and roughness are used. Harmonic factorization, group derivative products, tilted tails, and the fixed-index threshold are checked in the keeper. |
| candidate_mass.md 139–208 | Upper and lower local mass comparisons have constants depending only on early geometry and $\Psi$. The finite prefix contains no exceptional slot. The micro-band mass ratio cancels that slot, and $C_A=1+C_Q$ is independent of its later fixed position. No claim is made uniformly for positions growing with $x$. |

## E5: every derived Section 2 tool

The harmonic character estimate is proved in the first keeper. It uses
the stated Siegel–Walfisz theorem, without a primitive-character
restriction. The block sieve is examined above.

For fixed $k\ge0$, the tail
$\sum_{a\ge2}(a+1)^kp^{-a}$ is at most $c_kp^{-2}$
uniformly for primes $p\ge2$, by comparison with the convergent
series at $p=2$. Positivity and unique factorization therefore give,
for $Y\ge1$,

$$
 \sum_{n\le Y}\frac{\tau(n)^k}{n}
 \le\prod_{p\le Y}\left(1+\frac{2^k}{p}+\frac{c_k}{p^2}\right)
 \ll_k(\log(2Y))^{2^k}.
$$

Multiplication by $Y$ bounds the ordinary sum. This works for
real $k\ge0$, so includes the integer-$k$ source lemma.
For the mixed shifted sums, Cauchy–Schwarz uses the second moments
of $\tau(u),\tau(2u-1)$, and the second and sixth moments in
$\tau(v)\tau(v+1)^3$. Each shifted variable ranges in a set of
distinct integers of size $O(x)$; extending to all integers up to
that size is a positive upper bound.

A convolution of $b$ fixed factors of logarithmically bounded
coefficients is bounded pointwise by $L^C\tau(n)^{b-1}$:
choose the first $b-1$ divisors, which determine the last factor.
Its square sum on a dyad is $UL^{O(1)}$, and a reciprocal product
index changes this to $L^{O(1)}/U$. This checks the source
Lemma 2.5 consequence as well as the explicitly consumed bounds.
In the Type II endpoint use, $\tau(z_*)^4\le\tau(z)^4$;
the varying group-free part cannot defeat the ordinary moment bound.

For Fourier separation, choose the coordinate with largest
frequency and integrate by parts $j$ times in it. Along with the
zero-frequency bound this gives
$|\widehat F(\xi)|\ll_j L^{C(j+1)}(1+|\xi|)^{-j}$.
With $j=b+1$, integration gives mass $O(L^{C(b+2)})$.
Outside a ball of radius $L^{2C}$, the $j$-derivative estimate
gives tail

$$
 O_j(L^{-Cj+C(2b+1)}).
$$

Choose $j\ge2b+1+A/C$. Thus the frequency exponent $2C$
precedes the desired accuracy $A$. A coordinate box truncation
has no larger outside region than a comparable ball, so the
source's coordinatewise statement follows with fixed constants.
Fourier inversion separates the variables. Mellin inversion for
fixed $\Psi$ follows by applying this to the smooth compactly
supported function $\Psi\circ\exp$; its integrated absolute
cost is constant. Finite sums permit all these integral exchanges.

The earlier Type II slot split has $N_s=O(T)$ factors, so it
must not be treated as an application of the fixed-dimensional
lemma with a growing dimension. Instead separate each fixed
one-variable transition function individually. If $C_F$ bounds
their Fourier masses, the sum over the $2^{N_s}$ patterns has
mass at most $(2C_F)^{N_s}=L^{O(1)}$. The complement of the
frequency box $|\xi_i|\le L$ is a union of $N_s$ one-coordinate
tails. For every fixed $M$, its mass is at most
$2^{N_s}N_sC_MC_F^{N_s-1}L^{-M}$, a fixed logarithmic power
times $L^{-M}$. Selecting $M$ after that power gives any
required saving. Also $\sum_i1/s_{j(i)}\ll1/T$, by summing
the geometric scales up to the final scale $\asymp T$.
The retained slot twists are therefore $O(L/T)$.
The mixed divisor bound already proved controls the total
absolute error before the target accuracy is selected. Thus the
growing number of slots introduces no unproved dimension-uniform
version of Fourier separation. The later three-variable cutoff
does satisfy the fixed-dimensional hypothesis directly.

The squarefree reciprocal-$\varphi$ sum satisfies

$$
 \sum_{d\le y}\frac{\mu^2(d)}{\varphi(d)}
 \le\prod_{p\le y}\left(1+\frac1{p-1}\right)
 =V(y)^{-1}\ll\log(2y)
 \quad(y\ge1).
$$

For the balanced remainders,
$3^{\omega(n)}\le d_3(n)$ follows at each prime power from
$\binom{a+2}{2}\ge3$ for $a\ge1$. Counting triples and
summing two harmonic series yields
$\sum_{n\le D}3^{\omega(n)}\le D(1+\log D)^2$.
If $\nu(d)\le d3^{\omega(d)}$, then
$\sum_{d\le D}\nu(d)/d\le D(1+\log D)^2$ and
$\sum_{d\le D}\nu(d)\le D^2(1+\log D)^2$.
The reconstruction's weaker common formulation of these two bounds
is therefore valid.

Source Lemmas 2.6 and 2.7 and Corollary 2.10 are present in the
delivered source excerpt but not consumed by E or by the supplied
conditional Type II derivation. Their validity is not used here
as a way of certifying P. Basic Fourier decay, character
orthogonality, CRT, and elementary integral manipulations are
the explicit boundaries of the derived tools.

## E5: the Type I application, including all conductor losses

Fix $\vartheta<1/2$ and $D>0$. The interesting range is
$\vartheta>0$; otherwise the positive-integer modulus sum is
empty or contains only $d=1$, whose remainder is zero.
Extract the first pure slot of band 0. Its leftover coefficient
$b(r)$ is nonnegative and at most $L^{c_b}\tau(r)$:
the same exceptional-divisor and band-permutation argument used
for $a_Q$ applies after removing one labelled slot. The normalization
in band 0 remains $1/r_0!$, so removing that slot cannot increase
the permutation bound. Its prime is group-free and
$W_1(pr)=W_1(r)$.

Contributing dyads have $PU\asymp x$ and
$x^{a_0}\ll P,U\ll x^{1-a_0}$, $a_0=c_1s'>0$.
Indeed $p\in[x^{c_1s'},x^{c_2s'}]$, $c_2s'<1/4$,
and $r\asymp x/p$. Fix $c'$ bounding both the first
and second moments of $b$ before selecting any accuracy.

For odd squarefree $d$, the progression $2u-1\equiv0\bmod d$
is a unit class. A nonprincipal character has primitive conductor
$f>1$, with $d=hf$, $(h,f)=1$, and
$\varphi(d)=\varphi(h)\varphi(f)$. Its values are those of
the primitive character together with $(p,h)=(r,h)=1$.
This decomposition is unique. It requires retaining squarefreeness
of $h$ when estimating its harmonic mass.

For $R/2<f\le R$, the inequality
$1/\varphi(f)\le(2/R)f/\varphi(f)$, Cauchy–Schwarz,
and the multiplicative large sieve give, for every Mellin twist,

$$
 \sum_{R/2<f\le R}\frac1{\varphi(f)}
 \sum_{\chi\bmod f}^{*}|A_\chi B_\chi|
 \ll\frac{L^{c'/2}}R
       \sqrt{(P+1+R^2)(U+1+R^2)PU}.
$$

The prime square sum is $O(P)$, without needing a prime-density
gain, and the other is $UL^{c'}$.
The coprimality masks only reduce these square sums. Expanding the
square-root bound and using $PU\asymp x$ yields

$$
 xL^{c'/2}
 \left(R^{-1}+P^{-1/2}+U^{-1/2}+R/\sqrt x\right).
$$

One may drop squarefreeness of $f$ and $(f,h)=1$, since this
is a positive upper bound. Summing at most $O(L)$ conductor
dyads, $O(L^2)$ factor dyads, and squarefree $h$ with total
weight $O(L)$, then integrating the fixed Mellin transform,
gives

$$
 O\left(xL^{c'/2+4}
   (L^{-C'}+x^{-a_0/2}+x^{\vartheta-1/2})\right).
$$

Choose $C'\ge D+c'/2+4$. The latter two terms save every
fixed logarithmic power for the fixed positive gaps involved.

For $f\le L^{C'}$, apply Siegel–Walfisz to the prime sum
before Mellin separation. The logarithms of its endpoints are
comparable to $L$. Modulus exponent $2C'+1$ and accuracy
$K+C'+2$ give a nonprincipal prime sum $O_K(yL^{-K})$
after the loss from summing the $O(L^{C'})$ residue classes.
The cutoff $\Psi(yr/x)$, including its band and dyad endpoints,
has bounded total variation, uniformly on a contributing dyad.
Partial summation therefore gives $O_K(PL^{-K})$ per $r$.

The primes in this interval dividing $h\le x^\vartheta$ are
at most $\vartheta/a_0+1$. Removing them costs
$O(x^{1-a_0}L^{c'})$ per dyad before summing moduli.
The number of characters for each $f$ is at most
$\varphi(f)$, cancelled by its reciprocal weight. The sums
over $f,h$, and dyads give the complete bound

$$
 O\left(xL^{c'+C'+3-K}
       +x^{1-a_0}L^{c'+C'+3}\right).
$$

Choosing $K\ge D+c'+C'+3$ finishes the nonprincipal part.
A factor 2 in the conductor cutoff, as in the consumer's dyadic
notation, changes only a constant and not the choice order.

The principal term has a different, positive error. Every prime
dividing a supported $u\le2x$ is at least $L^{20}$, and their
number is $O(L/\log L)$. Breaking a squarefree modulus sharing
such a prime with $u$ into $ld'$, and overcounting if it shares
several primes, gives

$$
 \sum_{\substack{d\le x^\vartheta\\(d,u)>1}}
       \frac{\mu^2(d)}{\varphi(d)}
 \le\left(\sum_{l\mid u}\frac1{l-1}\right)
       \sum_{d'\le x}\frac{\mu^2(d')}{\varphi(d')}
 \ll L^{-18}.
$$

Multiplication by the nonnegative candidate weights proves the
$X_AL^{-18}$ error. Together these computations establish the
stated Type I bound with the order
$c'$, then $D$, then $C'$, then $K$.
No proxy precision is involved. Constants or eventual thresholds
may depend on fixed $\vartheta$; no uniform threshold as
$\vartheta\uparrow1/2$ is needed or claimed.

## Balanced-box application and the full choice order

This check concerns the actual consumers of E1, E3, E4, and E5.
It does not use or verify the truth of P.

The assignment retaining every micro-band entry and one mark from
each P-group has $D_1\le x^{1/20}$. The Q contribution is
at most $x^{1/25}$; the $O(T)$ marks contribute
$\exp(O(TL^{2/5}))=x^{o(1)}$. The harmonic sum of each
normalized mark is 1, so
$\sum\lambda/D_1=H_Q^{\rm mic}$ and
$\sum\lambda\le x^{1/20}H_Q^{\rm mic}$.
The exceptional integer is retained whole; its factors are not
mistakenly treated as belonging to prime bands.

Expanding the marked weight gives exactly one mark from each
group. Independent permissions with probability $q$ for the
remaining P-primes reproduce $q^{\omega(u)-s}$, because
$\omega$ counts distinct primes. The normalized number of
omitted pure-band lists for a fixed residual product is
$\prod1/a_p!\le1$. Dropping those restrictions gives the
stated pointwise majorant. This is an exact expectation of a
nonnegative majorant, not an averaging heuristic about primes.

For $D_1\mid u$ and $mn=2u-1$, one has
$mn\equiv-1\bmod D_1$. Even when $D_1$ has prime powers,
there are exactly $\varphi(D_1)$ pairs of unit residue classes.
At an odd sieve prime $l\nmid D_1$, $mn=0$ has $2l-1$
pairs and $mn=-1$ has $l-1$, and these sets are disjoint.
CRT thus gives $\varphi(D_1)\nu(d)$ pairs modulo $D_1d$.
The count per pair of residue classes has error
$O(1+(M_1+M_2)/(D_1d))$.
Using the E5 divisor sums yields total error

$$
 O\left(((M_1+M_2)D+D_1D^2)(1+\log D)^2\right),
 \qquad D=x^{10\theta}\le x^{1/20}.
$$

Dropping the parity of the actual odd $m,n$ only enlarges
the box count. The omission of the prime 2 changes Euler-product
comparisons by a fixed factor.

For a banned prime below $W$, the avoidance factor is
$(1-1/l)(1-2/l)$; above $W$ it is
$1-1/l+1/l^2$. Compare these with
$(1-1/l)^{1+2\mathbf1_{l\le W}}$, paying a convergent
$1+O(l^{-2})$ factor where needed.
An allowed P-prime has factor $(1-1/l)^2$ and needs one
compensating inverse factor. Primes removed because they divide
$D_1$ need at most three. Their compensation is bounded,
since each is at least $L^{20}$ and $D_1\le x^{1/20}$.
The mask expectation of the remaining compensation is at most
$\prod_{p\text{ P-prime}}(1+q/(p-1))\le H_P$.

Summing main terms gives
$O(xV(W)^2V(x^\theta)H_Q^{\rm mic}H_P)$.
E4, with constants independent of $j_{**}$, and
$V(x^\theta)\ll_\theta1/L$, make this
$O(X_AV(W)^2)$. Balanced dyads satisfy
$M_i\ll x^{0.54}$, uniformly for $0<\kappa<1/50$.
Summing their lattice errors over assignments gives at most
$x^{0.64}L^{O(1)}H_Q^{\rm mic}$.
Compared to $X_AV(W)^2\gg xH_QH_P/L^2$, this tends to
zero using $H_Q^{\rm mic}\ll H_Q$ and $H_P\ge1$.

There are $O(\kappa L+1)$ possible dyads for one balanced
factor, and $O(1)$ for the other once its partner and product
scale are fixed. The two prime proxies contribute at most
$9/(L^2V(W)^2)$. Hence the balanced removal is
$C_{\rm bal}(\kappa+L^{-1})X_A/L+o(X_A/L)$,
with a constant depending only on the early geometry,
$j',\theta,\Psi$, and the E4 comparison constants.
No later $\kappa,b_1,j_{**},S$ enters that constant.

The full order is therefore consistent: early geometry and
prefix; $j',\theta,j_0$; then $\kappa$ using this constant;
then sufficiently small $b_1$, $b_*=b_1/3$, fixed $j_{**}$,
and a fixed mesh; then Type II saving and its internal
$K_0,D_0,B$; then $S>2B+3$ and PNT accuracies; then $x$.
The Type I accuracy $D>C_A+10$, its conductor split, and
its SW accuracy can be fixed after the early exponent $C_A$
is known and before taking $x$ large. They do not constrain $S$.

The conditional prime mass and conversion to a distinct-prime
count use positivity, $X_A\gg xL^{-C_A}$, the pointwise
$\exp(C_w\sqrt L)$ bound, and injectivity of $u\mapsto2u-1$.
The prime-factor bound transfers to $p+1=2u$ for large $x$.
The resulting lower bound exceeds $x^{1-\eta}$ for any fixed
$\eta>0$, since $\eta L$ dominates both $\log L$
and $\sqrt L$. These are valid consequences if the stated
Type II hypothesis P and the consumer derivations hold. They
are not unconditional consequences of examining E.
