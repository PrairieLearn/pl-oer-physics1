import random
import math
from forces_practice import G, fmt, part, deliver

def s(x): return math.sin(math.radians(x))
def c(x): return math.cos(math.radians(x))
def t(x): return math.tan(math.radians(x))
def num(name,prompt,values,unit,solution):
    return part(name,prompt,fmt(values[0])+unit,[fmt(v)+unit for v in values[1:]],solution)

CASES=[(m,A,B) for m in (3,5) for A,B in ((25,60),(35,70))]
def build(data,case):
    m,A,B=case; F=m*G/s(B); N=F*c(B)
    context=f'<p>A {m} kg specimen is held stationary against a vertical frictionless wall on its left by a force directed upward and toward the wall. Initially the force makes {A}° above the leftward horizontal. Its direction is changed to {B}° above that horizontal and its magnitude is adjusted to keep the specimen at rest.</p>'
    parts=[num('newforce','What applied-force magnitude is needed after the direction changes?',[F,m*G/c(B),m*G,m*G/s(A)],' N',f'The smooth wall supplies only a horizontal normal force. Vertical balance requires F sin {B}°=mg, so F={fmt(F)} N.'),
    part('wall','Compared with the initial trial, how does the wall’s normal force change?','It decreases, and it points horizontally away from the wall.',['It increases, and it points horizontally away from the wall.','It stays equal to the specimen’s weight, vertically upward.','It decreases, and it points into the wall.'],f'N=F cos θ=mg cot θ. Increasing θ decreases cot θ. The new N={fmt(N)} N. A normal force is perpendicular to the contact surface and pushes the specimen away from the wall.')]
    deliver(data,context,parts,dict(m=m,A=A,B=B))


def generate(data):
    build(data, random.choice(CASES))
