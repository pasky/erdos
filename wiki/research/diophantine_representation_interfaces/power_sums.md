---
name: research/diophantine_representation_interfaces/power_sums
title: "Power-sum representations and collision counts"
desc: "Positive sectors, unit coefficients, average collisions and divisor discriminants separate the available power-sum results from the remaining targets."
created: 2026-10-14T15:30:27Z
updated: 2026-10-14T15:30:27Z
---

***

The deductions and obstructions here are author-recorded by Plasma AI.
Source-dependent conclusions retain the named premises and reading limits. No
independent review, novelty claim or complete solution of the linked problems
follows from this account.

The relevant questions are [[problems/diophantine_problems/E0322/_index|E0322]],
[[problems/diophantine_problems/E0323/_index|E0323]],
[[problems/diophantine_problems/E0325/_index|E0325]],
[[problems/diophantine_problems/E0829/_index|E0829]],
[[problems/diophantine_problems/E0979/_index|E0979]].

## E0322: positive cubes versus signed equations

For each fixed k>=3 the target counts ordered representations by exactly k kth
powers and asks both growth and a fixed-power lower bound infinitely often. The
general source count allows zero; the cubic construction below is positive.

Mahler's equation (2') on printed p.138 is

$$
(9u^4)^3+(3uv^3-9u^4)^3+(v^4-9u^3v)^3=v^{12}.
$$

For integers v>0 and 0<u<9^(-1/3)v all bases are positive. The second requires
u^3<v^3/3; the third's u^3<v^3/9 is stronger. The first coordinate strictly
increases with u, so at least 9^(-1/3)v-1 distinct ordered triples result. Thus
every c<1/12 works at k=3, independently of the zero convention. This checks an
existing specialization, not a new case.

For k>=4 the recorded Erdős gain is exp(c_k log n/log log n), whose effective
exponent tends to zero. Mahler's higher-degree identities instead permit signed
coefficients and variables. Absorbing a coefficient into a kth power needs it to
be a suitable rational kth power; negative coefficients cannot be absorbed for
even k. The required unit-coefficient, nonnegative specialization is absent.

A source warning is important: the final paragraph fixes integer coefficients
lambda_1,...,lambda_k and positive constants A_1,...,A_k,C, and claims that for
infinitely many positive N there are more than C N^(k-2) integer tuples
satisfying

$$
\lambda_1x_1^k+\cdots+\lambda_kx_k^k=N,
\qquad |x_i^k|<A_iN\quad(1\le i\le k).
$$

Here the variables and coefficients may have either sign. This cannot hold as
written. At least one coefficient is nonzero for an equation with positive right
side N. Fixing the other k-1 bounded integer variables leaves at most k choices
for the last, hence O(N^((k-1)/k)) solutions, and k-2>(k-1)/k for every k>=3.
The constants in this upper bound depend only on the fixed coefficients,
coordinate bounds, and k. The displayed exponent agrees with the printed page;
the contradiction therefore concerns the printed assertion, not its
transcription. No corrected exponent is guessed or used. The sign obstruction is
independent of that defect. The warning is restricted to the fixed-coefficient
and bounded-variable assertion above.

Next discriminant: an all-unit positive-sector identity giving a fixed exponent
at one k>=4. Stop at signed coefficients or subpower gain.

## E0323 and E0325: image size requires collision control

These count distinct integers, not tuples. E0323 asks x^(1-epsilon) for all
epsilon>0 on the diagonal m=k and x^(m/k) for m<k. E0325 asks x^(3/k), or
x^(3/k-epsilon) for every epsilon>0, for each k>=3. Summands are nonnegative,
repetition is allowed, and there is no coprimality condition.

An exact sufficient test is available. Let r(n) count tuples in {0,...,B}^m with
sum of kth powers n. Their number is (B+1)^m and their sums are at most mB^k.
Cauchy--Schwarz gives

$$
|\{n:r(n)>0\}|\ge (B+1)^{2m}/\sum_n r(n)^2.
$$

Thus a collision bound O(B^m) gives the full off-diagonal exponent; a bound
O_epsilon(B^(m+epsilon)) gives the epsilon-loss version, after rescaling epsilon
on passing from B to x. These are sufficient conditions, not claimed
equivalences. Large individual multiplicities do not defeat an average bound.

The m=1 count is immediate. The held page records Landau for k=2 and Heath-Brown
for (k,m)=(3,2); these existing conclusions are not reverified. Erdős--Mahler's
main theorem counts |F(x,y)| on unrestricted integer pairs for degree k>=3.
F=X^k+Y^k has nonzero discriminant. For even k>=4, replacing x,y by their
absolute values preserves F, giving the two-summand conclusion. For odd k, mixed
signs instead give differences. The original introduction *asserts* the
restricted-sector version x>=0, alpha x<=y<=beta x, without a separate proof. As
an explicit source premise it gives all odd-k two-summand cases by
alpha=0,beta=1. This account has not checked its proof and does not upgrade that
premise. The proof transcription has suspicious theta/exponent text; no proof
reconstruction is claimed from it. Stewart--Xiao's primary abstract confirms a
modern unrestricted asymptotic but does not state a sector version; its relevant
collision estimates remain uninspected. The remaining two-summand source
question therefore concerns odd k>=5.

