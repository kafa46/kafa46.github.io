(06-04)=
# 고급 기능 맛보기

Tkinter는 애플리케이션에 메뉴 추가하는 기능을 지원합니다. 메뉴를 추가하기 위해서는 `Memu` 객체를 사용합니다.

`tk.Menu.add_command()` 메서드를 이용하여 다양한 메뉴를 추가할 수 있습니다. 추가된 메뉴에는 별도의 함수를 만들어서 등록할 수 있습니다.

`tkinter.messagebox.showinfo()` 메서드를 이용하면 메시지 박스를 띄울 수 있습니다.

`tkinter.filedialog` 모듈을 이용하면 파일을 불러오거나 저장하는 기능을 구현할 수 있습니다.

계산기 애플리케이션이 실행되면 아래 그림과 같이 만드는 것이 목표입니다.

```{figure} ../imgs/chap_06/ch06_04_01_advanced_func.png
---
width: 80%
name: ch06_04_01_advanced_func
---
메뉴, 상태 표시줄이 적용된 계산기 애플리케이션 UI
```

다음 예제를 통해 실습해 보겠습니다.

```python
import tkinter as tk
from tkinter import messagebox, filedialog

# 버튼 클릭 시 메시지 박스 표시 함수
def show_message():
    messagebox.showinfo("메시지", "버튼이 클릭되었습니다!")

# 파일 열기 함수
def open_file():
    filepath = filedialog.askopenfilename()
    if filepath:
        messagebox.showinfo("파일 선택", f"선택한 파일: {filepath}")

# 파일 저장 함수
def save_file():
    filepath = filedialog.asksaveasfilename(
        defaultextension=".txt", 
        filetypes=[("텍스트 파일", "*.txt"), ("모든 파일", "*.*")]
    )
    if filepath:
        with open(filepath, 'w') as f:
            f.write("이 파일은 Tkinter로 저장되었습니다.")
        messagebox.showinfo("파일 저장", f"파일이 저장되었습니다: {filepath}")

# 메인 윈도우 생성
window = tk.Tk()
window.title("Tkinter 고급 기능")
window.geometry('500x300+200+200')

# 메뉴 객체 생성
menu = tk.Menu(window)

# 윈도우에 생성된 메뉴 등록
window.config(menu=menu)

# 파일 관련 메뉴 목록과 함수 등록
file_menu = tk.Menu(menu, tearoff=0)
menu.add_cascade(label="파일", menu=file_menu)
file_menu.add_command(label="열기", command=open_file)
file_menu.add_command(label="저장", command=save_file)
file_menu.add_separator()
file_menu.add_command(label="종료", command=window.quit)

# 도움말 관련 메뉴 등록과 함수 등록
help_menu = tk.Menu(menu, tearoff=0)
menu.add_cascade(label="도움말", menu=help_menu)
help_menu.add_command(label="정보", command=lambda: messagebox.showinfo("정보", "Tkinter 고급 기능 예제"))

# 상태 표시줄 추가
status = tk.Label(
    window, # 상태 표시줄을 
    text="상태: 대기 중", 
    bd=1, # 경계선 굵기
    relief=tk.SUNKEN,  # 상태 표시줄 표시 방법, 
    # SUNKEN: 움푹 들어간 형태, 
    # FLAT: 다른 객체와 동일, 
    # RAISED: 돌출된 모양, 
    # GROOVE: 테두리 모양으로 구분
    anchor=tk.W # west(왼쪽) 정렬
)
status.pack(
    side=tk.BOTTOM, # 객체 위치 
    # BOTTOM: 바닥에 배치, 
    # TOP: 상단 배치, 
    # LEFT: 왼쪽 배치, 
    # RIGHT: 오른쪽 배치
    fill=tk.X, # fill: 사용되지 않는 공간으로 늘이기
    # X: X축으로 가득 채우기(수평으로만 늘이기)
    # Y: Y축으로 가득 채우기(수직으로만 늘이기)
    # BOTH: 가능한 모든 공간으로 늘이기
    # NONE: 늘이지 않기 (원래 크기 유지)
)

# 버튼 추가
button = tk.Button(window, text="메시지 표시", command=show_message)
button.pack(padx=10, pady=10)

# 메인 루프 실행
window.mainloop()
```

[맨 위로 이동](06-04)