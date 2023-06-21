import math
import random as rd

def generate(data):

    # define bounds of the variables
    theta = round(rd.uniform(10.00, 90.0), 1)

    # store the variables in the dictionary "params"
    data["params"]["theta"] = theta

    # calculate cos(theta)
    # E = mgl(1-cos(theta)). We only need to calculate (1-cos(theta))
    E = 1 - math.cos(math.radians(theta))

    # define correct answer
    # only store the absolute value
    ans1 = math.acos(1 - E / 2)
    data["correct_answers"]["part1_ans"] = math.degrees(ans1)