from sklearn.datasets import load_iris
import matplotlib.pyplot as plt
import numpy as np
data = load_iris()

versicolor_petal_length = data.data[np.where(data.target == 1)][:,2]
versicolor_petal_width = data.data[np.where(data.target == 1)][:,3]

# Compute the covariance matrix: covariance_matrix

covariance_matrix = np.cov(versicolor_petal_length, versicolor_petal_width)


# Print covariance matrix

print ( covariance_matrix)


# Extract covariance of length and width of petals: petal_cov

petal_cov = covariance_matrix[0,1]


# Print the length/width covariance

print(petal_cov)

def pearson_r(x, y):
    """Compute Pearson correlation coefficient between two arrays."""
    # Compute correlation matrix: corr_mat
    
    corr_mat = np.corrcoef(x,y)

    print corr_mat


    # Return entry [0,1]
    return corr_mat[0,1]

# Compute Pearson correlation coefficient for I. versicolor: r

r = pearson_r(versicolor_petal_length, versicolor_petal_width)

# Print the result

print (r)

