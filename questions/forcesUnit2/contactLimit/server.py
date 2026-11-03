import random
import math
from forces_practice import G, fmt, part, deliver

def s(x): return math.sin(math.radians(x))
def c(x): return math.cos(math.radians(x))
def t(x): return math.tan(math.radians(x))
def num(name,prompt,values,unit,solution):
    return part(name,prompt,fmt(values[0])+unit,[fmt(v)+unit for v in values[1:]],solution)

CASES=[(m,A,fraction) for m in (6,10) for A in (30,40,55) for fraction in (0.4,0.7)]
def build(data,case):
    m,A,fraction=case; N=m*G*fraction; T=(m*G-N)/s(A); a=T*c(A)/m; maxa=G/t(A)
    context=f'<p>A {m} kg package is pulled across a horizontal frictionless floor by a light rope at {A}° above horizontal. While contact is maintained, a sensor reports that the normal force is exactly {fraction} times the package’s weight. The rope’s angle stays fixed as the pull is increased.</p>'
    parts=[num('acceleration','What is the horizontal acceleration at the stated sensor reading?',[a,G*(1-fraction),G*(1-fraction)*t(A),G/t(A)],' m/s²',f'Vertical acceleration is zero while contact is maintained: N+T sin θ=mg. Hence T=mg(1−{fraction})/sin θ. Horizontally, a=T cos θ/m=g(1−{fraction})cot θ={fmt(a)} m/s².'),
    part('threshold','At the greatest pull for which contact can still be maintained, what is the horizontal acceleration, and how would doubling the mass change that value?',f'{fmt(maxa)} m/s²; doubling the mass leaves this limiting acceleration unchanged.',[f'{fmt(maxa)} m/s²; doubling the mass doubles this limiting acceleration.',f'{fmt(G*t(A))} m/s²; doubling the mass leaves this limiting acceleration unchanged.',f'{fmt(a)} m/s²; doubling the mass halves this limiting acceleration.'],f'At the threshold N=0, so T_max sin θ=mg. Therefore a_max=T_max cos θ/m=g cot θ={fmt(maxa)} m/s². Mass cancels. A floor cannot provide a negative normal force; beyond this threshold the vertical-contact model fails.')]
    deliver(data,context,parts,dict(m=m,A=A,fraction=fraction))


def generate(data):
    build(data, random.choice(CASES))
