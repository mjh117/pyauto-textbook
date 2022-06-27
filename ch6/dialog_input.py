import tkinter as tk
import tkinter.messagebox as mb
import tkinter.simpledialog as sd

# tkinter 창 숨기기
win = tk.Tk().withdraw()

# 문자열 입력 대화상자에서 이름 받기 --- (1)
name = sd.askstring(
    '성명 입력', '성명을 입력해주세요.\n(미입력 시 종료)',
    initialvalue='제이펍')
if name =='' or name ==None: quit()

# 이름을 사용해 인사하기 --- (2)
mb.showinfo('인사', name + '님 안녕하세요.')
