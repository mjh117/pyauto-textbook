import tkinter as tk
import tkinter.messagebox as mb
import tkinter.filedialog as fd

# tkinter 윈도우 숨기기
tk.Tk().withdraw()

# 초기 폴더 및 확장자 지정 --- (1)
filepath = fd.askopenfilename(
    filetypes=[('Python 파일','*.py')],
    initialdir='./')

# 결과 표시
mb.showinfo('선택 파일', filepath)
