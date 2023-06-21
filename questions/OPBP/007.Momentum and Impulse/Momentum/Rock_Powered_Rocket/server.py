import random

import pandas as pd

def generate(data):

    # define or load names/items/objects from server files
    names = pd.read_csv(
        "https://raw.githubusercontent.com/open-resources/problem_bank_helpers/main/data/names.csv"
    )["Names"].tolist()
    name = random.choice(names)

    # store phrases etc
    data["params"]["units1"] = "m/s"
    data["params"]["units2"] = "kg"
    data["params"]["name"] = name

    # define bounds of the variables
    i = random.randint(300, 400)
    m = random.randint(20, 40)
    v_1 = random.randint(5, 30)
    v_2 = v_1 + random.randint(2, 25)

    # store the variables in the dictionary "params"
    data["params"]["i"] = i
    data["params"]["m"] = m
    data["params"]["v_1"] = v_1
    data["params"]["v_2"] = v_2

    ## Part 1

    # define correct answers
    data["correct_answers"]["part1_ans"] = 0

    ## Part 2

    # define correct answers
    data["correct_answers"]["part2_ans"] = (-((m + i) * v_1)) / m

    ## Part 3

    # define correct answers
    data["correct_answers"]["part3_ans"] = (((m + i) * v_1) - (i * v_2)) / m
