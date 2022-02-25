import pandas as pd
df= pd.read_excel('score.xlsx', index_col='지원 번호')
print(df)

print(df.groupby('학년').get_group('디지털고'))
print(df.groupby('학교').get_group('구로고'))

print(df.groupby('학교')['키'].mean())
df.groupby('학교')['키'].size()   #개수

df.groupby('학교')['키'].size()['구로고']   #학교로 나눠서 키의 개수를 보는데 그중 구로고의 것을 본다.


df.groupby('학년').mean().sort_values('키')   #학년으로 그룹 나눠서 컬럼별 평균을 출력하는데, 그걸 '키'의 값으로 정렬한다. 역순으로 하려면 ascending=False.

