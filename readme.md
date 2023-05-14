# 와인 카테고리 분류
##### k means, k medoid - clustering과 silhouette coefficent를 통하여 


# 도입
-----------------------------
- 모든 음식에는 맛의 카테고리가 있다. 매운맛 단맛 짠맛 신맛… 등등 우리가 보편적으로 많이 쓰이는 이름들은 우리가 이름만 들어도 어떤맛인지 감각적으로 기억하고있다. 우리는 맛을 여러가지 기관으로 나누어 느끼고 있으며
위와 같이 잘 알려진 맛의 카테고리들은 정확히 감각기관들에 대응이 되는 카테고리들이다.


- 하지만 세상에는 많고 많은 음식들이 있다. 예를들어 불고기과 된장찌게 이 둘은 같은 고소한맛 계열의 음식이지만 그렇다고 같은 맛의 음식이라고는 표현하지 않는다. 하지만 냉면과 막국수는 같은 계열의 음식으로 카테고리화 할 수 있을것이다. 이렇듯 우리는 우리 나름대로 음식을 분류하고 특정한 기준을 정의하여 그들을 clustring한다.

- 이 clustering을 수학적으로 나타내볼 수는 없을까? 우리는 Red Wine Quality data를 통해 수학적으로 각 맛의 지표를 분석하고 kmeans, kmedoid clustering을 통해 와인들을 카테고리별로 분류하려고 한다.


### 연구 방법
-----------------------------

#### 데이터

- 우선 와인의 맛에대한 정의부터 하고 실험을 시작하고 싶다.
- 와인의 맛은 딱 복합적인 기준을 정할수는 없겠지만, 단맛, 신맛, 짠맛, 밀도, 산도등을 기준으로 정할 수 있도록 그에 맞는 데이터셋을 kaggle에서 찾아냈다. (https://www.kaggle.com/datasets/uciml/red-wine-quality-cortez-et-al-2009?select=winequality-red.csv)  
- 우리는 해당 데이터셋에서 다음과 같은 와인 맛의 척도를 확인할 수 있었다.
![image](https://github.com/ysh4296/WineTaster/assets/29995264/6cce6b41-8b46-4410-985c-557c1e33f894)

```
1. 단맛 - 잔여 설탕
2. 짠맛 - 염화물
3. 신맛 - 고정산도, 휘발성산도, 구연산, 산도 4. 밀도 - 밀도 5. 신선도 - 무료 이산화황, 총 이산화황, 황산염  6. 알코올 농도 - 알코올 농도 7. 맛의 평가 - 평가도  
```

각 데이터는 배열형태로 저장되어있다.
![image](https://github.com/ysh4296/WineTaster/assets/29995264/0d1b8fc5-5769-4c96-8022-d2bf5e220780)



#### 군집화
- 다음의 맛의 척도등을 이용해서 kmeans clustering과 kmedoid clustering을 사용하고 이를 통해 새로운 와인 군집화, 분류를 실행할 것이다. 군집수를 점점 늘려가며 최적의 군집수를 찾는것을 목표로 한다.
- 군집화의 평가에는 Silhouette Value를 이용할 것이다. 이를 통해 kmeans clustering과 kmedoid clustering을 보다 심층적으로 비교할 수 있다.

> ### K means 알고리즘
> ```
> 데이터를 k개의 클러스터로 그룹화하는 비지도 학습 알고리즘, 알고리즘의 핵심 아이디어는 데이터 포인트와 클러스터 중심 간의 거리를 최소화하는 방식으로 클러스터를 형성하는 것 
> ```
>
> ### K medoid 알고리즘
> ```
> 데이터를 k개의 클러스터로 그룹화하는 비지도 학습 알고리즘, 이 알고리즘은 클러스터의 중심으로 실제 데이터 포인트를 사용하는 대신, 클러스터의 대표적인 데이터 포인트인 medoid를 사용.
> ```
>
> ### Silhouette 계수
> ```
> 클러스터링 결과의 품질을 측정하는 지표, 각 데이터 포인트가 속한 클러스터 내의 응집력(cohesion)과 다른 클러스터와의 분리도(separation)를 고려함.  응집력(cohesion) 계산
> 같은 클러스터 내의 데이터 포인트들 간의 평균 거리를 계산함. 이는 데이터 포인트가 자신이 속한 클러스터 내에서 얼마나 밀접하게 모여있는지를 나타냄.
> ```
>
> ### 응집력(cohesion) 계산
> ```
> 같은 클러스터 내의 데이터 포인트들 간의 평균 거리를 계산함. 이는 데이터 포인트가 자신이 속한 클러스터 내에서 얼마나 밀접하게 모여있는지를 나타냄.
> ```
> 
> ### 분리도(separation) 계산
> ```
> 각 데이터 포인트와 다른 클러스터들 사이의 평균 거리를 계산함. 이는 데이터 포인트가 다른 클러스터와 얼마나 잘 구분되는지를 나타냄.
> ```

### 결과설명
----------------
먼저 k-means 알고리즘을 통해 와인데이터를 클러스터링 해본 결과입니다.
![image](https://github.com/ysh4296/WineTaster/assets/29995264/f10d5440-b139-4807-8c65-0dd00069861a)

다음으로는 k medoid 알고리즘을 통해 와인 데이터를 클러스터링 해본 결과입니다.
![image](https://github.com/ysh4296/WineTaster/assets/29995264/d316c645-1e60-4ccb-95b8-88c2365f1762)


- 실루엣 계수는 1에 가까워질수록 수행된 군집화가 정확하다는 지표로 작용된다.

- 우선 k means 클러스터링을 1~20 개의 군집수에 각각 적용해본 결과 실루엣 계수는 점차 증가하는 양상을 보인다. 하지만 실루엣계수의 증가율은 군집수가 늘어날수록 점차 줄어들며 사실상 17이후의 군집수부터는 큰 변화가 없을것이라 생각된다.

- K medoid 클러스터링을 적용해본 결과는 좀 들쑥날쑥하긴 하지만 실루엣 계수가 군집의 증가에 따라 점차 증가했다는것을 알 수 있었다. 하지만 k medoid의 실루엣 계수는 kmeans의 실루엣 계수에 한참 못미치는 모습을 보여주었다. 



### 결론
----------------
- 우리는 와인맛에 대한 데이터를 받아와서 k means, k medoid 클러스터링을 수행하고 결과를 silhouette 계수를 통해 시각적으로 분석해보았다.
- k means의 결과로 silhouette 계수가 군집수의 증가와 함께 증가하며 정확도의 향상을 보여줬지만 k medoid의 결과로서 silhouette계수는 군집수의 증가와 상관이 깊다고 보기에는 좀 불안정한 모습을 보였다. 또한 모든 구간에서 silhouette 계수가 kmeans에 비해 낮은 모습을 보여주었다. 이를 통해 알 수 있는점은 k-medoid가 이 데이터에서 더 성능이 좋지 못했다는 뜻이다. 왜 이런결과가 발생했을까?

- k means는 cluster의 평균값을 중심으로 삼지만 k medoid는 클러스터의 중심값을 지정하는 알고리즘이다. 다른말로 표현하자면 kmedoid를 통해 구한 중심값들이 클러스터의 중심값으로서의 역활을 수행하지 못하기 때문에 이런 결과가 나왔다고 생각된다.

- 따라서 와인데이터는 카테고리를 통한 클러스터링에 이상적인 군집화 모습을 보여주지 못하는것 같다.


