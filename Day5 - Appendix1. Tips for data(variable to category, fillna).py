# -*- coding: utf-8 -*-
"""
# 데이터 타입 조정
- 변수(Column) 타입 확인 : 데이터.dtypes
- 변수를 범주형으로 변경하는 방법
  - 데이터['Column 이름'].astype('category')
- 변수를 수치형으로 변경하는 방법
  - 데이터['Column 이름'].astype('int')
  - 데이터['Column 이름'].astype('float')
- NA 값의 처리
  - NA 갯수 체크 : 데이터.isna().sum()
  - NA 값 채우기 : 데이터['Column 이름'].fillna(특정 수치)
"""

###########################
# 라이브러리 사용
import pandas as pd

###########################
# 파일 읽어오기
파일경로 = 'https://raw.githubusercontent.com/blackdew/tensorflow1/master/csv/iris2.csv'
아이리스 = pd.read_csv(파일경로)
아이리스.head()

###########################
# 칼럼의 데이터 타입 체크
print(아이리스.dtypes)

# 원핫인코딩 되지 않는 현상 확인 - pandas는 숫자가 들어있으면 숫자로 인식(iris1에서는 영어로 되어있었음)
인코딩 = pd.get_dummies(아이리스)
인코딩.head()

###########################
# 품종 타입을 범주형으로 바꾸어 준다. (object로 바꿔도 되네, iris1 타입 object로 되어있더라고. 아마 상위 데이터 타입이라 그런가보다)
아이리스['품종'] = 아이리스['품종'].astype('category')
print(아이리스.dtypes)

"""## 원핫인코딩
- 데이터를 0으로만 이루어진 벡터와 1로 구별하는 것
"""

# 카테고리 타입의 변수만 원핫인코딩
인코딩 = pd.get_dummies(아이리스)
인코딩.head()
#인코딩.tail()

###########################
# NA값을 체크해 봅시다
#아이리스.isna().sum()
아이리스.tail()

###########################
# NA값에 꽃잎폭 평균값을 넣어주는 방법 
mean = 아이리스['꽃잎폭'].mean()
print(mean)
아이리스['꽃잎폭'] = 아이리스['꽃잎폭'].fillna(mean)
아이리스.tail()