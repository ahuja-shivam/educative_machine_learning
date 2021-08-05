from numpy import true_divide
import pandas as pd
from pandas.core import series
from pandas.io.orc import read_orc
#the difference between dataframe abd series is that df has indexing for columns as well.

df_1 = pd.DataFrame([[1,2],[3,4]])
print(repr(df_1))

df_2 = pd.DataFrame([[1,2],[3,4]], index = ['r1','r2'], columns=['c1','c2'])
print(repr(df_2))

#passing a dictionary
df_3 = pd.DataFrame({'c1':[1,2,3], 'c2': [3,4,5]}, index=['r1','r2','r3'])
print(repr(df_3))
#for dictionary you can't only pass column argument by default columns are given as dictionary names 

#df_3 = pd.DataFrame({'c1':[1,2,3], 'c2': [3,4,5]}, columns=['r1','r2','r3']) "this won't work"

#upcasting is done as same as numpy 

#appending rows in a dataframe 
df = pd.DataFrame([[1,2],[3,4]])
series1 = pd.Series([0,0], name = 'r3')

df_app = df.append(series1)
print(repr(df_app))

#BY DEFAULT APPEND function adds name as in original series or df
#to counter this: - 

df_app = df.append(series1, ignore_index=True)
print(repr(df_app)) #this will add next row's column in the series in which it was appended 

#dropping data
df_5 = df_3.drop(labels='r1')
print(repr(df_5)) #we can use index (for rows) and columns instead of labels 
