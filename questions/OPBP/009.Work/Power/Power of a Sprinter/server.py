import random

def generate(data):
    # define bounds of the variables
    m = random.randint(55, 90)
    v = random.randint(8, 11)
    t = random.randint(1, 5)
    v2 = random.randint(1, 8)

    a = v / t

    # store the variables in the dictionary "params"
    data["params"]["v"] = v
    data["params"]["t"] = t
    data["params"]["m"] = m
    data["params"]["v2"] = v2

    # define correct answers
    data["correct_answers"]["part1_ans"] = m * a * v2
