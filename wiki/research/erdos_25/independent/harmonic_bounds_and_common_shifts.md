---
name: research/erdos_25/independent/harmonic_bounds_and_common_shifts
title: Independent investigation of Erdős Problem 25
desc: Unverified independent input; checked conclusions and corrections are recorded in the topical notes.
tags: []
sources: []
created: 2026-09-22T02:34:11Z
updated: 2026-10-13T05:28:09Z
---

# Independent investigation of Erdős Problem 25

***

## 1. Status and scope

**Incomplete: no proof in full generality and no counterexample to the exact
statement were obtained.** The results below are partial results and
restrictions on attempted constructions. Conjectural steps are identified
explicitly.

Only the supplied files were used. The supplied problem page and sources were
not modified.

The most substantial proved observation is a finite harmonic bound for the
first $K$ eligible points of each distinct-modulus congruence. It obstructs
a direct singleton version of Wang's bounded-quotient deletion epochs.
It does not control the points with unbounded quotient $n/q$, and it does
not resolve the conditioned-tail problem.

## 2. Exact formulation and elementary positive cases

Choose representatives $0\le a_i<n_i$. Then the forbidden set associated
with modulus $n_i$ is exactly
$$
 B_i=\{a_i+t n_i:t=1,2,\ldots\}.
$$
This uses the required inclusive activation condition $n\ge n_i$.
In particular, $a_i=0$ removes $n_i$ itself, whereas a nonzero least
representative $a_i<n_i$ is not removed by its own congruence.

Put
$$
 A=\mathbb N\setminus\bigcup_i B_i,\qquad
 A^{(k)}=\mathbb N\setminus\bigcup_{i\le k}B_i.
$$
The natural density of a set $S$, when it exists, is
$\lim_{X\to\infty}|S\cap[1,X]|/X$. Its lower and upper logarithmic
densities are
$$
 \underline\ell(S)=\liminf_{X\to\infty}
 \frac1{\log X}\sum_{\substack{n\le X\\n\in S}}\frac1n,\qquad
 \overline\ell(S)=\limsup_{X\to\infty}
 \frac1{\log X}\sum_{\substack{n\le X\\n\in S}}\frac1n.
$$
Logarithmic density exists when these agree. Natural density implies
logarithmic density with the same value, by partial summation; the converse
does not hold.

Each finite truncation $A^{(k)}$ is eventually periodic, with period
dividing $\operatorname{lcm}(n_1,\ldots,n_k)$. Its natural and logarithmic
densities therefore agree; call this value $\delta_k$. Then
$$
 \delta_k\downarrow\delta\in[0,1],\qquad
 \overline\ell(A)\le\delta.
$$
The same inclusion $A\subseteq A^{(k)}$ gives
$\overline d(A)\le\delta$. Thus $\delta=0$ already implies natural
and logarithmic density zero. The difficult regime has $\delta>0$.

If $\sum_i1/n_i<\infty$, natural density exists and equals $\delta$.
The important uniform estimate is
$$
 \#(B_i\cap[1,X])\le \lfloor X/n_i\rfloor,\qquad
 \#((A^{(k)}\setminus A)\cap[1,X])
 \le X\sum_{i>k}\frac1{n_i}.
$$
Only moduli at most $X$ can contribute. Comparing with the fixed periodic
truncation and then sending $k\to\infty$ proves the assertion. This
argument does not incorrectly assume countable subadditivity of upper
natural density.

For pairwise coprime moduli,
$$
 \delta_k=\prod_{i\le k}(1-1/n_i).
$$
Convergence of the reciprocal sum is covered above; divergence gives
$\delta=0$. Thus this case also has natural density.

For zero residues, the supplied Davenport--Erdős theorem gives logarithmic
density, but natural density can fail. The 1936 source, Theorem 1(a), and
the 1951 source, pp. 3--5, were checked. The 1951 proof uses multiplicative
harmonic weighting. Its divisibility invariance is not available for
arbitrary moving residues.

## 3. First-kill formulation and the actual gap

Define
$$
 E_i=A^{(i-1)}\cap B_i.
$$
These are disjoint and partition $\mathbb N\setminus A$. Their eventual
periodic densities satisfy
$$
 e_i=\delta_{i-1}-\delta_i,\qquad \sum_i e_i=1-\delta.
