# Catalan’s constant is irrational

OpenAI

## Abstract

We prove that Catalan’s constant $G=\sum_{j\geq0}(-1)^j/(2j+1)^2$ is irrational.

## Introduction

Catalan’s constant is the real number $$G=\beta(2)=\sum_{j=0}^{\infty}\frac{(-1)^j}{(2j+1)^2},
\qquad
\beta(s)=\sum_{j=0}^{\infty}\frac{(-1)^j}{(2j+1)^s}\quad(s>0).$$ It is the simplest even value of the Dirichlet beta function, or equivalently $L(2,\chi_{-4})$ for the odd quadratic character of conductor $4$. Its arithmetic illustrates a basic difficulty in the study of special values: rapidly converging rational approximations need not be sufficiently accurate after their denominators are cleared. We prove the following statement about this individual value.

**Theorem 1.1**. *Catalan’s constant is irrational.*

### Earlier results and the approximation problem

For odd positive integers, the beta values are rational multiples of the corresponding powers of $\pi$. The even values present a different arithmetic problem [19, Introduction]. Rivoal and Zudilin proved that infinitely many even beta values are irrational, and that at least one of $\beta(2),\beta(4),\ldots,\beta(14)$ is irrational [19, Theorems 1 and 2]. Zudilin reduced this finite collection to the six values through $\beta(12)$ [28, Theorem 1]. Lai and Zhou subsequently reduced it to the five values $\beta(2),\beta(4),\beta(6),\beta(8),\beta(10)$ [15, Theorem 6.1]. Fischler obtained stronger quantitative results for irrationality and linear independence in families of Dirichlet $L$-values [9, Theorems 1 and 2]. Such family results guarantee irrational members without identifying the particular value $\beta(2)$.

For an individual value, the basic approximation criterion requires nonzero integer linear forms $A_mG-B_m$ that tend to zero. Convergence of $B_m/A_m$ to $G$ alone does not suffice: multiplication by $A_m$ may remove the decay. Apéry’s recurrence constructions for $\zeta(2)$ and $\zeta(3)$ [2], and Beukers’s integral proofs of their irrationality [3] succeed because the analytic decay survives the necessary denominator clearing. For Catalan’s constant, Zudilin constructed Apéry-like recurrences, a continued fraction and double-integral representations [26, Theorems 1–3]. His discussion following Theorem 1 makes the obstruction explicit: the displayed integer linear forms do not tend to zero, despite the rapid convergence of their rational quotients.

The denominators themselves became an important part of the problem. Rivoal connected Padé approximation with the hypergeometric construction and proved its conjectured denominator bounds [18, Theorems 1 and 2]. Krattenthaler and Rivoal subsequently gave a more direct hypergeometric proof of these bounds [13, Theorems 1 and 2]. These results establish arithmetic cancellation that is invisible in a crude estimate of the individual summands. They still leave a denominator cost too large for the small-linear-form criterion. Krattenthaler and Zudilin later identified two apparently different hypergeometric constructions of the same approximants [14, Section 2 and Theorem 2]. Such identities matter arithmetically because different expressions can make different denominator factors visible.

Nesterenko developed effective approximations using half-integer hypergeometric series and double Euler integrals [17]. Viola announced joint work with Marcovecchio improving an approximation exponent through the Rhin–Viola permutation-group method [23]; their report gives the exponent $0.6293\ldots$ for its explicit approximants. A recent preprint of Eskandari constructs further explicit rational approximations satisfying $0<|G-p_m/q_m|\le q_m^{-0.62}$ for all sufficiently large $m$ [8, Theorem 1.1]. These are bounds for particular constructions, not irrationality measures. An error bound with exponent below $1$ does not by itself make the integer forms $q_mG-p_m$ tend to zero.

Results at other characters and other places give useful comparisons. Calegari, Dimitrov and Tang proved the $\mathbb Q$-linear independence of $1$, $\pi^2$ and $L(2,\chi_{-3})$ [5, Theorem A]. Their character has conductor $3$, rather than the conductor $4$ of $G$. Their discussion of two Catalan approximation families again identifies the denominator cost as an obstruction for those constructions [5, Remark 11.1.17]. Calegari proved irrationality of a $2$-adic analogue $G_2\in\mathbb Q_2$ [4, Theorem 4.2]. As explained by Calegari, Dimitrov and Tang [6, Section 5.2, footnote 2], the related real identity contains an additional $\pi^2$ term that is absent in the $2$-adic identity. This illustrates why the $2$-adic result does not settle the real problem. In our construction, cancellation of an additional $\zeta(2)$ term is likewise essential, although the moment identities and the cancellation argument are proved directly below.

Sun [22, Theorem 1.1] has also announced a proof of the same qualitative irrationality statement. No result from that preprint is used here.

### The determinant strategy

We construct determinants $\Delta_N$ of size $n=48N$ whose entries combine moments of two elementary kernels. Each moment is a rational linear combination of $1$, $G$ and $\zeta(2)$. The polynomial rows are chosen to have high Taylor contact: two prescribed expressions in the rows have identical initial Taylor coefficients. This agreement cancels the $\zeta(2)$ term in every entry. Consequently, the single hypothesis $G\in\mathbb Q$ makes all the determinants rational.

For a nonzero rational number, its ordinary absolute value is determined by its prime valuations. Bounds on the denominators of $\Delta_N$ therefore give a lower bound on $\log|\Delta_N|$. An integral formula for the same determinant gives an upper bound. The contradiction comes from making these bounds incompatible as the size grows. Zudilin’s determinantal criterion gives a useful precedent for this comparison [27, Proposition 2 and Section 2]. There, a positive moment representation produces Hankel determinants with squared-Vandermonde integrals. Positivity supplies nonvanishing, and the denominator and integral estimates are compared on the scale of the square of the matrix size. His discussion of Catalan’s constant explains why the denominator growth of the approximation family considered there still prevents application of the criterion [27, Section 6]. Our determinant is mixed and signed; its nonvanishing and its real-place estimate require separate arguments.

Three features of the construction make this comparison possible. First, integral Chebyshev rows provide both the Taylor contact and useful divisibility. At the large odd primes relevant to the leading bound, denominators of order $p^2$ and $p$ must both be controlled. The arithmetic estimate follows these two layers separately; cancellation at the first layer alone would not give the required denominator bound.

Second, nonvanishing is arithmetic. Under the hypothesis $G\in\mathbb Q$, when $N=p$ is itself a sufficiently large prime, Frobenius and a pair of polynomial bases reduce the growing matrix to three fixed rational matrices. An exact finite certificate proves their nonvanishing. The reduction then gives nonzero determinants along an unbounded prime sequence, without asserting positivity of the mixed determinant.

Third, the real estimate respects both branches of the rational parametrization used to construct the rows. A bounded holomorphic interpolant controls their mixed evaluations in one range of configurations; a Hadamard bound treats the complementary range. The interpolation estimate is uniform even when nodes approach one another. Its proof uses a finite-dimensional Hardy-space operator, so the evaluation determinant cancels algebraically rather than introducing an inverse-Vandermonde estimate. Andréief’s integration identity [10], Cauchy’s double alternant [12], and the kernel/compression viewpoint of analytic interpolation [21] supply the classical context; the specific estimates are proved below.

The resulting Vandermonde products have logarithmic interactions, as in logarithmic potential theory [20]. A Chebyshev expansion of the logarithmic kernel [11, Lemma 3.1] reduces the estimate to quadratic sums and two one-variable functions in each case. We regularize their interactions together, control the omitted diagonals and endpoint terms, and only then take a supremum and pass to the limit. Explicit rational trial coefficients finish the argument. Their certificate exhausts all stationary points and bounds entire root brackets, rather than relying on a numerical search for the maxima.

For orientation, the two estimates are stated for the same normalized logarithm $$\begin{equation}
\tag{1}
\mathcal L_N=\frac{\log|\Delta_N|}{(48N)^2}-\frac12\log 2.
\end{equation}$$ Under the rationality hypothesis, Proposition 3.4 gives $\liminf\mathcal L_N>-2.29084$ along every sequence of nonzero determinants, and Proposition 4.1 supplies such a sequence with $N$ prime. Independently, Proposition 7.1 gives $\limsup\mathcal L_N\le-2.290939875<-2.2909$. These inequalities are incompatible. The argument proves qualitative irrationality; a bound for an irrationality measure would require additional control of rational approximations. Section 8 also deduces irrationality of the minimum volume of an orientable complete finite-volume hyperbolic three-manifold with exactly two cusps, and of certain arithmetic hyperbolic volumes.

### Organization and conventions

Section 2 constructs the rows and moments, proves cancellation and rationality, and gives the estimate at the prime $2$. Section 3 treats odd primes and derives the finite-place lower bound. Its only prime-distribution input is the ordinary prime number theorem; the weighted consequence needed here is proved locally. Section 4 establishes nonvanishing at prime scales. Sections 5 and 6 give the uniform real-place and energy estimates. Section 7 supplies the rational data certifying the real-place bound, and Section 8 assembles the contradiction.

All logarithms are natural. We use $v_p(p)=1$ and $v_p(0)=+\infty$; for real estimates we put $\log 0=-\infty$. Constants in asymptotic estimates may depend on the fixed rational value hypothetically assigned to $G$, but never on $N$ or on the integration points. The finite certificates are specified by rational data and arithmetic instructions in the text; supplementary programs reproduce them.

## Polynomial rows and mixed moments

We construct the determinant and prove that its entries are rational under $G\in\mathbb Q$. The row design serves two purposes: Taylor contact cancels $\zeta(2)$, while integral Chebyshev coefficients permit the finite-prime estimates. After the moment calculations, we establish the estimate at $2$; odd primes are treated in the next Section.

For each positive integer $N$, set $$\begin{equation}
\tag{2}
\begin{gathered}
n=48N,\qquad a=11N,\qquad b=7N,\qquad q=g=4N,\qquad h=2N,\\
L=n+a=n+b+q=59N,\qquad C=L+g=63N,\\
H=C+h=65N,\qquad A=a+2g=19N.
\end{gathered}
\end{equation}$$ Write $f(t)=\sqrt{1-t^2}$, with the positive branch on $(-1,1)$, and $w=t/(1+f)$. Then $$t=\frac{2w}{1+w^2},\qquad f=\frac{1-w^2}{1+w^2}.$$ The involution denoted by a star sends $w$ to $w^{-1}$, fixes $t$, and sends $f$ to $-f$. For $0\le r<n$, define $$\begin{equation}
\tag{3}
R_r=(1-t)^h t^{C-1}w^{r-g},\qquad
P_r=\frac{R_r+R_r^*}{2},\qquad
D_r=\frac{t(R_r^*-R_r)}{2f}.
\end{equation}$$ Here and below identities involving $f$ near zero use its Taylor branch with $f(0)=1$.

Let $T_d,U_d$ be the Chebyshev polynomials, normalized by $T_0=1,T_1=x,U_{-1}=0,U_0=1$, and the recurrence $S_{d+1}=2xS_d-S_{d-1}$. The associated Laurent expressions are the standard formulas [16, Equations (18.5.1)–(18.5.2)]. Since $(w+w^{-1})/2=1/t$ and $(w^{-1}-w)/2=f/t$, Equation (3) becomes, with $d=|r-g|$, $$P_r=(1-t)^h t^{C-1}T_d(1/t),\qquad
D_r=\operatorname{sgn}(r-g)(1-t)^h t^{C-1}U_{d-1}(1/t).$$ In particular these are integer polynomials; the second is zero when $r=g$. The inequality $d\le n-1-g$ gives $$\begin{equation}
\tag{4}
\operatorname{supp}P_r\subseteq\{A,\ldots,H-1\},\qquad
\operatorname{supp}D_r\subseteq\{A+1,\ldots,H-1\}.
\end{equation}$$ Moreover $w=t/2+O(t^3)$, so that $$\begin{equation}
\tag{5}
\frac{tP_r}{f}-D_r=\frac{tR_r}{f}=O(t^{C+r-g})=O(t^L).
\end{equation}$$

For nonnegative integers $i,j$, define $$\begin{equation}
\tag{6}
\begin{split}
M(i,j)&=\int_{-1}^1\int_0^1
 \frac{|t|}{f(t)}\frac{t^i s^j}{1-ts}\,ds\,dt,\\
Z(i,j)&=\int_0^1\int_0^1\frac{t^i s^j}{1-ts}\,ds\,dt.
\end{split}
\end{equation}$$ Extend these expressions bilinearly to polynomial arguments. The integrals converge absolutely. Indeed, for $0<u<1$, $$\int_0^1\frac{ds}{1-us}=\frac{-\log(1-u)}{u},$$ and $(-\log(1-u))/\sqrt{1-u^2}$ is integrable on $(0,1)$. This dominates the absolute $M$ integrand after integration in $s$; the corresponding assertion for $Z$ is weaker. Bounded polynomial factors preserve this domination. It also justifies termwise integration of the geometric series used below.

For each raw column index $b\le j<L$, let $$F_j(r)=M(P_r,j)-\frac32 Z(D_r,j)\qquad(0\le r<n).$$ The determinant used throughout the proof is $$\begin{equation}
\tag{7}
\Delta_N=\det_{0\le r,k<n}
\left(M\bigl(P_r,s^{b+k}(1-s)^q\bigr)
      -\frac32Z\bigl(D_r,s^{b+k}(1-s)^q\bigr)\right).
\end{equation}$$ Thus, if $\mathcal F$ is the $n$ by $n+q$ matrix with columns $F_j$, the matrix in Equation (7) is $\mathcal F\mathcal T$, where the integer matrix $\mathcal T$ has entries $$\begin{equation}
\tag{8}
\mathcal T_{j,k}=(-1)^{j-b-k}\binom{q}{j-b-k},
\qquad b\le j<L,\quad 0\le k<n.
\end{equation}$$ A binomial coefficient outside its usual range is zero. In particular, all raw columns required by the filter lie in the contact range $j<L$.

### Moment evaluation and cancellation

Set $$\begin{equation}
\tag{9}
c_l=4^{-l}\binom{2l}{l}\quad(l\ge0),\qquad
m_i=\int_{-1}^1t^i\frac{|t|}{f(t)}\,dt
=\begin{cases}\displaystyle\frac{2}{(i+1)c_{i/2}},&i\ge0\text{ even},\\
0,&i\ge0\text{ odd},\end{cases}
\end{equation}$$ and use the convention $m_{-1}=0$. The moment formula follows from symmetry, $m_0=2$, and integration by parts, which gives $(i+1)m_i=i m_{i-2}$ for $i\ge1$. Throughout, $c_z$ means zero unless $z$ is a nonnegative integer. Termwise integration gives $$\begin{equation}
\tag{10}
M(i,j)=\sum_{u\ge0}\frac{m_{i+u}}{j+u+1},\qquad
M(i,j)-M(i+1,j+1)=\frac{m_i}{j+1}.
\end{equation}$$

Put $K^-_d=M(d,0)$ and $K^+_d=M(0,d)$. Their boundary recurrences are $$\begin{equation}
\tag{11}
\begin{aligned}
dK^-_d&=(d-1)K^-_{d-2}+m_{d-2}+m_{d-1} &&(d\ge2),\\
K^-_1&=2,\\
(d-1)K^+_d&=(d-2)K^+_{d-2}+\frac{2}{d-1} &&(d\ge2).
\end{aligned}
\end{equation}$$ For the first recurrence, the moment recurrence gives the termwise identity $$\frac{d m_{d+u}-(d-1)m_{d+u-2}}{u+1}
=m_{d+u-2}-m_{d+u}.$$ The right side telescopes, since $m_v\to0$ as $v\to\infty$. The same identity for $d=1$, with the term multiplied by $d-1$ omitted, gives $K^-_1=m_{-1}+m_0=2$. For the last recurrence, shifting the first series by two leaves, for $u\ge2$, the terms $$\frac{(d-1)m_{u-2}-(d-2)m_u}{d+u-1}=m_{u-2}-m_u.$$ Their sum is $2$; the remaining boundary term is $-2(d-2)/(d-1)$, giving the claimed result.

The two independent starting values are $$\begin{equation}
\tag{12}
K^-_0=K^+_0=4G,\qquad K^+_1=\frac{\pi^2}{4}=\frac32\zeta(2).
\end{equation}$$ To verify the first, integrate in $s$ and put $t=\sin\theta$ on the positive half interval. This gives $$K^-_0=\int_0^{\pi/2}\log\frac{1+\sin\theta}{1-\sin\theta}\,d\theta
=-4\int_0^{\pi/4}\log\tan v\,dv=4G.$$ The last equality follows on setting $x=\tan v$ and integrating the geometric series for $(1+x^2)^{-1}$ against $-\log x$. For the other start, Equation (10) and Equation (9) yield $$K^+_1=\sum_{k\ge1}\frac{1}{2k^2c_k}.$$ The differential equation $(1-x^2)y''-xy'=2$, with $y(0)=y'(0)=0$, determines the Taylor series of $y=(\arcsin x)^2$ as $\sum_{k\ge1}x^{2k}/(2k^2c_k)$. Its nonnegative coefficients allow passage to $x=1$ by monotone convergence, giving $\pi^2/4$. For completeness, integrating $$\sum_{k\ge1}\frac{\rho^k\sin(kx)}{k}
=\operatorname{Im}\bigl(-\log(1-\rho e^{ix})\bigr),\qquad0<\rho<1,$$ over $0<x<\pi$ and letting $\rho\uparrow1$ gives $2\sum_{k\text{ odd}}k^{-2}=\pi^2/4$. Here the imaginary part is uniformly bounded and tends to $(\pi-x)/2$, so dominated convergence applies. The odd sum is $3\zeta(2)/4$, establishing the final equality in Equation (12).

Define $M^0(i,j)$ by the rational recurrences (10)–(11), replacing only the starts $K^-_0=K^+_0$ and $K^+_1$ by zero. More explicitly, let $k^-_d,k^+_d$ satisfy Equation (11) with $$\begin{equation}
\tag{13}
k^-_0=k^+_0=k^+_1=0,\qquad k^-_1=2.
\end{equation}$$ Then the following formulas specify the whole array without ambiguity: $$\begin{equation}
\tag{14}
M^0(i,j)=
\begin{cases}
\displaystyle k^-_{i-j}-\sum_{k=1}^{j}\frac{m_{i-j+k-1}}{k},&i\ge j,\\[6pt]
\displaystyle k^+_{j-i}-\sum_{k=j-i+1}^{j}
                  \frac{m_{k-(j-i)-1}}{k},&i<j.
\end{cases}
\end{equation}$$ Empty sums are zero. We shall also use the algebraic convention $$\begin{equation}
\tag{15}
M^0(-1,j)=k^+_{j+1}\qquad(j\ge0);
\end{equation}$$ this does not define an additional integral. Let $B_i^{(d)}=\sum_{k=1}^i k^{-d}$, with $B_0^{(d)}=0$, and put $$\begin{equation}
\tag{16}
Z^0(i,j)=\begin{cases}
-B_i^{(2)},&i=j,\\[2pt]
\displaystyle\frac{B_i^{(1)}-B_j^{(1)}}{i-j},&i\ne j.
\end{cases}
\end{equation}$$ The evaluations of the moments are $$\begin{equation}
\tag{17}
\begin{split}
M(i,j)&=M^0(i,j)+4G c_{(i-j)/2}
                      +\frac32\zeta(2)c_{(j-i-1)/2},\\
Z(i,j)&=Z^0(i,j)+[i=j]\zeta(2).
\end{split}
\end{equation}$$ Indeed, the homogeneous parts of the minus and plus boundary recurrences propagate the starts by precisely these two $c$-kernels. Diagonal reduction preserves both index differences. The formula for $Z$ follows from $$Z(i,j)=\sum_{u\ge0}\frac{1}{(i+u+1)(j+u+1)}$$ by partial fractions when $i\ne j$, and directly when $i=j$.

For later valuation calculations, it is useful to solve the rational boundary recurrences explicitly. Define $$\begin{equation}
\tag{18}
H_z^*=\begin{cases}
c_{z/2},&z\ge0\text{ even},\\
\displaystyle\frac{1}{z c_{(z-1)/2}},&z\ge1\text{ odd}.
\end{cases}
\qquad\frac{H_{z+2}^*}{H_z^*}=\frac{z+1}{z+2}.
\end{equation}$$ Then $$\begin{equation}
\tag{19}
\begin{split}
k^-_u&=\begin{cases}
\displaystyle H_u^*\sum_{\substack{1\le z\le u\\z\ \text{even}}}
            \frac{2}{z^2(H_z^*)^2},&u\text{ even},\\[6pt]
\displaystyle H_u^*\sum_{\substack{1\le z\le u\\z\ \text{odd}}}
            \frac{2}{z},&u\text{ odd},