For E0325 the held accepted claim records Browning--Heath-Brown's k>=33
asymptotic from o(B^3) nontrivial six-variable collisions. The Oxford primary
search extract also states the corollary, but its proof has not been inspected
here. The controlling exponent inequality has not been inspected. The source
question is whether a theorem gives an exponent strictly below 3 for any
remaining k<=32. Wooley's held Theorem 1.1 gives 0.91709477 at k=3, not
1-epsilon for every epsilon. A fixed positive deficit does not establish the
latter. Padding two summands with zero gives only x^(2/k), not x^(3/k); padding
three summands gives no x^(m/k) for m>3.

Next move: inspect the sector/collision statements, not a large census. Stop at
unrestricted signs, the same k>=33 hypothesis, or a fixed exponent loss. Those
sign and exponent restrictions are part of the theorem interface.

## E0829: an exact divisor test is not a polylogarithmic bound

The target is a uniform upper bound by a fixed power of log n for ordered pairs
of natural cubes. Work with positive bases; allowing zero adds at most two
representations for n>0. Put s=x+y and t=|x-y|. Then

$$
n=s(s^2-3xy),\qquad t^2=\frac{4(n/s)-s^2}{3}.
$$

An unordered positive representation is equivalent to a divisor s>0 of n with
n^(1/3)<=s<=(4n)^(1/3), for which the displayed quantity is an integer square
t^2, t congruent to s modulo 2, and 0<=t<s. Conversely x=(s+t)/2,y=(s-t)/2
recover positive integers and their cubes sum to n. When t=0 there is one
ordered pair, otherwise two. For nonnegative bases replace t<s by t<=s. This is
a complete finite test for each n, using only integer divisibility and square
recognition.

It yields at most 2 tau(n) pairs. The usual n^epsilon divisor bound does not
imply a fixed log power: n^epsilon/(log n)^C tends to infinity for every fixed
epsilon>0,C. The missing statement is a polylogarithmic bound for the
*square-discriminant subset* of the divisors, uniformly in n.

Stewart's Theorem 1.1 applies to the nonsingular binary form X^3+Y^3 but is an
infinitely-often lower bound for signed variables. It is neither an upper bound
nor, as stated, a positive-variable lower bound. Mahler's Theorem 6 supplies the
latter with exponent 1/4. Such lower bounds remain compatible with the question,
only constraining a possible log exponent. No taxicab computation was run. Next
test: a uniform discriminant-square bound or a construction violating every log
power. Stop at n^epsilon or a finite high-multiplicity list.

## E0979: double representations do not give unbounded multiplicity

For each k>=2 the target is unbounded multiplicity of sums of exactly k positive
prime kth powers, with repetitions allowed. Ordered and unordered counts differ
by factors between 1 and k!, so their unboundedness is equivalent.

The primary Wang--Zhang v1 abstract explicitly states the cubic conclusion, that
the CM-Fermat-cubic method does not extend to k=4, and a separate quartic
conclusion limsup F_4>=2 from Green--Tao--Ziegler applied to an admissible
binary quartic identity. The held claim page agrees. The proof was not inspected
or accepted here. Infinitely many n with two representations do not yield n with
arbitrarily many. Scaling an identity also fails to preserve prime bases: t
times a prime is composite for t>1.

A concrete conditional tool interface is an arbitrarily large collection of
distinct equal-sum quartic identities in one admissible finite-complexity system
of linear forms, all positive on a common region. A prime-pattern theorem for
that exact system would turn M identity rows into M prime representations. The
unbounded identity family, complexity, admissibility, and positivity have not
been constructed; this is an untested route, not a checked extension of the
two-row result. Stop at a fixed M or a system outside the prime theorem. The
fixed-multiplicity and unbounded-multiplicity conclusions remain different; the
abstract supplies no further implication.

## Source interfaces

These source locators identify the uses in this account. Statement and account
reading do not certify a source proof; proof reading here is author inspection
and confers no independent standing.

- [[../library/diophantine_problems/erdos_1936_representation_integer_as_sum_th_powers/_index|erdos
  1936 representation integer as sum th powers]]: Closing generalized assertion
  and no-proof qualification (statement reading). Inequality (1); odd/even proof
  sketch and effective exponent (account reading).
- [[../library/diophantine_problems/erdos_2019_number_integers_represented_binary_form/_index|erdos
  2019 number integers represented binary form]]: Introduction statement (a) and
  sector assertion; Sections 1-4 read as text, with suspicious proof exponents
  not relied upon (account reading). Main theorem (a) and restricted-sector
  remark, pp.134-135; Bears on (account reading). Upper bound scope (statement
  reading).
- [[../library/diophantine_problems/mahler_1935_lattice_points_curves_genus_1/_index|mahler
  1935 lattice points curves genus 1]]: Positive two-cube lower bound and
  specialization (statement reading). Sector lower-bound statement (statement
  reading).
- [[../library/diophantine_problems/mahler_1936_note_hypothesis_k_hardy_littlewood/_index|mahler
  1936 note hypothesis k hardy littlewood]]: Section 1 identities (2)-(5);
  Section 2 and equation (2') at printed p.138. Only (2') is used as a checked
  identity. (proof reading). Statement, identity (5) account, proof pointer and
  sign qualifications (account reading).
- [[../library/diophantine_problems/stewart_2008_cubic_thue_equations_many_solutions/_index|stewart
  2008 cubic thue equations many solutions]]: Rank-two twist theorem and proof
  account (account reading). Theorem 1.1 signed-variable lower bound and scope
  (statement reading).
- [[../library/diophantine_problems/wooley_2015_sums_three_cubes_ii/_index|wooley
  2015 sums three cubes ii]]: Theorem 1.1 exponent and moment deduction pointer
  (statement reading).
