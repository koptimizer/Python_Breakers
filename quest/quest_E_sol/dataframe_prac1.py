import pandas as pd
pd.options.mode.chained_assignment = None

# 1-1
# df = pd.read_excel("corona.xlsx")
# df['한국'] = [1,1,2,3,4,7]
# df.to_excel('corona.xlsx')

# # 2-1
# df = pd.read_excel("corona.xlsx")
# df.drop(df.columns[0], axis =1, inplace = True)
# df1 = df[:]
# df1.drop(['타국','한국'], axis = 1, inplace=True)
# df2 = df[:]
# df2.drop(['중국','한국'], axis = 1, inplace=True)
# df3 = df[:]
# df3.drop(['중국','타국'], axis = 1, inplace=True)

# writer = pd.ExcelWriter("corona.xlsx")
# df.to_excel(writer, sheet_name='sheet1')
# df1.to_excel(writer, sheet_name='sheet2')
# df2.to_excel(writer, sheet_name='sheet3')
# df3.to_excel(writer, sheet_name='sheet4')
# writer.close()