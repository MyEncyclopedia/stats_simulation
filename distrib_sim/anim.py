import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import seaborn as sns

from discrete import binomial_exp_dgen

n = 1000

data = [binomial_exp_dgen(6, 0.8) for i in range(n)]

def clt(current):
    # if animation is at the last frame, stop it
    plt.cla()
    if current == n:
        a.event_source.stop()

    # ax = sns.distplot(data[0:current], hist=True)
    # ax.set_xlim(0, 6)
    # ax.set_ylim(0, 1)

    # ax = plt.hist(data[0:current], density=True, histtype='stepfilled', rwidth=4)
    ax = plt.hist(data[0:current], density=True, rwidth=4, histtype='bar')
    plt.xlim(0, 7)
    plt.ylim(0, 1.1)

    # plt.gca().set_title('Expected value of die rolls')
    # plt.gca().set_xlabel('Average from die roll')
    # plt.gca().set_ylabel('Frequency')

    # plt.annotate('Die roll = {}'.format(current), [3,27])

fig = plt.figure()
a = animation.FuncAnimation(fig, clt, interval=1)
plt.show()