import numpy as np
from numpy.lib.npyio import load

arr = np.array([[0, 72, 3],
                [1, 3, -60],
                [-3, -2, 4]])
sum1 = np.sum(arr)
sum2 = np.cumsum(arr) #returns 1d array
#can use axis argument also

#Concatenation
arr2 = np.array([[-15, 6, 1],
                 [8, 9, -4],
                 [5, -21, 18]])

arr3 = np.concatenate([arr,arr2]) #default axis is zero, length increases along columns 
arr3 = np.concatenate([arr,arr2], axis = 1) #legth increases along rows

