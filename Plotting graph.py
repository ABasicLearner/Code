"""
Matplotlib
"""

import matplotlib.pyplot as p
import libraryNumpy as np

#creating data
x = [1, 7, 8, 8, 6]
y = [1, 1, 1, 1, 1]
#plotting lines
p.plot(x, y, label = "line1")
#p.plot(x, y, label = "line2")
p.plot(x, np.sin(x), label = "curve1")
#p.plot(x, np.cos(x), label = "curve2")
p.legend()
p.show()
