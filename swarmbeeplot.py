from sklearn.datasets import load_iris
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import pandas as pd
data = load_iris()


#print np.shape(data.data) = (150,4)
#print np.shape(data.target) = (150,)

# first combime data and target arrays
# we can't use np.concatenate without unless there they have shape

data_cms = data.data
target = data.target
target_reshape = np.reshape(data.target, (len(data.target),1))
data_and_target =  np.concatenate((data_cms, target_reshape), axis=1)

# converting numpy to pandas dataframe

df = pd.DataFrame(data_and_target, columns=['sepal length (cm)','sepal width (cm)',
	                                       'petal length (cm)', 'petal width (cm)', 'target flower'])

print df





