
#x1 and x2 are elements of {0,1}
#need to implement nn for x1 AND x2 
import math
import numpy as np

x1 = 0
x2 = 0
b = -30

def sigmoid(x):
    z_bottom = math.exp(-x)
    z = 1/(1+z_bottom)
    z = round(z,4)
    return z

w = [1,20,20]
w = np.transpose(w)
x = [b,x1,x2]

final = np.dot(x,w)

print(sigmoid(final))
