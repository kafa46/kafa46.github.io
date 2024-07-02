(07-03)=
# 패키징 및 배포

지금까지 만든 게임을 실행파일로 만들어 보겠습니다.

파이썬 코드로 작성된 게임을 실행 파일로 만드는 방법은 여러 가지가 있지만, `pyinstaller`를 사용하는 방법을 소개합니다. `pyinstaller`는 파이썬 스크립트를 독립 실행형 실행 파일로 변환해 주는 도구입니다.

## PyInstaller 설치

먼저, PyInstaller를 설치해야 합니다. 터미널이나 명령 프롬프트에서 다음 명령을 실행하면 쉽게 설치할 수 있습니다.

```bash
pip install pyinstaller
```

## 파이썬 스크립트를 실행 파일로 변환

작성한 파이썬 스크립트를 실행 파일로 변환해야 합니다. 

예를 들어, 스크립트 파일의 이름이 game.py라고 가정해 보겠습니다.

터미널이나 명령 프롬프트에서 다음 명령을 실행하면 됩니다.

```bash
pyinstaller --onefile game.py
```

아래 그림을 참고해 주세요.

```{figure} ../imgs/chap_07/ch07_03_01_pyinstall_1.png
---
width: 90%
name: ch07_03_01_pyinstall_1
---
pyinstaller를 이용하기 위한 터미널 실행 및 명령어 입력
```

명령어를 실행하면 현재 폴더에 다음과 같은 폴더와 파일이 생성됩니다.
- `build` 폴더: 실행 파일을 만들기 위해 사용한 임시 생성 파일
- `dist` 폴더: 최종 실행 파일이 저장된 폴더
- `script_name.spec` 파일: 실행 파일을 생성하기 위한 명세서(specification, Spec) 내용이 기록됩니다.

아래 그림을 참고하세요.

```{figure} ../imgs/chap_07/ch07_03_02_pyinstall_after.png
---
width: 90%
name: ch07_03_02_pyinstall_after
---
pyinstaller를 이용하기 위한 터미널 실행 및 명령어 입력
```

`build` 폴더와 `.spec` 파일은 삭제해도 무방합니다. `dist` 폴더에 있는 실행 파일을 다른 위치로 옮기거나 친구에게 이메일을 보내도 잘 작동합니다.

```{Warning}
pyinstaller 실행할 때 --onefile 옵션을 사용하지 않은 경우

build 폴더와 .spec 파일은 계속 동일한 폴더에 유지해야 하는 상황이 발생할 수도 있습니다. 자세한 내용은 PyInstaller 공식문서(https://pyinstaller.org/en/stable/)를 참고하기 바랍니다.
```

이 명령은 game.py 스크립트를 한개의 실행 파일로 변환합니다. 

변환이 완료되면 현재 작업 폴더에 `dist` 폴더가 생깁니다. `dist` 폴더 안에 `game`이라는 실행 파일이 생성됩니다.

## 실행 파일 실행

`dist` 디렉토리 안의 실행 파일을 더블 클릭하여 게임을 실행할 수 있습니다.

[맨 위로 이동](07-03)