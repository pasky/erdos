# The normal order of the number of iterations of Euler’s function

Plasma AI

## Abstract

Let $f(n)$ be the smallest nonnegative integer $k$ for which the $k$th iterate of Euler’s totient function at $n$ equals $1$. We prove that there is a constant $\alpha\in[1/\log 3,1/\log 2]$ such that $$\sum_{n\leq x}(f(n)-\alpha\log n)^2\ll\frac{x(\log x)^2}{(\log\log x)^5}.$$ Thus $f(n)/\log n$ converges to $\alpha$ on a set of natural density one, answering the first two questions of Erdős Problem 408. The proof follows the moment method of Erdős, Granville, Pomerance and Spiro, replacing their Elliott–Halberstam-type hypotheses by estimates derived from the recent zero-free half-plane and weighted dilation-graph results.

## Introduction

Let $\varphi$ be Euler’s totient function, set $\varphi_0(n)=n$, and define $\varphi_{k+1}=\varphi\circ\varphi_k$ for $k\geq0$. For $n\geq1$, put $$f(n)=\min\{k:\varphi_k(n)=1\}.$$ Erdős asked whether $f(n)/\log n$ has a limiting distribution and whether it is almost always constant. Both questions appear in Erdős and Subbarao [4, p. 125] (see also Erdős and Graham [2, pp. 80–81], where they are attributed to Erdő). They are cataloged by Bloom [1] as the first two parts of Erdős Problem 408.

**Theorem 1.1**. *There is a constant $\alpha$, with $$\frac1{\log 3}\leq\alpha\leq\frac1{\log 2},$$ such that, for all sufficiently large $x$, $$\begin{equation}
\label{eq:variance}
 \sum_{n\leq x}\bigl(f(n)-\alpha\log n\bigr)^2
 \ll \frac{x(\log x)^2}{(\log\log x)^5}.
\end{equation}$$ Moreover, $$\begin{equation}
\label{eq:exceptional}
 \#\left\{3\leq n\leq x:
  |f(n)-\alpha\log n|>\frac{\log n}{\log\log n}\right\}
 \ll \frac{x}{(\log\log x)^3}+\sqrt{x}.
\end{equation}$$ In particular, $f(n)/\log n\to\alpha$ on a set of natural density one.*

Pillai [8, p. 841] proved that $f(n)$ lies between $(\log n)/\log 3+O(1)$ and $(\log n)/\log 2+O(1)$. Erdős, Granville, Pomerance and Spiro [3, Theorems 2.1–2.2] proved the existence of a normal order $\alpha\log n$ under suitable Elliott–Halberstam-type estimates. Their method replaces $f$ by a completely additive function $F$ with $|f-F|\leq1$. Since $F(p)=F(p-1)$ for odd primes $p$, estimates for prime factors of $p-1$ give relations between the first two moments of $F$ over primes and harmonic sums of its prime values. Solving these relations gives the normal order. We use the same method and obtain their variance bound with error function $(\log\log x)^{-6}$. The value of $\alpha$ remains undetermined.

The estimates for shifted primes come from OpenAI’s zero-free half-plane result for Dirichlet $L$-functions [9, Theorem 1.1] and their work on the Poisson–Dirichlet law and weighted dilation graphs [6, 7]. To our knowledge, this unconditional normal-order result has not previously been recorded. Our contribution is to extend the estimate in [6, Theorem 7.1] in two ways so that the moment method applies. First, the weights $F(q)$ and $F(q)F(r)$ depend on the prime factors themselves, so a result about their normalized logarithms alone does not suffice. Second, the moment relations require a summable error, whereas the cited estimate gives $o(1)$ for a fixed region. Theorem 2.1 allows bounded weights depending jointly on all but one prime factor, with an explicit error as the region approaches the boundary.

The restriction on one prime factor comes from the use of an unweighted prime sum in the analytic argument. To estimate a weighted sum over one or two prime factors of $p-1$, we introduce an additional prime divisor and sum over it. The resulting multiplier lies between zero and one. The rectangle estimate then shows that removing it costs only a small error. Section 3 gives this argument. Sections 4 and 5 deduce the prime moments and the normal order. Section 6 outlines the proof of the rectangle estimate, including the changes to the graph arguments needed for the weights and error term.

The third question in Problem 408 asks what can be said about the largest prime factor of $\varphi_k(n)$ when, for example, $k=\lfloor\log\log n\rfloor$. In connection with this question, we record a consequence of Ford, Konyagin and Luca [5, Theorem 5]: for every integer-valued $k(n)\to\infty$, the largest prime factor of $\varphi_{k(n)}(n)$ is $n^{o(1)}$ on a set of natural density one. Section 7 gives the deduction.

##### Formalization.

Theorem 1.1 has been formalized in Lean 4 using Mathlib; the source code is available in [15]. The development incorporates OpenAI’s formalization of the zero-free half-plane theorem [10], Yao Xu’s formalization of the weighted dilation-graph results [11], and code from *PrimeNumberTheoremAnd* [12] and Adam Benenson’s *rellich-kondrachov* [13]. The statements of the first two questions are adapted from the Formal Conjectures project [14].

## The additive function and the prime-factor estimate

To estimate the moments of $f$, we use the completely additive function $F$ of Erdős, Granville, Pomerance and Spiro [3, p. 166], determined recursively by $$\begin{equation}
\label{eq:F}
 F(2)=1,\qquad F(p)=F(p-1)\quad(p>2\text{ prime}),\qquad F(1)=0.
\end{equation}$$ For $n>1$, this function satisfies $$\begin{equation}
\label{eq:F-f}
 F(n)=\begin{cases}f(n),&n\text{ even},\\ f(n)-1,&n\text{ odd}.
 \end{cases}
\end{equation}$$ Indeed, applying complete additivity to $\varphi(n)=\prod_{p^e\parallel n}p^{e-1}(p-1)$ gives $F(\varphi(n))=F(n)-1$ for even $n$, and $F(\varphi(n))=F(n)$ for odd $n>1$. Equation (eq:F-f) follows by induction on the number of iterations needed to reach $1$.

We also have $$\begin{equation}
\label{eq:F-bounds}
 \frac{\log n}{\log 3}\leq F(n)\leq\frac{\log n}{\log 2}
 \qquad(n\geq1).
\end{equation}$$ To prove these bounds by induction, it suffices to consider primes. The case $p=2$ follows from $F(2)=1$. For odd $p$, the upper bound follows from $F(p)=F(p-1)$ and the inductive hypothesis. For the lower bound, write $p-1=2m$ and use $F(p)=1+F(m)\geq\log(3m)/\log 3\geq\log p/\log 3$. Both bounds then extend to composites by additivity. In particular, $0\leq F(n)\leq2\log n$, and $|f(n)-F(n)|\leq1$ for all $n\geq1$.

