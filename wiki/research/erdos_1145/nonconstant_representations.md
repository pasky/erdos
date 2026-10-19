---
name: research/erdos_1145/nonconstant_representations
desc: Every bounded representation function of a balanced pair differs from each nonzero periodic pattern on a set of positive lower density.
tags: [proved, reductions]
sources: []
created: 2026-09-22T18:25:06Z
updated: 2026-10-13T05:28:09Z
---


# research/erdos_1145/nonconstant_representations

***

## Theorem

Suppose $A,B$ are infinite positive integer sets with $a_n/b_n\to1$.
If their representation function $r=r_{A,B}$ is bounded, it cannot equal
a fixed positive integer $k$ on a set of natural density one.

In particular, under the hypotheses of Problem 1145, the representation
function is not eventually constant. This is a restricted result: it does
not exclude a bounded function with several values occurring at positive
densities.

The proof below is author-recorded; no independent verification record
exists. It uses only elementary Laplace-transform arguments, weak
convergence of finite measures, and the Hilbert-space criterion that weak
convergence plus convergence of norms implies strong convergence.

## Laplace asymptotics

Assume for contradiction that $r(n)=k$ outside a density-zero set. Write

$$
F(t)=\sum_{a\in A}e^{-ta},\quad G(t)=\sum_{b\in B}e^{-tb},\quad H(t)=F(t)G(t).
$$

Boundedness and density-one equality imply, by summation by parts,

$$
H(t)\sim k/t,\qquad
\sum_n r(n)^2e^{-tn}\sim k^2/t\quad(t\downarrow0).
\tag{1}
$$

Termwise balance gives, for any fixed $0<\varepsilon<1$,

$$
G((1+\varepsilon)t)-C_\varepsilon\le F(t)
\le G((1-\varepsilon)t)+C_\varepsilon.
$$

Using monotonicity of $F$, these inequalities give

$$
H((1+\varepsilon)t)\le F(t)(F(t)+C_\varepsilon),\qquad
F(t)(F(t)-C_\varepsilon)\le H((1-\varepsilon)t).
$$

Equation (1), followed by $\varepsilon\downarrow0$, proves

$$
F(t)\sim G(t)\sim\sqrt{k}\,t^{-1/2}.
\tag{2}
$$

For $\lambda>0$, define finite measures

$$
\mu_{N,\lambda}=N^{-1/2}\sum_{a\in A}e^{-\lambda a/N}\delta_{a/N},
\quad
\nu_{N,\lambda}=N^{-1/2}\sum_{b\in B}e^{-\lambda b/N}\delta_{b/N}.
$$

They both converge weakly to $p_\lambda(x)\,dx$, where

$$
p_\lambda(x)=\sqrt{k/\pi}\,x^{-1/2}e^{-\lambda x}\mathbf1_{x>0}.
\tag{3}
$$

Here is a direct justification, avoiding a separate Tauberian invocation.
Their masses converge by (2), and their mass above $R$ is at most
$e^{-\lambda R/2}N^{-1/2}F(\lambda/(2N))$, or its $G$ analog.
They are therefore tight. Every subsequential limit has Laplace transform
$\sqrt{k}(\lambda+s)^{-1/2}$ for $s\ge0$, again by (2).
Uniqueness of Laplace transforms identifies it with (3).

## A weighted difference energy

For integer $t$, put

$$
D_{N,\lambda}(t)=\sum_{a-b=t}e^{-\lambda(a+b)/N},
\qquad f_{N,\lambda}(u)=D_{N,\lambda}(\lfloor Nu\rfloor).
$$

Rearranging nonnegative sums gives the exact energy identity

$$
\int_{\mathbb R}f_{N,\lambda}(u)^2\,du
=\frac1N\sum_n r(n)^2e^{-2\lambda n/N}
\longrightarrow\frac{k^2}{2\lambda}.
\tag{4}
$$

Indeed $a-b=a'-b'$ is equivalent to $a+b'=a'+b=n$, and the weight
of either quadruple is $e^{-2\lambda n/N}$.

The measure $f_{N,\lambda}(u)\,du$ is the convolution of
$\mu_{N,\lambda}*\widetilde\nu_{N,\lambda}$ with uniform probability
on $[0,1/N)$; tilde denotes reflection. Hence it converges weakly to
$h_\lambda(u)\,du$, with

$$
h_\lambda=p_\lambda*\widetilde p_\lambda.
$$

There is a continuous counterpart of the same energy identity:

$$
\|p*\widetilde p\|_2^2=\|p*p\|_2^2
\tag{5}
$$

for every nonnegative integrable $p$, permitting infinite values.
For completeness, expand the left side as
$\int p(x)p(x-u)p(y)p(y-u)\,dx\,dy\,du$, and change variable
$s=x+y-u$. Tonelli's theorem yields the right side.
The beta integral gives

$$
(p_\lambda*p_\lambda)(s)=ke^{-\lambda s}\mathbf1_{s>0}.
$$

