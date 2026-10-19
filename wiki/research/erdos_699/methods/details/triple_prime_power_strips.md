---
name: research/erdos_699/methods/details/triple_prime_power_strips
title: "Erdős 699: finite three-prime cofactor bounds by CRT strips"
desc: "Exact three-dimensional exponent covers give .61 through 10^1000 and .66 through 10^3000; direct product checks remove every large exception to the latter."
created: 2026-09-22T16:49:25Z
updated: 2026-09-22T19:12:28Z
---

# Erdős 699: finite three-prime cofactor bounds by CRT strips

***

The [checker](../../computations/erdos_699_triple_prime_power_strips.py)
and [certificate](../../computations/erdos_699_triple_prime_power_strips.json)
prove the following finite statement. It concerns integer factorizations,
not bad binomial triples.

Let $134\le n\le10^{1000}$, put $h=n-6$, and choose

$$
r_2,r_3,r_5\in\{0,\ldots,6\},\qquad\min(r_2,r_3,r_5)=0.
$$

Suppose

$$n-r_2=2^a u_2,\qquad n-r_3=3^b u_3,\qquad
  n-r_5=5^c u_5,$$

where the exponents are nonnegative integers and the cofactors are positive
integers. Then

$$
\boxed{\max(u_2,u_3,u_5)\ge h^{61/100}}
$$

except for the configurations explicitly listed in the certificate.
There are **208 exceptional configurations on 68 rows**. Their largest row is

$$
1\,379\,463\,064\,453\,125.
$$

The factorization need not use the full valuation at each prime. The positions
may coincide. The requirement that one position be zero comes from the
[proved row-zero restriction](../../archive/other_approaches/low_crt_row_zero.md) in the
index-six and index-seven applications.

The computation uses 55 anchors and 2,783 exact boundary triples. It does
not enumerate the rows up to the height cap.

## The stronger exponent $33/50$

A [second certificate](../../computations/erdos_699_triple_prime_power_strips_066_3000.json)
uses the same algorithm and proves

$$
\max(u_2,u_3,u_5)\ge(n-6)^{33/50}
$$

for $262\le n\le10^{3000}$, except for 4,531 configurations on
1,224 explicitly listed rows. It uses 395 anchors and 2,101,496 exact
boundary triples. The largest exceptional row has 157 decimal digits.

There are only 114 exceptional rows greater than $10^{53}$. At each of
these rows, the [direct product checker](../../computations/erdos_699_triple_exception_products.py)
computes the full maximal valuations at two, three, and five, choosing the
smallest cofactor in the event of a tie. The [retained product certificates](../../computations/erdos_699_triple_exception_products.json)
prove

$$
\boxed{(u_2u_3u_5)^{50}\ge(n-6)^{53}}
$$

at every one of those rows. This therefore holds for every selection of
maximal-valuation positions on those rows.

Away from the listed exceptions, the triple exponent $33/50$, together
with a pair exponent $2/5$ on the other two primes, gives the same product
exponent $53/50$. If those two positions coincide, their two cofactors
already have product at least $n-6$, so the pair bound follows directly.
The triple certificate and the 114 direct product checks consequently
supply the product estimate above $10^{53}$ once the three required
pair estimates have also been checked on the range in question.

## The slab inequality

Fix a rational exponent $\delta=r/s<2/3$ and positions in $[0,D]$.
At an exponent anchor put

$$
P=p^a>D,\qquad Q=q^b>D,\qquad R=\ell^c>D,\qquad M=PQR,
$$

for three distinct primes. Let $n_0\in[0,M)$ be the CRT solution to

$$n_0\equiv r_p\pmod P,\quad
n_0\equiv r_q\pmod Q,\quad
n_0\equiv r_\ell\pmod R.$$

Define $u_{p,0}$ to be the least positive representative of
$(n_0-r_p)/P$ modulo $QR$. In particular, when all positions are zero and
$n_0=0$, take $u_{p,0}=QR$.

If a later exponent triple has first power $Pp^A$, and its positive
cofactor is $u_p'$, then

$$p^A u_p'\equiv u_{p,0}\pmod{QR},\qquad
  u_p'\ge u_{p,0}/p^A.$$

Let $\mu_p$ be the minimum of $u_{p,0}$ over the allowed position patterns.
Consequently

$$
\boxed{\mu_p^{s-r}\ge P^r p^{sA_0}}\tag{1}
$$

certifies every exponent with $0\le A\le A_0$, independently of the
increases at the other two primes. Indeed (1) gives

$$
u_p'^{s-r}\ge(Pp^A)^r,
$$

