import itertools
import random
from forces_practice import G, fmt, part, deliver

CASES = list(itertools.product([12, 18], [24, 36, 48]))


def build(data, case):
    mass, force = case
    context = (
        f"<p>A {mass} kg delivery robot starts on a level floor. Its driven wheels grip without slipping "
        f"and push the floor west with a total horizontal force of {force} N. Ignore all other horizontal resistance.</p>"
    )
    parts = [
        part("traction", "Which external force accelerates the complete robot, and what is its acceleration?",
             f"The floor pushes the wheels east; acceleration {fmt(force/mass)} m/s² east.",
             [f"The motor exerts an external force on the complete robot eastward; acceleration {fmt(force/mass)} m/s² east.",
              f"The floor pushes the wheels west; acceleration {fmt(force/mass)} m/s² west.",
              "The wheel–floor action and reaction cancel on the robot; acceleration is zero."],
             f"The wheels push west on the floor, and the floor pushes east on the wheels. These forces act on different objects. "
             f"For the whole robot, the external horizontal force is {force} N from the floor, giving a = {force}/{mass} = {fmt(force/mass)} m/s². "
             "The motor supplies energy but the floor supplies the external traction force."),
        part("internal_pull", "Later, the robot stops and switches off its wheel motors. An onboard winch pulls upward on a handle rigidly attached to the same chassis. Nothing is expelled, and the winch is not attached to the ceiling. Could this lift the entire robot off the floor?",
             "No. The winch and handle forces are internal to the complete robot and cannot provide a net upward force on it.",
             ["Yes, if the winch force exceeds the robot's weight, even though both ends are attached to the robot.",
              "Yes, because the upward force acts before its downward reaction.",
              "No, because the floor can never push harder than the robot's weight, even during a powered jump."],
             "Pulling one part of a rigid robot with another creates internal forces. A jump instead requires an increased external upward push "
             "from the floor while the robot's legs or mechanism push downward on it. Equal and opposite forces act on different objects; "
             "Earth's acceleration is tiny because its mass is enormous."),
    ]
    deliver(data, context, parts, dict(mass=mass, force=force))


def generate(data):
    build(data, random.choice(CASES))
