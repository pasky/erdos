-- EXPECT: Erdos.L9995.claim (Erdos.AuditSelfTestProbe): 1 compiler axiom evaluated true
-- EXPECT: claims, 1 compiler axioms: AUDIT PASS
-- MODE: print
-- RECORD: L9995 Erdos.L9995.claim
-- RECORD: L9994 Erdos.L9995.claim
-- RECORD: top Erdos.L9995.claim
-- A native_decide claim and a claim that uses it: the manifest must
-- record the minted compiler axiom, with the declaration whose proof
-- term uses it, in the claim's row, in the user's row and in the
-- top-level array.
def Erdos.L9995.statement : Prop := 1 + 1 = 2
theorem Erdos.L9995.claim : Erdos.L9995.statement := by
  show 1 + 1 = 2
  native_decide
def Erdos.L9994.statement : Prop := Erdos.L9995.statement
theorem Erdos.L9994.claim : Erdos.L9994.statement := Erdos.L9995.claim
