---
name: problems/integer_sequences
title: Sequences and Densities of Integers
desc: |
  Problems on sets and sequences of integers defined by divisibility,
  coprimality, gcd or lcm, or residue conditions, or by avoiding a pattern,
  asking for their density, counting function, gaps or growth, including
  covering-congruence and sieve questions.
created: 2026-09-04T09:17:27Z
updated: 2026-10-13T13:29:21Z
---

# Sequences and Densities of Integers

[[problems/_index|..]]

[[problems/integer_sequences/E0012/_index|E0012/]]: Asks how large an infinite
set with no element dividing the sum of two larger elements can be, in terms of
its counting function, its density and its reciprocal sum. The first two
questions are answered by a refereed construction of 2026, and the
reciprocal-sum question is open.

[[problems/integer_sequences/E0013/_index|E0013/]]: Asks whether a subset of
$\{1,\ldots,N\}$ with no element dividing the sum of two larger elements has
size at most $N/3+O(1)$. Bedert proved it in 2023 and showed that $\lceil
N/3\rceil$ is the exact bound for large $N$.

[[problems/integer_sequences/E0025/_index|E0025/]]: Asks whether the integers
avoiding a chosen residue class for each modulus in an increasing sequence
always have a logarithmic density.

[[problems/integer_sequences/E0038/_index|E0038/]]: Asks whether a set that is
not an additive basis can, for every set $A$ of Schnirelmann density
$\alpha\in(0,1)$ and every $N$, supply a shift $b$ such that $A\cup(A+b)$ has at
least $(\alpha+f(\alpha))N$ elements up to $N$, with $f(\alpha)>0$; proved in 2026.

[[problems/integer_sequences/E0121/_index|E0121/]]: Asks whether the largest
subset of $\{1,\ldots,N\}$ in which no $5$ distinct elements, or more generally
no fixed odd number at least $5$ of them, multiply to a square has size
$(1-o(1))N$. Tao (2024) disproved it for products of any fixed number $k\geq4$
of elements.

[[problems/integer_sequences/E0131/_index|E0131/]]: Asks for an estimate of the
largest subset of $\{1,\ldots,N\}$ in which no element divides the sum of any
distinct others. The question whether it exceeds $N^{1/2-o(1)}$ is answered no,
and one unreviewed claim asserts the order $N^{1/5+o(1)}$.

[[problems/integer_sequences/E0145/_index|E0145/]]: Asks whether the average of
the $\alpha$-th powers of the gaps between consecutive squarefree numbers up to
$x$ has a limit for every $\alpha\geq0$.

[[problems/integer_sequences/E0208/_index|E0208/]]: Asks whether the gap after
the squarefree number $s_n$ is $\ll_\epsilon s_n^{\epsilon}$ for every
$\epsilon>0$, and whether it is at most $(1+o(1))\frac{\pi^2}{6}\frac{\log
s_n}{\log\log s_n}$.

[[problems/integer_sequences/E0220/_index|E0220/]]: Asks whether the sum of the
squared gaps between consecutive integers below $n$ that are coprime to $n$ is
$\ll n^2/\phi(n)$.

[[problems/integer_sequences/E0222/_index|E0222/]]: Asks for good upper and
lower bounds on the gaps between consecutive integers that are sums of two
squares.

[[problems/integer_sequences/E0235/_index|E0235/]]: Asks whether the
distribution of normalized gaps between the integers coprime to the product of
the first $k$ primes tends to a continuous limiting function.

[[problems/integer_sequences/E0253/_index|E0253/]]: Asks whether a sequence with
$a_{i+1}/a_i\to1$, whose sums of distinct terms meet every arithmetic
progression infinitely often, must represent every large integer as such a sum.

[[problems/integer_sequences/E0254/_index|E0254/]]: Asks whether a set $A$ with
$|A\cap(x,2x]|\to\infty$ and $\sum_{n\in A}\{\theta n\}=\infty$ for every
$\theta\in(0,1)$, where $\{\cdot\}$ is the distance to the nearest integer,
represents every large integer as a sum of distinct elements.

[[problems/integer_sequences/E0329/_index|E0329/]]: Asks how large
$\limsup_{N\to\infty}|A\cap\{1,\ldots,N\}|/N^{1/2}$ can be for an infinite Sidon
set $A\subseteq\mathbb{N}$.

[[problems/integer_sequences/E0332/_index|E0332/]]: Asks which conditions on a
set of integers ensure that the differences occurring infinitely often in it
have bounded gaps.

