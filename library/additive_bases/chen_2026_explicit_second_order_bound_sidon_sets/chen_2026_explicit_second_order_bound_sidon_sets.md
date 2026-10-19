# An explicit second-order bound for Sidon sets and the limit of the fixed-kernel energy method

Haoyu Chen  
Independent researcher

October 2, 2026; version 3, October 10, 2026

## Abstract

Let  $F(N)$  be the largest size of a Sidon subset of  $\{1, \dots, N\}$ , with diagonal pair sums included. We prove  $F(N) \leq \sqrt{N} + (2\sqrt{2}/3)N^{1/4} + 1$  for every integer  $N \geq 4600\,000$ ; this statement is also kernel-checked in Lean. The proof uses weighted Erdős–Turán energy with  $h(t) = 2(1-t)\mathbf{1}_{[0,1]}(t)$  and an exact boundary correction of  $2/3$ ; an elementary contraction estimate makes the remainder explicit. We also prove the sharp bound  $\liminf_{L \rightarrow \infty} (C_f(L) - L) \geq 8/(9f(0))$  for nonnegative normalized kernels, giving a limitation for every choice of scale in the fixed-kernel scalar capacity method with full difference sums under a unit-slope hypothesis. For the Hou–Zhao covering certificates the limit  $2\sqrt{2}/3$  was proved independently, one day before the first version of this note, by J. Akwei; see Section 8.6. Reported coefficients run from Lindström’s 1 through Hou–Zhao’s 0.94349 ... to unrefereed repository claims near 0.94324, 0.94301 and 0.94280952; the present coefficient is 0.942809 ... Erdős’s conjecture  $F(N) = \sqrt{N} + O_\varepsilon(N^\varepsilon)$  for every  $\varepsilon > 0$  remains untouched.

*Keywords:* Sidon sets; distinct differences; finite energy; explicit bounds; boundary correction.

## 1 Introduction

A Sidon set of integers has distinct unordered two-term sums, including sums in which the two summands agree. Write  $F(N)$  for the largest cardinality of such a set in  $\{1, \dots, N\}$ . Translation gives the same maximum on  $\{0, \dots, N-1\}$ . The problem of bounding  $F(N)$  goes back to Erdős and Turán [ET41], who proved  $F(N) \leq \sqrt{N} + O(N^{1/4})$ . Lindström [Lind69] gave the explicit bound  $F(N) < \sqrt{N} + N^{1/4} + 1$ , valid for every positive integer  $N$ . Cilleruelo [Cil10] reduced its additive constant to  $1/2$ . The reproductions and proofs in Balogh–Füredi–Roy [BFR23] also record these two explicit statements.

Table 1 gives a source-qualified progression of second-order coefficients at the scale  $\sqrt{N} + cN^{1/4}$ . Where a source states a uniform  $O(1)$  remainder or a stronger form, the table indicates it; no additional remainder assertion is assigned here to an announcement. A coefficient with an unspecified  $O(1)$  is not a printed numerical pair of additive constant and onset. Publication years and preprint years are listed separately when they differ. The table includes unrefereed announcements and repository claims as such, and does not certify their computational certificates.

Carter–Hunter–O’Bryant [CHO25] state a diameter bound  $k^2 - 1.96365k^3/2 - O(k)$  for a  $k$ -element Sidon set, yielding the safe cardinality coefficient 0.98183 in the table. The 2025 collaboration of Carter, Georgiev, Gómez-Serrano, Hunter, O’Bryant, Tao and Wagner reported a diameter coefficient 1.9526463099204112; half that value explains the rounded safe entry 0.97633 [AE25]. These comparisons concern asymptotic coefficients: the difference between diameter  $N-1$  and interval parameter  $N$  does not affect that coefficient, but must be retained when asserting a specified additive constant.

The present note gives a complete proof with the numerical additive constant and onset printed in the theorem. It uses the autocorrelation of a decreasing linear weight. An exact correction on a half-line has excess mass  $1/3$ ; joining two copies gives the boundary term  $2/3$ . A quantitative elementary contraction controls the tails. The auxiliary measure on a finite interval is signed, which is permitted because the energy comparison is an  $L^2$  Cauchy–Schwarz inequality. No theorem about renewal processes is needed.

Theorem 8.1 proves the sharp bound  $\liminf_{L \rightarrow \infty} (C_f(L) - L) \geq 8/(9f(0))$  without assuming that a finite capacity intercept exists; the ramp attains equality. The proof uses nonnegative boundary trials and an exact weak-derivative certificate, permitting signed autocorrelation factors and unbounded support. Under the separate unit-slope condition, the scalar method using the full difference sum cannot improve its second-order coefficient by any choice of scale. This does not limit all weighted Erdős–Turán arguments or resolve the original conjecture.[^1]

| Source                                     | Coefficient $c$      | Form and status                                                                                                                                           |
|--------------------------------------------|----------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------|
| Erdős–Turán (1941) [ET41]                  | unspecified          | $O(N^{1/4})$ ; journal article                                                                                                                            |
| Lindström (1969) [Lind69]                  | 1                    | additive +1, every $N \geq 1$ ; journal article                                                                                                           |
| Cilleruelo (2010) [Cil10]                  | 1                    | additive +1/2, every $N \geq 1$ ; journal article                                                                                                         |
| Balogh–Füredi–Roy (2021/2023) [BFR23]      | 0.998                | no additive term for all sufficiently large $N$ ; journal article                                                                                         |
| O’Bryant (2022/2024) [OB24]                | 0.99703              | no additive term for all sufficiently large $N$ ; journal article                                                                                         |
| Carter–Hunter–O’Bryant (2023/2025) [CHO25] | 0.98183              | $O(1)$ remainder; journal article                                                                                                                         |
| AlphaEvolve collaboration (2025) [AE25]    | 0.97633              | rounded safe coefficient; unrefereed announcement                                                                                                         |
| Hou–Zhao v1 (July 2026) [HZ26]             | 0.9460052 . . .      | $O(1)$ remainder; preprint                                                                                                                                |
| Hou–Zhao v3 (September 2026) [HZ26]        | 0.9434925907 . . .   | $O(1)$ remainder; preprint                                                                                                                                |
| JoshMadeiros (August 2026) [Josh26]        | $\approx 0.94324445$ | $c < 0.94325$ ; $O(1)$ ; unrefereed forum claim                                                                                                           |
| Wu, q1 (August 2026) [Wu26]                | $\approx 0.94324253$ | $c < 0.94325$ ; $O(1)$ ; unrefereed repository claim                                                                                                      |
| Wu, q2 (August 2026) [Wu26]                | $\approx 0.94300617$ | $c < 0.94301$ ; $O(1)$ ; unrefereed repository claim                                                                                                      |
| Akwei (October 2026) [Akw26a]              | $\approx 0.94280952$ | $\gamma < 0.942809522$ ; $O(1)$ , no explicit onset; unrefereed repository claim; proves $\gamma \geq 2\sqrt{2}/3$ for all Hou–Zhao covering certificates |
| This note                                  | $2\sqrt{2}/3$        | additive +1 for every $N \geq 4600\,000$ ( $N \geq 120^4$ in v1–v2); kernel-checked in Lean; review status below                                          |

Table 1: Selected coefficient history. The initial date is the preprint or announcement date when a later journal date is also displayed. Decimal entries retain the scope and status of their cited sources.

Erdős’s conjecture asks for  $F(N) = \sqrt{N} + O_\varepsilon(N^\varepsilon)$  for every  $\varepsilon > 0$ ; see the problem record [EP30]. The estimate proved here retains the exponent  $1/4$  and does not resolve that conjecture. The source comparison above makes no claim that the displayed list is exhaustive or that the method has a universal optimality barrier.

## 2 Statement

A finite set of integers  $A$  is a **Sidon set** if the map

$$\{(a, b) \in A^2 : a \leq b\} \longrightarrow \mathbb{Z}, \quad (a, b) \longmapsto a + b$$

is injective. In particular, the pairs  $(a, a)$  are included: equality  $a + b = c + d$ , with  $a \leq b$  and  $c \leq d$ , requires  $a = c$  and  $b = d$ .

**Theorem 2.1.** *For every integer  $N \geq 4600\,000$  and every Sidon set  $A \subseteq \{1, \dots, N\}$ ,*

$$|A| \leq \sqrt{N} + \frac{2\sqrt{2}}{3} N^{1/4} + 1. \quad (2.1)$$

All powers and square roots in this document are positive real ones. In particular, there is no requirement that  $N$  be a fourth power. The onset is 4600 000; versions 1 and 2 of this note used the convenience onset 207 360 000 = 120<sup>4</sup>.

**Lemma 2.2** (equivalent difference convention). *The Sidon condition is equivalent to*

$$a - b = c - d \neq 0, \quad a, b, c, d \in A \implies (a, b) = (c, d). \quad (2.2)$$

*Here the differences are indexed by ordered pairs, and zero differences are excluded. Equivalently, each positive integer is the difference  $a - b$ , with  $a, b \in A$  and  $a > b$ , at most once.*

*Proof.* Suppose first that pair sums, including diagonal sums, are unique. The equality  $a - b = c - d \neq 0$  gives  $a + d = c + b$ . Equality of the two unordered pairs with multiplicities gives either  $a = c, d = b$ , as required, or  $a = b, d = c$ . The latter possibility contradicts the nonzero difference.

Conversely, suppose (2.2) holds, and let  $a + b = c + d$ . If  $a = c$ , then  $b = d$ . Otherwise  $a - c = d - b \neq 0$ , so (2.2), applied to the ordered pairs  $(a, c)$  and  $(d, b)$ , gives  $a = d, c = b$ . Thus the unordered pairs with multiplicities agree. Restricting both pairs to increasing order proves the stated Sidon condition, including when a pair is diagonal. Finally, a negative difference becomes a positive one on reversing both ordered pairs; hence uniqueness of positive differences is equivalent to (2.2).  $\square$ 

