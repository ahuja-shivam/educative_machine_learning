import numpy as np
#index is almost same as we do in arrays 

#slicing 
arr = np.array([1, 2, 3, 4, 5])
print(repr(arr[:]))
print(repr(arr[1:]))
print(repr(arr[2:4]))
print(repr(arr[:-1]))
print(repr(arr[-2:])) #Slicing in one d array is same as that of strings and lists

#If one arg is given, then slicing of outer most index is done
arr1 = np.arange(9)
arr1 = np.reshape(arr1,(3,3))
print(repr(arr1[1:])) #print except 1st row

#For multi-dimensional arrays, we can use a comma to separate slices across each dimension.
print(repr(arr1[:, -1])) #print last element(column) of every row
print(repr(arr[:, 1:])) #print except 1st element of each row 
print(repr(arr[0, 1:])) #print except 1st element of first row only 