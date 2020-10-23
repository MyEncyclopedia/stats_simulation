import random


def bernoulli(p: float) -> int:
    assert 0 <= p <= 1
    u = random.random()
    return 1 if u <= p else 0