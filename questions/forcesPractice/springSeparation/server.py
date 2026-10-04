import itertools
import random
from forces_practice import G, fmt, part, deliver

CASES = list(itertools.product([2, 3, 4], [2, 3], [6, 9, 12]))


def build(data, case):
    light, ratio, force = case
    heavy = light*ratio
    context = (
        f"<p>Two small service robots of masses {light} kg and {heavy} kg are initially at rest on a level, "
        "frictionless track. A compressed spring of negligible mass lies between them. "
        f"At one instant after release, the spring pushes the lighter robot left with {force} N. "
        "The track provides no horizontal force.</p>"
    )
    parts = [
        part("accelerations", "At that instant, what are the accelerations of the lighter and heavier robots, respectively?",
             f"{fmt(force/light)} m/s² left; {fmt(force/heavy)} m/s² right.",
             [f"{fmt(force/light)} m/s² left; {fmt(force/light)} m/s² right.",
              f"{fmt(force/heavy)} m/s² left; {fmt(force/light)} m/s² right.",
              "Both accelerations are zero because the spring's forces cancel."],
             f"A spring with negligible mass transmits equal force magnitudes to the two robots. "
             f"Each robot obeys its own F = ma, so the accelerations are {force}/{light} and {force}/{heavy}. "
             "Equal forces do not imply equal accelerations when masses differ."),
        part("system", "For a system containing both robots and the spring, which statement is correct?",
             "The total external horizontal force is zero, even though the individual robots accelerate in opposite directions.",
             [f"The total external horizontal force is {2*force} N because both spring forces must be added.",
              "The heavier robot produces a stronger spring force, so the complete system accelerates toward the lighter robot.",
              "Internal forces cannot change the motion of any part of a system, so the robots must remain at rest."],
             "Both spring forces are internal when both robots and the spring are included in the system. "
             "They cancel in the whole-system force sum, while each robot still has its own nonzero net force. "
             "This is why a system can have zero net external force while its parts move relative to one another."),
    ]
    deliver(data, context, parts, dict(light_mass=light, heavy_mass=heavy, force=force))


def generate(data):
    build(data, random.choice(CASES))
