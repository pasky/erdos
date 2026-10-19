---
name: research/erdos_25/unresolved_estimates
desc: Unresolved uniform-tail and endpoint targets, with exact obstructions to sharper claims.
tags: [open-questions, obstructions]
sources: []
created: 2026-09-21T22:54:02Z
updated: 2026-10-14T00:26:52Z
---


# research/erdos_25/unresolved_estimates

***

## A refuted finite Dirichlet inequality

For a finite distinct-modulus singleton family, let $B$ be its delayed
union and $\beta$ the density of its full periodic union. The assertion
$$
\sum_{n\in B}n^{-s}\le\beta\zeta(s)\qquad(s>1)
\tag{D}
$$
would imply the general problem positively. Indeed, monotone convergence
over finite families bounds the normalized infinite Dirichlet series above
by $\beta_\infty=\lim\beta_k$, while each fixed finite prefix supplies the
matching lower limit as $s\downarrow1$. The Hardy–Littlewood/Karamata
Tauberian theorem for nonnegative coefficients then gives logarithmic
density $\beta_\infty$ for the excluded union. Equivalently one applies the
Laplace–Stieltjes form to
$\sum_{\log n\le t,n\in B}1/n$.
The analogous Tauberian passage is the one used in the Davenport–Erdős
1936 proof, whose Theorem 1(a) proof was checked in the supplied full source.
However, the [prime-constellation construction](finite_sharp_counterexamples.md)
now refutes (D) for finite distinct prime families and $s>1$ arbitrarily
close to $1$. The implication above remains correct, but (D) is not an
available route to the problem.

For $s\ge2$, (D) is elementary and does not approach the missing limit.
If $Q$ is the least modulus, then $B\subseteq[Q,\infty)$ and
$\beta\ge1/Q$. Also $Q\sum_{n\ge Q}n^{-s}$ decreases with integer $Q$:
its consecutive difference is
$\sum_{n\ge Q+1}n^{-s}-Q^{1-s}\le0$, by the integral estimate for $s\ge2$.
Its value at $Q=1$ is $\zeta(s)$, proving (D) in this range.

The stronger normalized compression comparison with the zero classes is
false. Take moduli
$$
D=\{2,3,5,7,11,13,25\}
$$
with zero residues except $4\pmod{25}$, and take $X=29$. For the zero union
$M=M(D)$,
$$
d(M)=\frac{809}{1001},\qquad
H_M(29)=\frac{29970107}{10810800}.
$$
The shifted class adds just $29$ below $X$, and adds periodic density
$48/5005$. Exact subtraction gives
$$
\frac{H_M(29)+1/29}{809/1001+48/5005}
-\frac{H_M(29)}{809/1001}
=\frac{41902022}{21605821425}>0.
$$
This refutes that normalized comparison, not (D).

Nor can (D) be proved separately for every first-kill increment. The old
classes $0\pmod2$, $0\pmod3$, $1\pmod4$, $5\pmod6$ leave only $7\pmod{12}$.
Adding $0\pmod7$ has incremental periodic density $1/84$, but its first-kill
set contains $7$, and $1/49>\zeta(2)/84$.

## Coherent quotient sieves can also have large harmonic spikes

The following tempting bound is false:
$$
H_S(Y)\ll d(S)\log(zY+2)
\tag{F}
$$
for all coherent finite sieves $S=\{t\ge1:t\not\equiv\alpha\pmod d
\ (d\in D)\}$ with $D\subseteq[2,z]$.
Coherence alone does not supply the missing first-kill charge.

**Proof of failure.** Set $z=Y=N$ and take $D$ to be the primes at most $N$.
For $p=2,3$, choose the forbidden residue uniformly modulo $p$.
For every prime $p\ge5$, independently choose it uniformly from
$$
R_p=\{\lceil\sqrt p\rceil,\ldots,p-1\}.
$$
CRT realizes every resulting selection as one common integer $\alpha$.
Regardless of the selection,
$d(S)=\prod_{p\le N}(1-1/p)$.

For a fixed integer $t$, a prime $p>t^2$ cannot remove it, since its allowed
forbidden residues all exceed $t$ and $p>t$. For the other primes the
hitting probability is at most $1/(p-\lceil\sqrt p\rceil)$.
The infinite product
$$
c_0=\prod_{p\ge5}
\frac{1-1/(p-\lceil\sqrt p\rceil)}{1-1/p}
$$
is strictly positive: every factor is positive, and each is
$1-O(p^{-3/2})$. Independence and the classical Euler-product bound
$\prod_{p\le x}(1-1/p)^{-1}\ll\log(2x)$ give
$$
\Pr(t\in S)\ge
c_0\prod_{p\le\max(3,t^2)}(1-1/p)
\gg\frac1{\log(t+2)}.
$$
Consequently $\mathbb EH_S(N)\gg\log\log N$, so some coherent selection has
that harmonic mass. On the other hand,
$\prod_{p\le N}(1-1/p)^{-1}\ge H_N$, since every integer at most $N$ is
$N$-smooth. Therefore $d(S)\log(N^2+2)=O(1)$, contradicting (F).
The Euler-product upper bound was checked in the Davenport–Erdős 1951
source before equation (12). $\square$

