import itertools
import random
from forces_practice import G, fmt, part, deliver

CASES = list(itertools.product([0.2, 0.3, 0.5], [4, 6, 8], [0.4, 0.6]))


def build(data, case):
    mass, acceleration, time = case
    force = mass*(G+acceleration)
    release = acceleration*time
    height = release**2/(2*G)
    context = (
        f"<p>A vertical launch fixture pushes a {fmt(mass)} kg sensor upward with a constant contact force "
        f"of {fmt(force)} N for {fmt(time)} s. The sensor starts from rest. At the end of that interval it leaves "
        "the fixture, which no longer touches it. Ignore air resistance.</p>"
    )
    parts = [
        part("rise", "How much farther does the sensor rise after it leaves the fixture, measured from its release point?",
             f"{fmt(height)} m",
             [f"{fmt((force/mass*time)**2/(2*G))} m",
              f"{fmt(0.5*acceleration*time**2+height)} m",
              f"{fmt(release**2/G)} m"],
             f"During contact, a = F/m − g = {fmt(acceleration)} m/s². Its release speed is at = {fmt(release)} m/s. "
             f"After release, gravity alone slows it: 0 = v² − 2gh, so h = {fmt(release)}²/(2 × 9.8) = {fmt(height)} m. "
             "The displacement while the fixture still touches it is not part of the requested height."),
        part("apex", "At the highest point after release, which statement describes the sensor?",
             f"Its velocity is zero, its acceleration is 9.80 m/s² downward, and its only force is gravity, {fmt(mass*G)} N downward.",
             ["Its velocity, acceleration, and net force are all zero.",
              "Its velocity is zero, but the fixture's upward force still acts and balances gravity.",
              "Its velocity is zero and it experiences an upward motion force that is just about to run out."],
             "The fixture stopped exerting force at release. Gravity acts during both the upward and downward parts of the free flight, "
             "including the instant when velocity is zero at the top."),
    ]
    deliver(data, context, parts, dict(mass=mass, force=force, contact_time=time))


def generate(data):
    build(data, random.choice(CASES))