For the rest of the argument write $$L=\log x,\qquad T=\log L,\qquad
 \Pi_x=\pi(2x)-\pi(x),\qquad
 \mathbb E_x H(p)=\frac1{\Pi_x}\sum_{x<p\leq2x}H(p).$$ Letters $p,q,r$ in sums denote primes. All asymptotic assertions are for sufficiently large $x$. The following estimate compares divisibility by a tuple of prime factors with the harmonic weight given by the reciprocal of their product.

**Theorem 2.1** (Quantitative rectangle estimate). *There are constants $c,C>0$ such that the following holds. Let $1\leq k\leq3$, and let $I_i=(x^{u_i},x^{v_i}]$ be prime intervals satisfying $$u_i\geq cT^{-20},\qquad \sum_{i=1}^k v_i\leq1-cT^{-20}.$$ For any real coefficient $b(q_1,\ldots,q_{k-1})$ of absolute value at most $1$, $$\begin{equation}
\label{eq:R}
 \left|\mathbb E_x\sum_{\substack{q_i\in I_i\ \mathrm{distinct}\\
                         q_1\cdots q_k\mid p-1}}
 b(q_1,\ldots,q_{k-1})
 -\sum_{\substack{q_i\in I_i\ \mathrm{distinct}}}
 \frac{b(q_1,\ldots,q_{k-1})}{q_1\cdots q_k}\right|
 \leq CT^{-300}.
\end{equation}$$ The constants and the threshold for $x$ are uniform in the intervals and in $b$. The coefficient may depend on $x$, but not on $p$ or $q_k$. For $k=1$ it is a constant.*

We outline the proof in Section 6. The deduction of Theorem 1.1 from this estimate uses Mertens’ theorems and elementary estimates. The coefficient $b$ must be independent of $q_k$, because the analytic proof uses an unweighted sum over that prime. We next sum over an auxiliary prime $q_k$ to obtain estimates with arbitrary bounded weights on one or two prime factors.

## Summing over an auxiliary prime factor

We restrict the prime factors to intervals on a logarithmic grid. The parameter $a$ measures the part of the boundary we omit, $m$ is the mesh size, and $\delta$ is the margin required by Theorem 2.1. Set $$a=T^{-6},\qquad m=\frac1{\lceil T^{20}\rceil},\qquad
 \delta=cT^{-20},\qquad
 J_j=(x^{a+jm},x^{a+(j+1)m}].$$ Let $\mathcal R_1$ be a set of primes and $\mathcal R_2$ a set of ordered pairs of distinct primes, defined by $$\begin{align*}
 \mathcal R_1&=\bigcup_{0\leq j<N_1}J_j,
 &N_1&=\left\lfloor\frac{1-2a}{m}\right\rfloor,\\
 \mathcal R_2&=\bigcup_{i+j+2\leq N_2}
       \{(q,r)\in J_i\times J_j:q\ne r\},
 &N_2&=\left\lfloor\frac{1-3a}{m}\right\rfloor.
\end{align*}$$ The indices in the second union are nonnegative. Every prime in these tuples exceeds $x^a$, and each tuple has product at most $x^{1-a}$. The regions are unions of rectangles to which Theorem 2.1 applies. In Section 4 we bound the contribution of the omitted prime factors.

For $\mathbf q\in\mathcal R_d$, with $d=1,2$, put $Q=\prod_{i=1}^d q_i$. Let $s$ be the sum of the upper logarithmic endpoints of the grid intervals containing its coordinates. Then $$s-dm\leq\frac{\log Q}{L}\leq s\leq1-a,
 \qquad d\in\{1,2\}.$$ We sum the auxiliary prime over the intervals $$S_j=(x^{\delta+jm},x^{\delta+(j+1)m}],\qquad
 0\leq j<J(s),\qquad
 J(s)=\left\lfloor\frac{1-2\delta-s}{m}\right\rfloor.$$ These choices leave the margin required by Theorem 2.1. We weight a prime in $S_j$ by the lower endpoint of its logarithmic interval, divided by $\log(2x/Q)$. Thus the weight is independent of that prime within $S_j$. Define $$\begin{align}
 w_j(Q)&=\frac{(\delta+jm)L}{\log(2x/Q)},\label{eq:w}\\
 Z_{\mathbf q}(n)&=\sum_{j<J(s)}w_j(Q)
      \sum_{\substack{r\in S_j\\r\mid n,\ r\notin\{q_1,\ldots,q_d\}}}1,
      \label{eq:Z}\\
 A(\mathbf q)&=\sum_{j<J(s)}w_j(Q)
      \sum_{\substack{r\in S_j\\r\notin\{q_1,\ldots,q_d\}}}\frac1r.
      \label{eq:Zmodel}
\end{align}$$ The sum $A(\mathbf q)$ is the harmonic analogue of $Z_{\mathbf q}(n)$. The denominator $\log(2x/Q)$ makes $Z_{\mathbf q}(n)\leq1$ when $Q\mid n$ and $n<2x$, while keeping the weight independent of $n$.

**Lemma 3.1**. *If $Q\mid n$ and $n<2x$, then $0\leq Z_{\mathbf q}(n)\leq1$. For $d=1,2$, uniformly over $\mathbf q\in\mathcal R_d$, $|1-A(\mathbf q)|\ll T^{-10}$.*

*Proof.* Each auxiliary prime counted in (eq:Z) divides $n/Q$, and the intervals $S_j$ are disjoint. Also $(\delta+jm)L\leq\log r$ for $r\in S_j$. Consequently, $$\sum_{j<J(s)}(\delta+jm)L
   \sum_{\substack{r\in S_j\\r\mid n,\ r\notin\{q_i\}}}1
 \leq\sum_{r\mid n/Q}\log r
 \leq\log(n/Q)\leq\log(2x/Q).$$ This proves $Z_{\mathbf q}(n)\leq1$.

Put $v=\delta+jm$. Mertens’ first theorem gives $$v\sum_{r\in S_j}\frac1r
 =m+O\left(\frac1L+m\sum_{r\in S_j}\frac1r\right).$$ Sum this over $j<J(s)$ and use Mertens’ second theorem to bound the harmonic mass of the union by $O(\log(1/\delta)+1/(\delta L))$. There are $O(1/m)$ cells. Excluding the at most two primes in $\mathbf q$ costs at most $O(1/(mx^a))$. Since $J(s)m=1-2\delta-s+O(m)$ and $s-\log Q/L=O(m)$, division by $1-\log Q/L+\log2/L\geq a$ gives $$\begin{equation}
