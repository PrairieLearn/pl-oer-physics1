import random
import math
from forces_practice import G, fmt, part, deliver

def s(x): return math.sin(math.radians(x))
def c(x): return math.cos(math.radians(x))
def t(x): return math.tan(math.radians(x))
def num(name,prompt,values,unit,solution):
    return part(name,prompt,fmt(values[0])+unit,[fmt(v)+unit for v in values[1:]],solution)

CASES=[(W,ratio) for W in (120,180,240) for ratio in (1.5,2.0)]
def build(data,case):
    W,ratio=case; limit=W*ratio; angle=math.degrees(math.asin(1/ratio)); H=math.sqrt(limit**2-W**2)
    context=f'<p>A stationary hanging display weighs {W} N. It is held at a junction by one cable running upward to the right at an adjustable angle above horizontal, and one horizontal tie running left to a wall. The angled cable’s allowed tension is {fmt(limit)} N. The horizontal tie has no relevant tension limit. All cables are light.</p>'
    parts=[num('minimum','What is the smallest permitted angle of the angled cable above horizontal?',[angle,math.degrees(math.acos(1/ratio)),math.degrees(math.atan(1/ratio)),90],'°',f'Only the angled cable supplies an upward component, so T sin θ=W. Requiring T≤{fmt(limit)} N gives sin θ≥W/T_max. Thus θ_min={fmt(angle)}°. Weight is already a force in newtons; do not multiply it by g.'),
    num('tie','At that limiting angle, what is the tension in the horizontal tie?',[H,limit,W,limit+W],' N',f'Horizontal equilibrium gives H=T cos θ. At the minimum angle T=T_max; hence H=√(T_max²−W²)={fmt(H)} N. The horizontal tie supplies no vertical support.')]
    deliver(data,context,parts,dict(W=W,ratio=ratio))


def generate(data):
    build(data, random.choice(CASES))
