import random
from math import log2 as ln

def exp_gen(lambbda: float) -> float:
    u = random.random()
    return -ln(u) / lambbda