Translation preserves these conditions. We may consequently replace  $A$  by  $A - 1 \subseteq \{0, \dots, N - 1\}$  when proving (2.1).

### 3 Kernel and energy

Lebesgue measure on the real line is denoted by  $dt$ . For an integrable function  $v$  and a measure  $\mu$ , write

$$(v * \mu)(x) = \int v(x - t) d\mu(t)$$

whenever the integral exists. A finite signed real measure means one with finite total variation  $\|\mu\|_{\text{TV}} = |\mu|(\mathbb{R})$ .

Set

$$h(t) = 2(1 - t)\mathbf{1}_{[0,1]}(t), \quad \tilde{h}(t) = h(-t), \quad f = h * \tilde{h}. \quad (3.1)$$

The specified value  $h(0) = 2$  will be convenient in a pointwise identity.

**Lemma 3.1** (kernel and Cauchy inequality). *The function  $f$  is even and*

$$f(x) = \begin{cases} \frac{4}{3} - 2|x| + \frac{2}{3}|x|^3, & |x| \leq 1, \\ 0, & |x| > 1. \end{cases} \quad (3.2)$$

*It is nonnegative, nonincreasing on  $[0, \infty)$ , and satisfies*

$$f(0) = \|h\|_2^2 = \frac{4}{3}, \quad \int_{\mathbb{R}} h(t) dt = 1, \quad \int_{\mathbb{R}} f(t) dt = 1. \quad (3.3)$$

*For finite signed real measures define*

$$E(\mu, \nu) = \iint f(x - y) d\mu(x) d\nu(y).$$

*Then*

$$E(\mu, \nu) = \int_{\mathbb{R}} (h * \mu)(t)(h * \nu)(t) dt, \quad E(\mu, \mu) \geq 0, \quad (3.4)$$

*and*

$$|E(\mu, \nu)|^2 \leq E(\mu, \mu)E(\nu, \nu). \quad (3.5)$$

*Proof.* The autocorrelation is even by a change of variable. For  $0 \leq x \leq 1$ , its value is

$$4 \int_0^{1-x} (1-s-x)(1-s) ds = \frac{4}{3} - 2x + \frac{2}{3}x^3;$$

for  $x > 1$  the two supports have no overlap of positive length. This proves (3.2). Nonnegativity also follows directly from the integral of the two nonnegative factors. On  $[0, 1]$  the derivative is  $-2 + 2x^2 \leq 0$ , and outside this interval the function is zero. Integrating  $h$  and  $h^2$  gives (3.3); the mass of  $f$  is  $(\int h)^2 = 1$  by Tonelli's theorem.

For any finite signed measure, Cauchy–Schwarz with respect to  $|\mu|$  gives

$$\int |h * \mu|^2 \leq \|\mu\|_{\text{TV}} \int \int |h(t-x)|^2 d|\mu|(x) dt = \|\mu\|_{\text{TV}}^2 \|h\|_2^2.$$

Thus  $h * \mu \in L^2$ . Moreover,  $\int |h(t-x)h(t-y)| dt \leq \|h\|_2^2$ , so the corresponding triple integral against  $|\mu|$  and  $|\nu|$  is finite. Fubini's theorem is therefore applicable. Its inner integral is  $f(x-y)$ , which proves (3.4). Applying the usual Cauchy–Schwarz inequality in real  $L^2$  proves (3.5). This argument allows either measure to be signed.  $\square$ 

## 4 The half-line correction

Let  $U$  be the probability measure with density  $v_1 = \mathbf{1}_{[0,1)}$ , and let  $U^{*0} = \delta_0$ . Define

$$g_+ = \frac{1}{2} \sum_{n=0}^{\infty} U^{*n}. \quad (4.1)$$

The following construction proves everything needed about this measure; no renewal theorem is used.

**Lemma 4.1** (local finiteness and exact potential). *The measure  $g_+$  is locally finite, supported on  $[0, \infty)$ , and*

$$h * g_+ = \mathbf{1}_{[0, \infty)}, \quad (f * g_+)(x) = 1 \quad (x \geq 0). \quad (4.2)$$

*Proof.* For  $n \geq 1$ , let  $v_n$  be the density of  $U^{*n}$ . Convolution gives representatives satisfying, for  $t \geq 0$ ,

$$0 \leq v_n(t) \leq \frac{t^{n-1}}{(n-1)!}. \quad (4.3)$$

For  $n = 1$  this is the bound  $v_1 \leq 1$ . If it holds at  $n$ , then

$$v_{n+1}(t) = \int_0^{\min(1, t)} v_n(t-s) ds \leq \int_0^t \frac{(t-s)^{n-1}}{(n-1)!} ds = \frac{t^n}{n!}.$$

For every fixed  $R \geq 0$ , it follows that  $U^{*n}([0, R]) \leq R^n/n!$ . The sum in (4.1) consequently has finite mass on every bounded interval.

For a direct proof of the first identity in (4.2), put  $H = \mathbf{1}_{[0, \infty)}$ . The definitions give the pointwise identity  $h/2 = H - U * H$ . Thus each finite partial sum telescopes:

$$\frac{1}{2} \sum_{n=0}^m h * U^{*n} = H - U^{*(m+1)} * H. \quad (4.4)$$

For  $t \geq 0$ , the last term on the right is between zero and  $t^{m+1}/(m+1)!$ , by (4.3), and this tends to zero. For  $t < 0$ , both sides vanish. The nonnegative partial sums on the left converge to  $h * g_+$ , proving the identity. This also fixes its value at  $t = 0$ .

Tonelli's theorem allows association of the nonnegative convolutions. For  $x \geq 0$ ,

$$(f * g_+)(x) = (\tilde{h} * (h * g_+))(x) = \int_{-1}^0 \tilde{h}(y) H(x-y) dy = \int_{-1}^0 \tilde{h}(y) dy = 1.$$

Write

$$g_+ = \frac{1}{2}\delta_0 + \frac{1}{2}u(t)\mathbf{1}_{[0,\infty)}(t) dt, \quad u(t) = \sum_{n=1}^{\infty} v_n(t) \quad (t \geq 0). \quad (4.5)$$

Use the right-continuous representative of  $u$ . In particular,

$$u(0) = 1, \quad u(t) = e^t \quad (0 \leq t < 1), \quad u(1) = e - 1. \quad (4.6)$$

The left limit at 1 is  $e$ , and must not be substituted for  $u(1)$  in the recurrence below. To justify these regularity claims, the series in (4.5) converges uniformly on compact intervals by (4.3). For  $n \geq 2$ , the density  $v_n(t) = \int_{t-1}^t v_{n-1}(s) ds$ , with densities set to zero for  $s < 0$ , is continuous. Only  $v_1$  has a jump at 1. For  $0 \leq t < 1$ , the induction proving (4.3) gives equality. At  $t = 1$ ,  $v_1(1) = 0$  and  $v_n(1) = 1/(n-1)!$  for  $n \geq 2$ . These observations prove (4.6) and the stated representative convention.

**Lemma 4.2** (quantitative convergence of the density). *For almost every  $t \geq 0$ ,*

$$|u(t) - 2| \leq (e-1)(3/4)^{\lfloor t \rfloor} < 2(3/4)^{\lfloor t \rfloor}. \quad (4.7)$$

*Proof.* Summing the convolution recurrence for the densities yields  $u = v_1 + U * u$ . Thus

$$u(t) = \int_{t-1}^t u(s) ds \quad (t \geq 1). \quad (4.8)$$

This includes  $t = 1$  with the right-continuous value in (4.6). On  $(1, \infty)$ , this identity makes  $u$  locally absolutely continuous, and  $u'(t) = u(t) - u(t-1)$  almost everywhere. Fix an integer  $n \geq 1$ . Solving this first-order equation on  $[n, n+1]$  gives

$$u(n+x) = e^x u(n) - \int_0^x e^{x-y} u(n-1+y) dy \quad (0 \leq x \leq 1).$$

Since  $u(n) = \int_0^1 u(n-1+y) dy$ , this becomes

$$u(n+x) = \int_0^1 K_x(y) u(n-1+y) dy, \quad K_x(y) = e^x - \mathbf{1}_{\{y \leq x\}} e^{x-y}. \quad (4.9)$$

For  $0 \leq x, y \leq 1$ , the kernel is nonnegative, and

$$\int_0^1 K_x(y) dy = e^x - \int_0^x e^{x-y} dy = 1.$$

For  $y \in [1/2, 1]$ , it also satisfies  $K_x(y) \geq 1/2$ . Indeed, if  $y > x$ , its value is  $e^x \geq 1$ . If  $y \leq x$ , its value is  $e^{x-y} (e^y - 1) \geq e^{1/2} - 1 > 1/2$ , using the exponential series.

Let  $[m_n, M_n]$  be the smallest closed interval containing the essential range of  $u$  on  $[n, n+1)$ . Here essential extrema ignore sets of Lebesgue measure zero. Initially  $[m_0, M_0] = [1, e]$ . Equation (4.9) first implies that these closed intervals are nested. For the width estimate, every  $K_x(y) dy$  contains the common measure

$$w(y) dy = \frac{1}{2} \mathbf{1}_{[1/2, 1]}(y) dy$$

of mass  $1/4$ . Put  $c_n = \int_0^1 w(y) u(n-1+y) dy$ . The remaining nonnegative measure has mass  $3/4$ , so every value in (4.9) lies between  $c_n + (3/4)m_{n-1}$  and  $c_n + (3/4)M_{n-1}$ . Consequently,