\label{eq:defect-bound}
 |1-A(\mathbf q)|\ll
 \frac{\delta+m+L^{-1}+(mL)^{-1}
       +m\log(1/\delta)+m/(\delta L)+(mx^a)^{-1}}a.
\end{equation}$$ With the chosen values of $a,m,\delta$, the right-hand side is $O(T^{-14}\log T)$, and hence $O(T^{-10})$. ◻

**Proposition 3.2**. *For $d=1,2$ and every real coefficient $b$ on $\mathcal R_d$ with $|b|\leq1$, $$\begin{equation}
\label{eq:weighted}
 \mathbb E_x\sum_{\substack{\mathbf q\in\mathcal R_d\\Q\mid p-1}}b(\mathbf q)
 =\sum_{\mathbf q\in\mathcal R_d}\frac{b(\mathbf q)}Q+O(T^{-7}),
\end{equation}$$ uniformly in $b$.*

*Proof.* For $\mathbf q\in\mathcal R_d$, define $$\mu(\mathbf q)=\mathbb E_x\mathbf 1_{Q\mid p-1},\qquad
 \mu_Z(\mathbf q)=\mathbb E_x\bigl(\mathbf 1_{Q\mid p-1}Z_{\mathbf q}(p-1)\bigr),\qquad
 \nu(\mathbf q)=\frac1Q.$$ We write $\mu(b)=\sum_{\mathbf q\in\mathcal R_d}b(\mathbf q)\mu(\mathbf q)$, and similarly for $\mu_Z$ and $\nu$. The coefficient $b(\mathbf q)w_j(Q)$ is independent of the auxiliary prime and has absolute value at most one. Summing (eq:R) over the grid rectangles gives $$|\mu_Z(b)-\nu(bA)|\ll T^{60}T^{-300}.$$ Applying (eq:R) to the $d$ original factors with coefficient $1$ gives $|\mu(1)-\nu(1)|\ll T^{40}T^{-300}$. By Lemma 3.1, the measure $\mu-\mu_Z$ is nonnegative. Thus, for $|b|\leq1$, $$\begin{align*}
 |\mu(b)-\nu(b)|
 &\leq (\mu-\mu_Z)(1)+|\mu_Z(b)-\nu(bA)|
          +\nu(|1-A|)\\
 &\leq 2\nu(|1-A|)+O(T^{-240}).
\end{align*}$$ Mertens’ second theorem gives $\nu(1)\ll(1+\log(1/a))^d\ll T^2$. The defect bound therefore gives $O(T^{-8})$, and in particular the claimed $O(T^{-7})$. ◻

## First and second moments over primes

Complete additivity expresses $F(p-1)$ and $F(p-1)^2$ as sums over one or two prime factors. Proposition 3.2 therefore leads to the following harmonic sums. Write $a_q=F(q)$ and define $$\begin{align*}
 B(x)&=\sum_{q\leq x}\frac{a_q}{q},&
 C(x)&=\sum_{q\leq x}\frac{a_q^2}{q},\\
 D(x)&=\sum_{\substack{q\ne r\\qr\leq x}}\frac{a_qa_r}{qr},&
 A_i(x)&=\sum_{p\leq x}F(p)^i\quad(i=1,2).
\end{align*}$$ Pairs in $D$ are ordered. Thus $D$ is twice the sum over $q<r$ used in parts of [3, Section 2].

To bound the terms outside $\mathcal R_1$ and $\mathcal R_2$, we compare them with the corresponding logarithmic weights. The latter have almost their full mass inside these regions. Since all omitted terms are nonnegative and $a_q\leq2\log q$, the same comparison controls the omitted terms involving $a_q$.

Put $t_q=\log q/L$. Mertens’ first theorem, applied on the cells, gives $$\begin{align}
 \sum_{q\in\mathcal R_1}\frac{t_q}{q}&=1+O(a),\label{eq:logfirst}\\
 \sum_{q\in\mathcal R_1}\frac{t_q^2}{q}
   +\sum_{(q,r)\in\mathcal R_2}\frac{t_qt_r}{qr}&\geq1-O(a).
   \label{eq:logsecond}
\end{align}$$ The two sums in (eq:logsecond) are each $1/2+O(a)$. The first is a Riemann sum for $\int_a^{1-a}t\,\mathrm dt$, while the pair sum is a Riemann sum for the area of $\{(u,v):u,v\geq a,\ u+v\leq1-a\}$. The cell estimates have errors $O(1/L)$; there are $O(m^{-2})$ cells, and their total error is $o(a)$. The repeated-prime diagonal costs $o(a)$ as well, since $q>x^a$. The union of grid rectangles differs from this triangle by strips of width $O(m)$.

Put $\ell=\log(2x)$. For $n=p-1<2x$, let $$\begin{align*}
 U(n)&=\sum_{\substack{q\in\mathcal R_1\\q\mid n}}\log q,\\
 V(n)&=\sum_{\substack{q\in\mathcal R_1\\q\mid n}}(\log q)^2
    +\sum_{\substack{(q,r)\in\mathcal R_2\\qr\mid n}}\log q\log r.
\end{align*}$$ Both sums are nonnegative, with $U(n)\leq\log n\leq\ell$ and $V(n)\leq(\log n)^2\leq\ell^2$. Applying Proposition 3.2 with the bounded coefficients $t_q,t_q^2,t_qt_r$, and then (eq:logfirst)–(eq:logsecond), yields $$\begin{equation}
\label{eq:logdefects}
 \mathbb E_x(\ell-U(p-1))\ll La,\qquad
 \mathbb E_x(\ell^2-V(p-1))\ll L^2a.
\end{equation}$$

Complete additivity and $a_q\leq2\log q$ imply $$\begin{align}
 0\leq F(n)-\sum_{\substack{q\in\mathcal R_1\\q\mid n}}a_q
       &\leq2(\ell-U(n)),\label{eq:Fdefect}\\
 0\leq F(n)^2-
 \left(\sum_{\substack{q\in\mathcal R_1\\q\mid n}}a_q^2+
       \sum_{\substack{(q,r)\in\mathcal R_2\\qr\mid n}}a_qa_r\right)
       &\leq4(\ell^2-V(n)).\label{eq:Fsqdefect}
\end{align}$$ Indeed, expand $F(n)$ and $\log n$ over prime factors with multiplicity. The truncated sums select the same occurrences and ordered pairs from the two expansions. Every omitted term is nonnegative and is bounded by two, or respectively four, times its logarithmic counterpart. This also accounts for all prime powers.

