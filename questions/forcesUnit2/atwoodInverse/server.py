import random
import math
from forces_practice import G, fmt, part, deliver

def s(x): return math.sin(math.radians(x))
def c(x): return math.cos(math.radians(x))
def t(x): return math.tan(math.radians(x))
def num(name,prompt,values,unit,solution):
    return part(name,prompt,fmt(values[0])+unit,[fmt(v)+unit for v in values[1:]],solution)

CASES=[(m,r) for m in (3,5,7) for r in (0.2,0.4)]
def build(data,case):
    m,r=case; M=m*(1+r)/(1-r); T=m*G*(1+r)
    context=f'<p>A known {m} kg mass and an unknown mass hang from opposite ends of one light, inextensible rope over a fixed massless, frictionless pulley. On release the known mass accelerates upward at exactly {r}g. Both masses remain clear of the floor.</p>'
    parts=[num('hidden','What is the unknown mass?',[M,m*(1-r)/(1+r),m*(1+r),2*m],' kg',f'For the rising known mass, T−mg=ma, so T=mg(1+{r}). For the descending unknown mass, Mg−T=Ma. Thus M=m(g+a)/(g−a)={fmt(M)} kg.'),
    num('tension','What is the tension in the rope?',[T,m*G,M*G,(M+m)*G],' N',f'The known mass accelerates upward, so tension exceeds its weight: T=m(g+a)={fmt(T)} N. The descending mass has tension below its weight. A single ideal rope has the same tension on both sides.')]
    deliver(data,context,parts,dict(m=m,r=r))


def generate(data):
    build(data, random.choice(CASES))
