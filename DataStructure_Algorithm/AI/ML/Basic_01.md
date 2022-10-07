## 머신 러닝
알고리즘 : 어떠한 문제를 해결하기 위해 정해진 절차나 방법을 공식화한 형태로 표현한 것
머신러닝 : 복잡한 알고리즘을 기계가 풀게 하는 것
딥러닝 : 머신러닝의 방법 중 하나

## 머신러닝 문제푸는 방법
머신러닝에서 문제를 풀 때 해답을 내는 방법을 크게 회귀 또는 분류로 나눌 수 있다.
문제를 풀기 위해서는 먼저 입력값(Input)과 출력값(Output)을 정의해야 한다.
머신러닝에선 소수(flot)를 많이 쓴다.


```
참고

명명척도 = 이름을 붙여서 클래스를 만든다.
서열척도 = 이름을 붙이고 서열을 나눠서 클래스를 만든다.
등간척도 = 이름을 붙이고 서열을 나누고 간격을 같게 만들어서 클래스를 만든다.
비율척도 = 이름을 붙이고 서열을 나누고 간격을 같게 만든 다음, 절대 0점(기준)을 만들어 클래스를 만든다.
```

## 머신러닝 학습 방법

### 지도학습(Supervised Learning)
정답을 알려주면서 학습시키는 방법
Input data(입력값), Annotations(출력값) => Prediction
정답을 입력해주는 작업을 많이 하게 된다(Labeling, Annotation)

#### 회귀(Regression)
출력값이 연속적인 것을 예측 할 때
ex) 나이

##### 선형 회귀(Linear Regression)
머신러닝이나 딥러닝의 기본 구조는 항상 선형(1차함수)에서 시작한다.
가설을 세우고 손실 함수를 정의하는 것
가설과 손실 함수를 정의하면 알아서 최소값을 찾아준다

가설(Hypothesis) : 결과를 직선 1개(1차 함수)로 표현할 수 있다.
![Hypothesis](/image/Hypothesis.png)

가설에서 알아내야 되는 것
Weight = 기울기, x에 곱하는 값
bias = y절편, Wx에 더하는 값
W, b 둘다 행령(매트릭스) 형태로 되어 있다.

x에 값을 넣고 가설값을 알아내서 
가설값과 정답값의 차이를 계산한 다음에 
w, b를 다시 바꿔보면서 손실 함수가 가장 낮은 값을 찾는 것을 기계한테 시키면 된다.

실험결과 = 데이터셋
입력한 값(독립변수) = 입력값
출력된 값(종속변수) = 출력값 = 정답값

점 = 정답값
선 = 예측한 값(가설값)

점과 선이 가까워지게 학습시켜야 한다.

![Cost function](/image/Cost_function.png)

loss/Cost function(손실 함수) : 점과 직선의 거리를 계산한 식 = Mean Squared Error(평균 제곱 오차)
Minimization, optimization 문제 : 손실 함수 값이 작아지도록 하는 문제

##### 다중 선형 회귀(Multi-variable Liner Reqression)
가설
![Hypothesis](/image/Hypothesis2.png)

손실 함수
![Cost function](/image/Cost_function2.png)

#### 경사 하강법(Gradient descent method)
optimizer 안에 gradient descent가 있따.
가설을 계산하면서 손실함수가 줄어드는 방향으로 가면서 최소점에 도달하게 학습하는 것
이 때 손실함수가 한 점씩 줄어드는 거리를 Learning rate라고 한다.
Learning rate가 작으면 시간이 오래 걸린다. = 학습이 느리다.
무조건 크게하면 최소점을 못찻고 튕겨나갈 수 있다. = Overshooting

실제 손실 함수는 엄청 복잡하다.
그래서 경사 하강법을 진행하다보면 원래 목표인 최소점(global minimum)에 도달하지 못하고 중간에 걸리는 경우가 있다. = local minimum에 빠졌다.

#### 분류(Classsification)
출력값은 비연속적인 것을 예측할 때
ex) bloonen(True or False) = 이진 클래스(Birnary class) => 이진 분류(Binary Classification)
ex) 분류값이 3개 이상일 때   =  다중 클래스(Multi class) => 다중 분류(Multi-class Classification)

나이를 범위를 나눠서 분류로 풀 수 있다.

### 비지도학습(Unsupervised Learning)
정답을 알려주지 않고 군집화(Clustering)하는 방법
출력값(Label, Class)이 없을 때 사용
INput data(입력값) => Prediction
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

### 강화 학습(Reinforcement Learnig)
주어진 데이터없이 실행과 오류를 반복하면서 학습하는 방법
보상(Reward)를 받으면서 학습하는 것

개념
Agent(에이전트) - 학습하는 개체
Environment(환경) - 룰
suate(상태) - 현재 상태
Action(행동) - 행동을 위한 행동 목록이 정해져야 한다
Reward(보상)

ex) 알파고

## 데이터셋 분할
학습(Training set) = 교과서
머신러닝 모델을 학습을 시키는 용도로 사용한다.
전체 데이터의 80%

검증(Validation set) = 모의고사
모델의 성능과 적합성을 검증하고 튜닝하는 지표의 용도로 사용
학습 때 쓰지 않은 데이터 사용

테스트(Testing set) = 수능
학습, 검증 때 쓰지 않은 데이터 사용

## 실습
fitting : 가설을 정답값에 맞춘다.
Adom : 보편적으로 성능이 좋아서 많이 쓰인다.
epochs : 반복 학습
scatter : 점 그래프

### 실습 순서
데이터 셋 다운로드
데이터 셋 압축 해제
데이터 예측
    - 데이터 셋 로드(pd.read_csv)
    - 데이터 셋 크기 살펴보기(shape)
    - 데이터 셋 살펴보기(sns.pairplot)
    - 데이터 셋 가공(shape, np.array, reshape)
    - 데이터 셋 분할(train_test_split)
학습(Sequential, Dense, compile, Adom, fit, epochs)
검증 데이터로 예측하기(predict, scatter)