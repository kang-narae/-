import matplotlib.pyplot as plt
import matplotlib 
import pandas as pd

matplotlib.rcParams['font.family'] = 'Malgun Gothic'
matplotlib.rcParams['font.size']=15

df= pd.read_excel('score.xlsx')
print(df['이름'])
x=[1,2,3]
y=[2,4,8]  #x와 y축의 데이터

# plot: 선.   bar넣으면 막대기. pie하면 원.
# plt.plot(x,y)
plt.bar(df['이름'], df['키'])
plt.title('라인 그래프- Line graph')
plt.show()