**Proposition 4.1**. *The rectangle estimate implies $$\begin{align}
 \mathbb E_x F(p)&=B(x)+O(LT^{-6}),\label{eq:M1}\\
 \mathbb E_x F(p)^2&=C(x)+D(x)+O(L^2T^{-6}).\label{eq:M2}
\end{align}$$ Consequently, $$\begin{align}
 A_1(x)&=\pi(x)B(x)+O(xT^{-6}),\label{eq:cum1}\\
 A_2(x)&=\pi(x)(C(x)+D(x))+O(xLT^{-6}).\label{eq:cum2}
\end{align}$$*

*Proof.* For $p>2$, (eq:F) gives $F(p)=F(p-1)$. Average (eq:Fdefect)–(eq:Fsqdefect), use (eq:logdefects), and apply Proposition 3.2 to $a_q/(2L)$, $a_q^2/(4L^2)$ and $a_qa_r/(4L^2)$. This proves the desired formulas with the harmonic sums restricted to $\mathcal R_1$ and $\mathcal R_2$.

It remains to extend the harmonic sums from $\mathcal R_1$ and $\mathcal R_2$ to the full ranges defining $B,C,D$. For example, $$\sum_{q\leq x^a}\frac{a_q}{q}\ll aL+1,\qquad
 \sum_{x^{1-a-O(m)}<q\leq x}\frac{a_q}{q}\ll(a+m)L+1.$$ Multiplying by $O(L)$ bounds the corresponding tails for $C$. For $D$, use $a_qa_r\leq4\log q\log r$. The weighted harmonic measure $(\log q/L)/q$ has cumulative mass $t+O(1/L)$ up to $x^t$. The excluded pairs either have a coordinate at most $a$, or lie in a strip of width $a+O(m)$ along $u+v=1$. Summing Mertens’ first theorem in one coordinate and then the other bounds these contributions by $O(aL^2+L)$. This proves (eq:M1)–(eq:M2).

To pass to cumulative sums, decompose the primes up to $x$ into dyads $(y,2y]$. Mertens’ first theorem and (eq:F-bounds) give $$B(x)-B(y)\ll1+\log(x/y),$$ and $$C(x)-C(y)+D(x)-D(y)
 \ll L(1+\log(x/y)).$$ For the pair sum, obtain the latter inequality by summing the one-variable Mertens bound over $q$. Chebyshev’s estimate $\Pi_y\ll y/\log y$ and the convergence of $\sum_{j\geq0}(j+1)2^{-j}$ show that replacing the dyadic main terms by their values at $x$ costs $O(x/L)$ and $O(x)$. The dyadic error terms above $\sqrt{x}$ sum to $O(xT^{-6})$ and $O(xLT^{-6})$; the smaller primes contribute less by the elementary bound $F(p)\ll L$. This proves (eq:cum1)–(eq:cum2). ◻

## From prime moments to normal order

The first prime moment gives a recurrence for $B(2^k)$. After dividing by its multiplicative growth factor, we obtain a convergent series; its limit determines $\alpha$. The second moment gives a recurrence for $C(2^k)$, while $D$ is a convolution of $B$. This is a discrete form of the argument in [3, Section 2].

Fix a sufficiently large integer $k_0$. For integers $k\geq1$ and $K\geq k_0$, put $$h_k=\sum_{2^k<p\leq2^{k+1}}\frac1p,\qquad
 P_K=\prod_{k_0\leq j<K}(1+h_j).$$ Mertens’ second theorem gives $$\begin{equation}
\label{eq:h}
 h_k\ll k^{-1},\qquad
 \sum_{K\leq j<M}h_j=\log(M/K)+O(K^{-1}).
\end{equation}$$ It follows, by expanding $\log(1+h_j)$ and summing $h_j^2$, that $$\begin{equation}
\label{eq:P}
 P_K=\kappa K+O(1)\quad(\kappa>0),\qquad
 \sum_{k_0\leq k<K}kh_k=K+O(\log K).
\end{equation}$$ The second formula follows by partial summation from $\sum_{j<K}h_j=\log K+\text{constant}+O(1/K)$.

**Lemma 5.1**. *There is a real $\alpha$ in $[1/\log3,1/\log2]$ such that $$\begin{equation}
\label{eq:B}
 B(x)=\alpha\log x+O\bigl(LT^{-5}\bigr).
\end{equation}$$*

*Proof.* Set $B_k=B(2^k)$. For $y=2^k$ and $y\leq t\leq2y$, (eq:cum1) and $B(t)-B(y)=O(1)$ show that the partial sums of $F(p)-B(y)$ over $(y,t]$ are $O(y(\log k)^{-6}+y/k)$. Partial summation with weight $1/p$ therefore gives $$\begin{equation}
\label{eq:renewB}
 B_{k+1}=(1+h_k)B_k+e_k,\qquad
 e_k=O\bigl((\log k)^{-6}+k^{-1}\bigr).
\end{equation}$$ Divide by $P_{k+1}$ and telescope. The series $\sum e_k/P_{k+1}$ converges, since its terms are $O(1/(k\log^6 k)+1/k^2)$; its tail is $O((\log K)^{-5})$. Together with (eq:P), this proves $B(2^K)=\alpha K\log2+O(K/\log^5 K)$ for some $\alpha$. The variation of $B$ on one dyad is $O(1)$, so (eq:B) holds for real $x$ as well. Finally, (eq:F-bounds) and $\sum_{q\leq x}(\log q)/q=\log x+O(1)$ give the bounds on $\alpha$. ◻

The error rate in (eq:renewB) ensures that $\sum e_k/P_{k+1}$ converges. An estimate $e_k=o(1)$ alone would not suffice.

**Lemma 5.2**. *For the constant in Lemma 5.1, $$\begin{equation}
\label{eq:CD}
 C(x)=\frac{\alpha^2}2 L^2+O(L^2T^{-5}),\qquad
 D(x)=\frac{\alpha^2}2 L^2+O(L^2T^{-5}).
\end{equation}$$*

*Proof.* First consider $D$. Put $\mathcal B(u)=B(e^u)$, extended by zero for $u<\log2$. The diagonal sum $\sum_q a_q^2/q^2$ converges, so $$D(e^y)=\int_{[0,y]}\mathcal B(y-u)\,\mathrm d\mathcal B(u)+O(1).$$ Write $\mathcal B(u)=\alpha u+E(u)$. Lemma 5.1 and the bound $\mathcal B(u)\ll u+1$ imply, uniformly for $0\leq u\leq y$, $$|E(u)|\ll\sqrt y+\frac{u}{(\log y)^5}.$$ Use this estimate first in the integrand, and then in $$\int_{[0,y]}(y-u)\,\mathrm d\mathcal B(u)=\int_0^y\mathcal B(u)\,\mathrm du.$$ The measure $\,\mathrm d\mathcal B$ is positive and has total mass $O(y)$. The resulting error is $O(y^{3/2}+y^2/\log^5y)$, proving the formula for $D$.

