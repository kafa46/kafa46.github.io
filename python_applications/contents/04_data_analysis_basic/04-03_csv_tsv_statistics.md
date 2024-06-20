(04-03)=
# 기본 데이터 분석

컴퓨터가 관리하는 데이터는 `CSV` 또는 `TSV` 형태로 관리되는 경우가 많습니다. CSV와 TSV는 모두 데이터를 저장하고 교환하는 데 매우 유용한 형식입니다. CSV는 더 널리 사용되지만, TSV는 필드 값에 콤마가 포함된 경우 더 유리할 수 있습니다. 적절한 형식을 선택하는 것은 데이터의 특성과 사용 목적에 따라 달라집니다.

## CSV (Comma-Separated Values)

CSV 파일은 콤마(,)로 구분된 데이터를 저장하는 파일 형식입니다. 각 줄은 데이터 레코드를 나타내며, 각 레코드는 쉼표로 구분된 필드(열)로 구성됩니다. CSV 파일은 간단하고 널리 사용되며, 다양한 프로그램에서 지원됩니다.

**특징**

- 구분자: 콤마(,).
- 사용 사례: 스프레드시트 프로그램(예: MS Excel, Google Sheets), DBMS, 데이터 분석 도구 등
- 장점: 간단한 구조, 다양한 애플리케이션에서 쉽게 사용 가능
- 단점: 데이터에 콤마가 포함될 경우 이스케이프(제거 또는 다른 문자로 치환) 처리가 필요
- 데이터 예시
    ```markdown
    Name,Age,City
    John,28,New York
    Anna,24,Paris
    Peter,35,Berlin
    Linda,32,London
    ```

## TSV (Tab-Separated Values)

TSV 파일은 탭(tab) 문자로 구분된 데이터를 저장하는 파일 형식입니다. CSV와 유사하게, 각 줄은 데이터 레코드를 나타내며, 각 레코드는 탭 문자 (`\t`)로 구분된 필드로 구성됩니다. TSV 파일은 특히 텍스트 편집기와 스프레드시트 프로그램에서 쉽게 읽을 수 있습니다.

**특징**

- 구분자: 탭 문자(`\t`)
- 사용 사례: 스프레드시트 프로그램, DBMS, 데이터 분석 도구 등
- 장점: 필드 값에 콤마가 포함되어도 문제가 되지 않음, 구분자가 명확하여 가독성 높음
- 단점: CSV에 비해 덜 일반적이며, 일부 애플리케이션에서는 기본적으로 지원하지 않을 수 있음
- 데이터 예시
    ```markdown
    Name    Age    City
    John    28    New York
    Anna    24    Paris
    Peter    35    Berlin
    Linda    32    London
    ```

## 파일 데이터 불러오기

파일을 읽어오려면 `pandas`의  `read_csv()` 메서드를 사용하면 됩니다. 파일에서 데이터를 읽어오면  데이터 프레임으로 리턴합니다.

