from numpy.random import exponential


def poisson(lambdda: float) -> int:
    total = 0.0
    i = 0
    while total <= lambdda:
        y = exponential(1)
        total += y
        i += 1
    return i - 1

