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

# 4. 데이터 분석
avg_age_by_department = merged_data.groupby('Department')['Age'].mean()
print(avg_age_by_department)

avg_sales_by_jobtitle = merged_data.groupby('JobTitle')['SalesAmount'].mean()
print(avg_sales_by_jobtitle)

total_sales_by_country = merged_data.groupby('Country')['SalesAmount'].sum()
print(total_sales_by_country)

# 5. 데이터 시각화
# 월별 총 판매 금액 시각화
monthly_sales = merged_data.groupby('Month')['SalesAmount'].sum()
monthly_sales.plot(kind='line')
plt.xlabel('Month')
plt.ylabel('Total Sales')
plt.title('Monthly Total Sales')
plt.show()

# 부서별 평균 연령 시각화
avg_age_by_department.plot(kind='bar')
plt.xlabel('Department')
plt.ylabel('Average Age')
plt.title('Average Age by Department')
plt.show()

# 국가별 총 판매 금액 시각화
total_sales_by_country.plot(kind='pie', autopct='%1.1f%%')
plt.title('Total Sales by Country')
plt.show()

```