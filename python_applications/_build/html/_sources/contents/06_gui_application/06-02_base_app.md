(06-02)=
# 기본 GUI 애플리케이션


## 윈도우 생성 및 텍스트 추가

Tkinter 라이브러리를 사용하여 기본 윈도우를 만들고, "Hello, World!" 텍스트가 표시된 레이블을 추가한 후, 메인 이벤트 루프를 실행하여 윈도우를 표시해 봅니다.

```python
import tkinter as tk

# 메인 윈도우 생성
root = tk.Tk()
root.title("Hello Tkinter")

# 레이블 추가
label = tk.Label(root, text="Hello, World!")
label.pack()

# 메인 루프 실행
root.mainloop()
```

**실행 결과**

```{figure} ../imgs/chap_06/ch06_02_01_base.png
---
width: 40%
name: ch06_02_01_base_01
---
레이블, 버튼, 텍스트 입력 필드, 체크박스 포함하는 앱
```

## 버튼, 체크박스 추가

Tkinter로 간단한 앱을 만들고 다양한 위젯을 추가하는 예제입니다. 이 앱은 레이블, 버튼, 텍스트 입력 필드, 체크박스를 포함합니다.

```{figure} ../imgs/chap_06/ch06_02_02_add_widgets.png
---
width: 40%
name: ch06_02_02_add_widgets
---
Hello, world 실행 결과
```