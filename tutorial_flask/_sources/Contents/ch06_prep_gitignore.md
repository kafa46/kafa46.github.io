# 준비 4. `.gitignore` 세팅

내 컴퓨터에서 작업한 것들을 협업 또는 백업을 위해 원격 저장소에 업로드해야 하는 경우가 항상 발생합니다.
이 경우 사용하는 것이 `git` 이라는 도구입니다.
본 책자는 `git`에 대한 튜토리얼이 아니므로 `git`에 대한 세부적인 설명은 생략합니다.
`git`에 대해 좀 더 공부하고자 하는 여러분은 `git` 튜토리얼이 블로그, 유튜브 강의, 전문서적 구매 등을 통하여 학습할 것을 추천합니다.

`.gitignore`는 `git`을 이용하여 내 컴퓨터에서 작업한 소스코드를 원격 저장소(repository)로 업로드 할 때
불필요한 파일까지 업로드 되는 것을 방지하기 위해 작성하는 텍스트 파일입니다.
예를 들면 VS Code 설정파일(`.vscode`)은 내 컴퓨터에서는 필요하지만, 원격저장소에 올릴 필요는 없습니다.
Jupyter Notebook에 필요한 `.ipynb_checkpoint` 폴더, 백업 파일(`.bak`), 데이터베이스 파일(`.db`), 개인 정보나 비밀번호 등이
담긴 파일(`*.secret`) 등은 원격 저장소에 올리면 안됩니다.

작업 디렉토리에 `.gitignore`라는 빈 파일 하나를 만들고 그 안에 내가 원격저장소로 업로드 할때
자동으로 딸려 올라가지 않도록 할 파일들을 쭉 적어주면 됩니다.
`.gitignore` 파일 작성법은 [참고 블로그](https://programming119.tistory.com/105)를 방문해서 관련 내용을 참고하기 바랍니다.

## 유용한 사이트 `gitignore.io`

자주 사용하는 운영체제, 개발환경(IDE), 프로그래밍 언어에 대한  `.gitignore` 내용을 자동을 작성해 주는 유용한 사이트가 있습니다.
해당 사이트는 [`gitignore.io`](https://www.toptal.com/developers/gitignore) 입니다.
[`gitignore.io`](https://www.toptal.com/developers/gitignore)에서 `python, flask, linux, windows, macOS, VisualStudioCode`와 관련된
`gitignore` 내용을 생성해 보겠습니다.

```{figure} ../imgs/gitignore.io_screen.jpg
---
width: 650
align: left
alt: gitignore.io screen
name: gitignore_screen
---
gitignore.io를 이용해서 `.gitignore` 내용을 자동으로 생성하기
```

gitignore.io에서 `생성` 아이콘을 클릭하면 아래와 같이 자동으로 원격 저장소 업로드 시 제외할 파일/디렉토리 목록을 생성해 줍니다.

```{note}
gitignore.io에서 모든 것을 해결해 주지는 않습니다. 
자주 사용하는 것들만 모아서 생성해 주기 때문에 
개인적으로 제외할 파일을 별도로 지정해 주어야 합니다.
```

```text
# Created by https://www.toptal.com/developers/gitignore/api/python,flask,linux,windows,macos,visualstudiocode
# Edit at https://www.toptal.com/developers/gitignore?templates=python,flask,linux,windows,macos,visualstudiocode

### Flask ###
instance/*
!instance/.gitignore
.webassets-cache
.env

### Flask.Python Stack ###
# Byte-compiled / optimized / DLL files
__pycache__/
*.py[cod]
*$py.class

# C extensions
*.so

# Distribution / packaging
.Python
build/
develop-eggs/
dist/
downloads/
eggs/
.eggs/
lib/
lib64/
parts/
sdist/
var/
wheels/
share/python-wheels/
*.egg-info/
.installed.cfg
*.egg
MANIFEST
:
:
```

VS Code에서 `.gitingnore` 파일을 만들고 위에서 생성한 목록을 복사하여 붙여넣기 합니다.
다음 그림을 참고하세요.

```{figure} ../imgs/vscode_07_gitignore_file_create.png
---
width: 700
align: left
alt: vscode .gitingnore file create
name: gitingnore_file_create
---
VS Code에서 `.gitignore` 파일 만들기
```

## `.gitignore` 추가 설정

`flask`를 사용하려면 데이터베이스가 필요합니다.
나중에 `sqlite`라는 데이터베이스를 사용할 예정입니다.
`.gitignore` 파일의 맨 마지막에 아래 내용을 추가로 복사하여 붙여넣기 한 다음 파일을 저장합니다.

```python
# sqlite
*.db
```

```{admonition} 파일 이름에서 . 과  * 의미
파일이름에서 파일 이름이 없고 `점(.)` 다음에 확장자 이름 형태로 되어 있는 것은 
대부분  설정(configuration) 파일(또는 디렉토리)을 의미합니다. 
- `.gitignore` $\to$ `gitignore` 설정파일
- `.bash` $\to$ `bash` 설정파일
- `.vscode` $\to$ `VS Code` 설정 파일

파일 이름에 와일드 문자 `*`가 있다면 
`모든(all)`을 의미합니다.
- `*.txt`  $\to$ `.txt`를 확장자로 갖는 모든 파일
- `.gitignore` 파일 안에 `*.txt`가 기록되어 있다면, 
`.txt`를 확장자로 갖는 모든 파일을 원격 저장소 업로드 시 제외하겠다는 의미입니다.

```
