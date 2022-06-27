import openpyxl as excel

# 새 워크북 생성 --- (1)
book = excel.Workbook()
#  활성화된 워크시트 가져오기--- (2)
sheet = book.active

#  A열에 연속 데이터 채우기  --- (3)
for i in range(10):
    # A열 i+1행에 데이터 쓰기  --- (4)
    sheet.cell(row=(i+1), column=1, value=i)

# 파일 저장 --- (5)
book.save("output/write_column.xlsx")
