import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import empiricalcumulativedistribution as ecdf
# Seed the random number generator

import seaborn as sns

# Take 10,000 samples out of the binomial distribution: n_defaults

n_defaults = np.random.binomial(100, 0.05, 10000)
# Compute CDF: x, y

x,y = ecdf.ecdf(n_defaults)


# Plot the CDF with axis labels

_ = plt.plot(x,y, marker ='.', linestyle ='none')
_ = plt.xlabel('number of defaults out of 100')
_ = plt.ylabel('CDF')




# Show the plot

plt.show()