$$[m_n, M_n] \subseteq [m_{n-1}, M_{n-1}], \quad M_n - m_n \leq \frac{3}{4}(M_{n-1} - m_{n-1}).$$

The nested closed intervals therefore meet in a single real number  $c$ , and

$$|u(t) - c| \leq (e-1)(3/4)^{\lfloor t \rfloor} \quad (4.10)$$

For  $t > 1$ , the atom in (4.5) contributes nothing to  $h * g_+(t)$ , so Lemma 4.1 gives

$$1 = \frac{1}{2} \int_0^1 h(s) u(t-s) ds.$$

Letting  $t \rightarrow \infty$  in this integral, (4.10) and  $\int h = 1$  imply  $1 = c/2$ . Thus  $c = 2$ . Finally,  $e < 3$ : in its series  $e = 2 + \sum_{j \geq 2} 1/j!$ , the tail is strictly smaller than  $\sum_{j \geq 2} 2^{-(j-1)} = 1$ . This proves (4.7).  $\square$ 

**Lemma 4.3** (size, tail, and mass of the correction). *Define the signed measure supported on  $[0, \infty)$* 

$$q = g_+ - \mathbf{1}_{[0, \infty)}(t) dt = \frac{1}{2} \delta_0 + r(t) \mathbf{1}_{[0, \infty)}(t) dt, \quad r(t) = \frac{1}{2} u(t) - 1. \quad (4.11)$$

*It is a finite signed measure, and, with  $\alpha = \log(4/3)$ ,*

$$|r(t)| \leq (3/4)^{\lfloor t \rfloor} \quad \text{almost everywhere,} \quad \|q\|_{\text{TV}} \leq \frac{9}{2}, \quad (4.12)$$

$$|q|((L, \infty)) \leq 6e^{-\alpha L} \quad (L \geq 1), \quad (4.13)$$

and

$$q(\mathbb{R}) = \frac{1}{3}. \quad (4.14)$$

*Proof.* The first bound follows from Lemma 4.2. Integration on unit intervals then gives

$$\|q\|_{\text{TV}} \leq \frac{1}{2} + \sum_{n=0}^{\infty} (3/4)^n = \frac{9}{2}.$$

For  $L \geq 1$ , the atom at zero is outside  $(L, \infty)$ , and

$$|q|((L, \infty)) \leq \sum_{n=\lfloor L \rfloor}^{\infty} (3/4)^n = 4(3/4)^{\lfloor L \rfloor} \leq \frac{16}{3} e^{-\alpha L} \leq 6e^{-\alpha L}.$$

It remains to compute the signed mass, not just its absolute bound. For  $s > 0$ , Tonelli's theorem and the product rule for Laplace transforms of nonnegative convolutions give

$$\begin{aligned} \int e^{-st} dg_+(t) &= \frac{1}{2} \sum_{n=0}^{\infty} \left( \int_0^1 e^{-st} dt \right)^n \\ &= \frac{1}{2(1 - (1 - e^{-s})/s)}. \end{aligned} \quad (4.15)$$

The geometric series converges since  $0 < \int_0^1 e^{-st} dt < 1$ . Taylor's formula for the exponential, as  $s \downarrow 0$ , gives

$$\phi(s) := 1 - \frac{1 - e^{-s}}{s} = \frac{s}{2} - \frac{s^2}{6} + O(s^3).$$

This use of  $O(s^3)$  concerns only a limit: for  $0 < s \leq 1$ , Taylor's remainder after the cubic term of  $e^{-s}$  has absolute value at most  $s^4/24$ , which supplies the displayed bound directly. Subtracting the Laplace transform  $1/s$  of half-line Lebesgue measure gives

$$\int e^{-st} dq(t) = \frac{1}{2\phi(s)} - \frac{1}{s} = \frac{s - 2\phi(s)}{2s\phi(s)} \rightarrow \frac{1}{3}.$$

Because  $q$  has finite total variation and is supported on the nonnegative half-line,  $|e^{-st}| \leq 1$  there. Dominated convergence for the finite measure  $|q|$  shows that the limit is  $q(\mathbb{R})$ , proving (4.14).  $\square$ 

#### 4.1 Joining two half-lines

**Lemma 4.4** (finite-interval energy bound). *Let  $L \geq 1$ , and let  $\mu$  be any finite positive measure supported on the closed interval  $[0, L]$ . If  $k = \mu(\mathbb{R})$ , then*

$$E(\mu, \mu) \geq \frac{k^2}{L + \frac{2}{3} + 200e^{-\alpha L}}, \quad \alpha = \log(4/3). \quad (4.16)$$

*Proof.* Let  $q_L$  be the pushforward of  $q$  by the reflection  $t \mapsto L - t$ , and set

$$\nu_L = \mathbf{1}_{[0, L]}(t) dt + q + q_L. \quad (4.17)$$

This is a finite signed real measure, with

$$\nu_L(\mathbb{R}) = L + \frac{2}{3}. \quad (4.18)$$

Let  $g_-^L$  denote the same reflection of  $g_+$ . As locally finite measures,

$$\nu_L = g_+ + g_-^L - dt. \quad (4.19)$$

Indeed, the two half-line Lebesgue measures sum to full-line Lebesgue measure plus Lebesgue measure on  $[0, L]$ ; endpoints do not change those Lebesgue measures. The atoms of  $q$  at 0 and of  $q_L$  at  $L$  remain included in (4.17). Since  $f$  is compactly supported, (4.19) may be convolved locally with  $f$ . Lemma 4.1 and evenness of  $f$  give, for  $0 \leq x \leq L$ ,

$$V_L(x) := (f * \nu_L)(x) = 1 + 1 - \int f = 1. \quad (4.20)$$

This holds also at both endpoints. For every real  $x$ , nonnegativity and mass one of  $f$ , together with Lemma 4.3, imply

$$|V_L(x)| \leq 1 + \|f\|_\infty (\|q\|_{\text{TV}} + \|q_L\|_{\text{TV}}) \leq 1 + \frac{4}{3} \cdot 9 = 13. \quad (4.21)$$

Outside  $[0, L]$ , the only measure in (4.17) on  $(L, \infty)$  is the tail of  $q$ ; on  $(-\infty, 0)$  it is the reflection of the same tail. In particular there are no excluded endpoint atoms. Thus (4.13) gives

$$|\nu_L|(\mathbb{R} \setminus [0, L]) \leq 12e^{-\alpha L}.$$

By (4.18), (4.20), and (4.21),

$$\begin{aligned} \left| E(\nu_L, \nu_L) - \left( L + \frac{2}{3} \right) \right| &= \left| \int_{\mathbb{R} \setminus [0, L]} (V_L(x) - 1) d\nu_L(x) \right| \\ &\leq 14 \cdot 12e^{-\alpha L} = 168e^{-\alpha L} \leq 200e^{-\alpha L}. \end{aligned} \quad (4.22)$$

Also  $E(\mu, \nu_L) = \int V_L d\mu = k$ . Lemma 3.1 now gives

$$k^2 \leq E(\mu, \mu) E(\nu_L, \nu_L) \leq E(\mu, \mu) \left( L + \frac{2}{3} + 200e^{-\alpha L} \right).$$

The denominator is positive and  $E(\mu, \mu) \geq 0$ , proving (4.16). There is no assumption that  $\nu_L$  is positive.  $\square$ 

## 5 The discrete inequality

**Lemma 5.1** (Sidon energy upper bound). *For every integer  $N \geq 1$ , every Sidon set  $A \subseteq \{0, \dots, N-1\}$ , and every real  $0 < T \leq N$ , writing  $k = |A|$  gives*

$$\boxed{k^2 \leq \left( \frac{N}{T} + \frac{2}{3} + 200e^{-\alpha N/T} \right) \left( T + \frac{4}{3} k \right)}. \quad (5.1)$$

*Proof.* Put  $L = N/T \geq 1$  and  $\mu = \sum_{a \in A} \delta_{a/T}$ . Its mass is  $k$ , and its support lies in  $[0, L]$ . In fact its right endpoint is at most  $(N-1)/T$ ; using the larger interval of length  $N/T$  is permitted in Lemma 4.4.

Let  $D_+(A)$  denote the set of positive differences of elements of  $A$ . Lemma 2.2 says that each such difference occurs for exactly one ordered pair. The zero differences are precisely the  $k$  diagonal ordered pairs. Evenness of  $f$  therefore gives the exact identity

$$E(\mu, \mu) = \frac{4}{3}k + 2 \sum_{d \in D_+(A)} f(d/T) \leq \frac{4}{3}k + 2 \sum_{d=1}^{\infty} f(d/T). \quad (5.2)$$

The inequality uses nonnegativity of  $f$ . For every integer  $d \geq 1$ , monotonicity on the positive half-line implies

$$f(d/T) \leq T \int_{(d-1)/T}^{d/T} f(s) ds.$$

Summing, and using evenness and  $\int f = 1$ , yields

$$\sum_{d=1}^{\infty} f(d/T) \leq T \int_0^{\infty} f(s) ds = \frac{T}{2}.$$

Only finitely many summands can be nonzero. It follows that  $E(\mu, \mu) \leq T + 4k/3$ . Combining this with (4.16) proves (5.1). This proof applies also to the empty set and to singleton sets.  $\square$ 

## 6 Explicit constants and onset

*Proof of Theorem 2.1.* Put  $N_1 = 4600\,000$  and  $x_1 = N_1^{1/4}$ . Let  $N \geq N_1$  be an integer and let  $A \subseteq \{0, \dots, N-1\}$  be a Sidon set. Write  $k = |A|$ . Set

