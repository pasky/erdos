---
name: research/leads/totient_binary_series/integer_interpolation/shadows
title: Shadows, Flatness and the Two-Approximant Criterion
desc: |
  Two exact kernel vectors with non-proportional shadows exclude every
  denominator below 2^J over their cost; a rational value makes every large
  depth flat, an irrational value leaves infinitely many depths non-flat, and
  rounding turns two shadows and an odd starting vector into a cheap odd
  kernel vector.
problems:
- 249
research_state: ready
review_status: unreviewed
created: 2026-09-17T14:40:00Z
updated: 2026-09-17T14:40:00Z
---

***

The
[[research/leads/totient_binary_series/integer_interpolation/two_depth_carries|odd
scalar-kernel criterion]] asks for a kernel vector with odd normalized
prefix pairing and weighted cost $o(2^J)$. This page shows that the
parity can be supplied once two suitable kernel vectors and any odd
kernel vector are available.
Two exact kernel vectors whose integer
shadows $(u,v)$ are not proportional already exclude every denominator
below $2^J$ divided by their larger cost. Given any odd starting vector,
an elementary rounding turns them into an odd vector of comparable
cost. It then proves a dichotomy: a
rational value of $S$ makes every large depth *flat*, while an irrational
value leaves infinitely many depths non-flat, with polynomial cost. Hence
the sufficient cost target, with a growing cutoff on the supports
specified below, is equivalent to irrationality. This supplies alternative
construction criteria, without deciding any of them or ruling out
arithmetic and phase methods. All arguments are author-recorded and
unreviewed. Nothing here changes the status of
[[problems/irrationality/E0249/_index|Problem 249]], which is unresolved.

## Shadows of kernel vectors

Retain $\Phi_n=\sum_{m\le n}\varphi(m)2^{n-m}$, $T_n=2^nS-\Phi_n$,
$0<T_n\le n+2$, and $U_J(n)=\Phi_{n+J}-2^J\Phi_n=2^JT_n-T_{n+J}$.
Fix integers $4\le B<R$ and $J\ge1$, the support
$\mathcal N=[B,R]\cap\mathbb Z$ with $N=R-B+1$ elements, the weights
$w_n=n+J+2$, and the cost $\|z\|=\sum_nw_n|z_n|$ of an integer vector
$z=(z_n)_{n\in\mathcal N}$. Define

$$
L=\Bigl\{z\in\mathbb Z^{\mathcal N}:\ \sum_nz_nU_J(n)=0\Bigr\},\qquad
\sigma(z)=\bigl(u(z),v(z)\bigr)=\Bigl(\sum_nz_n2^n,\ \sum_nz_n\Phi_n\Bigr),
$$

and $L_{00}=\{z\in L:\sigma(z)=0\}$. The pair $\sigma(z)$ is the
*shadow* of $z$. For $z\in L$ the exact identity

$$
u(z)S-v(z)=\sum_nz_nT_n=2^{-J}\sum_nz_nT_{n+J},\qquad
|u(z)S-v(z)|\le\frac{\|z\|}{2^J},
\tag{1}
$$

is the complete-tail bound of the two-depth page. A vector is *odd* when
$v(z)\equiv2\pmod4$, which is the odd normalized prefix pairing there.

**Proposition 1 (two shadows exclude a denominator range).** Let
$z_1,z_2\in L$ have costs at most $C$ and
$u(z_1)v(z_2)\ne u(z_2)v(z_1)$. Then $S\ne a/b$ for every integer $a$
and every integer $1\le b<2^J/C$.

*Proof.* If $S=a/b$, then $b(u(z_i)S-v(z_i))=au(z_i)-bv(z_i)$ is an
integer of absolute value at most $bC/2^J<1$ by (1), hence zero. So
$(u(z_i),v(z_i))$ is a rational multiple of $(b,a)$ for both $i$, and
the two shadows are proportional. $\square$

Corollary 8 of the two-depth page is the one-vector variant: the second
approximation is replaced by the 2-adic information
$v_2(u)>v_2(b)+v_2(v)$, which also prevents $(u,v)$ from being a
multiple of $(b,a)$. Both are certificate formats for the classical
fact that a rational number with denominator $b$ admits no two
non-proportional approximations $|uS-v|<1/b$; the kernel condition
certifies the approximation from finitely many totient values.

