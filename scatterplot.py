from sklearn.datasets import load_iris
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
data = load_iris()

versicolor_petal_length = data.data[np.where(data.target == 1)][:,2]
versicolor_petal_width = data.data[np.where(data.target == 1)][:,3]

sns.set()

# Make a scatter plot

_ = plt.plot(versicolor_petal_length,versicolor_petal_width, marker ='.', linestyle= 'none') 


# Set margins
_ = plt.margins(0.02)


# Label the axes
_ = plt.xlabel('petal length')
_ = plt.ylabel('petal width')


# Show the result

plt.show()