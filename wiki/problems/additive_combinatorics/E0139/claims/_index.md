---
name: problems/additive_combinatorics/E0139/claims
desc: The 6 claim pages of Problem 139, one per claimant's result; the problem's standing derives from them.
tags: []
sources: []
created: 2026-10-07T08:44:40Z
updated: 2026-10-11T22:24:14Z
---

# problems/additive_combinatorics/E0139/claims

[[problems/additive_combinatorics/E0139/_index|..]]

[[problems/additive_combinatorics/E0139/claims/1975_01_01_szemeredi|1975_01_01_szemeredi]]: Szemerédi's 1975 theorem in Acta Arithmetica states that $r_k(N)=o(N)$ for
every $k$. It is accepted on the refereed publication and the site's credit,
and the page links the unaudited Lean formalization of it in Boris Alexeev's
repository.

[[problems/additive_combinatorics/E0139/claims/2017_05_04_green_tao|2017_05_04_green_tao]]: Theorem 1.1 of Green and Tao (Mathematika 2017) bounds the size of a subset of
the first $N$ integers with no four-term progression by $N$ over a power of
$\log N$. This proves the instance $k=4$ of Problem 139 with a rate, and it is
accepted as refereed.

[[problems/additive_combinatorics/E0139/claims/2023_02_10_kelley_meka|2023_02_10_kelley_meka]]: Theorem 1.1 of Kelley and Meka (FOCS 2023) bounds the size of a subset of the
first $N$ integers with no three-term progression by
$N\,2^{-c(\log N)^{\beta}}$ for some $c,\beta>0$. This is the instance $k=3$
of Problem 139 with a rate, accepted as reviewed.

[[problems/additive_combinatorics/E0139/claims/2023_09_05_bloom_sisask|2023_09_05_bloom_sisask]]: Theorem 1 of Bloom and Sisask's 2023 note bounds the size of a subset of the
first $N$ integers with no three-term progression by
$\exp(-c(\log N)^{1/9})N$. This is the instance $k=3$ of Problem 139 with a
sharper rate, and as a preprint it is claimed.

[[problems/additive_combinatorics/E0139/claims/2024_02_28_leng_sah_sawhney|2024_02_28_leng_sah_sawhney]]: Theorem 1.1 of Leng, Sah and Sawhney (2024) bounds the size of a subset of the
first $N$ integers with no $k$-term progression by
$N\exp(-(\log\log N)^{c_k})$ for every $k\ge5$, which gives those instances of
Problem 139 with a rate. It is a preprint, so it is claimed.

[[problems/additive_combinatorics/E0139/claims/2026_09_23_openai|2026_09_23_openai]]: The OpenAI release states the bound
$r_k(N)\le C_kN\exp(-c_k(\log N)^{\varepsilon_k})$ for each fixed $k\ge3$,
which gives $r_k(N)=o(N)$ at once. It is accepted as a second route, on a
built Lean declaration of a weaker saving that suffices.

***
