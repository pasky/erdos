---
name: research/erdos_25/independent/profinite_shifts_and_long_windows
title: Independent investigation of Erdős Problem 25
desc: Unverified independent input; checked additions and superseded targets are recorded in the topical notes.
tags: []
sources: []
created: 2026-09-22T11:42:07Z
updated: 2026-10-13T05:28:09Z
---

# Independent investigation of Erdős Problem 25

***

## 1. Status and scope

**The general problem was not resolved in this investigation.** No rigorous counterexample satisfying distinct moduli and singleton residue classes was obtained, and no proof of logarithmic-density existence in full generality was obtained. Research stopped at the user's instruction. This record separates established arguments, calculations, failed mechanisms, and unproved possibilities.

Only the problem and source files supplied in this research folder were used. The supplied problem page and sources were not edited. Auxiliary records are linked below; this file contains the main mathematical content needed to understand the investigation independently.

The exact problem is the following. Given strictly increasing positive integers $q_1<q_2<\cdots$, and one class $a_i\pmod{q_i}$ per modulus, set
$$
 B_i=\{n\in\mathbb N:n\ge q_i,\ n\equiv a_i\pmod{q_i}\},
 \qquad B=\bigcup_iB_i,\qquad A=\mathbb N\setminus B.
$$
Canonical representatives will always satisfy $0\le a_i<q_i$. Consequently
$$
 B_i=\{a_i+tq_i:t=1,2,\ldots\},
$$
including the case $a_i=0$. The missing point $a_i<q_i$ cannot be silently restored.

For $S\subseteq\mathbb N$, write
$$
 H_S(X)=\sum_{n\le X,\ n\in S}\frac1n,
 \qquad L_S(X)=\frac{H_S(X)}{\log X}.
$$
Natural density concerns $\#(S\cap[1,X])/X$. Lower and upper logarithmic densities are $\liminf L_S(X)$ and $\limsup L_S(X)$; logarithmic density means their equality. Natural density implies logarithmic density with the same value, but the converse is false. Throughout, the density of a finite periodic union means its natural density, equivalently its uniform measure on a common finite period.

## 2. Finite truncations and positive cases

Let
$$
 A^{(k)}=\mathbb N\setminus\bigcup_{i\le k}B_i,
 \qquad U_k=\bigcup_{i\le k}(a_i+q_i\mathbb Z).
$$
Above $q_k$, the set $A^{(k)}$ is periodic modulo $\operatorname{lcm}(q_1,\ldots,q_k)$. Its natural and logarithmic densities therefore agree; denote their value by $\delta_k=1-d(U_k)$. The sequence decreases to a limit $\delta\in[0,1]$.

Since $A\subseteq A^{(k)}$,
$$
 \overline d(A)\le\delta,
 \qquad \overline{\operatorname{ld}}(A)\le\delta.                 \tag{2.1}
$$
Thus $\delta=0$ already implies natural and logarithmic density zero. In general (2.1) supplies no matching lower bound. Even equality of an existing logarithmic density with $\delta$ would need proof.

### 2.1 Summable reciprocal moduli

Activation gives the useful exact bound
$$
 \#(B_i\cap[1,X])\le\lfloor X/q_i\rfloor.
$$
Hence, if $\sum_i1/q_i<\infty$,
$$
 \frac1X\#((A^{(k)}\setminus A)\cap[1,X])
 \le\sum_{i>k}\frac1{q_i}.
$$
Taking lower and upper natural densities and then $k\to\infty$ proves
$$
 d(A)=\delta.
$$
This also proves logarithmic-density existence. The infinite union bound is justified by the finite counting bound, not by a generally invalid countable subadditivity assertion for upper density.

### 2.2 Pairwise-coprime moduli

CRT gives
$$
 \delta_k=\prod_{i\le k}(1-1/q_i).
$$
If the reciprocal sum converges, use the preceding argument. If it diverges, the product tends to zero and (2.1) gives natural density zero. Modulus 1 is the immediate trivial case.

These statements and their hypotheses were checked against the full Chojecki source, Sections 2–3. That source does not claim the general result.

### 2.3 Zero residues

For a set of moduli $D$, put
$$
 M(D)=\bigcup_{q\in D}q\mathbb N.
$$
The Davenport–Erdős theorem gives
$$
 \operatorname{ld}(M(D))
 =\lim_{Q\to\infty}d\bigl(M(D\cap[1,Q])\bigr).                 \tag{2.2}
