import itertools
import random
from forces_practice import part, deliver

CASES = list(itertools.product(["right", "left"], ["along", "against"]))


def build(data, case):
    direction, remaining = case
    opposite = "left" if direction == "right" else "right"
    remaining_direction = direction if remaining == "along" else opposite
    switched_off = opposite if remaining == "along" else direction
    context = (
        f"<p>A magnetic puck is moving {direction} along a level, frictionless air track. "
        "Two magnetic devices pull on it with equal horizontal force magnitudes: one pulls left and the other right.</p>"
        f"<p>The device pulling {switched_off} is switched off. The other device keeps exerting the same constant force "
        "throughout the period considered, even if the puck stops or changes direction. "
        "No other horizontal forces act, and there is enough clear track for the motion described below.</p>"
    )
    choices = {
        "constant": f"It continues {direction} at its original constant speed.",
        "speed_up": f"It continues moving {direction} and gains speed.",
        "reverse": f"It initially slows while moving {direction}, stops momentarily, then moves {opposite} and gains speed.",
        "stay_stopped": f"It slows while moving {direction}, then stops and remains at rest.",
    }
    correct = "speed_up" if remaining == "along" else "reverse"
    explanation = (
        f"After the switch, the remaining net force and acceleration point {remaining_direction}. "
        + (
            "This is the same direction as the initial velocity, so the puck keeps moving that way and speeds up."
            if remaining == "along" else
            "At first this is opposite the velocity, so the puck slows. At zero velocity the force does not disappear: "
            "the acceleration continues in the same direction, so the puck reverses and then speeds up."
        )
        + " The force determines the change in velocity, not the direction of velocity at every instant."
    )
    models = [correct, *[key for key in choices if key != correct]]
    question = part("sequence", "Which description gives the puck's subsequent motion?",
                    choices[correct], [choices[key] for key in models[1:]], explanation)
    for option, model in zip(question["choices"], models):
        option["model"] = model
    deliver(data, context, [question], dict(direction=direction, switched_off=switched_off))


def generate(data):
    build(data, random.choice(CASES))
