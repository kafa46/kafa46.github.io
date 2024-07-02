(14_06)=
# 연습 문제

1. **기본 로깅 설정**
    - 로깅을 사용하여 콘솔에 다음과 같은 로그 메시지를 출력하는 프로그램을 작성하세요.
        - `DEBUG` 레벨: "This is a debug message"
        - `INFO` 레벨: "This is an info message"
        - `WARNING` 레벨: "This is a warning message"
        - `ERROR` 레벨: "This is an error message"
        - `CRITICAL` 레벨: "This is a critical message"

    ```python
    import logging

    logging.basicConfig(level=logging.DEBUG,
                        format='%(asctime)s - %(levelname)s - %(message)s',
                        datefmt='%Y-%m-%d %H:%M:%S')

    logging.debug("This is a debug message")
    logging.info("This is an info message")
    logging.warning("This is a warning message")
    logging.error("This is an error message")
    logging.critical("This is a critical message")
    ```

2. **파일에 로그 기록하기**
    - 로그 메시지를 `application.log` 파일에 기록하는 프로그램을 작성하세요. 로그 레벨은 `INFO`로 설정하세요.

    ```python
    import logging

    logging.basicConfig(filename='application.log', level=logging.INFO,
                        format='%(asctime)s - %(levelname)s - %(message)s',
                        datefmt='%Y-%m-%d %H:%M:%S')

    logging.info("This is an info message")
    logging.warning("This is a warning message")
    logging.error("This is an error message")
    ```

3. **포매터 사용하기**
    - 로그 메시지를 다음 형식으로 출력하는 프로그램을 작성하세요.
        - `2024-01-01 12:00:00 - example_logger - DEBUG - This is a debug message`

    ```python
    import logging

    # 로거 생성
    logger = logging.getLogger('example_logger')
    logger.setLevel(logging.DEBUG)

    # 콘솔 핸들러 생성
    console_handler = logging.StreamHandler()

    # 포매터 생성 및 설정
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                                  datefmt='%Y-%m-%d %H:%M:%S')
    console_handler.setFormatter(formatter)

    # 핸들러를 로거에 추가
    logger.addHandler(console_handler)

    # 로그 메시지 생성
    logger.debug("This is a debug message")
    ```

4. **파일 핸들러와 콘솔 핸들러 사용하기**
    - 로그 메시지를 콘솔과 `application.log` 파일에 모두 기록하는 프로그램을 작성하세요. 콘솔에는 `DEBUG` 레벨 이상의 메시지를, 파일에는 `INFO` 레벨 이상의 메시지를 기록하세요.

    ```python
    import logging

    # 로거 생성
    logger = logging.getLogger('example_logger')
    logger.setLevel(logging.DEBUG)

    # 콘솔 핸들러 생성 및 설정
    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.DEBUG)

    # 파일 핸들러 생성 및 설정
    file_handler = logging.FileHandler('application.log')
    file_handler.setLevel(logging.INFO)

    # 포매터 생성 및 설정
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                                  datefmt='%Y-%m-%d %H:%M:%S')
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

5. **설정 파일 사용하기 (INI 형식)**
    - INI 형식의 로깅 설정 파일을 작성하고, 이를 사용하여 로깅을 설정하는 프로그램을 작성하세요. 설정 파일 이름은 `logging.ini`로 하세요.

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

6. **설정 파일 사용하기 (YAML 형식)**
    - YAML 형식의 로깅 설정 파일을 작성하고, 이를 사용하여 로깅을 설정하는 프로그램을 작성하세요. 설정 파일 이름은 `logging.yaml`로 하세요.

    ```yaml
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

이 연습 문제들을 통해 학생들은 파이썬의 `logging` 모듈을 사용하여 다양한 방식으로 로깅을 설정하고, 로그 메시지를 기록하는 방법을 익힐 수 있습니다. 각 문제에 대한 답을 작성하여 제출하세요.

[맨 위로 이동](14_06)
