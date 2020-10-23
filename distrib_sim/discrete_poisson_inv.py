import random
from math import exp


def poisson(lambdda: float) -> int:
    total = 1.0
    i = 0
    threshold = exp(-1 * lambdda)
    while total >= threshold:
        u = random.random()
        total *= u
        i += 1
    return i - 1