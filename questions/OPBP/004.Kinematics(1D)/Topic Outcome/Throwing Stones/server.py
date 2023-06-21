import random as rd
from collections import defaultdict

import pandas as pd


def generate(data):
    data2 = lambda: defaultdict(data2)

    # define or load names/items/objects
    names = pd.read_csv(
        "https://raw.githubusercontent.com/open-resources/problem_bank_helpers/main/data/names.csv"
    )["Names"].tolist()

    # store phrases etc
    data2["params"]["vars"]["name"] = rd.choice(names)
    data2["params"]["vars"]["units"] = "$s$"

    # define bounds of the variables
    v = round(rd.uniform(10.0, 30.0), 1)

    # store the variables in the dictionary "params"
    data2["params"]["v"] = v

    # define g
    g = 9.81

    # define correct answers
    data2["correct_answers"]["part1_ans"] = (2 * v) / g

    # Update the data object with a new dict
    data.update(data2)
