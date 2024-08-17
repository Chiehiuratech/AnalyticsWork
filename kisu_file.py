import pandas as pd
dataset=pd.read_csv("qc_public-sector_nga.csv")
dataset.loc[0, "Country ISO3"]="COUNTRY'S CODE"
dataset.loc[0, "Year"]="DATE\YEAR"
dataset.loc[0, "Indicator Code"]="CODE"
dataset.loc[0, "Value"]=" VALUE NUM"
print(dataset.duplicated(subset=["Year"]).to_string())
print(dataset.to_string())