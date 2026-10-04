import itertools
import random
from forces_practice import G, fmt, part, deliver

CASES = list(itertools.product([3, 5, 7], [1.4, 2.8], [2.8, 4.2, 5.6]))


def build(data, case):
    mass, downward_acceleration, speed = case
    weight = mass*G
    tension = mass*(G-downward_acceleration)
    time = speed/downward_acceleration
    context = (
        f"<p>A specimen basket has a gravitational weight of {fmt(weight)} N. It is moving upward at "
        f"{fmt(speed)} m/s when a hoist changes the upward cable tension to a constant {fmt(tension)} N. "
        "The basket is hanging freely and touches nothing else. Ignore air resistance.</p>"
    )
    parts = [part("stop", "What is the basket's mass, and how long does it take to first reach zero velocity after the tension changes?",
        f"Mass {fmt(mass)} kg; time {fmt(time)} s.",
        [f"Mass {fmt(mass)} kg; time {fmt(speed/(tension/mass))} s.",
         f"Mass {fmt(mass)} kg; time {fmt(speed/G)} s.",
         f"Mass {fmt(weight)} kg; time {fmt(time*G)} s."],
        f"The mass is W/g = {fmt(mass)} kg. Up is positive, so T − W = ma gives a = −{fmt(downward_acceleration)} m/s². "
        f"The basket is moving up but accelerating down. From 0 = {fmt(speed)} − {fmt(downward_acceleration)}t, "
        f"t = {fmt(time)} s. The tension alone is not the net force, and the basket is not in free fall.")]
    deliver(data, context, parts, dict(weight=weight, tension=tension, initial_up_speed=speed))


def generate(data):
    build(data, random.choice(CASES))