For $C$, put $C_k=C(2^k)$, $D_k=D(2^k)$ and $b=\alpha^2(\log2)^2/2$. On the dyad $(2^k,2^{k+1}]$, $C$ varies by $O(k)$; the asymptotic just proved shows that $D$ varies by $O(k+k^2/\log^5 k)$. Apply partial summation to (eq:cum2), as in the proof of (eq:renewB). It gives $$C_{k+1}=(1+h_k)C_k+D_kh_k+e'_k,
 \qquad e'_k=O(k/\log^5 k).$$ Since $D_k=bk^2+O(k^2/\log^5k)$ and $P_{k+1}=\kappa(k+1)+O(1)$, $$\frac{D_kh_k+e'_k}{P_{k+1}}
 =\frac b\kappa kh_k+O\bigl((\log k)^{-5}+h_k\bigr).$$ After telescoping, (eq:P) yields $C_K/P_K=(b/\kappa)K+O(K/\log^5 K)$. Thus $C_K=bK^2+O(K^2/\log^5K)$. Monotonicity and the $O(K)$ variation of $C$ on a dyad extend the result to real $x$. ◻

**Lemma 5.3** (Integer moments). *For $x\geq2$, $$\begin{align}
 \frac1x\sum_{n\leq x}F(n)&=B(x)+O(1),\label{eq:int1}\\
 \frac1x\sum_{n\leq x}F(n)^2&=C(x)+D(x)+O(L).\label{eq:int2}
\end{align}$$*

*Proof.* These identities are [3, (2.8), (2.19)]. To track the error terms, replace $F(n)$ by $F^*(n)=\sum_{q\mid n}a_q$. The average difference is bounded by $$\sum_q\sum_{e\geq2}\frac{a_q}{q^e}
 =\sum_q\frac{a_q}{q(q-1)}\ll1.$$ Since $F(n)+F^*(n)\ll L$ for $n\leq x$, this replacement costs $O(L)$ in the second moment. Expand the first and second powers of $F^*$ and count multiples. Replacing $\lfloor x/q\rfloor$ by $x/q$ costs $O(\sum_{q\leq x}\log q/x)=O(1)$ in the first moment. The diagonal error in the second moment is $O(L)$. For its off-diagonal error, Chebyshev’s bound gives $$\sum_{qr\leq x}\log q\log r
 \ll x\sum_{q\leq x}\frac{\log q}{q}\ll xL.$$ These estimates prove both identities. ◻

*Proof of Theorem 1.1 from Theorem 2.1.* Lemmas 5.1–5.3 give $$\frac1x\sum_{n\leq x}F(n)=\alpha L+O(LT^{-5}),\qquad
 \frac1x\sum_{n\leq x}F(n)^2=\alpha^2L^2+O(L^2T^{-5}).$$ Expanding the square shows that $\sum_{n\leq x}(F(n)-\alpha L)^2\ll xL^2T^{-5}$. Also $$\sum_{n\leq x}(\log x-\log n)^2
 \leq\int_0^x(\log x-\log t)^2\,\mathrm dt=2x.$$ The inequality $(u+v)^2\leq2u^2+2v^2$ and $|f(n)-F(n)|\leq1$ now prove (eq:variance).

For $\sqrt{x}<n\leq x$, the threshold $\log n/\log\log n$ is at least $L/(2T)$ for large $x$. Chebyshev’s inequality applied to (eq:variance) bounds the number of exceptions in this range by $O(xT^{-3})$. Adding at most $\sqrt{x}$ smaller integers proves (eq:exceptional). On the complement of these exceptions, $|f(n)/\log n-\alpha|\leq1/\log\log n\to0$. ◻

**Corollary 5.4**. *The limiting distribution function of $f(n)/\log n$ is $$H(t)=\begin{cases}0,&t<\alpha,\\1,&t\geq\alpha.
 \end{cases}$$ More precisely, at every continuity point $t$ of $H$, $x^{-1}\#\{2\leq n\leq x:f(n)/\log n\leq t\}\to H(t)$.*

*Proof.* For $t<\alpha$, convergence to $\alpha$ on a set of density one shows that the displayed set has density zero. For $t>\alpha$, its complement has density zero. ◻

## Proof outline for the rectangle estimate

We outline the adaptation of [6, Sections 3–7] needed for Theorem 2.1. The graph constructions and divisor weights are those of the cited sections. The changes concern the coefficient $b$, the shrinking margin $cT^{-20}$, and the error $O(T^{-300})$. We first describe where these changes enter the graph estimates, then give the analytic bounds and the weights used in the sieve argument.

### The two graph estimates

For the intervals and coefficient in Theorem 2.1, put $$f_b(w)=\sum_{\substack{q_i\in I_i\ \mathrm{distinct}\\
                       \prod q_i\mid w}}b(q_1,\ldots,q_{k-1}),
 \qquad
 C_b=\sum_{\substack{q_i\in I_i\ \mathrm{distinct}}}
          \frac{b(q_1,\ldots,q_{k-1})}{\prod q_i}.$$ The aim is to bound the mean of $f_b(p-1)-C_b$. The proof in [6, Section 7] first replaces primality by a sieve condition. It then uses a one-sided graph estimate to replace prime factors of the resulting composite integers by weights on rough numbers. A two-sided graph estimate bounds the correlation of these weights with $f_b-C_b$.

Both estimates use auxiliary bands of small primes and divisor weights attached to those bands. We use the marking weights of [6, (3.4), Section 6]. A function is invariant under a band if multiplying its argument by a prime in that band leaves its value unchanged. This invariance allows the graph argument to insert and remove auxiliary prime divisors.

The one-sided estimate extends [6, Theorem 3.1]. It bounds a bilinear sum against a marked invariant function of $mn-1$. The proof allows one coefficient to be any sequence supported on rough numbers whose character twists satisfy the bound used in [6, Lemma 5.2]. We need this estimate on dyadic scales $H_mH_n\asymp x$ with $H_m,H_n\geq x^\gamma$ and $\gamma\geq L^{-1/100}$. For any prescribed power saving $L^{-A}$, the number of separated marking bands is fixed sufficiently large in terms of $A$ and the coefficient bounds.