Thus (5) says $\|h_\lambda\|_2^2=k^2/(2\lambda)$. The uniform
$L^2$ bound (4) and weak measure convergence imply weak $L^2$
convergence, by first testing against compactly supported continuous
functions and then using their density in $L^2$. Equality of the limiting
norms now gives

$$
f_{N,\lambda}\longrightarrow h_\lambda\quad\hbox{strongly in }L^2.
\tag{6}
$$

## The contradiction from individual atoms

For every integer $t$, positivity gives

$$
D_{N,1}(t)^2\ge D_{N,2}(t).
\tag{7}
$$

This simply retains the diagonal terms in the square. By (6),
$f_{N,1}^2\to h_1^2$ in $L^1$. Testing (7) against nonnegative
compactly supported continuous functions and using weak measure
convergence for $\lambda=2$ gives

$$
h_1(u)^2\ge h_2(u)\quad\hbox{for almost every }u.
\tag{8}
$$

But for $u>0$, formula (3) gives

$$
h_\lambda(u)=\frac{k}{\pi}\int_u^\infty
\frac{e^{-\lambda s}}{\sqrt{s^2-u^2}}\,ds
\sim\frac{k}{\sqrt{2\pi\lambda u}}e^{-\lambda u}
\quad(u\to\infty).
$$

The asymptotic follows by substituting $s=u+v$ and dominated convergence
after multiplying the integral by $\sqrt u e^{\lambda u}$.
Consequently

$$
\frac{h_1(u)^2}{h_2(u)}\sim\frac{k}{\sqrt{\pi u}}\longrightarrow0,
$$

contradicting (8). This proves the theorem.

## What does not follow

With a general bounded $r$, weak convergence of $f_{N,\lambda}$ still
has a useful interpretation, but (4) need not equal the norm of the weak
limit. Microscopic variance of $r$ leaves an energy gap, so the decisive
strong convergence (6) is unavailable. Replacing weak convergence by strong
convergence without this equality would incorrectly assert the full problem.

## Extension: eventual periodicity is also impossible

The same method proves a stronger restriction.

**Theorem.** If $a_n/b_n\to1$ and $r_{A,B}$ is bounded, it cannot agree
on a density-one set with a nonzero nonnegative periodic sequence.

Here the period may be any fixed positive integer $P$, and some residue
values may be zero. This extension is also author-recorded.

**Proof.** Suppose the periodic values are $c_0,\ldots,c_{P-1}$, with
$\kappa=P^{-1}\sum_j c_j>0$. The preceding Laplace argument gives the
same total limiting measures $p_\lambda(x)\,dx$, with $k$ replaced by
$\kappa$.

Split the measures $\mu_{N,1},\nu_{N,1}$ according to the residue classes
of $a,b$ modulo $P$. Along a common subsequence all $2P$ component
measures converge weakly. Each limiting measure is dominated by
$p_1(x)\,dx$, so it has a nonnegative density. Write these densities as
$u_{i,1},v_{i,1}$. Multiplication by $e^{-x}$ also supplies convergence
at $\lambda=2$, to $u_{i,2}=e^{-x}u_{i,1}$ and
$v_{i,2}=e^{-x}v_{i,1}$. For $\lambda=1,2$,
$$
\sum_i u_{i,\lambda}=\sum_i v_{i,\lambda}=p_\lambda.
$$
All group indices in what follows are taken modulo $P$.

Define the sum and difference density vectors
$$
s_{j,\lambda}=\sum_i u_{i,\lambda}*v_{j-i,\lambda},
\qquad
h_{j,\lambda}=\sum_i u_{i,\lambda}*\widetilde v_{i-j,\lambda}.
$$
The sum measures count the representations with $n\equiv j\pmod P$.
Density-one agreement and boundedness therefore give exactly
$$
s_{j,\lambda}(x)=\frac{c_j}{P}e^{-\lambda x}\mathbf1_{x>0}.
\tag{9}
$$

The energy identity on $\mathbb R\times\mathbb Z/P\mathbb Z$ is
$$
\sum_j\|h_{j,\lambda}\|_2^2
=\sum_j\|s_{j,\lambda}\|_2^2
=\frac{\sum_j c_j^2}{2\lambda P^2}.
\tag{10}
$$
It needs no regularity beyond nonnegativity and integrability. To verify
the first equality directly, expand its left side as the sum over
$j,i,\ell$ of
$$
\iiint u_{i,\lambda}(x)u_{\ell,\lambda}(y)
v_{i-j,\lambda}(x-z)v_{\ell-j,\lambda}(y-z)\,dx\,dy\,dz.
$$
Set $s=x+y-z$ and replace $j$ by $i+\ell-j$ in the finite group.
Tonelli's theorem gives the right-hand energy.

To match the discrete functions to these profiles, put
$$
f_{N,j,\lambda}(u)
=D_{N,\lambda}\!\left(j+
 P\left\lfloor\frac{Nu-j}{P}\right\rfloor\right).
