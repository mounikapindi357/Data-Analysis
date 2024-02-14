# -*- coding: utf-8 -*-
"""DAP.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1tMnA6OzQiGV5BBGfURrn3OMFXc0ehNdY
"""

#import pandas

import pandas as pd
a=['Thiru','hafiza','pravalli','Mouni','Siri']
r=pd.Series(a,index=[89,59,65,78,90])
print(r)
d=pd.read_csv("/content/WHO_PM.csv")
print(d)
df=pd.read_csv("/content/WHO_PM.csv",sep=" , ")
print(df)
print(df.loc[1])

import pandas as pd
d=pd.read_csv("/content/WHO_PM.csv")
mv=d['min'].mean()
print(mv)
d=d.fillna(mv)
print(d)

import numpy as np
arr=np.array([1,2,3,4,5])
print(arr)
a=np.zeros((3,3),dtype=int)
print(a)
b=np.ones((2,2),dtype=int)
print(b)
c=np.arange(10)
print(c)
#array manipulation
d=arr.reshape(5,1)
print(d)
sliced_arr=arr[2:4]
print(sliced_arr)
arr1=np.array([1,2,3,4,5])
arr2=np.array([6,7,8,9,10])
print(arr1+arr2)
#broadcast
print(arr1+3)
w=np.stack(arr1+arr2)
print(w)
y=np.array([1,2,3,4,5,6])
z=np.split(y,3)
print(z)
n=np.array([[1,2,3],[4,5,6]])
b=n.T
print(b)
g=np.array([[1,2],[4,5]])
h=np.array([[4,7],[1,6]])
x=np.dot(g,h)
print(x)
u=np.linalg.eig(x)
print(u)
#dot
m=np.array([[1,2,3],[6,2,4]])
n=np.array([[2,5,3],[1,8,4]])
v=np.sum(m,axis=0) #rows
u=np.sum(m,axis=1)
print(v)
print(u)
#statistical operations
n=np.array([1,2,3,4,5])
m=np.mean(n)
print(m)
v=np.median(n)
print(v)
u=np.var(n)
print(u)
w=np.std(n)
print(w)
data=np.loadtxt("/content/data.txt",dtype=int)
data=np.savetxt("/content/date.txt",data)
print(data)

import matplotlib.pyplot as plt
a=np.array([1,2,3,4])
plt.plot(a)

import pandas as pd
e=pd.read_excel("/content/blinkit_retail.xlxs")
print(e)
d=pd.read_excel("/content/blinkit_retail.xlxs",sheet_name=1)
print(d)

import pandas as pd
d=pd.read_csv("/content/WHO_PM.csv")
print(d)
d.shape
d=pd.read_csv("/content/WHO_PM.csv")

d=pd.read_csv("/content/WHO_PM.csv")
t=d.tail(10)
for i in range(12,2,-1):
  d.drop([i],axis=0,inplace=True)
t.to_csv("manual_testing.csv")
d=pd.read_csv("/content/manual_testing.csv")
print(d)
print(d.groupby(['Indicator'])['ValueType'].count())

from google.colab import drive
drive.mount('/content/drive')

d=pd.read_csv("/content/WHO_PM.csv")
d=d.drop_duplicates()
print(d)

import numpy as np
import matplotlib.pyplot as plt
runs=np.array([100,50,91,78,89,25,34,19,9,10])
w=np.array([1,0,2,0,3,7,8,9,7,5])
plt.plot(runs,w,color='orange')
plt.title('IndvsAus_score')
plt.show()

import numpy as np
import matplotlib.pyplot as plt
#Genereate array of 200 values b/w -pi & pi
tigar=np.linspace(-2*np.pi, 2*np.pi, 100)
print(tigar)
plt.scatter(tigar,np.sin(tigar),color='black')
plt.title("sin(x)")
plt.show()

import numpy as np
import matplotlib.pyplot as plt
#creating x
overs=np.arange(5,50,5)
overs_a=np.arange(5,30,5)
#creating y
runs_i=np.array([25,51,84,131,160,189,220,250,267])
runs_a=np.array([15,41,94,110,151])
wickets=np.array([12,32,96])
#plotting
plt.subplot(2,1,2)
plt.plot(overs,runs_i,color='blue',label='India')
plt.legend(loc='best')
plt.subplot(2,1,1)
plt.plot(overs_a,runs_a,color='yellow',label='Aus')
plt.subplot(2,1,1)
#combining two graphs
plt.legend(loc='best')
#displaying the final graph
plt.show()

import matplotlib.pyplot as plt
a=[230,560,780,127,128]
b=[200,160,270,127,400]
years=[1,2,3,4]

profit_a=[(a[i]-a[i-1]) for i in range(1,len(a))]
profit_b=[(b[i]-b[i-1]) for i in range(1,len(b))]
plt.subplot(2,1,2)
plt.plot(years,profit_a,color='hotpink',linewidth='3',label='CompanyA',marker='>',ms='15',mec='k')
plt.subplot(2,1,1)
plt.plot(years,profit_b,color='black',linestyle='dotted',label='CompanyB',marker='H')

a=np.array([25,60,5,10])
labe=["AIML","Python","Pandas","Numpy"]
plt.pie(a,labels=labe)
plt.show()

#explode
a=np.array([25,60,5,10])
labe=["AIML","Python","Pandas","Numpy"]
col=['blue','green','pink','yellow']
explo=[0.2,0,0,0]
plt.pie(a,labels=labe,explode = explo,startangle = 180,colors=col,textprops={'fontsize':20})
plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
d=pd.read_csv("/content/jan_month_temp.csv")
print(d)

average_temperature = d['temp'].mean()
highest_temperature = d['temp'].max()
lowest_temperature = d['temp'].min()
threshold=27
days_above_threshold=d[d['temp']>threshold].shape[0]


print("Average temperature for the month:",average_temperature)
print("Highest temperature for the month:",highest_temperature)
print("Lowest temperature for the month:",lowest_temperature)
print("Number of days temperature exceeded",threshold,"degree Celsius:",days_above_threshold)

d.plot(kind='line',color='black')
plt.title('Jan month temp')
plt.xlabel('days')
plt.ylabel('temp')

!pip install seaborn

import seaborn as sns
import matplotlib.pyplot as plt
#load eg dataset
tips=sns.load_dataset("tips")
#create a scatter plot
sns.violinplot(x="total_bill",y="tip",data=tips)
plt.title("Scattter plot of total bill vs tip")
plt.xlabel("Total bill ($)")
plt.ylabel("Tips($)")
plt.show()

import seaborn as sns
import matplotlib.pyplot as plt
#load eg dataset
flights_data=sns.load_dataset("flights")
print(flights_data.tail())
flights_pivot=flights_data.pivot_table(index='month',columns='year',values='passengers')
sns.heatmap(flights_pivot,cmap='coolwarm',annot=True,fmt='d')
plt.title=("Flights data-heatmap")
plt.xlabel("Year")
plt.ylabel("month")
plt.show()

import seaborn as sns
import matplotlib.pyplot as plt
iris=sns.load_dataset("iris")
print(iris.tail())
correlation_matrix=iris.corr()
sns.heatmap(correlation_matrix,annot=True,cmap="coolwarm")
plt.title("Correlation heatmap of iris dataset")
plt.show()