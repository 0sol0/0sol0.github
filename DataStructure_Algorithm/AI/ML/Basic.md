# 머신 러닝
알고리즘 : 어떠한 문제를 해결하기 위해 정해진 절차나 방법을 공식화한 형태로 표현한 것<br>
머신러닝 : 복잡한 알고리즘을 기계가 풀게 하는 것<br>
딥러닝 : 머신러닝의 방법 중 하나<br>
<br>

## 머신러닝 문제푸는 방법
머신러닝에서 문제를 풀 때 해답을 내는 방법을 크게 회귀 또는 분류로 나눌 수 있다.<br>
문제를 풀기 위해서는 먼저 입력값(Input)과 출력값(Output)을 정의해야 한다.<br>
머신러닝에선 소수(flot)를 많이 쓴다.<br>
<br>

## 머신러닝 학습 방법

### 지도학습(Supervised Learning)
정답을 알려주면서 학습시키는 방법<br>
Input data(입력값), Annotations(출력값) => Prediction<br>
정답을 입력해주는 작업을 많이 하게 된다(Labeling, Annotation)<br>
<br>

#### 회귀(Regression)
출력값이 연속적인 것을 예측 할 때<br>
ex) 나이<br>
<br>

##### **선형 회귀(Linear Regression)**
머신러닝이나 딥러닝의 기본 구조는 항상 선형(1차함수)에서 시작한다.<br>
가설을 세우고 손실 함수를 정의하는 것<br>
가설과 손실 함수를 정의하면 알아서 최소값을 찾아준다<br>
<br>
가설(Hypothesis) : 결과를 직선 1개(1차 함수)로 표현할 수 있다.<br>
![Hypothesis](/image/Liner_Hypothesis.png)<br>
<br>
가설에서 알아내야 되는 것<br>
Weight = 기울기, x에 곱하는 값<br>
bias = y절편, Wx에 더하는 값<br>
W, b 둘다 행령(매트릭스) 형태로 되어 있다.<br>
<br>
x에 값을 넣고 가설값을 알아내서 <br>
가설값과 정답값의 차이를 계산한 다음에 <br>
w, b를 다시 바꿔보면서 손실 함수가 가장 낮은 값을 찾는 것을 기계한테 시키면 된다.<br>
<br>
실험결과 = 데이터셋<br>
입력한 값(독립변수) = 입력값<br>
출력된 값(종속변수) = 출력값 = 정답값<br>
<br>
점 = 정답값<br>
선 = 예측한 값(가설값)<br>
<br>
점과 선이 가까워지게 학습시켜야 한다.<br>
<br>
![Cost function](/image/Cost_function.png)<br>
<br>
loss/Cost function(손실 함수) : 점과 직선의 거리를 계산한 식 = Mean Squared Error(평균 제곱 오차)<br>
Minimization, optimization 문제 : 손실 함수 값이 작아지도록 하는 문제<br>
<br>

##### **다중 선형 회귀(Multi-variable Liner Reqression)**
가설<br>
![Hypothesis](/image/Liner_Hypothesis2.png)<br>
<br>

손실 함수<br>
![Cost function](/image/Cost_function2.png)<br>
<br>

##### **경사 하강법(Gradient descent method)**
optimizer 안에 gradient descent가 있다.<br>
가설을 계산하면서 손실함수가 줄어드는 방향으로 가면서 최소점에 도달하게 학습하는 것<br>
이 때 손실함수가 한 점씩 줄어드는 거리를 Learning rate라고 한다.<br>
Learning rate가 작으면 시간이 오래 걸린다. = 학습이 느리다.<br>
무조건 크게하면 최소점을 못찻고 튕겨나갈 수 있다. = Overshooting<br>
<br>
실제 손실 함수는 엄청 복잡하다.<br>
그래서 경사 하강법을 진행하다보면 원래 목표인 최소점(global minimum)에 도달하지 못하고 중간에 걸리는 경우가 있다. = local minimum에 빠졌다.<br>
<br>

