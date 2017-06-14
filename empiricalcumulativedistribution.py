from sklearn.datasets import load_iris
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
data = load_iris()



def ecdf(data):
    """Compute ECDF for a one-dimensional array of measurements."""

    # Number of data points: n
    n = len(data)

    # x-data for the ECDF: x 
    x = np.sort(data)

    # y-data for the ECDF: y
    y = np.arange(1, n+1) / float(n)
    return x, y

def plot_ecdf():

	# Get  petal length
	setosa_petal_length = data.data[np.where(data.target == 0)][:,2]
	versicolor_petal_length = data.data[np.where(data.target == 1)][:,2]
	virginica_petal_length = data.data[np.where(data.target == 2)][:,2]

	# Compute ECDF for setosa, versicolor, virginica data:
	x_set, y_set = ecdf(setosa_petal_length)
	x_vers, y_vers = ecdf(versicolor_petal_length)
	x_virg, y_virg = ecdf(virginica_petal_length)

	# Generate plot
	# Plot all ECDFs on the same plot
	_ = plt.plot(x_set, y_set, marker ='.', linestyle ='none')
	_ = plt.plot(x_vers, y_vers, marker ='.', linestyle ='none')
	_ = plt.plot(x_virg, y_virg, marker ='.', linestyle ='none')	
	
	# Make the margins nice
	_ = plt.margins(0.02)

	# Annotate the plot
	plt.legend(('setosa', 'versicolor', 'virginica'), loc='lower right')
	_ = plt.xlabel('petal length (cm)')
	_ = plt.ylabel('ECDF')
	# Display the plot
	plt.show()

if __name__ == "__main__":
	
	#plot ECDF
	plot_ecdf()
	


