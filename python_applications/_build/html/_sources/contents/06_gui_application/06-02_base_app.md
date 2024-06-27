(06-02)=
# 기본 GUI 애플리케이션


## 윈도우 생성 및 텍스트 입력(`Label`) 객체 추가

Tkinter 라이브러리를 사용하여 기본 윈도우를 만들고, "Hello, World!" 텍스트가 표시된 레이블을 추가한 후, 메인 이벤트 루프를 실행하여 윈도우를 표시해 봅니다.

```python
import tkinter as tk

# 메인 윈도우 생성
window = tk.Tk()
window.title("Tkinter 기본 앱")
window.geometry('500x300+200+200')

# 레이블 추가
label = tk.Label(root, text="Hello, World!")
label.pack()

# 메인 루프 실행
window.mainloop()
```

**실행 결과**

```{figure} ../imgs/chap_06/ch06_02_01_base.png
---
width: 70%
name: ch06_02_01_base_01
---
텍스트 입력(`Label`) 객체 추가하여 실행한 결과
```

## 텍스트 입력(`Entry`) 객체 추가

Tkinter로 간단한 앱을 만들고 다양한 위젯을 추가하는 예제입니다. 

기존 앱에 텍스트 입력 객체를 추가하고 `pack()` 메서드를 이용하여 `Label` 객체 아래에 추가하고 패딩을 설정해 줍니다.

```python
import tkinter as tk

# 메인 윈도우 생성
window = tk.Tk()
window.title("Tkinter 기본 앱")
window.geometry('500x300+200+200')

# 레이블 추가 및 위치 지정
label = tk.Label(window, text="Hello, Tkinter!")
label.pack(padx=10, pady=10)  # pack() 메서드 사용, 패딩 추가

# 텍스트 입력 필드 추가
entry = tk.Entry(window)
entry.pack(padx=10, pady=10) # pack() 메서드 사용, 패딩 추가

# 메인 루프 실행
window.mainloop()
```

```{figure} ../imgs/chap_06/ch06_02_02_add_label.png
---
width: 70%
name: ch06_02_02_add_label
---
텍스트 입력(`Entry`) 객체를 추가하여 실행한 결과
```

## 클릭 버튼(`Button`) 및 체크박스(`BooleanVar`)객체 추가

기존 앱에 버튼을 축하고 패딩을 줍니다.

```python
import tkinter as tk

# 메인 윈도우 생성
window = tk.Tk()
window.title("Tkinter 기본 앱")
window.geometry('500x300+200+200')

# 레이블 추가 및 위치 지정
label = tk.Label(window, text="Hello, Tkinter!")
label.pack(padx=10, pady=10)  # pack() 메서드 사용, 패딩 추가

# 텍스트 입력 필드 추가
entry = tk.Entry(window)
entry.pack(padx=10, pady=10) # pack() 메서드 사용, 패딩 추가

# 버튼이 클릭되었을 때 수행할 작업 정의
def on_button_click():
    '''모니터에 입력 내용을 간단히 출력하여 작동 여부 확인'''
    print(f"버튼이 클릭되었습니다! 입력 내용:{entry.get()}")

# 버튼 추가
button = tk.Button(window, text="Click Me!", command=on_button_click)
button.pack(padx=10, pady=10) # pack() 메서드 사용, 패딩 추가 

# 체크박스 추가
checkbox_var = tk.BooleanVar()
checkbox = tk.Checkbutton(window, text="Check me", variable=checkbox_var)
checkbox.pack(padx=10, pady=10) # pack() 메서드 사용, 패딩 추가

# 메인 루프 실행
window.mainloop()
```

**실행 결과**

텍스트 입력란(`Entry` 객체)에 글자를 입력합니다.

버튼(`Button` 객체)를 클릭했을 때, 모니터(콘솔)에 내용이 출력되는지 확인합니다.

```{figure} ../imgs/chap_06/ch06_02_03_add_btn_checkbox.png
---
width: 70%
name: ch06_02_03_add_btn_checkbox
---
버튼, 체크박스 객체 추가하여 실행한 결과
```