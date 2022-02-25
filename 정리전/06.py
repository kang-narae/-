import pandas as pd
df=  pd.read_excel('score.xlsx')

print(df.groupby('학교')['학년'].value_counts())    #학교로 그룹 나눠서 학년별로 카운팅
print(df.groupby('학교')['학년'].value_counts(normalize=True))   #학교로 그룹나눠서 학년별로 비중이 어떻게 되는지.
print(df.groupby('학교')['학년'].value_counts(normalize=True).loc['구로고'])   #학교로 그룹나눠서 학년별로 비중이 어떻게 되는지. 그중 '구로고' row를 출력.