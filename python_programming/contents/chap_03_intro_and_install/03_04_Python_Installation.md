(03_04)=
# 파이썬 설치 방법

파이썬을 설치하는 방법은 사용하는 운영체제에 따라 다를 수 있습니다. 이 장에서는 윈도우, macOS, 리눅스에서 파이썬을 설치하는 방법을 단계별로 설명하겠습니다.

## 윈도우에서 파이썬 설치

1. **파이썬 다운로드**
   - [파이썬 공식 웹사이트](https://www.python.org/)에 접속합니다.
   - 상단 메뉴에서 "Downloads"를 클릭한 후 "Download for Windows" 버튼을 클릭하여 최신 버전의 파이썬 설치 파일을 다운로드합니다.

2. **설치 파일 실행**
   - 다운로드한 설치 파일을 실행합니다.
   - 설치 화면에서 "Add Python to PATH" 옵션을 체크한 후 "Install Now"를 클릭합니다.

3. **설치 확인**
  설치가 완료되면 명령 프롬프트(cmd)를 열어 `python --version`을 입력하여 파이썬이 정상적으로 설치되었는지 확인합니다.

   ```sh
   python --version
   ```

## macOS에서 파이썬 설치

1. **파이썬 다운로드**
   - [파이썬 공식 웹사이트](https://www.python.org/)에 접속합니다.
   - 상단 메뉴에서 "Downloads"를 클릭한 후 "Download for macOS" 버튼을 클릭하여 최신 버전의 파이썬 설치 파일을 다운로드합니다.

2. **설치 파일 실행**
   - 다운로드한 설치 파일(.pkg)을 실행합니다.
   - 설치 마법사의 지시에 따라 파이썬을 설치합니다.

3. **설치 확인**
   - 터미널을 열어 `python3 --version`을 입력하여 파이썬이 정상적으로 설치되었는지 확인합니다.

   ```sh
   python3 --version
   ```

## 리눅스에서 파이썬 설치

리눅스 배포판에 따라 파이썬 설치 방법이 다를 수 있습니다. 여기서는 Ubuntu를 기준으로 설명하겠습니다.

1. **패키지 업데이트**
   터미널을 열고 아래 명령어를 입력하여 패키지 목록을 업데이트합니다.

   ```sh
   sudo apt update
   ```

2. **파이썬 설치**

   다음 명령어를 입력하여 파이썬을 설치합니다.

   ```sh
   sudo apt install python3
   ```

3. **설치 확인**
   설치가 완료되면 `python3 --version`을 입력하여 파이썬이 정상적으로 설치되었는지 확인합니다.

   ```sh
   python3 --version
   ```

## 파이썬 패키지 관리자(`pip`) 설치

`pip`는 "Pip Installs Packages"의 약자로, 파이썬 패키지 관리 도구입니다. 자세한 내용은 [pip 홈페이지](https://pip.pypa.io/en/stable/)에서 확인할 수 있습니다.

`pip`를 사용하면 파이썬 패키지 인덱스([PyPI](https://pypi.org/))에 등록된 다양한 파이썬 패키지를 쉽게 설치, 업데이트 및 삭제할 수 있습니다.

   ```{admonition} pip와 PyPI의 관계

      - PyPI: 사용자들이 만든 파이썬 패키지를 저장한 창고(게시판)

      - pip: PyPI에 저장된 패키지를 설치/업그레이드/제거 등을 자동으로 해주는 소프트웨어
   ```

- 주요 기능
  - **패키지 설치**: pip를 사용하여 PyPI에서 원하는 패키지를 설치할 수 있습니다.
  - **패키지 업그레이드**: 설치된 패키지를 최신 버전으로 업그레이드할 수 있습니다.
  - **패키지 제거**: 더 이상 필요 없는 패키지를 제거할 수 있습니다.
  - **패키지 목록 확인**: 현재 설치된 패키지 목록을 확인할 수 있습니다.
  - **요구사항 파일 사용**: 여러 패키지를 한 번에 설치하기 위해 요구사항 파일을 사용할 수 있습니다.


- 주요 명령어
  - **패키지 설치**: `pip install package_name`
  - **패키지 업그레이드**: `pip install --upgrade package_name`
  - **패키지 제거**: `pip uninstall package_name`
  - **설치된 패키지 목록**: `pip list`
  - **요구사항 파일에서 설치**: `pip install -r requirements.txt`


최신 파이썬 버전에는 기본적으로 pip가 포함되어 있지만, 만약 설치되어 있지 않다면 다음 단계를 따릅니다.

1. **`pip` 설치**
   아래 명령어를 터미널이나 명령 프롬프트에 입력하여 pip를 설치합니다.

   ```sh
   python -m ensurepip --upgrade
   ```

2. **설치 확인**
   `pip --version`을 입력하여 `pip`가 정상적으로 설치되었는지 확인합니다.

   ```sh
   pip --version
   ```

이제 파이썬과 `pip`가 모두 설치되었습니다.

파이썬 설치가 완료된 후에는 다양한 파이썬 패키지를 설치하여 활용할 수 있습니다.

### `pip` 활용 예제

1. **패키지 설치**
   ```bash
   # `requests`라는 패키지를 설치합니다.
   pip install requests
   ```

2. **패키지 업그레이드**
   ```bash
   # `requests`라는 패키지를 최신 버전으로 업그레이드합니다.
   pip install --upgrade requests
   ```

3. **패키지 제거**
   ```bash
   # `requests`라는 패키지를 제거합니다.
   pip uninstall requests
   ```

4. **설치된 패키지 목록 확인**
   ```bash
   # 현재 설치된 모든 패키지 목록을 출력합니다.
   pip list
   ```

5. **요구사항 파일에서 설치**
   ```bash
   # `requirements.txt` 파일에 명시된 모든 패키지를 설치합니다.
   pip install -r requirements.txt
   ```
   - `requirements.txt` 파일(예시)

      ```python
      requests==2.24.0
      numpy>=1.18.5
      pandas
      ```

[맨 위로 이동](03_04)

