import numpy as np

# create numpy array and dtype
arr = np.array([[1,4,5], [6,7,8]], dtype=np.float32)
print(repr(arr))

# upcasting: string > float > int == all string
arr2 = np.array([3, 5.6, 'shivam'])
print(repr(arr2))