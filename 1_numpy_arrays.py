import numpy as np

# create numpy array and dtype
arr = np.array([[1,4,5], [6,7,8]], dtype=np.float32)
print(repr(arr))


# upcasting: string > float > int == all string
arr2 = np.array([3, 5.6, 'shivam'])
print(repr(arr2))


# copy function
arr3 = np.array([1,2,3,4])
a = arr3 #changes in a will change arr3 as well
a[0] = 10
print(repr(arr3))
b = arr3.copy()
b[1] = 101
print(repr(arr3)) #copy function makes the copy


#Casting and arr.dtype for checking data type
arr4 = np.array([4,5,7])
print(arr4.dtype)
arr4 = arr4.astype(np.float32)
print(arr4.dtype)

#NaN, used when we don't want value on perticular index
arr5 = np.array([np.nan,2,3,4],dtype=np.int32)#'''Now this will give error''' as NaN is float type and can't be converted in int


#infinity 
print(np.inf > 100000) #noe this will return true
arr = np.array([1,5,np.inf], dtype = np.int32) # now this will return error as inf is float