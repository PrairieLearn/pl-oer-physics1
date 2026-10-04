import itertools
import random
from forces_practice import G, fmt, part, deliver

CASES = list(itertools.product([10, 15, 20], [2, 3], [20, 30], [2, 3]))


def build(data, case):
    mass, deceleration, drive, time = case
    brake = drive + mass*deceleration
    speed = deceleration*time
    context = (
        f"<p>A camera dolly is moving right at {fmt(speed)} m/s along a level rail. Its motor continues "
        f"to push right with {fmt(drive)} N while a magnetic brake exerts {fmt(brake)} N left. "
        f"With both forces constant, the dolly first reaches rest after {fmt(time)} s. Other horizontal forces are negligible.</p>"
    )
    parts = [
        part("mass", "What is the dolly's mass?",
             f"{fmt(mass)} kg",
             [f"{fmt(brake*time/speed)} kg", f"{fmt((brake+drive)*time/speed)} kg", f"{fmt((brake-drive)/speed)} kg"],
             f"Right is positive. The measured acceleration is (0 − {fmt(speed)})/{fmt(time)} = −{fmt(deceleration)} m/s². "
             f"The force sum is {fmt(drive)} − {fmt(brake)} = −{fmt(brake-drive)} N. "
             f"Then m = F_net/a = {fmt(mass)} kg. Leaving the motor force out overestimates the mass."),
        part("coasting", "In another run, both the motor and brake switch off while the dolly is still moving right. Under the same negligible-resistance assumption, what happens next?",
             "It continues right at constant velocity; motion by itself does not require a continuing net force.",
             ["It gradually stops because moving objects naturally use up their motion.",
              "It accelerates right because the previous motor force remains stored in it.",
              "It immediately stops because the forces have become equal."],
             "With no horizontal net force, horizontal acceleration is zero, not velocity. "
             "A real dolly slows because of resistance, which this scenario explicitly neglects."),
    ]
    deliver(data, context, parts, dict(drive=drive, brake=brake, initial_speed=speed, stopping_time=time))


def generate(data):
    build(data, random.choice(CASES))
