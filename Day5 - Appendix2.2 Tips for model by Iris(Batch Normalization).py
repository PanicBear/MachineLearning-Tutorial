###########################
# 라이브러리 사용 
import tensorflow as tf 
import pandas as pd

###########################
# 1.과거의 데이터를 준비합니다. 
파일경로 = 'https://raw.githubusercontent.com/blackdew/tensorflow1/master/csv/iris.csv'
아이리스 = pd.read_csv(파일경로)
아이리스.head()

인코딩 = pd.get_dummies(아이리스)
인코딩.head()

"""원핫인코딩 = 범주형 데이터를 1과 0의 데이터로 변환하는 것"""

# 원핫인코딩
아이리스 = pd.get_dummies(아이리스)

#꽃잎길이	꽃잎폭	꽃받침길이	꽃받침폭	품종.setosa  품종.virginica  품종.versicolor
# y1 = f(w1x1 + w2x2 + w3x3 + w4x4 +b)
# y2 = f(w1x1 + w2x2 + w3x3 + w4x4 +b)
# y3 = f(w1x1 + w2x2 + w3x3 + w4x4 +b)

# 종속변수, 독립변수
독립 = 아이리스[['꽃잎길이', '꽃잎폭', '꽃받침길이', '꽃받침폭']]
종속 = 아이리스[['품종_setosa', '품종_versicolor', '품종_virginica']]
print(독립.shape, 종속.shape)

"""### 분류 모델을 0 ~ 100%로 나타내주는 활성화 함수 : **sigmoid, softmax**

현재의 분류모델은 0과 1을 판단하기에, softmax로 수식을 감싸면 0 또는 1 반환
y1 = softmax(w1x1 + w2x2 + w3x3 + w4x4 +b)


### 분류에 사용하는 모델 : **categorical_crossentropy**
### 회귀에 사용하는 모델 : **mse**
(아직까지는)
"""

###########################
# 2. 모델의 구조를 만듭니다
X = tf.keras.layers.Input(shape=[4])
# H = tf.keras.layers.Dense(8, activation="swish")(X)
# H = tf.keras.layers.Dense(8, activation="swish")(H)
# H = tf.keras.layers.Dense(8, activation="swish")(H)

H = tf.keras.layers.Dense(8)(X)
H = tf.keras.layers.BatchNormalization()(H)
H = tf.keras.layers.Activation('swish')(H)

H = tf.keras.layers.Dense(8)(H)
H = tf.keras.layers.BatchNormalization()(H)
H = tf.keras.layers.Activation('swish')(H)

H = tf.keras.layers.Dense(8)(H)
H = tf.keras.layers.BatchNormalization()(H)
H = tf.keras.layers.Activation('swish')(H)

Y = tf.keras.layers.Dense(3, activation='softmax')(H)
model = tf.keras.models.Model(X, Y)

# 분류에서는 정확도가 판단하기 더 좋음
model.compile(loss = 'categorical_crossentropy', metrics = 'accuracy')
# model.compile(loss = 'categorical_crossentropy')

# 모델 구조 확인
model.summary()

"""###기존의 데이터 종속 변수 : **양적 데이터 -> 회귀 알고리즘**
###이번 데이터의 종속 변수 : **범주형 데이터 => 분류 알고리즘**
"""

###########################
# 3.데이터로 모델을 학습(FIT)합니다.
model.fit(독립, 종속, epochs=1000, batch_size=150)

###########################
# 4. 모델을 이용합니다
# 맨 처음 데이터 5개
print(model.predict(독립[:5]))
print(종속[:5])

# 맨 마지막 데이터 5개
print(model.predict(독립[-5:]))
print(종속[-5:])

###########################
# weights & bias 출력
print(model.get_weights())