$$
It does not assert natural-density existence. Its statement and finite-density identification were checked in the supplied 1951 source, pp. 1–5, and in Section 2 of the 1936 source. The lower natural density assertion for the removed set must not be mistaken for a natural-density assertion; some OCR displays in the older source omit lower-limit notation.

Section 3.2 below also records an elementary finite harmonic inequality from which (2.2) follows.

### 2.4 Finitely many fixed integer representatives

A further positive case established here is:

> If a fixed finite set $T\subset\mathbb Z$ contains an integer representative of every selected class, then $A$ has logarithmic density $\delta$.

Choose one $t_i\in T$ for each class, and partition the distinct moduli into $D_t=\{q_i:t_i=t\}$. Set
$$
 V_t=(t+M(D_t))\cap\mathbb N,
 \qquad B_t=\bigcup_{q\in D_t}\{n\ge q:n\equiv t\pmod q\}.
$$
For $t\ge0$, $B_t\triangle V_t$ is finite. For $t<0$, activation can omit infinitely many first points $q+t$. They must not be dismissed as a finite boundary correction.

Let $P_t$ consist of the divisibility-minimal members of $D_t$. It is a primitive set. If $q\in D_t\setminus P_t$, $q>2|t|$, and $d\in D_t$ is a proper divisor of $q$, then
$$
 d\le q/2<q+t,
 \qquad q+t\equiv t\pmod d.
$$
The first point omitted by modulus $q$ is therefore already removed by an eligible modulus $d$. Thus
$$
 B_t\triangle V_t\subseteq(t+P_t)\cup F_t                       \tag{2.3}
$$
for some finite $F_t$.

Every primitive set $P$ has upper logarithmic density zero. Indeed,
$$
 P\setminus[1,Q]\subseteq M(P)\setminus M(P\cap[1,Q]),
$$
and (2.2) makes the logarithmic density of the set on the right tend to zero. Fixed integer translations change harmonic sums by $O_t(1)$, so (2.3) has upper logarithmic density zero.

Finally, each $V_t$ is logarithmically approximable by finite translated multiples unions: by (2.2),
$$
 \operatorname{ld}\bigl(M(D_t)\setminus M(D_t\cap[1,Q])\bigr)
 \longrightarrow0.
$$
Translation preserves this assertion; a finite union over $t\in T$ preserves the approximation. Each finite approximant is eventually periodic and differs only finitely from the corresponding delayed finite union. This proves the stated value $\delta$. Natural density is not asserted.

The full details were recorded in a companion note that is not retained. A claim in an earlier auxiliary note that every fixed integer shift has only a finite activation correction was corrected: for negative shifts the correction can be infinite, though logarithmically negligible as above.

## 3. Compression and harmonic support estimates

### 3.1 Finite coset compression

For a finite singleton family with modulus set $D$, write
$$
 U=\bigcup_{q\in D}(a_q+q\mathbb Z).
$$
Then
$$
 d(U)\ge d\left(\bigcup_{q\in D}q\mathbb Z\right).               \tag{3.1}
$$

**Proof.** Put $L=\operatorname{lcm}(D)$, and decompose $\mathbb Z/L\mathbb Z$ into its prime-power CRT coordinates. In a fixed prime coordinate, each class contributes a congruence ball. Fix all the other coordinates. Among the balls present in that fiber, the original union has size at least that of its largest ball. Replacing every ball in this coordinate by the zero-centered ball of the same size makes the balls nested, so the new union has exactly the largest size. Thus this operation cannot increase measure. Repeat over the primes dividing $L$. The final family is the zero-class family. $\square$

This statement also holds for a family with repeated moduli, but collapsing repeated zero classes loses their multiplicity. That distinction matters in all support-counting applications.

The supplied Filaseta–Ford–Konyagin–Pomerance–Yu source, Section 1, attributes this minimal-union fact to Rogers. The proof just given is self-contained.

### 3.2 A coefficient-one harmonic bound for sets of multiples

For finite $D\subseteq[1,X]$, let $\rho=d(M(D))$, and $H_X=\sum_{n\le X}1/n$. Then
$$
 H_{M(D)}(X)\le\rho H_X,
 \qquad \sum_{q\in D}\frac1q\le\rho H_X\le d(U)H_X.             \tag{3.2}
