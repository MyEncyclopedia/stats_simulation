import random

def normal():
    import math
    u = random.random()
    return (math.pow(u, 0.135) - math.pow(1-u, 0.135)) / 0.1975
