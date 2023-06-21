import random as rd
import sympy as sp

def generate(data):

    # define the variable x
    x = sp.Symbol("x")

    # Generate coefficients.
    # For simplicity, we limit ourselves to quadratic functions
    # To obtain a positive answer for the length, we need the coefficients of x^2 and x to be of opposite signs
    a = rd.randint(1, 20)  # coefficient of x^2
    b = rd.randint(-20, -1)  # coefficient of x
    c = rd.randint(-100, 100)  # constant

    # Generate expression for U(x)
    Ux = a * x**2 + b * x + c

    str_Ux = "$" + str(Ux).replace("**", "^") + "$"

    # store the expression in the dictionary "params"
    data["params"]["Ux"] = str_Ux.replace("*", "")

    # Find the force.  F = - (dU/dx)
    F = (-1) * sp.diff(Ux)

    # Solve for x.  Returns a list.
    ans = sp.solve(F, x)

    # define correct answers
    data["correct_answers"]["part1_ans"] = float(ans.pop(0))