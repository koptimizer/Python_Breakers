import pandas as pd
pd.options.mode.chained_assignment = None

df = pd.read_excel("남북한발전전력량.xlsx")

new_df = df[:]
new_df.drop([3,4,8], axis = 0, inplace = True)
new_df.index = [0,1,2,3,4,5]

for items in range(len(new_df.columns)-2) :
    new_df.iloc[0][items+2] = new_df.iloc[1][items+2] + new_df.iloc[2][items+2]
    new_df.iloc[3][items+2] = new_df.iloc[4][items+2] + new_df.iloc[5][items+2]

print(new_df)
writer = pd.ExcelWriter("남북한발전전력량2.xlsx")

df.to_excel(writer, sheet_name = "sheet 1")
new_df.to_excel(writer, sheet_name = "sheet 2")
writer.save()