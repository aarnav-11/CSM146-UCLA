import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import math
import sklearn as sk

#Load the data
data = pd.read_csv("single_feature_data.csv")
x = data[["hours_studied"]]
y = data["passed"]
rows_size, columns_size = np.shape(data)

# def plot_data(x,y):
#     plt.scatter(x,y)
#     plt.show()

# plot_data(x,y)

def knn(x,y,k,val):
    knn = sk.neighbors.KNeighborsClassifier(n_neighbors = k)
    knn.fit(x,y)
    return_val = knn.predict([[val]])
    return return_val

# knn_val = knn(x,y,3,50)
# print(knn_val)



