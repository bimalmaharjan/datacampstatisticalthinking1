import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import empiricalcumulativedistribution as ecdf
# Seed the random number generator

import seaborn as sns

sns.set()

# Take 10,000 samples out of the binomial distribution: n_defaults

n_defaults = np.random.binomial(100, 0.05, 10000)


# Compute bin edges: bins
bins = np.arange(0, max(n_defaults) + 1.5) - 0.5

# Generate histogram

_ = plt.hist(n_defaults, bins= bins, normed= True)


# Set margins
_ = plt.margins(0.02)


# Label axes
_ = plt.xlabel('defaults')
_ = plt.ylabel('probability')



# Show the plot
plt.show()

