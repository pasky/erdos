# Prime Predecessors with an Even Number of Prime Factors

OpenAI

## Abstract

We prove that there are infinitely many primes $p$ for which $p-1$ is squarefree and has an even number of prime factors. Equivalently, there are infinitely many primes $p$ with $\mu(p-1)=1$.

## Introduction

Let $\Omega(n)$ be the number of prime factors of $n$, counted with multiplicity, and let $\omega(n)$ count its distinct prime factors. We prove the following affirmative answer to the parity question for predecessors of primes.

**Theorem 1.1**. *There are infinitely many primes $p$ such that $p-1$ is squarefree and $\Omega(p-1)$ is even. In particular, there are infinitely many such primes under either convention for counting prime factors.*

The squarefreeness condition is useful rather than cosmetic: it removes the ambiguity between the two counting conventions. Writing $p=2u+1$, we will construct nonnegative weights on odd integers $u$ for which $\Omega(u)$ is odd. These weights have enough bilinear distribution to detect prime values of $2u+1$, and their nonsquarefree part is negligible at the scale of the detected prime mass.

##### Relation to earlier work.

Prime-factor parity is a classical obstruction in sieve theory: congruence information alone need not distinguish the two Liouville signs. The role of additional bilinear information is illustrated by the asymptotic sieve of Friedlander and Iwaniec [2, Section 1]. Work on smooth shifted primes, including Baker and Harman [1] and Lichtman [3], provides related context for imposing multiplicative restrictions on a prime’s predecessor. The parity condition here is a different restriction; we do not deduce it from smoothness alone.

Our structural inputs are the dilation-graph transference, ideal-kernel, weighted-sieve, and proxy estimates of the companion paper *Weighted dilation graphs, smooth shifted primes and totient fibers* [4], hereafter S. Their hypotheses and the conclusions needed here are stated where they enter the proof. We do not reprove those results.

S’s shifted-correlation argument uses a rough integer in a designated long factor slot and unsigned marked weights. Neither smoothness of the predecessor nor that unsigned statement gives the parity conclusion of Theorem 1.1. The new work is to permit a prime in the long slot and the same group-supported Liouville sign at both endpoints. We prove both extensions here.

##### The two analytic extensions.

First, a logarithmic-phase estimate gives arbitrary fixed logarithmic cancellation in a prime Dirichlet polynomial of positive-power length at all sufficiently large logarithmic heights up to $x^2$. A quantitative power-sum iteration supplies the weak high-height zero-free strip needed for this estimate. The growing degree and all its constants are kept explicit enough for the application.

Second, the sign of a shared dilation occurs twice in a lifted correlation and cancels by complete multiplicativity. This observation allows the graph reduction to retain a parity-sensitive weight. The comparison terms are controlled by local Fourier energy: a small-prime factor restricts difficult frequencies to a sparse set, the new prime estimate treats its large frequencies, and a prescribed character–Mellin discrepancy treats its small frequencies. The resulting correlation estimate implies a Type II theorem for the nonnegative parity-selecting weight.

The common-sign cancellation and the prime-slot estimate are stated separately, so their use is not tied to the final sieve. In the extraction argument, ordinary congruence distribution handles the initial sieve; the stronger Type II statement justifies replacing prime and roughness indicators by bounded local-density proxies. An upper bound for balanced semiprimes then leaves positive prime mass.

##### Organization.

Section 2 fixes conventions and records the classical inputs. Section 3 proves the prime-polynomial estimate, Lemma 3.1, and Section 4 proves the twisted correlation, Theorem 4.1. Section 5 constructs the weights. Their Type II and congruence distribution are Theorems 6.1 and 7.1, proved in Sections 6 and 7. Section 8 extracts the required primes. All auxiliary constants are fixed before $x$ tends to infinity; in particular, the final proxy precision is chosen only after the required discrepancy exponent. We make this order explicit at the steps where it matters.

## Conventions and classical estimates

Throughout the proof, $$x\longrightarrow\infty,\qquad L=\log x,\qquad T=\log L,
 \qquad W=\exp(\sqrt L),\qquad \mathrm{e}(t)=\exp(2\pi i t).$$ A logarithmic power always has a fixed exponent, chosen before $x$ tends to infinity. The implied constants may depend on all previously fixed parameters. No effective threshold for $x$ is asserted. The letters $p$ and $q$ in explicitly indicated prime sums range over primes; general factorization variables are positive integers. We put $P^-(1)=\infty$, where $P^-(n)$ is the least prime factor of $n>1$, and write $\tau(n)$ for its divisor function. The notation $n\asymp Y$ restricts $n$ to a fixed constant enlargement of a dyad $[Y,2Y)$. All such enlargements remain bounded independently of $x$. Dirichlet characters are extended by zero on nonunits.

We use the following classical estimates in the forms recorded in S [4, Section 2]. This explicit list fixes their uniformity; it does not require any distribution theorem beyond the stated ranges.

**Proposition 2.1** (Prime estimates). *The prime number theorem holds with an error smaller than every fixed negative logarithmic power. Mertens’ estimates give $$\sum_{p\le y}\frac1p=\log\log y+O(1),\qquad
 \prod_{p\le y}\left(1-\frac1p\right)
 \sim\frac{e^{-\gamma_E}}{\log y},$$ where $\gamma_E$ is Euler’s constant. For fixed $A,C>0$, uniformly for $r\le(\log y)^C$ and $(a,r)=1$, the Siegel–Walfisz estimate is $$\#\{p\le y:p\equiv a\pmod r\}
 =\frac{\mathop{\mathrm{Li}}(y)}{\varphi(r)}
   +O_{A,C}\left(\frac{y}{(\log y)^A}\right).$$ Its constants need not be effective.*

All short intervals used with the prime number theorem have either a fixed logarithmic-length interpretation in a fixed positive-power band, or relative length a fixed negative power of $L$; the absolute error above is made sufficiently small before taking their differences. We never assume a relative prime asymptotic on every arbitrarily short interval.

**Proposition 2.2** (Large sieve and moment bounds). *For arbitrary coefficients supported on the integers of an interval of length $H$, $$\sum_{r\le R}\frac r{\varphi(r)}
 \sum_{\chi\bmod r}^{*}
 \left|\sum_n a_n\chi(n)\right|^2
 \ll (H+1+R^2)\sum_n|a_n|^2.$$ The asterisk denotes primitive characters. For every fixed integer $k\ge0$ there is $C_k$ such that $$\sum_{n\le Y}\tau(n)^k\ll_k Y(\log(2Y))^{C_k},\qquad
 \sum_{n\le Y}\frac{\tau(n)^k}{n}
 \ll_k(\log(2Y))^{C_k}.$$ If $P(t)=\sum_{n\le Y}c_n n^{it}$, then on any real interval $I$ of length $H$, $$\int_I|P(t)|^2\,dt
 \ll (H+Y\log(2Y))\sum_n|c_n|^2.$$ For a set $\mathcal T\subset I$ with mutual spacing at least one, $$\sum_{t\in\mathcal T}|P(t)|^2
 \ll (H+1+Y\log(2Y))(\log(2Y))^2\sum_n|c_n|^2.$$ The constants in the last two estimates are absolute, independently of how the coefficients were formed.*

These are Theorem 2.3 and Lemmas 2.5–2.6 of S. In particular, the fixed-moment estimate applies to a convolution of a fixed number of logarithmically bounded sequences, giving coefficient-square mass $UL^{O(1)}$ on a dyad of size $U$. With reciprocal-index normalization the bound is $L^{O(1)}/U$. For the one growing power used later, we instead prove a factorial coefficient bound and use the coefficient-independent mean-square inequality.

**Proposition 2.3** (Derivative tests). *Let $f$ be real-valued on an interval containing $H$ consecutive integers. If $f'$ is monotone and remains in $[j+\lambda,j+1-\lambda]$ for an integer $j$ and $0<\lambda\le1/2$, then $$\sum_n\mathrm{e}(f(n))\ll\lambda^{-1}.$$ If instead $f$ is twice continuously differentiable and $\lambda\le|f''|\le C\lambda$ throughout the interval, then $$\sum_n\mathrm{e}(f(n))\ll_C H\sqrt\lambda+\lambda^{-1/2}.$$ Both estimates apply on every subinterval satisfying their hypotheses.*

This is the form of S, Lemma 2.7. The distance from integers in the first test is part of the hypothesis, not merely a lower bound on the absolute derivative.

We will repeatedly separate smooth functions in logarithmic coordinates. The following elementary version of S, Lemma 2.8, explains the order in which frequency cutoffs and accuracies may be chosen.

**Lemma 2.4** (Smooth separation). *Let $F$ be smooth and supported on a fixed bounded box in $\mathbb{R}^b$, with $b$ fixed. Suppose all derivatives of order $j$ are bounded by $C_jL^{C(j+1)}$. Fourier inversion separates its variables with integrated absolute coefficient mass $L^{O(1)}$. There is a fixed exponent $C'>0$, depending on $b,C$, such that truncating each frequency at $L^{C'}$ makes an error $O_A(L^{-A})$ for every fixed $A>0$. The exponent $C'$ is fixed before $A$.*

*Proof.* Integration by parts gives, for each fixed $j$, an integrable tail bounded by a constant times $L^{C(j+1)}(1+|\xi|)^{-j}$. Using a fixed $j>b$ first bounds the full integral by a fixed logarithmic power. Outside $|\xi|\ge L^{C'}$ the same calculation gives $$O_j\bigl(L^{C(j+1)-C'(j-b)}\bigr).$$ Fix $C'>C$ and then increase $j$ for any prescribed $A$. The Fourier phase factors into one-dimensional phases. Applied to normalized logarithmic coordinates, these are multiplicative power twists. ◻

The fixed-dimension condition in Lemma 2.4 will not be used with a growing-dimensional box. In the allocation argument there are $O(T)$ separate one-dimensional transitions, each with a fixed Fourier integral norm. Their product costs only $\exp(O(T))=L^{O(1)}$; a telescoping estimate controls their combined tails.

The weighted block sieve and local-density proxies are stated in the prime-extraction section, where their particular coefficient bounds and precision dependence are needed. The generic dilation-graph results are likewise stated at their application in the shifted correlation section. These are the only nonclassical imported ingredients of the proof.

## A long prime polynomial

The correlation argument will require cancellation in a prime polynomial at frequencies as large as $x^2$. We prove the required estimate here, including the dependence on a growing degree in the elementary mean-value argument. Throughout this section, $L=\log x$ and $T=\log L$.

**Lemma 3.1** (Long prime polynomial). *Fix $0<\tau<\eta<1$, $C>0$, and $A>0$. There is a constant $B_0=B_0(\tau,\eta,C,A)$ such that, uniformly for $$\frac{x^\tau}{2}\le N\le x^\eta,\qquad
 q\le L^C,\qquad L^{B_0}\le |t|\le x^2,$$ every Dirichlet character $\chi$ modulo $q$ and every interval $I\subset[N,2N]$ satisfy $$\begin{equation}
\tag{3.1}
 \left|\sum_{p\in I}\chi(p)p^{-1+it}\right|
 \ll_{\tau,\eta,C,A} L^{-A}.
\end{equation}$$*

The proof proceeds from a quantitative power-sum estimate to cancellation for a logarithmic phase, then to a high-height zero-free strip, and finally to primes by Mellin inversion. We first establish a power-sum estimate with sufficient uniformity in its degree. For integers $k\ge2$, $s\ge1$, and $M\ge1$, let $J_{s,k}(M)$ count the solutions of $$\sum_{i=1}^s u_i^j=\sum_{i=1}^s v_i^j
 \quad(1\le j\le k),\qquad 1\le u_i,v_i\le M.$$ Writing $K=k(k+1)/2$ and $$f(\boldsymbol\alpha)=\sum_{n=1}^M
       \mathrm{e}\!\left(\sum_{j=1}^k\alpha_j n^j\right),$$ orthogonality gives $J_{s,k}(M)=\int_{[0,1]^k}|f(\boldsymbol\alpha)|^{2s} \,d\boldsymbol\alpha$.

The argument uses the classical Vinogradov mean-value method in Linnik’s $p$-adic form; see Wooley [5, Section 2, pp. 1583–1585] for an exposition. We derive the required degree-uniform quantitative estimate below, without invoking the modern efficient-congruencing theorem of that paper.

**Lemma 3.2** (A quantitative power-sum bound). *There are absolute constants $C_1,C_2>0$ such that, for every integer $k\ge2$, some integer $s$ with $k\le s\le C_1k^4$ satisfies $$\begin{equation}
\tag{3.2}
 J_{s,k}(M)\le \exp(C_1k^{C_2})M^{2s-K+1/100}
 \qquad(M\ge1).
\end{equation}$$*

*Proof.* We iterate estimates $$\begin{equation}
\tag{3.3}
 J_{s,k}(M)\le C_s M^{E_s},\qquad
 E_s=2s-K+\epsilon_s,
\end{equation}$$ starting with $s=k$, $C_k=1$, and $\epsilon_k=K$. The iteration sends $s$ to $s+k$ and $\epsilon_s$ to $(1-1/k)\epsilon_s$.

Choose a sufficiently large absolute constant $A_1$. If $M^{1/k}<A_1k^6$, then $\log M\ll k\log(2k)$, and the trivial bound $J_{u,k}(M)\le M^{2u}$ costs at most $$\begin{equation}
\tag{3.4}
 M^K\le\exp\bigl(O(k^3\log(2k))\bigr)
\end{equation}$$ relative to every proposed estimate with exponent $2u-K+\epsilon$, $\epsilon\ge0$. Thus it suffices to treat $M^{1/k}\ge A_1k^6$. The prime number theorem in Proposition 2.1, after enlarging $A_1$, supplies a fixed list of $2k^3+5$ primes $r$ in $[M^{1/k},2M^{1/k}]$, all greater than $k$.

At moment $s+k$, call a tuple degenerate if it has fewer than $k$ distinct coordinates. There are at most $k^{s+k}M^{k-1}$ such tuples. If $G$ is their exponential sum, its contribution on one side of the equations is at most $$\int_{[0,1]^k}|G|\,|f|^{s+k}
 \le k^{s+k}M^{k-1}J_{s+k,k}(M)^{1/2}.$$ The contribution with a degenerate tuple on either side is therefore at most twice this quantity.

For a nondegenerate solution, select $k$ distinct coordinates on each side and permute them to the first $k$ positions. This costs at most $(s+k)^{2k}$. The product of the two Vandermonde products is a nonzero integer of absolute value at most $M^{k(k-1)}$. Fewer than $k^2(k-1)+1$ primes of size at least $M^{1/k}$ can divide it. Hence some prime $r$ in our list makes these first $k$ coordinates distinct modulo $r$ on each side.

For such a prime put $$F_r(\boldsymbol\alpha)=
 \sum_{\substack{1\le z_1,\ldots,z_k\le M\\
                  z_i\not\equiv z_j\pmod r\ (i\ne j)}}
 \mathrm{e}\!\left(\sum_{j=1}^k\alpha_j\sum_{i=1}^kz_i^j\right).$$ The relevant number of solutions is bounded by $$(s+k)^{2k}\sum_r\int_{[0,1]^k}|F_r|^2|f|^{2s}.$$ The integrands are nonnegative. Write $f=\sum_{a\bmod r}f_a$, where $f_a$ is restricted to $n\equiv a\pmod r$. Hölder’s inequality gives $$|f|^{2s}\le r^{2s-1}\sum_{a\bmod r}|f_a|^{2s}.$$

