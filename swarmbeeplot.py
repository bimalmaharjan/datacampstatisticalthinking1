from sklearn.datasets import load_iris
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import pandas as pd



#print np.shape(data.data) = (150,4)
#print np.shape(data.target) = (150,)

# first combime data and target arrays
# we can't use np.concatenate without unless there they have shape

def create_panda_dataframe_iris_data(data):
	data_cms = data.data
	target = data.target
	target_names = data.target_names
	# print target_names

	target_reshape = np.reshape(data.target, (len(data.target),1))
	data_and_target =  np.concatenate((data_cms, target_reshape), axis=1)

	df_target_names = pd.DataFrame(target_names,columns=['species'])
	# print df_target_names

	# converting numpy to pandas dataframe
	# df_features doesn't have species name so we will merge with target names to get species names

	df_features = pd.DataFrame(data_and_target, columns=['sepal length (cm)','sepal width (cm)',
		                                       'petal length (cm)', 'petal width (cm)', 'species_id'])
	df = pd.merge(df_features,df_target_names,left_on ='species_id', right_index = True)

	return df

def plot_swarmplot():

	data = load_iris()
	df = create_panda_dataframe_iris_data(data)
	# Create bee swarm plot with Seaborn's default settings
	_ = sns.swarmplot(x = 'species', y='petal length (cm)', data=df)


	# Label the axes
	_ = plt.xlabel('species')
	_ = plt.ylabel('petal length (cm)')


	# Show the plot
	plt.show()


if __name__ == "__main__":
	plot_swarmplot()








