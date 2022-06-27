import tkinter as tk
import tkinter.messagebox as mb
import tkinter.filedialog as fd

# tkinter 윈도우 숨기기
tk.Tk().withdraw()

# 폴더 선택 대화상자 띄우기 --- (1)
dirpath = fd.askdirectory(
    title='폴더를 지정해주세요',
    initialdir='./')

# 결과 표시
mb.showinfo('선택 폴더', dirpath)
