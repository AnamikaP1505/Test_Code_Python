import pandas as pd
import numpy as np


df=pd.read_csv('data.csv',encoding= 'unicode_escape')

df['SalePrice']=df.apply(lambda row: (row['Quantity']*row['UnitPrice']), axis=1)
df1=pd.DataFrame(df.groupby(['CustomerID'])[['Quantity','SalePrice']].sum())
df1.columns=['Total_Quantity','Total_Price']
df1=df1.reset_index()

print(df1.head(10))