#### 분류(Classsification)
출력값은 비연속적인 것을 예측할 때<br>
ex) bloonen(True or False) = 이진 클래스(Birnary class) => 이진 분류(Binary Classification)<br>
ex) 분류값이 3개 이상일 때   =  다중 클래스(Multi class) => 다중 분류(Multi-class Classification)<br>
<br>
나이를 범위를 나눠서 분류로 풀 수 있다.<br>
<br>

##### **논리 회귀(Logistic Regression)**
Yes or No, Pass or Fail, True or False 같은 출력값을 가진 문제는 선형회귀로 풀 수 없다.<br>
이런 경우 `이진 논리 회귀(Binary Logistic Regression)`로 해결할 수 있다.<br>
논리 회귀의 실질적인 계산은 선형 회귀와 비슷하지만 출력값을 0과 1 사이의 값을 가지도록 중간에 `Sigmoid function`을 붙이는 것이다.<br>
![Logistic function(=Sigmoid function)](/image/Sigmoid_function.png)<br>
<br>
x(입력)가 음수 방향으로 갈 수록 y(출력)가 0에 가까워지고,<br>
x(입력)가 양수 방향으로 갈 수록 y(출력)가 1에 가까워진다!<br>
<br>
논리 회귀의 가설 함수는 선형 회귀 가설 함수에 시그모이드 함수를 추가해주면 된다.<br>
<br>
가설 함수<br>
![Hypothesis](/image/Logistic_Hypothesis.png)<br>
<br>

손실함수<br>
![binary_crossentropy](/image/Binary_Crossentropy.png)<br>
<br>
확률분포그래프 : 가로축을 라벨(클래스)로 표시하고 세로축을 확률로 표시하는 그래프<br>
확률분포그래프의 차이를 비교할 때는 Crossentropy 함수를 쓴다.<br>
<br>

##### **다항 논리 회귀 (Multinomial logistic regression)**
라벨(클래스)가 2개 이상인 논리 회귀<br>
One hot encoding : 다항 분류를 0과 1을 통해서 표현하는 인코딩 방법<br>
Softmax 함수 : 선형 모델에서 나온 결과를 모두 합한 값이 `1`이 되게 해주는 함수<br>
예측 결과를 확률로 만들기 위해 사용<br>
<br>

Softmax 함수<br>
![Softmax](/image/Softmax_function.png)<br>
categorical_crossentropy 손실 함수 사용<br>
<br>

### 비지도학습(Unsupervised Learning)
정답을 알려주지 않고 군집화(Clustering)하는 방법<br>
출력값(Label, Class)이 없을 때 사용<br>
INput data(입력값) => Prediction<br>

- Clustering(군집) : 비슷한 것끼리 묶기
    - K-평균(K-Means)
    - 계측 준집 분석(HA, Hierarchical Cluster Analysis)
    - 기댓값 최대화(Expectation Maximization)
-  데이터들이 어느 방향으로 놓여있는지 봐서 Dimensionaity Reduction(차원 축소) : 필요없는 차원 없애기 / Visualization(시각화) : 잘 보이는 방향 찾기
    - 주성분 분석(PCA, Principal Component Analysis)
    - 커널 PCA(Kernel PCA)
    - 지역적 선형 임베딩(LLE, Locally-Linear-Embedding)
    - t-SNE(t-distributed Stochatic Meighbor Embedding)
- Association Rule Learning(연관 규칙 학습) : 어떤 값이 서로연관 있는지 찾기
    - 어프라이어리(Apriori)
    - 이클렛(Eclat)
<br>

### 강화 학습(Reinforcement Learnig)
주어진 데이터없이 실행과 오류를 반복하면서 학습하는 방법<br>
보상(Reward)를 받으면서 학습하는 것<br>
<br>
ex) 알파고
<br>

