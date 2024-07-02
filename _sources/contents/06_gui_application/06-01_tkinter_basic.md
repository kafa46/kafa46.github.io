(06-01)=
# Tkinter 기초

Tkinter는 Python의 표준 GUI 라이브러리로, 간단한 그래픽 사용자 인터페이스 애플리케이션을 개발하는 데 사용됩니다. Tkinter는 Python에 기본적으로 포함되어 있어 별도의 설치가 필요 없으며, 사용하기 쉽고 배우기 간편합니다.

Tkinter는 학습 곡선이 낮아 Python으로 GUI 프로그래밍을 시작하려는 초보자에게 적합합니다.
우리도 Tkinter를 이용해 학습을 진행할 것입니다.

## 설치

Tkinter는 Python 표준 라이브러이므로 별도의 설치가 필요 없습니다.

## 주요 특징
- 간편한 사용: Python 표준 라이브러리로 제공되며, 추가 설치 없이 바로 사용 가능.
- 직관적인 인터페이스: 간단한 코드로 GUI 요소를 만들 수 있음.
- 경량성: 복잡하지 않은 애플리케이션에 적합.

## 구성요소

**Tkinter Windows**

애플리케이션을 표현할 윈도우 창을 의미합니다.

tkinter.Tk 클래스의 객체를 생성하면 하나의 윈도우 객체가 생성됩니다.

```python
import tkinter as tk

# 윈도우 객체 생성
window = tk.Tk()

# 메인 루프 실행
window.mainloop()
```

**실행 결과**

```{figure} ../imgs/chap_06/ch06_01_01_tk_window_01.png
---
width: 20%
name: ch06_01_01_tk_window_01.png
---
단순히 윈도우만 생성한 경우
```

윈도우 객체는 다양한 메서드를 사용할 수 있습니다.
- `title()`: 윈도우 창 이름(제목)
- `geometry(str)`: 메서드를 사용하여 생성될 때 크기를 지정("가로x세로+x좌표+y좌표")
- `resiable(bool, bool)`: 사용자의 창 크기 변경 허용 여부(가로, 세로)

- 윈도우 이름, 시작할 때 크기를 지정한 경우
  ```python
    import tkinter as tk

    # 윈도우 객체 생성
    window = tk.Tk()

    window.title("cju test")

    # 윈도우 크기 지정 -> 가로 800 픽셀, 세로: 500 픽셀
    # 윈도우 위치 지정 -> x 위치: 200 픽셀, y 위치: 300 픽셀
    window.geometry('800x500+200+300')

    # 메인 루프 실행
    window.mainloop()
  ```

**실행 결과**
```{figure} ../imgs/chap_06/ch06_01_01_tk_window_02.png
---
width: 40%
name: ch06_01_01_tk_window_02.png
---
윈도우의 제목, 크기, 위치를 설정한 경우
```


**Tkinter Widgets**

Tkinter 위젯은 모든 Tkinter 기반 GUI 애플리케이션의 기능 단위입니다.

Python에서 Tkinter 모듈을 사용할 때 첫 번째 단계는 Window 객체를 만드는 것입니다.

Window 객체를 만든 후에는 Tkinter 위젯(widgets)을 창에 추가할 수 있습니다.

사용자 인터페이스를 만드는 데 직접 사용할 수 있는 다양한 준비된 Tkinter 위젯이 있습니다.

```{figure} ../imgs/chap_06/ch06_01_02_tk_widgets.jpg
---
width: 100%
name: ch06_01_02_tk_widgets
---
Tkinter 주요 위젯 (출처: [Studytonight](https://www.studytonight.com/tkinter/python-tkinter-widgets))
```

Python Tkinter 모듈에서 사용할 수 있는 19개의 위젯이 있습니다.

다음 표에는 기본 설명과 함께 모든 위젯이 나열되어 있습니다.

