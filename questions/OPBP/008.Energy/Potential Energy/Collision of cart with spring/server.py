import math
import random as rd

def generate(data):

    # define bounds of the variables
    m = rd.randint(10, 100)
    k = rd.randint(200, 400)
    x = rd.randint(20, 100)

    # store the variables in the dictionary "params"
    data["params"]["m"] = m
    data["params"]["k"] = k
    data["params"]["x"] = x

    # define correct answers
    data["correct_answers"]["part1_ans"] = math.sqrt(k / m) * (x / 100)
