from math import cos, sin
import random

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from scipy import optimize

plt.style.use('seaborn-poster')

def first_example(x):
    return pow(x, 2) - 12 * x + 30
    # return pow(x, 2) - 2 * x + 1


def second_example(x):
    return sin(x) - cos(x)


def third_example(x):
    return 2*pow(x, 3) - 3 * x + 15


def generate_nodes(n, x0, xn, func):
    x = [x0]
    y = [func(x0)]
    for i in range(1, n):
        aux = random.uniform(x[i - 1], xn)
        x.append(aux)
        y.append(func(aux))
    return x, y


def newton_interpolation(x, y, xi):
    # length/number of datapoints
    n = len(x)
    # divided difference initialization
    fdd = [[None for x in range(n)] for x in range(n)]
    # f(X) values at different degrees
    yint = [None for x in range(n)]
    # error value
    ea = [None for x in range(n)]

    # finding divided difference
    for i in range(n):
        fdd[i][0] = y[i]
    for j in range(1, n):
        for i in range(n - j):
            fdd[i][j] = (fdd[i + 1][j - 1] - fdd[i][j - 1]) / (x[i + j] - x[i])

    # interpolating xi
    xterm = 1
    yint[0] = fdd[0][0]
    for order in range(1, n):
        xterm = xterm * (xi - x[order - 1])
        yint2 = yint[order - 1] + fdd[0][order] * xterm
        ea[order - 1] = yint2 - yint[order - 1]
        yint[order] = yint2
    # returning a map for pandas dataframe
    return yint

def horner(poly, n, x):
    # Initialize result
    result = poly[0]

    # Evaluate value of polynomial
    # using Horner's method
    for i in range(1, n):
        result = result * x + poly[i]

    return result

def lsm(x,y):
    # assemble matrix A
    A = np.vstack([x, np.ones(len(x))]).T

    # turn y into a column vector
    y_new = y[:, np.newaxis]

    # Direct least square regression
    alpha = np.dot((np.dot(np.linalg.inv(np.dot(A.T, A)), A.T)), y_new)
    print(alpha)


def run_example(example):
    while 1:
        try:
            n = int(input('n = '))
            x0 = float(input('x0 = '))
            xn = float(input('xn = '))
            point = float(input('point = '))
            if x0 < xn:
                break
            print('\tMake sure x0 < xn')
        except Exception as e:
            print(e)

    func = example

    x, y = generate_nodes(n + 1, x0, xn, func)
    print('x = ', x)
    print("\n")
    print('y = ', y)
    print("\n")

    a = newton_interpolation(x, y, 2)
    print(a)
    print("\n")
    lsm(np.array(x), np.array(y))
    print("\n")


if __name__ == '__main__':
    run_example(first_example)
    run_example(second_example)
    run_example(third_example)