개념
- Agent(에이전트): 학습하는 개체
- Environment(환경) : 룰
- suate(상태) : 현재 상태
- Action(행동) : 행동을 위한 행동 목록이 정해져야 한다
- Reward(보상)
<br>

## 머신러닝 모델
Support vector machine (SVM)
- 그래프 축 = Feature(특성)
- 그래프 선 = Support vector(구분선)
- 구분선과 입력값의 거리 = Margin

k-Nearest neighbors (KNN)
- 비슷한 특성을 가진 개체끼리 군집화하는 알고리즘

Decision tree (의사결정나무)
- 한 사람의 의견을 듣고 결정

Random forest
- 의사결정나무를 여러개 합친 모델
- 여러사람의 의견을 모아 마지막에 투표(Majority voting)를 통해 답을 결정

## 전처리
넓은 범위의 데이터 정제 작업<br>
필요없는 데이터를 지우고 필요한 데이터만을 취하는 것<br>
null 값이 있는 행을 삭제하는 것<br>
ex) 정규화(Normalization), 표준화(Standardization) 등<br>
<br>

### 정규화(Normalization)
데이터를 0과 1 사이의 값으로 만든다.<br>
같은 특성의 데이터 중에서 가장 작은 값을 0으로 만들고, 가장 큰 값을 1로 만들어준다.<br>
![Normalization](/image/Normalization.png)<br>
<br>

### 표준화(Standardization)
데이터의 분포를 정규분포로 바꿔준다.<br>
데이터의 평균이 0이 되도록하고 표준편차가 1이 되도록 만들어 준다.<br>
![Standardization](/image/Standardization.png)<br>
<br>
평균이 0이 되면 데이터의 중심이 0이 된다(zero-centered).<br>
표준편차가 1이 되면 정규화(Normalization)이 된다.<br>
=> 학습 속도(최저점 수렴 속도)가 빠르고 Local minima에 빠질 가능성이 적다.<br>
<br>

## 데이터셋 분할
학습(Training set) = 교과서<br>
머신러닝 모델을 학습을 시키는 용도로 사용한다.<br>
전체 데이터의 80%<br>
<br>
검증(Validation set) = 모의고사<br>
모델의 성능과 적합성을 검증하고 튜닝하는 지표의 용도로 사용<br>
학습 때 쓰지 않은 데이터 사용<br>
<br>
테스트(Testing set) = 수능<br>
학습, 검증 때 쓰지 않은 데이터 사용<br>
<br>

## 실습
fitting : 가설을 정답값에 맞춘다.
Adom : 보편적으로 성능이 좋아서 많이 쓰인다.
epochs : 반복 학습
scatter : 점 그래프

### 선형 회귀
1. 텐서플로우를 임포트하고 데이터와 변수들을 설정해줍니다.
    
    ```python
    import tensorflow as tf
    
    tf.compat.v1.disable_eager_execution()
    
    x_data = [[1, 1], [2, 2], [3, 3]]
    y_data = [[10], [20], [30]]
    
    X = tf.compat.v1.placeholder(tf.float32, shape=[None, 2])
    Y = tf.compat.v1.placeholder(tf.float32, shape=[None, 1])
    
    W = tf.Variable(tf.random.normal(shape=(2, 1)), name='W')
    b = tf.Variable(tf.random.normal(shape=(1,)), name='b')
    ```
    
2. 가설과 비용함수, optimizer를 정의합니다.
    
    ```python
    hypothesis = tf.matmul(X, W) + b
    cost = tf.reduce_mean(tf.square(hypothesis - Y))
    optimizer = tf.compat.v1.train.GradientDescentOptimizer(learning_rate=0.01).minimize(cost)
    ```
    