The two-sided estimate extends [6, Theorem 6.1]. One endpoint carries $f_b-C_b$, and the other carries a nonnegative invariant function bounded by $L^{B_0}$ for a fixed $B_0$. Both carry the divisor weights of the graph theorem. We need uniformity for margins $cT^{-20}$, for $O(\log T)$ inert bands, and for smooth cutoffs whose derivatives of each fixed order are bounded by fixed powers of $T$. The graph comparison uses [7, Lemma 3.4, Theorem 3.5, Corollary 3.11, Theorem 4.1, Lemma 4.3], as in [6, Propositions 6.2–6.3].

The condition that $b$ is independent of $q_k$ enters the high-frequency estimate [6, (6.31)–(6.38)]. After removing repeated-prime terms, we place $b$ in the polynomial formed from the other factors and reserve $q_k$ for the unweighted prime sum. Removing repetitions first is necessary: a condition $q_i\ne q_k$ inside the residual coefficient would make it depend on $q_k$. At low frequencies, the divisor calculation in [6, Lemma 6.5] is linear in the coefficient and centers $f_b$ at $C_b$.

### Analytic estimates at the required scales

OpenAI’s zero-free half-plane theorem [9, Theorem 1.1] gives $$\begin{equation}
\label{eq:Q}
 L(z,\chi)\ne0\quad(\Re z>\beta)
\end{equation}$$ for every Dirichlet character $\chi$, away from the principal pole, with $\beta=7/8$. The argument below only requires a fixed $\beta<1$.

Two consequences of (eq:Q) replace the fixed-scale analytic estimates in [6]. Given fixed $A,C>0$, one can choose a fixed $E$ such that $$\begin{equation}
\label{eq:prime-twist}
 \left|\sum_{p\in I}\chi(p)p^{-1+iu}\right|\ll L^{-A}
 \quad\left(L^E\leq|u|\leq x^3,\quad
     I\subset[H,2H],\quad \exp(L/T^{22})\leq H\leq x,\quad q\leq L^C\right),
\end{equation}$$ where $q$ is the modulus of $\chi$. On the same scale range, the integer sums satisfy $$\begin{equation}
\label{eq:kernel}
 \frac1H\left|\sum_{\substack{n\in I\\n\equiv b\pmod q}}n^{iu}\right|
 \ll\frac1{1+|u|}+\exp(-L^{0.95})
 \quad(1\leq|u|\leq x^3).
\end{equation}$$ The constant term in the two-sided estimate requires the progression bound also at slightly larger scales.

For the prime sum, one shifts the contour for $-L'/L$ a fixed distance into the zero-free half-plane. For the integer sum, Borel–Carathéodory and the three-circles theorem, applied to an analytic logarithm, give a bound $\exp(O(\sqrt L))$ for the $L$-function on the shifted line. The factor $H^{-d}$ from a fixed shift $d>0$ dominates this growth on the stated scales. At small frequencies, elementary summation gives a principal integral of size $O(H/(1+|u|))$. This accounts for the first term of (eq:kernel). In the sparse mean-square estimate of [6, Section 6], this term has harmonic row sums $O(L)$, while the exponential remainder absorbs the $\exp(O(L^{0.91}))$ exceptional frequencies.

### Weights on rough numbers

The sieve argument produces products of $j$ prime factors, with $j$ growing slowly with $x$. The replacement weights must allow this growth while keeping the moment exponents in the graph estimates fixed. Put $s=\log T$ and choose $$h=C_hs,\qquad J=\lceil C_js\rceil,\qquad
 \gamma\asymp T^{-20}/s,\qquad z=x^\gamma,\qquad
 Y=\exp(L/T^{25}).$$ Round the sieve depth $h$ to an even integer. All constants are fixed before $x$ tends to infinity.

Use the candidate prime bands of [6, Section 7]: these are intervals $[\exp(y),\exp(2y)]$ with $y$ successively doubled in the ranges $[L^{0.28},L^{0.35}]$ and $[L^{0.40},L^{0.45}]$. Let $\mathcal P$ be their union. For a fixed $c_{\mathcal P}>0$, $$\sum_{p\in\mathcal P}\frac1p=c_{\mathcal P}T+O(1).$$ For sufficiently large $x$, every prime in $\mathcal P$ lies between $W=\exp(L^{0.24})$ and $Y$.

For $2\leq j\leq J$, set $t=1/j$. Let $\bar n$ be obtained from $n$ by removing all prime powers with prime in $\mathcal P$, and let $\Omega_{\mathcal P}(n)$ count those prime factors with multiplicity. Write $P^-(n)$ for the least prime factor of $n$, with $P^-(1)=\infty$. Define $$\begin{align}
 g_j(n)&=\mathbf 1_{P^-(\bar n)>Y}\,t^{\Omega_{\mathcal P}(n)},\nonumber\\
 d_j&=\prod_{p\leq Y}(1-1/p)
       \prod_{p\in\mathcal P}(1-t/p)^{-1},\label{eq:proxy}\\
 a_j^0(n)&=\mathbf 1_{n>x^\gamma}\frac{g_j(n)}{d_j\log n},\qquad
 a_j(n)=\mathbf 1_{\bar n>x^\gamma}\frac{g_j(n)}{d_j\log\bar n}.
 \nonumber
\end{align}$$ Each quotient is defined to be zero when its indicated support condition fails.

The factor $d_j$ normalizes the multiplicative weight $g_j$. At a prime in $\mathcal P$, its local mean is $(1-1/p)\sum_{e\geq0}t^ep^{-e}=(1-1/p)/(1-t/p)$. Mertens’ theorem gives, uniformly in $j$, $$d_j=\frac{T^{25}}L L^{c_{\mathcal P}/j}\exp(O(1)).$$ Consequently $0\leq a_j^0(n)\ll1/(\gamma T^{25})=o(1)$. The weight vanishes unless every prime factor of $n$ exceeds $W$.

