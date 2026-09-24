"""Infer two speeds, then distinguish a ground path from a robot heading."""

import math
import random


# Speeds are sampled in hundredths of m/s so displayed observations are exact.
# These ranges keep westward travel and straight-north travel possible, and
# keep the three direction misconceptions distinct at the displayed precision.
ROBOT_SPEED_HUNDREDTHS = (40, 45, 50, 55, 60)
BELT_SPEED_HUNDREDTHS = (15, 20, 25)


def generate(data):
    robot_hundredths = random.choice(ROBOT_SPEED_HUNDREDTHS)
    belt_hundredths = random.choice(BELT_SPEED_HUNDREDTHS)
    robot_speed = robot_hundredths / 100
    belt_speed = belt_hundredths / 100

    # u + b = eastward speed; u - b = westward speed magnitude.
    east_trial = (robot_hundredths + belt_hundredths) / 100
    west_trial = (robot_hundredths - belt_hundredths) / 100

    # Straight-north ground path: the robot's westward component cancels b.
    compensation_angle = math.degrees(math.asin(belt_speed / robot_speed))
    north_speed = math.sqrt(robot_speed**2 - belt_speed**2)

    # Northward robot heading: the camera sees (b east, u north).
    observed_angle = math.degrees(math.atan2(belt_speed, robot_speed))
    observed_speed = math.hypot(robot_speed, belt_speed)

    data["params"].update(
        east_trial=f"{east_trial:.2f}",
        west_trial=f"{west_trial:.2f}",
        robot_speed=f"{robot_speed:.2f}",
        belt_speed=f"{belt_speed:.2f}",
        # Part 1 distractors: take observed speeds as the unknowns; swap the
        # two inferred speeds; add/subtract observations but forget to halve.
        twice_robot_speed=f"{2 * robot_speed:.2f}",
        twice_belt_speed=f"{2 * belt_speed:.2f}",
        # Part 2 distractors: compensate in the wrong direction; use the
        # uncorrected-path angle and full robot speed; use the complement.
        compensation_angle=f"{compensation_angle:.1f}",
        complement_angle=f"{90 - compensation_angle:.1f}",
        north_speed=f"{north_speed:.2f}",
        # Part 3 distractors: reuse the compensated result; ignore the belt;
        # add perpendicular speed magnitudes as if they were collinear.
        observed_angle=f"{observed_angle:.1f}",
        observed_speed=f"{observed_speed:.2f}",
        scalar_sum=f"{robot_speed + belt_speed:.2f}",
    )
