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

from continuous import exp_gen


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


def hypergeometrix_dgen():
    # bisect
    pass

def binomial_dgen(n: int, p: float) -> int:
    return sum(bernoulli_gen(p) for _ in range(n))


def binomial_geometric_dgen(n: int, p: float) -> int:
    total = 0
    i = 0
    while total <= n:
        y = geometric_d_gen(p)
        total += y + 1
        i += 1
    return i - 1


def binomial_exp_dgen(n: int, p: float) -> int:
    total = 0.0
    i = 0
    threshold = -ln(1-p)
    while total <= threshold:
        y = exp_gen(1.0)
        i += 1
        total += y / (n - i + 1)
    return i - 1

def nagetive_binomial_dgen2(p: float) -> int:
    pass


def poisson_dgen(lambdda: float) -> int:
    pass



def poisson_dgen(lambdda: float) -> int:
    pass


def plot_bernoulli(p: float, n=1000):
    # data = [bernoulli_gen(p) for i in range(n)]
    # data = [uniform_discrete_gen(3, 8) for i in range(n)]
    # data = [geometric_d_gen2(0.3) for i in range(n)]
    # data = [binomial_dgen(6, 0.8) for i in range(n)]
    # data = [binomial_geometric_dgen(6, 0.8) for i in range(n)]
    data = [binomial_exp_dgen(6, 0.8) for i in range(n)]
    sns.distplot(data)
    plt.show()


if __name__ == "__main__":
    plot_bernoulli(0.3)

