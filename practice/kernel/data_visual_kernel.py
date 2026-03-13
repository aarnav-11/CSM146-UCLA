
import pandas as pd
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import math

data = pd.read_csv("kernel/kernel.csv")
x1 = data["x1"]
x2 = data["x2"]
x3 = pow(x1, 2) + pow(x2, 2)
y = data["label"]

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# class 0
ax.scatter(x1[y == 0], x2[y == 0], x3[y == 0],
           color="blue", label="0")

# class 1
ax.scatter(x1[y == 1], x2[y == 1], x3[y == 1],
           color="red", label="1")

plt.show()