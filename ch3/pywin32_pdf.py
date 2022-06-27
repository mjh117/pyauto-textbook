import win32com.client as com
import os

# 절대 경로 형식으로 파일명 지정 --- (1)
src_file = os.path.abspath(__file__)
src_dir = os.path.dirname(src_file)
in_file = os.path.join(src_dir,'input', 'stock-data.xlsx')
pdf_file = os.path.join(src_dir, 'output', 'pywin32_pdf.pdf')

# 엑셀 실행하기 --- (2)
app = com.Dispatch("Excel.Application")
app.Visible = True
app.DisplayAlerts = False

# 엑셀에서 기존 문서 열기 --- (3)
book = app.Workbooks.Open(in_file)

# 문서를 PDF로 내보내기 --- (4)
xlTypePDF = 0 # PDF를 나타내는 상수
book.ExportAsFixedFormat(xlTypePDF, pdf_file)

# 엑셀을 종료 --- (5)
app.Quit()
