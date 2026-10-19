---
name: research/erdos_25/independent/bounded_quotient_blocks_and_recentering
title: "Erdős Problem 25: established results and remaining gap"
desc: Unverified independent input; checked additions and superseded targets are recorded in the topical notes.
tags: []
sources: []
created: 2026-09-22T07:11:39Z
updated: 2026-10-13T05:28:09Z
---

# Erdős Problem 25: established results and remaining gap

***

**Status of this investigation: unresolved.** This document does not claim a proof or counterexample to the unrestricted problem. All constructions below respect one residue per distinct modulus and activation at the modulus. The supplied sources have not been edited.

For a set S of positive integers write

$$
 d(S)=\lim_{X\to\infty}\frac{|S\cap[1,X]|}{X},\qquad
 \operatorname{ld}(S)=\lim_{X\to\infty}\frac1{\log X}
       \sum_{n\le X,\ n\in S}\frac1n,
$$

when the limits exist. Upper and lower densities are the corresponding limsup and liminf; natural and logarithmic densities must not be interchanged. Put H_X=\sum_{n\le X}1/n.

## 1. Finite approximation and positive cases

Normalize 0<=a_i<n_i and put B_i={a_i+t n_i:t>=1}. This is exactly the exclusion in the problem, including a_i=0 and n=n_i. Let A_k=N\setminus\bigcup_{i<=k}B_i. Above n_k it is periodic modulo lcm(n_1,...,n_k). Its natural and logarithmic densities agree, say δ_k, and δ_k decreases to δ. Consequently

$$
 \overline{\operatorname{ld}}(A)\le\delta.
$$

There is no established reverse inequality here in full generality.

If \sum_i1/n_i<\infty, then, for every X,

$$
 |(A_k\setminus A)\cap[1,X]|
 \le\sum_{i>k}|B_i\cap[1,X]|
 \le X\sum_{i>k}\frac1{n_i}.
$$

The last bound uses the activation condition: there are at most floor(X/n_i) eligible points of the i-th class. Therefore the natural density of A exists and is δ. If the moduli are pairwise coprime and the reciprocal sum diverges, CRT gives δ_k=\prod_{i<=k}(1-1/n_i) tending to zero, so A has natural density zero. These results also appear in Chojecki, `source.md`, Theorems 3.1 and 3.2; the direct proof above avoids any unjustified countable subadditivity of upper density.

## 2. Finite periodic compression

Let D be a finite set of moduli, let U=\bigcup_{q\in D}(a_q+qZ), and let M_D=\bigcup_{q\in D}qZ. Their periodic natural densities satisfy

$$
 d(M_D)\le d(U).                                      \tag{2.1}
$$

Proof: work in Z/LZ, L=lcm(D), with its uniform measure. CRT decomposes this group into prime-power coordinates. Fix one coordinate p^v and all the others. The relevant sections of the congruence classes are p-adic balls, and the measure of their union is at least the largest individual ball measure. Replacing every p-coordinate residue by zero makes these balls nested, so the union has exactly that largest measure. This simultaneous replacement cannot increase the union measure. Repeat over all prime coordinates. The final family consists of the zero classes, proving (2.1).

The statement is attributed to Rogers in the checked Introduction of Filaseta--Ford--Konyagin--Pomerance--Yu, `source.md`, paragraph beginning “Similar to the definition of δ^-(S)”. The proof above is self-contained.

## 3. Exact harmonic inequality for sets of multiples

For every finite D and every X>=1,

$$
 \sum_{n\le X,\ n\in M_D}\frac1n\le d(M_D)H_X.        \tag{3.1}
$$

Here and below M_D on positive integers means its positive part. To prove (3.1), first discard q>X; this leaves the left side unchanged and can only decrease the density on the right. Let P be the primes at most X, and let independent V_p have probabilities

$$
 \mathbb P(V_p=e)=(1-1/p)p^{-e}\quad(e=0,1,\ldots).
$$

For Z=\prod_{p\in P}p^{V_p} and Π=\prod_{p\in P}(1-1/p)^{-1}, one has P(Z=n)=1/(Π n) on the P-smooth positive integers. The event Z\in M_D is increasing in every V_p; the event Z<=X is decreasing. The elementary product correlation inequality therefore gives

$$
 \mathbb P(Z\in M_D\mid Z\le X)\le\mathbb P(Z\in M_D).