so $u_p'\ge(n-r_p)^{r/s}\ge(n-D)^{r/s}$.

Thus each anchor can certify up to three coordinate slabs. Their complement
is a single orthant, obtained by raising exactly those coordinate lower
bounds whose slabs were proved. Every comparison in (1) is integer
arithmetic; floating logarithms only propose step counts, subsequently
checked exactly.

## Minimal CRT rows suffice

Every nonminimal positive CRT solution has $n\ge M$. Therefore

$$u_pu_qu_\ell
 =\frac{(n-r_p)(n-r_q)(n-r_\ell)}M
 \ge\frac{h^3}{h+D},\qquad h=n-D.$$

For $\delta=61/100$, $D=6$, and $h\ge64$,

$$
h^{3(1-\delta)}\ge2h\ge h+6,
$$

because $64^{17}\ge2^{100}$. Hence at least one cofactor is at least
$h^{61/100}$. Only $n_0$ can be exceptional. The all-zero position pattern
has $n_0=0$, which is outside the physical height range; all its positive
solutions are covered by this argument.

If any prime power is at most six, its cofactor is at least $h/6$.
For $h\ge128$ this is at least $h^{61/100}$, since
$128^{39}\ge6^{100}$. Thus the exponent search can begin with powers
$8,9,25$, and the claimed row range begins at $128+6=134$.

For general $r/s<2/3$, the code chooses a power of two $H$ satisfying

$$
H^{3(s-r)}\ge(H+D)^s,\qquad H^{s-r}\ge D^s.
$$

The ratio $h^{3(s-r)}/(h+D)^s$ is increasing, since it is the product
$h^{2s-3r}(h/(h+D))^s$ of two increasing positive functions. Thus the
first comparison handles every nonminimal CRT solution with $h\ge H$;
the second handles any prime power at most $D$. For $r/s=33/50$ and
$D=6$, the two exact comparisons hold at $H=256$, giving row start 262.

## Exact boundary planes

Suppose no slab is available at an anchor. Remove its three boundary
planes, with shared edges assigned to the first plane containing them.
On the plane with first power fixed at $P$, a violation implies

$$
h/P\le u_p<h^{r/s},\qquad h<P^{s/(s-r)}.
$$

Therefore both other prime powers are less than

$$
P^{s/(s-r)}+D.
$$

This leaves an explicit finite exponent box on the plane. At each exponent
triple in that box, compute the CRT row for each position pattern, and test
its three cofactors by the exact inequality

$$
\max(u_p,u_q,u_\ell)^s<h^r.
$$

Record every violation inside the specified height range. Increasing all
three anchor exponents by one then leaves precisely the unprocessed
orthant. This procedure terminates when one anchor power exceeds the
height cap.

There is a useful exact shortcut on a boundary plane with row bound $L$.
If the other two powers satisfy $QR>L$, only their minimal two-prime CRT
solution can lie in the interval. For each signed difference $d$ with
$0<|d|\le D$, compute

$$
v\equiv dQ^{-1}\pmod R,\quad 0<v<R,\qquad X=Qv.
$$

The possible rows are $n=X+t$, where $t,r_\ell=t+d\in[0,D]$.
Testing $n\bmod P\le D$ supplies the remaining position, and the requirement
that one position be zero is checked directly. When $d=0$, the first
positive physical row is at least $QR>L$, so there is nothing to test.
This shortcut gives exactly the same minimal CRT rows as the three-prime
calculation while avoiding most divisions and large power comparisons.

Both retained computations use $7^3-6^3=127$ allowed position patterns. As a targeted implementation check, an independent enumeration
of the exponent box through $10^4$ reproduced all 121 exceptional
configurations on 37 rows returned by the strip computation at that cap. The corresponding check
for exponent $33/50$ reproduced all 304 configurations on 90 rows.

The retained exceptional rows are inputs to a subsequent binomial
argument. An exception to this cofactor inequality is not itself a
counterexample to Erdős problem 699.

Run the checker with the
[pinned dependencies](../../evidence/assets/erdos_699_interpolation_requirements.txt),
including `gmpy2`, installed in the repository's `.venv/`:

```sh
.venv/bin/python \
  wiki/research/erdos_699/computations/erdos_699_triple_prime_power_strips.py \
  --cap 1000 --exponent 61/100
```

To reproduce the stronger certificate, add `--cap 3000 --exponent 33/50`,
set `--output` to a path under the ignored repository `tmp/`, and compare
the result with the retained `_066_3000.json` certificate on its
mathematical fields.
