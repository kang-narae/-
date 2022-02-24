
import pandas as pd
df= pd.read_excel('score.xlsx', index_col='지원 번호')
df['총합']=df['국어']+df['영어']+df['수학']+df['사회']+df['과학']
# print(df)
df['학년']=[3,3,2,1,1,3,2,2]
# print(df)


df['결과'] = 'fail'
# print(df)

filterdata = df['총합'] >= 400
df.loc[filterdata, '결과'] = 'Pass'  # filterdata가 참인 row들의 결과 컬럼값에 pass를 넣는다.
# print(df)


df.loc['4번', '학교'] = '왕왕고'
# print(df)


# df.drop(columns=['결과'], inplace=True)
# print(df)

# df.drop(columns=['국어','영어','수학'], inplace=True)
print(df)

df.to_excel('score.xlsx')   #엑셀로 저장