$$
For $j<i$, let $g_{ij}=(n_i,n_j)$. If the two residues are incompatible
modulo $g_{ij}$, there is no restriction from $j$ on $B_i$. Otherwise,
writing $n=a_i+n_i t$, the earlier congruence becomes one forbidden
residue modulo
$$
 q_{ij}=n_j/g_{ij}.
$$
Thus $E_i$ is the image of a finite periodic quotient sieve $S_i$, and
$d(S_i)=n_i e_i$.

Chojecki's supplied source was checked, including Sections 4--7. Its
proposed uniform harmonic estimate has an additional charge $\tau_i$:
$$
 \sum_{\substack{t\le Y\\t\in S_i}}\frac1{t+a_i/n_i}
 =d(S_i)\log Y+
 O\!\left(d(S_i)\log\frac2{d(S_i)}+\tau_i\right).
$$
The required global statement
$$
 \sum_{n_i\le X}\frac{\tau_i}{n_i}=o(\log X)
$$
is not proved there or in this investigation. The entropy part alone is
harmless; the charge is the missing input.

The tower in that source is a real obstruction to a termwise entropy-only
estimate. For $m_j=u2^{r-j}3^j$, with suitable stated residues, the top
first-kill set is
$$
 \{u3^r(1+2^r t):t\ge0\}.
$$
Its density is $1/(u6^r)$, but its first point contributes $1/(u3^r)$
to the harmonic sum. Their ratio is $2^r$. Consequently a single
first-kill spike cannot simply be bounded by a constant times
$e_i\log(1/e_i)$.

## 4. Proved compression and harmonic bounds

### 4.1 Prime-coordinate compression

Let $D$ be a finite set of moduli, choose one residue $a_q\bmod q$
for each $q\in D$, and set
$$
 U=\bigcup_{q\in D}(a_q+q\mathbb Z),\qquad
 M(D)=\{n\ge1:q\mid n\text{ for some }q\in D\}.
$$
Both have periodic natural densities. Then
$$
 d(U)\ge d(M(D)). \tag{4.1}
$$

**Proof.** In the finite uniform space modulo
$L=\operatorname{lcm}(D)$, use the Chinese remainder decomposition
$$
 \mathbb Z/L\mathbb Z=\prod_{p\mid L}\mathbb Z/p^{v_p(L)}\mathbb Z.
$$
A class modulo $q$ is a product of $p$-adic balls of measures
$p^{-v_p(q)}$. Fix a prime coordinate and all the other coordinates.
The classes present in this fiber have some collection of balls in the
remaining coordinate. Replace all their centers by zero. The new balls
are nested, so their union has the largest of their individual measures,
no more than the old union measure. Integrating over the other coordinates
shows that total union measure cannot increase. Repeat for every prime.
The resulting classes are the zero classes modulo the same moduli. This
proves (4.1). Repeated moduli are permitted in this compression argument.
$\square$

### 4.2 Harmonic domination for a set of multiples

For every finite $D$ and integer $X\ge1$,
$$
 \sum_{\substack{n\le X\\n\in M(D)}}\frac1n
 \le d(M(D))H_X,\qquad H_X=\sum_{n=1}^X\frac1n. \tag{4.2}
$$

**Proof.** Discard moduli greater than $X$; this does not change the
left side and can only decrease the density on the right. For every prime
$p\le X$, take independent random variables
$$
 \mathbb P(V_p=k)=(1-1/p)p^{-k},\qquad k\ge0,
$$
and let $N=\prod_{p\le X}p^{V_p}$. On integers supported on these primes,
$$
 \mathbb P(N=n)=c_X/n,\qquad c_X=\prod_{p\le X}(1-1/p).
$$
Conditionally on $N\le X$, its law is therefore $1/(nH_X)$.

The event $F=\{N\in M(D)\}$ is increasing in the prime valuations;
$G=\{N\le X\}$ is decreasing. Product-measure association gives
$\mathbb P(F\cap G)\le\mathbb P(F)\mathbb P(G)$.
Here association can be proved without an external theorem: for increasing
bounded functions of one random variable, covariance is nonnegative because
$$
 2\operatorname{Cov}(f(V),g(V))
 =\mathbb E[(f(V)-f(V'))(g(V)-g(V'))]\ge0.