$$

Here is a proof not requiring a quantitative Mertens estimate. For the finitely many primes $p\le X$, take independent geometric exponents
$$
 \mathbb P(V_p=k)=(1-1/p)p^{-k},\qquad k\ge0,
 \qquad N=\prod_{p\le X}p^{V_p}.
$$
The event $E=\{N\in M(D)\}$ is increasing in the exponents; $F=\{N\le X\}$ is decreasing. Product-measure positive association therefore gives
$$
 \mathbb P(E\cap F)\le\mathbb P(E)\mathbb P(F).
$$
For completeness, association for increasing functions follows by induction on the number of independent coordinates: in one coordinate, use
$2\operatorname{Cov}(f(V),g(V))=\mathbb E[(f(V)-f(V'))(g(V)-g(V'))]\ge0$; condition on the last coordinate and apply this identity together with the induction hypothesis. Apply it to $1_E$ and $-1_F$ for the displayed inequality.

The distribution of divisibility by members of $D$ is the same as for a uniform residue modulo $L=\operatorname{lcm}(D)$, so $\mathbb P(E)=\rho$. Conditional on $N\le X$, the mass of $n\le X$ is exactly $1/(nH_X)$. This proves the first inequality of (3.2); the others follow from $D\subseteq M(D)$ and (3.1).

Applying the first inequality to $D\cap[1,X]$, then using finite periodic lower bounds, also proves (2.2). Earlier notes used the weaker estimate
$$
 \sum_{q\in D}\frac1q\le
 \left(\prod_{p\le X}(1-1/p)^{-1}\right)d(U)
 \ll d(U)\log(2X),                                             \tag{3.3}
$$
obtained by summing over all $X$-smooth multiples. This is the smooth-number mechanism checked in Davenport–Erdős (1951), equations (7), (11), and (12). Inequality (3.2) supersedes that constant in this finite support application.

### 3.3 What bounded quotient points permit

For a fixed integer $K\ge1$, the harmonic mass of deleted points with a witnessing representation $n=a_q+tq$, $1\le t\le K$, is at most
$$
 \sum_{q\in D}\sum_{t=1}^K\frac1{a_q+tq}
 \le H_K\sum_{q\in D}\frac1q
 \le H_K d(U)H_X,                                              \tag{3.4}
$$
when all relevant $q\le X$. Overcounting is harmless. This gives a useful uniform statement for small activation quotients. It leaves $t\to\infty$ uncontrolled; summing (3.4) over an unbounded quotient range loses a logarithmic factor.

It does not control a *conditioned* tail: most of a late class may already belong to an earlier periodic union, so its new periodic contribution can be much smaller than the full class density.

## 4. Why the direct Wang adaptation fails

The supplied Wang paper concerns multiple residue classes per modulus. Its Section 3 was checked against the full source. At scale $Q=2^j$, it constructs $\gg Q$ endpoints $m\asymp Q$, assigns moduli $q_m\asymp Q$ with $q_m<m$, and has a completed periodic footprint at most $e^{-c\sqrt j}$. However,
$$
 q_m=q_{K(m)},
$$
so only $2^{O(\sqrt j)}$ different moduli are available. Many distinct endpoint residues use the same modulus. Sorting the moduli does not fix this violation of the singleton hypothesis.

Its Section 4 recovery-and-epoch argument is valid as a general assembly mechanism: finite families recover their periodic logarithmic density; future moduli can be placed above a chosen cutoff; sufficiently many deletion blocks force low averages. The missing component for the present problem is a legal singleton deletion construction.

### 4.1 A rigorous obstruction to summable-footprint first-period blocks

Suppose finite singleton blocks have disjoint modulus sets $D_j$, full periodic unions $U_j$, and
$$
 \sum_jd(U_j)<\infty.
$$
Assign each selected endpoint to an eligible modulus $q\le n$, and suppose each modulus receives at most a fixed $K$ selected endpoints. Then the endpoint union has logarithmic density zero.

For every $J$, finite compression and the union bound give
$$
 d\bigl(M(F)\bigr)\le\sum_{j\ge J}d(U_j)
$$
for every finite $F\subseteq\bigcup_{j\ge J}D_j$. Davenport–Erdős therefore implies
$$
 \overline{\operatorname{ld}}\left(\bigcup_{j\ge J}D_j\right)
 \le\operatorname{ld}\left(M\left(\bigcup_{j\ge J}D_j\right)\right)
 \le\sum_{j\ge J}d(U_j).
