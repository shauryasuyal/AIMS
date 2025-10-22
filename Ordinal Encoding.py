import pandas as pd

data = { 'Size': ['Small', 'Medium', 'Large', 'Medium', 'Small'],
    'Type': ['Caramel', 'Salted', 'Cheese', 'Salted', 'Caramel']
}
df = pd.DataFrame(data)
order = {'Small': 1, 'Medium': 2, 'Large': 3}

encoded = []
for i in range(len(df)):
    size = df.loc[i, 'Size']
    if size in order:
     encoded.append(order[size])

df['Size Encoded'] = encoded
print("\n After encoding - ")
print(df)
