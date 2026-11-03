import random
import math
from forces_practice import G, fmt, part, deliver

def s(x): return math.sin(math.radians(x))
def c(x): return math.cos(math.radians(x))
def t(x): return math.tan(math.radians(x))
def num(name,prompt,values,unit,solution):
    return part(name,prompt,fmt(values[0])+unit,[fmt(v)+unit for v in values[1:]],solution)

CASES=[(m,angle,P) for m in (3,6) for angle in (25,40) for P in (12,20)]
def build(data,case):
    m,angle,P=case; N=m*G*c(angle)+P; a=G*s(angle)
    context=f'<p>A {m} kg slider is moving down a frictionless ramp inclined at {angle}° above horizontal. A device now presses it directly into the ramp with a force of {P} N, exactly perpendicular to the surface. The slider remains in contact.</p>'
    parts=[num('normal','What normal force does the ramp exert while the device presses?',[N,m*G*c(angle),m*G+P,m*G*c(angle)-P],' N',f'There is no acceleration perpendicular to the ramp. The ramp balances both the inward weight component and the device: N=mg cos θ+P={fmt(N)} N.'),
    part('acceleration','How does pressing change the downhill acceleration?','It stays the same because the added force has no component along the ramp.',['It increases because the total force magnitude increases.','It becomes zero because the normal force balances all of gravity.','It decreases because a larger normal force always creates friction.'],f'The surface is frictionless. The new force is perpendicular to motion and contributes nothing along the ramp; a=g sin θ={fmt(a)} m/s² downhill.')]
    deliver(data,context,parts,dict(m=m,angle=angle,P=P))


def generate(data):
    build(data, random.choice(CASES))