[[problems/integer_sequences/E0341/_index|E0341/]]: Asks whether the sequence
that extends a finite set by repeatedly adding the least larger integer that is
not a sum of two earlier terms has eventually periodic differences.

[[problems/integer_sequences/E0342/_index|E0342/]]: Asks what can be said about
the sequence starting $1,2$ in which each later term is the least larger integer
that is uniquely a sum of two earlier terms, in particular about its density and
its gaps.

[[problems/integer_sequences/E0356/_index|E0356/]]: Asks whether there is $c>0$
such that, for all large $n$, some integers $a_1<\cdots<a_k\leq n$ have at least
$cn^2$ distinct sums of consecutive terms.

[[problems/integer_sequences/E0357/_index|E0357/]]: Asks how fast the largest
number $f(n)$ of integers up to $n$ with all sums of consecutive terms distinct
grows, and whether $f(n)=o(n)$.

[[problems/integer_sequences/E0359/_index|E0359/]]: Asks what can be said about
the density of the sequence starting at $n$ in which each later term is the
least integer that is not a sum of consecutive earlier terms.

[[problems/integer_sequences/E0360/_index|E0360/]]: Asks how fast $f(n)$ grows,
the least number of classes into which $\{1,\ldots,n-1\}$ can be partitioned so
that $n$ is never a sum of distinct members of one class.

[[problems/integer_sequences/E0361/_index|E0361/]]: Asks for the size of the
largest $A\subseteq\{1,\ldots,\lfloor cn\rfloor\}$ with no subset summing to
$n$, and whether this size depends on $n$ in an irregular way.

[[problems/integer_sequences/E0375/_index|E0375/]]: Asks whether any $k$
consecutive composite integers $n+1,\ldots,n+k$ can be assigned distinct primes
$p_1,\ldots,p_k$ with $p_i\mid n+i$.

[[problems/integer_sequences/E0402/_index|E0402/]]: Asks for a proof that every
finite set $A$ of integers has two members $a,b$ with $\gcd(a,b)\leq a/|A|$.

[[problems/integer_sequences/E0421/_index|E0421/]]: Asks whether there is an
increasing sequence of density $1$ whose products of blocks of consecutive terms
are all distinct. Chojecki and Sneiderman answered yes in July 2026, in work the
site accepts but that is not refereed.

[[problems/integer_sequences/E0422/_index|E0422/]]: Asks how the sequence given
by $f(1)=f(2)=1$ and $f(n)=f(n-f(n-1))+f(n-f(n-2))$ behaves, and whether it
misses infinitely many integers.

[[problems/integer_sequences/E0423/_index|E0423/]]: Asks for the asymptotic
behaviour of the sequence with $a_1=1$, $a_2=2$ in which each later term is the
least integer above the previous one that is a sum of at least two consecutive
earlier terms.

[[problems/integer_sequences/E0424/_index|E0424/]]: Asks whether the integers
that eventually appear, starting from $2,3$ and repeatedly appending every
$a_ia_j-1$ with $i\neq j$, have positive density, read as positive lower density
following the site's curator.

[[problems/integer_sequences/E0429/_index|E0429/]]: Asks whether every
sufficiently sparse $A\subseteq\mathbb{N}$ that misses a residue class modulo
every prime has a shift $n+A$ made up only of primes; disproved by Weisenberg
(2024), who built arbitrarily sparse admissible sets with no prime shift.

[[problems/integer_sequences/E0430/_index|E0430/]]: Asks whether, for all large
$n$, the decreasing sequence with $a_1=n-1$ and each $a_k$ the greatest integer
in $[2,a_{k-1})$ whose prime factors all exceed $n-a_k$ must contain a composite
term.

[[problems/integer_sequences/E0432/_index|E0432/]]: Asks how dense $A+B$ can be
for infinite sets $A,B\subseteq\mathbb{N}$ when the elements of $A+B$ are
pairwise coprime.

[[problems/integer_sequences/E0436/_index|E0436/]]: Asks whether $\Lambda(k,2)$
is finite for all $k$ and $\Lambda(k,3)$ for all odd $k$, and how large they
are, where $\Lambda(k,m)$ is the limsup over primes $p$ of the least start of
$m$ consecutive $k$th power residues modulo $p$.

[[problems/integer_sequences/E0438/_index|E0438/]]: Asks how large
$A\subseteq\{1,\ldots,N\}$ can be if $A+A$ contains no square.

[[problems/integer_sequences/E0440/_index|E0440/]]: Asks whether $A(x)\ll
x^{1/2}$, where $A(x)$ counts the consecutive pairs of an infinite
$A\subseteq\mathbb{N}$ with $\mathrm{lcm}(a_i,a_{i+1})\le x$, and how large
$\liminf A(x)/x^{1/2}$ can be; both answered by Erdős and Szemerédi in 1980.

