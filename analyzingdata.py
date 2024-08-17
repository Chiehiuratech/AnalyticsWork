import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
df=pd.read_csv("qc_public-sector_nga.csv")
df=pd.DataFrame(df)
data1=tuple(df)
df=df.drop(index=[0])
# data1=np.array([["Year"]])
# data2 =np.array([["Value"]])
# data1=df.head(5)
# data2 =df.head(5)
# plt.xlabel("Value")
# plt.ylabel("Year")
print(data1)
# plt.plot(data1,data2)
# plt.show()
