(14_04)=
# 핸들러(Handler)와 포매터(Formatter)

파이썬의 `logging` 모듈은 핸들러(`Handler`)와 포매터(`Formatter`)를 사용하여 유연하고 강력한 로깅 기능을 제공합니다. 이 장에서는 핸들러와 포매터의 역할과 이를 사용하여 로깅을 설정하는 방법을 알아보겠습니다.

## 핸들러(Handler)

핸들러는 로그 레코드를 적절한 출력 대상으로 보내는 역할을 합니다. 로거(`Logger`)와 함께 사용되며, 다양한 출력 대상을 지원합니다. 핸들러는 여러 종류가 있으며, 한 로거에 여러 핸들러를 추가할 수 있습니다.

## 주요 핸들러 종류

- `StreamHandler`: 콘솔에 로그 메시지를 출력합니다.
- `FileHandler`: 파일에 로그 메시지를 기록합니다.
- `RotatingFileHandler`: 파일 크기가 일정 크기를 초과하면 새 파일로 로그를 기록합니다.
- `SMTPHandler`: 이메일을 통해 로그 메시지를 전송합니다.
- `HTTPHandler`: HTTP를 통해 로그 메시지를 전송합니다.

## 핸들러 설정 예제

로거에 핸들러를 추가하여 로그 메시지를 다양한 출력 대상으로 보낼 수 있습니다.

다음 코드에서 로거는 콘솔과 파일에 로그 메시지를 기록합니다. 

콘솔 핸들러는 모든 로그 레벨의 메시지를 출력하며, 파일 핸들러는 `INFO` 이상의 로그 메시지를 기록합니다.

```python
import logging

# 로거 생성
logger = logging.getLogger('example_logger')
logger.setLevel(logging.DEBUG)

# 콘솔 핸들러 생성 및 설정
console_handler = logging.StreamHandler()
console_handler.setLevel(logging.DEBUG)

# 파일 핸들러 생성 및 설정
file_handler = logging.FileHandler('example.log')
file_handler.setLevel(logging.INFO)

# 핸들러를 로거에 추가
logger.addHandler(console_handler)
logger.addHandler(file_handler)

# 로그 메시지 생성
logger.debug("This is a debug message")
logger.info("This is an info message")
logger.warning("This is a warning message")
logger.error("This is an error message")
logger.critical("This is a critical message")
```


## 포매터(Formatter)

포매터는 로그 메시지의 형식을 지정하는 역할을 합니다. 

포매터를 사용하여 로그 메시지에 시간, 로그 레벨, 메시지 등을 포함할 수 있습니다.

## 포매터 생성 및 설정

포매터는 `logging.Formatter` 클래스를 사용하여 생성할 수 있습니다. 

포매터는 핸들러에 설정되어 로그 메시지의 형식을 지정합니다.

```python
# 포매터 생성
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

# 핸들러에 포매터 설정
console_handler.setFormatter(formatter)
file_handler.setFormatter(formatter)
```

## 종합 예제

로거, 핸들러, 포매터를 사용하여 종합적으로 로깅을 설정하는 예제를 살펴보겠습니다.

다음 예제에서는 다음과 같은 작업을 수행합니다:

- `example_logger`라는 이름의 로거를 생성하고 로그 레벨을 `DEBUG`로 설정합니다.
- 콘솔 핸들러와 파일 핸들러를 생성하고, 각각의 로그 레벨을 설정합니다.
- 포매터를 생성하고, 핸들러에 설정합니다.
- 핸들러를 로거에 추가합니다.
- 다양한 로그 레벨의 로그 메시지를 생성합니다.


```python
import logging

# 로거 생성
logger = logging.getLogger('example_logger')
logger.setLevel(logging.DEBUG)

# 콘솔 핸들러 생성 및 추가
console_handler = logging.StreamHandler()
console_handler.setLevel(logging.DEBUG)

# 파일 핸들러 생성 및 추가
file_handler = logging.FileHandler('example.log')
file_handler.setLevel(logging.INFO)

# 포매터 생성 및 설정
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
console_handler.setFormatter(formatter)
file_handler.setFormatter(formatter)

# 핸들러를 로거에 추가
logger.addHandler(console_handler)
logger.addHandler(file_handler)

# 로그 메시지 생성
logger.debug("This is a debug message")
logger.info("This is an info message")
logger.warning("This is a warning message")
logger.error("This is an error message")
logger.critical("This is a critical message")
```

## 추가 핸들러 및 포매터 설정 예제

`RotatingFileHandler`는 파일 크기가 일정 크기를 초과하면 새 파일로 로그를 기록하는 핸들러입니다.

아래 코드에서 `RotatingFileHandler`는 파일 크기가 `2,000` 바이트를 초과하면 새 파일로 로그를 기록하며, 최대 5개의 백업 파일을 유지합니다.

```python
import logging
from logging.handlers import RotatingFileHandler

# 로거 생성
logger = logging.getLogger('rotating_logger')
logger.setLevel(logging.DEBUG)

# RotatingFileHandler 생성
rotating_handler = RotatingFileHandler('rotating.log', maxBytes=2000, backupCount=5)
rotating_handler.setLevel(logging.INFO)

# 포매터 생성 및 설정
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
rotating_handler.setFormatter(formatter)

# 핸들러를 로거에 추가
logger.addHandler(rotating_handler)

# 로그 메시지 생성
for i in range(100):
    logger.info(f"This is log message {i}")
```


[맨 위로 이동](14_04)

