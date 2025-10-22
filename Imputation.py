import pandas as pd
import numpy as np

data = {'score':[10, 20, np.nan, 30, np.nan]}
df = pd.DataFrame(data)

sumval = 0
count = 0
for i in range(len(df)):
    if not pd.isnull(df.loc[i, 'score']):
        sumval += df.loc[i, 'score']
        count += 1
mval = sumval / count
for i in range(len(df)):
    if pd.isnull(df.loc[i, 'score']):
        df.loc[i, 'score'] = mval

print("After imputation ( mean )- ")
print(df)
