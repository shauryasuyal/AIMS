import pandas as pd
import numpy as np

data = {'score':[10, 20, np.nan, 30, np.nan]}
df = pd.DataFrame(data)

print("Write down your preferred type of imputation - mean , median , mode")
choice = input()

values = [df.loc[i, 'score'] for i in range(len(df)) if not pd.isnull(df.loc[i, 'score'])]
fill_val = None
if choice == 'mean':
    fill_val = sum(values) / len(values)
elif choice == 'median':
    sorted_vals = sorted(values)
    n = len(sorted_vals)
    if n % 2 == 1:
        fill_val = sorted_vals[n // 2]
    else:
        fill_val = (sorted_vals[n // 2 - 1] + sorted_vals[n // 2]) / 2
elif choice == 'mode':
    freq = {}
    for val in values:
        freq[val] = freq.get(val, 0) + 1
    fill_val = max(freq, key=freq.get)
else:
    print("Invalid choice, defaulting to mean.")
    fill_val = sum(values) / len(values)
for i in range(len(df)):
    if pd.isnull(df.loc[i, 'score']):
        df.loc[i, 'score'] = fill_val

print(f"After imputation {choice}  -")
print(df)