This mechanism is related to the original reciprocal-admissible-set
construction in [this mathematical discussion](https://math.stackexchange.com/questions/4976415/is-the-function-gn-displaystyle-sum-k-1-pin-1-left-frac1n-p);
the argument above was independently checked in full.

It is realizable as an actual coherent first-kill quotient. After the
prime moduli $p\le N$, choose any prime $Q>N$ and prescribe
$$
\alpha\equiv0\pmod Q,\qquad \alpha\equiv Qb_p\pmod p,
$$
where $b_p$ are a successful selection from the construction.
At the top modulus $Q$, every earlier modulus is active and the first-kill
set is exactly $\{Qt:t\in S\}$. Its density is $d(S)/Q$, but its harmonic
mass up to $QN$ is $H_S(N)/Q\gg(\log\log N)/Q$.
Choosing $Q<2N$ by Bertrand's postulate makes the putative bound
$e_Q\log(QN)$ only $O(1/Q)$. This is not an infinite counterexample:
repeating an ever larger prime sieve forces the full survivor density to zero.

## Bounded-quotient first kills: still unproved in general

For fixed $K$, it would be useful to establish logarithmic density zero for
$$
\bigcup_i(E_i\cap[n_i,Kn_i]).
$$
For first endpoints, this is a shifted primitive-set question: selected
$r_i\in[n_i,2n_i)$ must satisfy
$r_j\not\equiv r_i\pmod{n_i}$ whenever $i<j$.
Primitive moduli and the structured residue families in
[structured cases](structured_residues.md) are controlled, but no general
endpoint theorem was proved.

A new [recurrence obstruction](recurrence_obstruction.md) shows that
finite-horizon privacy is much weaker: a set of natural density arbitrarily
close to one can assign distinct $q(r)\le r<2q(r)$ so that all its first
$c\sqrt{\log r}$ positive progression steps miss the set. Every assigned
progression nevertheless returns eventually. Thus infinite privacy cannot
be replaced by a bounded-return estimate or by that particular growing
return horizon.

A cutoff-preserving compression to primitive subsets is already false.
The pairs
$$
(4,6),(5,5),(6,8),(7,7),(8,13),(9,9),(10,11),(12,12),(16,16)
$$
satisfy these first-kill conditions. The endpoint set has reciprocal sum
larger by $1/48$ than the largest reciprocal sum of a primitive subset of
$[4,16]$, attained by $\{4,5,6,7,9,11,13\}$.
Indeed the difference replaces $1/4$ by $1/8+1/12+1/16$.
For the primitive optimum, $5$ outweighs any compatible selection from
$\{10,15\}$, then $4$ outweighs any compatible selection from
$\{8,12,16\}$; next $6$ outweighs $12$ and $7$ outweighs $14$.
The remaining isolated available integers are $9,11,13$.
This only rules out this particular compression, not the endpoint statement.

## Further checks after renewed work

Even **coherent, pairwise-coprime** moduli do not permit harmonic compression
to zero residues. With $D=\{2,3,5\}$, common shift $\alpha=12$, and $X=17$,
the delayed system $0\pmod2$, $0\pmod3$, $2\pmod5$ loses $5$ and gains
$7,17$ relative to $M(D)$. Consequently
$$
H_B(17)-H_{M(D)}(17)=\frac17+\frac1{17}-\frac15=\frac1{595}>0.
$$
Both periodic union densities are $11/15$. This refutes the additive
comparison $H_B-\beta H_X\le H_{M(D)}-d(M(D))H_X$ as well as the normalized
comparison, even under coherence. It does not refute the direct possible
bound $H_B\le\beta H_X$.

### Exact protected-root accounting

For any increasing-modulus family, put
$$
C_i=[a_i]_{n_i},\qquad F_i=C_i\setminus\bigcup_{j<i}C_j,
\quad 0\le a_i<n_i.
$$
On positive integers, $E_i=F_i\cap[n_i,\infty)$. The only possible positive
point of $F_i$ below $n_i$ is $a_i$. Therefore, if
$$
R=\{a_i>0:a_i\notin\bigcup_{j<i}C_j\},
$$
then the delayed excluded union is exactly
$$
B=\left(\bigcup_i C_i\right)\cap\mathbb N\ \setminus R.
$$
Indeed every integer in the full union has a first full covering class;
if that class is inactive, all later classes are also inactive. This
identity is valid for infinite families as well as finite ones.

For a finite family, the direct harmonic bound is equivalently
$H_U(X)-\beta H_X\le H_R(X)$.
The [finite prime-constellation construction](finite_sharp_counterexamples.md)
refutes this exact compensation inequality. The identity itself remains
valid, including with repeated moduli; a sublogarithmic-error variant has
not been proved or refuted here.

### Dirichlet compression to zero residues fails as well

The preceding finite harmonic counterexample does not by itself settle a
comparison of Dirichlet series. However, the quotient-sieve construction
above gives a separate rigorous obstruction: for some $s>1$ arbitrarily
close to $1$, even a coherent pairwise-coprime finite family can have
$$
D_B(s)-\beta\zeta(s)
> D_{M(D)}(s)-d(M(D))\zeta(s),
\qquad D_E(s)=\sum_{n\in E}n^{-s}.
\tag{3}
$$
This is still not a counterexample to the direct global bound (D).

Keep the old zero classes at primes $p\le N$. In a quotient sieve, set
$b_2=b_3=0$ and independently choose
$b_p\in\{\lceil\sqrt p\rceil,\ldots,p-1\}$ for $p\ge5$. Let
$S_N=\{t\ge1:t\not\equiv b_p\pmod p\ (p\le N)\}$.
The previously proved product estimate now gives, for $(t,6)=1$,
$$
\Pr(t\in S_N)\gg1/\log(t+2)
$$
uniformly in $N$. By Tonelli,
$$
\mathbb E D_{S_N}(s)
\gg\sum_{(t,6)=1}\frac{t^{-s}}{\log(t+2)}.
$$
The right side tends to infinity as $s\downarrow1$: at $s=1$ it diverges,
as is seen by restricting to the two reduced residue classes modulo $6$,
and monotone convergence applies. Choose $s$ close enough that the lower
bound exceeds $3$. For this fixed $s$, choose $N$ sufficiently large that
$$
D_{S_N^0}(s)=\zeta(s)\prod_{p\le N}(1-p^{-s})<2,
\quad S_N^0=\{t:(t,\prod_{p\le N}p)=1\}.
$$
The Euler product tends to $1/\zeta(s)$, so this choice is possible. A
realization of the $b_p$ has $D_{S_N}(s)>3$.

Writing $P=\prod_{p\le N}p$, CRT supplies arbitrarily large positive $q$
with
$$
q\equiv1\pmod6,
\qquad q\equiv-6b_p^{-1}\pmod p\quad(5\le p\le N).
$$
These congruences force $(q,P)=1$. Choose $q>\max(N,6)$ and append the
single class $6\pmod q$. Its delayed first-kill set is
$\{qt+6:t\in S_N\}$, because all earlier prime moduli are active there.
Its Dirichlet contribution is
$$
q^{-s}\sum_{t\in S_N}(t+6/q)^{-s}.
$$
Along the permitted arbitrarily large $q$, dominated convergence makes the
inner sum tend to $D_{S_N}(s)>3$. Appending $0\pmod q$ instead contributes
$q^{-s}D_{S_N^0}(s)<2q^{-s}$. Thus the former contribution is larger for
large enough $q$. The completed periodic densities of these two systems
are equal, since $q$ is coprime to $P$, proving (3). All moduli are distinct
and pairwise coprime, so the systems are coherent by CRT.

The old zero-sieve deficit has not been shown to be overcome by this small
positive increment. This argument rules out additive and normalized
Dirichlet comparison to the zero system, not the global inequality (D).

### Two additional endpoint and charging checks

For a first-endpoint family $r_i\in[q_i,2q_i)$ satisfying the avoidance
condition above, write $\alpha=\overline{\operatorname{ld}}(\{r_i\})$ and
let $\beta$ be the limiting periodic density of its full congruence unions.
The proved endpoint compression bound gives $\alpha\le\beta$. Avoidance
of every fixed prefix gives $\alpha\le1-\beta$, hence $\alpha\le1/2$.
If every $r_i\ge\lambda q_i$, then the first bound sharpens to
$\lambda\alpha\le\beta$, and $\alpha\le1/(1+\lambda)$.
These bounds do not imply zero logarithmic density.

Cylinder containment antichains alone cannot prove that zero-density
conclusion. Let $D=\{q\ge2:\sigma(q)<2q\}$. For every $q\in D$, recursively
choose a residue avoiding all earlier classes whose moduli properly divide
$q$. This is possible because
$$
\sum_{\substack{d\mid q\\1<d<q}}\frac1d
=\frac{\sigma(q)}q-1-\frac1q<1.
$$
Classes with comparable selected moduli are therefore disjoint. Yet $D$
has lower natural density at least $2-\zeta(2)>0$: each nondeficient
integer contributes at least one to $\sigma(n)/n-1$, whereas
$$
 \frac1N\sum_{n\le N}\left(\frac{\sigma(n)}n-1\right)
 =\sum_{2\le d\le N}\frac{\lfloor N/d\rfloor}{Nd}
 \le\zeta(2)-1.
$$
Deleting the single integer $1$ has no effect on the lower density.
The construction imposes no avoidance of earlier *nondividing* moduli and
is not an endpoint counterexample.

Finally, a positive global survivor density cannot repair a false
individual first-kill estimate. Replacing each $(q,a)$ in a spike example
by $(Mq,Ma)$ confines all exclusions to $M\mathbb N$ and leaves survivor
density at least $1-1/M$, while multiplying both first-kill densities and
harmonic masses (with rescaled cutoff) by $1/M$. The local discrepancy
persists; a successful charge must account for the relevant fibers rather
than only the total survivor density.

### A containment antichain can use every sufficiently large modulus

Section 6.1 of the [[research/erdos_25/independent/profinite_shifts_and_long_windows|third independent record]]
strengthens the deficient-modulus example above. Set $N=10^{16}+1$.
For every successive integer $q\ge N$, choose $a_q\pmod q$ outside
all earlier classes whose moduli properly divide $q$. Such a residue
exists: otherwise those finitely many distinct divisor-modulus classes
would cover every residue modulo $q$, and hence all integers. This
contradicts [Hough's Theorem 1](../../../library/covering_systems/hough_2015_solution_minimum_modulus_problem_covering_systems/_index.md),
which bounds the least modulus of a finite distinct covering system by
$10^{16}$. The digest and the actual theorem statement were checked.

Classes with comparable selected moduli are therefore disjoint, although
every modulus $q\ge N$ occurs and $\sum_{q\ge N}1/(q\log q)$ diverges.
Dilating $(q,a_q)$ to $(Mq,Ma_q)$ confines the full union to
$M\widehat{\mathbb Z}$ and gives modulus natural density $1/M$.
In fact both its full Haar union and its delayed union have density
$1/M$: before dilation, the selected primes alone have divergent
reciprocal sum and hence delayed deletion density one.

Thus even this particularly dense containment antichain is not a
counterexample. Containment avoidance says nothing about earlier
nondividing moduli. The [two-colored construction](binary_colored_private_witnesses.md)
supplies a different, stronger profinite-private phenomenon, but neither
construction supplies comparable positive integer private witnesses.

## Later progress and obstructions

The finite [bounded-rank estimate](bounded_prime_rank.md) proves natural
density for arbitrary residues when $\Omega(n_i)$ is uniformly bounded.
It also proves natural density for coherent residues with bounded
$\omega(n_i)$, allowing unbounded exponents. The general coherent case
and the arbitrary unbounded-rank singleton case remain unresolved.

The accompanying [rank and moment obstructions](rank_and_moment_obstructions.md)
rule out two extensions of that proof. Divisor-face capacities, even with
their exact harmonic cutoffs and primitive distinct moduli, do not imply
rank-independent control. The usual first-kill Haar potential does not
have any uniform $L^p$ bound for $p>1$, even for zero residues.
The [transversal-prime argument](transversal_prime_groups.md) separately
rules out one coherent high-rank construction suggested by those abstract
capacity examples.

### Private-witness reduction for endpoints

For $q_i\le r_i\le Kq_i$ satisfying
$r_j\not\equiv r_i\pmod{q_i}$ whenever $i<j$, the endpoint set partitions
into at most $\lceil K\rceil$ sets $R_c$ such that
$$
 [r_i]_{q_i}\cap R_c=\{r_i\}\quad\text{whenever }r_i\in R_c.
$$
Indeed, later endpoints never lie in the $i$th class. Every earlier
endpoint is at most $Kq_i$, so that class contains at most
$\lceil K\rceil$ endpoints in total, including $r_i$.
Greedily color the indices, avoiding the colors of earlier endpoints
in the current class. There are at most $\lceil K\rceil-1$ forbidden
colors. Earlier classes automatically avoid the new endpoint.
Thus the endpoint-nullity question reduces to a distinct-modulus family
whose assigned classes each have a private endpoint. Nullity for that
private-witness problem is still unproved.

The remaining private-witness problem reduces further to
$q_i\le r_i<2q_i$. Partition by the finitely many values
$t=\lfloor r_i/q_i\rfloor$, and in each part replace $q_i$ by $tq_i$.
The new moduli are distinct, the new cylinders are contained in the old
ones, and $tq_i\le r_i<2tq_i$. Thus the private-witness property is preserved.

### Private positive witnesses can still have very small individual increments

For $L\ge3$, take
$$
 (q_j,r_j)=(2^j,3\cdot2^{j-1})\quad(1\le j\le L),
 \qquad (Q,R)=(2^L+1,2^{L+1}).
$$
All witnesses lie in $[q,2q)$, and all moduli are distinct and increasing.
The dyadic cylinders are the disjoint classes of exact valuations
$v_2(n)=j-1$; the last witness $R$ avoids them. The last cylinder contains
no earlier witness: if $Q\mid R-r_j$, then $0<R-r_j<2Q$ forces
$R-r_j=Q$, or $r_j=2^L-1$, impossible for $L\ge3$. Thus every witness
is private in the entire finite family.

Nevertheless the final first-kill density is
$$
 e_Q=\frac1{Q2^L},
$$
because the old survivors are $0\pmod{2^L}$ and $\gcd(Q,2^L)=1$.
In particular no uniform individual lower bound
$e_i\gg1/(q_i\log q_i)$ holds even for globally private positive
endpoints. This does not disprove endpoint nullity or any appropriately
amortized charge; it only rules out this individual charging argument.

### Purely profinite private witnesses are insufficient

For every prime $p$, $e\ge1$, and $1\le j<p$, consider
$$
 C_{p,e,j}=[jp^{e-1}]_{jp^e}.
$$
The moduli are globally distinct. Give this cylinder the profinite witness
whose $p$-adic coordinate is $jp^{e-1}$ and whose other prime coordinates
are zero. Each cylinder contains exactly its own witness: another prime's
coordinate is zero, and for the same prime the valuation and next digit
distinguish $(e,j)$. These witnesses have exactly one accumulation point,
$0$. Indeed outside any neighborhood $[0]_m$ there are only finitely many
of them.

Their modulus set nevertheless has positive lower logarithmic density:
$$
 \sum_{\substack{q\le X\\q=jp^e,\ j<p}}\frac1q
 \ge\sum_{p\le\sqrt X}\frac{H_{p-1}}p
 \ge\frac{\log2}{2}\log X-O(1).
$$
For the last estimate, $H_{p-1}\ge\log p$ and
$\vartheta(y)\ge y\log2-O(\sqrt y\log y)$ suffice by partial summation.
The latter follows elementarily because the central binomial coefficient
divides $\operatorname{lcm}(1,\ldots,2n)$, while prime-power terms beyond
the first contribute $O(\sqrt y\log y)$ to the logarithm of that lcm.

Every finite subsystem also has positive integer private witnesses by CRT,
but with no required size bound. There are no positive integer private
witnesses for this entire infinite system: every positive $n$ belongs to
$C_{p,1,n}$ for every prime $p>n$. Thus compactness and abstract private
witnesses cannot replace the quantitative requirement that the witnesses
be positive integers comparable to their moduli. This is not an endpoint
counterexample.

### Positive survivor measure does not make essential moduli sparse

The preceding profinite-private example also refutes the stronger
proposed assertion that positive survivor Haar measure forces the set
of moduli with nonempty full first-kill cells to have logarithmic
density zero. Replace each pair $(q,a)$ in that example by
$(2q,2a)$. Distinctness and all private profinite witnesses are
preserved by dilation; hence every finite first-kill cell is nonempty.
All cylinders now lie in the even fiber. The original family has
full Haar union measure one already from the classes $1\pmod p$
(take $e=j=1$), so the dilated family's survivor Haar measure is
exactly $1/2$. Its modulus set still has positive lower logarithmic
density. This is not a family of comparable integer private endpoints,
and supplies no density counterexample.

### Even conditional contraction for a new prime fails

Take old zero classes at every prime at most $53$, append $2\pmod{59}$,
and put $X=179$. The new first kills below $X$ are $61,179$, so
$$
 59H_E(179)=\frac{14160}{10919}.
$$
The old survivors are $1$ and the $25$ primes from $59$ through $179$.
Grouping these primes successively into groups of $5,10,10$ gives
$$
 H_{A_{\rm old}}(179)
 \le1+\frac5{59}+\frac{10}{79}+\frac{10}{131}
 =\frac{786236}{610591}<\frac{14160}{10919}.
$$
Thus the tempting conditional contraction
$H_E(X)\le H_{A_{\rm old}}(X)/59$ is false. Its Haar analog is exact
because the new prime is coprime to the old moduli. All moduli here are
distinct primes, and the residues are coherent by CRT.

### A limitation of unconditioned weak-type bounds

Failure of a uniform estimate
$$
 \sup_{\substack{\text{finite singleton families }F\,,\ \mu(U_F)\le b\\X\ge2}}
 \frac{H_{B_F}(X)}{H_{\lfloor X\rfloor}}\longrightarrow0
 \qquad(b\downarrow0)
$$
would supply small-footprint epochs for a counterexample: a footprint
less than $1/Y$ automatically has every modulus greater than $Y$, so
successive anomalous blocks can be installed beyond any recovery cutoff.

The converse has **not** been established. Conditioning on a fixed old
period $P$ expands a tail class into classes modulo $\operatorname{lcm}(P,q)$.
This introduces a bounded multiplicity depending on $P$, and changes
activation by a factor at most $P$. An unconditioned bound with modulus
of continuity $f(b)$ would therefore give a bound with a factor depending
on $P$. As the old prefix grows, $P$ may grow arbitrarily faster than its
omitted Haar measure decreases. Hence this localization does not by itself
turn $f(b)\to0$ into the required conditioned-tail theorem.

## Comparison with the first independent record

The [[research/erdos_25/independent/harmonic_bounds_and_common_shifts|independent investigation]]
was treated as unverified input, not as a replacement for the established
arguments. Its finite-truncation and summable cases, first-kill
decomposition, compression, and first-$K$-hit arguments agree with the proofs in
[basic reductions](basic_reductions.md) and
[compression and blocks](compression_and_blocks.md). Its dyadic
second-moment obstruction is also already covered there.

The main disagreement is substantive: its proposed sharp inequalities
(7.1) and (7.2) are **false**, not merely unproved. The established
[finite prime-constellation counterexamples](finite_sharp_counterexamples.md)
refute both. Small finite checks failing to find counterexamples do not
support retaining either estimate as a proof target. The weaker uniform
additive $o(\log X)$ harmonic target is still open.

The following checked additions were retained:

- Section 5's arbitrary-common-shift interval theorem is correct.
  [Common-shift blocks](common_shift_blocks.md) gives a finite bound and
  its stronger, uniform harmonic corollary for a single coherent dyadic
  block, including unbounded quotients. Accumulation across arbitrarily
  many blocks remains uncontrolled.
- Section 7's finite zero-residue Dirichlet sandwich is correct; a
  self-contained valuation proof is in
  [basic reductions](basic_reductions.md#a-quantitative-finite-dirichlet-comparison-for-multiples-proved).
- Section 8's affine-endpoint nullity is correct. Comparing its smooth-part
  argument with [structured residues](structured_residues.md#rational-congruence-patterns-without-coprimality)
  also removes the coprimality hypothesis from the fixed rational-translate
  theorem. General private-endpoint nullity remains unproved.

Section 8's deficient-modulus construction needs an arithmetic repair:
exclude modulus $1$, and count
$$
 \sum_{\substack{d\mid q\\1<d<q}}q/d=\sigma(q)-q-1<q.
$$
The displayed divisor-sum equality in the independent input is incorrect
as written. Its improved density bound $2-\zeta(2)$ is valid and has been
incorporated above. This only supplies a containment antichain, not the
avoidance of all earlier cylinders needed for endpoint nullity.

Finally, its failed attempts to refine Wang's reused moduli are superseded
by the proved [arbitrary-divisor-refinement bound](compression_and_blocks.md#every-divisor-refinement-of-a-wang-block-is-uniformly-small).
Its generalized-tower and biased-label ideas supply no verified new
construction. The former's synchronization difficulty is partially
quantified by [colored towers](colored_towers.md); neither mechanism
controls the general conditioned incremental footprint.

## Latest checked partial results

For coherent residues, [the power-cutoff argument](coherent_power_cutoff.md)
now gives a uniform bound for selected first-kill cells of total Haar
mass $\tau$, provided their moduli are at most $H^{1-\eta}$ on an interval
of length $H$: their relative count is
$O(1/(\eta\log(2/\tau)))$. This is a conditioned estimate with no
constant depending on an old period. It proves natural density for every
fixed power delay and for the original activation under the stated
reciprocal-shell sparsity criterion. The general near-diagonal layer is
not controlled.

For residues $\lfloor\theta q\rfloor$ with $\theta$ badly approximable,
[bounded-quotient first kills](irrational_slope_endpoints.md) have natural
density zero. A Liouville-slope construction shows that replacing badly
approximable by irrational in this natural-nullity theorem is false:
it gives globally private endpoints with positive upper natural density,
but logarithmic density zero. This does not refute the general logarithmic
endpoint target.

Finally, the [fixed-rank product obstruction](product_capacity_obstruction.md)
shows that divisor-face capacities alone remain insufficient even for
distinct primitive moduli with at most three distinct prime factors.
The bounded-$\omega$ question for actual arbitrary-residue systems is not
settled by these abstract weights. The later
[one-unbounded-prime-power argument](one_unbounded_prime_power.md)
does prove natural density for arbitrary singleton residues when
$\omega(q)\le2$. The subsequent
[squarefull-kernel truncation](squarefull_kernel_truncation.md)
proves natural density for all bounded-$\omega$ singleton systems,
and for the larger class with bounded exponent-one prime rank.
The abstract weights do not meet the additional arithmetic constraints
used in that proof.

## Comparison with the second independent record

The [[research/erdos_25/independent/bounded_quotient_blocks_and_recentering|independent investigation]]
was checked as unverified input. Its unresolved status agrees with the
current research, but several of its proposed targets have already been
refuted or its partial results strengthened. Its text is preserved
unchanged; references there to companion `notes/` and `research/` files
are not available in this research folder and are not used as evidence.

### Agreements and results already covered

Sections 1--4 agree with the established finite-truncation arguments,
finite compression, exact harmonic comparison for multiples, and the
sharpened bounded-quotient bound in [basic reductions](basic_reductions.md)
and [compression and blocks](compression_and_blocks.md). They concern
the total periodic footprint, not the incremental footprint inside an
old survivor set.

Section 7's counterexample to a uniform local large-quotient counting
bound is correct. Besicovitch's averaged dyadic-window theorem suffices
for its subsequence choice, but the established
[quotient-only natural obstruction](coherent_power_cutoff.md#a-quotient-only-natural-estimate-cannot-close-the-gap)
is stronger: the footprint tends to zero for all sufficiently large
base scales, primitive reduction is allowed, and the large quotients
can remain uniformly subpower. Thus this section adds no new theorem
and no logarithmic-density counterexample.

The Wang objections in Sections 4 and 8.1 are also correct. The existing
[arbitrary-divisor-refinement bound](compression_and_blocks.md#every-divisor-refinement-of-a-wang-block-is-uniformly-small)
already rules out a larger class of repairs, with no upper bound on
the multipliers or quotients. Biased labels and translated windows in
Sections 8.1--8.2 supply no checked new infinite construction.

### Sharp comparisons: false, not open

The finite harmonic target (5.1) and Dirichlet target (8.2) are both
**false**, by [finite sharp counterexamples](finite_sharp_counterexamples.md).
The [energy construction](energy_counterexample.md) additionally gives
an elementary harmonic refutation with unbounded excess. Failed small
searches in Section 9 do not support retaining these exact targets.

Their hypothetical sufficiency is correct: at cutoff $X$ only moduli
$q\le X$ are active, so an exact harmonic bound for that finite family
would squeeze the infinite union to its Haar candidate. For the
Dirichlet version, the nonnegative Laplace--Stieltjes Tauberian passage
already recorded at the start of this note is valid; it is not a further
unresolved step. The obstacle is the false finite premise. A uniform
additive $o(\log X)$ harmonic comparison remains open.

The example $(2,3,5)$ in Section 5 is already recorded above.
Section 6's $(2,3,35)$ example is also exact and has been retained in
[the harmonic-constant comparison](finite_sharp_counterexamples.md#an-elementary-recentering-obstruction-for-harmonic-constants).
It proves a strictly positive change in the asymptotic harmonic
constant and a Dirichlet recentering failure near $1$. The
stopped-coordinate model of Section 8.4 is valid, but this same example refutes
its proposed domination of the actual Dirichlet trace. The example's
constant is still below $\beta\gamma$; the separate changing-family
Dirichlet violations do not alone settle that fixed-family constant
question. No floating-point evidence is needed for these checks.

### Entropy, conditioning, and positive regimes

Section 8.3's entropy summation is valid. With
$S=\sum_{q_i\le X}e_i\le1$ and
$R=\sum_{q_i\le X}1/q_i\le H_{\lfloor X\rfloor}$, log-sum gives
$$
 \sum_{q_i\le X}e_i\log\frac1{q_i e_i}
 \le S\log(R/S)
 \le\log H_{\lfloor X\rfloor}+1/e.
$$
The zero-mass case is interpreted as zero. This checks the entropy
calculation in the [Chojecki source](../../../library/integer_sequences/chojecki_2026_truncated_congruence_sieves_erdos_problem_25/_index.md),
Lemma 5.2 and Corollary 5.3, read after its digest. It does not supply
the source's missing sublogarithmic charge, nor the different
[empirical first-kill entropy bound](rank_and_moment_obstructions.md#entropy-of-the-disjoint-potential-an-unresolved-stronger-target).
The tower discussion supplies no new amortized estimate.

The warning about period-dependent conditioning is still necessary for
general residues. For coherent systems, however, the later
[period-independent reduction](coherent_power_cutoff.md#an-unconditioned-finite-estimate-would-suffice-proved-reduction)
already overcomes that particular localization loss, conditional on
the still-unproved finite harmonic small-footprint estimate.

Sections 8.5--8.6 give correct positive cases, both subsumed by
[finite rational patterns](structured_residues.md). The abstract
[$S_M$-stability lemma](structured_residues.md#stability-under-multipliers-congruent-to-one)
has been checked and retained with a proof; it also allows repeated
moduli and arbitrary finite activation thresholds in its bounded-order
application. This is an alternative structural formulation, not a new
solution of the unrestricted singleton problem. No general conditioned
logarithmic-tail estimate has resulted from this review.

## Comparison with the third independent record

The [[research/erdos_25/independent/profinite_shifts_and_long_windows|independent investigation]]
was read as unverified input and compared with the established topical
arguments. Its mathematical text is preserved unchanged. Its linked
companion files are absent from this research folder; all additions below
have proofs here rather than relying on those links.

### Agreements and stronger existing results

Sections 2--4 agree with [basic reductions](basic_reductions.md) and
[compression and blocks](compression_and_blocks.md), including the
coefficient-one multiples inequality and bounded-witness nullity for
summable full footprints. The negative-integer-center correction in
Section 2.4 is correct and can be infinite: with every prime modulus
and center $-1$, every point $p-1$ is omitted by activation. Its primitive
exception argument proves logarithmic nullity. The density conclusion
is already subsumed by [finite rational patterns](structured_residues.md)
and [signed branch-separated centers](branch_separated_centers.md).

The Wang distinctness objection is correct. The established
[arbitrary-divisor-refinement bound](compression_and_blocks.md#every-divisor-refinement-of-a-wang-block-is-uniformly-small)
is stronger than the input's bounded-scale refinement obstruction and
handles unbounded multipliers and quotients. Section 5's original
common-shift estimate is also correct but has a narrower interval
range than [common-shift blocks](common_shift_blocks.md).

The tower and quotient-sieve discussion in Section 6.2 correctly keeps
the proposed global charge conjectural. None of the biased-label or
rare-progression-word heuristics in Section 6.5 supplies a verified
singleton epoch. The newer [conditioned endpoint blocks](conditioned_endpoint_blocks.md)
and [overlapping preparations](overlapping_parent_preparations.md)
go farther on finite preparations, but still lack a long active trace.

### Checked additions

The two briefly reported window calculations were proved from their
displayed mechanisms in [weighted prime-residue windows](weighted_prime_residue_windows.md).
For one dyadic block, with $r_p$ permitted residues at each selected
prime, the finite interval bound is
$$
 |U\cap I|\ll T/h+(T/Q+Q)m^2/h^2,
 \quad h=\sum_p\frac1{pr_p},\quad m=\#\{p\text{ used}\}.
$$
Keeping the modulus-window error makes this uniform in arbitrarily
large $T$. Truncation then proves the stronger harmonic bound
$\sup_X H_B(X)/H_{\lfloor X\rfloor}\le\min(1,C/\mathcal H)$
for the full prime-support parameter. Completing missing prime supports
with singletons gives $O(R/\log\log Q)$ when all local support sizes
are at most $R$. The input's power-law exponent
$\delta_*=0.086071\ldots$ is also verified, using two Bonferroni
truncations and a factorial moment. These results require only the
stated prime-level coherence, not coherence at higher prime powers.
They do not give an inverse theorem or a general conditioned-tail bound.

Other useful verified additions are the
[nearby-multiple injection failure](compression_and_blocks.md#nearby-multiple-injections-need-not-exist),
the [rough-window reciprocal support bound](compression_and_blocks.md#rough-moduli-in-a-fixed-power-range-have-small-reciprocal-cost),
and the [every-large-modulus antichain](#a-containment-antichain-can-use-every-sufficiently-large-modulus).
The [all-prime $(2,3,23)$ example](finite_sharp_counterexamples.md#an-all-prime-three-modulus-variant)
is an exact, smaller variant of the $(2,3,35)$
recentering obstruction. It refutes weighted comparison with zero
residues, not comparison with the full periodic density itself.

### Dirichlet targets and unsupported charges

The substantive disagreement is Section 7's status of the **exact**
finite Dirichlet bound: it is false, not open, by
[finite sharp counterexamples](finite_sharp_counterexamples.md).
The input's unsuccessful small searches do not alter that conclusion.
Its weaker uniform assertion
$$
 F_{\mathcal F}(s)/\zeta(s)\le d_{\mathcal F}+\eta(s),
 \qquad \eta(s)\to0\quad(s\downarrow1),
 \tag{U}
$$
remains unproved and unrefuted. Its sufficiency is correct: monotone
convergence over finite families and fixed-prefix lower bounds give
the normalized infinite Dirichlet limit, and the nonnegative
Laplace--Stieltjes Tauberian passage gives logarithmic density. The
threshold-sensitive inclusion--exclusion and digamma formulas in
Section 7.1 are correct for each fixed family; their remainder is not
uniform in the family and supplies no proof of (U).

The speculative reciprocal-cost bound
$H_B(X)\le\beta\log X+C\sum_q1/q$ has neither a proof nor a
refutation in these notes. The [energy example](energy_counterexample.md)
has reciprocal sum and harmonic excess of the same order; its failed
linear reciprocal charge concerns a different, entropy quantity.
[Prime-only unbounded excess](prime_additive_excess.md) likewise does
not refute this cost bound, because its old prime reciprocal sum grows.
Distinctness alone gives only $\sum_{q\le X}1/q\le H_{\lfloor X\rfloor}$,
not an $o(\log X)$ error. No new reduction is asserted here.

Section 7.4's decreasing-step observation is valid when its periodic
least-modulus function is defined on all integers. It gives no charging
estimate; the exact protected-root identity above and
[affine first-kill flow](affine_dynamics_and_traces.md) already expose
the missing transfer. The period-dependent conditioning warning
remains valid for general residues, whereas the established
[coherent conditioning reduction](coherent_power_cutoff.md#an-unconditioned-finite-estimate-would-suffice-proved-reduction)
does remove that particular loss in the coherent case.

### A finite epoch already refutes the multi-residue uniform analog

Section 7.3 correctly notes that one Wang block only gives a normalized
Dirichlet contribution of order $1/\log Q$. However, one need not
invoke an infinite multi-epoch construction to refute the multi-residue
analog of (U). A single finite epoch suffices.

Take the source's blocks with indices $j=a,\ldots,2a$. By
[Wang's Lemma 3.4](../../../library/integer_sequences/wang_2026_proposed_solution_erdos_problem_486/_index.md),
checked after its digest, their disjoint endpoint sets lie in
$[(11/10)2^j,(19/10)2^j]$, have size at least $(3/8)2^j$, and
are active. Each therefore has harmonic mass at least $15/76$.
Their combined periodic footprint is at most
$\sum_{j\ge a}\eta_j\to0$. Put $t=1/(a\log2)$. Every selected
endpoint satisfies $n^{-t}\ge e^{-3}$ for large $a$, so the delayed
finite union has
$$
 \frac{F_a(1+t)}{\zeta(1+t)}
 \ge\frac{15e^{-3}(a+1)}{76\zeta(1+t)},\qquad
 \liminf_{a\to\infty}\frac{F_a(1+t)}{\zeta(1+t)}
 \ge\frac{15e^{-3}}{76\log2}>0.
$$
This directly contradicts a uniform vanishing error for multiple
residues. The repeated-modulus obstruction remains, so it gives no
counterexample to the singleton version (U) or to Problem 25.

## Comparison with the fourth independent record

The [[research/erdos_25/independent/harmonic_capacity_and_narrow_windows|independent investigation]]
was checked as unverified input against the linked topical notes. Its
mathematical text is preserved unchanged. The review adds a two-class
positive result and a small moment certificate, but no general
conditioned-tail estimate or singleton counterexample. The auxiliary
files named by the input are absent from this research folder and were not
used as evidence.

### Sharp comparisons and the checked two-class boundary

The main disagreement is the status of Section 5's inequalities (H)
and (D): both are **false in general**, not open, by the established
[finite sharp counterexamples](finite_sharp_counterexamples.md).
The [energy example](energy_counterexample.md) independently refutes
(H) with unbounded additive excess. Failed finite searches do not
change either conclusion. A uniform sublogarithmic harmonic error,
or the vanishing normalized Dirichlet error (U) above, remains open.
The nonnegative Tauberian passage from an appropriate Dirichlet limit
to logarithmic density is already justified at the start of this note;
it is not the unresolved part of that route.

The input's **two-class Dirichlet proof is correct**. Moreover, its
intersection shift loss is a sub-sum of the larger-modulus shift loss,
so the argument works for every nonnegative decreasing summable weight
when the classes are compatible. This proves both sharp (H) and (D)
for families of at most two classes. The full proof and precise
weight restriction are retained in
[the two-class proposition](finite_sharp_counterexamples.md#two-classes-satisfy-the-sharp-comparisons).
Comparison with the zero union already fails for three compatible
classes; the result supplies no many-class extension.

Both Section 6 calculations were checked by exact finite-period
counting and rational arithmetic. For moduli $4,7,9,10,18$, changing
the last residue from $0$ to $4$ at $X=100$ gives
$$
 u_0=\frac7{15},\quad u_1=\frac{17}{35},\qquad
 u_0h_1-u_1h_0
 =\frac{113383068679483}{482750393681556000}>0.
$$
For moduli $4,9,11,210$, changing the last residue from $0$ to
$48$ at $X=1000$ preserves density $274/693$, while the
additional points outside the first three classes change from
$\{210\}$ to $\{258,678\}$. Thus
$$
 h_{48}-h_0=\frac1{258}+\frac1{678}-\frac1{210}
 =\frac{601}{1020390}>0.
$$
These are correct recentering obstructions, not violations of (H)
at those cutoffs. Their qualitative conclusions are already covered
by the smaller [three-modulus example](#further-checks-after-renewed-work)
and the [harmonic-constant obstruction](finite_sharp_counterexamples.md#an-elementary-recentering-obstruction-for-harmonic-constants).

### Capacity, windows, and Wang refinements

Sections 1--3 agree with [basic reductions](basic_reductions.md) and
[compression and blocks](compression_and_blocks.md), including the
coefficient-one harmonic capacity and the factor $H_K$ for the first
$K$ hits. The input correctly confines these estimates to the
**whole** periodic footprint. They do not imply that every
counterexample must use unbounded quotients: arbitrary conditioned
bounded-quotient first kills remain uncontrolled, as the
[endpoint reduction](#private-witness-reduction-for-endpoints) makes precise.

Section 4's Wang distinctness objection is correct. In particular,
the endpoint interval is shorter than every assigned modulus, so a
legal singleton block with those endpoints would have
$\mu(U)H_{\lfloor19Q/10\rfloor}\ge15/76$.
The label-incidence count is also valid, with the intended bound
$$
 O\!\left(Q\,2^k4^{-(k+1)(k/2-\sqrt k)}+2^k\right)=o(Q).
$$
This writes the intended product explicitly in place of the input's
comma after $Q$. The arithmetic skeleton and endpoint bounds were
checked in Wang's full source, Lemmas 3.1 and 3.4, after its digest.
The existing [arbitrary-divisor-refinement theorem](compression_and_blocks.md#every-divisor-refinement-of-a-wang-block-is-uniformly-small)
is stronger than the input's refinement failures: it controls all
cutoffs and unbounded multipliers and quotients.

Section 7's second-moment proof is valid uniformly in its integer
translate, but [common-shift blocks](common_shift_blocks.md) already
allow the wider interval range $H/N\to\infty$. The
[weighted prime-residue theorem](weighted_prime_residue_windows.md)
gives, for fixed $K,C>1$, the quantitative strengthening
$$
 \sup_R\sum_{\substack{N\le n\le N^C\\
       q\mid n-R\text{ for some }N\le q\le KN}}\frac1n
 \ll_{K,C}\frac{\log N}{\log\log N}.
$$
Indeed split the modulus window into finitely many dyadic blocks and
apply its one-residue harmonic bound; any inactive points lie below
$KN$ and cost at most $\log K+O(1)$. This still does not allow
summation over arbitrarily many windows or conditioning on old survivors.

### Exact conditioning formulas and their scope

Section 8's formulas are correct. On a surviving prefix fiber
$n=L(u-1)+r$, with $1\le r\le L$, write $g=(q,L)$ and $m=q/g$.
A tail cylinder meets the fiber exactly when $a_q\equiv r\pmod g$;
then it pulls back to one class modulo $m$, since $(m,L/g)=1$.
Its actual activation is
$$
 gm\le L(u-1)+r,
$$
not $m\le u$. For a fixed $m$, possible original moduli have
$g\mid L$ and $(m,L/g)=1$, giving the exact upper multiplicity
$$
 \prod_{\substack{p^\ell\parallel L\\p\nmid m}}(\ell+1)\le\tau(L).
$$
If $R$ is the set of surviving prefix fibers and $\nu_r$ the full
tail measure on the pulled-back fiber, the exact average is
$$
 \frac1L\sum_{r\in R}\nu_r
 =\mu(U_{\rm tail}\setminus U_{\rm prefix}),
$$
as in (8.3). The harmonic change of variables is harmless for fixed
$L$: all terms $1/(L(u-1)+r)-1/(Lu)$ are nonnegative, and in fact
their total over all fibers and $u\ge1$ is
$$
 \lim_{M\to\infty}(H_{LM}-H_M)=\log L.
$$
This sharpens the input's valid $H_L$ error bound, but does not fix
the separate period-dependent multiplicity and activation losses.

The input's quantifier warning remains necessary for general residues:
shrinking incremental measure need not compensate for growing prefix
periods. For a concrete example, take zero classes at distinct primes
$2^j\le p_j<2^{j+1}$, $j\ge1$. Their survivor measure
$\delta=\prod_j(1-1/p_j)$ is positive, and the incremental tail
$\epsilon_k=\mu(U\setminus U_k)$ tends to zero, but
$$
 L_k\epsilon_k
 \ge \frac{\delta L_k}{p_{k+1}}
 \ge \delta\,2^{k(k+1)/2-k-2}\longrightarrow\infty.
$$
These summable systems already have natural density; the example
only defeats the naive period-dependent bound.

For **coherent** systems the already established
[period-independent conditioning reduction](coherent_power_cutoff.md#an-unconditioned-finite-estimate-would-suffice-proved-reduction)
does overcome this particular loss, conditional on the still-open
unconditioned small-footprint estimate. The input does not supersede
that reduction or the more specialized
[prepared-block bounds](prepared_blocks_entropy.md).

### First-kill charges and a small second-moment failure

The first-kill representation and tower example in Section 9 check
out; the tower is exactly Chojecki's Proposition 6.3. The inequality
$1/r\le2\log(q/m)$, for $r=m/(m,q)\ge2$ and $m<q$, is also
valid, but has no accompanying conservation or multiplicity bound.
It does not prevent repeated charges to the same predecessor.

For each fixed infinite family, dominated convergence gives
$$
 \mathcal E_X:=\sum_{q_i\le X}e_i\log q_i=o(\log X),
 \qquad \sum_i e_i\le1.
$$
The proposed (9.1), with an unrestricted system-dependent
$o(\log X)$ remainder, is therefore equivalent to the desired
candidate-density conclusion: also $\sum_{q_i\le X}e_i\to1-\delta$,
and the finite-prefix lower bound supplies the opposite inequality.
No estimate for that remainder was provided. Dropping it and requiring
an absolute implied constant would give a **refuted** uniform
linear-energy bound, whereas (9.1)
as written is not refuted by the known sublogarithmic excess.

The final four-prime calculation is exact and is retained as
[a small second-moment certificate](rank_and_moment_obstructions.md#a-four-prime-certificate-against-the-sharper-second-moment-charge).
Its potential $V/H_X$ is precisely the overlapping potential already
known to have unbounded higher moments, not the disjoint entropy
potential or the capped prime-stage fractions. None of those distinct
unresolved targets is settled by this calculation.

## Private canonical witnesses can occur in a full finite cover

The pairs
$$
 (q,r)=(2,2),(3,3),(4,5),(6,7),(12,23)
$$
have distinct moduli and satisfy $q\le r<2q$, with every selected
witness private in the entire finite family. Their full cylinders are
$$
 [0]_2,\quad[0]_3,\quad[1]_4,\quad[1]_6,\quad[11]_{12},
$$
and cover every residue modulo $12$. The first covers the even
residues; the others cover, among the odd residues, respectively
$3,9$, $1,5,9$, $1,7$, and $11$. Direct substitution of
$2,3,5,7,23$ shows that each is in only its own cylinder.

Thus privacy of canonical positive endpoints does not imply positive
uncovered Haar measure, even with the exact size restriction. This
finite family cannot be extended by another private endpoint, so it
does not refute infinite logarithmic endpoint nullity.

Nor does full-cylinder disjointness follow from privacy. The
[disjoint-selector bound](prepared_blocks_entropy.md#disjoint-copies-cannot-amplify-these-blocks)
therefore cannot be applied to these first-kill families. In Croot's
prime-factor iteration, full nonintersection forces another modulus
to share an additional prime with a chosen modulus after common
coordinates have been fixed. Endpoint avoidance does not imply that
prime-sharing assertion. A separate
[profinite-fiber obstruction](prime_block_obstructions.md#even-diagonal-profinite-fibers-need-not-return-in-haar-measure)
also rules out deducing the required return solely from bounded
endpoint and modulus marginals. No private-endpoint nullity theorem
or positive-logarithmic-density private family was obtained.

### Affine rough shadows can overlap with arbitrarily large multiplicity

One attempted analog of the primitive-set proof attached to a private
endpoint $q+a$ the points $a+qt$ whose quotient $t$ has no small prime
factor. These shadows are neither disjoint nor of bounded multiplicity.

Fix $k\ge1$, set $P=\prod_{p\le k}p$, and choose
$Q>20kP$ and $k$ distinct primes
$Q\le q_1<\cdots<q_k\le1.1Q$. Such intervals exist arbitrarily
far out: if every interval $[1.1^j,1.1^{j+1})$ beyond some point
contained fewer than $k$ primes, the prime reciprocal sum would
converge. Put $a_i=iP$ and $r_i=q_i+a_i$.
Then $q_i\le r_i<2q_i$, and the distinct witnesses have diameter
less than $Q$. Hence every witness is private in the whole family.

Nevertheless, CRT produces arbitrarily large $x$ for which all
$(x-a_i)/q_i$ are integers having no prime factor at most $2Q$.
At each $q_i$, impose $x\equiv a_i+q_i\pmod{q_i^2}$, so the
$i$th quotient is $1\pmod{q_i}$. For $j\ne i$, it is also
nonzero in the $j$th quotient, since
$0<|a_i-a_j|<Q\le q_i$. At a prime $p\le k$, impose
$x\equiv1\pmod p$; all $a_i$ are zero modulo $p$.
At each remaining prime $p\le2Q$ other than the $q_i$, choose a
residue outside $\{a_1,\ldots,a_k\}\pmod p$, possible because
$p>k$. These prime-power conditions are compatible by CRT.
They describe a positive-density progression of $x$ on which all
$k$ shadows overlap.

Thus bounded-multiplicity disjointification cannot repair this rough
shadow argument. The later [rough-shadow energy construction](rough_shadow_energy.md)
also rules out a uniform quadratic charge: globally private canonical
endpoints can have bounded total shadow measure and unbounded second
moment. Neither obstruction rules out a different fractional allocation.
In particular, the possible private-endpoint bound
$\sum_i1/(q_i\log(2q_i))<\infty$ remains unproved and unrefuted
by this construction. Such a bound would imply logarithmic endpoint
nullity, but it has not been established here.

## Globally private canonical endpoints can have quadratic-small cells

Global privacy does not restore a pointwise estimate
$qe_q\gg(\log q)^{-C}$, for any fixed $C$. The following finite
families have a final cell of density exactly $1/(q(q+1))$.

The four pairs
$$
 (d,s)=(2,2),(3,3),(4,5),(6,7)
$$
have globally private witnesses and leave only $-1\pmod{12}$
uncovered. For $j=0,\ldots,k-1$, install the lifted pairs
$$
 q_{j,d}=12^j d,\qquad r_{j,d}=12^j(s+1)-1.
$$
Each witness satisfies $q_{j,d}\le r_{j,d}<2q_{j,d}$. The $j$-th
block lies in the old survivor fiber $-1\pmod{12^j}$, and leaves
$-1\pmod{12^{j+1}}$. Witnesses in a block are private within it;
earlier witnesses lie outside its parent fiber, while later ones
survive its classes. Thus all witnesses are globally private, and
the moduli are distinct and strictly ordered block by block.

Put $M=12^k$ and append the zero class at $q=M-1$, with witness
$r=q$. Its endpoint is an old survivor. The old moduli are at most
$M/2$, and their witnesses are at most $2M/3-1<q$, so none of
the old positive witnesses is in the new zero class. The entire
family remains globally private, with the exact original activation.
Since $(M,M-1)=1$, its final first-kill density is
$$
 e_q=\mu([-1]_M\cap[0]_{M-1})
     =\frac1{M(M-1)}=\frac1{q(q+1)}.
$$
This is another local obstruction, not a refutation of any summed
entropy estimate or of private-endpoint logarithmic nullity.

## Final status of the private-endpoint attempt

No positive-upper-logarithmic-density family of globally private
integer witnesses $q\le r_q<2q$ with distinct moduli was found.
Nor was logarithmic nullity proved. A stronger finite assertion
considered during the continuation was
$$
 \sup_{\mathcal F}\frac1{\log X}
       \sum_{\substack{q\le X\\q\in\mathcal F}}\frac1q
 \longrightarrow0,
$$
where the supremum is over finite globally private canonical families.
This remains an unproved target, not an estimate available for use.
It would imply endpoint nullity, since $1/r_q\le1/q$.

The attempted arguments based only on containment antichains or
private profinite witnesses are insufficient for the already documented
[binary-colored example](binary_colored_private_witnesses.md).
Rough-shadow multiplicity and quadratic-energy bounds are ruled out
by the explicit examples above and in
[rough-shadow energy](rough_shadow_energy.md). These obstructions do
not disprove the displayed finite target or the original endpoint
assertion. Mixed-idempotent coding likewise failed to control
incomparable earlier moduli, as recorded in
[the preparation notes](overlapping_parent_preparations.md#status-of-mixed-root-and-coding-attempts).
No theorem converting the height restriction on the witnesses into
the needed logarithmic bound was obtained.
