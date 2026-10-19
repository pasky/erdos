---
name: research/erdos_824_uniformity/evidence/verify/endpoint_cancellation/mellin_cancellation
title: "Local energy for the full endpoint class"
desc: Independent full-endpoint reduction to local Mellin energy, including short rough intervals and sparse exceptional times.
created: 2026-10-16T04:10:53Z
updated: 2026-10-16T04:16:14Z
---

# Local energy for the full endpoint class

***

This examines the comparison-correlation part of Section 5 and its Section 2
inputs in the [preserved source](../../assets/endpoint_cancellation_subject/source_sections_2_to_5.md.txt).
The source proof is OpenAI's; the independent examination is prepared for
Plasma AI. No restriction to the special pair in the signed application is
made here. The first endpoint may have arbitrary allowed $\alpha,c_r$,
and the second endpoint may have completely different allowed data.

## The residual coefficient stays arbitrary

In a comparison pattern all freed labels are big. The number of small
marks in every small group therefore remains $\ell\ge1$. Select one
designated small mark. If its group has no prime square dividing $w$,
removing that prime lowers both $\omega_g$ and the mark count by one.
It gives

$$
W_{\mathbf t}^{\mathbf b}(w)=
\sum_{p_s\in\mathcal P_{g_s},\ p_s\mid w}
 V_{g_s}^{-1}W_{\mathbf t-\mathbf e_{g_s}}^{\mathbf b}(w/p_s).
\tag{F1}
$$

There is no factorial multiplier: fixing the designated slot and ordering
the other slots gives a bijection. The mark function uses only big labels,
so it is unaffected. The discrepancy-bearing endpoint is invariant under
removing group primes.

For the excluded square multiples, both sides have fixed logarithmic
bounds. Their endpoint-weighted squared error is bounded by

$$
Y L^{O(1)}\sum_{p_s\in\mathcal P_{g_s}}p_s^{-2}
\ll Y L^{O(1)}e^{-L^a}.
\tag{F2}
$$

Indeed $w_*\mid w/p_s^2$, so a fixed fourth divisor moment bounds the
sum after writing $w=p_s^2v$; every $Y/p_s^2$ is $x^{1+o(1)}$.
Parseval disposes of this error in local Fourier energy.

Because $m$ and the long integer $p$ are rough above $W$, neither has a
group prime factor. The remaining factorization is exactly
$w=mp_s p r$ with residual coefficient

$$
c_{r_*}W_{\mathbf t-\mathbf e_{g_s}}^{\mathbf b}(r).
\tag{F3}
$$

It is bounded by a fixed power of $L$ and has no roughness requirement.
This is valid for every original residual sequence; no multiplicativity
or regularity was introduced.

At a major-arc denominator $q\le L^{C_{\rm arc}}$, the variables
$m,p_s,p$ are units for large $x$. Split $r$ by $d=(r,q)$ and expand
the rational phase on the units modulo $q/d$. The argument
$mp_s p(r/d)$ is a unit there. Character orthogonality includes all
characters of this quotient, including principal and imprimitive ones.
The condition $(r,q)=d$ and the factor $\chi(r/d)$ go into (F3).
The $m$ factor is still the original restricted $\alpha_m$, multiplied
only by its original character, an additional character of bounded
logarithmic modulus, and a bounded logarithmic power twist.

After extracting the polynomial logarithmic costs, each sequence has form

$$
a_w=\Psi_1(w/Y)w^{iv}
 \sum_{mp_s p r=w}
 \alpha_m\chi_m(m)m^{i\sigma_0}
 b_s(p_s)\mathbf1_{p\in I_p,\ P^-(p)>W}
 \chi_p(p)p^{i\sigma_1}d_r,
\tag{F4}
$$

with $|b_s|=O(1)$ and $|d_r|\le L^{O(1)}$. The first coefficient
sequence has not been replaced by a convolution or a residue-class
restriction. Products of the two $m$ characters have modulus bounded by
the product of their moduli, a fixed power of $L$ chosen before $B$.

## Fourier-to-Mellin normalization

Let $H=H'/L^{C_{\rm arc}}$, where the product of free-cell sizes satisfies
$H'\ge\exp(L^c)$, and put $Y=ZH'=x^{1+o(1)}$. Choose a fixed smooth
kernel $K$ of integral one, with small compact support, whose Fourier
transform has modulus at least $1/2$ on $[-1,1]$. Plancherel for the
smoothed discrete measure gives

$$
\int_{|\beta|\le1/H}|\widehat a(\beta)|^2\,d\beta
\ll H^{-2}\int
 \left|\sum_w a_wK((w-v)/H)\right|^2dv.
