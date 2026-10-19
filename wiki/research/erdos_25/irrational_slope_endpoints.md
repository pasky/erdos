---
name: research/erdos_25/irrational_slope_endpoints
desc: Natural nullity for Brjuno slope endpoints, and a Liouville obstruction to extending it to all irrational slopes.
tags: [endpoints, partial-results, diophantine-approximation]
sources: []
created: 2026-09-22T03:23:08Z
updated: 2026-10-14T00:26:52Z
---


# research/erdos_25/irrational_slope_endpoints

***

These results concern the bounded-quotient first-kill problem, not the
full delayed union. The positive result controls conditioning on an old
period without a constant growing with that period. The original badly
approximable theorem below extends to every Brjuno slope.

A different [curvature argument](curved_residue_profiles.md) proves
natural endpoint nullity for $\lfloor\theta q+q^\alpha\rfloor$,
$0<\alpha<1$, for every slope $\theta$, including Liouville slopes.
It changes the residue profile; it does not remove the hypothesis from
the purely linear theorem below or control unbounded quotients.

## Badly approximable slopes: proved natural nullity

Fix $0<\theta<1$ with
$$
 c_\theta:=\inf_{k\ge1}k\|k\theta\|>0,
$$
and put $a_q=\lfloor\theta q\rfloor$, $C_q=[a_q]_q$.
Let $D$ be a set of distinct moduli and fix an integer $\ell\ge1$.
Suppose
$$
 r_q=\ell q+a_q\notin C_p
 \qquad(p,q\in D,\ p<q).
 \tag{1}
$$
Then both $D$ and $\{r_q:q\in D\}$ have **natural density zero**.
Full privacy is not required.

Consequently, in any sieve with these residues, the union of first-kill
points with $q\le n\le Kq$ has natural density zero for every fixed $K$.
Partition those points by the finitely many possible quotient indices
$\ell=(n-a_q)/q$ and apply the theorem to each selected modulus set.

### A uniform dyadic second moment

For $D_Q\subseteq[Q,2Q)\cap\mathbb N$, let
$Y_Q=\sum_{q\in D_Q}\mathbf1_{C_q}$ on Haar space. Then
$$
 \mathbb EY_Q^2\le C_\theta,
 \qquad C_\theta=10+16/c_\theta
 \tag{2}
$$
is one possible uniform bound.

Indeed, for compatible distinct $q,r$, write $g=(q,r)$ and
$k=|q/g-r/g|$. Compatibility implies
$$
 1\le k\le Q/g,\qquad \|k\theta\|<1/g,
$$
because $\lfloor\theta q\rfloor-\lfloor\theta r\rfloor$ is divisible
by $g$ and differs from $\theta(q-r)$ by less than one. Among
$1\le k\le T$, the fractional parts $k\theta$ have circular separation
at least $c_\theta/T$. Hence at most
$2+2Q/(c_\theta g^2)$ possible $k\le Q/g$ qualify.
Each gives at most $4Q/g$ ordered pairs $(q,r)$ in the block. Since
$g<Q$ for distinct pairs,
$$
 \sum_{\substack{q,r\in[Q,2Q)\\q\ne r,\ C_q\cap C_r\ne\varnothing}}
                  (q,r)
 \le\sum_{g<Q}4Q\left(2+\frac{2Q}{c_\theta g^2}\right)
 \le(8+16/c_\theta)Q^2.
$$
Divide by $qr\ge Q^2$ and add the diagonal sum $\sum1/q\le1$.
This proves (2).

### A reciprocal cost that does not grow with the old period

Fix a finite initial part $F\subset D$. Let
$$
 U=\bigcup_{q\in D}C_q,\quad U_F=\bigcup_{q\in F}C_q,
 \quad \tau_F=\mu(U\setminus U_F),
$$
and let $S\subseteq\mathbb Z/P\mathbb Z$ be the survivor residues of
$U_F$ for a common period $P$. If $S$ is empty, (1) permits no later
selected endpoint, so there is nothing to prove.

For $q$ beyond $F$, define $d=(q,P)$ and
$$
 f(q)=\frac{|S\cap[a_q]_d|}{P/d}.
