# Residue Class Patterns of Consecutive Primes

Cheuk Fung (Joshua) Lau

## Abstract.

Dickson’s conjecture and the Hardy–Littlewood prime tuple conjecture predict that every pattern of reduced residue classes modulo $q$ is attained by infinitely many strings of $m$ consecutive primes. At present, however, even proving that a single non-constant residue class pattern of length $m$ occurs infinitely often is beyond the reach of existing methods. Combining Dirichlet’s theorem on primes in arithmetic progressions with a theorem of Shiu (2000) shows that, for any $m,q\in\mathbb{N}$ with $q\geq 3$, at least $m\varphi(q)$ residue class patterns of length $m$ are attained by infinitely many consecutive primes.\

In this paper, we prove that if $q$ is squarefree, every prescribed sequence of at least $60m\log m$ reduced residue classes mod $q$ contains, in order, an $m$-term block pattern that occurs infinitely often among consecutive primes, with each constant block of length at most $\lceil\log m\rceil$. A recursive combinatorial argument then shows that if $q$ is squarefree and $q\gg(\log m)^{2}$, then at least

$$\gg\frac{m}{(\log m)^{10}}\varphi(q)^{2}$$

residue class patterns of length $m$ occur infinitely often among consecutive primes. Moreover, we also show that if $q$ is squarefree and $q\gg(\log m)^{2}$, then at least

$$\gg e^{-O(m\log_{2}m/\log m)}\varphi(q)^{m/\lceil\log m\rceil}$$

residue class patterns of length $m$ occur infinitely often among consecutive primes. The proof consists of a modification of the Maynard–Tao sieve found in Banks, Freiberg, and Maynard (2016), by considering the $r$-th moment instead of the 2nd moment for an integer $r$ depending on $m$, which is then combined with an Erdős–Rankin type construction.

*Key words and phrases:* prime numbers, sieve methods, residue classes

*2020 Mathematics Subject Classification* Primary 11N05, 11N13; Secondary 11N36

## 1. Introduction

A central theme in analytic number theory is that, after accounting for the obvious local congruence obstructions, the prime numbers should behave like a random set. This philosophy underlies the Hardy–Littlewood prime tuple conjecture and predicts that every admissible local pattern of primes should occur infinitely often. One way to study this phenomenon is to examine the residue classes of consecutive primes modulo a fixed integer $q$.\

For $q,m\in\mathbb{N}$ with $q\geq 2$, $x\in\mathbb{R}$ and $\mathbf{a}\in\prod_{i=1}^{m}(\mathbb{Z}/q\mathbb{Z})^{\times}$, define

$$\pi(x;q,\mathbf{a})=\#\{p_{n}\leq x:p_{n+i-1}\equiv a_{i}\pmod{q}\text{ for all }i=1,2,\ldots,m\},$$

where $p_{i}$ denotes the $i$-th prime. Thus $\pi(x;q,\mathbf{a})$ counts occurrences of a prescribed residue class pattern among $m$ consecutive primes.\

Understanding these patterns is closely related to the broader question of how randomly distributed consecutive primes are. Numerical investigations and probabilistic models suggest that, apart from congruence restrictions, every residue class pattern should occur infinitely often. A consequence of Dickson’s conjecture states the following.

**Conjecture 1.1.** For any $q,m\in\mathbb{N}$ with $q\geq 2$ and $\mathbf{a}\in\prod_{i=1}^{m}(\mathbb{Z}/q\mathbb{Z})^{\times}$, $\pi(x;q,\mathbf{a})\to\infty$ as $x\to\infty$. Equivalently,

$$\#\left\{\mathbf{a}\in\prod_{i=1}^{m}(\mathbb{Z}/q\mathbb{Z})^{\times}:\pi(x;q,\mathbf{a})\to\infty\text{ as }x\to\infty\right\}=\varphi(q)^{m}.$$

Additionally, the Hardy–Littlewood prime tuple conjecture predicts the quantitative asymptotic behaviour of $\pi(x;q,\mathbf{a})$. Recently, more refined heuristics were developed by Lemke Oliver and Soundararajan (2016). Their work predicts substantial biases for finite ranges, for example, consecutive primes tend to avoid repeating the same residue class modulo $q$ more often than naive randomness would suggest, but these biases are expected to disappear asymptotically.\

Despite these strong heuristic predictions, our current understanding remains extremely limited. Dirichlet’s theorem on primes in arithmetic progressions states that $\pi(x;q,a)\to\infty$ as $x\to\infty$ for any $a\in(\mathbb{Z}/q\mathbb{Z})^{\times}$, so Conjecture 1.1 is known when $m=1$. For general $m\in\mathbb{N}$, we have the following result of Shiu (2000).

**Theorem 1.2 (Shiu).** For any $m,q\in\mathbb{N}$ with $q\geq 2$ and $a\in(\mathbb{Z}/q\mathbb{Z})^{\times}$, let $\mathbf{a}=(a,\ldots,a)\in\prod_{i=1}^{m}(\mathbb{Z}/q\mathbb{Z})^{\times}$. Then, $\pi(x;q,\mathbf{a})\to\infty$ as $x\to\infty$.

Moreover, Maynard (2016) proved that $\pi(x;q,(a,\ldots,a))\gg\pi(x)$. However, even proving that a single non-constant residue class pattern of length $m$ occurs infinitely often among consecutive primes is beyond the reach of existing methods. In an easier setting of consecutive sums of two squares instead of primes, Kimmel and Kuperberg (2024); Kimmel and Kuperberg (2025) considered

$$\mathbf{E}=\{c^{2}+d^{2}:c,d\in\mathbb{N}\}=\{E_{n}:n\in\mathbb{N}\},$$

and call $a\in\mathbb{Z}/q\mathbb{Z}$ $\mathbf{E}$-admissible if there is $c,d\in\mathbb{N}$ such that $c^{2}+d^{2}\equiv a\ (\mathrm{mod}\ q)$. For an $m$-tuple of admissible residue classes $\mathbf{a}=(a_{1},...,a_{m})\in(\mathbb{Z}/q\mathbb{Z})^{m}$, let

$$N(x,q,\mathbf{a})=\#\{E_{n}\leq x:E_{n+i-1}\equiv a_{i}\ (\mathrm{mod}\ q)\ \forall 1\leq i\leq m\}.$$

Kimmel and Kuperberg (2024) proved that for any $q\in\mathbb{N}$ with $q\geq 2$ and $a_{1},a_{2},a_{3}\in\mathbb{Z}/q\mathbb{Z}$ $\mathbf{E}$-admissible, $N(x,q,(a_{1},a_{2},a_{3}))\to\infty$ as $x\to\infty$. For a general $m\in\mathbb{N}$ and squarefree $q\in\mathbb{N}$, Kimmel and Kuperberg (2025) proved that for any $m$-tuple $\mathbf{a}$ that is a concatenation of two constant tuples $(a_{1},\ldots,a_{1})$ and $(a_{2},\ldots,a_{2})$ with $a_{1},a_{2}\in(\mathbb{Z}/q\mathbb{Z})^{\times}$, we have $N(x,q,\mathbf{a})\to\infty$ as $x\to\infty$. Even in this easier setting, we are very far from proving that all $\mathbf{E}$-admissible tuples of residue classes are indeed attained by infinitely many consecutive sums of two squares.\

In this paper, we investigate the number of residue class patterns that are attained by infinitely many consecutive primes. One may use Dirichlet’s theorem to show that for any $q,m\in\mathbb{N}$ with $q\geq 2$, there are at least $\varphi(q)$ many $m$-tuples $\mathbf{a}\in\prod_{i=1}^{m}(\mathbb{Z}/q\mathbb{Z})^{\times}$ such that $\pi(x;q,\mathbf{a})\to\infty\text{ as }x\to\infty.$ Using Shiu (2000) along with Dirichlet’s theorem, we may obtain a better lower bound.

**Proposition 1.3.** For any $q,m\in\mathbb{N}$ with $q\geq 3$, there are at least $m\varphi(q)$ many $m$-tuples $\mathbf{a}\in\prod_{i=1}^{m}(\mathbb{Z}/q\mathbb{Z})^{\times}$ such that $\pi(x;q,\mathbf{a})\to\infty\text{ as }x\to\infty.$

*Proof.* For each $a\in(\mathbb{Z}/q\mathbb{Z})^{\times}$, Shiu’s theorem states $\pi(x;q,(a,\ldots,a))\to\infty$ as $x\to\infty$. By Dirichlet’s theorem, we know that each string of consecutive primes all congruent to $a\pmod{q}$ must terminate. Since $\varphi(q)\geq 2$, by the pigeonhole principle there must exist $a^{\prime}\in(\mathbb{Z}/q\mathbb{Z})^{\times}$ with $a^{\prime}\neq a$ such that $\pi(x;q,(a,\ldots,a,a^{\prime}))\to\infty$ as $x\to\infty$. Repeating this ‘shifting’ argument $m-1$ more times, we obtain for each $a\in(\mathbb{Z}/q\mathbb{Z})^{\times}$ there are $m$ many $m$-tuples attained by infinitely many consecutive primes. By considering the first entry, the $m$-tuples obtained in this way for distinct $a\in(\mathbb{Z}/q\mathbb{Z})^{\times}$ are distinct, so in total we can obtain at least $m\varphi(q)$ such tuples. ∎

In fact, this lower bound is optimal if the only property of primes we use is Theorem 1.2. Let $q\in\mathbb{Z}_{>1}$, and let $(\mathbb{Z}/q\mathbb{Z})^{\times}=\{c_{1},\ldots,c_{\varphi(q)}\}$. Consider the sequence

$$\begin{aligned}b_{n}&=c_{k},\text{ where }k-1<n\leq k,\ 1\leq k\leq\varphi(q),\\ b_{\varphi(q)+n}&=c_{k},\text{ where }2(k-1)<n\leq 2k,\ 1\leq k\leq\varphi(q),\\ b_{3\varphi(q)+n}&=c_{k},\text{ where }3(k-1)<n\leq 3k,\ 1\leq k\leq\varphi(q),\end{aligned}$$

and so on, i.e.

$$b_{r(r-1)\varphi(q)/2+n} =c_{k},\text{ where }(k-1)r<n\leq kr,\ 1\leq k\leq\varphi(q),\ r\geq 1.$$

For $m\in\mathbb{N}$ and $\mathbf{a}=(a_{1},\ldots,a_{m})\in\prod_{i=1}^{m}(\mathbb{Z}/q\mathbb{Z})^{\times}$, define the corresponding counting function

$$\widetilde{\pi}_{q}(x;\mathbf{a})=\#\{b_{n}\leq x:b_{n+i-1}\equiv a_{i}\ (\mathrm{mod}\ q)\text{ for all }i=1,2,\ldots,m\}.$$

We observe that for any $m\in\mathbb{N}$, $a\in(\mathbb{Z}/q\mathbb{Z})^{\times}$, and $\mathbf{a}=(a,\ldots,a)\in\prod_{i=1}^{m}(\mathbb{Z}/q\mathbb{Z})^{\times}$, the sequence $(b_{n})_{n=1}^{\infty}$ satisfies $\widetilde{\pi}_{q}(x;\mathbf{a})\to\infty$ as $x\to\infty$. However, there are exactly $m\varphi(q)$ many $m$-tuples $\mathbf{a}\in\prod_{i=1}^{m}(\mathbb{Z}/q\mathbb{Z})^{\times}$ such that $\widetilde{\pi}_{q}(x;\mathbf{a})\to\infty$ as $x\to\infty$, namely

$$(\underbrace{c_{t},\ldots,c_{t}}_{r\text{ times}},\underbrace{c_{t+1},\ldots,c_{t+1}}_{m-r\text{ times}})\in\prod_{i=1}^{m}(\mathbb{Z}/q\mathbb{Z})^{\times},\quad 1\leq r\leq m,\quad 1\leq t\leq\varphi(q),\quad c_{\varphi(q)+1}:=c_{1}.$$

For general $m\in\mathbb{N}$, despite knowing that $m\varphi(q)$ tuples of residue classes are attained by infinitely many consecutive primes, it is currently not known whether any other specific tuple of residue classes is attained by infinitely many consecutive primes. To state our main results, we make the following definitions.

**Definition 1.4.** For a squarefree integer $q\geq 2$, $m\in\mathbb{Z}^{+}$, and $A\subseteq\prod_{i=1}^{m}(\mathbb{Z}/q\mathbb{Z})^{\times}$, define

$$\pi(x;q,A)=\#\{p_{n}\leq x:(p_{n}\ \mathrm{mod}\ q,\ldots,p_{n+m-1}\ \mathrm{mod}\ q)\in A\}.$$

Also, for $r\in\mathbb{Z}^{+}$ with $r>1$, define

$$M{}=\left\lceil\left(\frac{2^{3r-2}(r-1)^{2r-1}}{r!}\right)^{\frac{1}{r-1}}m(m(r-1)+r)^{\frac{1}{r-1}}\right\rceil,$$

and define the set of functions

$$J_{r}(m,M)=\{j:\{1,\ldots,m\}\to\{1,\ldots,M\}:j(i+1)\geq j(i),\text{ no consecutive $r$ values }j(i)\text{ are equal}\}.$$

The main result of this paper is the following theorem, proven in Section 7.

