# 매개변수와 반환값

함수는 입력을 받아 출력을 반환하는 역할을 합니다. 이때 입력을 매개변수(`parameter`)라 하고, 출력을 반환값(`return value`)이라고 합니다.

## 매개변수

매개변수는 함수 정의 시 괄호 안에 작성되며, 함수 호출 시 전달되는 인수(`argument`)로 대체됩니다. 

매개변수를 사용하여 함수 내부에서 다양한 작업을 수행할 수 있습니다.

```python
def greet(name):
    print(f"안녕하세요, {name}님!")
```

## 기본값 매개변수

함수를 정의할 때 매개변수에 기본값을 설정할 수 있습니다. 

기본값이 설정된 매개변수는 함수 호출 시 인수가 전달되지 않으면 기본값이 사용됩니다.

```python
def greet(name, greeting="안녕하세요"):
    print(f"{greeting}, {name}님!")

greet("철수")  # 출력: 안녕하세요, 철수님!
greet("영희", "반갑습니다")  # 출력: 반갑습니다, 영희님!
```

## 가변 인수

함수를 정의할 때 매개변수 앞에 `*`를 붙이면 가변 인수를 받을 수 있습니다. 

가변 인수는 튜플로 전달됩니다.

```python
def add_all(*args):
    total = 0
    for num in args:
        total += num
    return total

print(add_all(1, 2, 3))  # 출력: 6
print(add_all(1, 2, 3, 4, 5))  # 출력: 15
```

## 키워드 인수

함수를 정의할 때 매개변수 앞에 `**`를 붙이면 키워드 인수를 받을 수 있습니다. 

키워드 인수는 딕셔너리로 전달됩니다.

```python
def print_info(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

print_info(name="철수", age=30, city="서울")

# 출력:
# name: 철수
# age: 30
# city: 서울
```
