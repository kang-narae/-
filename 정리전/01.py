import pandas as pd
df = pd.read_excel('coding-basic/score.xlsx')
# print(df)

# 컬럼의 데이터 수정
df['SW특기']= df['SW특기'].str.lower() # 소문자
# df['SW특기'].str.upper() # 대문자

print(df)


# 컬럼 추가
df['총합'] = df['국어']+df['영어']+df['수학']+df['과학']+df['사회']
print(df)

