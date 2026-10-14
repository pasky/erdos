# Problem 408: the statement and formulation

Verbatim from the corpus problem page (wiki/problems/arithmetic_functions/E0408/_index.md, as of 2026-10-14), the Statement and Formulation paragraphs only.

**Statement.** Let $\phi(n)$ be the Euler totient function and $\phi_k(n)$ be
the iterated $\phi$ function, so that $\phi_1(n)=\phi(n)$ and
$\phi_k(n)=\phi(\phi_{k-1}(n))$. Let

$$
f(n) = \min \{ k : \phi_k(n)=1\}.
$$

Does $f(n)/\log n$ have a distribution function? Is $f(n)/\log n$ almost always
constant? What can be said about the largest prime factor of $\phi_k(n)$ when,
say, $k=\log\log n$?

**Formulation.** The second question is read as asking for a normal order:
whether $f(n)/\log n$ tends to a constant on a set of asymptotic density one.
That is how Erdős and Graham pose it on p. 81 of [ErGr80], asking whether
$f(n)/\log n$ is almost always constant, how [EGPS90] states its conjecture on
p. 166, $k(n)\sim\alpha\log n$ on a set of asymptotic density one, and how
erdosproblems.com reads it. Read as Bloom's catalog words it, the question has a
trivial answer no: $f(n)/\log n=c$ determines $n$ from $f(n)$, so each value of
$f$ gives at most one such $n$.