$$
Induction on the finite number of independent coordinates proves the
product version; apply it to $1_F$ and $-1_G$.

Finally, $\mathbb P(F)=d(M(D))$, since inclusion-exclusion gives the
same finite sum of reciprocal least common multiples for both quantities.
Condition on $G$ to obtain (4.2). $\square$

The product-geometric distribution is the multiplicative weighting in the
checked Davenport--Erdős 1951 source. The association argument above is
written out independently and supplies the constant one.

### 4.3 First $K$ eligible points

Now normalize $0\le a_q<q$, and let
$$
 E_K=\bigcup_{q\in D}\{a_q+tq:1\le t\le K\}.
$$
For distinct moduli,
$$
 \boxed{\quad
 \sum_{\substack{n\le X\\n\in E_K}}\frac1n
 \le H_K\,d(U)\,H_X.\quad} \tag{4.3}
$$
Indeed,
$$
 \begin{aligned}
 \sum_{\substack{n\le X\\n\in E_K}}\frac1n
 &\le \sum_{\substack{q\in D\\q\le X}}
          \sum_{t=1}^K\frac1{a_q+tq}\\
 &\le H_K\sum_{\substack{q\in D\\q\le X}}\frac1q\\
 &\le H_K\sum_{\substack{n\le X\\n\in M(D)}}\frac1n\\
 &\le H_K d(M(D))H_X\le H_Kd(U)H_X.
 \end{aligned}
$$
Distinctness is used when the moduli themselves are counted just once
inside $M(D)$. The eligibility condition is used in $t\ge1$.

This bound applies to an entire finite epoch, regardless of overlap
between its blocks. If all proposed deleted endpoints have witnesses
with $n/q\le K$, their normalized harmonic mass cannot remain positive
while the total completed footprint tends to zero. Thus a Wang-type
singleton replacement retaining bounded endpoint/modulus ratios cannot
work.

The estimate does **not** say that every conceivable counterexample is
impossible. Its factor $H_K$ is unbounded, and the relevant tail after
conditioning on earlier survivors need not have small ambient footprint.

### 4.4 Another finite capacity calculation

Suppose $D\subseteq[Q,CQ]$ contains at least $cQ$ distinct moduli,
where $c,C>0$ are fixed. Any choice of singleton residues satisfies
$$
 d(U)\gg_{c,C}\frac1{\log Q}.
$$
To see this, let $F=\sum_{q\in D}1_{[a_q]_q}$ on the finite uniform
period space. Then $\int F\ge c/C$, while
$$
 \begin{aligned}
 \int F^2
 &\le\sum_{Q\le q,r\le CQ}\frac{(q,r)}{qr}\\
 &=\sum_{d\le CQ}\frac{\varphi(d)}{d^2}
       \left(\sum_{Q/d\le u\le CQ/d}\frac1u\right)^2
 \ll_C\log Q.
 \end{aligned}
$$
The harmonic sums in parentheses are bounded in terms of $C$, including
the range $d>Q$. Cauchy--Schwarz on the support of $F$ proves the claim.
This calculation independently excludes Wang's
$\exp(-\Omega(\sqrt{\log Q}))$ footprint at a scale containing a positive
proportion of all nearby singleton moduli.

## 5. A proved restriction on arbitrary common shifts

For integer $b$, define
$$
 U_Q(b)=\bigcup_{Q\le q\le2Q}(b+q\mathbb Z).
$$
Uniformly in $b$ and intervals $I$ of length $H$,
$$
 \frac{|U_Q(b)\cap I|}{H}\longrightarrow0
 \quad\text{when }Q\to\infty,\quad H/Q\to\infty. \tag{5.1}
$$
Thus even arbitrarily large CRT shifts of a dyadic multiples block cannot
maintain positive local density on intervals much longer than its moduli.

**Proof.** Fix a squarefree $P$. For $r\bmod P$, put
$$
 S_Q(r)=\sum_{Q\le q\le2Q}
 \frac{(q,P)}q\,1_{(q,P)\mid r-b}.
$$
Counting simultaneous congruences gives
$$
 |U_Q(b)\cap I\cap(r+P\mathbb Z)|
 \le \frac HP S_Q(r)+O(Q).
