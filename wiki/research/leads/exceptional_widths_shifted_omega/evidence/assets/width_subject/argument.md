[cut]

It answers the modified E0122 property negatively for f = omega, not the
whole classification question. The argument uses the literal allowance that
F(n)/f(n) tends to zero on a density-one set; it makes no monotonicity or
everywhere-smallness assumption on F. It also gives a real-location extension.

The source input is Erdős, Pomerance and Sárközy, *On locally repeated
values of certain arithmetic functions, IV* (1997), Lemma 1, printed
pp. 229–230, with modulus m = 1, additive function omega, and K = 1:

$$
\sum_{n\le X}(\omega(n)-A(X))^2\ll X(A(X)+1),
\qquad A(X)=\sum_{p\le X}\frac1p.
$$

At modulus 1, the condition on primes dividing the modulus is vacuous;
omega is nonnegative and additive, and omega(p^a)=1 makes K=1 for X>=2.

[cut]

Euler's divergence of the prime reciprocal sum gives A(X) tending
to infinity, while A(X) is at most 1 + log X. No computational evidence is
needed.

Put X_j = 2^(j+2), A_j = A(X_j), and H_j = ceil(A_j^(3/4)), for sufficiently
large integer j. Let

$$
D_j=\{n\le X_j:|\omega(n)-A_j|>H_j\}.
$$

Chebyshev's inequality applied to the displayed source estimate gives

$$
|D_j|\ll X_j\frac{A_j+1}{H_j^2}=o(2^j).
$$

For each integer u in [2^j,2^(j+1)), let b_j(u) count the members n of
D_j whose image n + omega(n) belongs to (u,u+H_j+1). Since the image is
an integer, each n contributes to at most H_j + 1 different u. Therefore

$$
\sum_{2^j\le u<2^{j+1}} b_j(u)\le (H_j+1)|D_j|.
$$

Set E_j = {u in that dyadic interval: b_j(u) > H_j + 1}. Then
|E_j| <= |D_j| = o(2^j). The union E of the E_j has natural density zero:
given epsilon > 0, take J such that |E_j| <= epsilon 2^j for every j >= J
and sum the dyadic bounds up to the last partial interval. The finite
initial part contributes o(x), and the other intervals contribute at most
2 epsilon x.

If u is outside E_j, every n with

$$
n+\omega(n)\in(u,u+H_j+1)
$$

is below X_j for all large j, because omega is nonnegative and
2^(j+1)+H_j+1 < 2^(j+2). If n is outside D_j as well, then

$$
u-A_j-H_j<n<u+2H_j+1-A_j.
$$

There are at most 3H_j + 2 integers in that interval. Including the bad
inputs, whose contribution is at most H_j + 1, the image count is at most
4H_j + 3.

Define F on real x >= 1, with u = floor(x) and u in [2^j,2^(j+1)), by

$$
F(x)=\begin{cases}
H_j,&u\notin E_j,\\
2(u+1),&u\in E_j.
\end{cases}
$$

For the finitely many early u use the second alternative. This makes
F(x) tend to infinity for all x, including exceptional locations. At a
nonexceptional x, (x,x+F(x)) is contained in (u,u+H_j+1), so the normalized
count is at most 4 + 3/H_j, eventually at most 7. At an exceptional x,
any counted positive integer n satisfies n < x+F(x) < 3(u+1). Hence its
normalized count is less than 3/2. Positivity of n and omega is all that
this latter estimate uses. Consequently the normalized count is bounded
for every sufficiently large real x and cannot diverge on any sequence.

It remains to check the width hypothesis at the integers. Outside the
density-zero union E and the set of u in [2^j,2^(j+1)) belonging to D_j,

$$
\omega(u)\ge A_j-H_j\ge A_j/2,
\qquad \frac{F(u)}{\omega(u)}\le\frac{2H_j}{A_j}\longrightarrow0.
$$

The second exceptional union also has density zero by the same dyadic
argument. Thus F is admissible under the exact modified Statement but
defeats its conclusion for omega. The harmless value omega(1) = 0 is
outside all limiting assertions.

[cut]

An additional condition such
as F(n) = o(log log n) everywhere would prohibit this construction; the
argument does not decide that different formulation or the tau case.

[cut]
