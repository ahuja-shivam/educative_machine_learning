import numpy as np

#randint function, this function makes an array of randomly added intigers
random_arr =np.random.randint(5) #default argument is max value
random_arr2 = np.random.randint(5, high = 6,size=(2,2)) #highest value set to 6, then default value will bw lowest one 

#utility function 
np.random.seed(1)
print(np.random.randint(5))

np.random.seed(2)
print(np.random.randint(5))

np.random.seed(1)
print(np.random.randint(5)) #seed is used to access same random values 

#shuffle 
vec = np.arange(5)
print(vec)
np.random.shuffle(vec)
print(vec)

#uniform is the functions to access random distributions 
vec2 = np.random.uniform(size = 3) #default range is [0,1)
print(vec2)
print(repr(np.random.uniform(low=-3.4, high=5.9, size=(2, 2)))) #here max and min values are defined 
print(repr(np.random.normal(loc=-2.4, scale=4.0, size=(2, 2)))) #loc means mean and scale is std deviation and normal refers to normal guassian plane

#Custopm sampling 

vec3 = ['a','b','c''d']
print(np.random.choice(vec3, sixe = 2, p = [0.3,0.3,0.3,0.1])) #p is probabilityy