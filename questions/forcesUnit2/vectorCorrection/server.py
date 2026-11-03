import random
import math
from forces_practice import G, fmt, part, deliver

def s(x): return math.sin(math.radians(x))
def c(x): return math.cos(math.radians(x))
def t(x): return math.tan(math.radians(x))
def num(name,prompt,values,unit,solution):
    return part(name,prompt,fmt(values[0])+unit,[fmt(v)+unit for v in values[1:]],solution)

CASES=[(m,F,A,H) for m in (4,6) for F in (18,26) for A in (30,50) for H in (6,10)]
def build(data,case):
    m,F,A,H=case; X=F*c(A)-H; Y=F*s(A); C=math.hypot(X,Y); angle=math.degrees(math.atan2(Y,X)); a=X/m
    context=f'<p>A {m} kg puck moves on a horizontal frictionless table. In the table’s plane, thruster 1 exerts {F} N at {A}° north of east, and thruster 2 exerts {H} N west. Gravity and the table’s normal force cancel vertically. A third thruster can act in any direction in the table’s plane.</p>'
    parts=[num('east','The third thruster is set due south just strongly enough that the puck’s acceleration is due east. What is that eastward acceleration?',[a,F/m,(F-H)/m,(F*c(A)+H)/m],' m/s²',f'The third thruster removes the northward component F sin θ. It contributes no eastward force. The remaining eastward resultant is F cos θ−H, so a={fmt(a)} m/s². Cancellation along one axis does not imply equilibrium.'),
    part('equilibrium','Instead, what third force would make the entire in-plane acceleration zero?',f'{fmt(C)} N at {fmt(angle)}° south of west.',[f'{fmt(C)} N at {fmt(angle)}° north of east.',f'{fmt(Y)} N due south.',f'{fmt(F+H)} N due west.'],f'The first two forces sum to ({fmt(X)} east, {fmt(Y)} north) N. The correcting force is the opposite vector. Its magnitude is √(X²+Y²)={fmt(C)} N and angle is atan2(Y,X)={fmt(angle)}° south of west.')]
    deliver(data,context,parts,dict(m=m,F=F,A=A,H=H))


def generate(data):
    build(data, random.choice(CASES))
