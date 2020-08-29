import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
pd.set_option('display.expand_frame_repr', False) # DataFrame 출력시 짤림 해결

# seaborn의 mpg 데이터셋 가져오기
mpg_df = sns.load_dataset('mpg')

## 데이터 확인
# 데이터 살펴보기
print(mpg_df.info())
print(mpg_df.head())
print(mpg_df.tail())
print(mpg_df.describe(include = 'all'))
print('----- 데이터 확인 중 -----\n')


## 출력에 noise 존재 및 출시년도, 제조국 번호가 범주형 아닌 연속형임 확인 -> 전처리
# 출시년도 및 제조국 번호를 astype() 메소드로 int -> object 변환
mpg_df[['model_year', 'origin']] = mpg_df[['model_year', 'origin']].astype('object')
print(mpg_df.describe(include = "all"),"\n")

# 결측값 대체 - 기존 DF를 복제하고 '출력 column'에 '?'가 있는 row을 제거하고 출력의 평균을 구해서 hpMean에 삽입
mpg_df_ex = mpg_df
mpg_df_ex['horsepower'].replace('?', np.nan, inplace = True)
mpg_df_ex.dropna(subset=['horsepower'], axis = 0, inplace = True)
mpg_df_ex['horsepower'] = mpg_df_ex['horsepower'].astype('float')
hpMean = round(mpg_df_ex['horsepower'].mean(),3)
print("결측값용 대체값 :",hpMean,"\n")

# 결측값 대체 - ?를 제외한 출력의 평균을 결측치들에 넣어준다.
mpg_df_ex['horsepower'].replace('?', hpMean, inplace = True)
mpg_df_ex.dropna(subset=['horsepower'], axis = 0, inplace = True)
mpg_df_ex['horsepower'] = mpg_df_ex['horsepower'].astype('float')

print(mpg_df.describe(include = 'all'))
print('----- 데이터 전처리 완료 -----\n')


## 변수 선택
# 분석에 활용할 변수 선택 (연비, 실린더, 출력, 중량)
ndf = mpg_df[['mpg', 'cylinders', 'horsepower', 'weight']]

# 두 변수씩 짝을 지을 수 있는 모든 경우에 대한 그래프(산점도) 확인(seaborn.pairplot())
sns.pairplot(ndf)  
plt.show()
plt.close()


## mpg와 horsepower, weight가 선형관계임이 확인 weight을 x, mpg를 y로 선택
# 속성(변수) 선택
X = ndf[['weight']]  #독립 변수 X
Y = ndf['mpg']       #종속 변수 Y


## dataset을 training data와 test data로 분할
# train_test_split(독립변수, 종속변수, test data 사이즈(%), 랜덤 추출 시드값)
from sklearn.model_selection import train_test_split
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.3, random_state=10)

print('train data 개수: ', len(X_train))
print('test data 개수: ', len(X_test),"\n")

# sklearn 라이브러리에서 선형회귀분석 모듈 가져오기
from sklearn.linear_model import LinearRegression

# 단순회귀분석 모형 객체 생성
lr = LinearRegression()   

## 학습 시작
# train data를 가지고 모형 학습
lr.fit(X_train, Y_train)

# 학습을 마친 모형에 test data를 적용하여 결정계수(R^2) 계산
r_square = lr.score(X_test, Y_test)

# 회귀식과 결정계수(R^2) 산출
print('회귀식 :', float(lr.coef_),'X +',lr.intercept_)
print('결정계수(R^2) :', r_square)
print('\n')

# 모형에 전체 X 데이터를 입력하여 예측한 값 y_hat을 실제 값 y와 비교 
Y_hat = lr.predict(X)

plt.figure(figsize = (10, 5))
ax1 = sns.distplot(Y, hist = False, label = "Y")
ax2 = sns.distplot(Y_hat, hist = False, label = "Y_hat", ax = ax1)
plt.show()
plt.close()