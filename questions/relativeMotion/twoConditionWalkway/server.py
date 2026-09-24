import random, math

def generate(data):
    length = random.choice([60, 72, 84])
    stand_time = random.choice([60, 72, 90])
    walk_time = random.choice([20, 24, 30])

    walkway_speed = length / stand_time
    walking_speed = length / walk_time - walkway_speed
    path_angle = math.degrees(math.atan2(walking_speed, walkway_speed))
    direct_angle = math.degrees(math.asin(walkway_speed / walking_speed))

    data["params"].update(
        length=length,
        stand_time=stand_time,
        walk_time=walk_time,
        path_angle=f"{path_angle:.1f}",
        direct_angle=f"{direct_angle:.1f}",
        wrong_path=f"{math.degrees(math.atan2(walkway_speed, walking_speed)):.1f}",
        wrong_direct=f"{90-direct_angle:.1f}",
    )
