# 로깅 설정 파일 사용

파이썬의 `logging` 모듈은 설정 파일을 사용하여 로깅을 구성할 수 있습니다. 설정 파일을 사용하면 로깅 구성을 코드에서 분리하여 관리할 수 있으며, 로깅 구성을 쉽게 변경할 수 있습니다. 설정 파일은 INI 형식 또는 YAML 형식으로 작성할 수 있으며, 이를 파이썬 코드에서 읽어 로깅 구성을 적용할 수 있습니다.

## `ini` 형식 설정 파일 사용

### `ini` 설정 파일 작성

로깅 설정을 INI 형식으로 작성합니다. 

파일 이름은 `logging.ini`로 하겠습니다.

```ini
[loggers]
keys=root,exampleLogger

[handlers]
keys=consoleHandler,fileHandler

[formatters]
keys=exampleFormatter

[logger_root]
level=DEBUG
handlers=consoleHandler

[logger_exampleLogger]
level=DEBUG
handlers=consoleHandler,fileHandler
qualname=exampleLogger
propagate=0

[handler_consoleHandler]
class=StreamHandler
level=DEBUG
formatter=exampleFormatter
args=(sys.stdout,)

[handler_fileHandler]
class=FileHandler
level=INFO
formatter=exampleFormatter
args=('example.log', 'w')

[formatter_exampleFormatter]
format=%(asctime)s - %(name)s - %(levelname)s - %(message)s
datefmt=%Y-%m-%d %H:%M:%S
```

### `ini` 설정파일 적용

설정 파일을 읽어 로깅 구성을 적용하려면 `logging.config` 모듈을 사용합니다.

다음 코드는 logging.config.fileConfig 함수를 사용하여 logging.ini 파일을 읽고 로깅 구성을 적용합니다.

```python
import logging
import logging.config

# 설정 파일 읽기
logging.config.fileConfig('logging.ini')

# 로거 생성
logger = logging.getLogger('exampleLogger')

# 로그 메시지 생성
logger.debug("This is a debug message")
logger.info("This is an info message")
logger.warning("This is a warning message")
logger.error("This is an error message")
logger.critical("This is a critical message")
```

## `yaml` 형식 사용

### `yaml` 설정 파일 작성

로깅 설정을 YAML 형식으로 작성합니다. 

파일 이름은 `logging.yaml`로 하겠습니다.

```yaml
코드 복사
version: 1
disable_existing_loggers: False

loggers:
  exampleLogger:
    level: DEBUG
    handlers: [consoleHandler, fileHandler]
    propagate: no

handlers:
  consoleHandler:
    class: logging.StreamHandler
    level: DEBUG
    formatter: exampleFormatter
    stream: ext://sys.stdout

  fileHandler:
    class: logging.FileHandler
    level: INFO
    formatter: exampleFormatter
    filename: example.log
    mode: w

formatters:
  exampleFormatter:
    format: '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    datefmt: '%Y-%m-%d %H:%M:%S'
```

### `yaml` 설정파일 적용

설정 파일을 읽어 로깅 구성을 적용하려면 `yaml` 모듈과 `logging.config` 모듈을 사용합니다.

아래  예제에서는 `yaml.safe_load` 함수를 사용하여 `logging.yaml` 파일을 읽고, `logging.config.dictConfig` 함수를 사용하여 로깅 구성을 적용합니다.

```python
import logging
import logging.config
import yaml

# 설정 파일 읽기
with open('logging.yaml', 'r') as f:
    config = yaml.safe_load(f.read())
    logging.config.dictConfig(config)

# 로거 생성
logger = logging.getLogger('exampleLogger')

# 로그 메시지 생성
logger.debug("This is a debug message")
logger.info("This is an info message")
logger.warning("This is a warning message")
logger.error("This is an error message")
logger.critical("This is a critical message")
```