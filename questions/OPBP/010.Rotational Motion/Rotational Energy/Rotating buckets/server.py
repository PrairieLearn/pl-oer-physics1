import random as rd

import prairielearn as pl
import sympy as sp

def generate(data):

    # define bounds of the variables
    # use m1 for mass because m needs to be used as a sympy symbol
    # c is the constant divisor in part 2
    m1 = round(rd.uniform(1.00, 3.00), 2)
    c = rd.randint(2, 6)

    # store the variables in the dictionary "params"
    data["params"]["m1"] = m1
    data["params"]["c"] = c

    ## Part 1

    # Declare math symbols to be used by sympy
    m, l = sp.symbols("m l")

    # Describe the solution equation
    I = m * l * l / 2

    # Answer to fill in the blank input stored as JSON.
    data["correct_answers"]["part1_ans"] = pl.to_json(I)

    ## Part 2

    # calculate final mass of one bucket
    m_f = c * m1

    # define correct answers
    data["correct_answers"]["part2_ans"] = 2 * (m_f - m1)