[[problems/integer_sequences/E0441/_index|E0441/]]: Asks for the size of the
largest $A\subseteq\{1,\ldots,N\}$ with $\mathrm{lcm}(a,b)\le N$ for all $a,b\in
A$, and whether Erdős's construction attains it. Chen showed the size is
$\sim(9N/8)^{1/2}$, and Chen and Dai showed the construction is not optimal for
infinitely many $N$.

[[problems/integer_sequences/E0442/_index|E0442/]]: Asks whether, when
$\sum_{n\in A\cap[1,x)}1/n$ grows faster than $\log\log x$, the sum of
$1/\mathrm{lcm}(a,b)$ over pairs $a<b$ in $A$, divided by the square of that
sum, must tend to infinity; disproved by Tao, whose construction also gives the
optimal growth threshold.

[[problems/integer_sequences/E0451/_index|E0451/]]: Asks for estimates of $n_k$,
the least integer $>2k$ such that $\prod_{1\le i\le k}(n_k-i)$ has no prime
factor in $(k,2k)$. A 2026 preprint claims that $n_k$ grows faster than any
power of $k$, and an elementary bound makes it at most exponential in $k$.

[[problems/integer_sequences/E0453/_index|E0453/]]: Asks whether, for all large
$n$, some $i<n$ satisfies $p_n^2<p_{n+i}p_{n-i}$, where $p_k$ is the $k$th
prime.

[[problems/integer_sequences/E0455/_index|E0455/]]: Asks whether every sequence
of primes $q_1<q_2<\cdots$ with non-decreasing gaps must satisfy
$q_n/n^2\to\infty$.

[[problems/integer_sequences/E0457/_index|E0457/]]: Asks whether some
$\epsilon>0$ gives infinitely many $n$ such that every prime
$p\le(2+\epsilon)\log n$ divides $\prod_{1\le i\le\log n}(n+i)$; yes, by a 2026
AI construction the site accepted. Erdős's 1979 form, which asks the opposite,
has the answer no.

[[problems/integer_sequences/E0460/_index|E0460/]]: Asks whether
$\sum_{0<a_i<n}1/a_i\to\infty$ for the greedy sequence with $a_0=0$, $a_1=1$ and
each $a_k$ the least integer above $a_{k-1}$ with $n-a_k$ coprime to every
earlier $n-a_i$, and the same for two complementary parts of the sum.

[[problems/integer_sequences/E0467/_index|E0467/]]: Asks whether, for all large
$x$, one can choose a residue class for each prime $p\le x$ and split these
primes into two non-empty sets so that every $n<x$ lies in the chosen class of
some prime in each set; open, with one sentence of the 1980 monograph as its
only source.

[[problems/integer_sequences/E0471/_index|E0471/]]: Asks whether some finite set
of primes grows without bound when one repeatedly adds every prime that is a sum
of three distinct members; yes, by Vinogradov's three-primes theorem, an
observation the site accepted.

[[problems/integer_sequences/E0472/_index|E0472/]]: Asks whether some finite
starting sequence of primes $q_1<\cdots<q_m$ makes infinite the sequence in
which each next term $q_{n+1}$ is the least prime of the form $q_n+q_i-1$.

[[problems/integer_sequences/E0473/_index|E0473/]]: Asks whether the positive
integers can be permuted so that every two consecutive terms sum to a prime;
yes, by an unpublished construction of Odlyzko reported by Erdős and Graham in
1980 and accepted by the site.

[[problems/integer_sequences/E0481/_index|E0481/]]: Asks whether, when $\sum_i
1/a_i>1$, iterating the maps $x\mapsto a_ix+b_i$ from $A_1=(1)$ must produce
some $A_k$ with repeated elements; yes, by Klarner's 1982 theorem, its 2022
extension and a 2025 thread proof.

[[problems/integer_sequences/E0487/_index|E0487/]]: Asks whether every set of
integers of positive density contains three distinct members $a,b,c$ with $c$
the least common multiple of $a$ and $b$; true by Kleitman's union-free theorem,
attested here second-hand.

[[problems/integer_sequences/E0488/_index|E0488/]]: Asks whether, for a finite
set $A$ with set of multiples $B$, $|B\cap[1,m]|/m<2|B\cap[1,n]|/n$ for all
$m>n\ge\max(A)$; a counterexample claim of September 2026 is pending and
unreviewed.

