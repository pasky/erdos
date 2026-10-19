"""Write the signed Boolean formulation of a bad k-list assignment as DIMACS CNF (discovery only).

Variables L_s = s+1 and R_s = C(n,k)+s+1 select the k-subset number s (in
itertools.combinations order) as a left or a right list. Clauses: at most one
side per subset (unless --allow-both), every colour pair inside a selected list,
at most v selected lists, an optional window --amin/--amax on the number of left
lists, per-colour degree bounds (exact with --degrees, else at least
ceil((n-1)/(k-1))), the first --fix lists {0..k-1} and {k..2k-1} fixed on the
left, and, for every palette subset T not already settled by a fixed list, the
clause "some selected left list is disjoint from T or some selected right list
lies inside T". Cardinalities use sequential counters. A satisfying assignment
is a candidate bad assignment and must be re-checked independently; UNKNOWN
from a solver proves nothing.

usage: python signed_cnf.py OUT.cnf [--n 17 --k 4 --v 26 --amin 12 --amax 13 --fix 2 --degrees ...]
"""
import argparse, sys, itertools
import numpy as np

ap = argparse.ArgumentParser()
ap.add_argument('out')
ap.add_argument('--n', type=int, default=17)
ap.add_argument('--k', type=int, default=4)
ap.add_argument('--v', type=int, default=26)
ap.add_argument('--amin', type=int, default=0)
ap.add_argument('--amax', type=int, default=10**9)
ap.add_argument('--fix', type=int, default=2, help='number of fixed disjoint left lists (0,1,2)')
ap.add_argument('--degrees', default='', help='comma list of exact color degrees (n ints); empty = only the implied lower bound')
ap.add_argument('--allow-both', action='store_true', help='let a block be on both sides (counts twice)')
args = ap.parse_args()
n, k, v = args.n, args.k, args.v
blocks = [sum(1 << c for c in comb) for comb in itertools.combinations(range(n), k)]
nb = len(blocks)
barr = np.array(blocks, dtype=np.int64)
L = lambda s: s + 1
R = lambda s: nb + s + 1
nvars = 2 * nb
clauses = []  # small structural clauses kept in memory; T-clauses streamed

# at most one side per block
if not args.allow_both:
    for s in range(nb):
        clauses.append((-L(s), -R(s)))
# pair coverage
for x, y in itertools.combinations(range(n), 2):
    pm = (1 << x) | (1 << y)
    lits = []
    for s in range(nb):
        if blocks[s] & pm == pm:
            lits += [L(s), R(s)]
    clauses.append(tuple(lits))

def seq_counter_atmost(lits, kk):
    """Sinz sequential counter: at most kk of lits true. Returns clauses, uses fresh vars."""
    global nvars
    out = []
    m = len(lits)
    if kk >= m:
        return out
    if kk == 0:
        return [(-x,) for x in lits]
    reg = [[0] * (kk + 1) for _ in range(m)]
    for i in range(m - 1):
        for j in range(1, kk + 1):
            nvars += 1
            reg[i][j] = nvars
    x = lits
    out.append((-x[0], reg[0][1]))
    for j in range(2, kk + 1):
        out.append((-reg[0][j],))
    for i in range(1, m - 1):
        out.append((-x[i], reg[i][1]))
        out.append((-reg[i - 1][1], reg[i][1]))
        for j in range(2, kk + 1):
            out.append((-x[i], -reg[i - 1][j - 1], reg[i][j]))
            out.append((-reg[i - 1][j], reg[i][j]))
        out.append((-x[i], -reg[i - 1][kk]))
    out.append((-x[m - 1], -reg[m - 2][kk]))
    return out

def seq_counter_atleast(lits, kk):
    """Direct at-least-kk sequential counter: s[i][j] -> at least j of lits[:i] true; assert s[n][kk]."""
    global nvars
    out = []
    m = len(lits)
    if kk <= 0:
        return out
    if kk > m:
        return [(lits[0],), (-lits[0],)]  # unsatisfiable
    s = [[None] * (kk + 1) for _ in range(m + 1)]  # s[0][j] false (j>=1); s[i][0] true
    for i in range(1, m + 1):
        for j in range(1, kk + 1):
            nvars += 1
            s[i][j] = nvars
    for i in range(1, m + 1):
        for j in range(1, kk + 1):
            prev_j = s[i - 1][j]            # None means false
            c1 = [-s[i][j], lits[i - 1]]
            if prev_j is not None:
                c1.append(prev_j)
            out.append(tuple(c1))
            if j >= 2:
                c2 = [-s[i][j], s[i - 1][j - 1]] if s[i - 1][j - 1] is not None else [-s[i][j]]
                if prev_j is not None:
                    c2.append(prev_j)
                out.append(tuple(c2))
    out.append((s[m][kk],))
    return out

all_lits = [L(s) for s in range(nb)] + [R(s) for s in range(nb)]
clauses += seq_counter_atmost(all_lits, v)          # at most v blocks; pair coverage forces 26 only in the (17,4,26) case
left = [L(s) for s in range(nb)]
if args.amin > 0:
    clauses += seq_counter_atleast(left, args.amin)
if args.amax < nb:
    clauses += seq_counter_atmost(left, args.amax)
# per-color degree: exact values when given, else the lower bound implied by pair coverage
dmin = -(-(n - 1) // (k - 1))
exact = [int(t) for t in args.degrees.split(',')] if args.degrees else None
for x in range(n):
    lits = []
    for s in range(nb):
        if blocks[s] >> x & 1:
            lits += [L(s), R(s)]
    if exact is None:
        clauses += seq_counter_atleast(lits, dmin)
    else:
        clauses += seq_counter_atleast(lits, exact[x])
        clauses += seq_counter_atmost(lits, exact[x])
# fixed disjoint left lists
fixed = []
if args.fix >= 1:
    fixed.append(sum(1 << c for c in range(0, k)))
if args.fix >= 2:
    fixed.append(sum(1 << c for c in range(k, 2 * k)))
for f in fixed:
    clauses.append((L(blocks.index(f)),))

full = (1 << n) - 1
ncl_T = 0
body = args.out + '.body'
with open(body, 'w') as fh:
    for c in clauses:
        fh.write(' '.join(map(str, c)) + ' 0\n')
    lines = []
    for T in range(1 << n):
        if any(T & f == 0 for f in fixed):
            continue  # satisfied by a fixed left list
        disj = np.nonzero((barr & T) == 0)[0] + 1
        cont = np.nonzero((barr & ~T) == 0)[0] + 1 + nb
        lines.append(' '.join(map(str, disj)) + ' ' + ' '.join(map(str, cont)) + ' 0\n')
        ncl_T += 1
        if len(lines) >= 4096:
            fh.writelines(lines); lines = []
    fh.writelines(lines)
total = len(clauses) + ncl_T
import shutil, os
with open(args.out, 'w') as out:
    out.write(f'p cnf {nvars} {total}\n')
    with open(body) as fh:
        shutil.copyfileobj(fh, out)
os.remove(body)
print(f'vars={nvars} clauses={total} (T-clauses {ncl_T}, structural {len(clauses)})', file=sys.stderr)
