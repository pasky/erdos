---
name: problems/integer_sequences/E1063/claims/evidence/verify/white_upper_bound/report
title: Independent examination of White's upper bound for Problem 1063
desc: |
  Independent attempted refutation of White's exact-one-failure upper bound,
  covering the construction, valuations, simultaneous approximation, uniform
  cost, existence, and both asymptotic consequences.
created: 2026-10-15T11:43:59Z
updated: 2026-10-15T11:43:59Z
---

# Independent examination of White's upper bound for Problem 1063

***

## Subject and independence

**Reviewer:** independent mathematical reviewer, disclosed model
gpt-6-astra, reasoning effort max. **Examination date:** 2026-10-15 UTC.
**Frozen subject date:** 2026-10-15 at 05:52:55.296610 UTC.
**Charge:** attempt to refute the entire eventual quantitative bound and both
of its stated asymptotic consequences, including every essential deduction of
the supplied proof. This is a whole-proof examination, not an acceptance or
grading record.

The convention is $n\ge2k$ with exactly one index $0\le j<k$ for which
$n-j$ fails to divide $\binom nk$; it is never relaxed to at most one.

The assessed mathematical subject consists exactly of the following frozen
fragments. The paths identify the source pages, not permission to read their
other sections.

| Subject | Assessed scope and reading depth |
| --- | --- |
| `wiki/problems/integer_sequences/E1063/_index.md` | Statement, lines 23–26; entire supplied fragment read. |
| `wiki/problems/integer_sequences/E1063/claims/2026_07_25_white.md` | Mathematical claim, lines 25–34, and the supplied dependency sentence on line 56; entire supplied fragment read. |
| [Patrick White's immutable README](https://raw.githubusercontent.com/pw/erdos1063-upper-bound/a28481f5b4bda374086533397269c5b550c759b8/README.md) | Theorem, lines 47–54, and Sections 1–5, lines 61–190; entire supplied mathematical text read and examined. |

The first two fragments and their provenance belong with this report under
`wiki/problems/integer_sequences/E1063/claims/evidence/assets/white_review_subject/`.
The README is identified by its immutable external URL. Its copied text is
private: no open license for republication was established, and this report
does not reproduce it. The independent reasoning is retained below, with
canonical home
`wiki/problems/integer_sequences/E1063/claims/evidence/verify/white_upper_bound/report.md`.
There is no computational warrant, keeper program, or executable rerun
requirement. Credit for the source construction and bound remains with Patrick
White and the collaborators credited by the source.

The reviewer neither authored nor collaborated on the subject and had not
built on it in an author-side or consumer-side working context. The
examination began from the commission and prepared neutral extraction. The
extraction's manifest was read before its mathematical files; all supplied
sizes and identities matched before reading. The same frozen bytes, rather
than changing canonical pages, were used throughout. The extraction and its
retained copies were checked again when this report was prepared for delivery.

The mathematical read set was only that manifest and its three enumerated
fragments. Operating reading comprised the supplied root instructions;
`README.md`; the introduction, Claims, Evidence, Tiers, and Project claims in
`docs/anatomy.md`; `docs/verification.md`, `docs/evidence.md`,
`docs/approach_vetting.md`, `docs/math_authoring.md`, and `docs/weaving.md`;
`campaign/AGENTS.md`; `campaign/guides/verification.md`; and Reading in
`campaign/guides/research.md`. The named charter, step instructions,
configuration, template record, and applicable installed operating skills
were also inspected. Other named operating files were checked for identity
without using them as mathematical inputs. Operating examples and links were
not followed into the corpus.

Isolation settings were checked against the supplied operating manifest;
subscriptions were empty after startup and before mathematical reading.
Native configuration outside the read set was accepted on the operator's
attestation. Empty subscriptions support isolation but do not prove what was
read. No author plans, prior reviews, standing text, ledger, or excluded
communications were read. No broad search, external repository access, or web
browsing was performed. No excluded exposure is known. The source version
and range attribution come from the supplied manifest; no separate network
authentication of that extraction is claimed.

## Restatement

The variables $k,n,j,E,S,m$ are integers; logarithms are natural. For
$k\ge2$, let

$$
\mathcal A_k=\left\{n\ge2k:
 \#\left\{j\in\{0,\ldots,k-1\}:n-j\nmid\binom nk\right\}=1\right\}.
$$

The extremal quantity is $n_k=\min\mathcal A_k$. The assertion examined is
that absolute constants $C>0$ and $K$ exist such that, for every $k\ge K$,

$$
n_k\le\exp\left(C\frac{k\log\log k}{\log k}\right).
$$

The two further assertions are $\log n_k=o(k)$ and

$$
\frac{n_k}{k\operatorname{lcm}(1,\ldots,k-1)}\longrightarrow0.
$$

Exactly one failure is essential. The theorem is eventual; it asserts neither
a numerical value of $K$ nor a sharp value of $n_k$. Nonemptiness and
admissibility are examined below, including the definition for small $k$.

## Premises and their actual basis

On 2026-10-15 UTC, reading the entire frozen statement, argument, and
consequence sentences identified **no consumed native L-claim or ledger
row**. This finding was derived from the mathematical text, independently of
its negative dependency sentence. Consequently there is no local tier or
staleness premise to check, no pending native grade, and no batch acceptance
order. No ledger was read.

The following are the precise external interfaces allowed by the commission
and used by the source. Here
$\theta(t)=\sum_{p\le t}\log p$ and
$\psi(t)=\sum_{p^a\le t,\,a\ge1}\log p$.

| Interface | Hypotheses, use, locator, and reading depth |
| --- | --- |
| Legendre valuation formula | For a prime $p$ and integer $u\ge0$, $v_p(u!)=\sum_{a\ge1}\lfloor u/p^a\rfloor$. Used in README Section 1, equation (4), and Section 3.1, equation (11). The formula and its specialization are checked; its elementary proof counts one contribution from each multiple of every $p^a$. No separate external edition was read. |
| Chebyshev estimates | Absolute $c_0,C_0,C_1>0$ and a threshold give $c_0t\le\theta(t)\le C_0t$ and $\pi(t)\le C_1t/\log t$. Section 5 uses the upper bounds for cost and dimension, and the lower bound for eventual admissibility. These are commission-permitted classical premises. Their precise applications are checked; their external proofs and any particular edition remain unread. |
| Higher prime powers | $\psi(k)-\theta(k)=O(\sqrt{k}\log k)$ with an absolute constant, used in Section 5, equation (23). Besides checking this permitted interface, the bound is rederived below by a finite count. No source proof is claimed inspected. |
| Prime number theorem in $\psi$ form | $\psi(t)/t\to1$ as $t\to\infty$, specialized to $t=k-1$ in Section 5's final lcm comparison. This is a commission-permitted classical premise whose external proof was not inspected. It is stronger than the Chebyshev estimates and is not attributed to them. |

The exact source version and locators for these uses are the immutable README
listed above. It supplies no separate bibliographic editions for the
classical facts in the assessed fragments. Reliance is therefore explicitly
on the named, permitted interfaces, not on an independently inspected
literature proof or a source card's coverage label. The verdict below is
relative to these interfaces as authorized; it does not certify their
external proof coverage.

The pigeonhole argument, valuation comparisons, binomial estimate, finite
counting, and asymptotic deductions are examined directly. Kummer's theorem
is not an additional premise: the needed carry identity is derived from
Legendre. Neither Erdős–Selfridge nor a Chinese remainder theorem is used.
The small-$k$ parenthetical about Cambie's construction is unread support for
that particular attribution. It is not needed for the eventual theorem, and
the given finite construction itself supplies nonemptiness as checked below.
No assertion about Cambie's proof is made.

## Weakest steps and full proof coverage

### 1. Valuation coverage and the unique failure

Fix $1\le E<k$, set $r=k-1-E$ and $\rho=\max(E,r)$, and write
$x=Sm$, $n=E+x$, and $W_j=n-j$. In the construction, the small, exceptional,
and regular prime sets are subsets of the primes $p\le k$. This scope is
required by equation (21), the bound $d\le\pi(k)$, and the separate treatment
of $p>k$ in Section 4. An unbounded interpretation of the regular set would
not support the displayed pigeonhole argument. Making this implicit scope
explicit uses the scope already present in those proof sites.

To fix the notation independently, let $y=\max(E,\lfloor\sqrt k\rfloor)$
and, for $p\le k$, define

$$
\begin{aligned}
A_p&=\lfloor\log_p k\rfloor,\\
\sigma_p&=\sum_{a=1}^{A_p}
 \mathbf1_{E\bmod p^a<k\bmod p^a},\\
T_p&=\max_{\substack{0\le j<k\\j\ne E}}v_p(E-j),\qquad
H_p=\max(0,T_p-\sigma_p).
\end{aligned}
$$

Valuations of negative nonzero integers mean valuations of their absolute
values. A prime $y<p\le k$ is exceptional when $k\bmod p<2E$ and regular
otherwise. The factors prescribed for $S$ are $p^{A_p+H_p}$ for small
primes and $p^2$ for exceptional primes, together with
$p_*^{A_{p_*}+1}$ for the selected prime $p_*$ described below.

For a fixed $p\le k$, abbreviate $A=A_p$. At level $q=p^a$, writing
$n=uq+v$ and $k=hq+s$ with $0\le v,s<q$ shows that the number of multiples
of $q$ in the window, denoted $c_{p,a}(n)$, is $h+\mathbf1_{v<s}$.
In particular, the extra term is zero when $q\mid k$. Legendre therefore gives

$$
v_p\binom nk=\sum_{a\ge1}\varepsilon_a,
\qquad
\varepsilon_a=\mathbf1_{n\bmod p^a<k\bmod p^a}.
$$

These sums are finite: when $p^a>n\ge k$, the count and the carry are zero.

Divisibility of $W_j$ requires the valuation inequality for **all** primes,
not for one selected prime. This is the universal interpretation of
Section 1's equations (1)–(2). For a fixed prime its deficit is

$$
v_p\binom nk-v_p(W_j)
=\sum_{a=1}^{A}\varepsilon_a-\min(v_p(W_j),A)
+\sum_{a>A}\left(c_{p,a}(n)-\mathbf1_{p^a\mid W_j}\right).
$$

Every summand in the final sum is nonnegative: it counts multiples elsewhere
in the window. For $p^a>k$ there is at most one multiple, including at a
boundary of the window. Thus a very high power on a coordinate $j\ne E$
cannot invalidate the truncated covering lemma. The equality case $p^a=k$
belongs in the initial sum; it has no extra carry. For $p>k$, the simpler
identity $v_p(k!)=0$ already gives
$v_p\binom nk=\sum_i v_p(W_i)\ge v_p(W_j)$.

This also checks Section 2's obstruction at its stated scope. If $q\mid k$
and $q<k$, then $q\le k/2$ and the window has at least two multiples of $q$.
At least one is not the excused coordinate. Its removal lowers that level's
count below $\lfloor k/q\rfloor$, so a requirement imposed separately at
each prime-power level cannot succeed. This is an obstruction to that
sufficient recipe, not to the valuation sum or to every possible proof.

For the accounting identity, write $E=uq+e$ and $r=vq+f$. Since
$k=E+r+1$, the difference
$\lfloor k/q\rfloor-\lfloor E/q\rfloor-\lfloor r/q\rfloor$ is zero when
$e+f+1<q$ and one otherwise. In the former case $e<k\bmod q$; in the
latter case $e\ge k\bmod q$. Summing gives

$$
A_p-\sigma_p=v_p(D),\qquad
D=\frac{k!}{E!r!}=k\binom{k-1}{E}.
$$

The nonzero differences $E-j$ have absolute values covering the integers
from $1$ through $\rho$. Consequently
$T_p=\lfloor\log_p\rho\rfloor\le A_p$, and
$H_p=\max(0,T_p-\sigma_p)\le A_p-\sigma_p$. This includes $r=0$ and
$\rho=1$, with $T_p=0$ in the latter case. There is no valuation of zero
in $T_p$, because $j=E$ is excluded.

Now check each prime class for $j\ne E$, writing $d_j=E-j$.

| Class | Required valuation coverage |
| --- | --- |
| $p\le y$, $H_p=0$ | The first $A_p$ carries equal $\sigma_p$. If $v_p(d_j)<A_p$, adding $x$, which is divisible by $p^{A_p}$, preserves that valuation. Otherwise $T_p\ge A_p$, so truncation is at most $A_p\le T_p$. In either case the truncated valuation is at most $T_p\le\sigma_p$. Cancellation above $A_p$ is handled by the nonnegative tail just proved. |
| $p\le y$, $H_p>0$ | Since $p^{A_p+H_p}\mid x$ and $p^{A_p+1}>k>|d_j|$, the valuation of $x+d_j$ equals that of $d_j$, at most $T_p$. Each level from $A_p+1$ through $A_p+H_p$ has residue $E<k$ and contributes one carry. Thus the binomial valuation is at least $\sigma_p+H_p=T_p$. |
| $y<p\le k$, exceptional | Here $p>\lfloor\sqrt k\rfloor$, so $p^2>k$ even when $k$ is not a square. The condition $p^2\mid x$ fixes $v_p(x+d_j)=v_p(d_j)\le1$. The $p^2$ level contributes a carry because its residue is $E<k$. |
| $y<p\le k$, regular | The simultaneous argument in Step 2 gives $0<n\bmod p<k\bmod p$. Hence the first carry is one, and $A_p=1$ makes the truncated lemma cover every coordinate at this prime. |
| $p>k$ | The factorial denominator has valuation zero, so these primes cannot cause a divisibility failure. |

These cases cover all primes. A possible concern is the removal of $p_*$
from the regular set. In fact, no regular prime can be chosen as $p_*$:
if $p>y\ge E$ is regular, then $A_p=1$ and
$E<2E\le k\bmod p$, so $\sigma_p=1$ and $v_p(D)=0$.
Thus the selected prime is already in a covered class. Its extra anchor only
strengthens a divisibility condition used above.

It remains to prove a failure rather than just an upper bound on their
number. The integer $D\ge k>1$ has a prime divisor $p_*$, necessarily at
most $k$ since $D$ divides $k!$. Let $A=A_{p_*}$ and
$b=v_{p_*}(x)\ge A+1$, as forced by the augmentation. The first $A$
carries total $\sigma_{p_*}$, and the next $b-A$ carries are one. Write
$x=p_*^b u$ with $p_*\nmid u$. Its next residue satisfies

$$
n\bmod p_*^{b+1}=E+p_*^b(u\bmod p_*),
\qquad k<p_*^b<E+p_*^b(u\bmod p_*)<p_*^{b+1}.
$$

Residues modulo subsequent powers cannot decrease: each adds a nonnegative
multiple of the previous modulus. Thus all later carries vanish, including
when $m$ has made $b$ arbitrarily large. It follows that

$$
v_{p_*}\binom nk=\sigma_{p_*}+b-A
=b-v_{p_*}(D)<b=v_{p_*}(W_E).
$$

The proof for $j\ne E$ and this strict deficit establish exactly
one failure. No theorem asserting that some failure must exist is imported.

### 2. A common multiplier and an admissible integer

Choose $S$ to be the least positive integer satisfying the prescribed prime
power divisibilities. Such an integer exists, being the least common multiple
of a finite list. This makes the size accounting precise; arbitrary extra
factors are not silently charged the same bound. The selection of $p_*$ and
its anchor use only $k$ and $E$, not the unknown $m$.

Let $\mathcal R$ be the finite regular set, $d=|\mathcal R|$, and
$Q=\lceil k/E\rceil\ge2$. Partition $[0,1)^d$ into half-open cubes of side
$1/Q$. Use the $Q^d+1$ points
$P_t=(\{tS/p\})_{p\in\mathcal R}$ for $t=0,\ldots,Q^d$, where braces
denote fractional part. Two lie in one cube. Order their indices and
subtract to obtain $1\le m\le Q^d$.
In every coordinate the difference of fractional parts has absolute value
strictly less than $1/Q$, and it differs from $mS/p$ by an integer. Hence
there is an integer residue $z_p$ of $mS$ modulo $p$ satisfying

$$
|z_p|<\frac pQ\le\frac kQ\le E.
$$

For a regular prime, $k\bmod p\ge2E$, so

$$
1\le E+z_p\le2E-1<k\bmod p<p.
$$

Thus the signed approximation cannot wrap past zero or $p$, and it gives
exactly the carry required in Step 1. The argument needs no independence or
irrationality of the numbers $S/p$, no equidistribution, no coprimality
condition, and no probabilistic assumption. If $d=0$, take $m=1$; the
empty-dimensional assertion is vacuous and the same bound $m\le Q^0$ holds.
In particular, the construction supplies an actual common positive integer,
not a list of separately realizable congruences.

Admissibility survives two checks. The source's eventual check uses
$S\ge\prod_{p\le y}p$ and the permitted lower bound on $\theta(y)$; with
the Section 5 choice of $E$, it gives $S>2k$ for large $k$. There is also a
direct check from the same anchor requirements, which addresses small $k$
without reading another construction. Every prime factor of $k$ is either
small, in which case its exponent in $S$ is at least its exponent in $k$, or
large, in which case it has exponent one in $k$ and is exceptional because
$k\bmod p=0<2E$. Therefore $k\mid S$. The $p_*$ anchor gives
$S\ge p_*^{A_{p_*}+1}>k$. Consequently

$$
S\ge2k,\qquad n=E+Sm\ge2k+1.
$$

This uses only the prescribed divisibilities. It introduces no new
construction or external premise. It also places $n$ in the positive
factorial domain before any use of the carry formula. For any $k\ge2$, the
allowed choice $E=1$ in Sections 3–4 now gives an element of $\mathcal A_k$.
Well-ordering gives its least element $n_k$. This all-$k$ existence check is
an explicit reconstruction from the supplied parameterized construction;
it is not a verification of the Cambie parenthetical or an all-$k$ extension
of the quantitative estimate.

### 3. Uniform cost and each asymptotic consequence

Put $L=\log k$ and $F(k)=k\log L/L$. For sufficiently large $k$, the
specified $E=\lceil k/L^3\rceil$ satisfies

$$
\frac{k}{L^3}\le E\le\frac{2k}{L^3},\qquad
\sqrt k<E<k,\qquad y=E.
$$

All subsequent constants and thresholds are absolute. This is a statement
for every sufficiently large integer, with no selection of a subsequence.

For the small-prime base, all prime powers with exponent at least two have
prime base at most $\sqrt k<y$. Thus

$$
\sum_{p\le y}A_p\log p
=\theta(y)+\psi(k)-\theta(k)
=O\left(\frac{k}{L^3}+\sqrt k\,L\right).
$$

The higher-power estimate can also be seen directly: for each
$p\le\sqrt k$, its contribution $(A_p-1)\log p$ is at most $L$; there
are at most $\lfloor\sqrt k\rfloor$ such primes. No prime-distribution
claim beyond the separately stated bound on $\theta(y)$ is needed for this
term.

For the extra depth, the accounting identity gives
$\sum_{p\le y}H_p\log p\le\log D$. The elementary estimates
$E!\ge(E/e)^E$ and
$\binom{k-1}{E}\le k^E/E!$ yield

$$
\log D\le L+E\log(ek/E)
\le L+\frac{2k}{L^3}(1+3\log L).
$$

For completeness, the factorial inequality follows from
$\sum_{j=1}^E\log j\ge\int_1^E\log t\,dt=E\log E-E+1$.
This bound includes the endpoint $E=1$ and uses no unproved entropy estimate.

For exceptional primes, let $M=\lfloor k/y\rfloor\le L^3$. Each such
prime has a unique positive integer $\ell=\lfloor k/p\rfloor\le M$ and
lies in the interval $((k-2E)/\ell,k/\ell]$. An interval of that length has
at most $2E/\ell+1$ integers. Counting all integers overcounts the primes
and therefore remains an upper bound, regardless of overlaps. It follows
that

$$
\begin{aligned}
\sum_{\substack{y<p\le k\\p\text{ exceptional}}}\log p
&\le L\left(2E\sum_{\ell=1}^{M}\frac1\ell+M\right)\\
&\le L\bigl(2E(1+\log M)+M\bigr)\\
&=O\left(\frac{k\log L}{L^2}+L^4\right).
\end{aligned}
$$

The square anchors double this contribution. Adding the forced prime's
anchor costs at most
$(A_{p_*}+1)\log p_*\le2L$, even if none of that exponent had already been
included. Overlaps between prescriptions only reduce the cost of their least
common multiple. Combining these explicit estimates gives

$$
\log S
=O\left(\frac{k\log L}{L^2}+\sqrt k\,L+L^4\right)
=o(F(k)).
$$

The last equality is stronger than merely $o(k)$. Dividing its three terms
by $F(k)$ gives respectively
$1/L$, $L^2/(\sqrt k\log L)$, and $L^5/(k\log L)$, all tending to zero.
The source's final appeal to its summary $\log S=o(k)$ is compressed:
that summary alone would not imply the quantitative theorem. The explicit
estimates preceding it do, as this substitution shows. No new estimate or
missing essential lemma is needed.

The approximation dimension satisfies $d\le\pi(k)=O(k/L)$, while
$Q\le L^3+1$ and $\log Q=O(\log L)$. Hence

$$
\log m\le d\log Q=O(F(k)).
$$

Since $E<k\le S/2\le Sm/2$, we have $n=E+Sm\le2Sm$ and therefore
$\log n\le\log2+\log S+\log m=O(F(k))$. This supplies absolute $C,K$
for the constructed admissible $n$, and $n_k\le n$ supplies the bound in
the stated extremal units. The original admissibility estimate is valid
as well: $\theta(E)\ge c_0E$ and $E/\log k\to\infty$ imply
$\log S>\log(2k)$ eventually.

For the first consequence, the two-sided inequality

$$
0\le\frac{\log n_k}{k}
\le C\frac{\log\log k}{\log k}
$$

forces $\log n_k=o(k)$; it is not an inference from a finite set of $k$.
For the second, prime factorization gives the exact identity
$\log\operatorname{lcm}(1,\ldots,k-1)=\psi(k-1)$. The permitted prime
number theorem gives $\psi(k-1)=k+o(k)$, including the shift by one.
Consequently

$$
\log\frac{n_k}{k\operatorname{lcm}(1,\ldots,k-1)}
=\log n_k-\log k-\psi(k-1)=-k+o(k).
$$

Thus the ratio tends to zero, and the source's stated exponential decay on
the $k$ scale is justified. Both consequences have been checked in their own
variables, rather than inferred from a general description of the construction.

## Strongest attempted refutation and other attacks

The strongest attack was to make the prime-power argument lose exactness:
cancellation in a nonexcused coordinate might create a second failure, or
additional carries above the forced valuation might remove the claimed
failure at $E$. Both would invalidate the target even if all size estimates
were sound.

A concrete cancellation test within the specified construction is
$k=7$, $E=2$, $S=44100=2^2\cdot3^2\cdot5^2\cdot7^2$, and $m=1$.
Here $D=105$ permits $p_*=3$, all large primes are exceptional, and the
small prime $2$ has $A_2=T_2=\sigma_2=2$ and $H_2=0$.
For $j=6$, the difference $E-j=-4$ has valuation two but

$$
n-j=44096=2^6\cdot689
$$

has valuation six. A proof equating these valuations in the $H_p=0$ case
would fail on this exact input. The actual truncated lemma survives: at
$n=44102$, the six carry levels for $p=2$ are all present. The residues
modulo $2,4$ are $0,2$, and modulo $8,16,32,64$ they are all $6$; the
residue modulo $128$ is $70$, so no subsequent level contributes. This
is exposed exact arithmetic, not a computational or finite-to-infinite
warrant.

For the exceptional coordinate, a separate deletion calculation attacks the
source's assertion about the infinite tail without assuming it. At $p_*$,
we have $p_*^b>k>|E-j|$ for every $j\ne E$. Therefore

$$
\sum_{j\ne E}v_{p_*}(n-j)
=\sum_{j\ne E}v_{p_*}(E-j)=v_{p_*}(E!r!).
$$

Subtracting the factorial denominator gives the exact identity

$$
v_{p_*}(n-E)-v_{p_*}\binom nk=v_{p_*}(D)>0.
$$

This confirms the strict failure through a finite product identity, as well
as through the carry-tail proof in Step 1. Increasing $v_{p_*}(m)$ does not
alter the deficit. These two derivations do not invoke a theorem about the
existence of a nondivisor.

Other attempted failure mechanisms were checked as follows.

- **Signed residues crossing the permitted interval:** the strict inequality
  $|z_p|<E$ and the full margin $k\bmod p\ge2E$ place $E+z_p$ in
  $[1,2E-1]$, so neither endpoint can produce a lost carry.
- **A prime omitted when $p_*$ is removed:** a regular prime has
  $A_p-\sigma_p=0$, so it cannot be $p_*$. Primes above $k$ are covered
  directly by the denominator valuation.
- **A nonexistent or too-small construction:** the finite pigeonhole gives
  a positive $m$ even for $d=0$, while $k\mid S$ and $S>k$ give
  $n\ge2k$. No separate congruence solutions are being composed without a
  common witness.
- **An asymptotic weakening hidden in the cost summary:** $o(k)$ alone would
  be insufficient, since, for example, $k/\sqrt{\log k}$ is $o(k)$ but
  larger than $F(k)$. The explicit anchor estimates instead give $o(F(k))$.
- **A stronger consequence than the proof supplies:** each limit is derived
  separately, and the lcm limit's stronger external premise is identified.

The reconstructions above make explicit the prime universe, the least anchor
choice, empty-dimensional pigeonhole, elementary accounting, all-$k$
nonemptiness from the same construction, and the substitution of explicit
cost estimates. They neither modify the frozen subject nor replace an
unsupported essential step with a different proof. No missing essential
lemma was found in the commissioned theorem and consequences.

## Checklist

### Canonical failure modes

| Item | Examination verdict |
| --- | --- |
| Almost all quietly upgraded to all | No failure found. Step 3 supplies one absolute threshold and a construction for every integer above it; no density statement is substituted. |
| Induction that presupposes termination | Inapplicable: no induction or unbounded search is used. Pigeonhole uses the explicitly finite set of $Q^d+1$ points. |
| Probabilistic or averaging heuristics presented as proofs | Inapplicable: the approximation is deterministic pigeonhole, and the exceptional-prime estimate is an upper count over all relevant integer intervals. |
| Circular use of a statement equivalent to the claim | No failure found. $S$, $p_*$, and the finite points are defined from $k,E$ before any exact-one-failure integer is assumed. The deficit is proved rather than imported. |
| Exceptional sets dropped from density arguments | No failure found. Every prime at most $k$ enters a small, exceptional, or regular case, and primes above $k$ are handled separately. No density argument is used. |
| Finite verification cited as more than base-case coverage | No failure found. The proof is symbolic for the stated range; the $k=7$ arithmetic only exposes the cancellation surface and is not extrapolated. |
| Convergence of a relaxed or averaged system standing in for actual objects | No failure found. The common integer $m$ realizes all required residues; Step 1 transfers those residues to divisibility of the actual binomial coefficient. |

### Named patterns

| Item | Examination verdict |
| --- | --- |
| Model-class transport instead of entailment | Axiom-system classification is inapplicable. The relevant entailment is checked explicitly: carry inequalities imply each integer divisibility, while a strict deficit implies its failure. No parallel vocabulary substitutes for this implication. |
| Uniformity over an infinite family asserted from finitely many instances | No failure found. The constants in the allowed prime estimates and in Step 3 are absolute; the parameter $k$ is not bounded by a checked sample. |
| Extremal claims are audited in the claim's own units | No failure found. Nonemptiness of $\mathcal A_k$ and its least element are supplied, and an admissible constructed $n$ gives $n_k\le n$. There is no claim of sharpness or attainment of a lower estimate. |
| Consequence sentences are claim surfaces | Both displayed asymptotic consequences and the stated exponential ratio decay are separately derived in Step 3. The unread Cambie attribution is expressly outside the warrant; all-$k$ existence follows directly from the same supplied construction. |
| Carry hypotheses actually used by a quantified argument | No failure found. Positivity, integer domains, $1\le E<k$, finite prime universe, $p^2>k$, the regular margin, and eventual $E\asymp k/(\log k)^3$ are retained at their uses. |
| A composition inherits its unproved premises | No missing internal interface found. The carry, anchor, approximation, and size implications are supplied. The external classical interfaces remain explicit, including the stronger premise for the lcm comparison. |
| Reproducibility notes are claims | No executable rerun or checker-coverage claim is used. The independent derivations and the exact cancellation example are retained here; source checker material was outside the subject. Computational reproduction is inapplicable. |
| Verifier quotations are claims | Inapplicable to this blind subject: prior verdicts and standing prose were excluded and not read. This report makes no claim about an earlier verifier's ruling. Their fidelity is for the separate grader or integrator where relevant. |
| Verdict words spelled in full | The mathematical verdict is written as **refutation-failed**. A proof defect would instead be reported as **proof defective; statement unresolved**, and an actual disproof as **refuted-as-stated**; no ambiguous abbreviation is used. |
| Certified-bracket functions fail loudly | Inapplicable: no numerical enclosure, iterative approximation routine, floating-point value, or numerical stopping cap is used. The approximation proof is exact finite pigeonhole. |
| A harness leg with no failing input is decoration | Inapplicable: there is no computational evidence leg. The explicit $k=7$ example would refute the stronger but false valuation-equality shortcut; the actual lemma survives it. |
| A gate that reads caches instead of re-running is defective | Inapplicable: no gate result, cached success output, or source checker run carries the mathematical verdict. |

The neighboring disciplines are also respected: there are no statistical
samples for which independence or correlation must be inferred, and every
retained argument is matched to its stated scope. The finite arithmetic
example is not assigned universal coverage.

### Erdos-specific checklist

| Item | Examination verdict |
| --- | --- |
| Quantifiers and scope | No failure found. Exactly one failure, $n\ge2k$, all sufficiently large $k$, and both limits retain their stated quantifiers. Separate all-$k$ existence does not strengthen the quantitative bound's range. |
| Circularity | No failure found. The finite construction and strict valuation deficit do not assume existence of $n_k$; they establish nonemptiness before the minimum is used. |
| Model and convention changes | No failure found. Least nonnegative residues and signed approximation residues are distinguished; their transfer is proved. The positive integer binomial coefficient and its original $k$ coordinates are used throughout. |
| Finite and statistical overreach | No failure found. No statistical claim or finite extrapolation is made; all universal conclusions follow from algebra and the permitted asymptotic interfaces. |
| Uniformity | No failure found. Ceiling errors, dimension, least anchor cost, the forced prime, and each residual term are bounded with absolute constants. No exchange of nonuniform limits is used. |
| Extremal conclusions | No failure found. Existence and well-ordering justify $n_k$, and the construction is compared directly with that minimum. No optimality claim is inferred. |
| Consequences and composition | No failure found. Every prime class, the positive multiplier, admissibility, and each asymptotic consequence have an explicit connecting deduction. The prime-number-theorem use is separate from Chebyshev. |
| Computation | Executable computation is inapplicable. Arithmetic and estimates are exact mathematical derivations; the exposed integer example has explicitly finite diagnostic scope. |
| Reproduction | Computational replay is inapplicable. The report retains its definitions, derivations, example, and exact source locators; no unavailable program or private output is a mathematical premise. |
| Source and verdict fidelity | The entire permitted Theorem and Sections 1–5 were examined at the frozen version. Routine reconstruction is disclosed, prior verifier rulings are not characterized, and no review is claimed for omitted source material or later revisions. |

This is a single noncomputational examination. A computational batch's
structurally different reproduction leg and a second cycle's disjoint-attack
requirement are inapplicable; no extra review cycle or unseen prior attack
record is claimed.

## Verdict and grading

**refutation-failed.** The supplied argument survives this attempted
refutation of the whole commissioned quantitative theorem and both asymptotic
consequences, with the explicitly permitted classical interfaces at the
reading depths stated above. The examination covers existence and
admissibility, every prime and prime-power case, the unique failed divisor,
the common multiplier, all quantitative costs, and the minimum's asymptotic
consequences. No counterexample or unsupported essential step was found.

The quantitative conclusion uses the source's explicit cost estimates, not
the weaker $o(k)$ summary alone. The prime universe and least anchor choice
are made explicit, and the additional nonemptiness check is derived from
the very same prescribed factors. These are disclosed reconstructions, not
an assessment of repaired source bytes.

The warrant excludes source checker code, finite checker claims, prior
reviews, Cipollini's proof, LEAP developments, Cambie's construction, and any
statement outside the supplied Theorem and Sections 1–5. It does not
independently certify the unread external proofs of Chebyshev estimates or
the prime number theorem. It provides no numerical optimal constants, no
Lean verification, no report grade, and no alteration of tier or catalog
standing. A separate eligible grader must judge the report's contract and
independence before any acceptance rests on it.
