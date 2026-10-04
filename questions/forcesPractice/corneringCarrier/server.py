import random
from forces_practice import G, fmt, part, deliver

CASES = [("east", "north", "west"), ("north", "west", "south"), ("west", "south", "east")]


def build(data, case):
    original, turn, opposite = case
    context = (
        f"<p>An automated carrier travels {original} with a loose vial on a level, frictionless tray. "
        f"The carrier begins a smooth turn toward {turn}. During the short interval under consideration, "
        "the vial has not touched the tray's rim. Air resistance is negligible. A camera is fixed to the building.</p>"
    )
    parts = [
        part("trajectory", "Which explanation correctly predicts what the building camera sees during that interval?",
             f"The vial continues along its original straight path toward {original}; the tray turns underneath it because no horizontal force turns the vial.",
             [f"The vial follows the tray toward {turn} because a constant speed means no acceleration is needed.",
              f"The vial accelerates toward {opposite} because inertia is a force opposite its original motion.",
              "The vial stops as soon as the carrier changes direction because its original driving force is gone."],
             "Newton's first law preserves the full velocity vector when the horizontal net force is zero. "
             "Changing direction, even without changing speed, requires acceleration and thus a horizontal net force. "
             "Relative to the carrier the vial drifts, but that is not evidence of an outward interaction force."),
        part("reaction", "The tray pushes upward on the vial. Which statement correctly identifies that force's third-law partner?",
             "The vial pushes downward on the tray; the vial's gravitational pull on Earth is the partner of its weight.",
             ["Earth pulls downward on the vial; this is the third-law partner of the tray's upward force.",
              "The vial pushes down on the tray only if the vial is accelerating vertically.",
              "The vial pulls up on Earth, but Earth exerts no force back because it is much heavier."],
             "Each interaction pair connects the same two objects in opposite order. Tray-on-vial pairs with vial-on-tray. "
             "Earth-on-vial pairs with vial-on-Earth. The two forces on the vial can balance without being a third-law pair. "
             "Equal gravitational forces produce very different accelerations because Earth has much more mass."),
    ]
    deliver(data, context, parts, dict(original=original, turn=turn, opposite=opposite))


def generate(data):
    build(data, random.choice(CASES))
