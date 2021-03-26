# This is Machine Learning program algorithm linear regression model

import numpy as np
import matplotlib.pyplot as plt

x = np.array([1,2,6,4,7,8,9,21,4,32,3,5,6,2])
y = np.array([10,12,16,14,17,18,19,31,6,11,30,15,4,27])

funct1 = np.polyfit(x,y,1)

#plot
plt.plot(x,y, '.')
plt.plot(x, np.polyval(funct1, x),'r-')
plt.show()
# no correlation between x and y