The Dirichlet series of $g_j$ twisted by a character $\chi$ is $$L(z,\chi)\prod_{p\leq Y}(1-\chi(p)p^{-z})
       \prod_{p\in\mathcal P}(1-t\chi(p)p^{-z})^{-1}.$$ A contour shift by $1/\log Y$ gives a saving $\exp(-c'\gamma T^{25})$, for a fixed $c'>0$. Since $\gamma T^{25}\gg T$, this is smaller than any prescribed fixed negative power of $L$. At low frequencies, the normalization $d_j$ makes the principal main term agree with that of the prime indicator. Thus the difference between the prime indicator and $a_j^0$ satisfies the character-twist bound required by the one-sided estimate.

Replace the prime factors one at a time. At each step, combine all factors other than the one being replaced into a single convolution coefficient. Dividing just these two variables into dyadic intervals costs $O(L^2)$ intervals, independently of $j$. The convolution coefficient has second moment $HL^{-1+o(1)}$ on an interval of size $H$, uniformly for $j\leq J$. It can therefore be truncated at a fixed power of $L$. This step uses $a_j^0$; the replacement of $a_j^0$ by $a_j$ is made afterward. Removing the factors from $\mathcal P$ can reduce the remaining variable below $x^\gamma$, so the rough-number estimates are also used with exponent $\gamma/2$.

The choice $t=1/j$ compensates for the number of ways to distribute a prime in $\mathcal P$ among the $j$ factors. After excluding multiples of squares of primes in $\mathcal P$, there are $j$ such choices, each of weight $t$. Their total weight is one. Summing over these choices leaves the function $$G_j(v)=\sum_{e_1\cdots e_j=\bar v}
       \prod_{i=1}^j
       \frac{\mathbf 1_{P^-(e_i)>Y}\mathbf 1_{e_i>x^\gamma}}{d_j\log e_i},$$ where each factor is zero off its indicated support. This function depends only on $\bar v$, so it is invariant under multiplication by primes in $\mathcal P$. For every fixed integer $r\geq2$, its moments satisfy $$\begin{equation}
\label{eq:core-moment}
 \sum_{v\leq X}G_j(v)^r
 \leq X L^{-1-(r-1)c_{\mathcal P}+o(1)}
\end{equation}$$ in the ranges used by the graph estimates. The inequality $$G_j\mathbf 1_{G_j>L^{B_0}}\leq L^{-(r-1)B_0}G_j^r$$ then bounds the error from replacing $G_j$ by $\min(G_j,L^{B_0})$. We choose $B_0$ before fixing the graph parameters, so the graph estimate is applied to a function with a fixed pointwise bound.

### The sieve and the auxiliary bands

The prime factors in $\mathcal P$ also provide the active groups required in [6, Section 6]. In the local probability model for one factor, the residue law at $p\in\mathcal P$ is $$\mu_p(0)=\frac{t}{p-1+t},\qquad
 \mu_p(b)=\frac1{p-1+t}\quad(b\not\equiv0\pmod p).$$ For a product $v$ of $j$ independently sampled factors, $$\begin{align*}
 \Pr(p\mid v)&=1-(1-\mu_p(0))^j=\frac1p+O(p^{-2}),\\
 \Pr(p\mid v-1)&=\frac{(1-\mu_p(0))^j}{p-1}
                           =\frac1p+O(p^{-2}),
\end{align*}$$ uniformly in $j$. Thus each candidate band has a probability bounded away from zero of providing the divisors needed for an active group. The corresponding joint estimates over all candidate bands follow by the Chinese remainder theorem and give, by a Chernoff bound, a failure proportion bounded by a fixed negative power of $L$.

The inert bands used for the one-sided estimate have the form $[\exp(L^{a_i}),\exp(2L^{a_i})]$, with the $a_i$ in a fixed compact subinterval of $(0.1,0.2)$. Place $N=C_Ns$ such bands in $K$ separated clusters, with $K$ fixed. Let $v_i\in[0,1]$ be their normalized nonnegative marking weights, and put $$P(n)=\prod_{\mathcal C}
          \left(1-\prod_{i\in\mathcal C}(1-v_i(n))\right),$$ where the product is over the clusters. Then $0\leq P\leq1$. Each monomial in its expansion contains a band from each cluster, providing the $K$ separated marks needed by the one-sided theorem. The sum of the absolute values of the coefficients is at most $2^N=L^{o(1)}$. The mass missed by the marking is $O(K\exp(-c''N/K))$; choose $C_N$ after $K$ to make this smaller than the required power of $T^{-1}$.

Apply the block sieve [7, Lemma 2.9], also stated as [6, Lemma 2.6], to the nonnegative marked statistic before expanding $P$. Take $c_0\asymp T^{-20}$ and $\gamma=c_0/(4h+3)$, so $z^{4h+2}<x^{c_0}$. The divisor expansion and Chinese remainder calculation of [6, Lemma 7.2] give the progression remainder, with uniform bounds for the interval endpoints and coefficients. The relative sieve error is $O(e^{-h}/\gamma)$. Among the integers left by the sieve, those divisible by a square of a prime greater than $z$ contribute $O(x/z)$. The upper sieve and a Rankin bound give a normalized contribution $O(T^{60}\gamma^{-2}2^{-J})$ from integers with more than $J$ prime factors. Enlarging $C_h,C_j$ makes these errors $O(T^{-300})$.

For the remaining composite terms, apply the one-sided estimate to replace prime factors by the weights in (eq:proxy). Summing over the distributions of auxiliary primes and truncating $G_j$ gives the invariant function to which the two-sided estimate applies. Its comparison terms are bounded as in [6, Section 6], using Mellin separation, major and minor arcs, the low-frequency divisor model, and (eq:prime-twist)–(eq:kernel). All graph parameters are fixed. Factors $\exp(O(s^r))$, for fixed $r$, are $L^{o(1)}$ and are absorbed by the power savings. The root and collision counts in the one-sided argument are at most $\exp(O_K(L^{0.98}))$, while $\gamma L\gg L^{0.99}$.

These estimates give the smoothed prime sum with error $O(T^{-300})$. Apply the upper block sieve to remove the marking weight. To pass to $(x,2x]$, choose smooth upper and lower cutoffs with relative transition width $\theta=T^{-400}$. At an integer of size $O(x)$ there are $O(T^{60})$ admissible tuples. The prime number theorem obtained from (eq:Q) bounds the primes in the endpoint intervals by $O(\theta x/L)$ plus a power-saving error. After normalization, the cost is $O(T^{-340})$. The same prime number theorem replaces $x/L$ by $\Pi_x$, giving (eq:R).

## The largest prime factor of an iterated totient

The third question in Problem 408 asks about the largest prime factor after a growing number of iterations. For $m\geq2$, let $P^+(m)$ be its largest prime factor, and put $P^+(1)=1$. Ford, Konyagin and Luca [5, Theorem 5] proved that, for every $\varepsilon,\delta>0$, there is an integer $k$ such that, for all sufficiently large $x$, $$\begin{equation}
\label{eq:FKL}
 \#\{n\leq x:P^+(\varphi_k(n))>x^\varepsilon\}\leq\delta x.
\end{equation}$$

**Proposition 7.1** (Consequence of Ford–Konyagin–Luca). *Let $k(n)$ be integer-valued with $k(n)\to\infty$. Then $$\frac{\log P^+(\varphi_{k(n)}(n))}{\log n}\longrightarrow0$$ in natural density, and hence on some set of natural density one. In particular this holds for $k(n)=\lfloor\log\log n\rfloor$ for sufficiently large $n$.*

*Proof.* Every prime factor of $\varphi(m)$ is at most $P^+(m)$, so the largest prime factor cannot increase along a totient orbit. Fix $\eta,\delta>0$ and apply (eq:FKL) with $\varepsilon=\eta/2$. For sufficiently large $x$, every $\sqrt{x}<n\leq x$ has $k(n)\geq k$. Outside at most $\delta x$ exceptions, $$P^+(\varphi_{k(n)}(n))\leq P^+(\varphi_k(n))
          \leq x^{\eta/2}\leq n^\eta.$$ The smaller integers contribute at most $\sqrt{x}$ exceptions. Since $\delta$ is arbitrary, this proves convergence in density.

To obtain a single density-one set, for each integer $j\geq1$ let $E_j$ be the set where the ratio exceeds $1/j$. Each $E_j$ has density zero. Choose increasing cutoffs $X_j$ such that, for every $x\geq X_j$, $\#((E_1\cup\cdots\cup E_j)\cap[1,x])\leq x/j$. Delete $E_j\cap[X_j,X_{j+1})$ for every $j$. Because $E_i\subseteq E_j$ for $i\leq j$, the deleted set has density zero; on its complement the ratio tends to zero. ◻

## References

**[1]** T. F. Bloom, *Erdős problem \#408*, <https://www.erdosproblems.com/408>.

**[2]** P. Erdős and R. L. Graham, *Old and New Problems and Results in Combinatorial Number Theory*, Monographies de L’Enseignement Mathématique **28**, Université de Genève, Geneva, 1980. <https://mathweb.ucsd.edu/~ronspubs/80_11_number_theory.pdf>.

**[3]** P. Erdős, A. Granville, C. Pomerance, and C. Spiro, *On the normal behavior of the iterates of some arithmetic functions*, in Analytic Number Theory (Allerton Park, IL, 1989), Progress in Mathematics **85**, Birkhäuser, Boston, 1990, pp. 165–204. [doi:10.1007/978-1-4612-3464-7_13](https://doi.org/10.1007/978-1-4612-3464-7_13). Author’s copy: <https://math.dartmouth.edu/~carlp/iterate.pdf>.

**[4]** P. Erdős and M. V. Subbarao, *On the iterates of some arithmetic functions*, in The Theory of Arithmetic Functions (Kalamazoo, MI, 1971), Lecture Notes in Mathematics **251**, Springer, Berlin, 1972, pp. 119–125. [doi:10.1007/BFb0058789](https://doi.org/10.1007/BFb0058789). <https://users.renyi.hu/~p_erdos/1972-17.pdf>.

**[5]** K. Ford, S. V. Konyagin, and F. Luca, *Prime chains and Pratt trees*, Geom. Funct. Anal. **20** (2010), 1231–1258. [doi:10.1007/s00039-010-0089-0](https://doi.org/10.1007/s00039-010-0089-0). Reading version: [arXiv:0904.0473v4](https://arxiv.org/abs/0904.0473v4).

**[6]** OpenAI, *The Poisson–Dirichlet law for prime predecessors*, preprint, September 24, 2026. [Manuscript and source, openai/math](https://github.com/openai/math/blob/main/preprints/The-Poisson-Dirichlet-Law-for-Prime-Predecessors-September-24-2026/paper.pdf).

**[7]** OpenAI, *Weighted dilation graphs, smooth shifted primes and totient fibers*, preprint, September 24, 2026. [Manuscript and source, openai/math](https://github.com/openai/math/blob/main/preprints/Weighted-Dilation-Graphs-Smooth-Shifted-Primes-and-Totient-Fibers-September-24-2026/paper.pdf).

**[8]** S. S. Pillai, *On a function connected with $\varphi(n)$*, Bull. Amer. Math. Soc. **35** (1929), 837–841. [doi:10.1090/S0002-9904-1929-04800-6](https://doi.org/10.1090/S0002-9904-1929-04800-6).

**[9]** OpenAI, *The Quasi-Riemann Hypothesis: A Zero-Free Half-Plane $\operatorname{Re}(s)>7/8$*, preprint, September 30, 2026, Theorem 1.1. [Manuscript and source, openai/math](https://github.com/openai/math/blob/main/preprints/The-Quasi-Riemann-Hypothesis-September-30-2026/paper.pdf).

**[10]** OpenAI, *openai/math*, Lean 4 source library (2026), revisions [`fd4aeeb2ee4f`](https://github.com/openai/math/tree/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/lean) and [`adc7f1241b42`](https://github.com/openai/math/tree/adc7f1241b42e322a6451854ab7e4b4c146bf78a/lean). <https://github.com/openai/math>.

**[11]** Y. Xu, *totient-fibers-lean4*, Lean 4 formalization of weighted dilation graphs and totient fibers (2026), revision [`dfce35707a67`](https://github.com/cadamcat/totient-fibers-lean4/tree/dfce35707a67fce7362cb2bd95af8b80a0b0373e). <https://github.com/cadamcat/totient-fibers-lean4>.

**[12]** A. Kontorovich, T. Tao, and contributors, *PrimeNumberTheoremAnd*, Lean 4 source library (2026), revision [`c39a751132c8`](https://github.com/AlexKontorovich/PrimeNumberTheoremAnd/tree/c39a751132c88b6e8080b74c74023fd95b3d8be0). <https://github.com/AlexKontorovich/PrimeNumberTheoremAnd>.

**[13]** A. Benenson, *rellich-kondrachov*, Lean 4 formalization of the Rellich–Kondrachov theorem (2026), revision [`70f85d4c1bf9`](https://github.com/abenenson/rellich-kondrachov/tree/70f85d4c1bf99c6e7d61e8be4daa6f3664d08d23). <https://github.com/abenenson/rellich-kondrachov>.

**[14]** The Formal Conjectures Authors, *Formal Conjectures: Erdős Problem 408* (2026), revision `7db2ea3b91bf`. [Source statement](https://github.com/google-deepmind/formal-conjectures/blob/7db2ea3b91bfbd0ab620215163e6c488bbb916d5/FormalConjectures/ErdosProblems/408.lean). <https://github.com/google-deepmind/formal-conjectures>.

**[15]** Plasma AI, *Erdős Problem 408: distribution of iterated totient heights*, Lean 4 formalization (2026). <https://github.com/plasma-ai/erdos-408>.