$$x = N^{1/4}, \quad T = \sqrt{2}x^3, \quad \gamma = \frac{2\sqrt{2}}{3}, \quad \alpha = \log(4/3), \quad \varepsilon = 200e^{-\alpha x/\sqrt{2}}. \quad (6.1)$$

The estimates below hold, in fact, for every real  $x \geq x_1$ , regardless of whether  $x^4$  is integral. Put  $s = \sqrt{2}$ ,  $\beta = \alpha/s$ , and  $u = 463/10$ . Since  $463^4 = 45\,954\,068\,161 < 46\,000\,000\,000 = 10^4 N_1$ , we have  $x \geq x_1 > u > 46 > 2 > s > 0$ . Here  $u > 46$  follows from  $463 > 460$ , and  $2 > s$  follows from  $2 < 4 = 2^2$ . Consequently  $L = N/T = x/s > 1$  and  $0 < T < N$ . Thus the interval parameter in Lemma 5.1 is admissible.

Expanding Lemma 5.1 gives  $P_\varepsilon(k) \leq 0$ , where

$$P_\varepsilon(z) = z^2 - \left( \gamma x + \frac{8}{9} + \frac{4}{3}\varepsilon \right) z - x^4 - \gamma x^3 - \sqrt{2}\varepsilon x^3. \quad (6.2)$$

Indeed,  $(4/3)(x/s + 2/3 + \varepsilon) = \gamma x + 8/9 + (4/3)\varepsilon$ , and  $(x/s + 2/3 + \varepsilon)sx^3 = x^4 + \gamma x^3 + s\varepsilon x^3$ .

Here are exact elementary bounds for the exponential. Substitution in the logarithm integral gives

$$\alpha = 2 \int_0^{1/7} \frac{dt}{1-t^2} > 2 \left( \frac{1}{7} + \frac{1}{3 \cdot 7^3} \right) = \frac{296}{1029} > \frac{719}{2500}.$$

The first strict inequality follows from  $1/(1-t^2) > 1 + t^2$  for  $0 < t \leq 1/7$ . The last comparison is  $740\,000 > 739\,851$ . Also  $s < 99/70$ , since  $99^2 = 9801 > 9800 = 2 \cdot 70^2$ . Therefore

$$\beta u > \frac{719}{2500} \cdot \frac{463}{10} \cdot \frac{70}{99} > \frac{941}{100} > 1. \quad (6.3)$$

The middle comparison is exactly  $2\,330\,279\,000 > 2\,328\,975\,000$ , obtained by multiplying the positive denominators; the last is  $941 > 100$ .

The positive-term exponential series yields

$$e^3 > \sum_{j=0}^9 \frac{3^j}{j!} = \frac{22471}{1120} > \frac{1003}{50}, \quad e^{41/100} > \sum_{j=0}^3 \frac{(41/100)^j}{j!} = \frac{9033221}{6000000} > \frac{3}{2}.$$

$$e^{\beta u} > e^{941/100} = (e^3)^3 e^{41/100} > \frac{3 \cdot 1003^3}{2 \cdot 50^3} > 12100, \quad 200e^{-\beta u} < \frac{2}{121}. \quad (6.4)$$

The penultimate comparison is exactly  $3 \cdot 027 \cdot 081 \cdot 081 > 3 \cdot 025 \cdot 000 \cdot 000$ .

Put  $y = x^2 + \gamma x + 1$ . Since  $\gamma^2 = 8/9$ , direct expansion gives

$$P_0(y) = \frac{10}{9}x^2 + \frac{\gamma}{9}x + \frac{1}{9} \geq x^2. \quad (6.5)$$

We retain the full leading term  $(10/9)x^2$  in what follows. In particular  $P_0(y) \geq (10/9)x^2$ . Also  $0 < \gamma < 1$ , because  $0 < \gamma^2 = 8/9 < 1$ .

Normalize the error by  $x^2$ :

$$\Phi(x) := \frac{\varepsilon((4/3)y + sx^3)}{x^2} = 200e^{-\beta x} \left( sx + \frac{4}{3} + \frac{4\gamma}{3x} + \frac{4}{3x^2} \right).$$

This function is strictly decreasing on  $[u, \infty)$ . To see this without any estimate on an unspecified remainder, its four summands are positive constant multiples of  $xe^{-\beta x}$ ,  $e^{-\beta x}$ ,  $x^{-1}e^{-\beta x}$ , and  $x^{-2}e^{-\beta x}$ . The derivative of the first is  $e^{-\beta x}(1 - \beta x) < 0$ , by (6.3). For  $j = 0, 1, 2$ , the derivative of  $x^{-j}e^{-\beta x}$  is  $-e^{-\beta x}(jx^{-j-1} + \beta x^{-j}) < 0$ .

At the rational endpoint  $u$ ,

$$su < \frac{99}{70} \cdot \frac{463}{10} = \frac{45837}{700} < \frac{131}{2}, \quad \frac{4}{3} \left( 1 + \frac{\gamma}{u} + \frac{1}{u^2} \right) < \frac{4}{3} \left( 1 + \frac{1}{46} + \frac{1}{46^2} \right) = \frac{721}{529} < \frac{3}{2}.$$

These comparisons are  $45837 < 45850$ ,  $463 > 460$ , and  $1442 < 1587$ . Combining them with (6.4) gives, uniformly for  $x \geq x_1 > u$ ,

$$\Phi(x) \leq \Phi(u) < \frac{2}{121} \left( \frac{131}{2} + \frac{3}{2} \right) = \frac{134}{121}. \quad (6.6)$$

Finally, (6.2), (6.5), and (6.6) give

$$\begin{aligned} P_\varepsilon(y) &= P_0(y) - \varepsilon \left( \frac{4}{3}y + sx^3 \right) \\ &> \left( \frac{10}{9} - \frac{134}{121} \right) x^2 = \frac{4}{1089}x^2 > 0. \end{aligned} \quad (6.7)$$

Here  $10 \cdot 121 - 134 \cdot 9 = 1210 - 1206 = 4 > 0$ . This proves  $P_\varepsilon(y) > 0$  for every real  $x \geq x_1$ .

The quadratic  $P_\varepsilon$  has leading coefficient 1 and strictly negative constant term. Its discriminant is positive, and its two roots have negative product, so precisely one root is positive. Since  $k \geq 0$  and  $P_\varepsilon(k) \leq 0$ ,  $k$  is at most that positive root. Since  $y > 0$  and  $P_\varepsilon(y) > 0$ , the positive root is strictly smaller than  $y$ . Consequently

$$k < x^2 + \gamma x + 1 = \sqrt{N} + \frac{2\sqrt{2}}{3}N^{1/4} + 1.$$

Translation from  $A \subseteq \{1, \dots, N\}$  to  $A - 1 \subseteq \{0, \dots, N - 1\}$  preserves the given Sidon condition, as in Section 2. This proves (2.1), and indeed its strict version, for every integer  $N \geq 4600 \cdot 000$ . The root argument also includes  $k = 0$ .  $\square$ 

*Remark 6.1* (version history of the onset). Versions 1 and 2 of this note (2 October 2026) proved Theorem 2.1 with the convenience onset  $N_0 = 120^4 = 207 \cdot 360 \cdot 000$ : they replaced  $\alpha/\sqrt{2}$  by  $1/6$  and absorbed the error through the envelope  $\varepsilon x < 1/32$ , which needs  $x \geq 120$ . The present section (version 3) keeps Lemma 5.1 and the identities (6.2), (6.5) unchanged and replaces only the numerical absorption; the earlier argument remains valid on its own range, which is contained in the range of this one. The onset  $4600 \cdot 000$  is not claimed minimal; see Remark 9.1.

## 7 Where $2\sqrt{2}/3$ comes from

Two exact constants determine this coefficient in the retained scalar energy inequality:

$$a = f(0) = \frac{4}{3}, \quad b = 2q(\mathbb{R}) = \frac{2}{3}. \quad (7.1)$$

The first is the diagonal cost per point in (5.2). The second is the sum of the two half-line excess masses in (4.18). Apart from the explicitly controlled exponential error, (5.1) has right side

$$\left(\frac{N}{T} + b\right)(T + ak) = N + bT + \frac{aNk}{T} + abk. \quad (7.2)$$

To read its second-order scale, put  $N = x^4$ ,  $T = tx^3$  for a fixed  $t > 0$ , and  $k = x^2 + cx + O(1)$ . The terms of order  $x^3$  in the two sides of the inequality are respectively  $2cx^3$  and  $(bt + a/t)x^3$ . The resulting upper coefficient is

$$c(t) = \frac{1}{2} \left(bt + \frac{a}{t}\right) = \frac{t}{3} + \frac{2}{3t}. \quad (7.3)$$

For  $t > 0$ ,

$$bt + \frac{a}{t} - 2\sqrt{ab} = \left(\sqrt{bt} - \sqrt{a/t}\right)^2 \geq 0.$$

Thus the minimum in (7.3) is  $\sqrt{ab} = 2\sqrt{2}/3$ , attained precisely at  $t = \sqrt{a/b} = \sqrt{2}$ . This gives the scale chosen in (6.1). For fixed  $t$ , the exponential term has argument  $-\alpha x/t$ , so it contributes no term at this order; Section 6 supplies its fully effective treatment for the selected  $t$ .

A precise limitation statement is also possible. It concerns **only the scalar inequalities** (5.1), **with this kernel and these retained energy estimates**. It does not concern all arguments using this kernel, all boundary corrections, or all Sidon methods.

To prove this limited statement, for each  $N > 0$  let  $\kappa_N > 0$  be the solution of

$$\kappa_N = \sqrt{N} + \sqrt{ab\kappa_N}. \quad (7.4)$$

Writing  $x = N^{1/4}$  and  $\gamma = \sqrt{ab}$  gives explicitly

