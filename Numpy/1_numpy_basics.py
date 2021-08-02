import numpy as np
from numpy.core.fromnumeric import reshape
from numpy.core.numeric import identity
from numpy.lib.stride_tricks import as_strided

#ranged array
arr = np.arange(7)
print(repr(arr), arr.dtype)
arr = np.arange(2,8,2)
print(repr(arr)) #here last element is not included, works same as range function 

#linspace function, last element is included by default 
arr1 = np.linspace(5,11,num=4) #num here tells the number of total elements in array
print(repr(arr))

arr1 = np.linspace(5,11,num=4,endpoint=False) #now the last element will not be included
print(repr(arr))

#reshaping the data
#(reshape function)
arr2 = np.arange(8)
reshaped = np.reshape(arr2,(2,4)) #2*4 matrix will be created here
print(repr(arr2),repr(reshaped))
reshaped2 = np.reshape(arr2,(-1,2,2)) #here -1 is replaced by the required value by the compiler. -1 can be assigned to only one dim
print('New shape: {}'.format(reshaped2.shape)) #thhis prints the sahpe of array

#flatten func
arr3 = reshaped.flatten()#it converts the array in 1-d array
print(repr(arr3))

#transposing a matrix
matrix1 = np.transpose(reshaped)
print(repr(matrix1))

matrix2 = np.transpose(reshaped2, axes=(1,2,0)) #here axis is defined to transpose a 3-d matrix
print(repr(matrix2))

#zeros and ones
#matrix can intially be filled with values zero or one usning: -
arr_z=np.zeros(16)
arr_z = np.reshape(arr_z,(4,4))
print("final step")
print(arr_z)

arr_o = np.ones(16)
#and so on dtype in both case float 64