$$

For completeness, positive correlation of two increasing functions of one variable follows by taking independent copies V,V' and observing that

$$
 2\operatorname{Cov}(f(V),g(V))
 =\mathbb E[(f(V)-f(V'))(g(V)-g(V'))]\ge0.
$$

Induction on the number of independent coordinates proves the product assertion, since conditional expectations preserve monotonicity. Apply it to the increasing indicators of M_D and of Z>X. Truncation of the geometric variables followed by convergence justifies the argument for their unbounded supports.

The conditional law given Z<=X assigns probability 1/(nH_X) to each 1<=n<=X. Also P(Z\in M_D)=d(M_D): the independent geometric prime valuations have exactly the distributions of divisibility valuations under uniform measure modulo L. These observations prove (3.1).

This immediately gives the Davenport--Erdős logarithmic-density result for arbitrary sets of multiples. If D is infinite and Δ is the increasing limit of finite-union densities, apply (3.1) to D\cap[1,X] to obtain H_{M_D}(X)<=ΔH_X. Every fixed finite union gives the opposite asymptotic lower bound. Thus ld(M_D)=Δ. This argument is supplied here, rather than assuming that the source's multiplicative argument extends to translated classes; it does not.

## 4. An exact obstruction to bounded-quotient counterexample blocks

Let D\subset[1,X] be finite and have distinct moduli, with one class per modulus. Put ε=d(U). Since each q\in D itself belongs to M_D, (2.1) and (3.1) imply the sharper bound

$$
 \boxed{\quad\sum_{q\in D}\frac1q\le\varepsilon H_X.\quad} \tag{4.1}
$$

For K>=1 define

$$
 E_K(X)=\{n\le X:\text{some }q\in D\text{ satisfies }
          q\le n\le Kq,\ n\equiv a_q\pmod q\}.
$$

Writing n=tq+a_q with t>=1, each q contributes at most one point for each t<=floor(K), of weight at most 1/(tq). Hence

$$
 \boxed{\quad
 \sum_{n\in E_K(X)}\frac1n
 \le H_{\lfloor K\rfloor}\varepsilon H_X.
 \quad}                                               \tag{4.2}
$$

For fixed K, vanishing total periodic footprint therefore forces vanishing normalized harmonic deletion through such bounded-quotient endpoints. This applies to an entire finite collection of scales at once, so overlapping the completed footprints does not evade it.

In particular, Wang's supplied multi-residue block, all of whose deleted endpoints satisfy q<n<=2q, cannot be converted to a singleton block with both vanishing total footprint and a fixed positive proportion of harmonic deletion. This is a structural obstruction, not just a loss in one attempted matching. Wang `source.md`, Section 3, assigns q_{K(m)} to many different endpoints m; those endpoints are distinct residues of the same modulus. The proof therefore does not satisfy the present problem's singleton condition.

## 5. What remains

Neither (4.1) nor (4.2) controls hits with unbounded n/q. Moreover, in an infinite system the relevant small quantity is the additional periodic footprint outside a fixed initial union, not necessarily the footprint of the whole tail. Restricting to residue classes of a fixed initial period creates quotient-modulus multiplicities and period-dependent constants; no uniform estimate overcoming this problem has been proved here.

One tempting sufficient assertion is

$$
 \sum_{n\le X,\ n\in\bigcup_{q\in D}\{n\ge q:
                                  n\equiv a_q\pmod q\}}
 \frac1n\le d(U)H_X                                  \tag{5.1}
$$

for arbitrary finite singleton families. If (5.1) were true, finite approximation would settle the full problem immediately. It is **not proved** in this investigation. The weaker Dirichlet-series analog is likewise unproved.

Simple recentering does not prove (5.1). For D={2,3,5}, residues (0,0,2), and X=18, the translated delayed union loses 5 and gains 7 and 17 relative to the zero-residue union. Both periodic densities equal 11/15, but the harmonic prefix increases by

$$
 \frac17+\frac1{17}-\frac15=\frac1{595}>0.
$$

Thus one cannot transfer (3.1) by asserting that recentering maximizes harmonic prefixes. A similar failure for asymptotic harmonic constants is proved in `../notes/translated_phase.md`.

**Unresolved requirement:** prove a uniform control of the full activated, unshadowed tail sufficient for logarithmic convergence, or construct distinct singleton classes whose unbounded-quotient/conditioned transients produce two separated logarithmic subsequential limits. Neither has been accomplished here.

