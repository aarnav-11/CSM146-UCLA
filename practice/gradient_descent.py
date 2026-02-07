
import random
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

dataset_url = "Housing.csv"
housing_df = pd.read_csv(dataset_url)

housing_df = housing_df[['price', 'area']] #select just the price and area

# #visualizing the data
# plt.scatter(housing_df['area'], housing_df['price'])
# plt.show()
# print(housing_df.head())
n, m = np.shape(housing_df)

w_tilde = np.zeros(m+1)

for price, area in housing_df:
    w_tilde = w_tilde