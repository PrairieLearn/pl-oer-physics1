import itertools
import random
from forces_practice import part, deliver

CASES = list(itertools.product(["right", "left"], ["A", "B"], ["steady", "speeding", "slowing"]))


def build(data, case):
    direction, heavier, motion = case
    opposite = "left" if direction == "right" else "right"
    observation = {
        "steady": "Each pod maintains its own constant speed.",
        "speeding": "Both speeds are increasing at the same rate.",
        "slowing": "Both speeds are decreasing at the same rate; neither pod has stopped.",
    }[motion]
    equal_direction = opposite if motion == "slowing" else direction
    context = (
        "<p>Two sensor pods, A and B, travel along separate straight, level tracks. "
        f"Both are moving {direction}, and A is moving faster than B. Pod {heavier} has the greater mass. "
        f"During the interval being observed, {observation[0].lower()+observation[1:]}</p>"
    )
    choices = {
        "zero": "Both pods have zero horizontal net force.",
        "equal": f"The pods have equal, nonzero horizontal net forces, both toward the {equal_direction}.",
        "heavier_along": f"Pod {heavier} has the larger horizontal net-force magnitude; both net forces point {direction}.",
        "heavier_opposite": f"Pod {heavier} has the larger horizontal net-force magnitude; both net forces point {opposite}.",
    }
    correct = {"steady": "zero", "speeding": "heavier_along", "slowing": "heavier_opposite"}[motion]
    explanation = (
        "Both velocities are constant, so both horizontal accelerations and net forces are zero. "
        "A faster speed or a greater mass does not by itself imply a nonzero net force."
        if motion == "steady" else
        f"Both pods have the same acceleration, toward the {equal_direction}. "
        f"For the same nonzero acceleration, the greater mass of pod {heavier} requires a greater net force. "
        "Their different speeds do not determine their net forces."
    )
    models = [correct, *[key for key in choices if key != correct]]
    question = part("comparison", "Which conclusion about the horizontal net forces is justified by these observations?",
                    choices[correct], [choices[key] for key in models[1:]], explanation)
    for option, model in zip(question["choices"], models):
        option["model"] = model
    deliver(data, context, [question], dict(direction=direction, heavier=heavier, motion=motion))


def generate(data):
    build(data, random.choice(CASES))
