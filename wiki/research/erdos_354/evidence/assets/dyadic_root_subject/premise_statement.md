[cut]

## Statement

The theorem's type is formal-conjectures' `Erdos354.erdos_354.parts.i` with
`answer(sorry)` instantiated to `True`:

```lean
True ↔ ∀ α > 0, ∀ β > 0, Irrational (α / β) →
  IsAddCompleteNatSeq' (Erdos354.FloorMultiples.interleave α β 2)
```

Unfolded with formal-conjectures' definitions
(`FormalConjectures/ErdosProblems/354.lean` and
`FormalConjecturesForMathlib/NumberTheory/AdditivelyComplete.lean`, `main` at
`e6fac203`): `FloorMultiples a γ n` is $\lfloor\gamma^na\rfloor$ in $\mathbb Z$;
`interleave a b γ n` is `FloorMultiples a γ (n / 2)` for even $n$ and
`FloorMultiples b γ (n / 2)` for odd $n$, so `interleave α β 2` is the sequence
$\lfloor\alpha\rfloor,\lfloor\beta\rfloor,\lfloor2\alpha\rfloor,\lfloor2\beta\rfloor,\lfloor4\alpha\rfloor,\ldots$;
`subseqSums' A` (line 42) is the set of sums $\sum_{i\in B}A(i)$ over finite
sets $B\subset\mathbb N$ of indices; `IsAddCompleteNatSeq' A` (line 100) says
that every sufficiently large $k\in\mathbb Z$ lies in `subseqSums' A`. In
erdosproblems.com's words: for all $\alpha,\beta>0$ with $\alpha/\beta$
irrational, every sufficiently large integer $n$ is

$$
n=\sum_{s\in S}\lfloor2^s\alpha\rfloor+\sum_{t\in T}\lfloor2^t\beta\rfloor
$$

for some finite $S,T\subset\mathbb N$.

**Fidelity to erdosproblems.com's first question.** Exact. A finite index set
$B$ of the interleaving is the pair $S=\{n/2:n\in B,\ n\text{ even}\}$,
$T=\{(n-1)/2:n\in B,\ n\text{ odd}\}$, and conversely; each index is used
at most once and equal values at different indices count separately,
which is the multiset reading erdosproblems.com's "That is" clause fixes; zero
terms ($\lfloor2^s\alpha\rfloor=0$ when $2^s\alpha<1$) change no sum;
"every sufficiently large integer" in $\mathbb Z$ is "all sufficiently
large natural numbers"; the hypotheses $\alpha,\beta>0$ and $\alpha/\beta$
irrational are erdosproblems.com's. The theorem says nothing about
erdosproblems.com's second question (a base $\gamma\in(1,2)$), about strong
completeness (deleting finitely many terms) or about the set-union reading.

[cut]

