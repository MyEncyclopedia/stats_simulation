from discrete_bernoulli import bernoulli


def geometric(p: float) -> int:
    success_times = 0
    while not bernoulli(p):
        success_times += 1
    return success_times