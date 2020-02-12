import pandas as pd
import numpy as np
pd.set_option('display.max_rows', 400)
pd.set_option('display.max_columns', 20)
pd.set_option('display.width', 1000)

# 1. dataset 확인
mpg_df = pd.read_csv("auto-mpg.csv")

# 1-a. data의 대략적인 모양새 파악 head는 상위 로우 5개, tail은 하위 로우 5개
print(mpg_df.head(),"\n\n")
print(mpg_df.tail(),"\n\n")

# 1-a. 컬럼 라벨링
mpg_df.columns = ['mpg(연비)', 'cylinders(실린더 수)', 'displacement(배기량)', 'horsepower(출력)', 'weight(차중)', 'acceleration(가속능력)', 'model_year(출시년도)', 'origin_number(제조국 번호)', 'name(모델 명)']

# 1-a. 요약통계량 및 데이터정보 확인 (출력에 noise 존재 및 출시년도, 제조국 번호가 범주형 아닌 연속형임 확인)
print(mpg_df.info())
print(mpg_df.describe(include = "all"),"\n\n")
print(mpg_df,"\n\n")

# 1-a. 출시년도 및 제조국 번호를 astype() 메소드로 int -> object 변환
mpg_df[['model_year(출시년도)', 'origin_number(제조국 번호)']] = mpg_df[['model_year(출시년도)', 'origin_number(제조국 번호)']].astype('object')
print(mpg_df.describe(include = "all"),"\n\n")

# 2. 결측값 처리
# 2-b. 결측값 대체 - 기존 DF를 복제하고 '출력 column'에 '?'가 있는 row을 제거하고 출력의 평균을 구해서 hpMean에 삽입
mpg_df_ex = mpg_df
mpg_df_ex['horsepower(출력)'].replace('?', np.nan, inplace = True)
mpg_df_ex.dropna(subset=['horsepower(출력)'], axis = 0, inplace = True)
mpg_df_ex['horsepower(출력)'] = mpg_df_ex['horsepower(출력)'].astype('float')
hpMean = round(mpg_df_ex['horsepower(출력)'].mean(),3)
print(hpMean,"\n\n")

# 2-b. 결측값 대체 - ?를 제외한 출력의 평균을 결측치들에 넣어준다.
mpg_df_ex['horsepower(출력)'].replace('?', hpMean, inplace = True)
mpg_df_ex.dropna(subset=['horsepower(출력)'], axis = 0, inplace = True)
mpg_df_ex['horsepower(출력)'] = mpg_df_ex['horsepower(출력)'].astype('float')

# 2-b. 처리된 데이터셋 확인
print(mpg_df_ex.info())
print(mpg_df_ex.describe(include = "all"))