$$
The finitely many earlier moduli do not affect logarithmic density. Letting $J\to\infty$ shows that the entire modulus set has logarithmic density zero. Eligibility then gives
$$
 \sum_{n\le X,\ n\text{ selected}}\frac1n
 \le K\sum_{q\le X,\ q\in\cup_jD_j}\frac1q=o(\log X).
$$
In particular, a literal singleton version of Wang's summably small, fixed-ratio blocks is impossible. This is a mathematical obstruction, not merely a defect of one proposed conversion.

### 4.2 Refining repeated classes into larger moduli

Containment $[b]_d\subseteq[a]_q$ forces $q\mid d$. If both the original modulus and the permitted endpoint scale are $\asymp Q$, each original $q$ has only boundedly many available multiples $d$. Wang's $2^{O(\sqrt{\log Q})}$ original moduli can then produce only that order of magnitude of new eligible singleton moduli, not $\gg Q$.

Allowing large multipliers gives more choices but moves activation beyond the original endpoints. Uniformly scaling endpoints retains only a vanishing harmonic mass if the scaling factor must tend to infinity. No refinement preserving the required deletion mass was obtained.

### 4.3 An independent second-moment restriction

For distinct $q\in[Q,2Q]$, let $F=\sum_q1_{[a_q]_q}$ on a common period. Then
$$
 \int F^2\le\sum_{q,r}\frac{(q,r)}{qr}
 =\sum_{d\le2Q}\varphi(d)
   \left(\sum_{\substack{Q\le q\le2Q\\d\mid q}}\frac1q\right)^2
 \le9(1+\log(2Q)).                                            \tag{4.1}
$$
For the last bound, the inner sum is at most $1/d+1/Q\le3/d$, and $\varphi(d)\le d$.

If such a family deletes at least $cQ$ points in $[Q,2Q]$, at least $cQ/2$ classes are needed, so $\int F\ge c/4$. Cauchy–Schwarz and (4.1) give
$$
 d(U)\ge\frac{c^2}{144(1+\log(2Q))}.                            \tag{4.2}
$$
Thus even an individual comparable-scale singleton block cannot retain Wang's exponentially-in-$\sqrt{\log Q}$ small footprint. This does not rule out a different singleton counterexample.

The details were recorded in companion notes that are not retained.

## 5. Compatible profinite shifts and a proved long-window obstruction

Another attempted construction imposed $a_q\equiv\alpha\pmod q$ for one profinite integer $\alpha$. Every finite completed union is then an integer translate of a multiples union, so its periodic footprint is known exactly. This is more general than one fixed ordinary integer representative.

The hope was to translate a low-footprint window $q\in[Q,2Q]$ so that it deletes a positive proportion over a logarithmically long range $[Q,Q^{1+c}]$. A single interval of width $O(Q)$ contributes only $O(1)$ harmonic mass and cannot itself give a fixed normalized logarithmic spike.

The proposed amplification is ruled out by the following proved estimate:

> For fixed $\varepsilon>0$, uniformly in $\alpha$ and in intervals $I$ of $X\ge Q^{1+\varepsilon}$ consecutive integers,
> $$
> \#\{n\in I:\exists q\in[Q,2Q],\ n\equiv\alpha\pmod q\}
> \ll_\varepsilon X/\log\log Q.                               \tag{5.1}
> $$

Here is the proof mechanism, including the uniform errors. For arbitrary prescribed residues at primes $p\le z$, the count
$K(t)=\sum_{p\in\mathcal P}1_{t\equiv r_p\ (p)}$, with mean parameter $L_{\mathcal P}=\sum_{p\in\mathcal P}1/p$, satisfies on any interval of $T$ consecutive integers
$$
 \sum(K(t)-L_{\mathcal P})^2\ll T L_{\mathcal P}+z^2.            \tag{5.2}
$$
This follows by counting single and double congruences by CRT, each with error at most one.

Take $z=Q^{\min(\varepsilon,1)/10}$ and $L=\sum_{p\le z}1/p\asymp_\varepsilon\log\log Q$. By (5.2), all but $O(Q/L)$ moduli $q\in[Q,2Q]$ have $\omega_z(q)\ge0.9L$. Their exceptional contribution to $I$ is $O(X/L)$.

