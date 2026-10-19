---
name: research/sidon_extremal_error/perfect_difference_cuts
title: "Perfect-difference cuts and the lower half"
desc: "Every arc count of a perfect difference set modulo q^2+q+1 lies within sqrt(q)(1+ln(M/2)) of its mean, so cuts of moderate order reach sqrt(N)-O(N^eps) only from an order within O(N^(1/4) log N) of sqrt(N)."
created: 2026-10-15T18:04:27Z
updated: 2026-10-15T18:04:27Z
---

***

The arc estimate and its consequences are Plasma AI's author-recorded
mathematics, not independently reviewed. They use one source premise:
[[../library/additive_bases/singer_1938_theorem_finite_projective_geometry_some_applications_number_theory/theorem_p380|Singer's theorem, which supplies a perfect difference set of order q+1 modulo q^2+q+1 for every prime power q, and its remark that dilates by units and translates are again perfect]].

## Arc discrepancy of a perfect difference set

Let $q\ge2$, $M=q^2+q+1$, and let $S\subset\mathbb Z_M$ be a perfect difference
set: $|S|=q+1$ and every nonzero residue is a difference $s-s'$ of elements of
$S$ in exactly one way.

**Proposition.** For every arc $I=\{u,u+1,\ldots,u+L-1\}\subset\mathbb Z_M$
with $1\le L\le M$,

$$
\Bigl|\,|S\cap I|-\frac{(q+1)L}{M}\Bigr|<\sqrt q\,\Bigl(1+\ln\frac M2\Bigr).
$$

**Proof.** Write $\hat F(\xi)=\sum_{a\in F}e(a\xi/M)$. For $\xi\not\equiv0$,

$$
|\hat S(\xi)|^2=\sum_{s,s'\in S}e\bigl((s-s')\xi/M\bigr)
=(q+1)+\sum_{r\ne0}e(r\xi/M)=q ,
$$

because the nonzero differences run once over the nonzero residues. By
Parseval, $|S\cap I|=M^{-1}\sum_\xi\hat S(\xi)\overline{\hat I(\xi)}$, and the
term $\xi=0$ is $(q+1)L/M$. For $\xi\ne0$,
$|\hat I(\xi)|\le1/\sin(\pi\|\xi/M\|)$, and $\sin x\ge2x/\pi$ on $[0,\pi/2]$
gives, since $M$ is odd,

$$
\sum_{\xi=1}^{M-1}\frac1{\sin(\pi\xi/M)}
\le 2\sum_{\xi=1}^{(M-1)/2}\frac M{2\xi}
\le M\Bigl(1+\ln\frac{M-1}2\Bigr).
$$

So the error is at most $M^{-1}\sqrt q\,M(1+\ln\frac{M-1}2)$. $\square$

Every dilate $tS$ with $\gcd(t,M)=1$ and every translate is again a perfect
difference set, so the bound holds uniformly over all affine images and all
arcs. In the cases $q\in\{5,7,11,13,17\}$, computed over every unit dilate and
every arc of a Singer set, the largest deviation was between $1.18\sqrt q$ and
$1.43\sqrt q$, well inside the bound.

## The cut ceiling

Call $A\subset\{0,\ldots,N-1\}$ a *cut of order $q$* if there are a perfect
difference set $S$ modulo $M=q^2+q+1$ and an integer $u$ such that
$a\mapsto(a+u)\bmod M$ maps $A$ injectively into $S$. Every cut is a Sidon set,
since an equation $a+b=c+e$ in $A$ holds modulo $M$ and injectivity returns the
equality of pairs. The constructions that choose a dilate and a translate of a
Singer set and keep the elements lying in an interval are cuts.

**Corollary.** Let $A$ be a cut of order $q$ in $\{0,\ldots,N-1\}$. Then
$|A|\le q+1$, and if $M>N$,

$$
|A|<\frac Nq+\sqrt q\,\Bigl(1+\ln\frac M2\Bigr).
$$

**Proof.** The first bound is injectivity. If $M>N$, the image of
$\{0,\ldots,N-1\}$ is an arc of length $N$, so the proposition bounds $|A|$ by
$(q+1)N/M+\sqrt q(1+\ln\frac M2)$, and $(q+1)N/M\le N/q$ because
$q(q+1)<M$. $\square$

Now let $x=\sqrt N$, $0\le\Delta\le x/8$ and
$E=\sqrt{2x}\,(1+\ln(5N))$, and suppose $N$ is large enough that
$E\le 3x/8$. If a cut of order $q$ has $|A|\ge x-\Delta$, then

$$
x-\Delta-1\le q\le x+2(\Delta+E)
\qquad\text{or}\qquad
q>\frac{9N}{64(1+2\ln N)^2}.
$$

Indeed, $q+1\ge x-\Delta$ by the first bound. If $x<q\le2x$, then $M>N$,
$M\le5N$, and the corollary gives $x-\Delta<N/q+E$, so
$q<x/(1-(\Delta+E)/x)\le x+2(\Delta+E)$. If $q>2x$, then $N/q<x/2$ and the
corollary needs $\sqrt q(1+2\ln q)>3x/8$, using $M/2\le q^2$; this forces
$q>9N/(64(1+2\ln N)^2)$, directly if $q\le N$ and trivially otherwise.

## Consequence for Problem 30

The lower half of [[problems/additive_bases/E0030/_index|Problem 30]] asks for
$h(N)\ge\sqrt N-O_\epsilon(N^\epsilon)$ for every $N$. Suppose that, for some
$\epsilon<1/4$ and $C$, every large $N$ admitted a cut of order at most
$9N/(64(1+2\ln N)^2)$ with at least $\sqrt N-CN^\epsilon$ elements. Taking
$\Delta=CN^\epsilon=Cx^{2\epsilon}$, every large $x=\sqrt N$ would then have a
perfect difference set order within $O(x^{1/2}\log x)$ of $x$. In the Singer construction these orders are prime powers, so gaps between
consecutive prime powers near $x$ would
be $O(x^{1/2}\log x)$. This is a necessary short-interval input for the
specified construction class; the argument here supplies no such prime-power
gap theorem.

A proof of the lower half by Singer cuts of moderate order would therefore
imply such a prime-power gap theorem. Conversely, a prime power $q$ with
$|q-x|\le g$ gives $h(N)\ge\sqrt N-g-O(1)$. Use the whole Singer set if
$M\le N$. Otherwise the best arc of length $N$ contains at least the mean
$(q+1)N/M\ge N/(q+1)\ge x-g-1$. In particular, prime-power gaps
$O(x^{1/2}\log x)$ would supply an error $O(N^{1/4}\log N)$ by this averaging
argument. Reaching every exponent $\epsilon>0$ still needs closer parameters
or a sufficiently favorable arc count. The necessary and sufficient estimates
are distinct, and no prime-gap assertion is used as a premise here.

What the ceiling does not cover:

- Cuts of order larger than $9N/(64(1+2\ln N)^2)$. The arc estimate is then
  too weak to exclude an arc of length $N$ holding about $\sqrt N$ elements,
  far above its mean of about $N/q$. A uniform bound for such sparse cuts
  would need a stronger concentration statement than the Fourier bound.
- The Bose–Chowla and Ruzsa families. Their difference-coverage statements
  would need to be inspected before applying an analogous Fourier argument.
- Constructions not derived from a perfect difference set.

## The arc identity on the upper side

Removing an arc $W$ of length $L\le q^{3/2}$ from a Singer set leaves a Sidon
set of $k=q+1-|S\cap W|$ elements in an interval of length $N=M-L$, and

$$
k-\sqrt N=\frac L{2q}-|S\cap W|+O(1).
$$

By the proposition this is at most $\sqrt q(1+\ln\frac M2)+O(1)$, so such
cuts never exceed $\sqrt N+O(N^{1/4}\log N)$, consistent with the classical
upper bound. An arc with $|S\cap W|\le L/(2q)-G$ in some unit dilate gives
$h(N)\ge\sqrt N+G-O(1)$. Whether such arcs exist with $G\to\infty$, which
would make $h(N)-\sqrt N$ unbounded above, is not settled here; it needs the
lower tail of arc counts of Singer sets at arc lengths of order $q\log q$,
below the reach of the Fourier bound.
