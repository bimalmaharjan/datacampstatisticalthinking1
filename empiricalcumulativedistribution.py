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
    
def plot_ecdf(x_vers,y_vers):
	# Generate plot
	plt.plot(x_vers,y_vers, marker='.',linestyle='none')
	# Make the margins nice
	_ = plt.margins(0.02)


	# Label the axes
	_ = plt.xlabel('versicolor_petal_length')
	_ = plt.ylabel('ECDF')

	# Display the plot
	plt.show()

if __name__ == "__main__":
	
	# Get versicolor petal length
	versicolor_petal_length = data.data[np.where(data.target == 1)][:,2]
	print versicolor_petal_length

	# Compute ECDF for versicolor data: x_vers, y_vers
	x_vers, y_vers = ecdf(versicolor_petal_length)

	#plot ECDF
	plot_ecdf(x_vers,y_vers)
	


