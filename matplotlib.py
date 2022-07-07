import matplotlib.pyplot as plt
import numpy as np
X = np.array([1, 2, 3])
Y = np.array([5, 8, 6])
plt.plot(X,Y,label="line",linestyle="-.")
plt.legend()
#plt.fill_between(X,Y)
plt.show()