import itertools
import random
from forces_practice import G, fmt, part, deliver

CASES = list(itertools.product([1.5, 2.0, 3.0], [3.0, 5.0, 7.0], ["upward", "downward"], [1.0, 2.0]))


def build(data, case):
    mass, buoyant, direction, magnitude = case
    acceleration = magnitude if direction == "upward" else -magnitude
    reading = mass * (G + acceleration) - buoyant
    equilibrium = mass * G - buoyant
    opposite_sign = mass * (G - acceleration) - buoyant
    buoyancy_down = mass * (G + acceleration) + buoyant
    context = (
        f"<p>A {fmt(mass)} kg metal artifact hangs from a spring scale and is fully submerged in water without "
        f"touching the container. The container and scale are fixed inside an elevator accelerating "
        f"{fmt(magnitude)} m/s² {direction}. The water exerts a buoyant force of {fmt(buoyant)} N upward, "
        "and the artifact remains at rest relative to the elevator.</p>"
    )
    parts = [
        part(
            "equation",
            "Taking upward as positive, which force equation and spring-scale reading are correct?",
            f"R_s + F_b − mg = ma; R_s = {fmt(reading)} N.",
            [
                f"R_s + F_b − mg = 0; R_s = {fmt(equilibrium)} N.",
                f"R_s + F_b − mg = −ma; R_s = {fmt(opposite_sign)} N.",
                f"R_s − F_b − mg = ma; R_s = {fmt(buoyancy_down)} N.",
            ],
            f"Three forces act on the artifact: scale tension R_s upward, buoyancy F_b upward, and weight mg downward. "
            f"With upward positive, its signed acceleration is {fmt(acceleration)} m/s², so "
            f"R_s + {fmt(buoyant)} − {fmt(mass * G)} = {fmt(mass)}({fmt(acceleration)}). "
            f"Solving gives R_s = {fmt(reading)} N. The object is not in equilibrium merely because it stays at one "
            "location inside the accelerating elevator.",
        )
    ]
    deliver(
        data,
        context,
        parts,
        dict(mass=mass, buoyant_force=buoyant, direction=direction, acceleration=magnitude),
    )


def generate(data):
    build(data, random.choice(CASES))