$$\kappa_N = \left(\frac{\gamma + \sqrt{\gamma^2 + 4x^2}}{2}\right)^2 = x^2 + \gamma\sqrt{x^2 + \gamma^2/4} + \frac{\gamma^2}{2}. \quad (7.5)$$

For every  $T > 0$ , the elementary square inequality gives

$$bT + \frac{aN\kappa_N}{T} \geq 2\sqrt{abN\kappa_N}.$$

Consequently,

$$\begin{aligned} \left(\frac{N}{T} + b\right)(T + a\kappa_N) &\geq N + 2\sqrt{abN\kappa_N} + ab\kappa_N \\ &= \left(\sqrt{N} + \sqrt{ab\kappa_N}\right)^2 = \kappa_N^2. \end{aligned} \quad (7.6)$$

Equality occurs at  $T = \sqrt{aN\kappa_N/b}$ . In particular,  $\kappa_N$  satisfies the entire collection of these scalar inequalities simultaneously, even if one allows every  $T > 0$  and removes the nonnegative exponential error. It therefore also satisfies (5.1) for every allowed  $0 < T \leq N$ .

Formula (7.5) gives the exact remainder identity

$$\kappa_N - x^2 - \gamma x = \frac{\gamma^2}{2} + \frac{\gamma^3}{4(\sqrt{x^2 + \gamma^2/4} + x)}. \quad (7.7)$$

Thus  $\kappa_N = x^2 + \gamma x + O(1)$ . Even imposing integrality on a scalar  $k$  does not change this leading limitation: for each fixed  $T$ , the inequality in  $k$  is a monic quadratic inequality with negative constant term, so it holds on the full interval from zero to its positive root. It therefore holds at  $\lfloor \kappa_N \rfloor$ , simultaneously for all  $T$ , including with the exponential error restored. These integers still equal  $x^2 + \gamma x + O(1)$ . For large  $N$  they also lie between 0 and  $N$ .

It follows that these scalar inequalities alone cannot imply  $k \leq \sqrt{N} + cN^{1/4} + C$  for any fixed  $c < \gamma$  and fixed  $C$ : the admissible scalar values  $\lfloor \kappa_N \rfloor$  eventually violate that conclusion. These are scalar comparison values, **not constructed Sidon sets**. Improving an earlier estimate, retaining more information about the differences, or choosing another kernel lies outside this limitation statement. No general method barrier is claimed.

## 8 Optimality of the constant within the fixed-kernel capacity method

Here  $f$  continues to denote the ramp autocorrelation in (3.2); a general kernel is denoted by  $\varphi$ . Let  $C_0(\mathbb{R})$  denote the continuous functions tending to zero at infinity. For an even nonnegative kernel  $\varphi \in C_0(\mathbb{R}) \cap L^1(\mathbb{R})$  with  $\int \varphi = 1$  and  $a = \varphi(0) > 0$ , define

$$E_\varphi(\mu, \nu) = \iint \varphi(x-y) d\mu(x) d\nu(y), \quad C_\varphi(L) = \left( \min_{\substack{\mu \geq 0, \mu(\mathbb{R})=1 \\ \supp \mu \subseteq [0, L]}} E_\varphi(\mu, \mu) \right)^{-1}. \quad (8.1)$$

The interval is closed, and the measures are nonnegative Borel measures. Weak compactness of its probability measures and continuity of the kernel give a minimum. It is strictly positive:  $\varphi \geq a/2$  near zero, and a finite partition into intervals of smaller diameter bounds every energy below by  $(a/2) \sum_j \mu(I_j)^2$ , uniformly away from zero. Nonnegativity permits discarding the cross-interval terms.

**Theorem 8.1** (universal positive-capacity bound). *Let  $\varphi$  have the properties just stated and define the extended real number*

$$\beta = \liminf_{L \rightarrow \infty} (C_\varphi(L) - L).$$

Then

$$\boxed{\beta \geq \frac{8}{9a}, \quad a = \varphi(0).} \quad (8.2)$$

*No finite intercept, unit-slope condition, positive definiteness, or sampling assumption is required. If, in particular,*

$$C_\varphi(L) = L + b + o(1) \quad (L \rightarrow \infty) \quad \text{with finite } b, \quad (8.3)$$

*then  $\beta = b$  and  $ab \geq 8/9$ . The general result applies to every real  $h \in L^1(\mathbb{R}) \cap L^2(\mathbb{R})$  with  $\int h = 1$  and  $\varphi = h * \tilde{h} \geq 0$ , including signed  $h$  and kernels of unbounded support, without assuming (8.3).*

**Theorem 8.2** (attainment by the ramp). *For the kernel  $f$  in (3.2), with  $\alpha = \log(4/3)$ , every real  $L \geq 1$  satisfies*

$$\begin{aligned} L + \frac{2}{3} - 168e^{-\alpha L} - 192e^{-2\alpha L} &\leq C_f(L) \leq L + \frac{2}{3} + 168e^{-\alpha L}, \\ \left| C_f(L) - L - \frac{2}{3} \right| &\leq 360e^{-\alpha L}. \end{aligned} \quad (8.4)$$

*Thus  $a = 4/3$ ,  $\beta = b = 2/3$ , and  $a\beta = ab = 8/9$ . Moreover,  $\sum_{d \geq 1} f(d/T) \leq T/2$  for every  $T > 0$ . Hence  $8/9$  is the infimum even when the kernels in Theorem 8.1 are restricted to autocorrelations satisfying the sampling condition  $\sum_{d \geq 1} \varphi(d/T) \leq T/2 + O(1)$  as  $T \rightarrow \infty$ .*

### 8.1 Positive capacity and its necessary first moment

For a finite nonnegative measure  $\nu$  supported on  $[0, L]$ , write  $M(\nu) = \nu(\mathbb{R})$ . Scaling each probability measure and maximizing  $2c - c^2 E_\varphi(\mu, \mu)$  over  $c \geq 0$  gives

$$C_\varphi(L) = \sup_{\substack{\nu \geq 0 \\ \supp \nu \subseteq [0, L]}} \{2M(\nu) - E_\varphi(\nu, \nu)\}. \quad (8.5)$$

The zero measure may be included. For Lebesgue measure  $\lambda_L$  on  $[0, L]$ , evenness and mass one give

$$E_\varphi(\lambda_L, \lambda_L) = \int_{\mathbb{R}} (L - |t|)_+ \varphi(t) dt = L - \int_{\mathbb{R}} \min\{|t|, L\} \varphi(t) dt.$$

Consequently (8.5) and monotone convergence give

$$\begin{aligned} M_1(L) &:= \int_{\mathbb{R}} \min\{|t|, L\} \varphi(t) dt, & C_\varphi(L) &\geq L + M_1(L), \\ m_1 &:= \int_{\mathbb{R}} |t| \varphi(t) dt \leq \beta. \end{aligned} \quad (8.6)$$

If  $m_1 = \infty$ , then  $\beta = \infty$ , proving Theorem 8.1 in this case. If  $m_1 < \infty$ , the boundary energy expansion below applies without any assumption that  $\beta$  is finite or the excess has a limit. A finite intercept is the special case  $\beta = b$  and implies  $m_1 \leq b < \infty$ .

## 8.2 An exact boundary-correlation certificate

We retain  $U$ ,  $g_+$  and  $q$  from Section 4:  $U$  is the uniform probability measure,  $2g_+ = \sum_{n \geq 0} U^{*n}$  is the full renewal measure, and  $q = g_+ - H_+(t) dt$ , where  $H_+ = \mathbf{1}_{[0, \infty)}$  and  $H_-(t) = H_+(-t)$ . Put  $m = q(\mathbb{R}) = 1/3$  and retain the density  $r = u/2 - 1$  from (4.11). The nested ranges in the proof of Lemma 4.2 lie in  $[1, e]$ , so

$$u(t) \geq 1 \quad \text{almost everywhere on } [0, \infty). \quad (8.7)$$

Lemmas 4.1–4.3 give exponential decay of  $r$ , finite total variation of  $q$ , and its exact mass. Set

$$R(s) = 2g_+([0, s]) \quad (s \geq 0), \quad R(s) = 0 \quad (s < 0).$$

It is nonnegative, is at least one for  $s \geq 0$ , and has a jump of one at zero. The renewal equation gives, almost everywhere for  $s > 0$ ,

$$R'(s) = R(s) - R(s-1), \quad R(s) = 2s + \frac{2}{3} + O(e^{-\alpha s}) \quad (s \rightarrow \infty). \quad (8.8)$$

Indeed  $R' = u$ ; the mass of  $2g_+$  between  $s-1$  and  $s$  equals  $u(s)$ , including the atom when  $s < 1$ . Values at  $s = 1$  do not affect this assertion. The asymptotic follows from  $2g_+ = 2H_+(t) dt + 2q$  and Lemma 4.3.

For  $t > 0$  put  $J(t) = q([t, \infty))$ , and use a tilde for reflection of a finite measure by  $t \mapsto -t$ . Define the even locally finite signed measure

$$B = [-|t| + 2m + 2J(|t|)] dt + 2q * \tilde{q}. \quad (8.9)$$

The value of  $J(0)$  is immaterial.

**Lemma 8.3** (boundary-correlation identity). *As locally finite signed measures,*

$$\boxed{B = \frac{1}{2}\delta_0 - \frac{1}{2}\mathbf{1}_{\{|t|>1\}} R(|t|-1) dt.} \quad (8.10)$$

*In particular its density away from the atom at zero is nonpositive.*

*Proof.* Weak derivatives are interpreted against compactly supported smooth test functions. Let  $D$  denote differentiation, let  $\tau_1$  translate to the right by one, and put  $\mathcal{A} = D - I + \tau_1$ . Differentiating  $(\delta_0 - U) * g_+ = (1/2)\delta_0$ , with  $U' = \delta_0 - \delta_1$ , yields