## 6. A second exact failure of recentering: harmonic constants

This calculation rules out a stronger approach even after averaging to infinity. Compare the zero residues for D={2,3,35} with residues (0,0,2). Both completed unions have density

$$
 \Delta=1-\frac12\frac23\frac{34}{35}=\frac{71}{105}.
$$

The latter residues even have a common CRT phase, namely 72 modulo 210. After removing the multiples of 2 and 3, the new forbidden points from modulus 35 are respectively

$$
 E_0=\{210k+35,\ 210k+175:k\ge0\},\qquad
 E_2=\{210k+37,\ 210k+107:k\ge0\}.
$$

These formulas include the activation at 35. The difference of their asymptotic harmonic constants is the convergent series

$$
 \sum_{k\ge0}\left(
 \frac1{210k+37}+\frac1{210k+107}
 -\frac1{210k+35}-\frac1{210k+175}\right)>0.            \tag{6.1}
$$

To verify the sign, put x=210k. The summand is

$$
 \frac{68}{(x+107)(x+175)}-
 \frac2{(x+35)(x+37)}.
$$

After multiplying by positive denominators, positivity reduces to

$$
 33x^2+2166x+25305>0.
$$

The decay is O((k+1)^{-2}), proving convergence. Thus zero residues need not maximize asymptotic harmonic constants, normalized Dirichlet mass for s sufficiently close to 1, or the Dirichlet defect relative to density. In particular, neither a global recentering comparison nor a ratio comparison to the all-zero system is valid.

For reference, a finite delayed union B with completed period L, completed forbidden residues R\subset{1,...,L}, and finite activation-omission set D_0 satisfies

$$
 \sum_{n\le X,\ n\in B}\frac1n=\Delta\log X+C_B+o(1),
$$

where

$$
 C_B=-\frac1L\sum_{r\in R}
            \left(\log L+\psi(r/L)\right)
       -\sum_{n\in D_0}\frac1n,
 \qquad\Delta=|R|/L.                                  \tag{6.2}
$$

Here ψ is the logarithmic derivative of Γ. Formula (6.2) follows directly from the reciprocal-sum identity for one arithmetic progression. It also gives the constant term at s=1 of \sum_{n\in B}n^{-s}. Consequently C_B>Δγ would refute the raw proposed Dirichlet inequality near 1. No such example was found, and there is no proof here that one cannot exist.

Illustrative, uncertified decimal evaluations for (6.1) give an increase about 0.0032843906741, with constants about -0.0458709419036 and -0.0425865512295. These numerical values are not needed for the exact sign proof and do not contradict the comparison with Δγ.

## 7. Why a local large-quotient estimate is insufficient

One attempted next step was a uniform bound of the form

$$
 \frac{|U\cap[X,2X]|}{X}
 \le f(d(U))+\epsilon(K),\qquad
 f(t)\to0\ (t\to0),\quad\epsilon(K)\to0\ (K\to\infty), \tag{7.1}
$$

for finite singleton families whose largest modulus is at most X/K. Such a statement would make the unbounded-quotient remainder much easier. It is false already for zero residues.

Here is the precise obstruction. Fix K>=2. Choose finitely many primes P_K, all at least 2K, such that

$$
 \prod_{p\in P_K}(1-1/p)\le\frac12,
$$

and let T_K be at least their maximum. Existence uses the elementary divergence of the reciprocal-prime sum; an elementary proof is to note that convergence would bound every finite Euler product, whereas the product over p<=Y is at least \sum_{n<=Y}1/n. Set

$$
 D_N=[N,NT_K/K]\cap\mathbb N,
 \qquad X=NT_K.
$$

For this fixed K and T_K, there are arbitrarily large dyadic N for which the density of M(D_N) is arbitrarily small. Indeed, D_N is contained in a fixed number of consecutive dyadic divisor windows. Besicovitch's checked source, §5 Theorem 1, gives e_1+...+e_l=o(l) for their densities e_i. The sum over any fixed number of consecutive windows therefore has arbitrarily small values at arbitrarily large starting indices.

If n\in[X,2X] is divisible by p\in P_K, then

$$
 N\le n/p\le NT_K/K,
$$

