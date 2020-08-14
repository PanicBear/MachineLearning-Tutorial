# -*- coding: utf-8 -*-
"""Day2 - Lemonade Selling Prediction

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1TEf657kFe0YxDmXe1PE_rK5dgOuSdZ-b
"""

###########################
# 라이브러리 사용
import pandas as pd
import tensorflow as tf

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
X = tf.keras.layers.Input(shape=[1])
Y = tf.keras.layers.Dense(1)(X)
model = tf.keras.models.Model(X, Y)
model.compile(loss='mse')

###########################
# 모델을 학습시킵니다.
model.fit(독립, 종속, epochs=1000, verbose=0)
model.fit(독립, 종속, epochs=10)

###########################
# 모델을 이용합니다.
print(model.predict(독립))
print(model.predict([[15]]))