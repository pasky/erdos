---
name: problems/ramsey_theory/E0800/claims/1997_06_01_li_rousseau_soltes
title: Li, Rousseau and Šoltés improve the linear Ramsey constant to 6
desc: |
  In a refereed 1997 paper, Li, Rousseau and Šoltés prove that a graph on $n$
  vertices whose vertices of degree at least three are independent has two-color
  Ramsey number at most $6n$. This answers Problem 800 yes, and only the paper's
  abstract has been read here.
authors:
- Yusheng Li
- Cecil C. Rousseau
- Ľubomír Šoltés
status: accepted
claim: proved
scope: full
evidence:
- refereed
submitted: null
links:
- url: https://doi.org/10.1016/S0012-365X(96)00311-1
  kind: paper
created: 2026-10-07T06:52:50Z
updated: 2026-10-08T01:29:59Z
---

***

**Claim.** [[problems/ramsey_theory/E0800/_index|Problem 800]] asks whether
$R(G)\ll n$, with an absolute implied constant, for every graph $G$ on $n$
vertices in which no two adjacent vertices both have degree at least three.
Li, Rousseau and Šoltés answer yes with the constant $6$: the abstract of
*Ramsey linear families and generalized subdivided graphs* states that

$$
r(G,G)\le6\,|V(G)|
$$

whenever the vertices of $G$ of degree at least three form an independent
set, which is the problem's hypothesis, and that no constant below $4$ works
for this class; $r(G,G)$ is the two-color Ramsey number $R(G)$ of the
problem page. The result sharpens Alon's constant $12$ for the same class
([[problems/ramsey_theory/E0800/claims/1994_07_01_alon|Alon 1994]]). Read
depth: claims checked against the abstract only, as given by an indexed copy
of the publisher's page, with the publication data from the Crossref record,
which carries no abstract; neither the $6n$ statement nor the remark that no
constant below $4$ works has been checked against a primary text; the paper's
full results and proof are unread, and the paper has no library card.

**Scope.** Full. The bound is the problem's statement with an explicit
absolute constant.

**Depends on.** Nothing in this wiki; the result rests on the cited paper
alone.

**Acceptance.** Refereed: the paper appeared in Discrete Math. 170 (1997), no.
1--3, 269--275 (the Crossref record, read 2026-10-07, dates the issue June
1997). Bloom's catalog labeled the problem PROVED, and its commentary credits
Alon without naming this paper. The erdosproblems.com discussion thread and
proof-claim tab are empty. So the acceptance rests on the refereed publication
alone. The proof is unread, and the abstract check is not acceptance evidence.

**Dating.** The page is dated by the issue month the journal record gives;
the day in the page name is a placeholder, since no earlier posting is
known.
