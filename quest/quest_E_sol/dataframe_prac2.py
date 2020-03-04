import pandas as pd

# 2-1
# df = pd.read_csv('auto-mpg.csv')
# df.columns = ['mpg(연비)', 'cylinders(실린더 수)', 'displacement(배기량)', 'horsepower(출력)', 'weight(차중)', 'acceleration(가속능력)', 'model_year(출시년도)', 'origin_number(제조국 번호)', 'name(모델 명)']
# df.to_excel('auto-mpg-2.xlsx')

# # 2-2
# df = pd.read_excel('auto-mpg-2.xlsx')
# print(df[['mpg(연비)', 'weight(차중)']].mean())

# # 2-3
# df = pd.read_excel('auto-mpg-2.xlsx')
# print(df[['mpg(연비)', 'horsepower(출력)']].std())

# # 2-4
# df = pd.read_excel('auto-mpg-2.xlsx')
# print(df.info())
# horsepower는 데이터 중 ?가 포함되서 object 타입이므로 문자열이라 실수의 연산형 통계에는 이용될 수 없다.

# 2-5
df = pd.read_csv('auto-mpg.csv')
df.columns = ['mpg(연비)', 'cylinders(실린더 수)', 'displacement(배기량)', 'horsepower(출력)', 'weight(차중)', 'acceleration(가속능력)', 'model_year(출시년도)', 'origin_number(제조국 번호)', 'name(모델 명)']

# 새 데이터프레임을 할당하고 sort_values를 이용해 열을 기준으로 내림차순 정렬한다)
new_df = df.sort_values(by='model_year(출시년도)', ascending=False)

# 판다스의 ExcelWriter 객체를 생성해서 각 시트에 저장
writer = pd.ExcelWriter("auto-mpg-2.xlsx")
df.to_excel(writer, sheet_name='sheet1')
new_df.to_excel(writer, sheet_name='sheet2')
writer.save()