$$
For fixed $P$, harmonic summation in residue classes yields uniformly
in $r,b$
$$
 S_Q(r)=\log2\,W_P(r-b)+o_P(1),
$$
where
$$
 W_P(t)=
 \prod_{\substack{p\mid P\\p\mid t}}(2-1/p)
 \prod_{\substack{p\mid P\\p\nmid t}}(1-1/p).
$$
Indeed, integers with $(q,P)=d$ have density
$\varphi(P/d)/P$; the resulting divisor sum factors into this product.

Let $\rho_P(\varepsilon)$ be the proportion of residues with
$W_P(t)>\varepsilon$. Count those residue classes trivially and the
others by the preceding incidence bound:
$$
 \frac{|U_Q(b)\cap I|}{H}
 \le \rho_P(\varepsilon)+\varepsilon\log2+o_P(1)
       +O(PQ/H+P/H).
$$
First let $Q,H/Q\to\infty$, holding $P$ fixed.

Next take $P$ to be the product of the first $k$ primes. For uniform
$t\bmod P$, the indicators $1_{p\mid t}$ are independent, with
probability $1/p$. With $\lambda_k=\sum_{p\mid P}1/p$,
$$
 \mathbb E\log W_P=-(1-\log2)\lambda_k+O(1),\qquad
 \operatorname{Var}(\log W_P)=O(\lambda_k).
$$
Since $\lambda_k\to\infty$, Chebyshev gives $W_P\to0$ in probability.
Hence $\rho_P(\varepsilon)\to0$. Send $k\to\infty$ and then
$\varepsilon\downarrow0$. This proves (5.1). $\square$

Truncation to $n\ge q$ only reduces these sets, so the upper bound also
holds with the exact activation rule.

For completeness, a simpler common-shift restriction is useful. If all
moduli are at least $N$ and $0\le b<N$, every eligible point can be
written $n=b+m$ with $m\in M(D)$, and $1/n\le1/m$. Thus its total
harmonic deletion is at most $d(M(D))H_X$. A negative shift with
$|b|\le CN$ costs at most a fixed factor $1+C$. Large positive
representatives do not admit this direct comparison; (5.1) handles their
dyadic-window variant instead.

## 6. Attempted counterexamples and why they did not close

### Wang's multi-residue construction

The supplied Wang source was checked in Lemmas 4--7 and Section 4.
At scale $Q=2^j$, it uses approximately $k\asymp\sqrt j$ auxiliary
primes and a modulus $q_S\asymp Q$ for each central label set $S$.
It deletes $\gg Q$ endpoints in a fixed interval above $Q$, with
completed footprint $\exp(-\Omega(k))$. Long dyadic epochs and periodic
recovery then yield logarithmic oscillation for **multi-residue** sieves.

There are at most $2^k$ different $q_S$, but $\gg Q$ endpoints.
Keeping one endpoint per modulus leaves total harmonic mass at most
$O(2^k/Q)$ at that scale, which tends to zero rapidly.

Trying to add many distinct moduli with the same prime signature encounters
a stronger capacity problem. A signature $S$ requires divisibility by
$d_S=\prod_{i\in S}p_i$. Among $O(Q)$ nearby integers there are only
$O(Q/d_S+1)$ such moduli, whereas fair labels ask for about $Q/2^k$
endpoints of that signature. In Wang's skeleton $d_S$ is much larger
than $2^k$ for central $S$.

Biased labels of probability $1/p_i$, rather than $1/2$, were considered
because their pattern frequencies match the divisibility frequencies of
ordinary moduli. This suggests a possible matching of endpoint patterns to
moduli, but no construction was proved. The corresponding informal anchor
calculation has scale
$$
 \prod_i(1-1/p_i)\,2^{|T|},\qquad |T|\approx\sum_i1/p_i,
$$
whose logarithm is roughly
$-(1-\log2)\sum_i1/p_i$. This is far slower than Wang's decay. It did
not give a summable cost over the required consecutive dyadic epochs.
This is a failed heuristic route, not a proved nonexistence theorem.

