import math
import random

import pandas as pd

def generate(data):

    # define or load names/items/objects
    vehicles = pd.read_csv(
        "https://raw.githubusercontent.com/open-resources/problem_bank_helpers/main/data/vehicles.csv"
    )["Vehicles"].tolist()


    # define bounds of the variables
    mu_k = round(random.uniform(0.2, 0.5), 2)
    mu_s = round(random.uniform(mu_k + 0.1, 1.0), 2)
    theta = random.randint(10, 30)

    # store the variables in the dictionary "params"
    data["params"]["vehicles"] = random.choice(vehicles)
    data["params"]["mu_s"] = mu_s
    data["params"]["mu_k"] = mu_k
    data["params"]["theta"] = theta

    # define g
    g = 9.81

    # calculate a_max
    theta_r = math.radians(theta)  # convert to radians
    a_max = g * (mu_s * math.cos(theta_r) - math.sin(theta_r))

    # define correct answers
    data["correct_answers"]["part1_ans"] = a_max