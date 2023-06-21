import random as rd

import pandas as pd


def generate(data):

    # define or load names/items/objects
    names = pd.read_csv(
        "https://raw.githubusercontent.com/open-resources/problem_bank_helpers/main/data/names.csv"
    )["Names"].tolist()

    # store phrases etc
    data["params"]["name"] = rd.choice(names)

    # define bounds of the variables
    v = round(rd.uniform(10.0, 30.0), 1)

    # store the variables in the dictionary "params"
    data["params"]["v"] = v

    # define g
    g = 9.81

    # define correct answers
    data["correct_answers"]["part1_ans"] = (2 * v) / g

    # Update the data object with a new dict
    data.update(data)