$$
These are constant on cells of length $P/N$, starting at the actual
points $(j+P\ell)/N$. Their weak measure limits are
$P h_{j,\lambda}(u)\,du$, and their total squared norms satisfy
$$
\sum_j\|f_{N,j,\lambda}\|_2^2
=\frac PN\sum_n r(n)^2e^{-2\lambda n/N}
\longrightarrow\frac{\sum_jc_j^2}{2\lambda}.
\tag{11}
$$
Equations (10)--(11) give strong convergence in the vector-valued
$L^2$ space.

The pointwise diagonal inequality at each integer difference again gives,
in the limit,
$$
P h_{j,1}(u)^2\ge h_{j,2}(u)\quad\text{almost everywhere}.
$$
All profiles are nonnegative, and their sums are
$$
\sum_j h_{j,\lambda}
=p_\lambda*\widetilde p_\lambda=:h_\lambda.
$$
Consequently
$$
h_2\le P\sum_j h_{j,1}^2\le P h_1^2.
$$
This contradicts $h_1(u)^2/h_2(u)\sim\kappa/\sqrt{\pi u}\to0$.
The extension follows. ∎

This still does not address an arbitrary bounded representation function:
finite-period structure supplies the exact energy equality (10)--(11).
Without it, a nonzero energy deficit can remain after every fixed finite
residue decomposition.

## Strengthening: positive lower density of disagreement

The same argument excludes periodic agreement even along a subsequence
of initial intervals with vanishing relative error.

**Theorem.** Let $A,B$ be infinite positive integer sets with
$a_n/b_n\to1$, and suppose $r=r_{A,B}$ is bounded. For every
fixed nonzero nonnegative integer-valued periodic sequence $c(n)$,
$$
 \liminf_{X\to\infty}\frac1X
 \#\{1\le n\le X:r(n)\ne c(n)\}>0.
\tag{12}
$$
No coverage hypothesis is needed. In particular, a bounded counterexample
to Problem 1145 would differ from every fixed positive constant on a set
of positive lower density. This does not rule out such a counterexample.

**Proof.** Write $E(X)$ for the cardinality in (12). If its lower
density were zero, there would be $X_j\to\infty$ with
$E(X_j)=o(X_j)$. Set
$$
 N_j=\sqrt{X_j(E(X_j)+1)}.
$$
Then $N_j\to\infty$, $X_j/N_j\to\infty$, and
$E(X_j)/N_j\to0$. Let $P$ be a period of $c$, and let
$c_i$ be its value in residue class $i\pmod P$.
For every fixed $\lambda>0$, $m\in\{1,2\}$, and residue $i$,
boundedness gives
$$
 \begin{split}
 &\frac1{N_j}\sum_{\substack{n\ge1\\n\equiv i\ (P)}}
 |r(n)^m-c(n)^m|e^{-\lambda n/N_j}\\
 &\qquad\le C_m\frac{E(X_j)}{N_j}
 +\frac{C_m}{N_j}\sum_{n>X_j}e^{-\lambda n/N_j}
 \longrightarrow0.
 \end{split}
\tag{13}
$$
The geometric series in each residue class consequently yields
$$
 \frac1{N_j}\sum_{\substack{n\ge1\\n\equiv i\ (P)}}
 r(n)^m e^{-\lambda n/N_j}
 \longrightarrow\frac{c_i^m}{P\lambda}.
\tag{14}
$$

For clarity, these subsequential moment limits suffice for every step
of the periodic proof above. Put $\kappa=P^{-1}\sum_i c_i>0$.
Summing (14) for $m=1$ gives
$$
 N_j^{-1}F(\lambda/N_j)G(\lambda/N_j)\to\kappa/\lambda.
$$
The rank-balance Laplace squeeze used in (2), applied at every fixed
multiple of $1/N_j$, gives
$$
 N_j^{-1/2}F(\lambda/N_j),\quad
 N_j^{-1/2}G(\lambda/N_j)\longrightarrow\sqrt{\kappa/\lambda}.
$$
Hence the total weighted counting measures converge to
$p_\lambda(x)\,dx$, with
$p_\lambda(x)=\sqrt{\kappa/\pi}\,x^{-1/2}e^{-\lambda x}
\mathbf1_{x>0}$. Extracting the finitely many residue components
supplies the densities $u_{i,\lambda},v_{i,\lambda}$ as above.
Equation (14) for $m=1$, also with an additional Laplace test
parameter, gives exactly (9). The continuous energy identity (10)
therefore holds for their difference densities $h_{i,\lambda}$.
Equation (14) for $m=2$ supplies the discrete norm limit (11),
now along $N_j$. Weak convergence plus equality of norms gives
strong convergence at $\lambda=1,2$.

The discrete diagonal inequality (7) thus implies
$P h_{i,1}^2\ge h_{i,2}$ almost everywhere. Summing over residues
again yields $h_2\le P h_1^2$, whereas
$$
 \frac{h_1(u)^2}{h_2(u)}\sim\frac{\kappa}{\sqrt{\pi u}}
 \longrightarrow0.
$$
This is the same contradiction as before, and proves (12). $\square$

The remaining gap is unchanged: (12) forces persistent variation, but
does not bound the number of values taken by $r$. A representation
function taking several values between $1$ and a fixed $M$ can
satisfy this necessary condition.
