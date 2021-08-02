import numpy as np
from numpy.core.arrayprint import array2string
#Filtering deals woth boolean value 
arr = np.array([[0, 2, 3],
                [1, 3, -6],
                [-3, -2, 1]])
print(repr(arr == 3))

#np.nan means not a number
arr2 = np.array([[0, 2, np.nan],
                [1, np.nan, -6],
                [np.nan, -2, 1]])
print(repr(np.isnan(arr2)))

print(repr(np.where(arr == 3))) #return an array of index
print(repr(np.where(arr == 3, 5, 0))) #fills 5 where true and 0 where falls

# np.any is like or and np.all is like and, returns single bool value
print(repr(np.any(arr > 0, axis=0)))

# returns array if axis is defined,like axis is defined in argmin argmax