[[problems/integer_sequences/E0489/_index|E0489/]]: Asks whether, for
$A\subseteq\mathbb{N}$ with $|A\cap[1,x]|=o(x^{1/2})$ and $b_1<b_2<\cdots$ the
integers divisible by no member of $A$, the limit of
$\frac1x\sum_{b_i<x}(b_{i+1}-b_i)^2$ exists and is finite.

[[problems/integer_sequences/E0490/_index|E0490/]]: Asks whether
$A,B\subseteq\{1,\ldots,N\}$ with all products $ab$ distinct must satisfy
$|A||B|\ll N^2/\log N$; proved by Szemerédi (1976), with a second proof by Erdős
and Szemerédi.

[[problems/integer_sequences/E0535/_index|E0535/]]: Asks for estimates of
$f_r(N)$, the size of the largest subset of $\{1,\ldots,N\}$ with no $r$
elements whose pairwise greatest common divisors are all equal, for $r\ge3$.

[[problems/integer_sequences/E0536/_index|E0536/]]: Asks for estimates of
$f(N)$, the size of the largest $A\subseteq\{1,\ldots,N\}$ with no distinct
$a,b,c$ such that $\mathrm{lcm}(a,b)=\mathrm{lcm}(b,c)=\mathrm{lcm}(a,c)$, and
in particular whether $f(N)=o(N)$.

[[problems/integer_sequences/E0537/_index|E0537/]]: Asks whether, for each
$\epsilon>0$ and all large $N$, every $A\subseteq\{1,\ldots,N\}$ with
$|A|\ge\epsilon N$ contains $a_1,a_2,a_3$ with $a_1p_1=a_2p_2=a_3p_3$ for some
distinct primes $p_1,p_2,p_3$.

[[problems/integer_sequences/E0538/_index|E0538/]]: Asks for the best possible
upper bound on $\sum_{n\in A}1/n$ for $A\subseteq\{1,\ldots,N\}$ in which each
$m$ has at most $r$ representations $m=pa$ with $p$ prime and $a\in A$.

[[problems/integer_sequences/E0539/_index|E0539/]]: Asks for estimates of
$h(n)$, the least size of $\{a/\gcd(a,b):a,b\in A\}$ over all sets
$A\subseteq\mathbb{N}$ of size $n$.

[[problems/integer_sequences/E0540/_index|E0540/]]: Asks whether every
$A\subseteq\mathbb{Z}/N\mathbb{Z}$ with $|A|\gg N^{1/2}$ has a non-empty subset
summing to $0$ modulo $N$; proved by Szemerédi in 1970 for all finite abelian
groups.

[[problems/integer_sequences/E0541/_index|E0541/]]: Asks whether $p$ residues
modulo $p$ whose non-empty zero-sum subsets all have the same size must take at
most two distinct values. This is Graham's conjecture, proved for large primes
in 1976 and for every modulus in 2010.

[[problems/integer_sequences/E0542/_index|E0542/]]: Asks whether a set
$A\subseteq\{1,\ldots,n\}$ with all pairwise least common multiples above $n$
has $\sum_{a\in A}1/a\le31/30$, and whether a positive proportion of the
integers up to $n$ are divisible by no element of $A$. Schinzel and Szekeres
answered yes and no.

[[problems/integer_sequences/E0587/_index|E0587/]]: Asks for the size of the
largest subset of $\{1,\ldots,N\}$ in which no non-empty subset has a square
sum.

[[problems/integer_sequences/E0635/_index|E0635/]]: Asks how large a set
$A\subseteq\{1,\ldots,N\}$ can be if $b-a\nmid b$ for all $a,b\in A$ with
$b-a\ge t$.

[[problems/integer_sequences/E0650/_index|E0650/]]: Asks for the least number
$f(m)$ of distinct multiples of distinct elements of an $m$-element set
$A\subseteq\{1,\ldots,N\}$ that every interval of length $2N$ contains. By van
Doorn, Li and Tang (2026), $f(m)=\min(m,\lceil2\sqrt m\rceil)$, so the answer to
whether $f(m)\le\sqrt m$ is no.

[[problems/integer_sequences/E0675/_index|E0675/]]: Asks which sets of integers,
such as the sums of two squares, have the translation property: for every $n$,
some shift $t_n\ge1$ leaves membership of each $a\le n$ unchanged.

[[problems/integer_sequences/E0677/_index|E0677/]]: Asks whether two disjoint
blocks of $k$ consecutive integers can have the same least common multiple.
Erdős's 1979 conjecture that they cannot is open, and the few known solutions
all use blocks of different lengths.

