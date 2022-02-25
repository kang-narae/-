import pandas as pd
df= pd.read_excel('pandas_code.xlsx')
# print(df)

print(df.groupby(['학교']).mean())
print(df.groupby('학교')['이름','sw특기'].count())
