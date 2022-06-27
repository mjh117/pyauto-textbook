# pywin32(win32com) 라이브러리 가져오기 --- (1)
import win32com.client as com

# 엑셀 실행하기 --- (2)
app = com.Dispatch("Excel.Application")
app.Visible = True
app.DisplayAlerts = False

# 엑셀에 신규 문서 생성 --- (3)
book = app.Workbooks.Add()
# 활성 시트 가져오기 --- (4)
sheet = book.ActiveSheet

# 시트에 값 쓰기 --- (5)
sheet.Range("B2").Value = "안녕하세요"
