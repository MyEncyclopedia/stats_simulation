import bisect
import random
from typing import List


def categorical(probs: List[float]) -> int:
    assert abs(sum(probs) - 1.0) < 0.001
    cum = probs.copy()

    for i in range(1, len(cum)):
        cum[i] = cum[i-1] + probs[i]

    u = random.random()
    return bisect.bisect(cum, u)