import itertools
import random
from forces_practice import G, fmt, part, deliver

CASES = list(itertools.product([6, 8, 10], [2.45, 3.92, 4.9]))


def build(data, case):
    reading, local_g = case
    weight = reading * G
    mass = weight / local_g
    context = (
        f"<p>An outpost has gravitational acceleration {fmt(local_g)} m/s². A spring balance from Earth "
        "has not been recalibrated: it displays the supporting force divided by 9.8 and labels the result “kg.” "
        f"A technician adds material to an otherwise massless container until the balance reads {fmt(reading)} kg. "
        "Everything is stationary, and buoyancy is negligible.</p>"
    )
    parts = [
        part("mass_weight", "What are the material's actual mass and its gravitational weight at the outpost?",
             f"Mass {fmt(mass)} kg; weight {fmt(weight)} N.",
             [f"Mass {fmt(reading)} kg; weight {fmt(reading*local_g)} N.",
              f"Mass {fmt(mass)} kg; weight {fmt(mass*G)} N.",
              f"Mass {fmt(weight)} kg; weight {fmt(weight)} N."],
             f"The display is a force-based calibration, not a direct mass measurement in a different gravitational field. "
             f"The supporting force is {fmt(reading)} × 9.8 = {fmt(weight)} N. At rest that equals the local weight. "
             f"Thus m = W/g = {fmt(weight)}/{fmt(local_g)} = {fmt(mass)} kg. "
             "An equal force-defined weight can therefore correspond to different masses at different locations."),
        part("hover", "A magnetic support now holds the same container motionless a few centimetres above the balance. Treat gravity as unchanged over that small height. Which statement is correct?",
             f"Its weight is still {fmt(weight)} N downward, and its net force is zero.",
             ["Both its gravitational weight and its net force are zero because it is no longer touching the balance.",
              f"Its weight is still {fmt(weight)} N downward, and its net force is {fmt(weight)} N downward.",
              f"Its actual mass has fallen to {fmt(reading)} kg because the balance no longer supports it."],
             "Removing contact with the balance removes that support force, not gravity. The magnetic support replaces the balance's force. "
             "At rest the upward and downward forces balance, so the net force is zero while the weight remains nonzero. "
             "Mass does not change when support or location changes."),
    ]
    deliver(data, context, parts, dict(reading=reading, local_g=local_g))


def generate(data):
    build(data, random.choice(CASES))
