from discrete_geometric import geometric


def nagative_binomial_dgen(n: int, p: float) -> int:
    return sum(geometric(p) for _ in range(n))