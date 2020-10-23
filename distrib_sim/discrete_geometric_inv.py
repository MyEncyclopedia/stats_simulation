import random
from math import floor
from math import log2 as ln


def geometric(p: float) -> int:
    u = random.random()
    return floor(ln(u) / ln(1-p))