**Theorem 1.5.** Let $q$ be a squarefree integer, and $r,m\in\mathbb{Z}^{+}$ with $r>1$. Recall $\pi(x;q,A)$, $M$, and $J_{r}(m,M)$ from Definition 1.4. For any $a_{1},\ldots,a_{M{}}\in(\mathbb{Z}/q\mathbb{Z})^{\times}$, let

$$A=\{(c_{1},\ldots,c_{m}):\exists j\in J_{r}(m,M)\text{ s.t. }c_{i}=a_{j(i)}\forall 1\leq i\leq m\}.$$

Then $\pi(x;q,A)\to\infty$ as $x\to\infty$.

Using this, one can argue combinatorially to obtain the following result for $q$ in ‘medium’ range, which is proven in Section 8.

**Corollary 1.6.** For any $0<c<1$, if $q\geq 2$ is squarefree and $\varphi(q)>8c^{-1}e^{2}(\log m)^{2}$, then for $m$ sufficiently large,

$$\#\left\{\mathbf{a}\in\prod_{i=1}^{m}(\mathbb{Z}/q\mathbb{Z})^{\times}:\lim_{x\to\infty}\pi(x;q,\mathbf{a})=\infty\right\}\geq\frac{\lfloor(1-c)m\rfloor c^{5}}{256e^{10}(\log m)^{10}}\varphi(q)(\varphi(q)-1).$$

Choosing $c=5/6$, this gives a better lower bound than that of Proposition 1.3 when

$$\varphi(q)>3823e^{10}(\log m)^{10}+1.$$

In Section 8, we also obtain a corresponding lower bound when $q$ is in a ‘large’ range.

**Corollary 1.7.** For $m,r\in\mathbb{Z}^{+}$, recall $M$ from Definition 1.4. If $q\geq 2$ is squarefree and $\varphi(q)\geq M{}$, there are at least

$$\frac{\lceil m/(r-1)\rceil!}{M{}(M{}-1)\cdots(M{}-\lceil m/(r-1)\rceil+1)}\cdot\varphi(q)(\varphi(q)-1)\cdots(\varphi(q)-\lceil m/(r-1)\rceil+1)$$

$m$-tuples $\mathbf{a}$ such that $\pi(x;q,\mathbf{a})\to\infty$ as $x\to\infty$.

For example, for $m=2$, we may choose $r=2$ in Corollary 1.7 to show that for any $q$ squarefree and $\varphi(q)\geq 64$,

$$\#\{(a_{1},a_{2})\in(\mathbb{Z}/q\mathbb{Z})^{\times}\times(\mathbb{Z}/q\mathbb{Z})^{\times}:\lim_{x\to\infty}\pi(x;q,(a_{1},a_{2}))=\infty\}\geq\frac{1}{2016}\varphi(q)(\varphi(q)-1).$$

In particular, when $\varphi(q)>4033$, we beat the lower bound in Proposition 1.3. This misses the conjectured lower bound of $\varphi(q)^{2}$ by a constant. Putting $r=\lceil\log m+1\rceil$ in Corollary 1.7, we get

**Corollary 1.8.** If $q\geq 2$ is squarefree and $\varphi(q)>8e^{2}m\log m$, then for $m$ sufficiently large,

$$\#\left\{\mathbf{a}\in\prod_{i=1}^{m}(\mathbb{Z}/q\mathbb{Z})^{\times}:\lim_{x\to\infty}\pi(x;q,\mathbf{a})=\infty\right\}\gg e^{-O(m\log_{2}m/\log m)}\varphi(q)^{m/\lceil\log m\rceil}.$$

In both corollaries, we chose $r=\lceil\log m+1\rceil$. Heuristically this is because for $m$ large, we have $M=\Theta(r^{1+o(1)}m^{1+1/r+o(1/r)})$. To minimise $M$, we choose $r\approx\log m$.

## 2. Outline

The proof of Theorem 1.5 has two main ingredients. First, in Section 5 we develop a modification of the Maynard–Tao sieve which guarantees the existence of several clusters of primes satisfying prescribed spacing conditions. Second, in Section 6 we adapt the Erdős–Rankin construction so that these clusters consist of consecutive primes lying in prescribed residue classes modulo $q$. Combining these two ingredients yields Theorem 1.5, from which the lower bounds for the number of attainable residue class patterns follow by a combinatorial argument in Section 8.\

A finite set of integers $\mathcal{H}$ is said to be *admissible* if for every prime $p$,

$$\#\left\{n\ (\mathrm{mod}\ p):\prod_{h\in\mathcal{H}}(n+h)\equiv 0\ (\mathrm{mod}\ p)\right\}<p.$$

Fix $m,r\in\mathbb{Z}^{+}$ with $r>1$, and let $q$ be squarefree. Define the parameter $M$ as in Definition 1.4. For sufficiently large $N$, let $W$ denote the usual product of small primes appearing in the Maynard–Tao sieve. We also introduce the Maynard–Tao sieve weights

$$w_{n}=\left(\sum_{\begin{subarray}{c}d_{1},\ldots,d_{k}\\
d_{i}\mid qn+h_{i}\end{subarray}}\lambda_{d_{1},\ldots,d_{k}}\right)^{2},$$

where the coefficients $\lambda_{d_{1},\ldots,d_{k}}$ are defined in Section 5. Our main sieve result (Proposition 5.6) states that if $\mathcal{H}=\{h_{1},\ldots,h_{k}\}\subset[0,N]$ is an admissible $k$-tuple whose pairwise differences are $\varepsilon\log N$-smooth, then one can choose a residue class $b\ (\mathrm{mod}\ W)$ satisfying suitable local congruence conditions so that, for any partition

$$\mathcal{H}=\mathcal{H}_{1}\cup\cdots\cup\mathcal{H}_{M}$$

into equal-sized subsets, there exists $n\in[N,2N]$ for which $m+1$ of the sets $qn+\mathcal{H}_{i}$ each contain between $1$ and $r-1$ primes, while every intermediate block contains no primes.\

The proof of Proposition 5.6 follows the ideas of Banks et al. (2016) and Merikoski (2020). Observe that it suffices to establish the positivity of the sum

$$\begin{align*}S=\sum_{N<n\leq 2N}\Bigg(&\sum_{i=1}^{k}\bm{1}_{\mathbb{P}}(qn+h_{i})-m(r-1){}\\ &-(m(r-1)+r)\sum_{j=1}^{M}{}\sum_{\begin{subarray}{c}h_{j_{1}},\ldots,h_{j_{r}}\in\mathcal{H}_{j}\\
j_{1}<\cdots<j_{r}\end{subarray}}\prod_{i=1}^{r}\bm{1}_{\mathbb{P}}(qn+h_{j_{i}})\Bigg)w_{n}. \tag{2.1}\end{align*}$$

To do this, in Lemma 5.5 we first establish estimates for the total weight, the weighted count of primes, and the weighted $r$-fold correlations

$$\begin{aligned}&\sum_{\begin{subarray}{c}N<n\leq 2N\\
n\equiv b\;(\bmod W)\end{subarray}}w_{n},\\ &\sum_{\begin{subarray}{c}N<n\leq 2N\\
n\equiv b\;(\bmod W)\end{subarray}}\mathbf{1}_{\mathbb{P}}(qn+h_{j})\,w_{n},\\ &\sum_{\begin{subarray}{c}N<n\leq 2N\\
n\equiv b\;(\bmod W)\end{subarray}}\mathbf{1}_{\mathbb{P}}(qn+h_{j_{1}})\cdots\mathbf{1}_{\mathbb{P}}(qn+h_{j_{r}})\,w_{n}.\end{aligned}$$

These estimates are then combined to prove the positivity of (2.1).\

To apply Proposition 5.6, Section 6 develops a modified Erdős–Rankin construction. Given prescribed residue classes $r_{1},...,r_{k}\ (\mathrm{mod}\ q)$, in Lemma 6.2 we construct an admissible tuple $\{h_{1},\ldots,h_{k}\}$ with $h_{i}\equiv r_{i}\ (\mathrm{mod}\ q)$, whose pairwise differences are $\varepsilon\log N$-smooth, together with the required residue class $b\ (\mathrm{mod}\ W)$. This construction also ensures that the primes detected by the sieve are consecutive, completing the proof of Theorem 1.5.\

Finally, Section 8 uses Theorem 1.5 in a recursive combinatorial argument to obtain lower bounds for the number of residue class patterns attained by infinitely many consecutive primes.

## 3. Acknowledgements

We would like to thank Jori Merikoski for suggesting this question, and for numerous helpful comments throughout the writing of this paper.

## 4. Notation

Throughout this paper, we use $\lfloor x\rfloor$ to denote the largest integer not greater than $x$, and $\lceil x\rceil$ to denote the least integer not less than $x$. We say $f\ll g$ and $f=O(g)$ when there exists a constant $C>0$ such that $|f(x)|\leq Cg(x)$ for $x$ sufficiently large. If the implied constant depends on parameter $\varepsilon$ say, then we write $f\ll_{\varepsilon}g$ or $f=O_{\varepsilon}(g)$. We use $f=o(g)$ to mean $\lim_{x\to\infty}f(x)/g(x)=0$.\

Sums of the form $\sum_{p}$ range over primes, and $\mathbb{P}$ denotes the set of primes. We use $\bm{1}_{\mathbb{P}}(n)$ to denote the indicator function of whether $n\in\mathbb{P}$. Given integers $d_{1},d_{2}$ we use $\operatorname{gcd}(d_{1},d_{2})$ or $(d_{1},d_{2})$ to denote the greatest common divisor of $d_{1}$ and $d_{2}$, and $\operatorname{lcm}(d_{1},d_{2})$ or $[d_{1},d_{2}]$ to denote the least common multiple of $d_{1}$ and $d_{2}$. For a positive integer $q>1$, denote by $P^{+}(q)$ the largest prime factor of $q$. We use $\varphi(q)$ to denote the Euler totient function of $q$. Given integers $k$ and $n$, $\log_{k}n$ denotes the $k$-fold iterated logarithm of $n$ in base $e$, for example $\log_{1}n=\log n$ and $\log_{2}n=\log\log n$.

## 5. A Modified Maynard–Tao Sieve

In order to use the methods of Banks et al. (2016), we need the following results.

**Lemma 5.1.** Let $T\geq 3$ and $P\geq T^{1/\log_{2}T}$. Among all primitive characters $\chi\ (\mathrm{mod}\ q)$ with $q\leq T$ and $P^{+}(q)\leq P$, there exists at most one such character such that $L(s,\chi)$ has a zero in the region

$$\Re(s)>1-\frac{c}{\log P},\quad|\Im(s)|\leq\exp\left(\log P/\sqrt{\log T}\right),$$

where $c$ is a positive absolute constant. If this character $\chi\ (\mathrm{mod}\ q)$ exists and is real, then $L(s,\chi)$ has precisely one zero in the above region, which is simple and real, and satisfies

$$P^{+}(q)\gg\log q\gg\log_{2}T.$$

*Proof.* This is (Banks et al., 2016, Lemma 4.1). ∎

We fix the absolute constant $c$ in Banks et al. (2016) and define $Z_{T}=P^{+}(q)$ if such exceptional modulus $q$ exists, and set $Z_{T}=1$ otherwise.

**Theorem 5.2 (Modified Bomberi–Vinogradov).** Let $N>2$. Fix any $C>0$, $\theta=1/2-\delta\in(0,1/2)$ and $\varepsilon>0$. Suppose $q_{0}$ is a squarefree integer with $q_{0}<N^{\varepsilon}$ and $P^{+}(q_{0})<N^{\varepsilon/\log_{2}N}$. If $\varepsilon$ is sufficiently small in terms of $C,\delta,c$ in Lemma 5.1, then with $Z_{N^{2\varepsilon}}$ as above we have

$$\sum_{\begin{subarray}{c}q<N^{\theta}\\
q_{0}\mid q\\
(q,Z_{N^{2\varepsilon}})=1\end{subarray}}\max_{(q,a)=1}\left|\psi(N;q,a)-\frac{\psi(N)}{\varphi(q)}\right|\ll_{\delta,C}\frac{N}{\varphi(q_{0})(\log N)^{C}}.$$

*Proof.* This is (Banks et al., 2016, Theorem 4.2). ∎

Given a squarefree integer $q\geq 2$ and an admissible tuple $(h_{1},\ldots,h_{k})$, define the set

$$\mathcal{H}(n)=\{qn+h_{1},\ldots,qn+h_{k}\}.$$

We define the sieve weights $\lambda_{d_{1},\ldots,d_{k}}$ the same way as Banks et al. (2016), i.e.

