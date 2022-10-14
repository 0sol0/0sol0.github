# 딥러닝
머신러닝은 AND, OR 문제로부터 시작<br>
XOR 문제를 풀기 위해 역전파(Backpropagation) 알고리즘을 사용<br>
<br>

## Deep Neural Networks 구성 방법
### Layer(층) 쌓기
Input Layer(입력층) : 네트워크 입력, 학습시키고 싶은 값, x값<br>
Output Layer(출력층) : 네트워크 출력, 예측한 값, y값<br>
Hedden Layers(은닉층) : 입력층과 출력층을 제외한 중간층<br>
- 은닉층은 `완전연결 계층(Fully connected layer = Dense layer)`으로 이루어져 있다.<br>
node(노드) : Layer(층) 안에 있는 입력값<br>
<br>

### 너비(Width)와 깊이(Depth)
Baseline model(베이스라인 모델) : 적당한 연산량을 가진 적당한 정확도의 딥러닝 모델
#### 베이스라인 모델을 가지고 실험(튜닝)하는 방법
1. 너비 늘리기 : 각 은닉층의 노드의 개수를 늘리는 것
2. 깊이 늘리기 : 은닉층을 늘리는 것
3. 너비와 깊이 늘리기 : 은닉층을 늘리고 각 층의 노드 갯수를 늘리는 것
<br>

## 딥러닝 주요 개념
### 단위
- batch : 데이터셋을 나누는 단위
- iteration : batch를 반복하는 것
- epoch : 반복학습하는 것
<br>

ex) 데이터셋 = 10,000,000개 일 때
- 데이터셋을 1,000개의 betch로 나누면,
- 10,000,000/1,000 = 10,000개의 betch가 나오고,
- 10,000개의 betch를 100epoch씩 반복학습하면,
- 10,000 * 100 = 1,000,000 iteration을 도는 것이다.
<br>

### Activation functions (활성화 함수)
뉴런들은 전기신호가 특정 임계치(Threshold)를 넘어야 다음 뉴런으로 신호를 전달할 수 있도록 설계됨<br>
- Sigmoid
- tanh
- **ReLU** : 다른 함수에 비해 학습이 빠르고, 연산 비용이 적고, 구현이 간단함
- Leaky ReLU
- Maxout
- ELU\
<br>

### Overfitting, Underfitting (과적합, 과소적합)
Overfitting(과적합) : 모델을 학습시킬 때 Training loss보다 Validation loss가 높아질 때<br>
=> 문제 난이도보다 모델의 복잡도(Complexity)가 클 경우<br>
Underfitting(과적합) : 모델을 학습시킬 때 Training loss보다 Validation loss가 낮아질 때<br>
=> 문제 난이도보다 모델의 복잡도(Complexity)가 작을 경우<br>
Best fit(최적합) : Training loss와 Validation loss가 비슷할 때
- 데이터 더 모으기
- Data augmenation
- Dropout
<br>

## 딥러닝 주요 스킬
### Data augmentation (데이터 증강기법)
데이터가 부족할 때 이미 있는 데이터를 사용해 데이터를 증강시키는 것<br>
과적합을 해결하기 좋은 방법<br>
이미지 처리 분야의 딥러닝에서 주로 사용하는 기법<br>
원본 이미지를 여러가지 방법으로 복사해서 학습시키는 것<br>
<br>

### Dropout (드랍아웃)
각 노드들이 이어진 선을 빼서 없애는 것<br>
과적합을 해결하기 가장 간단한 방법<br>
<br>

### Ensemble (앙상블)
random forest 기법과 비슷<br>
여러개의 딥러닝 모델을 만들어 각각 학습시킨 후 각각의 모델에서 나온 출력을 기반으로 투표를 하는 방법
- 다수결로 투표(Majority voting)
- 평균값 구하기
- 마지막에 결정 레이어 붙이기
<br>

### Learning rate decay (Learning rate schedules)
Learning rate를 조금씩 줄여서 Local minimum을 찾는 기법<br>
Local minimum에 빠르게 도달하고 싶을 때 사용<br>
<br>

## 실습
### XOR 실습
1. 필요한 패키지 임포트하기
    
    ```python
    import numpy as np
    from tensorflow.keras.models import Sequential
    from tensorflow.keras.layers import Dense
    from tensorflow.keras.optimizers import Adam, SGD
    ```
    
2. XOR 데이터셋 만들기
    
    ```python
    x_data = np.array([[0, 0], [0, 1], [1, 0], [1, 1]], dtype=np.float32)
    y_data = np.array([[0], [1], [1], [0]], dtype=np.float32)
    ```
    
