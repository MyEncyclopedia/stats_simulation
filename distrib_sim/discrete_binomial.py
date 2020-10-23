from discrete_bernoulli import bernoulli


def binomial(n: int, p: float) -> int:
    return sum(bernoulli(p) for _ in range(n))