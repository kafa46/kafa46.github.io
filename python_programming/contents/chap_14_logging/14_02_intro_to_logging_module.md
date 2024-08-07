(14_02)=
# 파이썬 로깅 모듈 소개

파이썬 표준 라이브러리는 다양한 로깅 기능을 제공하는 `logging` 모듈을 포함하고 있습니다. `logging` 모듈은 프로그램의 실행 흐름을 추적하고, 문제를 진단하며, 필요한 정보를 기록하는 데 매우 유용합니다. 이 장에서는 `logging` 모듈의 기본 사용법과 주요 구성 요소를 소개합니다.

## 로깅 모듈의 주요 구성 요소

### 로거(Logger)

로거는 애플리케이션 코드에서 직접 사용하는 인터페이스입니다. 로거를 사용하여 로그 메시지를 생성하고, 로그 레벨을 설정할 수 있습니다.

### 핸들러(Handler)

핸들러는 로그 레코드를 적절한 출력 대상으로 보내는 역할을 합니다. 예를 들어, 콘솔, 파일, 네트워크 등 다양한 출력 대상에 로그를 기록할 수 있습니다.

### 포매터(Formatter)

포매터는 로그 메시지의 형식을 지정하는 역할을 합니다. 시간, 로그 레벨, 메시지 등의 정보를 포함하는 로그 메시지의 형식을 정의할 수 있습니다.

### 필터(Filter)

필터는 특정 기준에 따라 로그 레코드의 처리를 제어합니다. 로그 레코드를 필터링하여 필요한 정보만 로그로 기록할 수 있습니다.

## 기본 사용법

`logging` 모듈을 사용하여 간단한 로그 메시지를 기록하는 방법을 살펴보겠습니다.


## 로그 레벨

로그 레벨은 로그 메시지의 중요도를 나타냅니다. 

`logging` 모듈은 다음과 같은 로그 레벨을 제공합니다:

- `DEBUG`: 디버깅 목적으로 상세한 정보를 기록합니다.

- `INFO`: 일반적인 정보를 기록합니다.

- `WARNING`: 경고 메시지를 기록합니다. 주의가 필요한 상황을 나타냅니다.

- `ERROR`: 오류 메시지를 기록합니다. 애플리케이션 실행에 문제가 있는 상황을 나타냅니다.

- `CRITICAL`: 심각한 오류 메시지를 기록합니다. 즉각적인 조치가 필요한 상황을 나타냅니다.

[맨 위로 이동](14_02)