자세한 사용법은 [pandas.read_dsv](https://pandas.pydata.org/docs/reference/api/pandas.read_csv.html#pandas-read-csv)를 참고하면 됩니다.

`read_csv()` 메서드 파라미터는 2개만 신경쓰면 됩니다.
```python
import pandas as pd

pd.read_csv('filepath_or_buffer', sep=',')
```
- `'filepath_or_buffer'`: 파일 이름입니다. 만약 파일 내용이 메인 메모리에 적재되고 변수로 관리되고 있다면 변수 이름을 입력하면 됩니다.
- `sep`는 구분자를 의미합니다. 기본값은 콤마(`,`) 입니다. 아무것도 입력하지 않으면 콤마를 기준으로 데이터 열을 구분합니다. `CSV` 파일은 콤마로 구분되기 때문에 별도로 입력할 필요가 없습니다. `TSV` 파일은 탭으로 구분하기 때문에 `sep='\t'`라고 입력해 주어야 합니다.

```python
import pandas as pd

# CSV 파일을 읽어 데이터 프레임으로 변환
df = pd.read_csv('data.tsv', sep=',') # sep=',' 생략 가능

# TSV 파일을 읽어 데이터 프레임으로 변환
df = pd.read_csv('data.tsv', sep='\t')

# 데이터 프레임 출력
print(df.head())
```
## 데이터 분석

### 데이터 탐색

**데이터의 기본 정보를 확인하고, 통계 요약을 출력하기**

```python
# 데이터 프레임의 정보 출력
print(df.info())

# 데이터 프레임의 통계 요약 출력
print(df.describe())

# 첫 n개 데이터만 보기
print(pd.head(5)) # 첫 5줄만 보기

# 마지막 n개 데이터만 보기
print(pd.tail(7)) # 마지막 7줄만 보기
```

### 데이터 선택 및 필터링

특정 열을 선택하고, 조건에 맞는 데이터를 필터링합니다.

```python
# 특정 열 선택
names = df['Name']
print(names)

# 조건에 맞는 데이터 필터링 (예: Age가 30보다 큰 경우)
adults = df[df['Age'] > 30]
print(adults)
```

### 데이터 정렬

특정 열을 기준으로 데이터를 정렬합니다.

```python
# Age 열을 기준으로 데이터 정렬
sorted_df = df.sort_values(by='Age')
print(sorted_df)
```

### 데이터 그룹화 및 집계

특정 열을 기준으로 데이터를 그룹화하고, 집계 연산을 수행합니다.

```python
# Country 열을 기준으로 데이터 그룹화 후 평균값 계산
grouped = df.groupby('Country').mean()
print(grouped)
```

### 서로 다른 데이터 합치기(병합)

`pandas.merge()` 메서드를 이용하면 서로 다른 데이터 테이블을 합칠 수 있습니다.

자세한 내용은 [pandas.merge()](https://pandas.pydata.org/docs/reference/api/pandas.merge.html#pandas.merge)를 참고하세요.

데이터 프레임(데이터베이스의 경우 DB Table)을 병합하는 방법은 다양합니다. 대표적으로는 `merge()`, `join()`, `concatenate()`, `stack()` 등이 있습니다.

그림을 이용한 간단한 설명은 [여기를 클릭](https://pandas.pydata.org/docs/user_guide/merging.html#merge)하면 확인할 수 있습니다.

우리는 `merge()` 메서드를 활용하여 2개 데이터 테이블을 합치는 실습을 간단하게 해 보겠습니다.

아래 코드는 2개의 데이터 프레임을 `EmployeeID`라는 컬럼명(column name) 기준으로 병합하는 코드입니다.

```python
import pandas as pd
import matplotlib.pyplot as plt

# 1. 데이터 로드
employees = pd.read_csv('employees.csv')
sales = pd.read_csv('sales.tsv', sep='\t')

# 2. 데이터 탐색
print(employees.head())
print(sales.head())
print(employees.info())
print(sales.info())

# 3. 데이터 병합
merged_data = pd.merge(employees, sales, on='EmployeeID')
print(merged_data.head())
```

### 데이터 시각화
Matplotlib과 통합하여 데이터를 시각화할 수 있습니다.

```python
import matplotlib.pyplot as plt

# Age 열의 히스토그램 그리기
df['Age'].hist()
plt.xlabel('Age')
plt.ylabel('Frequency')
plt.title('Age Distribution')
plt.show()
```

### 전체 예제 코드

아래는 위의 모든 단계를 포함한 전체 예제 코드입니다.

```python
import pandas as pd
import matplotlib.pyplot as plt

# 1. TSV 파일을 읽어 데이터 프레임으로 변환
df = pd.read_csv('data.tsv', sep='\t')
print(df.head())

# 2. 데이터 탐색
print(df.info())
print(df.describe())

# 3. 데이터 선택 및 필터링
names = df['Name']
print(names)
adults = df[df['Age'] > 30]
print(adults)

# 4. 데이터 정렬
sorted_df = df.sort_values(by='Age')
print(sorted_df)

# 5. 데이터 그룹화 및 집계
grouped = df.groupby('Country').mean()
print(grouped)

# 6. 데이터 시각화
df['Age'].hist()
plt.xlabel('Age')
plt.ylabel('Frequency')
plt.title('Age Distribution')
plt.show()
```

[맨 위로 이동](04-03)
