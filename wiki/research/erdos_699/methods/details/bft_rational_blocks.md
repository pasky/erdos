---
name: research/erdos_699/methods/details/bft_rational_blocks
title: "Erdős 699: rational Padé blocks and a cofactor tradeoff"
desc: "Clearing the denominators of unmatched Padé blocks gives a piecewise linear cofactor restriction and improves the effective 2,3 maximum exponent to .2926. No additional index is settled."
created: 2026-09-22T05:39:49Z
updated: 2026-09-22T19:12:28Z
---

# Erdős 699: rational Padé blocks and a cofactor tradeoff

[[research/erdos_699/_index|P699 research]] ·
[[research/erdos_699/methods/details/asymmetric_cofactors|The asymmetric BFT bounds]]

***

The Padé block in BFT Section 7 can exceed one of the available
prime-power blocks. The remaining cofactor is then rational; clearing
its denominator retains a useful integer inequality. This yields a
piecewise linear restriction beyond the earlier endpoint alternatives.

One concrete consequence is the following effective improvement:

> For every fixed $D\ge1$, there is an effectively computable $x_0(D)$
> such that
> $$|2^a u-3^b v|\le D,\qquad x=\min(2^a u,3^b v)\ge x_0(D)$$
> implies
> $$\boxed{\max(u,v)>x^{.2926}.}$$
> Here $u,v$ are positive integers and $a,b$ are nonnegative integers.

The numerical value of $x_0$ has not been evaluated. Since $u,v\ge1$,
the same conclusion gives $uv>x^{.2926}$. This is a small improvement
over the retained exponent $.2921$; it is far from the product exponent
$5/6$ that would directly settle the remaining quartic configurations.
No additional whole index follows from this note.

## An integer inequality with rational residual cofactors

Fix valid BFT Theorem 2.4 parameters, with seed

$$
P=p^{k_0},\qquad Q=q^{l_0},\qquad aP-bQ=D_0>0,\qquad s=c/d.
$$

Here $p,q$ are distinct primes. Suppose the coefficient-gcd estimate
holds for every $m>m_0$, with constants $L_1,\kappa_1,\kappa_2$ and
$\Omega_3,\Omega_4>1$. Write

$$A=\log P,\qquad B=\log Q,\qquad
K=\max(A,B)+\frac{\log\Omega_4}{s}.$$

Let $X=p^k u$, $Y=q^l v$ be positive integers with $|X-Y|\le D$.
For **any** integer $m>m_0$, define

$$
U_m=X/P^{cm},\qquad V_m=Y/Q^{cm},
$$

$$
Z_m=p^{(k_0cm-k)_+}q^{(l_0cm-l)_+},\qquad
\Delta_m=\log Z_m
=(cmA-k\log p)_++(cmB-l\log q)_+. \tag{1}
$$

The notation $z_+=\max(z,0)$ denotes the positive part.
The factor $Z_m$ clears both residual denominators.

The two BFT Padé choices have integral coefficients
$\mathcal P_m,\mathcal Q_m,\mathcal E_m$ satisfying

$$
(aP)^{cm}\mathcal P_m-(bQ)^{cm}\mathcal Q_m=\mathcal E_m.
$$

Their determinant identity ensures that at least one choice has

$$
T_m=b^{cm}\mathcal Q_m U_m-a^{cm}\mathcal P_m V_m\ne0.
$$

This nonvanishing argument works for positive rational $U_m,V_m$ too.
Since $Z_mT_m$ is a nonzero integer,

$$
1\le Z_m|T_m|
\le Z_m\left(
\frac{Db^{cm}|\mathcal Q_m|}{P^{cm}}
+\frac{|\mathcal E_m|Y}{(PQ)^{cm}}
\right). \tag{2}
$$

The same estimates used in BFT (7.4)--(7.6) give

$$
\frac{Db^{cm}|\mathcal Q_m|}{P^{cm}}
\le\frac{\kappa_1}{2}\Omega_3^{-dm},\qquad
\frac{|\mathcal E_m|}{(PQ)^{cm}}
\le\frac{1}{2\kappa_2}e^{-cmK}.
$$

Consequently

$$
\boxed{
1\le\frac{\kappa_1}{2}
       e^{\Delta_m-dm\log\Omega_3}
 +\frac{Y}{2\kappa_2}e^{\Delta_m-cmK}
\quad\text{for every integer }m>m_0.
} \tag{3}
$$

