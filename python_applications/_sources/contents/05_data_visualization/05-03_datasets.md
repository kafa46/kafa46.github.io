(05-03)=
# 자주 사용되는 Dataset 소개

데이터 시각화는 데이터를 직관적으로 이해하고 분석하는 데 중요한 역할을 합니다. 다양한 데이터셋이 데이터 시각화에 사용되며, 그 중 몇 가지 대표적인 데이터셋을 소개합니다.

표 형식 데이터는 행과 열로 구성된 스프레드시트나 데이터베이스 테이블 형태로, 변수와 관측치가 명확히 구분됩니다.

대표적인 예로, `Iris` 데이터셋과 `Titanic` 데이터셋이 있습니다.

`Iris` 데이터셋은 꽃잎과 꽃받침의 길이와 너비를 포함한 간단한 데이터셋으로, 데이터 시각화와 머신러닝 초보자들에게 자주 사용됩니다.

`Titanic` 데이터셋은 타이타닉 호의 승객 정보를 포함하고 있어, 생존자 분석 등 다양한 시각화와 분석을 수행할 수 있습니다.

시계열 데이터는 시간의 경과에 따른 데이터를 포함하며, 시간 순서대로 정렬된 데이터 포인트로 구성됩니다. 예를 들어, `Global Temperature` 데이터셋은 특정 지역의 일별 기온 변화를 기록한 데이터셋으로, 기후 변화와 관련된 시각화에 유용합니다.

범주형 데이터는 고정된 수의 범주로 구성된 데이터입니다. 예를 들어, `Penguins` 데이터셋은 펭귄의 종, 섬, 성별 등을 포함하여 범주형 데이터를 시각화하는 데 자주 사용됩니다.

공간 데이터는 지리적 위치와 관련된 데이터를 포함하며, 지도 시각화에 사용됩니다. 대표적인 예로, `Earthquake` 데이터셋은 지진 발생 위치와 강도를 포함하여 지진의 분포와 패턴을 시각화하는 데 유용합니다.

이미지 데이터는 이미지 파일로 구성된 데이터로, 이미지 분류와 객체 탐지 등의 시각화에 사용됩니다.
예를 들어, `MNIST` 데이터셋은 손글씨 숫자 이미지 데이터셋으로, 이미지 처리와 관련된 다양한 시각화와 분석을 수행할 수 있습니다. `CIFAR-10` 데이터셋은 10개 클래스의 이미지 데이터셋으로, 보다 복잡한 이미지 분류 작업에 사용됩니다.

텍스트 데이터는 텍스트 형식의 데이터를 포함하며, 자연어 처리와 관련된 시각화에 사용됩니다. 예를 들어, `IMDb` 영화 리뷰 데이터셋은 영화 리뷰 텍스트와 평점을 포함하여 텍스트 데이터의 감정 분석과 시각화에 유용합니다.


## 표 형식 데이터 (Tabular Data)

행과 열로 구성된 표 형식의 데이터로, 스프레드시트나 데이터베이스 테이블 형태로 자주 사용됩니다. 각 열은 변수(피처, 특성벡터, `feature` 등으로 부르기도 함)를 나타내고, 각 행은 관측치를 나타냅니다.

- **`Iris` 데이터셋**: 꽃잎과 꽃받침의 길이와 너비를 포함한 간단한 데이터셋 ([download link](https://raw.githubusercontent.com/mwaskom/seaborn-data/master/iris.csv))
- **`Titanic` 데이터셋**: 타이타닉 호의 승객 정보를 포함한 데이터셋 ([download link](https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv))


## 시계열 데이터 (Time Series Data)

시간의 경과에 따른 데이터로, 주로 시간 순서대로 정렬된 데이터 포인트로 구성됩니다. 주식 가격, 기온 변화, 판매 수치 등이 이에 해당합니다.

- **기온 변화 데이터셋**: 특정 지역의 일별 기온 변화를 기록한 데이터셋 ([download link](https://raw.githubusercontent.com/datasets/global-temp/master/data/monthly.csv))
- **주식 가격 데이터셋**: 특정 주식의 일별 종가를 기록한 데이터셋 ([github code](https://github.com/gomjellie/kospi-kosdaq-csv))


## 범주형 데이터 (Categorical Data)

범주형 데이터는 고정된 수의 범주로 구성된 데이터를 말하며, 주로 막대 그래프나 파이 차트로 시각화됩니다.

- **자동차 데이터셋**: 자동차의 종류, 제조사, 연료 타입 등을 포함한 데이터셋 ([Kaggle dataset](https://www.kaggle.com/datasets/jahaidulislam/car-specification-dataset-1945-2020))
- **펭귄 데이터셋**: 펭귄의 종, 섬, 성별 등을 포함한 데이터셋 ([download link](https://raw.githubusercontent.com/mwaskom/seaborn-data/master/penguins.csv))


## 공간 데이터 (Spatial Data)

지리적 위치와 관련된 데이터를 말하며, 주로 지도 시각화에 사용됩니다. 좌표, 지역, 경계선 등의 정보를 포함합니다.

- **지도 데이터셋**: 특정 지역의 지리적 경계 데이터를 포함한 데이터셋 ([geoBoundaries download](https://www.geoboundaries.org/countryDownloads.html))
- **지진 데이터셋**: 지진 발생 위치와 강도를 포함한 데이터셋 ([download link](https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/all_week.csv))

## 이미지 데이터 (Image Data)

이미지 파일로 구성된 데이터로, 이미지 분류, 객체 탐지 등의 시각화에 사용됩니다.

- **`MNIST` 데이터셋**: 손글씨 숫자 이미지 데이터셋 ([download link](http://yann.lecun.com/exdb/mnist/))
- **`CIFAR-10` 데이터셋**: 10개 클래스의 이미지 데이터셋 ([download link](https://www.cs.toronto.edu/~kriz/cifar.html))


## 텍스트 데이터 (Text Data)

텍스트 형식의 데이터로, 자연어 처리와 관련된 시각화에 사용됩니다.

- **뉴스 기사 데이터셋**: 뉴스 기사 텍스트를 포함한 데이터셋 ([공공데이터포털](https://www.data.go.kr/))
- **영화 리뷰 데이터셋**: 영화 리뷰 텍스트와 평점을 포함한 데이터셋 ([download link](https://ai.stanford.edu/~amaas/data/sentiment/))


[맨 위로 이동](05-03)