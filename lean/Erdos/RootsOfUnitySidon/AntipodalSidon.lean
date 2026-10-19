import Erdos.RootsOfUnitySidon.RootsOfUnitySidon

/-!
The analytic treatment of antipodal pairs.
-/

namespace Erdos.Research.Problem774

open scoped ComplexConjugate

private theorem norm_pair_le (a b : ℂ) :
    ‖a‖ + ‖b‖ ≤ ‖a + conj b‖ + ‖a - conj b‖ := by
  have ha := norm_add_le (a + conj b) (a - conj b)
  have hb := norm_sub_le (a + conj b) (a - conj b)
  have hxa : (a + conj b) + (a - conj b) = (2 : ℂ) * a := by ring
  have hxb : (a + conj b) - (a - conj b) = (2 : ℂ) * conj b := by ring
  rw [hxa] at ha
  rw [hxb] at hb
  simp only [norm_mul, Complex.norm_conj] at ha hb
  norm_num at ha hb
  nlinarith

private theorem pair_re (a b : ℂ) (t : Circle) :
    ((a + conj b) * (t : ℂ)).re =
      (a * (t : ℂ) + b * ((t⁻¹ : Circle) : ℂ)).re := by
  rw [Circle.coe_inv_eq_conj]
  have h : (conj b * (t : ℂ)).re = (b * conj (t : ℂ)).re := by
    calc
      (conj b * (t : ℂ)).re = (conj (b * conj (t : ℂ))).re := by
        simp [map_mul]
      _ = (b * conj (t : ℂ)).re := Complex.conj_re _
  simpa only [add_mul, Complex.add_re] using congrArg (fun x : ℝ =>
    (a * (t : ℂ)).re + x) h

