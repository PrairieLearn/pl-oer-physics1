import itertools
import random
from forces_practice import G, fmt, part, deliver

CASES = list(itertools.product([0.5, 0.8, 1.2], ["upward", "downward"], [1.5, 2.5]))


def build(data, case):
    mass, direction, magnitude = case
    acceleration = magnitude if direction == "upward" else -magnitude
    buoyant = mass * (G + acceleration)
    weight = mass * G
    reversed_value = mass * (G - acceleration)
    context = (
        f"<p>A {fmt(mass)} kg sealed wooden sample floats in a tank of water inside an elevator. "
        f"The elevator has acceleration {fmt(magnitude)} m/s² {direction}. After initial sloshing has ended, "
        "the water and sample remain at rest relative to the tank. The sample touches neither the tank nor any cable.</p>"
    )
    parts = [
        part(
            "forces",
            "Which force description is correct for the sample?",
            f"Water pushes upward with {fmt(buoyant)} N; Earth pulls downward with {fmt(weight)} N.",
            [
                f"Water pushes upward with {fmt(weight)} N; Earth pulls downward with {fmt(weight)} N.",
                f"Water pushes upward with {fmt(reversed_value)} N; Earth pulls downward with {fmt(weight)} N.",
                f"Water pushes downward with {fmt(buoyant)} N; Earth pulls downward with {fmt(weight)} N.",
            ],
            f"Take upward as positive. The only forces on the sample are buoyancy upward and weight downward. "
            f"Because it shares the elevator's acceleration, F_b − mg = ma. Thus F_b = m(g + a) = "
            f"{fmt(mass)}(9.80 + ({fmt(acceleration)})) = {fmt(buoyant)} N. Its weight remains {fmt(weight)} N.",
        ),
        part(
            "submersion",
            "Compared with floating in the same water when the elevator is not accelerating, how much of the sample is submerged?",
            "The same fraction is submerged.",
            [
                "A larger fraction is submerged, regardless of the acceleration direction.",
                "A smaller fraction is submerged, regardless of the acceleration direction.",
                "It cannot float while the elevator accelerates because buoyancy exists only when acceleration is zero.",
            ],
            "Elevator acceleration changes the effective downward field that creates the water's pressure gradient. "
            "The buoyant force per unit displaced volume and the force required to accelerate the floating sample change "
            "by the same factor. Therefore the displaced-water volume, and hence the submerged fraction, is unchanged. "
            "This assumes ordinary nonzero effective gravity and that the water has settled relative to the tank.",
        ),
    ]
    deliver(data, context, parts, dict(mass=mass, direction=direction, acceleration=magnitude))


def generate(data):
    build(data, random.choice(CASES))
