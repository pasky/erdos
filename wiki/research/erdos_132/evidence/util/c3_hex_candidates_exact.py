# Unreviewed finite subcase certificate; see ../../independent/c3_13_unreviewed.md.
import sympy as s
x=s.symbols('x', positive=True)
for typ in ['V','E']:
    if typ=='V':
        vals=[s.Integer(1),s.Integer(3),s.Integer(4),x*x,3*x*x,x*x+1-2*x,x*x+1-x,x*x+1+x,x*x+1+2*x]
    else:
        vals=[s.Integer(1),s.Integer(3),s.Integer(4),x*x/3,x*x,x*x/3+1-x,x*x/3+1,x*x/3+1+x]
    roots=set()
    for i in range(len(vals)):
        for j in range(i):
            for a in s.solve(vals[i]-vals[j],x):
                if a.is_real and a.is_positive and a != (1 if typ=='V' else s.sqrt(3)):
                    roots.add(a)
    out=[]
    for a in roots:
        vs={s.expand(s.simplify(v.subs(x,a))) for v in vals}
        if len(vs)<=6:
            out.append((a,len(vs),sorted(vs,key=float)))
    print(typ,'candidates tested',len(roots),'survivors',len(out))
    for a,k,vs in sorted(out,key=lambda t:float(t[0])):
        print('parameter',a,'squared radius',s.simplify(a*a/(1 if typ=='V' else 3)),'q',k,'spectrum',vs)