/-- A positive-real estimate on one representative of each antipodal pair
controls the two coefficients together, with a factor of two in the analytic
Sidon constant. The statement is about indexed pairs and does not require a
separate disjointness assumption. -/
theorem analyticBound_antipodal_pairs (s : Set ℂ) (K : ℝ) (hK : 0 ≤ K)
    (h : PositiveRealBound s K) (A : Finset ℂ) (hA : (↑A : Set ℂ) ⊆ s)
    (a b : ℂ → ℂ) :
    ∃ χ : AddChar ℂ Circle,
      (∑ z ∈ A, (‖a z‖ + ‖b z‖)) ≤
        (2 * K) * ‖∑ z ∈ A,
          (a z * (χ z : ℂ) + b z * (χ (-z) : ℂ))‖ := by
  classical
  let cPlus : ℂ → ℂ := fun z => a z + conj (b z)
  let cMinus : ℂ → ℂ := fun z => -(Complex.I) * (a z - conj (b z))
  obtain ⟨chiPlus, hPlus⟩ := h A hA cPlus
  obtain ⟨chiMinus, hMinus⟩ := h A hA cMinus
  let P (χ : AddChar ℂ Circle) : ℂ :=
    ∑ z ∈ A, (a z * (χ z : ℂ) + b z * (χ (-z) : ℂ))
  have hPPlus : (∑ z ∈ A, cPlus z * (chiPlus z : ℂ)).re = (P chiPlus).re := by
    simp only [Complex.re_sum, P]
    apply Finset.sum_congr rfl
    intro z _
    have hz : chiPlus (-z) = (chiPlus z)⁻¹ := chiPlus.map_neg_eq_inv z
    simpa only [cPlus, hz] using pair_re (a z) (b z) (chiPlus z)
  have hPMinus : (∑ z ∈ A, cMinus z * (chiMinus z : ℂ)).re =
      ((-Complex.I) * P chiMinus).re := by
    have hc (z : ℂ) :
        cMinus z = (-Complex.I * a z) + conj (-Complex.I * b z) := by
      simp [cMinus, map_mul, Complex.conj_I]
      ring
    calc
      (∑ z ∈ A, cMinus z * (chiMinus z : ℂ)).re =
          ∑ z ∈ A, (cMinus z * (chiMinus z : ℂ)).re := by simp
      _ = ∑ z ∈ A,
          ((-Complex.I) *
            (a z * (chiMinus z : ℂ) + b z * (chiMinus (-z) : ℂ))).re := by
        apply Finset.sum_congr rfl
        intro z _
        rw [hc]
        have hz : chiMinus (-z) = (chiMinus z)⁻¹ := chiMinus.map_neg_eq_inv z
        calc
          (((-Complex.I * a z) + conj (-Complex.I * b z)) *
              (chiMinus z : ℂ)).re =
              ((-Complex.I * a z) * (chiMinus z : ℂ) +
                (-Complex.I * b z) * (((chiMinus z)⁻¹ : Circle) : ℂ)).re :=
            pair_re (-Complex.I * a z) (-Complex.I * b z) (chiMinus z)
          _ = _ := by rw [hz]; congr 1; ring
      _ = ((-Complex.I) * P chiMinus).re := by
        simp only [P, Complex.re_sum, Finset.mul_sum]
  have hnormMinus : ∀ z, ‖cMinus z‖ = ‖a z - conj (b z)‖ := by
    intro z
    simp [cMinus]
  have hL : (∑ z ∈ A, (‖a z‖ + ‖b z‖)) ≤
      (∑ z ∈ A, ‖cPlus z‖) + (∑ z ∈ A, ‖cMinus z‖) := by
    rw [← Finset.sum_add_distrib]
    apply Finset.sum_le_sum
    intro z _
    simpa only [cPlus, hnormMinus] using norm_pair_le (a z) (b z)
  have hmain : (∑ z ∈ A, (‖a z‖ + ‖b z‖)) ≤
      K * ‖P chiPlus‖ + K * ‖P chiMinus‖ := by
    calc
      _ ≤ (∑ z ∈ A, ‖cPlus z‖) + (∑ z ∈ A, ‖cMinus z‖) := hL
      _ ≤ K * (P chiPlus).re + K * ((-Complex.I) * P chiMinus).re := by
        rw [← hPPlus, ← hPMinus]
        exact add_le_add hPlus hMinus
      _ ≤ K * ‖P chiPlus‖ + K * ‖(-Complex.I) * P chiMinus‖ := by
        apply add_le_add
        · exact mul_le_mul_of_nonneg_left (Complex.re_le_norm (P chiPlus)) hK
        · exact mul_le_mul_of_nonneg_left
            (Complex.re_le_norm ((-Complex.I) * P chiMinus)) hK
      _ = K * ‖P chiPlus‖ + K * ‖P chiMinus‖ := by
        simp
  by_cases hle : ‖P chiPlus‖ ≤ ‖P chiMinus‖
  · refine ⟨chiMinus, ?_⟩
    change _ ≤ (2 * K) * ‖P chiMinus‖
    nlinarith [mul_nonneg hK (sub_nonneg.mpr hle)]
  · refine ⟨chiPlus, ?_⟩
    change _ ≤ (2 * K) * ‖P chiPlus‖
    have hle' : ‖P chiMinus‖ ≤ ‖P chiPlus‖ := le_of_not_ge hle
    nlinarith [mul_nonneg hK (sub_nonneg.mpr hle')]

/-- The pair estimate rewritten for a disjoint union of a finite set and its
negative. The ambient coefficient function may vanish on either member of a
pair. -/
theorem analyticBound_antipodal_finset (s : Set ℂ) (K : ℝ) (hK : 0 ≤ K)
    (h : PositiveRealBound s K) (B : Finset ℂ)
    (hB : (↑B : Set ℂ) ⊆ s)
    (hdisj : Disjoint B (B.map (AddEquiv.neg ℂ).toEmbedding))
    (c : ℂ → ℂ) :
    ∃ χ : AddChar ℂ Circle,
      (∑ z ∈ B ∪ B.map (AddEquiv.neg ℂ).toEmbedding, ‖c z‖) ≤
        (2 * K) *
          ‖∑ z ∈ B ∪ B.map (AddEquiv.neg ℂ).toEmbedding,
            c z * (χ z : ℂ)‖ := by
  classical
  let N : Finset ℂ := B.map (AddEquiv.neg ℂ).toEmbedding
  have hsum (f : ℂ → ℂ) :
      (∑ z ∈ B, (f z + f (-z))) = ∑ z ∈ B ∪ N, f z := by
    rw [Finset.sum_add_distrib, Finset.sum_union (by simpa [N] using hdisj)]
    congr 1
    simp only [N, Finset.sum_map]
    rfl
  obtain ⟨χ, hχ⟩ :=
    analyticBound_antipodal_pairs s K hK h B hB c (fun z => c (-z))
  refine ⟨χ, ?_⟩
  have hnorm' :
      (∑ z ∈ B, (‖c z‖ + ‖c (-z)‖)) =
        ∑ z ∈ B ∪ N, ‖c z‖ := by
    rw [Finset.sum_add_distrib, Finset.sum_union (by simpa [N] using hdisj)]
    congr 1
    simp only [N, Finset.sum_map]
    rfl
  have hpoly := hsum (fun z => c z * (χ z : ℂ))
  change (∑ z ∈ B, (‖c z‖ + ‖c (-z)‖)) ≤
    (2 * K) * ‖∑ z ∈ B,
      (c z * (χ z : ℂ) + c (-z) * (χ (-z) : ℂ))‖ at hχ
  rw [hnorm', hpoly] at hχ
  simpa only [N] using hχ

/-- Coefficients supported on a subset of a finite antipodal grid inherit the
same analytic estimate. -/
theorem analyticBound_antipodal_finset_subset (s : Set ℂ) (K : ℝ) (hK : 0 ≤ K)
    (h : PositiveRealBound s K) (B : Finset ℂ)
    (hB : (↑B : Set ℂ) ⊆ s)
    (hdisj : Disjoint B (B.map (AddEquiv.neg ℂ).toEmbedding))
    (A : Finset ℂ)
    (hA : A ⊆ B ∪ B.map (AddEquiv.neg ℂ).toEmbedding)
    (c : ℂ → ℂ) :
    ∃ χ : AddChar ℂ Circle,
      (∑ z ∈ A, ‖c z‖) ≤
        (2 * K) * ‖∑ z ∈ A, c z * (χ z : ℂ)‖ := by
  classical
  let C : Finset ℂ := B ∪ B.map (AddEquiv.neg ℂ).toEmbedding
  let d : ℂ → ℂ := fun z => if z ∈ A then c z else 0
  obtain ⟨χ, hχ⟩ := analyticBound_antipodal_finset s K hK h B hB hdisj d
  have hnorm : (∑ z ∈ C, ‖d z‖) = ∑ z ∈ A, ‖c z‖ := by
    calc
      (∑ z ∈ C, ‖d z‖) = ∑ z ∈ A, ‖d z‖ := by
        apply (Finset.sum_subset (show A ⊆ C from hA) ?_).symm
        intro z _ hz
        simp [d, hz]
      _ = ∑ z ∈ A, ‖c z‖ := by
        apply Finset.sum_congr rfl
        intro z hz
        simp [d, hz]
  have hpoly : (∑ z ∈ C, d z * (χ z : ℂ)) =
      ∑ z ∈ A, c z * (χ z : ℂ) := by
    calc
      (∑ z ∈ C, d z * (χ z : ℂ)) =
          ∑ z ∈ A, d z * (χ z : ℂ) := by
        apply (Finset.sum_subset (show A ⊆ C from hA) ?_).symm
        intro z _ hz
        simp [d, hz]
      _ = ∑ z ∈ A, c z * (χ z : ℂ) := by
        apply Finset.sum_congr rfl
        intro z hz
        simp [d, hz]
  refine ⟨χ, ?_⟩
  change (∑ z ∈ C, ‖d z‖) ≤
    (2 * K) * ‖∑ z ∈ C, d z * (χ z : ℂ)‖ at hχ
  rw [hnorm, hpoly] at hχ
  exact hχ

/-- In an even radical-order cyclotomic grid, the odd-order half of each
canonical coset. -/
private def halfGrid (n q : ℕ) : Set ℂ :=
  {z | ∃ i : Fin (n / radical n), ∃ w ∈ nthRoots q,
    z = zeta n ^ (i : ℕ) * w}

private theorem nthRoots_half_subset {n q : ℕ}
    (hr : radical n = 2 * q) : nthRoots q ⊆ nthRoots (radical n) := by
  intro w hw
  change w ^ q = 1 at hw
  change w ^ radical n = 1
  rw [hr, mul_comm 2 q, pow_mul, hw, one_pow]

private theorem halfGrid_subset_nthRoots (n : ℕ) (hn : 0 < n) (q : ℕ)
    (hr : radical n = 2 * q) : halfGrid n q ⊆ nthRoots n := by
  rintro z ⟨i, w, hw, rfl⟩
  exact radical_coset_mem_nthRoots n hn i w (nthRoots_half_subset hr hw)

private theorem halfGrid_fiber_eq (n : ℕ) (hn : 0 < n) (q : ℕ)
    (hr : radical n = 2 * q) (i : Fin (n / radical n)) :
    {z | z ∈ halfGrid n q ∧ rootCosetIndex n hn z = i} =
      ((fun w : ℂ => zeta n ^ (i : ℕ) * w) '' nthRoots q) := by
  ext z
  constructor
  · rintro ⟨⟨j, w, hw, hzw⟩, hindex⟩
    have hwr : w ∈ nthRoots (radical n) := nthRoots_half_subset hr hw
    have hz : z ∈ nthRoots n :=
      halfGrid_subset_nthRoots n hn q hr ⟨j, w, hw, hzw⟩
    have hj : rootCosetIndex n hn z = j :=
      rootCosetIndex_eq n hn z j w hwr hz hzw
    have hji : j = i := hj.symm.trans hindex
    exact ⟨w, hw, by simpa only [hji] using hzw.symm⟩
  · rintro ⟨w, hw, rfl⟩
    have hwr : w ∈ nthRoots (radical n) := nthRoots_half_subset hr hw
    have hz := radical_coset_mem_nthRoots n hn i w hwr
    exact ⟨⟨i, w, hw, rfl⟩,
      rootCosetIndex_eq n hn _ i w hwr hz rfl⟩

/-- The odd half of every even cyclotomic coset inherits the same positive-real
bound; character choices on distinct cosets glue via their linear independence. -/
theorem positiveRealBound_halfGrid (n : ℕ) (hn : 0 < n) (q : ℕ)
    (hr : radical n = 2 * q) (K : ℝ)
    (h : PositiveRealBound (nthRoots q) K) :
    PositiveRealBound (halfGrid n q) K := by
  apply positiveRealBound_of_fibers (halfGrid n q) (rootCosetIndex n hn) K
  · intro i
    rw [halfGrid_fiber_eq n hn q hr i]
    let u : ℂˣ := Units.mk0 (zeta n ^ (i : ℕ))
      (pow_ne_zero _ (Complex.exp_ne_zero _))
    exact positiveRealBound_scalar u (nthRoots q) K h
  · intro χi
    obtain ⟨χ, hχ⟩ := rootCoset_characters_glue n hn χi
    exact ⟨χ, fun z hz => hχ z (halfGrid_subset_nthRoots n hn q hr hz)⟩

private theorem nthRoots_subset_halfGrid_union_neg (n : ℕ) (hn : 0 < n)
    (q : ℕ) (hr : radical n = 2 * q) (hq : Odd q) :
    nthRoots n ⊆ halfGrid n q ∪ ((fun z : ℂ => -z) '' halfGrid n q) := by
  intro z hz
  obtain ⟨w, hw, hzw⟩ := rootCosetIndex_spec n hn z hz
  have hw' : w ∈ nthRoots (2 * q) := by simpa only [hr] using hw
  rw [nthRoots_two_mul_odd q hq] at hw'
  rcases hw' with hwq | ⟨v, hv, hvw⟩
  · exact Or.inl ⟨rootCosetIndex n hn z, w, hwq, hzw⟩
  · right
    refine ⟨zeta n ^ (rootCosetIndex n hn z : ℕ) * v,
      ⟨rootCosetIndex n hn z, v, hv, rfl⟩, ?_⟩
    calc
      -(zeta n ^ (rootCosetIndex n hn z : ℕ) * v) =
          zeta n ^ (rootCosetIndex n hn z : ℕ) * (-v) := by ring
      _ = zeta n ^ (rootCosetIndex n hn z : ℕ) * w := by
        simpa using congrArg (fun t : ℂ => zeta n ^ (rootCosetIndex n hn z : ℕ) * t) hvw
      _ = z := hzw.symm

private theorem halfGrid_neg_not_mem (n : ℕ) (hn : 0 < n) (q : ℕ)
    (hr : radical n = 2 * q) (hq : Odd q)
    (z : ℂ) (hz : z ∈ halfGrid n q) : -z ∉ halfGrid n q := by
  rintro ⟨j, v, hv, hnegz⟩
  obtain ⟨i, w, hw, hzw⟩ := hz
  have hwr : w ∈ nthRoots (radical n) := nthRoots_half_subset hr hw
  have hnegvr : -v ∈ nthRoots (radical n) := by
    change (-v) ^ radical n = 1
    change v ^ q = 1 at hv
    rw [hr, mul_comm 2 q, pow_mul, hq.neg_pow, hv]
    norm_num
  have heq : zeta n ^ (i : ℕ) * w = zeta n ^ (j : ℕ) * (-v) := by
    calc
      zeta n ^ (i : ℕ) * w = z := hzw.symm
      _ = -(-z) := by simp
      _ = -(zeta n ^ (j : ℕ) * v) := by rw [hnegz]
      _ = zeta n ^ (j : ℕ) * (-v) := by ring
  have hij : i = j := radical_coset_unique n hn hwr hnegvr heq
  rw [hij] at heq
  have hwv : w = -v :=
    mul_left_cancel₀ (pow_ne_zero _ (Complex.exp_ne_zero _)) heq
  have hp := congrArg (fun t : ℂ => t ^ q) hwv
  change w ^ q = 1 at hw
  change v ^ q = 1 at hv
  rw [hq.neg_pow, hw, hv] at hp
  norm_num at hp

/-- A finite subset of an even cyclotomic grid has a finite set of odd-half
representatives whose antipodal union covers it. -/
private theorem finite_halfGrid_cover (n : ℕ) (hn : 0 < n) (q : ℕ)
    (hr : radical n = 2 * q) (hq : Odd q)
    (A : Finset ℂ) (hA : (↑A : Set ℂ) ⊆ nthRoots n) :
    ∃ B : Finset ℂ, (↑B : Set ℂ) ⊆ halfGrid n q ∧
      Disjoint B (B.map (AddEquiv.neg ℂ).toEmbedding) ∧
      A ⊆ B ∪ B.map (AddEquiv.neg ℂ).toEmbedding := by
  classical
  let H := halfGrid n q
  let As := A.filter (fun z => z ∈ H)
  let At := A.filter (fun z => z ∉ H)
  let B := As ∪ At.map (AddEquiv.neg ℂ).toEmbedding
  have hB : (↑B : Set ℂ) ⊆ H := by
    intro z hz
    rcases Finset.mem_union.mp hz with hzAs | hzAt
    · exact (Finset.mem_filter.mp hzAs).2
    · obtain ⟨y, hy, rfl⟩ := Finset.mem_map.mp hzAt
      obtain ⟨hyA, hyNot⟩ := Finset.mem_filter.mp hy
      have hyCover := nthRoots_subset_halfGrid_union_neg n hn q hr hq (hA hyA)
      rcases hyCover with hyH | ⟨x, hx, hxy⟩
      · exact False.elim (hyNot hyH)
      · have heq : -y = x := by rw [← hxy]; simp
        change -y ∈ H
        simpa only [heq] using hx
  refine ⟨B, hB, ?_, ?_⟩
  · apply Finset.disjoint_left.mpr
    intro z hzB hzNeg
    obtain ⟨y, hy, hzy⟩ := Finset.mem_map.mp hzNeg
    have hyH : y ∈ H := hB hy
    have hzH : z ∈ H := hB hzB
    have hnegz : -z ∈ H := by
      rw [← hzy]
      simpa using hyH
    exact halfGrid_neg_not_mem n hn q hr hq z hzH hnegz
  · intro z hzA
    by_cases hzH : z ∈ H
    · apply Finset.mem_union.mpr
      left
      apply Finset.mem_union.mpr
      left
      exact Finset.mem_filter.mpr ⟨hzA, hzH⟩
    · apply Finset.mem_union.mpr
      right
      apply Finset.mem_map.mpr
      refine ⟨-z, ?_, by simp⟩
      apply Finset.mem_union.mpr
      right
      apply Finset.mem_map.mpr
      exact ⟨z, Finset.mem_filter.mpr ⟨hzA, hzH⟩, by simp⟩

/-- The analytic Sidon assertion for all complex roots follows from one
positive-real bound on every odd squarefree root grid. The even-order case
uses antipodal pairs and loses a factor of two. -/
theorem analyticSidon_of_odd_squarefree_positiveRealBound (K : ℝ) (hK : 0 < K)
    (h : ∀ q : ℕ, 0 < q → Odd q → Squarefree q →
      PositiveRealBound (nthRoots q) K) : AnalyticSidon := by
  apply analyticSidon_iff_finiteOrders.mpr
  refine ⟨2 * K, by positivity, ?_⟩
  intro n hn A hA c
  by_cases hodd : Odd (radical n)
  · obtain ⟨χ, hχ⟩ :=
      positiveRealBound_of_radical n hn K
        (h (radical n) (radical_pos n) hodd (radical_squarefree n)) A hA c
    refine ⟨χ, hχ.trans ?_⟩
    let P : ℂ := ∑ z ∈ A, c z * (χ z : ℂ)
    calc
      K * P.re ≤ K * ‖P‖ :=
        mul_le_mul_of_nonneg_left (Complex.re_le_norm P) hK.le
      _ ≤ (2 * K) * ‖P‖ :=
        mul_le_mul_of_nonneg_right (by linarith : K ≤ 2 * K) (norm_nonneg P)
  · have heven : Even (radical n) := Nat.not_odd_iff_even.mp hodd
    let q := radical n / 2
    have hr : radical n = 2 * q := by
      simpa [q] using (Nat.mul_div_cancel' (even_iff_two_dvd.mp heven)).symm
    have hq : Odd q := squarefree_even_half_odd (radical_squarefree n) heven
    have hqPos : 0 < q := by have := radical_pos n; omega
    have hqSq : Squarefree q :=
      (radical_squarefree n).squarefree_of_dvd
        ⟨2, by simpa [mul_comm] using hr⟩
    have hHalf : PositiveRealBound (halfGrid n q) K :=
      positiveRealBound_halfGrid n hn q hr K (h q hqPos hq hqSq)
    obtain ⟨B, hB, hdisj, hcover⟩ := finite_halfGrid_cover n hn q hr hq A hA
    exact analyticBound_antipodal_finset_subset (halfGrid n q) K hK.le
      hHalf B hB hdisj A hcover c

end Erdos.Research.Problem774