[[problems/integer_sequences/E0678/_index|E0678/]]: Asks whether, infinitely
often, a block of $k$ consecutive integers has a larger least common multiple
than a later block of $k+1$. Cambie (2024, arXiv) proved this in a strong form,
with the ratio exceeding any constant.

[[problems/integer_sequences/E0687/_index|E0687/]]: Asks for the order of the
longest initial interval that one residue class for each prime $p\le x$ can
cover, the covering form of Jacobsthal's function. It is open: an accepted
partial claim gives $Y(x)\ll x^2/(\log x)^2$, so $Y(x)=o(x^2)$, and the order
lies between $x\log x$ times iterated logarithms and that bound.

[[problems/integer_sequences/E0688/_index|E0688/]]: Asks for the largest
$\epsilon_n$ such that one residue class for each prime $p$ with
$n^{\epsilon_n}<p\le n$ covers every integer in $[1,n]$, and whether
$\epsilon_n\to0$. It is open, between Erdős's lower bound and a counting bound
of $1/e$.

[[problems/integer_sequences/E0689/_index|E0689/]]: Asks whether, for large $n$,
one residue class can be chosen for each prime $p\le n$ so that every integer in
$[1,n]$ lies in at least two of them. It was open on the site, with three
pending AI-assisted full claims from April and July 2026.

[[problems/integer_sequences/E0691/_index|E0691/]]: Asks for a necessary and
sufficient condition on a set of positive integers for its set of multiples to
have density $1$; open, with one family of block sequences settled by Tenenbaum.

[[problems/integer_sequences/E0695/_index|E0695/]]: Asks whether primes
$p_1<p_2<\cdots$ with $p_{i+1}\equiv1\pmod{p_i}$ must have $p_k^{1/k}\to\infty$,
and whether such a sequence exists with $p_k\le\exp(k(\log k)^{1+o(1)})$.

[[problems/integer_sequences/E0708/_index|E0708/]]: Asks for bounds on the
fewest integers from a run of $\max(A)$ consecutive integers whose product is
divisible by $\prod_{a\in A}a$, for any set $A$ of $n$ integers. The corrected
at-most statement is open, with a partial bound of $12n$ pending.

[[problems/integer_sequences/E0709/_index|E0709/]]: Asks for good bounds on, or
an asymptotic formula for, the least $f(n)$ such that any $f(n)\max(A)$
consecutive integers hold distinct multiples of the $n$ elements of $A$, for
every $n$-element set $A$. Known bounds are $\log n/\log\log n\ll f(n)\ll\sqrt
n$.

[[problems/integer_sequences/E0710/_index|E0710/]]: Asks for an asymptotic
formula for the least $f(n)$ such that $(n,n+f(n))$ holds distinct
$a_1,\ldots,a_n$ with $k\mid a_k$ for each $k$. It is known to lie between
$n\sqrt{\log n/\log\log n}$ and $1.74\,n\sqrt{\log n}$, with a 2026 claim
pending.

[[problems/integer_sequences/E0711/_index|E0711/]]: Asks to prove
$\max_mf(n,m)\le n^{1+o(1)}$ and $\max_m(f(n,m)-f(n,n))\to\infty$, where
$(m,m+f(n,m))$ is the shortest interval holding distinct $a_1,\ldots,a_n$ with
$k\mid a_k$. The second was proved by van Doorn (2026); the first is open, with
an upper bound of order $n^{3/2}$ proved.

[[problems/integer_sequences/E0726/_index|E0726/]]: Asks whether $\sum1/p$ over
the primes $p\le n$ for which $n\bmod p$ lies in $(p/2,p)$ is asymptotic to
$\tfrac12\log\log n$.

[[problems/integer_sequences/E0748/_index|E0748/]]: Asks whether the number of
sum-free subsets of $\{1,\ldots,n\}$ is $2^{(1+o(1))n/2}$.

[[problems/integer_sequences/E0768/_index|E0768/]]: Asks whether the proportion
of $n\le N$ such that every prime $p\mid n$ has a divisor $d>1$ of $n$ with
$d\equiv1\pmod p$ is $\exp(-(c+o(1))\sqrt{\log N}\log\log N)$.

[[problems/integer_sequences/E0770/_index|E0770/]]: Asks about the densities and
growth of $h(n)$, the least $h$ with $\gcd(2^n-1,3^n-1,\ldots,h^n-1)=1$.

[[problems/integer_sequences/E0771/_index|E0771/]]: Asks whether
$f(n)=(\tfrac12+o(1))n/\log n$, where $f(n)$ is the largest size such that, for
every $m$, some subset of $\{1,\ldots,n\}$ of that size has no subset summing to
$m$.

