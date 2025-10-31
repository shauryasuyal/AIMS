import pandas as pd

data = {'Colour':['Red','Blue','Green','Blue','Red']}
df = pd.DataFrame(data)
column_name = 'Colour'
unique_vals = df[column_name].unique()
encoded_df = pd.DataFrame()

for val in unique_vals:
    col_data = []
    for i in range(len(df)):
        if df.loc[i, column_name] == val:
            col_data.append(1)
        else:
            col_data.append(0)
    encoded_df[column_name + '_' + val] = col_data
final_df = pd.concat([df, encoded_df], axis=1)
print("After one hot encoding - ")
print(final_df)
