import itertools
import random
from forces_practice import G, fmt, part, deliver

CASES = list(itertools.product([6, 8], [2, 3], [1.2, 1.8]))


def build(data, case):
    lower, upper, acceleration = case
    v1, time = 1.0, 2.0
    v2 = v1 + acceleration*time
    weight = lower*G
    contact = upper*(G-acceleration)
    support = (lower+upper)*(G-acceleration)
    def triple(a, b, c):
        return f"Stage on lower case: {fmt(a)} N upward; Earth on lower case: {fmt(b)} N downward; upper case on lower case: {fmt(c)} N downward."
    context = (
        f"<p>A {upper} kg optical unit rests on a {lower} kg equipment case, which rests on a level stage. "
        f"The stage descends, increasing its downward speed from {fmt(v1)} to {fmt(v2)} m/s in {fmt(time)} s. "
        "Its acceleration is constant; neither object separates from its support. Ignore air resistance.</p>"
    )
    parts = [part("force_inventory", "Which list gives all three vertical forces acting on the lower case during this interval?",
        triple(support, weight, contact),
        [triple((lower+upper)*G, weight, upper*G),
         triple(lower*(G-acceleration), weight, contact),
         triple(support, weight, upper*G)],
        f"The acceleration is {fmt(acceleration)} m/s² downward. The upper unit requires an upward support "
        f"m(g − a) = {fmt(contact)} N and pushes down equally on the lower case. "
        f"The stage supports and accelerates both masses, so its force is (M + m)(g − a) = {fmt(support)} N. "
        f"The lower case's own weight is {fmt(weight)} N. Check the lower case alone: "
        f"{fmt(support)} − {fmt(weight)} − {fmt(contact)} = −{fmt(lower*acceleration)} N.")]
    deliver(data, context, parts, dict(lower_mass=lower, upper_mass=upper, v1=v1, v2=v2, time=time))


def generate(data):
    build(data, random.choice(CASES))