so n\in M(D_N). The union of the finitely many prime-multiple classes has density at least 1/2; hence for all sufficiently large N it occupies at least X/3 points of [X,2X]. On the other hand, max D_N<=X/K and the completed density d(M(D_N)) can be arbitrarily small. Choosing N after K and then letting K tend to infinity disproves (7.1). Every modulus is distinct, every residue is zero, and activation holds throughout the tested interval.

This is not a counterexample to logarithmic-density existence: each such finite system is periodic, and the diagonal construction here establishes only the failure of the asserted *uniform local estimate*. A successful argument must retain multiscale logarithmic information.

## 8. Other proof ideas pursued and their specific obstructions

### 8.1 Wang's labels and attempts to split repeated moduli

In Wang's Section 3, at scale Q=2^j the number of prime coordinates is k=O(sqrt(j)). Moduli q_S~Q are indexed by central subsets S, so there are at most 2^k distinct moduli. A positive fraction of Q endpoints m use q_{K(m)}. Because their interval has diameter smaller than q_S, distinct endpoints assigned to a given q_S are distinct residue classes, not repeated points of one singleton class.

Keeping one endpoint per modulus leaves at most exp(O(sqrt(log Q))) endpoints of size about Q, losing the required local harmonic deletion. Providing many moduli with the same large-prime divisibility pattern also fails at the level of capacity: requiring all p in S to divide q gives availability roughly Q/\prod_{p\in S}p, far smaller than the Q2^{-k} endpoint demand for Wang's large primes. More decisively, the proved bound (4.2) rules out *any* singleton, bounded-quotient, vanishing-total-footprint version of the desired logarithmic hump, not just this particular matching.

A speculative replacement uses labels with probabilities 1/p rather than 1/2, to match the small-prime divisibility distribution of moduli. This avoids the immediate pattern-capacity mismatch but supplies only multiplication-table-type compression. No estimates were established that create a logarithmically long deletion epoch with vanishing total footprint. These label-matching considerations are heuristics, not a constructed system.

Splitting each repeated modulus q into distinct multiples qr preserves containment of each new class in the old class, but activation then requires n>=qr. At Wang's endpoints n~q, only bounded multipliers are available. Moving or dilating endpoints to make room loses the original dense transient interval. No valid infinite conversion was obtained.

### 8.2 Translated divisor windows and common profinite phases

One can take a finite divisor-window union and translate all its classes by a common CRT phase. Its periodic density is unchanged, while its finite harmonic prefixes can change, as Sections 5 and 6 explicitly show. The hoped-for construction was a phase making a small-density divisor union unusually dense throughout an interval [N,N^C] of positive logarithmic width. No such construction was found.

Besicovitch's sparse windows produce large natural-density excursions near their own scale, but Davenport--Erdős forbids obtaining a logarithmic counterexample from zero classes. Translating a dense finite window a very large distance does not automatically solve this: the moduli must remain at most every point being removed, and a short additive interval at a huge location has too little harmonic mass. Common-phase optimization at bounded periods did not resolve this obstacle.

### 8.3 The first-kill/tower reduction

For the exact first-kill partition

$$
 E_i=A_{i-1}\cap B_i,
 \qquad e_i=d(E_i)=\delta_{i-1}-\delta_i,
$$

one has \sum_i e_i=1-δ. For an earlier compatible class with modulus n_j, restriction to n=a_i+n_it gives a forbidden quotient class modulo

$$
 q_{ij}=\frac{n_j}{\gcd(n_i,n_j)}.
$$

Thus E_i is a translate-dilate of a finite quotient sieve S_i of density d_i=n_i e_i. These statements are exact: n>=n_i implies that all earlier congruences are already active.

Chojecki's checked Conjecture 5.1 asks for a uniform harmonic estimate of the form

$$
 \sum_{t\le Y,\ t\in S_i}\frac1{t+a_i/n_i}
 =d_i\log Y+O\!\left(d_i\log\frac2{d_i}+\tau_i\right),
 \qquad
 \sum_{n_i\le X}\frac{\tau_i}{n_i}=o(\log X).          \tag{8.1}
$$

The entropy part can indeed be summed: with \sum e_i<=1 and distinct n_i,

$$
 \sum_{n_i\le X}e_i\log\frac1{n_i e_i}
 \le O(1)+\log\!\left(\sum_{n_i\le X}\frac1{n_i}\right)
 =O(\log\log X).
$$