Fix $a$. In the system counted by $\int|F_r|^2|f_a|^{2s}$, translate all variables by $-a$. Translation preserves the equations for the first $k$ powers by the binomial formula. The remaining $s$ variables on either side are multiples of $r$, so the first lists $\boldsymbol z,\boldsymbol z'$ obey $$\begin{equation}
\tag{3.5}
 \sum_{i=1}^kz_i^j\equiv\sum_{i=1}^k(z_i')^j\pmod{r^j}
 \qquad(1\le j\le k).
\end{equation}$$ There are at most $M^k$ choices for the first list. For each such list, there are at most $k!r^{K-k}$ choices for the second. To see this, lift the prescribed $j$th sum modulo $r^j$ to a residue modulo $r^k$. The number of choices for all lifts is $\prod_{j=1}^k r^{k-j}=r^{K-k}$. For each full vector of sums modulo $r^k$, Newton’s identities determine the multiset of roots modulo $r$, since $r>k$. There are at most $k!$ orderings. The Jacobian of the power sums has determinant $$k!\prod_{i<j}(z_j'-z_i'),$$ up to sign, and is invertible modulo $r$. Each ordering therefore lifts uniquely from modulus $r$ to modulus $r^k$: at each stage the next digits are the unique solution of the corresponding linear system modulo $r$. Finally, an interval of $M$ integers contains at most one representative of any residue modulo $r^k$, because $M\le r^k$.

After both first lists are fixed, divide the remaining variables by $r$. They range over a common interval of at most $\lceil M/r\rceil$ integers and have prescribed differences of power sums. Translation to an initial interval changes only these prescribed differences. The count is a Fourier coefficient of the nonnegative function $|f|^{2s}$ at that shorter length, and consequently is at most $J_{s,k}(\lceil M/r\rceil)$. Summing over $a$ accounts for the final factor $r$, and gives $$\begin{equation}
\tag{3.6}
 \begin{split}
 J_{s+k,k}(M)
 &\le 2k^{s+k}M^{k-1}J_{s+k,k}(M)^{1/2}\\
 &\quad +(s+k)^{2k}(2k^3+5)k!
       \max_r r^{2s+K-k}M^kJ_{s,k}(\lceil M/r\rceil).
 \end{split}
\end{equation}$$

Insert (3.3). Since $E_s\ge0$, rounding costs at most $2^{E_s}$, and the exponent of $r$ becomes $$2s+K-k-E_s=k^2-\epsilon_s\ge0.$$ Replacing $r$ by at most $2M^{1/k}$ therefore gives the exponent $$k+E_s+\frac{k^2-\epsilon_s}{k}
 =2(s+k)-K+(1-1/k)\epsilon_s.$$ The inequality $J\le a\sqrt J+b$ implies $J\le2a^2+2b$. The exponent $2k-2$ from $a^2$ is admissible: the target exponent starts at $2k$, and at each step its increase is $2k-\epsilon_s/k\ge2k-K/k>0$. Thus the asserted iteration holds. Its constants can be chosen with $$\log C_{s+k}\le \log(1+C_s)
 +O\!\left((s+k)\log(2k)+k\log(s+k)+k^3\log(2k)\right),$$ including (3.4).

After $O(k\log(2k))$ steps, $\epsilon_s=K(1-1/k)^{(s-k)/k}\le1/100$. Then $s=O(k^2\log(2k))\le C_1k^4$, and summing the displayed costs gives $\log C_s\le C_1k^{C_2}$ for absolute constants. Increasing the exponent from $\epsilon_s$ to $1/100$ proves the Lemma. ◻

**Lemma 3.3** (A logarithmic phase on progressions). *Fix $C>0$. There is an absolute constant $C_3>0$ such that, for sufficiently large $x$ in terms of $C$, the following holds uniformly: $$\exp(L/T^2)\le N'\le2x^5,\qquad q\le L^C,\qquad
 \exp(L/(2T^2))\le |v|\le4x^3.$$ For every residue $a\pmod q$ and every interval $I\subset[N',2N']$, $$\begin{equation}
\tag{3.7}
 \left|\sum_{\substack{n\in I\\n\equiv a\pmod q}}n^{iv}\right|
 \ll \frac{N'}q\exp(-L/T^{C_3}).
\end{equation}$$*

*Proof.* Put $H=N'/q$ and $y=\log|v|/\log H$. Then $$\begin{equation}
\tag{3.8}
 \log H\ge L/T^2-CT\gg L/T^2,\qquad y\ll T^2.
\end{equation}$$ Writing $n=q(b+a/q)$, with $0\le a<q$, reduces the sum, up to a factor of modulus one, to $\sum_{b\in\mathcal I}(b+a/q)^{iv}$, where $\mathcal I$ is an interval of integers and $H\le b+a/q\le2H$.

If $y<4/5$, the derivative of $v\log(b+a/q)/(2\pi)$ is monotone, has magnitude comparable to $|v|/H$, and has magnitude less than $1/2$. The monotone first derivative estimate in Proposition 2.3 therefore bounds the sum by $O(H/|v|)$. The lower bound on $|v|$ makes this smaller than (3.7).

Suppose now that $y\ge4/5$. Set $$M=\lfloor H^{3/4}\rfloor,\qquad k=\lceil4y+8\rceil.$$ Averaging the sum over forward shifts $1\le h\le M$ changes it by $O(M)$: a shift changes an interval at only $O(h)$ endpoints. For $b\in\mathcal I$, Taylor expansion gives $$\frac{v}{2\pi}\log(b+h+a/q)
 =\frac{v}{2\pi}\log(b+a/q)
       +\sum_{j=1}^k\alpha_j(b)h^j+O(H^{-2}),
 \qquad
 \alpha_j(b)=\frac{(-1)^{j-1}v}{2\pi j(b+a/q)^j}.$$ Indeed the remainder is $O(|v|(M/H)^{k+1})=O(H^{y-(k+1)/4})=O(H^{-9/4})$, uniformly even as $k$ grows. Thus, with $$S(\boldsymbol\alpha)=\sum_{h=1}^M
                 \mathrm{e}\!\left(\sum_{j=1}^k\alpha_jh^j\right),$$ the original sum is bounded by $$\begin{equation}
\tag{3.9}
 \frac1M\sum_{b\in\mathcal I}|S(\boldsymbol\alpha(b))|
       +O(M+H^{-1}).
\end{equation}$$

Partition the coefficient torus $[0,1)^k$ into boxes with side length $M^{-j}$ in coordinate $j$. Each box contains at most $$\begin{equation}
\tag{3.10}
 \exp(O(k))H^{4/5}
\end{equation}$$ of the vectors $\boldsymbol\alpha(b)\pmod1$. For this it suffices to use the coordinate $j=\lceil y+3/20\rceil$, which lies between $1$ and $k$. Before reduction modulo one, this coordinate has magnitude $O(H^{-3/20})$, is monotone, and has derivative of magnitude at least $$\frac{|v|}{2\pi(2H)^{j+1}}
       \ge\exp(-O(k))H^{y-j-1}.$$ A coordinate interval of length $M^{-j}$ on the torus pulls back to at most two intervals in $b$. Their total length is at most $\exp(O(k))H^{1+j/4-y}$. Here the floor in $M$ costs $\exp(O(k))$, while $$y-\frac j4\ge\frac{3y}4-\frac{23}{80}
       \ge\frac5{16}>\frac15.$$ Counting integer points proves (3.10).

Let $s$ be supplied by Lemma 3.2. We also need the following bound for suprema over boxes $Q$: $$\begin{equation}
\tag{3.11}
 \sum_Q\sup_{\boldsymbol\alpha\in Q}|S(\boldsymbol\alpha)|^{2s}
 \le\exp(O(sk+k))M^KJ_{s,k}(M).
\end{equation}$$ To prove it, rescale each box to $[0,1]^k$. Iterating the one-dimensional fundamental theorem of calculus gives, for any smooth function $F$ on that cube, $$\sup|F|\le\sum_{\boldsymbol\epsilon\in\{0,1\}^k}
       \int_{[0,1]^k}|\partial^{\boldsymbol\epsilon}F|.$$ Hölder’s inequality bounds the $2s$th power of the right-hand side by $2^{k(2s-1)}$ times the sum of the corresponding $2s$th moments. For the rescaled $S$, every mixed derivative has coefficients bounded in modulus by $(2\pi)^k$: each differentiation in coordinate $j$ introduces the factor $2\pi i h^j/M^j$. On summing over the boxes, change of variables contributes $M^K$. Orthogonality then bounds the full-torus moment of every such derivative by $(2\pi)^{2sk}J_{s,k}(M)$. This proves (3.11), with constants controlled at the growing degree.

Apply Hölder’s inequality to the sum in (3.9), and use (3.10), (3.11), and (3.2). Since $|\mathcal I|\ll H$, the result is $$\begin{equation}
\tag{3.12}
 \frac1M\sum_{b\in\mathcal I}|S(\boldsymbol\alpha(b))|
 \ll H\left(\exp(O(k^{C_4}))H^{-1/5}M^{1/100}\right)^{1/(2s)}
\end{equation}$$ for an absolute constant $C_4$. We have $k\ll T^2$ and $s\ll T^8$, whereas $$-\frac15\log H+\frac1{100}\log M
       \le-\frac{77}{400}\log H.$$ Every fixed power of $T$ is $o(L/T^2)$. Thus the right-hand side of (3.12) is at most $H\exp(-c_1L/T^{10})$ for some absolute $c_1>0$, once $x$ is sufficiently large. The errors in (3.9) are smaller. Increasing a fixed exponent $C_3>10$ absorbs $c_1$ and proves the Lemma. ◻

We write $D(s,\chi)$ for the Dirichlet $L$-function, to distinguish it from $L=\log x$. Characters need not be primitive. Periodicity gives $\sum_{n\le u}\chi(n)=c_\chi u+O(q)$, where $c_\chi=q^{-1}\sum_{a\bmod q}\chi(a)$. Partial summation therefore continues $D(s,\chi)$ meromorphically to $\operatorname{Re}s>0$, with only the possible simple pole at $s=1$, and gives, for $\sigma=\operatorname{Re}s$ in a fixed compact subinterval of $(0,\infty)$, $$\begin{equation}
\tag{3.13}
 D(s,\chi)=\sum_{n\le Y}\frac{\chi(n)}{n^s}
       +\frac{c_\chi Y^{1-s}}{s-1}
       +O\bigl(q(1+|s|)Y^{-\sigma}\bigr).
\end{equation}$$

**Lemma 3.4** (A bound near the line $\operatorname{Re}s=1$). *Fix $C>0$ and put $r_*=T^4/L$. Uniformly for $q\le L^C$, $$\begin{equation}
\tag{3.14}
 \log|D(\sigma+iv,\chi)|\ll_C T^2
 \quad\left(|\sigma-1|\le10r_*,\quad
                   \frac12\le|v|\le3x^3\right).
\end{equation}$$*

*Proof.* First suppose $|v|\le\exp(L/(2T^2))$, and use $Y=\exp(2L/T^2)$ in (3.13). Absolute summation gives $$\sum_{n\le Y}n^{-\sigma}
 \ll(1+\log Y)\max(1,Y^{1-\sigma})\le\exp(O(T^2)).$$ Since $|s-1|\ge1/2$, the pole term has the same bound. The error is at most $$\exp\left(-\frac{3L}{2T^2}+O(T^2+CT)\right),$$ and hence is negligible.

For $\exp(L/(2T^2))<|v|\le3x^3$, take $Y=x^5$. The terms with $n\le\exp(L/T^2)$ again contribute $\exp(O(T^2))$ in absolute value. On a dyadic interval above this threshold, sum (3.7), with phase $-v$, over the residue classes modulo $q$, including their character coefficients. The factors $q$ and $1/q$ cancel. Partial summation with $n^{-\sigma}$ bounds that dyad by $$\exp(-L/T^{C_3})\exp(O(T^4)).$$ There are $O(L)$ dyads, and the same bound applies to a final partial dyad. Their total is negligible, since $L/T^{C_3}$ exceeds every fixed power of $T$. Finally, the pole term and remainder in (3.13) are bounded respectively by $$\exp\left(-\frac{L}{2T^2}+O(T^4)\right),\qquad
 \exp\bigl(-2L+O(T^4+CT)\bigr).$$ This proves (3.14). ◻

**Lemma 3.5** (Local logarithmic derivative). *Fix $C>0$, let $q\le L^C$, and put $s_0=1+r_*+iv$, where $1\le|v|\le\tfrac52x^3$. There is a radius $R$ with $4r_*\le R\le5r_*$, with no zero on its boundary, for which $$\begin{equation}
\tag{3.15}
 \frac{D'}{D}(s,\chi)
 =\sum_{|\rho-s_0|<R}\frac1{s-\rho}
       +O_C(T^2/r_*)\qquad(|s-s_0|\le2r_*),
\end{equation}$$ away from zeros. The sum counts zeros with multiplicity and has $O_C(T^2)$ terms.*

*Proof.* For large $x$, the disk $|s-s_0|\le8r_*$ avoids the possible pole at $s=1$ and lies in the region of Lemma 3.4. At its center the Euler product gives $$|D(s_0,\chi)|\ge\prod_p(1+p^{-1-r_*})^{-1}
       =\frac{\zeta(2+2r_*)}{\zeta(1+r_*)}\gg r_*.$$ Thus $\log|D(s_0,\chi)|\ge-O(T)$. Jensen’s formula, using the radius $8r_*$ and the upper bound $O_C(T^2)$, shows that the disk of radius $5r_*$ contains $O_C(T^2)$ zeros. Choose $R\in[4r_*,5r_*]$ so that none lies on its boundary.

Use centered coordinates $z=s-s_0$, and write $a=\rho-s_0$ for each zero in $|z|<R$. Divide $D(s_0+z,\chi)$ by the disk Blaschke factors $$B_a(z)=\frac{R(z-a)}{R^2-\overline a z},$$ repeated with multiplicity. The quotient $G$ is holomorphic and nonvanishing on the closed disk, and has the same boundary modulus as $D$. Maximum modulus gives $\log|G|\le M_0$ throughout the disk for some $M_0=O_C(T^2)$. Since $|B_a(0)|<1$, $\log|G(0)|\ge-O(T)$.

Let $h$ be an analytic logarithm of $G$. The positive harmonic function $M_0-\operatorname{Re}h$ has value $O_C(T^2)$ at the center. The Poisson formula, or its derivative together with Harnack’s inequality on concentric disks, gives $$|h'(z)|\ll_C T^2/r_*\qquad(|z|\le2r_*).$$ Restoring the factors uses $$\frac{B_a'}{B_a}(z)=\frac1{z-a}
       +\frac{\overline a}{R^2-\overline a z}.$$ The second term is $O(1/r_*)$ on $|z|\le2r_*$, uniformly in $|a|<R$. There are $O_C(T^2)$ such terms, giving exactly (3.15). ◻

**Lemma 3.6** (A zero-free strip at large height). *For each fixed $C>0$ there is $c=c(C)>0$ such that every character of modulus at most $L^C$ has no zero in $$\begin{equation}
\tag{3.16}
 \operatorname{Re}s\ge1-cT^2/L,\qquad
                    1\le|\operatorname{Im}s|\le x^3.
\end{equation}$$ Moreover, $$\begin{equation}
\tag{3.17}
 \left|\frac{D'}D(s,\chi)\right|\ll_C L
 \quad\left(1-\frac{cT^2}{2L}\le\operatorname{Re}s\le1+\frac1L,
       \quad2\le|\operatorname{Im}s|\le\frac{x^3}{2}\right).
\end{equation}$$*

*Proof.* For $\sigma>1$, the Euler products and the inequality $3+4\cos\theta+\cos(2\theta)=2(1+\cos\theta)^2\ge0$ give $$\begin{equation}
\tag{3.18}
 0\le-3\frac{\zeta'}\zeta(\sigma)
       -4\operatorname{Re}\frac{D'}D(\sigma+iv,\chi)
       -\operatorname{Re}\frac{D'}D(\sigma+2iv,\chi^2).
\end{equation}$$ Indeed this follows term by term in the absolutely convergent prime-power expansions; primes dividing the modulus contribute only the positive zeta term. Also $-\zeta'/\zeta(\sigma)=1/(\sigma-1)+O(1)$ near $1$.

Suppose $\rho=\beta+iv$ were a zero in (3.16), and set $\sigma=1+20cT^2/L$. Apply Lemma 3.5 at heights $v$ and $2v$. The evaluation points lie in the respective inner disks, and $\rho$ lies in the first zero sum, because $T^2/L=o(r_*)$. No zero has real part greater than $1$, by the absolutely convergent Euler product. All terms in the zero sums therefore contribute nonpositively to the negative real logarithmic derivatives. Retaining the term at $\rho$, and using $0<\sigma-\beta\le21cT^2/L$, bounds the right-hand side of (3.18) by $$\left(\frac{3}{20c}-\frac{4}{21c}+O_C(1)\right)\frac L{T^2}
 =\left(-\frac{17}{420c}+O_C(1)\right)\frac L{T^2}.$$ Here the errors are $O_C(T^2/r_*)=O_C(L/T^2)$. Choosing a sufficiently small fixed $c>0$ gives a contradiction.

For $s$ in the region of (3.17), apply the local formula centered at $1+r_*+i\operatorname{Im}s$. Every zero in its sum has absolute imaginary part between $1$ and $x^3$, since $2\le|\operatorname{Im}s|\le x^3/2$ and $r_*=o(1)$. By (3.16), its horizontal distance from $s$ is at least $cT^2/(2L)$. The $O_C(T^2)$ zero terms and the local error therefore total $O_C(L)$, proving (3.17). ◻

*Proof of Lemma 3.1.* We first establish the analogous bound with the von Mangoldt weight. Let $\delta=L^{-A-4}$. Smooth the indicator of $I/N\subset[1,2]$ by convolution with a nonnegative smooth kernel of width $\delta$. This gives $0\le g\le1$, supported in $[1/2,3]$, whose difference from the indicator is supported within $O(\delta)$ of its endpoints, and with $\|g^{(j)}\|_\infty\ll_j\delta^{-j}$. The construction also applies when $I$ is shorter than $\delta N$. Since $\Lambda(n)\le\log n$, the error in replacing the interval by $g(n/N)$ is $$\begin{equation}
\tag{3.19}
 O\!\left((\delta N+1)\frac{\log(3N)}N\right)
       =O(L^{-A-2}),
\end{equation}$$ uniformly in $I$.

Define the Mellin transform by $$\widehat g(z)=\int_0^\infty g(w)w^z\,\frac{dw}{w}.$$ On every fixed bounded real-part strip, integration by parts gives $$\begin{equation}
\tag{3.20}
 |\widehat g(u+iv)|\ll_j
       L^{(j+1)(A+5)}(1+|v|)^{-j}.
\end{equation}$$ Also $|\widehat g(u+iv)|\ll1$ there, by absolute integration. Mellin inversion and the absolutely convergent logarithmic derivative on $\operatorname{Re}z=1/L$ yield $$\begin{equation}
\tag{3.21}
 \sum_n\Lambda(n)\chi(n)n^{-1+it}g(n/N)
 =\frac1{2\pi i}\int_{1/L-i\infty}^{1/L+i\infty}
       \widehat g(z)N^z
       \left(-\frac{D'}D(1-it+z,\chi)\right)dz.
\end{equation}$$ On this full line, absolute convergence gives $$\left|\frac{D'}D(1+1/L+i u,\chi)\right|
 \le\sum_n\frac{\Lambda(n)}{n^{1+1/L}}
       =-\frac{\zeta'}\zeta(1+1/L)\ll L,$$ at every height $u$.

Choose a fixed $C_5>A+6$ and put $H_0=L^{C_5}$. Then choose a fixed integration-by-parts order $j$ large enough that (3.20) makes the two tails with $|\operatorname{Im}z|>H_0$ in (3.21) $O(L^{-A-2})$. Explicitly their bound is $$O_j\!\left(L^{1+(j+1)(A+5)}H_0^{1-j}\right),$$ since $N^{1/L}\ll1$. Fix $B_0>C_5+2$. For $L^{B_0}\le|t|\le x^2$, every point in the rectangle $$-\frac{cT^2}{2L}\le\operatorname{Re}z\le\frac1L,
       \qquad |\operatorname{Im}z|\le H_0$$ has $$\begin{equation}
\tag{3.22}
 2\le|-t+\operatorname{Im}z|
       \le x^2+H_0<\frac{x^3}{2}
\end{equation}$$ for large $x$. Thus Lemma 3.6 applies throughout the rectangle. There are no zeros or poles of the logarithmic derivative inside it; in particular, the possible principal-character pole at $z=it$ is outside it.

Shift the truncated contour to $\operatorname{Re}z=-cT^2/(2L)$. The horizontal edges are $O(L^{-A-2})$, by (3.17) and (3.20), increasing the already fixed order $j$ if necessary. On the new vertical segment, $$|N^z|=\exp\left(-\frac{cT^2\log N}{2L}\right)
       \ll\exp(-c\tau T^2/2).$$ Its remaining factors and length cost at most a fixed power of $L$. Since $\exp(-c\tau T^2/2)$ is smaller than every prescribed fixed power of $L^{-1}$, the shifted integral is $O(L^{-A-2})$. Together with (3.19), this proves, uniformly for all subintervals $I\subset[N,2N]$, $$\begin{equation}
\tag{3.23}
 \sum_{n\in I}\Lambda(n)\chi(n)n^{-1+it}\ll L^{-A-2}.
\end{equation}$$

Prime powers of exponent at least two contribute in absolute value at most $O(N^{-1/2}(\log(3N))^2)$: there are $O(\sqrt N\log(3N))$ possible bases and exponents with $N\le p^a\le2N$, and every summand has size $O(\log(3N)/N)$. This is smaller than every fixed power of $L^{-1}$ in the present range. Removing them from (3.23) gives the same uniform bound for $\sum_{p\in I}(\log p)\chi(p)p^{-1+it}$. Finally, partial summation against $1/\log u$, whose value and total variation on $[N,2N]$ are $O_{\tau}(1/L)$, removes the logarithmic weight and proves (3.1). ◻

## A prime-slot shifted correlation with a common parity twist

We prove the shifted-correlation estimate needed below. The graph transference and residual ideal operator are imported from [4]; the replacement of a long rough-integer factor by a prime factor, and the common parity twist, are proved here.

### Groups, marked weights, and the assertion

Fix $$0<a<b<c<d<0.47,\qquad c_0,C_0,v_-,v_+>0,
 \qquad 0<q_0<1,\qquad \ell\geq1.$$ The integer $\ell$ is fixed. Let $\mathcal S,\mathcal B$ index pairwise disjoint groups of primes $\mathcal P_g$, with $$\begin{gather}
 c_0T\leq |\mathcal S|,|\mathcal B|\leq C_0T,
 \qquad v_-\leq V_g:=\sum_{p\in\mathcal P_g}\frac1p\leq v_+,
 \tag{4.1}\\
 \mathcal P_g\subset[\exp(L^a),\exp(L^b)]\quad(g\in\mathcal S),
 \qquad
 \mathcal P_g\subset[\exp(L^c),\exp(L^d)]\quad(g\in\mathcal B).
 \notag
\end{gather}$$ Each big group is the set of all primes in an interval. Put $\mathcal P=\bigcup_g\mathcal P_g$, $s_P=|\mathcal S|+|\mathcal B|$, and, for $n\geq1$, $$n_*=\prod_{p\notin\mathcal P}p^{v_p(n)},\qquad
 \omega_g(n)=\sum_{p\in\mathcal P_g}\mathbf{1}_{p\mid n},\qquad
 \omega_P(n)=\sum_g\omega_g(n).$$ For the graph definitions below, extend $\omega_g$ and $\omega_P$ to all $n\in\mathbb Z$ by these same divisibility formulas, including the convention that every prime divides zero. For a vector $\mathbf t=(t_g)$ of nonnegative integers define $$\begin{equation}
\tag{4.2}
 W_{\mathbf t}(n)=q_0^{\omega_P(n)-\sum_g t_g}
                   \prod_g\frac{(\omega_g(n))_{t_g}}{V_g^{t_g}},
 \qquad W_\ell=W_{(\ell,\ldots,\ell)}.
\end{equation}$$ Here $(u)_t=u(u-1)\cdots(u-t+1)$, and $(u)_0=1$. An ordered marked list has $t_g$ distinct prime divisors from each $\mathcal P_g$. If $\mathbf b$ is a function of these lists, define $$W_{\mathbf t}^{\mathbf b}(n)
 =q_0^{\omega_P(n)-\sum_g t_g}
       \prod_g V_g^{-t_g}\sum_{\text{marked lists at }n}\mathbf b.$$ Equivalently, this is $W_{\mathbf t}(n)$ times the average of $\mathbf b$ over its lists, with value zero when no such list exists. If $t_g\leq t_{\max}$ and $|\mathbf b|\leq1$, then $$\begin{equation}
\tag{4.3}
 |W_{\mathbf t}^{\mathbf b}(n)|\leq W_{\mathbf t}(n)
 \leq L^{C(t_{\max})}.
\end{equation}$$ Indeed $q_0^{u-t}(u)_tV_g^{-t}$ is bounded uniformly in integers $u\geq t$, with a bound depending only on $t_{\max}$ and the fixed group data, and there are $O(T)$ groups.

Use the same choice at both endpoints in $$\begin{equation}
\tag{4.4}
 \varepsilon(n)=1\quad\hbox{or}\quad
 \varepsilon(n)=(-1)^{\sum_{p\in\mathcal P}v_p(n)}.
\end{equation}$$ In either case $\varepsilon$ is completely multiplicative, real, and of modulus one. An invariant endpoint core has the form $$\begin{equation}
\tag{4.5}
 F(n)=\sum_{mpr=n_*}\alpha_m\chi_0(m)m^{i\sigma_0}
           \mathbf{1}_{p\in I_p,\ p\ {\rm prime}}p^{i\sigma_1}c_r.
\end{equation}$$ Fix $0<\tau<\eta<1/4$. Here $I_p\subset[x^\tau,x^\eta]$ is an interval, $|\alpha_m|,|c_r|\leq L^{C}$, $\alpha_m=0$ unless $P^-(m)>W$, and the modulus of $\chi_0$ and $|\sigma_0|,|\sigma_1|$ are at most $L^C$. The constants in this section may depend on these fixed bounds. The word invariant refers to the identity $F(vn)=F(n)$ whenever $v_*=1$.

**Theorem 4.1** (Twisted prime-slot correlation). *Let $F,G$ have the form (4.5), with possibly different coefficients, characters, intervals, and frequencies, subject to fixed bounds as above. For every fixed $D_0>0$ there is a fixed $B>0$ with the following property. Suppose that the sequence $\alpha$ in $F$ satisfies $$\begin{equation}
\tag{4.6}
 \left|\sum_{m\in I}\alpha_m\chi(m)m^{-1+it}\right|\leq L^{-B}
 \quad\left(
 \begin{array}{l}
 I\subset[1,x^2]\text{ an interval},\\
 \operatorname{mod}(\chi)\leq L^B,\quad |t|\leq L^B
 \end{array}\right).
\end{equation}$$ There is no discrepancy requirement on $G$. Uniformly for $xL^{-C}\leq Z\leq xL^C$, integers $0<|k|\leq L^C$, $|a_1|,|a_2|\leq L^C$, and smooth functions $\psi$ supported in a fixed compact subinterval of $(0,\infty)$ with $\|\psi^{(j)}\|_\infty\ll_j L^{C(j+1)}$, one has $$\begin{equation}
\tag{4.7}
 \sum_{\substack{z>0\\z+k>0}}\frac{\psi(z/Z)}z
 z^{ia_1}(z+k)^{ia_2}\overline{F(z)}G(z+k)
 W_\ell(z)W_\ell(z+k)\varepsilon(z)\varepsilon(z+k)
 \ll L^{-D_0}.
\end{equation}$$ The exponent $B$ depends only on $D_0$ and the displayed fixed data.*

The proof uses a residual operator made up of one raw term and signed comparison terms. Transference makes the residual pairing small; after the shared dilation is removed, the raw term is the correlation in (4.7), because the common sign cancels. Each comparison has two independent large free products, allowing a Fourier estimate. We will bound these comparisons and subtract them from the residual pairing.

### The graph inputs

We give the operator definitions to specify their normalizations. For a sufficiently large fixed integer $J$, put $M=J+\ell$ and $\mu_g(p)=1/(pV_g)$. A pattern $\nu$ specifies $C_g\subset\{1,\ldots,J\}$ with $C_g=\varnothing$ in small groups and $|C_g|\leq m_0$ in big groups. Put $t_g=\ell+|C_g|$. The first $J$ slots outside $C_g$ are shared between the endpoints. To form the dilation $D$, take their labels and independent auxiliary labels of law $\mu_g$ in the slots of $C_g$. Thus $D$ contains $J$ labels from each group, counted with multiplicity. The coefficient $K_\nu$ may depend only on the ordered big-group source and target labels and the auxiliary big-group free labels.

A physical state at $n\in\mathbb Z$ consists of $M$ ordered, distinct divisors from each group. Each state has mass $\prod_gV_g^{-M}$, with counting measure in $n$. For a row transition from $n$ to $n'=n+kD$, retain the shared labels and sum over all physical target lists with coefficient $\prod_gV_g^{-t_g}$. Auxiliary free labels are forbidden from both endpoint lists; they may coincide with one another. The row multiplier is $$\begin{equation}
\tag{4.8}
 K_\nu D^{i\zeta}
 q_0^{(\omega_P(n)-Ms_P)/2}q_0^{(\omega_P(n')-Ms_P)/2}.
\end{equation}$$ The operator $\mathcal A_\zeta$ is the sum of these row operations, averaged over independent permutations of the $M$ slots in every group at each endpoint. In particular the joint normalization of the two lists in group $g$ is $V_g^{-M-t_g}$.

The ideal operator acts on the probability space of the ordered big-group lists, with independent coordinates of law $\mu_g$; repetitions are permitted. It retains the same shared slots and samples both the unshared target slots and the auxiliary slots independently. If $D_{\mathcal B}$ is the big-group part of $D$, its multiplier is $K_\nu D_{\mathcal B}^{i\zeta}\mathrm{e}(\Theta D_{\mathcal B})$. The sum, symmetrized at both ends, is $\mathcal T_\zeta(\Theta)$.

**Proposition 4.2** (Transference input). *The following are the Local Transference Theorem, its Endpoint Pairing Corollary, and the Absolute Physical Bounds Lemma of [4, Section 3, Theorem 3.5, Corollary 3.11, and Lemma 3.4]. Assume $\sum_\nu\sup|K_\nu|\leq L^{C_1}$, where $m_0,C_1$ are fixed independently of $J$. For every fixed $E>0$ there is an $E_{\rm id}>0$, depending only on $E$ and the group data, such that $$\sup_{\Theta\in\mathbb R}
       \|\mathcal T_\zeta(\Theta)\|_{2\to2}\leq L^{-E_{\rm id}}$$ implies the following conclusion for all sufficiently large fixed $J$. Let $I=[X,2X)$ with $x^\gamma\leq X\leq x^{1/\gamma}$ for some fixed $\gamma>0$. If $f$ is supported on positions in $I$, is independent of the chosen marks, and $$\sup|f|\leq\exp(O(\sqrt L)),\qquad
 \|f\|,\|g\|\leq X^{1/2}L^{C_3},$$ then $$\begin{equation}
\tag{4.9}
 |\langle f,\mathcal A_\zeta g\rangle|
 \ll XL^{-E+2C_3}.
\end{equation}$$ The lower bound for $J$ may depend on $m_0,C_1$; the threshold for $x$ may also depend on $J$, the fixed exponent bounding $|k|$, and $\gamma$. There is no additional restriction on $\zeta$ beyond the ideal norm hypothesis. The operator obtained by taking absolute values of all transition coefficients has row and column sums at most $L^{C_{\rm abs}}$, with $C_{\rm abs}$ independent of $J$.*

**Proposition 4.3** (Residual ideal family and comparison kernels). *The following are the Residual Ideal Operator Theorem and Comparison Kernel Lemma of [4, Section 4, Theorem 4.1 and Lemma 4.3]. For every prescribed $E_{\rm id}>0$ and fixed $C_4\geq0$, there are fixed $m_0,J_0,C_1$ such that, for each fixed $J\geq J_0$, a family consisting of the raw pattern $C_g=\varnothing$, $K_0=1$, and signed comparison patterns satisfies $$\begin{equation}
\tag{4.10}
 \sum_\nu\sup|K_\nu|\leq L^{C_1},\qquad
 \sup_{\substack{\Theta\in\mathbb R\\|\zeta|\leq L^{C_4}}}
       \|\mathcal T_\zeta(\Theta)\|_{2\to2}
       \leq L^{-E_{\rm id}}.
\end{equation}$$ The family is independent of the individual values of $\Theta,\zeta$, and all its defining parameters are independent of $J$.*

*Split the big groups into two blocks. Every comparison frees nonempty sets of probes $A,B$ in the respective blocks and has coefficient $$\begin{equation}
\tag{4.11}
 -(-1)^{|A|+|B|}\mathcal K_A(D_A,X_A)\mathcal K_B(D_B,X_B).
\end{equation}$$ Here $D_A,D_B$ are the free products, $X_A$ is the corresponding target-mark product, and $X_B$ the corresponding source-mark product. No shared label or final $\ell$ mark enters these kernels. For a slot set $\Lambda$, their exact form is $$\begin{equation}
\tag{4.12}
 \mathcal K_\Lambda(D,X)
 =\sum_{j:\nu_{\Lambda j}\geq\xi}
   \frac{\mathbf{1}_{\log D\in I_j}\mathbf{1}_{\log X\in I_j}}{\nu_{\Lambda j}}
   \sum_{\substack{\chi\ {\rm primitive}\\
                    \operatorname{cond}(\chi)\leq Q}}
               \overline{\chi(D)}\chi(X),
 \quad I_j=[jh,(j+1)h),
\end{equation}$$ where $\nu_{\Lambda j}$ is the probability of the indicated cell under the independent slot laws. The quantities $Q,h^{-1},\xi^{-1}$ are fixed powers of $L$, with $h\leq1$. There are at most $Q^2$ characters and $O_{m_0}(1+TL^d/h)$ nonempty cells, and $$\sup|\mathcal K_\Lambda|\leq Q^2\xi^{-1},\qquad
 \sup_X\mathbb E_D|\mathcal K_\Lambda(D,X)|\leq Q^2.$$ More precisely, the parameters can be chosen, independently of $J$, so that for any fixed $A_0>0$, any tuple tests $f(X_B),g(X_A)$, and every $\theta\in\mathbb R$, $|\zeta|\leq L^{C_4}$, $$\begin{align}
 \Big|\mathbb E\,\overline{f(X_B)}g(X_A)
 \big[&(X_AX_B)^{i\zeta}\mathrm{e}(\theta X_AX_B)\notag\\
 &-\mathcal K_A(D_A,X_A)\mathcal K_B(D_B,X_B)
       (D_AD_B)^{i\zeta}\mathrm{e}(\theta D_AD_B)\big]\Big|
 \leq L^{-A_0}\|f\|_2\|g\|_2.
 \tag{4.13}
\end{align}$$ All four label tuples in this expectation are independent. The tests need not be functions only of their products. Expanding the two kernels in (4.11), including all patterns, has total coefficient mass and number of terms bounded by fixed powers of $L$.*

These are precisely the graph inputs we use. In particular, (4.12) consists of two global character and cell expansions, not one expansion for each group.

### Endpoint norms and removal of the shared dilation

We now prove Theorem 4.1 using these contracts. Write $\tau(v)$ for the divisor-counting function. The pointwise estimate $$\begin{equation}
\tag{4.14}
 |F(n)|\ll L^{C'}\tau(n_*)^2
\end{equation}$$ follows by counting the three-factor decompositions in (4.5); the same estimate holds for $G$. On physical states the function $$F(n)\varepsilon(n)q_0^{(\omega_P(n)-Ms_P)/2}$$ is independent of the chosen marks, and its damping is at most one. For a fixed physical list of product $P$, one has $n_*\mid n/P$. Consequently Proposition 2.2 gives, uniformly on a fixed enlargement of a position dyad, $$\sum_{\substack{n\asymp X\\P\mid n}}|F(n)|^2
 \ll L^{C'}\sum_{v\ll X/P}\tau(v)^4
 \ll (X/P)L^{C''}.$$ The normalized reciprocal sum of the admissible lists is at most $$\prod_g V_g^{-M}
       \sum_{\text{lists}}\frac1P
 \leq\prod_g\left(\sum_{p\in\mathcal P_g}\frac1{pV_g}\right)^M=1.$$ Here $P\leq\exp(O_J(TL^d))=x^{o(1)}$, so $X/P$ is in the ordinary divisor-moment range. We have proved $$\begin{equation}
\tag{4.15}
 \|F\varepsilon q_0^{(\omega_P-Ms_P)/2}\|_{n\asymp X}
 \ll X^{1/2}L^{C_3},
\end{equation}$$ with $C_3$ independent of $J$ and of the subsequent kernel choices. Bounded smooth factors do not affect this independence. Moreover, both $m$ and $p$ in (4.5) are $W$-rough for large $x$. There are at most $O(\sqrt L)$ prime factors above $W$ in $n\asymp x^{1+o(1)}$, counted with multiplicity. Assigning each such factor to $m,p$, or the remaining factor shows $$\begin{equation}
\tag{4.16}
 |F(n)|\leq L^{C'}3^{O(\sqrt L)}=\exp(O(\sqrt L)).
\end{equation}$$ This proves every endpoint hypothesis of Proposition 4.2.

Consider the physical pairing with extra cutoff, harmonic measure, and phases $$\begin{equation}
\tag{4.17}
 \frac{\psi(n/(ZD))}{n}
 D^{-i(a_1+a_2)}n^{ia_1}(n')^{ia_2}
 \overline{F(n)}G(n')\varepsilon(n)\varepsilon(n')
 q_0^{(\omega_P(n)-Ms_P)/2}q_0^{(\omega_P(n')-Ms_P)/2}.
\end{equation}$$ The row operation itself contributes the other two half-damping factors in (4.8). Summation over states, auxiliary draws, and patterns is understood in (4.17), with the row coefficient $K_\nu$.

Here $n\asymp ZD=x^{1+o(1)}$ and $|n'-n|=x^{o(1)}$. Split $n$ among $O(L)$ dyads $[X,2X)$ and restrict $n'$ to a fixed enlargement of each dyad. As in Lemma 2.4, Fourier inversion of $u\mapsto\psi(e^u)$ separates the cutoff into powers of $n$ and $D$; put the bounded factor $X/n$ in the first vector and divide the pairing by $X$. The total Fourier integral mass is a fixed power of $L$, independent of $J$.

We specify a useful quantifier here. If the logarithmic cutoff derivatives are bounded by $O_j(L^{C_\psi(j+1)})$, fix an exponent $F_0>C_\psi+2$ before forming the ideal family. Integration by parts gives, for each fixed $N$, $$\int_{|v|>L^{F_0}}|\widehat{\psi\circ\exp}(v)|\,dv
 \ll_N L^{C_\psi(N+1)-F_0(N-1)}.$$ Thus this same cutoff exponent permits arbitrary saving by increasing $N$. Choose $C_4$ to contain $a_1+a_2$ and all frequencies in the truncated integral. By (4.15) and (4.16), choose $E$ large enough for the desired saving after the fixed Fourier and dyadic costs; then choose $E_{\rm id}$, the residual family, and finally $J$. The Fourier tail is bounded using the absolute row and column bounds of Proposition 4.2; its accuracy can be increased after the family and $J$ have been fixed without changing $F_0$ or $C_4$. It follows that the sum of the residual pairings is $O(L^{-D})$ for any prescribed fixed $D$.

We next identify each individual pairing. Write $D=D_RD_C$, where $D_R$ is the shared product and $D_C$ the free product, and put $n=D_Rw$, $n'=D_Rw'$. Then $w'=w+kD_C$. Away from overlaps of shared labels with one another or with the divisors of $w,w'$, the number of shared labels in group $g$ is $M-t_g$, and $$\omega_g(D_Rw)-M=\omega_g(w)-t_g.$$ The full damping therefore leaves exactly the two damping factors of $W_{\mathbf t}(w)W_{\mathbf t}(w')$. The identity $$V_g^{-M-t_g}=V_g^{-(M-t_g)}V_g^{-2t_g}$$ and $1/n=1/(D_Rw)$ turn the shared labels into independent draws of law $\mu_g$, leaving the normalizations for the two unshared marked lists. The cores are unchanged. The sign identity is exact, even when overlaps occur: $$\begin{equation}
\tag{4.18}
 \varepsilon(D_Rw)\varepsilon(D_Rw')
 =\varepsilon(D_R)^2\varepsilon(w)\varepsilon(w')
 =\varepsilon(w)\varepsilon(w').
\end{equation}$$ The phases and cutoff in (4.17) become $$\psi(w/(ZD_C))\,(w/D_C)^{ia_1}(w'/D_C)^{ia_2}/(D_Rw).$$ Since the outer vectors were mark-independent, the initial symmetrizations do not alter this computation. After summing the shared labels, the pairing for pattern $\nu$ is, up to negligible error, $$\begin{align}
 \mathbb E_{\rm free}\sum_{\substack{w>0\\w'=w+kD_C>0}}
 &\frac{\psi(w/(ZD_C))}{w}
 (w/D_C)^{ia_1}(w'/D_C)^{ia_2}
 \overline{F(w)}G(w')\varepsilon(w)\varepsilon(w')\notag\\
 &\hspace{10mm}\cdot W_{\mathbf t}(w)W_{\mathbf t}(w')
                   \mathbb E_{\rm marks}K_\nu.
 \tag{4.19}
\end{align}$$ The final expectation means averaging over the unshared marked lists.

For completeness, all discarded restrictions have superpolynomial logarithmic saving. Conditional on $w,w'$, the free labels, and earlier shared draws, at most $O_J(L)$ prime values are excluded from a shared draw. Every atom is $O(\exp(-L^a))$. When bounding actual overlapping configurations, unshared physical marks still divide $w,w'$; ignoring damping changes their weight by at most $q_0^{-2Ms_P}=L^{O_J(1)}$. Equations (4.3) and (4.14), followed by Cauchy–Schwarz and fixed divisor moments on the two translated intervals, bound the remaining harmonic sum by $L^{O_J(1)}$. Shared overlaps thus cost $L^{O_J(1)}\exp(-L^a)$.

If an auxiliary free label $p'$ belongs to an unshared endpoint list, then $p'\mid D_C$ and hence $p'\mid w,w'$. Set $w=p'y$. The new shift $kD_C/p'$ is integral, the invariant cores are unchanged, and the harmonic measure supplies $1/p'$. Applying the same divisor moments at scale $ZD_C/p'$ bounds this contribution by $L^{O_J(1)}/p'$. There are $O_J(T)$ free slots and $p'\geq\exp(L^c)$. This bounds all free exclusions. After summing the fixed-power coefficient costs, the error in (4.19) is $O_A(L^{-A})$ for every fixed $A$. For the raw pattern, $D_C=1$, $\mathbf t=(\ell,\ldots,\ell)$, and (4.19) is exactly the left side of (4.7). It remains to bound the comparisons.

### Comparison multipliers and minor arcs

Expand the two kernels in a comparison using (4.12). Their four factors are bounded weights on $D_A,D_B$ and on the big unshared marks at the respective endpoints, times a total coefficient cost $L^{O(1)}$. The free products are restricted to logarithmic cells of width at most one. Let their lower endpoints be $U_1,U_2$, put $H'=U_1U_2$, and set $Y=ZH'$. Then $$\begin{equation}
\tag{4.20}
 U_1,U_2\geq\exp(L^c-O(1)),\quad
 H'\leq\exp(O(TL^d)),\quad Y=x^{1+o(1)}.
\end{equation}$$ The positions $w,w'$ in (4.19) are comparable to $Y$. Logarithmic Fourier separation of the smooth cutoff and phases therefore reduces it, with total cost $L^{O(1)}/Y$, to expressions $$\begin{equation}
\tag{4.21}
 \mathbb E\,b_1(D_A)b_2(D_B)
       \sum_w\overline{\mathcal U(w)}\mathcal V(w+kD_AD_B),
 \qquad |b_1|,|b_2|\leq1.
\end{equation}$$ An endpoint here is its core times $\varepsilon$, a power twist of fixed log-power frequency, $W_{\mathbf t}^{\mathbf b}$ with $\mathbf b$ depending only on big marks, and a smooth size cutoff at $Y$. Fixed divisor moments give $$\begin{equation}
\tag{4.22}
 \sum_w|\mathcal U(w)|^2+\sum_w|\mathcal V(w)|^2
 \ll YL^{C_5}.
\end{equation}$$ They also control the Fourier-separation tails to arbitrary accuracy.

The Fourier multiplier of (4.21) is $$\mathfrak m(\theta)=\mathbb E\,b_1(D_A)b_2(D_B)
                                     \mathrm{e}(k\theta D_AD_B),
 \qquad |\mathfrak m(\theta)|\leq1.$$ For a selected product $D$ with at most $m_0$ slots per group, unique factorization gives $$\begin{equation}
\tag{4.23}
 \mathbb P(D=n)=\frac1n\prod_g
       \frac{k_g!}{V_g^{k_g}\prod_{p\in\mathcal P_g}v_p(n)!}
 \leq\frac{L^{C_6}}n.
\end{equation}$$ Thus a bounded test collapsed onto product values $n\asymp U_i$ has squared coefficient norm $O(L^{C_6}/U_i)$.

We use the integer bilinear estimate of [4, Section 4, Lemma 4.2]: for coefficients on intervals of lengths $O(U),O(V)$, and $\alpha=u/r+\beta$ with $(u,r)=1$, $|\beta|\leq r^{-2}$, $$\left|\sum_{n,t}a_nb_t\mathrm{e}(\alpha nt)\right|
 \ll\|a\|_2\|b\|_2
       [U+(1+V/r)\{U+r\log(2r)\}]^{1/2}.$$ Arbitrary missing coefficients and translated containing intervals are allowed. Together with (4.23), this bounds $|\mathfrak m(\theta)|$ by $$\begin{equation}
\tag{4.24}
 L^{C_7}\left(\frac1{U_2}+\frac1r+
          \frac{\log(2r)}{U_1}+
          \frac{r\log(2r)}{H'}\right)^{1/2}
\end{equation}$$ whenever $r$ is a Dirichlet-approximation denominator for $k\theta$.

Choose such an approximation with maximum denominator $\lfloor H'/L^{C'}\rfloor$. If $r>L^{C'}$, all terms in (4.24) save an arbitrarily large fixed log power when $C'$ is sufficiently large, by (4.20). If $r\leq L^{C'}$, then $\theta$ belongs, after accounting for $|k|\leq L^C$, to an arc $$\begin{equation}
\tag{4.25}
 \left|\theta-\frac hr\right|_{\mathbb R/\mathbb Z}
 \leq\frac{L^{C_{\rm arc}}}{H'},
 \qquad 1\leq r\leq L^{C_{\rm arc}},\quad h\bmod r,
\end{equation}$$ for a sufficiently large fixed $C_{\rm arc}$. The letters $h,r$ in (4.25) denote the resulting rational center, rather than necessarily the original approximation. There are a fixed logarithmic power of arcs. Parseval and (4.22) dispose of their complement. On the arcs, Cauchy–Schwarz shows that it suffices to prove, for every fixed $A>0$ and every arc center $h/r$, $$\begin{equation}
\tag{4.26}
 \int_{|\beta|\leq1/H}
   |\widehat{\mathcal U}(h/r+\beta)|^2\,d\beta
 \ll_A YL^{-A},\qquad H=H'/L^{C_{\rm arc}}.
\end{equation}$$ Here $\widehat{\mathcal U}(\theta)=\sum_w\mathcal U(w)\mathrm{e}(\theta w)$, $H\to\infty$, and $H=x^{o(1)}$.

### The endpoint on a major arc

Choose a small group $g_s$ and a designated one of its $\ell\geq1$ marks. Because the mark weight $\mathbf b$ uses only big marks, removing this prime gives, unless a prime in $g_s$ divides $w$ twice, $$\begin{equation}
\tag{4.27}
 W_{\mathbf t}^{\mathbf b}(w)
 =\frac1{V_{g_s}}\sum_{\substack{p_s\mid w\\p_s\in\mathcal P_{g_s}}}
           W_{\mathbf t-\mathbf e_{g_s}}^{\mathbf b}(w/p_s).
\end{equation}$$ The equality includes damping: removing $p_s$ decreases both $\omega_P$ and $\sum_g t_g$ by one. On the excluded set both weights are bounded by fixed log powers. Since $w_*\mid w/p_s^2$ on a multiple of $p_s^2$, divisor moments show that the endpoint error has squared norm $$\begin{equation}
\tag{4.28}
 \ll YL^{C_8}\sum_{p_s\in\mathcal P_{g_s}}p_s^{-2}
 \ll YL^{C_8}\exp(-L^a).
\end{equation}$$ Its Fourier energy is negligible by Parseval.

The factors $m,p$ in (4.5) contain no group prime. After (4.27), write $w=mp_sp r'$. Complete multiplicativity gives $\varepsilon(w)=\varepsilon(p_s)\varepsilon(r')$; the remaining marked weight and $c_{r'_*}$ are functions of $r'$ alone. They have a fixed log-power bound, so may be absorbed into one residual coefficient.

To remove the rational center, fix $d'=(r',r)$ and put $q=r/d'$. The first three factors $m,p_s,p$ are units modulo $r$ for all large $x$, and $r'/d'$ is a unit modulo $q$. On units the exact character expansion is $$\begin{equation}
\tag{4.29}
 \mathrm{e}(hv/q)=\sum_{\chi\bmod q}c_{h,q}(\chi)\chi(v),\qquad
 c_{h,q}(\chi)=\frac1{\varphi(q)}
       \sum_{v\bmod q}^{*}\mathrm{e}(hv/q)\overline{\chi(v)},
 \quad |c_{h,q}(\chi)|\leq1.
\end{equation}$$ Apply this with $v=mp_sp(r'/d')$. The gcd restriction and $\chi(r'/d')$ go into the residual coefficient. Summing over $d'$ and all characters costs a fixed power of $L$ and includes the principal and imprimitive characters. The product of the new character on $m$ with $\chi_0$ is a character of fixed log-power modulus. It is therefore enough to bound the energy at zero of $$\begin{equation}
\tag{4.30}
 a_w=\psi_1(w/Y)w^{iv_1}
       \sum_{mp_sp r'=w}\alpha_m\chi_m(m)m^{i\sigma_0}
       b_s(p_s)\mathbf{1}_{p\in I_p,\ p\ {\rm prime}}
       \chi_p(p)p^{i\sigma_1}d_{r'}.
\end{equation}$$ Here $p_s\in\mathcal P_{g_s}$, $|b_s|\ll1$, $|d_{r'}|\leq L^{C_9}$, and all characters, frequencies and smooth-cutoff derivatives have fixed log-power bounds. The sign on $p_s$ and $1/V_{g_s}$ are included in $b_s$. In particular, $$\begin{equation}
\tag{4.31}
 \sum_w|a_w|^2\ll YL^{C_{10}}.
\end{equation}$$

### Local Fourier energy and Mellin polynomials

We include the scale conversion from [4, Section 5, equation (5.16)] with its proof, as its normalization is useful here.

**Lemma 4.4** (Local Mellin energy). *Let $a_w$ be supported on $w\asymp Y$, where $Y=x^{1+o(1)}$, and let $H=x^{o(1)}$ tend to infinity. For every fixed $j\geq1$, $$\begin{equation}
\tag{4.32}
 \int_{|\beta|\leq1/H}|\widehat a(\beta)|^2\,d\beta
 \ll_j \frac1Y\int_{\mathbb R}(1+H|t|/Y)^{-j}
           \left|\sum_w a_ww^{it}\right|^2dt
       +\left(\frac HY\right)^2\sum_w|a_w|^2.
\end{equation}$$*

*Proof.* Take a smooth bump $K$ of integral one, supported sufficiently near zero that its Fourier transform, with convention $\widehat K(\xi)=\int K(u)\mathrm{e}(-\xi u)\,du$, has modulus at least $1/2$ on $[-1,1]$. Plancherel gives $$\int_{|\beta|\leq1/H}|\widehat a(\beta)|^2\,d\beta
 \ll H^{-2}\int_{\mathbb R}
          \left|\sum_w a_wK((w-v)/H)\right|^2dv.$$ Only $v\asymp Y$ contributes. Keep this restriction when replacing the kernel by $K(v\log(w/v)/H)$. On the union of their supports, $|w-v|\ll H$, and their arguments differ by $O(H/Y)$. Cauchy–Schwarz over the $O(H)$ possible integers $w$, followed by integration over the $O(H)$ centers for each $w$, bounds the normalized squared error by $(H/Y)^2\sum_w|a_w|^2$.

Put $h_0=H/Y$, $v=Y\exp(u)$, and $P_a(t)=\sum_w a_ww^{it}$. Fourier inversion for the new kernel gives $$\sum_w a_wK(v\log(w/v)/H)
 =\frac{h_0}{2\pi}\int_{\mathbb R}
   e^{-u}\widehat K(h_0e^{-u}t/(2\pi))v^{-it}P_a(t)\,dt.$$ Insert a fixed smooth compact cutoff in $u$ equal to one on the required range. The Fourier transform in $u$ of the resulting amplitude $e^{-u}\widehat K(h_0e^{-u}t/(2\pi))$ is bounded by $$C_j(1+|s|)^{-2}(1+h_0|t|)^{-j},$$ by two integrations by parts and the Schwartz bounds for $\widehat K$. Expand that amplitude in its $u$-Fourier transform, apply Minkowski in $s$ and Plancherel in $u$, and use $dv\ll Y\,du$. The normalization is $H^{-2}Yh_0^2=Y^{-1}$. Increasing the decay order if necessary proves (4.32). ◻

Apply this lemma to (4.30). The error term is $O_A(YL^{-A})$ for every fixed $A$, by (4.31). Dirichlet-polynomial mean squares imply, on every dyadic time scale $R\geq1$, $$\begin{equation}
\tag{4.33}
 Y^{-2}\int_{R\leq|t|\leq2R}|P_a(t)|^2dt
 \ll(1+R/Y)L^{C_{11}}.
\end{equation}$$ Consequently, with $T_0=LY/H$, the part $|t|>T_0$ of the first term in (4.32) is at most $$YL^{C_{11}}\sum_{r\geq0}
       (2^rL)^{-j}\left(1+\frac{2^rL}{H}\right)
 \ll_j YL^{C_{11}-j}(1+L/H).$$ It is $O_A(YL^{-A})$ on taking $j$ large enough.

Split the four variables in (4.30) into dyads. There are $O(L^4)$ relevant boxes, and their product scales are comparable to $Y$. Write $$\frac{P_a(t)}Y
 =\sum_w\frac1w\big((w/Y)\psi_1(w/Y)\big)w^{i(t+v_1)}
        \sum_{mp_sp r'=w}(\text{the four coefficients}).$$ Fourier-separate the parenthesized function in $\log(w/Y)$. On every box the fourfold collapsed reciprocal coefficients have squared norm $\ll L^{C_{12}}/Y$, by a fixed divisor moment. Hence centered mean squares give a bound $L^{C_{13}}$ for the integral of their squared polynomial on any translate of $[-T_0,T_0]$. Minkowski therefore bounds a separating-frequency tail by a fixed log power times the square of the $L^1$ mass of that tail. Integration by parts makes it arbitrarily small at a fixed log-power cutoff. This proves the claimed separation also for unbounded tail frequencies. Retained shifts enlarge the time interval to at most $[-2T_0,2T_0]$, since $Y/H$ exceeds every fixed log power.

After absorbing these shifts into $t$ and the fixed frequencies, it suffices to prove, for arbitrary fixed $A'>0$, $$\begin{equation}
\tag{4.34}
 \int_{|t|\leq2LY/H}|P_s(t)P_l(t)\mathcal R(t)|^2dt
 \ll L^{-A'},
\end{equation}$$ where $$\begin{align*}
 P_s(t)&=\sum_{p_s\asymp P}b_s(p_s)p_s^{-1+it},\\
 P_l(t)&=\sum_{\substack{p\asymp P',\ p\in I_p\\p\ {\rm prime}}}
                      \chi_p(p)p^{-1+i\sigma_1+it},\\
 \mathcal R(t)&=
  \left(\sum_{m\asymp M_1}\alpha_m\chi_m(m)m^{-1+i\sigma_0+it}\right)
  \left(\sum_{r'\asymp R_1}d_{r'}(r')^{-1+it}\right).
\end{align*}$$ The small primes retain their group restriction, and each dyad is intersected with its original interval. Their sizes satisfy $$\begin{equation}
\tag{4.35}
 \tfrac12\exp(L^a)\leq P\leq\exp(L^b),\qquad
 x^\tau/2\leq P'\leq x^\eta,\qquad PM_1P'R_1\asymp Y.
\end{equation}$$ For any subproduct of these four polynomials, collapsed as $\sum_{n\asymp U}c_nn^{it}$, a fixed divisor moment gives $$\begin{equation}
\tag{4.36}
 \sum_n|c_n|^2\ll L^{C_{14}}/U.
\end{equation}$$ Only four convolution factors are involved: all remaining marked weights have already entered the single bounded coefficient $d_{r'}$.

### Exceptional times and completion of the proof

First consider $|P_s(t)|\leq L^{-A_s}$. The polynomial $P_l\mathcal R$ has size $Y/P$, and $$\frac{Y/P}{2LY/H}=\frac{H}{2LP}\longrightarrow\infty$$ by $b<c$ and (4.20). Its mean square on the entire time interval is $L^{O(1)}$, by (4.36). Choose $A_s$ sufficiently large to bound this part of (4.34).

Let $\mathcal J$ be the integer unit intervals meeting $\{|t|\leq2LY/H:|P_s(t)|>L^{-A_s}\}$. We establish $$\begin{equation}
\tag{4.37}
 |\mathcal J|\leq
 \exp\big(O(L^b+L^{1-a}\log L)\big)=Y^{o(1)}.
\end{equation}$$ Put $j_0=\lfloor\log Y/\log(2P)\rfloor$. Unique factorization shows directly that the squared coefficient norm of $P_s^{j_0}$ is at most $$\begin{equation}
\tag{4.38}
 j_0!\left(\sum_{p_s\asymp P}|b_s(p_s)|^2p_s^{-2}\right)^{j_0}
 \leq j_0!(C/P)^{j_0}.
\end{equation}$$ Indeed for each multiset of $j_0$ primes, one of the two multinomial coefficients in its squared coefficient is at most $j_0!$. This argument remains valid when $j_0$ grows; no growing-order divisor-moment estimate is being used.

Select a point with $|P_s|>L^{-A_s}$ in each occupied interval. Split the intervals into three classes according to their integer index modulo three, so the chosen points in a class are separated by at least one. The indices of $P_s^{j_0}$ are at most $Y$, and the time range is contained in $[-Y,Y]$ for large $x$. The separated-point mean-square inequality and (4.38) give $$|\mathcal J|\ll YL^{C_{15}}j_0!
                         (CL^{2A_s}/P)^{j_0}.$$ Since $YP^{-j_0}\leq2P\,2^{j_0}$, $\log P\leq L^b$, and $j_0=O(L^{1-a})$, this proves (4.37).

We next prove the sparse mean-square estimate $$\begin{equation}
\tag{4.39}
 \sum_{I\in\mathcal J}\sup_{t\in I}|\mathcal R(t)|^2
 \ll L^{C_{16}}.
\end{equation}$$ Collapse $\mathcal R(t)=\sum_{n\asymp U}c_nn^{it}$, where $$U=M_1R_1\asymp Y/(PP')\geq Y^{1-\eta-o(1)}>Y^{0.6},
 \qquad \sum_n|c_n|^2\ll L^{C_{14}}/U.$$ Choose a maximizing point on each closed unit interval and again split into three separated classes. The Gram matrix of the evaluation vectors $(n^{it_i})_{n\asymp U}$ has entries $\sum_{n\asymp U}n^{i(t_i-t_j)}$. For $1\leq|\Delta|\leq c_*U$, with a sufficiently small fixed $c_*>0$, the derivative of $\Delta\log n/(2\pi)$ is monotone, has magnitude comparable to $|\Delta|/U$, and is bounded away from nonzero integers. The first derivative test of Proposition 2.3 gives $O(U/|\Delta|)$. For $c_*U\leq|\Delta|\ll Y$, the second derivative test gives $$O\big(\sqrt{|\Delta|}+U/\sqrt{|\Delta|}\big)=O(Y^{1/2}).$$ The diagonal entry is $O(U)$. Thus all entries are bounded by $$O\left(\frac{U}{1+|t_i-t_j|}+Y^{1/2}\right).$$ Separation and (4.37) bound an absolute row sum by $$O\big(U\log Y+|\mathcal J|Y^{1/2}\big)=O(U\log Y).$$ The operator norm is bounded by this row sum. Multiplying by $\sum|c_n|^2$ proves (4.39).

On the exceptional intervals, $|P_s(t)|\ll1$. Prescribe a sufficiently large saving for $P_l$, and apply Lemma 3.1. Choose $B_1$ larger than its frequency threshold and the fixed exponent bounding $|\sigma_1|$. For $|t|\geq L^{B_1}$ in the present range, the lemma applies to $t+\sigma_1$: it is above the required logarithmic threshold and $$|t+\sigma_1|\leq2LY/H+|\sigma_1|<x^2.$$ It bounds $P_l$ by an arbitrarily large negative log power. Equation (4.39) then proves the required integral bound for these times.

For $|t|\leq L^{B_1}$, use (4.6) on the $m$-polynomial in $\mathcal R$. Its dyad lies below $x^2$; the character modulus and shifted frequency are fixed log powers. All other factors have fixed log-power absolute bounds. Choosing $B$ last, larger than these modulus and frequency exponents and with $2B>B_1+C_{17}+A'$, makes this last integral $O(L^{-A'})$. This proves (4.34), hence (4.26).

The major-arc estimate, the minor-arc estimate, and Parseval now bound every comparison (4.19) by an arbitrarily large negative log power, after paying the fixed number of arcs, kernel expansions, and Fourier integrals. Their sum has the same bound. Subtracting it from the controlled residual pairing leaves the raw pattern, which is (4.7). This completes the proof of Theorem 4.1.

*Remark 4.5* (Order of choices). The endpoint norm exponent and the original Fourier cutoff exponent are fixed from the input data. Then choose the physical accuracy $E$, ideal accuracy $E_{\rm id}$, ideal frequency range $C_4$, all kernel parameters, and finally a sufficiently large fixed $J$. Once this family is fixed, choose the minor-arc and major-arc accuracies, the prime-polynomial accuracy and threshold $B_1$, and last the discrepancy exponent $B$. Any stronger Fourier-tail saving required by these choices is obtained by more integrations by parts at the already fixed cutoff exponent. No kernel parameter or frequency range has to be changed after choosing $J$.

## Candidate weights and their mass

The ordinary bands $Q_j$ give an even number of prime slots and allow the candidate to be split near a prescribed size. The smaller groups $\mathcal P_g$ supply the graph marks and the odd parity restriction. Separating the two families keeps these roles independent.

We now fix the prime groups used in the remainder of the proof. All constants in this section depend only on the following fixed geometry and on the function $\Psi$. In particular, they are independent of the parameters $\kappa,b_1$ and of the proxy precision chosen later.

Choose a fixed even integer $r_0$ sufficiently large that $$\frac{(r_0-1)c_1}{2}\ge c_2+1,
 \qquad c_2s'<\frac14,$$ where $$\begin{equation}
\tag{5.1}
 c_1=1,\quad c_2=\frac65,\quad c_3=\frac32,\quad c_4=\frac95,
 \qquad s'=\frac1{r_0(c_1+c_2)},\qquad s_j=s'2^{-j}L.
\end{equation}$$ Let $j_x$ be the largest nonnegative integer with $c_1s_{j_x}\ge20T$, and let $Q_j$ consist of the primes with $c_1s_j\le\log p\le c_2s_j$, for $0\le j\le j_x$. For each $j$ such that $[c_3s_j,c_4s_j]$ is contained in either $[L^{1/10},L^{1/5}]$ or $[L^{3/10},L^{2/5}]$, take the primes whose logarithms belong to $[c_3s_j,c_4s_j]$ as one group $\mathcal P_g$. As before, $\mathcal P$ is the union of these groups and $n_*$ is the part of $n$ supported outside $\mathcal P$.

These intervals are mutually disjoint, including between the $Q_j$ and the $\mathcal P_g$: indeed $c_2<c_3<c_4<2c_1$ and $c_4/2<c_1$. The number of groups in a logarithmic range $[L^a,L^b]$ is $(b-a)T/\log2+O(1)$. The prime number theorem and partial summation give, uniformly in the indices, $$\begin{equation}
\tag{5.2}
 V_{Q,j}:=\sum_{p\in Q_j}\frac1p=\log\frac65+o(1),
 \qquad
 V_g:=\sum_{p\in\mathcal P_g}\frac1p=\log\frac65+o(1).
\end{equation}$$ The uniformity follows because the smallest logarithmic endpoint tends to infinity. Thus the group hypotheses of Theorem 4.1 hold with $(a,b,c,d)=(1/10,1/5,3/10,2/5)$. Every prime in our construction is at least $L^{20}$ once $x$ is sufficiently large. The classical prime estimates used here and below are those in [4, Section “Notation and preliminary estimates”].

Take $q_0=1/2$ and $\ell=1$ in the marked weights, so explicitly $$W_1(n)=\prod_g \frac{q_0^{\omega_g(n)-1}\omega_g(n)}{V_g}.$$ For a positive integer $v$, let $a(v)$ be the number of ordered prime tuples with product $v$, with $r_0$ slots in every $Q_j$, divided by $(r_0!)^{j_x+1}$. Repetitions are allowed. Fix a nonnegative smooth function $\Psi$ supported in $[1,2]$ and positive on a nonempty open subinterval of $(1,2)$. Define $$\begin{equation}
\tag{5.3}
 \begin{gathered}
 \mathcal E(u)=(-1)^{\sum_{p\in\mathcal P}v_p(u)},\qquad
 A_0(u)=W_1(u)a(u_*),\\
 A(u)=A_0(u)\frac{1-\mathcal E(u)}2,
 \qquad X_A=\sum_u A(u)\Psi(u/x).
 \end{gathered}
\end{equation}$$ Here $v_p(u)$ denotes the exponent of $p$ in $u$. If $e_p$ are the exponents of an integer in the support of $a$, then $$a(v)=\prod_{j=0}^{j_x}\prod_{p\in Q_j}\frac1{e_p!},
 \qquad \sum_{p\in Q_j}e_p=r_0.$$ In particular $0\le a(v)\le1$. The function $k\mapsto kq_0^{k-1}$ is bounded on the nonnegative integers, and there are $O(T)$ groups with $V_g$ bounded away from zero. Consequently $$\begin{equation}
\tag{5.4}
 0\le A(u)\le A_0(u)\le L^{C_0}
\end{equation}$$ for a fixed $C_0$. The ordinary part of a supported integer has exactly $r_0(j_x+1)$ prime factors counted with multiplicity. This number is even, whereas the parity projection in $A$ selects an odd number of group-prime factors. Thus $$\begin{equation}
\tag{5.5}
 A(u)>0\quad\Longrightarrow\quad
 \Omega(u)\ \hbox{is odd},\qquad \Omega(2u)\ \hbox{is even}.
\end{equation}$$

### Harmonic measures and the group tail

Set $$\begin{equation}
\tag{5.6}
 H_Q=\sum_v\frac{a(v)}v
     =\prod_{j=0}^{j_x}\frac{V_{Q,j}^{r_0}}{r_0!},
 \qquad
 H_P=\sum_{r:\,r_*=1}\frac{W_1(r)}r.
\end{equation}$$ Since $j_x+1=O(T)$, Equation (5.2) gives $L^{-C}\le H_Q\le L^C$ for a fixed $C$. For one group introduce $$Z_g(q)=\prod_{p\in\mathcal P_g}\left(1+\frac q{p-1}\right).$$ The factor of $H_P$ associated with this group is $$\begin{equation}
\tag{5.7}
 H_g=\frac{Z_g'(q_0)}{V_g}
 =\frac{Z_g(q_0)}{V_g}
       \sum_{p\in\mathcal P_g}\frac1{p-1+q_0}.
\end{equation}$$ This follows by expanding the Euler product: each occurring prime has harmonic mass $\sum_{k\ge1}p^{-k}=1/(p-1)$, and differentiation chooses one of the distinct prime divisors as its mark. Because $q_0\le1$, the sum on the right of Equation (5.7) is at least $V_g$. The same sum is bounded above, and $Z_g(q_0)$ is bounded above, by constants uniform in $g$. Hence $$\begin{equation}
\tag{5.8}
 1\le Z_g(q_0)\le H_g\le C,
 \qquad
 H_P=\prod_gH_g,\qquad 1\le H_P\le L^C,
 \qquad
 \prod_{p\in\mathcal P}\left(1+\frac{q_0}{p-1}\right)\le H_P.
\end{equation}$$

Normalize $a(v)/v$ and $W_1(r)/r$ by $H_Q$ and $H_P$, respectively, and draw the two parts independently. The $Q$-measure can equivalently be sampled by drawing every ordered slot independently with law $1/(pV_{Q,j})$ in band $j$. The group measure is a product of the normalized measures belonging to Equation (5.7). Write $V$ and $R$ for these two random integers and $U=VR$.

In one group the unnormalized harmonic mass of total multiplicity one is exactly $V_g/V_g=1$. The contribution to multiplicity two from two distinct primes is $$\frac{2q_0}{V_g}\sum_{p<q\in\mathcal P_g}\frac1{pq}
 =\frac{q_0}{V_g}
     \left(V_g^2-\sum_{p\in\mathcal P_g}\frac1{p^2}\right).$$ It is bounded below by a positive constant for sufficiently large $x$. Since $H_g\le C$, each group therefore has both even and odd total multiplicity with probability at least a fixed $\delta_0>0$. Conditioning on all groups except one proves $$\begin{equation}
\tag{5.9}
 \mathbb P\bigl(\mathcal E(R)=-1\bigr)\ge\delta_0.
\end{equation}$$ The bound is independent of the number of groups.

**Lemma 5.1** (Tail of the group part). *There is a fixed $C$ such that, for each fixed $\sigma>0$, $$\sum_{\substack{r>x^\sigma\\r_*=1}}\frac{W_1(r)}r
 \le L^C\exp(-\sigma L^{3/5})$$ for all sufficiently large $x$.*

*Proof.* Put $\delta=L^{-2/5}$. The mass in one group after inserting $r^\delta$ is $$\prod_{p\in\mathcal P_g}
      \left(1+\frac{q_0}{p^{1-\delta}-1}\right)
 \frac1{V_g}\sum_{p\in\mathcal P_g}
      \frac1{p^{1-\delta}-1+q_0}.$$ Every group prime satisfies $p^\delta\le e$, so this expression is bounded above by a fixed constant, using Equation (5.2). Multiplying over $O(T)$ groups gives $\sum_{r_* =1}W_1(r)r^{-1+\delta}\le L^C$. For $r>x^\sigma$, the extra factor is at least $x^{\sigma\delta}=\exp(\sigma L^{3/5})$, proving the assertion. ◻

### Localization at the target size

**Lemma 5.2** (Total candidate mass). *There is a fixed $C_A$ such that $$X_A\asymp\frac{x}{L}H_QH_P,
 \qquad X_A\gg xL^{-C_A}.$$ The implied constants and $C_A$ depend only on the fixed geometry and on $\Psi$.*

*Proof.* The exact probability identity is $$\begin{equation}
\tag{5.10}
 X_A=H_QH_P\,
 \mathbb E\left[U\Psi(U/x)\,
                   \mathbf{1}_{\{\mathcal E(R)=-1\}}\right].
\end{equation}$$ Leave one ordered slot in $Q_0$ free and condition on every other variable. On the support of $\Psi(U/x)$, its logarithm must lie in an interval of length $\log2$. Uniformly in the location of such an interval, its normalized harmonic prime mass in $Q_0$ is $O(1/L)$. For example, after intersecting with $Q_0$, the interval is contained in $[y,2y]$ with $\log y\asymp L$, and the prime number theorem bounds the reciprocal prime sum there by $O(1/L)$. Since $U\le2x$ on the effective support, this proves the upper bound.

For the lower bound let $$m_j=\frac{c_1+c_2}{2}s_j,
 \qquad \Delta=(c_2-c_1)s'L.$$ The infinite midpoint sum satisfies $r_0\sum_{j\ge0}m_j=L$, by the choice of $s'$. Choose a fixed integer $J_0$ such that $$\sum_{j>J_0}r_0c_2s_j<\Delta/24.$$ For sufficiently large $x$ we have $j_x>J_0$. Restrict all slots in $0\le j\le J_0$, except the free slot in $Q_0$, to fixed small neighborhoods of their respective midpoints, choosing the widths so that their total logarithmic deviation is less than $\Delta/24$. There are only finitely many restrictions, each with harmonic probability bounded below by a positive constant by the prime number theorem. Their joint probability is therefore bounded below.

Independently, require $\mathcal E(R)=-1$ and $\log R\le\Delta/12$. Equations (5.8) and (5.9), together with Lemma 5.1 applied to the fixed positive number $\Delta/(12L)$, show that these two requirements have probability at least $\delta_0/2$ for sufficiently large $x$. No restrictions are needed on the remaining $Q$-slots. Their total logarithm and the infinite midpoint sum for their bands both lie between zero and $\Delta/24$. Consequently, if $B$ is the logarithm of the product of all variables except the free prime, then on the event just described $$\left|B-(L-m_0)\right|<\Delta/6.$$

Choose $1<\alpha<\beta<2$ with $\Psi(t)\ge c_\Psi>0$ throughout $[\alpha,\beta]$. For the free prime it is enough to require $$\log p\in[L+\log\alpha-B,\ L+\log\beta-B].$$ This interval has the fixed positive length $\log(\beta/\alpha)$. Its endpoints lie strictly inside $[c_1s_0,c_2s_0]$ with distance $\gg\Delta$ from the boundary, since $m_0$ is its midpoint and $\Delta$ its full width. The prime number theorem and partial summation give harmonic mass $\gg1/L$ for the interval, uniformly in the conditioned variables. On it $U\ge\alpha x$ and $\Psi(U/x)\ge c_\Psi$. Equation (5.10) now gives the lower bound. Finally $H_Q\ge L^{-C}$ and $H_P\ge1$ imply the stated fixed-power lower bound for $X_A$. ◻

### Squarefree predecessors

**Lemma 5.3** (Squarefree loss). *The mass of nonsquarefree predecessors satisfies $$\sum_{\substack{u\ge1\\2u\ {\rm not\ squarefree}}}
       A(u)\Psi(u/x)=o(X_A/L).$$*

*Proof.* In one $Q$-band the probability that two given slots coincide is $$\sum_{p\in Q_j}\frac1{p^2V_{Q,j}^2}
 \le\frac{L^{-20}}{V_{Q,j}}\ll L^{-20}.$$ The number of pairs of slots within bands is $O(T)$, so the probability of any repeated $Q$-prime is $O(TL^{-20})$.

For completeness, fix $p\in\mathcal P_g$ and write $Z_{g,p}(q)=\prod_{q'\in\mathcal P_g,\ q'\ne p} (1+q/(q'-1))$. The unnormalized mass of integers in this group that are divisible by $p$ is $$\frac{Z_{g,p}(q_0)+q_0Z_{g,p}'(q_0)}{V_g(p-1)}\ll\frac1p.$$ The bound follows from the uniform group harmonic masses; division by $H_g\ge1$ preserves it. Conditional on the set of distinct prime divisors, the exponent of an occurring prime has distribution proportional to $p^{-k}$, $k\ge1$. The conditional probability that its exponent is at least two is therefore exactly $1/p$. Thus the probability of a square from the group part is $$\ll\sum_{p\in\mathcal P}\frac1{p^2}
 \le e^{-L^{1/10}}\sum_gV_g
 \ll T e^{-L^{1/10}}.$$ All bands and groups are disjoint, and all their primes are odd. It follows that $2U$ is not squarefree with probability $O(TL^{-20})$ under the unrestricted harmonic measure. Using Equation (5.10) and dropping parity and size localization gives the upper bound $$2x\|\Psi\|_\infty H_QH_P\,O(TL^{-20})
   \ll xH_QH_PT L^{-20}.$$ By Lemma 5.2, its ratio to $X_A/L$ is $O(TL^{-18})=o(1)$, as required. ◻

## Bilinear distribution

We retain the groups, ordinary prime bands, and weights of the preceding section. In particular, every ordinary slot contains a prime, there are $r_0$ labelled slots in each $Q_j$, and $$s_j=s'2^{-j}L,\qquad 20T\le s_{j_x}<40T,\qquad
 \frac{(r_0-1)c_1}{2}\ge c_2+1.$$ The smooth allocation and change of variables below follow the Type II method of [4]. We give the argument for the present all-prime weight and its parity twist, using Theorem 4.1 for the resulting correlations.

**Theorem 6.1** (Type II distribution). *Fix $D_*,b_*,C>0$. Let $U,V$ be dyadic scales such that $$UV\asymp x,\qquad x^{b_*}\le U,V\le x^{1-b_*},$$ and let $K\subset[U,2U)$ and $J\subset[V,2V)$ be intervals. Suppose $|\alpha_m|,|\beta_n|\le L^C$ and $\alpha_m=0$ unless $P^-(m)>W$. There is a fixed $B$, depending only on these fixed data and on the fixed weight and cutoff data, for which the following holds. Assume that the sequence $\alpha_m\mathbf{1}_{m\in K}$ satisfies (4.6); explicitly, assume $$\begin{equation}
\tag{6.1}
 \left|\sum_{m\in I}\alpha_m\mathbf{1}_{m\in K}
                    \chi(m)m^{-1+it}\right|\le L^{-B}
 \quad\left(
 \begin{array}{c}
 I\subset[1,x^2]\text{ an interval},\\
 \operatorname{mod}(\chi)\le L^B,\quad |t|\le L^B
 \end{array}\right).
\end{equation}$$ Then $$\begin{equation}
\tag{6.2}
 \sum_{\substack{m\in K,\ n\in J,\ u\ge1\\mn=2u+1}}
       \alpha_m\beta_n A(u)\Psi(u/x)
       \ll xL^{-D_*}.
\end{equation}$$ The estimate is uniform in the intervals and coefficient sequences satisfying these assumptions. No discrepancy or smoothness assumption is imposed on $\beta$.*

*Proof.* Extend the actually restricted sequences by zero, and write them again as $\alpha$ and $\beta$. Thus $\alpha$ in every subsequent convolution is the sequence appearing in (6.1). By $A=A_0(1-\mathcal E)/2$, it suffices to prove the assertion with $A_0(u)\varepsilon(u)$, for each of the two choices $$\varepsilon=1\quad\hbox{or}\quad
                    \varepsilon=\mathcal E.$$ The choice will be the same at the two endpoints of each correlation.

##### Removing a large group-prime part.

Choose a fixed band index $j_{**}$ so large that $$\begin{equation}
\tag{6.3}
 \tau=c_1s'2^{-j_{**}}>0,\qquad
 \eta=c_2s'2^{-j_{**}}<\min(b_*/4,1/4).
\end{equation}$$ For sufficiently large $x$, this band is present. Designate one of its labelled slots, whose prime therefore lies in $[x^\tau,x^\eta]$. This merely names an existing slot in the weight.

Put $u_P=u/u_*$. We first discard $u_P>x^{b_*/4}$. For $u\asymp x$, the part of $2u+1$ supported on primes exceeding $W$ has at most $O(L/\log W)=O(\sqrt L)$ prime factors with multiplicity. Its number of divisors is consequently at most $\exp(O(\sqrt L))$, since $a+1\le2^a$ for $a\ge1$. This bounds the possible rough divisors $m$. The tail bound in Lemma 5.1, with $d=2/5$, gives $$\begin{align}
 &\sum_{\substack{mn=2u+1,\ u\asymp x\\u_P>x^{b_*/4}}}
          |\alpha_m\beta_n|A_0(u)|\Psi(u/x)|\notag\\
 &\qquad\ll
 xL^{O(1)}\exp(O(\sqrt L))
   \left(\sum_v\frac{a(v)}v\right)
   \sum_{\substack{r>x^{b_*/4}\\r_*=1}}\frac{W_1(r)}r
 \ll xL^{O(1)}
       \exp\left(-\frac{b_*}{4}L^{1-d}+O(\sqrt L)\right).
 \tag{6.4}
\end{align}$$ To obtain the first inequality, write $u=vr$, use $vr\asymp x$ to bound $1\ll x/(vr)$, and then drop the product restriction. The harmonic ordinary-slot mass is $H_Q=L^{O(1)}$. Since $1-d>1/2$, (6.4) is $O_H(xL^{-H})$ for every fixed $H$. The same conclusion will hold whenever we reinstate these discarded tuples with a multiplier of absolute value at most one.

##### A smooth allocation with bounded residual.

Set $$\begin{equation}
\tag{6.5}
                            E=UL^{-K_0},
\end{equation}$$ where the fixed positive constant $K_0$ will be chosen below. Put the entire group-prime part and the designated prime into $h$. Process all remaining ordinary slots by increasing band index, in a fixed order within each band, assigning each slot either to $e$ or to $h$. Write these slots as $p_1,\ldots,p_N$, with band indices $j(i)$; here $N=r_0(j_x+1)-1=O(T)$.

Fix a smooth function $\gamma:\mathbb R\to[0,1]$ equal to zero on $(-\infty,0]$ and to one on $[1,\infty)$. At slot $i$, with residual target $R_i$, assign the prime to $e$ with weight $$\gamma\left(\frac{R_i-\log p_i}{s_{j(i)}}\right)$$ and to $h$ with the complementary weight. Start with $R_1=\log E$, and subtract $\log p_i$ from the residual precisely when the slot is assigned to $e$.

For a tuple surviving the preceding deletion, the product withheld from allocation is at most $x^{b_*/2}$. Since $u\asymp x$ and $U\le x^{1-b_*}$, its available logarithms satisfy, for large $x$, $$0<\log E\le\sum_{i=1}^N\log p_i.$$ Every branch of positive weight has the invariant $$\begin{equation}
\tag{6.6}
 0\le R_i\le\sum_{t=i}^N\log p_t+(c_2+1)s_{j_x}
                    \qquad(1\le i\le N+1).
\end{equation}$$ Indeed, taking a slot requires $R_i>\log p_i$, so preserves both nonnegativity and the upper bound after subtracting that logarithm. Skipping a slot in band $j$ requires $$R_i<\log p_i+s_j\le(c_2+1)s_j.$$ If $j<j_x$, the next band has at least $r_0-1$ available slots and therefore total logarithm at least $(r_0-1)c_1s_j/2\ge(c_2+1)s_j$. These slots are all still unprocessed. If $j=j_x$, the error term in (6.6) supplies the bound directly. This proves the invariant by induction, including the terminal step.

The geometric sum of all unprocessed band scales is $O(s_{j(i)})$. Thus (6.6) also places every argument $(R_i-\log p_i)/s_{j(i)}$ in one fixed compact interval, independently of $K_0$. At termination, $$0\le\log(E/e)=R_{N+1}\le(c_2+1)s_{j_x}.$$ Choose once and for all $C_s>40(c_2+1)$. Every surviving branch has $$\begin{equation}
\tag{6.7}
                         EL^{-C_s}\le e\le E.
\end{equation}$$ This choice of $C_s$ is independent of $K_0$.

Choose a fixed smooth $\rho:\mathbb R\to[0,1]$ of compact support which equals one throughout the possible argument interval, and put $$f_1=\rho\gamma,\qquad f_0=\rho(1-\gamma).$$ The allocation is unchanged on the retained tuples. On any tuple the sum of its full branch weights is at most one, since $f_0+f_1=\rho\le1$ at every node of the choice tree. We may consequently impose (6.7) and reinstate all discarded tuples, with the same negligible error (6.4).

##### Separation and its uniform cost.

Use the Fourier convention $$\widehat f(\xi)=\int_{\mathbb R}f(t)e^{-i\xi t}\,dt,
 \qquad f(t)=\int_{\mathbb R}\widehat f(\xi)e^{i\xi t}
                                    \frac{d\xi}{2\pi},$$ and set $$C_F=\max\left(1,
       \int|\widehat f_0(\xi)|\frac{d\xi}{2\pi},
       \int|\widehat f_1(\xi)|\frac{d\xi}{2\pi}\right).$$ For a fixed branch $\delta=(\delta_1,\ldots,\delta_N)\in\{0,1\}^N$, Fourier inversion of its $N$ transitions has total variation at most $C_F^N$. Summing over the branches costs at most $$\begin{equation}
\tag{6.8}
                         (2C_F)^N\le L^{C_f}
\end{equation}$$ for a fixed exponent, increased below to include the fixed cutoff $\Psi$. In particular this exponent is independent of $K_0$. Truncating each transition variable at $|\xi_i|\le L$ has total error at most $$\begin{equation}
\tag{6.9}
                  2^N N C_M C_F^{N-1}L^{-M}
\end{equation}$$ for any fixed $M$, by the union bound on the complementary integration regions and the rapid decay of a single Fourier factor. The constant $C_M$ occurs only once in each term of this estimate. Increasing $M$ therefore does not increase the exponent arising from $C_F^N$.

To see the separated phases explicitly, use $R_i=\log E-\sum_{t<i}\delta_t\log p_t$. The product of the Fourier phases is $$\begin{equation}
\tag{6.10}
 \exp\left(i\log E\sum_{i=1}^N\frac{\xi_i}{s_{j(i)}}\right)
       \prod_{t=1}^N p_t^{i\sigma_t},\qquad
 \sigma_t=-\frac{\xi_t}{s_{j(t)}}
           -\delta_t\sum_{i>t}\frac{\xi_i}{s_{j(i)}}.
\end{equation}$$ The dependence on $E$ is entirely in the scalar of modulus one. Since $\sum_i s_{j(i)}^{-1}=O(T^{-1})$, the retained frequencies satisfy $|\sigma_t|=O(L/T)$. Fourier inversion of the fixed smooth function $t\mapsto\Psi(e^t)$ likewise separates $\Psi(eh/x)$, with bounded integral norm; truncation at a fixed power of $L$ has arbitrary logarithmic accuracy. Its contribution is a factor $h^{i\varrho}$, a factor $e^{i\varrho}$ absorbed into the coefficient of $e$, and a scalar of modulus one.

All these errors can be summed before Cauchy–Schwarz. The original $m,n$ restrictions still imply $u\asymp x$, and the unmodified factorization mass is bounded by $$\sum_{\substack{mn=2u+1\\u\asymp x}}
       |\alpha_m\beta_n|A_0(u)
       \ll L^{O(1)}\sum_{v\asymp x}\tau(v)
       \ll xL^{O(1)}.$$ Here and below $\tau$ is the divisor function. The same estimate applies to the labelled-slot sum with its original factorial normalization. Combining it with (6.9) proves an error $O_H(xL^{-H})$ for arbitrary fixed $H$, without changing the fixed exponent in (6.8).

Consequently the required sum is, up to these errors, a sum and integral of total variation at most $L^{C_f}$ of expressions $$\begin{equation}
\tag{6.11}
 \begin{split}
 B'&=\sum_{e,n}a_e(e)\beta_n
                  \sum_{mn=2eh+1}\alpha_m a_h(h),\\
 a_h(h)&=h^{i\varrho}\varepsilon(h)W_1(h)H(h_*),\qquad
 H(t)=\sum_{pr=t}\mathbf{1}_{p\in Q_{j_{**}}}p^{i\sigma}c_r.
 \end{split}
\end{equation}$$ The original $m,n$ restrictions are in $\alpha,\beta$, and the $e$ range (6.7) is in $a_e$. The prime in $H$ is the designated prime. Its phase can be taken to be zero at this stage; we allow a bounded-power frequency $\sigma$ in the notation. All phases in (6.11) have fixed logarithmic-power bounds.

Both $a_e$ and $c_r$ are bounded coefficients. In fact, for a fixed branch and a fixed product, disjointness of the bands determines the prime multiset in every band. There are at most $r_0!$ assignments to the relevant labelled slots of any one band, even when primes repeat. Distributing the original factorial normalizations between the two coefficients only improves the resulting bound $$\begin{equation}
\tag{6.12}
 |a_e(e)|,|c_r|\le(r_0!)^{j_x+1}\le L^{C_a},
 \qquad |a_h(h)|\le L^{C_h}\tau(h_*).
\end{equation}$$ The last bound comes from summing over the designated prime divisor of $h_*$. The exponents $C_a,C_h$ are fixed independently of $K_0$ and of the Fourier error accuracy. Only ordinary-band primes were assigned to $e$, so its removal leaves the marked group weight and the sign exactly on $h$, as used in (6.11).

##### Cauchy–Schwarz and the diagonal.

Choose bounded nonnegative smooth majorants $\eta_e,\eta_n$, equal to at least one on the $e,n$ ranges. We can arrange $$\operatorname{supp}\eta_e\subset[\tfrac12L^{-C_s},2],
 \qquad \operatorname{supp}\eta_n\subset[1/2,3],
 \qquad
 \|\eta_e^{(j)}\|_\infty+\|\eta_n^{(j)}\|_\infty
                           \ll_j L^{C_{\eta}(j+1)},$$ where $C_{\eta}$ depends only on $C_s$. There are $O(EV)$ pairs $(e,n)$ in the original ranges. Hence (6.12) and Cauchy–Schwarz give $$\begin{equation}
\tag{6.13}
 |B'|^2\ll EVL^{C_p}\mathcal N,\qquad
 \mathcal N=\sum_{e,n}\eta_e(e/E)\eta_n(n/V)
                \left|\sum_{mn=2eh+1}\alpha_m a_h(h)\right|^2.
\end{equation}$$ Here $C_p$ is fixed independently of $K_0$.

The diagonal $m=m'$ in the square forces $h=h'$. Collecting by $v=mn$ and then using (6.12) gives $$\begin{align}
 \mathcal N_{\mathrm{diag}}
 &\ll L^{C_d}\sum_{\substack{v\asymp x\\v\ {\rm odd}}}
       \tau(v)\sum_{e\mid(v-1)/2}
                   \tau\left(\frac{v-1}{2e}\right)^2\notag\\
 &\le L^{C_d}\sum_{v\asymp x}\tau(v)\tau(v-1)^3
 \ll xL^{C_d'}.
 \tag{6.14}
\end{align}$$ The final estimate follows from Cauchy–Schwarz and the fixed second and sixth moments of $\tau$ in Proposition 2.2. Enlarging the $e$ divisor set in this calculation makes $C_d'$ independent of $K_0$. Since $EV\asymp xL^{-K_0}$, the diagonal contribution to the right side of (6.13) is at most $x^2L^{-K_0+C_p+C_d'}$. We now fix $$\begin{equation}
\tag{6.15}
                  K_0>2(D_*+C_f+1)+C_p+C_d'.
\end{equation}$$ It remains to obtain an arbitrarily strong logarithmic saving for the off-diagonal part of $\mathcal N$ with this fixed $K_0$.

##### The off-diagonal change of variables.

A pair of representations in the expanded square satisfies $$mn=2eh+1,\qquad m'n=2eh'+1.$$ The first identity gives $(n,2e)=1$. Subtracting the two identities therefore gives a unique integer $k$ with $$\begin{equation}
\tag{6.16}
 m'-m=2ek,\qquad h'-h=kn,\qquad
 z=m'h,\qquad z+k=mh'.
\end{equation}$$ Indeed $mh'-m'h=k(mn-2eh)=k$. On the off-diagonal $k\ne0$, and the lower support bound for $e$ gives $$\begin{equation}
\tag{6.17}
                         0<|k|\ll L^{K_0+C_s}.
\end{equation}$$

For completeness, this parametrization is reversible for both signs of $k$. Start from positive factorizations $z=m'h$, $z+k=mh'$, require $m'\equiv m\pmod{2|k|}$, and put $$\begin{equation}
\tag{6.18}
               e=\frac{m'-m}{2k}>0,\qquad
               n=\frac{2eh+1}{m}.
\end{equation}$$ The first quantity is an integer. The determinant identity implies $$m(h'-h)=k(2eh+1).$$ Since $P^-(m)>W$ and $k$ has the fixed logarithmic-power bound (6.17), we have $(m,k)=1$ for large $x$. Thus $n$ is a positive integer and $h'-h=kn$. Substituting $m'=m+2ek$ recovers $m'n=2eh'+1$. Every reconstructed variable is unique. Applying the size cutoffs in (6.13) therefore gives an exact bijection, with no additional multiplicity or divisibility condition.

Both $m,m'$ are odd and coprime to $k$. With $q_k=2|k|$, their congruence is imposed exactly by $$\begin{equation}
\tag{6.19}
 \mathbf{1}_{m'\equiv m\ ({\rm mod}\ q_k)}
        =\frac1{\varphi(q_k)}\sum_{\chi\ ({\rm mod}\ q_k)}
                              \chi(m)\overline{\chi(m')}.
\end{equation}$$ The normalized character sum has total coefficient mass one.

##### The pulled-back cutoffs.

On the supports above, $h\asymp x/e$ and $m'\asymp U$. Thus $z\asymp Ux/e$ lies between fixed constant multiples of $xL^{K_0}$ and $xL^{K_0+C_s}$. Insert a smooth dyadic partition in $z$, retaining an outer cutoff $\psi_Z(z/Z)$ in every piece. Only $O(1+T)$ dyads are needed, and all have $Z=xL^{O(1)}$.

For a fixed $k,Z$, put $$t_1=\log(m/U),\quad t_2=\log(m'/U),\quad t_3=\log(z/Z).$$ The arguments of the two majorants are exactly $$\begin{equation}
\tag{6.20}
 \begin{split}
 \frac eE
    &=\frac{m'-m}{2kE}
      =\frac{U}{2kE}(e^{t_2}-e^{t_1}),\\
 \frac nV
    &=\frac1V\left(\frac{(m'-m)z}{kmm'}+\frac1m\right)\\
    &=\frac{Z}{kUV}e^{t_3}(e^{-t_1}-e^{-t_2})
                                      +\frac1{UV}e^{-t_1}.
 \end{split}
\end{equation}$$ On a fixed compact box in these coordinates, every log-coordinate derivative of the first expression is $O_j(U/(|k|E))$, and every derivative of the second is $$O_j\left(\frac{Z}{|k|UV}+\frac1{UV}\right).$$ All these quantities are bounded by fixed powers of $L$ after (6.15). The chain rule and the derivative bounds for $\eta_e,\eta_n$ therefore give, for each multi-index $\nu$, $$\begin{equation}
\tag{6.21}
             \|\partial^\nu b_{k,Z}\|_\infty
                         \ll_\nu L^{C_0(|\nu|+1)}
\end{equation}$$ for the pulled-back product of majorants, multiplied by fixed smooth buffers in $t_1,t_2,t_3$. Choose these buffers to equal one on the original $m,m'$ dyads and on the support of the outer $z$ cutoff. This places $b_{k,Z}$ on a fixed compact box and leaves the sequence $\alpha$ unchanged. The majorants vanish in neighborhoods of nonpositive $e/E$ and $n/V$, so extending the product by zero across those regions is smooth. Positivity in (6.18) is thereby imposed by the same cutoffs.

This is the fixed-dimensional setting of Lemma 2.4. Choose a fixed $C_8$ larger than the slope required in (6.21), and put $P=L^{C_8}$. Repeated integration by parts in these three coordinates gives $$|\widehat b_{k,Z}(\boldsymbol\xi)|
       \ll_j(1+|\boldsymbol\xi|/P)^{-j},\qquad
 \int_{\mathbb R^3}|\widehat b_{k,Z}(\boldsymbol\xi)|
                                      \,d\boldsymbol\xi\ll P^3,$$ and $$\begin{equation}
\tag{6.22}
 \int_{|\boldsymbol\xi|>PL}|\widehat b_{k,Z}(\boldsymbol\xi)|
                 \,d\boldsymbol\xi\ll_j P^3L^{3-j}.
\end{equation}$$ Consequently the cutoffs separate into phases $m^{i\xi_1}(m')^{i\xi_2}z^{i\xi_3}$ at fixed logarithmic-power cost and with fixed logarithmic-power frequencies. Scalars involving $U$ and $Z$ have modulus one.

To justify the tails absolutely, an endpoint convolution is bounded by $L^{O(1)}\tau(v_*)^2$: there are at most $\tau_3(v_*)\le\tau(v_*)^2$ triples $mpr=v_*$. Including the bounded group weights and dropping the congruence, Cauchy–Schwarz and the fixed fourth divisor moment in Proposition 2.2 give $$\begin{equation}
\tag{6.23}
 L^{O(1)}\sum_{z\asymp Z}\tau(z)^2\tau(z+k)^2
                         \ll ZL^{O(1)}.
\end{equation}$$ Here $|k|\ll L^{O(1)}=o(Z)$ and both positions are positive. This estimate controls (6.22), after summing over all $k$ and $Z$, to arbitrary logarithmic accuracy by increasing $j$. The fixed exponent $C_8$ need not increase with that accuracy.

##### Identifying the two endpoints.

Fix one character in (6.19) and one retained Fourier term. Before the character and Fourier factors, the coefficient from the expanded square is $$\alpha_m\overline{\alpha_{m'}}
                        a_h(h)\overline{a_h(h')}.$$ Define invariant cores, for positive integers $v$, by $$\begin{equation}
\tag{6.24}
 \begin{split}
 F_0(v)&=\sum_{mpr=v_*}\alpha_m\chi(m)
             m^{i(\varrho-\xi_2)}
             \mathbf{1}_{p\in Q_{j_{**}}}p^{-i\sigma}\overline{c_r},\\
 G_0(v)&=\sum_{mpr=v_*}\alpha_m\chi(m)
             m^{i(\xi_1+\varrho)}
             \mathbf{1}_{p\in Q_{j_{**}}}p^{-i\sigma}\overline{c_r}.
 \end{split}
\end{equation}$$ Both cores contain the original restricted sequence $\alpha$. All group primes are below $W$, whereas $m,m'$ have no prime factor at most $W$. Therefore $$\begin{equation}
\tag{6.25}
 \begin{gathered}
 z_*=m'h_*,\qquad (z+k)_*=mh'_*,\\
 W_1(z)=W_1(h),\quad W_1(z+k)=W_1(h'),\qquad
 \varepsilon(z)=\varepsilon(h),\quad
 \varepsilon(z+k)=\varepsilon(h').
 \end{gathered}
\end{equation}$$ Using also $h=z/m'$ and $h'=(z+k)/m$, direct expansion shows that the separated sum is precisely $$\begin{equation}
\tag{6.26}
 \sum_{\substack{z>0\\z+k>0}}
  \psi_Z(z/Z)z^{i(\varrho+\xi_3)}(z+k)^{-i\varrho}
       \overline{F_0(z)}G_0(z+k)
       W_1(z)W_1(z+k)\varepsilon(z)\varepsilon(z+k).
\end{equation}$$ For example, conjugating the first core supplies $\overline{\alpha_{m'}}\overline{\chi(m')} (m')^{i(\xi_2-\varrho)}H(h_*)$, while the second core supplies $\alpha_m\chi(m)m^{i(\xi_1+\varrho)}\overline{H(h'_*)}$. The remaining powers in (6.26) give exactly $h^{i\varrho}(h')^{-i\varrho}z^{i\xi_3}$. Thus the discrepancy-bearing first core has the required coefficient $\alpha$, with its conjugation occurring outside that core.

Every hypothesis of Theorem 4.1 is now satisfied. The designated slot is a prime in the fixed range (6.3); the residual coefficients are bounded by (6.12); the character modulus $2|k|$ and all frequencies have fixed logarithmic-power bounds; and the two endpoints have the same allowed sign. Finally, set $$\widetilde\psi_Z(t)=t\psi_Z(t).$$ Then $\psi_Z(z/Z)=(Z/z)\widetilde\psi_Z(z/Z)$. Consequently (6.26) is exactly $Z$ times a harmonic correlation covered by that theorem. For any prescribed $D_0$ it is therefore $$\begin{equation}
\tag{6.27}
                              O(ZL^{-D_0}),
\end{equation}$$ provided the discrepancy exponent $B$ is chosen sufficiently large after all the fixed bounds and $D_0$.

##### Completing the parameter choices.

Here is an explicit ordering of the choices. First fix the weight geometry, $b_*,D_*,C$, the designated band, the allocation functions, and the cutoff. These determine the exponents $$C_s,\ C_a,\ C_h,\ C_f,\ C_p,\ C_d'.$$ Fix $K_0$ by (6.15). This fixes the derivative and frequency bounds after Cauchy–Schwarz, the Fourier scale $P$, and exponents $K_k,K_z,C_{\rm sep}$ such that there are at most $L^{K_k}$ shifts, $Z\le xL^{K_z}$, and the total post-Cauchy separation cost, including the dyads, is at most $L^{C_{\rm sep}}$. These exponents are all fixed.

Choose $A_{\rm off}>0$ so that $$-K_0+C_p-A_{\rm off}<-2(D_*+C_f+1),$$ and then choose $$D_0>A_{\rm off}+K_k+K_z+C_{\rm sep}+2.$$ Choose the differentiation orders in the Fourier tail estimates large enough for the same error target. Theorem 4.1 now supplies a sufficiently large fixed $B$. Summing (6.27) over shifts, dyads, characters, and the retained Fourier integrals gives $$|\mathcal N_{\rm off}|
                                  \ll xL^{-A_{\rm off}}.$$ Together with (6.14), (6.15), and (6.13), this proves $|B'|\ll xL^{-D_*-C_f-1}$. The total pre-Cauchy variation $L^{C_f}$ and the arbitrarily small previously discarded errors prove (6.2) for each choice of $\varepsilon$, and hence for $A$. ◻

*Remark 6.2* (Precision in subsequent proxy replacements). Theorem 6.1 permits the actual interval restriction to be included in $\alpha$, and it asks only for boundedness of the other coefficient. Thus it can be applied a second time after exchanging the two factors, even if the first coefficient has already been replaced by a nonsmooth bounded proxy. On $O(L)$ contributing factor dyads, its total error is $O(xL^{-D_*+1})$. The lower bound $X_A\gg xL^{-C_A}$ in Lemma 5.2 makes this $o(X_A/L)$ whenever $D_*>C_A+2$.

In particular, if a later proxy construction has coefficients bounded by one independently of its logarithmic cell precision $S_1$, use that coefficient bound when making all the choices above. First fix $K_0$, the shifted-correlation accuracy, and finally the discrepancy exponent $B$; only afterwards choose the proxy precision $S_1>2B+3$. Neither $C_f$ nor the coefficient or diagonal exponents depends on $S_1$. Increasing $S_1$ therefore changes only how large $x$ must be and does not reopen any earlier choice.

## Distribution in congruence classes

For an odd squarefree integer $d$ define $$\begin{equation}
\tag{7.1}
 r(d)=\sum_{\substack{u\ge1\\2u+1\equiv0\pmod d}}
                    A(u)\Psi(u/x)-\frac{X_A}{\varphi(d)}.
\end{equation}$$ The following estimate supplies the distribution needed by the sieve. Its proof uses only the prime slot in $Q_0$, the weight bounds already proved, and the classical Siegel–Walfisz and multiplicative large sieve estimates in [4, Section “Notation and preliminary estimates”].

**Theorem 7.1** (Congruence distribution). *For every fixed $0<\vartheta<1/2$ and $D>0$, $$\sum_{\substack{d\le x^\vartheta\\d\ {\rm odd\ and\ squarefree}}}
       |r(d)|\ll_{\vartheta,D}xL^{-D}+X_A L^{-18}.$$ The constants may depend on the fixed weight geometry and $\Psi$, but not on any later proxy precision. No effective bound on the threshold for $x$ is asserted.*

*Proof.* Write $Q=x^\vartheta$ and $w(u)=A(u)\Psi(u/x)$. The congruence in Equation (7.1) is the single unit class $a_d\equiv-2^{-1}\pmod d$. Character orthogonality gives the exact identity $$\begin{equation}
\tag{7.2}
 r(d)=\frac1{\varphi(d)}
       \sum_{\substack{\chi\bmod d\\\chi\ne\chi_0}}
          \overline{\chi(a_d)}\sum_u w(u)\chi(u)
       -\frac1{\varphi(d)}\sum_{(u,d)>1}w(u).
\end{equation}$$ We first bound the correction in the second term. Mertens’ estimate implies $$\begin{equation}
\tag{7.3}
 \sum_{h\le Q}\frac{\mu^2(h)}{\varphi(h)}
 \le\prod_{p\le Q}\left(1+\frac1{p-1}\right)\ll L.
\end{equation}$$ For a fixed $u$ in the effective support of $w$, we have $x\le u\le2x$ and every prime divisor of $u$ is at least $L^{20}$. Writing a squarefree $d$ divisible by $p$ as $ph$, and then using a union bound, gives $$\sum_{\substack{d\le Q\\d\ {\rm squarefree}\\(d,u)>1}}
       \frac1{\varphi(d)}
 \le\sum_{p\mid u}\frac1{p-1}
        \sum_{h\le Q}\frac{\mu^2(h)}{\varphi(h)}
 \ll L\sum_{p\mid u}\frac1{p-1}\ll L^{-18}.$$ For the last inequality, $u$ has at most $\log(2x)/(20T)$ distinct prime divisors. Since $w\ge0$, the total principal correction is therefore $O(X_A L^{-18})$.

To treat the nonprincipal characters, delete one designated ordered slot of $Q_0$ from the definition of $a$. Retain the original divisor $(r_0!)^{j_x+1}$ in the resulting coefficient, denoted by $a^-(v)$. If the residual exponents are $e_p$, then $$a^-(v)=\frac1{r_0}\prod_{j=0}^{j_x}\prod_{p\in Q_j}\frac1{e_p!}
 \le\frac1{r_0},$$ with $r_0-1$ slots in $Q_0$ and $r_0$ slots in every other band, and $a^-(v)=0$ off this support. Partitioning ordered tuples by the deleted prime gives, including when primes repeat, $$a(v)=\sum_{\substack{p\in Q_0\\p\mid v}}a^-(v/p).$$ The $Q_0$-primes lie outside $\mathcal P$, so removing that slot changes neither $W_1$ nor $\mathcal E$. Consequently $$\begin{equation}
\tag{7.4}
 A(u)=\sum_{\substack{pr=u\\p\in Q_0}}b(r),
 \qquad
 b(r)=W_1(r)\frac{1-\mathcal E(r)}2a^-(r_*),
 \qquad |b(r)|\le L^{B_0},
\end{equation}$$ where $B_0$ is fixed by the weight geometry.

Split $p,r$ into dyads of sizes $P,R$. Only $O(L)$ pairs of dyads contribute, and on these $PR\asymp x$. Since $x^{c_1s'}\le p\le x^{c_2s'}$, there is a fixed $c>0$, depending only on Equation (5.1), such that $$\begin{equation}
\tag{7.5}
 P,R\ge x^c
\end{equation}$$ for every contributing pair and all sufficiently large $x$. For example any $c<\min(c_1s',1-c_2s')$ suffices.

Every character modulo an odd squarefree $d$ is induced by a unique primitive character $\chi_f$ of conductor $f\mid d$. Write $d=fh$; then $(f,h)=1$ and $\varphi(d)=\varphi(f)\varphi(h)$. For such an induced character, $$\chi(pr)=\chi_f(p)\chi_f(r)
                  \mathbf{1}_{\{(p,h)=1\}}\mathbf{1}_{\{(r,h)=1\}}.$$ The nonprincipal characters have $f>1$; there is no multiplicity in this parametrization. After applying the triangle inequality in Equation (7.2), it remains to bound sums of the form $$\begin{equation}
\tag{7.6}
 \begin{split}
 \sum_{\substack{h\le Q\\h\ {\rm odd\ and\ squarefree}}}
 \frac1{\varphi(h)}
 \sum_{\substack{1<f\le Q/h\\f\ {\rm odd\ and\ squarefree}\\(f,h)=1}}
 &\frac1{\varphi(f)}\sum_{\chi_f\bmod f}^{*}\\
 &\quad\cdot
 \left|\sum_{\substack{p\in Q_0,\ p\asymp P\\r\asymp R}}
       b(r)\chi_f(pr)\mathbf{1}_{\{(pr,h)=1\}}\Psi(pr/x)\right|.
 \end{split}
\end{equation}$$ Here and below the asterisk denotes primitive characters. Modulus restrictions may be discarded in nonnegative majorants, which will be useful when applying the large sieve.

Choose a fixed $K$ later, and first consider the conductors $f>L^K$. Put $\psi(v)=\Psi(e^v)$ and $\widehat\psi(t)=\int_{\mathbb R}\psi(v)e^{-itv}\,dv$. Fourier inversion gives $$\Psi(pr/x)=\frac1{2\pi}\int_{\mathbb R}
             \widehat\psi(t)x^{-it}p^{it}r^{it}\,dt,
 \qquad \int_{\mathbb R}|\widehat\psi(t)|\,dt\ll_\Psi1.$$ There is no frequency truncation error. For fixed $h,t$, define $$\mathcal P_h(\chi,t)=
    \sum_{\substack{p\in Q_0,\ p\asymp P\\(p,h)=1}}\chi(p)p^{it},
 \qquad
 \mathcal R_h(\chi,t)=
    \sum_{\substack{r\asymp R\\(r,h)=1}}b(r)\chi(r)r^{it}.$$ Their coefficient squared norms are at most $O(P)$ and $O(RL^{2B_0})$, respectively, uniformly in $h,t$. On a conductor dyad $F<f\le2F$, Cauchy–Schwarz followed by the primitive multiplicative large sieve therefore yields $$\begin{align}
 \sum_{F<f\le2F}\frac1{\varphi(f)}
       \sum_{\chi_f\bmod f}^{*}
       |\mathcal P_h(\chi_f,t)\mathcal R_h(\chi_f,t)|
 &\ll \frac{L^{B_0}}{F}
       \sqrt{(P+F^2)(R+F^2)PR} \notag\\
 &\ll xL^{B_0}
       \left(\frac1F+\frac1{\sqrt P}+\frac1{\sqrt R}
                        +\frac F{\sqrt x}\right).
       \tag{7.7}
\end{align}$$ Indeed $1/\varphi(f)\ll F^{-1}f/\varphi(f)$ on this dyad, giving exactly the large sieve’s primitive-character weight. The masks $\mathbf{1}_{(p,h)=1},\mathbf{1}_{(r,h)=1}$ do not enlarge the coefficient norms.

Integrate against $|\widehat\psi|$, sum the conductor and factor dyads, and use Equation (7.3) for the remaining $h$-sum. Since $F\le Q$, Equations (7.5) and (7.7) give a total at most $$\begin{equation}
\tag{7.8}
 xL^{B_2}
       \left(L^{-K}+x^{-c/2}+x^{\vartheta-1/2}\right)
\end{equation}$$ for a fixed $B_2$ independent of $K$. One can use dyads intersected with $f>L^K$, so their lower endpoints are at least $L^K/2$. In particular the summation over $h$ costs a logarithmic factor, not a factor $Q$. Taking $K>B_2+D+2$ makes Equation (7.8) $O(xL^{-D})$, because $\vartheta<1/2$.

It remains to consider $1<f\le2L^K$. For fixed $r\asymp R$, apply Siegel–Walfisz to the nonprincipal character $\chi_f$ on the prime interval $Q_0\cap[P,2P)$. Since $P\ge x^c$, the modulus is bounded by a fixed power of $\log P$. Summing the residue-class estimate against $\chi_f$ and asking for a stronger initial saving absorbs the at most $\varphi(f)$ classes. Partial summation, using the uniformly bounded supremum and total variation of $p\mapsto\Psi(pr/x)$ on this interval, gives, for any fixed $M$, $$\begin{equation}
\tag{7.9}
 \sum_{\substack{p\in Q_0\\p\asymp P}}
       \chi_f(p)\Psi(pr/x)\ll_{K,M}P L^{-M}.
\end{equation}$$ This use of Siegel–Walfisz includes possible exceptional real characters; its potentially ineffective constants cause no problem.

Imposing $(p,h)=1$ deletes only $O(1)$ terms in Equation (7.9): each deleted prime is at least $x^c$, while $h\le x^\vartheta$, so there are at most $\vartheta/c+O(1)$ such primes. Thus the inner double sum in Equation (7.6) is at most $$RL^{B_0}\bigl(PL^{-M}+O(1)\bigr)
 \ll xL^{B_0-M}+x^{1-c}L^{B_0}.$$ The other mask, $(r,h)=1$, only decreases this absolute bound. For the small conductors, $$\sum_{1<f\le2L^K}\frac1{\varphi(f)}
                         \sum_{\chi_f\bmod f}^{*}1\ll L^K.$$ Combining this with Equation (7.3) and the number of factor dyads bounds the small-conductor contribution by $$\begin{equation}
\tag{7.10}
 xL^{B_3+K-M}+x^{1-c}L^{B_3+K}
\end{equation}$$ for a fixed $B_3$ independent of $K,M$. Choose $M>B_3+K+D+2$. Equation (7.10) is then $O(xL^{-D})$. Together with the large-conductor estimate and the principal correction, this proves the theorem. ◻

## Prime extraction

Put $N_u=2u+1$ and $a_x(u)=A(u)\Psi(u/x)$, so that $a_x(u)\ge0$ and $X_A=\sum_u a_x(u)$. Throughout this section the band geometry, the even integer $r_0$, the damping $q_0=1/2$, and $\Psi$ are the fixed data of the weight construction. In particular, Lemma 5.2 gives $$\begin{equation}
\tag{8.1}
 X_A\asymp\frac{x}{L}H_QH_P,\qquad X_A\gg xL^{-C_A},\qquad H_P\ge1.
\end{equation}$$ We use the Type II and congruence distribution results proved above, together with the following explicitly stated sieve and proxy inputs.

### Sieve and proxy inputs

**Lemma 8.1** (Block sieve, imported). *Consider finitely many objects with nonnegative weights and, at some primes $p\le z$, designated bad conditions. Suppose that for every squarefree product $d$ of these primes, including $d=1$, the weight on which all conditions indexed by $p\mid d$ hold is $Xg(d)+r(d)$. Here $X\ge0$, $g$ is multiplicative, and, for fixed $\eta_0>0$ and $C$, one has $$0\le g(p)\le1-\eta_0,\qquad
 \sum_{w<p\le w^2}g(p)\le C\quad(w>1).$$ For every sufficiently large even integer $h$, the weight avoiding all the bad conditions equals $$\begin{equation}
\tag{8.2}
 X\prod_{p\le z}(1-g(p))(1+O(e^{-h}))
 +O\!\left(\sum_{\substack{d\le z^{4h+2}\\d\text{ squarefree}}}
                 |r(d)|\right).
\end{equation}$$ The products and sums use only the designated primes. Constants depend only on the two density bounds, and are uniform when $h$ grows. For $h=2$ there is an upper bound by a fixed constant times the displayed main term, plus the same remainder sum.*

*The upper and lower inclusion–exclusion polynomials have coefficients of absolute value at most one, supported on squarefree $d\le z^{4h+2}$. The upper polynomial is nonnegative. Its overcount is bounded by the nonnegative difference between the upper and lower polynomials; that difference also has coefficients of absolute value at most one and the same support bound.*

This is the Block sieve, Lemma 2.9 of [4]. Its coefficient bound, its growing-$h$ uniformity, and its fixed-depth upper bound will each be used below. No sieve assertion about the present weight is included in the import: its required remainder estimates come from Theorem 7.1 or from the explicit box count below.

Define $$\begin{equation}
\tag{8.3}
 \begin{split}
 V(y)&=\prod_{p\le y}(1-1/p),\qquad
 V_1(y)=\prod_{3\le p\le y}(1-1/(p-1)),\\
 \mathfrak S&=2\prod_{p\ge3}\left(1-\frac1{(p-1)^2}\right)>0.
 \end{split}
\end{equation}$$ Mertens’ estimate and the convergent quotient product give $$\begin{equation}
\tag{8.4}
 V(y)\sim\frac{e^{-\gamma_E}}{\log y},\qquad
 V_1(y)\sim\mathfrak S V(y),
\end{equation}$$ where $\gamma_E$ is Euler’s constant.

Here are the proxy estimates we use. For the moment let $0<\kappa<1/50$ and $0<b_1<1/2-\kappa$ be arbitrary fixed numbers, and let $(\gamma,\gamma']$ range over a fixed finite partition of $(b_1,1/2-\kappa]$. On $[x^{b_1/4},x^{1-b_1/4}]$ consider the tests $$I_{\mathrm{pr}}(m)=\mathbf{1}_{m\text{ prime}},\qquad
 I_\gamma(m)=\mathbf{1}_{P^-(m)>x^\gamma}.$$ For a fixed precision $S_1>0$, partition the logarithmic axis into cells of width $\Delta_L=L^{-S_1}$. On every full cell $C_Y=(Y,e^{\Delta_L}Y]$ meeting the ambient interval, put $$\begin{equation}
\tag{8.5}
 c_I(C_Y)=
 \frac{\sum_{m\in C_Y}I(m)}
      {\#\{m\in C_Y:P^-(m)>W\}},\qquad
 B_I(m)=c_I(C_Y)\mathbf{1}_{P^-(m)>W}\quad(m\in C_Y).
\end{equation}$$ Even if a later factor range cuts a cell, both counts in this definition are taken on the full cell. Range restrictions are applied only after the ratio has been defined.

**Lemma 8.2** (Proxy estimates, imported). *For sufficiently large $x$, the denominators in (8.5) are positive and $0\le c_I\le1$. For every fixed $B>0$, every fixed $S_1>2B+3$, and every interval $K$ inside a dyad in the stated factor ranges, the sequence $$\alpha_m=(I(m)-B_I(m))\mathbf{1}_{m\in K}$$ vanishes outside $P^-(m)>W$, has absolute value at most one, and satisfies $$\begin{equation}
\tag{8.6}
 \left|\sum_{m\in J}\alpha_m\chi(m)m^{-1+it}\right|\le L^{-B}
\end{equation}$$ for every interval $J\subset[1,x^2]$, every Dirichlet character of modulus at most $L^B$, and every $|t|\le L^B$.*

*Write $$\mathcal B_\kappa=[x^{1/2-2\kappa},x^{1/2+2\kappa}].$$ There is an absolute constant $C_{\mathrm{pr}}$ such that $$\begin{equation}
\tag{8.7}
 c_{\mathrm{pr}}(m)\le\frac{C_{\mathrm{pr}}}{LV(W)}
       \qquad(m\in\mathcal B_\kappa).
\end{equation}$$ The constant is independent of $\kappa$ and $S_1$; the threshold for $x$ may depend on all fixed parameters.*

*For $w>\gamma>0$, set $$\begin{equation}
\tag{8.8}
 D_\gamma(w)=\frac1w+
 \sum_{l\ge2}\frac1{l!}
 \int_{\substack{t_i\ge\gamma\ (1\le i<l)\\
                   \sum_{i<l}t_i\le w-\gamma}}
       \frac{\prod_{i<l}(dt_i/t_i)}{w-\sum_{i<l}t_i}.
\end{equation}$$ This sum is locally finite and nonnegative, and is jointly continuous on compact subsets of $w>\gamma>0$, including the thresholds $w=l\gamma$. If $mn=N_u$ on the support of $\Psi(u/x)$ and $\log n/L\in(\gamma,\gamma']$, then $$\begin{equation}
\tag{8.9}
 c_\gamma(m)\le
 \frac{\sup_{\gamma\le t\le\gamma'}D_\gamma(1-t)+o(1)}{LV(W)}.
\end{equation}$$ Here the parameters are restricted to a compact subset of $w>\gamma>0$, as holds for the bins under consideration. For fixed sufficiently small $b>0$, $$\begin{align}
 \int_b^{1/2}D_\alpha(1-\alpha)\frac{d\alpha}{\alpha}
     &=D_b(1)-1,\tag{8.10}\\
 D_b(1)&\le\frac{e^{-\gamma_E}}b(1+O(e^{-c/b}))
       \tag{8.11}
\end{align}$$ with an absolute $c>0$. The endpoint of the integral is interpreted by its left limit.*

The discrepancy assertion and the density assertions are, respectively, Lemmas 7.3 and 7.4 of [4], in the section “Extracting primes with smooth predecessors.” These results concern ordinary integer cells; their hypotheses contain no candidate weight. In particular they apply to the present $A$. The exact bound $c_I\le1$ also follows directly because each test selects a subset of the $W$-rough integers in its cell. Thus the coefficient bounds of both $B_I$ and $I-B_I$ do not depend on the precision $S_1$. In (8.9), $$\frac{\log m}{L}=1-\frac{\log n}{L}+O(1/L),\qquad
 \frac{\log m}{L}-\gamma\ge2\kappa+O(1/L),$$ which verifies the required separation from $w=\gamma$. Every little-oh assertion in the proxy estimates is taken only after its parameters have been fixed.

### A uniform positive pair bound

We first prove an upper bound that uses only the original weight geometry. This establishes the constant needed to choose $\kappa$ without referring to $b_1$, the Type II discrepancy exponent, or the eventual proxy precision.

Choose a sufficiently large fixed integer $j'$ and a fixed $\theta$ in the gap $$\begin{equation}
\tag{8.12}
 c_2s'2^{-j'}<\theta<c_1s'2^{-j'+1},\qquad
 10\theta\le\frac1{20},\qquad
 \sum_{j\ge j'}r_0c_2s'2^{-j}\le\frac1{25}.
\end{equation}$$ Such choices exist because $c_2<2c_1$, and all endpoints decrease geometrically. Call $Q_j$ with $j\ge j'$ the micro bands and those with $j<j'$ the macro bands.

**Lemma 8.3** (Assignment and mask majorant). *An assignment $a$ consists of the complete ordered $r_0$-tuples in all the micro bands and one prime mark from each $\mathcal P_g$. Let $D_1=D_1(a)$ be their product, with multiplicities retained, and put $$\lambda_a=\prod_{j=j'}^{j_x}\frac1{r_0!}\prod_g V_g^{-1}.$$ For sufficiently large $x$, $$\begin{equation}
\tag{8.13}
 D_1\le x^{1/20},\qquad
 \sum_a\frac{\lambda_a}{D_1}\ll H_Q,\qquad
 \sum_a\lambda_a\ll x^{1/20}H_Q.
\end{equation}$$ For each assignment, ban every odd non-$\mathcal P$ prime at most $x^\theta$ not dividing $D_1$, and independently ban each $\mathcal P$ prime not dividing $D_1$ with probability $1-q_0$. With expectation over this finite random mask, $$\begin{equation}
\tag{8.14}
 A(u)\le A_0(u)\le
 \sum_a\lambda_a\mathbf{1}_{D_1\mid u}\,\mathbb E_a
           \mathbf{1}_{u\text{ is divisible by no banned prime}}.
\end{equation}$$ The constants in (8.13) depend only on the fixed weight geometry and $j'$.*

*Proof.* The product of the micro entries is at most $x^{1/25}$ by (8.12). There are $O(T)$ marks and every mark is at most $\exp(L^{2/5})$, so their product is $\exp(O(TL^{2/5}))=x^{o(1)}$. This proves the asserted bound for $D_1$, including assignments with repeated micro entries. Write $$H_Q^{\mathrm{mic}}
 =\prod_{j=j'}^{j_x}\frac1{r_0!}
                      \left(\sum_{p\in Q_j}\frac1p\right)^{r_0}.$$ Summing the reciprocal product of the marks gives $\prod_g(V_g^{-1}\sum_{p\in\mathcal P_g}p^{-1})=1$. Consequently $\sum_a\lambda_a/D_1=H_Q^{\mathrm{mic}}\ll H_Q$: only finitely many fixed band factors, bounded above and below, have been omitted from $H_Q$. The last assertion in (8.13) follows by multiplying by the bound for $D_1$.

To prove the majorant, fix $u$ with $A_0(u)>0$ and a compatible choice of ordered micro entries and marks. The band gap in (8.12) implies that all non-$\mathcal P$ prime factors of $u$ below $x^\theta$ are among these micro entries, whereas every macro prime exceeds $x^\theta$. All group primes are below $x^\theta$ for sufficiently large $x$. The only random survival conditions are therefore at the distinct unmarked group-prime divisors of $u$. There are exactly $\omega_P(u)-s_P$ of them, so the survival probability is $q_0^{\omega_P(u)-s_P}$, even when marked or unmarked primes occur to higher powers.

Summing one mark per group with normalization $\prod_g V_g^{-1}$ recovers the factor $W_1(u)$. For a fixed prime multiset in any band, the number of ordered $r_0$-tuples divided by $r_0!$ is $1/\prod_p v_p!\le1$. Summing the normalized compatible micro lists retains their exact contribution to $a(u_*)$; dropping the remaining macro-list contribution can only increase it. Thus the compatible assignments already dominate $A_0(u)$. Incompatible assignments contribute nonnegative terms, proving (8.14). ◻

**Lemma 8.4** (Positive dyadic pair estimate). *There is a constant $C_{\mathrm{box}}$, depending only on the fixed weight data and the choices in (8.12), such that, on every dyadic box with $M_1M_2\asymp x$ and $M_i\ll x^{0.54}$, $$\begin{equation}
\tag{8.15}
 \sum_{\substack{M_1\le m<2M_1,\ M_2\le n<2M_2\\
                 mn=N_u,\ P^-(m),P^-(n)>W}}
       a_x(u)\le C_{\mathrm{box}}X_AV(W)^2.
\end{equation}$$ The fixed constants in the size comparisons can be taken to cover all boxes meeting $mn=2u+1$ with $u\in[x,2x]$.*

*Proof.* Use Lemma 8.3 and bound $\Psi$ by its fixed supremum. Fix an assignment and a mask. Since $D_1$ is odd, $D_1\mid u$ implies $mn\equiv1\pmod{D_1}$. We count all pairs in the box with this congruence, dropping both the parity of $mn$ and the remaining support restriction on $u$.

For every odd prime $l\le x^\theta$ not dividing $D_1$, impose the bad condition $mn\equiv0\pmod l$ when $l\le W$, and the bad condition $mn\equiv1\pmod l$ when $l$ is banned. There are $2l-1$ pairs of residues with product zero and $l-1$ with product one; the two sets are disjoint. Hence the local number and density of bad residue pairs are $$\begin{equation}
\tag{8.16}
 \nu(l)=(2l-1)\mathbf{1}_{l\le W}+(l-1)\mathbf{1}_{l\text{ banned}},
 \qquad g(l)=\frac{\nu(l)}{l^2}.
\end{equation}$$ In particular $g(l)\le7/9$ and $g(l)\le3/l$. These give uniform density hypotheses for Lemma 8.1, independent of the assignment and mask.

There are exactly $\varphi(D_1)$ residue pairs with product one modulo $D_1$: choose the first unit and then its unique inverse. This statement does not require $D_1$ to be squarefree. For a squarefree $d$ built from the sieving primes, the Chinese remainder theorem gives exactly $\varphi(D_1)\nu(d)$ pairs modulo $D_1d$, where $\nu$ is multiplicative. Each pair of classes contributes $$\frac{M_1M_2}{(D_1d)^2}
  +O\left(1+\frac{M_1+M_2}{D_1d}\right).$$ Thus the base mass is $M_1M_2\varphi(D_1)/D_1^2$, with local density $g(d)$. Since $\nu(d)\le d\tau(d)^2$, the lattice remainders satisfy $$|r_a(d)|\ll\tau(d)^2\{M_1+M_2+D_1d\}.$$ Use the $h=2$ upper bound in Lemma 8.1, whose level is $D=(x^\theta)^{10}$. Fixed divisor-moment bounds give $$\begin{equation}
\tag{8.17}
 \sum_{d\le D}|r_a(d)|
 \ll L^{C_0}\{(M_1+M_2)D+D_1D^2\}
\end{equation}$$ for a fixed $C_0$. This includes $d=1$ and is uniform in the mask.

We next compare the sieve product with Mertens products. For $l\le W$ banned by the mask, its factor is $1-3/l+2/l^2$; for an allowed $l\le W$ it is $(1-1/l)^2$. For $W<l\le x^\theta$ outside $D_1$, all primes are non-group primes and banned, and the factor is $1-1/l+1/l^2$. Comparing these factors, allowing a convergent product of $1+O(l^{-2})$ and the fixed factor at $2$, gives $$\begin{equation}
\tag{8.18}
 \prod_{\substack{3\le l\le x^\theta\\l\nmid D_1}}(1-g(l))
 \ll V(W)^2V(x^\theta)
       \prod_{l\mid D_1}(1-1/l)^{-3}
       \prod_{\substack{l\in\mathcal P,\ l\nmid D_1\\
                         l\text{ allowed}}}(1-1/l)^{-1}.
\end{equation}$$ Every prime dividing $D_1$ is at least $L^{20}$, and $\log D_1=O(L)$, so $$\sum_{l\mid D_1}\frac1l
       \ll\frac{L^{-19}}{\log L}.$$ Its correction product in (8.18) is therefore uniformly bounded. Independence of the mask gives $$\begin{align*}
 \mathbb E_a
 \prod_{\substack{l\in\mathcal P,\ l\nmid D_1\\l\text{ allowed}}}
              (1-1/l)^{-1}
 &=\prod_{\substack{l\in\mathcal P\\l\nmid D_1}}
              \left(1+\frac{q_0}{l-1}\right)\\
 &\le\prod_{l\in\mathcal P}\left(1+\frac{q_0}{l-1}\right)
 \le H_P.
\end{align*}$$ For the last inequality, the group factor in $H_P$ is $$\prod_{p\in\mathcal P_g}\left(1+\frac{q_0}{p-1}\right)
       \frac1{V_g}\sum_{p\in\mathcal P_g}\frac1{p-1+q_0},$$ and the final factor is at least one.

Since $\varphi(D_1)/D_1^2\le1/D_1$, summing the main term over assignments with Lemma 8.3 gives $$\begin{equation}
\tag{8.19}
 \ll xV(W)^2V(x^\theta)H_QH_P
 \ll X_AV(W)^2.
\end{equation}$$ Here $V(x^\theta)\asymp L^{-1}$, with $\theta$ already fixed, and we used (8.1). It remains essential to sum the errors over assignments as well. From (8.13), $$\sum_a\lambda_aD_1\le x^{1/10}O(H_Q).$$ Since $D\le x^{1/20}$ and $M_i\ll x^{0.54}$, $$\begin{align}
 \sum_a\lambda_a\sum_{d\le D}|r_a(d)|
 &\ll L^{C_0}H_Q
       \{x^{1/20}(M_1+M_2)D+x^{1/10}D^2\}\notag\\
 &\ll L^{C_0}H_Q(x^{0.64}+x^{0.20})
   =o(X_AV(W)^2).\tag{8.20}
\end{align}$$ Indeed $X_AV(W)^2\asymp xH_QH_P/L^2$ and $H_P\ge1$. This proves (8.15). Every constant used here depends only on the original weight data and $j',\theta$. ◻

For later use, a dyadic decomposition of $\mathcal B_\kappa$ and Lemma 8.4 imply $$\begin{equation}
\tag{8.21}
 R_\kappa:=
 \sum_{\substack{mn=N_u,\ m,n\in\mathcal B_\kappa\\
                  P^-(m),P^-(n)>W}}a_x(u)
 \le C_1(\kappa L+1)X_AV(W)^2.
\end{equation}$$ There are $O(\kappa L+1)$ first-factor dyads because the interval has logarithmic length $4\kappa L$, and only $O(1)$ second-factor dyads per first-factor dyad because $mn\in[2x+1,4x+1]$. Enlarging partially intersected boxes is legitimate by positivity. For $\kappa<1/50$ all their sides are $O(x^{0.54})$. Consequently $C_1$ is independent of $\kappa,b_1,S_1$. Fix, at this point, the constant $$\begin{equation}
\tag{8.22}
 C_{\mathrm{bal}}=C_{\mathrm{pr}}^2C_1,
\end{equation}$$ enlarging it if necessary to absorb the fixed dyadic conventions.

### Parameter choice and test replacement

Choose $0<\kappa<1/50$ so small that $$\begin{equation}
\tag{8.23}
 C_{\mathrm{bal}}\kappa<\mathfrak S/4.
\end{equation}$$ Next choose $b_1>0$ sufficiently small, with $b_1<1/100$, to satisfy the presieve and subtraction conditions below. The constants in those conditions do not depend on a later proxy precision. Set $$\vartheta=\frac12-\frac\kappa2,\qquad b_* = b_1/3.$$ By continuity in Lemma 8.2, a sufficiently fine fixed partition of $(b_1,1/2-\kappa]$ satisfies $$\begin{equation}
\tag{8.24}
 \sum_{(\gamma,\gamma']}
    \sup_{\gamma\le t\le\gamma'}D_\gamma(1-t)
                      \log(\gamma'/\gamma)
 \le D_{b_1}(1)-1+\frac1{10}.
\end{equation}$$ In fact these sums converge to $\int_{b_1}^{1/2-\kappa}D_\alpha(1-\alpha)\,d\alpha/\alpha$: on this fixed compact range, replacing $\gamma$ and $t$ by the same point changes the continuous integrand uniformly by a quantity tending to zero with the mesh. Positivity and (8.10) then give (8.24).

Prescribe a Type II saving $D_*>C_A+4$ and a congruence saving $D_{\mathrm{cg}}>C_A+4$. Apply Theorem 6.1 with $b_*$ and coefficient bound one, obtaining its required fixed discrepancy exponent $B$. Only now fix $S_1>2B+3$ and define the proxies by (8.5). All these parameters, including any prime number theorem accuracies in the proxy inputs, are fixed before $x$ tends to infinity.

**Lemma 8.5** (Replacement on the required factor ranges). *In all factor sums used below, a test $I$ on either factor of $mn=N_u$ can be replaced by $B_I$ with total error $o(X_A/L)$, provided the coefficient on the other factor has absolute value at most one. This holds also when that other coefficient is a proxy.*

*Proof.* For the unbalanced sums, the prime factor $n$ is in $(x^{b_1},x^{1/2-\kappa}]$, and the complementary factor lies between fixed positive multiples of $x^{1/2+\kappa}$ and $x^{1-b_1}$. For the balanced sums both factors are in $\mathcal B_\kappa$. Thus every contributing factor dyad, after intersecting with its actual interval, has scale between $x^{b_1/3}$ and $x^{1-b_1/3}$ for sufficiently large $x$. The actual factor ranges also lie inside the ambient proxy interval. The fixed gaps in these exponent inequalities absorb all dyadic endpoint constants.

On a dyad use $(I-B_I)\mathbf{1}_K$ as the first sequence in Theorem 6.1, where $K$ is the actual summation interval. Lemma 8.2 supplies its rough support, coefficient bound, and discrepancy. Exchange the factor names when the test is on the second factor. The theorem requires only boundedness of the companion sequence, so a nonsmooth proxy is permitted. There are $O(L)$ contributing dyadic pairs for each of the fixed finitely many tests. The total error is therefore $O(xL^{-D_*+1})=o(X_A/L)$ by (8.1). The full-cell normalization is retained when $K$ cuts a cell. In particular, neither $B$ nor the coefficient exponent used in the Type II theorem depends on $S_1$. ◻

### Presieving and unbalanced composites

For odd squarefree $d$ write, as in the congruence theorem, $$r(d)=\sum_{d\mid N_u}a_x(u)-\frac{X_A}{\varphi(d)}.$$ Theorem 7.1, with the already fixed $\vartheta,D_{\mathrm{cg}}$, gives $$\begin{equation}
\tag{8.25}
 \sum_{\substack{d\le x^\vartheta\\d\text{ odd and squarefree}}}
       |r(d)|
 \ll xL^{-D_{\mathrm{cg}}}+X_AL^{-18}=o(X_A/L).
\end{equation}$$

**Lemma 8.6** (Initial sifted mass). *For sufficiently small fixed $b_1$, $$\begin{equation}
\tag{8.26}
 \sum_{P^-(N_u)>x^{b_1}}a_x(u)
 \ge\frac{\mathfrak S X_A}{L}
       \left\{\frac{e^{-\gamma_E}}{b_1}
                    (1-O(e^{-c/b_1}))+o(1)\right\}.
\end{equation}$$*

*Proof.* Apply Lemma 8.1 to the nonnegative weights $a_x(u)$, with bad condition $p\mid N_u$ at odd primes $p\le z=x^{b_1}$. Its density is $g(p)=1/(p-1)$, at most $1/2$; the sums of these densities over $(w,w^2]$ are bounded. Take $$h=2\left\lfloor\frac1{40b_1}\right\rfloor.$$ Making $b_1$ small ensures that this even integer is sufficiently large for the two-sided sieve. Its level satisfies $$b_1(4h+2)\le\frac15+2b_1<\vartheta.$$ Thus (8.25) supplies the full remainder sum. Since $N_u$ is odd, avoiding the specified odd primes is exactly $P^-(N_u)>x^{b_1}$. Finally use (8.4) and $e^{-h}=O(e^{-c/b_1})$ in (8.2). ◻

**Lemma 8.7** (Conditional small-prime sieve). *For each fixed bin $(\gamma,\gamma']$ of the chosen partition, $$\begin{equation}
\tag{8.27}
 \sum_{\substack{x^\gamma<n\le x^{\gamma'}\\n\text{ prime}}}
       \sum_{\substack{n\mid N_u\\P^-(N_u)>W}}a_x(u)
 =X_AV_1(W)\{\log(\gamma'/\gamma)+o(1)\}.
\end{equation}$$*

*Proof.* Fix such a prime $n$. For each odd squarefree $d$ supported on primes at most $W$, one has $n>W$ for sufficiently large $x$, and $$\sum_{nd\mid N_u}a_x(u)
   =\frac{X_A}{(n-1)\varphi(d)}+r(nd).$$ Apply Lemma 8.1 on the objects with $n\mid N_u$, using base mass $X_A/(n-1)$, local density $1/(p-1)$, and $h=2\lceil T^2\rceil$. Its stated growing-$h$ uniformity applies; the level for $d$ is $$D_W=W^{4h+2}=\exp(O(\sqrt L\,T^2))=x^{o(1)}.$$ Every product $nd$ used is at most $x^{1/2-\kappa+o(1)}<x^\vartheta$.

Crucially, the map $(n,d)\mapsto nd$ is injective, since $n$ is the unique prime divisor of $nd$ exceeding $W$. This remains true when the sums are taken over all the disjoint bins. The sieve polynomials have coefficients of absolute value at most one, so the sum of the remainders over all $n$ and $d$ is bounded by the single sum (8.25), with no divisor multiplicity. It is $o(X_AV_1(W))$, since $V_1(W)\asymp L^{-1/2}$. The main terms are $$X_AV_1(W)(1+O(e^{-h}))
          \sum_{\substack{x^\gamma<n\le x^{\gamma'}\\n\text{ prime}}}
                         \frac1{n-1}.$$ Partial summation from the prime number theorem gives the last sum as $\log(\gamma'/\gamma)+o(1)$, proving the result. ◻

**Lemma 8.8** (Removal of unbalanced composites). *The weight of prime values $N_u$, together with composite values whose least prime factor exceeds $x^{1/2-\kappa}$, is at least $$\begin{equation}
\tag{8.28}
 \frac{\mathfrak S X_A}{2L}
\end{equation}$$ for sufficiently large $x$ after $b_1$ is chosen sufficiently small.*

*Proof.* If a presieved composite has least prime factor $n\in(x^\gamma,x^{\gamma'}]$, every prime factor of $m=N_u/n$ is at least $n>x^\gamma$. This includes a repeated occurrence of $n$. Its weight is therefore bounded above by the sum over $mn=N_u$ of $I_\gamma(m)\mathbf{1}_{x^\gamma<n\le x^{\gamma'},\ n\text{ prime}} a_x(u)$. Other divisors counted by this sum merely increase the upper bound.

Replace $I_\gamma$ by $B_\gamma$ using Lemma 8.5, and use (8.9). Because $n>W$, $P^-(m)>W$ is equivalent to $P^-(N_u)>W$; no coprimality between $m$ and $n$ is needed. Lemma 8.7 and (8.4) bound the weight removed for this bin by $$\frac{\mathfrak S X_A}{L}
 \left\{\sup_{\gamma\le t\le\gamma'}D_\gamma(1-t)
                       \log(\gamma'/\gamma)+o(1)\right\},$$ apart from the total $o(X_A/L)$ replacement error. Summing over the fixed mesh and using (8.24) bounds the total removed weight by $$\frac{\mathfrak S X_A}{L}
       \{D_{b_1}(1)-1+1/10+o(1)\}.$$ Subtract this from Lemma 8.6. By (8.11), the coefficient of $\mathfrak S X_A/L$ left over is at least $$1-\frac1{10}-O(b_1^{-1}e^{-c/b_1})+o(1).$$ Choose $b_1$ so small that this is greater than $1/2$ for sufficiently large $x$. This choice also satisfies the initial sieve conditions. The surviving presieved values are exactly among the two classes in the assertion, so their weight proves (8.28). ◻

### Balanced composites and the conclusion

**Lemma 8.9** (Balanced composite bound). *With the constant fixed in (8.22), the weight of composite $N_u$ with $P^-(N_u)>x^{1/2-\kappa}$ is at most $$\begin{equation}
\tag{8.29}
 C_{\mathrm{bal}}(\kappa+1/L)\frac{X_A}{L}+o(X_A/L).
\end{equation}$$*

*Proof.* Such a composite has exactly two prime factors counted with multiplicity: three would give $N_u>x^{3(1/2-\kappa)}>4x+1$. Both factors lie in $\mathcal B_\kappa$ for sufficiently large $x$, since the larger one is at most $(4x+1)x^{-1/2+\kappa}<x^{1/2+2\kappa}$. Ordered prime pairs cover every such composite at least once; distinct primes give two pairs and a repeated prime gives one. Thus their total weight is bounded by $$\sum_{\substack{mn=N_u\\m,n\in\mathcal B_\kappa}}
              I_{\mathrm{pr}}(m)I_{\mathrm{pr}}(n)a_x(u).$$ Use the exact identity $$I_{\mathrm{pr}}(m)I_{\mathrm{pr}}(n)
       -B_{\mathrm{pr}}(m)B_{\mathrm{pr}}(n)
 =(I_{\mathrm{pr}}-B_{\mathrm{pr}})(m)I_{\mathrm{pr}}(n)
   +B_{\mathrm{pr}}(m)(I_{\mathrm{pr}}-B_{\mathrm{pr}})(n).$$ Lemma 8.5 applies to the two terms in turn, exchanging factor roles in the second. Both companion sequences have absolute value at most one, independently of $S_1$. The resulting positive proxy sum is, by (8.7), at most $$\begin{equation}
\tag{8.30}
 \frac{C_{\mathrm{pr}}^2}{L^2V(W)^2}
 \sum_{\substack{mn=N_u,\ m,n\in\mathcal B_\kappa\\
                  P^-(m),P^-(n)>W}}a_x(u).
\end{equation}$$ Apply (8.21) and (8.22), and add the $o(X_A/L)$ replacement error. This proves (8.29). ◻

*Proof of Theorem 1.1.* Combining Lemmas 8.8 and 8.9 gives $$\sum_{N_u\text{ prime}}a_x(u)
 \ge\left(\frac{\mathfrak S}{2}
               -C_{\mathrm{bal}}\kappa-o(1)\right)\frac{X_A}{L}
 \gg\frac{X_A}{L},$$ by (8.23). Lemma 5.3 removes only $o(X_A/L)$ from this mass. Consequently there is a supported $u$ with $2u+1$ prime and $2u$ squarefree.

For completeness, the support condition counts prime factors with their multiplicities. The ordinary part $u_*$ has $r_0(j_x+1)$ prime factors, an even number because $r_0$ is even. The factor $(1-\mathcal E(u))/2$ in $A(u)$ imposes an odd total multiplicity on the group-prime part. Hence $\Omega(u)$ is odd. Every supported $u$ is odd, so $\Omega(2u)=1+\Omega(u)$ is even. On the retained squarefree predecessors this is also an even number of distinct prime factors. Finally $u\in[x,2x]$ wherever $a_x(u)>0$; the resulting primes exceed $x$ for arbitrarily large $x$, proving infinitude. ◻

The order of choices is intrinsic to the argument: the original weight data and the micro-band choices determine $C_{\mathrm{box}}$ and $C_{\mathrm{bal}}$; then come $\kappa$, $b_1$, the finite mesh, the distribution savings and their discrepancy exponent, and finally $S_1$. All thresholds for $x$ are imposed afterwards. In particular the absolute prime-proxy constant and the coefficient bound one, rather than any precision-dependent regularity, are what make this order valid.

## References

**[1]** R. C. Baker and G. Harman, *Shifted primes without large prime factors*, Acta Arith. **83** (1998), no. 4, 331–361. [doi:10.4064/aa-83-4-331-361](https://doi.org/10.4064/aa-83-4-331-361).

**[2]** J. Friedlander and H. Iwaniec, *Asymptotic sieve for primes*, Ann. of Math. (2) **148** (1998), no. 3, 1041–1065. [doi:10.2307/121035](https://doi.org/10.2307/121035); [arXiv:math/9811186v1](https://arxiv.org/abs/math/9811186v1).

**[3]** J. D. Lichtman, *Primes in arithmetic progressions to large moduli, and shifted primes without large prime factors*, [arXiv:2211.09641v1](https://arxiv.org/abs/2211.09641v1), 14 November 2022.

**[4]** OpenAI, *Weighted dilation graphs, smooth shifted primes and totient fibers*, OpenAI Math Release preprint [OAI:Weighted-Dilation-Graphs-Smooth-Shifted-Primes-and-Totient-Fibers-September-24-2026](https://github.com/openai/math/blob/main/preprints/Weighted-Dilation-Graphs-Smooth-Shifted-Primes-and-Totient-Fibers-September-24-2026/paper.pdf), 2026.

**[5]** T. D. Wooley, *Vinogradov’s mean value theorem via efficient congruencing*, Ann. of Math. (2) **175** (2012), 1575–1627. [doi:10.4007/annals.2012.175.3.12](https://doi.org/10.4007/annals.2012.175.3.12).
