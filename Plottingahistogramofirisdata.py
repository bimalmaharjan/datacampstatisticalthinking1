from sklearn.datasets import load_iris
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
data = load_iris()

# np.where(data.target == 1) gives indices where versicolor = 1

versicolor_petal_length = data.data[np.where(data.target == 1)][:,2]

# Set default Seaborn style
sns.set()

# Compute number of data points: n_data
n_data = len(versicolor_petal_length)


# Number of bins is the square root of number of data points: n_bins
n_bins = np.sqrt(n_data)


# Convert number of bins to integer: n_bins
n_bins = int(n_bins)

# Plot histogram of versicolor petal lengths
# _ = plt.hist(versicolor_petal_length)
# Plot the histogram
_ = plt.hist(versicolor_petal_length, bins=n_bins)

# Label axes
_ = plt.xlabel('petal length (cm)')
_ = plt.ylabel('count')


# Show histogram

plt.show()



