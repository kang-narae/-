import matplotlib.pyplot as plt
import matplotlib 
import pandas as pd

matplotlib.rcParams['font.family'] = 'Malgun Gothic'
matplotlib.rcParams['font.size']=15
matplotlib.rcParams['axes.unicode_minus'] = False

x=[1,2,3]
y=[160,333,232]

plt.xlabel('이름', loc='right', color='red')
plt.ylabel('키', loc='top', color='#ff0000')
plt.yticks([150,200,300,350])   #이게 다 나오는 건 아니고 이 중에서 나옴?
plt.xticks([1,2,3])
plt.title('꺾은선그래프')
plt.plot(x,y,label='범례데이터')          #여기서의 라벨은 plot-선의 라벨.
plt.legend()
plt.show()