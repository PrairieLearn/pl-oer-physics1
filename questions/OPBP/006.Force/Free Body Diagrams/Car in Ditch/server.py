import random

import numpy as np


def generate(data):


    # define bounds of the variables
    F = 100 * (
        10 * random.randint(2, 8) + 5 * random.randint(0, 1)
    )  # So that the force is a multiple of 500, from 2000-8500 N

    # store the variables in the dictionary "params"
    data["params"]["F"] = F

    # define correct answers
    data["correct_answers"]["part1_ans"] = F / (2 * np.sin(np.deg2rad(5)))