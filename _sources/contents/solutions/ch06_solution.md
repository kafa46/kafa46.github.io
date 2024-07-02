(ch06-solution)=
**6장 솔루션**

[정답 리스트로 이동](./00_solutions.md)

아래 코드는 메모장 앱에 찾기 기능을 추가한 참고 코드입니다.

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
    file_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("텍스트 파일", "*.txt"), ("모든 파일", "*.*")])
    if file_path:
        with open(file_path, 'w') as file:
            file.write(text_area.get(1.0, tk.END))
        messagebox.showinfo("저장 완료", f"파일이 저장되었습니다: {file_path}")

def find_text():
    find_window = tk.Toplevel(window)
    find_window.title("찾기")

    tk.Label(find_window, text="찾을 내용:").grid(row=0, column=0, padx=5, pady=5)
    find_entry = tk.Entry(find_window, width=30)
    find_entry.grid(row=0, column=1, padx=5, pady=5)

    def find():
        text_area.tag_remove('found', '1.0', tk.END)
        find_word = find_entry.get()
        if find_word:
            start_pos = '1.0'
            while True:
                # 시작 위치부터 문서의 마지막까지 스캔
                # find_word와 동일한 문자열을 찾았다면 찾은 문자열의 첫글자 인덱스를 리턴
                # 찾지 못했다면 빈 문자열 리턴
                start_pos = text_area.search(find_word, start_pos, stopindex=tk.END)
                if not start_pos:
                    break
                # 종료 인덱스 업데이트: 출발 인덱스 + 찾은 문자열의 글자수
                end_pos = f"{start_pos}+{len(find_word)}c"
                # 찾은 문자열의 시작 인덱스와 끝 인덱스에 'found'라고 태그 붙여주기
                text_area.tag_add('found', start_pos, end_pos)
                # 찾은 문자열의 마지막 인덱스를 시작점으로 삼아 다시 탐색 시작
                start_pos = end_pos
            # 'found'라고 태그된 영역의 배경색을 'yellow'로 변경
            text_area.tag_config('found', background='yellow')
    
    tk.Button(find_window, text="찾기", command=find).grid(row=1, column=0, columnspan=2, pady=5)

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

edit_menu = tk.Menu(menu, tearoff=0)
menu.add_cascade(label="편집", menu=edit_menu)
edit_menu.add_command(label="찾기", command=find_text)

# 텍스트 영역 추가
text_area = tk.Text(window, wrap=tk.WORD)
text_area.pack(expand=1, fill=tk.BOTH)

# 상태 표시줄 추가
status = tk.Label(window, text="상태: 대기 중", bd=1, relief=tk.SUNKEN, anchor=tk.W)
status.pack(side=tk.BOTTOM, fill=tk.X)

# 메인 루프 실행
window.mainloop()

```

[맨 위로 이동](ch06-solution)