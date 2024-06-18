(14_03)=
# 기본 로깅 설정

파이썬의 `logging` 모듈을 사용하여 로깅을 설정하는 기본 방법을 알아보겠습니다. 기본 로깅 설정은 `logging.basicConfig()` 함수를 사용하여 간단하게 설정할 수 있습니다.

## 기본 설정

`logging.basicConfig()` 함수를 사용하여 기본적인 로깅 설정을 할 수 있습니다. 이 함수는 로그 메시지를 기록할 때 사용할 로거, 핸들러, 포매터를 자동으로 구성합니다.

## 예제: 기본 설정

다음 코드에서 `basicConfig` 함수는 로그 레벨을 `DEBUG`로 설정하여 모든 레벨의 로그 메시지를 기록

```python
import logging

# 기본 설정
logging.basicConfig(level=logging.DEBUG)

# 로그 메시지 생성
logging.debug("This is a debug message")
logging.info("This is an info message")
logging.warning("This is a warning message")
logging.error("This is an error message")
logging.critical("This is a critical message")
### 기본 설정
```

## 매개변수

`logging.basicConfig()` 함수는 다양한 매개변수를 통해 로깅 설정을 세부 조정할 수 있습니다.

- `filename`: 로그 메시지를 기록할 파일 이름을 지정

- `filemode`: 로그 파일을 열 때 사용할 모드를 지정. 기본값은 `a (append)`이며, `w (write)`로 설정하면 파일을 덮어씁니다.

- `format`: 로그 메시지의 형식을 지정

- `datefmt`: 로그 메시지의 날짜 형식을 지정

- `level`: 로그 레벨을 지정

- `stream`: 로그 메시지를 출력할 스트림을 지정. `sys.stdout` 또는 `sys.stderr`을 사용할 수 있습니다.

## 예제: 파일에 로그 기록

`basicConfig` 함수는 로그 메시지를 `app.log` 파일에 기록하고, 파일 모드를 `w`로 설정하여 파일을 덮어씁니다. 

로그 메시지의 형식과 날짜 형식도 지정합니다.

```python
import logging

# 파일에 로그 기록 설정
logging.basicConfig(filename='app.log', filemode='w', level=logging.DEBUG,
                    format='%(asctime)s - %(levelname)s - %(message)s',
                    datefmt='%Y-%m-%d %H:%M:%S')

# 로그 메시지 생성
logging.debug("This is a debug message")
logging.info("This is an info message")
logging.warning("This is a warning message")
logging.error("This is an error message")
logging.critical("This is a critical message")
```


## 로그 메시지 형식

`format` 매개변수를 사용하여 로그 메시지의 형식을 지정할 수 있습니다. 

다음은 로그 메시지 형식에서 사용할 수 있는 일부 포맷 문자열입니다:

- `%(asctime)s`: 로그 메시지가 생성된 시간

- `%(levelname)s`: 로그 레벨 이름

- `%(message)s`: 로그 메시지

- `%(filename)s`: 로그 메시지를 생성한 소스 파일 이름

- `%(funcName)s`: 로그 메시지를 생성한 함수 이름

- `%(lineno)d`: 로그 메시지를 생성한 소스 파일의 라인 번호

- `%(name)s`: 로거 이름


## 예제: 로그 메시지 형식 지정

다음 코드에서 로그 메시지는 시간, 로거 이름, 로그 레벨, 메시지 순서로 출력됩니다.

```python
import logging

# 로그 메시지 형식 지정
logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

# 로그 메시지 생성
logging.debug("This is a debug message")
logging.info("This is an info message")
logging.warning("This is a warning message")
logging.error("This is an error message")
logging.critical("This is a critical message")
```

## 날짜 형식

`datefmt` 매개변수를 사용하여 로그 메시지의 날짜 형식을 지정할 수 있습니다. 

날짜 형식은 `strftime` 형식을 따릅니다.

## 예제: 날짜 형식 지정

다음 코드 에서 날짜 형식은 `YYYY-MM-DD HH:MM:SS` 형식으로 지정됩니다.

```python
import logging

# 날짜 형식 지정
logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(levelname)s - %(message)s',
                    datefmt='%Y-%m-%d %H:%M:%S')

# 로그 메시지 생성
logging.debug("This is a debug message")
logging.info("This is an info message")
logging.warning("This is a warning message")
logging.error("This is an error message")
logging.critical("This is a critical message")
```

[맨 위로 이동](14_03)

