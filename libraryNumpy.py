import numpy as np
p = np.array([2, 3, 4, 5])
print(p.dtype)                   # gives datatype of an array
print(p.size)                    # gives number of elements in an array
print(p.shape)                   # gives dimension of an array
print(np.array({22, 33, 44, 55}))

# intrinsic numpy array creation objects(arange, ones, zeros, etc)
print(np.zeros((3, 4)))            # assigns value zero to all the elements in the 3*4 array
print(np.arange(1, 25, 2))        # gives values starting from 1 and ending on 25-1 with a difference of 2
print(np.array(10))               # gives numbers from 0 to 9
print(np.linspace(1, 2, 12))      # gives equally linearly spaced 12 elements between 1 and 2
print(np.linspace(1, 10, 10))     # gives equally linearly spaced 10 elements between 1 and 10
print(np.empty((3, 4)))            # gives 3*4 array(matrix) with random array elements
a = np.array([1, 2, 4, 7, 10, 15])
print(np.empty_like(a))           # gives zero array with same shape as that of array a
print(np.identity(5))             # gives 5*5 identity matrix
print(a.reshape(2, 3))            # reshapes array 'a' from 1*6 to 2*3 array
print(a.ravel())                  # converts n*m array to 1*(n*m) array
print(a.shape)                    # returns (6,)
x = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
ar = np.array(x)
print(ar)
print(ar.sum(axis=0))
print(ar.sum(axis=1))
print(ar.T)
print(ar.flat)
for i in ar.flat:
    print(i)
print()
print(ar.ndim)
print(ar.size)
print(ar.nbytes)                  # total bytes consumed
print(ar.argmax())                # gives index where the maximum element is present in the array
print(ar.argmin())                # gives index where the minimum element is present in the array
print(p.argsort())                # gives indices by which array can be sorted
print(ar.argsort())
print(ar.argmax(axis=0))
print(ar.argmax(axis=1))
ar1 = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9])
ar2 = np.array([1, 0, 0, 0, 1, 0, 0, 0, 1])
print(ar1+ar2)
print(ar1-ar2)
print(ar1*ar2)
print(np.sqrt(ar1))
print(np.sum(ar1))
print(np.max(ar1))
print(np.min(ar1))
print(np.where(ar1 > 5))
print(np.count_nonzero(ar1))
print(np.nonzero(ar1))
ar1[2] = 0
print(np.nonzero(ar1))

import sys
py_ar = [1, 5, 8, 9]
np_ar = np.array(py_ar)
print(np_ar)
print(sys.getsizeof(1) * len(py_ar))
print(np_ar.itemsize * np_ar.size)