The source argument corresponds to choosing $m$ so that $Z_m=1$.
Equation (3) also permits larger blocks, with their exact denominator cost.

## A directly usable positive-part restriction

Put

$$
C=\frac{\log\Omega_3}{s},\qquad J=K-C,
$$

and suppose $J>0$. For $x=\min(X,Y)>1$, define

$$
e_p=\frac{\log u}{\log x},\qquad e_q=\frac{\log v}{\log x},
$$

$$
T(e_p,e_q)=(A-J(1-e_p))_++(B-J(1-e_q))_+.
$$

For every $\epsilon>0$, sufficiently large inputs necessarily satisfy

$$
\boxed{T(e_p,e_q)>C-\epsilon.} \tag{4}
$$

The threshold is effective. In fact it suffices to take

$$
x>\max\left\{
D,\ e^{cJ(m_0+1)},\
\left(\frac{\kappa_1}{2}e^{cC}
      +\frac{e^{cK}}{\kappa_2}\right)^{J/\epsilon}
\right\}. \tag{5}
$$

**Proof.** Suppose $T(e_p,e_q)\le C-\epsilon$ and choose
$m=\lfloor\log x/(cJ)\rfloor$. Then $m>m_0$ by (5). Because
$X,Y\ge x$, equation (1) gives

$$
\Delta_m\le \frac{T(e_p,e_q)}J\log x.
$$

Also $cm>\log x/J-c$, and $Y\le x+D<2x$. The right side of (3)
is therefore at most

$$
\left(\frac{\kappa_1}{2}e^{cC}
      +\frac{e^{cK}}{\kappa_2}\right)x^{-\epsilon/J}<1,
$$

a contradiction. $\square$

This is a sufficient contradiction criterion obtained from one particular
block size. It is not asserted to describe the complete optimum over all
$m$: the function $Kt-\Delta(t)$ can decrease after both available blocks
have been exceeded.

When $J>\max(A,B)$, the two coordinates in (4) have positive transition
values $1-A/J$ and $1-B/J$. For example, if
$e_q\le1-B/J$, then (4) requires

$$
e_p>\frac{K-A-\epsilon}{J}. \tag{6}
$$

When both positive parts occur, (4) instead gives

$$
e_p+e_q>2-\frac{A+B-C+\epsilon}{J}. \tag{7}
$$

These are conditional parts of one restriction; neither is a simultaneous
unconditional lower bound on both cofactors.

## The seed $9-8=1$

Take $P=9$, $Q=8$, $a=b=1$, $c/d=3/2$, and

$$
\log L_1=\frac{308}{625}=.4928.
$$

The retained coefficient-gcd formula gives

$$
\log L(3/2)>.49283363527>.4928.
$$

Thus BFT Theorem 2.2 supplies an effective $m_0$ for this strictly smaller
$L_1$. The directed interval checker certifies

$$\begin{aligned}
C&=.1178365156647256\ldots,\\
K&=3.0576959900410894\ldots,\\
J&=2.9398594743763638\ldots>\log9>\log8.
\end{aligned}$$

In prime order $3,2$, the transition values are

$$1-\frac{\log9}{J}=.2526089779164293\ldots,
\qquad
1-\frac{\log8}{J}=.2926731499229395\ldots.$$

If both cofactors have exponent at most $.2926$, the second positive
part in (4) vanishes. The first falls below $C$ by more than $.0002685$.
Taking, for example, $\epsilon=.0002$ in (4) proves the displayed
maximum-cofactor improvement.

The limiting intercept when the $2$-cofactor lies below its transition
value is

$$
\frac{K-\log9}{J}=.2926913412714745\ldots.
$$

This also gives a product bound directly: for nonnegative $e_3,e_2$, the
sum of the two positive parts is at most
$J(e_3+e_2-(1-\log9/J))_+$. Thus every fixed exponent smaller than
$.29269134127$ is an effective lower exponent for $uv$.

The proof uses the identities and coefficient bounds in
BFT Section 7.
The [checker](../../computations/erdos_699_bft_rational_blocks.py)
and [directed interval output](../../computations/erdos_699_bft_rational_blocks.json)
verify the strict coefficient-gcd and exponent margins. They do not
assign a numerical value to the effective threshold.
