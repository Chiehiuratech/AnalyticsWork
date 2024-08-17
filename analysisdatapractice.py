from array import array
from tokenize import Name
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
data = pd.read_csv("qc_public-sector_nga.csv")
frame = pd.DataFrame(data)
data= frame.head(10)
data=data.drop(index=[0])
# selectcolum = data[["Year","Value"]]
selectcolum=np.array(data[["Year","Value"]])
frame2= pd.DataFrame.to_numpy(selectcolum)
# convert = tuple(frame2[['Year','Value']].apply(tuple, axis=1))
# convert = np.array(selectcolum)
# tuples = [tuple(x) for x in frame2.to_numpy()]
# [tuple(x) for x in frame2.to_records(index=False)]
# print(frame2)
plt.plot(frame2)
plt.show()











# print(data1.dtypes)
# newdata1 = data1.convert_dtypes(infer_objects=True)
# print(newdata1.dtypes)
# print(data1.shape)
# data1.set_index("Year",inplace=True)
# data1.replace('#','', regex=True)
# data1.replace('+','',regex=True)
# data1 = data1.convert_dtypes("convert_floating")
# data1.info(verbose=False)