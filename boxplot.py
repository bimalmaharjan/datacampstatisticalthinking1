from sklearn.datasets import load_iris
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import pandas as pd
import swarmbeeplot as swbp



def plot_box_plot():
	data = load_iris()
	df = swbp.create_panda_dataframe_iris_data(data)

	# Create box plot with Seaborn's default settings
	_ = sns.boxplot(x='species', y = 'petal length (cm)', data=df)


	# Label the axes

	_ = plt.xlabel('species')
	_ = plt.ylabel('petal length (cm)')



	# Show the plot

	plt.show()


if __name__ == "__main__":
	plot_box_plot()

