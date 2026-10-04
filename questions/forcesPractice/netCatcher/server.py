import itertools
import random
from forces_practice import G, fmt, part, deliver

CASES = list(itertools.product([200, 350, 500], [3, 4], [0.2, 0.4]))


def build(data, case):
    grams, speed, distance = case
    mass = grams/1000
    acceleration = speed**2/(2*distance)
    force = mass*(G+acceleration)
    weak = 0.5*mass*G
    context = (
        f"<p>A {grams} g sample container enters a catching net at {fmt(speed)} m/s downward. "
        f"The net stretches downward by {fmt(distance)} m while bringing the container to rest. "
        "During this stretch the net exerts a constant upward force. Ignore air resistance.</p>"
    )
    parts = [
        part("net_force", "What is the magnitude of the upward force exerted by the net?",
             f"{fmt(force)} N",
             [f"{fmt(mass*acceleration)} N", f"{fmt(mass*(G+speed**2/distance))} N", f"{fmt(mass*G)} N"],
             f"Take up as positive. Then v_i = −{fmt(speed)} m/s and Δy = −{fmt(distance)} m. "
             f"From 0 = v_i² + 2aΔy, a = {fmt(acceleration)} m/s² upward. "
             f"The mass is {fmt(mass)} kg, and F_netting − mg = ma, so the net's force is {fmt(force)} N. "
             "The applied contact force is greater than the net force because it must also oppose gravity."),
        part("weak_catch", f"In a separate catch, the container is moving downward while the net initially provides only {fmt(weak)} N upward. What happens during that interval?",
             "Its acceleration is downward and its downward speed increases.",
             ["Its acceleration is upward and its downward speed decreases because any upward force slows a falling object.",
              "Its acceleration is zero because the net has made contact.",
              "It immediately reverses and moves upward."],
             f"The upward contact force is less than the weight {fmt(mass*G)} N. The resultant force is still downward. "
             "A force pointing upward need not produce an upward acceleration; all forces on the container must be combined."),
    ]
    deliver(data, context, parts, dict(mass_grams=grams, entry_speed=speed, stopping_distance=distance, weak_force=weak))


def generate(data):
    build(data, random.choice(CASES))
