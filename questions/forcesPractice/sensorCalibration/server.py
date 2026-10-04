import itertools
import random
from forces_practice import G, fmt, part, deliver

CASES = list(itertools.product([10, 15, 20], [0.7, 0.8], [2, 3]))


def build(data, case):
    mass, ratio, time = case
    reading = mass*ratio
    speed = G*(1-ratio)*time
    context = (
        "<p>A payload rests on a force-sensing pad fixed to a vertical test carriage. "
        "The pad displays its upward contact force divided by 9.8 and labels it “kg.” "
        f"At rest, it reads {fmt(mass)} kg. The carriage then accelerates from rest, and "
        f"the display remains at {fmt(reading)} kg for {fmt(time)} s. The payload remains on the pad; "
        "its contents do not change. Ignore air resistance.</p>"
    )
    parts = [part("velocity_mass", "At the end of this interval, what are the payload's velocity relative to the building and its actual mass?",
        f"{fmt(speed)} m/s downward; actual mass {fmt(mass)} kg.",
        [f"{fmt(speed)} m/s upward; actual mass {fmt(mass)} kg.",
         f"{fmt((mass-reading)*time)} m/s downward; actual mass {fmt(mass)} kg.",
         f"{fmt(speed)} m/s downward; actual mass {fmt(reading)} kg."],
        f"The at-rest reading gives the real mass {fmt(mass)} kg. During motion, N = {fmt(reading)} × 9.8 = "
        f"{fmt(reading*G)} N, while mg stays {fmt(mass*G)} N. Thus a = (N − mg)/m = −{fmt(G*(1-ratio))} m/s². "
        f"Starting from rest gives v = at = −{fmt(speed)} m/s. The lower display reflects less support, not lost mass.")]
    deliver(data, context, parts, dict(rest_reading=mass, moving_reading=reading, time=time))


def generate(data):
    build(data, random.choice(CASES))
