---
name: problems/primes/E0855/claims/2025_03_04_chahal_elma_fellini_vatwani_vo
title: Chahal, Elma, Fellini, Vatwani and Vo's prime-number-theorem range
desc: |
  Theorem 1.1 of the paper, refereed in Acta Arithmetica, proves
  $\pi(x+y)\le\pi(x)+\pi(y)$ for large $x$ and
  $3CR(2x)\log^2x/\log\log x\le y\le x$, where $CR(x)$ bounds the error in the
  prime number theorem. Smaller $y$ stay open.
authors:
- Bittu Chahal
- Ertan Elma
- Nic Fellini
- Akshaa Vatwani
- Do Nhat Tan Vo
status: accepted
claim: proved
scope: partial
evidence:
- refereed
submitted: null
links:
- url: https://arxiv.org/abs/2503.02766v1
  kind: preprint
  date: 2025-03-04
- url: https://doi.org/10.4064/aa250808-4-11
  kind: paper
  date: 2026-04-01
created: 2026-10-13T13:20:00Z
updated: 2026-10-13T13:20:00Z
---

***

**Claim.** B. Chahal, E. Elma, N. Fellini, A. Vatwani and D. N. T. Vo, *On
the second Hardy--Littlewood conjecture*, arXiv:2503.02766v1 (4 March 2025),
[[../library/primes/chahal_et_al_2025_second_hardy_littlewood_conjecture/theorem_1_1|Theorem 1.1]]
(p. 3): let $C>0$, $x_0\ge2$ and a positive nondecreasing function $R$
satisfy $|\pi(x)-\operatorname{li}(x)|\le CR(x)$ for $x\ge x_0$ (display
(1.4)); then for $x\ge x_0$ and

$$
\frac{3CR(2x)\log^2x}{\log\log x}\le y\le x
$$

$\pi(x+y)\le\pi(x)+\pi(y)$. Any unconditional error term of the prime number
theorem may serve as $R$; the paper lists explicit ones, (1.5)--(1.7), cited
from Johnston and Yang and from Mossinghoff, Trudgian and Yang, and with them
the lower end of the range is $x$ times a factor that tends to zero faster
than any power of $1/\log x$
([[../library/primes/chahal_et_al_2025_second_hardy_littlewood_conjecture/corollary_1_5|Corollary 1.5]],
p. 4, gives the matching count of possible exceptions). The proof (Section
2.1) compares $\operatorname{li}(x)+\operatorname{li}(y)-\operatorname{li}(x+y)
\ge y\log\log x/\log^2x$ with the three error terms. Under the Riemann
hypothesis,
[[../library/primes/chahal_et_al_2025_second_hardy_littlewood_conjecture/corollary_1_2|Corollary 1.2]]
(p. 3) gives the inequality for $x\ge x_\epsilon$ and
$(2+\epsilon)\sqrt x\log^2x/(8\pi)\le y\le x$; that conditional range is
recorded here and is not part of this page's scope. The paper is compiled
at
[[../library/primes/chahal_et_al_2025_second_hardy_littlewood_conjecture/_index|its card]],
whose statements were read clause by clause on arXiv v1 with the proofs of
Section 2 followed.

**Covers.** Every pair whose larger entry $x\ge x_0$ and smaller entry $y$
satisfy $y\ge3CR(2x)\log^2x/\log\log x$ for an unconditional error term $R$.
For large pairs this contains the ranges of
[[problems/primes/E0855/claims/2002_01_01_dusart|Dusart's claim]],
[[problems/primes/E0855/claims/2022_06_03_alkan|Alkan's claim]] and
[[problems/primes/E0855/claims/2019_09_27_axler|Axler's claim]]. Not covered:
smaller $y$, for instance $y=\lfloor\sqrt x\rfloor$, so the problem as posed
is not settled.

**Depends on.** Nothing in this wiki.

**Acceptance.** Refereed: Acta Arithmetica 223 (2026), 185--196,
doi:10.4064/aa250808-4-11, published online 1 April 2026 (the publisher's
article page and the Crossref record). The journal's abstract states the
unconditional improvement of the range and the Riemann-hypothesis range of
Corollary 1.2. The statements above are read from arXiv v1; the journal text
was not compared. The page is named by the first version's posting date.
