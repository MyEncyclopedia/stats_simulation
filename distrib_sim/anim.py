import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import seaborn as sns

from discrete import binomial_exp_dgen, uniform_discrete_gen, geometric_d_gen, categorical_dgen

n = 5000

# data = [binomial_exp_dgen(6, 0.8) for i in range(n)]
# data = [geometric_d_gen(0.8) for i in range(n)]
# data = [uniform_discrete_gen(0, 6) for _ in range(n)]
# data = np.random.geometric(p=0.8, size=10000)
# data = [categorical_dgen([0.1, 0.2, 0.4, 0.05, 0.05, 0.1, 0.1]) for i in range(n)]

def clt(current):
    print(current)
    # if animation is at the last frame, stop it
    plt.cla()
    if current == n:
        a.event_source.stop()

    min_x = 0
    max_x = 6
    # ax = sns.distplot(data[0: 5* current], hist=True, bins=np.arange(min_x + 0.5, max_x+2, 1), kde_kws={'bw':1}, hist_kws={"histtype": "step", "linewidth": 3, "alpha": 0.5, "color": "g"})
    ax = sns.distplot(data[0: 5* current], hist=True, bins=np.arange(min_x + 0.5, max_x+2, 1), kde_kws={'bw':1}, hist_kws={"linewidth": 3, "alpha": 0.5, "color": "g"})
    plt.xticks(np.arange(min_x, max_x + 2, 1))
    plt.xlim(min_x, max_x+2)
    plt.ylim(0, 1)

    # ax = plt.hist(data[0:current], density=True, histtype='stepfilled')
    # ax = plt.hist(data[0:10*current], density=True, rwidth=4, histtype='bar', align="center")
    # ax = plt.hist(data[0:10*current], density=True, rwidth=4, histtype='bar', align='center')
    # plt.xlim(0, 6)
    # plt.ylim(0, 1.1)

    # plt.gca().set_title('Expected value of die rolls')
    # plt.gca().set_xlabel('Average from die roll')
    # plt.gca().set_ylabel('Frequency')


# from discrete_poisson_from_exp import poisson
# from discrete_poisson_inv import poisson
# data = [poisson(4) for _ in range(n)]

def clt_possion(current):
    print(current)
    # if animation is at the last frame, stop it
    plt.cla()
    if current == n:
        a.event_source.stop()

    min_x = 0
    max_x = 14
    # ax = sns.distplot(data[0: 5* current], hist=True, bins=np.arange(min_x + 0.5, max_x+2, 1), kde_kws={'bw':1}, hist_kws={"histtype": "step", "linewidth": 3, "alpha": 0.5, "color": "g"})
    ax = sns.distplot(data[0: 5* current], hist=True, bins=np.arange(min_x + 0.5, max_x+2, 1), kde_kws={'bw':1}, hist_kws={"linewidth": 3, "alpha": 0.5, "color": "g"})
    plt.xticks(np.arange(min_x, max_x + 2, 1))
    plt.xlim(min_x, max_x+2)
    plt.ylim(0, 1)


# from discrete_hypergeometric_inv import hypergeometric
# from discrete_hypergeometric import hypergeometric
# data = [hypergeometric(20, 7, 12) for _ in range(n)]
# def clt_hypergeometric(current):
#     print(current)
#     # if animation is at the last frame, stop it
#     plt.cla()
#     if current == n:
#         a.event_source.stop()
#
#     min_x = 0
#     max_x = 8
#     # ax = sns.distplot(data[0: 5* current], hist=True, bins=np.arange(min_x + 0.5, max_x+2, 1), kde_kws={'bw':1}, hist_kws={"histtype": "step", "linewidth": 3, "alpha": 0.5, "color": "g"})
#     ax = sns.distplot(data[0: 1* current], hist=True, bins=np.arange(min_x + 0.5, max_x+2, 1), kde_kws={'bw':1}, hist_kws={"linewidth": 3, "alpha": 0.5, "color": "g"})
#     plt.xticks(np.arange(min_x, max_x + 2, 1))
#     plt.xlim(min_x, max_x+2)
#     plt.ylim(0, 1)

# from discrete_nagative_binomial import negative_binomial
from discrete_nagative_binomial_from_geometric import negative_binomial
data = [negative_binomial(5, 0.5)  for _ in range(n)]
def clt_negbinomial(current):
    print(current)
    # if animation is at the last frame, stop it
    plt.cla()
    if current == n:
        a.event_source.stop()

    min_x = 0
    max_x = 16
    # ax = sns.distplot(data[0: 5* current], hist=True, bins=np.arange(min_x + 0.5, max_x+2, 1), kde_kws={'bw':1}, hist_kws={"histtype": "step", "linewidth": 3, "alpha": 0.5, "color": "g"})
    ax = sns.distplot(data[0: 20 * current], hist=True, bins=np.arange(min_x + 0.5, max_x+2, 1), kde_kws={'bw':1}, hist_kws={"linewidth": 3, "alpha": 0.5, "color": "g"})
    plt.xticks(np.arange(min_x, max_x + 2, 1))
    plt.xlim(min_x, max_x+2)
    plt.ylim(0, 1)

fig = plt.figure()
a = animation.FuncAnimation(fig, clt_negbinomial, interval=1)
plt.show()