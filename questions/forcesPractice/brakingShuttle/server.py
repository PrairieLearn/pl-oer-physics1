import itertools
import random
from forces_practice import G, fmt, part, deliver

CASES = list(itertools.product([4, 6], [1, 1.5], [1, 2]))


def build(data, case):
    speed, deceleration, time = case
    ahead = 0.5 * deceleration * time**2
    context = (
        f"<p>A lab shuttle and a loose sample puck are moving east at {fmt(speed)} m/s. "
        f"The puck rests on the shuttle's level, frictionless deck. The shuttle brakes "
        f"with a constant westward acceleration of {fmt(deceleration)} m/s² for {fmt(time)} s. "
        "The puck never touches a wall, and air resistance is negligible.</p>"
        "<p>A camera is fixed to the laboratory floor. A second camera rides on the shuttle.</p>"
    )
    parts = [
        part("motion", "At the end of the braking interval, what do the cameras show?",
             f"Floor camera: {fmt(speed)} m/s east; shuttle camera: puck {fmt(ahead)} m ahead of its starting mark.",
             [f"Floor camera: {fmt(speed-deceleration*time)} m/s east; shuttle camera: puck stays over its starting mark.",
              f"Floor camera: {fmt(speed)} m/s east; shuttle camera: puck {fmt(ahead)} m behind its starting mark.",
              f"Floor camera: {fmt(speed)} m/s east; shuttle camera: puck {fmt(deceleration*time**2)} m ahead of its starting mark."],
             f"No horizontal force acts on the puck, so its floor-frame velocity stays {fmt(speed)} m/s east. "
             f"The shuttle covers less distance by one-half times its braking acceleration times time squared: "
             f"0.5 × {fmt(deceleration)} × {fmt(time)}² = {fmt(ahead)} m. Motion relative to an accelerating shuttle "
             "does not establish a new horizontal interaction force on the puck."),
        part("forces", "Which description correctly identifies the forces on the puck during braking and the reaction to the deck's upward force?",
             "Only gravity downward and the deck's normal force upward act on the puck; the reaction to the normal force is the puck pushing down on the deck.",
             ["Gravity downward, the normal force upward, and a forward inertia force act on the puck; gravity is the reaction to the normal force.",
              "Only gravity downward and the normal force upward act on the puck; these two forces are a Newton's-third-law pair.",
              "Gravity downward, the normal force upward, and the shuttle's backward braking force act on the puck; the reaction is the deck pushing up again."],
             "The deck is frictionless, so it cannot transmit the shuttle's horizontal braking force to the puck. "
             "Gravity and the normal force balance on the puck, but are not a third-law pair. The normal-force pair acts on puck and deck; "
             "the gravitational pair acts on puck and Earth."),
    ]
    deliver(data, context, parts, dict(speed=speed, deceleration=deceleration, time=time))


def generate(data):
    build(data, random.choice(CASES))
