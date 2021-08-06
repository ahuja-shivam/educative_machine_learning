
import pandas as pd
df = pd.DataFrame({'c1': [1, 2], 'c2': [3, 4],
                   'c3': [5, 6]}, index=['r1', 'r2'])

print(repr(df['c1'])) #this will return a series (single brackets)
print(repr(df[['c1']])) #this will return a Dataframe 

print(repr(df[['c1','c2']]))

#slicing 

print(repr(df[0:2])) #this will slice the rows can use lables
#df['r1'] error

#using iloc and loc
print('{}\n'.format(df.iloc[1])) #access single row by intiger
print('{}\n'.format(df.loc['r1'])) #access single row by label 

df.loc[['r1', 'r3'], 'c2'] = 0
print('{}\n'.format(df))


