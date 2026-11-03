import random
import math
from forces_practice import G, fmt, part, deliver

def s(x): return math.sin(math.radians(x))
def c(x): return math.cos(math.radians(x))
def t(x): return math.tan(math.radians(x))
def num(name,prompt,values,unit,solution):
    return part(name,prompt,fmt(values[0])+unit,[fmt(v)+unit for v in values[1:]],solution)

CASES=[(A,B,T) for A in (25,35) for B in (60,70) for T in (80,140)]
def build(data,case):
    A,B,T=case; U=T*c(A)/c(B); W=T*s(A)+U*s(B)
    context=f'<p>A stationary load is supported by two light cables. The left cable makes {A}° with horizontal and its force sensor reads {T} N. The right cable makes {B}° with horizontal. No other support acts on the load.</p>'
    parts=[num('right','What is the right-cable tension?',[U,T,T*s(A)/s(B),T*c(B)/c(A)],' N',f'Horizontal components must cancel: T_left cos {A}°=T_right cos {B}°. Therefore T_right={fmt(U)} N. The steeper cable needs more tension to produce the same horizontal component.'),
    num('weight','What is the weight of the load?',[W,T+U,T*s(A),W/G],' N',f'Vertical equilibrium gives W=T_left sin {A}°+T_right sin {B}°={fmt(W)} N. Tension magnitudes cannot simply be added because the cables are not vertical. Dividing by g would give mass in kilograms, not weight.')]
    deliver(data,context,parts,dict(A=A,B=B,T=T))


def generate(data):
    build(data, random.choice(CASES))
