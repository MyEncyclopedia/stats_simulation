from discrete_bernoulli import bernoulli


def hypergeometric(N: int, K_succ_num: int, n_trial_num: int) -> int:
    x = N - K_succ_num
    n_hit = 0
    while n_trial_num:
        hit = bernoulli(K_succ_num / (K_succ_num + x))
        n_hit += hit
        if hit:
            K_succ_num -= 1
        else:
            x -= 1
        if K_succ_num == 0:
            return n_hit
        n_trial_num -= 1
    return n_hit