Replacing repeated $q$'s by distinct multiples $kq$ preserves containment
of completed cylinders, but an endpoint $n\asymp q$ allows only bounded
$k$ under activation. Moving endpoints much farther out reduces their
harmonic weights. No way was found to compensate by many successive
eligible points of each refined modulus.

### Shifted intervals of multiples

For $q\in[Q,2Q)$, assign the common residue $Q\bmod q$. The points
$q+Q\in[2Q,3Q)$ are all deleted by eligible singleton congruences. The
completed footprint is a translate of the multiples union of
$[Q,2Q)$, whose density tends to zero. Thus this is a useful
natural-density spike.

Its harmonic mass is only of constant size. One needs order $\log Q$
consecutive logarithmic scales for a fixed logarithmic-density spike.
Small footprint at one scale therefore does not settle the problem.
Trying to correlate such footprints by common shifts is obstructed by
Sections 4 and 5.

Exact containment of a new full class in the old completed union also
cannot help: when a new modulus is active, all earlier moduli are active.
Such a class makes no new deletion. A successful variant would require
tiny exceptional parts outside the old union, synchronized near the
relevant endpoints.

### Generalized towers

The prime-power tower can formally be generalized. For an odd top modulus
$q$ and divisors $D_j\mid q$ satisfying suitable congruences, take
$$
 m_j=2^j q/D_j<q,\qquad
 a_{m_j}\equiv(q/D_j)(1+2^{j-1})\pmod {m_j}.
$$
If $D_j\equiv1\pmod{2^j}$, then on the top class $n=qt$ this removes
$t\equiv1+2^{j-1}\pmod{2^j}$. Different layers have different
2-adic valuations, and some same-layer collisions can use identical
residues.

This did not produce a legal global oscillation construction. Shared tower
data can kill the proposed first points of other towers. Already the
layer modulo $4u$, with residue $3u$, removes top points $ud$ with
$d\equiv3\pmod4$. Restricting all relevant factors to favorable residue
classes makes the available tops sparse. No simultaneous lower bound for
surviving endpoints and upper bound for total periodic loss was proved.

## 7. Positive approaches left unproved

A sufficient finite statement would be
$$
 \sum_{\substack{n\le X\\
 n\in\bigcup_{q\in D}\{a_q+tq:t\ge1\}}}\frac1n
 \le d(U)H_X. \tag{7.1}
$$
This is **not proved**. It would settle the problem directly: apply it to
all installed moduli at most $X$, whose completed union density is at
most $1-\delta$. The lower logarithmic density of $A$ would be at
least $\delta$, matching the upper bound in Section 2.

A related unproved sufficient statement is Dirichlet domination:
$$
 \frac1{\zeta(s)}
 \sum_{n\in U_{\mathrm{del}}}n^{-s}\le d(U),\qquad s>1. \tag{7.2}
$$
Finite approximation would then yield the infinite Dirichlet limit; the
same nonnegative-coefficient Tauberian step used in the checked
Davenport--Erdős 1936 source would yield logarithmic density.

The proof of (4.2) does not establish either assertion for moving residues:
the congruence event is not increasing in prime valuations, and unit
residues are not independent coordinates of the weighted integer law.
Haar compression alone only gives (4.1); it does not control the harmonic
mass of all shifted points.

Small finite checks did not refute (7.1) or (7.2). They provide no proof.
A still stronger normalized comparison with the all-zero system was
considered and not established. The analogous counting-function comparison
is false: for moduli $\{3,4,6\}$, residues $(0,0,4)$, the delayed
union has six points up to 10 and periodic density $7/12$; the zero
system has five points and density $1/2$. Thus
$$
 \frac6{7/12}=\frac{72}7>10=\frac5{1/2}.
$$
One cannot infer a weighted rearrangement from an unweighted one.

A proved auxiliary zero-residue estimate is, for finite $D$ with
$\max D=M$,
$$
 M^{1-s}d(M(D))
 \le \zeta(s)^{-1}\sum_{n\in M(D)}n^{-s}
 \le d(M(D)).
$$
For the lower bound, partition by the first dividing generator $m_i$.
The quotient avoids a finite multiples union. Davenport--Erdős Dirichlet
domination makes its Dirichlet probability at least its natural density
$d_i$. Its contribution is at least
$m_i^{-s}d_i=e_i m_i^{1-s}\ge e_iM^{1-s}$. Sum over $i$.
This auxiliary bound did not extend to shifted classes.