$$\mathcal{A}g_+ = \frac{1}{2}\delta'_0, \quad \mathcal{A}H_+ = \delta_0 - U, \quad \mathcal{A}q = U - \delta_0 + \frac{1}{2}\delta'_0.$$

Functions also denote their Lebesgue-density measures here. The convolutions below are defined:  $q$  has finite total variation, an exponentially decreasing density, and one atom; convolution with a half-line indicator is bounded. The last identity expresses  $q'$  as a finite signed measure plus one derivative of an atom, justifying commutation of the weak derivatives below.

Almost everywhere  $H_- * q + H_+ * \tilde{q} = m + J(|t|)$ , so

$$B = -|t| dt + 2H_- * q + 2H_+ * \tilde{q} + 2q * \tilde{q}.$$

Apply  $\mathcal{A}$  on  $q$  in the second and fourth terms and on  $H_+$  in the third. Since  $H_- * \delta'_0 = -\delta_0$ ,

$$\begin{aligned} \mathcal{A}B &= \mathcal{A}(-|t|) + 2H_- * (U - \delta_0 + \frac{1}{2}\delta'_0) \\ &\quad + 2(\delta_0 - U) * \tilde{q} + 2(U - \delta_0 + \frac{1}{2}\delta'_0) * \tilde{q} \\ &= \mathcal{A}(-|t|) + 2(H_- * U - H_-) - \delta_0 + (\tilde{q})'. \end{aligned}$$

The two ordinary functions on the last line cancel: on  $(0, 1)$  they are  $2(t-1)$  and  $2(1-t)$ , respectively, and both vanish elsewhere. We obtain the exact identity

$$B' - B + \tau_1 B = (\tilde{g}_+)'. \quad (8.11)$$

The only atom of  $B$  has mass  $2(1/2)^2 = 1/2$  at zero. Write  $B = (1/2)\delta_0 + D_0(t) dt$ , where  $D_0$  is even. For  $t > 0$ ,

$$D_0(t) = -t + 2m + 2J(t) + r(t) + 2 \int_0^\infty r(s) r(s+t) ds. \quad (8.12)$$

Thus  $D_0(t) = -t + 2m + O(e^{-\alpha t})$  as  $t \rightarrow \infty$ . The right side of (8.11) is supported on the nonpositive half-line, so on  $(0, 1)$ 

$$D'_0(t) = D_0(t) - D_0(1-t).$$

This first implies local absolute continuity. The derivative of  $D_0(t) - D_0(1-t)$  is zero, and this difference changes sign under  $t \mapsto 1-t$ . Hence it vanishes, and  $D_0$  is a constant  $d$  on  $(0, 1)$ . The translated atom gives a jump of  $-1/2$  at  $t = 1$ . For  $t > 1$  the equation is  $D'_0 = D_0 - D_0(\cdot - 1)$ , with no further jumps. The unit jump and delay equation of  $R$ , and uniqueness successively on unit intervals, imply

$$D_0(t) = d - \frac{1}{2}R(t-1) \quad (t > 1).$$

By (8.8), its large- $t$  constant term is  $d + 2/3$ . By (8.12), it is  $2m = 2/3$ . Thus  $d = 0$ , proving the identity.  $\square$ 

### 8.3 Positive trials and the universal bound

*Proof of Theorem 8.1.* The case  $m_1 = \infty$  was proved above. Assume henceforth that  $m_1 < \infty$ ;  $\beta$  may still be infinite. Restrict  $q$  to  $q^{[L]}$  on  $[0, L]$ , let  $\rho_L(t) = L - t$ , and set

$$\sigma_L = \lambda_L + q^{[L]} + (\rho_L)_* q^{[L]}. \quad (8.13)$$

Its endpoint atoms have mass  $1/2$ , and its interior density is

$$1 + r(x) + r(L - x) = \frac{1}{2}u(x) + \frac{1}{2}u(L - x) - 1 \geq 0$$

by (8.7). It is therefore nonnegative for every  $L > 0$ , with mass  $L + 2m + o(1) = L + 2/3 + o(1)$ .

We retain every term in its energy expansion. The uniform part is  $L - m_1 + o(1)$  by (8.6). At a fixed  $y \geq 0$  the uniform potential tends to

$$\int_0^\infty \varphi(x - y) dx = \frac{1}{2} + \int_0^y \varphi(t) dt,$$

and is bounded by one. Dominated convergence against  $|q|$ , followed by Fubini, shows that the two endpoints and both orders of each uniform-boundary cross term together contribute

$$2m + 4 \int_0^\infty \varphi(t) J(t) dt + o(1).$$

The two same-end self-energies contribute  $2 \int \varphi d(q * \tilde{q}) + o(1)$ , since  $\varphi$  is bounded and  $q$  has finite total variation. The opposite-end cross term tends to zero: for fixed  $x, y \geq 0$ ,  $\varphi(x + y - L) \rightarrow 0$ , and dominated convergence applies against  $|q| \times |q|$ . Restrictions to  $[0, L]$  converge in total variation and introduce no further term. Altogether,

$$\begin{aligned} E_\varphi(\sigma_L, \sigma_L) &= L + \int_{\mathbb{R}} \varphi(t) dB(t) + o(1) \\ &= L + \frac{a}{2} - \frac{1}{2} \int_{|t|>1} \varphi(t) R(|t| - 1) dt + o(1). \end{aligned} \quad (8.14)$$

The integral against the linear-growth density converges by (8.6). Insert this nonnegative trial into (8.5), subtract  $L$ , and take the lower limit:

$$\beta \geq \frac{4}{3} - \frac{a}{2} + \frac{1}{2} \int_{|t|>1} \varphi(t) R(|t| - 1) dt \geq \frac{4}{3} - \frac{a}{2}. \quad (8.15)$$

For  $\ell > 0$  apply this to  $\varphi_\ell(t) = \ell \varphi(\ell t)$ . Its mass is one and its value at zero is  $\ell a$ . Pushing probability measures forward under  $x \mapsto \ell x$  gives the exact identities

$$C_{\varphi_\ell}(L) = \frac{C_\varphi(\ell L)}{\ell}, \quad \beta(\varphi_\ell) = \frac{\beta(\varphi)}{\ell},$$

the second in the extended real numbers. Changing variables in the tail integral and multiplying by  $\ell$ ,

$$\beta \geq \frac{4\ell}{3} - \frac{a\ell^2}{2} + \frac{\ell}{2} \int_{|t|>\ell} \varphi(t) R(|t|/\ell - 1) dt \geq \frac{4\ell}{3} - \frac{a\ell^2}{2}. \quad (8.16)$$

The final quadratic is maximized at  $\ell = 4/(3a)$ , with value  $8/(9a)$ . This proves (8.2); the finite-intercept corollary follows by setting  $\beta = b$ .  $\square$ 

#### 8.4 Attainment for the positive capacity

*Proof of Theorem 8.2.* Lemma 3.1 gives  $f(0) = 4/3$  and  $\int f = 1$ . Let  $L \geq 1$ , reflect  $q$  to  $q_L$  as in Lemma 4.4, and set

$$\eta_L = \lambda_L + q + q_L, \quad d_L = L + \frac{2}{3}, \quad V_L = f * \eta_L, \quad z_L = e^{-\alpha L}.$$

This finite signed measure has mass  $d_L$ . As in (4.19), it is the sum of  $g_+$  and its reflection minus full-line Lebesgue measure. Lemma 4.1 gives  $V_L = 1$  on the closed interval  $[0, L]$ . Nonnegativity and mass one of  $f$ , its maximum  $4/3$ , and  $\|q\|_{\text{TV}} \leq 9/2$  give

$$|V_L(x)| \leq 1 + 2 \cdot \frac{4}{3} \cdot \frac{9}{2} = 13 \quad (x \in \mathbb{R}).$$

Write  $\eta_L = \sigma_L + \tau_L$ , where  $\sigma_L$  is its restriction to  $[0, L]$ . It is exactly the nonnegative trial in (8.13). The exterior part consists of two correction tails, so Lemma 4.3 gives

$$\|\tau_L\|_{\text{TV}} \leq 12z_L, \quad |E_f(\eta_L, \eta_L) - d_L| = \left| \int_{\mathbb{R} \setminus [0, L]} (V_L - 1) d\eta_L \right| \leq 168z_L.$$

For every probability measure  $\mu$  on  $[0, L]$ ,  $E_f(\mu, \eta_L) = 1$ . Cauchy–Schwarz from Lemma 3.1 implies

$$C_f(L) \leq E_f(\eta_L, \eta_L) \leq d_L + 168z_L.$$

For the lower bound,  $V_L = 1$  on the support of  $\sigma_L$  gives  $E_f(\eta_L, \sigma_L) = M(\sigma_L)$ . Expanding  $\eta_L = \sigma_L + \tau_L$  yields the exact identity

$$2M(\sigma_L) - E_f(\sigma_L, \sigma_L) = E_f(\eta_L, \eta_L) - E_f(\tau_L, \tau_L).$$

The last energy is at most  $(4/3)\|\tau_L\|_{\text{TV}}^2 \leq 192z_L^2$ . Use  $\sigma_L$  in (8.5) to obtain

$$C_f(L) \geq d_L - 168z_L - 192z_L^2 \geq d_L - 360z_L.$$

This proves the positive-capacity asymptotic and remainder without assuming equality with a signed-measure capacity. Finally, monotonicity and the cellwise integral comparison of Lemma 5.1 give, for every  $T > 0$ ,

$$\sum_{d \geq 1} f(d/T) \leq T \int_0^\infty f(t) dt = \frac{T}{2}.$$

