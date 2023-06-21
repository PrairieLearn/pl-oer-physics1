import math
import random as rd

def generate(data):

    # define bounds of the variables
    v1 = rd.randint(1, 3)
    v2 = rd.randint(1, 3)

    # generate different values
    while v2 == v1:
        v2 = rd.randint(1, 3)

    # store the variables in the dictionary "params"
    data["params"]["v1"] = v1
    data["params"]["v2"] = v2

    # find the angle using conservation of momentum and solving for theta by division
    # atan(p_y/p_x)
    # After cancelling, py = v1 and px = 2*(v2)
    angle = math.degrees(math.atan((2 * v2) / v1))

    # calculate magnitude by sustituting in one of the momentum equations
    # mv1 = (3m)(vf)cos(theta_f)
    # => v1 = (3)(vf)cos(theta_f)

    mag = v1 / (3 * math.cos(math.radians(angle)))

    ## Part 1

    # define correct answers
    data["correct_answers"]["part1_ans"] = mag

    ## Part 2

    # define correct answers
    data["correct_answers"]["part2_ans"] = angle

