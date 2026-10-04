import itertools
import random
from forces_practice import G, fmt, part, deliver

CASES = list(itertools.product([20, 30, 40], [1.4, 2.1], [2, 3]))


def build(data, case):
    mass, acceleration, time = case
    speed = acceleration * time
    context = (
        f"<p>A {mass} kg camera case rides on a force-sensing pad on a vertically moving stage. "
        f"The stage is descending at {fmt(speed)} m/s when its controller begins to stop it. "
        f"It reaches rest after {fmt(time)} s with constant acceleration; the case stays on the pad.</p>"
        "<p>The pad displays its upward contact force divided by 9.8 and labels the result “kg.” "
        "Ignore vibration and air resistance.</p>"
    )
    parts = [
        part("display", "What does the pad display during the stopping interval?",
             f"{fmt(mass*(G+acceleration)/G)} kg",
             [f"{fmt(mass*(G-acceleration)/G)} kg", f"{fmt(mass)} kg", f"{fmt(mass*acceleration/G)} kg"],
             f"The downward velocity decreases in magnitude, so acceleration is upward: a = {fmt(speed)}/{fmt(time)} = "
             f"{fmt(acceleration)} m/s². N − mg = ma, giving N = {fmt(mass*(G+acceleration))} N. "
             f"The display is N/9.8 = {fmt(mass*(G+acceleration)/G)} kg. A larger display does not mean a larger true mass."),
        part("interpretation", "In a separate run, an observer knows the case's true mass and sees a pad reading larger than that mass, but cannot see the motion. What follows from that reading alone, while contact is maintained?",
             "The acceleration is upward; the case could be moving upward, moving downward, or instantaneously at rest.",
             ["Both velocity and acceleration must be upward.",
              "The case must be moving downward because it is being pressed into the pad.",
              "The case has gained mass, so its gravitational weight has increased."],
             "The reading fixes the contact force, and N > mg implies upward acceleration. It does not determine the sign of velocity. "
             "The stopping stage in the first part is one possible example: the case moves down while its acceleration points up."),
    ]
    deliver(data, context, parts, dict(mass=mass, initial_down_speed=speed, time=time))


def generate(data):
    build(data, random.choice(CASES))
