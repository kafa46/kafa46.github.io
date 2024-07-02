(14_05)=
# 로깅 설정 파일 사용

파이썬의 `logging` 모듈은 설정 파일을 사용하여 로깅을 구성할 수 있습니다. 설정 파일을 사용하면 로깅 구성을 코드에서 분리하여 관리할 수 있으며, 로깅 구성을 쉽게 변경할 수 있습니다. 설정 파일은 INI 형식 또는 YAML 형식으로 작성할 수 있으며, 이를 파이썬 코드에서 읽어 로깅 구성을 적용할 수 있습니다.

## `INI` 형식 설정 파일 사용

### `INI` 파일이란?

`INI` 파일은 구성 파일의 한 종류로, 단순한 `키-값` 쌍을 포함하는 텍스트 파일입니다.

주로 소프트웨어 설정을 저장하는 데 사용됩니다.

`INI` 파일은 일반적으로 세션, 키, 값의 구조를 따르며, 각 세션은 키와 값을 포함할 수 있습니다.

- `INI` 파일 구조
  - `INI` 파일은 섹션(Section), 속성(Property), 값(Value)으로 구성됩니다.
  - 각 섹션은 대괄호 `[]`로 묶이며, 그 안에 `키-값` 쌍이 위치합니다.
  - 속성(Property)와 값(Value): 각 속성은 `키-값` 쌍으로 표현되며, 등호 `=` 또는 콜론 `:`으로 구분됩니다.
  - 주석은 `;` 또는 `#`로 시작하며, 해당 줄의 끝까지 주석으로 처리됩니다.
  - 작성 예시
    ```ini
    ; This is a comment
    # This is also a comment
    [general]
    appname = My Application
    version = 1.0

    [database]
    server = localhost
    port = 3306
    username = root
    password = password123
    ```

- 파이썬에서는 `configparser` 모듈을 사용하여 `INI` 파일을 읽고 쓸 수 있습니다.
  - `INI` 읽기(파싱) 예시
    ```python
    import configparser

    config = configparser.ConfigParser()
    config.read('config.ini')

    appname = config['general']['appname']
    version = config['general']['version']
    server = config['database']['server']

    print(f"App Name: {appname}")
    print(f"Version: {version}")
    print(f"Database Server: {server}")
    ```
  - `INI` 쓰기 예시
    ```python
    import configparser

    config = configparser.ConfigParser()

    config['general'] = {
        'appname': 'My Application',
        'version': '1.0'
    }

    config['database'] = {
        'server': 'localhost',
        'port': '3306',
        'username': 'root',
        'password': 'password123'
    }

    with open('config.ini', 'w') as configfile:
        config.write(configfile)
    ```

### (실습) `INI` 로깅 설정 작성

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

### (실습) `INI` 설정파일 적용

설정 파일을 읽어 로깅 구성을 적용하려면 `logging.config` 모듈을 사용합니다.

다음 코드는 `logging.config.fileConfig` 함수를 사용하여 `logging.ini` 파일을 읽고 로깅 구성을 적용합니다.

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

## `YAML` 형식 사용

### `YAML` 이란?

`YAML`은 "YAML Ain't Markup Language"의 약자로, 사람이 읽기 쉬운 데이터 직렬화 형식입니다.

주로 구성 파일과 데이터 교환을 위해 사용됩니다.

`YAML`은 `JSON` 보다 가독성이 높고, 복잡한 데이터 구조를 쉽게 표현할 수 있습니다.

  - 참고: `JSON` (JavaScript Obejct Notation): `Javascript` 문법으로 데이터를 표현하는 방법


- `YAML` 파일 구조
  - `YAML` 파일은 들여쓰기를 사용하여 계층적 구조를 표현합니다.
  - `공백` 또는 `탭` 문자를 사용하여 들여쓰기 할 수 있지만, 일반적으로 `공백`을 사용합니다.
  - 콜론(`:`)을 사용하여 `키-값` 쌍을 정의합니다.
  - `키-값` 쌍(Key-Value Pair): `YAML`에서는 콜론(`:`)을 사용하여 키와 값을 구분
  - 리스트(`List`): 하이픈(`-`)을 사용하여 리스트 항목을 정의
  - 주석(`Comment`): 해시 기호(`#`)를 사용하여 주석 작성
  - 작성 예시
    ```yaml
    general:
      appname: My Application
      version: 1.0

    database:
      server: localhost
      port: 3306
      username: root
      password: password123

    # 리스트 데이터 표현
    servers:
      - name: server1
        ip: 192.168.1.1
      - name: server2
        ip: 192.168.1.2
    ```

- 파이썬에서는 `yaml` 모듈을 사용하여 `YAML` 파일을 읽고 쓸 수 있습니다.

  - `YAML` 읽기(파싱) 예시
    ```python
    import yaml

    with open('config.yaml', 'r') as file:
        config = yaml.safe_load(file)

    appname = config['general']['appname']
    version = config['general']['version']
    server = config['database']['server']

    print(f"App Name: {appname}")
    print(f"Version: {version}")
    print(f"Database Server: {server}")
    ```

  - `YAML` 쓰기 예시
    ```python
    import yaml

    config = {
        'general': {
            'appname': 'My Application',
            'version': '1.0'
        },
        'database': {
            'server': 'localhost',
            'port': 3306,
            'username': 'root',
            'password': 'password123'
        }
    }

    with open('config.yaml', 'w') as file:
        yaml.dump(config, file)
    ```

### (실습) `YAML` 로깅 설정 작성

로깅 설정을 `YAML` 형식으로 작성합니다.

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

### (실습) `YAML` 설정파일 적용

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

[맨 위로 이동](14_05)

