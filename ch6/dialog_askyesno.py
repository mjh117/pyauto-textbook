import tkinter as tk
import tkinter.messagebox as mb

# 윈도우 숨기기 --- (1)
tk.Tk().withdraw()

# 질문 대화상자 표시 --- (2)
yesno = mb.askyesno('질문', '처리를 실행하시겠습니까?')

# 유저의 응답에 따라 동작을 달리한다 --- (3)
if yesno:
    mb.showinfo('예를 선택', '실행 완료')
else:
    mb.showinfo('아니요를 선택', '실행하지 않음')
