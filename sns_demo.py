import random

import seaborn as sns
import numpy as np
import pandas as pd


def gen_gaussian():
    # 0. Initialize random number generator
    rng = np.random.RandomState(seed=42)

    # 1. Generate 1000 U1 and U2, which are Unif(0, 1)
    u1s, u2s = rng.uniform(size=1000), rng.uniform(size=1000)

    # 2. Tranform U1 to s
    ss = -np.log(u1s)

    # 3. Transform U2 to theta
    thetas = 2 * np.pi * u2s

    # 4. Convert s to r
    rs = np.sqrt(2 * ss)

    # 5. Calculate x and y from r and theta
    xs, ys = rs * np.cos(thetas), rs * np.sin(thetas)

    return xs, ys


def gaussian():
    # u = random.random()

    # 1. Generate 1000 U1 and U2, which are Unif(0, 1)
    u1s, u2s = random.random(), random.random()

    # 2. Tranform U1 to s
    ss = -np.log(u1s)

    # 3. Transform U2 to theta
    thetas = 2 * np.pi * u2s

    # 4. Convert s to r
    rs = np.sqrt(2 * ss)

    # 5. Calculate x and y from r and theta
    xs, ys = rs * np.cos(thetas), rs * np.sin(thetas)

    return [xs, ys]

# print(gaussian())
data = [gaussian() for i in range(1000)]

# df = pd.DataFrame(data, columns =['x', 'y'])
df = pd.DataFrame.from_records(data, columns=['x', 'y'])
# print(df)
# df = sns.load_dataset('iris')

# Custom the inside plot: options are: “scatter” | “reg” | “resid” | “kde” | “hex”
# sns.jointplot(x=df["sepal_length"], y=df["sepal_width"], kind='scatter')
# sns.jointplot(x=df["sepal_length"], y=df["sepal_width"], kind='hex')
sns.jointplot(x=df["x"], y=df["y"], kind='kde')
import matplotlib.pyplot as plt
plt.show()
# print('oe')