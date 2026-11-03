import random
import math
from forces_practice import G, fmt, part, deliver

def s(x): return math.sin(math.radians(x))
def c(x): return math.cos(math.radians(x))
def t(x): return math.tan(math.radians(x))
def num(name,prompt,values,unit,solution):
    return part(name,prompt,fmt(values[0])+unit,[fmt(v)+unit for v in values[1:]],solution)

CASES=[(m,A) for m in (0.3,0.5) for A in (15,25,35)]
def build(data,case):
    m,A=case; a=G*t(A); T=m*G/c(A)
    context=f'<p>A {m} kg sensor hangs from a light cord attached to the ceiling of a cabin moving on a horizontal track. After any swinging has died away, the sensor remains at rest relative to the cabin with the cord tilted {A}° west of vertical: the sensor is west of its ceiling attachment. The cabin has no vertical acceleration. Use the ground frame.</p>'
    parts=[part('direction','What can you conclude about the cabin?','Its acceleration is eastward; its velocity could be eastward or westward.',['Its acceleration and velocity must both be westward.','Its acceleration is westward; its velocity could be eastward or westward.','Its velocity is eastward and its acceleration is zero.'],'Tension on the sensor points toward the ceiling attachment, upward and eastward. Gravity is downward. Thus the resultant is eastward. A deflection reveals acceleration, not the direction of velocity.'),
    part('values','What are the cabin’s acceleration magnitude and the cord tension?',f'{fmt(a)} m/s²; {fmt(T)} N.',[f'{fmt(G/t(A))} m/s²; {fmt(T)} N.',f'{fmt(a)} m/s²; {fmt(m*G)} N.',f'{fmt(G*s(A))} m/s²; {fmt(m*G*c(A))} N.'],f'The angle is measured from vertical. Thus T cos θ=mg and T sin θ=ma. Dividing gives a=g tan θ={fmt(a)} m/s², and T=mg/cos θ={fmt(T)} N. The horizontal net force is an actual component of tension.')]
    deliver(data,context,parts,dict(m=m,A=A))


def generate(data):
    build(data, random.choice(CASES))
