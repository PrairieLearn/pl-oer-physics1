import prairielearn as pl
import sympy as sp

def generate(data):

    # Declare math symbols to be used by sympy
    g, h = sp.symbols("g h")
    r = sp.symbols("r", positive=True)
    # Describe the solution equation
    w = sp.sqrt(2 * g * h) / r

    # Answer to fill in the blank input stored as JSON.
    data["correct_answers"]["part1_ans"] = pl.to_json(w)
