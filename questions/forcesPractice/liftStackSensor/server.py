import itertools
import random
from forces_practice import G, fmt, part, deliver

CASES = list(itertools.product([6, 8], [2, 3], [-1.4, 1.4, 2.8]))


def build(data, case):
    lower, upper, acceleration = case
    between = upper*(G+acceleration)
    beneath = (lower+upper)*(G+acceleration)
    direction = "upward" if acceleration > 0 else "downward"
    opposite = "downward" if acceleration > 0 else "upward"
    ignored_upper = beneath/lower-G
    ignored_upper_mass = between/(G+ignored_upper)
    wrong_dir = "upward" if ignored_upper > 0 else "downward"
    context = (
        f"<p>Two equipment modules are stacked on a level platform in a vertical test rig. The lower module "
        f"has mass {lower} kg; the upper module's mass is unknown. During one interval, a thin sensor between "
        f"the modules reads a contact-force magnitude of {fmt(between)} N. A sensor between the platform "
        f"and the lower module reads {fmt(beneath)} N.</p>"
        "<p>Both modules stay at rest relative to the platform, so they share its vertical acceleration. "
        "The sensors have negligible mass. No other contact or cable forces act on the modules.</p>"
    )
    parts = [part("hidden_mass", "What are the upper module's mass and the platform's acceleration?",
        f"Upper mass {fmt(upper)} kg; acceleration {fmt(abs(acceleration))} m/s² {direction}.",
        [f"Upper mass {fmt(between/G)} kg; acceleration {fmt(abs(acceleration))} m/s² {direction}.",
         f"Upper mass {fmt(upper)} kg; acceleration {fmt(abs(acceleration))} m/s² {opposite}.",
         f"Upper mass {fmt(ignored_upper_mass)} kg; acceleration {fmt(abs(ignored_upper))} m/s² {wrong_dir}."],
        f"For the lower module, upward minus downward forces give {fmt(beneath)} − {fmt(between)} − "
        f"{fmt(lower*G)} = {lower}a. Thus a = {fmt(acceleration)} m/s² (up is positive). "
        f"For the upper module, {fmt(between)} − mg = ma, so m = {fmt(between)}/(9.8 + ({fmt(acceleration)})) "
        f"= {fmt(upper)} kg. The upper module's push on the lower module is a real force that must be included; "
        "omitting it gives both an incorrect acceleration and an incorrect inferred mass.")]
    deliver(data, context, parts, dict(lower_mass=lower, between_force=between, beneath_force=beneath))


def generate(data):
    build(data, random.choice(CASES))
