import numpy as np
#save
arr = np.array([[1, 72, 3],
                [1, 3, -60],
                [-3, -2, 4]])
np.save('arr.npy', arr) #array can be saved in a file 
#and can be accessed again by: -
load_arr = np.load('arr.npy')
print(repr(load_arr))
