import math
import random

import numpy as np

def generate(data):

    # define bounds of the variables
    m = random.randint(1, 10)
    theta = random.randint(25, 40)
    k = random.randint(2, 8) * 50
    us = random.randint(5, 7) / 10
    uk = random.randint(35, 40) / 100
    g = 9.8

    # store the variables in the dictionary "params"
    data["params"]["m"] = m
    data["params"]["theta"] = theta
    data["params"]["k"] = k
    data["params"]["us"] = us
    data["params"]["uk"] = uk

    ## Part 1

    # define correct answers
    data["correct_answers"]["part1_ans"] = round(
        (m * g / k)
        * (us * math.cos(math.radians(theta)) + math.sin(math.radians(theta))),
        2,
    )

    ## Part 2

    # define correct answers
    data["correct_answers"]["part2_ans"] = round(
        (m * g / k)
        * (uk * math.cos(math.radians(theta)) + math.sin(math.radians(theta))),
        2,
    )
