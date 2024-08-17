from statistics import correlation
from turtle import color
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

My_File = pd.read_csv("qc_public-sector_nga.csv")
frame =pd.DataFrame(My_File)
frame=frame.drop(index=[0])
frame= frame.head(5)
sort= frame.sort_values('Year', ascending=True)
sort= frame.sort_values('Value', ascending=True)
selectcolumns =frame[['Year','Value']]
frame2 = pd.DataFrame(selectcolumns)
type = frame2['Year']= frame2['Year'].astype(int)
x = frame2['Value']= frame2['Value'].astype(float)
# I = frame2.reset_index(drop=True)
# print(type)

plt.hist(frame2['Year'],frame2['Value'], bins='auto', color=['blue','pink'],alpha = 0.7 )
plt.title("Public Sector Data Set",size=40, color="cyan")
plt.xlabel('Value', size= 15,color="purple" )
plt.ylabel('Year',size=15,color="purple")
# plt.grid()
# plt.subplot(3,2,1)

# plt.plot(frame2['Value'], frame2['Year'],'*:r')
# plt.title("Public Sector Data Set",size=40, color="cyan")
# plt.xlabel('Value', size= 15,color="purple" )
# plt.ylabel('Year',size=15,color="purple")
# plt.grid()
# plt.subplot(3,2,2)

# plt.bar(frame2['Value'], frame2['Year'], color= "Hotpink")
# plt.title("Public Sector Data Set",size=40, color="cyan")
# plt.xlabel('Year', size= 15,color="purple" )
# plt.ylabel('Value',size=15,color="purple")
# plt.grid()
# plt.subplot(3,2,3)

# plt.pie(frame2['Year'],autopct='%1.1f%%')
# plt.title("Public Sector Data Set",size=40, color="cyan")
# plt.subplot(2,2,4)
# plt.legend(frame2)
plt.show()
# corr1 = frame2['Value']
# corr2 = frame2['Year']
# corre = corr1.corr(corr2) 
# print(corre)
