import pandas as pd
df=pd.read_excel('score.xlsx', index_col='지원 번호')
print(df)


# df.drop(columns=['총합'], inplace=True)


# df.drop(index='4번', inplace=True)   #row 삭제
# # print(df)

# df.drop(index=['3번', '6번'] ,inplace=True)  #row 여러개 삭제
# print(df)




# filterdata= df['국어'] < 60

# print(df[filterdata])


# df.drop(index=df[filterdata].index, inplace=True)    #해당조건 만족하는 row의 인덱스를 찾아서 해당 row 삭제
# print(df)


cols= list(df.columns)
# print(cols)
#한개짜리는 컬럼이름이 나오니까 리스트로 묶어줘야함. 슬라이싱은 결과가 리스트로 나오고.
df= df[cols[0:2] + [cols[9]] + cols[2:8] + cols[10:12]+ [cols[8]]]
print(df)

df.to_excel('score.xlsx')