### 8.5 Sampling and the limitation for every choice of scale

The capacity theorem requires no hypothesis on the leading slope. For the method limitation impose the separate condition

$$\limsup_{L \rightarrow \infty} \frac{C_\varphi(L)}{L} \leq 1. \quad (8.17)$$

A finite intercept in (8.3) implies this condition. We state it explicitly as a hypothesis of the method limitation. Define the extended lattice sum

$$S_T = \sum_{d \in \mathbb{Z}} \varphi(d/T) \in (0, \infty].$$

*Remark 8.4* (sampling lower bound). Condition (8.17) forces  $S_T \geq T$  for every  $T > 0$ . If  $S_T = \infty$  this is immediate. Otherwise the probability measure  $\mu_n = n^{-1} \sum_{j=0}^{n-1} \delta_{j/T}$  gives, by nonnegativity,

$$E_\varphi(\mu_n, \mu_n) = \frac{1}{n^2} \sum_{|d| < n} (n - |d|) \varphi(d/T) \leq \frac{S_T}{n}, \quad C_\varphi((n-1)/T) \geq \frac{n}{S_T}.$$

Divide by  $(n-1)/T$  and let  $n \rightarrow \infty$ ; (8.17) gives  $1 \geq T/S_T$ . No upper sampling bound is required.

For a Sidon set of size  $k$  in  $\{1, \dots, N\}$ , nonnegative majorization of its distinct ordered differences therefore gives

$$\begin{aligned} k^2 &\leq C_\varphi(N/T) \left( ak + 2 \sum_{d \geq 1} \varphi(d/T) \right) \\ &= C_\varphi(N/T) (a(k-1) + S_T). \end{aligned} \quad (8.18)$$

An infinite lattice sum makes this inequality uninformative.

**Lemma 8.5** (simultaneous comparison for all scales). *Let  $\beta = \liminf_{L \rightarrow \infty} (C_\varphi(L) - L)$ . For every real  $\theta < \sqrt{a\beta}$ , with  $\beta = \infty$  permitting every finite  $\theta$ , all sufficiently large  $N$  satisfy*

$$\begin{aligned} x &= N^{1/4}, \quad k_N = \lfloor x^2 + \theta x \rfloor, \\ k_N^2 &\leq C_\varphi(N/T) (a(k_N - 1) + T) \quad \text{for every } T > 0. \end{aligned} \quad (8.19)$$

*The threshold in  $N$  is independent of  $T$ .*

*Proof.* Choose a finite  $B$  with  $0 < B < \beta$  and  $\sqrt{aB} > \theta$ ; Theorem 8.1 ensures  $\beta > 0$ . Put  $L = N/T$  and  $c(L) = C_\varphi(L) - L$ . The definition of liminf gives  $L_0 > 0$  such that  $c(L) \geq B$  for  $L \geq L_0$ . The uniform trial gives  $c(L) \geq M_1(L) > 0$  for every  $L > 0$ , where  $M_1$  is defined in (8.6). For  $0 < L \leq L_0$ ,

$$\frac{M_1(L)}{L} = \int_{\mathbb{R}} \min\{|t|/L, 1\} \varphi(t) dt \geq \frac{M_1(L_0)}{L_0} =: \eta > 0.$$

The ratio also tends to one as  $L \downarrow 0$ , by dominated convergence. For large  $N$  we have  $k_N \geq 1$ , so throughout this range

$$C_\varphi(L) (N/L + a(k_N - 1)) \geq N(1 + \eta) > k_N^2.$$

For  $L \geq L_0$ , expansion and AM-GM give, uniformly in  $L$ ,

$$\begin{aligned} (L + c(L)) (N/L + a(k_N - 1)) &\geq N + \frac{NB}{L} + a(k_N - 1)L \\ &\geq N + 2\sqrt{aBN(k_N - 1)} \\ &= x^4 + 2\sqrt{aB}x^3 + O(x^2). \end{aligned}$$

Since  $k_N^2 = x^4 + 2\theta x^3 + O(x^2)$  and  $\sqrt{aB} > \theta$ , this exceeds  $k_N^2$  for all large  $N$ . The error constants do not depend on  $L$ , proving the simultaneous assertion.  $\square$ 

Under (8.17), Remark 8.4 and Lemma 8.5 show that these integers satisfy every exact majorized inequality (8.18) simultaneously. They are scalar comparison integers, *not* constructed Sidon sets. No choice  $T = T(N)$ , nor simultaneous use of all  $T$ , can therefore force a smaller coefficient: for any proposed  $c < \sqrt{a\beta}$  and fixed additive constant, choose  $c < \theta < \sqrt{a\beta}$  and the comparison integers eventually violate that conclusion. The universal floor is  $2\sqrt{2}/3$ . For a finite intercept,  $\beta = b$ , so the comparison  $\lfloor x^2 + (\sqrt{ab} - \varepsilon)x \rfloor$  works for every  $\varepsilon > 0$ . The argument also covers nonconvergent capacity excess under (8.17); if  $\beta = \infty$ , every finite comparison coefficient survives.

To produce an asymptotic upper bound, the additional assumptions  $C_\varphi(L) = L + b + o(1)$  with finite  $b$  and

$$\sum_{d \geq 1} \varphi(d/T) \leq T/2 + O(1) \quad (T \rightarrow \infty)$$

give  $k^2 \leq C_\varphi(N/T)(ak + T + O(1))$ . For  $x = N^{1/4}$  and  $T = tx^3$  with fixed  $t > 0$ , its positive root is

$$x^2 + \frac{1}{2}(bt + a/t)x + o(x).$$

This is an upper bound on cardinalities, not an assertion about the size of arbitrary Sidon sets. Optimizing over  $t$  gives  $\sqrt{ab}$ ; the all-scale argument above supplies the stronger limitation. An  $o(1)$  capacity remainder gives only an  $o(N^{1/4})$  remainder, whereas  $C_\varphi(L) \leq L + b + O(1/L)$  and a bounded sampling error suffice for an additive  $O(1)$ . The ramp remainder is stronger.

The method limitation concerns fixed kernels, scalar positive capacity, nonnegative majorization by the full infinite lattice difference sum, and the unit-slope hypothesis (8.17). The capacity lower bound itself needs no slope hypothesis. No claim is made for replacing the full sum by a truncated sum restricted to  $d \leq N$ . This is not a barrier for all weighted Erdős–Turán arguments, extra variance or missing-difference information, other counting majorants, or arbitrary  $N$ -dependent kernels without uniform control. It does not resolve the original conjecture or assert a lattice-restricted capacity extension. No uniqueness is proved: equality  $a\beta = 8/9$  forces  $\varphi(t) = 0$  for  $|t| > 4/(3a)$  by (8.16) and  $R \geq 1$ , but this does not characterize all equality kernels. Signed-probability capacity can be larger, even infinite; it cannot replace the positive capacity here.

## 8.6 Independent work on the same constant

A manuscript by John Akwei, posted on GitHub on 1 October 2026 (one day before the first version of this note) and expanded on 5 October 2026 [Akw26a, Akw26b], proves that every symmetric or two-sided covering certificate in the vector-valued smoothing framework of Hou–Zhao satisfies  $ab \geq 8/9$ , so that the certificate coefficient  $\gamma = \sqrt{ab}$  cannot fall below  $2\sqrt{2}/3$ , and that the infimum is attained in the continuum by the ramp density  $\rho(x) = 2x$  on  $[0, 1]$  ( $a = 4/3$ ,  $b = 2/3$ ); it also reports a rational certificate with  $\gamma < 0.942809522$  and the bound  $h(N) \leq \sqrt{N} + 0.9428096 N^{1/4} + O(1)$  (his  $h$  is our  $F$ ). The ramp is the reflection of our kernel and has the same autocorrelation, and the renewal-measure multiplier is the same up to normalisation. The statements differ in the quantified object: Akwei bounds the boundary cost of Hou–Zhao covering certificates over finite mixtures of autocorrelations, while Theorem 8.1 bounds the positive capacity intercept over all even nonnegative kernels in  $C_0 \cap L^1$ ; neither statement is known to imply the other. The explicit cardinality theorem with the exact coefficient, the additive constant  $+1$  and an explicit onset (now  $N \geq 4600\,000$ ;  $N \geq 120^4$  in the first two versions) appears to be new to this note. We learned of Akwei’s manuscript on 9 October 2026, after the first two versions of this note had been published.

## 9 Remarks

### 9.1 The earlier numerical kernel scan

The exploratory numerical scan is superseded, within the stated scope, by Theorem 8.1.

*Remark 9.1* (numerical onset, not certified). Numerical evaluation of the same inequalities gives the stated Sidon bound already for  $N \geq 4540\,589$  (computed by a referee of version 1 and reproduced independently in 60-digit arithmetic). This evaluation is not certified here and does not replace the proved onset 4600\,000 in Theorem 2.1.

## 9.2 The same numerical constant in a different ruler problem

Gupta and O'Bryant [GO26, Definition 2 and Theorem 3] define an LM ruler by requiring that a positive distance  $d$  have at most  $d - 1$  representations. For an  $n$ -element LM ruler  $\{0 = \ell_1 < \dots < \ell_n\}$  they prove

$$\ell_n \geq \sqrt{8/9} (n - 1)^{3/2}.$$

Thus the number  $\sqrt{8/9} = 2\sqrt{2}/3$  occurs there as well. This is a numerical coincidence between the stated constants: the multiplicity condition, main scale, and conclusion differ. No implication between that LM-ruler theorem and the Sidon cardinality bound of this note is asserted.

## 9.3 Analytic inputs and finite checks

The following description of analytic inputs and finite checks concerns the original upper-bound proof in Sections 2–7. Section 8 additionally uses weak derivatives against smooth compactly supported test functions and the convolution identities proved in Lemma 8.3.