\end{cases}\\
k^+_{u+1}&=H_u^*\sum_{\substack{1\le z\le u\\z\equiv u\ (2)}}
                 \frac{2}{z^2H_z^*}\qquad(u\ge0).
\end{split}
\end{equation}$$ To see this, divide each recurrence by the appropriate $H^*$ and use the ratio in Equation (18). For the minus recurrence the inhomogeneous increment after division is $2/(z^2(H_z^*)^2)$ when $z$ is even and $2/z$ when $z$ is odd. The odd case starts with $k^-_1/H_1^*=2$. For the plus recurrence the increment is $2/(z^2H_z^*)$, with initial values $k^+_1=0$ and $k^+_2=2$. This proves all the formulas, including their empty-sum cases.

**Proposition 2.1**. *Each raw entry $F_j(r)$ lies in $\mathbb Q+\mathbb QG$. Consequently, if $G\in\mathbb Q$, then $\Delta_N\in\mathbb Q$ for every positive integer $N$.*

*Proof.* Since $f(t)^{-1}=\sum_{l\ge0}c_l t^{2l}$, the coefficient of $\zeta(2)$ in $F_j(r)$ is $$\frac32\left(\sum_i[t^i]P_r\,c_{(j-i-1)/2}-[t^j]D_r\right)
=\frac32[t^j]\left(\frac{tP_r}{f}-D_r\right)=0$$ by Equation (5) and $j<L$. More explicitly, $$\begin{equation}
\tag{20}
F_j(r)=\sum_i[t^i]P_r
       \left(M^0(i,j)+4G c_{(i-j)/2}\right)
       -\frac32\sum_i[t^i]D_r Z^0(i,j).
\end{equation}$$ The assertion follows from the rational arrays and the integer filter. ◻

### A uniform estimate at the prime two

We normalize $v_p(p)=1$ and set $v_p(0)=+\infty$. In the rest of this section assume $G\in\mathbb Q$, viewed also in $\mathbb Q_2$. Constants allowed to depend on this fixed rational number will carry a subscript $G$.

**Proposition 2.2**. *With $\delta=(q+g+h)/n=5/24$, one has, for every positive integer $N$, $$\begin{equation}
\tag{21}
v_2(\Delta_N)\ge
-\left(\frac{\delta}{2}+\frac{\delta^2}{8}\right)n^2
-O_G\bigl(n\log(n+2)\bigr)
=-\frac{505}{4608}n^2-O_G\bigl(n\log(n+2)\bigr).
\end{equation}$$ The same bound holds for every full minor of the raw column matrix.*

*Proof.* We first construct a $2$-adic version of the geometric moment series: $$\begin{equation}
\tag{22}
M_{\rm s}(i,j)=\sum_{k\ge0}\frac{m_{i+k}}{j+k+1}\quad\text{in }\mathbb Q_2.
\end{equation}$$ For even $u$, the factorial formula implies $$v_2(m_u)=1+u-v_2\binom{u}{u/2}
\ge u+1-\log_2(u+1).$$ The last bound follows, for example, by subtracting the factorial-floor formulas: each binary place contributes at most one to the binomial valuation. Odd moments are zero. If $0\le i,j<H$, every nonzero term of Equation (22) therefore has valuation at least $$\begin{equation}
\tag{23}
i+k+1-2\log_2(H+k)
\ge i+1-2\log_2 H+k-2\log_2(k+1)
\ge i-2\log_2 H-1.
\end{equation}$$ The middle expression tends to infinity with $k$. Thus the infinite tail converges, and the final bound is uniform over all its terms and over $0\le i,j<H$. In particular $v_2(M_{\rm s}(i,j))\ge i-2\log_2H-1$.

The diagonal recurrence and both boundary recurrences hold for $M_{\rm s}$ as well. The same finite telescoping calculations prove this because their tails tend to zero $2$-adically. In particular its minus start at one is forced to be $2$. There are therefore exactly two homogeneous discrepancies between $M_{\rm s}$ and the rational part $M^0(i,j)+4G c_{(i-j)/2}$. Write $$\begin{equation}
\tag{24}
e_1=4G-M_{\rm s}(0,0),\qquad e_2=-M_{\rm s}(0,1).
\end{equation}$$ These are fixed elements of $\mathbb Q_2$, independent of $N$ and of all degree indices, and $$M^0(i,j)+4G c_{(i-j)/2}
=M_{\rm s}(i,j)+e_1c_{(i-j)/2}+e_2c_{(j-i-1)/2}.$$ Contracting the last kernel with $P_r$ and applying Equation (5) expresses each raw column as the sum of three column vectors: $$\begin{equation}
\tag{25}
\begin{split}
F_j(r)&=S_j(r)+E_j(r)+B_j(r),\\
S_j(r)&=M_{\rm s}(P_r,j),\\
E_j(r)&=e_1\sum_i[t^i]P_r\,c_{(i-j)/2},\\
B_j(r)&=\sum_i[t^i]D_r\left(e_2[i=j]-\frac32Z^0(i,j)\right).
\end{split}
\end{equation}$$ If either discrepancy is zero, the corresponding summands vanish; there is no need to assign a finite valuation to a zero constant.

Here are the coefficient and denominator bounds needed for these columns. Remove the factor $(1-t)^h$ and write the resulting polynomials as $$\begin{equation}
\tag{26}
\frac{P_r(t)}{(1-t)^h}=\sum_{u\ge0}p_{r,u}t^{C-1-u},\qquad
\frac{D_r(t)}{(1-t)^h}=\sum_{u\ge0}d_{r,u}t^{C-1-u}.
\end{equation}$$ All sums here are finite. Induction in the Chebyshev recurrence shows that the coefficient of $x^u$ in $T_d$ has valuation at least $u-1$ and that in $U_d$ has valuation at least $u$; the assertion at $u=0$ uses only integrality. Hence $$\begin{equation}
\tag{27}
v_2(p_{r,u})\ge u-1,\qquad v_2(d_{r,u})\ge u-1.
\end{equation}$$ Convolution with $(1-t)^h$ uses integer coefficients. Combining Equations (23) and (27), every entry of $S_j$ has valuation at least $C-2\log_2H-3$.

Set $L_2=\lfloor\log_2H\rfloor$. Equation (16) gives $$\begin{equation}
\tag{28}
v_2(Z^0(i,j))\ge-2L_2\qquad(0\le i,j<H).
\end{equation}$$ Indeed, the harmonic sum of order $d$ has valuation at least $-dL_2$; when $i\ne j$, division by $i-j$ loses at most another $L_2$. The ultrametric inequality introduces no loss for the number of terms in these sums or in polynomial convolutions.

Choose a fixed nonnegative integer $K_G$ with $v_2(e_1),v_2(e_2)\ge-K_G$. Let $\mathbf p_u=(p_{r,u})_r$ and $\mathbf d_u=(d_{r,u})_r$. The exceptional columns in Equation (25) have expansions $$E_j=\sum_u\mathbf p_u\,a_{u,j},\qquad
B_j=\sum_u\mathbf d_u\,b_{u,j},$$ where $$\begin{align*}
a_{u,j}&=e_1\sum_{v=0}^h(-1)^v\binom hv
                    c_{(C-1-u+v-j)/2},\\
b_{u,j}&=\sum_{v=0}^h(-1)^v\binom hv
 \left(e_2[C-1-u+v=j]-\frac32Z^0(C-1-u+v,j)\right).
\end{align*}$$ Only $u$ with a nonzero coefficient vector need be included, so all moment indices in these expressions are between $0$ and $H-1$. Since $v_2(c_l)\ge-2l$, every contributing summand yields $$\begin{equation}
\tag{29}
v_2(a_{u,j})\ge u+j-H+1-K_G,\qquad
v_2(b_{u,j})\ge-2L_2-1-K_G.
\end{equation}$$

We now apply the bounds in the order needed to preserve alternation. First expand $\det(\mathcal F\mathcal T)$ by Cauchy–Binet. Each term is an integer times a full raw minor, whose column indices $j_1,\ldots,j_n$ are distinct. Fix such a minor, expand each column by Equation (25), and consider a term containing $m$ columns of type $E$, $l$ of type $B$, and $n-m-l$ columns of type $S$.

Expand the $E$ columns through the fixed vectors $\mathbf p_u$ and the $B$ columns through the fixed vectors $\mathbf d_u$. Repeated indices within the first group give equal coefficient vectors and hence zero determinants; the same holds within the second group. No distinctness between the two groups is asserted or needed. For nonzero terms we therefore have $$\sum_{E\text{ columns}}u\ge\frac{m(m-1)}2,\qquad
\sum_{B\text{ columns}}u\ge\frac{l(l-1)}2.$$ The already fixed, distinct raw column indices also give $$\sum_{E\text{ columns}}j\ge mb+\frac{m(m-1)}2.$$ Equations (27) and (29) show that the first group contributes at least $2\sum u+\sum j-Hm-K_Gm$. The second contributes at least $\sum u-O_G(l\log(H+2))$; the smoothed columns contribute at least $C(n-m-l)-O((n-m-l)\log(H+2))$. Thus every term, every raw minor, and finally the filtered determinant satisfies $$\begin{equation}
\tag{30}
\begin{split}
v_2(\Delta_N)\ge{}&-O_G(n\log(n+2))\\
&+\min_{\substack{m,l\ge0\\m+l\le n}}
\left\{-(H-b)m+\frac32m^2+\frac12l^2+C(n-m-l)\right\}.
\end{split}
\end{equation}$$ Finite summation causes no further loss in valuation.

For completeness minimize over real $m,l$; this can only lower the minimum over integer choices. Since $C\ge n$, the expression decreases as $l$ increases up to $n-m$, so its minimum occurs at $l=n-m$. Using $H-b=n(1+\delta)$, the remaining expression is $$\frac{n^2}{2}-(2+\delta)nm+2m^2
=2\left(m-\frac{(2+\delta)n}{4}\right)^2
 -\left(\frac\delta2+\frac{\delta^2}{8}\right)n^2.$$ This proves Equation (21) and the stated bound for each raw minor. ◻

## Odd primes and the finite-place lower bound

Throughout this section assume that $G\in\mathbb Q$, so that the columns $F_j$ of Section 2 are rational. We regard each $F_j$ as a column in $\mathbb Q^n$. For an odd prime $p$, reduction modulo $p$ always means reduction of a member of $\mathbb Z_p$; in particular, every congruence below includes the assertion that its two sides are locally integral.

The raw matrix has $n+q$ columns, whereas the filtered determinant has size $n$. At the large primes treated first, each raw column has at most two powers of $p$ in its denominator. We shall make invertible column changes over $\mathbb Z_p$ and bound how many columns can still have denominator $p^2$ or $p$. Such bounds control every full minor of the raw matrix, and Cauchy–Binet then transfers them to the integer column filter. The first reduction identifies residues after multiplication by $p^2$; for $p>H/2$ a second reduction identifies the remaining residues after multiplication by $p$.

### Digit reduction of the rational moments

We first prove the reductions needed at primes $$2\sqrt H<p\le H.$$ We may suppose that $p$ does not divide the denominator of $G$: as $N$ tends to infinity, every fixed denominator prime eventually lies below $2\sqrt H$. Put $$E(t)=(1-t^2)^{(p-1)/2}=\sum_{d=0}^{p-1}E_dt^d
 \quad\text{in }\mathbb F_p[t],\qquad
 \epsilon=(-1)^{(p-1)/2}.$$ We set $E_d=0$ outside $0\le d<p$. Within this range, $$E_d=\begin{cases}c_{d/2}\pmod p,&d\text{ even},\\0,&d\text{ odd},\end{cases}
 \qquad E_{p-1-d}=\epsilon E_d.$$ The first identity follows from $(-1)^k\binom{(p-1)/2}{k}\equiv4^{-k}\binom{2k}{k}$; the second follows by reversing the coefficients of $E$.

