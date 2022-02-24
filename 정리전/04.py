import pandas as pd
df= pd.read_excel('score.xlsx', index_col='지원 번호')
# print(df)

df.replace({'구로고':'영등포고'}, inplace=True)
# print(df)


# print(df.columns)
# print(df[df.columns[0]])  
# print(df['이름'])

df.rename(columns={'이름':'name', '학교':'school'}, inplace=True)
# print(df)

# df.columns=['name', 'school',...] 개수맞춰서


# df['학교'] = df['학교']+'등학교'   #컬럼명 변경


df['음악']=100
# print(df)

# df['키'] =df['키'].astype(str) + 'cm'
# print(df)


def add_cm(height):
    return str(height)+'cm'

df['키'] = df['키'].apply(add_cm)
print(df)