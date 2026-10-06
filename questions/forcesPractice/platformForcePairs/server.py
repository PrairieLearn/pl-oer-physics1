import itertools
import random
from forces_practice import part, deliver

CASES = list(itertools.product(["freight platform", "inspection stage"], ["upward", "downward"], ["upward", "downward"]))


def build(data, case):
    support, velocity, acceleration = case
    relation = "greater than" if acceleration == "upward" else "less than"
    opposite_relation = "less than" if acceleration == "upward" else "greater than"
    context = (
        f"<p>A sealed case rests on a horizontal {support}. At the instant considered, the case is moving {velocity} "
        f"but accelerating {acceleration}. It stays in contact with the {support}, and air resistance is negligible.</p>"
    )
    parts = [
        part(
            "comparison",
            "Which comparison of the two forces acting on the case is correct?",
            f"The {support}'s upward force on the case is {relation} Earth's downward force on the case, so the net force is {acceleration}.",
            [
                f"The two forces are equal because the case and {support} move together.",
                f"The {support}'s upward force on the case is {opposite_relation} Earth's downward force on the case, because the case is moving {velocity}.",
                "The two forces must be equal and opposite because they form a Newton's-third-law pair.",
            ],
            f"Only two forces act on the case: the {support}'s contact force upward and Earth's gravitational force downward. "
            f"The acceleration is {acceleration}, so the net force must point {acceleration}; therefore the upward support force is {relation} the weight. "
            "The direction of velocity does not determine the direction of net force.",
        ),
        part(
            "partners",
            "Which statement correctly identifies the reaction partner of each force acting on the case?",
            f"The partner of {support} on case is case on {support}; the partner of Earth on case is case on Earth.",
            [
                f"The partner of {support} on case is Earth on case because those forces point in opposite directions.",
                f"The partner of Earth on case is {support} on case because both forces determine the case's acceleration.",
                f"The partner of {support} on case is case on Earth; the partner of Earth on case is case on {support}.",
            ],
            f"A third-law partner comes from the same interaction with the object names reversed. "
            f"The {support}-case interaction gives {support} on case and case on {support}. "
            "The Earth-case interaction gives Earth on case and case on Earth. "
            "The two forces on the case may be unequal and therefore produce acceleration; they are not a third-law pair.",
        ),
    ]
    deliver(data, context, parts, dict(support=support, velocity=velocity, acceleration=acceleration))


def generate(data):
    build(data, random.choice(CASES))