3. 매 스텝 별로 결과를 출력하며 비용함수가 줄어드는 것을 확인합니다.
    
    ```python
    with tf.compat.v1.Session() as sess:
      sess.run(tf.compat.v1.global_variables_initializer())
    
      for step in range(50):
        c, W_, b_, _ = sess.run([cost, W, b, optimizer], feed_dict={X: x_data, Y: y_data})
        print('Step: %2d\t loss: %.2f\t' % (step, c))
    
      print(sess.run(hypothesis, feed_dict={X: [[4, 4]]}))
    ```
    
- 실제로는 이렇게 Keras를 이용해 쉽게 선형회귀를 실행해볼 수 있습니다!
    
    ```python
    import numpy as np
    from tensorflow.keras.models import Sequential
    from tensorflow.keras.layers import Dense
    from tensorflow.keras.optimizers import Adam, SGD
    
    x_data = np.array([[1], [2], [3]])
    y_data = np.array([[10], [20], [30]])
    
    model = Sequential([
      Dense(1)
    ])
    
    model.compile(loss='mean_squared_error', optimizer=SGD(lr=0.1))
    
    model.fit(x_data, y_data, epochs=100) # epochs 복수형으로 쓰기!
    ```
    
    ```python
    y_pred = model.predict([[4]])
    print(y_pred)
    ```
    

