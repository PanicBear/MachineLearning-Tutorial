###########################
# 라이브러리 사용
import pandas as pd
import tensorflow as tf

"""1.   과거의 데이터를 준비합니다
2.   모델의 구조를 만듭니다.
3.   데이터로 모델을 학습(FIT)합니다
4.   모델을 이용합니다
"""

###########################
# 파일로부터 데이터 읽어오기
파일경로 = 'https://raw.githubusercontent.com/blackdew/tensorflow1/master/csv/lemonade.csv'
레모네이드 = pd.read_csv(파일경로)
레모네이드.head()

###########################
# 종속변수, 독립변수
독립 = 레모네이드[['온도']]
종속 = 레모네이드[['판매량']]

###########################
# 모델을 만듭니다.
X = tf.keras.layers.Input(shape=[1])    # shape=[독립변수의 갯수]
Y = tf.keras.layers.Dense(1)(X)         # Dense(종속변수의 갯수)(X)
model = tf.keras.models.Model(X, Y)
model.compile(loss='mse')

###########################
# 모델을 학습시킵니다.
model.fit(독립, 종속, epochs=1000, verbose=0)     # epoches : 학습 횟수  / 시간 / 손실률(학습률 지표 = (예측 - 결과)^2)
model.fit(독립, 종속, epochs=10)                  # 손실률이 낮을수록 정확한 것
                                                 # verbose는 출력을 없애는 것
###########################
# 모델을 이용합니다.
print(model.predict(독립))
print(model.predict([[15]]))