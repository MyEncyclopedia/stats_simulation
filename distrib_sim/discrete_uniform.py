import random
from math import floor


def uniform(a: int, b: int) -> int:
    assert a <= b
    u = random.random()
    return a + floor((b - a + 1) * u)