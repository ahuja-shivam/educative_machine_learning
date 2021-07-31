import numpy as np

#arithemtic_operation(linear)
arr = np.arange(4)
arr2 = arr + 2
arr2 = arr/2
arr2 = arr//2 #Etc more operations, each element will be calculated for every operation

#We can create our own function as well e.g: -
def ftc(a):
    return (5/9)*(a-32) #converts temprature f to c
arr[0] = 32
arr[1] = -40
cel = ftc(arr)
#print(repr(cel))

#Non linear function, e.g np.exp, np.log, np.log10, np.log2, np.exp2
arr = np.arange(4)
print(np.exp(arr))
print(np.log2(arr))
print(np.power(4,arr)) # 4 power elements of matrix

#Matrix multiplication 
arr1 = np.array([[1,2,3],[3,2,1]])
arr2 = np.array([[1,2],[2,3],[3,4]])
matmul1 = np.matmul(arr1,arr2)
matmul2 = np.matmul(arr2,arr1)
'''matmul3 = np.matmul(arr2,arr2)''' #this case will give error as matmul[(2*3)(2*3)] isn't defined 
print(matmul1)
print(matmul2)  