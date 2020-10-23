from discrete_geometric import geometric


def binomial(n: int, p: float) -> int:
    total = 0
    i = 0
    while total <= n:
        y = geometric(p)
        total += y + 1
        i += 1
    return i - 1
