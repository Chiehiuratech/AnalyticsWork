import pandas as pd
pd.options.display.max_rows = 2000
data = {
  "calories": [420, 380, 390],
  "duration": [50, 40, 45]
}
# stored = pd.Series(data)
# print(stored["duration"])
stored = pd.DataFrame(data, index=["day 1", "day 2", "day 3"])
stored.corr()
print(stored)
# print(stored.loc[["day 2"]])
# print(pd.options.display.max_rows)