For any $q\in[Q,2Q]$,
$$
 \sum_{p\le z,\ p\mid q}\frac1p=O(\log\log\log Q)=o(L),
$$
by splitting at $\log Q$. Along a nonexceptional progression $n=a_q+qt$, the primes dividing $q$ already force at least $0.9L$ matches to $\alpha$. The remaining primes impose one residue each on $t$, with mean at least $0.9L$. Except for
$$
 O(T_q/L+z^2/L^2),\qquad T_q\le X/q+1,
$$
points on this progression, they supply at least another $0.8L$ matches. Such points have $K(n)\ge1.7L$. Globally (5.2) says that the set where $K(n)\ge1.5L$ has size $O(X/L)$. Summing the progression exceptions costs
$$
 O(X/L+Qz^2/L^2)=O(X/L),
$$
because $Qz^2=o(X)$. This proves (5.1).

Splitting the harmonic sum at $Q^{1+\varepsilon}$, the initial active part contributes at most $\varepsilon\log Q+O(1)$; subsequent dyadic intervals use (5.1). Consequently
$$
 \lim_{Q\to\infty}\sup_\alpha\sup_{x\ge Q}
 \frac1{\log x}\sum_{\substack{n\le x\\n\ge q,\ n\equiv\alpha\ (q)\text{ for some }q\in[Q,2Q]}}\frac1n=0. \tag{5.3}
$$
This remains valid for any subset of the window. It does not permit summing an unbounded number of windows without a new argument.

The full proof was recorded in a companion note that is not retained, together with elementary derivations of the prime estimates it uses.

### Further window calculations, with review status

Two additional auxiliary proofs were written and locally checked by their author but were not given a separate full independent audit; neither is retained:

* The first companion note obtains a bound $X(\log Q)^{-\delta_*+o(1)}$, where
  $$
  \delta_*=1-\frac{1+\log\log2}{\log2}=0.086071\ldots.
  $$
  The calculation splits at a prime-count threshold $bL$. The upper-tail exponent is $I_1(b)=b\log b-b+1$; a truncated generating-function calculation for covered low-count points gives $I_2(b)=2-b+b\log(b/2)$. They balance at $b=1/\log2$. Brun expansions of degree $20L+O(1)$, with $z=Q^{\min(\varepsilon,1)/(1000\log\log Q)}$, make CRT errors negligible. The note records the need to absorb the modulus-interval error before multiplying by the possibly arbitrarily large interval length.
* The second companion note allows several residue choices at each prime. If $R_p$ contains all residues $a_q\pmod p$ for selected moduli divisible by $p$, put $r_p=|R_p|$ and
  $$
  H=\sum_{p\le z,\ r_p>0}\frac1{p r_p}.
  $$
  Weight the prime count by $1/r_p$. Its variance is $O(H)$, while a typical modulus forces an additional amount comparable to $H$. The resulting bound is $O(X/H+Qz^2/H^2)$ in the stated long-window setting. Thus growing but sufficiently coherent prime-residue supports are still an obstruction to a long burst.

Neither estimate supplies an inverse theorem saying that a small periodic footprint has few compatible profiles or large $H$. That missing implication is substantial; no such theorem was proved.

## 6. Other structural observations and failed approaches

### 6.1 Coset antichains are not primitive modulus sets

A class at $q$ may be discarded if an earlier $d\mid q$ has the same residue modulo $d$; it is redundant even with activation. It was tempting to apply primitive-set bounds to the remaining cosets. This fails.

Let $N=10^{16}+1$. For every integer $q\ge N$, choose $a_q\pmod q$ inductively outside all earlier classes whose moduli divide $q$. If no residue were available, these distinct divisor-modulus classes would cover every residue modulo $q$, and hence all integers, contradicting Hough's checked Theorem 1. Thus one obtains a containment-antichain with **every** modulus $q\ge N$, and
$$
 \sum\frac1{q\log q}=\infty.
$$
Scaling moduli and residues by a fixed $M$ gives an antichain with moduli $Mq$, logarithmic modulus density $1/M$, and full union contained in $M\mathbb Z$. Therefore even positive logarithmic density of antichain moduli does not force full periodic union measure one.

### 6.2 First kills localize, but do not settle, the problem

