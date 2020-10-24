from discrete_geometric import geometric


def negative_binomial(r: int, p: float) -> int:
    return sum([geometric(p) for _ in range(r)])


