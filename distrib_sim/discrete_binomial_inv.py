from scipy.special import comb

from discrete_categorical import categorical
from math import pow


def binomial(n: int, p: float) -> int:
    pmf = [comb(n, k, exact=True) * pow(p, k) * pow(1-p, n-k) for k in range(0, n + 1)]
    return categorical(pmf)