(12_00)=
# 예외 처리

파이썬 예외처리는 프로그램 실행 중 발생할 수 있는 오류(예외)를 처리하여 프로그램이 중단되지 않고 계속 실행될 수 있도록 하는 기법입니다. 
예외는 파일을 열 수 없는 경우, `0`으로 나누려는 시도, 배열의 범위를 벗어난 인덱스 접근 등 다양한 상황에서 발생할 수 있습니다. 파이썬에서는 이러한 예외를 처리하기 위해 `try`, `except`, `else`, `finally` 구문을 제공합니다.

```{figure} ../images/12_00_1_exceptions.webp
---
width: 400px
name: 12_00_1_exceptions
---
난 예외 없는 완전한 인생이 좋아요!!! <br>
그런데 항상 예외를 만나게 될거라구요???
```


우리가 모든 예외 상황을 알 수는 없습니다.
하지만, 대부분의 예외를 예상해 볼 수 있습니다.

프로그래머가 예측할 수 있는 에러를 적절히 처리해서 프로그램의 품질을 높이는 작업을 `에러 처리` 또는 `Error Handling`이라고 부릅니다.

우리는 이번 장을 공부함으로써 개발자다운 개발자에 더욱 다가설 것입니다.


[맨 위로 이동](12_00)

