import numpy as np 
import pandas as pd 

df= pd.read_html ("https://www.kaggle.com/datasets/antimoni/bone-tumor?resource=download") 
df=df.dropna()
df=df.drop_duplicates()
date_columns= ['grade','sex','age'] 
df[date_columns] = df[date_columns].apply(pd.to_datetime)

df2= df.set_index('grade').groupby('grade').mean()
df3= df.set_index('sex').groupby('sex').mean()
df4 = df.set_index('age').groupby('age').mean()

print(df2,df3,df4)


                  