""" Patient's inflammation analysis for day 1 """

import numpy as np
import matplotlib.pyplot as plt

data = np.loadtxt(fname='data/inflammation1.csv', delimiter=',')

#Finding the dimensions of the data
dimensions=shape(data)

print(data)

image-1=plt.plot(data)

plt.show(image-1)