| Widget | Description |
|--------|-------------|
| [Button](http://studytonight.com/tkinter/python-tkinter-button-widget) | 클릭 가능한 버튼으로, 사용자가 클릭하여 동작을 수행 |
| [Canvas](http://studytonight.com/tkinter/python-tkinter-canvas-widget) | 그래픽, 텍스트 등 복잡한 레이아웃을 그리기 위한 위젯 |
| [CheckButton](http://studytonight.com/tkinter/python-tkinter-checkbutton-widget) | 체크박스로 여러 옵션을 표시하며, 여러 개 선택 가능 |
| [Entry](http://studytonight.com/tkinter/python-tkinter-entry-widget) | 사용자 입력을 받는 단일 행 텍스트 필드 |
| [Frame](http://studytonight.com/tkinter/python-tkinter-frame-widget) | 다른 위젯들을 그룹화하고 조직하는 컨테이너|
| [Label](http://studytonight.com/tkinter/python-tkinter-label-widget) | 다른 위젯에 단일 행 캡션을 제공, 이미지를 포함할 수 있음|
| [Listbox](http://studytonight.com/tkinter/python-tkinter-listbox-widget) | 사용자에게 여러 옵션을 제공하는 리스트 박스|
| [Menu](http://studytonight.com/tkinter/python-tkinter-menu-widget) | 사용자에게 다양한 명령을 제공하는 메뉴 위젯|
| [Menubutton](http://studytonight.com/tkinter/python-tkinter-menubutton-widget) | 사용자가 메뉴 항목을 볼 수 있도록 하는 메뉴 버튼 위젯|
| [Message](http://studytonight.com/tkinter/python-tkinter-message-widget)  | 사용자에게 메시지 박스를 표시하는 위젯으로, 기본적으로 편집할 수 없는 다중 행 텍스트|
| [Radiobutton](http://studytonight.com/tkinter/python-tkinter-radiobutton-widget) | 여러 옵션을 라디오 버튼으로 표시하며, 한 번에 하나만 선택 가능|
| [Scale](http://studytonight.com/tkinter/python-tkinter-scale-widget) | 그래픽 슬라이더로, 눈금에서 값을 선택할 수 있음|
| [Scrollbar](http://studytonight.com/tkinter/python-tkinter-scrollbar-widget) | 창을 위아래로 스크롤할 수 있는 스크롤바|
| [Text](http://studytonight.com/tkinter/python-tkinter-text-widget) | 사용자가 텍스트를 입력하거나 편집할 수 있는 다중 행 텍스트 필드|
| [Toplevel](http://studytonight.com/tkinter/python-tkinter-toplevel-widget) | 별도의 창 컨테이너를 제공하는 위젯|
| [SpinBox](http://studytonight.com/tkinter/python-tkinter-spinbox-widget)  | 고정된 숫자 값 세트를 선택하여 값을 입력할 수 있는 위젯|
| [PanedWindow](http://studytonight.com/tkinter/python-tkinter-panedwindow-widget) | 여러 창틀을 처리하기 위한 컨테이너 위젯으로, 창틀은 수평 또는 수직으로 배열 가능|
| [LabelFrame](http://studytonight.com/tkinter/python-tkinter-labelframe-widget) | 복잡한 위젯을 처리하기 위한 컨테이너 위젯으로, 레이블과 테두리를 포함|
| [MessageBox](http://studytonight.com/tkinter/python-tkinter-messagebox) | 데스크탑 애플리케이션에서 메시지를 표시하는 위젯|

출처: [Studytonight](https://www.studytonight.com/tkinter/python-tkinter-widgets)

## Tkinter로 만들 수 있는 것들

Tkinter는 파이썬을 이용해 간단한 GUI 애플리케이션을 제작하기 위한 라이브러이이므로 복잡하거나 화려한 GUI 프로그램을 구현하기는 어렵습니다. 그러나 기능 위주의 간단한 애플리케이션은 얼마든지 만들 수 있습니다.

Tkinter로 구현할 수 있는 간단한 애플리케이션은 다음과 같습니다.

```{figure} ../imgs/chap_06/ch06_01_03_tk_apps.webp
---
width: 80%
name: ch06_01_03_tk_apps
---
Tkinter로 만들 수 있는 간단한 애플리케이션
```


| 애플리케이션         | 설명                                                                 |
|----------------------|----------------------------------------------------------------------|
| 계산기               | 기본적인 산술 연산을 수행할 수 있는 간단한 계산기 애플리케이션        |
| 텍스트 에디터        | 메모장과 유사한 텍스트 편집 기능을 제공하는 애플리케이션             |
| 할 일 목록 관리 앱   | 사용자들이 할 일을 추가, 삭제 및 정리할 수 있는 애플리케이션         |
| 이미지 뷰어          | 사용자가 이미지를 탐색하고 볼 수 있는 간단한 이미지 뷰어             |
| 파일 탐색기          | 파일 및 폴더를 탐색하고 관리할 수 있는 애플리케이션                  |


## Geometry Manager

Tkinter는 부모 윈도우 내에서 모든 위젯을 조직, 배열 및 배치하기 위한 기하학적 구성을 제공합니다. GUI 애플리케이션 레이아웃은 주로 Tkinter의 `Geometric Managers`에 의해 제어됩니다.

각 윈도우와 프레임은 하나의 기하학적 관리자를 사용할 수 있습니다. 또한, 서로 다른 프레임은 다른 기하학적 관리자를 사용할 수 있습니다.

기하학적 관리자의 주요 방법은 다음 세 가지입니다:

- `pack()`: 윈도우, 프레임 내에서 위젯의 순서를 할당
- `grid()`: 격자를 생성하여 위젯을 순서대로 할당
- `place()`: 프로그래머가 위젯 위치를 명시적으로 지정

### `pack()` 매니저

**`pack()` 옵션 없이 3개 위젯을 쌓는 예제**

```python
import tkinter as tk

win = tk.Tk()
win.title('cju python')
window.geometry('800x500+200+300')

# add an orange frame
frame1 = tk.Frame(master=win, width=100, height=100, bg="orange")
frame1.pack()

# add blue frame
frame2 = tk.Frame(master=win, width=50, height=50, bg="blue")
frame2.pack()

# add green frame
frame3 = tk.Frame(master=win, width=25, height=25, bg="green")
frame3.pack()

window.mainloop()
```

**실행 결과**

```{figure} ../imgs/chap_06/ch06_01_04_pack_wo_params.png
---
width: 30%
name: ch06_01_04_pack_wo_params
---
파라미터 설정 없이 pack( ) 실행한 결과
```

**`pack()` 옵션을 사용하여 3개 위젯을 쌓는 예제**

```python
import tkinter as tk

win= tk.Tk()

frame1 = tk.Frame(master=win, height=80, bg="red")
# adding the fill argument with
# horizontal fill value
frame1.pack(fill=tk.X)

frame2 = tk.Frame(master=win, height=50, bg="yellow")
frame2.pack(fill=tk.X)

frame3 = tk.Frame(master=win, height=40, bg="blue")
frame3.pack(fill=tk.X)

win.mainloop()
```

**실행 결과**

```{figure} ../imgs/chap_06/ch06_01_05_pack_w_params.png
---
width: 30%
name: ch06_01_05_pack_w_params
---
파라미터 사용하여 pack( ) 실행한 결과
```

### `grid()` 매니저

**`5 × 3` grid 프레임을 만드는 예제**

```python
import tkinter as tk

win = tk.Tk()
win.title('cju python')

for i in range(5):
    for j in range(3):
        frame = tk.Frame(
            master = win,
            relief = tk.RAISED,
            borderwidth = 1
        )
        frame.grid(row=i, column=j)
        label = tk.Label(master=frame, text=f"Row {i}\nColumn {j}")
        label.pack()

win.mainloop()
```

**실행 결과**

```{figure} ../imgs/chap_06/ch06_01_06_grid_wo_params.png
---
width: 30%
name: ch06_01_06_grid_wo_params
---
파라미터 사용하지 않고 grid 생성
```

**패딩(`padx`, `pady`) 파라미터를 사용하여 `5 × 3` grid 프레임을 만드는 예제**

```python
import tkinter as tk

win = tk.Tk()

for i in range(5):
    for j in range(3):
        frame = tk.Frame(
            master=win,
            relief=tk.RAISED,
            borderwidth=1
        )
        frame.grid(row=i, column=j, padx=5, pady=5)
        label = tk.Label(master=frame, text=f"Row {i}\nColumn {j}")
        label.pack()

win.mainloop()
```

**실행 결과**

```{figure} ../imgs/chap_06/ch06_01_07_grid_w_params.png
---
width: 30%
name: ch06_01_07_grid_w_params
---
파라미터 사용하지 않고 grid 생성
```

### `place()` 매니저

```python
from tkinter import *

# 윈도우 객체 생성 및 크기 지정
top = Tk()
top.geometry("400x250")

# Label (글자) 객체 생성
Username = Label(top, text = "Username").place(x = 30,y = 50)
email = Label(top, text = "Email").place(x = 30, y = 90)
password = Label(top, text = "Password").place(x = 30, y = 130)

# Entry (입력) 객체를 생성하고 위치를 직접 지정
e1 = Entry(top).place(x = 80, y = 50)
e2 = Entry(top).place(x = 80, y = 90)
e3 = Entry(top).place(x = 95, y = 130)

# 메인 루푸 실행
top.mainloop()
```

**실행 결과**

```{figure} ../imgs/chap_06/ch06_01_08_place.png
---
width: 50%
name: ch06_01_08_place
---
파라미터 사용하지 않고 grid 생성
```

[맨 위로 이동](06-01)