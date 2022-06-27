import tkinter as tk
import tkinter.messagebox as mb
import tkinter.filedialog as fd

# tkinter 윈도우 숨기기
tk.Tk().withdraw()

# 파일 선택 대화상자 띄우기 --- (1)
filepath = fd.askopenfilename()

# 결과 표시 --- (2)
mb.showinfo('선택 파일', filepath)