$$
The endpoint condition gives $f(q)>0$, and CRT gives
$\mu(C_q\setminus U_F)=f(q)/q$.

For fixed residues $(t,b)=(q\bmod P,a_q\bmod P)$, admissibility means
$b+\ell t\in S$. Writing $d=(t,P)$, let $f(t,b)$ be the same survivor
fraction. Then
$$
 \sum_{\substack{b\bmod P\\b+\ell t\in S}}\frac1{f(t,b)}
 =\frac Pd\,\#\{\text{nonempty }S\text{-fibers modulo }d\}
 \le P.
 \tag{3}
$$
The equality holds because $d\mid t$: in each nonempty residue fiber,
there are exactly $|S\cap[b]_d|$ admissible values of $b$, each with
reciprocal cost $(P/d)/|S\cap[b]_d|$.

For fixed $P$, the pairs
$(q\bmod P,\lfloor\theta q\rfloor\bmod P)$ have frequency $1/P^2$.
To see this, write $q=t+Pm$: the second residue is determined by which
of the $P$ equal intervals contains
$\{\theta m+\theta t/P\}$. Irrational rotation is equidistributed,
as follows from the geometric sums of its nonconstant Fourier characters.
Consequently (3), summed over $t$, gives
$$
 \sum_{\substack{Q\le q<2Q\\a_q+\ell q\bmod P\in S}}
                   \frac1{f(q)}\le Q+o_{P,\theta}(Q).
 \tag{4}
$$
The period is held fixed when taking this limit.

Let $m_Q=|D\cap[Q,2Q)|$. Cauchy--Schwarz and (4) imply
$$
 \sum_{q\in D\cap[Q,2Q)}f(q)
 \ge\frac{m_Q^2}{Q+o_{P,\theta}(Q)}.
$$
The nonnegative function
$Z_Q=\sum_{q\in D\cap[Q,2Q)}\mathbf1_{C_q\setminus U_F}$
has support of measure at most $\tau_F$ and second moment at most
$C_\theta$. Thus
$$
 \frac{m_Q^2}{2Q(Q+o_{P,\theta}(Q))}
 \le\mathbb EZ_Q\le\sqrt{C_\theta\tau_F},
$$
and hence
$$
 \limsup_{Q\to\infty}\frac{m_Q}{Q}
 \le(4C_\theta\tau_F)^{1/4}.
$$
Now exhaust $D$ by finite prefixes, so $\tau_F\to0$. Dyadic block
densities tend to zero, proving $d(D)=0$. Since $r_q\ge q$, the endpoint
set also has natural density zero.

## Extension to Brjuno slopes: proved

Let $b_n$ be the continued-fraction denominators of an irrational
$0<\theta<1$. The same natural-nullity conclusion holds under the weaker
hypothesis
$$
 \mathcal B(\theta):=\sum_{n\ge0}\frac{\log b_{n+1}}{b_n}<\infty.
 \tag{B}
$$
This is the Brjuno condition. In particular, it holds for every
irrational of finite irrationality exponent.

The only new ingredient needed in the preceding proof is
$$
 \mathbb E\left(\sum_{Q\le q<2Q}
                  \mathbf1_{[\lfloor\theta q\rfloor]_q}\right)^2
 \le C(1+\mathcal B(\theta)),
 \tag{6}
$$
with an absolute constant $C$. Subfamilies obey the same bound by
pointwise domination. We prove (6) next.

For compatible distinct $q,r\in[Q,2Q)$, write $g=(q,r)$ and
$k=|q-r|/g$. As above,
$$
 k<Q/g,\qquad \|k\theta\|<1/g,
$$
and at most $4Q/g$ ordered pairs correspond to fixed $g,k$. Summing
their contributions $g/(qr)\le g/Q^2$ and then interchanging $g,k$
gives
$$
 \mathbb EY_Q^2\le1+4S_\theta(Q),\qquad
 S_\theta(Q)=\sum_{k\le Q}
             \min\left(\frac1k,\frac1{Q\|k\theta\|}\right).
 \tag{7}
$$

