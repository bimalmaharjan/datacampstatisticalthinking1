from sklearn.datasets import load_iris
import numpy as np
data = load_iris()

versicolor_petal_length = data.data[np.where(data.target == 1)][:,2]
# Array of differences to mean: differences

differences = versicolor_petal_length - np.mean(versicolor_petal_length)


# Square the differences: diff_sq

diff_sq = differences ** 2


# Compute the mean square difference: variance_explicit

variance_explicit = np.mean(diff_sq)

# Compute the variance using NumPy: variance_np

variance_np = np.var(versicolor_petal_length)


# Print the results

print ( variance_explicit, variance_np)

# Print the square root of the variance

print (variance_np ** 0.5)


# Print the standard deviation
print (np.std(versicolor_petal_length))