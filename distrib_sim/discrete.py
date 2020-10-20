import random
import math
import bisect
from typing import List

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


def categorical_dgen(probs: List[float]) -> int:
    assert abs(sum(probs) - 1.0) < 0.001
    cum = probs.copy()

    for i in range(1, len(cum)):
        cum[i] = cum[i-1] + probs[i]

    u = random.random()
    return bisect.bisect(cum, u)


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
        # print(f'{i}, (n - i + 1) = {(n - i + 1)}')
        if n - i + 1 == 0:
            return n
        total += y / (n - i + 1)
    return i - 1

def nagative_binomial_dgen(n: int, p: float) -> int:
    return sum(geometric_d_gen(p) for _ in range(n))


def poisson_dgen(lambdda: float) -> int:
    pass



def poisson_dgen(lambdda: float) -> int:
    pass

def plot_compare():
    sns.set_style("white")

    data1 = [binomial_exp_dgen(6, 0.8) for i in range(2000)]
    data2 = [binomial_exp_dgen(6, 0.8) for i in range(2000)]
    # data2 = [binomial_geometric_dgen(6, 0.8) for i in range(1000)]

    # Plot
    kwargs = dict(hist_kws={'alpha':.6}, kde_kws={'linewidth':2, 'shade': True})

    plt.figure(figsize=(10,7), dpi= 80)
    sns.distplot(data1, color="dodgerblue", label="Compact", **kwargs)
    sns.distplot(data2, color="orange", label="SUV", **kwargs)
    # plt.xlim(50,75)
    plt.legend();
    print('done')

def plot_bernoulli(p: float, n=1000):
    # data = [bernoulli_gen(p) for i in range(n)]
    # data = [uniform_discrete_gen(3, 8) for i in range(n)]
    # data = [geometric_d_gen2(0.3) for i in range(n)]
    # data = [binomial_dgen(6, 0.8) for i in range(n)]
    # data = [binomial_geometric_dgen(6, 0.8) for i in range(n)]
    data = [binomial_exp_dgen(6, 0.8) for i in range(n)]
    # data = [nagative_binomial_dgen(6, 0.8) for i in range(n)]
    sns.distplot(data)
    plt.show()


if __name__ == "__main__":
    plot_compare()
    # plot_bernoulli(0.3)
    # for _ in range(100):
    #     print(categorical_dgen([0.1, 0.5, 0.15, 0.15, 0.1]))