This follows from nonnegativity of relative entropy, or the log-sum inequality. The missing global estimate is precisely the bound for the τ_i term, not the entropy calculation.

The source's tower, with moduli u2^{r-j}3^j for 0<=j<=r and (u,6)=1, has top first-kill set

$$
 E=\{u3^r(1+2^r t):t\ge0\},\qquad
 e=\frac1{u6^r}.
$$

Its first point contributes 1/(u3^r), much larger than the corresponding entropy scale. Consequently a term-by-term entropy bound without an additional charge is false. Replicating towers, sharing preparatory classes, and replacing prime-power factors by different prime factors were considered. The obstacles were sparse top moduli, conflicts between the residues needed by shared preparatory moduli, and concentration of candidate endpoints in rare old-period fibers. No global charge estimate or synchronized counterexample was obtained.

A finite-period conditioning argument gives estimates with constants depending on the old period L. Such constants cannot simply be allowed to grow with the truncation level: δ_k-δ may tend to zero too slowly relative to L_k. This is an unresolved gap, not a proved tail-control principle.

### 8.4 Dirichlet domination and an auxiliary stopped-coordinate model

A sufficient finite assertion, weaker than (5.1), is

$$
 \frac1{\zeta(s)}\sum_{n\in B}n^{-s}\le d(U)
 \quad(s>1),                                         \tag{8.2}
$$

where B is the delayed finite union. It remains unproved and unrefuted here. If it held, applying it to increasing finite families and using monotone convergence would give the Dirichlet-density limit for the infinite union; a suitable logarithmic Tauberian step would then be needed to conclude the logarithmic-density limit. This was a proposed route, not a completed argument.

An auxiliary finite expression does have a monotonicity proof:

$$
 P_C(s)=\sum_{\substack{\varnothing\ne J\subseteq C\\J\text{ compatible}}}
      (-1)^{|J|+1}\operatorname{lcm}(q_j:j\in J)^{-s}
 \le P_C(1)=d(U).
$$

For each prime independently, take a uniform infinite p-adic digit sequence and retain it only to a random depth whose tail is p^{-e(s-1)} at depth e. A class modulo p^e is hit only if those e digits match and the depth is at least e. Compatible intersections then have probability lcm^{-s}. Increasing s only suppresses hits, proving the inequality by inclusion--exclusion. However, the *actual* delayed Dirichlet mass is not bounded by ζ(s)P_C(s): the coherent example in Section 6 disproves that stronger assertion near s=1. Thus this model does not establish (8.2).

The smooth reciprocal probability measure on an initial segment of primes was another possible comparison device. An unproved domination of its probability of B by d(U) would yield at most a bound of the form H_B(X)<=C d(U)log X using the usual Euler-product upper bound. This is **not** by itself the exact harmonic inequality (5.1), and the necessary conditioned-tail passage was not established. An earlier auxiliary note suggested a stronger implication; it should not be relied on.

### 8.5 A further proved positive regime

If all classes admit nonnegative representatives from one fixed finite set {0,...,R}, logarithmic density exists and equals the limiting finite-prefix density. For q>R the delayed class with representative r is exactly r+qN. For each fixed r, apply Davenport--Erdős to the multiples of its assigned moduli. Its complement relative to a finite initial union has logarithmic density tending to zero as the union increases. Translation by fixed r preserves logarithmic density (the reciprocal-weight change is summable and the cutoff discrepancy is bounded). A finite union of these tails therefore has upper logarithmic density tending to zero. The finitely many q<=R do not affect this approximation argument. This does not apply to arbitrary varying representatives.

### 8.6 A further positive regime: bounded residue orders

Suppose that there is a fixed positive integer M such that

$$
 q\mid M a_q\quad\text{for every chosen modulus }q.    \tag{8.3}
$$

Equivalently, all orders q/gcd(q,a_q) divide a fixed M; this holds if those orders are uniformly bounded. Then the logarithmic density exists and equals the limiting finite-prefix density.

Here is a proof of the general stability statement used. Let S_M={k>=1:k≡1 mod M}, and suppose E satisfies n∈E, k∈S_M ⇒ nk∈E. Let D be the semigroup supported on the finitely many primes dividing M. Write each integer uniquely as n=du with d∈D and gcd(u,M)=1. For each d and invertible residue r modulo M, set

