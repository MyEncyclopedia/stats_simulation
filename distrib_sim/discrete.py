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
from math import floor

def uniform_discrete_gen(a: int, b: int) -> int:
    u = random.random()
    return a + floor((b - a + 1) * u)


def bernoulli_gen(p: float):
    assert 0 <= p <= 1
    u = random.random()
    return 1 if u <= p else 0


def geometric_d_gen(p: float) -> int:
    success_times = 0
    while not bernoulli_gen(p):
        success_times += 1
    return success_times


def geometric_d_gen2(p: float) -> int:
    u = random.random()
    return floor(ln(u) / ln(1-p))


def binomial_dgen(p: float) -> int:
    pass


def binomial_dgen2(p: float) -> int:
    pass


def nagetive_binomial_dgen2(p: float) -> int:
    pass


def poisson_dgen(lambdda: float) -> int:
    pass



def poisson_dgen(lambdda: float) -> int:
    pass


def plot_bernoulli(p: float, n=1000):
    # data = [bernoulli_gen(p) for i in range(n)]
    # data = [uniform_discrete_gen(3, 8) for i in range(n)]
    data = [geometric_d_gen2(0.3) for i in range(n)]
    sns.distplot(data)
    plt.show()


if __name__ == "__main__":
    plot_bernoulli(0.3)

