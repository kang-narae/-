import matplotlib.pyplot as plt
import matplotlib 
import pandas as pd

matplotlib.rcParams['font.family'] = 'Malgun Gothic'
matplotlib.rcParams['font.size']=15
matplotlib.rcParams['axes.unicode_minus'] = False
df= pd.read_excel('score.xlsx')

label=['강나래', '강태원', '강호림']   #x이름을 라벨이라고 한 거
values=[190,187,184]

plt.bar(label, values, color=['r','b','y'], width=0.1)
plt.show()