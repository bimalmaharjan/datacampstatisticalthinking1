from sklearn.datasets import load_iris
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import empiricalcumulativedistribution as ecdf
data = load_iris()

versicolor_petal_length = data.data[np.where(data.target == 1)][:,2]

# Compute the mean: mean_length_vers
mean_length_vers = np.mean(versicolor_petal_length)

# Print the result with some nice formatting
print('I. versicolor:', mean_length_vers, 'cm')

# Specify array of percentiles: percentiles
percentiles = np.array([2.5,25,50,75,97.5])


# Compute percentiles: ptiles_vers
ptiles_vers= np.percentile(versicolor_petal_length, percentiles)

# Print the result
print (ptiles_vers)

x_vers,y_vers = ecdf.ecdf(versicolor_petal_length)

# Plot the ECDF
_ = plt.plot(x_vers, y_vers, '.')
plt.margins(0.02)
_ = plt.xlabel('petal length (cm)')
_ = plt.ylabel('ECDF')

# Overlay percentiles as red diamonds.
_ = plt.plot(ptiles_vers, percentiles/100, marker ='D', color='red',
         linestyle='none')

# Show the plot

plt.show()

