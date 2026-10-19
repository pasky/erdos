---
name: research/leads/totient_binary_series/progression_means
title: Progression Means of Infinite Totient Kernels
desc: |
  Fresh-prime refinements separate nonzero absolutely summable kernels of
  normalized shifted totients; fixed dilation grids have a precise
  noncancellation result and explicit bounds for their full signed tails.
tags: []
sources: []
problems:
- 249
review_status: unreviewed
created: 2026-09-17T04:59:47Z
updated: 2026-10-14T00:26:52Z
---

***

This is an author-recorded argument supporting the
[[research/leads/totient_binary_series/_index|binary totient sketch]]. No
independent review or novelty claim is attached. Its mechanism is related
to the progression-mean step in the identified
[Problem 252 manuscript](https://github.com/tokengr1nder/Erdos252/blob/dc071aafce41bbae41caf4c015499db6dafafd11/PROOF.tex),
but the self-contained core proof is in the native claim linked below.
It shows that finite support is unnecessary for that step. The later
error bounds and applications are proved here. None makes rationality
of the binary series imply the required limiting identity.

Write $\rho(n)=\varphi(n)/n$ for positive integers $n$, so
$0<\rho(n)\le1$ and $\rho(n)=\sum_{d\mid n}\mu(d)/d$.

## The mean and separation theorem

The canonical statement and complete proof are
[[theory/irrationality/L16_totient_kernel_separation/_index|L16]], at
**tier 0: author-recorded, without independent acceptance**. The labels
below retain the notation used by the research applications.

**Lemma 1 (the mean calculation in L16).** For fixed $Q\ge1$ and
integer $a$, the mean of $\rho$ over positive members of the progression
is

$$
\kappa_Q(a)
 =\sum_{\substack{d\ge1\\(d,Q)\mid a}}
       \frac{\mu(d)(d,Q)}{d^2}
 =\frac1{\zeta(2)}
   \prod_{p\mid Q}(1-p^{-2})^{-1}
   \prod_{p\mid(Q,a)}(1-p^{-1})>0.
$$

For a real absolutely summable kernel $c$, let
$F(N)=\sum_{s\ge1}c_s\rho(N+s)$. Its mean is

$$
\mathcal M_Q(a)=\sum_{s\ge1}c_s\kappa_Q(a+s).
$$

For a prime $\ell\nmid Q$, let $a_b\equiv a\pmod Q$ and
$a_b\equiv b\pmod\ell$. The refinement formula is

$$
\kappa_{Q\ell}(a_b+s)
 =\frac{\kappa_Q(a+s)}{1-\ell^{-2}}
   \left(1-\frac{\boldsymbol1_{\ell\mid b+s}}\ell\right).
$$

The [[theory/irrationality/L16_totient_kernel_separation/_proof|canonical proof]]
derives these formulas by divisor-congruence counting and absolute
convergence; it uses no pointwise asymptotic for $\rho$.

**Theorem 2 (L16).** If $c$ is nonzero, then for every fixed $Q\ge1$
and integer $a$,

$$
\limsup_{\substack{N\to\infty\\N\equiv a\ (Q)}}|F(N)|>0.
$$

More precisely, put $d_s=c_s\kappa_Q(a+s)$. Choose any $s_*$ with
$d_{s_*}\ne0$, any $K\ge s_*$ with
$\sum_{s>K}|d_s|<|d_{s_*}|/4$, and any prime $\ell>K$ not dividing
$Q$. The means on the refinements $N\equiv0$ and $N\equiv-s_*$
modulo $\ell$ differ; one has modulus greater than
$\eta=|d_{s_*}|/[4\ell(1-\ell^{-2})]$. That refinement contains
infinitely many $N$ with $|F(N)|>\eta/2$.

First fix the kernel and original progression, then choose the anchor,
cutoff and prime, and finally take the limit. For growing data the anchor
may shrink and $K,\ell,Q$ may grow. No uniform separation follows
without controlling those quantities. The finite-window estimate below
makes one such control available; Corollary 5 gives a particular family
where its growing-shift error can actually be bounded.

## An explicit error bound for the means

The limiting argument has the following quantitative form. This makes its
dependence on a growing modulus or kernel available for comparison; it does
not assert that a proposed growing family satisfies the resulting bounds.
Logarithms in this subsection are natural.

**Lemma 2a.** Let $R,X,H\ge1$ and $T\ge0$ be integers, $0\le b<R$,
and let $c$ be an absolutely summable real kernel. Write

$$
B_H=\sum_{s\le H}|c_s|,\qquad E_H=\sum_{s>H}|c_s|,
\qquad F(N)=\sum_{s\ge1}c_s\rho(N+s).
$$

Then

$$
\left|\frac1X\sum_{t=1}^X F\bigl(b+R(T+t)\bigr)
       -\mathcal M_R(b)\right|
\le
\frac{B_H\bigl(2+\log(R(T+X+1)+H)\bigr)}X+2E_H.
$$

*Proof.* For a single $s\le H$, put $Y=b+R(T+X)+s$. As in Lemma 1,
counting a soluble congruence for $t$ in this interval differs from its
mean by at most one. After division by $X$, the divisor-sum error is at
most $X^{-1}\sum_{d\le Y}1/d\le(1+\log Y)/X$. Completing the main
series contributes at most
$R\sum_{d>Y}d^{-2}\le R/Y\le1/X$.
Since $Y\le R(T+X+1)+H$, multiplying by $|c_s|$ and summing gives the
first term. The omitted kernel contributes at most $E_H$ to each of the
sample average and the limiting mean, because $\rho,\kappa_R\le1$.
$\square$

For the choices $s_*,K,\ell$ in Theorem 2, put

$$
R=Q\ell,\qquad
\eta=\frac{|d_{s_*}|}{4\ell(1-\ell^{-2})}>0.
$$

One of the two refined means has magnitude greater than $\eta$.
Choose any $T\ge0$, then $H$ and $X$ satisfying

$$
E_H\le\eta/8,\qquad
\frac{B_H\bigl(2+\log(R(T+X+1)+H)\bigr)}X\le\eta/4.
$$

On at least one refinement there is a member
$N=b+R(T+t)$, $1\le t\le X$, for which $|F(N)|>\eta/2$.
Indeed the error from Lemma 2a is at most $\eta/2$, so the signed
sample mean has magnitude greater than $\eta/2$. Such $H$ and $X$
exist for each fixed kernel, modulus and $T$.
In particular the same refinement contains infinitely many such members,
and the limsup in Theorem 2 is at least $\eta/2$.

This is an explicit finite-window separation criterion, including the
infinite kernel tail. For a parameter family, its anchor, refinement
modulus, tail mass and sample length must satisfy these very inequalities.
A family may use a different kernel on each sample window, provided it
is held fixed throughout that window and the displayed inequalities are
verified with that window's data. The two candidate refinements for a
given kernel use that same kernel. Substituting a different kernel at each
$N$, or retaining only a selected member that need not be the separating
one, is not licensed by the criterion. No implication from rationality
to smallness on any such window has been supplied.

## A precise obstruction for a fixed dilation grid

Retain $T_n=\sum_{j\ge1}\varphi(n+j)2^{-j}$ from the main sketch.
Fix a nonempty finite set of pairwise distinct integers $p_e\ge2$, offsets
$0\le t_e<p_e$, and integer weights $w_e$ not all zero. Suppose a fixed
progression $N\equiv a\pmod Q$ satisfies all
$N\equiv t_e\pmod{p_e}$, and define

$$
\Lambda(N)=\sum_e w_e\varphi(p_e)T_{(N-t_e)/p_e}.
$$

Only sufficiently large positive $N$ are considered.

**Corollary 3.** For every fixed finitely supported real sequence
$(h_s)_{s\ge1}$, the expression

$$
\Lambda(N)-\sum_{s\ge1}h_s\varphi(N+s)
$$

is not $o(N)$ as $N\to\infty$ through the progression
$N\equiv a\pmod Q$.

In particular a fixed finite correction cannot give an error $o(1)$
uniformly on the entire progression. This is a conclusion about one fixed
grid and one fixed correction; a cutoff or grid depending on $N$ is outside
its hypotheses.
The same conclusion holds on every fixed subprogression, by applying
the statement with that subprogression as the original one. A selected
subsequence containing no full subprogression remains outside the claim.

*Proof.* Refine the progression to one whose modulus $Q'$ is divisible
by $Q$ and every $p_e^2$. Such a refinement can be obtained by choosing
any one member and its residue modulo the least common multiple. From
$\varphi(p)\varphi(m)=\varphi(pm)\varphi((p,m))/(p,m)$, the exact expansion is

$$
\Lambda(N)=\sum_{s\ge1}A_N(s)\varphi(N+s),\qquad
A_N(s)=\sum_{e:\ p_e\mid s+t_e}
 w_e\frac{\varphi(g_{e,N,s})}{g_{e,N,s}}2^{-(s+t_e)/p_e},
\quad
 g_{e,N,s}=\gcd\!\left(p_e,\frac{N+s}{p_e}\right).
$$

On the refined progression the coefficient $A_N(s)=A(s)$ is fixed,
since the gcd depends only on $N\pmod{p_e^2}$. Also
$\sum_s s|A(s)|\le\sum_e2p_e|w_e|<\infty$.

Let $p$ be the largest dilation with a nonzero weight. On the residue
class $s\equiv-t\pmod p$ belonging to that dilation, its summand has
magnitude at least $(\varphi(p)/p)2^{-(s+t)/p}$. Every other nonzero
summand decays at least as fast as a constant times $2^{-s/(p-1)}$.
Consequently $A(s)$ is nonzero for all sufficiently large $s$ in that
class. This is the coefficient calculation of Proposition 4 of the main
sketch, with the dependence on $N$ correctly retained before refinement.

Set $c_s=A(s)-h_s$. This is a nonzero sequence with an absolutely summable
first moment. Uniformly over the refined progression,

$$
\frac{\Lambda(N)-\sum_s h_s\varphi(N+s)}N
 =\sum_s c_s\rho(N+s)+O\!\left(\frac{\sum_s s|c_s|}{N}\right).
$$

If the numerator were $o(N)$ on the original progression, the kernel on
the right would tend to zero on the refinement. Theorem 2 forbids that.
$\square$

## The signed tail after a growing common cutoff

For the same fixed grid, a direct truncation of its exact coefficient
expansion has a quantitative limitation even when the cutoff grows.
This concerns the particular correction using the first $H$ coefficients
$A_N(s)$, not an arbitrary correction with $H$ terms.

**Lemma 4.** Let $p=p_{e_*}$ be the largest dilation with nonzero weight,
$t=t_{e_*}$, and set

$$
V=\sum_e|w_e|,\qquad W=V-|w_{e_*}|,\qquad
\alpha=|w_{e_*}|\frac{\varphi(p)}p\,2^{-t/p}>0.
$$

For every compatible $N>2\max_ep_e$ and integer $H\ge0$,
define the exact remainder

$$
\mathcal R_H(N)=\Lambda(N)-\sum_{s\le H}A_N(s)\varphi(N+s).
$$

It satisfies

$$
|\mathcal R_H(N)|\le 2V(N+H+2p)2^{-H/p}.
$$

If in addition

$$
\frac{2W}{\alpha}(1+\log_2N)
 \left(1+\frac{H+2p}{N}\right)
 2^{-H/[p(p-1)]}\le\frac12,
$$

then $\mathcal R_H(N)$ has the sign of $w_{e_*}$ and

$$
|\mathcal R_H(N)|\ge
 \frac{\alpha N}{2(1+\log_2N)}\,2^{-H/p}.
$$

*Proof.* Put $J_e=\lfloor(H+t_e)/p_e\rfloor$. The contribution of
dilation $e$ to the remainder is

$$
w_e\sum_{j>J_e}
 \frac{\varphi(\gcd(p_e,n_e+j))}{\gcd(p_e,n_e+j)}
 \varphi(N+jp_e-t_e)2^{-j},\qquad n_e=(N-t_e)/p_e.
$$

Every argument $N+jp_e-t_e$ exceeds $N$. The elementary bound on
the main sketch, and the monotonicity of $x/(1+\log_2x)$ for $x\ge2$,
give a lower bound $N/(1+\log_2N)$ for each totient. The contribution
of $e_*$ therefore has its weight's sign and magnitude at least

$$
|w_{e_*}|\frac{\varphi(p)}p\frac{N}{1+\log_2N}2^{-J_{e_*}}
 \ge \frac{\alpha N}{1+\log_2N}2^{-H/p}.
$$

For any active dilation, the bounds on its gcd factor and
$\varphi(n)\le n$ give an absolute contribution at most

$$
|w_e|\bigl(N-t_e+p_e(J_e+2)\bigr)2^{-J_e}
 \le 2|w_e|(N+H+2p)2^{-H/p_e}.
$$

Summing proves the upper bound. Every other active dilation has
$p_e\le p-1$, so their total absolute contribution is at most
$2W(N+H+2p)2^{-H/(p-1)}$. The displayed hypothesis makes this at
most half the lower bound for the $e_*$ contribution, proving the sign
and lower bound. The case $W=0$ is included. $\square$

In particular fix a real $c>0$ and use
$H=\lceil c\log_2N\rceil$. If $0<c<p$, the dominance hypothesis
eventually holds and $|\mathcal R_H(N)|\to\infty$, uniformly over
compatible $N$. If $c>p$, the upper bound gives
$\mathcal R_H(N)\to0$ uniformly. At $c=p$ these estimates give only
a lower bound of order $1/\log N$ and an upper bound of order one;
they do not decide convergence to zero. Thus the direct common-shift
truncation needs the logarithmic scale set by its largest dilation.
The calculation controls the entire infinite remainder and does not
exchange a limit with a kernel whose parameters vary. It does not supply
the arithmetic fractional-part separation needed under rationality.

The finite-window mean estimate settles uniform convergence at the
critical scale, by keeping the varying shift fixed on each sampled block.

**Corollary 5.** On every fixed compatible progression
$N\equiv a\pmod Q$, let $H_N=\lceil p\log_2N\rceil$. Then

$$
\limsup_{\substack{N\to\infty\\N\equiv a\ (Q)}}
 |\mathcal R_{H_N}(N)|
 \ge \frac{|w_{e_*}|\varphi(p)}{8p}\,\kappa_Q(0)>0.
$$

*Proof.* Write $D=|w_{e_*}|\varphi(p)/p$ and
$\gamma=\kappa_Q(0)>0$. The product in Lemma 1 gives
$\kappa_Q(r)\ge\gamma$ for every integer $r$. For each large integer
$k$, consider all progression members in the interval

$$
2^k<N\le2^{k+1/p}.
$$

Throughout this interval $H_N=pk+1$, so the leading dilation's
$J_{e_*}=\lfloor(H_N+t)/p\rfloor=k+\epsilon$, where
$\epsilon=\lfloor(1+t)/p\rfloor\in\{0,1\}$. Its first retained
term has the fixed shift $s_k=p(k+\epsilon+1)-t$.

The interval contains
$X_k=(2^{1/p}-1)2^k/Q+O(1)$ consecutive members of the progression.
Apply Lemma 2a with $R=Q$, its starting index $T=O_Q(2^k)$, and the
kernel consisting of the single coefficient $c_{s_k}=1$, with cutoff
$s_k$. Here $B_{s_k}=1$, $E_{s_k}=0$ and $s_k=O_p(k)$, so the error is
$O_{p,Q}(k2^{-k})$. This tends to zero uniformly in the phase
$a+s_k\pmod Q$. Thus for each sufficiently large $k$ at least one
member $N_k$ in this interval satisfies
$\rho(N_k+s_k)\ge\gamma/2$.

At that member, the leading dilation's whole tail has its weight's
sign and magnitude at least its first retained term, namely

$$
D\,\varphi(N_k+s_k)2^{-(k+\epsilon+1)}
 \ge \frac{D\gamma}{2}(N_k+s_k)2^{-(k+\epsilon+1)}
 > \frac{D\gamma}{2^{\epsilon+2}}
 \ge \frac{D\gamma}{8}.
$$

The other dilations contribute in total at most
$2W(N_k+H_{N_k}+2p)2^{-H_{N_k}/(p-1)}
=O_{p,w}(N_k^{-1/(p-1)})=o(1)$, by the proof of Lemma 4.
Subtracting this bound along $N_k\to\infty$ proves the result.
$\square$

Consequently the direct truncation at $H_N=\lceil c\log_2N\rceil$
has a remainder tending to zero on a whole fixed compatible progression
exactly when $c>p$, among fixed real $c>0$. For $c=p$ the conclusion is
a positive limsup, not a positive lower bound at every member or a claim
about every selected subsequence. The quantitative mean bound is what
permits this particular family of growing shifts; a bare exchange of
fixed-kernel limits would not do so.

## The unsupplied irrationality implication

Rationality $S=a/b$ makes $b\Lambda(N)$ integral for integer $w_e$.
It does not make $\Lambda(N)$ bounded or its normalized kernel tend to
zero. Corollary 3 explains why subtracting a fixed number of shifted
values cannot supply such a uniform reduction on a whole progression.
Theorem 2 remains usable for a different construction that really does
produce a null kernel; that construction is open.

Possible changes of mechanism include growing grids, corrections more
general than the direct truncation of Lemma 4, coefficients with an
additional parameter, or a carefully selected proper subsequence of a
progression. They require their own error bounds and nonvanishing
arguments. Even where Lemma 4 makes the tail small, the needed separation
of the finite prefix from the rationality lattice remains unproved.

The same finite-window estimate has a separate quantitative application
to [[research/leads/totient_binary_series/integer_interpolation/geometry|shifted-totient
interpolation matrices]]. Averaging the squared limiting means over
every class of one prime $\ell>2k$ gives a lower bound uniform over
unit coefficient vectors on at most $2k$ shifts. Lemma 2a transfers
that bound to common finite samples with explicit growing parameters.
The resulting singular-value estimate bounds the prescribed real
solution's contribution to the weighted interpolation cost. It supplies
neither a quantitative integral-image endpoint nor a small rounding
error in the integer coset, so the irrationality implication remains
conditional on that additional arithmetic control.