Partition $k\le Q$ into dyadic blocks $T\le k<2T$, truncated at $Q$,
and take the largest convergent denominator $b=b_n\le T$. Fractional
parts in any block of at most $b$ consecutive integers are circularly
separated by more than $1/(2b)$. Here is a short verification of the
continued-fraction fact used in that assertion. Consecutive convergent
vectors $(b_{n-1},p_{n-1})$ and $(b_n,p_n)$ form an integer basis, and
their errors $\delta_{n-1}=b_{n-1}\theta-p_{n-1}$ and
$\delta_n=b_n\theta-p_n$ have opposite signs. Write any integer pair
$(h,m)$ in this basis. If $0<h<b_n$, its coefficients cannot both be
nonnegative with a positive coefficient at $b_n$, nor both be
nonpositive. Opposite nonzero signs make the two error terms have the
same sign, with absolute sum at least $|\delta_{n-1}|$. The remaining
case is a positive multiple of the previous vector, which has the same
lower bound. Thus $\|h\theta\|\ge|\delta_{n-1}|$ for $0<h<b_n$.
Writing the continued-fraction tail after the $n$th convergent as $u>1$
gives
$$
 |\delta_{n-1}|=\frac{u}{b_nu+b_{n-1}}
 >\frac1{b_n+b_{n-1}}\ge\frac1{2b_n}.
$$
The case $b=1$ is vacuous. Initial repeated denominator $1$ may simply
be omitted when selecting the largest denominator.

Partition a dyadic block into at most $2T/b$ consecutive blocks of at
most $b$ integers. The separation just proved implies, for
$0<u\le1/2$,
$$
 F_T(u):=\#\{T\le k<\min(2T,Q+1):\|k\theta\|\le u\}
 \le8Tu+\frac{2T}{b}.
 \tag{8}
$$
For $T\le Q/2$, integrate the distribution function of
$\min(1/T,1/(Q\|k\theta\|))$ to obtain
$$
 \begin{aligned}
 S_T
 &\le\frac{2T}{Q}+
       \frac1Q\int_{T/Q}^{1/2}\frac{F_T(u)}{u^2}\,du\\
 &\le\frac{2T}{Q}+
       \frac{8T}{Q}\log(Q/T)+\frac2b.
 \end{aligned}
 \tag{9}
$$
For $T>Q/2$, the same upper bound follows from $S_T\le1$.
The first two terms in (9) sum to an absolute constant over dyadic
$T$. A denominator $b_n$ is selected only for $b_n\le T<b_{n+1}$,
so
$$
 \sum_{T\text{ dyadic}}\frac1{b(T)}
 \le\sum_n\frac{1+\log_2(b_{n+1}/b_n)}{b_n}
 \ll1+\mathcal B(\theta).
$$
The harmless sum $\sum1/b_n$ is absolutely bounded, because
$b_{n+2}\ge2b_n$. Equations (7)--(9) prove (6).

The preceding period-independent reciprocal-cost argument uses only
irrational equidistribution apart from the second moment. Replacing
$C_\theta$ by $C(1+\mathcal B(\theta))$ in that argument therefore gives
$$
 \limsup_{Q\to\infty}\frac{|D\cap[Q,2Q)|}{Q}
 \le\bigl(4C(1+\mathcal B(\theta))\tau_F\bigr)^{1/4}.
$$
Exhausting $D$ by finite prefixes proves natural nullity. The same proof
allows an added fixed integer $c$ in $a_q=\lfloor\theta q\rfloor+c$:
compatibility differences are unchanged and the residue-pair distribution
is merely translated. These are normalized residues for all sufficiently
large $q$; discarding the remaining finite set does not affect density.
Finitely many such perturbations or slopes satisfying (B) are handled by
partitioning the selected endpoints into finitely many subfamilies.

To check the finite-irrationality-exponent assertion, an inequality
$|\theta-a/b|\ge c b^{-M}$ for sufficiently large denominators, together
with the convergent estimate $|\theta-p_n/b_n|<1/(b_nb_{n+1})$, gives
$b_{n+1}\le c^{-1}b_n^{M-1}$. Thus
$\log b_{n+1}=O(\log b_n)$, and the at-least-Fibonacci growth of $b_n$
makes (B) converge.

### Why the remaining irrational logarithmic case is not settled

