import pandas as pd
from pandas.core import indexing

#initializing pandas
series = pd.Series([1,2,3])
print(repr(series)) #here it is accepting list as argument

#we can pass np array & dictionary as well
series2 = pd.Series({'a':1, 'b':2,'c':3})
print('{}/n'.format(series2))

#we can also use indexing keyword for: -
series3 = pd.Series([1,2,3], index = ['a',0.6,'c'])
print(repr(series3))