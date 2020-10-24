from discrete_bernoulli import bernoulli


# todo has bug
def negative_hypergeometric(M: int, n: int, r: int) -> int:
    x = M - n
    failures = 0
    while r:
        success = bernoulli(n / (n + x))
        if success:
            r -= 1
            n -= 1
            if n == 0:
                return failures
        else:
            failures += 1
            x -= 1
    return success
