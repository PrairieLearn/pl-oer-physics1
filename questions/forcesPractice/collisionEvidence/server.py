import itertools
import random
from forces_practice import part, deliver

CASES = list(itertools.product(["A", "B"], ["A", "B"]))


def build(data, case):
    heavier, moving = case
    lighter = "B" if heavier == "A" else "A"
    stationary = "B" if moving == "A" else "A"
    context = (
        f"<p>Two equipment cases, A and B, can slide freely along a level, frictionless track. "
        f"Case {heavier} has much more mass than case {lighter}. "
        f"Initially, {moving} is moving and {stationary} is at rest. They collide head-on. "
        "During the collision, their horizontal contact forces on one another are nonzero; "
        "there are no other horizontal forces.</p>"
    )
    choices = {
        "pair_and_mass": f"The contact forces are equal in magnitude and opposite in direction; case {lighter} has the greater acceleration magnitude.",
        "stronger_heavy": f"Case {heavier} exerts a stronger contact force than case {lighter}, because it has more mass.",
        "equal_acceleration": "The contact forces are equal in magnitude, so the cases also have equal acceleration magnitudes.",
        "one_way": f"Only case {moving} exerts a contact force, because case {stationary} was initially at rest.",
    }
    correct = "pair_and_mass"
    models = list(choices)
    question = part("interaction", "At the same instant during contact, which statement is correct?",
                    choices[correct], [choices[key] for key in models[1:]],
                    "Newton's third law gives equal and opposite forces for this one interaction, regardless of which case "
                    "was moving first. These forces act on different cases, so they do not cancel in either case's force sum. "
                    f"With equal force magnitudes, acceleration is larger for the smaller mass, case {lighter}. "
                    "A larger acceleration does not mean that the case experiences a larger contact force.")
    for option, model in zip(question["choices"], models):
        option["model"] = model
    deliver(data, context, [question], dict(heavier=heavier, moving=moving))


def generate(data):
    build(data, random.choice(CASES))
