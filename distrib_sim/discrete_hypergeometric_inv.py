from scipy.special import comb

from discrete_categorical import categorical


def hypergeometric(M: int, n: int, N: int) -> int:
    pmf = [comb(n, k, exact=True) * comb(M - n, N - k, exact=True) / comb(M, N, exact=True)
           for k in range(max(0, N - (M-n)), min(n, N)+1)]
    return categorical(pmf)