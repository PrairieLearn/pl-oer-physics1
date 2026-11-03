import random
import math
from forces_practice import G, fmt, part, deliver

def s(x): return math.sin(math.radians(x))
def c(x): return math.cos(math.radians(x))
def t(x): return math.tan(math.radians(x))
def num(name,prompt,values,unit,solution):
    return part(name,prompt,fmt(values[0])+unit,[fmt(v)+unit for v in values[1:]],solution)

CASES=[(m,a,site) for m in (2,4) for a in (1.5,2.5) for site in ('north','east')]
def build(data,case):
    m,a,site=case; inward='south' if site=='north' else 'west'; tangent='east' if site=='north' else 'south'; T=m*a
    context=f'<p>A {m} kg puck moves clockwise around a circle on a horizontal frictionless table, attached by a taut light cord to a fixed central pin. At the instant considered, the puck is at the {site} side of the circle and its acceleration magnitude is {a} m/s² toward the pin. The cord supplies the only horizontal force. Gravity and the table’s normal force cancel.</p>'
    parts=[part('force','What is the cord’s force on the puck at this instant?',f'{fmt(T)} N toward the {inward}.',[f'{fmt(T)} N toward the {tangent}.',f'{fmt(m*G)} N toward the {inward}.','Zero, because the puck is moving along its path.'],f'The horizontal resultant is the cord tension, so T=ma={fmt(T)} N. It points inward toward the pin, which is {inward} of the puck. The instantaneous velocity is tangent to the path; it is not the force direction.'),
    part('release','If the cord breaks at that instant, what happens next? Assume the puck remains on the table. ',f'It travels in a straight line toward the {tangent} at constant speed.', ['It continues clockwise around the same circle.',f'It travels in a straight line toward the {inward} at constant speed.','It stops because the force maintaining its motion disappears.'],f'When the cord breaks the horizontal force vanishes. The puck retains its instantaneous tangential velocity, toward the {tangent}, and continues in a straight line. The inward acceleration ends when tension ends.')]
    deliver(data,context,parts,dict(m=m,a=a,site=site))


def generate(data):
    build(data, random.choice(CASES))