[[problems/integer_sequences/E0774/_index|E0774/]]: Asks whether every infinite
set of natural numbers whose finite subsets each contain a dissociated subset
(one with distinct subset sums) of proportional size is a finite union of
dissociated sets.

[[problems/integer_sequences/E0783/_index|E0783/]]: Asks which set of pairwise
coprime integers in $\{2,\ldots,N\}$ with reciprocal sum at most a fixed $C$
leaves the fewest integers up to $N$ divisible by none of its elements.
Following the site, it is read up to an error of $o(N)$, and then the largest
primes up to $N$ are optimal.

[[problems/integer_sequences/E0784/_index|E0784/]]: Asks whether a set of
integers in $[2,x]$ with reciprocal sum at most $C$ must leave $\gg x/(\log
x)^c$ integers up to $x$ divisible by none of them, for some $c>0$.

[[problems/integer_sequences/E0786/_index|E0786/]]: Asks whether, for every
$\epsilon>0$, some $A\subset\mathbb{N}$ of density above $1-\epsilon$ has equal
products of distinct elements only with equally many factors.

[[problems/integer_sequences/E0793/_index|E0793/]]: Asks whether the largest
$A\subseteq\{1,\ldots,n\}$ in which no element divides the product of two others
has size $\pi(n)+(C+o(1))n^{2/3}(\log n)^{-2}$. Chojecki's 2026 manuscript,
accepted by the site, proves this with $C=27/2$.

[[problems/integer_sequences/E0795/_index|E0795/]]: Asks whether the largest
$A\subseteq\{1,\ldots,n\}$ with all subset products distinct has size at most
$\pi(n)+\pi(n^{1/2})+o(n^{1/2}/\log n)$; proved by Raghavan with a power-saving
error term.

[[problems/integer_sequences/E0796/_index|E0796/]]: Asks whether
$g_3(n)=n\log\log n/\log n+(c+o(1))n/\log n$ for some constant $c$, where
$g_k(n)$ is the size of the largest $A\subseteq\{1,\ldots,n\}$ in which every
number has fewer than $k$ representations $a_1a_2$ with $a_1<a_2$ in $A$.

[[problems/integer_sequences/E0820/_index|E0820/]]: Asks whether
$\gcd(2^n-1,3^n-1)=1$ for infinitely many $n$, and how fast the least bases
$k<l$ with $\gcd(k^n-1,l^n-1)=1$ grow.

[[problems/integer_sequences/E0839/_index|E0839/]]: Asks whether an increasing
sequence of positive integers in which no term is a sum of consecutive earlier
terms must satisfy $\limsup a_n/n=\infty$.

[[problems/integer_sequences/E0848/_index|E0848/]]: Asks whether the maximum
size of a set $A\subseteq\{1,\ldots,N\}$ with $ab+1$ never squarefree for
$a,b\in A$ is attained by the integers $n\equiv7\pmod{25}$.

[[problems/integer_sequences/E0851/_index|E0851/]]: Asks whether, for each
$\epsilon>0$, some $r\ll_\epsilon1$ makes the integers $2^k+n$, with $n$ having
at most $r$ prime divisors, have density at least $1-\epsilon$.

[[problems/integer_sequences/E0854/_index|E0854/]]: Asks, for the integers
$a_1<a_2<\cdots$ coprime to the $k$th primorial $n_k$ (the product of the first
$k$ primes), for an estimate of the smallest even number not of the form
$a_{i+1}-a_i$, and whether $\gg\max_i(a_{i+1}-a_i)$ even numbers have that form.

[[problems/integer_sequences/E0856/_index|E0856/]]: Asks, for $k\ge3$, for an
estimate of the largest $\sum_{n\in A}1/n$ over sets $A\subseteq\{1,\ldots,N\}$
with no $k$ members sharing the same pairwise least common multiple.

[[problems/integer_sequences/E0873/_index|E0873/]]: Asks whether, for every
$\epsilon>0$, there is a $k$ such that fewer than $X^\epsilon$ blocks of $k$
consecutive terms of an increasing integer sequence have least common multiple
below $X$.

[[problems/integer_sequences/E0879/_index|E0879/]]: Asks for an estimate of the
largest sum of a set of pairwise coprime integers up to $n$, and whether, for
each $k\ge2$ and large $n$, the best such set contains a number with at least
$k$ prime factors.

[[problems/integer_sequences/E0888/_index|E0888/]]: Asks for the size of the
largest $A\subseteq\{1,\ldots,n\}$ in which any $a\le b\le c\le d$ in $A$ with
$abcd$ a square satisfy $ad=bc$.

