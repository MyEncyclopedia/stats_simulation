import math

import numpy as np
import matplotlib.pyplot as plt


def normal_box_muller_polar():
    import random
    from math import sqrt, log2
    while True:
        u = random.uniform(-1, 1)
        v = random.uniform(-1, 1)
        s = u * u + v * v
        if s >= 1.0 or s == 0.0:
            continue
        return sqrt(-2*log2(s)), s
        # z0 = u * sqrt(-2 * log2(s) / s)
        # z1 = v * sqrt(-2 * log2(s) / s)
        # return z0, z1


def normal_box_muller():
    import random
    from math import sqrt, log2, pi, cos, sin
    u1 = random.random()
    u2 = random.random()
    r = sqrt(-2 * log2(u1))
    theta = 2 * pi * u2
    z0 = r * cos(theta)
    z1 = r * sin(theta)
    return z0, z1


def gen_gaussian_2d(var=1.0, size=10):
    # 0. Initialize random number generator
    rng = np.random.RandomState(seed=42)
    # 1. Generate 1000 U1 and U2, which are Unif(0, 1)
    u1s, u2s = rng.uniform(size=size), rng.uniform(size=size)
    # 2. Tranform U1 to S
    ss = -np.log(u1s)
    # 3. Transform U2 to theta
    thetas = 2*np.pi*u2s
    # 4. Convert s to r
    rs = np.sqrt(2*ss)
    # 5. Calculate x and y from r and theta
    xs, ys = rs*np.cos(thetas), rs*np.sin(thetas)
    return xs * var, ys * var


def plot_2d(X, Y):
    import seaborn as sns
    g = sns.JointGrid(x=X, y=Y, size=4)
    g.plot_joint(sns.kdeplot, cmap="Purples_d")
    g.plot_marginals(sns.kdeplot, color="m", shade=True)
    plt.show()


def plot_1d(X):
    import seaborn as sns
    plt.rcParams.update({
        "text.usetex": True,
        "font.family": "sans-serif",
        "font.sans-serif": ["Helvetica"]})
    # n, bins, patches = plt.hist(X, 100, density=True, facecolor='g', alpha=0.75, normed=True)
    sns.distplot(X, hist=True, kde=True, bins=100, color='darkblue',
                 hist_kws={'edgecolor': 'black'},
                 kde_kws={'linewidth': 4})
    # plt.title('PDF $\sqrt{-2 \ln(s)}$')
    plt.title('PDF $s=R^2$')
    plt.show()


if __name__ == "__main__":
    X, Y = [], []
    for i in range(50000):
        x, y = normal_box_muller_polar()
        # x, y = normal_box_muller()
        X.append(x)
        Y.append(y)

    # plot_2d(X, Y)
    plot_1d(Y)