3. 이진논리회귀로 풀어보기
    
    ```python
    model = Sequential([
      Dense(1, activation='sigmoid')
    ])
    
    model.compile(loss='binary_crossentropy', optimizer=SGD(lr=0.1))
    
    model.fit(x_data, y_data, epochs=1000, verbose=0)
    
    y_pred = model.predict(x_data)
    ```
    
4. 딥러닝(MLP)로 풀어보기
    
    ```python
    model = Sequential([
      Dense(8, activation='relu'),
      Dense(1, activation='sigmoid'),
    ])
    
    model.compile(loss='binary_crossentropy', optimizer=SGD(lr=0.1))
    
    model.fit(x_data, y_data, epochs=1000, verbose=0)
    
    y_pred = model.predict(x_data)
    ```
    
5. Keras Functional API 써보기
    
    ```python
    import numpy as np
    from tensorflow.keras.models import Sequential, Model
    from tensorflow.keras.layers import Dense, Input
    from tensorflow.keras.optimizers import Adam, SGD
    ```
    
    ```python
    input = Input(shape=(2,))
    hidden = Dense(8, activation='relu')(input)
    output = Dense(1, activation='sigmoid')(hidden)
    
    model = Model(inputs=input, outputs=output)
    
    model.compile(loss='binary_crossentropy', optimizer=SGD(lr=0.1))
    
    model.summary()
    ```
    
    ```python
    model.fit(x_data, y_data, epochs=1000, verbose=0)
    
    y_pred = model.predict(x_data)
    ```
    

## 딥러닝 실습
1. 런타임Runtime - 런타임 유형 변경Change runtime type - GPU 선택해서 연산속도 늘리기
2. 데이터셋 다운로드
    
    ```python
    import os
    os.environ['KAGGLE_USERNAME'] = 'username' # username
    os.environ['KAGGLE_KEY'] = 'key' # key
    ```
    
    ```bash
    !kaggle datasets download -d datamunge/sign-language-mnist
    !unzip sign-language-mnist.zip
    ```
    
3. 필요한 패키지 임포트하기
    
    ```python
    from tensorflow.keras.models import Model
    from tensorflow.keras.layers import Input, Dense
    from tensorflow.keras.optimizers import Adam, SGD
    import numpy as np
    import pandas as pd
    import matplotlib.pyplot as plt
    import seaborn as sns
    from sklearn.model_selection import train_test_split
    from sklearn.preprocessing import StandardScaler
    from sklearn.preprocessing import OneHotEncoder
    ```
    
4. 데이터셋 로드하기
    
    ```python
    train_df = pd.read_csv('sign_mnist_train.csv')
    test_df = pd.read_csv('sign_mnist_test.csv')
    ```
    
5. 라벨 분포 확인하기
    
    ```python
    plt.figure(figsize=(16, 10))
    sns.countplot(train_df['label'])
    plt.show()
    ```
    
6. 전처리하기
    1. 입력과 출력 나누기
        
        ```python
        train_df = train_df.astype(np.float32)
        x_train = train_df.drop(columns=['label'], axis=1).values
        y_train = train_df[['label']].values
        
        test_df = test_df.astype(np.float32)
        x_test = test_df.drop(columns=['label'], axis=1).values
        y_test = test_df[['label']].values
        ```
        
    2. 데이터 미리보기
        
        ```python
        index = 1
        plt.title(str(y_train[index]))
        plt.imshow(x_train[index].reshape((28, 28)), cmap='gray')
        plt.show()
        ```
        
    3. one-hot 인코딩하기
        
        ```python
        encoder = OneHotEncoder()
        y_train = encoder.fit_transform(y_train).toarray()
        y_test = encoder.fit_transform(y_test).toarray()
        ```
        
    4. 일반화하기
        
        ```python
        x_train = x_train / 255.
        x_test = x_test / 255.
        ```
        
7. 네트워크 구성하기
    
    ```python
    input = Input(shape=(784,))
    hidden = Dense(1024, activation='relu')(input)
    hidden = Dense(512, activation='relu')(hidden)
    hidden = Dense(256, activation='relu')(hidden)
    output = Dense(24, activation='softmax')(hidden)
    
    model = Model(inputs=input, outputs=output)
    
    model.compile(loss='categorical_crossentropy', optimizer=Adam(lr=0.001), metrics=['acc'])
    ```
    
8. 모델 학습시키기
    
    ```python
    history = model.fit(
        x_train,
        y_train,
        validation_data=(x_test, y_test), # 검증 데이터를 넣어주면 한 epoch이 끝날때마다 자동으로 검증
        epochs=20 # epochs 복수형으로 쓰기!
    )
    ```
    