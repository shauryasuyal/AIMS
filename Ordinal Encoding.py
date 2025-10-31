import pandas as pd

data = { 'Size': ['Small', 'Medium', 'Large', 'Medium', 'Small'],}


df = pd.DataFrame(data)
unique_values = list(df['Size'].unique())
order = {val: i+1 for i, val in enumerate(unique_values)}
encoded = []
for i in range(len(df)):
    val = df.loc[i, 'Size']
    encoded.append(order[val])


df['Size_Encoded'] = encoded
print("\n After encoding - ")
print(df)
