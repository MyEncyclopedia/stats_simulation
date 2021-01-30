from scipy.special import comb

from discrete_categorical import categorical


def hypergeometric(N: int, K_succ_num: int, n_trial_num: int) -> int:
    pmf = [comb(K_succ_num, k, exact=True) * comb(N - K_succ_num, n_trial_num - k, exact=True) / comb(N, n_trial_num, exact=True)
           for k in range(max(0, n_trial_num - (N - K_succ_num)), min(K_succ_num, n_trial_num) + 1)]
    return categorical(pmf)