import openpyxl as xl

book = xl.Workbook()
sheet = book.active

# 숫자 데이터 설정 --- (1)
cell = sheet["A1"]
cell.value = 345
sheet["B1"] = "data_type=" + cell.data_type

# 문자열 데이터 설정 --- (2)
cell = sheet["A2"]
cell.value = "abc"
sheet["B2"] = "data_type=" + cell.data_type

# 날짜 데이터 설정 --- (3)
cell = sheet["A3"]
from datetime import date
cell.value = date(2021, 4, 1)
sheet["B3"] = "data_type=" + cell.data_type

# 파일 저장
book.save("output/cellformat_datatype.xlsx")