**Lemma 3.1** (Digit reductions). *For $0\le i,j<H$, let $$\ell=j\bmod p,\quad d=(j-i-1)\bmod p,
 \qquad
 i'=\frac{i+1+d-\ell}{p}-1,\quad j'=\left\lfloor\frac jp\right\rfloor,
 \qquad 0\le\ell,d<p.$$ Then $i'\ge-1$, and, with the convention $M^0(-1,j')=k^+_{j'+1}$, $$\begin{equation}
\tag{31}
 \begin{split}
 p^2M^0(i,j)&\equiv E_dM^0(i',j')\pmod p,\\
 p^2Z^0(i,j)&\equiv
 \begin{cases}
 Z^0(\lfloor i/p\rfloor,j'),&i\equiv j\pmod p,\\
 0,&i\not\equiv j\pmod p.
 \end{cases}
 \end{split}
\end{equation}$$*

*Proof.* We first give the parity and carry calculation for the factors $H_z^*$ in the explicit formulas of Section 2. Write $z=Pp+r$, $0\le r<p$, $0\le z<H$. Since $H<p^2/4$, all factors at the reduced indices $P$ are $p$-adic units. If $z$ is even, then $$\begin{equation}
\tag{32}
 \begin{cases}
 H_z^*\equiv H_P^*c_{r/2}\pmod p,&r\text{ even},\\
 v_p(H_z^*)=1,&r\text{ odd}.
 \end{cases}
\end{equation}$$ Indeed, when $r$ is even, $P$ is even and the base-$p$ digits of $z/2$ are $P/2,r/2$. Expanding $(1+x)^z$ modulo $p$ by $(1+x)^p=1+x^p$ gives the first assertion, including the factor $4^{-z/2}$. When $r$ is odd, $P$ is odd and the low digit of $z/2$ is $(p+r)/2$. The factorial formula for $\binom z{z/2}$ has exactly one carry: $$\left\lfloor\frac zp\right\rfloor
       -2\left\lfloor\frac{z/2}{p}\right\rfloor=1,$$ and there is no contribution from $p^2$. Thus, for positive even $z$, $v_p(zH_z^*)$ is either zero or one. It is one precisely when $r=0$ or $r$ is odd.

For odd $z$ one has $$\begin{equation}
\tag{33}
 \frac1{H_z^*}\in\mathbb Z_p,\qquad
 pH_z^*\equiv
 \begin{cases}
 \epsilon c_{r/2}H_P^*,&r\text{ even},\\
 0,&r\text{ odd}.
 \end{cases}
\end{equation}$$ If $r$ is odd, both $z$ and $c_{(z-1)/2}$ are units by the same digit calculation. If $r$ is even, $P$ is odd. At $z=Pp$, digit expansion gives $$c_{(Pp-1)/2}\equiv c_{(P-1)/2}c_{(p-1)/2}
       =\epsilon c_{(P-1)/2},
 \qquad pH_{Pp}^*\equiv\epsilon H_P^*.$$ The recurrence $H_{z+2}^*/H_z^*=(z+1)/(z+2)$, applied through $r=0,2,\ldots,p-1$, now proves the nonzero case of Equation (33). Its denominators on this interval are units. Since $m_{z-1}=2H_z^*$ for odd $z$ and is zero for even $z$, these formulas imply $$\begin{equation}
\tag{34}
 pm_{z-1}\equiv E_{p-1-r}m_{P-1}\pmod p.
\end{equation}$$ This includes $z=0$, using $m_{-1}=0$.

We next reduce the two starting arrays. For $u=Pp+r$, $0\le u<H$, we claim $$\begin{equation}
\tag{35}
 p^2k^-_u\equiv E_{p-1-r}k^-_P,
 \qquad
 p^2k^+_{u+1}\equiv E_r k^+_{P+1}\pmod p.
\end{equation}$$ For odd $u$, write the first formula as $$p^2 k^-_u=(pH_u^*)
           \sum_{\substack{1\le z\le u\\z\text{ odd}}}\frac{2p}{z}.$$ Only $z=mp$, with $m$ odd, survives in the sum. If $r$ is odd the first factor vanishes modulo $p$. If $r$ is even, $P$ is odd and Equation (33) gives $\epsilon E_rH_P^*\sum_{m\le P,\ m\text{ odd}}2/m =E_{p-1-r}k^-_P$, as required.

For even $u$ the quantities $p/(zH_z^*)$, for positive even $z\le u$, are integral. Thus $$p^2k^-_u=H_u^*
     \sum_{\substack{1\le z\le u\\z\text{ even}}}
                  2\left(\frac{p}{zH_z^*}\right)^2$$ is integral, and is zero modulo $p$ when $r$ is odd. If $r$ is even, then $P$ is even. The nonzero summands form precisely the complete blocks $$z=mp-\lambda,\qquad
 m=2,4,\ldots,P,\qquad \lambda=0,2,\ldots,p-1.$$ To see completeness, the indices with $z\bmod p$ odd lie immediately below an even multiple $mp$, while that multiple supplies $\lambda=0$. The upper limit $u=Pp+r$ contains the whole block ending at $Pp$, and the next such block begins at $(P+1)p+1>u$. No partial block is present. The recurrence, started at $mp$ and followed downwards, gives $$\frac{p}{(mp-\lambda)H_{mp-\lambda}^*}
       \equiv\frac{c_{\lambda/2}}{mH_m^*}\pmod p.$$ For example, each downward step from $z$ to $z-2$ multiplies this quantity by $(z-1)/(z-2)$; these multipliers give successively $(2j-1)/(2j)$ modulo $p$. Finally, with $s=(p-1)/2$, $$\sum_{j=0}^{s}c_j^2
  \equiv\sum_{j=0}^{s}\binom{s}{j}^2
  =\binom{2s}{s}\equiv(-1)^s=\epsilon\pmod p.$$ The equality is the coefficient identity obtained from $(1+x)^s(1+x)^s$. Multiplying the block sums by $H_u^*\equiv E_rH_P^*$ proves the first congruence of Equation (35) also for even $u$.

For the second congruence, suppose first that $u$ is even. In $$p^2k^+_{u+1}
   =H_u^*\sum_{\substack{1\le z\le u\\z\equiv u\ (2)}}
                     \frac{2p^2}{z^2H_z^*},$$ every term with $p\nmid z$ vanishes modulo $p$, because $v_p(H_z^*)\le1$. At $z=mp$, necessarily $m$ is even and $H_{mp}^*\equiv H_m^*$. The result is $E_r k^+_{P+1}$ when $r$ is even, and zero when $r$ is odd. For odd $u$ instead write the expression as $$(pH_u^*)\sum_{\substack{1\le z\le u\\z\text{ odd}}}
                         \frac{2p}{z^2H_z^*}.$$ The reciprocal $1/H_z^*$ is integral. Again only multiples $z=mp$ can survive; there $pH_{mp}^*\equiv\epsilon H_m^*$, and the two factors of $\epsilon$ cancel. If $r$ is odd the prefactor is zero. This proves the second congruence in every case and also proves the local integrality asserted in Equation (35).

If $i\ge j$, put $u=i-j=Pp+r$. Then $d=p-1-r$ and $i'=j'+P$. The diagonal reduction is $$M^0(i,j)=k^-_u-\sum_{k=1}^{j}\frac{m_{u+k-1}}k.$$ After multiplication by $p^2$, terms with $p\nmid k$ vanish by Equation (34). At $k=mp$ the surviving term is $E_{p-1-r}m_{P+m-1}/m$. The first starting congruence therefore gives $$p^2M^0(i,j)\equiv E_{p-1-r}
       \left(k^-_P-\sum_{m=1}^{j'}\frac{m_{P+m-1}}m\right)
       =E_dM^0(i',j').$$ If $i<j$, put $u=j-i-1=Pp+r$, so $d=r$ and $i'=j'-P-1$. Now $$M^0(i,j)=k^+_{u+1}-\sum_{k=u+2}^{j}\frac{m_{k-u-2}}k.$$ For a multiple $k=mp$ in the sum, $$k-u-1=(m-P-1)p+(p-1-r).$$ Equation (34) gives the reduced summand $E_r m_{m-P-2}/m$. A possible first multiple with $m=P+1$ contributes zero, since its reduced moment is $m_{-1}$. Thus the reduced sum is over $m=P+2,\ldots,j'$, as in the formula for $M^0(i',j')$. The expression for $i'$ is also $i'=\lfloor(i-\ell)/p\rfloor$, so $i'\ge-1$. When $i'=-1$, $j'=P$, the sum is empty and the starting term is exactly $k^+_{j'+1}=M^0(-1,j')$. This proves the first assertion of Equation (31), including its boundary convention. The reduced array indices are less than $H/p<p/4$; even the boundary index $j'+1$ is less than $p$. Thus the explicit rational formulas show that all quantities on its right side are integral at $p$.

For $Z^0$, write $I=\lfloor i/p\rfloor$ and $J=\lfloor j/p\rfloor$. Because $i,j<p^2$, the harmonic sums satisfy $$pB_i^{(1)}\equiv B_I^{(1)},\qquad
 p^2B_i^{(2)}\equiv B_I^{(2)}\pmod p.$$ The diagonal formula follows at once. Off the diagonal, if $i\not\equiv j\pmod p$, the denominator $i-j$ is a unit and $p^2Z^0(i,j)$ is zero modulo $p$. If the residues agree, $i-j=p(I-J)$ with $I-J$ a unit; substituting the first harmonic congruence gives $Z^0(I,J)$. This also proves integrality of $p^2Z^0(i,j)$. ◻

### The leading layer and paired raw columns

We now gather the moment reductions into column vectors. This will identify pairs of raw columns whose sum has at most one power of $p$ in its denominator. For a fixed residue $0\le\ell<p$, define column vectors over $\mathbb F_p$ by $$P'_u=[t^{(u+1)p+\ell}]\,tP(t)E(t)\quad(u\ge-1),
 \qquad
 D'_u=[t^{up+\ell}]\,D(t)\quad(u\ge0).$$ Here $P,D$ denote the vectors of all row polynomials; the dependence of these extracted vectors on $\ell$ is understood. Their supports are finite. Lemma 3.1, gathered by coefficient residue, gives $$\begin{equation}
\tag{36}
 X_{kp+\ell}:=p^2F_{kp+\ell}\bmod p
   =\sum_{u\ge-1}P'_uM^0(u,k)
          -\frac32\sum_{u\ge0}D'_uZ^0(u,k).
\end{equation}$$ For a term $[t^i]P$, its unique residue $d$ satisfies $i+1+d=(i'+1)p+\ell$, so that it contributes exactly to $P'_{i'}$, including $i'=-1$. The $Z^0$ reduction survives only when $i=up+\ell$, which is precisely the extraction defining $D'_u$. The coefficient of $G$ in $F_j$ is a sum of integral multiples of $c_{(i-j)/2}$. These coefficients are integral at every odd prime, so this term disappears after multiplication by $p^2$. Every raw column therefore lies in $p^{-2}\mathbb Z_p^n$.

If $\ell\ge H-2p$, the degree bounds $\deg(tPE)\le H+p-1$ and $\deg D<H$ show that $P'_u,D'_u$ vanish for $u>1$. Put $$V_\ell=2P'_1-\frac32D'_1,
 \qquad U_\ell=2P'_{-1}-\frac32D'_0.$$ The needed small values of the reduced arrays are $$\begin{array}{c|rrr}
 u&-1&0&1\\\hline
 M^0(u,0)&0&0&2\\
 M^0(u,1)&2&0&-2
 \end{array}
 \qquad
 \begin{array}{c|rr}
 u&0&1\\\hline
 Z^0(u,0)&0&1\\
 Z^0(u,1)&1&-1
 \end{array}.$$ Consequently, whenever the indicated columns exist, $$\begin{equation}
\tag{37}
 X_\ell=V_\ell,\qquad X_{p+\ell}=U_\ell-V_\ell.
\end{equation}$$ Since $tP$ and $D$ have no terms below degree $A+1$, $U_\ell=0$ for $\ell\le A$.

We record explicitly how changes in the full column pool will be used. Let $T$ be the $n$ by $(n+q)$ matrix of all raw columns. If $Q\in\operatorname{GL}_{n+q}(\mathbb Z_p)$ and every full minor of $TQ$ has valuation at least $-D$, the same holds for every full minor of $T=(TQ)Q^{-1}$ by Cauchy–Binet. The coefficients in this expansion are minors of the integral matrix $Q^{-1}$. Applying Cauchy–Binet once more to the integer matrix defining the prescribed filter gives $v_p(\Delta_N)\ge-D$. This transfer applies even when the columns or their leading residues are linearly dependent.

For $2\sqrt H<p\le H/2$, use each pair of columns with $$\max(b,H-2p)\le\ell<\min(p,L-p,A).$$ Their number is exactly $$d_0=\bigl(\min(p,L-p,A)-\max(b,H-2p)\bigr)_+,
 \qquad y_+=\max(y,0).$$ Replacing its high column by the sum of the pair is an integral elementary column operation with integral inverse. The pair sum lies in $p^{-1}\mathbb Z_p^n$ by Equation (37); all other columns still lie in $p^{-2}\mathbb Z_p^n$. These pairs are disjoint, since $\ell<p$. Any selection of $n$ columns from the pool of $n+q$ contains at least $(d_0-q)_+$ of the improved columns. The transfer just explained gives $$\begin{equation}
\tag{38}
 v_p(\Delta_N)\ge-2n+(d_0-q)_+.
\end{equation}$$

### The central layer and integral column elimination

For $p>H/2$, the next lemma identifies the residues of central columns after multiplication by $p$. It expresses them in terms of the same vectors $V_\ell$ that occur in the leading residues of noncentral columns. The elimination proof will retain noncentral columns and use $p$ times those columns to cancel the corresponding $V_\ell$ terms.

**Lemma 3.2** (Central layer). *Suppose $H/2<p\le H$, and write $K=L-p$ and $J=H-p$. For every central column, by which we mean $$b\le j<\min(p,L),\qquad j\ge J,$$ one has $$\begin{equation}
\tag{39}
 pF_j\in\mathbb Z_p^n,\qquad
 pF_j\equiv-\sum_{0\le\ell<J}\frac{V_\ell}{j-\ell}\pmod p.
\end{equation}$$ All denominators $j-\ell$ occurring here are units at $p$.*

*Proof.* For every contributing row degree $0\le i<H$, $i-j\le H-1-J=p-1$ and $j-i<p$. Hence $|i-j|<p$, and the starting value $k^-_{i-j}$ or $k^+_{j-i}$ in the diagonal reduction is integral at $p$. In either case that reduction can be written as the starting value minus $$\sum_{0\le\ell<\min(i,j)}\frac{m_{i-\ell-1}}{j-\ell}.$$ Here $1\le j-\ell<p$. By Equation (34), a nonzero reduction after multiplication by $p$ requires $p\le i-\ell<2p$, and then $$pm_{i-\ell-1}\equiv2E_{2p+\ell-1-i}.$$ Such an index necessarily has $0\le\ell<J$. Conversely its coefficient can be collected over all $i$ with no truncation, since $j\ge J>\ell$ and $i\ge p+\ell>\ell$. Thus $$pM^0(P,j)\equiv-\sum_{0\le\ell<J}\frac{2P'_1}{j-\ell}.$$ The extracted vector $P'_1$ in each summand is the one belonging to that residue $\ell$. For $Z^0(i,j)$, the harmonic sums have a pole only if $i=p+\ell$ with $0\le\ell<J$. The denominator $i-j$ is then a unit: equality modulo $p$ would require $j=\ell<J$. Therefore $$pZ^0(p+\ell,j)\equiv\frac1{\ell-j}.$$ All other $Z^0(i,j)$ are integral. Combining these two calculations with the factor $-3/2$ proves Equation (39); the $G$ term is integral here as before. ◻

We now carry out these cancellations in the full column pool. In the resulting pool, $R$ will count the retained columns with possible denominator $p^2$, and $S$ will bound the number of other columns with possible denominator $p$; every remaining column will be integral. The proof first uses the $V_\ell$ supplied by retained noncentral columns to modify the central columns. We then use the rank of their remaining scaled residues to bound the number of central columns that can still have denominator $p$ after an invertible column change.

**Lemma 3.3** (Elimination over the local integers). *For $H/2<p\le H$, define $$\begin{align*}
 R&=K_++(K-A)_++(J-\max(b,K))_+,\\
 S&=(\min(A,K)-b)_+
        +(\min(b,J)-\max(0,K))_+.
\end{align*}$$ Then every full raw minor, and hence the filtered determinant, satisfies $$\begin{equation}
\tag{40}
 v_p(\Delta_N)\ge-\min(2n,n+R,2R+S).
\end{equation}$$*

*Proof.* The noncentral columns are precisely the high columns $F_{p+\ell}$ for $0\le\ell<K$ and the low columns $F_\ell$ for $b\le\ell<J$. Empty ranges are allowed. Indeed $p>b$, $J<p$, and $K<J$. For $$b\le\ell<\min(A,K)$$ retain the low column and replace the high column by $F_{p+\ell}+F_\ell$. Let $$B=(\min(A,K)-b)_+$$ be the number of these pair sums. Each lies in $p^{-1}\mathbb Z_p^n$. Retain every other noncentral column as a column in $p^{-2}\mathbb Z_p^n$, whether or not its leading residue depends on the others. The number of columns so retained is $$\begin{equation}
\tag{41}
 R_0=K_++(J-b)_+-B.
\end{equation}$$ It equals the stated $R$. To verify the identity, split $K$ into $K\le0$, $0<K\le b$, $b<K\le A$, and $K>A$; use $K<J$ in the last two cases. The resulting formulas are respectively $(J-b)_+$, $K+(J-b)_+$, $J$, and $K+J-A$.

These retained columns furnish a representative of every vector $V_\ell$ with $0\le\ell<J$ except possibly those in $$\mathcal E=\{\ell:\max(0,K)\le\ell<\min(b,J)\}.$$ For $b\le\ell<J$, the retained low column has leading residue $p^2F_\ell\equiv V_\ell$. For $0\le\ell<\min(b,K)$, the unpaired high column has leading residue $-V_\ell$, because $\ell<b<A$ makes $U_\ell=0$. These two ranges exhaust the complement of $\mathcal E$. Denote the size of $\mathcal E$ by $$e=|\mathcal E|=(\min(b,J)-\max(0,K))_+.$$

For each represented residue choose a retained column $Y_\ell$ and a sign $\sigma_\ell\in\{1,-1\}$ such that $p^2Y_\ell\equiv\sigma_\ell V_\ell$. For every central $j$, choose $a_{\ell j}\in\mathbb Z_p$ reducing to $\sigma_\ell/(j-\ell)$ and replace that column by $$C_j=F_j+p\sum_{\substack{0\le\ell<J\\\ell\notin\mathcal E}}
                                      a_{\ell j}Y_\ell.$$ This is a shear of the whole column pool with integral coefficients and inverse obtained by changing the signs of the added coefficients. It preserves every retained column and every pair sum. The resulting central columns lie in $p^{-1}\mathbb Z_p^n$ and satisfy $$pC_j\equiv-\sum_{\ell\in\mathcal E}\frac{V_\ell}{j-\ell}
       \pmod p.$$ This step does not require any information about the next coefficient of $Y_\ell$. Explicitly, if $Y_\ell=p^{-2}y_0+p^{-1}y_1+y_2$ with integral lifts $y_0,y_1,y_2$, then $pY_\ell=p^{-1}y_0+y_1+py_2$; its unknown second coefficient is already integral.

Let $c$ be the number of central columns. Their scaled residues define a linear map $$\varphi:\mathbb F_p^c\longrightarrow\mathbb F_p^n,
 \qquad (a_j)_j\longmapsto\sum_j a_j(pC_j\bmod p).$$ Its image is contained in the span of the $e$ exceptional vectors, so $d:=\operatorname{rank}\varphi\le\min(c,e)$. Choose a basis of $\mathbb F_p^c$ whose last $c-d$ vectors form a basis of $\ker\varphi$. Lift its basis matrix arbitrarily to a matrix $W\in\operatorname{Mat}_{c}(\mathbb Z_p)$. Its determinant is a unit, so $W\in\operatorname{GL}_c(\mathbb Z_p)$ and the adjugate formula gives $W^{-1}\in\operatorname{Mat}_{c}(\mathbb Z_p)$. Applying this change to the central columns leaves at most $d$ columns in $p^{-1}\mathbb Z_p^n$; the other $c-d$ are integral, because their scaled residues vanish and they already belonged to $p^{-1}\mathbb Z_p^n$. If $c=0$ this step is the empty identity.

The resulting full pool consequently contains $R$ columns with possible denominator $p^2$, at most $B+d\le B+e=S$ other columns with possible denominator $p$, and integral remaining columns. No noncentral column was discarded, nor was its denominator reduced on the strength of a leading linear dependence. In a full minor, if $r$ columns come from the first group and $s$ from the second, the loss is at most $2r+s$. The inequalities $$2r+s\le2n,\qquad 2r+s\le n+R,\qquad 2r+s\le2R+S$$ hold since $r+s\le n$, $r\le R$, and $s\le S$. All changes used above and their inverses are integral, so the Cauchy–Binet transfer proves Equation (40) for all original full minors and for $\Delta_N$. ◻

The omission of the optional pair at $\ell=A$ is harmless: its physical column is included in $R$. The preceding proof also covers $K\le0$ and $J\le b$. In particular, if $L\le p\le H$, there are no high or low noncentral columns, $R=0$, and $S=H-p$; all raw columns are central. At the formal endpoint $p=H$, all of them are integral.

### Summing the prime losses

For a nonzero rational determinant, the valuations weighted by $\log p$ sum to its ordinary logarithmic absolute value. We now combine the odd-prime estimates with the bound at $2$ to obtain the lower bound used in the final comparison.

**Proposition 3.4** (Finite-place bound). *Assume $G\in\mathbb Q$. Along any sequence of positive integers $N\to\infty$ for which $\Delta_N\ne0$, one has $$\begin{equation}
\tag{42}
 \liminf_{N\to\infty}
 \left(\frac{\log|\Delta_N|}{n^2}-\frac12\log2\right)
 \ge -\frac{8609}{4608}
       -\left(\frac12+\frac{505}{4608}\right)\log2
 >-2.29084.
\end{equation}$$*

*Proof.* We first compute the complete loss function. Put $x=p/N$. For $x\le65/2$, Equation (38) has $$\frac{d_0}{N}
  =\bigl(\min(x,59-x,19)-\max(7,65-2x)\bigr)_+.$$ For $0\le x\le23$ this is zero; for $23\le x\le29$ it is $2x-46$; and for $29\le x\le65/2$ it is $12$. Only the part exceeding $q/N=4$ improves a full minor. For $x>65/2$, the formulas of Lemma 3.3 give the following values; the table retains the intermediate breakpoint $52$ at which the counting formula changes: $$\begin{array}{c|cc}
 x\text{ range}&R/N&S/N\\\hline
 {[65/2,40]}&105-2x&12\\
 {[40,52]}&65-x&52-x\\
 {[52,58]}&117-2x&x-52\\
 {[58,59]}&59-x&6\\
 {[59,65]}&0&65-x
\end{array}.$$ The entries agree at their common endpoints. Taking $\min(96,48+R/N,2R/N+S/N)$ yields the additional breakpoint $69/2$. Thus for every relevant prime $p>2\sqrt H$ the valuation is bounded below by $-Nd(p/N)$, where $d$ is continuous, is zero for $x\ge65$, and has the following exact pieces: $$\begin{equation}
\tag{43}
\begin{array}{c|c|c|c}
 x\text{ range}&d(x)&
       \text{endpoint values}&\displaystyle\int_{\text{range}}d(x)\,dx\\\hline
 {[0,25]}&96&96,96&2400\\
 {[25,29]}&146-2x&96,88&368\\
 {[29,65/2]}&88&88,88&308\\
 {[65/2,69/2]}&153-2x&88,84&172\\
 {[69/2,40]}&222-4x&84,62&803/2\\
 {[40,58]}&182-3x&62,8&630\\
 {[58,59]}&124-2x&8,6&7\\
 {[59,65]}&65-x&6,0&18
\end{array}.
\end{equation}$$ In particular, $$\begin{equation}
\tag{44}
 \int_0^{65}d(x)\,dx=\frac{8609}{2}.
\end{equation}$$

For completeness, the omitted small odd primes cost only $o(n^2)$ in the logarithm of the determinant. At any odd prime, the factorial formula gives $$0\le v_p\binom{2l}{l}\le1+\frac{\log H}{\log p}
 \qquad(2l\le H).$$ Each factorial-floor difference is zero or one. The displayed formulas for $H_z^*,m_i,k_d^\pm,Z^0$, and diagonal reduction then give, with an absolute constant $C_0$ and with $\operatorname{den}G$ denoting the positive reduced denominator of $G$, $$v_p(F_j(r))\ge
   -C_0\left(1+\frac{\log H}{\log p}\right)-v_p(\operatorname{den}G).$$ For instance, each summand in $k^-_u$ uses at most two powers of $z$ and two powers of $H_z^*$ in its denominator; no additional loss arises from summing. All row and filter coefficients are integers. Expanding a determinant therefore multiplies this entry bound by at most $n$, and summing it over $p\le2\sqrt H$ with weights $\log p$ gives $$O\bigl(n\sqrt H\log H+n\log(\operatorname{den}G)\bigr)
       =o(n^2).$$ This estimate uses only that the number of such primes is at most $2\sqrt H$. For sufficiently large $N$, every prime $p>H$ is integral throughout the calculation: factorials and degree denominators introduce only prime factors at most $H$, and the fixed denominator of $G$ has no prime factor above $H$. Thus these primes give no negative contribution.

We use the classical prime number theorem in the form $$\theta(y):=\sum_{p\le y}\log p\sim y
       \qquad(y\to\infty);$$ see [25, Step VI, p. 707], which presents Newman’s analytic proof. The weighted consequence needed here follows directly: $$\begin{equation}
\tag{45}
 \frac1N\sum_{p\le65N}d(p/N)\log p
       \longrightarrow\int_0^{65}d(x)\,dx.
\end{equation}$$ Here is a direct justification of the weight. For a fixed partition $0=x_0<\cdots<x_m=65$, the prime number theorem gives $$\frac{\theta(Nx_j)-\theta(Nx_{j-1})}{N}
       \longrightarrow x_j-x_{j-1}.$$ Upper and lower step functions formed from the supremum and infimum of $d$ on each interval bound the weighted sum. Their limiting difference tends to zero as the mesh decreases, since $d$ is uniformly continuous. Individual partition endpoints change the sum by at most $O(\log N/N)$. This proves Equation (45). The prime $2$ and the primes below $2\sqrt H$ may be removed from that sum at cost $o(1)$, using $\|d\|_\infty=96$ and the elementary bound $\theta(2\sqrt H)\le2\sqrt H\log(2\sqrt H)$.

Combining these estimates with Equation (44) and $n^2=2304N^2$ gives $$\sum_{p\text{ odd}}v_p(\Delta_N)\log p
       \ge-\frac{8609}{4608}n^2-o(n^2).$$ Proposition 2.2, with $\delta=10/48$, gives $$v_2(\Delta_N)\ge
  -\left(\frac\delta2+\frac{\delta^2}{8}\right)n^2-o(n^2)
  =-\frac{505}{4608}n^2-o(n^2).$$ For a nonzero rational number its numerator and denominator factorizations give the exact identity $$\log|\Delta_N|=\sum_pv_p(\Delta_N)\log p.$$ Subtracting $\tfrac12\log2$ after dividing by $n^2$ proves the non-strict inequality in Equation (42).

The final numerical comparison also has a short rational check. The identity $$\log2=2\sum_{j=0}^{\infty}\frac{3^{-(2j+1)}}{2j+1}$$ and its positive geometric tail give $$\log2\le
 2\sum_{j=0}^{5}\frac{3^{-(2j+1)}}{2j+1}
       +\frac{2\,3^{-13}}{13(1-3^{-2})}
 <\frac{693149}{10^6}.$$ Consequently the lower constant is strictly larger than $$-\frac{8609}{4608}-\frac{2809}{4608}\frac{693149}{10^6}
 =-\frac{10556055541}{4608000000}>-2.29084,$$ which completes the proof. ◻

## Nonvanishing along the prime sequence

The next proposition supplies the nonzero determinants needed in Proposition 3.4.

**Proposition 4.1**. *Assume that $G\in\mathbb Q$. For every sufficiently large prime $p$, the determinant with scale parameter $N=p$ satisfies $$\begin{equation}
\tag{46}
 v_p(\Delta_p)=-96p.
\end{equation}$$ In particular, $\Delta_p\ne0$ for every sufficiently large prime $p$.*

We prove the proposition by reducing a matrix of size $48p$ to three fixed rational matrices of size $48$. Throughout this section, an underlined row polynomial is formed with $N=1$, so that $$n_0=48,\quad b_0=7,\quad q_0=g_0=4,\quad h_0=2,\quad
 L_0=59,\quad C_0=63,\quad H_0=65.$$ In addition to the usual rows $0,\ldots,47$, define the auxiliary row $48$ by exactly the formulas in Equation (3). For $0\le r\le48$ and $0\le k<48$, put $$\begin{equation}
\tag{47}
 \mathcal B(r,k)=\sum_{j=0}^{4}(-1)^j\binom4j
 \left\{M^0(\underline P_r,7+k+j)
              -\frac32 Z^0(\underline D_r,7+k+j)\right\}.
\end{equation}$$ Here $M^0$ and $Z^0$ act linearly on the first polynomial argument. Thus $\mathcal B$ is a fixed rational $49$ by $48$ matrix. Define $$\mathcal B_0=(\mathcal B(r,k))_{0\le r,k<48},\qquad
 \mathcal B_1=(\mathcal B(r+1,k))_{0\le r,k<48}.$$ The arithmetic certificate below proves $$\begin{equation}
\tag{48}
 \det\mathcal B_0\ne0,\qquad
 \det(\mathcal B_0+\mathcal B_1)\ne0,\qquad
 \det(\mathcal B_0-\mathcal B_1)\ne0.
\end{equation}$$ First we show why these three fixed assertions imply the proposition.

### Two palindromic bases

Let $p$ be an odd prime and work over $\mathbb F_p$. The vector space $$\mathcal P_p=\{Q\in\mathbb F_p[w]:\deg Q\le2p-2,
                \ w^{2p-2}Q(1/w)=Q(w)\}$$ has dimension $p$: its coefficients of $w^0,\ldots,w^{p-1}$ determine all its coefficients. For $0\le\ell,i<p$, consider $$U_\ell(w)=(2w)^\ell(1+w^2)^{p-1-\ell},\qquad
 Q_i(w)=w^i\sum_{j=0}^{p-i-1}w^{2j}.$$ Both families belong to $\mathcal P_p$. The lowest terms of $U_\ell$ and $Q_i$ are respectively $2^\ell w^\ell$ and $w^i$. Triangularity of their coefficients in degrees $0,\ldots,p-1$ proves that each family is a basis. Define $a_{\ell i}\in\mathbb F_p$ by $$Q_i=\sum_{\ell=0}^{p-1}a_{\ell i}U_\ell,
 \qquad \mathbf a=(a_{\ell i})_{0\le\ell,i<p}.$$ The same lowest-term comparison gives $$\begin{equation}
\tag{49}
 a_{\ell i}=0\quad(\ell<i),\qquad a_{ii}=2^{-i},\qquad
 \det\mathbf a=2^{-p(p-1)/2}\ne0.
\end{equation}$$ In particular, invertibility of this varying-size matrix introduces no exceptional odd primes.

Define $Q'_0=0$ and $Q'_i=Q_{p-i}$ for $1\le i<p$, and write $Q'_i=\sum_\ell b_{\ell i}U_\ell$. Equivalently, $$\begin{equation}
\tag{50}
 \mathbf b=\mathbf a\Pi,\qquad
 \Pi e_0=0,\qquad \Pi e_i=e_{p-i}\quad(1\le i<p),
\end{equation}$$ where $e_i$ are the standard coordinate vectors. The explicit forms are $$Q_i=w^i\frac{1-w^{2(p-i)}}{1-w^2},\qquad
 Q'_i=w^{p-i}\frac{1-w^{2i}}{1-w^2};$$ the latter formula gives zero also when $i=0$. Their sum satisfies $$Q_i+w^pQ'_i
 =w^i\sum_{j=0}^{p-1}w^{2j}
 =w^i(1-w^2)^{p-1},$$ because $\binom{p-1}{j}=(-1)^j$ in $\mathbb F_p$. With $$t=\frac{2w}{1+w^2},\qquad f=\frac{1-w^2}{1+w^2},\qquad
 E(t)=(1-t^2)^{(p-1)/2}=f^{p-1},$$ division by $(1+w^2)^{p-1}$ therefore proves the rational-function identity $$\begin{equation}
\tag{51}
 E(t)w^i=\sum_{\ell=0}^{p-1}t^\ell
              (a_{\ell i}+b_{\ell i}w^p).
\end{equation}$$

### Frobenius and the two extraction shifts

Set $N=p$, and write every row index uniquely as $r=pr_0+i$, with $0\le r_0<48$ and $0\le i<p$. Put $t'=t^p$, $w'=w^p$, and $f'=f^p$. Frobenius gives $$t'=\frac{2w'}{1+(w')^2},\qquad
 f'=\frac{1-(w')^2}{1+(w')^2},\qquad (f')^2=1-(t')^2.$$ Using $C=63p$, $h=2p$, and $g=4p$ in the row definition gives $$\begin{align}
 tR_rE(t)
 &= (1-t')^2(t')^{63}(w')^{r_0-4}E(t)w^i\notag\\
 &=\sum_{\ell=0}^{p-1}t^\ell t'
       \bigl(a_{\ell i}\underline R_{r_0}(t',w')
            +b_{\ell i}\underline R_{r_0+1}(t',w')\bigr).
 \tag{52}
\end{align}$$ Here the single factor $w'$ in the second term creates exactly one successor row; its index is at most $48$.

To separate the polynomial parts, star fixes $t,t'$ and negates $f,f'$. Moreover $fE=f'$, so the row identities give $$tR_rE=tP_rE-f'D_r,
 \qquad t'\underline R_j=t'\underline P_j-f'\underline D_j.$$ Taking the star-invariant part of Equation (52) and then its anti-invariant part, and cancelling the nonzero rational function $f'$ in the latter, yields two separate polynomial identities: $$\begin{align}
 tP_r(t)E(t)
 &=\sum_{\ell=0}^{p-1}t^\ell t'
       \bigl(a_{\ell i}\underline P_{r_0}(t')
              +b_{\ell i}\underline P_{r_0+1}(t')\bigr),
       \tag{53}\\
 D_r(t)
 &=\sum_{\ell=0}^{p-1}t^\ell
       \bigl(a_{\ell i}\underline D_{r_0}(t')
              +b_{\ell i}\underline D_{r_0+1}(t')\bigr).
       \tag{54}
\end{align}$$ These are polynomial identities since the row polynomials on both sides are polynomials, and substitution $t=2w/(1+w^2)$ is injective on $\mathbb F_p[t]$.

In the notation of Equation (36), the extractions for a fixed residue $\ell$ are $$P'_u=[t^{(u+1)p+\ell}]tP_r(t)E(t),\qquad
 D'_u=[t^{up+\ell}]D_r(t).$$ Every polynomial has a unique expression $\sum_{\ell=0}^{p-1}t^\ell A_\ell(t^p)$. Consequently Equations (53) and (54) give $$\begin{equation}
\tag{55}
 (P'_u,D'_u)=[(t')^u]
 \left\{a_{\ell i}(\underline P_{r_0},\underline D_{r_0})(t')
        +b_{\ell i}(\underline P_{r_0+1},\underline D_{r_0+1})(t')\right\}.
\end{equation}$$ Thus the $t'$ in the first identity is exactly consumed by the $u+1$ in the $P$ extraction. The $D$ extraction has no such shift. Negative coefficient indices are zero; in particular $P'_{-1}=0$ here.

There is a degree issue at the last successor row which is useful to make explicit. The auxiliary polynomials have $$\begin{equation}
\tag{56}
 \min\deg\underline P_{48}=62-44=18,\qquad
 \min\deg\underline D_{48}=63-44=19.
\end{equation}$$ These coefficients must be retained, even though the first $48$ base rows have minimum degrees at least $19$ and $20$. For the last block $r=47p+i$, $i>0$, Equation (50) gives $b_{\ell i}=a_{\ell,p-i}=0$ for $\ell<p-i$, and $b_{p-i,i}=2^{-(p-i)}\ne0$. The successor contribution in either $tP_rE$ or $D_r$ therefore starts at $$19p+(p-i)=20p-i.$$ The first-row contribution starts no earlier than $20p+i$. Directly from the original rows, $|r-g|=43p+i$, so $tP_r$ and $D_r$ also start at $C-|r-g|=20p-i$; since $E(0)=1$, this agrees with the extraction. The leading Chebyshev coefficients are powers of $2$, hence are nonzero in odd characteristic. When $i=0$, the successor term is zero and the first term starts at $20p$. The lower degree of the auxiliary row therefore introduces no forbidden coefficient into the growing matrix. Its contact identity is also valid: $t\underline R_{48}/f=O(t^{107})$, since $63+48-4=107>59$.

### The residue blocks and their determinant

For this paragraph take $p>260$ and exclude primes dividing the denominator of the hypothesized rational number $G$. Then $$p>2\sqrt{65p}=2\sqrt H,$$ so Equations (31) and (36) apply at the same prime $p$ used as the scale parameter. To spell out the role of $G$, the rational raw entry is $$F_j(r)=M^0(P_r,j)-\frac32 Z^0(D_r,j)
          +4G\sum_v[t^v]P_r\,c_{(v-j)/2}.$$ The last sum is $p$-integral: its polynomial coefficients are integers, and every $c_d=4^{-d}\binom{2d}{d}$ is integral at an odd prime. The $G$ term therefore reduces to zero after multiplication by $p^2$. All entries of the scaled matrix are $p$-integral by the cited layer formulas. Substitution of Equation (55) into Equation (36) gives the reduced raw entry $$\begin{align}
 p^2F_{kp+\ell}(pr_0+i)
 \equiv{}&a_{\ell i}\left\{M^0(\underline P_{r_0},k)
                         -\frac32 Z^0(\underline D_{r_0},k)\right\}
                         \notag\\
 &+b_{\ell i}\left\{M^0(\underline P_{r_0+1},k)
                         -\frac32 Z^0(\underline D_{r_0+1},k)\right\}
                         \pmod p.
 \tag{57}
\end{align}$$ This applies to every raw column in the specified range. The base entries here have denominators with prime factors at most $65$, as the rational recipes below also show, so their reductions exist for $p>260$.

The integer filter also respects residues. Write the column index uniquely as $k=\ell+pk_0$, where $0\le\ell<p$ and $0\le k_0<48$. In $\mathbb F_p[s]$, $$\begin{equation}
\tag{58}
 s^{7p+k}(1-s)^{4p}
   =s^\ell(s^p)^{7+k_0}(1-s^p)^4.
\end{equation}$$ Multiplying each raw entry by $p^2$ before reduction makes this polynomial congruence applicable to the column operation: coefficient differences divisible by $p$ multiply integral scaled entries. The fourth finite difference on the right uses exactly the five base raw indices $7+k_0,\ldots,11+k_0$, all in $7,\ldots,58$. Each of the $p$ residue groups thus contains exactly $48$ base filtered columns, and no operation changes $\ell$.

Order rows by $(i,r_0)$ and columns by $(\ell,k_0)$. The reduction of the scaled $48p$ by $48p$ matrix has $(i,\ell)$ block $$a_{\ell i}\mathcal B_0+b_{\ell i}\mathcal B_1.$$ Writing this matrix as $\mathcal L_p$ makes its orientation explicit: $$\begin{equation}
\tag{59}
 \begin{split}
 \mathcal L_p&=\mathbf a^T\otimes\mathcal B_0
                       +\mathbf b^T\otimes\mathcal B_1,\\
 \mathcal L_p\bigl((\mathbf a^T)^{-1}\otimes I_{48}\bigr)
      &=I_p\otimes\mathcal B_0+\Pi^T\otimes\mathcal B_1.
 \end{split}
\end{equation}$$ Indeed $\mathbf b^T=\Pi^T\mathbf a^T$, which explains both the transpose and the side of multiplication.

The nonzero indices $1,\ldots,p-1$ fall into $(p-1)/2$ disjoint pairs $\{i,p-i\}$. On each pair the vectors $e_i+e_{p-i}$ and $e_i-e_{p-i}$ are eigenvectors of $\Pi$ with eigenvalues $1$ and $-1$. Together with $e_0$, of eigenvalue zero, they form a basis since $2$ is invertible. Thus the eigenvalue multiplicities of $\Pi^T$ are $1,(p-1)/2,(p-1)/2$ for $0,1,-1$, respectively. A similarity on the $p$-dimensional factor in Equation (59) now proves the exact identity in this block ordering: $$\begin{align}
 \det\mathcal L_p
  ={}&(\det\mathbf a)^{48}\det\mathcal B_0\notag\\
    &\quad\cdot\det(\mathcal B_0+\mathcal B_1)^{(p-1)/2}
          \det(\mathcal B_0-\mathcal B_1)^{(p-1)/2}.
 \tag{60}
\end{align}$$ There is no determinant factor from the similarity. Returning to the original row and column orders changes at most the sign.

### An exact certificate for the fixed matrices

All entries in Equation (47) can be constructed by the following rational arithmetic. This also specifies their reduction modulo $101$ without any numerical approximation. First form $m_0=2$, $m_i=0$ for odd $i$, and $m_i=i m_{i-2}/(i+1)$ for even $2\le i\le64$. Set $$k^-_0=0,\quad k^-_1=2,\qquad k^+_0=k^+_1=0,$$ and use $$\begin{align*}
 k^-_d&=\frac{(d-1)k^-_{d-2}+m_{d-2}+m_{d-1}}{d}
                  &&(2\le d\le64),\\
 k^+_d&=\frac{(d-2)k^+_{d-2}+2/(d-1)}{d-1}
                  &&(2\le d\le58).
\end{align*}$$ On $0\le i\le64$, $0\le j\le58$, form $$Y_{i0}=k^-_i,\qquad Y_{0j}=k^+_j,\qquad
 Y_{ij}=Y_{i-1,j-1}-\frac{m_{i-1}}j\quad(i,j\ge1).$$ Thus $Y_{ij}=M^0(i,j)$. With $B_i^{(d)}=\sum_{u=1}^i u^{-d}$ and $B_0^{(d)}=0$, set $$J_{ij}=\frac32\begin{cases}
       -B_i^{(2)},&i=j,\\[2pt]
       (B_i^{(1)}-B_j^{(1)})/(i-j),&i\ne j.
      \end{cases}$$ This gives $J_{ij}=\tfrac32Z^0(i,j)$, with the sign on its diagonal included.

For the polynomial construction define $$E_0=t^{62},\quad E_1=t^{61},\qquad I_0=0,\quad I_1=t^{62},$$ and, for either family $S=E,I$, use $$S_m=2S_{m-1}/t-S_{m-2}\qquad(2\le m\le44).$$ These are ordinary integer polynomials: they are $E_m=t^{62}T_m(1/t)$ and $I_m=t^{62}U_{m-1}(1/t)$. For $0\le r\le48$ let $u=|r-4|$ and form the coefficient vectors, in degrees $0,\ldots,64$, of $$y_r(t)=(1-t)^2E_u(t),\qquad
 z_r(t)=\operatorname{sign}(r-4)(1-t)^2I_u(t).$$ They are exactly $\underline P_r$ and $\underline D_r$. Contract them with the arrays to obtain the length-$52$ vector $$v_r(j)=\sum_{i=0}^{64}\bigl([t^i]y_r\,Y_{ij}
                                  -[t^i]z_r\,J_{ij}\bigr),
               \qquad j=7,\ldots,58.$$ Replace a vector $v$ four times successively by its vector of consecutive differences $(v(j)-v(j+1))_j$. The resulting length-$48$ vector is row $r$ of $\mathcal B$. In particular, the construction includes all coefficients of the auxiliary row, including its degree-$18$ term.

Every scalar denominator in these recipes is a product of nonzero integers of absolute value at most $65$. Every rational array entry therefore has denominator prime factors at most $65$, so each denominator is a unit modulo $101$. Polynomial division by $t$ above shifts exponents of polynomials divisible by $t$ and introduces no scalar denominator. Consequently the entire construction can be performed over $\mathbb F_{101}$ and agrees with reduction of the rational matrices.

For completeness, the elimination rule producing the certificate is as follows. For $\sigma\in\{0,1,-1\}$, start with row vectors $R_i=\mathcal B(i,{\cdot})+\sigma\mathcal B(i+1,{\cdot})$, $0\le i<48$, in increasing order. At step $i$, if $R_i(i)=0$, swap row $i$ with the first later row having a nonzero entry in column $i$. Record $d_i=R_i(i)$ and replace every row $j>i$ by $$R_j-\frac{R_j(i)}{d_i}R_i.$$ There are no swaps for $\sigma=0,-1$. For $\sigma=1$ the only swaps, using indices starting at zero, are $(30,31)$ and $(45,46)$ at their respective steps. The pivots are given in Table 1; its three lines for each $\sigma$ list the pivots consecutively, with $16$ entries per line.

**Table 1:** Exact Gaussian pivots for $\mathcal B_0+\sigma\mathcal B_1$ modulo $101$.

| $\sigma$ | Successive pivots in $\mathbb F_{101}$            |
|:--------:|:--------------------------------------------------|
|   $0$    | $60,68,62,79,47,32,69,57,30,72,35,66,43,20,85,48$ |
|          | $88,4,77,54,60,79,26,68,83,39,40,65,1,68,78,24$   |
|          | $15,98,32,22,94,9,99,10,15,75,4,2,25,53,90,79$    |
|   $1$    | $38,51,90,70,5,21,88,55,45,20,35,41,77,10,18,25$  |
|          | $76,14,38,72,6,66,56,35,83,58,56,11,17,20,30,24$  |
|          | $28,11,25,70,79,99,66,38,4,41,63,91,63,17,90,98$  |
|   $-1$   | $82,92,26,87,21,74,87,88,88,3,14,23,38,58,36,20$  |
|          | $26,33,94,74,78,45,93,86,73,66,45,30,61,3,88,27$  |
|          | $20,58,69,48,78,39,48,1,66,18,86,93,52,92,39,77$  |

Every listed pivot is nonzero. Since the swaps and row additions are invertible, all three matrices are invertible modulo $101$ and hence have nonzero determinants over $\mathbb Q$. This proves Equation (48). The modulus $101$ is used only for this fixed finite certificate; the growing determinant uses arbitrary sufficiently large primes as follows.

*Completion of the proof of Proposition 4.1.* Let $\mathcal E$ consist of $2$, the primes dividing the denominator of $G$, the primes dividing any denominator of an entry of $\mathcal B$, and the primes dividing the numerator or denominator, in lowest terms, of any of the three nonzero rational determinants in Equation (48). This is a fixed finite set. For $p>260$ outside $\mathcal E$, all three fixed matrices reduce to invertible matrices over $\mathbb F_p$. Equation  (49) and the factorization in Equation (60) then show that $\det\mathcal L_p\ne0$.

Let $\mathcal F_p$ be the original filtered matrix whose determinant is $\Delta_p$. Its size is $n=48p$, and $p^2\mathcal F_p$ is integral over the local ring $\mathbb Z_{(p)}$. Its reduction, after the stated row and column permutations, is $\mathcal L_p$. Therefore $$p^{2n}\Delta_p=\det(p^2\mathcal F_p)$$ is a unit in $\mathbb Z_{(p)}$. This proves $v_p(\Delta_p)=-2n=-96p$. Every sufficiently large prime is outside $\mathcal E$ and exceeds $260$, as required. ◻

## The real-place determinant estimates

We estimate the determinant defined in Equation (7) without a rationality assumption. Write $$\begin{equation}
\tag{61}
 \begin{gathered}
 \alpha=\frac an=\frac{11}{48},\quad
 \beta=\frac bn=\frac7{48},\quad
 \gamma=\frac gn=\frac qn=\frac4{48},\quad
 \eta=\frac hn=\frac2{48},\\
 D_*=n-1-2g=40N-1.
 \end{gathered}
\end{equation}$$ In particular, $0<D_*<n$ and $n\ge48$. For a real list $y$ of length $n$, let $$V(y)=\prod_{i<j}(y_j-y_i),\qquad \mathcal V(y)=|V(y)|.$$ All constants in the estimates of this Section are independent of the locations and separations of the integration variables.

### The integral and its two sheets

Put $d\mu(t)=|t|\,dt/f(t)$ on $(-1,1)$, and set $$A_r(t)=P_r(t)-\frac32\boldsymbol 1_{\{t>0\}}\frac{f(t)}tD_r(t),
 \qquad \psi_k(s)=s^{b+k}(1-s)^q.$$ The value at $t=0$ is immaterial; the displayed expression has a finite limit there because $D_r(t)/t$ is a polynomial. The determinant entries are exactly $$\int_{-1}^1\int_0^1 A_r(t)\frac{\psi_k(s)}{1-ts}\,ds\,d\mu(t).$$ The measure has mass $\mu((-1,1))=2$. The scalar majorant $\int\!\int(1-|t|s)^{-1}\,ds\,d\mu(t)$ is finite: integration in $s$ gives at worst a logarithmic singularity at $|t|=1$, which is integrable against $(1-t^2)^{-1/2}dt$. The functions $A_r$ and $\psi_k$ are bounded for each fixed $n$. Thus all permutation expansions below are absolutely integrable.

We apply Andréief’s determinant integration identity twice [10, Equation (1.7) and Section 2.2]. Expanding determinants and relabeling integration variables gives the identity $$\begin{equation}
\tag{62}
 \Delta_N=\frac1{(n!)^2}\int_{(-1,1)^n}\int_{(0,1)^n}
 \det[A_r(t_i)]_{r,i}\,
 \det\left[\frac1{1-t_i s_j}\right]_{i,j}\,
 \det[\psi_k(s_j)]_{j,k}\,ds\,d\mu^n(t).
\end{equation}$$ Here $0\le r,k<n$ and $1\le i,j\le n$. To see the factor $1/n!$ at each application directly, expand the two determinants sharing an integration list: every one of the $n!$ permutations of that list gives the same determinant of single integrals. Fubini’s theorem applies by the preceding majorant, also after each permutation expansion.

Cauchy’s double alternant in multiplicative variables [12, Section 2.1, Equation (2.7)] is $$\begin{equation}
\tag{63}
 \det\left[\frac1{1-t_i s_j}\right]_{i,j}
 =\frac{V(t)V(s)}{\prod_{i,j}(1-t_i s_j)}.
\end{equation}$$ For completeness, multiplying by the denominator gives a polynomial alternating separately in $t$ and $s$, of degree at most $n-1$ in each individual variable. Dividing by $V(t)V(s)$ therefore leaves a constant. Expanding $(1-t_i s_j)^{-1}$ at $s=0$, the first nonzero homogeneous part of the determinant is $V(t)V(s)$, so that constant is one. Also $\det[\psi_k(s_j)]_{j,k}=V(s)\prod_j s_j^b(1-s_j)^q$.

Use the real coordinate $$\begin{equation}
\tag{64}
 x_i=\frac{t_i}{1+\sqrt{1-t_i^2}},\qquad
 t_i=\frac{2x_i}{1+x_i^2},\qquad
 d\mu(t_i)=\frac{4|x_i|}{(1+x_i^2)^2}\,dx_i.
\end{equation}$$ The coordinate maps $(-1,1)$ bijectively to $(-1,1)$. Except on a set of measure zero we may assume that all $x_i$ are distinct and nonzero. Define $$(\xi_{\mathrm f}(x),\xi_{\mathrm n}(x))=
 \begin{cases}(1/2,1/2),&x<0,\\(-1/4,5/4),&x>0,\end{cases}
 \qquad
 \mathcal R_n(x)=
 \det\left[\xi_{\mathrm f}(x_i)x_i^{g-r}
             +\xi_{\mathrm n}(x_i)x_i^{r-g}\right]_{r,i}.$$ The subscripts $\mathrm n$ and $\mathrm f$ refer to the near and far evaluations at $x_i$ and $1/x_i$, respectively, inside and outside the unit circle. Indeed, $fD_r/t=(R_r^*-R_r)/2$, so the negative half-interval has the row $(R_r+R_r^*)/2$, whereas the positive half-interval has $(5R_r-R_r^*)/4$. Factoring $(1-t_i)^ht_i^{C-1}$ out of the $i$th column therefore gives the exact identity $$\begin{equation}
\tag{65}
 \Delta_N=\frac1{(n!)^2}\int\!\int
 \mathcal R_n(x)\,
 \frac{V(t)V(s)^2}{\prod_{i,j}(1-t_i s_j)}
 \prod_j s_j^b(1-s_j)^q
 \prod_i t_i^{C-1}(1-t_i)^h\,ds\,d\mu^n(t).
\end{equation}$$ In particular, there is one $t$ Vandermonde and two $s$ Vandermondes. All the denominators in this formula are positive.

### A uniform interpolating function

The interpolation problem comes from factoring out the far-sheet weight. Put $c_i=\xi_{\mathrm n}(x_i)/\xi_{\mathrm f}(x_i)$; the denominator is nonzero on both half-intervals. For $0\le r<n$, $$\begin{equation}
\tag{66}
 \xi_{\mathrm f}(x_i)x_i^{g-r}
   +\xi_{\mathrm n}(x_i)x_i^{r-g}
 =\xi_{\mathrm f}(x_i)x_i^{g-(n-1)}
   \left(x_i^{n-1-r}+c_i x_i^{D_*}x_i^r\right).
\end{equation}$$ Thus a holomorphic function with values $h_*(x_i)=c_i x_i^{D_*}$ turns the expression in parentheses into $x_i^{n-1-r}+h_*(x_i)x_i^r$. We shall bound the resulting evaluation determinant by controlling the norm of this function. The first estimate applies when $$\begin{equation}
\tag{67}
 \sum_{i=1}^n\frac{1-x_i^2}{1+x_i^2}\le D_*.
\end{equation}$$ The following construction is uniform even when the nodes cluster.

**Lemma 5.1**. *Let $x_1,\ldots,x_n$ be distinct nonzero real numbers in $(-1,1)$ satisfying Equation (67). There is a function $h_*$ holomorphic on a neighborhood of the closed unit disk such that $$h_*(x_i)=c_i x_i^{D_*},\qquad
 c_i=\begin{cases}1,&x_i<0,\\-5,&x_i>0,\end{cases}
 \qquad
 \sup_{|z|\le1}|h_*(z)|\le K_0 n,
 \quad K_0=10e^{12}.$$ The neighborhood may depend on the node list; the displayed bound does not.*

*Proof.* Set $$B(z)=\prod_i\frac{z-x_i}{1-x_i z},\qquad
 F(z)=\frac{z^{D_*}}{B(z)}.$$ For $0<u\le1$ and a real $x$ with $0<|x|<1$, the logarithmic derivative of one factor on the imaginary diameter is $$\frac{d}{d\log u}\frac12\log\frac{u^2+x^2}{1+x^2u^2}
 =\frac{(1-x^4)u^2}{(u^2+x^2)(1+x^2u^2)}
 \le\frac{1-x^2}{1+x^2}.$$ The inequality follows on dividing the denominator by $u^2$ and using $u^2+u^{-2}\ge2$. Integration from $u$ to $1$ gives $$|B(iu)|\ge u^{\sum_i(1-x_i^2)/(1+x_i^2)}\ge u^{D_*}.$$ The same holds at $-iu$, and $F(0)=0$. For $1\le u\le1+2/n$, each factor has modulus at least one because $(u^2+x^2)-(1+x^2u^2)=(u^2-1)(1-x^2)\ge0$. Consequently $$\begin{equation}
\tag{68}
 |F(iu)|\le e^2\qquad (|u|\le1+2/n).
\end{equation}$$

Orient the fixed segment $\Gamma=[-i(1+2/n),i(1+2/n)]$ upwards, and, off that segment, define the fixed Cauchy integral $$\mathcal C(z)=\frac1{2\pi i}\int_\Gamma\frac{6F(w)}{w-z}\,dw.$$ Write $c_-=1$, $c_+=-5$, with the sign specifying the left or right half-plane, and put $$\begin{equation}
\tag{69}
 h_*(z)=c_\pm z^{D_*}-B(z)\mathcal C(z)
 \quad\text{when }\ \pm\operatorname{Re}z>0.
\end{equation}$$ The density is holomorphic in a neighborhood of every point of $\Gamma$, since its poles $x_i$ are nonzero and real. Local contour deformation and the Cauchy integral formula show that the left lateral value of $\mathcal C$ minus its right lateral value is $6F$. More explicitly, move a short upward piece of $\Gamma$ to its left; the closed contour formed by the original piece followed by the reversed new piece is positively oriented, and its residue at $w=z$ is $6F(z)$. Thus the difference of the two local analytic continuations in Equation (69) is $(c_--c_+)z^{D_*}-6B(z)F(z)=0$. This proves holomorphic gluing across the segment, including its two crossings of the unit circle.

For each fixed node list the poles $1/x_i$ of $B$ and the endpoints of $\Gamma$ lie strictly outside the closed unit disk. A sufficiently small exterior neighborhood avoids all these points, and the same local gluing works there. It follows that $h_*$ is holomorphic on that neighborhood. Since $B(x_i)=0$ and $\mathcal C$ is regular at the nonzero real point $x_i$, the required interpolation follows.

It remains to bound this one fixed function. In either radius-$1/4$ disk about $i$ or $-i$, the quantities $|w|$, $|w-x_i|$, and $|1-x_iw|$ are at least $3/4$. Hence $F$ is nonzero there and $$\begin{equation}
\tag{70}
 \left|\frac{F'(w)}{F(w)}\right|
 \le\frac43D_*+\frac83n<4n.
\end{equation}$$ As $|F(i)|=|F(-i)|=1$, integration along a segment in either disk gives $|F(w)|\le e^{12}$ whenever $|w-i|\le3/n$ or $|w+i|\le3/n$.

If $|z|=1$ and $|\operatorname{Re}z|\ge1/(10n)$, the original segment has distance at least $1/(10n)$ from $z$; its length is at most $3$. Equation (68) gives $|\mathcal C(z)|\le30e^2n$. If instead $0<|\operatorname{Re}z|<1/(10n)$, $z$ is near one of $\pm i$. Near $i$, replace the portion of $\Gamma$ from $i(1-1/n)$ to $i(1+2/n)$ by the three sides of the rectangle whose other vertical side has real part $-\operatorname{sign}(\operatorname{Re}z)/n$. Near $-i$, make the identical replacement of the bottom portion with imaginary parts from $-1-2/n$ to $-1+1/n$. The swept rectangle is in the opposite half-plane from $z$, and it is contained in the radius-$1/4$ disk about the relevant endpoint. It contains neither $z$ nor a pole of $F$, so this deformation leaves the value of the fixed integral $\mathcal C(z)$ unchanged.

Each new side is within $3/n$ of $i$ or $-i$. The new contour has length at most $3$ and distance at least $1/(2n)$ from $z$. For the latter assertion the vertical side has horizontal separation at least $1/n$, the outer horizontal side has vertical separation at least $2/n$, and the inner horizontal side and remaining diameter have separation at least $$\frac1n-\bigl(1-\sqrt{1-(10n)^{-2}}\bigr)>\frac1{2n}.$$ Thus $|\mathcal C(z)|\le6e^{12}n$ in this case. Only the two endpoint neighborhoods were deformed; the middle diameter uses its absolute bound (68), with no derivative estimate near zero. Finally $|B(z)|=1$ on $|z|=1$, so Equation (69) gives $|h_*(z)|\le K_0n$ there. At $z=\pm i$ use continuity of the glued function. The maximum modulus principle proves the bound in the disk. No uniform lower bound for the exterior neighborhood was used. ◻

### Evaluation in a finite-dimensional Hilbert space

The following argument uses the kernel and compression viewpoint of bounded analytic interpolation; see [21]. We prove the needed finite-dimensional facts directly.

**Proposition 5.2** (Interpolation estimate). *Under Equation (67), $$\begin{equation}
\tag{71}
 |\mathcal R_n(x)|\le(1+K_0n)^n
       \mathcal V(1/x)\prod_i|x_i|^g.
\end{equation}$$ In particular, the prefactor is $\exp(O(n\log n))$ uniformly in the nodes.*

*Proof.* Let $Q(z)=\prod_i(1-x_i z)$, and give $$\mathcal H_Q=\{v/Q:\ v\in\mathbb C[z],\ \deg v<n\}$$ the norm inherited from the Hilbert space $H^2$ of analytic functions with square-summable Taylor coefficients: $$\|v/Q\|^2=\frac1{2\pi}\int_0^{2\pi}
          \frac{|v(e^{i\theta})|^2}{|Q(e^{i\theta})|^2}\,d\theta.$$ For each fixed list the zeros of $Q$ lie outside the closed disk, so this is a well-defined norm. Define $\widetilde v(z)=z^{n-1}v(1/z)$ and $R(v/Q)=\widetilde v/Q$. This is a complex-linear involution and an isometry: on the circle $|\widetilde v(e^{i\theta})|=|v(e^{-i\theta})|$, while the real coefficients of $Q$ imply $|Q(e^{i\theta})|=|Q(e^{-i\theta})|$.

The functions $k_i(z)=(1-x_i z)^{-1}$ belong to $\mathcal H_Q$. They are linearly independent, as their distinct poles $1/x_i$ show, and hence form a basis. For $u\in H^2$, the Taylor coefficient inner product gives $\langle u,k_i\rangle=u(x_i)$. If $\Pi_Q$ is orthogonal projection from $H^2$ to $\mathcal H_Q$, it follows that $$(\Pi_Q u)(x_i)=u(x_i)\quad(1\le i\le n).$$ Multiplication by the function $h_*$ of Lemma 5.1 has $H^2$ operator norm at most $\|h_*\|_\infty$. Consequently $$J=\Pi_Q M_{h_*}|_{\mathcal H_Q},\qquad L=I+JR
 \quad\text{satisfy}\quad \|L\|\le1+K_0n.$$

Let $E:\mathcal H_Q\to\mathbb C^n$ send $v/Q$ to $(v(x_i))_i$. It is invertible because a polynomial of degree less than $n$ cannot vanish at all the distinct nodes. For $u\in\mathcal H_Q$, $E(u)_i=Q(x_i)u(x_i)$. Since $LR=R+J$ and projection preserves function values, applying this identity to $LR(v/Q)$ cancels the factors $Q(x_i)$ algebraically and gives $$\begin{equation}
\tag{72}
 E L R(v/Q)=\bigl(\widetilde v(x_i)+h_*(x_i)v(x_i)\bigr)_i.
\end{equation}$$ In the basis $1/Q,z/Q,\ldots,z^{n-1}/Q$, $\det E=V(x)$, and $R$ has determinant of absolute value one. Hence the determinant of the mixed evaluations divided by $V(x)$ has absolute value $|\det L|\le\|L\|^n\le(1+K_0n)^n$. This is an algebraic cancellation of the evaluation determinant. In particular no bound for the inverse evaluation matrix, which might be poorly conditioned, enters the argument.

Apply this bound to the mixed evaluations in Equation (66). Since $|\xi_{\mathrm f}(x_i)|\le1/2\le1$ and $\mathcal V(1/x)=\mathcal V(x)\prod_i|x_i|^{-(n-1)}$, Equation (71) follows. ◻

**Proposition 5.3** (Hadamard estimate). *For every distinct nonzero real list in $(-1,1)$, and in particular when Equation (67) fails, $$\begin{equation}
\tag{73}
 |\mathcal R_n(x)|\le
 (3/2)^n n^{n/2}2^{-\binom n2}
 \prod_i(1+x_i^2)^{(n-1)/2}|x_i|^{g-(n-1)}.
\end{equation}$$ The factor $(3/2)^n n^{n/2}$ is $\exp(O(n\log n))$; the power $2^{-\binom n2}$ is retained in the principal integrand below.*

*Proof.* Expand the determinant by choosing one sheet in each column. For $z_i\in\{x_i,1/x_i\}$ the absolute monomial determinant is $\mathcal V(z)\prod_i|z_i|^{-g}$. Write $z_i=\tan\phi_i$ with $-\pi/2<\phi_i<\pi/2$. Then $$\mathcal V(z)=\prod_i(1+z_i^2)^{(n-1)/2}
              \prod_{i<j}|\sin(\phi_j-\phi_i)|.$$ The last product is $2^{-\binom n2}$ times the Vandermonde on the unit-circle points $e^{2i\phi_i}$. Its monomial matrix has column norms $\sqrt n$, so Hadamard’s inequality gives the bound $2^{-\binom n2}n^{n/2}$. The ratio of the remaining weight on the far sheet to that on the near sheet is $$\frac{|1/x|^{-g}(1+x^{-2})^{(n-1)/2}}
      {|x|^{-g}(1+x^2)^{(n-1)/2}}
 =|x|^{-D_*}\ge1.$$ Thus all the weights can be bounded by their far-sheet values. Finally the sum of absolute sheet coefficients is at most $\prod_i(|\xi_{\mathrm f}(x_i)|+|\xi_{\mathrm n}(x_i)|) \le(3/2)^n$, proving the result. ◻

### The two principal integrands

To state precisely the quantities needed for the real-place energy estimate, put $t_i=2x_i/(1+x_i^2)$ and $$\mathcal J_n(x,s)=
 \frac{\mathcal V(t)\mathcal V(s)^2}{\prod_{i,j}(1-t_i s_j)}
 \prod_j s_j^b(1-s_j)^q
 \prod_i |t_i|^{C-1}(1-t_i)^h.$$ Define $$\begin{equation}
\tag{74}
 \begin{split}
 \mathcal I_{2,n}(x,s)
   &=\mathcal J_n(x,s)\mathcal V(1/x)\prod_i|x_i|^g,\\
 \mathcal I_{1,n}(x,s)
   &=\mathcal J_n(x,s)2^{-\binom n2}
       \prod_i(1+x_i^2)^{(n-1)/2}|x_i|^{g-(n-1)}.
 \end{split}
\end{equation}$$ Let $\Omega_{2,n}$ be the set of interior configurations with distinct nonzero $x_i$ satisfying Equation (67), and let $\Omega_{1,n}$ be its complementary case among such configurations. We use the interpolation estimate on $\Omega_{2,n}$ and the Hadamard estimate on $\Omega_{1,n}$; the latter estimate is valid in both cases. After substituting $t=2x/(1+x^2)$, $\kappa$ is the exponent of the absolute $x$-Vandermonde in the corresponding majorant: $\kappa=2$ for the interpolation estimate and $\kappa=1$ for the Hadamard estimate. The $s_j$ always range over $(0,1)$.

The preceding propositions and Equation (65) give $$|\Delta_N|\le\frac{2^n K_n}{(n!)^2}
 \max_{\kappa\in\{1,2\}}\sup_{(x,s)\in\Omega_{\kappa,n}}
      \mathcal I_{\kappa,n}(x,s),
 \quad
 K_n=\max\{(1+K_0n)^n,(3/2)^n n^{n/2}\}.$$ Indeed $d\mu^n(t)\,ds$ has total mass $2^n$, and the two case sets partition its domain up to a null set. In logarithmic form, with $\log0=-\infty$, this yields $$\begin{equation}
\tag{75}
 \frac{\log|\Delta_N|}{n^2}-\frac12\log2
 \le\max_{\kappa\in\{1,2\}}
 \sup_{(x,s)\in\Omega_{\kappa,n}}
 \left(\frac{\log\mathcal I_{\kappa,n}(x,s)}{n^2}
                -\frac12\log2\right)
 +O\left(\frac{\log(n+2)}n\right).
\end{equation}$$ The error is independent of both integration lists. Factorials, measure masses, and sheet sums have all been accounted for explicitly.

Repeated nonzero $x_i$ give a zero original row determinant and are also handled by continuity in the first estimate; repeated $s_j$ give a zero $s$ Vandermonde. The sets with a zero node or a boundary node have measure zero for the absolutely continuous measures above. At such points the original expression in Equation (62), rather than its factored Laurent expression, supplies the integrable definition. Approaches to these exceptional sets require no separation condition in any bound proved here. In particular all configurations arbitrarily close to them remain included in the suprema in Equation (75).

## A uniform energy bound

The purpose of this Section is to replace the two many-variable majorants by one-variable suprema and explicit quadratic terms. The bound must be uniform before taking those suprema. Matched damping and retained endpoint corrections provide this uniformity.

We retain the constants $\alpha,\beta,\gamma,\eta$, the two cases $\kappa=2,1$, and the nonnegative majorants $\mathcal I_{\kappa,n}$ of Equation (74). Put $$\begin{align}
 W_\kappa(x)&=(\alpha+2\gamma)\log|x|+2\eta\log(1-x)
 -(\kappa/2+\alpha+\eta+\gamma)\log(1+x^2),\notag\\
 W_s(s)&=\beta\log s+\gamma\log(1-s),\notag\\
 D(x)&=2\gamma-\frac{2x^2}{1+x^2}.
 \tag{76}
\end{align}$$ Here $D(x)$ is a scalar function, distinct from the row polynomials $D_r(t)$. For a real sequence $u=(u_k)_{k\ge1}$ with $|u_k|\le K r^k$ for some $K<\infty$ and $0<r<1$, define $$\begin{equation}
\tag{77}
 \|u\|_*^2=\sum_{k\ge1}\frac{u_k^2}{k},\qquad
 T(u,x)=\sum_{k\ge1}\frac{u_kT_k(x)}{k},\qquad
 S(u,x)=\sum_{k\ge1}\frac{u_kx^k}{k}.
\end{equation}$$ These series converge uniformly for $-1\le x\le1$.

The sequences $p,v$ below are freely chosen trial coefficients. The inequality $-a^2\le b^2-2ab$ lets them replace two negative quadratic sums in the logarithmic interactions by affine upper bounds, leaving the two one-variable suprema. Each admissible choice gives a valid bound; the certificate will supply one successful choice for each case.

**Proposition 6.1**. *Let $p,v$ be two such sequences, and take $\lambda=0$ in case $\kappa=2$ or any fixed $\lambda\ge0$ in case $\kappa=1$. Uniformly over configurations in the indicated case, $$\begin{align}
 &\limsup_{N\to\infty}\ \sup_{\text{case }\kappa}
 \left(\frac{\log\mathcal I_{\kappa,n}}{n^2}
                  -\frac12\log2\right)\notag\\
 &\qquad\le (-1+\alpha+\gamma)\log2
       +\kappa\|p\|_*^2+\frac12\|v\|_*^2\notag\\
 &\qquad\quad+\sup_{\substack{-1\le x<1\\x\ne0}}
       \{W_\kappa(x)+\lambda D(x)-2\kappa T(p,x)-S(v,x)\}\notag\\
 &\qquad\quad+\sup_{0<s<1}\{W_s(s)+2T(v,s)\}.
 \tag{78}
\end{align}$$ Consequently the maximum of the right sides for the two cases bounds $$\limsup_{N\to\infty}\left(n^{-2}\log|\Delta_N|-\tfrac12\log2\right).$$ We use $\log0=-\infty$.*

*Proof.* For a one-variable function $F$, write $\langle F(x)\rangle=n^{-1}\sum_iF(x_i)$, and similarly for $s$. In a double average $\langle K(x,x')\rangle_{\ne}$ we sum over ordered pairs $i\ne j$ and divide by $n^2$; a double average without the subscript includes every pair. The substitution $t=2x/(1+x^2)$ gives $$\begin{equation}
\tag{79}
 |t-t'|=\frac{2|x-x'|(1-xx')}{(1+x^2)(1+x'^2)},\qquad
 1-ts=\frac{1-2xs+x^2}{1+x^2},\qquad
 1-t=\frac{(1-x)^2}{1+x^2}.
\end{equation}$$ In particular, the exponent of $|x_i|$ in either majorant is exactly $$(C-1)+g-(n-1)=C+g-n=a+2g;$$ there is no singular finite-size correction at $x=0$. Keeping the other powers as well gives the following exact identity: $$\begin{align}
 \frac{\log\mathcal I_{\kappa,n}}{n^2}-\frac12\log2
 &=c_{\kappa,n}\log2
   +\left\langle W_\kappa(x)+\frac{\kappa+2}{2n}\log(1+x^2)\right\rangle
   +\langle W_s(s)\rangle\notag\\
 &\quad+\frac\kappa2\langle\log|x-x'|\rangle_{\ne}
       +\frac12\langle\log(1-xx')\rangle_{\ne}
       +\langle\log|s-s'|\rangle_{\ne}\notag\\
 &\quad-\langle\log(1-2xs+x^2)\rangle,
 \tag{80}\\
 c_{\kappa,n}&=\frac Cn+\frac{\kappa-2}{2}
                       -\frac{\kappa+1}{2n}.\notag
\end{align}$$ The displayed correction involving $\log(1+x^2)$ is bounded by $2\log2/n$ on the whole domain.

We use the classical Chebyshev expansion of the logarithmic kernel, in the form of Haagerup’s identity presented in [11, Lemma 3.1 and its proof]. We first record its damped form on $[-1,1]$. If $u=\cos\theta$, $u'=\cos\theta'$, and $0\le r<1$, set $$\begin{align}
 L_r(u,u')
 &=-\log2+\log|1-re^{i(\theta+\theta')}|
                 +\log|1-re^{i(\theta-\theta')}|\notag\\
 &=-\log2-2\sum_{k\ge1}\frac{r^kT_k(u)T_k(u')}{k}.
 \tag{81}
\end{align}$$ This follows from the power series for $\log(1-z)$ and the addition formula for cosines. Letting $r\uparrow1$ at distinct $u,u'$ gives $L_1(u,u')=\log|u-u'|$, since the product of the two chord lengths is $2|u-u'|$. The other two identities, for $|z|,|z'|<1$, are $$\begin{equation}
\tag{82}
 \log(1-zz')=-\sum_{k\ge1}\frac{z^kz'^k}{k},\qquad
 -\log(1-2zs+z^2)=2\sum_{k\ge1}\frac{z^kT_k(s)}{k}.
\end{equation}$$ For the last identity the logarithm is the logarithm of a positive real number, equal to $\log|1-ze^{i\arccos s}|^2$. The singular kernels cannot be summed at empirical diagonals. We regularize all appearances of the same moment by the same factor so that the pure and cross interactions still complete a square. Near $(x,s)=(1,1)$, the identity $|1-xe^{i\arccos s}|^2=(1-x)^2+2x(1-s)$ identifies the scales $1-x$ and $\sqrt{1-s}$ used in the following damping factors.

Fix $0<\varepsilon<1/8$ and define $$\begin{equation}
\tag{83}
 \tau=1-\varepsilon,\qquad
 \rho(x)=1-\varepsilon(1-x),\qquad
 \sigma(s)=1-\varepsilon\sqrt{1-s}.
\end{equation}$$ Replace the $x$ cosine kernel in Equation (80) by $L_{\tau^2}(x,x')$ and the $s$ cosine kernel by $L_{\sigma(s)\sigma(s')}(s,s')$. Replace the power kernel by $$\log(1-\rho(x)\rho(x')xx'),$$ and the cross kernel by $$-\log|1-\rho(x)\sigma(s)xe^{i\arccos s}|^2.$$ Every original kernel is bounded above by its replacement plus $O(\varepsilon)$, with an absolute constant independent of the configuration. We give the global estimates, including the signs in the power kernel.

For $|\zeta|=1$ and $0<r\le1$, $$|1-r\zeta|^2-r|1-\zeta|^2=(1-r)^2\ge0.$$ Thus each of the cosine kernels costs at most $-\log r$ in the comparison, and here $r\ge(1-\varepsilon)^2$. For the power kernel put $u=xx'$ and $r=\rho(x)\rho(x')$. If $u\ge0$, monotonicity gives $\log(1-u)\le\log(1-ru)$. If $u<0$, write $q=-u\le1$; then $$\begin{equation}
\tag{84}
 \log(1+q)-\log(1+rq)
 \le\frac{(1-r)q}{1+rq}\le1-r\le4\varepsilon.
\end{equation}$$ For the cross kernel write $a=1-x$, $b=\sqrt{1-s}$, $\theta=\arccos s$, $z=1-xe^{i\theta}$, and $z_\varepsilon=1-\rho(x)\sigma(s)xe^{i\theta}$. Then $|z_\varepsilon-z|\le\varepsilon|x|(a+b)$. On $x\le0$ we have $|z|\ge1$ and $|x|(a+b)\le3$. On $0\le x\le1/2$ we have $|z|\ge1/2$ and $|x|(a+b)\le1$. On $1/2\le x<1$ we have $$|z|^2=a^2+2xb^2\ge a^2+b^2,
 \qquad |x|(a+b)\le\sqrt2\,|z|.$$ Consequently $|z_\varepsilon-z|\le3\varepsilon|z|$ on all three domains, and in the direction required for an upper bound, $$\begin{equation}
\tag{85}
 -\log|z|^2\le-\log|z_\varepsilon|^2
                +2\log(1+3\varepsilon)
 \le-\log|z_\varepsilon|^2+6\varepsilon.
\end{equation}$$

For each fixed finite interior configuration all the damped series are absolutely convergent. Put $$A_k=\langle\tau^kT_k(x)\rangle,\qquad
 B_k=\langle\rho(x)^kx^k\rangle,\qquad
 C_k=\langle\sigma(s)^kT_k(s)\rangle.$$ Inserting the diagonals gives the two exact negative-square identities $$\begin{align}
 \frac\kappa2\langle L_{\tau^2}(x,x')\rangle
 &=-\frac\kappa2\log2-\kappa\sum_{k\ge1}\frac{A_k^2}{k},
 \tag{86}
\end{align}$$ $$\begin{align}
 &\frac12\langle\log(1-\rho(x)\rho(x')xx')\rangle
 +\langle L_{\sigma(s)\sigma(s')}(s,s')\rangle\notag\\
 &\qquad-\langle\log|1-\rho(x)\sigma(s)xe^{i\arccos s}|^2\rangle\notag\\
 &\quad=-\log2-\frac12\sum_{k\ge1}\frac{(B_k-2C_k)^2}{k}.
 \tag{87}
\end{align}$$ In particular the $B_k$ and $C_k$ in the cross term are exactly the same ones as in the pure power and cosine terms. Adding the constants in these identities to $c_{\kappa,n}\log2$ gives $$\left(-1+\alpha+\gamma-\frac{\kappa+1}{2n}\right)\log2.$$ The omitted-diagonal constants are part of the next $O_\varepsilon(1/n)$ correction.

We control this correction before taking any supremum. A damped cosine diagonal is bounded below by $-\log2+2\log(1-r)$, so the $x$ cosine diagonals cost $O_\varepsilon(1/n)$. For the power diagonal, $$1-\rho(x)^2x^2\ge1-x\quad(x\ge0),\qquad
 1-\rho(x)^2x^2\ge1-(1-\varepsilon)^2\ge\varepsilon\quad(x\le0).$$ Since $1\le1-x\le2$ when $x\le0$, their upward correction is at most $$O_\varepsilon(1/n)-\frac1{2n}\langle\log(1-x)\rangle.$$ Finally, $$1-\sigma(s)^2
 =\varepsilon\sqrt{1-s}\,(2-\varepsilon\sqrt{1-s})
 \ge\varepsilon\sqrt{1-s},$$ so the $s$ cosine diagonals cost at most $O_\varepsilon(1/n)-n^{-1}\langle\log(1-s)\rangle$. The cross term already contains all pairs. There is no loss involving $\log|x|$ or $\log(1+x)$.

For real numbers $a,b$ we have $-a^2\le b^2-2ab$. Apply this to the first square with $b=p_k$, and to the second with $b=v_k$; after dividing by $k$ and summing, the two inequalities are $$\begin{align*}
 -\kappa\sum_k A_k^2/k
 &\le\kappa\|p\|_*^2-2\kappa\sum_kp_kA_k/k,\\
 -\tfrac12\sum_k(B_k-2C_k)^2/k
 &\le\tfrac12\|v\|_*^2-\sum_kv_kB_k/k+2\sum_kv_kC_k/k.
\end{align*}$$ For $\kappa=1$, failure of Equation (67) says $$1-2\left\langle\frac{x^2}{1+x^2}\right\rangle
 >1-\frac1n-2\gamma,
 \qquad\text{hence}\qquad \langle D(x)\rangle>-1/n.$$ It follows that adding $\lambda\langle D(x)\rangle$ costs at most $\lambda/n$ for an upper bound; this explains both $\lambda\ge0$ and its sign in Equation (78).

Let $T_\varepsilon(p,x)$, $S_\varepsilon(v,x)$, and $T_\varepsilon(v,s)$ denote the three series in Equation (77) with factors $\tau^k$, $\rho(x)^k$, and $\sigma(s)^k$, respectively. The preceding pointwise bounds reduce the upper estimate to the sum of two one-variable suprema, with functions $$\begin{align*}
 X_{n,\varepsilon}(x)
 &=\frac{19}{48}\log|x|
   +\left(\frac1{12}-\frac1{2n}\right)\log(1-x)
   \\
 &\quad-(\kappa/2+\alpha+\eta+\gamma)\log(1+x^2)
   +\lambda D(x)\\
 &\quad-2\kappa T_\varepsilon(p,x)-S_\varepsilon(v,x),\\
 Y_{n,\varepsilon}(s)
 &=\frac7{48}\log s
   +\left(\frac1{12}-\frac1n\right)\log(1-s)
   +2T_\varepsilon(v,s),
\end{align*}$$ plus the constant in Equation (78) and $O(\varepsilon)+O_\varepsilon(1/n)$. All bounded finite-size terms from Equation (80) are included in this last error. For $n\ge24$ both weakened endpoint coefficients are at least $1/24$.

Set $P_1=\sum_k|p_k|$ and $V_1=\sum_k|v_k|$, which are finite. The inequality $1-(1-d)^k\le kd$ shows uniformly that $$\begin{align*}
 |T_\varepsilon(p,x)-T(p,x)|&\le\varepsilon P_1,\\
 |S_\varepsilon(v,x)-S(v,x)|&\le2\varepsilon V_1,\\
 |T_\varepsilon(v,s)-T(v,s)|&\le\varepsilon V_1.
\end{align*}$$ Thus the changes in the two tangent functions are at most $2\kappa\varepsilon P_1+2\varepsilon V_1$ and $2\varepsilon V_1$, respectively. These are common summable bounds; no uniform convergence of the raw square series is required. All remaining nonsingular terms are bounded uniformly in $n\ge24$ and $0<\varepsilon<1/8$. The unchanged positive coefficients $19/48,7/48$ and the weakened coefficients at least $1/24$ force uniform decay to $-\infty$ near $x=0$, $x=1$, $s=0$, and $s=1$. The values at the fixed comparison points $x=-1/2$, $s=1/2$ have a common finite lower bound. For the first supremum we include the regular endpoint $x=-1$ by continuous extension. There are therefore compact sets, independent of $n\ge24$ and small $\varepsilon$, containing maximizers for both suprema. On these sets the functions converge uniformly as $n\to\infty$ with $\varepsilon$ fixed, and subsequently as $\varepsilon\downarrow0$. Taking the limits in precisely this order removes $O_\varepsilon(1/n)$ first and proves Equation (78). Finally apply Equation (75). ◻

## An exact certificate for the two barriers

All finite decimals in this Section denote exact rational numbers. We specify trial sequences for Equation (78), isolate every stationary point of its two one-variable functions, and bound their values using rational arithmetic.

**Proposition 7.1**. *For the determinants of Equation (7), $$\begin{equation}
\tag{88}
 \limsup_{N\to\infty}\left(\frac{\log|\Delta_N|}{n^2}
                    -\frac12\log2\right)
 \le -2.290939875<-2.2909.
\end{equation}$$ The separate bounds for the majorants in cases $\kappa=2$ and $\kappa=1$ are $-2.290939875$ and $-2.296789875$, respectively.*

### Exact trial sequences

For $\kappa=2$ take $d=10$ and $\lambda_2=0$. For $\kappa=1$ take $d=8$ and $\lambda_1=2.47405979$. Write each sequence as $$\begin{equation}
\tag{89}
 u_k=l_k+\sum_{z}r_z z^k,\qquad l_k=0\quad(k>d).
\end{equation}$$ The following tables give all coefficients. Every integer coefficient in them is to be multiplied by $10^{-8}$. The finite parts are listed in increasing order of $k$:

<table>
<thead>
<tr>
<th style="text-align: center;"><span class="math inline">$\kappa$</span></th>
<th style="text-align: center;"><span class="math inline">$u$</span></th>
<th colspan="5" style="text-align: center;">finite coefficients</th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: center;">2</td>
<td style="text-align: center;"><span class="math inline">$p$</span></td>
<td style="text-align: right;">45559127</td>
<td style="text-align: right;">-50750856</td>
<td style="text-align: right;">-6578767</td>
<td style="text-align: right;">13970217</td>
<td style="text-align: right;">4786184</td>
</tr>
<tr>
<td style="text-align: center;"></td>
<td style="text-align: center;"></td>
<td style="text-align: right;">-4292433</td>
<td style="text-align: right;">-576704</td>
<td style="text-align: right;">1311615</td>
<td style="text-align: right;">671564</td>
<td style="text-align: right;">-346453</td>
</tr>
<tr>
<td style="text-align: center;">2</td>
<td style="text-align: center;"><span class="math inline">$v$</span></td>
<td style="text-align: right;">-23910158</td>
<td style="text-align: right;">21152432</td>
<td style="text-align: right;">-2885110</td>
<td style="text-align: right;">-11558199</td>
<td style="text-align: right;">6485289</td>
</tr>
<tr>
<td style="text-align: center;"></td>
<td style="text-align: center;"></td>
<td style="text-align: right;">1456821</td>
<td style="text-align: right;">-1912176</td>
<td style="text-align: right;">-2263524</td>
<td style="text-align: right;">2742210</td>
<td style="text-align: right;">-1162454</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th style="text-align: center;"><span class="math inline">$\kappa$</span></th>
<th style="text-align: center;"><span class="math inline">$u$</span></th>
<th colspan="4" style="text-align: center;">finite coefficients</th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: center;">1</td>
<td style="text-align: center;"><span class="math inline">$p$</span></td>
<td style="text-align: right;">11913521</td>
<td style="text-align: right;">-79993701</td>
<td style="text-align: right;">-21956443</td>
<td style="text-align: right;">37903579</td>
</tr>
<tr>
<td style="text-align: center;"></td>
<td style="text-align: center;"></td>
<td style="text-align: right;">10744022</td>
<td style="text-align: right;">-2073193</td>
<td style="text-align: right;">570246</td>
<td style="text-align: right;">-24939103</td>
</tr>
<tr>
<td style="text-align: center;">1</td>
<td style="text-align: center;"><span class="math inline">$v$</span></td>
<td style="text-align: right;">-89913025</td>
<td style="text-align: right;">52874280</td>
<td style="text-align: right;">45168341</td>
<td style="text-align: right;">-30708629</td>
</tr>
<tr>
<td style="text-align: center;"></td>
<td style="text-align: center;"></td>
<td style="text-align: right;">-19269841</td>
<td style="text-align: right;">33922112</td>
<td style="text-align: right;">9819141</td>
<td style="text-align: right;">-16992389</td>
</tr>
</tbody>
</table>

Case $\kappa=1$ has no exponential terms. The exponential terms for $\kappa=2$ are as follows. For a real base $z$ the displayed $a$ is the coefficient of $z^k$. For a nonreal base the two entries $a,b$ are the coefficients of $\Re(z^k),\Im(z^k)$, in that order. In Equation (89) such a pair is represented by $r_z=(a-ib)/2$ and $r_{\bar z}=\overline{r_z}$, with the factor $10^{-8}$ applied to $a,b$. Each real base appears once and each nonreal base together with its conjugate.

| $u$ |   base $z$   |       $a$ |       $b$ |
|:---:|:------------:|----------:|----------:|
| $p$ |    $.85$     |  -9338452 |         — |
|     |    $.94$     |  -2141509 |         — |
|     |    $.7i$     | -66277922 | -31907569 |
|     |    $.85i$    |  -1231651 |   6002645 |
|     | $.092+.92i$  |  -3225918 |   8928234 |
|     | $-.092+.92i$ |  -2105536 |  -9091287 |
| $v$ |    $-.8$     |  15199211 |         — |
|     |    $-.96$    |   4451662 |         — |
|     |    $.88$     |   2545398 |         — |
|     |    $.95$     |  -4932634 |         — |
|     |    $.984$    |  11618157 |         — |
|     |    $.78i$    |  27238714 | -38447936 |
|     |    $.9i$     | -31341084 | -30188786 |
|     |   $.955i$    |  -6693542 |  11912254 |
|     |   $.984i$    |   2055213 | -21715849 |

In particular these are real exponentially decaying sequences. There are ten $p$ tail terms and thirteen $v$ tail terms when conjugates are counted, and their base moduli are at most $.94$ and $.984$, respectively. All the $|l_k|$ and $|r_z|$ are less than $1$.

The convergent power series for the logarithm give the finite formulas $$\begin{align}
 \|u\|_*^2
 &=\sum_{k=1}^d\frac{l_k^2+2l_k\sum_zr_zz^k}{k}
             -\sum_{z,z'}r_zr_{z'}\operatorname{Log}(1-zz'),\notag\\
 T(u,x)&=\sum_{k=1}^d\frac{l_kT_k(x)}{k}
             -\frac12\sum_zr_z\operatorname{Log}(1-2xz+z^2),\notag\\
 S(u,x)&=\sum_{k=1}^d\frac{l_kx^k}{k}
             -\sum_zr_z\operatorname{Log}(1-xz).
 \tag{90}
\end{align}$$ Here $\operatorname{Log}$ is the principal complex logarithm; all sums are real by conjugation. There is no branch ambiguity in these formulas. For the norm and power terms the log arguments have positive real part. For the cosine term, writing $x=\cos\theta$ gives $$1-2xz+z^2=(1-ze^{i\theta})(1-ze^{-i\theta}).$$ Both factors have positive real part, and their principal arguments sum strictly inside $(-\pi,\pi)$. The sum of their logarithms is therefore exactly the principal logarithm of the product, including when the product has negative real part.

For these choices put $$\begin{align}
 X_\kappa(x)&=W_\kappa(x)+\lambda_\kappa D(x)
                         -2\kappa T(p,x)-S(v,x),\notag\\
 Y_\kappa(x)&=\beta\log x+\gamma\log(1-x)+2T(v,x).
 \tag{91}
\end{align}$$ The domain of $X_\kappa$ is $[-1,1)\setminus\{0\}$, and that of $Y_\kappa$ is $(0,1)$.

### Derivative numerators and exhaustive root brackets

Define the rational functions $$\begin{align*}
 t_u(x)&=\sum_{k=1}^dl_kU_{k-1}(x)
               +\sum_z\frac{r_zz}{1-2xz+z^2},\\
 h_u(x)&=\sum_{k=1}^dl_kx^{k-1}
               +\sum_z\frac{r_zz}{1-xz}.
\end{align*}$$ Differentiation of Equation (90) yields $$\begin{align}
 X_\kappa'(x)
 &=\frac{\alpha+2\gamma}{x}-\frac{2\eta}{1-x}
 -(\kappa+2\alpha+2\eta+2\gamma)\frac{x}{1+x^2}
 \notag\\
 &\quad-\frac{4\lambda_\kappa x}{(1+x^2)^2}
 -2\kappa t_p(x)-h_v(x),\notag\\
 Y_\kappa'(x)&=\frac\beta x-\frac\gamma{1-x}+2t_v(x).
 \tag{92}
\end{align}$$ For a completely specified rational numerator, use $$\begin{align}
 Q_X(x)&=x(1-x)(1+x^2)^{3-\kappa}
       \prod_{z\text{ in }p}(1-2xz+z^2)
       \prod_{z\text{ in }v}(1-xz),\notag\\
 Q_Y(x)&=x(1-x)\prod_{z\text{ in }v}(1-2xz+z^2),\notag\\
 A_X(x)&=Q_X(x)X_\kappa'(x),\notag\\
 A_Y(x)&=Q_Y(x)Y_\kappa'(x).
 \tag{93}
\end{align}$$ Empty products equal $1$. These equations, the coefficient tables, and $T_0=1,T_1=x$, $U_0=1,U_1=2x$, with recurrence $V_{k+1}=2xV_k-V_{k-1}$, specify the four polynomials over $\mathbb Q$ without any numerical root calculation. The denominators do not vanish on the indicated open domains: $|1-xz|\ge1-|z|>0$, and $|1-2xz+z^2|\ge(1-|z|)^2>0$ for real $|x|\le1$. Conjugate factors in $Q_X,Q_Y$ have positive products, and real-base factors are positive. Hence $Q_X$ has the sign of $x$ on its domain and $Q_Y>0$ on $(0,1)$.

Here is an exact root-count certificate. If $A(x)=\sum_{j=0}^{d_0}A_jx^j$ is the specified numerator, on a subinterval $(b,c)$ form $$\begin{equation}
\tag{94}
 (1+t)^{d_0}A\left(\frac{b+ct}{1+t}\right)
 =\sum_{h=0}^{d_0}a_ht^h,\qquad
 a_h=\sum_{j=0}^{d_0}\sum_{k=0}^j
 A_j\binom jk b^{j-k}c^k\binom{d_0-j}{h-k},
\end{equation}$$ where out-of-range binomial coefficients are zero. Delete zero coefficients and count consecutive sign changes. The degrees and the resulting counts, in the order of the consecutive intervals, are

| $\kappa$ | function | $d_0$ | division points  | sign variations |
|:--------:|:--------:|:-----:|:-----------------|:----------------|
|    2     |   $X$    |  36   | $-1,0,1$         | $9,9$           |
|    2     |   $Y$    |  24   | $0,.25,.5,.75,1$ | $5,2,2,6$       |
|    1     |   $X$    |  13   | $-1,-.5,0,.5,1$  | $1,1,2,1$       |
|    1     |   $Y$    |   9   | $0,1$            | $5$             |

The sign-variation bound is Descartes’ rule of signs [7, Book III, p. 373]. For completeness, the required bound follows by factoring out positive real roots: multiplication of a real polynomial by $t-r$, $r>0$, increases the number of variations by at least one. To see this, positive rescaling of the variable reduces to $r=1$, and zero initial coefficients can be removed. If $a_0,\ldots,a_d$ are the old coefficients and $b_0,\ldots,b_{d+1}$ the new ones, then $$\sum_{j=0}^h b_j=-a_h\quad(0\le h\le d),\qquad b_{d+1}=a_d.$$ Each sign change between nonzero partial sums forces an intervening $b_j$ with the sign of the later partial sum. Starting with $b_0=-a_0$, these choices give an ordered subsequence with all the variations of the $a_h$; the final coefficient $b_{d+1}$ has the opposite sign to the last partial sum and supplies one further variation. Factoring successively therefore proves that the variation count bounds the number of positive roots with multiplicity. The substitution in Equation (94) sends $t>0$ bijectively to $(b,c)$ and does not change multiplicities.

The following integers $m$ specify disjoint open brackets $(m,m+2)/10^{10}$ for roots of the corresponding derivative:

<table>
<thead>
<tr>
<th style="text-align: center;"><span class="math inline">$\kappa$</span></th>
<th style="text-align: center;">function</th>
<th colspan="3" style="text-align: center;"><span class="math inline">$m$</span></th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: center;">2</td>
<td style="text-align: center;"><span class="math inline">$X$</span></td>
<td style="text-align: right;">-9601109148</td>
<td style="text-align: right;">-8942317572</td>
<td style="text-align: right;">-7608305633</td>
</tr>
<tr>
<td style="text-align: center;"></td>
<td style="text-align: center;"></td>
<td style="text-align: right;">-6503394794</td>
<td style="text-align: right;">-5185864065</td>
<td style="text-align: right;">-4015634158</td>
</tr>
<tr>
<td style="text-align: center;"></td>
<td style="text-align: center;"></td>
<td style="text-align: right;">-3108806646</td>
<td style="text-align: right;">-2067921826</td>
<td style="text-align: right;">-1589849496</td>
</tr>
<tr>
<td style="text-align: center;"></td>
<td style="text-align: center;"></td>
<td style="text-align: right;">1531948062</td>
<td style="text-align: right;">2072448179</td>
<td style="text-align: right;">3208186484</td>
</tr>
<tr>
<td style="text-align: center;"></td>
<td style="text-align: center;"></td>
<td style="text-align: right;">4381119427</td>
<td style="text-align: right;">5851354199</td>
<td style="text-align: right;">7269030693</td>
</tr>
<tr>
<td style="text-align: center;"></td>
<td style="text-align: center;"></td>
<td style="text-align: right;">8390277402</td>
<td style="text-align: right;">9332614564</td>
<td style="text-align: right;">9709786219</td>
</tr>
<tr>
<td style="text-align: center;">2</td>
<td style="text-align: center;"><span class="math inline">$Y$</span></td>
<td style="text-align: right;">176402802</td>
<td style="text-align: right;">330649406</td>
<td style="text-align: right;">764952882</td>
</tr>
<tr>
<td style="text-align: center;"></td>
<td style="text-align: center;"></td>
<td style="text-align: right;">1227250753</td>
<td style="text-align: right;">2149465998</td>
<td style="text-align: right;">3048189112</td>
</tr>
<tr>
<td style="text-align: center;"></td>
<td style="text-align: center;"></td>
<td style="text-align: right;">4322699096</td>
<td style="text-align: right;">5564757994</td>
<td style="text-align: right;">6801929373</td>
</tr>
<tr>
<td style="text-align: center;"></td>
<td style="text-align: center;"></td>
<td style="text-align: right;">8031988371</td>
<td style="text-align: right;">8877037851</td>
<td style="text-align: right;">9577761832</td>
</tr>
<tr>
<td style="text-align: center;"></td>
<td style="text-align: center;"></td>
<td style="text-align: right;">9838463999</td>
<td style="text-align: right;">9972727815</td>
<td style="text-align: right;">9992037196</td>
</tr>
<tr>
<td style="text-align: center;">1</td>
<td style="text-align: center;"><span class="math inline">$X$</span></td>
<td style="text-align: right;">-9917299785</td>
<td style="text-align: right;">-2259572153</td>
<td style="text-align: right;">2543808026</td>
</tr>
<tr>
<td style="text-align: center;"></td>
<td style="text-align: center;"></td>
<td style="text-align: right;">4437270259</td>
<td style="text-align: right;">6348298970</td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td style="text-align: center;">1</td>
<td style="text-align: center;"><span class="math inline">$Y$</span></td>
<td style="text-align: right;">532669786</td>
<td style="text-align: right;">2504239325</td>
<td style="text-align: right;">5701738806</td>
</tr>
<tr>
<td style="text-align: center;"></td>
<td style="text-align: center;"></td>
<td style="text-align: right;">7966939383</td>
<td style="text-align: right;">9454490138</td>
<td style="text-align: right;"></td>
</tr>
</tbody>
</table>

For each integer in this table the exact sign check is $$\begin{equation}
\tag{95}
 N_A(m)N_A(m+2)<0,\qquad
 N_A(s)=\sum_{j=0}^{d_0}A_j(10^{10})^{d_0-j}s^j.
\end{equation}$$ Equations (93), (94), and (95) give rational addition and multiplication recipes for every entry of the root certificate. The numbers of brackets in each consecutive interval equal the displayed variation counts. The intermediate value theorem and the variation bound therefore give exactly one simple root per bracket and no other roots in those open intervals. Possible roots at the division points are harmless because all finite division points are evaluated separately below.

### Rational logarithms and all candidate values

Here is the rational procedure used for the value bounds. For a positive rational $s$, write $s=2^m y$ with $1\le y\le2$, and put $$\begin{equation}
\tag{96}
 H(y)=2\sum_{j=0}^{17}\frac1{2j+1}
               \left(\frac{y-1}{y+1}\right)^{2j+1}.
\end{equation}$$ The substitution for $\log s$ is $mH(2)+H(y)$. If $q=(y-1)/(y+1)$, its unscaled positive remainder is bounded by $$0\le\log y-H(y)\le\frac{2q^{37}}{37(1-q^2)}.$$ For a nonzero rational complex number $a+ib$, its real log part is half the real log of $a^2+b^2$. For its principal argument choose an octant: rotate by $-k\pi/4$, $-4\le k\le4$, so the rotated real part is positive and the imaginary-to-real ratio $t$ satisfies $|t|\le1/2$. Select the rotation for which $k\pi/4+\arctan t$ is the principal argument; at the negative real axis use the value $\pi$. The ratio $t$ is rational, since the rotation can be performed, up to a positive scale, by repeated maps $(a,b)\mapsto(a+b,b-a)$ or $(a-b,a+b)$. With $$\begin{equation}
\tag{97}
 J(t)=\sum_{j=0}^{23}\frac{(-1)^jt^{2j+1}}{2j+1},
\end{equation}$$ substitute $k(J(1/2)+J(1/3))+J(t)$ for the argument. The identity $$\arctan(1/2)+\arctan(1/3)=\pi/4$$ follows from the tangent addition formula and the fact that both summands are positive and their sum is less than $\pi/2$. The alternating-series estimate gives $|\arctan t-J(t)|\le |t|^{49}/49$.

All positive inputs used here, including squared moduli, lie between $2^{-100}$ and $2^{100}$. Indeed, the real arguments at the evaluation points are between $.0007$ and $2$, and the squared moduli of all complex arguments lie between $(.016)^4$ and $(1+.984)^4$, by the factor bounds following Equation (93). Thus at most $100$ scaling steps are needed. To make the error allowance explicit, set $$h_0=\frac{2(1/3)^{37}}{37(1-1/9)},\qquad
 j_0=\frac{(1/2)^{49}}{49}.$$ A real log substitution costs at most $101h_0$, and an argument costs at most $9j_0$. In particular $2\cdot101h_0+9j_0<7\cdot10^{-16}$, so $10^{-15}$ is an upper bound for the absolute error of a complex log. This also proves the coarser allowance $10^{-11}$ per log.

All rational polynomial terms in Equation (90) are evaluated exactly. The total absolute log coefficient mass in $\kappa\|p\|_*^2+\|v\|_*^2/2$ is at most $2\cdot10^2+13^2/2=284.5$, in $X_\kappa$ it is less than $2\cdot10+13+2=35$, and in $Y_\kappa$ it is less than $13+1=14$. Their resulting substitution errors are respectively less than $2.85\cdot10^{-13}$, $3.5\cdot10^{-14}$, and $1.4\cdot10^{-14}$, all less than $10^{-8}$. One may enclose each rational series term between consecutive multiples of $10^{-40}$, add the displayed remainder bounds with outward signs, and then propagate intervals linearly. This additional rounding changes the preceding allowances by less than $10^{-32}$. For a complex weight $c$, use $\Re(c\operatorname{Log}z)=\Re(c)\Re(\operatorname{Log}z) -\Im(c)\Im(\operatorname{Log}z)$, retaining the sign of each weight in interval multiplication. This fully specifies a rational interval calculation; no numerical logarithms are needed.

For transparency, Table 2 gives all fifty point-value upper bounds. Its argument column is $10^{10}x$. A row marked $B$ is the left endpoint of the corresponding root bracket above; a row marked $P$ is a finite division point. Each displayed bound is a rational upper bound rounded upwards to twelve decimal places after the series remainder has been included. The largest unrounded interval width in this table is less than $2.16146856249281\cdot10^{-16}$.

**Table 2:** Certified rational upper bounds at every candidate evaluation point.

<table>
<thead>
<tr>
<th style="text-align: center;"><span class="math inline">$\kappa$</span></th>
<th style="text-align: center;">function</th>
<th style="text-align: right;"><span class="math inline">$10^{10}x$</span></th>
<th style="text-align: right;">type</th>
<th style="text-align: right;">upper bound</th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: center;">2</td>
<td style="text-align: center;"><span class="math inline">$X$</span></td>
<td style="text-align: right;">-9601109148</td>
<td style="text-align: right;">B</td>
<td style="text-align: right;">-0.984034048775</td>
</tr>
<tr>
<td style="text-align: center;">2</td>
<td style="text-align: center;"><span class="math inline">$X$</span></td>
<td style="text-align: right;">-8942317572</td>
<td style="text-align: right;">B</td>
<td style="text-align: right;">-0.984375363807</td>
</tr>
<tr>
<td style="text-align: center;">2</td>
<td style="text-align: center;"><span class="math inline">$X$</span></td>
<td style="text-align: right;">-7608305633</td>
<td style="text-align: right;">B</td>
<td style="text-align: right;">-0.984034052640</td>
</tr>
<tr>
<td style="text-align: center;">2</td>
<td style="text-align: center;"><span class="math inline">$X$</span></td>
<td style="text-align: right;">-6503394794</td>
<td style="text-align: right;">B</td>
<td style="text-align: right;">-0.984105522615</td>
</tr>
<tr>
<td style="text-align: center;">2</td>
<td style="text-align: center;"><span class="math inline">$X$</span></td>
<td style="text-align: right;">-5185864065</td>
<td style="text-align: right;">B</td>
<td style="text-align: right;">-0.984034053414</td>
</tr>
<tr>
<td style="text-align: center;">2</td>
<td style="text-align: center;"><span class="math inline">$X$</span></td>
<td style="text-align: right;">-4015634158</td>
<td style="text-align: right;">B</td>
<td style="text-align: right;">-0.984092061375</td>
</tr>
<tr>
<td style="text-align: center;">2</td>
<td style="text-align: center;"><span class="math inline">$X$</span></td>
<td style="text-align: right;">-3108806646</td>
<td style="text-align: right;">B</td>
<td style="text-align: right;">-0.984034037901</td>
</tr>
<tr>
<td style="text-align: center;">2</td>
<td style="text-align: center;"><span class="math inline">$X$</span></td>
<td style="text-align: right;">-2067921826</td>
<td style="text-align: right;">B</td>
<td style="text-align: right;">-0.984364031075</td>
</tr>
<tr>
<td style="text-align: center;">2</td>
<td style="text-align: center;"><span class="math inline">$X$</span></td>
<td style="text-align: right;">-1589849496</td>
<td style="text-align: right;">B</td>
<td style="text-align: right;">-0.984034038450</td>
</tr>
<tr>
<td style="text-align: center;">2</td>
<td style="text-align: center;"><span class="math inline">$X$</span></td>
<td style="text-align: right;">1531948062</td>
<td style="text-align: right;">B</td>
<td style="text-align: right;">-0.984033385315</td>
</tr>
<tr>
<td style="text-align: center;">2</td>
<td style="text-align: center;"><span class="math inline">$X$</span></td>
<td style="text-align: right;">2072448179</td>
<td style="text-align: right;">B</td>
<td style="text-align: right;">-0.984776982913</td>
</tr>
<tr>
<td style="text-align: center;">2</td>
<td style="text-align: center;"><span class="math inline">$X$</span></td>
<td style="text-align: right;">3208186484</td>
<td style="text-align: right;">B</td>
<td style="text-align: right;">-0.984034026898</td>
</tr>
<tr>
<td style="text-align: center;">2</td>
<td style="text-align: center;"><span class="math inline">$X$</span></td>
<td style="text-align: right;">4381119427</td>
<td style="text-align: right;">B</td>
<td style="text-align: right;">-0.984264010107</td>
</tr>
<tr>
<td style="text-align: center;">2</td>
<td style="text-align: center;"><span class="math inline">$X$</span></td>
<td style="text-align: right;">5851354199</td>
<td style="text-align: right;">B</td>
<td style="text-align: right;">-0.984034029391</td>
</tr>
<tr>
<td style="text-align: center;">2</td>
<td style="text-align: center;"><span class="math inline">$X$</span></td>
<td style="text-align: right;">7269030693</td>
<td style="text-align: right;">B</td>
<td style="text-align: right;">-0.984245044505</td>
</tr>
<tr>
<td style="text-align: center;">2</td>
<td style="text-align: center;"><span class="math inline">$X$</span></td>
<td style="text-align: right;">8390277402</td>
<td style="text-align: right;">B</td>
<td style="text-align: right;">-0.984034016294</td>
</tr>
<tr>
<td style="text-align: center;">2</td>
<td style="text-align: center;"><span class="math inline">$X$</span></td>
<td style="text-align: right;">9332614564</td>
<td style="text-align: right;">B</td>
<td style="text-align: right;">-0.984567630027</td>
</tr>
<tr>
<td style="text-align: center;">2</td>
<td style="text-align: center;"><span class="math inline">$X$</span></td>
<td style="text-align: right;">9709786219</td>
<td style="text-align: right;">B</td>
<td style="text-align: right;">-0.984033926884</td>
</tr>
<tr>
<td style="text-align: center;">2</td>
<td style="text-align: center;"><span class="math inline">$X$</span></td>
<td style="text-align: right;">-10000000000</td>
<td style="text-align: right;">P</td>
<td style="text-align: right;">-0.986727371546</td>
</tr>
<tr>
<td style="text-align: center;">2</td>
<td style="text-align: center;"><span class="math inline">$Y$</span></td>
<td style="text-align: right;">176402802</td>
<td style="text-align: right;">B</td>
<td style="text-align: right;">-1.608946411646</td>
</tr>
<tr>
<td style="text-align: center;">2</td>
<td style="text-align: center;"><span class="math inline">$Y$</span></td>
<td style="text-align: right;">330649406</td>
<td style="text-align: right;">B</td>
<td style="text-align: right;">-1.609949505120</td>
</tr>
<tr>
<td style="text-align: center;">2</td>
<td style="text-align: center;"><span class="math inline">$Y$</span></td>
<td style="text-align: right;">764952882</td>
<td style="text-align: right;">B</td>
<td style="text-align: right;">-1.608960295828</td>
</tr>
<tr>
<td style="text-align: center;">2</td>
<td style="text-align: center;"><span class="math inline">$Y$</span></td>
<td style="text-align: right;">1227250753</td>
<td style="text-align: right;">B</td>
<td style="text-align: right;">-1.609094597854</td>
</tr>
<tr>
<td style="text-align: center;">2</td>
<td style="text-align: center;"><span class="math inline">$Y$</span></td>
<td style="text-align: right;">2149465998</td>
<td style="text-align: right;">B</td>
<td style="text-align: right;">-1.608960426500</td>
</tr>
<tr>
<td style="text-align: center;">2</td>
<td style="text-align: center;"><span class="math inline">$Y$</span></td>
<td style="text-align: right;">3048189112</td>
<td style="text-align: right;">B</td>
<td style="text-align: right;">-1.608992193672</td>
</tr>
<tr>
<td style="text-align: center;">2</td>
<td style="text-align: center;"><span class="math inline">$Y$</span></td>
<td style="text-align: right;">4322699096</td>
<td style="text-align: right;">B</td>
<td style="text-align: right;">-1.608960428486</td>
</tr>
<tr>
<td style="text-align: center;">2</td>
<td style="text-align: center;"><span class="math inline">$Y$</span></td>
<td style="text-align: right;">5564757994</td>
<td style="text-align: right;">B</td>
<td style="text-align: right;">-1.608979509517</td>
</tr>
<tr>
<td style="text-align: center;">2</td>
<td style="text-align: center;"><span class="math inline">$Y$</span></td>
<td style="text-align: right;">6801929373</td>
<td style="text-align: right;">B</td>
<td style="text-align: right;">-1.608960430478</td>
</tr>
<tr>
<td style="text-align: center;">2</td>
<td style="text-align: center;"><span class="math inline">$Y$</span></td>
<td style="text-align: right;">8031988371</td>
<td style="text-align: right;">B</td>
<td style="text-align: right;">-1.608990548812</td>
</tr>
<tr>
<td style="text-align: center;">2</td>
<td style="text-align: center;"><span class="math inline">$Y$</span></td>
<td style="text-align: right;">8877037851</td>
<td style="text-align: right;">B</td>
<td style="text-align: right;">-1.608960429811</td>
</tr>
<tr>
<td style="text-align: center;">2</td>
<td style="text-align: center;"><span class="math inline">$Y$</span></td>
<td style="text-align: right;">9577761832</td>
<td style="text-align: right;">B</td>
<td style="text-align: right;">-1.609055802895</td>
</tr>
<tr>
<td style="text-align: center;">2</td>
<td style="text-align: center;"><span class="math inline">$Y$</span></td>
<td style="text-align: right;">9838463999</td>
<td style="text-align: right;">B</td>
<td style="text-align: right;">-1.608960412835</td>
</tr>
<tr>
<td style="text-align: center;">2</td>
<td style="text-align: center;"><span class="math inline">$Y$</span></td>
<td style="text-align: right;">9972727815</td>
<td style="text-align: right;">B</td>
<td style="text-align: right;">-1.609694899071</td>
</tr>
<tr>
<td style="text-align: center;">2</td>
<td style="text-align: center;"><span class="math inline">$Y$</span></td>
<td style="text-align: right;">9992037196</td>
<td style="text-align: right;">B</td>
<td style="text-align: right;">-1.608958123669</td>
</tr>
<tr>
<td style="text-align: center;">2</td>
<td style="text-align: center;"><span class="math inline">$Y$</span></td>
<td style="text-align: right;">2500000000</td>
<td style="text-align: right;">P</td>
<td style="text-align: right;">-1.608973617030</td>
</tr>
<tr>
<td style="text-align: center;">2</td>
<td style="text-align: center;"><span class="math inline">$Y$</span></td>
<td style="text-align: right;">5000000000</td>
<td style="text-align: right;">P</td>
<td style="text-align: right;">-1.608971701898</td>
</tr>
<tr>
<td style="text-align: center;">2</td>
<td style="text-align: center;"><span class="math inline">$Y$</span></td>
<td style="text-align: right;">7500000000</td>
<td style="text-align: right;">P</td>
<td style="text-align: right;">-1.608976908052</td>
</tr>
<tr>
<td style="text-align: center;">1</td>
<td style="text-align: center;"><span class="math inline">$X$</span></td>
<td style="text-align: right;">-9917299785</td>
<td style="text-align: right;">B</td>
<td style="text-align: right;">-2.778491531574</td>
</tr>
<tr>
<td style="text-align: center;">1</td>
<td style="text-align: center;"><span class="math inline">$X$</span></td>
<td style="text-align: right;">-2259572153</td>
<td style="text-align: right;">B</td>
<td style="text-align: right;">-1.324666731948</td>
</tr>
<tr>
<td style="text-align: center;">1</td>
<td style="text-align: center;"><span class="math inline">$X$</span></td>
<td style="text-align: right;">2543808026</td>
<td style="text-align: right;">B</td>
<td style="text-align: right;">-1.324655807046</td>
</tr>
<tr>
<td style="text-align: center;">1</td>
<td style="text-align: center;"><span class="math inline">$X$</span></td>
<td style="text-align: right;">4437270259</td>
<td style="text-align: right;">B</td>
<td style="text-align: right;">-1.352236629957</td>
</tr>
<tr>
<td style="text-align: center;">1</td>
<td style="text-align: center;"><span class="math inline">$X$</span></td>
<td style="text-align: right;">6348298970</td>
<td style="text-align: right;">B</td>
<td style="text-align: right;">-1.324666329425</td>
</tr>
<tr>
<td style="text-align: center;">1</td>
<td style="text-align: center;"><span class="math inline">$X$</span></td>
<td style="text-align: right;">-10000000000</td>
<td style="text-align: right;">P</td>
<td style="text-align: right;">-2.775818077526</td>
</tr>
<tr>
<td style="text-align: center;">1</td>
<td style="text-align: center;"><span class="math inline">$X$</span></td>
<td style="text-align: right;">-5000000000</td>
<td style="text-align: right;">P</td>
<td style="text-align: right;">-1.544057819905</td>
</tr>
<tr>
<td style="text-align: center;">1</td>
<td style="text-align: center;"><span class="math inline">$X$</span></td>
<td style="text-align: right;">5000000000</td>
<td style="text-align: right;">P</td>
<td style="text-align: right;">-1.347557680876</td>
</tr>
<tr>
<td style="text-align: center;">1</td>
<td style="text-align: center;"><span class="math inline">$Y$</span></td>
<td style="text-align: right;">532669786</td>
<td style="text-align: right;">B</td>
<td style="text-align: right;">-1.428286151250</td>
</tr>
<tr>
<td style="text-align: center;">1</td>
<td style="text-align: center;"><span class="math inline">$Y$</span></td>
<td style="text-align: right;">2504239325</td>
<td style="text-align: right;">B</td>
<td style="text-align: right;">-1.515602647362</td>
</tr>
<tr>
<td style="text-align: center;">1</td>
<td style="text-align: center;"><span class="math inline">$Y$</span></td>
<td style="text-align: right;">5701738806</td>
<td style="text-align: right;">B</td>
<td style="text-align: right;">-1.428335732372</td>
</tr>
<tr>
<td style="text-align: center;">1</td>
<td style="text-align: center;"><span class="math inline">$Y$</span></td>
<td style="text-align: right;">7966939383</td>
<td style="text-align: right;">B</td>
<td style="text-align: right;">-1.465686164672</td>
</tr>
<tr>
<td style="text-align: center;">1</td>
<td style="text-align: center;"><span class="math inline">$Y$</span></td>
<td style="text-align: right;">9454490138</td>
<td style="text-align: right;">B</td>
<td style="text-align: right;">-1.428335358167</td>
</tr>
</tbody>
</table>

The same calculation gives the following upper bounds for $\kappa\|p\|_*^2+\tfrac12\|v\|_*^2$: $$.778415976284\quad(\kappa=2),\qquad
 .931985203901\quad(\kappa=1).$$ In particular the rational substituted expressions, before their error allowances are added, satisfy the following convenient stronger cutoffs:

| $\kappa$ | $\kappa\Vert p\Vert_*^2+\Vert v\Vert_*^2/2$ | $X$ at listed points | $Y$ at listed points |
|:--:|:--:|:--:|:--:|
| 2 | $.77843$ | $-.98400$ | $-1.60891$ |
| 1 | $.93205$ | $-1.32442$ | $-1.42805$ |

Each entry means a strict upper bound. With the $10^{-8}$ allowance, the weaker cutoffs we shall actually use are $$\begin{equation}
\tag{98}
\begin{array}{c|ccc}
 \kappa&\kappa\|p\|_*^2+\tfrac12\|v\|_*^2&X&Y\\\hline
 2&.77844&-.98399&-1.60890\\
 1&.9321&-1.3244&-1.4280.
\end{array}
\end{equation}$$ The logarithm procedure also gives $.693146<\log2<.693149$.

### From bracket values to global suprema

A single derivative bound suffices on every whole closed bracket in the root table. All its points have distance greater than $.0007$ from both $0$ and $1$. In particular the bracket nearest $s=1$ has right endpoint $9992037198/10^{10}$, whose distance from $1$ is exactly $.0007962802$. For $|x|\le1$, the identity $U_{k-1}(\cos\theta)=\sin(k\theta)/\sin\theta$ gives $|U_{k-1}(x)|\le k$, including its endpoint limits. Using the coefficient and base bounds above, the polynomial part of $X_\kappa'$ is at most $4\sum_{k=1}^{10}k+10=230$ in absolute value; its endpoint terms are bounded by $(19/48+1/12)/.0007<685$; its $x/(1+x^2)$ term is less than $3$; and its multiplier term is less than $4\lambda_1<10$. Its two log-tail derivatives are bounded by $$\frac{4\cdot10}{(.06)^2}+\frac{13}{.016}<11924.$$ Consequently $|X_\kappa'|<12852<120000$ throughout every listed bracket. For $Y_\kappa'$ the polynomial part is at most $110$, the endpoint terms are bounded by $(7/48+1/12)/.0007<328$, and the log tails are bounded by $26/(.016)^2=101562.5$. Hence $|Y_\kappa'|<102001<120000$ on every whole bracket as well. These estimates hold for both cases, with empty tails in case $1$.

It follows from the mean value theorem that moving from a left bracket endpoint to its stationary point increases either value by less than $$120000\cdot\frac2{10^{10}}=.000024.$$ Every interior stationary point is in one of these brackets or is a division point. All finite division points have been included in Table 2: $-1$ for $X_2$; $1/4,1/2,3/4$ for $Y_2$; and $-1,-1/2,1/2$ for $X_1$. The remaining endpoints are singular and have limit $-\infty$: $x\to0^\pm$ and $x\to1^-$ for $X_\kappa$, and $x\to0^+$ and $x\to1^-$ for $Y_\kappa$. The bounded tangent and multiplier terms do not alter these limits. Thus the root exhaustion, the finite endpoint values, and the derivative estimate together certify the global suprema, not merely the sampled values.

Finally $-1+\alpha+\gamma=-11/16$. Apply Proposition 6.1, use Equation (98), and add $.000024$ for each supremum. Since $\log2>.693146$, the right side is strictly less than, respectively, $$\begin{align*}
 -\frac{11}{16}(.693146)+.77844-.98399-1.60890+.000048
    &=-2.290939875,\\
 -\frac{11}{16}(.693146)+.9321-1.3244-1.4280+.000048
    &=-2.296789875.
\end{align*}$$ Taking the larger of these constants proves Proposition 7.1.

## Conclusion

*Proof of Theorem 1.1.* Suppose that $G$ is rational. Proposition 2.1 then makes $\Delta_N$ rational for every $N$. By Proposition 4.1, $\Delta_p\ne0$ for every sufficiently large prime $p$. Apply the product-formula lower bound of Proposition 3.4 along this sequence: $$\liminf_{\substack{p\to\infty\\p\ {\rm prime}}}
\left(\frac{\log|\Delta_p|}{(48p)^2}-\frac12\log2\right)>-2.29084.$$ Proposition 7.1 gives, along the same sequence, an upper limit strictly smaller than $-2.2909$. Since $-2.29084>-2.2909$, this is a contradiction. Therefore $G$ is irrational. ◻

##### Hyperbolic volumes.

Normalize sectional curvature to $-1$. Agol’s theorem identifies $4G$ as the minimum volume of an orientable complete finite-volume hyperbolic three-manifold with exactly two cusps, attained by the Whitehead-link and $(-2,3,8)$-pretzel-link complements [1, Introduction and Theorem 3.6]. Theorem 1.1 therefore makes this minimum and both link volumes irrational. More generally, every orientable arithmetic hyperbolic three-orbifold defined over $\mathbb Q(i)$ has irrational volume. Here its lattice $\Gamma\le\operatorname{PSL}_2(\mathbb C)$ is, up to conjugacy, commensurable with the projective norm-one group $\Gamma^1(\mathcal O)=\mathcal O^1/\{\pm1\}$ of a maximal order $\mathcal O$ in some quaternion algebra $B/\mathbb Q(i)$ [24, Definition 38.3.4]. For each such algebra, with finite reduced discriminant $\mathfrak D$, the volume formula gives $$\operatorname{vol}\bigl(\Gamma^1(\mathcal O)\backslash\mathbb H^3\bigr)
 =\frac{G}{3}\prod_{\mathfrak p\mid\mathfrak D}(N\mathfrak p-1),$$ where $N\mathfrak p=|\mathbb Z[i]/\mathfrak p|$; this follows by inserting $\zeta_{\mathbb Q(i)}(2)=\zeta(2)L(2,\chi_{-4})=(\pi^2/6)G$ into [24, Theorem 39.1.13]. After conjugating, a common finite-index subgroup $H$ gives $$\operatorname{vol}(\Gamma\backslash\mathbb H^3)
 =\frac{[\Gamma^1(\mathcal O):H]}{[\Gamma:H]}
   \operatorname{vol}\bigl(\Gamma^1(\mathcal O)\backslash\mathbb H^3\bigr),$$ so this volume is a positive rational multiple of $G$ and is irrational. In the split case $B=M_2(\mathbb Q(i))$, $\mathcal O=M_2(\mathbb Z[i])$, the empty product yields $\operatorname{vol}(\operatorname{PSL}_2(\mathbb Z[i])\backslash\mathbb H^3)=G/3$ [24, Example 39.1.16].

## References

**[1]** Ian Agol. The minimal volume orientable hyperbolic 2-cusped 3-manifolds. *Proceedings of the American Mathematical Society*, 138(10):3723–3732, 2010. doi: 10.1090/S0002-9939-10-10364-5. URL <https://arxiv.org/abs/0804.0043v2>. Linked preprint arXiv:0804.0043v2, revised 18 May 2010.

**[2]** Roger Apéry. Irrationalité de $\zeta 2$ et $\zeta 3$. In *Journées Arithmétiques de Luminy*, number 61 in Astérisque, pages 11–13. Société mathématique de France, 1979. URL <https://numdam.org/item/AST_1979__61__11_0/>.

**[3]** Frits Beukers. A note on the irrationality of $\zeta(2)$ and $\zeta(3)$. *Bulletin of the London Mathematical Society*, 11(3):268–272, 1979. doi: 10.1112/blms/11.3.268. URL <https://doi.org/10.1112/blms/11.3.268>.

**[4]** Frank Calegari. Irrationality of certain $p$-adic periods for small $p$. *International Mathematics Research Notices*, 2005(20):1235–1249, 2005. doi: 10.1155/IMRN.2005.1235. URL <https://www.math.uchicago.edu/~fcale/papers/Beukers.pdf>.

**[5]** Frank Calegari, Vesselin Dimitrov, and Yunqing Tang. The linear independence of $1$, $\zeta(2)$, and $L(2,\chi_{-3})$. Preprint, arXiv:2408.15403v2, 2024. URL <https://arxiv.org/abs/2408.15403v2>. Revised 16 September 2024.

**[6]** Frank Calegari, Vesselin Dimitrov, and Yunqing Tang. Arithmetic holonomy bounds and effective Diophantine approximation. Preprint, arXiv:2510.04156v1, 2025. URL <https://arxiv.org/abs/2510.04156v1>. 5 October 2025.

**[7]** René Descartes. La géométrie. In *Discours de la méthode*. Jan Maire, Leyde, 1637. URL <https://www.unicaen.fr/puc/sources/prodescartes/consult/descartes/Oeuvres/Oeuvres_Descartes/discours_de_la_methode.xml/la_geometrie.html>. Book III, p. 373.

**[8]** Payman Eskandari. Improved rational approximations to Catalan’s constant. Preprint, arXiv:2609.26354v1 \[math.NT\], 2026. URL <https://arxiv.org/abs/2609.26354v1>. Submitted 22 September 2026.

**[9]** Stéphane Fischler. Irrationality of values of $L$-functions of Dirichlet characters. *Journal of the London Mathematical Society*, 101(2):857–876, 2020. doi: 10.1112/jlms.12290. URL <https://www.imo.universite-paris-saclay.fr/~stephane.fischler/Lschi.pdf>.

**[10]** Peter J. Forrester. Meet Andréief, Bordeaux 1886, and Andreev, Kharkov 1882–83. Preprint, arXiv:1806.10411v1, 2018. URL <https://arxiv.org/abs/1806.10411v1>.

**[11]** Stavros Garoufalidis and Ionel Popescu. Analyticity of the planar limit of a matrix model. *Annales Henri Poincaré*, 14:499–565, 2013. doi: 10.1007/s00023-012-0191-y. URL <https://doi.org/10.1007/s00023-012-0191-y>.

**[12]** Christian Krattenthaler. Advanced determinant calculus. *Séminaire Lotharingien de Combinatoire*, 42:B42q, 1999. URL <https://arxiv.org/abs/math/9902004v3>. 67 pp.; arXiv:math/9902004v3.

**[13]** Christian Krattenthaler and Tanguy Rivoal. On a linear form for Catalan’s constant. *South East Asian Journal of Mathematics and Mathematical Sciences*, 6(2):3–15, 2008. URL <https://arxiv.org/abs/0810.1927v1>. Preprint arXiv:0810.1927v1.

**[14]** Christian Krattenthaler and Wadim Zudilin. Hypergeometry inspired by irrationality questions. *Kyushu Journal of Mathematics*, 73(1):189–203, 2019. doi: 10.2206/kyushujm.73.189. URL <https://arxiv.org/abs/1802.08856v2>. Preprint arXiv:1802.08856v2.

**[15]** Li Lai and Li Zhou. At least two of $\zeta(5),\zeta(7),\ldots,\zeta(35)$ are irrational. *Publicationes Mathematicae Debrecen*, 101(3–4):353–372, 2022. doi: 10.5486/PMD.2022.9252. URL <https://arxiv.org/abs/2103.00904v2>. Preprint arXiv:2103.00904v2.

**[16]** National Institute of Standards and Technology. Digital Library of Mathematical Functions, section 18.5, n.d. URL <https://dlmf.nist.gov/18.5>. Equations (18.5.1)–(18.5.2); accessed September 24, 2026.

**[17]** Yu. V. Nesterenko. On Catalan’s constant. *Proceedings of the Steklov Institute of Mathematics*, 292:153–170, 2016. doi: 10.1134/S0081543816010107. URL <https://doi.org/10.1134/S0081543816010107>.

**[18]** Tanguy Rivoal. Nombres d’Euler, approximants de Padé et constante de Catalan. *The Ramanujan Journal*, 11(2):199–214, 2006. doi: 10.1007/s11139-006-6507-0. URL <https://rivoal.perso.math.cnrs.fr/articles/gnew6.pdf>.

**[19]** Tanguy Rivoal and Wadim Zudilin. Diophantine properties of numbers related to Catalan’s constant. *Mathematische Annalen*, 326(4):705–721, 2003. doi: 10.1007/s00208-003-0420-2. URL <https://rivoal.perso.math.cnrs.fr/articles/betacatalan.pdf>.

**[20]** Edward B. Saff. Logarithmic potential theory with applications to approximation theory. *Surveys in Approximation Theory*, 5:165–200, 2010. URL <https://arxiv.org/abs/1010.3760v1>. arXiv:1010.3760v1.

**[21]** Donald Sarason. Generalized interpolation in $H^\infty$. *Transactions of the American Mathematical Society*, 127(2):179–203, 1967. doi: 10.1090/S0002-9947-1967-0208383-8. URL <https://doi.org/10.1090/S0002-9947-1967-0208383-8>.

**[22]** Zhi-Wei Sun. Catalan’s constant is irrational. Preprint, arXiv:2609.04176v1 \[math.GM\], 2026. URL <https://arxiv.org/abs/2609.04176v1>. Submitted 3 September 2026.

**[23]** Carlo Viola. Rational approximations to Catalan’s constant. *Oberwolfach Reports*, 19(2):1100–1101, 2022. doi: 10.4171/OWR/2022/21. URL <https://ems.press/content/serial-article-files/46958>. Joint work with Raffaele Marcovecchio; contribution to Report 21/2022, Diophantische Approximationen.

**[24]** John Voight. *Quaternion Algebras*, volume 288 of *Graduate Texts in Mathematics*. Springer, Cham, 2021. doi: 10.1007/978-3-030-56694-4. URL <https://link.springer.com/book/10.1007/978-3-030-56694-4>.

**[25]** Don Zagier. Newman’s short proof of the prime number theorem. *The American Mathematical Monthly*, 104(8):705–708, 1997. doi: 10.2307/2975232. URL <https://people.mpim-bonn.mpg.de/zagier/files/doi/10.2307/2975232/fulltext.pdf>.

**[26]** Wadim Zudilin. An Apéry-like difference equation for Catalan’s constant. *The Electronic Journal of Combinatorics*, 10(1):R14, 2003. doi: 10.37236/1707. URL <https://arxiv.org/abs/math/0201024v3>. 10 pp.; preprint arXiv:math/0201024v3.

**[27]** Wadim Zudilin. A determinantal approach to irrationality. *Constructive Approximation*, 45(2):301–310, 2017. doi: 10.1007/s00365-016-9333-7. URL <https://arxiv.org/abs/1507.05697v2>. Preprint arXiv:1507.05697v2.

**[28]** Wadim Zudilin. Arithmetic of Catalan’s constant and its relatives. *Abhandlungen aus dem Mathematischen Seminar der Universität Hamburg*, 89(1):45–53, 2019. doi: 10.1007/s12188-019-00203-w. URL <https://arxiv.org/abs/1804.09922v2>. Preprint arXiv:1804.09922v2.