$$
 T_{d,r}=\{u\ge1:u\equiv r\pmod M,\ du\in E\},
 \qquad W_{d,r}=\bigcup_{v\in T_{d,r}}v\mathbb N.
$$

Then T_{d,r}=W_{d,r}∩{u:u≡r mod M}. Indeed, if u=vk and both u and v are congruent to the invertible residue r, then k≡1 mod M, so stability applies. The multiples theorem proved in Section 3 approximates W_{d,r}, in upper logarithmic density, by the multiples of a finite subset G⊂T_{d,r}. Intersecting with the residue class cannot enlarge the error, and

$$
 \left(\bigcup_{v\in G}v\mathbb N\right)
       \cap\{u:u\equiv r\pmod M\}
 =\bigcup_{v\in G}vS_M.
$$

Dilation by fixed d multiplies upper logarithmic density by 1/d. Thus every fixed stratum is approximated by finitely many rays (dv)S_M. The unretained strata with d>Y have harmonic mass at most

$$
 H_X\sum_{\substack{d\in D\\d>Y}}\frac1d,
$$

whose normalized upper limit tends to zero as Y→∞ because

$$
 \sum_{d\in D}\frac1d
 =\prod_{p\mid M}(1-1/p)^{-1}<\infty.
$$

There are finitely many remaining strata. Consequently E is approximated in upper logarithmic density by finite unions of rays nS_M contained in E. Those finite unions are eventually periodic, so E has logarithmic density. For M=1, this is just the usual multiples theorem, using the single stratum d=1.

Under (8.3), if n≥q and n≡a_q mod q, then for k≡1 mod M,

$$
 kn\equiv ka_q\equiv a_q\pmod q,\qquad kn\ge q.
$$

Every individual delayed forbidden class, and hence their union B, has this stability. Each finite approximating ray nS_M remains within the original class witnessing n∈B. Therefore some finite original prefix contains any chosen finite ray approximation. The original finite prefixes thus approximate B in upper logarithmic density, proving the stated value as well as existence. No distinctness relaxation is used to construct a counterexample; this is only a positive subcase. The detailed parallel record is `notes/multiplicative_stability.md`.

## 9. Computational work and its limitations

Exploratory searches evaluated finite periodic systems via exact periods and numerical Hurwitz-zeta or digamma evaluations. Families included small consecutive moduli, divisor families of periods such as 4320 and 360360, and coherent phase families with bounded periods. Some searches used random residues or coordinate ascent. They did not find a violation of the raw inequality (8.2) or (5.1) in their tested families. These were bounded, mostly floating-point experiments, not certified exhaustive evidence for the unrestricted assertions. Their negative results are not used in any proof above.

The useful concrete outputs were the exact counterexamples to stronger recentering assertions in Sections 5 and 6. The exploratory coherent-phase script is retained at `notes/phase_constant_search.py`; no computation is needed to verify those two examples.

## 10. Source use, records, and final uncertainty

The original problem page and all supplied source files were left unchanged. No internet research was used. Relevant passages checked in full local Markdown were:

- Chojecki: finite densities, summable and coprime cases, first-kill quotient representation, conditional reduction, and tower obstruction.
- Wang: periodic recovery and Sections 3--4 of the multi-residue construction, including the repeated use of q_{K(m)} and the gliding-hump activation checks. Its conclusion is not a singleton solution.
- Davenport--Erdős 1936 and 1951: the divisibility-upward-closure and smooth-prime mechanisms; these do not extend merely by replacing zero residues by arbitrary translates.
- Besicovitch: §5, the averaged dyadic divisor-window density theorem used in Section 7. Natural-density failure is not logarithmic-density failure.
- Filaseta--Ford--Konyagin--Pomerance--Yu: the Introduction's Rogers density-minimization statement. The required compression argument is also proved directly in Section 2.

Additional notes containing earlier speculative formulations, superseded by the qualifications above, are not retained. This document is the consolidated independent record.

The unrestricted Erdős Problem 25 has **not** been resolved in this investigation. The strongest general proved bounds here are (2.1), (3.1) for zero residues, and (4.1)--(4.2) for arbitrary finite singleton families. The open task is still a rigorous uniform treatment of unbounded-quotient, unshadowed delayed tails, or an explicit distinct-modulus construction producing separated upper and lower logarithmic densities. No candidate infinite construction in these notes has been promoted to a counterexample.
