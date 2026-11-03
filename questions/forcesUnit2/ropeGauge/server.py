import random
import math
from forces_practice import G, fmt, part, deliver

def s(x): return math.sin(math.radians(x))
def c(x): return math.cos(math.radians(x))
def t(x): return math.tan(math.radians(x))
def num(name,prompt,values,unit,solution):
    return part(name,prompt,fmt(values[0])+unit,[fmt(v)+unit for v in values[1:]],solution)

CASES=[(F,) for F in (35,48,65,82)]
def build(data,case):
    F,=case
    context=f'<p>Two force-controlled winches pull opposite ends of a straight, light rope, each with {F} N. A light force gauge is inserted in the rope. The rope is at rest. One winch is then replaced by a rigid wall anchor, and the remaining winch still pulls with {F} N; equilibrium is restored.</p>'
    parts=[part('gauge','Which pair gives the gauge reading before and after the replacement?',f'{F} N before; {F} N after.',[f'{2*F} N before; {F} N after.',f'0 N before; {F} N after.',f'{F} N before; {2*F} N after.'],f'Cut the rope mentally at the gauge. Each section is in equilibrium under two opposing forces of magnitude {F} N. Tension is {F} N, rather than the sum or resultant of the two end forces. The wall provides the same opposing end force as the removed winch.'),
    part('partner','Which is the third-law partner of the wall’s force on the rope?','The rope’s force on the wall.',['The remaining winch’s force on the rope.','The tension force at the gauge on the same rope section.','The weight of the wall.'],'Reverse the interacting bodies: wall on rope pairs with rope on wall. Opposite forces acting on one object can balance without being a third-law pair.')]
    deliver(data,context,parts,dict(F=F))


def generate(data):
    build(data, random.choice(CASES))
