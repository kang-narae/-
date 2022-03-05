import matplotlib.pyplot as plt
import matplotlib 
import pandas as pd



plt.title('row 개수 달라도 되는지')

x1=[1,2,3,4,5,6,7,8,9,10]
x2=[1,3,5,7,9]  
y1=[10,20,30,40,50,60,70,80,90,100]
y2=[30,50,30,50,90]
plt.plot(x1,y1,label='row가 10개')
plt.plot(x2,y2, label='row가 5개')
plt.legend()

plt.show()