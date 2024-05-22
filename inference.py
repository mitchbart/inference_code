# Imports
import random
import math
import matplotlib.pyplot as plt


# Function to build sampling distribution list
def build_sampling_distribution(population, n_observations, n_times):
    sample_dist = []
    for i in range(n_times):  # loop through number of times to sample
        sample = random.sample(population, n_observations)  # sample without replacement
        count = sample.count(1)  # count occurrences of 1 in the sample
        p_hat = count / n_observations  # compute p hat
        sample_dist.append(p_hat)  # append p hat to list
    return sample_dist


# Function to visualise sampling distribution
def vis_distribution(p, n):
    pop_size = 40000  # population size - fill in
    n_samples = 1000  # number of times to repeat testing - fill in
    count_y = int(pop_size * p)  # calc % p
    count_n = pop_size - count_y  # calc % not p
    pop_list = [1] * count_y + [0] * count_n  # create a list representative of population
    sampling_dist = build_sampling_distribution(pop_list, n, n_samples)

    plt.hist(sampling_dist, bins=24, edgecolor='black')
    plt.title('Histogram of Entries')
    plt.xlabel('Entry Type')
    plt.ylabel('Frequency')
    plt.show()


# Function to calculate standard error
def calc_standard_error(n, p):
    se = math.sqrt(((1 - p) * p) / n)
    return se


def calc_ci_range(n, p, se=0, ci=95):
    # Calculated standard error if not provided
    if se == 0:
        se = calc_standard_error(n, p)
    # Determine confidence interval value
    if ci == 90:
        ci_val = 1.6449 * se
    elif ci == 99:
        ci_val = 2.58 * se
    else:  # 95% confidence interval
        ci_val = 1.96 * se
    return p - ci_val, p + ci_val


# Function to test if CTL holds
def test_CLT(n, p):
    # Sample is considered sufficiently large when np>=10 and n(1-p)>=10
    np = n * p
    n_one_minus_p = (1 - p) * n

    # Output results
    print("np:", np)
    print("n(1 - p):", n_one_minus_p)
    print()
    if np >= 10 and n_one_minus_p >= 10:
        print("Sample size is sufficiently large")
        return True
    else:
        print("Sample size is insufficient")
        return False


if __name__ == '__main__':
    p = 0.16  # p hat or p for following calculations
    n = 100 # observations per sample

    # View sampling distribution - needs additional info entered in function
    #vis_distribution(p, n)

    # Determine if CTL holds
    if test_CLT(n, p):
        print("mean:", p)

    # Determine standard error
    se = round(calc_standard_error(n, p), 3)
    print("standard error:", se)

    # Determine confidence interval
    lower, upper = calc_ci_range(n, p, se, 95)
    print("95% confidence interval: {} - {}".format(round(lower, 3), round(upper, 3)))