Finally, conditioning on a finite old period $L$ transforms a modulus
$q$ on a surviving fiber into $q/(q,L)$. Repeated quotient moduli
can occur, with multiplicity bounded in terms of the divisors of $L$;
activation can start below that quotient modulus by a factor depending
on $L$. The elementary resulting estimates have constants growing with
$L$. There is no justification for assuming those constants times
$\delta_k-\delta$ tend to zero.

## 8. An isolated-endpoint question and a proved special case

A narrower unproved target arose:
$$
 q_1<q_2<\cdots,\quad q_i\le b_i<2q_i,\quad
 b_j\not\equiv b_i\pmod {q_i}\quad(j>i).
 \tag{8.1}
$$
Must $\{b_i\}$ have upper logarithmic density zero?
No answer in this generality was obtained.

The $b_i$'s are distinct. With residue $b_i-q_i$, each $b_i$ is hit
by exactly one eligible congruence. Earlier ones are excluded by (8.1).
If $j>i$ and $q_j\le b_i$, both $b_i,b_j$ lie in
$[q_j,2q_j)$, so congruence modulo $q_j$ would force equality.
If $q_j>b_i$, that later class is inactive.

The corresponding full cylinders form an antichain under containment, but
this weaker property is insufficient. The deficient moduli
$\sigma(q)<2q$ admit greedy residues avoiding every proper-divisor
cylinder: at stage $q$, those cylinders occupy at most
$$
 \sum_{\substack{d\mid q\\d<q}}q/d=\sigma(q)-q<q
$$
residues. These moduli have positive lower density: averaging
$\sigma(q)/q-1$ gives at most $\zeta(2)-1<1$, so Markov gives lower
density at least $2-\zeta(2)$ for deficiency. This example does not
avoid non-divisor-related earlier classes and is not a counterexample
to (8.1).

**Proved special case.** If the pairs in (8.1) lie in finitely many fixed
rational affine relations
$$
 v b=u q+c
$$
with fixed positive integers $u,v$ and fixed integer $c$, their endpoint
set has logarithmic density zero.

**Proof.** Work in one relation. If $q_j=kq_i$ and
$k\equiv1\pmod v$, then
$$
 b_j-b_i=u q_i(k-1)/v
$$
is divisible by $q_i$, contradicting (8.1).
Let $h(q)$ be the part of $q$ supported on primes dividing $v$.
Fix $h$, and write $q=hr$, $(r,v)=1$. Any divisibility chain of
these $r$'s has length at most $\varphi(v)$: a longer chain contains
two elements equal modulo $v$, whose quotient is $1\bmod v$.
Coloring by maximal chain length ending at an element partitions the
set into at most $\varphi(v)$ primitive sets.

Every primitive set has logarithmic density zero by Davenport--Erdős:
its tail lies in its full multiples union minus a finite-prefix multiples
union, whose logarithmic densities differ by a quantity tending to zero.
Thus the moduli with bounded $h(q)$ have logarithmic density zero.
The rest have upper density at most
$$
 \sum_{\substack{h>H\\p\mid h\Rightarrow p\mid v}}\frac1h,
$$
which tends to zero, since the total sum is a finite Euler product.
The whole modulus subsequence consequently has logarithmic density zero.
Finally,
$$
 \sum_{b_i\le X}\frac1{b_i}\le\sum_{q_i\le X}\frac1{q_i}=o(\log X).
$$
Take the finite union of the affine subsequences. $\square$

This includes bounded choices of $b_i-q_i$ or $2q_i-b_i$.
Approximate affine relations do not preserve the exact congruence argument,
so this gives no extension to arbitrary moving residues.

## 9. Remaining uncertainty

No argument here controls the entire far-quotient contribution, or the
conditioned tail with constants uniform in the earlier system. No
construction overcomes the singleton capacity restrictions while producing
two separated logarithmic-density subsequences.

Accordingly, none of the failed constructions should be read as an explicit
counterexample, and neither (7.1), (7.2), nor the general endpoint assertion
(8.1) should be used as a proved lemma. Resolving one of those gaps, or
finding a substantially different construction, is still necessary to answer
the supplied problem.
