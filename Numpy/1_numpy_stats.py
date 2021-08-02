import numpy as np
arr = np.array([[0, 72, 3],
                [1, 3, -60],
                [-3, -2, 4]])
print(arr.min())
print(arr.max()) #axis can also be defined

#stats
print(np.mean(arr))
print(np.var(arr))
print(np.median(arr)) #axis can be defined here as well