For a convergent $A/b$, its approximation has error less than
$1/(b b_{\rm next})$. For $q<b_{\rm next}$ this gives the same floor as
$Aq/b$, except that $\theta<A/b$ subtracts one when $b\mid q$.
This is an exact reduction of the long approximation epoch to finitely
many rational patterns. It does not give a uniform estimate independent
of $b$. The verified rational-pattern proofs have denominator-dependent
losses, whereas (7) can already grow with $(\log Q)/b$ inside such an
epoch. No estimate bridging those regimes has been proved. In particular,
the Brjuno theorem does not establish logarithmic endpoint nullity for
every irrational slope.

## Irrationality alone does not give natural nullity

There is a Liouville number $\theta\in(1/4,1/2)$ and a globally private
family
$$
 r_q=q+\lfloor\theta q\rfloor,\qquad q\le r_q<2q,
$$
whose endpoint set has upper natural density at least $1/16$ but
logarithmic density zero. Its full footprint can be arbitrarily small.
This does not contradict logarithmic endpoint nullity.

For a fixed rational slope $A/b$, its full dyadic block union obeys
$$
 \mu\left(\bigcup_{Q\le q<2Q}[\lfloor Aq/b\rfloor]_q\right)
 \le b^2\mu(M([Q,2Q)))\longrightarrow0.
 \tag{5}
$$
Indeed every hit satisfies $q\mid bn+t$ for some $0\le t<b$.
The Haar measure of each affine preimage is at most $b$ times the
multiples-union measure, because multiplication by $b$ maps Haar
probability onto normalized Haar measure on $b\widehat{\mathbb Z}$.
The multiples-window limit is already proved in
[common-shift blocks](common_shift_blocks.md).

Fix $0<\varepsilon<1/4$. Construct increasing rational approximants
$\theta_j=A_j/b_j$ inside nested small intervals in $(1/4,1/2)$,
with $b_j\to\infty$. When the earlier selected cylinders have common
period $P$, require $(A_j+b_j,P)=1$. Such rationals are dense: take
$b_j$ divisible by $P$ and $A_j\equiv1\pmod P$.

Choose a sufficiently large dyadic $Q_j$ that the block footprint in
(5) is below $\varepsilon2^{-j}$, that $Q_j\gg b_jP$, and that
$Q_j/4-1$ exceeds every earlier endpoint. Among
$Q_j\le q<5Q_j/4$, retain endpoints
$q+\lfloor\theta_jq\rfloor$ avoiding the earlier full union.
Their residues modulo $P$ are uniform over a period $b_jP$: increasing
$q$ by $b_j$ increases the endpoint by $A_j+b_j$, a unit modulo $P$.
Since the earlier union has measure at most $\varepsilon$, at least
$Q_j/8$ endpoints can be retained for sufficiently large $Q_j$.

Their diameter is less than $Q_j$, so their classes are private within
the block. Every new least positive representative is greater than all
earlier endpoints, establishing reverse-direction privacy as well.

After choosing this block, take the next closed approximation interval
strictly to the right of $\theta_j$ and inside
$$
 \left(\theta_j,\theta_j+
       \min\{1/(2b_jQ_j),b_j^{-j}\}\right),
$$
also inside the preceding approximation interval. The limit $\theta$
therefore satisfies the indicated one-sided bounds for every $j$.
For $q<2Q_j$, changing the slope by less than $1/(2b_jQ_j)$ cannot
change the floor: the next rational integer boundary is at distance
at least $1/b_j$. The strict one-sided approximations with unbounded
denominators make the limit irrational and Liouville.

All constructed cylinders and endpoints thus persist for this single
$\theta$. Each block has at least $Q_j/8$ endpoints below $2Q_j$, so
$\overline d(E)\ge1/16$. Its block footprints are summable; the
[summable-footprint endpoint lemma](compression_and_blocks.md#summable-footprints-and-selected-endpoints-proved)
gives $\operatorname{ld}(E)=0$.

The positive theorem's Diophantine hypothesis therefore cannot simply be
replaced by irrationality if its **natural-density** conclusion is retained.
Neither construction resolves logarithmic nullity for general private
endpoints or controls unbounded-quotient first kills.
