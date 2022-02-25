import pandas as pd
df= pd.read_excel('score.xlsx', index_col='지원 번호')
# print(df)

# print(df.groupby(['학교','학년']).sum())   

# print(df.groupby('학교')['키'].size()['구로고'])

# print(df.groupby('학교').get_group('구로고'))

# print(df.groupby(['학교','학년']).mean())   #1차 학교 2차 학년으로 분류하고 각 컬럼별 평균값을 출력한다.


print(df.groupby('학교')['이름'].count())  #학교로 그룹핑한후, 그룹마다 이름 컬럼의 값이 몇개 있는지를 출력한다. (결측치 뺀 컬럼값 개수 확인할 수 있는 것.)