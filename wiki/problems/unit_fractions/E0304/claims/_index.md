---
name: problems/unit_fractions/E0304/claims
desc: The 5 claim pages of Problem 304, one per claimant's result; the problem's standing derives from them.
tags: []
sources: []
created: 2026-10-07T08:47:56Z
updated: 2026-10-11T22:24:14Z
---

# problems/unit_fractions/E0304/claims

[[problems/unit_fractions/E0304/_index|..]]

[[problems/unit_fractions/E0304/claims/1950_01_01_erdos|1950_01_01_erdos]]: Erdős's refereed 1950 paper proves $N(a,b)<c_1\log b/\log\log b$ for every
$a/b$ and $N(b-1,b)>\log\log b-1$, with the average of $N(a,b)$ over $a$ above
$\frac12(\log\log b-1)$. So $\log\log b\ll N(b)\ll\log b/\log\log b$.

[[problems/unit_fractions/E0304/claims/1985_01_01_vose|1985_01_01_vose]]: Vose proves that every $a/b<1$ is a sum of $O(\sqrt{\log b})$ distinct unit
fractions, so $N(b)\ll\sqrt{\log b}$, replacing Erdős's $\log b/\log\log b$.
It is a refereed paper in the Bulletin of the London Mathematical Society.

[[problems/unit_fractions/E0304/claims/2026_09_01_thepriceisright|2026_09_01_thepriceisright]]: A Lean proof of the formal-conjectures variant lower_1950 of Problem 304, that
$\log\log b\le6N(b)$ for $b\ge3$, produced by Harmonic's Aristotle prover and
published by the GitHub account thepriceisright. The claim is pending.

[[problems/unit_fractions/E0304/claims/2026_09_16_van_doorn|2026_09_16_van_doorn]]: Theorem 1.2 of the note by Wouter van Doorn and GPT-6 Astra Pro, posted on 16
September 2026 on Problem 18's proof-claims tab, states that every $a/b$ with
$b$ large is a sum of at most $2c_0(\log\log b)^2$ distinct unit fractions,
where $c_0=14/\log2$.

[[problems/unit_fractions/E0304/claims/2026_09_25_openai|2026_09_25_openai]]: Theorem 1.1 of the OpenAI mathematics release of 25 September 2026 states that
every $a/b$ with $1\le a<b$ is a sum of at most $c\log\log b$ distinct unit
fractions. It is accepted on the Lean declarations that the corpus's
verification built and audited.

***
