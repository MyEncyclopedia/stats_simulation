from discrete_bernoulli import bernoulli


def negative_hypergeometric(N: int, K_success_num: int, r_fail_times: int) -> int:
    fail_num = N - K_success_num
    succ_trials = 0
    while r_fail_times:
        success = bernoulli(K_success_num / (K_success_num + fail_num))
        if success:
            K_success_num -= 1
            succ_trials += 1
            if K_success_num == 0: # no more success elements
                return succ_trials
        else:
            fail_num -= 1
            r_fail_times -= 1
    return succ_trials
