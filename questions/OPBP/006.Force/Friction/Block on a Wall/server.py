import math
import random

def generate(data):

    # define bounds of the variables
    theta = random.randint(20, 70)
    m = random.randint(1, 10)
    mu = random.randint(200, 500) / 1000
    g = 9.81

    # store the variables in the dictionary "params"
    data["params"]["theta"] = theta
    data["params"]["m"] = m
    data["params"]["mu"] = mu

    # define correct answers
    data["correct_answers"]["part1_ans"] = (m * g) / (
        math.sin(math.radians(theta)) + mu * math.cos(math.radians(theta))
    )