[[problems/integer_sequences/E0896/_index|E0896/]]: Asks for an estimate of the
largest number of integers $m$ with exactly one representation $m=ab$, $a\in A$,
$b\in B$, over $A,B\subseteq\{1,\ldots,N\}$; the order of magnitude is
$N^2/((\log N)^{\delta}(\log\log N)^{3/2})$.

[[problems/integer_sequences/E0929/_index|E0929/]]: Asks for the least $x$ such
that a positive density of $n$ have each of $n+1,\ldots,n+k$ divisible by a
prime $\le x$, and whether it is at least $k^{1-o(1)}$. It is the inverse of the
covering function of Problem 687 and is open, with lower bounds only of order
$\sqrt{k}\log k$.

[[problems/integer_sequences/E0932/_index|E0932/]]: Asks whether infinitely many
prime gaps $(p_r,p_{r+1})$ contain at least two integers whose prime factors are
all smaller than $p_{r+1}-p_r$.

[[problems/integer_sequences/E0954/_index|E0954/]]: For the sequence with
$a_0=0$, $a_1=1$ and each next term the least $n$ for which $a_i+a_j\le n$ has
fewer than $n$ solutions, asks whether the number of solutions of $a_i+a_j\le x$
is $x+O(x^{1/4+o(1)})$.

[[problems/integer_sequences/E0961/_index|E0961/]]: Asks for an estimate of the
least $n$ such that every run of $n$ consecutive integers above $k$ contains one
divisible by a prime greater than $k$; open, between a Rankin-type prime-gap
lower bound and $k/\log k$ times iterated logarithms.

[[problems/integer_sequences/E0962/_index|E0962/]]: Asks for an estimate of the
greatest $k$ such that, for some $m\le n$, each of $m+1,\ldots,m+k$ is divisible
by a prime greater than $k$, and whether $\log k(n)\le(\log n)^{1/2+o(1)}$. Both
are open, and $\log k(n)$ lies between $c\sqrt{\log n\log\log n}$ and $(\log
n)/2$.

[[problems/integer_sequences/E0968/_index|E0968/]]: Asks whether the set of $n$
with $p_n/n<p_{n+1}/(n+1)$ has positive density.

[[problems/integer_sequences/E0970/_index|E0970/]]: Asks for the order of
magnitude of Jacobsthal's function $h(k)$ over integers with at most $k$
distinct prime factors, and whether $h(k)\ll k^2$. An accepted partial claim
proves the quadratic bound, and the order of magnitude stays open.

[[problems/integer_sequences/E0971/_index|E0971/]]: Asks whether some $c>0$
makes the least prime $p(a,d)\equiv a\pmod d$ exceed $(1+c)\phi(d)\log d$ for
$\gg\phi(d)$ residues $a$, for all large $d$. Two 2026 proof claims answer yes,
one with a Lean development; both are pending and unreviewed.

[[problems/integer_sequences/E0980/_index|E0980/]]: Asks whether
$\sum_{p<x}n_k(p)\sim c_kx/\log x$, with $n_k(p)$ the least $k$th power
nonresidue of $p$. It is proved for every $k$ under Elliott's convention (Erdős
1961 for $k=2$, Elliott 1967), and the variant over every prime with a $k$th
power nonresidue is open for composite $k$.

[[problems/integer_sequences/E0983/_index|E0983/]]: Asks for estimates of the
least $r=f(k,n)$ such that every $k$-element subset of $\{1,\ldots,n\}$ has more
than $r$ members divisible only by primes from some set of $r$ primes, and
whether $2\pi(n^{1/2})-f(\pi(n)+1,n)\to\infty$.

[[problems/integer_sequences/E0985/_index|E0985/]]: Asks whether every prime
$p>2$ has a primitive root modulo $p$ that is a prime $q<p$. The site's wording
also includes $p=2$, where it fails.

[[problems/integer_sequences/E1057/_index|E1057/]]: Asks whether the number
$C(x)$ of Carmichael numbers up to $x$ satisfies $C(x)=x^{1-o(1)}$. A Lean proof
submitted to a bounty site in October 2026 claims the answer yes.

[[problems/integer_sequences/E1062/_index|E1062/]]: Asks for the size $f(n)$ of
the largest subset of $\{1,\ldots,n\}$ in which no element divides two other
distinct elements, and whether $\lim f(n)/n$ is irrational. A Lean proof
certified by Conjectures.io gives an exact formula and an irrational limit near
0.67297.