### 캐글 선형 회귀
1. [캐글](https://www.kaggle.com/) 회원가입하기
    
    ![https://s3-us-west-2.amazonaws.com/secure.notion-static.com/9a6fe0d2-220b-4673-bcc0-551249242084/Untitled.png](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/9a6fe0d2-220b-4673-bcc0-551249242084/Untitled.png)
    
2. 로그인하고 내 프로필 클릭 > Account 탭 클릭하기
3. API - Create New API Token 클릭해서 kaggle.json 파일 다운로드 받기
4. 브라우저에서 파일을 열어 username과 key 복사하기
5. 환경변수 지정하기
    
    ```python
    import os
    os.environ['KAGGLE_USERNAME'] = '[내_캐글_username]' # username
    os.environ['KAGGLE_KEY'] = '[내_캐글_key]' # key
    ```
    
6. 원하는 데이터셋의 API를 복사해 와 실행하기
    
    ```bash
    !kaggle datasets download -d ashydv/advertising-dataset
    ```
    
7. 데이터셋 압축 풀어주기
    
    ```bash
    !unzip /content/advertising-dataset.zip
    ```
    
- 데이터 분석
    1. 필요한 라이브러리들 임포트하기
        
        ```python
        from tensorflow.keras.models import Sequential
        from tensorflow.keras.layers import Dense
        from tensorflow.keras.optimizers import Adam, SGD
        import numpy as np
        import pandas as pd
        import matplotlib.pyplot as plt 
        import seaborn as sns
        from sklearn.model_selection import train_test_split
        ```
        
    2. 데이터셋 불러와서 형태 확인하기
        
        ```python
        df = pd.read_csv('advertising.csv')
        df.head(5)
        ```
        
        ```python
        print(df.shape)
        ```
        
    3. 데이터셋 살짝 살펴보기
        
        ```python
        sns.pairplot(df, x_vars=['TV', 'Newspaper', 'Radio'], y_vars=['Sales'], height=4)
        ```
        
    4. 데이터셋 가공하기
        
        ```python
        x_data = np.array(df[['TV']], dtype=np.float32)
        y_data = np.array(df['Sales'], dtype=np.float32)
        
        print(x_data.shape)
        print(y_data.shape)
        ```
        
        ```python
        x_data = x_data.reshape((-1, 1))
        y_data = y_data.reshape((-1, 1))
        
        print(x_data.shape)
        print(y_data.shape)
        ```
        
    5. 데이터셋을 학습 데이터와 검증 데이터로 분할하기
        
        ```python
        x_train, x_val, y_train, y_val = train_test_split(x_data, y_data, test_size=0.2, random_state=2021)
        
        print(x_train.shape, x_val.shape)
        print(y_train.shape, y_val.shape)
        ```
        
    6. 학습시키기
        
        ```python
        model = Sequential([
          Dense(1)
        ])
        
        model.compile(loss='mean_squared_error', optimizer=Adam(lr=0.1))
        
        model.fit(
            x_train,
            y_train,
            validation_data=(x_val, y_val), # 검증 데이터를 넣어주면 한 epoch이 끝날때마다 자동으로 검증
            epochs=100 # epochs 복수형으로 쓰기!
        )
        ```
        
    7. 검증 데이터로 예측하기
        
        ```python
        y_pred = model.predict(x_val)
        
        plt.scatter(x_val, y_val)
        plt.scatter(x_val, y_pred, color='r')
        plt.show()
        ```
        
    8. 여러 X값을 이용하여 매출 예측하기
        
        ```python
        from tensorflow.keras.models import Sequential
        from tensorflow.keras.layers import Dense
        from tensorflow.keras.optimizers import Adam, SGD
        import numpy as np
        import pandas as pd
        import matplotlib.pyplot as plt 
        import seaborn as sns
        from sklearn.model_selection import train_test_split
        
        df = pd.read_csv('advertising.csv')
        
        x_data = np.array(df[['TV', 'Newspaper', 'Radio']], dtype=np.float32)
        y_data = np.array(df['Sales'], dtype=np.float32)
        
        x_data = x_data.reshape((-1, 3))
        y_data = y_data.reshape((-1, 1))
        
        print(x_data.shape)
        print(y_data.shape)
        
        x_train, x_val, y_train, y_val = train_test_split(x_data, y_data, test_size=0.2, random_state=2021)
        
        print(x_train.shape, x_val.shape)
        print(y_train.shape, y_val.shape)
        
        model = Sequential([
          Dense(1)
        ])
        
        model.compile(loss='mean_squared_error', optimizer=Adam(lr=0.1))
        
        model.fit(
            x_train,
            y_train,
            validation_data=(x_val, y_val), # 검증 데이터를 넣어주면 한 epoch이 끝날때마다 자동으로 검증
            epochs=100 # epochs 복수형으로 쓰기!
        )
        ```

### 논리 회귀
- 1) 데이터 다운받기
    
    ```python
    import os
    os.environ['KAGGLE_USERNAME'] = 'username' # username
    os.environ['KAGGLE_KEY'] = 'key' # key
    ```
    
    ```bash
    !kaggle datasets download -d heptapod/titanic
    !unzip titanic.zip
    ```
    
- 2) 필요한 패키지 임포트하기
    
    ```python
    from tensorflow.keras.models import Sequential
    from tensorflow.keras.layers import Dense
    from tensorflow.keras.optimizers import Adam, SGD
    import numpy as np
    import pandas as pd
    import matplotlib.pyplot as plt 
    import seaborn as sns
    from sklearn.model_selection import train_test_split
    from sklearn.preprocessing import StandardScaler
    ```
    
- 3) 데이터 로딩하기
    
    ```python
    df = pd.read_csv('train_and_test2.csv')
    ```
    
- 4) 전처리하기
    1.  사용할 컬럼 추출하기
        
        ```python
        df = pd.read_csv('train_and_test2.csv', usecols=[
          'Age', # 나이
          'Fare', # 승차 요금
          'Sex', # 성별
          'sibsp', # 타이타닉에 탑승한 형제자매, 배우자의 수
          'Parch', # 타이타니게 탑승한 부모, 자식의 수
          'Pclass', # 티켓 등급 (1, 2, 3등석)
          'Embarked', # 탑승국
          '2urvived' # 생존 여부 (0: 사망, 1: 생존)
        ])
        ```
        
    2. 비어있는 행 없애기
        
        ```python
        df = df.dropna()
        ```
        
    3. X, Y 데이터 분할하기
        
        ```python
        x_data = df.drop(columns=['2urvived'], axis=1)
        x_data = x_data.astype(np.float32)
        
        y_data = df[['2urvived']]
        y_data = y_data.astype(np.float32)
        ```
        
    4. 표준화하기
        
        ```python
        scaler = StandardScaler()
        x_data_scaled = scaler.fit_transform(x_data)
        ```
        
    5. 학습/검증 데이터 분할하기
        
        ```python
        x_train, x_val, y_train, y_val = train_test_split(x_data, y_data, test_size=0.2, random_state=2021)
        ```
        
