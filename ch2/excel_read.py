import openpyxl as excel

# 워크북(엑셀 파일) 열기 --- (1)
book = excel.load_workbook("./output/hello.xlsx")

# 워크북에서 첫 번째 워크시트 가져오기 --- (2)
sheet = book.worksheets[0]

# 시트에서 A1 셀 가져오기 --- (3)
cell = sheet["A1"]

# A1 셀의 데이터를 화면에 출력 --- (4)
print(cell.value)
