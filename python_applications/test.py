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
