from discrete_bernoulli import bernoulli


def hypergeometric(M: int, n: int, N: int) -> int:
    x = M - n
    n_hit = 0
    while N:
        hit = bernoulli(n / (n + x))
        n_hit += hit
        if hit:
            n -= 1
        else:
            x -= 1
        if n == 0:
            return n_hit
        N -= 1
    return n_hit