$$\lambda_{d_{1},\ldots,d_{k}}=\left\{\begin{aligned} \left(\prod_{i=1}^{k}\mu(d_{i})\right)\sum_{j=1}^{J}\prod_{\ell=1}^{k}F_{\ell,j}\left(\frac{\log d_{\ell}}{\log N}\right),&\quad\text{ if }\operatorname{gcd}(d_{1}\cdots d_{k},Z_{N^{4\varepsilon}})=1\\
0,&\quad\text{ otherwise}\end{aligned}\right.$$

for some fixed $J$, where $F_{\ell,j}:[0,\infty)\to\mathbb{R}$ are fixed smooth compactly supported functions that are not identically zero, with support condition

$$\sup\left\{\sum_{\ell=1}^{k}t_{\ell}:\prod_{\ell=1}^{k}F_{\ell,j}(t_{\ell})\neq 0\right\}\leq\delta$$

for all $j=1,2,\ldots,J$ and some small $\delta>0$. Let

$$F(t_{1},\ldots,t_{k}):=\sum_{j=1}^{J}\prod_{\ell=1}^{k}F_{\ell,j}^{\prime}(t_{\ell}),$$

where $F_{\ell,j}^{\prime}$ denotes the derivative of $F_{\ell,j}$. We also assume $F_{\ell,j}$ are chosen such that $F(t_{1},\ldots,t_{k})$ is symmetric. Since $J$ and $F_{\ell,j}$ for $1\leq\ell\leq k$ and $1\leq j\leq J$ are fixed, we have $\lambda_{d_{1},\ldots,d_{k}}\ll 1$ uniformly in $d_{1},\ldots,d_{k}$. We further define

$$w_{n}=\left(\sum_{\begin{subarray}{c}d_{1},\ldots,d_{k}\\
d_{i}\mid qn+h_{i}\end{subarray}}\lambda_{d_{1},\ldots,d_{k}}\right)^{2},$$

and for $\varepsilon>0$ define

$$W=\prod_{\begin{subarray}{c}p\leq\varepsilon\log N\\
p\nmid Z_{N^{4\varepsilon}}\end{subarray}}p,\quad B=\frac{\varphi(W)}{W}\log N.$$

We remark here, for $N$ sufficiently large in terms of $q$, we have $q\mid W$, so

$$\frac{\varphi(qW)}{qW}=\frac{\varphi(W)}{W}.$$

We define the following quantities for $r\in\mathbb{Z}^{+}$ and $k\geq r$

$$\begin{aligned}I_{k}(F)&:=\int_{0}^{\infty}\cdots\int_{0}^{\infty}F(t_{1},\ldots,t_{k})\,\textup{d}t_{1}\cdots\,\textup{d}t_{k},\\ J_{k}^{(r)}(F)&:=\int_{0}^{\infty}\cdots\int_{0}^{\infty}\left(\int_{0}^{\infty}\cdots\int_{0}^{\infty}F(t_{1},\ldots,t_{k})\,\textup{d}t_{k-r+1}\cdots\,\textup{d}t_{k}\right)^{2}\,\textup{d}t_{1}\cdots\,\textup{d}t_{k-r}.\end{aligned}$$

**Lemma 5.3.** Let $N$ be sufficiently large in terms of $q$. If $F_{1},\ldots,F_{k},G_{1},\ldots,G_{k}:[0,\infty)\to\mathbb{R}$ are compactly supported functions, then

$$\sideset{}{{}^{\prime}}{\sum}_{\begin{subarray}{c}d_{1},\ldots,d_{k}\\
d_{1}^{\prime},\ldots,d_{k}^{\prime}\end{subarray}}\prod_{j=1}^{k}\frac{\mu(d_{j})\mu(d_{j}^{\prime})}{[d_{j},d_{j}^{\prime}]}F_{j}\left(\frac{\log d_{j}}{\log N}\right)G_{j}\left(\frac{\log d_{j}^{\prime}}{\log N}\right)=(c+o(1))B^{-k},$$

where $\sum^{\prime}$ denotes the additional restriction of $[d_{1},d_{1}^{\prime}],\ldots,[d_{k},d_{k}^{\prime}],qWZ_{N^{4\varepsilon}}$ being pairwise coprime, and

$$c=\prod_{j=1}^{k}\int_{0}^{\infty}F_{j}^{\prime}(t_{j})G_{j}^{\prime}(t_{j})\,\textup{d}t_{j}.$$

The same result holds if $[d_{j},d_{j}^{\prime}]$ are replaced by $\varphi([d_{j},d_{j}^{\prime}])$, i.e.

$$\sideset{}{{}^{\prime}}{\sum}_{\begin{subarray}{c}d_{1},\ldots,d_{k}\\
d_{1}^{\prime},\ldots,d_{k}^{\prime}\end{subarray}}\prod_{j=1}^{k}\frac{\mu(d_{j})\mu(d_{j}^{\prime})}{\varphi([d_{j},d_{j}^{\prime}])}F_{j}\left(\frac{\log d_{j}}{\log N}\right)G_{j}\left(\frac{\log d_{j}^{\prime}}{\log N}\right)=(c+o(1))B^{-k}.$$

*Proof.* If $N$ is sufficiently large in terms of $q$ such that $Z_{N^{4\varepsilon}}>P^{+}(q)$ and $q\mid W$, then the additional restriction is the same as saying $[d_{1},d_{1}^{\prime}],\ldots,[d_{k},d_{k}^{\prime}],WZ_{N^{4\varepsilon}}$ being pairwise coprime, which is just (Banks et al., 2016, Lemma 4.5). ∎

We have an estimate for $J_{k}^{(r)}(F)$ in terms of $I_{k}(F)$.

**Lemma 5.4.** Let $0<\rho<1$ and $r\in\mathbb{Z}^{+}$ with $2\leq r\leq k$. Then there is a fixed choice of $J$ and $F_{\ell,j}$ for $\ell\in\{1,2,\ldots,k\}$ and $j\in\{1,2,\ldots,J\}$ with the required properties such that

$$\begin{aligned}J_{k}^{(1)}(F)&\geq(1+O((\log k)^{-1/2}))\left(\frac{\rho\delta\log k}{k}\right)I_{k}(F),\\ J_{k}^{(r)}(F)&\leq(1+O((\log k)^{-1/2}))\left(\frac{\rho\delta\log k}{k}\right)^{r}I_{k}(F).\end{aligned}$$

*Proof.* The proof is similar to (Banks et al., 2016, Lemma 4.7). The result is trivial if $k$ is bounded, so assume $k$ is sufficiently large. Define $F_{k}=F_{k}(t_{1},\ldots,t_{k})$ by

$$\begin{aligned}F_{k}(t_{1},\ldots,t_{k})&=\left\{\begin{aligned} \prod_{i=1}^{k}g(kt_{i}),&\quad\text{ if }\sum_{i=1}^{k}t_{i}\leq 1,\\
0,&\quad\text{ otherwise},\end{aligned}\right.\\ g(t)&=\left\{\begin{aligned} \frac{1}{1+At},&\quad\text{ if }t\in[0,T],\\
0,&\quad\text{ otherwise},\end{aligned}\right.\\ A&=\log k-2\log_{2}k,\\ T&=\frac{e^{A}-1}{A}.\end{aligned}$$

The first assertion follows from (Banks et al., 2016, Lemma 4.7). For the second assertion, we will first prove that for all $x\geq 0$ we have

$$\left(\int_{t_{1}+\cdots+t_{r}\leq x}g(t_{1})\cdots g(t_{r})\,\textup{d}t_{1}\cdots\,\textup{d}t_{r}\right)^{2} \leq(\log k)^{r}\int_{t_{1}+\cdots+t_{r}\leq x}g(t_{1})^{2}\cdots g(t_{r})^{2}\,\textup{d}t_{1}\cdots\,\textup{d}t_{r}. \tag{5.1}$$

For $0\leq x\leq\log k$, by Cauchy–Schwarz we have

$$\begin{aligned}\left(\int_{t_{1}+\cdots+t_{r}\leq x}g(t_{1})\cdots g(t_{r})\,\textup{d}t_{1}\cdots\,\textup{d}t_{r}\right)^{2}&\leq\frac{x^{r}}{2^{r}}\int_{t_{1}+\cdots+t_{r}\leq x}g(t_{1})^{2}\cdots g(t_{r})^{2}\,\textup{d}t_{1}\cdots\,\textup{d}t_{r}\\ &\leq(\log k)^{r}\int_{t_{1}+\cdots+t_{r}\leq x}g(t_{1})^{2}\cdots g(t_{r})^{2}\,\textup{d}t_{1}\cdots\,\textup{d}t_{r}.\end{aligned}$$

We now prove (5.1) for $x\geq\log k$. Let $y=\min(x,T)$ and note $\log(1+Ay)\leq A$. Hence

$$\begin{aligned}\int_{t_{1}+\cdots+t_{r}\leq x}g(t_{1})^{2}\cdots g(t_{r})^{2}&\,\textup{d}t_{1}\cdots\,\textup{d}t_{r}\\ &\geq\int_{t_{1}+\cdots+t_{r}\leq y}g(t_{1})^{2}\cdots g(t_{r})^{2}\,\textup{d}t_{1}\cdots\,\textup{d}t_{r}\\ &=\int_{\begin{subarray}{c}t_{1}+\cdots+t_{r-1}\leq y\\
t_{1},\ldots,t_{r-1}\geq 0\end{subarray}}\frac{1}{(1+At_{1})^{2}}\cdots\frac{1}{(1+At_{r-1})^{2}}\,\textup{d}t_{1}\cdots\,\textup{d}t_{r-1}\\ &\quad\times\int_{\begin{subarray}{c}0\leq t_{r}\leq y-(t_{1}+\cdots+t_{r-1})\end{subarray}}\frac{1}{(1+At_{r})^{2}}\,\textup{d}t_{r}\\ &\geq\int_{\begin{subarray}{c}t_{1}+\cdots+t_{r-1}\leq y-1\\
t_{1},\ldots,t_{r-1}\geq 0\end{subarray}}\frac{1}{(1+At_{1})^{2}}\cdots\frac{1}{(1+At_{r-1})^{2}}\,\textup{d}t_{1}\cdots\,\textup{d}t_{r-1}\\ &\quad\times\int_{\begin{subarray}{c}0\leq t_{r}\leq 1\end{subarray}}\frac{1}{(1+At_{r})^{2}}\,\textup{d}t_{r}\\ &=\frac{1}{A+1}\int_{\begin{subarray}{c}t_{1}+\cdots+t_{r-1}\leq y-1\\
t_{1},\ldots,t_{r-1}\geq 0\end{subarray}}\frac{1}{(1+At_{1})^{2}}\cdots\frac{1}{(1+At_{r-1})^{2}}\,\textup{d}t_{1}\cdots\,\textup{d}t_{r-1}.\end{aligned}$$

Since $y\geq\log k\geq r$ for $k$ sufficiently large, we can do this $r-1$ more times, and we get

$$\int_{t_{1}+\cdots+t_{r}\leq x}g(t_{1})^{2}\cdots g(t_{r})^{2}\,\textup{d}t_{1}\cdots\,\textup{d}t_{r} \geq\frac{1}{(A+1)^{r}}\geq\frac{1}{(\log k)^{r}}$$

for $k$ sufficiently large. Since the integral of $g$ over $[0,\infty)$ is 1, for all $x\geq 0$ we have

$$\left(\int_{t_{1}+\cdots+t_{r}\leq x}g(t_{1})\cdots g(t_{r})\,\textup{d}t_{1}\cdots\,\textup{d}t_{r}\right)^{2} \leq(\log k)^{r}\int_{t_{1}+\cdots+t_{r}\leq x}g(t_{1})^{2}\cdots g(t_{r})^{2}\,\textup{d}t_{1}\cdots\,\textup{d}t_{r},$$

so (5.1) holds for all $x\geq 0$. Therefore

$$\begin{aligned}J_{k}^{(r)}(F_{k})&=\idotsint\limits_{\sum_{i=1}^{k-r}t_{i}\leq 1}\left(\prod_{i=1}^{k-r}g(kt_{i})^{2}\right)\\ &\quad\times\left(\int_{0}^{1-\sum_{i=1}^{k-r}t_{i}}g(kt_{k-r+1})\cdots\int_{0}^{1-\sum_{i=1}^{k-1}t_{i}}g(kt_{k})\,\textup{d}t_{k}\cdots\,\textup{d}t_{k-r+1}\right)^{2}\,\textup{d}t_{1}\cdots\,\textup{d}t_{k-r}\\ &\leq\left(\frac{\log k}{k}\right)^{r}\idotsint\limits_{\sum_{i=1}^{k-r}t_{i}\leq 1}\left(\prod_{i=1}^{k-r}g(kt_{i})^{2}\right)\\ &\quad\times\left(\int_{0}^{1-\sum_{i=1}^{k-r}t_{i}}g(kt_{k-r+1})^{2}\cdots\int_{0}^{1-\sum_{i=1}^{k-1}t_{i}}g(kt_{k})^{2}\,\textup{d}t_{k}\cdots\,\textup{d}t_{k-r+1}\right)\,\textup{d}t_{1}\cdots\,\textup{d}t_{k-r}\\ &=\left(\frac{\log k}{k}\right)^{r}I_{k}(F_{k}).\end{aligned}$$

By the Stone-Weierstrass Theorem, we take $F(t_{1},\ldots,t_{k})$ to be a smooth approximation to $F_{k}(\rho\delta t_{1},\ldots,\rho\delta t_{k})$ such that

$$\begin{aligned}I_{k}(F)&=(\delta\rho)^{k}(1+O((\log k)^{-1/2}))I_{k}(F_{k})\\ J_{k}^{(r)}(F)&=(\delta\rho)^{k+r}(1+O((\log k)^{-1/2}))J_{k}^{(r)}(F_{k})\end{aligned}$$

for all $r\in\mathbb{Z}^{+}$, and we are done. ∎

**Lemma 5.5.** Let $q\geq 2$ be squarefree and $N$ sufficiently large in terms of $q$. Suppose $\{h_{1},\ldots,h_{k}\}\subseteq[0,N]$ is an admissible $k$-tuple such that for all $1\leq i<j\leq k$, we have $\operatorname{gcd}(h_{i},q)=1$ and

$$p\mid h_{i}-h_{j} \implies p\leq\varepsilon\log N.$$

Let $b\in\mathbb{Z}$ such that for all $j\in\{1,\ldots,k\}$, we have $\operatorname{gcd}(qb+h_{j},W)=1$. Then the following are true.

1.  We have

    $$\sum_{\begin{subarray}{c}N<n\leq 2N\\
    n\equiv b\ (\mathrm{mod}\ W)\end{subarray}}w_{n}=(1+o(1))\frac{N}{W}B^{-k}I_{k}(F).$$

2.  For each $j\in\{1,\ldots,k\}$, we have

    $$\sum_{\begin{subarray}{c}N<n\leq 2N\\
    n\equiv b\ (\mathrm{mod}\ W)\end{subarray}}\bm{1}_{\mathbb{P}}(qn+h_{j})w_{n}=(1+o(1))\frac{N}{W}B^{-k}J_{k}^{(1)}(F).$$

3.  For $r\in\{1,2,\ldots,k\}$ and $j_{1},\ldots,j_{r}\in\{1,\ldots,k\}$ strictly increasing, we have

    $$\sum_{\begin{subarray}{c}N<n\leq 2N\\
    n\equiv b\ (\mathrm{mod}\ W)\end{subarray}}\bm{1}_{\mathbb{P}}(qn+h_{j_{1}})\cdots\bm{1}_{\mathbb{P}}(qn+h_{j_{r}})w_{n}\leq(4^{r-1}(r-1)^{r-1}+O(\delta))\frac{N}{W}B^{-k}J_{k}^{(r)}(F).$$

*Proof.* Parts (1) and (2) is nearly identical to (Banks et al., 2016, Lemma 4.6), and any differences can be found in the proof of (3), so we only prove (3). We will use the sieve upper bound

$$\bm{1}_{\mathbb{P}}(qn+h_{j_{i}})\leq\left(\sum_{e_{i}\mid qn+h_{j_{i}}}\mu(e_{i})G_{i}\left(\frac{\log e_{i}}{\log N}\right)\right)^{2}$$

for smooth decreasing functions $G_{i}:[0,\infty)\to\mathbb{R}$ supported on $[0,\frac{1}{4(r-1)}-\frac{2\delta}{r-1}]$ with $G(0)=1$, for each $i=1,2,\ldots,r-1$. Observe that there is no contribution from any summand in the definition of $w_{n}$ unless $d_{j_{1}}=\cdots=d_{j_{r}}=1$, since $1_{\mathbb{P}}(qn+h_{j_{i}})$ together with the divisibility condition $d_{j_{i}}\mid(qn+h_{j_{i}})$ forces $d_{j_{i}}=1$ for each $i=1,\ldots,r$. Thus, we have

$$\begin{aligned}&\sum_{\begin{subarray}{c}N<n\leq 2N\\
n\equiv b\ (\mathrm{mod}\ W)\end{subarray}}\prod_{i=1}^{r}\bm{1}_{\mathbb{P}}(qn+h_{j_{i}})\left(\sum_{\begin{subarray}{c}d_{1},\ldots,d_{k}\\
d_{i}\mid qn+h_{j_{i}}\forall i\end{subarray}}\lambda_{d_{1}\cdots d_{k}}\right)^{2}\\ &\leq\sum_{\begin{subarray}{c}N<n\leq 2N\\
n\equiv b\ (\mathrm{mod}\ W)\end{subarray}}\bm{1}_{\mathbb{P}}(qn+h_{j_{r}})\prod_{i=1}^{r-1}\left(\sum_{e_{i}\mid qn+h_{j_{i}}}\mu(e_{i})G_{i}\left(\frac{\log e_{i}}{\log N}\right)\right)^{2}\Bigg(\sum_{\begin{subarray}{c}d_{1},\ldots,d_{k}\\
d_{i}\mid qn+h_{j_{i}}\forall i\\
d_{j_{1}}=\cdots=d_{j_{r}}=1\end{subarray}}\lambda_{d_{1}\cdots d_{k}}\Bigg)^{2}\\ &=\sum_{\begin{subarray}{c}N<n\leq 2N\\
n\equiv b\ (\mathrm{mod}\ W)\end{subarray}}\bm{1}_{\mathbb{P}}(qn+h_{j_{r}})\Bigg(\sum_{\begin{subarray}{c}d_{1},\ldots,d_{k}\\
e_{1},\ldots,e_{r-1}\\
d_{i}\mid qn+h_{j_{i}}\forall i\\
d_{j_{1}}=\cdots=d_{j_{r}}=1\\
e_{\ell}\mid qn+h_{j_{\ell}}\forall\ell\end{subarray}}\lambda_{d_{1},\ldots,d_{k}}\mu(e_{1})\cdots\mu(e_{r-1})G_{1}\left(\frac{\log e_{1}}{\log N}\right)\cdots G_{r-1}\left(\frac{\log e_{r-1}}{\log N}\right)\Bigg)^{2}.\end{aligned}$$

Expanding the square,

$$\begin{aligned}&=\sum_{\begin{subarray}{c}N<n\leq 2N\\
n\equiv b\ (\mathrm{mod}\ W)\end{subarray}}\bm{1}_{\mathbb{P}}(qn+h_{j_{r}})\sum_{\begin{subarray}{c}d_{1},\ldots,d_{k}\\
e_{1},\ldots,e_{r-1}\\
d_{i}\mid qn+h_{j_{i}}\forall i\\
d_{j_{1}}=\cdots=d_{j_{r}}=1\\
e_{\ell}\mid qn+h_{j_{\ell}}\forall\ell\end{subarray}}\sum_{\begin{subarray}{c}d_{1}^{\prime},\ldots,d_{k}^{\prime}\\
e_{1}^{\prime},\ldots,e_{r-1}^{\prime}\\
d_{i}^{\prime}\mid qn+h_{j_{i}}\forall i\\
d_{j_{1}}^{\prime}=\cdots=d_{j_{r}}^{\prime}=1\\
e_{\ell}^{\prime}\mid qn+h_{j_{\ell}}\forall\ell\end{subarray}}\lambda_{d_{1},\ldots,d_{k}}\lambda_{d_{1}^{\prime},\ldots,d_{k}^{\prime}}\\ &\hspace{241.84842pt}\times\prod_{i=1}^{r-1}\mu(e_{i})\mu(e_{i}^{\prime})G_{i}\left(\frac{\log e_{i}}{\log N}\right)G_{i}\left(\frac{\log e_{i}^{\prime}}{\log N}\right)\\ &=\sum_{\begin{subarray}{c}d_{1},\ldots,d_{k}\\
e_{1},\ldots,e_{r-1}\\
d_{j_{1}}=\cdots=d_{j_{r}}=1\\
\operatorname{gcd}(d_{i},q)=1\forall i\\
\operatorname{gcd}(e_{\ell},q)=1\forall\ell\end{subarray}}\sum_{\begin{subarray}{c}d_{1}^{\prime},\ldots,d_{k}^{\prime}\\
e_{1}^{\prime},\ldots,e_{r-1}^{\prime}\\
d_{j_{1}}^{\prime}=\cdots=d_{j_{r}}^{\prime}=1\\
\operatorname{gcd}(d_{i}^{\prime},q)=1\forall i\\
\operatorname{gcd}(e_{\ell}^{\prime},q)=1\forall\ell\end{subarray}}\lambda_{d_{1},\ldots,d_{k}}\lambda_{d_{1}^{\prime},\ldots,d_{k}^{\prime}}\prod_{i=1}^{r-1}\mu(e_{i})\mu(e_{i}^{\prime})G_{i}\left(\frac{\log e_{i}}{\log N}\right)G_{i}\left(\frac{\log e_{i}^{\prime}}{\log N}\right)\\ &\hspace{128.0374pt}\times\sum_{\begin{subarray}{c}N<n\leq 2N\\
n\equiv b\ \mathrm{mod}\ W\\
n\equiv-q^{-1}h_{j_{i}}\ \mathrm{mod}\ [d_{i},d_{i}^{\prime}]\forall i\\
n\equiv-q^{-1}h_{j_{\ell}}\ \mathrm{mod}\ [e_{\ell},e_{\ell}^{\prime}]\forall\ell\end{subarray}}\bm{1}_{\mathbb{P}}(qn+h_{j_{r}}),\end{aligned}$$

since we assumed $\operatorname{gcd}(q,h_{j_{i}})=1$ for all $1\leq i\leq r-1$. The innermost sum is

$$\frac{\pi(2qN+h_{j_{r}})-\pi(qN+h_{j_{r}})}{\varphi(qW)\prod_{i=1}^{k}\varphi([d_{i},d_{i}^{\prime}])\prod_{i=1}^{r-1}\varphi([e_{i},e_{i}^{\prime}])}+O\left(E\left(qN;qW\prod_{i=1}^{k}[d_{i},d_{i}^{\prime}]\prod_{i=1}^{r-1}[e_{i},e_{i}^{\prime}]\right)\right),$$

where

$$E(qN;q^{\prime})=\max_{\begin{subarray}{c}(a,q^{\prime})=1\\
h\in\mathcal{H}\end{subarray}}\left|\pi(2qN+h;q^{\prime},a)-\pi(qN+h;q^{\prime},a)-\frac{\pi(2qN+h)-\pi(qN+h)}{\varphi(q^{\prime})}\right|,$$

because by the support of $\lambda_{d_{1},\ldots,d_{k}}$ and the choice of $b$ we have $[d_{i},d_{i}^{\prime}],[e_{\ell},e_{\ell}^{\prime}]$ are all pairwise coprime, and by assumption $q\mid W$. We first deal with the error term. In the same way as (Banks et al., 2016, Lemma 4.6(iii)), we can restrict to arithmetic progressions mod $sW$, where

$$s=\prod_{i=1}^{k}[d_{i},d_{i}^{\prime}]\prod_{i=1}^{r-1}[e_{i},e_{i}^{\prime}]\leq N^{1/2-\delta}.$$

Using the bound $\lambda_{d_{1},\ldots,d_{k}}\ll 1$ and the trivial bound $E(qN;q^{\prime})\ll 1+qN/\varphi(q^{\prime})$, using Cauchy–Schwarz and Theorem 5.2, the error term contributes

$$\begin{aligned}&\sideset{}{{}^{\prime}}{\sum}_{\begin{subarray}{c}d_{1},\ldots,d_{k}\\
d_{1}^{\prime},\ldots,d_{k}^{\prime}\\
d_{j_{1}}=\cdots=d_{j_{r}}=1\\
d_{j_{1}}^{\prime}=\cdots=d_{j_{r}}^{\prime}=1\\
e_{1},\ldots,e_{r-1}\\
e_{1}^{\prime},\ldots,e_{r-1}^{\prime}\end{subarray}}|\lambda_{d_{1},\ldots,d_{k}}\lambda_{d_{1}^{\prime},\ldots,d_{k}^{\prime}}|E\left(qN;qW\prod_{i=1}^{k}[d_{i},d_{i}^{\prime}]\prod_{i=1}^{r-1}[e_{i},e_{i}^{\prime}]\right)\\ &\ll\sum_{\begin{subarray}{c}s\leq N^{\frac{1}{2}-\delta}\\
\operatorname{gcd}(s,WZ_{N^{4\varepsilon}})=1\end{subarray}}\mu(s)^{2}\tau_{6k}(s)E\left(qN;sqW\right)\\ &\ll\Bigg(\sum_{\begin{subarray}{c}s\leq N^{\frac{1}{2}-\delta}\\
\operatorname{gcd}(s,WZ_{N^{4\varepsilon}})=1\end{subarray}}\mu(s)^{2}\tau_{6k}(s)^{2}\left(1+\frac{qN}{\varphi(sqW)}\right)\Bigg)^{1/2}\Bigg(\sum_{\begin{subarray}{c}s\leq N^{\frac{1}{2}-\delta}\\
\operatorname{gcd}(s,WZ_{N^{4\varepsilon}})=1\end{subarray}}\mu(s)^{2}E\left(qN;sqW\right)\Bigg)^{1/2}\\ &\ll\frac{N}{W(\log N)^{2k}},\end{aligned}$$

where $\sum^{\prime}$ denotes the additional pairwise coprimality condition between $[d_{i},d_{i}^{\prime}],[e_{\ell},e_{\ell}^{\prime}],qWZ_{N^{2\varepsilon}}$ and $\tau_{6k}(s)$ denotes the number of ordered $6k$-tuples of positive integers whose product is $s$. The main term is treated the same as (Banks et al., 2016, Lemma 4.6(ii)). Expanding $\lambda_{d_{1},\ldots,d_{k}}$, the main term is

$$\begin{aligned}(1+o(1))\frac{qN}{\log N}\sum_{j=1}^{J}\sideset{}{{}^{\prime}}{\sum}_{\begin{subarray}{c}d_{1},\ldots,d_{k}\\
d_{1}^{\prime},\ldots,d_{k}^{\prime}\\
d_{j_{1}}=\cdots=d_{j_{r}}=1\\
d_{j_{1}}^{\prime}=\cdots=d_{j_{r}}^{\prime}=1\end{subarray}}&\prod_{j=1}^{k}\mu(d_{j})\prod_{\begin{subarray}{c}1\leq\ell\leq k\\
\ell\neq j_{1},\ldots,j_{r-1}\end{subarray}}F_{\ell,j}\left(\frac{\log d_{\ell}}{\log N}\right)\prod_{i=1}^{r-1}F_{j_{i},j}(0)\,G_{i}\left(\frac{\log d_{i}}{\log N}\right)\\ &\prod_{j=1}^{k}\mu(d_{j}^{\prime})\prod_{\begin{subarray}{c}1\leq\ell\leq k\\
\ell\neq j_{1},\ldots,j_{r-1}\end{subarray}}F_{\ell,j}\left(\frac{\log d_{\ell}^{\prime}}{\log N}\right)\prod_{i=1}^{r-1}F_{j_{i},j}(0)\,G_{i}\left(\frac{\log d_{i}^{\prime}}{\log N}\right)\\ &\times\varphi(qW)^{-1}\varphi([d_{1},d_{1}^{\prime}])^{-1}\cdots\varphi([d_{k},d_{k}^{\prime}])^{-1},\end{aligned}$$

where $\sum^{\prime}$ denotes the additional restriction of $[d_{1},d_{1}^{\prime}],\ldots,[d_{k},d_{k}^{\prime}],qWZ_{N^{4\varepsilon}}$ being pairwise coprime. Let

$$\begin{aligned}\widetilde{F}(t_{1},\ldots,t_{k})=&G_{1}^{\prime}(t_{j_{1}})\cdots G_{r-1}^{\prime}(t_{j_{r-1}})\\ &\times\int_{0}^{\infty}\cdots\int_{0}^{\infty}F(t_{1},\ldots,t_{j_{1}-1},u_{j_{1}},\ldots,u_{j_{r-1}},t_{j_{r}+1},\ldots,t_{k})\,\textup{d}u_{j_{1}}\cdots\,\textup{d}u_{j_{r-1}}.\end{aligned}$$

Note $\widetilde{F}$ is supported on $t_{1},\ldots,t_{k}$ with $\sum_{i=1}^{k}t_{i}\leq 1/4-\delta$. Using Lemma 5.3, the main term is

$$\begin{aligned}&(1+o(1))\frac{qN}{\varphi(qW)\log N}B^{-k+1}\sum_{j=1}^{J}\prod_{\begin{subarray}{c}1\leq\ell\leq k\\
\ell\neq j_{1},\ldots,j_{r}\end{subarray}}\int_{0}^{\infty}F^{\prime}_{\ell,j}(t_{\ell})^{2}\,\textup{d}t_{\ell}\prod_{i=1}^{r}F_{j_{i},j}(0)^{2}\prod_{i=1}^{r-1}\int_{0}^{\infty}G_{i}^{\prime}(t_{i})^{2}\,\textup{d}t_{i}\\ &\leq(1+o(1))\frac{N}{W}B^{-k}\int_{0}^{\infty}\cdots\int_{0}^{\infty}\left(\int_{0}^{\infty}\widetilde{F}(t_{1},\ldots,t_{k})\,\textup{d}t_{j_{r}}\right)^{2}\,\textup{d}t_{1}\cdots\,\textup{d}t_{j_{r}-1}\,\textup{d}t_{j_{r}+1}\cdots\,\textup{d}t_{k}.\end{aligned}$$

Combined with the above error term bound we have

$$\begin{aligned}&\sum_{\begin{subarray}{c}N<n\leq 2N\\
n\equiv b\ (\mathrm{mod}\ W)\end{subarray}}\prod_{i=1}^{r}\bm{1}_{\mathbb{P}}(qn+h_{j_{i}})\Bigg(\sum_{\begin{subarray}{c}d_{1},\ldots,d_{k}\\
d_{i}\mid qn+h_{j_{i}}\forall i\\
d_{j_{1}}=\cdots=d_{j_{r}}=1\end{subarray}}\lambda_{d_{1},\ldots,d_{k}}\Bigg)^{2}\\ &\leq(1+o(1))\frac{N}{W}B^{-k}\int_{0}^{\infty}\cdots\int_{0}^{\infty}\left(\int_{0}^{\infty}\widetilde{F}(t_{1},\ldots,t_{k})\,\textup{d}t_{j_{r}}\right)^{2}\,\textup{d}t_{1}\cdots\,\textup{d}t_{j_{r}-1}\,\textup{d}t_{j_{r}+1}\cdots\,\textup{d}t_{k}\\ &=(1+o(1))\frac{N}{W}B^{-k}J_{k}^{(r)}(F)\int_{0}^{\infty}\cdots\int_{0}^{\infty}\prod_{i=1}^{r-1}G_{i}^{\prime}(t_{j_{i}})^{2}\,\textup{d}t_{j_{1}}\cdots\,\textup{d}t_{j_{r-1}}.\end{aligned}$$

Taking $G_{i}(t)$ to be a fixed smooth approximation to $1-t/(\frac{1}{4(r-1)}-\frac{2\delta}{r-1})$ with $G(0)=1$ and $\int_{0}^{\infty}G_{i}^{\prime}(t)^{2}\,\textup{d}t\leq 4(r-1)+O(\delta)$, we are done. ∎

It will be helpful to make the following definitions.

**Definition 1.4.** For a squarefree integer $q\geq 2$, $m\in\mathbb{Z}^{+}$, and $A\subseteq\prod_{i=1}^{m}(\mathbb{Z}/q\mathbb{Z})^{\times}$, define

$$\pi(x;q,A)=\#\{p_{n}\leq x:(p_{n}\ \mathrm{mod}\ q,\ldots,p_{n+m-1}\ \mathrm{mod}\ q)\in A\}.$$

Also, for $r\in\mathbb{Z}^{+}$ with $r>1$, define

$$M{}=\left\lceil\left(\frac{2^{3r-2}(r-1)^{2r-1}}{r!}\right)^{\frac{1}{r-1}}m(m(r-1)+r)^{\frac{1}{r-1}}\right\rceil,$$

and define the set of functions

$$J_{r}(m,M)=\{j:\{1,\ldots,m\}\to\{1,\ldots,M\}:j(i+1)\geq j(i),\text{ no consecutive $r$ values }j(i)\text{ are equal}\}.$$

**Proposition 5.6.** Let $m,r\in\mathbb{Z}^{+}$ with $r>1$, $q\geq 2$ be a squarefree integer and recall $M$ from Definition 1.4. Let $k$ be a sufficiently large multiple of $M{}$ in terms of $m$ and $r$. Let $\varepsilon>0$ be sufficiently small. Define

$$W:=\prod_{\begin{subarray}{c}p\leq\varepsilon\log N\\
p\nmid Z_{N^{4\varepsilon}}\end{subarray}}p.$$

Let $\mathcal{H}=\{h_{1},\ldots,h_{k}\}\subseteq[0,N]$ be an admissible $k$-tuple such that for all $1\leq i<j\leq k$, $\operatorname{gcd}(h_{i},q)=1$ and

$$p\mid h_{i}-h_{j}\implies p\leq\varepsilon\log N.$$

Let $b\in\mathbb{Z}$ such that

$$\left(\prod_{j=1}^{k}(qb+h_{j}),W\right)=1.$$

Let $\mathcal{H}=\mathcal{H}_{1}\cup\cdots\cup\mathcal{H}_{M{}}$ be a partition of $\mathcal{H}$ into $M{}$ sets of equal size. Then for all sufficiently large $N$ in terms of $m,q,k,\varepsilon$, there is $n\in[N,2N]$ with $n\equiv b\ (\mathrm{mod}\ W)$ and some set of distinct indices $\{i_{1},\ldots,i_{m+1}\}$ such that

$$\begin{aligned}1\leq|\mathcal{H}_{i}(n)\cap\mathbb{P}|\leq r-1&\quad\text{ for all }i\in\{i_{1},\ldots,i_{m+1}\},\\ |\mathcal{H}_{i}(n)\cap\mathbb{P}|=0&\quad\text{ for all }i_{1}<i<i_{m+1}\text{ such that }i\neq i_{1},\ldots,i_{m+1}.\end{aligned}$$

*Proof.* The proof is similar to that of (Banks et al., 2016, Theorem 4.3). Consider

$$S=\sum_{N<n\leq 2N}\Bigg(\sum_{i=1}^{k}\bm{1}_{\mathbb{P}}(qn+h_{i})-m(r-1)-(m(r-1)+r)\sum_{j=1}^{M}{}\sum_{\begin{subarray}{c}h_{j_{1}},\ldots,h_{j_{r}}\in\mathcal{H}_{j}\\
j_{1}<\cdots<j_{r}\end{subarray}}\prod_{i=1}^{r}\bm{1}_{\mathbb{P}}(qn+h_{j_{i}})\Bigg)w_{n}.$$

By Lemma 5.5, we have

$$\begin{aligned}S\geq\sum_{i=1}^{k}&(1+o(1))\frac{N}{W}B^{-k}J_{k}^{(1)}(F)-m(r-1)(1+o(1))\frac{N}{W}B^{-k}I_{k}(F)\\ &-(m(r-1)+r)\sum_{\begin{subarray}{c}h_{j_{1}},\ldots,h_{j_{r}}\in\mathcal{H}_{j}\\
j_{1}<\cdots<j_{r}\end{subarray}}(4^{r-1}(r-1)^{r-1}+o(\delta))\frac{N}{W}B^{-k}J_{k}^{(r)}(F).\end{aligned}$$

Using Lemma 5.4 and choosing $0<\rho<1$ such that $\rho\delta\log k=2(r-1)m$, we get

$$\begin{aligned}S&\geq\frac{N}{W}B^{-k}I_{k}(F)\Bigg(k\cdot\frac{2(r-1)m}{k}-m(r-1)\\ &\hspace{91.04872pt}-4^{r-1}(r-1)^{r-1}(m(r-1)+r)M{}\binom{k/M{}}{r}\left(\frac{2(r-1)m}{k}\right)^{r}-O(\delta)\Bigg)\\ &>\frac{N}{W}B^{-k}I_{k}(F)\left(m(r-1)-4^{r-1}(r-1)^{r-1}(m(r-1)+r)\cdot\frac{2^{r}(r-1)^{r}m^{r}}{r!M{}^{r-1}}\right),\end{aligned}$$

so $S>0$ since

$$M{}=\left\lceil\left(\frac{2^{3r-2}(r-1)^{2r-1}}{r!}\right)^{\frac{1}{r-1}}m(m(r-1)+r)^{\frac{1}{r-1}}\right\rceil.$$

Therefore, there must exist $n\in(N,2N]$ making a positive contribution to $S$. Observe that

1.  every $\mathcal{H}_{i}$ with $|\mathcal{H}_{i}(n)\cap\mathbb{P}|\geq r$ contributes at most $r-m(r-1)-r=-m(r-1)$ to $S$,

2.  every $\mathcal{H}_{i}$ with $|\mathcal{H}_{i}(n)\cap\mathbb{P}|\in[1,r-1]$ contributes at most $r-1$.

For each $n\in(N,2N]$, define

$$\begin{aligned}s_{n}&=\text{ number of indices $i$ for which $|\mathcal{H}_{i}(n)\cap\mathbb{P}|\geq r$},\\ t_{n}&=\text{ number of indices $i$ for which $|\mathcal{H}_{i}(n)\cap\mathbb{P}|\in[1,r-1]$}.\end{aligned}$$

For those $n$ making a positive contribution to $S$, we must have

$$-m(r-1)s_{n}-m(r-1)+t_{n}(r-1)>0,$$

which implies $t_{n}\geq m+1+ms_{n}$, i.e. number of indices $j$ for which $|\mathcal{H}_{j}(n)\cap\mathbb{P}|\in[1,r-1]$ is at least $m+1+ms_{n}$. In particular, there must be some set of $m+1$ indices $i_{1}<\cdots<i_{m+1}$ for which $|\mathcal{H}_{i}(n)\cap\mathbb{P}|\in[1,r-1]$ for $i=i_{1},\ldots,i_{m+1}$ and $|\mathcal{H}_{i}(n)\cap\mathbb{P}|=0$ for $i_{1}<i<i_{m+1}$ and $i\neq i_{1},\ldots,i_{m+1}$. ∎

## 6. A Modified Erdős–Rankin Type Construction

We have the following elementary lemma.

**Lemma 6.1.** Let $\{h_{1},\ldots,h_{k}\}$ be an admissible $k$-tuple, let $S\subseteq\mathbb{Z}$, and $\mathcal{P}$ be a set of primes such that for some $x\geq 2$, we have

$$\left\{\begin{aligned} &\{h_{1},\ldots,h_{k}\}\subseteq S\subseteq[0,x^{2}],\\
&|\{p\in\mathcal{P}:p>x\}|>|S|+k.\end{aligned}\right.$$

Then, there is a set of integers $\{a_{p}:p\in\mathcal{P}\}$ such that

$$\{h_{1},\ldots,h_{k}\}=S\setminus\bigcup_{p\in\mathcal{P}}\{g:g\equiv a_{p}\ (\mathrm{mod}\ p)\}.$$

*Proof.* This is (Banks et al., 2016, Lemma 5.1). ∎

As in Banks et al. (2016), we need Mertens’ 3rd Theorem: for $x\geq 2$,

$$\prod_{p\leq x}\left(1-\frac{1}{p}\right) =\frac{e^{-\gamma}}{\log x}\left(1+O\left(\frac{1}{\log x}\right)\right), \tag{6.1}$$

where $\gamma=0.5772\ldots$ is the Euler-Mascheroni constant. Also, from (Davenport, 2013, Chapter 20 (13)), for any positive constant $c$, there is a positive constant $c^{\prime}$ depending only on $c$ such that

$$\sum_{\begin{subarray}{c}x<p\leq x+y\\
p\equiv a\ (\mathrm{mod}\ q)\end{subarray}}\log p=\frac{y}{\varphi(q)}+O\left(x\exp\left(-c^{\prime}\sqrt{\log x}\right)\right) \tag{6.2}$$

uniformly for $2\leq y\leq x,q\leq\exp(c\sqrt{\log x})$ and $\operatorname{gcd}(q,a)=1$, except possibly when $q$ is a multiple of some $q_{1}$ depending on $x$ which satisfies $P^{+}(q_{1})\gg_{c}\log_{2}x$.

**Lemma 6.2.** Fix $k\in\mathbb{N}$, squarefree integer $q\geq 2$ and integers $0<r_{1}\leq\cdots\leq r_{k}$ all coprime to $q$. There is a number $y^{\prime}=y^{\prime}(q,\mathbf{r},k)$ depending only on $q,r_{1},\ldots,r_{k}$ and $k$ such that the following holds. Let $x,y,z\in\mathbb{R}$ satisfy $x\geq 1,y\geq y^{\prime}$ and

$$2y(1+(1+r_{k})x)\leq\frac{2q}{\varphi(q)}z\leq y(\log_{2}y)(\log_{3}y)^{-1}.$$

Let $\mathcal{Z}$ be any (possibly empty) set of primes such that for all $p^{\prime}\in\mathcal{Z}$,

$$\sum_{\begin{subarray}{c}p\in\mathcal{Z}\\
p\geq p^{\prime}\end{subarray}}\frac{1}{p}\ll\frac{1}{p^{\prime}}\ll\frac{1}{\log z}. \tag{6.3}$$

There is a set $\{\widetilde{a}_{p}:p\leq y,p\notin\mathcal{Z}\}$ and an admissible $k$-tuple $\{h_{1},\ldots,h_{k}\}\subseteq(y,z]$ such that

$$\{h_{1},\ldots,h_{k}\} =\left((0,z]\cap\mathbb{Z}\right)\setminus\bigcup_{\begin{subarray}{c}p\leq y\\
p\notin\mathcal{Z}\end{subarray}}\{g:g\equiv\widetilde{a}_{p}\ (\mathrm{mod}\ p)\}$$

and $p\mid\widetilde{a}_{p}$ whenever $p\mid q$. Moreover, for $1\leq i<j\leq k$,

$$p\mid h_{i}-h_{j}\implies p\leq y,$$

and for $1\leq i\leq k$, $h_{i}\equiv r_{i}\ (\mathrm{mod}\ q)$.

*Proof.* The proof is very similar to the proof of (Banks et al., 2016, Lemma 5.2). Let $y_{1},y_{2},y,z$ be numbers satisfying

$$2<y_{1}<y_{2}<y<z<y_{1}y_{2},\quad 2\log y_{1}\leq(\log z)(\log_{2}z)^{-1}.$$

Let $\mathcal{Z}$ be any set consisting of primes satisfying (6.3). As in Banks et al. (2016), we have the following estimates on $\mathcal{Z}$:

$$\begin{align*}\prod_{p\in\mathcal{Z}}\left(1-\frac{1}{p}\right)^{-1}&=1+O\left(\frac{1}{\log z}\right), \tag{6.4}\\ \sum_{\begin{subarray}{c}p\in\mathcal{Z}\\
p\leq y_{0}\end{subarray}}1&\ll\log y_{0}\text{ for all }y_{0}\geq 1. \tag{6.5}\end{align*}$$

For $y$ (and hence $\log z$) sufficiently large, from (6.3) we may assume $2\notin\mathcal{Z}$. Suppose further that $y_{1}>P^{+}(q)$. Let

$$P_{1}=\prod_{\begin{subarray}{c}2<p\leq y_{1}\\
p\notin\mathcal{Z},p\neq\ell\end{subarray}}p,\quad P_{2}=\prod_{\begin{subarray}{c}y_{1}<p\leq y_{2}\\
p\notin\mathcal{Z}\end{subarray}}p,\quad P_{3}=\prod_{\begin{subarray}{c}y_{2}<p\leq y\\
p\notin\mathcal{Z}\end{subarray}}p,$$

where $\ell$ is a prime satisfying $\ell\gg\log y_{1}$ chosen later. For $p\mid P_{2}$, we choose $\widetilde{a}_{p}=0$, and let

$$\mathcal{N}_{1}=((0,z]\cap\mathbb{Z})\setminus\bigcup_{p\mid P_{2}}\{g:g\equiv\widetilde{a}_{p}\ (\mathrm{mod}\ p)\}=\{h\in(0,z]:\operatorname{gcd}(h,P_{2})=1\}.$$

From the proof of (Banks et al., 2016, Lemma 5.2), we get

$$|\mathcal{N}_{1}|\leq\frac{z}{\log y_{2}}(\log(z/y_{2})+O(1)).$$

For $p\mid P_{1}$ and $p\nmid q$, we choose $\widetilde{a}_{p}$ greedily as in Banks et al. (2016), which is, for any finite set $S\subseteq\mathbb{Z}$,

$$|S|=\sum_{a\ (\mathrm{mod}\ p)}\sum_{\begin{subarray}{c}g\in S\\
g\equiv a\ (\mathrm{mod}\ p)\end{subarray}}1,$$

so there is an integer $\widetilde{a}_{p}$ such that

$$|\{g\in S:g\equiv\widetilde{a}_{p}\ (\mathrm{mod}\ p)\}|\geq\frac{|S|}{p},$$

For $p\mid q$, set $\widetilde{a}_{p}=0$. Repeating this process with $p$ varied over all prime divisors of $P_{1}$, we obtain the set

$$\begin{aligned}\mathcal{N}_{2}&=\mathcal{N}_{1}\setminus\bigcup_{p\mid P_{1}}\{g:g\equiv\widetilde{a}_{p}\ (\mathrm{mod}\ p)\}\\ &=\mathcal{N}_{1}\setminus\Bigg[\bigcup_{\begin{subarray}{c}p\mid P_{1}\\
p\nmid q\end{subarray}}\{g:g\equiv\widetilde{a}_{p}\ (\mathrm{mod}\ p)\}\bigcup_{\begin{subarray}{c}p\mid P_{1}\\
p\mid q\end{subarray}}\{g:g\equiv 0\ (\mathrm{mod}\ p)\}\Bigg]\end{aligned}$$

whose cardinality satisfies the bound

$$|\mathcal{N}_{2}|\leq|\mathcal{N}_{1}|\prod_{\begin{subarray}{c}p\mid P_{1}\\
p\nmid q\end{subarray}}\left(1-\frac{1}{p}\right)\leq 2e^{-\gamma}\frac{qz(\log(z/y_{2})+O(1))}{\varphi(q)(\log y_{1})(\log y_{2})}$$

by Mertens’ theorem (6.1) and (6.4). By the prime number theorem,

$$\begin{aligned}\pi(y)-\pi(y_{2})&=\frac{y}{\log y}+O\left(\frac{y}{(\log y)^{2}}+\frac{y_{2}}{\log y_{2}}\right)\\ &\geq\frac{y}{\log y_{2}}-O\left(\frac{y_{2}}{\log y_{2}}\right)\end{aligned}$$

if $y_{2}\geq y\log(y/y_{2})/\log y$, which is implied by $y_{2}\geq y\log_{2}y/\log y$. By (6.5), we have

$$\begin{aligned}|\{p\in(y_{2},y]:p\notin\mathcal{Z}\}|-|\mathcal{N}_{2}|&\geq\frac{y}{\log y_{2}}\left(1-2e^{-\gamma}\frac{qz\log(z/y_{2})}{\varphi(q)y\log y_{1}}\right)\\ &\qquad-O\left(\frac{y_{2}}{\log y_{2}}+\frac{z}{(\log y_{1})(\log y_{2})}\right).\end{aligned}$$

We now assume

$$y_{1}=(\log y)^{1/4},\quad y_{2}=y(\log_{3}y)^{-1},\quad y<\frac{2qz}{\varphi(q)}\leq y(\log_{2}y)(\log_{3}y)^{-1}.$$

Substituting, we have

$$|\{p\in(y_{2},y]:p\notin\mathcal{Z}\}|-|\mathcal{N}_{2}|\geq\frac{y}{\log y}(1-e^{-\gamma})-O\left(\frac{y}{(\log y)(\log_{3}y)}\right),$$

which tends to infinity as $y\to\infty$, so

$$|\{p\in(y_{2},y]:p\notin\mathcal{Z}\}|>|\mathcal{N}_{2}|+k$$

for $y$ sufficiently large in terms of $k$, which we assume. Applying Lemma 6.1, if $\{h_{1},\ldots,h_{k}\}$ is any admissible $k$-tuple contained in $\mathcal{N}_{2}$, then there exist integers $\{\widetilde{a}_{p}:p\mid 2\ell P_{3}\}$ such that

$$\{h_{1},\ldots,h_{k}\}=\mathcal{N}_{2}\setminus\bigcup_{p\mid 2\ell P_{3}}\{g:g\equiv\widetilde{a}_{p}\ (\mathrm{mod}\ p)\}.$$

Note $\{p\leq y:p\notin\mathcal{Z}\}=\{p\leq y:p\mid 2\ell P_{1}P_{2}P_{3}\}$, so we are done if we can show there exists an admissible $k$-tuple $\{h_{1},\ldots,h_{k}\}\subseteq\mathcal{N}_{2}$ satisfying the required conditions. To do this, we first define an arithmetic progression mod $[q,P_{1}]$. For each prime $p\mid[q,P_{1}]$, let $A_{i}\ (\mathrm{mod}\ p)$ be defined by

$$A_{i}=\begin{cases}-1,&\quad\text{ if }\widetilde{a}_{p}\equiv 1\ (\mathrm{mod}\ p),p\nmid q,p\mid P_{1},\\
1,&\quad\text{ if }\widetilde{a}_{p}\equiv-1\ (\mathrm{mod}\ p),p\nmid q,p\mid P_{1},\\
r_{i},&\quad\text{ if }p\mid q,\end{cases}$$

Since these congruence conditions are prescribed modulo the distinct prime divisors of $[q,P_{1}]$, the Chinese Remainder Theorem yields a unique residue class $A_{i}\ (\mathrm{mod}\ [q,P_{1}])$ satisfying all of them simultaneously. Suppose we could choose $h_{i}$ to be distinct primes in $(y,z]$ congruent to $A_{i}\ (\mathrm{mod}\ [q,P_{1}])$. Then, $h_{i}\in\mathcal{N}_{1}$ implies $h_{i}\in\mathcal{N}_{2}$ since $\operatorname{gcd}(A_{i},P_{1})=1$. By the prime number theorem, note $P_{1}=e^{(1+o(1))y_{1}}$ as $y$ tends to infinity, so for $i\neq j$ we have

$$p\mid h_{i}-h_{j}\implies p\mid{\prod_{\begin{subarray}{c}p\nmid q\\
p\mid P_{1}\end{subarray}}p}\text{ or }p\mid\frac{h_{i}-h_{j}}{\prod_{\begin{subarray}{c}p\nmid q\\
p\mid P_{1}\end{subarray}}p}\implies p\leq\max\{y_{1},qz/P_{1}\}<y,$$

if $y$ is sufficiently large. Also, $\{h_{1},\ldots,h_{k}\}$ is admissible since $\min\{h_{1},\ldots,h_{k}\}\geq y>k$, which we assume. Therefore, we are left to show that we can find $k$ distinct primes in $(y,z]$ each congruent to $A_{i}\pmod{[q,P_{1}]}$.\

To show this, note Chebyshev’s bound implies $\sum_{p\leq y_{1}}\log p\ll 2y_{1}$, so $[q,P_{1}]<e^{3(\log y)^{1/4}}$. Therefore, by (6.2), for each $1\leq i\leq k$ we have

$$\sum_{\begin{subarray}{c}u\leq p\leq u+\Delta\\
p\equiv A_{i}\ (\mathrm{mod}\ [q,P_{1}])\end{subarray}}\log p=\frac{\Delta}{\varphi([q,P_{1}])}+O\left(y\exp\left(-c^{\prime}\sqrt{\log y}\right)\right)$$

uniformly for $2\leq\Delta\leq y\leq u\leq z$ and $c^{\prime}$ an absolute constant, apart from when possibly $[q,P_{1}]$ is a multiple of some $q_{1}$ depending on $u$ satisfying $P^{+}(q_{1})\gg_{c}\log_{2}u\gg\log y_{1}$. Therefore we now pick $\ell$ such that this possibility doesn’t occur. Choosing $\Delta=ye^{-(\log y)^{1/4}}$, we have

$$\sum_{\begin{subarray}{c}u\leq p\leq u+\Delta\\
p\equiv A_{i}\ (\mathrm{mod}\ [q,P_{1}])\end{subarray}}\log p\gg y\exp\left(-4(\log y)^{1/4}\right)$$

uniformly for $y\leq u\leq z$, so for each $i$, the left hand side is a sum of at least $k$ primes for every $A_{i}$ if $y$ is sufficiently large in terms of $k$. Now assume $y$ sufficiently large in terms of $r_{k}$ so that

$$2(1+(1+r_{k}))\leq(\log_{2}y)(\log_{3}y)^{-1},$$

and let $x\geq 1$ be any number such that

$$2y(1+(1+r_{k})x)\leq\frac{2q}{\varphi(q)}z\leq y(\log_{2}y)(\log_{3}y)^{-1}.$$

Let

$$u=r_{k}xy+y,$$

so that the interval $(u,u+\Delta]$ is contained in $(y,z]$. For $1\leq i\leq k$, we choose $h_{i}$ to be distinct primes in $(u,u+\Delta]$ such that $h_{i}\equiv A_{i}\ (\mathrm{mod}\ [q,P_{1}])$, and this is possible since each arithmetic progression $A_{i}\ (\mathrm{mod}\ [q,P_{1}])$ contains at least $k$ primes in the interval. Therefore, we are done. ∎

## 7. Proofs of Main Result

In this section we combine the results of Sections 5 and 6 to prove Theorem 1.5.

**Theorem 1.5.** Let $q\geq 2$ be a squarefree integer, and $r,m\in\mathbb{Z}^{+}$ with $r>1$. Recall $\pi(x;q,A)$, $M$, and $J_{r}(m,M)$ from Definition 1.4. For any $a_{1},\ldots,a_{M{}}\in(\mathbb{Z}/q\mathbb{Z})^{\times}$, let

$$A=\{(c_{1},\ldots,c_{m}):\exists j\in J_{r}(m,M)\text{ s.t. }c_{i}=a_{j(i)}\forall 1\leq i\leq m\}.$$

Then $\pi(x;q,A)\to\infty$ as $x\to\infty$.

*Proof.* The case $m=1$ is known. Fix $k\geq m\geq 2$, let $\varepsilon>0$ be sufficiently small, and let $k$ be a sufficiently large multiple of $M{}$. Let $\mathbf{r}=(r_{1},\ldots,r_{k})\in\mathbb{R}^{k}$ be given by

$$\mathbf{r}=(a_{1}\ \mathrm{mod}\ q,\ldots,a_{1}\ \mathrm{mod}\ q,a_{2}\ \mathrm{mod}\ q,\ldots,a_{2}\ \mathrm{mod}\ q,\ldots,a_{M{}}\ \mathrm{mod}\ q,\ldots,a_{M}{}\ \mathrm{mod}\ q),$$

where there are $k/M{}$ consecutive copies of each $a_{i}\ (\mathrm{mod}\ q)$ appearing in $\mathbf{r}$. We choose suitable representatives $r_{i}$ mod $q$ such that $r_{1}\leq\cdots\leq r_{k}$. Let $N$ be sufficiently large in terms of $k,m,\varepsilon$, and define parameters

$$x=\varepsilon^{-1},\quad y=\varepsilon\log N,\quad z=\varphi(q)y(\log_{2}(y))(2q\log_{3}(y))^{-1}.$$

If $N$ is sufficiently large in terms of $\mathbf{r}$ and $k$ as well, then with $y^{\prime}(q,\mathbf{r},k)$ as in Lemma 6.2, we have

$$x>1,\quad y\geq y^{\prime}(q,\mathbf{r},k),\quad 2y(1+(1+r_{k})x)\leq\frac{2q}{\varphi(q)}z\leq y(\log_{2}y)(\log_{3}y)^{-1}.$$

Let $Z_{N^{4\varepsilon}}$ be defined as in Section 5, $W=\prod_{p\leq\varepsilon\log N,p\nmid Z_{N^{4\varepsilon}}}p$, and let

$$\mathcal{Z}=\begin{cases}\emptyset,&\quad\text{ if }Z_{N^{4\varepsilon}}=1\\
\{Z_{N^{4\varepsilon}}\},&\quad\text{ if }Z_{N^{4\varepsilon}}\neq 1.\end{cases}$$

By Lemma 6.2, there is a set $\{a_{p}:p\leq y,p\notin\mathcal{Z}\}$ and an admissible $k$-tuple $\{h_{1},\ldots,h_{k}\}\subseteq(y,z]$ such that

$$\{h_{1},\ldots,h_{k}\} =\left((0,z]\cap\mathbb{Z}\right)\setminus\bigcup_{\begin{subarray}{c}p\leq y\\
p\notin\mathcal{Z}\end{subarray}}\{g:g\equiv\widetilde{a}_{p}\ (\mathrm{mod}\ p)\},$$

and $p\mid\widetilde{a}_{p}$ whenever $p\mid q$. Moreover, for $1\leq i<j\leq k$,

$$p\mid h_{i}-h_{j}\implies p\leq y,$$

and define the partition

$$\mathcal{H}=\mathcal{H}_{1}\sqcup\cdots\sqcup\mathcal{H}_{M{}}$$

such that for each $j=1,2,\ldots,M{}$ we have

$$h\equiv r_{jk/M}\ (\mathrm{mod}\ q)$$

for all $h\in\mathcal{H}_{j}$. Let $b\in\mathbb{Z}$ satisfying

$$b\equiv-q^{-1}\widetilde{a}_{p}\ (\mathrm{mod}\ p)$$

if $p\leq y,p\notin\mathcal{Z}$ and $p\nmid q$, whereas if $p\mid q$ set $b\equiv 0\ (\mathrm{mod}\ p)$. Therefore, the assumptions of Proposition 5.6 hold, and there is some $n\in(N,2N]$ with $n\equiv b\ (\mathrm{mod}\ W)$ and some set of distinct indices $\{i_{1},\ldots,i_{m+1}\}$ such that

$$\begin{aligned}1\leq|\mathcal{H}_{i}(n)\cap\mathbb{P}|\leq r-1&\quad\text{ for all }i\in\{i_{1},\ldots,i_{m+1}\},\\ |\mathcal{H}_{i}(n)\cap\mathbb{P}|=0&\quad\text{ for all }i_{1}<i<i_{m+1}\text{ such that }i\neq i_{1},\ldots,i_{m+1}.\end{aligned}$$

To prove they are consecutive primes, note

$$(qn,qn+z]\cap\mathbb{P}=\mathcal{H}(n)\cap\mathbb{P},$$

since if $g\in(0,z]$ and $g\notin\{h_{1},\ldots,h_{k}\}$, then $qn+g\equiv qb+\widetilde{a}_{p}\equiv-\widetilde{a}_{p}+\widetilde{a}_{p}\equiv 0\ (\mathrm{mod}\ p)$ for some $p\leq y$ with $p\notin\mathcal{Z}$, so the primes in $\mathcal{H}(n)$ are consecutive primes. Therefore, there must exist consecutive primes $p_{n},\ldots,p_{n+m-1}\in[qN,3qN]$ such that $p_{n+i-1}\equiv a_{j^{\prime}(i)}\ \mathrm{mod}\ q$ for all $1\leq i\leq m$, where $j^{\prime}(i+1)\geq j^{\prime}(i)$ for all $1\leq i\leq m$ and no consecutive $r$ of $(j^{\prime}(i))_{i=1}^{m}$ are congruent mod $q$. Taking $N\to\infty$, we are done. ∎

## 8. Number of Attainable Residue Class Patterns

In this section, we use Theorem 1.5 and recursive combinatorial arguments to obtain lower bounds for the number of $m$-tuples occurring infinitely often among consecutive primes.

**Corollary 8.1.** For $m,r\in\mathbb{Z}^{+}$ with $2\leq r\leq m/100$, recall $M$ from Definition 1.4. For any constant $0<c<1$, if $q$ is squarefree and $\varphi(q)\geq\lceil\frac{M{}}{\lfloor c(m-1)/(r-1)\rfloor}\rceil$, there are at least

$$4\lfloor(1-c)m\rfloor\left(\left\lceil\frac{M{}}{\lfloor c(m-1)/(r-1)\rfloor}\right\rceil\right)^{-5}\varphi(q)(\varphi(q)-1)$$

$m$-tuples $\mathbf{a}$ such that $\pi(x;q,\mathbf{a})\to\infty$ as $x\to\infty$.

*Proof.* Using Theorem 1.5, for any $a_{1},\ldots,a_{M{}}$, there must exist $\mathbf{a}=(a_{j(1)},\ldots,a_{j(m)})$ with $j$ increasing and no consecutive $r$ values the same, such that

$$\pi(x;q,\mathbf{a})\to\infty\text{ as }x\to\infty.$$

We call a $m$-tuple $\mathbf{a}$ with this property ‘good’. Define a set $S_{1}$ consisting of all $M{}$-tuples with entries in $(\mathbb{Z}/q\mathbb{Z})^{\times}$ of the form

$$(\underbrace{a_{1},\ldots,a_{1}}_{\lfloor c(m-1)/(r-1)\rfloor\text{ times}},\underbrace{a_{2},\ldots,a_{2}}_{\lfloor c(m-1)/(r-1)\rfloor\text{ times}},\cdots),\quad a_{i}\text{ distinct}.$$

Note $S_{1}$ is non-empty since $\varphi(q)\geq\lceil\frac{M{}}{\lfloor c(m-1)/(r-1)\rfloor}\rceil$ by assumption. We pick good $m$-tuples with the following recursive process.

1.  Take a $M$-tuple $(a_{1},\ldots,a_{1},a_{2},\ldots)\in S_{1}$. By Theorem 1.5, there is a good $m$-tuple of the form

    $$(b_{1},\ldots,b_{1},b_{2},\ldots,b_{2},\ldots,b_{\ell_{1}},\ldots,b_{\ell_{1}}),$$

    where $2\leq\ell_{1}\leq\lceil\frac{M{}}{\lfloor c(m-1)/(r-1)\rfloor}\rceil$.

2.  Define

    $$S_{2}:=S_{1}\setminus\{(a_{1},\ldots,a_{1},a_{2},\ldots,a_{2},\ldots): \exists i,i^{\prime},j\text{ s.t. }i<i^{\prime}\text{ and }a_{i}=b_{j},a_{i^{\prime}}=b_{j+1}\}.$$

3.  Take any element from $S_{2}$, then repeat the above process until $S_{k}$ is empty.

The good $m$-tuples obtained from this process must be piecewise constant with at least $2$ distinct entries, and no two good tuples have the same two consecutive distinct entries in the same order. To find the minimum number of good tuples obtained, note

$$\text{number of good tuples obtained }=\text{ number of times the process repeated,}$$

which can be minimised if at each step $k$ a good $m$-tuple $(b_{1}^{(k)},\ldots,b_{1}^{(k)},\ldots,b_{\ell_{k}}^{(k)},\ldots,b_{\ell_{k}}^{(k)})$ is obtained such that

$$S_{k}\cap\{(a_{1},\ldots,a_{1},a_{2},\ldots,a_{2},\ldots):\exists i,i^{\prime},j\text{ s.t. }i<i^{\prime}\text{ and }a_{i}=b_{j}^{(k)},a_{i^{\prime}}=b_{j+1}^{(k)}\}$$

is maximised. However, the size of this set is clearly at most the size of

$$S_{1}\cap\{(a_{1},\ldots,a_{1},a_{2},\ldots,a_{2},\ldots):\exists i,i^{\prime},j\text{ s.t. }i<i^{\prime}\text{ and }a_{i}=b_{j}^{(k)},a_{i^{\prime}}=b_{j+1}^{(k)}\}$$

Therefore, the number of elements removed every time is

$$\begin{aligned}&\leq\#(\text{choices of $j$})\cdot\#(\text{choices of $i,i^{\prime}$})\\ &\quad\ \#(\text{choices of $a_{k}$ for $k\neq i,i^{\prime}$})\cdot\#(\text{choices of order for $a_{i}$ with $a_{i}$ before $a_{i^{\prime}}$})\\ &\leq(\ell_{k}-1)\binom{\lceil\frac{M{}}{\lfloor c(m-1)/(r-1)\rfloor}\rceil}{2}\binom{\varphi(q)-2}{\lceil\frac{M{}}{\lfloor c(m-1)/(r-1)\rfloor}\rceil-2}\cdot\left\lceil\frac{M{}}{\lfloor c(m-1)/(r-1)\rfloor}\right\rceil!\cdot\frac{1}{2}.\end{aligned}$$

To maximise the number of elements removed, we suppose for all $k$, $\ell_{k}=\lceil\frac{M{}}{\lfloor c(m-1)/(r-1)\rfloor}\rceil$, since this is the greatest possible value of $\ell_{k}$. Repeating this process until it terminates, the number of good tuples obtained in this way is

$$\begin{aligned}&\geq 4\binom{\varphi(q)}{\lceil\frac{M{}}{\lfloor c(m-1)/(r-1)\rfloor}\rceil}\binom{\varphi(q)-2}{\lceil\frac{M{}}{\lfloor c(m-1)/(r-1)\rfloor}\rceil-2}^{-1}\left(\left\lceil\frac{M{}}{\lfloor c(m-1)/(r-1)\rfloor}\right\rceil\right)^{-3}\\ &\geq 4\left(\left\lceil\frac{M{}}{\lfloor c(m-1)/(r-1)\rfloor}\right\rceil\right)^{-5}\varphi(q)(\varphi(q)-1).\end{aligned}$$

By Dirichlet’s Theorem on primes in arithmetic progressions, for each $a\in(\mathbb{Z}/q\mathbb{Z})^{\times}$, there are infinitely many primes $p\equiv a\ (\mathrm{mod}\ q)$. Therefore, for each good $m$-tuple

$$\mathbf{a}=(a_{1},\ldots,a_{1},\ldots,a_{\ell},\ldots,a_{\ell})$$

obtained from the above process, by the pigeonhole principle we can create another good tuple by shifting: there exists $a\in(\mathbb{Z}/q\mathbb{Z})^{\times}$ such that

$$\mathbf{a}^{\prime}:=(a_{1},\ldots,a_{1},\ldots,a_{\ell},\ldots,a_{\ell},a)$$

is good, and we can keep shifting the resultant good tuple to get another good tuple.\

Let $G_{0}\subseteq\prod_{i=1}^{m}(\mathbb{Z}/q\mathbb{Z})^{\times}$ be the set of good tuples obtained from the above recursive process, and let $G_{i}$ be the set of good tuples obtained from shifting each tuple in $G_{0}$ $i$ times. We claim that

$$\left|\bigcup_{i=0}^{\lfloor(1-c)m\rfloor}G_{i}\right|=\lfloor(1-c)m\rfloor|G_{0}|,$$

i.e. all good tuples obtained from shifting at most $\lfloor(1-c)m\rfloor$ times are distinct. Indeed, observe from steps (1) and (2), $G_{0}$ has the following property: If $\mathbf{a},\mathbf{b}\in G_{0}$, then there does not exist $1\leq i,j\leq m$ such that $a_{i}=b_{j}$ and $a_{i+1}=b_{j+1}$. Also, $a_{m}$ appears in $\mathbf{a}$ at most $\lfloor c(m-1)/(r-1)\rfloor\cdot(r-1)\leq c(m-1)<cm$ times. Therefore, if we shift $\mathbf{a}$ and $\mathbf{b}$ each at most $\lfloor(1-c)m\rfloor$ times to obtain $\mathbf{a}^{\prime}$ and $\mathbf{b}^{\prime}$ respectively, we must have $(a_{1}^{\prime},a_{2}^{\prime})\neq(b_{1}^{\prime},b_{2}^{\prime})$ and so $\mathbf{a}^{\prime}\neq\mathbf{b}^{\prime}$. Thus, shifting each $m$-tuple in $G_{0}$ $\lfloor(1-c)m\rfloor$ times, we obtain a total of

$$4\lfloor(1-c)m\rfloor\left(\left\lceil\frac{M{}}{\lfloor c(m-1)/(r-1)\rfloor}\right\rceil\right)^{-5}\varphi(q)(\varphi(q)-1)$$

$m$-tuples $\mathbf{a}$ such that $\pi(x;q,\mathbf{a})\to\infty$ as $x\to\infty$. ∎

To simplify the final expression, we have

**Corollary 1.6.** For any $0<c<1$, if $q\geq 2$ is squarefree and $\varphi(q)>8c^{-1}e^{2}(\log m)^{2}$, then for $m$ sufficiently large,

$$\#\left\{\mathbf{a}\in\prod_{i=1}^{m}(\mathbb{Z}/q\mathbb{Z})^{\times}:\lim_{x\to\infty}\pi(x;q,\mathbf{a})=\infty\right\}\geq\frac{\lfloor(1-c)m\rfloor c^{5}}{256e^{10}(\log m)^{10}}\varphi(q)(\varphi(q)-1).$$

*Proof.* Letting $r=\lceil\log m+1\rceil$ in Theorem 1.5, we have $M{}/(m-1)<8e^{2}\log m$ as $m\to\infty$. Using Corollary 8.1, for $m$ sufficiently large there are at least

$$\geq\frac{4\lfloor(1-c)m\rfloor c^{5}}{4^{5}e^{10}(\log m)^{10}}\varphi(q)(\varphi(q)-1)$$

$m$-tuples $\mathbf{a}$ such that $\pi(x;q,\mathbf{a})\to\infty$ as $x\to\infty$. ∎

**Remark.** Shiu (2000) showed for all $a\in(\mathbb{Z}/q\mathbb{Z})^{\times}$ and $\mathbf{a}=(a,\ldots,a)\in\prod_{i=1}^{m}(\mathbb{Z}/q\mathbb{Z})^{\times}$,

$$\lim_{x\to\infty}\pi(x;q,\mathbf{a})=\infty.$$

From Proposition 1.3, we have

$$\#\left\{\mathbf{a}\in\prod_{i=1}^{m}(\mathbb{Z}/q\mathbb{Z})^{\times}:\lim_{x\to\infty}\pi(x;q,\mathbf{a})=\infty\right\}\geq m\varphi(q).$$

Therefore, Corollary 1.6 provides a better bound when

$$\varphi(q)>256e^{10}c^{-5}(1-c)^{-1}(\log m)^{10}+1.$$

To minimise this, we take $c=5/6$, and we get a better bound when

$$\varphi(q)>3823e^{10}(\log m)^{10}+1.$$

We can get a better lower bound for the number of patterns attainable by consecutive primes when $\varphi(q)$ is larger. In this case, the ‘shifting’ argument does not generate many more good tuples, so we do not consider it here.

**Corollary 1.7.** For $m,r\in\mathbb{Z}^{+}$, recall $M$ from Definition 1.4. If $q\geq 2$ is squarefree and $\varphi(q)\geq M{}$, there are at least

$$\frac{\lceil m/(r-1)\rceil!}{M{}(M{}-1)\cdots(M{}-\lceil m/(r-1)\rceil+1)}\cdot\varphi(q)(\varphi(q)-1)\cdots(\varphi(q)-\lceil m/(r-1)\rceil+1)$$

$m$-tuples $\mathbf{a}$ such that $\pi(x;q,\mathbf{a})\to\infty$ as $x\to\infty$.

*Proof.* Using Theorem 1.5, for any $a_{1},\ldots,a_{M{}}$, there must exist $\mathbf{a}=(a_{j(1)},\ldots,a_{j(m)})$ with $j$ increasing and no consecutive $r$ values the same, such that

$$\pi(x;q,\mathbf{a})\to\infty\text{ as }x\to\infty.$$

We call a $m$-tuple $\mathbf{a}$ with this property ‘good’. Define a set $S_{1}$ consisting of all $M{}$-tuples with distinct entries in $(\mathbb{Z}/q\mathbb{Z})^{\times}$. We pick good $m$-tuples with the following recursive process.

1.  Take an $M$-tuple $(a_{1},\ldots,a_{M})\in S_{1}$. By Theorem 1.5, there is a good $m$-tuple of the form

    $$(b_{1},\ldots,b_{1},b_{2},\ldots,b_{2},\ldots,b_{\ell_{1}},\ldots,b_{\ell_{1}}),$$

    where $\lceil m/(r-1)\rceil\leq\ell_{1}\leq m$.

2.  Define

    $$\begin{aligned}S_{2}:=S_{1}\setminus\{(a_{1},\ldots,a_{M}):&\text{ there exists increasing injection }\sigma:\{1,\ldots,\ell_{1}\}\to\{1,\ldots,M\}\\ &\text{ such that }b_{i}=a_{\sigma(i)}\text{ for all }i\}.\end{aligned}$$

3.  Take any element from $S_{2}$, then repeat the above process until $S_{k}$ is empty.

The good $m$-tuples obtained from this process must be piecewise constant with at least $m/(r-1)$ distinct entries, and no two good tuples have the same two consecutive distinct entries in the same order. To find the minimum number of good tuples obtained, note

$$\text{number of good tuples obtained }=\text{ number of times the process repeated,}$$

which can be minimised if at each step $k$ a good $m$-tuple $(b_{1}^{(k)},\ldots,b_{1}^{(k)},\ldots,b_{\ell_{k}}^{(k)},\ldots,b_{\ell_{k}}^{(k)})$ is obtained such that

$$\begin{aligned}S_{k}\cap\{(a_{1},\ldots,a_{M}):&\text{ there exists increasing injection }\sigma:\{1,\ldots,\ell_{k}\}\to\{1,\ldots,M\}\\ &\text{ such that }b_{i}^{(k)}=a_{\sigma(i)}\text{ for all }i\}\end{aligned}$$

is maximised. However, the size of this set is clearly at most the size of

$$\begin{aligned}S_{1}\cap\{(a_{1},\ldots,a_{M}):&\text{ there exists increasing injection }\sigma:\{1,\ldots,\ell_{k}\}\to\{1,\ldots,M\}\\ &\text{ such that }b_{i}^{(k)}=a_{\sigma(i)}\text{ for all }i\}\end{aligned}$$

Therefore, the number of elements removed every time is

$$\begin{aligned}&\leq\#(\text{choices for }a_{j}\neq b_{i})\cdot\#(\text{choices of order for }a_{\sigma(i)}=b_{i}^{(k)}\forall i).\\ &\leq\binom{\varphi(q)-\ell_{k}}{M-\ell_{k}}\cdot\frac{M!}{\ell_{k}!}.\end{aligned}$$

To maximise the number of elements removed, we suppose for all $k$, $\ell_{k}=\lceil\frac{m}{r-1}\rceil$, since this is the smallest possible value of $\ell_{k}$. Repeating this process until it terminates, the number of good tuples obtained is

$$\begin{aligned}&\geq\left\lceil\frac{m{}}{r-1}\right\rceil!\cdot\binom{\varphi(q)}{M}\binom{\varphi(q)-\lceil\frac{m}{r-1}\rceil}{M-\lceil\frac{m}{r-1}\rceil}^{-1}\\ &\geq\binom{M}{\lceil m/(r-1)\rceil}^{-1}\varphi(q)(\varphi(q)-1)\cdots(\varphi(q)-\lceil m/(r-1)\rceil+1).\end{aligned}$$

∎

Simplifying the expression, we have

**Corollary 1.8.** If $q\geq 2$ is squarefree and $\varphi(q)>8e^{2}m\log m$, then for $m$ sufficiently large,

$$\#\left\{\mathbf{a}\in\prod_{i=1}^{m}(\mathbb{Z}/q\mathbb{Z})^{\times}:\lim_{x\to\infty}\pi(x;q,\mathbf{a})=\infty\right\}\gg e^{-O(m\log_{2}m/\log m)}\varphi(q)^{m/\lceil\log m\rceil}.$$

*Proof.* Letting $r=\lceil\log m+1\rceil$ in Theorem 1.5, we have $M{}/(m-1)<8e^{2}\log m$ as $m\to\infty$. For $m$ sufficiently large, using Stirling’s approximation we have

$$\begin{aligned}&\binom{M}{\lceil m/(r-1)\rceil}\\ &=\frac{M!}{\lceil m/(r-1)\rceil!(M-\lceil m/(r-1)\rceil)!}\\ &\ll\frac{M^{M}e^{-M}}{\sqrt{\lceil m/(r-1)\rceil}\lceil m/(r-1)\rceil^{\lceil m/(r-1)\rceil}e^{-\lceil m/(r-1)\rceil}(M-\lceil m/(r-1)\rceil)^{M-\lceil m/(r-1)\rceil}e^{\lceil m/(r-1)\rceil-M}}\\ &\ll\frac{\left(\frac{M}{\lceil m/(r-1)\rceil}-1\right)^{\lceil m/(r-1)\rceil}}{\sqrt{\lceil m/(r-1)\rceil}\left(1-\frac{\lceil m/(r-1)\rceil}{M}\right)^{M}}\\ &\ll\frac{(8e^{2}(\log m)^{2})^{m/\log m}}{\sqrt{m/\log m}\ e^{-m/\log m}}\\ &\ll e^{O(m\log_{2}m/\log m)}.\end{aligned}$$

Therefore by Corollary 1.7, we are done, since for $m$ large it suffices to consider the leading order contribution. ∎

## References

- [1] W. D. Banks, T. Freiberg, and J. Maynard (2016) On limit points of the sequence of normalized prime gaps. Proceedings of the London Mathematical Society 113 (4), pp. 515–539. Cited by: §2, §5, §5, §5, §5, §5, §5, §5, §5, §5, §5, §5, §5, §6, §6, §6, §6, §6, §6.
- [2] H. Davenport (2013) Multiplicative number theory. Vol. 74, Springer Science & Business Media. Cited by: §6.
- [3] N. Kimmel and V. Kuperberg (2024) Consecutive runs of sums of two squares. Journal of Number Theory. Cited by: §1, §1.
- [4] N. Kimmel and V. Kuperberg (2025) Positive density for consecutive runs of sums of two squares. Journal of the Institute of Mathematics of Jussieu 24 (5), pp. 1995–2046. Cited by: §1, §1.
- [5] R. J. Lemke Oliver and K. Soundararajan (2016) Unexpected biases in the distribution of consecutive primes. Proceedings of the National Academy of Sciences 113 (31), pp. E4446–E4454. Cited by: §1.
- [6] J. Maynard (2016) Dense clusters of primes in subsets. Compositio Mathematica 152 (7), pp. 1517–1554. Cited by: §1.
- [7] J. Merikoski (2020) Limit points of normalized prime gaps. Journal of the London Mathematical Society 102 (1), pp. 99–124. Cited by: §2.
- [8] D. K. Shiu (2000) Strings of congruent primes. Journal of the London Mathematical Society 61 (2), pp. 359–373. Cited by: §1, §1, Remark.
