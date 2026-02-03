import warnings
warnings.filterwarnings("ignore")
import random
import numpy as np
import pandas as pd
pd.set_option('display.max_columns',100)
import seaborn as sns
import matplotlib.pyplot as plt
plt.rcParams['font.size'] = 14
plt.rcParams['figure.figsize'] = (22, 5)
plt.rcParams['figure.dpi'] = 100
import sqlite3
from sklearn.metrics import r2_score, roc_curve, auc
from urllib.request import urlretrieve
from sklearn.preprocessing import MinMaxScaler, OneHotEncoder
from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split

medical_charges_url = 'https://raw.githubusercontent.com/JovianML/opendatasets/master/data/medical-charges.csv'
#storing the data into a dataframe
medical_df = pd.read_csv(medical_charges_url)
print(medical_df.head())

# print(medical_df.shape) #1338 by 7 so 7 features and 1338 datapoints