import itertools
import random
from forces_practice import G, fmt, part, deliver

CASES = list(itertools.product([5, 8, 10], [0.4, 0.6], [2, 3]))


def build(data, case):
    mass, fraction, acceleration = case
    weight = mass * G
    first = fraction * weight
    second = mass * (G + acceleration)
    context = (
        f"<p>A sealed instrument has a measured weight of {fmt(weight)} N on Earth. It rests on a horizontal workbench. "
        "A vertical cable pulls upward on it. In the first trial the cable force is "
        f"{fmt(first)} N. In a separate trial, starting from rest on the bench, the cable force is {fmt(second)} N. "
        "The bench is rigid and there are no other forces besides gravity, the cable, and contact with the bench.</p>"
    )
    parts = [
        part("first_trial", "What happens in the first trial?",
             f"It remains on the bench with zero acceleration; the bench pushes upward with {fmt(weight-first)} N.",
             [f"It remains on the bench with zero acceleration; the bench pushes upward with {fmt(weight)} N.",
              f"It accelerates downward at {fmt((weight-first)/mass)} m/s² through the bench.",
              f"It lifts off and accelerates upward at {fmt(first/mass)} m/s²."],
             f"At rest the cable and bench share the support: N + T − W = 0. Hence N = {fmt(weight)} − {fmt(first)} = "
             f"{fmt(weight-first)} N. A support can change its normal force; it is not automatically equal to mg."),
        part("second_trial", "What happens in the second trial just after motion begins?",
             f"It lifts off; acceleration {fmt(acceleration)} m/s² upward and bench contact force 0 N.",
             [f"It stays on the bench; the bench pulls downward with {fmt(second-weight)} N.",
              f"It lifts off; acceleration {fmt(second/mass)} m/s² upward and bench contact force 0 N.",
              f"It lifts off; acceleration {fmt(acceleration)} m/s² upward and bench contact force {fmt(weight)} N."],
             f"The mass is W/g = {fmt(weight)}/9.8 = {fmt(mass)} kg. The second pull exceeds weight. "
             "The bench cannot pull the instrument downward, so contact is lost and N = 0. "
             f"Then a = (T − W)/m = ({fmt(second)} − {fmt(weight)})/{fmt(mass)} = {fmt(acceleration)} m/s² upward."),
    ]
    deliver(data, context, parts, dict(weight=weight, first=first, second=second))


def generate(data):
    build(data, random.choice(CASES))