The disjoint first-kill sets are
$$
 E_i=A^{(i-1)}\cap B_i,
 \qquad e_i=d(E_i)=\delta_{i-1}-\delta_i,
 \qquad\sum_i e_i=1-\delta.
$$
For compatible earlier classes, division by $g_{ij}=(q_i,q_j)$ gives quotient conditions modulo $q_j/g_{ij}$. Thus
$$
 E_i=\{a_i+q_it:t\ge1,\ t\in S_i\},\qquad d(S_i)=q_i e_i.
$$
Earlier moduli are active at every point of $B_i$, so this quotient description respects activation exactly.

The checked Chojecki source proposes a uniform harmonic estimate for $S_i$, with an entropy term and additional charges whose aggregate is $o(\log X)$. The charge bound is a conjecture, not a theorem.

Its tower example shows why individual entropy errors alone fail. For $(u,6)=1$, take
$$
 m_j=u2^{r-j}3^j\quad(0\le j\le r),
$$
with the source's residues
$$
 a_r=0,qquad
 a_j\equiv u3^r(1+2^{r-j-1})\pmod{m_j}\quad(j<r).
$$
The moduli strictly increase. The top first kill is
$$
 E_{m_r}=\{u3^r(1+2^r t):t\ge0\},\qquad e_{m_r}=1/(u6^r).
$$
Its first point has harmonic weight $1/(u3^r)$, exponentially larger than the entropy-sized quantity $O(r/(u6^r))$. No bound of each first-kill spike purely by its periodic density is available. Making many such spikes occur at distinct endpoints without spending too much earlier modulus capacity was not achieved.

### 6.3 A nearby-multiple injection fails

One idea was to assign every deleted $n$ to a distinct multiple $b\asymp n$ of a witnessing modulus, then use (3.2). Such an injection need not exist. Take moduli $q,2q,\ldots,Kq$ with $q\ge K$, and choose their classes in distinct residues modulo $q$. Up to $X=Kq$, there are on the order of $K\log K$ covered points, but only $O(K)$ multiples of $q$ below $CX$. The full union footprint is correspondingly larger, about $H_K/q$; an argument would have to retain that information rather than compress all residue fibers together.

### 6.4 Rough moduli cannot cheaply support large reciprocal mass

For fixed $u$, if distinct moduli $q\le y^u$ have no prime factor $\le y$, then arbitrary singleton classes satisfy
$$
 \sum_q1/q\le C_u d(U).
$$
Indeed, with $Z=\sum_q1_{[a_q]_q}$ and $S=\mathbb EZ$,
$$
 \mathbb EZ^2\le\sum_q\frac1q\sum_r\frac{(q,r)}r\le C_u S.
$$
Expand $(q,r)=\sum_{d\mid q,d\mid r}\varphi(d)$. There are at most $2^{\lceil u\rceil}$ divisors of such a $q$, and the reciprocal sum of all $y$-rough integers below $y^u$ is bounded in terms of $u$. Cauchy–Schwarz proves the claim. This shows that low-footprint, high-cost blocks need increasingly complicated small-prime structure, but gives no conditioned-tail estimate. Details: research/profinite_shift.md (unretained companion note `research/profinite_shift.md`).

### 6.5 Biased labels and rare long progression words

The direct Wang signature method runs out of distinct moduli: a pattern $S$ requires divisibility by $d_S=\prod_{i\in S}p_i$, leaving only $O(Q/d_S)$ moduli near $Q$, versus about $Q/2^k$ endpoints with a central unbiased pattern. In Wang's range $d_S\gg2^k$.

Choosing marking probabilities around $1/p$ matches actual divisibility frequencies and avoids this supply mismatch. A heuristic conditional footprint intensity is
$$
 \prod_{p\le z}(1-1/p+1_{p\in T}),
$$
whose typical magnitude is approximately $(\log z)^{-(1-\log2)}$. This decay does not pay for a positive proportion of logarithmic scales by the same union-bound epoch assembly. These are heuristic calculations, not a proof ruling out every biased-label construction.

A further unproved idea tried to choose one class at each $q\asymp Q$ whose first $D$ later hits all have a desired prime signature. For primes much larger than $D$, distinct progression hits query distinct residues. The negative-label probability was heuristically $\exp(-D\sum1/p)$, against roughly $q/d$ candidate residues. Balancing suggested $D\approx\log(q/d)/(\sum1/p)$. No proof of simultaneous choices, a positive density of distinct endpoints, or sufficiently small total footprint was obtained.

