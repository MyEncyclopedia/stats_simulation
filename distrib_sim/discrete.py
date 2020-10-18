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

def uniform_discrete_gen(a: float, b: float) -> float:
    u = random.random()
    return a + (b - a) * u


def bernoulli_gen(p: float):
    assert 0 <= p <= 1
    u = random.random()
    return 1 if u <= p else 0


def plot_bernoulli(p: float, n=1000):
    data = [bernoulli_gen(p) for i in range(n)]
    sns.distplot(data)
    plt.show()


if __name__ == "__main__":
    plot_bernoulli(0.3)

