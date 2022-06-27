# pywin32(win32com) 라이브러리 불러오기
import win32com.client as com
import os

# 절대 경로 형식으로 파일명 지정 --- (1)
src_file = os.path.abspath(__file__)
src_dir = os.path.dirname(src_file)
save_file = os.path.join(src_dir,'output','pywin32_save.xlsx')

# 엑셀 실행하기  --- (2)
app = com.Dispatch("Excel.Application")
app.Visible = True
app.DisplayAlerts = False

# 엑셀에 신규 문서 생성 --- (3)
book = app.Workbooks.Add()
# 활성 시트 가져오기
sheet = book.ActiveSheet

# 시트에 값 쓰기 --- (4)
sheet.Range("A1").Value = "배우고 시시때때로 익히면 또한 기쁘지 아니한가"
sheet.Range("B2").Value = "벗이 먼 곳에서 찾아오면 또한 즐겁지 아니한가"
sheet.Range("C3").Value = "남이 알아주지 않아도 성내지 않으면 이 또한 군자가 아닌가"

# 파일 저장 --- (5)
book.SaveAs(save_file)
# 엑셀 종료 --- (6)
app.Quit()
