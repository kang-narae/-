import matplotlib.pyplot as plt
import matplotlib 
import pandas as pd

matplotlib.rcParams['font.family'] = 'Malgun Gothic'
matplotlib.rcParams['font.size']=15
matplotlib.rcParams['axes.unicode_minus'] = False
df= pd.read_excel('score.xlsx')



day=[1,2,3]
az=[2,4,8] #단위만명
pfizer=[5,1,3]
modrena=[1,2,5]


plt.plot(day,az, label='az', marker='o', ms=7)
plt.plot(day,pfizer, label='az', marker='o', ms=7)
plt.plot(day,modrena, label='az', marker='o', ms=7)
plt.legend(ncol=3)
plt.show()