import itertools
import random
from forces_practice import part, deliver

CASES = list(itertools.product(["cord", "chain"], ["tracking tag", "inspection camera"], ["motionless", "accelerating upward"]))


def build(data, case):
    support, device, motion = case
    context = (
        f"<p>A display panel hangs from a vertical {support}. A small {device} is clipped securely underneath the panel. "
        f"The panel and {device} are {motion} together. Ignore air resistance.</p>"
        "<p>For every statement, pay attention to which object exerts the force and which object receives it.</p>"
    )
    balance = (
        f"Because the panel is motionless, the {support}'s upward force equals the sum of the two downward forces on the panel. "
        if motion == "motionless"
        else f"Because the panel accelerates upward, the {support}'s upward force is greater than the sum of the two downward forces on the panel. "
    )
    parts = [
        part(
            "inventory",
            "Which list contains all the forces acting on the display panel itself?",
            f"The {support} pulls the panel upward; Earth pulls the panel downward; the {device} pulls the panel downward.",
            [
                f"The {support} pulls the panel upward; Earth pulls the panel downward. The {device} has no effect because it moves with the panel.",
                f"The {support} pulls the panel upward; Earth pulls the panel downward; Earth pulls the {device} downward.",
                f"The panel pulls the {support} downward; the panel pulls Earth upward; the panel pulls the {device} upward.",
            ],
            f"Choose the panel as the object. It interacts with the {support}, Earth, and the {device}, so exactly three forces act on it. "
            f"Earth's force on the {device} is a force on the device, not on the panel. Forces exerted by the panel belong on other objects' diagrams.",
        ),
        part(
            "partners",
            "Which statement correctly identifies the Newton's-third-law partner of every force on the panel?",
            f"Panel on {support} pairs with {support} on panel; panel on Earth pairs with Earth on panel; panel on {device} pairs with {device} on panel.",
            [
                f"The {support}'s upward force on the panel pairs with Earth's downward force on the panel; the {device}'s force has no partner.",
                f"Earth on panel pairs with Earth on {device}, because both gravitational forces point downward.",
                f"All three forces on the panel are their own partners because their vector sum determines the panel's acceleration.",
            ],
            balance
            + "Those forces can balance, or fail to balance, because they all act on the same object. They are not third-law partners of one another. "
            "For a reaction pair, swap the two object names: A on B pairs with B on A. Each partner therefore acts on a different object.",
        ),
    ]
    deliver(data, context, parts, dict(support=support, device=device, motion=motion))


def generate(data):
    build(data, random.choice(CASES))