The proof uses only standard real analysis: Tonelli and Fubini under the nonnegativity and absolute-integrability conditions verified in the text; monotone and dominated convergence; Cauchy–Schwarz in real  $L^2$ ; absolute continuity of indefinite integrals of locally integrable functions and its integrating-factor consequence; completeness of the real numbers for nested compact intervals; and elementary exponential, logarithmic, and quadratic calculations. The factorial majorant proves compact uniform convergence of the density series. No external result about Sidon sets, renewal processes, or extremal constants is an input to the proof.

The accompanying audit script `check_sidon_bound.py` uses exact fractions and integer square roots for rational enclosures and finite sanity checks. A JavaScript translation was executed for the reported finite checks, including maxima on intervals of lengths at most 60; the Python deliverable itself was not executed in the drafting environment; it was later run by the coordinator and by both referees of version 1 (exit code 0). For version 3, `check_sidon_bound.v2.py` replays exactly every integer and rational comparison of Section 6 and of the tail chain of the Lean formalization, and tests the finite-certificate tail inequality used there for every integer  $N \in [4.6 \cdot 10^6, 5.6 \cdot 10^6]$  (exit code 0). These finite computations are not used to prove the theorem. In particular, numerical grids do not replace the all- $N$  monotonicity argument in Section 6.

## Provenance and verification status

The explicit Sidon upper bound in v1 was found by a clean-room GPT-6 Astra agent (OpenAI), then expanded and examined in informed same-vendor adversarial reviews. Its source proof, standalone expansion, and finite-audit code received same-vendor review. Cross-vendor referee reports on that upper bound by Claude Opus (Anthropic): two isolated reports dated 2026-10-02, both *PASS* with no repair required: referee A re-derived every display and checked the exact potential of the capacity lemma numerically; referee B reconstructed the main inequality independently from the statement and the constant, and tested every intermediate inequality on about  $1.2 \cdot 10^5$  Sidon sets (all maximum Sidon sets for  $N \leq 60$ , Singer and Bose–Chowla sets for prime powers  $q \leq 127$ , Mian–Chowla prefixes, random and adversarial sets) without a violation. Both referees note that the onset  $120^4$  is a convenient sufficient value: the same inequalities already give the stated bound for  $N \geq 4 540 589$  (numerical evaluation, not certified here).

The new optimality theorem in Section 8 was found by two isolated clean-room GPT-6 Astra agents (OpenAI). Same-vendor self-audit, informed route review, and final integration reviews returned *PASS*. These are mathematical derivations and reviews, not numerical evidence of optimality. The earlier Claude verdicts concern the v1 upper bound and do not apply to this new theorem. Cross-vendor referee A (Claude Opus): **PASS-WITH-REPAIRS, repairs applied.** The core proof was accepted; the all-scale scope argument and the liminf and sampling strengthenings were independently checked and incorporated. The referee’s reported numerical checks were not rerun here and are not numerical certificates. Cross-vendor referee B (Claude Opus, isolated, 2026-10-02): *PASS*; it reconstructed the lower bound independently from the statement, arriving at the same trial measure, and found no kernel below 8/9 among about thirty named kernels and four optimised parametric families.

The new Section 6 of v3 was written by a clean-room GPT-6 Astra agent (OpenAI) that received only Sections 2, 5 and 6 of the v1 proof and the finite-certificate chain of the Lean formalization, without the literature or earlier referee reports. Its every comparison was replayed in exact arithmetic by a separate Claude verifier, and two isolated cross-vendor referee reports by Claude (Anthropic), dated 2026-10-09 (UTC), returned *PASS* and *PASS* with no repair required, each recomputing every displayed comparison.

Lean: the upper bound is kernel-checked in Lean 4 with Mathlib in the project <https://github.com/chy4pro/automath/tree/main/lean/sidon30>. Theorem `sidon_second_order`' states it for every natural  $N \geq 4600\,000$  and every Sidon set  $A \subseteq \{1, \dots, N\}$ , with diagonal sums included, coefficient  $2\sqrt{2}/3$  and additive constant 1 (GitHub Actions run 37978411704); the v1 theorem `sidon_second_order` for  $N \geq 120^4$  is a corollary. Both depend only on the axioms `propext`, `Classical.choice` and `Quot.sound`. The formalization, written by GPT-6 Astra, uses a finite certificate in place of the real-variable Lemma 5.1; its tail estimate at the new onset was refereed together with Section 6. The optimality theorem of Section 8 is not formalized.

No independent human referee report is claimed. The author takes responsibility for the mathematics. Bibliography statements and unrefereed numerical claims are distinguished in the introduction; citing a claim does not certify its proof or computational certificate.

## References

- [ET41] P. Erdős and P. Turán, On a problem of Sidon in additive number theory, and on some related problems, *J. London Math. Soc.* (1) **16** (1941), no. 4, 212–215, doi:10.1112/jlms/s1-16.4.212.
- [Lind69] B. Lindström, An inequality for  $B_2$ -sequences, *J. Combin. Theory* **6** (1969), no. 2, 211–212, doi:10.1016/S0021-9800(69)80124-9.
- [Cil10] J. Cilleruelo, Sidon sets in  $\mathbb{N}^d$ , *J. Combin. Theory Ser. A* **117** (2010), no. 7, 857–871, doi:10.1016/j.jcta.2009.12.003.
- [BFR23] J. Balogh, Z. Füredi and S. Roy, An upper bound on the size of Sidon sets, *Amer. Math. Monthly* **130** (2023), no. 5, 437–445, doi:10.1080/00029890.2023.2176667; preprint arXiv:2103.15850v2, 17 June 2021 (v1: 29 March 2021).
- [OB24] K. O'Bryant, On the size of finite Sidon sets, *Ukrains'kyi Matematychnyi Zhurnal* **76** (2024), no. 8, 1192–1206, doi:10.3842/umzh.v76i8.7858; preprint arXiv:2207.07800v2, 25 July 2022 (v1: 16 July 2022).
- [CHO25] D. Carter, Z. Hunter and K. O'Bryant, On the diameter of finite Sidon sets, *Acta Math. Hungar.* **175** (2025), no. 1, 108–126, doi:10.1007/s10474-024-01499-8; preprint arXiv:2310.20032v1, 30 October 2023.
- [AE25] T. Tao, Comment on *Mathematical exploration and discovery at scale*, What's new, 11 November 2025, 5:52 pm (site-displayed time), <https://terrytao.wordpress.com/2025/11/05/mathematical-exploration-and-discovery-at-scale/#comment-689052>. Unrefereed announcement; attribution and safe rounded coefficient also recorded at <https://teorth.github.io/optimizationproblems/constants/5a.html>. Accessed 2 October 2026.
- [HZ26] J. Hou and H. Zhao, An Improved Upper Bound for Finite Sidon Sets via Vector-Valued Smoothing, preprint, arXiv:2607.01169v3, 4 September 2026 (v1: 1 July 2026; v2: 5 July 2026).
- [Josh26] J. Madeiros (JoshMadeiros), An improved constant in the second-order term:  $h(N) \leq N^{1/2} + 0.94325N^{1/4} + O(1)$ , comment on Erdős Problem #30, 17 August 2026, 12:14 (site-displayed time), <https://www.erdosproblems.com/forum/thread/30#post-8482>. Unrefereed forum claim; accessed 2 October 2026.
- [Wu26] wustep (Stephen Wu), *q2—grow free histograms from the q1 mix*, maths GitHub repository, 27 August 2026, commit `da2440b68979b78d201182118d30ca418e3c2001`, <https://github.com/wustep/maths/blob/da2440b68979b78d201182118d30ca418e3c2001/problems/sidon-second-term/compute/q2/README.md>. The q1 and q2 statements are also recorded in <https://github.com/wustep/maths/blob/da2440b68979b78d201182118d30ca418e3c2001/problems/sidon-second-term/PROBLEM.md>. Unrefereed repository claims; accessed 2 October 2026.
- [Akw26a] J. Akwei, *Vector-valued smoothing for Sidon sets cannot beat  $2\sqrt{2}/3$* , manuscript, GitHub repository `johnakwei/Science`, commit `7e78435` (1 October 2026); expanded as *The limit of vector-valued smoothing for Sidon sets is  $2\sqrt{2}/3$* , commit `15609b5` (5 October 2026). Unrefereed; accessed 9 October 2026.
- [Akw26b] J. Akwei, *A Data Science Analysis of Erdős Problem 30*, version 4, GitHub repository `johnakwei/Science`, commit `6b32990` (5 October 2026). Unrefereed; accessed 9 October 2026.
- [GO26] A. Gupta and K. O'Bryant, Optimal Diameters of High Multiplicity  $g$ -Golomb Rulers, preprint, arXiv:2605.14229v1, 14 May 2026.
- [EP30] T. F. Bloom, Erdős Problem #30, <https://www.erdosproblems.com/30>, accessed 2 October 2026.

[^1]: Changes in v2: Section 8 adds the complete fixed-kernel optimality proof and positive-capacity attainment estimate. Referee A’s all-scale repair and liminf and sampling strengthenings are applied. The v1 statements and proofs, including the certified onset 120<sup>4</sup>, were unchanged in v2; the numerical scan was replaced by the rigorous theorem. Cross-vendor referee A: PASS-WITH-REPAIRS, repairs applied; referee B: PASS. Changes in v3: Section 6 lowers the onset from 120<sup>4</sup> to 4600\,000 by a new numerical absorption, with Lemma 5.1 unchanged (two cross-vendor referees: PASS, PASS); the bound is kernel-checked in Lean; Section 8.6 records independent work of Akwei on the same constant. No other statement or proof is changed.