import itertools
import random
from forces_practice import G, fmt, part, deliver

CASES = list(itertools.product([0.2, 0.4], [0.15, 0.25], [0.45, 0.75]))


def build(data, case):
    mass, stroke, height = case
    force = mass*G*(1+height/stroke)
    context = (
        f"<p>A vertical actuator launches a {fmt(mass)} kg inspection capsule from rest. The actuator exerts "
        f"a constant upward force while moving the capsule through a {fmt(stroke)} m stroke. The capsule then "
        f"leaves the actuator and rises another {fmt(height)} m before momentarily stopping. "
        "Air resistance is negligible, and gravity acts throughout.</p>"
    )
    parts = [part("actuator_force", "What constant upward force did the actuator exert during its stroke?",
        f"{fmt(force)} N",
        [f"{fmt(mass*G*height/stroke)} N", f"{fmt(mass*G)} N", f"{fmt(mass*G*(2+height/stroke))} N"],
        f"The free-flight rise gives the release speed squared: v² = 2gH = {fmt(2*G*height)} m²/s². "
        f"The powered stroke began from rest, so v² = 2ad gives a = gH/d = {fmt(G*height/stroke)} m/s². "
        f"During the stroke, F − mg = ma, hence F = m(g + a) = {fmt(force)} N. "
        "Using ma alone omits gravity; using the total rise as the free-flight rise counts the stroke twice.")]
    deliver(data, context, parts, dict(mass=mass, stroke=stroke, free_height=height))


def generate(data):
    build(data, random.choice(CASES))
