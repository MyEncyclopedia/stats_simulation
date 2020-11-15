from discrete_bernoulli import bernoulli

def negative_binomial(r: int, p: float) -> int:
    failures = 0
    while r:
        success = bernoulli(p)
        if success:
            r -= 1
        else:
            failures += 1
    return failures

