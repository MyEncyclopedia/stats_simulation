import random
import math
import seaborn as sns
import matplotlib.pyplot as plt
from math import log2 as ln
from math import exp
from math import sqrt
from math import pow
from math import cos
from math import sin
from math import pi

def uniform_continous_gen(a: float, b: float) -> float:
    u = random.random()
    return a + (b - a) * u

def exp_gen(lambbda: float) -> float:
    u = random.random()
    return -ln(u) / lambbda


def weibull_gen(a: float, lambbda: float) -> float:
    u = random.random()
    return pow(-ln(u), 1/a) / lambbda


def gaussian_box_muller() -> float:
    u1 = random.random()
    u2 = random.random()
    x1 = sqrt(-2 * ln(u1)) * cos(2 * pi * u2)
    x2 = sqrt(-2 * ln(u1)) * sin(2 * pi * u2)
    return x1


def random_sign():
    return 1 if random.randint(0, 1) else 0


def gaussian_accept_reject() -> float:
    while True:
        y = exp_gen(1.0)
        u = random.random()
        if u <= exp(-pow(y-1, 2) / 2):
            return y * (1 if random.randint(0, 1) else -1)



def beta_cgen():
    # a, b = 4, 3
    while True:
        y = random.random()
        u = random.random()
        if u <= 60 * pow(y, 3) * pow(1-y, 2) / 2.0736:
            return y


def plot_exp(lambbda: float, n=1000):
    data = [exp_gen(lambbda) for i in range(n)]
    sns.distplot(data)
    plt.show()


def plot_gaussian(n=1000):
    # data = [gaussian_accept_reject() for i in range(n)]
    data = [gaussian_box_muller() for i in range(n)]
    sns.distplot(data)
    plt.show()


if __name__ == "__main__":
    # plot_exp(1.0)
    plot_gaussian(n=5000)