- 5) 모델 학습시키기
    
    ```python
    model = Sequential([
      Dense(1, activation='sigmoid')
    ])
    
    model.compile(loss='binary_crossentropy', optimizer=Adam(lr=0.01), metrics=['acc'])
    
    model.fit(
        x_train,
        y_train,
        validation_data=(x_val, y_val), # 검증 데이터를 넣어주면 한 epoch이 끝날때마다 자동으로 검증
        epochs=20 # epochs 복수형으로 쓰기!
    )
    ```
    

### 다항 논리회귀
- 1) 데이터 다운받기
    
    ```python
    import os
    os.environ['KAGGLE_USERNAME'] = 'username' # username
    os.environ['KAGGLE_KEY'] = 'key' # key
    ```
    
    ```bash
    !kaggle datasets download -d brynja/wineuci
    !unzip wineuci.zip
    ```
    
- 2) 필요한 패키지 임포트하기
    
    ```python
    from tensorflow.keras.models import Sequential
    from tensorflow.keras.layers import Dense
    from tensorflow.keras.optimizers import Adam, SGD
    import numpy as np
    import pandas as pd
    import matplotlib.pyplot as plt 
    import seaborn as sns
    from sklearn.model_selection import train_test_split
    from sklearn.preprocessing import StandardScaler
    from sklearn.preprocessing import OneHotEncoder
    ```
    
- 3) 데이터 로딩하기
    
    ```python
    df = pd.read_csv('Wine.csv')
    ```
    
- 4) 전처리하기
    1. 헤더 정보 채워넣기
        
        ```python
        df = pd.read_csv('Wine.csv', names=[
          'name'
          ,'alcohol'
          ,'malicAcid'
          ,'ash'
          ,'ashalcalinity'
          ,'magnesium'
          ,'totalPhenols'
          ,'flavanoids'
          ,'nonFlavanoidPhenols'
          ,'proanthocyanins'
          ,'colorIntensity'
          ,'hue'
          ,'od280_od315'
          ,'proline'
        ])
        ```
        
    2. X, Y 데이터 분할하기
        
        ```python
        x_data = df.drop(columns=['name'], axis=1)
        x_data = x_data.astype(np.float32)
        
        y_data = df[['name']]
        y_data = y_data.astype(np.float32)
        ```
        
    3. 표준화하기
        
        ```python
        scaler = StandardScaler()
        x_data_scaled = scaler.fit_transform(x_data)
        ```
        
    4. One-hot 인코딩하기
        
        ```python
        encoder = OneHotEncoder()
        y_data_encoded = encoder.fit_transform(y_data).toarray()
        ```
        
    5. 학습/검증 데이터 분할하기
        
        ```python
        x_train, x_val, y_train, y_val = train_test_split(x_data_scaled, y_data_encoded, test_size=0.2, random_state=2021)
        ```
        
- 5) 모델 학습시키기
    
    ```python
    model = Sequential([
      Dense(3, activation='softmax')
    ])
    
    model.compile(loss='categorical_crossentropy', optimizer=Adam(lr=0.02), metrics=['acc'])
    
    model.fit(
        x_train,
        y_train,
        validation_data=(x_val, y_val), # 검증 데이터를 넣어주면 한 epoch이 끝날때마다 자동으로 검증
        epochs=20 # epochs 복수형으로 쓰기!
    )
    ```
    