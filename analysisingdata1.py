from ast import Store
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
data = pd.read_csv("qc_public-sector_nga.csv")
data.loc[0,"Country ISO3"]="country name"
data.loc[0,"Year"]="year"
data.loc[0,"Indicator Code"] = "indicator code"
data.loc[0,"Value"] = "Value num"
data=pd.DataFrame(data)
data1 = tuple(data)
data1=np.array(["Country ISO3","Year","Indicator Code","Value"])
# data1["Country ISO3"] = pd.to_numeric(data1["Country ISO3"], errors="coerce")
data=data.head(10)
# print(data)
plt.plot(data1, marker="*", color="r")
# plt.pie(data1)
plt.show()
# print(data.duplicated().to_string())