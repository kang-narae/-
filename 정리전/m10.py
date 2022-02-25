import matplotlib.pyplot as plt
import matplotlib 
import pandas as pd

matplotlib.rcParams['font.family'] = 'Malgun Gothic'
matplotlib.rcParams['font.size']=15
matplotlib.rcParams['axes.unicode_minus'] = False
df= pd.read_excel('score.xlsx')


plt.plot(df['이름'], df['국어'], label='국어')
plt.plot(df['이름'], df['영어'], label='영어')
plt.legend(loc='upper left')
plt.xlabel('이름')
plt.ylabel('점수')
# plt.show()   이걸 지워야 그래프저장이된다. 오ㅐ지 ? ?? ?
plt.savefig('graph2.png')   #??? 왜 흰페이지나오지?


# plt.show () 로 표시된 이미지를 닫으면 이미지가 닫히고 메모리에서 해제됩니다.
#show 를 호출하기 전에 savefig 및 savetxt 를 호출해야합니다.

 