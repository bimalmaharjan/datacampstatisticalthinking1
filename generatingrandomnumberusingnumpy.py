import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import empiricalcumulativedistribution as ecdf
# Seed the random number generator

import seaborn as sns

np.random.seed(42)


# Initialize random numbers: random_numbers
random_numbers = np.empty(100000)

# Generate random numbers by looping over range(100000)
for i in range(100000):
    random_numbers[i] = np.random.random()

# Plot a histogram
_ = plt.hist(random_numbers)

# Show the plot
plt.show()


def perform_bernoulli_trials(n, p):
    """Perform n Bernoulli trials with success probability p
    and return number of successes."""
    # Initialize number of successes: n_success
    n_success = 0


    # Perform trials
    for i in range(n):
        # Choose random number between zero and one: random_number
        random_number = np.random.random()


        # If less than p, it's a success so add one to n_success
        if random_number < p:
            n_success += 1

    return n_success


# Initialize the number of defaults: n_defaults
n_defaults = np.empty(1000)


# Compute the number of defaults
for i in range(1000):
    n_defaults[i] = perform_bernoulli_trials(n = 100, p = 0.05)


# Plot the histogram with default number of bins; label your axes
_ = plt.hist(n_defaults, normed= True)
_ = plt.xlabel('number of defaults out of 100 loans')
_ = plt.ylabel('probability')

# Show the plot
plt.show()


# Compute ECDF: x, y
x,y = ecdf.ecdf(n_defaults)


# Plot the ECDF with labeled axes
_ = plt.plot(x,y, marker='.',linestyle='none')
_ = plt.xlabel('interest rate')
_ = plt.ylabel('probability of losing money')


# Show the plot
plt.show()


# Compute the number of 100-loan simulations with 10 or more defaults: n_lose_money
n_lose_money = np.sum(n_defaults >= 10)
    


# Compute and print probability of losing money
print('Probability of losing money =', n_lose_money / float(len(n_defaults)))
