import random
import math
from forces_practice import G, fmt, part, deliver

def s(x): return math.sin(math.radians(x))
def c(x): return math.cos(math.radians(x))
def t(x): return math.tan(math.radians(x))
def num(name,prompt,values,unit,solution):
    return part(name,prompt,fmt(values[0])+unit,[fmt(v)+unit for v in values[1:]],solution)

CASES = [(m,M,a) for m in (3,5) for M in (7,9) for a in (1.4,2.8)]
def build(data, case):
    m,M,a=case; lower=m*(G+a); upper=(M+m)*(G+a)
    context=f'<p>A {m} kg instrument hangs from an unknown-mass case by a light vertical cord. A second light cord connects the case to a lift ceiling. Both remain fixed relative to the lift. The lower sensor reads {fmt(lower)} N and the upper reads {fmt(upper)} N. The lift is moving downward.</p>'
    parts=[num('mass','What is the mass of the case?', [M,upper/G-m,upper/(G+a),lower/G], ' kg', f'The lower instrument gives g+a=T_lower/m={fmt(G+a)} m/s². For the complete hanging system, T_upper=(M+m)(g+a). Thus M=T_upper/(g+a)−m={fmt(M)} kg. The upper cord supports and accelerates both objects.'),
    part('motion','What do the readings imply about the lift’s motion?',f'It accelerates upward at {fmt(a)} m/s² and slows down.',[f'It accelerates downward at {fmt(a)} m/s² and speeds up.','It moves downward at constant velocity.',f'It accelerates upward at {fmt(lower/m)} m/s² and slows down.'],f'T_lower−mg=ma gives a={fmt(a)} m/s² upward. Acceleration is opposite the stated downward velocity, so the speed decreases.')]
    deliver(data,context,parts,dict(m=m,M=M,a=a,lower=lower,upper=upper))


def generate(data):
    build(data, random.choice(CASES))