## 7. A precise unproved Dirichlet route

For a finite family $\mathcal F$, let $B_{\mathcal F}$ be its delayed union, $U_{\mathcal F}$ its full periodic union, and
$$
 F_{\mathcal F}(s)=\sum_{n\in B_{\mathcal F}}n^{-s},\qquad
 d_{\mathcal F}=d(U_{\mathcal F}).
$$
A sufficient statement is the **uniform** estimate
$$
 \frac{F_{\mathcal F}(s)}{\zeta(s)}
 \le d_{\mathcal F}+\eta(s),
 \qquad \eta(s)\to0\quad(s\downarrow1),                         \tag{7.1}
$$
with the same error for every finite distinct-modulus singleton family. The stronger possibility $\eta=0$ was also investigated. Neither was proved or disproved.

Why (7.1) would suffice: pass to the infinite union by monotone convergence at each fixed $s>1$. This gives the upper limit $1-\delta$ as $s\downarrow1$. Each fixed finite union supplies the opposite lower limit. Thus
$$
 \sum_{n\in B}n^{-s}\sim\frac{1-\delta}{s-1}.
$$
The nonnegative Hardy–Littlewood Tauberian theorem explicitly used in the checked Davenport–Erdős 1936 source then yields $H_B(X)\sim(1-\delta)\log X$. This is a conditional reduction, not a solution.

For a single class,
$$
 \sum_{t\ge1}(a+qt)^{-s}\le q^{-s}\zeta(s)\le q^{-1}\zeta(s).
$$
For zero classes the bound follows from the multiplicative monotonicity in Davenport–Erdős. Arbitrary residues are the unresolved part.

### 7.1 Exact finite calculation with all thresholds retained

For a nonempty compatible subfamily $I$, let
$$
 \ell_I=\operatorname{lcm}_{i\in I}q_i,quad
 r_I\in[0,\ell_I),quad m_I=\max_{i\in I}q_i,
$$
where $r_I$ is its CRT residue. Its first eligible point is
$$
 b_I=r_I+\ell_I\left\lceil\frac{m_I-r_I}{\ell_I}\right\rceil.
$$
Inclusion–exclusion gives the exact formulas
$$
 F(s)=\sum_{I\text{ compatible}}(-1)^{|I|+1}
       \ell_I^{-s}\zeta(s,b_I/\ell_I),
 \qquad d=\sum_{I\text{ compatible}}\frac{(-1)^{|I|+1}}{\ell_I}.
$$
With $\psi$ the digamma function and $\gamma$ Euler's constant,
$$
 F(s)/\zeta(s)-d=(s-1)C+O((s-1)^2),
$$
where
$$
 C=\sum_{I\text{ compatible}}\frac{(-1)^{|I|+1}}{\ell_I}
 \left[-\psi(b_I/\ell_I)-\log\ell_I-\gamma\right].               \tag{7.2}
$$
Replacing $b_I$ with the first positive CRT representative would generally be wrong.

Reported experiments using these formulas included 20,000 small random systems with 2–8 distinct moduli below 45, several values of $s$, and optimization on divisor families of small common periods. No violation of $F/\zeta\le d$ was found. These computations are only exploratory evidence. They do not establish a uniform inequality, and no large finite search was treated as a proof.

### 7.2 Weighted compression is rigorously false

Ordinary compression (3.1) does not extend to maximizing $F/\zeta-d$ at zero residues. Take moduli $2,3,23$, with residues $0,0,2$. They are compatible with the common integer shift 48. Both this system and the all-zero system have periodic union density $47/69$.

Outside the first two classes, their delayed 23-class contributions are respectively
$$
 \{138j+25,138j+71:j\ge0\},
 \qquad \{138j+23,138j+115:j\ge0\}.
$$
Thus their Dirichlet-series difference is
$$
 \sum_{j\ge0}\bigl[(138j+25)^{-s}+(138j+71)^{-s}
                   -(138j+23)^{-s}-(138j+115)^{-s}\bigr].       \tag{7.3}
$$
At $s=1$, writing $x=138j$, each bracket equals
$$
 \frac{44}{(x+71)(x+115)}-\frac2{(x+23)(x+25)}>0,
$$
because
$$
 22(x+23)(x+25)-(x+71)(x+115)=21x^2+870x+4485>0.