\tag{F5}
$$

Only $v\asymp Y$ contributes. On the union of the supports of this
kernel and $K(v\log(w/v)/H)$, one has $|w-v|=O(H)$. Taylor's formula
therefore bounds the difference of the two arguments by $O(H/Y)$.
For each $v$ there are $O(H)$ possible integers $w$; Cauchy–Schwarz and
integration over the $O(H)$ possible centers for each $w$ show that the
normalized squared error is

$$
O\left((H/Y)^2\sum_w|a_w|^2\right).
\tag{F6}
$$

The logarithmic kernel is used only for $v\asymp Y$, not near zero.

Set $h=H/Y$, $v=Ye^u$, and $P(t)=\sum_w a_ww^{it}$. Logarithmic
Fourier inversion expresses the kernel sum as

$$
\frac h{2\pi}\int
 e^{-u}\widehat K(he^{-u}t/(2\pi))v^{-it}P(t)\,dt.
$$

Insert a compact cutoff in $u$ that is one on the required range. The
Fourier transform in $u$ of its amplitude is bounded, for each fixed $j$,
by $C_j(1+|s|)^{-2}(1+|ht|)^{-j}$. Two integrations by parts give
the first factor; the Schwartz bounds for $\widehat K$ absorb the
factors $ht$ produced by differentiation. Minkowski in $s$ and
Plancherel in $u$ yield

$$
\int_{|\beta|\le1/H}|\widehat a(\beta)|^2d\beta
\ll_j Y^{-1}\int(1+|ht|)^{-j}|P(t)|^2dt
 +(H/Y)^2\sum_w|a_w|^2.
\tag{F7}
$$

