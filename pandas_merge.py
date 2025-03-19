import pandas as pd
df1=pd.DataFrame({'ID':[1,2,3],'Name':['Alice','Bob','Charles']})
df2=pd.DataFrame({'ID':[2,3,4],'Score':[85,90,95]})
merged_df=pd.merge(df1,df2, on='ID',how='inner')
print(merged_df)