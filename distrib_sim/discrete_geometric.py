from discrete_bernoulli import bernoulli


def geometric(p: float) -> int:
    fail_num = 0
    while not bernoulli(p):
        fail_num += 1
    return fail_num