The normalization is $H^{-2}Yh^2=Y^{-1}$.
The ordinary coefficient mean square bounds a dyadic time interval by
$Y^{-2}\int_{T'\le|t|\le2T'}|P(t)|^2dt
\ll(1+T'/Y)L^{O(1)}$. Thus the tail $|t|>L/h$ contributes
$O(YL^{-A})$ to (F7) with large fixed $j$. The error (F6) has that
size for every $A$ as well, since $H=x^{o(1)}$.

Split the four factors in (F4) into dyads and separate the smooth product
cutoff in logarithmic coordinates. The number of boxes and the integral
coefficient mass are fixed powers of $L$. Integration by parts fixes the
frequency cutoff exponent before the desired tail saving: with a
derivative bound $L^{C(j+1)}$ and truncation $L^{C'}$, $C'>C$, the
tail exponent is $C(j+1)-C'(j-b)$ in fixed dimension $b$ and decreases
without bound as $j$ increases. This does not change the earlier ideal
frequency range.

Passing from $P(t)/Y$ to reciprocal-index coefficients is exact after
absorbing $w/Y$ into the smooth product cutoff: $1/Y=(w/Y)/w$.
The boundedness of $w/Y$ alone would not justify a termwise replacement
inside an oscillatory sum; it is this additional smooth separation that does.

The retained frequency shifts enlarge the time interval only to
$|t|\le2L/h$. The task is reduced to bounding

$$
\int_{|t|\le2L/h}|P_s(t)P_l(t)R(t)|^2dt,
\tag{F8}
$$

where $P_s$ is the reciprocal small-prime polynomial at scale $P$,
$P_l$ the reciprocal rough-integer polynomial at scale $P'$, and

$$
R(t)=\left(\sum_{m\asymp M_0}
 \alpha_m\chi_m(m)m^{-1+i\sigma_0+it}\right)
 \left(\sum_{r\asymp R_0}d_rr^{-1+it}\right).
$$

Their scales satisfy

$$
e^{L^a}/2\le P\le e^{L^b},\quad
x^\tau/2\le P'\le x^\eta,\quad
PM_0P'R_0\asymp Y.
\tag{F9}
$$

Every dyad is intersected with its original restrictions. A subproduct
at scale $U$ has coefficient-square sum $L^{O(1)}/U$: a convolution
of a fixed number of bounded coefficients has at most a fixed divisor
power of representations. The number of marked groups was already paid
for in the bound on (F3). It is not a growing divisor-moment order.

## Exceptional intervals do not cost their cardinality

Outside $E=\{t:|P_s(t)|>L^{-A_s}\}$, the mean square of $P_lR$ gives
$L^{-2A_s+O(1)}$, because its scale $Y/P$ exceeds the time interval:

$$
\frac{Y/P}{2L/h}=\frac H{2LP}\longrightarrow\infty
$$

by $b<c$.

For $j_0=\lfloor\log Y/\log(2P)\rfloor$, $P_s^{j_0}$ has indices
at most $Y$. Unique factorization gives at most $j_0!$ ordered prime
representations of an index, including repeated primes. Its squared
coefficient sum is at most $j_0!(C/P)^{j_0}$. Choose an exceptional
point in each occupied unit interval and split interval indices into
three classes to obtain unit separation. The coefficient mean square
and the elementary unit-interval Sobolev inequality give

$$
N_E\ll YL^{O(1)}j_0!
                 (CL^{2A_s}/P)^{j_0}.
$$

Here differentiation of the powered polynomial costs only $\log Y$,
not an uncontrolled constant depending on $j_0$. Since
$j_0=O(L^{1-a})$ and
$\log Y-j_0\log P=O(L^b+j_0)$,

$$
N_E\le\exp(O(L^b+L^{1-a}\log L))=Y^{o(1)}.
\tag{F10}
$$

Multiplying a logarithmic saving by (F10) would not suffice. Instead
collapse $R$ to coefficients on an interval at scale

$$
U\asymp Y/(PP')\ge Y^{1-\eta-o(1)}>Y^{0.6}.
\tag{F11}
$$

This holds for the whole claimed $\eta<1/4$ class. For $|z|\ll Y$,
the Gram kernel of the evaluation map satisfies

$$
\left|\sum_{n\asymp U}n^{iz}\right|
\ll U/(1+|z|)+Y^{1/2}.
\tag{F12}
$$

For $1\le|z|\le cU$, the first derivative test applied to
$z\log n/(2\pi)$ gives $O(U/|z|)$; negative derivatives use the
interval between the integers $-1$ and $0$. For $cU<|z|\ll Y$, the
second derivative test gives
$O(\sqrt{|z|}+U/\sqrt{|z|})=O(Y^{1/2})$. The range $|z|<1$ is trivial.

Take a maximum of $|R|$ on each closed exceptional unit interval, and
again split indices into three separated classes. For each class the
absolute Gram row sums are
$O(U\log(2Y)+N_EY^{1/2})=O(U\log(2Y))$, by (F10)–(F11).
The coefficient norm $L^{O(1)}/U$ then gives

$$
\sum_{I\ {\rm occupied}}\sup_{t\in I}|R(t)|^2\ll L^{O(1)}.
\tag{F13}
$$

This is the estimate that defeats arbitrary concentration of the residual
coefficients on the exceptional times.

## The long integer factor on every subinterval

The long factor has its stated special form: a character and a power twist
on rough integers in an interval. It is not an arbitrary coefficient
sequence. Let that interval be any $J'\subset[P',2P']$, even very short,
and put $u=t+\sigma$.

For completeness, the needed sieve polynomial can be reconstructed
elementarily. In the block $z^{2^{-j-1}}<p\le z^{2^{-j}}$ truncate
inclusion–exclusion at the even degree $h_j=(j+1)h_s$. If $t$ bad
conditions hold, its value for $t>0$ is $\binom{t-1}{h_j}$; for $t=0$
it is one. It is an upper bound and its overcount is at most
$\binom t{h_j+1}$. A telescoping product bounds the full overcount by
the sum of one-block corrections. The correction supports are mutually
disjoint and disjoint from the upper polynomial's support, so their
coefficients have modulus at most one. Their level is at most
$z^{4h_s+2}$, because $\sum_{j\ge0}(j+1)2^{-j}=4$.

For independent bad probabilities $g(p)$ satisfying the source's block
mass and upper-bound hypotheses, each block avoidance probability is
bounded below, while its correction expectation is at most
$C^{h_j+1}/(h_j+1)!$. The sum of relative corrections is $O(e^{-h_s})$
for large even $h_s$, uniformly as it grows. Apply this to $g(p)=1/p$;
Mertens supplies the bounded block masses. Counting multiples on any
interval gives the claimed overcount $O(|I|e^{-h_s}+D)$ with
$D=z^{4h_s+2}$.

Now take $z=W$, $h_s=2\lceil T^2\rceil$, and
$D=W^{4h_s+2}=x^{o(1)}$. Replacing roughness by the upper polynomial
$\sum_{d\mid n}\lambda_d$ costs
$O(e^{-h_s}+D/P')$ after reciprocal normalization, also on a subinterval
because the overcount is nonnegative. Further,

$$
\sum_d|\lambda_d|/d
\le\prod_{p\le W}(1+1/p)\ll\sqrt L.
\tag{F14}
$$

Let $q'$ be the character modulus. Terms with $(d,q')>1$ vanish. For
the others write $n=d(q'y+a)$ in each residue class. The new scale is
$N=P'/(dq')\ge x^{\tau/2}$ eventually. A sufficiently large fixed
$B_0>C+1$ ensures $|u|\ge L^{B_0}/2$ when $|t|\ge L^{B_0}$.

The phase $u\log(q'y+a)/(2\pi)$ has $k$th derivative of constant
sign and magnitude comparable to $|u|N^{-k}$. If $|u|\le cN$, the
monotone first derivative test gives $O(N/|u|)$ uniformly on every
subinterval. Otherwise the overlapping ranges

$$
N^{k-2+\varepsilon}\le|u|\le N^{k-\varepsilon},\qquad
\varepsilon=1/10,\quad 2\le k\le K=\lceil4/\tau\rceil+3,
\tag{F15}
$$

cover $cN<|u|\le x^2$. For $k=2$ use the second derivative test.
For $k>2$, difference $k-2$ times with positive shifts at most
$H_0=\lfloor N^{\varepsilon/(2k)}\rfloor$. The resulting second
derivative is an iterated integral of the $k$th derivative and lies,
up to fixed factors, between $N^{-2+\varepsilon}$ and
$N^{-\varepsilon/2}$. The second derivative test on any intersection
of the shifted supports gives $O(N^{1-\varepsilon/4})$.

To see the short-interval uniformity, extend the original phase sequence
by zero within a containing interval of length $O(N)$. Averaging $H_0$
translates and applying Cauchy–Schwarz gives a normalized recurrence
$B_j^2\ll H_0^{-1}+B_{j+1}$. Every correlation support is again an
interval, and all shifts are $o(N)$. Iteration yields
$B_0\ll N^{-\delta_k}$ with
$\delta_k=\varepsilon/(k2^{k-1})$. Thus, with a fixed positive
$\delta$ depending only on $\tau$,

$$
\left|\sum_y \exp(iu\log(q'y+a))\right|
\ll N(|u|^{-1}+N^{-\delta})
\tag{F16}
$$

on every subinterval. The same proof treats negative $u$ by absolute
derivative sizes. Partial summation of the reciprocal weight and summing
the $q'$ classes give the bound
$d^{-1}(|u|^{-1}+x^{-\tau\delta/2})$. By (F14), the long factor is
at most

$$
O(e^{-h_s}+D/P')+
O\bigl(\sqrt L(L^{-B_0}+x^{-\tau\delta/2})\bigr).
\tag{F17}
$$

Taking also $B_0>A_l+2$ proves any prescribed $L^{-A_l}$ saving.
No lower bound on the length of $J'$ was imposed. A one-integer interval,
for example, is already smaller than every fixed negative logarithmic
power after its reciprocal normalization.

## Closing the time split and choosing the discrepancy exponent

On the exceptional set with $|t|\ge L^{B_0}$, the actual retained
range obeys $|t+\sigma_1|<x^2$. The small-prime harmonic sum is bounded.
Combining (F13) and (F17), rather than multiplying by $N_E$, bounds this
part of (F8) by $L^{-2A_l+O(1)}$.

For $|t|\le L^{B_0}$, use the original discrepancy on the $m$ factor
in $R$. Its support is an interval inside $[1,x^2]$, since
$m\ll Y=x^{1+o(1)}$. Its character modulus and power twist have fixed
logarithmic exponents determined earlier. With $B$ above those exponents,
the factor is at most $L^{-B}$. All other harmonic sums have fixed
logarithmic bounds. This part is therefore
$L^{-2B+B_0+O(1)}$.

For constants $K_i$ fixed independently of $B$ and proxy precision, the
three ranges give

$$
\int_{|t|\le2L/h}|P_sP_lR|^2dt
\ll L^{-2A_s+K_1}+L^{-2A_l+K_2}
      +L^{-2B+B_0+K_3}+o(L^{-Q}).
\tag{F18}
$$

For a desired $Q$, first fix $A_s,A_l$, then $B_0$ using the long
factor estimate, and finally $B$ for the low-time saving and the modulus
and frequency requirements. This gives (F8) with arbitrary logarithmic
saving, and (F7) gives local Fourier energy $O(YL^{-A})$ after paying
the earlier separation costs.

This derivation uses no relation between the two endpoints, no roughness
of $c_r$, no regularity of $\alpha$, no minimum interval length for
$I_p$, and no information about proxy cells. Restricting $\alpha$ to
another interval preserves its discrepancy exactly because intersections
of intervals are intervals. Conjugation preserves it by
$(\chi,u)\mapsto(\overline\chi,-u)$. Additional fixed twists are
handled inside the endpoint representation by the final choice of $B$;
no unchanged-$B$ stability under arbitrary extra twists is asserted.

No computational experiment is used in this derivation.
