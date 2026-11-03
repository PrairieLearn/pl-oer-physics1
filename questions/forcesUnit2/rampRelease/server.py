import random
import math
from forces_practice import G, fmt, part, deliver

def s(x): return math.sin(math.radians(x))
def c(x): return math.cos(math.radians(x))
def t(x): return math.tan(math.radians(x))
def num(name,prompt,values,unit,solution):
    return part(name,prompt,fmt(values[0])+unit,[fmt(v)+unit for v in values[1:]],solution)

CASES=[(m,angle) for m in (4,7) for angle in (30,40,60)]
def build(data,case):
    m,angle=case; ratio=s(angle); a=G*ratio
    context=f'<p>A {m} kg glider rests on a frictionless ramp. A light string parallel to the ramp holds it still; its tension is exactly {ratio:.6f} times the glider’s weight (this ratio is rounded). In another trial on the same ramp, a launcher gives the glider an initial velocity up the ramp and then loses contact. Ignore air resistance.</p>'
    parts=[num('angle','What is the ramp angle above horizontal, to the nearest degree?',[angle,90,math.degrees(math.atan(ratio)),math.degrees(math.acos(ratio/2))],'°',f'Equilibrium along the ramp requires T=mg sin θ. Therefore sin θ={ratio:.6f} and θ={angle}°. Use the component parallel to the ramp.'),
    num('drive','While the glider is still moving uphill in the launch trial, the launcher exerts a force parallel to the ramp and produces an uphill acceleration of 2.00 m/s². What is the launcher force before it loses contact?', [m*(2+G*ratio),2*m,m*G*ratio,m*(G*ratio-2)], ' N', f'With uphill positive, F_launcher−mg sin θ=m(2.00). The holding experiment already gave mg sin θ as {ratio:.6f} times the weight. Therefore F_launcher=m(2.00+g sin θ)={fmt(m*(2+G*ratio))} N. The launcher must both oppose the downhill weight component and provide the uphill resultant.'),
    part('turn','After the launcher loses contact, what is the acceleration just before, at, and just after the glider’s highest point?',f'{fmt(a)} m/s² down the ramp at all three instants.',[f'{fmt(a)} m/s² down the ramp except zero at the highest point.',f'{fmt(a)} m/s² opposite its velocity, switching direction after the highest point.',f'{fmt(G*c(angle))} m/s² down the ramp at all three instants.'],f'After release only gravity and the perpendicular normal force act. Along the ramp, a=−g sin θ if uphill is positive. A zero instantaneous velocity does not remove gravity or change acceleration.')]
    deliver(data,context,parts,dict(m=m,angle=angle))


def generate(data):
    build(data, random.choice(CASES))
