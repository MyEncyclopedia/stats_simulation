import random
import math
import seaborn as sns
import matplotlib.pyplot as plt


def exp(lambbda: float) -> float:
    u = random.random()
    return -math.log2(u) / lambbda



def plot_exp(lambbda: float, n=3000):
    data = [exp(lambbda) for i in range(n)]
    sns.distplot(data)
    plt.show()

if __name__ == "__main__":
    plot_exp(1.0)

