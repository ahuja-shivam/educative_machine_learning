import pandas as pd
from pandas.core.reshape.concat import concat 


#combining using concat
df1 = pd.DataFrame({'c1':[1,2], 'c2':[3,4]},index=['r1','r2'])
df2 = pd.DataFrame({'c1':[5,6], 'c2':[7,8]},index=['r1','r2'])
df3 = pd.DataFrame({'c1':[5,6], 'c2':[7,8]})

print(pd.concat([df1,df2],axis=1))
print(pd.concat([df1,df2,df3], axis = 1))
print(pd.concat([df1,df2,df3], axis = 0))
print(pd.concat([df1,df3], axis = 1))

#combining using merge
mlb_df1 = pd.DataFrame({'name': ['john doe', 'al smith', 'sam black', 'john doe'],
                        'pos': ['1B', 'C', 'P', '2B'],
                        'year': [2000, 2004, 2008, 2003]})
mlb_df2 = pd.DataFrame({'name': ['john doe', 'al smith', 'jack lee'],
                        'year': [2000, 2004, 2012],
                        'rbi': [80, 100, 12]})
df_merge = pd.merge(mlb_df1,mlb_df2)
print(df_merge) #merge will merge the attributes of those elements which are same 
#e.g john doe(2000) is same is both DFs so are merged together 

                    