## Flat depths

Put $C_1=\sum_{n\in\mathcal N}w_n\le N(R+J+2)$; every vector with
coefficients in $\{-1,0,1\}$ has cost at most $C_1$. Call the triple
$(B,R,J)$ *flat* when the shadows of all $z\in L$ with $\|z\|\le C_1$
span a rational space of dimension at most one, and *non-flat*
otherwise. By Proposition 1, a non-flat triple excludes every
denominator $b<2^J/C_1$.

**Lemma 2 (collisions).** Suppose $2^{N-J-1}\ge N(R+2)$. Then there is
a set $\mathcal Z\subseteq\{0,1\}^{\mathcal N}$ with
$|\mathcal Z|\ge2^{N-J}/(N(R+2))\ge2$ on which
$W(z)=\sum_nz_nU_J(n)$ is constant. For distinct $z,z'\in\mathcal Z$,
the difference $z-z'$ lies in $L$, has coefficients in $\{-1,0,1\}$,
cost at most $C_1$, and $u(z-z')\ne0$.

*Proof.* From $U_J(n)=\sum_{j=1}^J2^{J-j}\varphi(n+j)$ and
$\varphi(m)\le m$, $0<U_J(n)<2^J(n+2)$, so $W$ maps
$\{0,1\}^{\mathcal N}$ into the integers of $[0,2^JN(R+2))$, at most
$2^JN(R+2)$ values. The largest fiber has the stated size, at least $2$
under the hypothesis. Distinct subsets of $\{2^n:n\in\mathcal N\}$ have
distinct sums, so $u(z)\ne u(z')$. $\square$

**Lemma 3 (flatness forces a rational approximation).** Under the
hypothesis of Lemma 2, if $(B,R,J)$ is flat then there are coprime
integers $\alpha,\beta$ with

$$
1\le\beta\le2^{J+B+2}N(R+2),\qquad
\Bigl|S-\frac\alpha\beta\Bigr|
\le\frac{4N^2(R+2)(R+J+2)}{\beta\,2^N}.
\tag{2}
$$

*Proof.* Fix $z_0\in\mathcal Z$ and let
$D=\{z-z_0:z\in\mathcal Z,\ z\ne z_0\}$, a set of $|\mathcal Z|-1$
vectors of $L$ with cost at most $C_1$ and nonzero $u$. Flatness puts
all their shadows on one line through the origin, so $v(d)/u(d)$ is a
constant $\alpha/\beta$ in lowest terms with $\beta\ge1$, and
$\beta\mid u(d)$ for every $d\in D$. The values $u(d)=u(z)-u(z_0)$ are
distinct nonzero multiples of $\beta$ of absolute value below
$2^{R+1}$, so $|\mathcal Z|-1\le2^{R+2}/\beta$, and some $d^*\in D$ has
$|u(d^*)|\ge\beta(|\mathcal Z|-1)/2$. Since
$|\mathcal Z|-1\ge|\mathcal Z|/2\ge2^{N-J-1}/(N(R+2))$ and $R-N=B-1$,
the first inequality in (2) follows. By (1) and $v(d^*)=\alpha u(d^*)/\beta$,

$$
\Bigl|S-\frac\alpha\beta\Bigr|
=\frac{|u(d^*)S-v(d^*)|}{|u(d^*)|}
\le\frac{2C_1}{2^J\beta(|\mathcal Z|-1)}
\le\frac{4C_1N(R+2)}{\beta2^N},
$$

and $C_1\le N(R+J+2)$. $\square$

**Proposition 4 (a rational value makes every large depth flat).** If
$S=a/b$ with $b\ge1$ and $bC_1<2^J$, then $(B,R,J)$ is flat: every
$z\in L$ with $\|z\|\le C_1$ has $au(z)=bv(z)$, so its shadow lies on the
line through $(b,a)$.

*Proof.* As in Proposition 1, $|au(z)-bv(z)|\le bC_1/2^J<1$. $\square$

## Chaining and the dichotomy

Fix $B\ge4$ and take $R=3J$, so $N=3J-B+1$. The hypothesis of Lemma 2
becomes

$$
2^{2J-B}\ \ge\ (3J-B+1)(3J+2),
\tag{H}
$$

which holds for all sufficiently large $J$ (for $B=4$, for all
$J\ge7$). Put $\gamma(x)=2B+4+6\log_2(5x)$.

**Lemma 5 (chaining).** Let $J<J'$ both satisfy (H), let both triples
$(B,3J,J)$ and $(B,3J',J')$ be flat, and let $\alpha/\beta$ and
$\alpha'/\beta'$ be the fractions supplied by Lemma 3. If
$\alpha/\beta\ne\alpha'/\beta'$ then $J'\ge3J-\gamma(J')$. In
particular, flat depths $J<J'<3J-\gamma(3J)$ share the same fraction.

*Proof.* Distinct fractions differ by at least $1/(\beta\beta')$, so

$$
1\le\beta\beta'\Bigl(\Bigl|S-\frac\alpha\beta\Bigr|
 +\Bigl|S-\frac{\alpha'}{\beta'}\Bigr|\Bigr).
$$

Insert (2) for both depths and the bounds $\beta'\le2^{J'+B+2}N'(R'+2)$,
$\beta\le2^{J+B+2}N(R+2)$, with $N=3J-B+1$, $R=3J$, $N'=3J'-B+1$,
$R'=3J'$. The first product is at most
$2^{J'-3J+2B+3}\,N'(R'+2)N^2(R+2)(R+J+2)$ and the second at most
$2^{J-3J'+2B+3}\,N(R+2)N'^2(R'+2)(R'+J'+2)$. Each polynomial factor is
at most $5J'$, and the second power of two is the smaller one, so
$1\le2^{J'-3J+2B+4}(5J')^6$, which is the claim. If $J'<3J-\gamma(3J)$
then $J'<3J-\gamma(J')$ because $\gamma$ is increasing and $J'<3J$.
$\square$

**Theorem 6 (flatness dichotomy).** Fix $B\ge4$ and $R=3J$.

1. If $S=a/b$ is rational, then $(B,3J,J)$ is flat for every $J$ with
   $bC_1<2^J$, where $C_1=\sum_{n=B}^{3J}(n+J+2)$.
2. If $S$ is irrational, let $F$ be the set of depths $J$ satisfying
   (H) at which $(B,3J,J)$ is flat. Either $F$ is finite, so that every
   sufficiently large depth is non-flat, or $F$ is infinite and there
   are infinitely many $x\in F$ such that every integer $J$ with
   $x<J<3x-\gamma(3x)$ is non-flat. In both cases the non-flat depths
   include infinitely many powers of two and infinitely many members of
   every arithmetic progression.

*Proof.* Part 1 is Proposition 4. For part 2, the right side of (2)
tends to zero as $J\to\infty$ with $\beta\ge1$, so for each fraction
$\alpha/\beta\ne S$ the set of $J\in F$ with that fraction is finite.
Let $x$ be the largest element of one such class. A flat $J'$ with
$x<J'<3x-\gamma(3x)$ would share the fraction of $x$ by Lemma 5,
contradicting maximality; so that whole interval is non-flat. If $F$ is
infinite it meets infinitely many classes, each with its own maximum.
For large $x$ the interval $(x,3x-\gamma(3x))$ contains $(x,2x]$, hence
a power of two and every residue class modulo any fixed modulus.
$\square$

**Corollary 7 (equivalence).** For every $B\ge4$ the following are
equivalent: $S$ is irrational; $(B,3J,J)$ is non-flat for infinitely
many $J$; $(B,3J,J)$ is non-flat for infinitely many $J=2^m$. A non-flat
depth supplies, by Proposition 1 with $C=C_1$, two exact kernel vectors
excluding every denominator $b<2^J/C_1$; since $2^J/C_1\to\infty$,
infinitely many of them exclude every denominator.

*Proof.* Theorem 6 gives the forward implications and Proposition 1
with Proposition 4 the converse. $\square$

**Corollary 7a (a growing cutoff).** Theorem 6 and Corollary 7 also hold
with

$$
B=B_J=\max\{4,\lfloor\log_2(J+1)\rfloor\},\qquad R=3J,
$$

and with $\gamma(x)=2\max\{4,\lfloor\log_2(x+1)\rfloor\}
+4+6\log_2(5x)$ in the intervals of Theorem 6.
All assertions concern sufficiently large depths, so $B_J<R$.

*Proof.* The collision hypothesis holds eventually. In the chaining
calculation the exponent $2B$ becomes $B_J+B_{J'}\le2B_{J'}$ for
$J<J'$, so the same proof gives the displayed $\gamma$.
The errors in (2) still tend to zero, and $\gamma(3x)=O(\log x)$.
Thus each rational fraction occurs at only finitely many flat depths
under irrationality, and the same class-maximum argument applies.
Conversely $C_1=O(J^2)$ still makes infinitely many non-flat depths
exclude every fixed denominator. $\square$

The proof of part 2 constructs no vector: it derives the existence of
non-flat depths from the hypothesis that $S$ is irrational. This is
one useful equivalence on the specified wider supports. One sufficient
way to prove irrationality is to show non-flatness at infinitely many
depths, that is, produce two
exact kernel vectors of cost at most $C_1$ with non-proportional
shadows. A direct odd-vector or phase construction can instead use the
two-depth criterion. The equivalence does not prove that these tasks
are inaccessible or that one must first settle irrationality by another
method. It makes no claim of equivalence on the narrower $[J,2J]$.

## Flat depths and partial quotients

**Proposition 8.** Assume (H) and $N^3(R+2)^2(R+J+2)<2^{2J-2B-4}$ with
$R=3J$, $N=3J-B+1$. If $(B,3J,J)$ is flat, then either
$S=\alpha/\beta$, where $\alpha/\beta$ is the fraction of Lemma 3,
or it is a nonterminal convergent $p_k/q_k$ of $S$ with
$q_k=\beta\le2^{J+B+2}N(R+2)$, and the next partial quotient satisfies

$$
a_{k+1}\ >\ \frac{2^{2J-2B-3}}{N^3(R+2)^2(R+J+2)}-2 .
$$

*Proof.* The second hypothesis and the first bound in (2) give
$|S-\alpha/\beta|<1/(2\beta^2)$. After separating equality with $S$,
Legendre's theorem makes $\alpha/\beta$ a nonterminal convergent.
From $|S-p_k/q_k|>1/(q_k(q_k+q_{k+1}))$ and (2),
$q_k+q_{k+1}\ge2^N/(4N^2(R+2)(R+J+2))$, and
$a_{k+1}>q_{k+1}/q_k-1$ with $q_k\le2^{J+B+2}N(R+2)$ and
$N-J-B-4=2J-2B-3$. $\square$

This is a necessary large-partial-quotient condition for a flat depth
whose fraction differs from $S$, not a converse characterization.
If $S$ were known to be irrational with irrationality measure less
than $4$, only finitely many depths could be flat for a fixed $B$.
Indeed choose $\mu<4$ above that measure. At sufficiently large flat
depths the distinct approximants have growing denominators and satisfy
$|S-\alpha/\beta|\ge\beta^{-\mu}$. Equation (2) and the denominator
bound would then give
$1\le O_B(J^{2\mu+2}2^{(\mu-4)J})$, a contradiction.
No such irrationality or measure bound is known here.

**Corollary 9 (a finite range of non-flat depths).** Take $B=4$. The
[[research/leads/totient_binary_series/evidence/_index|certified continued-fraction
prefix]] of $S$ has $11759$ partial quotients, largest quotient $15531$,
and a last common convergent whose denominator has $6018$ decimal
digits; these are fixed expectations of that evidence. Consequently
$(4,3J,J)$ is non-flat for every $33\le J\le19950$.

*Proof.* Suppose $(4,3J,J)$ is flat with $33\le J\le19950$. Then (H)
and the second hypothesis of Proposition 8 hold, and the convergent
$p_k/q_k$ of Proposition 8 has $q_k\le2^{J+6}(3J-3)(3J+2)<10^{6017}$,
below the denominator of the last common convergent. The same certified
prefix rules out equality $S=\alpha/\beta$ at so small a denominator:
its enclosing cylinder has Farey-neighbor endpoints, and every rational
strictly between them has denominator larger than the last common
convergent's denominator.
Hence the nonterminal alternative of Proposition 8 applies, $k+1\le11758$
and $a_{k+1}\le15531$. But
$2^{2J-11}\ge15533\,(3J-3)^3(3J+2)^2(4J+2)$ for $J\ge33$, so
Proposition 8 gives $a_{k+1}>15531$. All four integer inequalities at
every depth in the stated finite range are checked in
[shadows.py](evidence/shadows.py), together with the failed quotient
bound at $J=32$ and failed denominator bound at $J=19951$. $\square$

The corollary exhibits no vector; each of these depths carries two
exact kernel vectors of cost at most $C_1$ with non-proportional
shadows, excluding $b<2^J/C_1$, which is weaker than the
continued-fraction exclusion itself. It certifies finite non-flatness;
it does not choose a side of the infinite rationality dichotomy.

## Two shadows make an odd kernel vector

This section gives a conditional way to construct an odd vector. Write
$r_k=e_k-2e_{k-1}$ for $B<k\le R$, $f_k=\varphi(k)$ and
$g_k=\varphi(k+J)$; all $f_k,g_k$ are even.

**Lemma 10 (the shadow-zero sublattice is cheap).** Every
$z\in\mathbb Z^{\mathcal N}$ with $u(z)=0$ is $\sum_kc_kr_k$ with
integers $c_k$, and then $v(z)=\sum_kc_kf_k$ and
$\sum_nz_nU_J(n)=-\sum_kc_k(2^Jf_k-g_k)$. Hence
$z\in L_{00}$ exactly when $\sum_kc_kf_k=0=\sum_kc_kg_k$. If the rows
$(f_k)$ and $(g_k)$ are not proportional, $L_{00}$ has rank $N-3$ and
contains $N-3$ linearly independent vectors of cost at most
$18(R+J+2)^3$.

*Proof.* The kernel of $z\mapsto\sum_nz_n2^n$ is generated by the
$r_k$: subtract $z_Re_R-2z_Re_{R-1}$ and descend. The two formulas
follow from $\Phi_k-2\Phi_{k-1}=\varphi(k)$ and
$U_J(k)-2U_J(k-1)=\varphi(k+J)-2^J\varphi(k)$. Fix $a<b$ with
$D=f_ag_b-f_bg_a\ne0$. For $k\notin\{a,b\}$ the cross product
$c^{(k)}=D\,e_k+(f_bg_k-f_kg_b)e_a+(f_kg_a-f_ag_k)e_b$ annihilates
both rows, the $N-3$ vectors are independent because each owns its
$e_k$ coordinate, and $\|c^{(k)}\|_1\le6R(R+J)$ since $f\le R$ and
$g\le R+J$. Then $x^{(k)}=\sum_lc^{(k)}_lr_l$ has cost at most
$3(R+J+2)\|c^{(k)}\|_1\le18(R+J+2)^3$. $\square$

**Proposition 11 (rounding two shadows to an odd vector).** Suppose
$z_1,z_2\in L$ have $u(z_1)v(z_2)\ne u(z_2)v(z_1)$ and some $z_0\in L$
is odd. Then $L$ contains an odd vector $z$ with

$$
\|z\|\le\|z_1\|+\|z_2\|+9(N-3)(R+J+2)^3 .
\tag{3}
$$

*Proof.* If $z_1$ or $z_2$ is odd there is nothing to prove.
Otherwise $v(z_1)\equiv v(z_2)\equiv0\pmod4$. The $N-1$ vectors
$b_1,\dots,b_{N-1}$ consisting of $z_1$, $z_2$ and the $x^{(k)}$ of
Lemma 10 are available because the two independent shadows force the
rows $(f_k),(g_k)$ to be independent. To see this, if their rank is
$r$, the recurrence coordinates of Lemma 10 give
$\dim L_{00}=N-1-r$, whereas $\dim L=N-1$; hence
$\dim\sigma(L)=r$. The two shadows force $r=2$ and $N\ge3$.
The displayed $N-1$ vectors are linearly independent: applying
$\sigma$ to a vanishing
combination kills the $x^{(k)}$ and leaves
$\lambda\sigma(z_1)+\mu\sigma(z_2)=0$, so $\lambda=\mu=0$, and then
the $x^{(k)}$ coefficients vanish. As $L\otimes\mathbb Q$ has dimension
$N-1$, $z_0=\sum_i\alpha_ib_i$ with rational $\alpha_i$. Let $m_i$ be
nearest integers and $z=z_0-\sum_im_ib_i\in L$. Then
$\|z\|\le\sum_i|\alpha_i-m_i|\,\|b_i\|\le\frac12\sum_i\|b_i\|$, which
is at most the right side of (3), and $v(z)\equiv v(z_0)\equiv2\pmod4$
because every $v(b_i)$ is divisible by four. $\square$

This is direct rounding in a named real basis of the kernel space.
An integer basis of the whole lattice is unnecessary. The
odd start $z_0$ may be arbitrarily expensive: the two-term vector of
Proposition 9 on the two-depth page, of cost about $J^22^J$ divided
by a gcd, serves, and the rounding removes its size.

**Corollary 12 (a polynomial subsequence and its correct cutoff).**
Let $B\ge4$ and $R=3J$. If $(B,3J,J)$ is non-flat and $L$ contains an
odd vector, then $L$ contains an odd vector of cost at most
$2C_1+9(N-3)(4J+2)^3$, which is $O(J^4)$. Consequently:

- If $S$ is irrational, then for each fixed $B$, and also with the
  growing cutoff $B_J$ of Corollary 7a, infinitely many depths $J=2^m$
  carry an odd exact kernel vector on $[B,3J]$ of cost $O(J^4)$.
  Non-flatness follows from Theorem 6 or Corollary 7a, and an odd
  vector on $[J,2J]\subseteq[B,3J]$ exists for every large $J$ with
  $5\nmid J$ by Proposition 9 of the two-depth page, whose external
  input is the prime number theorem for the fixed modulus $20$ at its
  disclosed standing.
- If $S=a/b$ with $v_2(b)<B-1$, every odd vector at every depth costs
  at least $2^{J+1}/b_{\mathrm{odd}}$, by Proposition 6 of the two-depth
  page.

Consequently irrationality is equivalent to the existence of a family
on $[B_J,3J]$, $J\to\infty$, with odd pairing and cost $o(2^J)$;
irrationality would even supply an $O(J^4)$ family along some powers
of two. The reverse implication uses $B_J\to\infty$ in Corollary 7
of the two-depth page. A family for only one fixed $B$ excludes only
the denominators with $v_2(b)<B-1$ by this argument.

No estimate at every depth, on every infinite subset of depths, or
on the narrower support $[J,2J]$ follows from this construction.
In particular an upper bound
for one subsequence does not determine the order of the minimum
elsewhere. The required construction without assuming irrationality
remains open.

**Corollary 13 (realizing a shadow).** Let $(u,v)\in\mathbb Z^2$ with
$2^B\mid u$, $0<|u|<2^{R-1}$ and $v$ even. Let $z^{(0)}$ be the
signed-digit vector of $u$ on $[B,R]$, given by
$\nu_m=\operatorname{round}(u/2^m)$ and
$z^{(0)}_m=\nu_m-2\nu_{m+1}\in\{-1,0,1\}$, and put
$X=v-v(z^{(0)})$ and $Y=2^JX-\sum_nz^{(0)}_nU_J(n)$. Then

$$
Y=2^J\bigl(v-uS\bigr)+\sum_nz^{(0)}_nT_{n+J},\qquad
|Y|\le2^J|uS-v|+\|z^{(0)}\|,
$$

both $X$ and $Y$ are even, and if integers $c_k$ solve
$\sum_kc_kf_k=X$ and $\sum_kc_kg_k=Y$, then
$z=z^{(0)}+\sum_kc_kr_k\in L$ has $\sigma(z)=(u,v)$ and
$\|z\|\le\|z^{(0)}\|+3(R+J+2)\|c\|_1$. The system is solvable exactly
when $(X,Y)$ lies in the lattice generated by the columns $(f_k,g_k)$,
which is all of $2\mathbb Z^2$ when the normalized minors
$a_ka_{l+J}-a_la_{k+J}$, $a_m=\varphi(m)/2$, have no common prime
factor; this is not proved here for all depths.

*Proof.* The identity for $Y$ is (1) applied to the digit vector,
using $\sum_nz^{(0)}_n2^n=u$; $v(z^{(0)})$ is even because every
$\Phi_n$ on the support is even, and $U_J(n)$ is even. Lemma 10
gives the effect of the correction. $\square$

**Proposition 14 (determinant-scaled realization).** Suppose
$a,b\in(B,R]$ satisfy $D=f_ag_b-f_bg_a\ne0$. Let $u,v$ be integers
with $2^B\mid u$, $0<|u|<2^{R-1}$ and
$2^J|uS-v|\le1$. Put $H=R+J+2$, and form $z^{(0)},X,Y$ as in
Corollary 13. Then the explicit vector

$$
c_a=g_bX-f_bY,\qquad c_b=f_aY-g_aX,\qquad
z=Dz^{(0)}+c_ar_a+c_br_b
$$

belongs to $L$, has shadow $(Du,Dv)$, and has cost at most $30H^4$.
No full-image or coprimality condition on the two rows is needed.

*Proof.* The adjugate identities give
$f_ac_a+f_bc_b=DX$ and $g_ac_a+g_bc_b=DY$.
The change in the scalar row is therefore
$D(Y-2^JX)=-DW(z^{(0)})$, and Lemma 10 gives the claimed shadow.
Writing $C_0=\|z^{(0)}\|\le NH\le H^2$, the tail identities give
$|X|,|Y|\le1+H^2$. Also $|D|\le2H^2$,
$|c_a|+|c_b|\le2H(|X|+|Y|)$ and $\|r_k\|\le3H$. Consequently

$$
\|z\|\le2H^4+12H^2(1+H^2)\le26H^4<30H^4.
$$

The same $D$ scales both desired shadows, so it multiplies their
determinant by $D^2$ and preserves non-proportionality. $\square$

This removes the lattice-membership obstacle when scaled shadows suffice.
Exact unscaled realization in Corollary 13 has its stated additional
hypothesis; the two tasks should not be conflated.

**Corollary 15 (a narrower reverse construction).** If $S$ is
irrational, then along an unbounded sequence of depths $J$ there are
odd kernel vectors of cost $O(J^4)$ on supports $[B,R]$ with
$B\to\infty$ and $R=J+O(\log J)$. This uses the fixed-modulus prime
number theorem at the disclosed standing of Proposition 9 of the
two-depth page. It does not assert $B=J$ or support $[J,2J]$.

*Proof.* Let $p_k/q_k,p_{k+1}/q_{k+1}$ be consecutive convergents and set

$$
L_k=\lfloor\log_2q_{k+1}\rfloor,\quad
B=\lfloor\log_2L_k\rfloor,\quad J_0=L_k-B-8,\quad
R=B+\lceil\log_2q_{k+1}\rceil+2.
$$

Ignore finitely many $k$ so $B\ge4$. Choose $J\in\{J_0-1,J_0\}$ with
$5\nmid J$. Then $J\to\infty$, $R/J\to1$, and the two shadows
$u_i=2^Bq_i$, $v_i=2^Bp_i$ for $i=k,k+1$ satisfy the digit bound
of Proposition 14 and
$2^J|u_iS-v_i|<2^{J+B}/q_{k+1}\le2^{-8}$.
Their determinant is $\pm2^{2B}$.

Choose separate primes $a\in[\lceil R/2\rceil,R]$ and
$p\in[J+\lceil R/2\rceil,J+R]$ with
$a,p\equiv3\pmod4$, $a\equiv-J\pmod5$, $p\equiv J\pmod5$;
put $b=p-J$. The two reduced classes modulo 20 and $R/J\to1$
give both choices eventually by the fixed-modulus theorem. There are
only four classes in either choice, so the threshold is uniform over
the selected $J$. No simultaneous-prime assertion is used.
For large $k$ the indices $a,b$ are distinct and exceed $B$.
The normalized pairs $(f_a/2,g_a/2)$ and $(f_b/2,g_b/2)$ have
parities $(1,0)$ and $(0,1)$, so $D/4$ is odd. The identical
prefix/window parities supply an odd two-term kernel vector.

Apply Proposition 14 twice and Proposition 11. Since $N\le H$,
the final cost is at most $60H^4+9(N-3)H^3<70H^4=O(J^4)$.
All existence claims in this proof use the hypothesis that $S$ is
irrational; the proof is not an unconditional construction. $\square$

The evidence [shadows.py](evidence/shadows.py) exercises Corollary 13,
Lemma 10 and Propositions 11 and 14 in exact arithmetic at $B=8$ and
$J\in\{32,64,128,200\}$. It takes the shadows $2^B(q,p)$ of two
consecutive convergents of $S$, checking that both enclosure endpoints
share the selected prefix. It realizes both, separately checks the
determinant-scaled construction, builds the $N-3$ cross vectors, and
rounds the two-term odd vector. The kernel identity certifies the
resulting full-tail error bound. It also replays the 40000-term
continued-fraction enclosure used by Corollary 9 and checks that
corollary's integer inequalities at every stated depth. The
recorded outcomes are:

| $J$ | $R$ | $N$ | costs of the two realized vectors | $u_1v_2-u_2v_1$ | largest cross-vector cost | rounded odd cost | odd exclusion $b_{\rm odd}<2^{J+1}/C$ |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 32 | 60 | 53 | 37894, 32353 | $2^{16}$ | 321632 | 459427 | $1.8\cdot10^4$ |
| 64 | 92 | 85 | 894591, 127148 | $2^{16}$ | 1955928 | 1563054 | $2.3\cdot10^{13}$ |
| 128 | 155 | 148 | 267339, 917571 | $-2^{16}$ | 10751440 | 14707970 | $4.6\cdot10^{31}$ |
| 200 | 226 | 219 | 2806263, 30824564 | $-2^{16}$ | 30861984 | 31343164 | $1.0\cdot10^{53}$ |

The odd start vectors cost between $5\cdot10^{11}$ and $5\cdot10^{63}$;
the rounded vectors lie far below the bound (3). Both convergent
vectors are even at every depth, as $v=2^Bp$ predicts, so the odd
vector arises from the rounding alone. These are outcomes of one
construction with a crude correction step, not minima, and their
exclusions are far weaker than the continued-fraction record.

## What this settles and what remains

The qualitative bridges and the stated reverse implications are proved
here at author standing. Constructing the requisite family without
assuming irrationality remains open. In particular the polynomial upper
bound under irrationality concerns a subsequence on specified supports;
finite costs do not establish that hypothesis, and no all-depth
polynomial-versus-exponential dichotomy has been proved.

Two independent cheap shadows remove the need to construct parity
separately, provided an odd vector exists and the polynomial rounding
cost is small enough. Conversely a direct arithmetic construction of an
odd vector, a phase estimate, or a controlled integer-coset argument
might supply the original sufficient criterion without first producing
those two shadows. The gcd, residue-repair, conditional-count and Fourier
questions on the two-depth page remain possible approaches, with their
original hypotheses and limitations. Equivalence to the target does not
retire them.

The [[research/leads/totient_binary_series/integer_interpolation/phase_transference|phase
comparison]] uses Lemma 10's vectors to reduce the relevant dual problem
to a two-dimensional quotient. It obtains a converse to the phase-cost
lower bound up to an additive polynomial term, leaving a precise
totient-specific phase-growth estimate open.

A separate
[[research/leads/totient_binary_series/integer_interpolation/phase_localization|arithmetic
localization]] proves that irrationality is also equivalent to an
odd $o(2^J)$ family on $[J,2J]$ along a subsequence of powers of two.
That proof uses the totient identity at $2k,3k$ and rational phases;
it does not restrict the vectors constructed here. It supplies no
polynomial bound on that short support and no all-depth divergence.

Nor has arbitrary good rational approximation been equated with cheap
unscaled realization: Corollary 13 retains its lattice condition, while
Proposition 14 realizes a determinant multiple at a quantified cost.
These distinctions and the full-tail bound (1) remain part of any
construction consumed by the
[[research/leads/totient_binary_series/_index|main sketch]].
