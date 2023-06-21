import random

def generate(data):

    # define bounds of the variables
    v = random.randint(10, 30)
    r = random.randint(100, 300)
    mu = random.randint(500, 900) / 100

    # store the variables in the dictionary "params"
    data["params"]["v"] = v
    data["params"]["r"] = r
    data["params"]["mu"] = mu

    ## Part 1

    # define correct answers
    data["correct_answers"]["part1_ans"] = round(-0.850 * (9.8 + (v**2 / r)), 3)

    ## Part 2

    # define correct answers
    data["correct_answers"]["part2_ans"] = round(-0.850 * (9.8 - (v**2 / r)), 3)
