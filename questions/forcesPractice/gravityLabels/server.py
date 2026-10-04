import itertools
import random
from forces_practice import part, deliver

CASES = list(itertools.product(["A", "B"], ["weight", "mass"]))


def build(data, case):
    weak_site, matching = case
    strong_site = "B" if weak_site == "A" else "A"
    packing = (
        "At each outpost, a force meter measures the gravitational weight of its shipment. "
        "The two shipments are packed until these weight readings, in newtons, are equal."
        if matching == "weight" else
        "The two shipments are packed to have equal actual masses in kilograms. "
        "Their gravitational weights at their original outposts are not used to match them."
    )
    context = (
        "<p>Shipment A is packed at outpost A, and shipment B at outpost B. "
        f"Gravity is weaker at outpost {weak_site} than at outpost {strong_site}. {packing}</p>"
        "<p>The sealed shipments are then brought to the same laboratory without gaining or losing any material. "
        "Starting from rest on separate level, frictionless air tracks, they experience identical, constant "
        "horizontal net forces. Their vertical forces balance.</p>"
    )
    choices = {
        "A_first": "A reaches the target speed first because it has less mass.",
        "B_first": "B reaches the target speed first because it has less mass.",
        "same": "They reach the target speed at the same time because their masses are equal.",
        "no_acceleration": "Neither can accelerate because its upward support balances its gravitational weight.",
    }
    correct = "same" if matching == "mass" else strong_site+"_first"
    explanation = (
        "Their actual masses were matched, and transporting sealed shipments does not change those masses. "
        "Equal horizontal net forces therefore produce equal accelerations."
        if matching == "mass" else
        f"Equal original weights do not mean equal masses: weight is mass times local gravitational acceleration. "
        f"The shipment from the weaker-gravity outpost, {weak_site}, needs more mass to have the same weight. "
        f"That mass difference remains after transport, so shipment {strong_site} accelerates more under the same horizontal net force."
    )
    explanation += (
        " Starting from rest, the shipment with greater acceleration reaches a shared target speed sooner. "
        "Balanced vertical forces do not cancel a horizontal net force."
    )
    models = [correct, *[key for key in choices if key != correct]]
    question = part("race", "Which shipment reaches the same chosen nonzero speed first?",
                    choices[correct], [choices[key] for key in models[1:]], explanation)
    for option, model in zip(question["choices"], models):
        option["model"] = model
    deliver(data, context, [question], dict(weak_site=weak_site, matching=matching))


def generate(data):
    build(data, random.choice(CASES))
