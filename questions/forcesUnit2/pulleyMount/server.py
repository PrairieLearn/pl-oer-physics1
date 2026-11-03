import random
import math
from forces_practice import G, fmt, part, deliver

def s(x): return math.sin(math.radians(x))
def c(x): return math.cos(math.radians(x))
def t(x): return math.tan(math.radians(x))
def num(name,prompt,values,unit,solution):
    return part(name,prompt,fmt(values[0])+unit,[fmt(v)+unit for v in values[1:]],solution)

CASES=[(m,) for m in (4,6,9)]
def build(data,case):
    m,=case; T=m*G; F=math.sqrt(2)*T
    context=f'<p>A stationary {m} kg load hangs from a light rope passing over a massless, frictionless fixed pulley. One rope segment leaves the pulley vertically downward; the other leaves horizontally to the right and is anchored. In a second mounting arrangement, both segments leave the pulley vertically downward; the same load remains at rest.</p>'
    parts=[part('support','What force must the bracket exert on the pulley in the first arrangement?',f'{fmt(F)} N, directed 45° above the horizontal toward the left.',[f'{fmt(2*T)} N, vertically upward.',f'{fmt(T)} N, vertically upward.',f'{fmt(F)} N, directed 45° below the horizontal toward the right.'],f'Tension equals the supported weight, T=mg={fmt(T)} N. The rope pulls the pulley rightward and downward with equal magnitudes T. The bracket must supply equal leftward and upward components; its magnitude is √(T²+T²)={fmt(F)} N.'),
    num('second','What is the bracket-force magnitude in the second arrangement?',[2*T,T,F,0],' N','Both rope segments now pull downward. Their vector sum has magnitude 2T, so the bracket must exert 2T upward. Rope tension remains T; changing rope direction changes the mount load.')]
    deliver(data,context,parts,dict(m=m))


def generate(data):
    build(data, random.choice(CASES))
