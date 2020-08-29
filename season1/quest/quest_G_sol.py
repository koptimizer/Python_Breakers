import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
pd.set_option('display.expand_frame_repr', False) # DataFrame 출력시 짤림 해결

df = sns.load_dataset("titanic")

# 데이터 확인
print(df.info(),'\n')
print(df.head(),'\n')
print(df.tail(),'\n')
print(df.describe(include = 'all'),'\n')

# 중복되는 열 : pclass, embarked, who, alive
# 필용없는 열 : sibsp, parch, fare
df.drop(['pclass', 'sibsp', 'parch', 'embarked', 'adult_male', 'fare', 'alive', 'who'], axis = 1, inplace = True)

# 수정이 필요한 열 : survived(연속->범)
# age는 수정이 불필요할까?
df['survived'] = df['survived'].astype('object')

# 결측값 처리가 필요한 열 : age, embark_town, deck
# age -> 평균값 대체 // embark_town -> 이웃값 대체 // deck -> 결측값이 너무 많아 삭제
mean_age = df['age'].mean() # nan값 제외 됨
df['age'].fillna(round(mean_age,2), inplace = True)
df['embark_town'].fillna(method = 'ffill', inplace = True)
df.drop(['deck'], axis = 1, inplace= True)

print(df.info())
print(df)