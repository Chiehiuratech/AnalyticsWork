import pandas as pd
# pd.options.display.max_rows = 2060
data_set = pd.read_csv("public-sector_nga.csv")
data = pd.read_csv("qc_public-sector_nga.csv")
# print(data_set)
print(data.to_string())
# print(data.head(5))
# print(data.tail(5))
# print(data_set.head(10).to_string)
# stored = data_set['Indicator Name'].to_string
# print("show info of my data",data_set.info())
# print(stored)
