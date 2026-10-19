"""Write the side-free relaxation of a bad k-list assignment as DIMACS CNF (discovery only).

Badness of a signed system (left family A, right family B) implies that the
k-uniform hypergraph A u B has no proper 2-colouring: for a colouring with red
set T, a left list disjoint from T or a right list inside T is a monochromatic
list. This writes: one variable per k-subset of the n colours, every colour pair
inside a selected subset, at most v selected subsets, per-colour degree at
least ceil((n-1)/(k-1)) (or exact --degrees), the first --fix subsets
{0..k-1} and {k..2k-1} selected, and for every 2-colouring of the palette (T and
its complement give one clause) not already settled by a fixed subset, the
clause "some selected subset is monochromatic". UNSAT would exclude the signed
domain it relaxes; SAT gives candidate hypergraphs whose signings still need
testing; UNKNOWN proves nothing.

usage: python side_free_cnf.py OUT.cnf [--n 17 --k 4 --v 26 --fix 2 --degrees ...]
"""
import argparse, itertools, sys, os, shutil
import numpy as np
ap = argparse.ArgumentParser()
ap.add_argument('out')
ap.add_argument('--n', type=int, default=17)
ap.add_argument('--k', type=int, default=4)
ap.add_argument('--v', type=int, default=26)
ap.add_argument('--fix', type=int, default=2)
ap.add_argument('--degrees', default='')
args = ap.parse_args()
n, k, v = args.n, args.k, args.v
blocks = [sum(1 << c for c in comb) for comb in itertools.combinations(range(n), k)]
nb = len(blocks)
barr = np.array(blocks, dtype=np.int64)
X = lambda s: s + 1
nvars = nb
clauses = []
for x, y in itertools.combinations(range(n), 2):
    pm = (1 << x) | (1 << y)
    clauses.append(tuple(X(s) for s in range(nb) if blocks[s] & pm == pm))

def atmost(lits, kk):
    global nvars
    out = []; m = len(lits)
    if kk >= m: return out
    if kk == 0: return [(-x,) for x in lits]
    reg = [[0] * (kk + 1) for _ in range(m)]
    for i in range(m - 1):
        for j in range(1, kk + 1):
            nvars += 1; reg[i][j] = nvars
    x = lits
    out.append((-x[0], reg[0][1]))
    for j in range(2, kk + 1): out.append((-reg[0][j],))
    for i in range(1, m - 1):
        out.append((-x[i], reg[i][1])); out.append((-reg[i - 1][1], reg[i][1]))
        for j in range(2, kk + 1):
            out.append((-x[i], -reg[i - 1][j - 1], reg[i][j])); out.append((-reg[i - 1][j], reg[i][j]))
        out.append((-x[i], -reg[i - 1][kk]))
    out.append((-x[m - 1], -reg[m - 2][kk]))
    return out

def atleast(lits, kk):
    global nvars
    out = []; m = len(lits)
    if kk <= 0: return out
    s = [[None] * (kk + 1) for _ in range(m + 1)]
    for i in range(1, m + 1):
        for j in range(1, kk + 1):
            nvars += 1; s[i][j] = nvars
    for i in range(1, m + 1):
        for j in range(1, kk + 1):
            pj = s[i - 1][j]
            c1 = [-s[i][j], lits[i - 1]] + ([pj] if pj is not None else [])
            out.append(tuple(c1))
            if j >= 2:
                c2 = ([-s[i][j], s[i - 1][j - 1]] if s[i - 1][j - 1] is not None else [-s[i][j]]) + ([pj] if pj is not None else [])
                out.append(tuple(c2))
    out.append((s[m][kk],))
    return out

clauses += atmost([X(s) for s in range(nb)], v)
dmin = -(-(n - 1) // (k - 1))
exact = [int(t) for t in args.degrees.split(',')] if args.degrees else None
for x in range(n):
    lits = [X(s) for s in range(nb) if blocks[s] >> x & 1]
    if exact is None:
        clauses += atleast(lits, dmin)
    else:
        clauses += atleast(lits, exact[x]); clauses += atmost(lits, exact[x])
fixed = []
if args.fix >= 1: fixed.append(sum(1 << c for c in range(0, k)))
if args.fix >= 2: fixed.append(sum(1 << c for c in range(k, 2 * k)))
for f in fixed: clauses.append((X(blocks.index(f)),))
full = (1 << n) - 1
body = args.out + '.body'; ncl_T = 0
with open(body, 'w') as fh:
    for c in clauses: fh.write(' '.join(map(str, c)) + ' 0\n')
    lines = []
    for T in range(1 << (n - 1)):  # T and its complement give the same clause; fix colour n-1 outside T
        if any((T & f) == 0 or (T & f) == f for f in fixed):
            continue
        mono = np.nonzero(((barr & T) == 0) | ((barr & ~T & full) == 0))[0] + 1
        lines.append(' '.join(map(str, mono)) + ' 0\n'); ncl_T += 1
        if len(lines) >= 4096: fh.writelines(lines); lines = []
    fh.writelines(lines)
with open(args.out, 'w') as out:
    out.write(f'p cnf {nvars} {len(clauses) + ncl_T}\n')
    with open(body) as fh: shutil.copyfileobj(fh, out)
os.remove(body)
print(f'vars={nvars} clauses={len(clauses)+ncl_T} (T-clauses {ncl_T})', file=sys.stderr)