[[problems/integer_sequences/E1063/_index|E1063/]]: Asks for an estimate of the
least $n\ge2k$ such that $n-i$ divides $\binom{n}{k}$ for all but one $0\le
i<k$.

[[problems/integer_sequences/E1073/_index|E1073/]]: Asks whether the number
$A(x)$ of composite $u<x$ dividing $n!+1$ for some $n$ satisfies $A(x)\le
x^{o(1)}$.

[[problems/integer_sequences/E1074/_index|E1074/]]: Asks whether the set of $m$
such that $m!+1$ has a prime factor $p\not\equiv1\pmod m$, and the set of primes
arising this way (Pillai primes, as a proportion of all primes), have densities,
and what they are.

[[problems/integer_sequences/E1101/_index|E1101/]]: Asks whether a good sequence
of pairwise coprime integers with convergent reciprocal sum can have
$u_n<n^{O(1)}$, or at least $u_n\le e^{o(n)}$.

[[problems/integer_sequences/E1102/_index|E1102/]]: Asks how fast a sequence $A$
must increase if, for every $n$, only finitely many $a\in A$ make $n+a$
squarefree (property $P$), or if, for infinitely many $n$, every $a\in A$ with
$a<n$ makes $n+a$ squarefree (property $Q$).

[[problems/integer_sequences/E1103/_index|E1103/]]: Asks how fast an infinite
set of integers must grow if every sum of two of its members is squarefree.

[[problems/integer_sequences/E1109/_index|E1109/]]: Asks for an estimate of the
size $f(N)$ of the largest subset of $\{1,\ldots,N\}$ whose pairwise sums are
all squarefree, and whether $f(N)\le N^{o(1)}$.

[[problems/integer_sequences/E1134/_index|E1134/]]: Asks whether the smallest
set containing $1$ and closed under $x\mapsto2x+1$, $x\mapsto3x+1$ and
$x\mapsto6x+1$ has positive lower density.

[[problems/integer_sequences/E1136/_index|E1136/]]: Asks whether some
$A\subset\mathbb{N}$ with lower density above $1/3$ has no two members, possibly
equal, whose sum is a power of two.

[[problems/integer_sequences/E1146/_index|E1146/]]: Asks whether $\{2^m3^n :
m,n\ge0\}$ is an essential component, that is, a set $A$ with $d_s(A+B)>d_s(B)$
whenever the Schnirelmann density $d_s(B)$ lies strictly between $0$ and $1$.

[[problems/integer_sequences/E1149/_index|E1149/]]: States that for every
non-integer real $\alpha>0$ the integers $n\ge1$ with $(n,\lfloor
n^\alpha\rfloor)=1$ have density $6/\pi^2$.

[[problems/integer_sequences/E1181/_index|E1181/]]: Asks whether, for some $c>0$
and all large $n$, the least prime not dividing $\prod_{1\le i\le\log n}(n+i)$
is below $(1-c)(\log n)^2$. Only the trivial bound $(1+o(1))(\log n)^2$ is
known.

[[problems/integer_sequences/E1204/_index|E1204/]]: Asks for estimates of the
least possible largest element $A(k)$ and least possible mean $B(k)$ of $k$
integers missing a residue class modulo every prime; open. Asymptotically,
$A(k)$ lies between $\tfrac12k\log k$ and $k\log k$, and $B(k)$ between
$\tfrac14k\log k$ and $\tfrac12k\log k$.

[[problems/integer_sequences/E1205/_index|E1205/]]: Asks for estimates of
$F(x)$, the largest $F$ such that some choice of one class $a_n\pmod n$ for each
$n\le x$ makes every $m\le x$ satisfy at least $F$ of the congruences. The
site's own argument, a pending claim, gives $F(x)\sim\log x$.

[[problems/integer_sequences/E1209/_index|E1209/]]: Asks whether one $n$ making
every $n+a_k$ prime, for a fast-growing integer sequence $a_k$, forces
infinitely many such $n$, with squarefree and $n+2^{2^k}$ variants. Three of the
questions are answered no and three remain open.

[[problems/integer_sequences/E1210/_index|E1210/]]: Asks whether every set $A$
of pairwise coprime integers in $[1,n)$ satisfies $\sum_{a\in
A}\frac{1}{n-a}\le\sum_{p<n}\frac{1}{p}+O(1)$.

***

Problems on sets and sequences of integers defined by divisibility, coprimality,
gcd or lcm, or residue conditions, or by avoiding a pattern, asking for their
density, counting function, gaps or growth, including covering-congruence and
sieve questions.

Site tags routed here: additive combinatorics, number theory, primes, sidon
sets, squares.
