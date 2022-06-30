# 간단히 사용할 수 있는 대화상자를 정리한 모듈
import tkinter as tk
import tkinter.messagebox as mb
import tkinter.filedialog as fd
import tkinter.simpledialog as sd

# tkinter 창 숨기기
tk.Tk().withdraw()

# 정보 대화상자
def info(message, title='정보'):
    mb.showinfo(title, message)

# 경고 대화상자
def warning(message, title='경고'):
    mb.showwarning(title, message)

# 질문 대화상자
def yesno(message, title='질문'):
    return mb.askyesno(title, message)

# 입력 대화상자
def input(message, title='입력', value=''):
    return sd.askstring(
        title, message,
        initialvalue=value)

# 파일 선택 대화상자
def select_file(initdir='./'):
    return fd.askopenfilename(
        initialdir=initdir)

# 파일 저장 대화상자
def select_savefile(initdir='./'):
    return fd.asksaveasfilename(
        initialdir=initdir)

# 폴더 선택 대화상자
def select_dir(initdir='./'):
    return fd.askdirectory(
        initialdir=initdir)
