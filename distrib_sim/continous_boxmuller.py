import math

import numpy as np
import matplotlib.pyplot as plt


def normal_box_muller_polar():
    import random
    from math import sqrt, log
    while True:
        u = random.uniform(-1, 1)
        v = random.uniform(-1, 1)
        s = u * u + v * v
        if s >= 1.0 or s == 0.0:
            continue
        # return sqrt(-2*log2(s)), s
        z0 = u * sqrt(-2 * log(s) / s)
        z1 = v * sqrt(-2 * log(s) / s)
        return z0, z1


def normal_box_muller():
    import random
    from math import sqrt, log, pi, cos, sin
    u1 = random.random()
    u2 = random.random()
    r = sqrt(-2 * log(u1))
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




def plot_dist_1d(X, title='PDF '):
    import seaborn as sns
    plt.rcParams.update({
        "text.usetex": True,
        "font.family": "sans-serif",
        "font.sans-serif": ["Helvetica"]})
    # n, bins, patches = plt.hist(X, 100, density=True, facecolor='g', alpha=0.75, normed=True)
    sns.distplot(X, hist=True, kde=True, bins=100, color='darkblue',
                 hist_kws={'edgecolor': 'black'},
                 kde_kws={'linewidth': 4})
    plt.title(title)
    plt.show()

def plot_2d():
    x, y = np.random.normal(loc=0, scale=1, size=(2, 10000))
    import seaborn as sns
    g = sns.JointGrid(x=x, y=y, size=4)
    g.plot_joint(sns.kdeplot, cmap="Purples_d")
    g.plot_marginals(sns.kdeplot, color="m", shade=True)
    plt.show()


def plot_normal_1d():
    x, y = np.random.normal(loc=0, scale=1, size=(2, 10000))
    import seaborn as sns
    sns.distplot(x, hist=True, kde=True, bins=100, color='darkblue',
                 hist_kws={'edgecolor': 'black'},
                 kde_kws={'linewidth': 4})
    plt.title('PDF Normal 1D from 2D')
    plt.show()


def gen_polar_s():
    import random
    while True:
        u = random.uniform(-1, 1)
        v = random.uniform(-1, 1)
        s = u * u + v * v
        if s >= 1.0 or s == 0.0:
            continue
        return s


def plot_polar_s():
    s = [gen_polar_s() for _ in range(1000) ]
    a = -np.log(s)
    plot_dist_1d(a, title='PDF Polar $s = u^2 + v^2$')


def plot_r_squared():
    def gen_normal_samples(n):
        x, y = np.random.normal(loc=0, scale=1, size=(2, n))
        return x, y

    x, y = gen_normal_samples(10000)
    s = (x * x + y * y)/2
    s = np.exp(-s)
    plot_dist_1d(s, title='PDF $s = {{x^2 + y^2}\over{2}} \sim exp(1)$')

if __name__ == "__main__":
    # plot_r_squared()
    # plot_normal_1d()
    # plot_2d()
    plot_polar_s()
    # X, Y = [], []
    # for i in range(50000):
    #     x, y = normal_box_muller_polar()
    #     # x, y = normal_box_muller()
    #     X.append(x)
    #     Y.append(y)
    #
    # # plot_2d(X, Y)
    # plot_1d(Y)