$$
The series converges uniformly near $s=1$, by an $O((1+j)^{-2})$ bound. It is therefore positive for $s>1$ sufficiently close to 1. This disproves the proposed zero-residue comparison and even its single-prime-coordinate version. It does **not** disprove (7.1).

### 7.3 Why multiplicity cannot be ignored

Wang's finite blocks already contradict the unrestricted multi-residue analog of (7.1). Choose $s=1+1/\log Q$. Its $\gg Q$ active endpoints of size $\asymp Q$ give
$$
 F(s)/\zeta(s)\gg1/\log Q,
$$
whereas the footprint is $e^{-c\sqrt{\log Q}}$. For a uniform-o(1) statement one must use the assembled multi-epoch counterexample, not merely this one-block comparison; that assembled counterexample rules out a general multiplicity-free proof. The exact $\eta=0$ finite inequality is already contradicted by the single block. Any successful singleton proof must genuinely use the one-class-per-modulus restriction.

### 7.4 A decreasing-step reformulation, without an estimate

For a finite full union $U$, let $f(n)$ be the least modulus of a class containing $n$, and $f(n)=\infty$ outside $U$. Then
$$
 B=\{n\ge1:f(n)\le n\},
 \qquad f(n-f(n))\le f(n)\quad(n\in U).
$$
The backward map $n\mapsto n-f(n)$ has nonincreasing step labels. Positive points of $U\setminus B$ are roots $r<f(r)$; one singleton class at modulus $q$ supplies at most one possible canonical root $a_q$. This suggested charging harmonic excess to omitted seeds or to a decreasing dependency graph. No valid global charging inequality was derived. The monotone-label property itself also holds with repeated moduli and is therefore insufficient by itself.

A related speculative estimate was
$$
 H_{B_{\mathcal F}}(X)\le d(U_{\mathcal F})\log X
                         +C\sum_{q\in\mathcal F}1/q.
$$
It was not proved. Even a global bound with coefficient $C>1$ on $d(U)\log X$ would not automatically settle the problem: conditioning on a finite periodic prefix produces multiplicities and constants depending on its period. Their growth need not be dominated by the vanishing new periodic mass. No valid argument eliminating that dependence was found.

## 8. What remains open in this record

The exact missing lower bound is
$$
 \underline{\operatorname{ld}}(A)\ge\delta,
$$
or some other proof that lower and upper logarithmic densities agree. None of the support bounds, coherent-window estimates, or finite experiments provides it.

The established obstructions leave two possible counterexample mechanisms unexcluded:

1. Small completed singleton footprints with unboundedly many transiently deleted points per modulus, so the bounded-multiplicity argument in Section 4.1 does not apply.
2. Small *conditioned first-kill* footprints rather than small full class unions, with a rigorous global way of maintaining many distinct surviving endpoints.

Neither mechanism was constructed. The positive route (7.1), or a global charge bound of the kind isolated by Chojecki, remains unproved. The window estimates suggest an inverse structural question—whether a small periodic footprint forces enough prime-residue coherence to prevent long local deletion—but no inverse theorem was established.

## 9. Source checks and auxiliary records

Relevant source passages checked during the investigation:

* Davenport–Erdős (1936), Section 2: finite densities, monotonicity for zero residues, logarithmic-density theorem, and the Tauberian step.
* Davenport–Erdős (1951), pp. 1–5: finite-density limit and smooth reciprocal-weight proof.
* Chojecki, full source: positive cases, first-kill quotient representation, conditional charge hypothesis, and the tower obstruction. Its conjectural estimates were never used as proved facts.
* Wang, especially Sections 3–4: exact repeated-modulus endpoint assignment, footprint estimate, and recovery/deletion epoch assembly. Its result is not a singleton counterexample.
* Hough, Theorem 1 near the beginning: the stated $10^{16}$ minimum-modulus bound used in the antichain example.
* Filaseta–Ford–Konyagin–Pomerance–Yu, Section 1: the Rogers zero-residue extremal statement and context for divisor windows.
* Araújo, the weak-light-tail discussion and Remark 3.18: fully active translate examples do not preserve the present activation condition. Points prescribed below their moduli cannot be imported as deleted endpoints here.

Further records, all explicitly partial, were kept in companion notes that are not retained.

**Final status:** precise partial results and obstructions, but no resolution of Erdős Problem 25.
