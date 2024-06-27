(06-05)=
# 메모장 애플리케이션 만들기

지금까지 배운 내용을 바탕으로 메모장(Notepad) 앱을 만들어 보겠습니다.

메모장에는 텍스트를 입력할 수 있는 `tk.Text` 객체를 추가하는 작업이 필요합니다. 나머지 코드는 이전에 공부한 내용과 동일합니다.

계산기 애플리케이션이 실행되면 아래 그림과 같이 만드는 것이 목표입니다.

```{figure} ../imgs/chap_06/ch06_05_01_notepad_app.png
---
width: 80%
name: ch06_05_01_notepad_app
---
새파일, 저장, 불러오기 기능이 가능한 메모장 앱
```

다음 코드를 참고하여 메모장을 프로그램을 완성해 보세요.

```python
import tkinter as tk
from tkinter import filedialog, messagebox

def new_file():
    text_area.delete(1.0, tk.END)

def open_file():
    file_path = filedialog.askopenfilename()
    if file_path:
        with open(file_path, 'r') as file:
            text_area.delete(1.0, tk.END)
            text_area.insert(tk.END, file.read())

def save_file():
    file_path = filedialog.asksaveasfilename(
        defaultextension=".txt", 
        filetypes=[("텍스트 파일", "*.txt"), ("모든 파일", "*.*")]
    )
    if file_path:
        with open(file_path, 'w') as file:
            file.write(text_area.get(1.0, tk.END))
        messagebox.showinfo("저장 완료", f"파일이 저장되었습니다: {file_path}")

# 메인 윈도우 생성
window = tk.Tk()
window.title("메모장")

# 메뉴 추가
menu = tk.Menu(window)
window.config(menu=menu)

file_menu = tk.Menu(menu, tearoff=0)
menu.add_cascade(label="파일", menu=file_menu)
file_menu.add_command(label="새 파일", command=new_file)
file_menu.add_command(label="열기", command=open_file)
file_menu.add_command(label="저장", command=save_file)
file_menu.add_separator()
file_menu.add_command(label="종료", command=window.quit)

# 텍스트 영역 추가
text_area = tk.Text(window, wrap=tk.WORD)
text_area.pack(expand=1, fill=tk.BOTH)

# 상태 표시줄 추가
status = tk.Label(window, text="상태: 대기 중", bd=1, relief=tk.SUNKEN, anchor=tk.W)
status.pack(side=tk.BOTTOM, fill=tk.X)

# 메인 루프 실행
window.mainloop()
```

[맨 위로 이동]((06-05))