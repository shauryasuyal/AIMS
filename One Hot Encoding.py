import pandas as pd

data = {'Colour':['Red','Blue','Green','Blue','Red']}
df = pd.DataFrame(data)
colours = df['Colour'].unique()

newdf = pd.DataFrame()
for c in colours:
    col = []
    for i in range(len(df)):
        if df.loc[i,'Colour'] == c:
            col.append(1)
        else:
            col.append(0)
    newdf['Colour '+c] = col

final = pd.concat([df,newdf],axis=1)
print("After one hot encoding - ")
print(final)
